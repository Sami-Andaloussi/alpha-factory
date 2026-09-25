"""The registry on its own: what counts as a line, what gate 4 counts, and how lines lost or dropped
are put back, in throwaway repositories."""
import hashlib
import json
import subprocess

import pandas as pd
import pytest

from lab import registry
from lab.battery import Gate, Trial, Verdict


def git(*args, cwd):
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def commit(root, message, *paths):
    git("add", *paths, cwd=root)
    git("commit", "-q", "-m", message, cwd=root)


def repository(root):
    git("init", "-q", cwd=root)
    git("config", "user.name", "lab", cwd=root)
    git("config", "user.email", "lab@example.invalid", cwd=root)
    path = root / "registry" / "trials.jsonl"
    path.parent.mkdir()
    return path


def line(card, variant=0, sharpe=0.1, **more):
    """A registry line as the registry writes it."""
    return registry.compact({"time": "2026-01-01T00:00:00Z", "card": card, "card_hash": card * 8, "variant": variant,
                             "sharpe": sharpe, "monthly": {"2020-01": 0.01, "2020-02": -0.02} if sharpe is not None else {},
                             "gates": {}, "failed": 2, "survivor": False, **more})


def verdict(card, sharpes=(0.3, -0.1)):
    months = pd.date_range("2020-01-31", periods=24, freq="ME")
    trials = [Trial(f"{card}/{k}", pd.Series(0.01 * (k + 1), index=months), s, False) for k, s in enumerate(sharpes)]
    return Verdict(card, [Gate(1, "timing", True, "ok", {}), Gate(2, "edge", False, "no", {})], trials, {})


def test_a_line_that_is_not_a_registry_line_is_refused_by_its_number(tmp_path):
    path = repository(tmp_path)
    path.write_text(line("a") + "\n<<<<<<< HEAD\n" + line("b") + "\n")
    with pytest.raises(RuntimeError, match=r"trials.jsonl, line 2, is not a registry line: a merge .* keeps both sides"):
        registry.lines(path)
    for text in ("[1, 2]", '{"card": "x"}', "not json", '{"card_hash": "0000"}', line("a", variant="0"),
                 line("a", survivor=1), line("a", sharpe=True), line("a")[:-1] + ',"monthly":null}',
                 line("a", failed="2"), line("a", monthly={"2020-13": 0.01}), line("a", monthly={"2020-01": "a"}),
                 line("a", monthly={"2020-1": 0.01}), line("a", monthly={"2020-01": True}),
                 line("a", monthly={"0000-01": 0.01}),
                 line("a", monthly={"2020-0\u00b2": 0.01}), line("a", monthly={"2020-00": 0.01}),
                 line("a", monthly={"20a0-01": 0.01}), line("a", monthly={"2020x01": 0.01}),
                 line("a", monthly={"2020-12": 0.01, "2020-1\u0662": 0.02}),          # one month twice
                 line("a", monthly={"2020/01": 0.01}), line("a", monthly={"\u0662\u0660\u0662\u0660-01": 0.01}),
                 line("a", monthly={"2020-1\u0662": 0.01}),                    # which pandas reads, as no line is written
                 line("a", monthly={"2020-01": 10 ** 400}), line("a", sharpe=10 ** 400),
                 line("a", sharpe=float("inf")), line("a", sharpe=float("-inf")), line("a", sharpe=1e200),
                 line("a", monthly={"2020-01": float("inf")}), line("a", monthly={"2020-01": 2e6})):
        assert registry.entry(text) is None, text                     # every field the lab reads, of its type
    required = ("time", "card", "card_hash", "variant", "sharpe", "monthly", "failed", "survivor")
    assert tuple(registry.FIELDS) == required
    for name in required:                                              # and none left out
        assert registry.entry(json.dumps({k: v for k, v in json.loads(line("a")).items() if k != name})) is None, name
    assert registry.entry(line("a"))["card_hash"] == "a" * 8
    assert registry.entry(line("a", sharpe=float("nan"))) is not None    # gate 4 counts its trial, not its variance
    assert registry.entry(line("a", monthly={"2020-01": 0.01, "2020-12": -1}))["monthly"]["2020-12"] == -1


def test_a_committed_line_that_is_not_a_registry_line_is_no_drop_once_removed(tmp_path):
    path = repository(tmp_path)
    path.write_text(line("a") + "\n")
    commit(tmp_path, "a run", "registry/trials.jsonl")
    path.write_text(line("a") + "\n=======\n" + line("b") + "\n")         # a conflict committed with its markers
    commit(tmp_path, "merged", "registry/trials.jsonl")
    path.write_text(line("a") + "\n" + line("b") + "\n")
    commit(tmp_path, "markers removed", "registry/trials.jsonl")
    assert registry.dropped(path) == [] and registry.restore(path) == []
    assert registry.committed(path) == [line("a"), line("b")]
    path.write_text(line("a") + "\n" + line("b") + '\n{"card_hash":"0000"}\n')   # a line of another schema
    commit(tmp_path, "a line written by hand", "registry/trials.jsonl")
    with pytest.raises(RuntimeError, match="line 3, is not a registry line"):
        registry.lines(path)
    path.write_text(line("a") + "\n" + line("b") + "\n")
    commit(tmp_path, "removed", "registry/trials.jsonl")
    assert registry.dropped(path) == [] and registry.restore(path) == []
    path.write_text(line("a") + "\n" + line("b") + "\n" + line("c", monthly={"2020-13": 0.01}) + "\n")
    commit(tmp_path, "months that are not months", "registry/trials.jsonl")
    with pytest.raises(RuntimeError, match="line 3, is not a registry line"):
        registry.lines(path)
    path.write_text(line("a") + "\n" + line("b") + "\n")
    commit(tmp_path, "removed again", "registry/trials.jsonl")
    assert registry.dropped(path) == [] and registry.restore(path) == []
    path.write_text(line("a") + "\n" + line("b") + "\n" + line("c", monthly={"2020-0\u00b2": 0.01}) + "\n")
    commit(tmp_path, "a digit that is not ASCII", "registry/trials.jsonl")
    with pytest.raises(RuntimeError, match="line 3, is not a registry line"):
        registry.lines(path)
    path.write_text(line("a") + "\n" + line("b") + "\n")
    commit(tmp_path, "removed a third time", "registry/trials.jsonl")
    assert registry.dropped(path) == [] and registry.restore(path) == []


def test_restore_refuses_in_one_line_a_registry_it_cannot_write(tmp_path, capsys):
    path = repository(tmp_path)
    path.write_text(line("a") + "\n")
    commit(tmp_path, "a run", "registry/trials.jsonl")
    path.write_text("")
    path.chmod(0o444)
    try:
        assert registry.main(["restore"], path) == 1
    finally:
        path.chmod(0o644)
    said = capsys.readouterr().err
    assert said.startswith("refused: ") and said.count("\n") == 1 and "Traceback" not in said
    assert said == "refused: Permission denied: trials.jsonl\n"                 # the file named, not the machine
    registry.keep([line("a")], path)                                   # an edit to put back, by the other way
    path.write_text(line("a", sharpe=1.5) + "\n")
    path.chmod(0o444)
    try:
        assert registry.main(["restore"], path) == 1
        assert path.read_text() == line("a", sharpe=1.5) + "\n" and path.stat().st_mode & 0o777 == 0o444
    finally:
        path.chmod(0o644)
    assert capsys.readouterr().err == "refused: Permission denied: trials.jsonl\n"


def test_lines_kept_after_a_copy_cut_short_are_kept_whole(tmp_path):
    path = repository(tmp_path)
    registry.keep([line("a", 0)], path)
    with registry.copies(path).open("a") as rows:
        rows.write(line("a", 1)[:40])                                   # a full disk, as the copy was written
    registry.keep([line("b", 0)], path)
    assert registry.written(path) == [line("a", 0), line("b", 0)]


def test_a_line_of_a_card_this_clone_ran_that_its_run_did_not_write_is_removed(tmp_path):
    """Keyed on the card's hash: an edit of a line's variant and a line added under the card are none
    of the run's; another card's lines are left. Lines written by hand for a run that wrote none
    cannot be told from its own, and are left to the operator."""
    path = repository(tmp_path)
    registry.record("a" * 8, "2026-01-01T00:00:00Z", path)
    registry.keep([line("a", 0), line("a", 1)], path)
    registry.record("c" * 8, "2026-01-02T00:00:00Z", path)            # its run stopped before its lines
    edited, added, by_hand, other = line("a", 2, sharpe=1.5), line("a", 5), line("c", sharpe=1.5), line("b")
    path.write_text("\n".join([line("a", 0), edited, added, other]) + "\n")
    assert registry.missing(path) == ["a" * 8, "c" * 8]
    assert registry.restore(path) == [edited, added, line("a", 1)]
    assert path.read_text() == "\n".join([line("a", 0), other, line("a", 1)]) + "\n"
    assert registry.missing(path) == ["c" * 8]                         # void writes its lines
    assert registry.restore(path) == []
    registry.write([by_hand], path)
    for act in (registry.restore, registry.void_lost):
        with pytest.raises(RuntimeError, match="if they were written by hand, remove them from the file"):
            act(path)


def test_lines_added_by_the_first_commit_are_read_whatever_git_s_settings(tmp_path):
    path = repository(tmp_path)
    git("config", "log.showRoot", "false", cwd=tmp_path)
    path.write_text(line("a") + "\n")
    commit(tmp_path, "the first commit", "registry/trials.jsonl")
    assert registry.committed(path) == [line("a")]
    path.write_text("")
    assert registry.dropped(path) == [line("a")]


def test_the_registry_s_history_is_read_merges_included_and_a_resolution_counts(tmp_path):
    path = repository(tmp_path)
    path.write_text(line("a") + "\n")
    commit(tmp_path, "a run", "registry/trials.jsonl")
    trunk = git("symbolic-ref", "--short", "HEAD", cwd=tmp_path)
    git("checkout", "-q", "-b", "side", cwd=tmp_path)
    path.write_text(line("a") + "\n" + line("b") + "\n")
    commit(tmp_path, "a run on a side branch", "registry/trials.jsonl")
    git("checkout", "-q", trunk, cwd=tmp_path)
    path.write_text(line("a") + "\n" + line("c") + "\n")
    commit(tmp_path, "a run on the trunk", "registry/trials.jsonl")
    subprocess.run(["git", "merge", "-q", "side"], cwd=tmp_path, capture_output=True)
    path.write_text(line("a") + "\n" + line("c") + "\n" + line("b") + "\n" + line("d") + "\n")   # a line only the merge holds
    commit(tmp_path, "merged", "registry/trials.jsonl")
    assert set(registry.committed(path)) == {line(k) for k in "abcd"}
    path.write_text(line("a") + "\n" + line("c") + "\n")
    assert sorted(registry.dropped(path)) == [line("b"), line("d")]


def test_a_card_s_variant_counts_once_in_gate_four_as_first_committed(tmp_path):
    path = repository(tmp_path)
    path.write_text(line("a", 0, 0.1) + "\n" + line("a", 1, 0.2) + "\n")
    commit(tmp_path, "a run", "registry/trials.jsonl")
    edited = line("a", 0, 0.9)
    path.write_text(edited + "\n" + line("a", 1, 0.2) + "\n")               # edited in place
    assert registry.dropped(path) == [line("a", 0, 0.1)]
    assert registry.restore(path) == [line("a", 0, 0.1)]                    # the original put back, at the end
    assert [t.sharpe for t in registry.history(path)] == [0.2, 0.1]         # the edit counts nothing
    commit(tmp_path, "edited and restored", "registry/trials.jsonl")
    assert [t.sharpe for t in registry.history(path)] == [0.2, 0.1]


def test_a_void_run_counts_in_gate_four_when_its_returns_are_known(tmp_path):
    path = tmp_path / "trials.jsonl"
    registry.void("v", "v" * 8, [{"span": 1}, {"span": 2}], "the strategy changed the lab as it ran", path,
                  trials=verdict("v").trials)
    registry.void("w", "w" * 8, [{"span": 1}], registry.LOST, path)
    trials = registry.history(path)
    assert [(t.sharpe, t.survivor) for t in trials] == [(0.3, False), (-0.1, False)]
    held = registry.lines(path)
    assert [bool(h["monthly"]) for h in held] == [True, True, False] and {h["gates"] == {} for h in held} == {True}


def test_lines_lost_before_their_commit_are_put_back_with_their_returns(tmp_path):
    path = repository(tmp_path)
    path.write_text("")
    commit(tmp_path, "the registry", "registry/trials.jsonl")
    registry.record("r" * 8, "2026-01-01T00:00:00Z", path)
    wrote = registry.append(verdict("r"), "r" * 8, [{"span": 1}, {"span": 2}], "s", None, "c", {}, path)
    git("checkout", "--", "registry/trials.jsonl", cwd=tmp_path)            # lost before their commit
    assert registry.missing(path) == ["r" * 8]
    assert registry.void_lost(path) == ([], [], ["r" * 8])                  # not void: the clone kept them
    assert registry.lines(path) == []
    registry.restore(path)
    assert registry.lines(path) == wrote and registry.missing(path) == []
    assert [t.sharpe for t in registry.history(path)] == [0.3, -0.1]


def test_a_line_dropped_by_a_rewrite_of_the_branch_is_put_back_by_the_clone_that_wrote_it(tmp_path):
    path = repository(tmp_path)
    path.write_text("")
    commit(tmp_path, "the registry", "registry/trials.jsonl")
    registry.record("r" * 8, "2026-01-01T00:00:00Z", path)
    wrote = registry.append(verdict("r"), "r" * 8, [{"span": 1}, {"span": 2}], "s", None, "c", {}, path)
    path.write_text(registry.compact(wrote[0]) + "\n")                       # one variant's line left out
    git("add", "registry/trials.jsonl", cwd=tmp_path)
    git("commit", "-q", "--amend", "-m", "the registry", cwd=tmp_path)     # the history holds no trace of it
    assert registry.dropped(path) == [] and registry.missing(path) == ["r" * 8]
    assert registry.restore(path) == [registry.compact(wrote[1])]
    assert registry.missing(path) == []


def test_void_writes_lines_only_for_the_runs_that_wrote_none_named_by_their_card_s_id(tmp_path):
    path = repository(tmp_path)
    strategies = tmp_path / "strategies"
    text = "id: t-1-01-a\nvariants:\n  - {span: 1}\n  - {span: 2}\n"
    for folder in ("t-1-01-a", "t-1-02-copy"):                              # a copy of the card, same bytes
        (strategies / folder).mkdir(parents=True)
        (strategies / folder / "card.yaml").write_text(text)
    lost = hashlib.sha256(text.encode()).hexdigest()
    path.write_text("")
    commit(tmp_path, "the lab", "registry/trials.jsonl", "strategies")
    registry.record("r" * 8, "2026-01-01T00:00:00Z", path)
    registry.append(verdict("r"), "r" * 8, [{"span": 1}, {"span": 2}], "s", None, "c", {}, path)
    registry.record(lost, "2026-01-02T00:00:00Z", path)                     # began, and wrote nothing
    assert registry.void_lost(path) == (["t-1-01-a"], [], [])
    voided = [h for h in registry.lines(path) if h.get("void")]
    assert [(h["card"], h["card_hash"], h["variant"], h["time"]) for h in voided] == [
        ("t-1-01-a", lost, 0, "2026-01-02T00:00:00Z"), ("t-1-01-a", lost, 1, "2026-01-02T00:00:00Z")]
    assert registry.missing(path) == []


def test_void_waits_for_no_run_and_refuses_while_one_is_going(tmp_path, capsys):
    path = repository(tmp_path)
    with registry.held(path):
        with pytest.raises(RuntimeError, match="a run is going in this clone"):
            registry.void_lost(path)
        assert registry.main(["void"], path) == 1
    assert "refused: a run is going in this clone" in capsys.readouterr().err
    assert registry.main(["void"], path) == 0


def test_two_edits_are_put_back_each_in_its_place(tmp_path):
    path = repository(tmp_path)
    registry.record("a" * 8, "2026-01-01T00:00:00Z", path)
    registry.keep([line("a", 0), line("a", 1)], path)
    path.write_text("\n".join([line("a", 0, sharpe=1.5), line("a", 1, sharpe=1.5), line("b")]) + "\n")
    assert registry.restore(path) == [line("a", 0), line("a", 1)]
    assert path.read_text() == "\n".join([line("a", 0), line("a", 1), line("b")]) + "\n"


@pytest.mark.parametrize("damage", ["removed", "emptied", "older"])
def test_where_the_clone_s_copy_holds_none_of_a_card_its_lines_are_neither_removed_nor_voided(tmp_path, damage):
    """A copy lost, emptied, or an older one put back: the run's lines not yet committed cannot be
    told from lines written by hand, and restore and void refuse, and name the ways on."""
    path = repository(tmp_path)
    registry.record("z" * 8, "2026-01-01T00:00:00Z", path)
    registry.append(verdict("z", (0.2,)), "z" * 8, [{}], "s", None, "c", {}, path)
    commit(tmp_path, "an earlier run", "registry/trials.jsonl")
    older = registry.copies(path).read_text()
    registry.record("a" * 8, "2026-01-02T00:00:00Z", path)
    registry.append(verdict("a"), "a" * 8, [{}, {}], "s", None, "c", {}, path)
    kept = path.read_text()
    if damage == "removed":
        registry.copies(path).rename(tmp_path / "aside")
    else:
        registry.copies(path).write_text("" if damage == "emptied" else older)
    assert registry.missing(path) == ["a" * 8]
    for act in (registry.restore, registry.void_lost):
        with pytest.raises(RuntimeError, match="holds none of the card aaaaaaaa, .*cannot be told from lines written by hand"):
            act(path)
    assert path.read_text() == kept
    commit(tmp_path, "the runs' own lines", "registry/trials.jsonl")
    assert registry.missing(path) == [] and sorted(t.sharpe for t in registry.history(path)) == [-0.1, 0.2, 0.3]


@pytest.mark.parametrize("first", ["the run", "the void"])
def test_a_void_line_never_hides_the_returns_of_another_clone_s_run_of_its_card(tmp_path, first):
    """This clone's run of a card ended its process, and void wrote its lines; another clone ran the
    card in full. Whichever was committed first, every clone counts the run's returns."""
    path = repository(tmp_path)
    (tmp_path / "strategies" / "a").mkdir(parents=True)
    (tmp_path / "strategies" / "a" / "card.yaml").write_text("id: a\nvariants:\n  - {span: 1}\n")
    card = hashlib.sha256((tmp_path / "strategies" / "a" / "card.yaml").read_bytes()).hexdigest()
    run = registry.compact({**json.loads(line("a", sharpe=0.7)), "card_hash": card})
    path.write_text("")
    commit(tmp_path, "the lab", "registry/trials.jsonl", "strategies")
    registry.record(card, "2026-01-01T00:00:00Z", path)                 # its run ended its process
    if first == "the run":
        registry.write([run], path)
        commit(tmp_path, "another clone's run, merged", "registry/trials.jsonl")
    assert registry.void_lost(path) == ((["a"], [], []) if first == "the void" else ([], [], []))
    if first == "the void":
        commit(tmp_path, "void", "registry/trials.jsonl")
        registry.write([run], path)
        commit(tmp_path, "another clone's run, merged", "registry/trials.jsonl")
    counted = sorted((t.key, t.sharpe) for t in registry.history(path))
    assert counted == [(f"a/0@{card[:12]}", 0.7)] and counted == fresh(path, tmp_path)


def test_a_sharpe_edit_committed_at_once_counts_as_the_run_wrote_it_in_the_clone_that_ran_it(tmp_path):
    """And as edited in a clone that holds no copy to tell."""
    path = repository(tmp_path)
    registry.record("a" * 8, "2026-01-01T00:00:00Z", path)
    registry.append(verdict("a"), "a" * 8, [{}, {}], "s", None, "c", {}, path)
    ran = path.read_text().splitlines()
    edit = {**json.loads(ran[1]), "sharpe": 1.5}
    path.write_text(ran[0] + "\n" + registry.compact(edit) + "\n")
    commit(tmp_path, "an edit committed at once", "registry/trials.jsonl")
    assert registry.restore(path) == [ran[1]]                          # the run's line, beside its edit
    commit(tmp_path, "the run's line back", "registry/trials.jsonl")
    assert sorted((t.key, t.sharpe) for t in registry.history(path)) == [("a/0@aaaaaaaa", 0.3), ("a/1@aaaaaaaa", -0.1)]
    assert fresh(path, tmp_path) == [("a/0@aaaaaaaa", 0.3), ("a/1@aaaaaaaa", 1.5)]


def test_a_line_whose_sharpe_is_zero_has_returns(tmp_path):
    path = repository(tmp_path)
    path.write_text(line("q", sharpe=None, void=registry.LOST) + "\n" + line("q", sharpe=0.0) + "\n")
    assert [t.sharpe for t in registry.history(path)] == [0.0]


def test_the_refusal_names_every_card_the_copy_cannot_tell_and_void_leaves_the_cards_it_kept(tmp_path):
    path = repository(tmp_path)
    for card in "ac":
        registry.record(card * 8, "2026-01-01T00:00:00Z", path)
    registry.keep([line("a", 0), line("a", 1)], path)
    path.write_text("\n".join([line("a", 0), line("a", 1, sharpe=1.5)]) + "\n")    # an edit of a kept line
    assert registry.void_lost(path) == ([], ["c" * 8], ["a" * 8])      # a's run kept: restore puts it back
    registry.copies(path).unlink()
    registry.write([line("c", sharpe=1.5)], path)
    for act in (registry.restore, registry.void_lost):
        with pytest.raises(RuntimeError, match="holds none of the cards aaaaaaaa, cccccccc, whose lines"):
            act(path)


def test_two_cards_that_share_an_id_count_apart(tmp_path):
    path = repository(tmp_path)
    path.write_text(line("a") + "\n" + registry.compact({**json.loads(line("a")), "card_hash": "e" * 8}) + "\n")
    assert len(registry.history(path)) == 2


def fresh(path, tmp_path):
    """The history a clone that ran nothing reads: the record and the copy put aside, then back."""
    kept = [registry.marker(path), registry.copies(path)]
    aside = [tmp_path / f"aside-{k}" for k in range(2)]
    for there, away in zip(kept, aside):
        if there.exists():
            there.rename(away)
    try:
        return sorted((t.key, t.sharpe) for t in registry.history(path))
    finally:
        for there, away in zip(kept, aside):
            if away.exists():
                away.rename(there)


def test_committed_lines_count_alike_in_every_clone_the_one_that_ran_the_card_included(tmp_path):
    """A line committed counts in the clone that ran its card as in any other, whoever wrote it: an
    added variant, lines for a run that ended its process (another clone's run of the same card, or
    lines written by hand, which no clone can tell apart), and `void` writes nothing for them."""
    path = repository(tmp_path)
    (tmp_path / "strategies").mkdir()
    registry.record("a" * 8, "2026-01-01T00:00:00Z", path)
    registry.keep([line("a", 0), line("a", 1)], path)
    registry.record("c" * 8, "2026-01-02T00:00:00Z", path)            # its run ended its process
    path.write_text("\n".join([line("a", 0), line("a", 1), line("a", 5, sharpe=1.5), line("c", sharpe=1.5),
                               line("b")]) + "\n")
    commit(tmp_path, "lines committed at once", "registry/trials.jsonl")
    assert registry.missing(path) == [] and registry.void_lost(path) == ([], [], [])
    counted = sorted((t.key, t.sharpe) for t in registry.history(path))
    assert [k for k, _ in counted] == ["a/0@aaaaaaaa", "a/1@aaaaaaaa", "a/5@aaaaaaaa", "b/0@bbbbbbbb", "c/0@cccccccc"]
    assert counted == fresh(path, tmp_path)


@pytest.mark.parametrize("damage", ["removed", "emptied"])
def test_a_clone_whose_copy_is_lost_counts_every_trial_and_voids_no_run_that_wrote_its_lines(tmp_path, damage):
    """Runs committed, then the clone's copy removed or emptied: the next run starts a copy of its
    own lines, and the card after it counts every trial another clone counts."""
    path = repository(tmp_path)
    (tmp_path / "strategies").mkdir()
    for card in "ab":
        registry.record(card * 8, "2026-01-01T00:00:00Z", path)
        registry.append(verdict(card), card * 8, [{"span": 1}, {"span": 2}], "s", None, "c", {}, path)
    commit(tmp_path, "two runs", "registry/trials.jsonl")
    registry.copies(path).unlink() if damage == "removed" else registry.copies(path).write_text("")
    assert registry.missing(path) == []
    registry.record("c" * 8, "2026-01-02T00:00:00Z", path)
    registry.append(verdict("c"), "c" * 8, [{"span": 1}, {"span": 2}], "s", None, "c", {}, path)
    commit(tmp_path, "the next run", "registry/trials.jsonl")
    assert registry.missing(path) == [] and registry.void_lost(path) == ([], [], [])
    assert not any(h.get("void") for h in registry.lines(path))
    assert len(registry.history(path)) == 6 and sorted((t.key, t.sharpe) for t in registry.history(path)) == \
        fresh(path, tmp_path)


def test_a_line_is_judged_once_per_process(tmp_path):
    path = repository(tmp_path)
    path.write_text("\n".join([line("a", 0), line("a", 1), line("b")]) + "\n")
    registry.valid.cache_clear()
    for _ in range(3):
        registry.lines(path)
    assert registry.valid.cache_info().misses == 3


def test_restore_counts_the_lines_it_removes_apart(tmp_path, capsys):
    path = repository(tmp_path)
    registry.record("a" * 8, "2026-01-01T00:00:00Z", path)
    registry.keep([line("a", 0)], path)
    path.write_text(line("a", 0) + "\n" + line("a", 5) + "\n")
    assert registry.main(["restore"], path) == 0
    assert capsys.readouterr().out == "0 lines put back, 1 removed; commit registry/trials.jsonl at once, alone\n"
