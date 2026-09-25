"""The trial registry: one line per run, appended, never rewritten.

Each run of a card writes one line per variant, a JSON object: when it ran, the card's id and hash,
the variant and its parameters, the data snapshot's name and hash, the code commit, the versions
of the libraries, the thresholds' version, the variant's monthly excess returns hedged of its
benchmark and their Sharpe ratio (the appraisal ratio, under `sharpe`), and the card's gate
results. The lines feed the effective number of trials of gate 4, the survivors of gate 6, the
status board, and the rule that a card's holdout is opened once. A card whose strategy could not
run, or never held an asset, writes its lines too, without returns: it has run, and gate 4 has no
trial of it to count. So does a void run, with its reason under `void`: its strategy changed the
lab as it ran, and its returns are kept, since the battery computed them; or its run stopped
before it had any.

The clone keeps, in its git folder, which all its worktrees share and no stash, reset or checkout
reaches, the hash of every card whose run began, written before the battery opens the holdout, and
a copy of every line its runs wrote. No card runs while the registry lacks one of those lines, or a
card of the record has none, since gate 4 would count too few trials: `restore` puts back the lines
the clone kept, and `void` writes void lines for a run that wrote none. Nor does a card run while
the file lacks a line that a commit in the branch's history held.

    python -m lab.registry restore    # puts back the lines a commit held, or this clone wrote, that the file lacks
    python -m lab.registry void       # writes void lines for the runs this clone began that wrote none
"""
from __future__ import annotations

import fcntl
import functools
import hashlib
import json
import os
import re
import subprocess
import sys
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import yaml

from lab.battery import Trial, Verdict

REGISTRY = Path(__file__).resolve().parent.parent / "registry" / "trials.jsonl"
LOST = "no line of its run is in the registry or in this clone's copy"
UNTOLD = ("the clone's copy of the lines its runs wrote holds none of the card{s} {cards}, whose lines not yet "
          "committed the registry holds, so they cannot be told from lines written by hand: put the clone's own copy "
          "back in the git folder; if those lines are the runs' own, commit the registry as it is; if they were "
          "written by hand, remove them from the file")


def untold(cards) -> str:
    """The refusal for lines not yet committed of cards the clone's copy holds none of, naming them."""
    return UNTOLD.format(s="" if len(cards) == 1 else "s", cards=", ".join(sorted(h[:12] for h in cards)))


FIELDS = {"time": (str,), "card": (str,), "card_hash": (str,), "variant": (int,), "sharpe": (int, float, type(None)),
          "monthly": (dict,), "failed": (int, type(None)), "survivor": (bool,)}     # what the lab reads of a line
MONTH = re.compile(r"[0-9]{4}-(0[1-9]|1[0-2])")                                     # ASCII digits only
LARGEST = 1e6                         # a monthly return or a Sharpe ratio beyond it is not the lab's


def entry(text: str) -> dict | None:
    """What a registry line holds, or None for a text that is not one: a JSON object holding every
    field the lab reads, each of its type, and months that the lab reads as months, once each, each
    a number that reads as a float, as the Sharpe ratio does, and none infinite or beyond a million.
    A line is judged once."""
    return json.loads(text) if valid(text) else None


@functools.lru_cache(maxsize=None)
def valid(text: str) -> bool:
    """Whether `text` is a registry line (`entry`)."""
    try:
        line = json.loads(text)
    except ValueError:
        return False
    if not isinstance(line, dict):
        return False
    for name, kinds in FIELDS.items():
        value = line.get(name, ...)
        if not isinstance(value, kinds) or (isinstance(value, bool) and bool not in kinds):
            return False
    months, sharpe = line["monthly"], line["sharpe"]
    if any(not isinstance(v, (int, float)) or isinstance(v, bool) for v in months.values()) or \
            any(not isinstance(m, str) or not MONTH.fullmatch(m) for m in months):
        return False
    try:                                                  # read as gates 4 and 6 read them
        read = monthly_series(months)
        numbers = [float(v) for v in [*months.values(), *([] if sharpe is None else [sharpe])]]
    except (ValueError, TypeError, OverflowError):
        return False
    return read.index.is_unique and not any(abs(x) > LARGEST for x in numbers)      # infinite included


def texts(path: Path = REGISTRY) -> list[str]:
    """The registry's lines as written, refused in one line where one is not a registry line."""
    if not path.exists():
        return []
    held = []
    for number, text in enumerate(path.read_text().splitlines(), 1):
        if not text.strip():
            continue
        if entry(text) is None:
            raise RuntimeError(f"{path.name}, line {number}, is not a registry line: a merge of the registry keeps "
                               f"both sides' lines, and nothing else")
        held.append(text)
    return held


def lines(path: Path = REGISTRY) -> list[dict]:
    return [entry(text) for text in texts(path)]


def history(path: Path = REGISTRY, done: list[str] | None = None) -> list[Trial]:
    """Every trial the registry holds, as gates 4 and 6 read them, a void run's too when its returns
    are known, never as a survivor. A trial is named by its card, its variant and the start of its
    card's hash, so that two cards can never share a name. A trial counts once: where two lines hold
    one card's variant, the line this clone's run wrote counts, or else the line first committed, so
    that a line edited counts as its run wrote it in the clone that ran it (`restore` puts the run's
    line back in place of an edit not yet committed). A line with returns counts before one without,
    so that a void line saying that a card ran never hides a run's returns. Any other line committed
    counts alike in every clone, whoever wrote it: a clone's copy can be lost, and another clone can
    run the same card. `done` is `committed()`, when already read."""
    held = texts(path)
    mine = set(written(path))
    first = {}
    for text in committed(path) if done is None else done:
        first.setdefault(text, len(first))
    chosen: dict[tuple, int] = {}
    for k in sorted(range(len(held)), key=lambda k: (entry(held[k])["sharpe"] is None, held[k] not in mine,
                                                      first.get(held[k], len(first)), k)):
        line = entry(held[k])
        chosen.setdefault((line["card_hash"], line["variant"]), k)
    return [Trial(f"{line['card']}/{line['variant']}@{line['card_hash'][:12]}", monthly_series(line["monthly"]),
                  line["sharpe"], line["survivor"])
            for line in (entry(held[k]) for k in sorted(chosen.values())) if line["sharpe"] is not None]


def opened(card_hash: str, path: Path = REGISTRY) -> str | None:
    """When a card with this hash was run, if ever: its holdout is then open, and stays opened."""
    ran = next((line["time"] for line in lines(path) if line["card_hash"] == card_hash), None)
    if ran is None:
        ran = next((row[1] for row in recorded(path) if row[0] == card_hash), None)
    return ran


def marker(path: Path = REGISTRY) -> Path | None:
    """The clone's own list of the cards whose run began, in the git folder all its worktrees share,
    which no stash, reset or checkout reaches; None outside a git repository."""
    near = next(p for p in (path.parent, *path.parents) if p.exists())
    done = subprocess.run(["git", "rev-parse", "--git-common-dir"], cwd=near, capture_output=True, text=True)
    return (near / done.stdout.strip() / "alpha-lab-opened").resolve() if done.returncode == 0 else None


def recorded(path: Path = REGISTRY) -> list[list[str]]:
    """The clone's record: one row per card whose run began, its hash and when."""
    kept = marker(path)
    if kept is None or not kept.exists():
        return []
    return [row.split() for row in kept.read_text().splitlines() if row.strip()]


def copies(path: Path = REGISTRY) -> Path | None:
    """The clone's copy of every line its runs wrote, beside its record; None outside a git
    repository."""
    kept = marker(path)
    return None if kept is None else kept.with_name("alpha-lab-lines")


def written(path: Path = REGISTRY) -> list[str]:
    """The registry lines this clone's runs wrote, as kept in its git folder."""
    kept = copies(path)
    if kept is None or not kept.exists():
        return []
    return [text for text in kept.read_text().splitlines() if entry(text) is not None]


@contextmanager
def held(path: Path = REGISTRY, wait: bool = True):
    """The clone's record, held by one run at a time, from its checks until its lines are written.
    Without `wait`, refused at once while a run holds it."""
    kept = marker(path)
    if kept is None:
        yield
        return
    with kept.with_name(kept.name + ".lock").open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX if wait else fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError("a run is going in this clone: wait for its end") from None
        try:
            yield
        finally:
            fcntl.flock(lock, fcntl.LOCK_UN)


def record(card_hash: str, when: str, path: Path = REGISTRY) -> None:
    kept = marker(path)
    if kept is not None:
        with kept.open("a") as rows:
            rows.write(f"{card_hash} {when}\n")


def missing(path: Path = REGISTRY, done: list[str] | None = None) -> list[str]:
    """The cards whose run this clone began and whose lines the registry does not hold as they were
    written: a card of the record without a line, a line this clone wrote that the file lacks, or a
    line not yet committed that holds the hash of a card this clone ran, and not the text of a line
    its run wrote. A run still going, or lines put aside, lost, edited or written by hand. `done` is
    `committed()`, when already read."""
    held = texts(path)
    have, cards = set(held), {entry(text)["card_hash"] for text in held}
    mine = written(path)
    lost = {entry(text)["card_hash"] for text in mine if text not in have}
    was, ran, ours = set(committed(path) if done is None else done), ran_cards(path, mine), set(mine)
    edited = {entry(text)["card_hash"] for text in held
              if text not in was and text not in ours and entry(text)["card_hash"] in ran}
    return sorted(lost | edited | {row[0] for row in recorded(path) if row[0] not in cards})


def ran_cards(path: Path = REGISTRY, mine: list[str] | None = None) -> set[str]:
    """The hashes of the cards this clone ran: those of its record, and of the lines its runs wrote."""
    mine = written(path) if mine is None else mine
    return {entry(text)["card_hash"] for text in mine} | {row[0] for row in recorded(path)}


def key(text: str) -> tuple:
    """A line's card and variant: one run of a card writes one line of each."""
    line = entry(text)
    return line["card_hash"], line["variant"]


def committed(path: Path = REGISTRY) -> list[str]:
    """Every registry line that a commit in the branch's history held, in the order they were first
    committed, read in one pass over the file's history, merges included: each line was added by
    some commit, against one of its parents."""
    near = next(p for p in (path.parent, *path.parents) if p.exists())
    top = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=near, capture_output=True, text=True)
    if top.returncode:
        return []
    root = Path(top.stdout.strip())
    name = path.resolve().relative_to(root.resolve()).as_posix()
    log = subprocess.run(["git", "log", "--root", "--full-history", "--reverse", "--diff-merges=separate", "-p", "--format=",
                          "--no-color", "--no-ext-diff", "--no-textconv", "--no-renames", "HEAD", "--", name],
                         cwd=root, capture_output=True, text=True)
    seen: dict[str, None] = {}
    for row in log.stdout.splitlines() if log.returncode == 0 else []:
        if row.startswith("+") and entry(row[1:]) is not None:
            seen.setdefault(row[1:])
    return list(seen)


def dropped(path: Path = REGISTRY, done: list[str] | None = None) -> list[str]:
    """The lines that a commit in the branch's history held and the file lacks, in the order they
    were first committed: none, for a registry that only grows. Merges are read, so a merge keeping
    one side is found; a version restored, or two runs merged, lack nothing. A rewrite of the
    branch's own history (an amend, a rebase, a squash) leaves no commit behind: the lines this
    clone wrote are kept for that (`missing`). `done` is `committed()`, when already read."""
    have = set(path.read_text().splitlines()) if path.exists() else set()
    return [text for text in (committed(path) if done is None else done) if text not in have]


def write(texts: list[str], path: Path = REGISTRY) -> None:
    """Lines at the end of the registry, all in one write."""
    if not texts:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    start = "\n" if path.exists() and path.read_bytes()[-1:] not in (b"", b"\n") else ""
    with path.open("a") as registry:
        registry.write(start + "".join(text + "\n" for text in texts))


def keep(texts: list[str], path: Path = REGISTRY) -> None:
    """Lines in the clone's copy, before the registry: a registry that cannot be written, or lines
    lost before their commit, leave them there for `restore`."""
    kept = copies(path)
    if kept is not None and texts:
        start = "\n" if kept.exists() and kept.read_bytes()[-1:] not in (b"", b"\n") else ""   # after a write cut short
        with kept.open("a") as rows:
            rows.write(start + "".join(text + "\n" for text in texts))


def compact(line: dict) -> str:
    return json.dumps(line, separators=(",", ":"))


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def returns(trial) -> dict:
    """What gates 4 and 6 read of a trial; empty without one."""
    return {"sharpe": round(trial.sharpe, 6) if trial else None,
            "monthly": {when.strftime("%Y-%m"): round(float(v), 6) for when, v in trial.monthly.dropna().items()}
            if trial else {}}


def append(verdict: Verdict, card_hash: str, variants, snapshot: str, snapshot_hash: str | None, commit: str,
           versions: dict, path: Path = REGISTRY) -> list[dict]:
    """Write the run of a card, one line per variant, in the clone's copy, then at the end of the
    registry, in one write. The first gate failed and the survivor are read from the gates written,
    not from the verdict."""
    gates = {str(g.number): g.passed for g in verdict.gates}
    failed = next((g.number for g in verdict.gates if g.passed is not True), None)
    trials = verdict.trials or [None] * len(variants)          # nothing held, or nothing ran
    new = [{"time": now(), "card": verdict.card, "card_hash": card_hash, "variant": k,
            "parameters": parameters, "snapshot": snapshot, "snapshot_hash": snapshot_hash, "commit": commit,
            "versions": versions, "thresholds": verdict.thresholds, **returns(trial),
            "gates": gates, "failed": failed, "survivor": bool(verdict.gates) and failed is None}
           for k, (trial, parameters) in enumerate(zip(trials, variants))]
    keep([compact(line) for line in new], path)
    write([compact(line) for line in new], path)
    return new


def void(card: str, card_hash: str, variants, reason: str, path: Path = REGISTRY, when: str | None = None,
         trials=None, **known) -> list[dict]:
    """Write a void run of a card, one line per variant, without gates, with its reason, in the
    clone's copy and in the registry: its card has run, and runs no more. Its returns are kept when
    the battery computed them, and count in gate 4."""
    fields = ("snapshot", "snapshot_hash", "commit", "versions", "thresholds")
    trials = trials or [None] * len(variants)
    new = [{"time": when or now(), "card": card, "card_hash": card_hash, "variant": k, "parameters": parameters,
            **{f: known.get(f) for f in fields}, **returns(trial), "gates": {}, "failed": None,
            "survivor": False, "void": reason}
           for k, (trial, parameters) in enumerate(zip(trials, variants))]
    keep([compact(line) for line in new], path)
    write([compact(line) for line in new], path)
    return new


def restore(path: Path = REGISTRY) -> list[str]:
    """Put back what the file lacks, in one write, while no run is going in this clone. A line not
    yet committed that holds the hash of a card this clone ran, and not the text of a line its run
    wrote, was edited or written by hand: the run's line of its card and variant takes back its
    place, or, when the file holds it already or the run wrote none of that variant, the line is
    removed, which drops nothing a commit held. Refused while the copy holds no line of its card
    (lost, emptied, or an older copy put back): the run's own lines cannot be told from lines
    written by hand. Then the lines a commit held, and those this clone wrote, that the file
    lacks are appended. A line once committed is never replaced: the history only grows. Returns the
    lines put back and those removed."""
    with held(path, wait=False):
        rows = path.read_text().splitlines() if path.exists() else []
        done = committed(path)
        mine = written(path)
        run_line = {}
        for text in mine:
            run_line.setdefault(key(text), text)
        was, ours, ran, changed = set(done), set(mine), ran_cards(path, mine), []
        kept, unknown = {entry(text)["card_hash"] for text in mine}, set()
        for k, text in enumerate(rows):
            if entry(text) is None or text in was or text in ours or entry(text)["card_hash"] not in ran:
                continue
            if entry(text)["card_hash"] not in kept:
                unknown.add(entry(text)["card_hash"])
                continue
            original = run_line.get(key(text))
            there = original is None or original in rows
            rows[k] = None if there else original
            changed.append(text if there else original)
        if unknown:
            raise RuntimeError(untold(unknown))
        rows = [row for row in rows if row is not None]
        have = set(rows)
        back = [text for text in dict.fromkeys([*done, *mine]) if text not in have]
        if changed:
            if path.exists() and not os.access(path, os.W_OK):
                raise PermissionError(13, "Permission denied", path.name)
            fresh = path.with_name(path.name + ".restored")
            fresh.write_text("".join(row + "\n" for row in [*rows, *back]))
            fresh.replace(path)
        else:
            write(back, path)
    return [*changed, *back]


def void_lost(path: Path = REGISTRY) -> tuple[list[str], list[str], list[str]]:
    """Void lines for every run this clone began that wrote no line in the clone's copy, and whose
    card no line committed holds (`missing`). Refused while the file holds lines not yet committed of
    such a card, which the copy cannot tell from lines written by hand, and while a run is going in
    this clone. The card is found among the lab's strategy folders, and the lines are named by its
    id. Returns the ids voided, the hashes of the cards not found, and those of the runs whose lines
    the clone kept, which `restore` puts back."""
    with held(path, wait=False):
        folders = {hashlib.sha256(card.read_bytes()).hexdigest(): card
                   for card in sorted((path.parent.parent / "strategies").glob("*/card.yaml"))}
        began = {row[0]: row[1] for row in recorded(path)}
        wrote = {entry(text)["card_hash"] for text in written(path)}          # lines by hand are not the run's
        unknown = {entry(text)["card_hash"] for text in texts(path)} & (set(missing(path)) - wrote)
        if unknown:
            raise RuntimeError(untold(unknown))         # lines the copy cannot tell: the run's, or by hand
        done, unknown, kept = [], [], []
        for card_hash in missing(path):
            if card_hash in wrote:
                kept.append(card_hash)
                continue
            card = folders.get(card_hash)
            if card is None:
                unknown.append(card_hash)
                continue
            spec = yaml.safe_load(card.read_text())
            void(str(spec["id"]), card_hash, spec["variants"], LOST, path, when=began[card_hash])
            done.append(str(spec["id"]))
    return done, unknown, kept


def main(argv: list[str], path: Path = REGISTRY) -> int:
    command = argv[0] if argv else ""
    try:
        if command == "restore":
            changed = restore(path)
            now = set(path.read_text().splitlines()) if path.exists() else set()
            back, gone = [t for t in changed if t in now], [t for t in changed if t not in now]
            print(f"{len(back)} line{'' if len(back) == 1 else 's'} put back"
                  + (f", {len(gone)} removed" if gone else "")
                  + ("; commit registry/trials.jsonl at once, alone" if changed else ""))
            return 0
        if command == "void":
            done, unknown, kept = void_lost(path)
    except OSError as error:
        print(f"refused: {error.strerror}: {Path(str(error.filename)).name}" if error.filename else f"refused: {error}",
              file=sys.stderr)
        return 1
    except RuntimeError as error:
        print(f"refused: {error}", file=sys.stderr)
        return 1
    if command == "void":
        for card in done:
            print(f"{card}: void lines written ({LOST})")
        for card_hash in kept:
            print(f"the card {card_hash[:12]} wrote its lines, which this clone kept: python -m lab.registry restore "
                  f"puts them back", file=sys.stderr)
        for card_hash in unknown:
            print(f"no strategy folder holds the card {card_hash[:12]}: put its folder back, then run this again",
                  file=sys.stderr)
        if done:
            print("commit registry/trials.jsonl at once, alone")
        return 1 if unknown or kept else 0
    print("usage: python -m lab.registry restore | void", file=sys.stderr)
    return 2


def monthly_series(monthly: dict) -> pd.Series:
    """Months back on the month-end dates the battery uses."""
    ends = pd.PeriodIndex(list(monthly), freq="M").to_timestamp(how="end").normalize()
    return pd.Series(list(monthly.values()), index=ends, dtype=float)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
