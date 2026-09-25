"""The chain on a dummy strategy: a registry line, an executed notebook, a row on the board; and
every refusal that keeps a run honest."""
import atexit
import errno
import hashlib
import importlib.util
import json
import marshal
import os
import pickle
import py_compile
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
import warnings
from datetime import datetime, timedelta, timezone
from pathlib import Path

import nbformat
import numpy as np
import pandas as pd
import pytest

from lab import battery, costs, data, engine, registry, report, stats, status, universe
from tests.conftest import CLUSTERS, EIGHT, synthetic_market

CARD = """id: %s
theory: DEMO-1
mechanism: Returns persist over a few weeks.
prediction: {sign: positive, size: a Sharpe ratio of about 0.3}
universe: [%s]
horizon: weeks
signal: The assets whose return over the span is positive, in equal parts, reset every five sessions.
parameters:
  span: sessions of the return that decides
variants:
  - {span: %d}
  - {span: %d}
neighbours:
  span: {25: [%d, %d], 50: [%d, %d]}
refuted_if: The Sharpe ratio net of costs is not above the benchmark's.
"""

STRATEGY = '''import pandas as pd


def positions(market, span):
    up = (market.signal_prices.pct_change(span).shift(1) > 0).astype(float)
    weights = up.div(up.sum(axis=1).where(up.sum(axis=1) > 0), axis=0).fillna(0.0)
    every = pd.Series(range(len(weights)), index=weights.index) % 5 == 0
    return weights.where(every, axis=0)
'''

BROKEN = "def positions(market, span):\n    raise ValueError('no signal yet')\n"
FIRST_LINE = "def positions(market, span):\n"
LAB_OF = "import sys\nLAB = sys.modules\n"          # the lab reached without an import the runner reads

BANK = """---
id: DEMO-1
title: A demonstration theory
family: Trend and momentum
status: in-progress
---

## Mechanism
"""


def card(ident, span, universe=EIGHT):
    return CARD % (ident, ", ".join(universe), span, 2 * span, round(span * 0.75), round(span * 1.25),
                   round(span * 0.5), round(span * 1.5))


def git(*args, cwd):
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def commit(root, message, *paths):
    git("add", *paths, cwd=root)
    git("commit", "-q", "-m", message, cwd=root)


def new_strategy(root, ident, span=20, code=STRATEGY, universe=EIGHT):
    """A strategy folder the runbook's way: the card committed alone, then the code."""
    folder = root / "strategies" / ident
    folder.mkdir(parents=True)
    (folder / "card.yaml").write_text(card(ident, span, universe))
    commit(root, f"card: {ident}", f"strategies/{ident}/card.yaml")
    (folder / "strategy.py").write_text(code)
    commit(root, f"strategy: {ident}", f"strategies/{ident}/strategy.py")
    return folder


@pytest.fixture
def lab(tmp_path):
    """A lab in a subfolder of its repository, as the real one is."""
    top, root = tmp_path / "repository", tmp_path / "repository" / "alpha-lab"
    root.mkdir(parents=True)
    git("init", "-q", cwd=top)
    git("config", "user.name", "lab", cwd=top)
    git("config", "user.email", "lab@example.invalid", cwd=top)
    (root / "bank").mkdir()
    (root / "bank" / "DEMO-1.md").write_text(BANK)
    for name, text in (("lab/code.py", "# the lab's code\n"), ("templates/card.yaml", "id: x\n"),
                       ("data/manifest.json", "{}\n"), ("requirements.txt", "pandas==3.0.6\n"),
                       (".gitignore", "*.csv\n*.pyc\n__pycache__/\n.run.pkl\n")):
        (root / name).parent.mkdir(parents=True, exist_ok=True)
        (root / name).write_text(text)
    commit(root, "the lab", "bank/DEMO-1.md", "lab/code.py", "templates/card.yaml", "data/manifest.json",
           "requirements.txt", ".gitignore")
    return root, new_strategy(root, "demo-01-momentum")


@pytest.fixture(scope="module")
def market():
    return synthetic_market(7)[0]


def trials_file(root):
    return root / "registry" / "trials.jsonl"


SNAPSHOT_HASH = "5a" * 32


def run(root, folder, market, crypto=frozenset()):
    return report.run(folder, market=market, snapshot="synthetic", snapshot_hash=SNAPSHOT_HASH,
                      registry_path=trials_file(root), lab=root, board=root / "STATUS.md", crypto=crypto,
                      cluster=CLUSTERS.get)


def attempt(folder, market):
    return report.try_strategy(folder, market, crypto=frozenset(), cluster=CLUSTERS.get)


def outputs(folder):
    book = nbformat.read(folder / "report.ipynb", as_version=4)
    return [o for c in book.cells if c.cell_type == "code" for o in c.outputs]


def test_the_chain_leaves_a_registry_line_a_notebook_and_a_row_on_the_board(lab, market):
    root, folder = lab
    head = git("rev-parse", "HEAD", cwd=root)
    verdict = run(root, folder, market)
    lines = registry.lines(trials_file(root))
    assert [line["variant"] for line in lines] == [0, 1]
    assert {line["card"] for line in lines} == {"demo-01-momentum"}
    assert lines[0]["card_hash"] == hashlib.sha256((folder / "card.yaml").read_bytes()).hexdigest()
    assert [line["parameters"] for line in lines] == [{"span": 20}, {"span": 40}]
    for line in lines:
        assert (line["commit"], line["snapshot"], line["thresholds"]) == (head, "synthetic", battery.THRESHOLDS)
        assert line["snapshot_hash"] == SNAPSHOT_HASH
        assert line["gates"] == {str(g.number): g.passed for g in verdict.gates}
        assert line["versions"]["pandas"] and line["versions"]["python"]
        ran = datetime.strptime(line["time"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        assert timedelta(0) <= datetime.now(timezone.utc) - ran < timedelta(hours=1)
    shown = outputs(folder)
    assert shown and not [o for o in shown if o.output_type == "error"]
    # exposure, equity, one chart for each of gates 1 to 6, and two for gate 7: its equity and its bootstrap
    assert sum("image/png" in o.get("data", {}) for o in shown) == 10
    headline = shown[0]["data"]["text/markdown"]
    assert (f"stops at gate {verdict.failed}" if verdict.failed else "passes gates 1 to 7") in headline
    said = [o["data"]["text/markdown"] for o in shown if "text/markdown" in o.get("data", {})]
    words = [text.split("**")[1] for text in said if text.startswith(("**Passes**:", "**Fails**:", "**Not computed**:"))]
    assert words == [{True: "Passes", False: "Fails", None: "Not computed"}[g.passed] for g in verdict.gates]
    tables = [o["data"]["text/html"] for o in shown if "text/html" in o.get("data", {})]
    assert any("variant 1" in t and "span" in t for t in tables)                     # the variants tried
    verdict_table = tables[-1]
    assert [verdict_table.count(f"<td>{word}</td>") for word in ("passes", "fails")] == [
        sum(g.passed is True for g in verdict.gates), sum(g.passed is False for g in verdict.gates)]
    assert not (folder / report.EVIDENCE).exists()
    drawn_by = nbformat.read(folder / "report.ipynb", as_version=4).metadata["alpha_lab"]["template"]
    assert drawn_by == git("log", "-1", "--format=%H", "--", "report.ipynb", cwd=report.TEMPLATE.parent)
    board = (root / "STATUS.md").read_text()
    assert "DEMO-1" in board and "demo-01-momentum" in board and "report.ipynb" in board


def test_a_second_card_counts_the_first_card_s_trials(lab, market):
    root, first = lab
    one = run(root, first, market)
    commit(root, "registry", "registry/trials.jsonl")
    before = trials_file(root).read_bytes()
    history = registry.history(trials_file(root))
    card_hash = hashlib.sha256((first / "card.yaml").read_bytes()).hexdigest()
    assert [t.key for t in history] == [f"demo-01-momentum/{k}@{card_hash[:12]}" for k in (0, 1)]
    for mine, theirs in zip(one.trials, history):
        mine = mine.monthly.dropna()
        assert list(theirs.monthly.index) == list(mine.index)                 # month ends, as the battery writes
        assert np.allclose(theirs.monthly.to_numpy(), mine.to_numpy(), atol=1e-6)
        assert theirs.survivor == (one.failed is None)
    two = run(root, new_strategy(root, "demo-02-momentum", span=24), market)
    assert two.gates[3].figures["trials"] == 4
    assert trials_file(root).read_bytes().startswith(before)


def test_a_holdout_is_opened_once(lab, market):
    root, _ = lab
    folder = new_strategy(root, "demo-03-broken", code=BROKEN)
    run(root, folder, market)
    commit(root, "registry", "registry/trials.jsonl")
    with pytest.raises(RuntimeError, match="opened once"):
        run(root, folder, market)


def test_a_strategy_that_cannot_run_still_leaves_its_lines_and_its_report(lab, market):
    root, _ = lab
    folder = new_strategy(root, "demo-03-broken", code=BROKEN)
    verdict = run(root, folder, market)
    assert verdict.failed == 1 and "cannot run: no signal yet" in verdict.gates[0].reason
    lines = registry.lines(trials_file(root))
    assert [(line["variant"], line["sharpe"], line["failed"]) for line in lines] == [(0, None, 1), (1, None, 1)]
    assert registry.history(trials_file(root)) == []                    # no returns: no trial for gate 4 to count
    assert not [o for o in outputs(folder) if o.output_type == "error"]
    said = json.dumps([o.get("data", {}) for o in outputs(folder)])
    assert "The strategy cannot run: there is no equity to draw." in said and "nothing was held" not in said


def test_runs_that_break_before_the_gates_leave_their_trials_and_a_report_that_says_so(lab, market, monkeypatch):
    root, _ = lab
    ident = "demo-38-chooser"
    folder = root / "strategies" / ident
    folder.mkdir(parents=True)
    (folder / "card.yaml").write_text(card(ident, 20) + "choose: true\n")
    commit(root, f"card: {ident}", f"strategies/{ident}/card.yaml")
    (folder / "strategy.py").write_text(STRATEGY)
    commit(root, f"strategy: {ident}", f"strategies/{ident}/strategy.py")

    def broken(legs, market, period):
        raise RuntimeError("no year to choose from")

    monkeypatch.setattr(battery, "walk_forward", broken)
    verdict = run(root, folder, market)
    assert all(g.reason == "cannot be computed: RuntimeError: no year to choose from" for g in verdict.gates)
    assert [line["sharpe"] is not None for line in registry.lines(trials_file(root))] == [True, True]
    assert len(registry.history(trials_file(root))) == 2                # both variants ran: gate 4 counts them
    said = json.dumps([o.get("data", {}) for o in outputs(folder)])
    assert "not evaluated: the runs every gate judges broke (RuntimeError: no year to choose from)" in said
    assert "The runs every gate judges broke: there is no equity to draw." in said and "nothing was held" not in said


def test_a_card_whose_id_already_ran_or_is_not_its_folder_s_is_refused(lab, market):
    root, _ = lab
    folder = new_strategy(root, "demo-03-broken", code=BROKEN)
    run(root, folder, market)
    commit(root, "registry", "registry/trials.jsonl")
    (folder / "card.yaml").write_text(card("demo-03-broken", 30))          # the same id, another hypothesis
    commit(root, "reworded", "strategies/demo-03-broken/card.yaml")
    with pytest.raises(RuntimeError, match="a card with this id already ran"):
        run(root, folder, market)
    copy = root / "strategies" / "demo-04-copy"
    copy.mkdir()
    (copy / "card.yaml").write_text(card("demo-03-broken", 20))
    with pytest.raises(RuntimeError, match="is not its folder's name"):
        run(root, copy, market)


def test_a_card_changed_after_its_lock_is_refused(lab, market):
    root, folder = lab
    path = folder / "card.yaml"
    path.write_text(path.read_text().replace("persist over a few weeks", "persist for a month"))
    with pytest.raises(RuntimeError, match="differs from its commit"):
        run(root, folder, market)
    commit(root, "reworded", "strategies/demo-01-momentum/card.yaml")
    with pytest.raises(RuntimeError, match="changed after the commit that locked it"):
        run(root, folder, market)


def test_a_card_is_committed_alone_and_before_its_code(lab, market):
    root, _ = lab
    loose = root / "strategies" / "demo-08-loose"
    loose.mkdir()
    (loose / "card.yaml").write_text(card("demo-08-loose", 20))
    with pytest.raises(RuntimeError, match="the card is not committed"):
        run(root, loose, market)
    together = root / "strategies" / "demo-05-together"
    together.mkdir()
    (together / "card.yaml").write_text(card("demo-05-together", 20))
    (together / "strategy.py").write_text(STRATEGY)
    commit(root, "both", "strategies/demo-05-together")
    with pytest.raises(RuntimeError, match="holds other files"):
        run(root, together, market)
    late = root / "strategies" / "demo-06-late"
    late.mkdir()
    (late / "strategy.py").write_text(STRATEGY)
    commit(root, "code first", "strategies/demo-06-late/strategy.py")
    (late / "card.yaml").write_text(card("demo-06-late", 20))
    commit(root, "card after", "strategies/demo-06-late/card.yaml")
    with pytest.raises(RuntimeError, match="the card comes first"):
        run(root, late, market)


def test_anything_uncommitted_is_refused(lab, market):
    root, folder = lab
    (folder / "strategy.py").write_text(STRATEGY + "\n# tuned\n")
    with pytest.raises(RuntimeError, match="uncommitted"):
        run(root, folder, market)
    git("checkout", "--", "strategies/demo-01-momentum/strategy.py", cwd=root)
    (folder / "reasoning.md").write_text("Why this theory now.\n")
    with pytest.raises(RuntimeError, match="uncommitted"):
        run(root, folder, market)
    commit(root, "reasoning", "strategies/demo-01-momentum/reasoning.md")
    (root / "lab" / "helper.py").write_text("# not committed\n")
    with pytest.raises(RuntimeError, match="uncommitted"):
        run(root, folder, market)


def test_registry_lines_are_committed_before_the_next_run(lab, market):
    root, _ = lab
    run(root, new_strategy(root, "demo-03-broken", code=BROKEN), market)
    with pytest.raises(RuntimeError, match="uncommitted"):
        run(root, new_strategy(root, "demo-07-next", code=BROKEN), market)


def test_the_seed_is_the_card_s_hash(lab, market, monkeypatch):
    root, folder = lab
    seen = {}

    def spy(card, strategy, market, history, seed, **options):
        seen["seed"] = seed
        raise RuntimeError("stop here")

    monkeypatch.setattr(battery, "run", spy)
    with pytest.raises(report.Recorded, match="the run stopped .RuntimeError: stop here.; the run is void"):
        run(root, folder, market)
    card_hash = hashlib.sha256((folder / "card.yaml").read_bytes()).hexdigest()
    assert seen["seed"] == int(card_hash[:8], 16)
    lines = registry.lines(trials_file(root))                           # the card was recorded before the battery
    assert [(line["card_hash"], line["variant"], line["sharpe"], line["void"]) for line in lines] == [
        (card_hash, k, None, "the run stopped (RuntimeError: stop here)") for k in (0, 1)]


def test_a_notebook_that_fails_keeps_the_run_s_data_and_runs_again(lab, market, monkeypatch):
    root, _ = lab
    folder = new_strategy(root, "demo-03-broken", code=BROKEN)

    def broken_kernel(notebook, **options):
        raise OSError("no kernel\n  and what follows it")

    monkeypatch.setattr(report, "execute", broken_kernel)
    with pytest.raises(report.Recorded, match="the card has run, and its notebook failed") as failed:
        run(root, folder, market)
    assert failed.value.verdict.card == "demo-03-broken"                # the verdict, to show: the run is recorded
    assert (folder / report.EVIDENCE).exists() and len(registry.lines(trials_file(root))) == 2
    assert "demo-03-broken" in (root / "STATUS.md").read_text()         # the board is written all the same
    assert "the notebook failed (OSError: no kernel)" in str(failed.value) and "follows" not in str(failed.value)
    assert "cannot be drawn" not in str(failed.value)                   # its data is there

    def failing_cell(notebook, **options):
        from nbclient.exceptions import CellExecutionError
        raise CellExecutionError("An error occurred while executing the following cell:\n...", "ValueError", "no data")

    monkeypatch.setattr(report, "execute", failing_cell)
    with pytest.raises(RuntimeError, match=r"the notebook failed \(CellExecutionError: ValueError: no data\)"):
        report.execute_notebook(folder)                                 # the cell's error, not the cell
    monkeypatch.undo()
    report.execute_notebook(folder)
    assert not (folder / report.EVIDENCE).exists() and outputs(folder)


@pytest.mark.parametrize("stop", [KeyboardInterrupt, SystemExit])
def test_a_notebook_interrupted_before_its_client_handles_it_says_so_and_the_board_is_written(lab, market, monkeypatch,
                                                                                               stop):
    root, _ = lab
    folder = new_strategy(root, "demo-03-broken", code=BROKEN)

    def interrupted(notebook, **options):                               # Ctrl-C before the kernel's client takes it
        raise stop

    monkeypatch.setattr(report, "execute", interrupted)
    try:
        with pytest.raises(report.Recorded, match=rf"its notebook was interrupted \({stop.__name__}\): run python -m "
                                                  r"lab.report --notebook strategies/demo-03-broken"):
            run(root, folder, market)
    except (KeyboardInterrupt, SystemExit):
        pytest.fail("the interrupt escaped the run")
    assert "demo-03-broken" in (root / "STATUS.md").read_text() and (folder / report.EVIDENCE).exists()
    monkeypatch.undo()
    report.execute_notebook(folder)
    assert not (folder / report.EVIDENCE).exists() and outputs(folder)


def test_a_second_interrupt_as_the_board_is_written_is_said_with_the_verdict(lab, market, monkeypatch):
    root, _ = lab
    folder = new_strategy(root, "demo-03-broken", code=BROKEN)

    def interrupted(*args, **options):
        raise KeyboardInterrupt

    monkeypatch.setattr(report, "execute", interrupted)
    monkeypatch.setattr(status, "write", interrupted)
    try:
        with pytest.raises(report.Recorded, match=r"its notebook was interrupted .*; the board was not written "
                                                  r"\(KeyboardInterrupt\): run python -m lab.status") as said:
            run(root, folder, market)
    except KeyboardInterrupt:
        pytest.fail("the second interrupt escaped the run")
    assert said.value.verdict.card == "demo-03-broken"


def test_a_second_interrupt_as_a_void_run_s_board_is_written_is_said(lab, market, monkeypatch):
    root, _ = lab
    folder = new_strategy(root, "demo-03-broken", code=BROKEN)

    def interrupted(*args, **options):
        raise KeyboardInterrupt

    monkeypatch.setattr(battery, "run", interrupted)                   # Ctrl-C in the battery, then at the board
    monkeypatch.setattr(status, "write", interrupted)
    try:
        with pytest.raises(report.Recorded, match=r"the run is void, .*; the board was not written "
                                                  r"\(KeyboardInterrupt\): run python -m lab.status"):
            run(root, folder, market)
    except KeyboardInterrupt:
        pytest.fail("the second interrupt escaped the run")


@pytest.mark.parametrize("sent", ["SIGINT", "SIGTERM"])
def test_the_run_s_data_is_written_whole_whatever_interrupts_it(lab, market, monkeypatch, sent):
    root, _ = lab
    folder = new_strategy(root, "demo-03-broken", code=BROKEN)
    dump = pickle.dump

    def interrupted(data, handle):
        if handle.name.endswith(report.EVIDENCE + ".part"):
            os.kill(os.getpid(), getattr(signal, sent))                 # Ctrl-C or SIGTERM as the data is written
        dump(data, handle)

    def stopped(number, frame):                                         # SIGTERM, stopping this process's test only
        raise KeyboardInterrupt

    monkeypatch.setattr(pickle, "dump", interrupted)
    kept = {number: signal.signal(number, handler) for number, handler in (   # SIGINT is ignored in a shell's background
        (signal.SIGINT, signal.default_int_handler), (signal.SIGTERM, stopped))}
    try:
        with pytest.raises(report.Recorded, match="its notebook was interrupted"):
            run(root, folder, market)
    except KeyboardInterrupt:
        pytest.fail("the interrupt escaped the run")
    finally:
        for number, handler in kept.items():
            signal.signal(number, handler)
    assert pickle.loads((folder / report.EVIDENCE).read_bytes())["card"]["id"] == "demo-03-broken"
    assert not (folder / (report.EVIDENCE + ".part")).exists()


@pytest.mark.parametrize("stop, said", [(OSError(28, "No space left on device"), r"its notebook failed \(OSError: .*\): "
                                         "its data was not written, and its report cannot be drawn"),
                                        (KeyboardInterrupt(), "its data was not written, and its report cannot be drawn")])
def test_data_that_could_not_be_written_leaves_no_part_and_says_what_is_left(lab, market, monkeypatch, stop, said):
    root, _ = lab
    folder = new_strategy(root, "demo-03-broken", code=BROKEN)
    dump = pickle.dump

    def full(data, handle):
        if handle.name.endswith(report.EVIDENCE + ".part"):
            handle.write(b"partial")
            raise stop
        dump(data, handle)

    monkeypatch.setattr(pickle, "dump", full)
    try:
        with pytest.raises(report.Recorded, match=said):
            run(root, folder, market)
    except KeyboardInterrupt:
        pytest.fail("the interrupt escaped the run")
    assert not (folder / report.EVIDENCE).exists() and not (folder / (report.EVIDENCE + ".part")).exists()


def test_a_failed_notebook_tells_the_first_line_that_says_something():
    assert report.told("first\nsecond") == "first"
    assert report.told("\n  \nsaid late\n") == "said late"
    assert report.told("") == "" and report.told("", "AssertionError") == "AssertionError"
    assert report.told("\nno data", "ValueError") == "ValueError: no data"
    assert report.told("x" * 500) == "x" * 197 + "..."


def test_a_card_that_is_not_a_mapping_is_refused(lab, market):
    root, folder = lab
    (folder / "card.yaml").write_text("- id\n- theory\n")
    with pytest.raises(RuntimeError, match="a card is a mapping of fields"):
        report.read_card(folder, tickers=list(market.prices.columns))


@pytest.mark.parametrize("change, message", [
    (("  - {span: 20}\n", "  - {span: 20, since: 2008-01-01}\n"), "numbers, text or lists"),
    (("universe: [S1", "universe: [ZZZ, S1"), "outside the lab's universe: ZZZ"),
    (("universe: [S1, S2, S3, S4, S5, S6, S7, S8]", "universe: [S1, S2, S3]"), "4 assets at least"),
    (("neighbours:\n  span: {25: [15, 25], 50: [10, 30]}\n", ""), "neighbours of 'span'"),
    (("50: [10, 30]", "50: [9, 30]"), "neighbours of 'span' at ±50%"),
    (("  span: {25: [15, 25], 50: [10, 30]}\n", "  span: [15, 25, 10, 30]\n"), "neighbours not in the template's form"),
    (("  - {span: 40}\n", "  - {spna: 40}\n"), "the base's parameters"),
    (("refuted_if:", "splits: {in_sample: [2005-01-01, 2025-06-30], holdout: [2025-07-01, 2025-12-31]}\nrefuted_if:"),
     "holdout is 2023-01-01 to 2025-12-31"),
    (("refuted_if:", "splits: {in_sample: [2005-01-01, 2015-12-31], holdout: [2023-01-01, 2025-12-31]}\nrefuted_if:"),
     "ends on 2022-12-31"),
    (("refuted_if:", "splits: [2005-01-01, 2022-12-31]\nrefuted_if:"), "splits not in the template's form"),
    (("refuted_if:", "splits: {in_sample: [2010, 2022-12-31], holdout: [2023-01-01, 2025-12-31]}\nrefuted_if:"),
     "splits not in the template's form"),
    (("50: [10, 30]", "50: [ten, thirty]"), "neighbours not in the template's form"),
    (("id: demo-01-momentum", "id: [demo-01-momentum"), "not YAML"),
    (("id: demo-01-momentum", "id: demo-99-other"), "is not its folder's name"),
    (("universe: [S1", "universe: [[S1], S1"), "card.yaml: universe not in the template's form"),
    (("  - {span: 40}\n", "  - 40\n"), "card.yaml: variants not in the template's form"),
    (("span: {25: [15, 25]", "span: {~: [15, 25]"), r"card.yaml: int\(\) argument"),
])
def test_a_card_that_breaks_a_rule_is_refused_before_anything_runs(lab, market, change, message):
    root, folder = lab
    old, new = change
    text = (folder / "card.yaml").read_text()
    assert old in text
    (folder / "card.yaml").write_text(text.replace(old, new, 1))
    with pytest.raises(RuntimeError, match=message):
        report.read_card(folder, tickers=list(market.prices.columns))


def test_neighbours_move_a_numeric_parameter_only(lab, market):
    root, folder = lab
    text = (folder / "card.yaml").read_text()
    text = text.replace("  - {span: 20}\n  - {span: 40}\n", "  - {span: 20, how: fast}\n  - {span: 40, how: fast}\n")
    (folder / "card.yaml").write_text(text.replace("neighbours:\n", "neighbours:\n  how: {25: [1, 2], 50: [0, 3]}\n"))
    with pytest.raises(RuntimeError, match="card.yaml: neighbours move a numeric parameter of the base variant, "
                                           "and 'how' is not one"):
        report.read_card(folder, tickers=list(market.prices.columns))


def test_trying_a_strategy_checks_its_targets_and_shows_no_returns(lab, market):
    root, folder = lab
    tried = attempt(folder, market)
    assert tried["holds an asset"] and tried["look-ahead breaks"] == 0 and tried["same-day breaks"] == 0
    assert tried["dates checked"] == 2 * 2 * battery.CHECKED_DATES                 # both variants, both kinds of day
    assert tried["neighbours timed"] == 4 and tried["neighbour dates checked"] == 4 * 2 * battery.HOLDOUT_CHECKED_DATES
    assert tried["neighbour look-ahead breaks"] == 0 and tried["neighbour same-day breaks"] == 0
    assert tried["blocks of gate 5 after the first target"] == len(battery.BLOCKS) and "warning" not in tried
    assert tried["neighbours that hold the base"] == []
    assert not {"Sharpe", "alpha", "returns"} & set(tried)
    assert not trials_file(root).exists()


def test_trying_a_strategy_that_first_holds_too_late_for_gate_5_warns(lab, market):
    root, _ = lab
    late = STRATEGY.replace("    every = ", '    weights.loc[:"2015-12-31"] = 0.0\n    every = ')
    tried = attempt(new_strategy(root, "demo-35-late", code=late), market)
    assert tried["from"] >= "2016-01-01" and tried["blocks of gate 5 after the first target"] == 2
    assert "gate 5 needs 3: it would fail whatever the edge" in tried["warning"]


def test_trying_a_strategy_warns_of_neighbours_that_set_the_base_s_targets(lab, market):
    root, _ = lab
    coarse = STRATEGY.replace("pct_change(span)", "pct_change(10 * round(span / 10))")    # 15 and 25 read 20
    tried = attempt(new_strategy(root, "demo-58-coarse", code=coarse), market)
    assert tried["neighbours that hold the base"] == ["span=15", "span=25"]
    assert "span=15, span=25 set the base's targets on every session from its first holding" in tried["warning"]


def test_trying_a_strategy_judges_its_neighbours_from_the_base_s_first_holding(lab, market):
    root, _ = lab
    early = STRATEGY.replace("pct_change(span)", "pct_change(20)").replace(
        "    return weights.where(every, axis=0)\n",
        "    out = weights.where(every, axis=0)\n    out.iloc[:40] = float('nan')\n"
        "    out.iloc[span] = 0.0                    # no holding, before the first\n    return out\n")
    tried = attempt(new_strategy(root, "demo-67-early", code=early), market)
    assert tried["neighbours that hold the base"] == ["span=15", "span=25", "span=10", "span=30"]


def test_trying_a_strategy_judges_its_neighbours_on_every_session_from_the_first_holding(lab, market):
    """Neighbours that differ from the base by 0.005% on its first holding (15, 10) or on the last
    in-sample session (25, 30) move it, as gate 6 judges them."""
    root, _ = lab
    last = market.prices.index[market.prices.index <= battery.IN_SAMPLE[1]][-1].date()
    edges = STRATEGY.replace("pct_change(span)", "pct_change(20)").replace(
        "    return weights.where(every, axis=0)\n",
        "    out = weights.where(every, axis=0)\n    out.iloc[:40] = float('nan')\n"
        f"    end = out.index.get_indexer([pd.Timestamp('{last}')])[0]\n"
        "    if end >= 0:\n        out.iloc[end] = weights.iloc[end] * (1 - 5e-5 * (span > 20))\n"
        "    out.iloc[40] = weights.iloc[40] * (1 - 5e-5 * (span < 20))\n    return out\n")
    tried = attempt(new_strategy(root, "demo-72-edges", code=edges), market)
    assert tried["from"] == str(market.prices.index[market.prices.index >= "2005-01-01"][40].date())
    assert tried["neighbours that hold the base"] == []


def test_trying_a_strategy_judges_its_neighbours_from_the_base_s_own_first_holding(lab, market):
    """From the base variant's first holding, not a neighbour's nor another variant's: a neighbour
    that holds five sessions earlier, then sets the base's targets, holds the base (15); one that
    goes to cash for a session where the base holds (25), sets again the base's target where the
    base lets its weights drift (10), or sets four sessions early the base's next target (30), moves
    it; the second variant first holds twenty sessions later."""
    root, _ = lab
    starts = STRATEGY.replace("pct_change(span)", "pct_change(20)").replace(
        "    return weights.where(every, axis=0)\n",
        "    out = weights.where(every, axis=0)\n    out.iloc[:60 if span == 40 else 40] = float('nan')\n"
        "    if span == 15:\n        out.iloc[35] = weights.iloc[35]\n"
        "    if span == 25:\n        out.iloc[41] = 0.0\n"
        "    if span == 10:\n        out.iloc[41] = out.iloc[40]\n"
        "    if span == 30:\n        out.iloc[41] = weights.iloc[45]\n    return out\n")
    tried = attempt(new_strategy(root, "demo-73-starts", code=starts), market)
    assert tried["from"] == str(market.prices.index[market.prices.index >= "2005-01-01"][40].date())
    assert tried["neighbours that hold the base"] == ["span=15"]


@pytest.mark.parametrize("line", ["out.iloc[41] = weights.iloc[42]", "out.iloc[41] = out.iloc[40]"])
def test_trying_a_base_that_resets_every_other_session_moves_a_neighbour_that_sets_a_target_between(lab, market, line):
    """A neighbour that sets, on the session between two of the base's, its next target or its last
    one again trades otherwise: it moves the strategy."""
    root, _ = lab
    code = STRATEGY.replace("pct_change(span)", "pct_change(20)").replace("% 5 == 0", "% 2 == 0").replace(
        "    return weights.where(every, axis=0)\n",
        "    out = weights.where(every, axis=0)\n    out.iloc[:40] = float('nan')\n"
        f"    if span not in (20, 40):\n        {line}\n    return out\n")
    tried = attempt(new_strategy(root, f"demo-9{len(line) % 7}-between", code=code), market)
    assert tried["neighbours that hold the base"] == []


def test_trying_a_strategy_keeps_every_warning(lab, market):
    root, _ = lab
    both = STRATEGY.replace("pct_change(span)", "pct_change(10 * round(span / 10))").replace(
        "    every = ", '    weights.loc[:"2015-12-31"] = 0.0\n    every = ')
    tried = attempt(new_strategy(root, "demo-66-both", code=both), market)
    late, coarse = tried["warning"].split("; ")
    assert "gate 5 needs 3: it would fail whatever the edge" in late
    assert coarse.startswith("span=15, span=25 set the base's targets on every session from its first holding")


def test_trying_a_strategy_counts_a_block_of_exactly_126_sessions(lab, market):
    root, _ = lab
    first = market.prices.loc["2010":"2014"].index[-battery.MIN_BLOCK_SESSIONS - 1]   # 126 sessions after it
    before = (first - pd.Timedelta(days=1)).date()
    exact = STRATEGY.replace("    every = ", f'    weights.loc[:"{before}"] = 0.0\n    every = ').replace("% 5 == 0", "% 1 == 0")
    tried = attempt(new_strategy(root, "demo-39-exact", code=exact), market)
    assert tried["from"] == str(first.date()) and tried["blocks of gate 5 after the first target"] == 3
    assert "warning" not in tried


def test_trying_a_strategy_runs_every_neighbour_and_never_the_holdout(lab, market):
    root, _ = lab
    sealed = STRATEGY.replace("def positions(market, span):\n",
                              "def positions(market, span):\n"
                              "    if market.prices.index[-1] > pd.Timestamp('2022-12-31'):\n"
                              "        raise ValueError('the holdout')\n")
    assert attempt(new_strategy(root, "demo-09-sealed", code=sealed), market)["holds an asset"]
    fussy = STRATEGY.replace("def positions(market, span):\n",
                             "def positions(market, span):\n    if span < 12:\n        raise ValueError('too short')\n")
    with pytest.raises(ValueError, match="too short"):                   # a ±50% neighbour, 10 sessions
        attempt(new_strategy(root, "demo-10-fussy", code=fussy), market)


def test_trying_a_strategy_times_every_neighbour(lab, market):
    root, _ = lab
    peeks = STRATEGY.replace(".shift(1) > 0)", ".shift(1 if span != 30 else -1) > 0)")    # the ±50% neighbour reads tomorrow
    tried = attempt(new_strategy(root, "demo-37-peek", code=peeks), market)
    assert tried["look-ahead breaks"] == 0 and tried["neighbour look-ahead breaks"] > 0
    bar = STRATEGY.replace(".shift(1) > 0)", ".shift(1 if span != 30 else 0) > 0)")    # it reads the bar it trades on
    tried = attempt(new_strategy(root, "demo-57-bar", code=bar), market)
    assert tried["same-day breaks"] == 0 and tried["neighbour same-day breaks"] > 0


@pytest.mark.parametrize("ident, where", [("demo-32-variant", "span == 40"), ("demo-33-neighbour", "span == 30")])
def test_trying_a_strategy_checks_every_variant_and_neighbour_s_targets(lab, market, ident, where):
    root, _ = lab
    doubled = STRATEGY.replace("    return weights.where(every, axis=0)",
                               f"    weights = weights * 2 if {where} else weights\n    return weights.where(every, axis=0)")
    with pytest.raises(ValueError):
        attempt(new_strategy(root, ident, code=doubled), market)


def test_trying_a_strategy_runs_it_on_gate_6_s_smaller_markets(lab, market):
    root, _ = lab
    reads = STRATEGY.replace(FIRST_LINE, FIRST_LINE + "    market.signal_prices['S1']\n")
    attempt(new_strategy(root, "demo-33-reads", code=reads), market)          # a cluster left out is still read
    needy = STRATEGY.replace(FIRST_LINE, FIRST_LINE + "    assert market.tradable['S1'].any()\n")
    with pytest.raises(AssertionError):                                        # but it is never tradable
        attempt(new_strategy(root, "demo-34-needy", code=needy), market)


def test_trying_a_card_that_holds_bitcoin_runs_its_strategy_without_bitcoin(lab):
    root, _ = lab
    market, _ = synthetic_market(9, coin=True)
    needy = STRATEGY.replace(FIRST_LINE, FIRST_LINE + "    market.signal_prices['COIN']\n")
    folder = new_strategy(root, "demo-36-coin", code=needy, universe=(*EIGHT, "COIN"))
    with pytest.raises(KeyError, match="COIN"):                          # one cluster: only bitcoin is left out
        report.try_strategy(folder, market, crypto=frozenset({"COIN"}), cluster=lambda ticker: "all")


def test_a_reason_keeps_no_path_of_the_machine(tmp_path):
    lab = tmp_path / "repo" / "alpha-lab"
    reason = f"the strategy cannot run: [Errno 2] No such file: '{lab}/strategies/x/signal.csv' in {Path.home()}/data"
    assert report.clean(reason, lab) == ("the strategy cannot run: [Errno 2] No such file: "
                                         "'alpha-lab/strategies/x/signal.csv' in ~/data")


def test_the_lab_s_registry_only_grows():
    """The lab's registry holds every line any committed version of it held."""
    assert registry.dropped() == []


def registry_repository(root):
    git("init", "-q", cwd=root)
    git("config", "user.name", "lab", cwd=root)
    git("config", "user.email", "lab@example.invalid", cwd=root)
    path = root / "registry" / "trials.jsonl"
    path.parent.mkdir()
    return path


def full(**fields):
    """A registry line: every field the lab reads, those given and the rest as a run without returns
    writes them."""
    return {"time": "2026-01-01T00:00:00Z", "card": "x", "card_hash": "0" * 64, "variant": 0, "sharpe": None,
            "monthly": {}, "gates": {}, "failed": None, "survivor": False, **fields}


def held(*keys):
    """A registry holding a line for each card named."""
    return "".join(one(key) + "\n" for key in keys)


def one(key):
    return registry.compact(full(card=key, card_hash=key))


def test_a_line_a_commit_held_and_the_file_lacks_is_found(tmp_path):
    path = registry_repository(tmp_path)
    for text in (held("a"), held("a", "b"), held("b"), held("b", "c")):   # grows, loses a line, grows
        path.write_text(text)
        commit(tmp_path, "registry", "registry/trials.jsonl")
    assert registry.dropped(path) == [one("a")]
    path.write_text(held("b", "c", "a"))                                   # put back at the end: whole
    assert registry.dropped(path) == []
    path.write_text(held("b", "x", "a"))                                   # a line edited in place, same length
    assert registry.dropped(path) == [one("c")]
    path.write_text(held("b", "c"))
    assert registry.restore(path) == [one("a")] and path.read_text() == held("b", "c", "a")


def test_a_registry_restored_or_merged_whole_lacks_nothing(tmp_path):
    path = registry_repository(tmp_path)
    main = lambda: git("symbolic-ref", "--short", "HEAD", cwd=tmp_path)
    path.write_text(held("a"))
    commit(tmp_path, "registry", "registry/trials.jsonl")
    first, trunk = git("rev-parse", "HEAD", cwd=tmp_path), main()
    path.write_text("")
    commit(tmp_path, "rewritten", "registry/trials.jsonl")
    assert registry.dropped(path) == [one("a")]
    git("checkout", "-q", first, "--", "registry/trials.jsonl", cwd=tmp_path)
    commit(tmp_path, "restored", "registry/trials.jsonl")
    assert registry.dropped(path) == []                                  # restored: a rewrite in its past is no matter
    git("checkout", "-q", "-b", "side", cwd=tmp_path)
    path.write_text(held("a", "b"))
    commit(tmp_path, "a run on a side branch", "registry/trials.jsonl")
    git("checkout", "-q", trunk, cwd=tmp_path)
    path.write_text(held("a", "c"))
    commit(tmp_path, "a run on the trunk", "registry/trials.jsonl")
    subprocess.run(["git", "merge", "-q", "side"], cwd=tmp_path, capture_output=True)
    path.write_text(held("a", "c", "b"))                                   # both runs kept
    commit(tmp_path, "merged", "registry/trials.jsonl")
    assert registry.dropped(path) == []
    git("checkout", "-q", "-b", "other", "HEAD~1", cwd=tmp_path)         # the trunk before the merge
    git("checkout", "-q", "-b", "more", "side", cwd=tmp_path)
    path.write_text(held("a", "b", "d"))
    commit(tmp_path, "another side run", "registry/trials.jsonl")
    git("checkout", "-q", "other", cwd=tmp_path)
    subprocess.run(["git", "merge", "-q", "more"], cwd=tmp_path, capture_output=True)
    path.write_text(held("a", "c"))                                        # a merge that keeps one side only
    commit(tmp_path, "merged, one side", "registry/trials.jsonl")
    assert registry.dropped(path) == [one("b"), one("d")]


def test_the_board_links_the_reason_a_theory_is_not_testable(tmp_path):
    (tmp_path / "bank").mkdir()
    for ident, state in (("T-3", "not-testable"), ("T-4", "in-progress")):
        (tmp_path / "bank" / f"{ident}.md").write_text(f"---\nid: {ident}\ntitle: t\nfamily: f\nstatus: {state}\n---\n")
    for name in ("T-3-01-d", "T-4-01-e"):
        (tmp_path / "strategies" / name).mkdir(parents=True)
        (tmp_path / "strategies" / name / "reasoning.md").write_text("Why.\n")
    (tmp_path / "trials.jsonl").write_text("")
    board = status.render(tmp_path, tmp_path / "trials.jsonl")
    assert "| not-testable | [T-3-01-d](strategies/T-3-01-d/) · not testable: [reasoning](strategies/T-3-01-d/reasoning.md) |" in board
    assert "[T-4-01-e](strategies/T-4-01-e/) · no card: [reasoning](strategies/T-4-01-e/reasoning.md)" in board
    assert "**0 strategies**" in board                                    # a reasoning without a card is no strategy


def test_the_board_lists_every_theory_every_outcome_and_every_orphan(tmp_path):
    (tmp_path / "bank").mkdir()
    for ident, state in (("T-1", "untouched"), ("T-2", "not-testable")):
        (tmp_path / "bank" / f"{ident}.md").write_text(f"---\nid: {ident}\ntitle: t\nfamily: f\nstatus: {state}\n---\n")
    for name, theory in (("t-1-01-a", "T-1"), ("x-9-01-b", "X-9"), ("t-2-01-c", "T-2")):
        (tmp_path / "strategies" / name).mkdir(parents=True)
        (tmp_path / "strategies" / name / "card.yaml").write_text(f"id: {name}\ntheory: {theory}\n")
    (tmp_path / "strategies" / "t-1-01-a" / "verdict.md").write_text("Stops at gate 2.\n")
    hashes = {name: hashlib.sha256((tmp_path / "strategies" / name / "card.yaml").read_bytes()).hexdigest()
              for name in ("t-1-01-a", "x-9-01-b")}
    lines = [full(**line) for line in [{"card": "t-1-01-a", "card_hash": hashes["t-1-01-a"], "failed": 2, "survivor": False, "time": "2026-01-01T00:00:00Z"},
             {"card": "x-9-01-b", "card_hash": hashes["x-9-01-b"], "failed": None, "survivor": True, "time": "2026-01-02T00:00:00Z"},
             {"card": "gone-01", "card_hash": "0" * 64, "failed": 4, "survivor": False, "time": "2026-01-03T00:00:00Z"}]]
    (tmp_path / "trials.jsonl").write_text("".join(json.dumps(line) + "\n" for line in lines))
    board = status.render(tmp_path, tmp_path / "trials.jsonl")
    assert "**2 theories**: 1 untouched" in board and "1 not-testable" in board
    assert board.count("| [T-") == 2 and "| [T-2](bank/T-2.md) t | f | not-testable |" in board
    assert "**3 strategies**: 1 passing gates 1 to 7, 1 stopped at gate 2, 1 not run yet." in board
    assert "stops at gate 2" in board and "[verdict](strategies/t-1-01-a/verdict.md)" in board
    assert "Strategies whose theory is not in the bank:" in board and "x-9-01-b" in board.split("not in the bank:")[1]
    assert "gone-01, run on 2026-01-03" in board
    edited = tmp_path / "strategies" / "t-1-01-a" / "card.yaml"
    ran = edited.read_text()
    edited.write_text(ran.replace("id: t-1-01-a", "id: t-1-01-z") + "horizon: weeks\n")
    (tmp_path / "strategies" / "x-9-01-b" / ".run.pkl").write_bytes(b"")
    (tmp_path / "strategies" / "x-9-01-b" / "report.ipynb").write_text("{}")
    board = status.render(tmp_path, tmp_path / "trials.jsonl")
    assert "[t-1-01-a](strategies/t-1-01-a/) · stops at gate 2 (its card was edited after the run)" in board
    assert "t-1-01-a, run on" not in board                              # its folder is still there
    assert "report not yet drawn" in board and "x-9-01-b/report.ipynb" not in board
    copied = tmp_path / "strategies" / "t-1-02-copy"
    copied.mkdir()
    (copied / "card.yaml").write_text(ran)                              # the card that ran, in a folder of its own
    board = status.render(tmp_path, tmp_path / "trials.jsonl")
    assert "[t-1-02-copy](strategies/t-1-02-copy/) · stops at gate 2 (run as t-1-01-a, the folder's name then)" in board
    assert "[t-1-01-a](strategies/t-1-01-a/) · not run yet" in board   # the name, used again by another card
    assert "**4 strategies**: 1 passing gates 1 to 7, 1 stopped at gate 2, 2 not run yet." in board
    edited.write_text(ran)                                              # the source still holds it: a copy
    board = status.render(tmp_path, tmp_path / "trials.jsonl")
    assert "[t-1-01-a](strategies/t-1-01-a/) · stops at gate 2 ·" in board
    assert "[t-1-02-copy](strategies/t-1-02-copy/) · not run yet" in board          # named by its folder


def test_the_board_shows_void_runs_renamed_folders_and_cards_it_cannot_read(tmp_path):
    (tmp_path / "bank").mkdir()
    (tmp_path / "bank" / "T-1.md").write_text("---\nid: T-1\ntitle: t\nfamily: f\nstatus: in-progress\n---\n")
    cards = {"t-1-01-void": "id: t-1-01-void\ntheory: T-1\n", "t-1-02-renamed": "id: t-1-02-old\ntheory: T-1\n",
             "t-1-03-broken": "id: [t-1-03\n", "t-1-04-list": "- id\n- theory\n"}
    for name, text in cards.items():
        (tmp_path / "strategies" / name).mkdir(parents=True)
        (tmp_path / "strategies" / name / "card.yaml").write_text(text)
    digest = {name: hashlib.sha256(text.encode()).hexdigest() for name, text in cards.items()}
    lines = [full(**line) for line in [{"card": "t-1-01-void", "card_hash": digest["t-1-01-void"], "failed": None, "survivor": False,
              "void": registry.LOST, "time": "2026-01-01T00:00:00Z"},
             {"card": "t-1-02-old", "card_hash": digest["t-1-02-renamed"], "failed": 3, "survivor": False,
              "time": "2026-01-02T00:00:00Z"}]]
    (tmp_path / "trials.jsonl").write_text("".join(json.dumps(line) + "\n" for line in lines))
    board = status.render(tmp_path, tmp_path / "trials.jsonl")
    assert f"[t-1-01-void](strategies/t-1-01-void/) · void: {registry.LOST}" in board
    assert "[t-1-02-renamed](strategies/t-1-02-renamed/) · stops at gate 3 (run as t-1-02-old" in board
    assert "t-1-02-old, run on" not in board                            # renamed, not gone
    assert "[t-1-03-broken](strategies/t-1-03-broken/) · not run yet" in board
    assert "[t-1-04-list](strategies/t-1-04-list/) · not run yet" in board
    assert "**4 strategies**: 0 passing gates 1 to 7, 1 stopped at gate 3, 1 void, 2 not run yet." in board
    (tmp_path / "strategies" / "t-1-02-old").mkdir()                    # the folder it ran in is back: a copy
    (tmp_path / "strategies" / "t-1-02-old" / "card.yaml").write_text(cards["t-1-02-renamed"])
    board = status.render(tmp_path, tmp_path / "trials.jsonl")
    assert "[t-1-02-renamed](strategies/t-1-02-renamed/) · not run yet" in board
    assert "[t-1-02-old](strategies/t-1-02-old/) · stops at gate 3" in board and board.count("stops at gate 3") == 1


def test_libraries_other_than_their_pins_are_refused(tmp_path, monkeypatch):
    pins = tmp_path / "requirements.txt"
    pins.write_text("# the lab's libraries\npandas==0.0.1\n")
    monkeypatch.setattr(report, "REQUIREMENTS", pins)
    with pytest.raises(RuntimeError, match=r"pandas .* \(pinned 0\.0\.1\)"):
        report.pinned_versions()


def test_the_registry_gives_back_a_survivor_as_gates_4_and_6_read_it(tmp_path):
    line = {"time": "2026-01-02T00:00:00Z", "card": "x-01-a", "card_hash": "ab" * 32, "variant": 1,
            "sharpe": 0.8, "monthly": {"2020-01": 0.01, "2020-02": -0.02}, "failed": None, "survivor": True}
    (tmp_path / "trials.jsonl").write_text(json.dumps(line) + "\n")
    (trial,) = registry.history(tmp_path / "trials.jsonl")
    assert (trial.key, trial.sharpe, trial.survivor) == ("x-01-a/1@abababababab", 0.8, True)
    assert [d.strftime("%Y-%m-%d") for d in trial.monthly.index] == ["2020-01-31", "2020-02-29"]


def test_a_card_is_checked_against_the_registry_before_its_lock(lab, market):
    root, folder = lab
    run(root, folder, market)
    commit(root, "registry", "registry/trials.jsonl")
    with pytest.raises(RuntimeError, match="opened once"):
        report.check_card(folder, list(market.prices.columns), trials_file(root))
    elsewhere = root / "drafts" / "demo-11-draft"
    elsewhere.mkdir(parents=True)
    (elsewhere / "card.yaml").write_text(card("demo-11-draft", 20))
    with pytest.raises(RuntimeError, match="lies in strategies/"):
        report.read_card(elsewhere, list(market.prices.columns))
    nested = root / "drafts" / "strategies" / "demo-24-nested"
    nested.mkdir(parents=True)
    (nested / "card.yaml").write_text(card("demo-24-nested", 20))
    with pytest.raises(RuntimeError, match="lies in the lab's own strategies/"):
        report.check_card(nested, list(market.prices.columns), trials_file(root))


def test_a_card_is_checked_before_its_code_is_written(lab):
    root, _ = lab
    folder = root / "strategies" / "demo-26-early"
    folder.mkdir()
    (folder / "card.yaml").write_text(card("demo-26-early", 20))
    (folder / "reasoning.md").write_text("why\n")
    (folder / ".DS_Store").write_text("")
    assert report.drafted(folder) == []                                # the reasoning comes before the card
    (folder / "strategy.py").write_text(STRATEGY)
    (folder / "build-plan.md").write_text("plan\n")
    assert report.drafted(folder) == ["build-plan.md", "strategy.py"]  # written before the lock
    commit(root, "card", "strategies/demo-26-early/card.yaml")
    assert report.drafted(folder) == []                                # after it, as the runbook says


def test_a_run_whose_lines_were_stashed_still_opened_its_holdout(lab, market):
    root, folder = lab
    run(root, folder, market)
    card_hash = hashlib.sha256((folder / "card.yaml").read_bytes()).hexdigest()
    git("stash", "-u", cwd=root)                  # the registry, the notebook and the board put aside
    assert not trials_file(root).exists()
    assert registry.opened(card_hash, trials_file(root)) is not None
    other = new_strategy(root, "demo-25-other")
    for folder_ in (folder, other):               # gate 4 would count too few trials: nothing runs
        with pytest.raises(RuntimeError, match="put them back"):
            run(root, folder_, market)
    git("stash", "pop", cwd=root)
    commit(root, "registry", "registry/trials.jsonl")
    with pytest.raises(RuntimeError, match="opened once"):
        run(root, folder, market)
    assert run(root, other, market).card == "demo-25-other"


def test_a_card_is_opened_by_its_lines_or_by_the_clone_s_record(lab, market, tmp_path):
    root, folder = lab
    run(root, folder, market)
    commit(root, "registry", "registry/trials.jsonl")
    first = hashlib.sha256((folder / "card.yaml").read_bytes()).hexdigest()
    later = new_strategy(root, "demo-26-later")
    run(root, later, market)
    second = hashlib.sha256((later / "card.yaml").read_bytes()).hexdigest()
    git("stash", "-u", cwd=root)                  # the file keeps the first card's lines only
    assert registry.opened(second, trials_file(root)) is not None and registry.missing(trials_file(root)) == [second]
    git("stash", "pop", cwd=root)
    commit(root, "registry", "registry/trials.jsonl")
    clone = tmp_path / "fresh"
    git("clone", "-q", str(root.parent), str(clone), cwd=tmp_path)       # the repository, whose subfolder is the lab
    path = clone / root.name / "registry" / "trials.jsonl"
    assert registry.recorded(path) == [] and registry.missing(path) == []
    assert registry.opened(first, path) is not None and registry.opened(second, path) is not None
    assert registry.opened("0" * 64, path) is None


def test_the_record_is_shared_by_the_clone_s_worktrees(lab, market, tmp_path):
    root, folder = lab
    run(root, folder, market)                     # its lines left uncommitted
    git("worktree", "add", "-q", str(tmp_path / "other"), cwd=root)
    other = tmp_path / "other" / root.name
    assert registry.marker(other / "registry" / "trials.jsonl") == registry.marker(trials_file(root))
    with pytest.raises(RuntimeError, match="put them back"):
        run(other, other / "strategies" / "demo-01-momentum", market)


def test_a_registry_that_lost_a_committed_line_stops_every_run_until_it_is_restored(lab, market, capsys):
    root, folder = lab
    run(root, folder, market)
    commit(root, "registry", "registry/trials.jsonl")
    kept = trials_file(root).read_text().splitlines(keepends=True)
    trials_file(root).write_text("".join(kept[1:]))
    commit(root, "a line dropped", "registry/trials.jsonl")
    later = new_strategy(root, "demo-27-next")
    for attempted in (lambda: run(root, later, market), lambda: report.check_card(later, list(market.prices.columns),
                                                                                  trials_file(root))):
        with pytest.raises(RuntimeError, match="lacks 1 line that a commit of it held.*lab.registry restore"):
            attempted()
    assert registry.main(["restore"], trials_file(root)) == 0
    assert capsys.readouterr().out.startswith("1 line put back")
    commit(root, "restored", "registry/trials.jsonl")
    assert run(root, later, market).card == "demo-27-next"


@pytest.mark.parametrize("name", ["signal.csv", "inputs/signal.csv", "__pycache__/span.txt", "inputs/.run.pkl", ".run.pkl",
                                  "signal.pyc", "__pycache__/strategy.cpython-314.pyc",
                                  "inputs/__pycache__/span.cpython-314.pyc"])
def test_files_git_ignores_are_refused_at_any_depth(lab, market, name):
    root, folder = lab
    (folder / name).parent.mkdir(parents=True, exist_ok=True)
    (folder / name).write_text("20\n")
    with pytest.raises(RuntimeError, match="git ignores"):
        run(root, folder, market)


def test_the_lab_s_compiled_files_are_the_only_ignored_ones_kept(lab, market):
    root, folder = lab
    (root / "lab" / "__pycache__").mkdir()
    (root / "lab" / "__pycache__" / "code.cpython-314.pyc").write_bytes(b"")
    report.committed_code(folder, root, trials_file(root))


@pytest.mark.parametrize("name", ["lab/signal.pyc", "lab/inputs.csv", "templates/__pycache__/card.cpython-314.pyc"])
def test_files_git_ignores_beside_the_folder_are_refused(lab, market, name):
    root, folder = lab
    (root / name).parent.mkdir(parents=True, exist_ok=True)
    (root / name).write_bytes(b"")
    with pytest.raises(RuntimeError, match="git ignores"):
        run(root, folder, market)


def test_a_compiled_file_beside_the_strategy_is_never_read(lab, market, tmp_path):
    root, folder = lab
    positions = report.strategy_of(folder / "strategy.py")
    assert not (folder / "__pycache__").exists()                        # none written
    forged = tmp_path / "forged.py"
    forged.write_text(STRATEGY + "FORGED = True\n")
    compiled = folder / "__pycache__" / f"strategy.{sys.implementation.cache_tag}.pyc"
    py_compile.compile(str(forged), cfile=str(compiled), dfile=str(folder / "strategy.py"),
                       invalidation_mode=py_compile.PycInvalidationMode.UNCHECKED_HASH)
    positions = report.strategy_of(folder / "strategy.py")
    assert "FORGED" not in positions.__globals__                         # the source, not the compiled file
    with pytest.raises(RuntimeError, match="git ignores"):
        run(root, folder, market)


def test_uncommitted_files_are_refused_whatever_git_s_settings(lab, market):
    root, folder = lab
    git("config", "status.showUntrackedFiles", "no", cwd=root)
    for name in ("strategies/demo-01-momentum/span.txt", "lab/extra.py"):
        (root / name).write_text("20\n")
        with pytest.raises(RuntimeError, match="(?s)uncommitted files.*" + re.escape(name.rsplit("/", 1)[-1])):
            run(root, folder, market)
        (root / name).unlink()


@pytest.mark.parametrize("name", ["helper.py", "inputs/helper.py"])
def test_links_to_files_elsewhere_are_refused_at_any_depth(lab, market, name):
    root, folder = lab
    (folder / name).parent.mkdir(parents=True, exist_ok=True)
    (folder / name).symlink_to(root / "lab" / "code.py")
    commit(root, "a link", f"strategies/demo-01-momentum/{name}")
    with pytest.raises(RuntimeError, match="links to files elsewhere"):
        run(root, folder, market)


@pytest.mark.parametrize("flag", ["--assume-unchanged", "--skip-worktree"])
@pytest.mark.parametrize("path", ["strategies/demo-01-momentum/strategy.py", "lab/code.py", "templates/card.yaml"])
def test_an_edit_hidden_from_git_is_refused(lab, market, flag, path):
    root, folder = lab
    git("update-index", flag, path, cwd=root)
    (root / path).write_text((root / path).read_text().replace("% 5 == 0", "% 3 == 0") + "\n# hidden\n")
    with pytest.raises(RuntimeError, match="told to overlook"):
        run(root, folder, market)


def test_a_line_added_to_a_registry_hidden_from_git_is_refused(lab, market):
    root, folder = lab
    run(root, folder, market)
    commit(root, "registry", "registry/trials.jsonl")
    git("update-index", "--assume-unchanged", "registry/trials.jsonl", cwd=root)
    line = registry.lines(trials_file(root))[0]
    registry.write([json.dumps({**line, "card": "demo-98-forged", "card_hash": "f" * 64})], trials_file(root))
    with pytest.raises(RuntimeError, match="told to overlook"):
        run(root, new_strategy(root, "demo-38-after"), market)


@pytest.mark.parametrize("path", ["templates/card.yaml", "data/manifest.json", "requirements.txt"])
def test_what_a_run_reads_beside_its_folder_is_committed(lab, market, path):
    root, folder = lab
    (root / path).write_text((root / path).read_text() + "\n")
    with pytest.raises(RuntimeError, match="uncommitted"):
        run(root, folder, market)


def test_a_file_moved_twice_or_edited_as_it_moved_still_came_before_its_card(lab, market):
    root, _ = lab
    (root / "drafts").mkdir()
    (root / "drafts" / "idea.py").write_text(STRATEGY)
    commit(root, "a draft", "drafts/idea.py")
    twice = root / "strategies" / "demo-28-twice"
    twice.mkdir()
    (twice / "card.yaml").write_text(card("demo-28-twice", 20))
    commit(root, "card", "strategies/demo-28-twice/card.yaml")
    git("mv", "drafts/idea.py", "drafts/better.py", cwd=root)           # the first move, after the card
    git("commit", "-q", "-m", "renamed", cwd=root)
    git("mv", "drafts/better.py", "strategies/demo-28-twice/strategy.py", cwd=root)
    git("commit", "-q", "-m", "moved in", cwd=root)
    with pytest.raises(RuntimeError, match="strategy.py was committed before the card"):
        run(root, twice, market)
    (root / "drafts" / "other.py").write_text(STRATEGY)
    commit(root, "another draft", "drafts/other.py")
    edited = root / "strategies" / "demo-29-edited"
    edited.mkdir()
    (edited / "card.yaml").write_text(card("demo-29-edited", 20))
    commit(root, "card", "strategies/demo-29-edited/card.yaml")
    git("mv", "drafts/other.py", "strategies/demo-29-edited/strategy.py", cwd=root)
    (edited / "strategy.py").write_text(STRATEGY.replace("% 5 == 0", "% 4 == 0") + "# tuned\n")
    git("add", "strategies/demo-29-edited/strategy.py", cwd=root)
    git("commit", "-q", "-m", "moved in and tuned", cwd=root)
    with pytest.raises(RuntimeError, match="strategy.py was committed before the card"):
        run(root, edited, market)


def test_a_file_deleted_then_added_again_came_first_when_it_was_first_added(lab, market):
    root, _ = lab
    back = root / "strategies" / "demo-30-back"
    back.mkdir()
    (back / "helper.py").write_text("SPAN = 20\n")
    commit(root, "helper first", "strategies/demo-30-back/helper.py")
    git("rm", "-q", "strategies/demo-30-back/helper.py", cwd=root)
    git("commit", "-q", "-m", "helper gone", cwd=root)
    back.mkdir(exist_ok=True)                                           # git took the empty folder away
    (back / "card.yaml").write_text(card("demo-30-back", 20))
    commit(root, "card", "strategies/demo-30-back/card.yaml")
    (back / "helper.py").write_text("SPAN = 20\n")
    (back / "strategy.py").write_text(STRATEGY)
    commit(root, "code", "strategies/demo-30-back/helper.py", "strategies/demo-30-back/strategy.py")
    with pytest.raises(RuntimeError, match="helper.py was committed before the card"):
        run(root, back, market)


def test_a_file_whose_name_is_not_ascii_runs(lab, market):
    root, _ = lab
    folder = new_strategy(root, "demo-31-accents")
    (folder / "réflexion.md").write_text("Pourquoi.\n")
    commit(root, "reasoning", "strategies/demo-31-accents/réflexion.md")
    assert run(root, folder, market).card == "demo-31-accents"


def test_no_file_of_the_folder_comes_before_its_card_under_any_name(lab, market):
    root, _ = lab
    (root / "drafts").mkdir()
    (root / "drafts" / "idea.py").write_text(STRATEGY)
    commit(root, "a draft", "drafts/idea.py")
    renamed = root / "strategies" / "demo-12-renamed"
    renamed.mkdir()
    (renamed / "card.yaml").write_text(card("demo-12-renamed", 20))
    commit(root, "card", "strategies/demo-12-renamed/card.yaml")
    git("mv", "drafts/idea.py", "strategies/demo-12-renamed/strategy.py", cwd=root)
    git("commit", "-q", "-m", "moved", cwd=root)
    with pytest.raises(RuntimeError, match="strategy.py was committed before the card"):
        run(root, renamed, market)
    helped = root / "strategies" / "demo-13-helped"
    helped.mkdir()
    (helped / "helper.py").write_text("SPAN = 20\n")
    commit(root, "helper first", "strategies/demo-13-helped/helper.py")
    (helped / "card.yaml").write_text(card("demo-13-helped", 20))
    commit(root, "card", "strategies/demo-13-helped/card.yaml")
    (helped / "strategy.py").write_text(STRATEGY)
    commit(root, "code", "strategies/demo-13-helped/strategy.py")
    with pytest.raises(RuntimeError, match="helper.py was committed before the card"):
        run(root, helped, market)


def keep(monkeypatch):
    """Whatever a strategy under test changes in the lab is put back after the test."""
    monkeypatch.setattr(battery, "MIN_SHARPE", battery.MIN_SHARPE)
    monkeypatch.setitem(costs.PER_SIDE, "etf", costs.PER_SIDE["etf"])
    monkeypatch.setattr(battery.decide_economic, "__code__", battery.decide_economic.__code__)
    monkeypatch.setattr(stats, "sharpe", stats.sharpe)
    monkeypatch.setattr(registry, "append", registry.append)
    monkeypatch.setattr(costs.per_side, "__defaults__", costs.per_side.__defaults__)
    monkeypatch.setattr(data.Market, "window", vars(data.Market)["window"])
    monkeypatch.setattr(battery.Verdict, "failed", vars(battery.Verdict)["failed"])
    monkeypatch.setattr(report, "seed_of", report.seed_of)
    monkeypatch.setattr(engine, "run", engine.run)
    monkeypatch.setattr(universe, "cluster_of", universe.cluster_of)
    monkeypatch.setattr(status, "write", status.write)
    monkeypatch.setitem(data.CROSS_CHECK, "tickers", list(data.CROSS_CHECK["tickers"]))


def test_a_strategy_that_imports_the_lab_is_refused(lab, market):
    root, _ = lab
    reader = new_strategy(root, "demo-14-reader", code="from lab import stats\n" + STRATEGY)
    for attempted in (lambda: run(root, reader, market), lambda: attempt(reader, market)):
        with pytest.raises(RuntimeError, match="strategy.py imports lab: a strategy reads the market"):
            attempted()
    helped = new_strategy(root, "demo-15-helped", code="from helper import SPAN\n" + STRATEGY)
    (helped / "helper.py").write_text("import lab.battery\nSPAN = 20\n")
    commit(root, "helper", "strategies/demo-15-helped/helper.py")
    with pytest.raises(RuntimeError, match="helper.py imports lab.battery"):
        run(root, helped, market)
    assert not trials_file(root).exists()


@pytest.mark.parametrize("ident, code, name", [
    ("demo-16-loose", LAB_OF + 'LAB["lab.battery"].MIN_SHARPE = 0.0\n' + STRATEGY, "lab.battery.MIN_SHARPE"),
    ("demo-17-hidden", LAB_OF + 'KEPT = LAB["lab.battery"].MIN_SHARPE\nLAB["lab.battery"].MIN_SHARPE = 0.0\n'
     + STRATEGY.replace(FIRST_LINE, FIRST_LINE + '    LAB["lab.battery"].MIN_SHARPE = KEPT\n'), "lab.battery.MIN_SHARPE"),
    ("demo-19-costs", LAB_OF + 'LAB["lab.costs"].PER_SIDE["etf"] = 0.0\n' + STRATEGY, "lab.costs.PER_SIDE"),
    ("demo-20-code", LAB_OF + 'B = LAB["lab.battery"]\nB.decide_economic.__code__ = B.decide_hygiene.__code__\n'
     + STRATEGY, "lab.battery.decide_economic"),
    ("demo-21-stats", LAB_OF + 'LAB["lab.stats"].sharpe = lambda x: 9.0\n' + STRATEGY, "lab.stats.sharpe"),
    ("demo-22-silent", LAB_OF + 'LAB["lab.registry"].append = lambda *a, **k: []\n' + STRATEGY, "lab.registry.append"),
    ("demo-39-default", LAB_OF + 'LAB["lab.costs"].per_side.__defaults__ = (0.0, frozenset())\n' + STRATEGY,
     "lab.costs.per_side"),
    ("demo-40-method", LAB_OF + 'LAB["lab.data"].Market.window = lambda self, *a: self\n' + STRATEGY, "lab.data.Market"),
    ("demo-41-property", LAB_OF + 'LAB["lab.battery"].Verdict.failed = property(lambda self: None)\n' + STRATEGY,
     "lab.battery.Verdict"),
    ("demo-42-runner", LAB_OF + 'LAB["lab.report"].seed_of = lambda card_hash: 0\n' + STRATEGY, "lab.report.seed_of"),
    ("demo-43-engine", LAB_OF + 'LAB["lab.engine"].run = LAB["lab.engine"].run_many\n' + STRATEGY, "lab.engine.run"),
    ("demo-44-universe", LAB_OF + 'LAB["lab.universe"].cluster_of = lambda ticker: "one"\n' + STRATEGY,
     "lab.universe.cluster_of"),
    ("demo-45-board", LAB_OF + 'LAB["lab.status"].write = lambda *a, **k: None\n' + STRATEGY, "lab.status.write"),
    ("demo-46-nested", LAB_OF + 'LAB["lab.data"].CROSS_CHECK["tickers"].append("SPY")\n' + STRATEGY,
     "lab.data.CROSS_CHECK"),
    ("demo-47-added", LAB_OF + 'LAB["lab.battery"].float = int\n' + STRATEGY, "lab.battery.float (added)"),
])
def test_a_strategy_that_changes_the_lab_as_it_is_imported_is_refused(lab, market, monkeypatch, ident, code, name):
    """Rebound, edited in place, its code or defaults swapped, a class's method or property replaced,
    a name added: even when it puts the value back as it runs."""
    root, _ = lab
    keep(monkeypatch)
    folder = new_strategy(root, ident, code=code)
    try:
        with pytest.raises(RuntimeError, match=f"changed the lab as it was imported: (.*, )?{re.escape(name)}(,|;)"):
            run(root, folder, market)                     # a class shared by several modules is named in each
    finally:
        vars(battery).pop("float", None)
    assert not trials_file(root).exists() and registry.recorded(trials_file(root)) == []


def probe():
    class Probe:
        limits = [1, [2]]

        @staticmethod
        def fixed():
            return 1

        @classmethod
        def made(cls):
            return 1

        @property
        def shown(self):
            return 1
    return Probe


@pytest.mark.parametrize("change", [
    lambda c: setattr(c, "fixed", staticmethod(lambda: 2)),
    lambda c: setattr(vars(c)["made"].__func__, "__code__", (lambda cls: 2).__code__),
    lambda c: setattr(vars(c)["shown"].fget, "__code__", (lambda self: 2).__code__),
    lambda c: c.limits[1].append(3),
    lambda c: setattr(c, "added", 1),
    lambda c: setattr(c, "__repr__", lambda self: "a probe"),
])
def test_the_tripwire_sees_every_kind_of_class_attribute_change(change):
    kind = probe()
    before = report.fingerprint(kind)
    assert report.same(report.fingerprint(kind), before)
    change(kind)
    assert not report.same(report.fingerprint(kind), before)


def test_a_strategy_that_changes_the_lab_as_it_runs_voids_its_run(lab, market, monkeypatch):
    root, _ = lab
    keep(monkeypatch)
    floor = battery.MIN_SHARPE
    late = LAB_OF + STRATEGY.replace(FIRST_LINE, FIRST_LINE + '    LAB["lab.battery"].MIN_SHARPE = 0.0\n')
    folder = new_strategy(root, "demo-18-late", code=late)
    head = git("rev-parse", "HEAD", cwd=root)
    with pytest.raises(report.Recorded, match="changed the lab as it ran: lab.battery.MIN_SHARPE; the run is void") as done:
        run(root, folder, market)
    assert done.value.verdict is None                     # nothing computed on a changed battery is shown
    lines = registry.lines(trials_file(root))
    assert [(line["variant"], line["gates"], line["failed"], line["survivor"]) for line in lines] == [
        (0, {}, None, False), (1, {}, None, False)]
    assert {line["void"] for line in lines} == {"the strategy changed the lab as it ran: lab.battery.MIN_SHARPE"}
    for line in lines:                                    # named like any run's
        assert (line["commit"], line["snapshot"], line["snapshot_hash"], line["thresholds"]) == (
            head, "synthetic", SNAPSHOT_HASH, battery.THRESHOLDS)
        assert line["versions"]["pandas"] and line["versions"]["python"]
    trials = registry.history(trials_file(root))          # the battery computed them: they count in gate 4
    assert len(trials) == 2 and all(line["monthly"] for line in lines) and not any(t.survivor for t in trials)
    assert "[demo-18-late](strategies/demo-18-late/) · void" in (root / "STATUS.md").read_text()   # the board redrawn
    commit(root, "registry", "registry/trials.jsonl")
    with pytest.raises(RuntimeError, match="opened once"):
        run(root, folder, market)                         # the battery saw its holdout
    battery.MIN_SHARPE = floor
    assert run(root, new_strategy(root, "demo-23-next"), market).card == "demo-23-next"
    commit(root, "registry", "registry/trials.jsonl")
    with pytest.raises(RuntimeError, match="opened once"):
        run(root, folder, market)                         # and after another card ran
    board = status.render(root, trials_file(root))
    assert "[demo-18-late](strategies/demo-18-late/) · void: the strategy changed the lab as it ran" in board
    clone = root.parent.parent / "fresh" / root.name
    git("clone", "-q", str(root.parent), str(clone.parent), cwd=root)
    with pytest.raises(RuntimeError, match="opened once"):
        report.check_card(clone / "strategies" / "demo-18-late", list(market.prices.columns),
                          clone / "registry" / "trials.jsonl")  # every clone knows it


def unwritable(texts, path=registry.REGISTRY):
    raise PermissionError("read-only")


def test_a_registry_that_cannot_be_written_leaves_the_lines_in_the_clone_until_restore_puts_them_back(
        lab, market, monkeypatch, capsys):
    root, folder = lab
    monkeypatch.setattr(registry, "write", unwritable)
    with pytest.raises(report.Recorded, match="the card has run, and the registry could not be written "
                                              ".PermissionError: read-only.: this clone kept its lines.*lab.registry "
                                              "restore") as done:
        run(root, folder, market)
    assert done.value.verdict is not None and done.value.verdict.gates   # its verdict stands, and is shown
    assert (folder / "report.ipynb").exists() and not (folder / report.EVIDENCE).exists()   # and its report drawn
    monkeypatch.undo()
    other = new_strategy(root, "demo-38-other")
    with pytest.raises(RuntimeError, match="put them back.*lab.registry restore"):
        run(root, other, market)
    assert registry.main(["void"], trials_file(root)) == 1              # not void: its lines are kept
    assert "wrote its lines, which this clone kept" in capsys.readouterr().err
    assert registry.main(["restore"], trials_file(root)) == 0
    lines = registry.lines(trials_file(root))
    assert [(line["card"], line["variant"], line.get("void"), line["sharpe"]) for line in lines] == [
        ("demo-01-momentum", k, None, round(t.sharpe, 6)) for k, t in enumerate(done.value.verdict.trials)]
    commit(root, "registry", "registry/trials.jsonl")
    assert run(root, other, market).gates[3].figures["trials"] == 4      # gate 4 counts them


def test_a_run_that_wrote_no_line_is_left_to_void(lab, market, monkeypatch, capsys):
    root, folder = lab
    monkeypatch.setattr(registry, "write", unwritable)
    monkeypatch.setattr(registry, "keep", unwritable)
    with pytest.raises(report.Recorded, match="the card has run, and the registry could not be written "
                                              ".PermissionError: read-only.: once the registry can be written, "
                                              "python -m lab.registry void"):
        run(root, folder, market)
    monkeypatch.undo()
    card_hash = hashlib.sha256((folder / "card.yaml").read_bytes()).hexdigest()
    assert registry.missing(trials_file(root)) == [card_hash]           # the record took the card before the battery
    other = new_strategy(root, "demo-37-other")
    with pytest.raises(RuntimeError, match="put them back.*lab.registry void writes void lines"):
        run(root, other, market)
    assert registry.main(["void"], trials_file(root)) == 0
    assert "demo-01-momentum: void lines written" in capsys.readouterr().out
    lines = registry.lines(trials_file(root))
    assert [(line["card"], line["variant"], line["void"]) for line in lines] == [
        ("demo-01-momentum", 0, registry.LOST), ("demo-01-momentum", 1, registry.LOST)]
    assert lines[0]["time"] == registry.recorded(trials_file(root))[0][1]  # when its run began
    commit(root, "registry", "registry/trials.jsonl")
    assert run(root, other, market).card == "demo-37-other"
    commit(root, "registry", "registry/trials.jsonl")
    with pytest.raises(RuntimeError, match="opened once"):
        run(root, folder, market)
    rows = [row[0] for row in registry.recorded(trials_file(root))]    # appended, never rewritten
    assert rows == [card_hash, hashlib.sha256((other / "card.yaml").read_bytes()).hexdigest()]


def test_lines_are_written_on_lines_of_their_own(tmp_path):
    path = tmp_path / "trials.jsonl"
    path.write_text(one("a"))                                            # a last line left without its end
    registry.write([one("b"), one("c")], path)
    assert path.read_text() == held("a", "b", "c")
    registry.write([], path)
    assert [line["card_hash"] for line in registry.lines(path)] == ["a", "b", "c"]


def test_void_names_a_run_whose_card_is_in_no_folder(lab, market, capsys):
    root, folder = lab
    registry.record("e" * 64, "2026-01-01T00:00:00Z", trials_file(root))
    assert registry.main(["void"], trials_file(root)) == 1
    assert "no strategy folder holds the card eeeeeeeeeeee" in capsys.readouterr().err
    assert registry.main(["neither"], trials_file(root)) == 2


def test_the_registry_reads_a_run_s_outcome_from_the_gates_it_writes(tmp_path, monkeypatch):
    gates = [battery.Gate(n, name, n != 2, "why") for n, name in battery.GATES.items()]
    verdict = battery.Verdict("x-01-a", gates, [], {})
    monkeypatch.setattr(battery.Verdict, "failed", property(lambda self: None))
    (line,) = registry.append(verdict, "ab" * 32, [{"span": 1}], "s", None, "c", {}, tmp_path / "trials.jsonl")
    assert (line["failed"], line["survivor"]) == (2, False)
    verdict.gates = [battery.Gate(n, name, True, "why") for n, name in battery.GATES.items()]
    (line,) = registry.append(verdict, "cd" * 32, [{"span": 1}], "s", None, "c", {}, tmp_path / "trials.jsonl")
    assert (line["failed"], line["survivor"]) == (None, True)
    verdict.gates = []
    (line,) = registry.append(verdict, "ef" * 32, [{"span": 1}], "s", None, "c", {}, tmp_path / "trials.jsonl")
    assert line["survivor"] is False


def test_a_run_refuses_libraries_other_than_their_pins(lab, market, tmp_path, monkeypatch):
    root, folder = lab
    pins = tmp_path / "elsewhere" / "requirements.txt"
    pins.parent.mkdir()
    pins.write_text("pandas==0.0.1\n")
    monkeypatch.setattr(report, "REQUIREMENTS", pins)
    with pytest.raises(RuntimeError, match="pinned 0.0.1"):
        run(root, folder, market)
    assert not trials_file(root).exists()


def test_the_notebook_shows_no_path_of_the_machine(lab, market):
    root, _ = lab
    lost = f"def positions(market, span):\n    raise FileNotFoundError('{root}/strategies/x/signal.csv')\n"
    folder = new_strategy(root, "demo-15-lost", code=lost)
    verdict = run(root, folder, market)
    assert str(root) in verdict.gates[0].reason                        # the battery's own reason, raw
    shown = json.dumps([o.get("data", {}) for o in outputs(folder)])
    assert "strategies/x/signal.csv" in shown and str(root) not in shown


def test_the_report_names_the_assets_that_start_late(lab, market):
    root, _ = lab
    prices = market.prices.copy()
    prices.loc[:"2013-12-31", "S8"] = np.nan
    folder = new_strategy(root, "demo-59-late")
    run(root, folder, data.Market(prices, prices.notna(), market.rf, prices))
    shown = json.dumps([o.get("data", {}) for o in outputs(folder)])
    assert "Assets that start trading after 2005-" in shown and ": S8. A placebo shifts their weights" in shown


def drawn(folder):
    """The report template's cells, run here in `folder` on the data its run left: every axis the
    cells draw, by its title."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    book = nbformat.read(report.TEMPLATE, as_version=4)
    axes, here, namespace = {}, os.getcwd(), {}
    os.chdir(folder)
    try:
        for cell in (c for c in book.cells if c.cell_type == "code"):
            exec(cell.source, namespace)
            for number in plt.get_fignums():
                figure = plt.figure(number)
                figure.canvas.draw()
                axes.update({axis.get_title(): axis for axis in figure.axes})
            plt.close("all")
    finally:
        os.chdir(here)
    return axes


LEAKY = STRATEGY.replace("    every = ", "    ahead = (market.signal_prices.pct_change(span).shift(-1) > 0).astype(float)\n"
                         "    ahead = ahead.div(ahead.sum(axis=1).where(ahead.sum(axis=1) > 0), axis=0).fillna(0.0)\n"
                         "    years = (weights.index.year >= 2008) & (weights.index.year <= 2012)\n"
                         "    weights.loc[years] = ahead.loc[years]\n"
                         "    every = ")


def test_the_report_draws_each_floor_and_each_break_where_the_battery_sets_them(lab, market, monkeypatch):
    """Gate 1's red bars on the years of its breaks, gate 2's floor on its own bar, gate 7's floor at
    the battery's percentile of the in-sample paths."""
    from matplotlib.colors import to_rgba
    root, _ = lab
    folder = new_strategy(root, "demo-48-leaky", code=LEAKY)

    def later(notebook, **options):
        raise OSError("drawn by the test")
    monkeypatch.setattr(report, "execute", later)
    with pytest.raises(report.Recorded, match="its notebook failed"):
        run(root, folder, market)
    ev = pickle.loads((folder / report.EVIDENCE).read_bytes())["evidence"]
    breaks = {d.year for variant in ev["timing breaks"].values() for kind in variant.values() for d in kind}
    assert breaks and breaks <= set(range(2008, 2013))
    axes = drawn(folder)
    years = next(axis for title, axis in axes.items() if title.startswith("sessions where the strategy sets a target"))
    labels = [tick.get_text() for tick in years.get_xticklabels()]
    red = {labels[round(bar.get_x() + bar.get_width() / 2)] for bar in years.patches
           if bar.get_facecolor() == to_rgba("#c0504d")}
    assert red == {str(year) for year in breaks}
    sharpe = axes["Sharpe ratio, net of costs; red: the floor of each bar"]
    floors = {round(float(np.mean(segment[:, 1]))): float(segment[0, 0])
              for lines in sharpe.collections for segment in lines.get_segments()}
    assert floors == {1: battery.MIN_SHARPE_DOUBLED, 2: battery.MIN_SHARPE}      # at 2x costs, then at the stated costs
    for key, label in (("Sharpe", "Sharpe ratio"), ("alpha", "alpha")):
        paths = axes[f"in-sample {label}s, {battery.WINDOW}-session paths"]
        dashed = [line.get_xdata()[0] for line in paths.get_lines() if line.get_linestyle() == "--"]
        assert dashed == pytest.approx([np.percentile(ev["bootstrap"][key], battery.PERCENTILE)])


def test_a_card_that_holds_bitcoin_shows_its_figures_without_bitcoin(lab):
    root, _ = lab
    market, signal = synthetic_market(9, coin=True)
    folder = new_strategy(root, "demo-16-coin", universe=(*EIGHT, "COIN"))
    run(root, folder, market, crypto=frozenset({"COIN"}))
    shown = [o.get("data", {}) for o in outputs(folder)]
    at = next(k for k, o in enumerate(shown) if o.get("text/markdown") == "Without bitcoin, gate 2's figures:")
    assert "<table" in shown[at + 1].get("text/html", "") and "Sharpe" in shown[at + 1]["text/html"]


def test_the_snapshot_is_named_with_the_hash_of_its_files(tmp_path):
    files = {"SPY.csv": {"sha256": "ab" * 32, "rows": 10}}
    (tmp_path / "manifest.json").write_text(json.dumps({"snapshot": "2026-09-22", "files": files}))
    name, digest = report.snapshot_of(tmp_path)
    assert (name, digest) == ("2026-09-22", hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest())
    added = {"SHY.csv": {"sha256": "cd" * 32, "rows": 10}}
    (tmp_path / "manifest.json").write_text(json.dumps({"snapshot": "2026-09-22", "files": files,
                                                        "additions": [{"snapshot": "2026-09-24", "files": added}]}))
    name, digest = report.snapshot_of(tmp_path)                        # an addition joins the name and the hash
    assert (name, digest) == ("2026-09-22+2026-09-24",
                              hashlib.sha256(json.dumps([files, added], sort_keys=True).encode()).hexdigest())


def test_the_card_template_is_a_card_the_runner_accepts(tmp_path):
    folder = tmp_path / "strategies" / "SC-004-01-slug"                  # the template's own id
    folder.mkdir(parents=True)
    (folder / "card.yaml").write_text((report.LAB / "templates" / "card.yaml").read_text())
    spec, card = report.read_card(folder)
    assert spec["theory"] == "SC-004" and len(card.variants) == 2 and set(card.neighbours) == {"lookback"}


def test_the_committed_board_is_what_the_lab_holds():
    """The board is regenerated at every run and before every commit of a verdict or a status."""
    assert (report.LAB / "STATUS.md").read_text() == status.render()


def test_a_run_on_the_frozen_snapshot_records_its_name_and_hash(lab, market, tmp_path, monkeypatch):
    root, folder = lab
    files = {"S1.csv": {"sha256": "cd" * 32, "rows": 10}}
    (tmp_path / "frozen").mkdir()
    (tmp_path / "frozen" / "manifest.json").write_text(json.dumps({"snapshot": "2026-01-02", "files": files}))
    monkeypatch.setattr(data, "DATA", tmp_path / "frozen")
    monkeypatch.setattr(data, "load", lambda root: market)
    report.run(folder, registry_path=trials_file(root), lab=root, board=root / "STATUS.md", crypto=frozenset(),
               cluster=CLUSTERS.get)
    digest = hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()
    assert {(line["snapshot"], line["snapshot_hash"]) for line in registry.lines(trials_file(root))} == {
        ("2026-01-02", digest)}


def test_the_command_line_refuses_in_one_line_and_exits_1(lab, tmp_path, monkeypatch, capsys):
    root, folder = lab
    (folder / "card.yaml").write_text("- id\n- theory\n")
    assert report.main(["--check", str(folder)]) == 1
    said = capsys.readouterr().err.strip().splitlines()
    assert len(said) == 1 and said[0].startswith("refused: ") and "a card is a mapping" in said[0]
    (tmp_path / "frozen").mkdir()
    (tmp_path / "frozen" / "manifest.json").write_text(json.dumps({"snapshot": "gone", "files": {}}))
    monkeypatch.setattr(data, "DATA", tmp_path / "frozen")
    assert report.main([str(folder)]) == 1
    said = capsys.readouterr().err.strip().splitlines()
    assert len(said) == 1 and "the snapshot gone is not in data/gone/" in said[0]

    def unforeseen(folder):
        raise KeyError("S9")
    monkeypatch.setattr(report, "run", unforeseen)                     # any error, not only the lab's refusals
    assert report.main([str(folder)]) == 1
    assert capsys.readouterr().err.strip().splitlines() == ["refused: KeyError: 'S9'"]


def test_the_command_line_shows_a_recorded_run_whose_notebook_failed(lab, market, monkeypatch, capsys):
    root, folder = lab
    verdict = run(root, folder, market)

    def failing(folder):
        raise report.Recorded(verdict, "the run is recorded, and its notebook failed: demo-01-momentum: the "
                                       "notebook failed (CellExecutionError)")
    monkeypatch.setattr(report, "run", failing)
    assert report.main([str(folder)]) == 1
    said = capsys.readouterr()
    assert said.out.startswith("demo-01-momentum: ") and len(said.out.splitlines()) == 8
    assert "the run is recorded, and its notebook failed" in said.err and "refused" not in said.err

    def voided(folder):
        raise report.Recorded(None, "the strategy changed the lab as it ran: lab.battery.MIN_SHARPE; the run is void")
    monkeypatch.setattr(report, "run", voided)
    assert report.main([str(folder)]) == 1
    said = capsys.readouterr()
    assert said.out == "" and said.err.strip().splitlines() == [
        "the strategy changed the lab as it ran: lab.battery.MIN_SHARPE; the run is void"]


def test_a_failure_after_the_lines_says_the_run_is_recorded_and_shows_its_gates(lab, market, monkeypatch, capsys):
    root, folder = lab
    real = report.run

    def broken_board(*args, **kwargs):
        raise ValueError("a bank file the board cannot read")
    monkeypatch.setattr(status, "write", broken_board)
    monkeypatch.setattr(report, "run", lambda folder: real(folder, market=market, snapshot="synthetic",
                                                             registry_path=trials_file(root), lab=root,
                                                             crypto=frozenset(), cluster=CLUSTERS.get))
    assert report.main([str(folder)]) == 1
    said = capsys.readouterr()
    assert said.out.startswith("demo-01-momentum: ") and len(said.out.splitlines()) == 8
    assert said.err.strip().splitlines() == ["the card has run, and the board could not be written (ValueError: a "
                                             "bank file the board cannot read); fix the cause, then run python -m "
                                             "lab.status"]
    assert len(registry.lines(trials_file(root))) == 2 and (folder / "report.ipynb").exists()


def test_the_command_line_prints_a_refusal_of_several_lines_on_one(lab, market, monkeypatch, capsys):
    root, folder = lab
    real = report.run
    (folder / "strategy.py").write_text(STRATEGY + "\n# tuned\n")
    (root / "lab" / "extra.py").write_text("# new\n")
    monkeypatch.setattr(report, "run", lambda folder: real(folder, market=market, registry_path=trials_file(root),
                                                             lab=root, crypto=frozenset(), cluster=CLUSTERS.get))
    assert report.main([str(folder)]) == 1
    said = capsys.readouterr().err.strip().splitlines()
    assert len(said) == 1 and said[0].startswith("refused: uncommitted files") and "extra.py" in said[0]
    assert "strategy.py" in said[0]


def test_the_data_check_without_its_snapshot_refuses_in_one_line(tmp_path, capsys):
    (tmp_path / "manifest.json").write_text(json.dumps({"snapshot": "gone", "files": {}}))
    assert data.main(["check"], root=tmp_path) == 1
    said = capsys.readouterr().err.strip().splitlines()
    assert len(said) == 1 and said[0].startswith("refused: the snapshot gone is not in data/gone/")


def test_the_notebook_command_draws_the_report_and_the_board_from_a_committed_template(lab, monkeypatch, capsys):
    root, folder = lab
    done = []
    monkeypatch.setattr(report, "execute_notebook", lambda folder: done.append("report") or folder / "report.ipynb")
    monkeypatch.setattr(status, "write", lambda *args, **kwargs: done.append("board"))
    monkeypatch.setattr(report, "git", lambda *args, **kwargs: "")
    assert report.main(["--notebook", str(folder)]) == 0 and done == ["report", "board"]
    monkeypatch.setattr(report, "git", lambda *args, **kwargs: " M alpha-lab/templates/report.ipynb")
    assert report.main(["--notebook", str(folder)]) == 1 and done == ["report", "board"]
    assert "the report template is not committed" in capsys.readouterr().err


def test_two_runs_at_once_in_one_clone_run_one_after_the_other(lab, market):
    root, _ = lab
    slow = new_strategy(root, "demo-40-slow", code="import time\ntime.sleep(3)\n" + STRATEGY)
    quick = new_strategy(root, "demo-41-quick")
    done = {}

    def later():
        time.sleep(1)                             # the slow run holds the record, importing its strategy
        try:
            done["quick"] = run(root, quick, market)
        except Exception as error:
            done["quick"] = error
    second = threading.Thread(target=later)
    second.start()
    ran = run(root, slow, market)
    second.join()
    assert ran.card == "demo-40-slow"
    assert isinstance(done["quick"], RuntimeError) and "uncommitted" in str(done["quick"])   # after the slow one's lines
    assert [row[0] for row in registry.recorded(trials_file(root))] == [
        hashlib.sha256((slow / "card.yaml").read_bytes()).hexdigest()]


@pytest.mark.parametrize("error", [KeyError("lost"), OSError("disk")])
def test_any_error_of_the_battery_leaves_a_void_run(lab, market, monkeypatch, error):
    root, folder = lab

    def broken(*args, **options):
        raise error
    monkeypatch.setattr(battery, "run", broken)
    with pytest.raises(report.Recorded, match="the run stopped .*; the run is void.*the card has run"):
        run(root, folder, market)
    assert {line["void"].split(" (")[0] for line in registry.lines(trials_file(root))} == {"the run stopped"}


@pytest.mark.parametrize("stop", ["raise SystemExit(0)", "raise KeyboardInterrupt"])
def test_a_strategy_that_exits_or_an_interrupt_leaves_a_void_run(lab, market, stop):
    root, _ = lab
    folder = new_strategy(root, "demo-42-exits", code=STRATEGY.replace(FIRST_LINE, FIRST_LINE + f"    {stop}\n"))
    with pytest.raises(report.Recorded, match="the run was interrupted .*; the run is void.*the card has run"):
        run(root, folder, market)
    assert [line["variant"] for line in registry.lines(trials_file(root)) if line.get("void")] == [0, 1]


def test_a_void_run_whose_lines_cannot_be_written_names_void(lab, market, monkeypatch):
    root, folder = lab

    def broken(*args, **options):
        raise RuntimeError("stop here")
    monkeypatch.setattr(battery, "run", broken)
    monkeypatch.setattr(registry, "write", unwritable)
    monkeypatch.setattr(registry, "keep", unwritable)
    with pytest.raises(report.Recorded, match="its lines could not be written: python -m lab.registry void writes them"):
        run(root, folder, market)


def test_a_void_run_whose_lines_the_clone_kept_names_restore(lab, market, monkeypatch):
    root, folder = lab

    def broken(*args, **options):
        raise RuntimeError("stop here")
    monkeypatch.setattr(battery, "run", broken)
    monkeypatch.setattr(registry, "write", unwritable)                   # the clone's copy holds them
    with pytest.raises(report.Recorded, match="could not be written: this clone kept them, and python -m lab.registry "
                                              "restore puts them back"):
        run(root, folder, market)


def test_a_strategy_that_removes_a_module_of_the_lab_as_it_runs_voids_its_run(lab, market, monkeypatch):
    root, _ = lab
    monkeypatch.setitem(sys.modules, "lab.universe", universe)
    gone = LAB_OF + STRATEGY.replace(FIRST_LINE, FIRST_LINE + '    LAB.pop("lab.universe", None)\n')
    folder = new_strategy(root, "demo-43-gone", code=gone)
    with pytest.raises(report.Recorded, match=r"changed the lab as it ran: lab.universe \(removed\)"):
        run(root, folder, market)


def test_the_tripwire_s_helpers_cannot_be_rebound_to_blind_it(lab, market, monkeypatch):
    root, _ = lab
    monkeypatch.setattr(report, "same", report.same)
    blind = LAB_OF + 'LAB["lab.report"].same = lambda now, was: True\n' + STRATEGY
    folder = new_strategy(root, "demo-44-blind", code=blind)
    with pytest.raises(RuntimeError, match="changed the lab as it was imported: lab.report.same"):
        run(root, folder, market)


class Uncomparable:
    def __eq__(self, other):
        raise TypeError("no comparison")

    __hash__ = object.__hash__


def test_a_watched_value_that_cannot_be_compared_is_a_change(lab, market, monkeypatch):
    root, _ = lab
    monkeypatch.setitem(battery.GATES, 1, battery.GATES[1])
    monkeypatch.setitem(sys.modules, "uncomparable", sys.modules[__name__])
    odd = LAB_OF + 'LAB["lab.battery"].GATES[1] = LAB["uncomparable"].Uncomparable()\n' + STRATEGY
    folder = new_strategy(root, "demo-45-odd", code=odd)
    with pytest.raises(RuntimeError, match="changed the lab as it was imported: lab.battery.GATES"):
        run(root, folder, market)


def test_a_strategy_that_edits_its_market_in_place_changes_nothing_the_battery_prices(lab, market):
    root, folder = lab
    before = market.prices.copy()
    honest = run(root, folder, market)
    commit(root, "registry", "registry/trials.jsonl")
    edits = STRATEGY.replace(FIRST_LINE, FIRST_LINE + "    held = market.prices\n    held.iloc[len(held) // 2:] *= 2.0\n"
                                                      "    market.prices.fillna(0.0, inplace=True)\n"
                                                      "    market.rf.fillna(1.0, inplace=True)\n")
    edited = run(root, new_strategy(root, "demo-46-edits", code=edits), market)
    assert [t.sharpe for t in edited.trials] == [t.sharpe for t in honest.trials]
    assert market.prices.equals(before)                                      # the market itself untouched


def test_an_edit_that_a_filter_of_git_hides_is_refused(lab, market):
    root, folder = lab
    git("config", "filter.hide.clean", "sed -e /TUNED/d", cwd=root)
    attributes = root / git("rev-parse", "--git-path", "info/attributes", cwd=root)
    attributes.parent.mkdir(exist_ok=True)
    attributes.write_text("*.py filter=hide\n")
    (folder / "strategy.py").write_text(STRATEGY + "SPAN = 200  # TUNED\n")
    git("add", "strategies/demo-01-momentum/strategy.py", cwd=root)          # the filter cleans the line away
    assert git("status", "--porcelain", cwd=root) == ""                     # git sees nothing
    with pytest.raises(RuntimeError, match="bytes differ from their commit, which a filter of git's settings hides: "
                                           "strategies/demo-01-momentum/strategy.py"):
        run(root, folder, market)


def test_the_board_refuses_a_line_that_is_not_a_registry_line_in_one_line(monkeypatch, capsys):
    def broken(*args, **kwargs):
        raise RuntimeError("trials.jsonl, line 3, is not a registry line")
    monkeypatch.setattr(status, "write", broken)
    assert status.main() == 1
    assert capsys.readouterr().err == "refused: trials.jsonl, line 3, is not a registry line\n"


def compiled(source: Path, text: str, flags: int = 0, stale: bool = False, header: bytes | None = None) -> Path:
    """A compiled file of `source` as Python writes it, holding the code of `text`: checked by the
    source's time and size (stale: by another time), which Python reads whenever bit 0b01 is unset,
    or by its hash (flags 0b11), or unchecked (0b01); `header`, other bytes in place of the check."""
    folder = source.parent / "__pycache__"
    folder.mkdir(exist_ok=True)
    path = folder / f"{source.stem}.{sys.implementation.cache_tag}.pyc"
    stat = source.stat()
    if not flags & 0b01:
        check = ((int(stat.st_mtime) - stale) & 0xFFFFFFFF).to_bytes(4, "little") + \
                (stat.st_size & 0xFFFFFFFF).to_bytes(4, "little")
    else:
        check = importlib.util.source_hash(source.read_bytes())
    code = compile(text, str(source), "exec", dont_inherit=True)
    check = check if header is None else header
    path.write_bytes(importlib.util.MAGIC_NUMBER + flags.to_bytes(4, "little") + check + marshal.dumps(code))
    return path


def test_a_compiled_file_of_the_lab_that_holds_other_code_is_refused(lab, market):
    root, folder = lab
    source = root / "lab" / "code.py"
    name = f"lab/__pycache__/code.{sys.implementation.cache_tag}.pyc"
    for flags, header in ((0, None), (0b10, None), (0b01, None), (0b11, None), (0b01, b"elsewise")):
        compiled(source, "COSTS = 0\n", flags, header=header)          # each kind Python reads in place of the source
        with pytest.raises(RuntimeError, match=f"Python would read in place of their source, and that hold other "
                                               f"code: {re.escape(name)}; they are removed as this run ends"):
            run(root, folder, market)
        assert not (root / "lab" / "__pycache__").exists()
    assert report.compiled_as_source(compiled(source, "COSTS = 0\n", stale=True))   # never read: Python recompiles
    assert report.compiled_as_source(compiled(source, "COSTS = 0\n", flags=0b100))  # a flag Python does not know
    temporary = root / "lab" / "__pycache__" / f"code.{sys.implementation.cache_tag}.pyc.4242"
    temporary.write_bytes(compiled(source, "COSTS = 0\n").read_bytes())    # Python writes through it, never reads it
    assert report.kept(f"lab/__pycache__/{temporary.name}") and report.compiled_as_source(temporary)
    assert report.compiled_as_source(root / "lab" / "__pycache__" / "gone.cpython-314.pyc")   # removed meanwhile
    temporary.unlink()
    compiled(source, source.read_text())                                  # what the source compiles to
    assert run(root, folder, market).card == "demo-01-momentum"


def test_the_lab_s_compiled_files_are_removed_after_every_run_and_every_try(lab, market):
    """A strategy can write a compiled file of the runner itself, which the next run would read
    before any check: it is gone once the strategy's run or trial ends."""
    root, _ = lab
    writes = ("from pathlib import Path\n_cache = Path(__file__).resolve().parents[2] / 'lab' / '__pycache__'\n"
              "_cache.mkdir(exist_ok=True)\n(_cache / 'report.cpython-314.pyc').write_bytes(b'forged')\n" + STRATEGY)
    folder = new_strategy(root, "demo-65-forges", code=writes)
    attempt(folder, market)
    assert not (root / "lab" / "__pycache__").exists()
    run(root, folder, market)
    assert not (root / "lab" / "__pycache__").exists()


FORGE = ("import atexit, shutil, sys\nfrom pathlib import Path\n"
         "_cache = Path(__file__).resolve().parents[2] / 'lab' / '__pycache__'\n\n\n"
         "def forge():\n    _cache.mkdir(exist_ok=True)\n    (_cache / 'report.cpython-314.pyc').write_bytes(b'forged')\n\n\n")


@pytest.mark.parametrize("how", ["rebinds the removal", "rebinds the removal at exit", "rebinds rmtree", "at exit",
                                 "void"])
def test_a_compiled_file_a_strategy_leaves_is_removed_however_it_leaves_it(lab, market, monkeypatch, how):
    """The removal is bound before the strategy is imported, rmtree with it, and runs again as the
    interpreter exits, after any exit function of the strategy's, as it was bound, whatever the
    strategy rebinds; and after a run that is recorded, then fails."""
    root, _ = lab
    scrub = report.uncompiled
    monkeypatch.setattr(shutil, "rmtree", shutil.rmtree)                # put back whatever a strategy rebinds
    monkeypatch.setattr(report, "uncompiled", scrub)
    monkeypatch.setattr(battery, "MIN_SHARPE", battery.MIN_SHARPE)
    monkeypatch.setattr(report, "_AT_EXIT", set())
    exits = []
    monkeypatch.setattr(atexit, "register", lambda f, *args: exits.append((f, args)))
    late = how.endswith("at exit")
    head = {"rebinds rmtree": "shutil.rmtree = lambda *a, **k: None\n", "void": "LAB = sys.modules\n"}.get(how, "") + \
        ("atexit.register(forge)\n" if late else "")
    body = ("    sys.modules['lab.report'].uncompiled = lambda *a, **k: []\n" if how.startswith("rebinds the removal")
            else '    LAB["lab.battery"].MIN_SHARPE = 0.0\n' if how == "void" else "") + ("" if late else "    forge()\n")
    code = FORGE + head + STRATEGY.replace(FIRST_LINE, FIRST_LINE + body)
    for k, act in enumerate((attempt, run)):
        folder = new_strategy(root, f"demo-7{k}-{how.replace(' ', '-')}", code=code)
        monkeypatch.setattr(report, "_AT_EXIT", set())                  # each run is a process of its own
        monkeypatch.setattr(report, "uncompiled", scrub)
        exits.clear()
        try:
            act(folder, market) if act is attempt else run(root, folder, market)
        except report.Recorded:                                         # the lab changed as it ran: void
            assert (how == "void" or how.startswith("rebinds the removal")) and act is run
        assert not (root / "lab" / "__pycache__").exists(), (how, act.__name__)            # as it ends
        for f, args in reversed(exits):                                 # as the interpreter exits
            f(*args)
        assert exits[0][0].__qualname__ == "at_exit.<locals>.remove_at_exit"   # before the strategy's own
        assert any(getattr(f, "__name__", "") == "forge" for f, _ in exits) == late
        assert not (root / "lab" / "__pycache__").exists(), (how, act.__name__)


def test_a_compiled_folder_the_removal_cannot_remove_is_named(tmp_path, monkeypatch, capsys):
    here, running = tmp_path / "here", tmp_path / "running"
    for root in (here, running):
        (root / "lab" / "__pycache__").mkdir(parents=True)
    monkeypatch.setattr(report, "LAB", running)                         # the lab whose code runs is cleaned too
    assert report.uncompiled(here) == [] and not (here / "lab" / "__pycache__").exists()
    assert not (running / "lab" / "__pycache__").exists()
    (here / "lab" / "__pycache__").mkdir()
    (here / "lab" / "__pycache__" / "report.cpython-314.pyc").write_bytes(b"forged")         # as the run went
    os.utime(here / "lab" / "__pycache__" / "report.cpython-314.pyc", (time.time() - 1,) * 2)
    assert report.uncompiled(here, remove=lambda path, onexc: onexc(os.rmdir, str(path), PermissionError())) == \
        ["lab/__pycache__"]
    assert "the lab's compiled files in lab/__pycache__ could not be removed" in capsys.readouterr().err
    os.utime(here / "lab" / "__pycache__" / "report.cpython-314.pyc", (time.time() + 3600,) * 2)   # set ahead
    assert report.uncompiled(here, remove=lambda path, onexc: onexc(os.rmdir, str(path), PermissionError())) == \
        ["lab/__pycache__"]                                             # its change time is not
    capsys.readouterr()
    (here / "lab" / "__pycache__" / "report.cpython-314.pyc").unlink()

    def rewritten(path, onexc):                                         # another process writes as it removes
        (path / "stats.cpython-314.pyc").write_bytes(b"compiled")
        onexc(os.rmdir, str(path), OSError(errno.ENOTEMPTY, "Directory not empty"))
    assert report.uncompiled(here, remove=rewritten) == []

    def touched(path, onexc):                                           # a file changed as it removes
        os.chmod(path / "stats.cpython-314.pyc", 0o644)
        onexc(os.rmdir, str(path), OSError(errno.ENOTEMPTY, "Directory not empty"))
    assert report.uncompiled(here, remove=touched) == []                # its change time, not its birth
    (here / "lab" / "__pycache__" / "stats.cpython-314.pyc").write_bytes(b"compiled")
    os.utime(here / "lab" / "__pycache__" / "stats.cpython-314.pyc", (time.time() - 1,) * 2)
    with monkeypatch.context() as rebound:
        rebound.setattr(report, "older", lambda folder, than: False)      # rebound by a strategy at exit
        assert report.uncompiled(here, remove=lambda path, onexc: onexc(os.rmdir, str(path), OSError(
            errno.ENOTEMPTY, "not empty"))) == ["lab/__pycache__"]       # not written again: its file is older
    capsys.readouterr()

    def vanished(path, onexc):                                          # another process removed a file first
        shutil.rmtree(path)
        path.mkdir()
        (path / "engine.cpython-314.pyc").write_bytes(b"compiled")      # and writes one again
        onexc(os.unlink, str(path / "costs.cpython-314.pyc"), FileNotFoundError(errno.ENOENT, "gone"))
    assert report.uncompiled(here, remove=vanished) == []
    tries = []

    def second(path, onexc):                                            # removed on its second try
        tries.append(path)
        shutil.rmtree(path) if len(tries) > 1 else onexc(os.rmdir, str(path), OSError(errno.ENOTEMPTY, "not empty"))
    assert report.uncompiled(here, remove=second) == [] and not (here / "lab" / "__pycache__").exists()
    (here / "lab" / "__pycache__").mkdir()
    unread = tmp_path / "unread"
    unread.mkdir(mode=0o300)                                            # it cannot tell what the folder holds
    try:
        assert report.older(unread, time.time()) and not report.older(tmp_path / "gone", time.time())
        assert report.holds(unread) and not report.holds(tmp_path / "gone")
    finally:
        unread.chmod(0o700)
    empty = here / "lab" / "__pycache__"
    for name in os.listdir(empty):
        os.remove(empty / name)
    assert report.uncompiled(here, remove=lambda path, onexc: onexc(os.rmdir, str(path), PermissionError())) == []
    assert report.uncompiled(here, remove=lambda path, onexc: None) == []    # written again by another process
    assert report.uncompiled(here, remove=lambda path, onexc: (shutil.rmtree(path), onexc(os.rmdir, str(path), OSError()))) \
        == []                                                           # a failure, and yet the folder is gone
    assert capsys.readouterr().err == ""
    cache = here / "lab" / "__pycache__"                                # a real refusal, a link inside
    cache.mkdir(exist_ok=True)
    (cache / "report.cpython-314.pyc").write_bytes(b"forged")
    (cache / "w").mkdir()
    os.link(cache / "report.cpython-314.pyc", cache / "w" / "l")        # unlinked, it moves the file's change time
    cache.chmod(0o555)
    try:
        assert report.uncompiled(here) == ["lab/__pycache__"]
        monkeypatch.setattr(report, "older", lambda folder, than: False)    # rebound by a strategy at exit
        monkeypatch.setattr(report, "holds", lambda folder: False)
        assert report.uncompiled(here) == ["lab/__pycache__"]
    finally:
        cache.chmod(0o755)
    shutil.rmtree(cache)
    cache.mkdir()
    (cache / "report.cpython-314.pyc").symlink_to(tmp_path / "nowhere")    # a link that leads nowhere, for now
    cache.chmod(0o555)
    try:
        assert report.uncompiled(here) == ["lab/__pycache__"]
    finally:
        cache.chmod(0o755)


def test_void_lines_lost_before_their_commit_come_back_with_their_returns(lab, market, monkeypatch):
    root, _ = lab
    keep(monkeypatch)
    late = LAB_OF + STRATEGY.replace(FIRST_LINE, FIRST_LINE + '    LAB["lab.battery"].MIN_SHARPE = 0.0\n')
    folder = new_strategy(root, "demo-47-void-lost", code=late)
    with pytest.raises(report.Recorded, match="the run is void"):
        run(root, folder, market)
    written = trials_file(root).read_text()
    trials_file(root).write_text("")                                     # lost before their commit
    assert len(registry.restore(trials_file(root))) == 2 and trials_file(root).read_text() == written
    assert all(line["void"] and line["sharpe"] is not None for line in registry.lines(trials_file(root)))


def test_a_strategy_that_edits_any_frame_of_its_market_changes_nothing_the_battery_prices(lab, market):
    root, folder = lab
    honest = run(root, folder, market)
    commit(root, "registry", "registry/trials.jsonl")
    edits = STRATEGY.replace("    return weights.where(every, axis=0)\n",
                             "    targets = weights.where(every, axis=0)\n"
                             "    market.tradable.iloc[:, :] = False\n"
                             "    market.signal_prices.iloc[:, :] = 1.0\n"
                             "    market.rf.iloc[:] = 0.01\n"
                             "    return targets\n")
    edited = run(root, new_strategy(root, "demo-49-frames", code=edits), market)
    assert [t.sharpe for t in edited.trials] == [t.sharpe for t in honest.trials]
    assert edited.gates[1].figures == honest.gates[1].figures                # the seed is the card's: gate 2 alone


def test_a_strategy_that_rebinds_void_as_it_runs_still_leaves_void_lines(lab, market, monkeypatch):
    root, _ = lab
    monkeypatch.setattr(registry, "void", registry.void)
    rebinds = LAB_OF + STRATEGY.replace(FIRST_LINE, FIRST_LINE + '    LAB["lab.registry"].void = lambda *a, **k: []\n')
    folder = new_strategy(root, "demo-50-unvoid", code=rebinds)
    with pytest.raises(report.Recorded, match="changed the lab as it ran: lab.registry.void; the run is void"):
        run(root, folder, market)
    assert [line["variant"] for line in registry.lines(trials_file(root)) if line.get("void")] == [0, 1]


def test_a_lab_that_cannot_be_compared_after_the_battery_voids_the_run_with_its_returns(lab, market, monkeypatch):
    root, _ = lab
    monkeypatch.setitem(sys.modules, "lab.universe", universe)
    odd = LAB_OF + STRATEGY.replace(FIRST_LINE, FIRST_LINE + '    LAB["lab.universe"] = 0\n')
    folder = new_strategy(root, "demo-51-odd", code=odd)
    with pytest.raises(report.Recorded, match="the lab could not be compared after the battery .TypeError"):
        run(root, folder, market)
    lines = registry.lines(trials_file(root))
    assert len(lines) == 2 and all(line["void"] and line["sharpe"] is not None for line in lines)


def test_a_strategy_that_deletes_a_name_of_the_lab_as_it_is_imported_is_refused(lab, market, monkeypatch):
    root, _ = lab
    monkeypatch.setattr(costs, "PER_SIDE", costs.PER_SIDE)
    gone = LAB_OF + 'del LAB["lab.costs"].PER_SIDE\n' + STRATEGY
    folder = new_strategy(root, "demo-52-deletes", code=gone)
    with pytest.raises(RuntimeError, match="changed the lab as it was imported: lab.costs.PER_SIDE; nothing"):
        run(root, folder, market)


def test_a_strategy_that_exits_as_it_is_imported_is_refused_and_nothing_is_recorded(lab, market):
    root, _ = lab
    folder = new_strategy(root, "demo-53-exits-early", code="raise SystemExit(0)\n" + STRATEGY)
    with pytest.raises(RuntimeError, match=r"stopped as it was imported \(SystemExit: 0\); nothing was recorded"):
        run(root, folder, market)
    assert registry.recorded(trials_file(root)) == []


def test_lines_edited_before_their_first_commit_count_as_their_run_wrote_them(lab, market, monkeypatch):
    root, folder = lab
    run(root, folder, market)
    commit(root, "registry", "registry/trials.jsonl")
    run(root, new_strategy(root, "demo-54-stripped"), market)
    path = trials_file(root)
    ran = path.read_text()
    stripped = [json.loads(text) for text in ran.splitlines()]
    for line in stripped[2:]:
        line.update(sharpe=None, monthly={})
    path.write_text("".join(registry.compact(line) + "\n" for line in stripped))   # its returns taken out, uncommitted
    with pytest.raises(RuntimeError, match="lost or edited"):
        run(root, new_strategy(root, "demo-55-next"), market)
    assert registry.main(["restore"], path) == 0 and path.read_text() == ran        # put back in place
    commit(root, "registry", "registry/trials.jsonl")
    fresh = root.parent.parent / "fresh"
    git("clone", "-q", str(root.parent), str(fresh), cwd=root)
    for where in (path, fresh / root.name / "registry" / "trials.jsonl"):
        assert len(registry.history(where)) == 4                                     # here and in any clone
    run(root, new_strategy(root, "demo-56-edited"), market)
    ran = path.read_text().splitlines()
    edit = json.loads(ran[-1])
    edit.update(sharpe=None, monthly={})
    path.write_text("\n".join([*ran[:-1], registry.compact(edit)]) + "\n")
    commit(root, "an edit committed", "registry/trials.jsonl")                     # the history keeps it
    assert registry.restore(path) == [ran[-1]] and registry.dropped(path) == []   # appended: nothing committed replaced
    key = next(t.key for t in registry.history(path) if t.key.startswith("demo-56-edited/1"))
    assert [t.sharpe for t in registry.history(path) if t.key == key] == [json.loads(ran[-1])["sharpe"]]
    commit(root, "the original back", "registry/trials.jsonl")
    rows = path.read_text().splitlines()
    rows[-2:] = rows[-1], rows[-2]                                     # the original moved before its edit
    path.write_text("\n".join(rows) + "\n")
    commit(root, "moved", "registry/trials.jsonl")
    assert run(root, new_strategy(root, "demo-68-after"), market).card == "demo-68-after"   # the clone that ran runs on
    other = root.parent.parent / "other"
    git("clone", "-q", str(root.parent), str(other), cwd=root)
    seen = []

    def spy(card, strategy, market, history, seed, **options):
        seen.extend(history)
        raise RuntimeError("stop here")

    monkeypatch.setattr(battery, "run", spy)
    there = other / root.name                                          # a clone that holds no copy of the lines
    with pytest.raises(report.Recorded, match="stop here"):
        run(there, new_strategy(there, "demo-60-other"), market)
    assert [t.sharpe for t in seen if t.key == key] == [json.loads(ran[-1])["sharpe"]]   # returns before none


@pytest.mark.parametrize("road", ["time", "copy", "variant", "added"])
def test_a_run_s_lines_changed_before_their_first_commit_count_as_written_in_every_clone(lab, market, road):
    """Edited with their time, changed copies put before them, a line's variant edited, or a line
    added under the card: gate 4 would read the change in any clone that holds no copy of the run's
    lines."""
    root, folder = lab
    run(root, folder, market)
    commit(root, "registry", "registry/trials.jsonl")
    run(root, new_strategy(root, f"demo-61-{road}"), market)
    path = trials_file(root)
    ran = path.read_text()
    rows = ran.splitlines()
    forged = [registry.compact({**json.loads(text), "sharpe": 1.5, "time": "2020-01-01T00:00:00Z" if road == "time"
                                else json.loads(text)["time"]}) for text in rows[-2:]]
    if road in ("time", "copy"):
        rows[-2:] = forged if road == "time" else [*forged, *rows[-2:]]
    elif road == "variant":
        rows[-1] = registry.compact({**json.loads(forged[-1]), "variant": 2})
    else:
        rows.append(registry.compact({**json.loads(forged[-1]), "variant": 5}))
    path.write_text("\n".join(rows) + "\n")
    with pytest.raises(RuntimeError, match="lost or edited"):
        run(root, new_strategy(root, f"demo-62-{road}"), market)
    assert registry.main(["restore"], path) == 0 and path.read_text() == ran     # as the run wrote them
    commit(root, "registry", "registry/trials.jsonl")
    fresh = root.parent.parent / f"fresh-{road}"
    git("clone", "-q", str(root.parent), str(fresh), cwd=root)
    sharpes = [json.loads(text)["sharpe"] for text in ran.splitlines()[-2:]]
    for where in (path, fresh / root.name / "registry" / "trials.jsonl"):
        assert [t.sharpe for t in registry.history(where) if t.key.startswith(f"demo-61-{road}/")] == sharpes


def test_lines_written_by_hand_for_a_run_that_wrote_none_stop_void_until_removed_then_the_run_is_voided(lab, market):
    root, folder = lab
    run(root, folder, market)
    commit(root, "registry", "registry/trials.jsonl")
    killed, path = new_strategy(root, "demo-69-killed"), trials_file(root)
    card_hash = report.card_hash_of(killed / "card.yaml")
    registry.record(card_hash, registry.now(), path)                    # its run began, and ended its process
    hand = [registry.compact({**json.loads(text), "card": "demo-69-killed", "card_hash": card_hash, "sharpe": 1.5})
            for text in path.read_text().splitlines()]
    path.write_text(path.read_text() + "".join(text + "\n" for text in hand))
    with pytest.raises(RuntimeError, match="written for its card by hand"):
        run(root, new_strategy(root, "demo-70-next"), market)
    assert registry.main(["void"], path) == 1 and registry.main(["restore"], path) == 1   # which it cannot tell
    path.write_text("".join(text + "\n" for text in path.read_text().splitlines() if text not in hand))
    assert registry.main(["void"], path) == 0 and registry.main(["restore"], path) == 0
    assert [line["void"] for line in registry.lines(path) if line["card"] == "demo-69-killed"] == [registry.LOST] * 2
    commit(root, "registry", "registry/trials.jsonl")
    fresh = root.parent.parent / "fresh-killed"
    git("clone", "-q", str(root.parent), str(fresh), cwd=root)
    for where in (path, fresh / root.name / "registry" / "trials.jsonl"):
        assert 1.5 not in [t.sharpe for t in registry.history(where)]
    assert run(root, new_strategy(root, "demo-71-after"), market).card == "demo-71-after"


def test_one_restore_puts_back_an_edit_and_a_lost_line_together(lab, market, capsys):
    root, folder = lab
    run(root, folder, market)
    path = trials_file(root)
    ran = path.read_text().splitlines()
    path.write_text(registry.compact({**json.loads(ran[0]), "sharpe": 1.5}) + "\n")   # one edited, one lost
    assert registry.main(["restore"], path) == 0
    assert path.read_text().splitlines() == ran
    assert "2 lines put back; commit registry/trials.jsonl at once, alone" in capsys.readouterr().out
    assert registry.restore(path) == [] and path.read_text().splitlines() == ran     # the run's own lines stay


def test_a_strategy_that_writes_a_registry_line_as_it_is_imported_never_reaches_its_gate_4(lab, market, monkeypatch):
    root, folder = lab
    run(root, folder, market)
    commit(root, "registry", "registry/trials.jsonl")
    seen = []

    def spy(card, strategy, market, history, seed, **options):
        seen.extend(t.key for t in history)
        raise RuntimeError("stop here")

    monkeypatch.setattr(battery, "run", spy)
    planted = registry.compact({"time": "2026-01-01T00:00:00Z", "card": "planted-01", "card_hash": "f" * 64,
                                "variant": 0, "sharpe": 3.0, "monthly": {"2020-01": 0.05}, "failed": None,
                                "survivor": False})
    writes = (f"from pathlib import Path\n_path = Path(__file__).resolve().parents[2] / 'registry' / 'trials.jsonl'\n"
              f"_path.write_text(_path.read_text() + {planted!r} + '\\n')\n" + STRATEGY)
    folder = new_strategy(root, "demo-63-writes", code=writes)
    with pytest.raises(report.Recorded, match="stop here"):
        run(root, folder, market)
    assert planted in trials_file(root).read_text() and seen and not [k for k in seen if k.startswith("planted-01")]


def test_a_strategy_that_rebinds_written_still_names_restore_when_its_lines_cannot_be_written(lab, market, monkeypatch):
    root, _ = lab
    monkeypatch.setattr(registry, "written", registry.written)
    monkeypatch.setattr(registry, "write", unwritable)                   # the clone's copy holds them
    blind = LAB_OF + STRATEGY.replace(FIRST_LINE, FIRST_LINE + '    LAB["lab.registry"].written = lambda *a, **k: []\n')
    folder = new_strategy(root, "demo-64-blind", code=blind)
    with pytest.raises(report.Recorded, match="changed the lab as it ran: lab.registry.written; the run is void, and its "
                                              "lines could not be written: this clone kept them, and python -m "
                                              "lab.registry restore puts them back"):
        run(root, folder, market)


def test_restore_waits_for_no_run(lab):
    root, _ = lab
    with registry.held(trials_file(root)):
        with pytest.raises(RuntimeError, match="a run is going in this clone"):
            registry.restore(trials_file(root))


class Warns:
    """A value whose copy raises a warning in the name of the runner, as pandas names the code that
    called it."""
    def __deepcopy__(self, memo):
        level, frame = 1, sys._getframe(1)
        while frame.f_globals.get("__name__") != "lab.report":
            frame, level = frame.f_back, level + 1
        warnings.warn("deprecated", DeprecationWarning, stacklevel=level + 1)
        return self


def test_a_warning_raised_as_the_lab_is_read_changes_nothing(monkeypatch):
    monkeypatch.setattr(report, "EXTRA", [Warns()], raising=False)       # read as the runner's own names are
    monkeypatch.delitem(vars(report), "__warningregistry__", raising=False)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        before = report.battery_code()                                  # the registry of warnings appears as it runs
        assert "__warningregistry__" in vars(report) and report.unchanged(before) == []
