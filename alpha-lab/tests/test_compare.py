"""lab.compare: the battery's own figures, over the battery's own sessions, and no comparison of a
card that has not run as it stands."""
import json
import subprocess

import numpy as np
import pandas as pd
import pytest
import yaml

from lab import battery, compare, costs, report, stats
from tests.conftest import CLUSTERS, EIGHT, signal_strategy, synthetic_market

CARD = battery.Card("synthetic-01", EIGHT, ({"span": 10, "wait": 0}, {"span": 20, "wait": 800}),
                    {"span": {25: [8, 12], 50: [5, 15]}})


def waiting(signal):
    """signal_strategy, with no target before session `wait`: a variant that first holds later."""
    rule = signal_strategy(signal)

    def positions(market, span=10, every=5, wait=0):
        out = rule(market, span, every)
        out.iloc[:wait] = np.nan
        return out
    return positions


def equal_parts(market):
    trading = market.tradable.astype(float)
    weights = trading.div(trading.sum(axis=1), axis=0).fillna(0.0)
    out = weights * np.nan
    out.iloc[::21] = weights.iloc[::21]
    return out


@pytest.fixture(scope="module")
def judged():
    market, signal = synthetic_market(2, beta=0.5)
    rule = waiting(signal)
    verdict = battery.run(CARD, rule, market, seed=3, crypto=frozenset(), cluster=CLUSTERS.get)
    inside = battery.restrict(market, CARD.universe).window(*CARD.in_sample)
    return inside, rule, verdict


def test_the_figures_are_the_battery_s_own(judged):
    inside, rule, verdict = judged
    start = battery.first_held(battery.targets(rule, inside, CARD.variants[0]))
    for k, parameters in enumerate(CARD.variants):
        result = compare.difference(inside, rule, dict(parameters), equal_parts, {}, CARD.in_sample[1], start,
                                    crypto=frozenset())
        assert result["from"] == start                                    # the base's first session held, for every variant
        assert np.isclose(result["appraisal ratio"], verdict.trials[k].sharpe, rtol=0, atol=1e-12)
        if k == 0:
            assert np.isclose(result["alpha"], verdict.gates[1].figures["alpha"], rtol=0, atol=1e-12)


def test_a_later_variant_is_counted_from_the_base_s_first_holding(judged):
    inside, rule, verdict = judged
    own = compare.difference(inside, rule, dict(CARD.variants[1]), equal_parts, {}, CARD.in_sample[1],
                             crypto=frozenset())
    assert own["from"] > battery.first_held(battery.targets(rule, inside, CARD.variants[0]))
    assert not np.isclose(own["appraisal ratio"], verdict.trials[1].sharpe, rtol=0, atol=1e-6)


def test_the_difference_and_its_error(judged):
    inside, rule, _ = judged
    result = compare.difference(inside, rule, {"span": 10}, equal_parts, {}, CARD.in_sample[1], crypto=frozenset())
    assert abs(result["reference alpha"]) < 1e-12                          # the benchmark itself has no alpha
    assert np.isclose(result["difference"], result["alpha"] - result["reference alpha"], rtol=0, atol=1e-12)
    assert result["difference"] > 2 * result["standard error"] > 0          # the planted edge shows
    # the error, computed apart: the hedged gap compounded by calendar month, its spread over the years
    period = slice(result["from"], pd.Timestamp(CARD.in_sample[1]))
    hedged = []
    for positions in (battery.targets(rule, inside, {"span": 10}), battery.targets(equal_parts, inside, {})):
        mine = battery.excess(battery.at_cost(inside, positions, frozenset()), inside.rf, period)
        bench = battery.excess(costs.benchmark(inside, positions, 1, frozenset()), inside.rf, period)
        hedged.append(stats.hedged(mine, bench))
    gap = hedged[0] - hedged[1]
    months = (1 + gap).groupby([gap.index.year, gap.index.month]).prod() - 1
    years = len(gap) / 252
    assert np.isclose(result["standard error"], months.std(ddof=1) * np.sqrt(12) / np.sqrt(years), rtol=1e-12)


def test_a_rule_against_itself_differs_by_nothing(judged):
    inside, rule, _ = judged
    result = compare.difference(inside, rule, {}, rule, {}, CARD.in_sample[1], crypto=frozenset())
    assert result["difference"] == 0.0 and result["standard error"] == 0.0
    assert result["alpha"] == result["reference alpha"]
    assert result["ratio difference"] == 0.0 and result["ratio difference's standard error"] == 0.0


def test_the_ratio_difference_and_its_error_come_from_paired_months():
    """Two independent hedged series with no edge, thirteen years: each ratio is measured to about
    1/sqrt(13), their difference to about sqrt(2/13), from draws of whole months, repeatable."""
    rng = np.random.default_rng(4)
    days = pd.bdate_range("2010-01-01", periods=13 * 252)
    h = pd.Series(rng.normal(0.0, 0.003, len(days)), index=days)
    rh = pd.Series(rng.normal(0.0, 0.004, len(days)), index=days)
    gap, error = compare.ratio_difference(h, rh)
    assert gap == pytest.approx(stats.sharpe(h) - stats.sharpe(rh), rel=1e-12)
    assert 0.8 * np.sqrt(2 / 13) < error < 1.2 * np.sqrt(2 / 13)
    assert compare.ratio_difference(h, rh) == (gap, error)                   # a fixed seed
    together, apart = compare.ratio_difference(h, h + rh / 4)[1], error      # correlated series differ less
    assert together < apart / 2


def test_a_reference_that_holds_later_is_refused(judged):
    inside, rule, _ = judged
    with pytest.raises(ValueError, match="after the rule's"):
        compare.difference(inside, rule, {}, rule, {"wait": 800}, CARD.in_sample[1], crypto=frozenset())


def git(*args, cwd):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=True).stdout.strip()


@pytest.fixture
def lab(tmp_path, monkeypatch):
    """A card that ran: its folder in a strategies/ of its own repository, its line in a registry."""
    folder = tmp_path / "strategies" / "A-1-01-x"
    folder.mkdir(parents=True)
    (folder / "card.yaml").write_text("id: A-1-01-x\n")
    (folder / "strategy.py").write_text("def positions(market):\n    return None\n")
    git("init", "-q", cwd=tmp_path)
    git("-c", "user.name=t", "-c", "user.email=t@t", "add", ".", cwd=tmp_path)
    git("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "run", cwd=tmp_path)
    monkeypatch.setattr(compare, "STRATEGIES", folder.parent)
    line = {"card": "A-1-01-x", "card_hash": report.card_hash_of(folder / "card.yaml"),
            "commit": git("rev-parse", "HEAD", cwd=tmp_path)}
    return folder, [json.loads(json.dumps(line))]


def test_a_card_that_ran_as_it_stands_is_read(lab):
    folder, lines = lab
    assert compare.ran(folder, lines) is None


def test_a_card_that_has_not_run_is_refused(lab):
    folder, lines = lab
    assert "not in the registry" in compare.ran(folder, [])


def test_a_card_edited_after_its_run_is_refused(lab):
    folder, lines = lab
    (folder / "card.yaml").write_text("id: A-1-01-x\nvariants: [{lookback: 60}]\n")
    assert "differs from the one that ran" in compare.ran(folder, lines)


def test_a_strategy_edited_after_its_run_is_refused(lab):
    folder, lines = lab
    (folder / "strategy.py").write_text("def positions(market):\n    return 1\n")
    assert "strategy changed" in compare.ran(folder, lines)


def test_a_copy_outside_the_lab_s_strategies_is_refused(lab, tmp_path):
    folder, lines = lab
    copy = tmp_path / "elsewhere" / "strategies" / folder.name
    copy.parent.mkdir(parents=True)
    copy.mkdir()
    for name in ("card.yaml", "strategy.py"):
        (copy / name).write_text((folder / name).read_text())
    assert "lab's own strategies/" in compare.ran(copy, lines)


def test_a_run_without_a_recorded_commit_is_refused(lab):
    folder, lines = lab
    assert "not recorded" in compare.ran(folder, [{**lines[0], "commit": None}])


def test_the_command_refuses_before_it_loads_any_data(capsys, monkeypatch):
    def load(*args, **kwargs):
        raise AssertionError("data loaded")
    monkeypatch.setattr(compare.data, "load", load)
    strategies = compare.STRATEGIES
    code = compare.main([str(strategies / "TM-002-01-sector-52-week-high"), str(strategies / "TM-003-01-sector-momentum"),
                         "--variant", "5", "--reference-variant", "-1"])
    err = capsys.readouterr().err
    assert code == 1 and "--variant 5" in err and "--reference-variant -1" in err
    code = compare.main([str(strategies / "TM-002-01-sector-52-week-high"), str(strategies / "CA-001-01-momentum-within-groups")])
    assert code == 1 and "same universe" in capsys.readouterr().err
    code = compare.main([str(strategies / "no-such-card"), str(strategies / "TM-003-01-sector-momentum")])
    assert code == 1 and "refused:" in capsys.readouterr().err


def test_the_same_funds_in_another_order_are_refused(tmp_path, monkeypatch, capsys):
    source = compare.STRATEGIES / "TM-003-01-sector-momentum"
    cards = {}
    for name, order in (("A-1-01-a", None), ("B-1-01-b", "reversed")):
        spec = yaml.safe_load((source / "card.yaml").read_text())
        spec["id"] = name
        if order:
            spec["universe"] = list(reversed(spec["universe"]))
        folder = tmp_path / "strategies" / name
        folder.mkdir(parents=True)
        (folder / "card.yaml").write_text(yaml.safe_dump(spec, sort_keys=False))
        cards[name] = folder
    monkeypatch.setattr(compare, "ran", lambda folder, lines: None)
    monkeypatch.setattr(compare.data, "load", lambda *a, **k: (_ for _ in ()).throw(AssertionError("data loaded")))
    assert compare.main([str(cards["A-1-01-a"]), str(cards["B-1-01-b"])]) == 1
    assert "same order" in capsys.readouterr().err
