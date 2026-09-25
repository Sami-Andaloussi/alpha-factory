"""The calibration's cases, each what it says it is: the planted edge pays the signal it plants,
and the selection null judges the best of its rules."""
import json
import sys

import numpy as np
import pandas as pd

from lab import battery, calibration, data, stats
from lab.data import Market
from tests.conftest import EIGHT, synthetic_market


def test_the_targets_and_bars_are_those_of_their_version():
    """Changing one is a versioned decision, like the battery's thresholds."""
    assert calibration.TARGETS == {"planted 0.5": 0.5, "planted 0.8": 0.8}
    assert (calibration.MAX_FALSE_PASS, calibration.MIN_POWER) == (0.05, 0.5)
    assert (calibration.CHOICES, calibration.REGISTRIES) == (10, (10, 30, 100))
    assert (calibration.RHO, calibration.SLOW_RHO, calibration.EVERY, calibration.SLOW_EVERY) == (0.95, 0.995, 5, 21)
    late = ("late slow timing", "rotation", "binary rotation", "top sector", "near benchmark")
    assert calibration.NULLS == ("timing", "slow timing", "selection", "slow selection", *late)
    assert calibration.KINDS == ("timing", "slow timing", "selection", "slow selection", "planted 0.5", "planted 0.8", *late)
    assert (calibration.LATE_START, calibration.EARLY, calibration.LATER) == ("2012-01-01", ("SPY", "QQQ"), ("XLRE", "XLC"))
    assert calibration.UNIVERSES == {"late slow timing": ("SPY", "XLRE", "XLC", "BTC-USD"),
                                     "rotation": ("SPY", "QQQ", "XLRE", "XLC"), "binary rotation": ("SPY", "QQQ", "XLRE", "XLC"),
                                     "top sector": calibration.SECTORS, "near benchmark": calibration.SECTORS}
    assert calibration.SECTORS == ("XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY")


def test_a_planted_return_pays_the_signal_of_two_sessions_before():
    """The rule reads the signal at the close of the day before, and holds through the day it pays."""
    market, _ = synthetic_market(30, tickers=EIGHT[:4])
    planted, signal = calibration.planted_market(market, 0.02, np.random.default_rng(1))
    added = planted.prices.pct_change() - market.prices.pct_change()
    expected = 0.02 * market.prices.pct_change().std() * signal.shift(2)
    pd.testing.assert_frame_equal(added.iloc[3:], expected.iloc[3:], rtol=1e-6, atol=1e-10)


def test_the_selection_null_judges_the_best_of_its_rules():
    market, _ = synthetic_market(31, tickers=EIGHT[:4])
    strategy, history = calibration.selected("selection", 0, market, np.random.default_rng(2))
    assert len(history) == calibration.CHOICES - 1
    assert calibration.appraisal(market, strategy, calibration.VARIANTS[0]) > max(t.sharpe for t in history)


def test_a_case_keeps_its_planted_strength_in_full():
    market, _ = synthetic_market(32, tickers=EIGHT[:4])
    strength = 0.0123456789012345
    row = calibration.case("planted 0.8", 0, market, {"planted 0.8": strength})
    assert row["strength"] == strength and row["case"] == "planted 0.8"
    assert row["passed"] == (row["failed"] == 0) == all(row[f"gate {n}"] for n in range(1, 8))


def test_the_results_keep_every_planted_strength_in_full(tmp_path):
    strength = 0.0123456789012345
    rows = [{"case": "planted 0.8", "draw": 0, "strength": strength, "passed": True, "Sharpe": 0.123456789},
            {"case": "timing", "draw": 0, "strength": 0.0, "passed": False, "Sharpe": -0.1}]
    calibration.save(rows, tmp_path / "results.csv")
    table = pd.read_csv(tmp_path / "results.csv")
    assert table["strength"].tolist() == [strength, 0.0] and table["Sharpe"].tolist() == [0.12346, -0.1]


def test_a_null_rule_is_the_rule_on_a_signal_of_its_own_persistence_reset_at_its_own_pace():
    market, _ = synthetic_market(34, tickers=EIGHT[:4])
    for kind, rho, every, flat in (("timing", calibration.RHO, calibration.EVERY, False),
                                   ("slow timing", calibration.SLOW_RHO, calibration.SLOW_EVERY, True),
                                   ("slow selection", calibration.SLOW_RHO, calibration.SLOW_EVERY, True)):
        strategy = calibration.null_rule(kind, market, np.random.default_rng(5))
        signal = calibration.latent(market.prices.index, market.prices.columns, np.random.default_rng(5), rho)
        pd.testing.assert_frame_equal(strategy(market), calibration.rule(signal, every, flat=flat)(market))


def test_the_rule_reads_the_market_up_to_the_day_before():
    market, _ = synthetic_market(33, tickers=EIGHT[:4])
    signal = calibration.latent(market.prices.index, market.prices.columns, np.random.default_rng(3))
    strategy = calibration.rule(signal)
    for day in market.prices.index[[300, 1500, 3000]]:                  # sessions where it sets a target
        seen = market.asof(day)
        cut = strategy(seen).loc[[day]]
        assert cut.notna().all(axis=None)
        assert battery.same_rows(strategy(battery.scrambled(seen, [], np.random.default_rng(4))).loc[[day]], cut)


def test_each_case_is_judged_with_the_draws_of_its_kind_and_its_number(monkeypatch):
    market, _ = synthetic_market(35, tickers=EIGHT[:4])
    seeds = {}

    def judged(card, strategy, market, history=(), seed=0):
        seeds[card.id] = seed
        held = {"neighbours that hold the base": ["span=8", "span=12"]} if card.id.startswith("slow") else {}
        return battery.Verdict(card.id, [battery.Gate(n, name, False, "not run", held if n == 6 else {})
                                         for n, name in battery.GATES.items()], [], {})

    monkeypatch.setattr(calibration.battery, "run", judged)
    rows = [calibration.case(kind, 3, market, {}) for kind in ("timing", "slow timing")]
    assert seeds == {f"{kind}-3": int(np.random.SeedSequence([calibration.KINDS.index(kind), 3]).generate_state(1)[0])
                     for kind in ("timing", "slow timing")}
    assert len(set(seeds.values())) == 2
    assert [row["neighbours holding the base"] for row in rows] == [0, 2]    # what gate 6 names, counted


def test_the_power_against_a_registry_reads_the_weaker_of_the_edge_and_its_blend():
    rng = np.random.default_rng(6)
    strong, weak = pd.Series(rng.normal(0.001, 0.01, 3000)), pd.Series(rng.normal(0.0002, 0.01, 3000))
    verdict = battery.Verdict("x", [], [], {"edge": strong, "blend edge": weak})
    assert calibration.against(verdict, 30) == stats.dsr(weak, 30, 1 / 3000) < stats.dsr(strong, 30, 1 / 3000)


def test_the_planted_strength_is_searched_until_its_ratio_is_within_a_hundredth_of_its_target():
    market, _ = synthetic_market(36, tickers=EIGHT[:4])
    strength = calibration.strength_for(market, 2.5, draws=4)          # its first step lands 0.017 away
    rng = np.random.default_rng(7)                                     # the search's own draws
    ratios = []
    for _ in range(4):
        planted, signal = calibration.planted_market(market, strength, rng)
        ratios.append(calibration.appraisal(planted, calibration.rule(signal), calibration.VARIANTS[0]))
    assert abs(np.mean(ratios) - 2.5) < 0.01


def late_starts(tickers=("SPY", "QQQ", "XLRE", "XLC", "BTC-USD")):
    """A market of the late nulls' assets, whose later ones start as they do in the snapshot."""
    market, _ = synthetic_market(40, tickers=tickers)
    prices = market.prices.copy()
    for ticker, first in (("XLRE", "2016-09-19"), ("XLC", "2018-06-19"), ("BTC-USD", "2014-09-17")):
        if ticker in tickers:
            prices.loc[prices.index < first, ticker] = np.nan
    return Market(prices, prices.notna(), market.rf, prices)


def test_the_rotation_is_always_fully_invested_and_holds_the_later_funds_once_they_trade():
    market = battery.restrict(late_starts(), calibration.EARLY + calibration.LATER)
    for binary in (False, True):
        weights = calibration.rotation(3, binary)(market, span=10)
        targets = weights.dropna(how="all")
        assert targets.index.equals(weights.index[::20]) and np.allclose(targets.sum(axis=1), 1.0)
        assert (targets.loc[:"2016-09-16", ["XLRE", "XLC"]] == 0).all(axis=None)
        assert (targets.loc[:"2018-06-18", "XLC"] == 0).all()
        later = targets.loc["2019":, ["XLRE", "XLC"]]
        if binary:                                                     # all on one side, a coin's toss
            assert set(targets.loc["2019":, "SPY"].round(12)) == {0.0, 0.5} and set(later["XLRE"].round(12)) == {0.0, 0.5}
            assert 0.35 < (targets.loc["2019":, "SPY"] > 0).mean() < 0.65
        else:
            assert (later > 0).all(axis=None) and targets.loc["2019":, "SPY"].std() > 0.1
        for day in (targets.index[150], targets.loc["2020":].index[5]):   # it reads nothing it could not know
            assert battery.same_rows(calibration.rotation(3, binary)(market.asof(day), span=10).loc[[day]],
                                     weights.loc[[day]])
        assert not battery.same_rows(calibration.rotation(3, binary)(market, span=15), weights)   # its span moves it


def test_the_top_rule_holds_the_assets_that_trade_with_the_highest_signal_in_equal_parts():
    market = late_starts()
    signal = calibration.latent(market.prices.index, market.prices.columns, np.random.default_rng(2), calibration.SLOW_RHO)
    weights = calibration.top(signal, k=2)(market, span=10)
    targets = weights.dropna(how="all")
    assert targets.index.equals(weights.index[::calibration.SLOW_EVERY])
    score = signal.ewm(span=10).mean().shift(1).where(market.tradable)
    for day, row in targets.iloc[1:].iterrows():
        best = score.loc[day].nlargest(2).index
        assert set(row[row > 0].index) == set(best) and np.allclose(row[best], 0.5)
    assert (targets.loc[:"2014-09-16", "BTC-USD"] == 0).all()
    day = targets.index[100]                                           # it reads nothing it could not know
    assert battery.same_rows(calibration.top(signal, k=2)(market.asof(day), span=10).loc[[day]], weights.loc[[day]])


def test_the_top_rule_with_a_negative_count_leaves_out_the_lowest_signal_of_those_that_trade_that_day():
    market, _ = synthetic_market(40, tickers=("SPY", "QQQ", "GLD", "EFA"))
    prices = market.prices.copy()
    first = prices.index[calibration.SLOW_EVERY * 50]                  # EFA starts on a reset
    prices.loc[prices.index < first, "EFA"] = np.nan
    market = Market(prices, prices.notna(), market.rf, prices)
    signal = calibration.latent(market.prices.index, market.prices.columns, np.random.default_rng(4), calibration.RHO)
    targets = calibration.top(signal, -1)(market, span=10).dropna(how="all")
    score = signal.ewm(span=10).mean().shift(1).where(market.tradable)
    for day, row in targets.iloc[1:].iterrows():
        trading = market.tradable.loc[day]
        assert set(row[row > 0].index) == set(trading[trading].index) - {score.loc[day].idxmin()}
        assert np.allclose(row[row > 0], 1 / (trading.sum() - 1))
    assert targets.loc[first].gt(0).sum() == 3                         # four trade that day


def test_the_late_nulls_run_on_their_own_universes_from_2012(monkeypatch):
    market = late_starts()
    judged = {}

    def run(card, strategy, market, history=(), seed=0):
        judged[card.id] = (card, battery.targets(strategy, market.window(*card.in_sample), card.variants[0]))
        return battery.Verdict(card.id, [battery.Gate(n, name, False, "not run") for n, name in battery.GATES.items()],
                               [], {})

    monkeypatch.setattr(calibration.battery, "run", run)
    sectors = late_starts(calibration.SECTORS)
    for kind in ("late slow timing", "rotation", "binary rotation"):
        calibration.case(kind, 0, market, {})
    calibration.case("top sector", 0, sectors, {})
    calibration.case("near benchmark", 0, sectors, {})
    (late, slow), (rotation, _) = judged["late slow timing-0"], judged["rotation-0"]
    for kind in calibration.LATE:
        assert judged[f"{kind}-0"][0].universe == calibration.UNIVERSES[kind]
        assert judged[f"{kind}-0"][0].in_sample == ("2012-01-01", "2022-12-31")
    coin = judged["binary rotation-0"][1].dropna(how="all")
    assert set(coin.loc["2019":, "SPY"].round(12)) == {0.0, 0.5}
    held = judged["top sector-0"][1]
    rng, own = np.random.default_rng([calibration.KINDS.index("top sector"), 0]), battery.restrict(sectors, calibration.SECTORS)
    signal = calibration.latent(own.prices.index, own.prices.columns, rng, calibration.SLOW_RHO)   # the slow signal
    pd.testing.assert_frame_equal(held, battery.targets(calibration.top(signal), own.window("2012-01-01", "2022-12-31"),
                                                        calibration.VARIANTS[0]))
    rng = np.random.default_rng([calibration.KINDS.index("near benchmark"), 0])
    signal = calibration.latent(own.prices.index, own.prices.columns, rng, calibration.RHO)      # the fast signal
    near = judged["near benchmark-0"][1]                               # all the sectors that trade but one, monthly
    pd.testing.assert_frame_equal(near, battery.targets(calibration.top(signal, -1, calibration.SLOW_EVERY),
                                                        own.window("2012-01-01", "2022-12-31"), calibration.VARIANTS[0]))
    monthly = near.dropna(how="all")
    assert set(np.diff(near.index.get_indexer(monthly.index))) == {calibration.SLOW_EVERY}
    assert (monthly.gt(0).sum(axis=1) == own.tradable.loc[monthly.index].sum(axis=1) - 1).iloc[1:].all()   # never all
    one = held.dropna(how="all")
    assert set(np.diff(held.index.get_indexer(one.index))) == {calibration.SLOW_EVERY}
    assert (one.gt(0).sum(axis=1).iloc[1:] == 1).all()
    set_on = slow.dropna(how="all")                                    # the slow rule: equal parts, every 21 sessions
    assert set(np.diff(slow.index.get_indexer(set_on.index))) == {calibration.SLOW_EVERY}
    assert all(len(set(row[row > 0].round(12))) <= 1 for _, row in set_on.iterrows())


class Serial:
    """The pool of processes, run in this one."""
    def __init__(self, workers, initializer=None):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *error):
        return False

    def map(self, work, jobs, chunksize=1):
        return map(work, jobs)


def test_main_writes_its_table_and_draws_the_notebook_only_from_the_lab_s_own(tmp_path, monkeypatch):
    passing = {kind: kind.startswith("planted") for kind in calibration.KINDS}
    monkeypatch.setattr(calibration.data, "load", lambda: None)
    restricted = []
    monkeypatch.setattr(calibration.battery, "restrict", lambda market, tickers: restricted.append(tuple(tickers)))
    monkeypatch.setattr(calibration, "strength_for", lambda market, target: 0.01)
    monkeypatch.setattr(calibration, "ProcessPoolExecutor", Serial)
    monkeypatch.setattr(calibration, "_case", lambda job: {"case": job[0], "draw": job[1], "strength": 0.01,
                                                          "passed": passing[job[0]], "Sharpe": 0.5})
    drawn = []
    monkeypatch.setattr(calibration, "execute", drawn.append)
    monkeypatch.setattr(calibration, "RESULTS", tmp_path / "results.csv")
    elsewhere = tmp_path / "elsewhere" / "results.csv"
    monkeypatch.setattr(sys, "argv", ["calibration", "--draws", "2", "--workers", "1", "--out", str(elsewhere)])
    assert calibration.main() == 0
    table = pd.read_csv(elsewhere)
    assert len(table) == 2 * len(calibration.KINDS) and table["passed"].tolist() == [passing[k] for k in table["case"]]
    assert drawn == [] and restricted == [calibration.CALIBRATED]      # the market the calibration ran on
    monkeypatch.setattr(sys, "argv", ["calibration", "--draws", "2", "--workers", "1"])
    assert calibration.main() == 0
    assert (tmp_path / "results.csv").exists() and drawn == [calibration.NOTEBOOK]
    for null in [kind for kind in calibration.KINDS if not kind.startswith("planted")]:
        passing[null] = True                                            # any null that passes fails the calibration
        assert calibration.main() == 1, null
        passing[null] = False


def test_the_calibration_runs_on_the_twenty_assets_of_its_snapshot():
    """The universe gained Treasury funds after the calibration ran: a case run again must see the
    market its row was computed on."""
    manifest = json.loads((data.DATA / "manifest.json").read_text())
    assert calibration.CALIBRATED == tuple(manifest["tickers"]) and len(calibration.CALIBRATED) == 20
