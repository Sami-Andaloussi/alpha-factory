"""The battery, gate by gate: each decision on both sides of its thresholds, and each computation on
synthetic markets where the truth is known."""
from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest

from lab import battery, calibration, costs, data, engine, stats
from lab.data import Market
from tests.conftest import CLUSTERS, EIGHT, real_snapshot, signal_strategy, synthetic_market

NEIGHBOURS = {"span": {25: [8, 12], 50: [5, 15]}}
CARD = battery.Card("synthetic-01", EIGHT, ({"span": 10}, {"span": 20}), NEIGHBOURS)
NO_CRYPTO = frozenset()


def judge(strategy, market, card=CARD, history=(), crypto=NO_CRYPTO):
    return battery.run(card, strategy, market, history, seed=3, crypto=crypto, cluster=CLUSTERS.get)


def momentum(read):
    """A momentum rule that reads its returns `read` sessions late: 1 is clean, 0 reads the bar it
    trades on, -1 reads tomorrow."""
    def positions(market, span=10, every=5):
        score = market.signal_prices.pct_change().ewm(span=span).mean().shift(read).clip(lower=0).fillna(0.0)
        total = score.sum(axis=1)
        weights = score.div(total.where(total > 0), axis=0).fillna(0.0)
        out = weights * np.nan
        out.iloc[::every] = weights.iloc[::every]
        return out
    return positions


def card(ident, variants, choose=False, universe=EIGHT):
    return battery.Card(ident, universe, variants, NEIGHBOURS, choose=choose)


@pytest.fixture(scope="module")
def planted():
    market, signal = synthetic_market(1, beta=0.08)
    return market, signal_strategy(signal), signal


@pytest.fixture(scope="module")
def verdict(planted):
    return judge(planted[1], planted[0])


# --------------------------------------------------------------------------- the thresholds

def test_the_thresholds_are_those_of_their_version():
    """Changing a threshold is a versioned decision: this test changes with THRESHOLDS."""
    assert battery.THRESHOLDS == 2
    assert (battery.IN_SAMPLE, battery.HOLDOUT) == (("2005-01-01", "2022-12-31"), ("2023-01-01", "2025-12-31"))
    assert [b[0][:4] + "-" + b[1][:4] for b in battery.BLOCKS] == ["2005-2007", "2008-2009", "2010-2014",
                                                                   "2015-2019", "2020-2022"]
    assert (battery.CHECKED_DATES, battery.HOLDOUT_CHECKED_DATES, battery.MIN_DECISIONS) == (50, 10, 30)
    assert (battery.MIN_YEARS, battery.MIN_YEARS_CRYPTO) == (5, 4)
    assert (battery.MIN_SHARPE, battery.MIN_SHARPE_DOUBLED, battery.MAX_COST_SHARE) == (0.4, 0.3, 1 / 3)
    assert (battery.MIN_PSR, battery.PLACEBOS, battery.MIN_BEATEN, battery.MIN_SHIFT) == (0.95, 1000, 0.90, 252)
    assert battery.MIN_DSR == 0.90
    assert (battery.MIN_POSITIVE_BLOCKS, battery.MIN_BLOCK_SESSIONS, battery.MIN_WFE,
            battery.WALK_FORWARD_START) == (3, 126, 0.5, 3)
    assert (battery.NEIGHBOUR_MEDIAN, battery.NEIGHBOUR_FLOOR, battery.CLUSTER_OUT) == (0.7, 0.5, 0.5)
    assert (battery.MAX_ASSET_SHARE, battery.DELAY_KEEP, battery.MAX_CORRELATION) == (0.30, 0.7, 0.7)
    assert (battery.WINDOW, battery.BOOTSTRAPS, battery.PERCENTILE, battery.MEAN_BLOCK) == (630, 1000, 10, 21)
    assert (stats.NEAR_CLONE, stats.LO_LAGS) == (0.9, 10)


# --------------------------------------------------------------------------- the decisions

def decided(decide, figures, **change):
    return decide({**figures, **change}).passed


GATE_1 = {"dates checked": 200, "look-ahead breaks": 0, "same-day breaks": 0, "data problems": [],
          "clustered decisions": 30, "years in-sample": 5.0, "years needed": 5}
GATE_2 = {"Sharpe": 0.4, "benchmark Sharpe": 0.4, "alpha": 1e-9, "Sharpe at 2x costs": 0.3, "alpha at 2x costs": 1e-9,
          "gross Sharpe": 3.0, "costs in Sharpe units": 1.0}
GATE_3 = {"PSR": 0.95, "placebo sessions": 3000, "placebos": 1000, "placebos beaten": 0.9}
GATE_4 = {"trials": 3, "effective trials": 2, "appraisal ratio": 1.0, "Sharpe expected by luck": 0.5, "DSR": 0.9}
GATE_5 = {"blend passes gate 2": True, "blend passes gate 3": True, "blend passes gate 4": True,
          "worst variant Sharpe": 1e-9, "positive blocks": 3, "best year": 2010, "alpha without the best year": 1e-9,
          "walk-forward efficiency": 0.5}
GATE_6 = {"neighbour median ratio": 0.7, "lowest ±25% ratio": 0.5, "worst cluster out": "a",
          "worst cluster out ratio": 0.5, "largest P&L share": 0.3, "asset with the largest share": "S1",
          "gate 2 without bitcoin": True, "one day late ratio": 0.7, "highest correlation with a survivor": 0.7,
          "survivor most correlated": "old-01/0", "neighbours that hold the base": []}
GATE_7 = {"holdout Sharpe": 0.5, "Sharpe floor": 0.5, "holdout alpha": 0.01, "alpha floor": 0.01,
          "variants rewritten": 0, "dates checked": 40, "look-ahead breaks": 0, "same-day breaks": 0, "data problems": []}
NAN, TINY = float("nan"), 1e-9


def test_gate_one_passes_on_its_thresholds_and_fails_beyond_each():
    decide = battery.decide_hygiene
    assert decided(decide, GATE_1)
    for change in ({"look-ahead breaks": 1}, {"same-day breaks": 1}, {"data problems": ["S1 has no price"]},
                   {"clustered decisions": 29}, {"years in-sample": 5 - TINY}, {"years needed": 6},
                   {"clustered decisions": NAN}, {"years in-sample": NAN}):
        assert not decided(decide, GATE_1, **change), change
    assert "the data: S1 has no price" in decide({**GATE_1, "data problems": ["S1 has no price"]}).reason


def test_gate_two_passes_on_its_thresholds_and_fails_beyond_each():
    decide = battery.decide_economic
    assert decided(decide, GATE_2)
    for change in ({"Sharpe": 0.4 - TINY, "benchmark Sharpe": 0.0}, {"benchmark Sharpe": 0.4 + TINY}, {"alpha": 0.0},
                   {"Sharpe at 2x costs": 0.3 - TINY}, {"alpha at 2x costs": 0.0}, {"gross Sharpe": 0.0},
                   {"costs in Sharpe units": 1.0 + 1e-6}, {"Sharpe": NAN}):
        assert not decided(decide, GATE_2, **change), change


def test_gate_three_passes_on_its_thresholds_and_fails_beyond_each():
    decide = battery.decide_significance
    assert decided(decide, GATE_3)
    for change in ({"PSR": 0.95 - TINY}, {"PSR": NAN}, {"placebos beaten": 0.9 - TINY}, {"placebos beaten": None}):
        assert not decided(decide, GATE_3, **change), change
    assert "too short" in decide({**GATE_3, "placebos beaten": None}).reason


def test_gate_four_passes_on_its_threshold_and_fails_beyond_it():
    decide = battery.decide_multiple_testing
    assert decided(decide, GATE_4)
    assert not decided(decide, GATE_4, DSR=0.9 - TINY)
    assert not decided(decide, GATE_4, DSR=NAN)


def test_gate_five_passes_on_its_thresholds_and_fails_beyond_each():
    decide = battery.decide_stability
    assert decided(decide, GATE_5)
    assert decided(decide, {k: v for k, v in GATE_5.items() if k != "walk-forward efficiency"})
    for change in ({"blend passes gate 2": False}, {"blend passes gate 3": False}, {"blend passes gate 4": False},
                   {"worst variant Sharpe": 0.0}, {"positive blocks": 2}, {"alpha without the best year": 0.0},
                   {"walk-forward efficiency": 0.5 - TINY}, {"alpha without the best year": NAN},
                   {"worst variant Sharpe": NAN}, {"walk-forward efficiency": NAN}):
        assert not decided(decide, GATE_5, **change), change
    two = decide({**GATE_5, "blend passes gate 2": False, "blend passes gate 4": False}).reason
    assert "fails gates 2 and 4" in two


def test_gate_six_passes_on_its_thresholds_and_fails_beyond_each():
    decide = battery.decide_robustness
    assert decided(decide, GATE_6)
    nothing_to_move = {"neighbour median ratio": None, "lowest ±25% ratio": None, "worst cluster out": None,
                       "worst cluster out ratio": None, "highest correlation with a survivor": None}
    assert decided(decide, GATE_6, **nothing_to_move)
    for change in ({"neighbour median ratio": 0.7 - TINY}, {"lowest ±25% ratio": 0.5 - TINY},
                   {"worst cluster out ratio": 0.5 - TINY}, {"largest P&L share": 0.3 + TINY},
                   {"largest P&L share": None}, {"gate 2 without bitcoin": False},
                   {"neighbours that hold the base": ["k=1.5"]},
                   {"one day late ratio": 0.7 - TINY}, {"highest correlation with a survivor": 0.7 + TINY},
                   {"neighbour median ratio": NAN}, {"lowest ±25% ratio": NAN}, {"worst cluster out ratio": NAN},
                   {"largest P&L share": NAN}, {"one day late ratio": NAN},
                   {"highest correlation with a survivor": NAN}):
        assert not decided(decide, GATE_6, **change), change


def test_gate_seven_passes_on_its_thresholds_and_fails_beyond_each():
    decide = battery.decide_holdout
    assert decided(decide, GATE_7)
    for change in ({"holdout Sharpe": 0.5 - TINY}, {"holdout alpha": 0.01 - TINY}, {"variants rewritten": 1},
                   {"look-ahead breaks": 1}, {"same-day breaks": 1}, {"data problems": ["S3 has no price"]},
                   {"holdout Sharpe": NAN}, {"holdout alpha": NAN}, {"Sharpe floor": NAN}):
        assert not decided(decide, GATE_7, **change), change
    assert "the holdout's data: S3 has no price" in decide({**GATE_7, "data problems": ["S3 has no price"]}).reason


# --------------------------------------------------------------------------- the whole battery

def test_a_planted_edge_passes_gates_one_to_seven(verdict):
    assert verdict.failed is None, [g.reason for g in verdict.gates if not g.passed]


def test_every_gate_is_computed_and_the_verdict_is_the_first_failed():
    market, signal = synthetic_market(2)
    verdict = judge(signal_strategy(signal), market)
    assert [g.number for g in verdict.gates] == [1, 2, 3, 4, 5, 6, 7]
    assert all(g.passed is not None and g.reason for g in verdict.gates)
    assert verdict.failed == next(g.number for g in verdict.gates if not g.passed)
    assert verdict.failed in (2, 3)  # no edge: it earns nothing beyond what exposure pays
    positive = sum(1 for a in verdict.evidence["blocks"].values() if a is not None and a > 0)
    assert verdict.gates[4].figures["positive blocks"] == positive < len(battery.BLOCKS)


def test_each_figure_comes_from_the_run_it_names(planted, verdict):
    market, strategy, _ = planted
    gates, ev = {g.number: g.figures for g in verdict.gates}, verdict.evidence
    inside = market.window(*battery.IN_SAMPLE)
    base = battery.targets(strategy, inside, {"span": 10})
    period = slice(battery.first_holding(base), pd.Timestamp(battery.IN_SAMPLE[1]))
    # gate 1: fifty dates where each variant sets a target and fifty where it holds; years from the first holding
    assert gates[1]["dates checked"] == 2 * 2 * battery.CHECKED_DATES
    assert gates[1]["years in-sample"] == len(inside.prices.loc[period]) / battery.PERIODS
    # gate 2: doubled costs cost something, and the gross Sharpe ratio is before costs
    assert gates[2]["Sharpe at 2x costs"] < gates[2]["Sharpe"] < gates[2]["gross Sharpe"]
    # gate 4 deflates the edge, hedged of the benchmark; the registry keeps the same figure
    edge = stats.hedged(ev["excess"], ev["benchmark excess"])
    assert gates[4]["appraisal ratio"] == pytest.approx(stats.sharpe(edge), rel=1e-12)
    assert gates[4]["appraisal ratio"] != pytest.approx(gates[2]["Sharpe"], rel=1e-3)
    assert verdict.trials[0].sharpe == pytest.approx(gates[4]["appraisal ratio"], rel=1e-12)
    # gate 5: the best year is the year of the largest edge, and the alpha is measured without it
    x, b = ev["excess"], ev["benchmark excess"]
    best = gates[5]["best year"]
    assert best == ev["edge by year"].idxmax()
    assert gates[5]["alpha without the best year"] == pytest.approx(
        stats.alpha(x[x.index.year != best], b[b.index.year != best]), rel=1e-12)
    # gate 6: the floor looks at the ±25% neighbours; one day late moves the targets a session
    assert gates[6]["lowest ±25% ratio"] == min(ev["neighbours"]["span=8"], ev["neighbours"]["span=12"])
    assert abs(gates[6]["one day late ratio"] - 1) > 1e-6
    # gate 7 judges the holdout's own returns
    whole = market.window(battery.IN_SAMPLE[0], battery.HOLDOUT[1])
    result = battery.at_cost(whole, battery.targets(strategy, whole, {"span": 10}), NO_CRYPTO)
    sealed = battery.excess(result, whole.rf, slice(pd.Timestamp(battery.HOLDOUT[0]), None))
    assert gates[7]["holdout Sharpe"] == pytest.approx(stats.sharpe(sealed), rel=1e-9)


def test_the_same_seed_gives_the_same_verdict(planted, verdict):
    again = judge(planted[1], planted[0])
    assert [g.figures for g in again.gates] == [g.figures for g in verdict.gates]


def test_one_gate_s_draws_never_move_another_s(planted, verdict, monkeypatch):
    monkeypatch.setattr(battery, "CHECKED_DATES", 20)                # gate 1 draws fewer dates
    again = judge(planted[1], planted[0])
    assert again.gates[0].figures["dates checked"] < verdict.gates[0].figures["dates checked"]
    np.testing.assert_array_equal(again.evidence["placebos"], verdict.evidence["placebos"])
    assert [g.figures for g in again.gates[1:]] == [g.figures for g in verdict.gates[1:]]


# --------------------------------------------------------------------------- each gate's figures, recomputed

def above(result, market, period):
    """Daily returns above the bill rate over the period, computed here rather than by the battery."""
    return (result.returns - market.rf.reindex(result.returns.index).fillna(0.0)).loc[period]


def own_runs(strategy, market, variants, crypto=NO_CRYPTO):
    """A card's variants run on the in-sample years straight from the engine, with their benchmarks."""
    inside = market.window(*battery.IN_SAMPLE)
    positions = [battery.targets(strategy, inside, v) for v in variants]
    fee = {m: costs.per_side(inside.prices.columns, m, crypto) for m in (1, 2)}
    return SimpleNamespace(
        inside=inside, positions=positions, fee=fee[1],
        period=slice(battery.first_holding(positions[0]), pd.Timestamp(battery.IN_SAMPLE[1])),
        result=[engine.run(inside.prices, p, fee[1], inside.rf) for p in positions],
        doubled=[engine.run(inside.prices, p, fee[2], inside.rf) for p in positions],
        bench=[costs.benchmark(inside, p, 1, crypto) for p in positions],
        bench2=[costs.benchmark(inside, p, 2, crypto) for p in positions])


@pytest.fixture(scope="module")
def runs(planted):
    return own_runs(planted[1], planted[0], CARD.variants)


def figures(verdict, number):
    return verdict.gates[number - 1].figures


def test_gate_one_counts_the_decisions_of_the_positions_the_other_gates_judge(verdict, runs):
    f = figures(verdict, 1)
    assert f["clustered decisions"] == stats.decision_clusters(runs.positions[0].loc[runs.period])
    assert f["data problems"] == [] and f["years needed"] == battery.MIN_YEARS


def test_gate_two_s_figures_are_those_of_the_run_and_its_benchmark(verdict, runs):
    x, b = above(runs.result[0], runs.inside, runs.period), above(runs.bench[0], runs.inside, runs.period)
    x2, b2 = above(runs.doubled[0], runs.inside, runs.period), above(runs.bench2[0], runs.inside, runs.period)
    paid = runs.result[0].costs.loc[runs.period]
    a_year = paid.mean() * battery.PERIODS
    assert figures(verdict, 2) == pytest.approx({
        "Sharpe": stats.sharpe(x), "benchmark Sharpe": stats.sharpe(b), "alpha": stats.alpha(x, b),
        "Sharpe at 2x costs": stats.sharpe(x2), "alpha at 2x costs": stats.alpha(x2, b2),
        "gross Sharpe": stats.sharpe(x + paid), "costs a year": a_year,
        "costs in Sharpe units": a_year / (x.std(ddof=1) * np.sqrt(battery.PERIODS))}, rel=1e-9)


def test_gate_three_s_figures_are_those_of_the_run_and_its_placebos(verdict, runs):
    f, ev = figures(verdict, 3), verdict.evidence
    x = above(runs.result[0], runs.inside, runs.period)
    assert f["PSR"] == pytest.approx(stats.adjusted_psr(x), rel=1e-12)
    assert f["placebo sessions"] == len(x) and f["placebos"] == len(ev["placebos"]) == battery.PLACEBOS
    assert ev["placebo own Sharpe"] == pytest.approx(stats.sharpe(x.iloc[1:]), rel=1e-9)
    assert f["placebos beaten"] == np.mean(ev["placebos"] < ev["placebo own Sharpe"])
    assert ev["placebo window"] == (x.index[0], x.index[-1]) and ev["placebo late assets"] == []


def test_gate_four_s_figures_are_those_of_the_card_s_trials(verdict, runs):
    f = figures(verdict, 4)
    edges = [stats.hedged(above(r, runs.inside, runs.period), above(b, runs.inside, runs.period))
             for r, b in zip(runs.result, runs.bench)]
    assert [t.sharpe for t in verdict.trials] == pytest.approx([stats.sharpe(e) for e in edges], rel=1e-12)
    labels = stats.near_clone_clusters(pd.concat([(1 + e).resample("ME").prod() - 1 for e in edges], axis=1))
    daily = pd.Series([stats.sharpe(e) / np.sqrt(battery.PERIODS) for e in edges]).groupby(labels).mean()
    variance, count = max(daily.var(ddof=1) if len(daily) > 1 else 0.0, 1 / len(edges[0])), int(labels.max())
    assert f["trials"] == len(CARD.variants) and f["effective trials"] == count
    assert f["Sharpe expected by luck"] == pytest.approx(
        stats.expected_max_sharpe(count, variance) * np.sqrt(battery.PERIODS), rel=1e-9, abs=1e-12)
    assert f["DSR"] == pytest.approx(stats.dsr(edges[0], count, variance), rel=1e-9)


def test_gate_five_s_figures_are_those_of_the_variants_their_blend_and_the_blocks(verdict, runs):
    f, ev, inside, period = figures(verdict, 5), verdict.evidence, runs.inside, runs.period
    sharpes = [stats.sharpe(above(r, inside, period)) for r in runs.result]
    assert f["worst variant Sharpe"] == pytest.approx(min(sharpes), rel=1e-12) and sharpes[0] != sharpes[1]
    x, b = above(runs.result[0], inside, period), above(runs.bench[0], inside, period)
    blocks = {f"{first[:4]}-{last[:4]}": stats.alpha(x.loc[first:last], b.loc[first:last]) for first, last in battery.BLOCKS}
    assert ev["blocks"] == pytest.approx(blocks, rel=1e-12)          # every block holds 126 sessions or more
    assert f["positive blocks"] == sum(a > 0 for a in blocks.values())
    edge = stats.hedged(x, b)
    pd.testing.assert_series_equal(ev["edge by year"], edge.groupby(edge.index.year).sum(), rtol=1e-12)
    # the blend: the variants in equal parts, each paying its own costs, beside a benchmark set back
    # to equal weights on every session where a variant trades
    returns = sum(r.returns for r in runs.result) / len(runs.result)
    trading = pd.concat([p.notna().any(axis=1) for p in runs.positions], axis=1).any(axis=1)
    union = pd.DataFrame(0.0, index=inside.prices.index, columns=inside.prices.columns).where(trading, axis=0)
    blend = stats.hedged((returns - inside.rf.reindex(returns.index).fillna(0.0)).loc[period],
                         above(costs.benchmark(inside, union, 1, NO_CRYPTO), inside, period))
    pd.testing.assert_series_equal(ev["blend edge"], blend, check_names=False, rtol=1e-9)


def test_gate_six_moves_the_base_variant_and_judges_the_other_gates_positions(planted, verdict, runs):
    strategy, inside, period = planted[1], runs.inside, runs.period
    f, ev = figures(verdict, 6), verdict.evidence
    base = stats.sharpe(above(runs.result[0], inside, period))

    def sharpe_of(market, positions):
        fee = costs.per_side(market.prices.columns, 1, NO_CRYPTO)
        return stats.sharpe(above(engine.run(market.prices, positions, fee, market.rf), market, period))

    moved = {f"span={v}": sharpe_of(inside, battery.targets(strategy, inside, {"span": v})) / base for v in (8, 12, 5, 15)}
    assert ev["neighbours"] == pytest.approx(moved, rel=1e-9)
    assert f["neighbour median ratio"] == pytest.approx(np.median(list(moved.values())), rel=1e-12)
    left = {}
    for cluster in ("a", "b", "c"):
        out = [t for t in EIGHT if CLUSTERS[t] == cluster]
        others = [t for t in EIGHT if t not in out]
        seen = battery.targets(strategy, battery.unheld(inside, out), {"span": 10})[others]
        left[cluster] = sharpe_of(battery.restrict(inside, others), seen) / base
    assert ev["clusters out"] == pytest.approx(left, rel=1e-9)
    assert f["worst cluster out"] == min(left, key=left.get)
    assert f["worst cluster out ratio"] == pytest.approx(min(left.values()), rel=1e-9)
    pd.testing.assert_series_equal(ev["P&L shares"], battery.pnl_shares(runs.result[0], inside, period))
    assert f["one day late ratio"] == pytest.approx(sharpe_of(inside, runs.positions[0].shift(1)) / base, rel=1e-9)


def test_gate_seven_s_floors_are_percentiles_of_a_bootstrap_of_the_in_sample_run(planted, verdict, runs):
    market, strategy, _ = planted
    f, ev = figures(verdict, 7), verdict.evidence
    assert f["Sharpe floor"] == np.percentile(ev["bootstrap"]["Sharpe"], battery.PERCENTILE)
    assert f["alpha floor"] == np.percentile(ev["bootstrap"]["alpha"], battery.PERCENTILE)
    x = above(runs.result[0], runs.inside, runs.period)
    assert np.median(ev["bootstrap"]["Sharpe"]) == pytest.approx(stats.sharpe(x), abs=0.2)
    whole = market.window(battery.IN_SAMPLE[0], battery.HOLDOUT[1])
    positions = battery.targets(strategy, whole, {"span": 10})
    sealed = slice(pd.Timestamp(battery.HOLDOUT[0]), pd.Timestamp(battery.HOLDOUT[1]))
    xh = above(engine.run(whole.prices, positions, runs.fee, whole.rf), whole, sealed)
    bh = above(costs.benchmark(whole, positions, 1, NO_CRYPTO), whole, sealed)
    assert f["holdout alpha"] == pytest.approx(stats.alpha(xh, bh), rel=1e-9)
    assert (f["variants rewritten"], f["dates checked"], f["data problems"]) == (0, 2 * 2 * battery.HOLDOUT_CHECKED_DATES, [])


def test_gate_seven_s_bootstrap_draws_from_the_first_holding_on(planted, monkeypatch):
    market, strategy, _ = planted
    seen, drawn = {}, battery.bootstrap

    def watched(x, b, rng):
        seen["x"], seen["b"] = x, b
        return drawn(x, b, rng)

    def late(market, span=10):                                           # nothing held before 2010
        positions = strategy(market, span)
        positions.loc[:"2009-12-31"] = 0.0
        return positions

    monkeypatch.setattr(battery, "bootstrap", watched)
    judge(late, market)
    first = pd.Timestamp("2010-01-04")
    assert seen["x"].index[0] == seen["b"].index[0] == first         # the years before it hold nothing to draw
    assert seen["x"].index[-1] == seen["b"].index[-1] == market.prices.loc[:battery.IN_SAMPLE[1]].index[-1]


def paced(signal):
    """The planted rule, read the right way up or upside down, set every week or every month."""
    def positions(market, span=10, side="with", pace="weekly"):
        return signal_strategy(signal if side == "with" else -signal)(market, span, 5 if pace == "weekly" else 21)
    return positions


CHOOSER = battery.Card("chooser-01", EIGHT, ({"span": 10, "side": "against", "pace": "weekly"},
                                              {"span": 10, "side": "with", "pace": "monthly"}), NEIGHBOURS, choose=True)


@pytest.fixture(scope="module")
def chooser(planted):
    """A card whose base reads the signal upside down, every week; the walk-forward picks the other
    variant, monthly, from the fourth year on."""
    market, _, signal = planted
    strategy = paced(signal)
    mine = own_runs(strategy, market, CHOOSER.variants)
    legs = [battery.Leg(*parts) for parts in zip(mine.positions, mine.result, mine.doubled, mine.bench, mine.bench2)]
    mine.composite, mine.wfe = battery.walk_forward(legs, mine.inside, mine.period)
    mine.main = engine.run(mine.inside.prices, mine.composite, mine.fee, mine.inside.rf)
    return judge(strategy, market, CHOOSER), mine, strategy


def test_a_card_that_chooses_is_judged_on_its_choices_in_every_gate(planted, chooser):
    verdict, mine, strategy = chooser
    inside, period, ev = mine.inside, mine.period, verdict.evidence
    f = {g.number: g.figures for g in verdict.gates}
    choices, base = mine.composite.loc[period], mine.positions[0].loc[period]
    assert f[1]["clustered decisions"] == stats.decision_clusters(choices) != stats.decision_clusters(base)
    assert f[5]["walk-forward efficiency"] == pytest.approx(mine.wfe, rel=1e-12)
    x = above(mine.main, inside, period)
    b = above(costs.benchmark(inside, mine.composite, 1, NO_CRYPTO), inside, period)
    assert f[2]["Sharpe"] == pytest.approx(stats.sharpe(x), rel=1e-9) and f[2]["alpha"] == pytest.approx(stats.alpha(x, b), rel=1e-9)
    assert f[3]["PSR"] == pytest.approx(stats.adjusted_psr(x), rel=1e-9)
    assert ev["placebo own Sharpe"] == pytest.approx(stats.sharpe(x.iloc[1:]), rel=1e-9)
    assert f[4]["appraisal ratio"] == pytest.approx(stats.sharpe(stats.hedged(x, b)), rel=1e-9)
    blocks = {f"{first[:4]}-{last[:4]}": stats.alpha(x.loc[first:last], b.loc[first:last]) for first, last in battery.BLOCKS}
    assert ev["blocks"] == pytest.approx(blocks, rel=1e-9)
    best = int(battery.edge_by_year(x, b).idxmax())
    assert f[5]["best year"] == best and f[5]["alpha without the best year"] == pytest.approx(
        stats.alpha(x[x.index.year != best], b[b.index.year != best]), rel=1e-9)
    pd.testing.assert_series_equal(ev["exposure"], mine.main.weights.loc[period].sum(axis=1))
    pd.testing.assert_series_equal(ev["assets held"], mine.main.weights.loc[period].gt(1e-9).sum(axis=1))
    assert not ev["exposure"].equals(mine.result[0].weights.loc[period].sum(axis=1))
    assert verdict.failed == 4                                         # its choices pass gates 1 to 3
    late = engine.run(inside.prices, mine.composite.shift(1), mine.fee, inside.rf)
    assert f[6]["one day late ratio"] == pytest.approx(stats.sharpe(above(late, inside, period)) / stats.sharpe(x), rel=1e-9)
    pd.testing.assert_series_equal(ev["P&L shares"], battery.pnl_shares(mine.main, inside, period))
    # gate 7 bootstraps the choices, whose Sharpe ratio is far from the base's
    assert stats.sharpe(above(mine.result[0], inside, period)) < 0 < stats.sharpe(x)
    assert np.median(ev["bootstrap"]["Sharpe"]) == pytest.approx(stats.sharpe(x), abs=0.2)
    # the holdout trades the in-sample choices, then the variant of best in-sample Sharpe ratio
    whole = planted[0].window(battery.IN_SAMPLE[0], battery.HOLDOUT[1])
    full = [battery.targets(strategy, whole, v) for v in CHOOSER.variants]
    spliced = full[1].copy()
    before = spliced.index <= pd.Timestamp(battery.IN_SAMPLE[1])
    spliced.loc[before] = mine.composite.reindex(spliced.index[before])
    first = spliced.index[~before][0]
    spliced.loc[first] = full[1].ffill().loc[first]
    sealed = slice(pd.Timestamp(battery.HOLDOUT[0]), pd.Timestamp(battery.HOLDOUT[1]))
    xh = above(engine.run(whole.prices, spliced, mine.fee, whole.rf), whole, sealed)
    assert f[7]["variant traded"] == 1 and f[7]["holdout Sharpe"] == pytest.approx(stats.sharpe(xh), rel=1e-9)


def test_a_strategy_that_cannot_run_fails_gate_one_and_leaves_the_others_uncomputed(planted):
    def broken(market, span=10):
        raise ValueError("no signal yet")

    verdict = judge(broken, planted[0])
    assert verdict.failed == 1 and "cannot run: no signal yet" in verdict.gates[0].reason
    assert all(g.passed is None for g in verdict.gates[1:])


def test_runs_that_break_before_the_gates_fail_every_gate_with_their_error(planted, verdict, monkeypatch):
    def broken(legs, market, period):
        raise RuntimeError("no year to choose from")

    monkeypatch.setattr(battery, "walk_forward", broken)
    broke = judge(planted[1], planted[0], card("broken-01", ({"span": 10}, {"span": 20}), choose=True))
    assert [g.passed for g in broke.gates] == [False] * 7
    assert all("cannot be computed: RuntimeError: no year to choose from" in g.reason for g in broke.gates)
    # both variants ran before the error: their trials count, and are those of the same variants unbroken
    assert [t.key for t in broke.trials] == ["broken-01/0", "broken-01/1"]
    assert [t.sharpe for t in broke.trials] == [t.sharpe for t in verdict.trials]


def test_a_gate_that_breaks_fails_with_its_error():
    gate = battery.guarded(2, lambda: 1 / 0)
    assert gate.passed is False and "ZeroDivisionError" in gate.reason


# --------------------------------------------------------------------------- gate 1

def test_reading_tomorrow_breaks_hygiene(planted):
    gate = judge(momentum(-1), planted[0]).gates[0]
    assert not gate.passed and gate.figures["look-ahead breaks"] > 0
    assert gate.figures["same-day breaks"] == 0          # it reads tomorrow, not the bar it trades on


def test_a_look_ahead_confined_to_a_few_years_is_found(planted):
    def peeks_from_2012_to_2014(market, span=10):
        out = momentum(1)(market, span)
        years = (out.index.year >= 2012) & (out.index.year <= 2014)
        out.loc[years] = momentum(-1)(market, span).loc[years]
        return out

    gate = judge(peeks_from_2012_to_2014, planted[0], battery.Card("peek-02", EIGHT, ({"span": 10},), NEIGHBOURS)).gates[0]
    assert gate.figures["look-ahead breaks"] > 0 and not gate.passed     # dates are drawn across the whole period


def test_a_look_ahead_that_moves_a_weight_by_a_hair_is_found(planted):
    def nudged(market, span=10):
        tomorrow_up = market.prices.mean(axis=1).pct_change().shift(-1) > 0     # a shift the wrong way
        return momentum(1)(market, span).mul(np.where(tomorrow_up, 1.0, 0.999), axis=0)

    gate = judge(nudged, planted[0], battery.Card("nudge-01", EIGHT, ({"span": 10},), NEIGHBOURS)).gates[0]
    assert gate.figures["look-ahead breaks"] > 0


def test_reading_the_bar_being_traded_breaks_hygiene(planted):
    gate = judge(momentum(0), planted[0]).gates[0]
    assert not gate.passed
    assert gate.figures["look-ahead breaks"] == 0 and gate.figures["same-day breaks"] > 0
    assert judge(momentum(1), planted[0]).gates[0].figures["same-day breaks"] == 0


def test_reading_the_prices_of_the_bar_being_traded_breaks_hygiene(planted):
    def today(market, span=10):
        up = (market.prices.pct_change(span) > 0).astype(float)   # the close of the session it trades on
        weights = up.div(up.sum(axis=1).where(up.sum(axis=1) > 0), axis=0).fillna(0.0)
        return weights.where(pd.Series(np.arange(len(weights)) % 5 == 0, index=weights.index), axis=0)

    gate = judge(today, planted[0]).gates[0]
    assert gate.figures["look-ahead breaks"] == 0 and gate.figures["same-day breaks"] > 0

    def yesterday(market, span=10):
        up = (market.prices.pct_change(span).shift(1) > 0).astype(float)   # the closes up to the day before
        weights = up.div(up.sum(axis=1).where(up.sum(axis=1) > 0), axis=0).fillna(0.0)
        return weights.where(pd.Series(np.arange(len(weights)) % 5 == 0, index=weights.index), axis=0)

    clean = judge(yesterday, planted[0]).gates[0]
    assert clean.figures["look-ahead breaks"] == 0 and clean.figures["same-day breaks"] == 0


def test_bitcoin_read_through_its_own_close_breaks_hygiene():
    market, _ = synthetic_market(4, coin=True)
    universe = (*EIGHT, "COIN")

    def trend(market, source):
        closes = market.signal_prices if source == "signal" else market.prices
        up = (closes.pct_change(20).shift(1) > 0).astype(float)
        weights = up.div(up.sum(axis=1).where(up.sum(axis=1) > 0), axis=0).fillna(0.0)
        return weights.where(pd.Series(np.arange(len(weights)) % 5 == 0, index=weights.index), axis=0)

    coin = frozenset({"COIN"})
    lagged = judge(trend, market, battery.Card("coin-01", universe, ({"source": "signal"},)), crypto=coin)
    assert lagged.gates[0].figures["same-day breaks"] == 0
    assert lagged.gates[0].figures["years needed"] == battery.MIN_YEARS      # bitcoin is one asset of nine
    unlagged = judge(trend, market, battery.Card("coin-02", universe, ({"source": "prices"},)), crypto=coin)
    assert unlagged.gates[0].figures["same-day breaks"] > 0


def test_every_variant_is_checked_for_look_ahead(planted):
    def two(market, span=10, timing="clean"):
        return momentum(1 if timing == "clean" else -1)(market, span)

    verdict = judge(two, planted[0], card("two-01", ({"span": 10, "timing": "clean"}, {"span": 10, "timing": "tomorrow"})))
    assert not verdict.gates[0].passed
    breaks = verdict.evidence["timing breaks"]
    assert not breaks[0]["look-ahead"] and breaks[1]["look-ahead"]


def test_a_rule_that_reads_the_future_to_decide_when_to_hold_breaks_hygiene(planted):
    def holds_before_a_fall(market, span=10):
        weights = momentum(1)(market, span, every=1)
        tomorrow_down = market.prices.mean(axis=1).pct_change().shift(-1) < 0   # a shift the wrong way
        return weights.mask(tomorrow_down, axis=0)                               # NaN: hold

    gate = judge(holds_before_a_fall, planted[0]).gates[0]
    assert not gate.passed and gate.figures["look-ahead breaks"] > 0


def test_reading_the_bill_rate_of_the_session_is_not_a_break(planted):
    def rate_aware(market, span=10):                  # the rate of t was set at t-1: it may be read
        return momentum(1)(market, span).mul(1 - 50 * market.rf, axis=0)

    assert judge(rate_aware, planted[0]).gates[0].figures["same-day breaks"] == 0


def test_the_data_is_checked_for_prices_at_or_below_zero_and_gaps():
    market, _ = synthetic_market(7)
    prices = market.prices.copy()
    prices.iloc[100, 0] = np.nan
    prices.iloc[200, 1] = 0.0
    problems = battery.data_problems(Market(prices, prices.notna(), market.rf, prices))
    assert problems == ["S1 has no price on 1 sessions of its life", "S2 has 1 prices at or below zero"]
    late = market.prices.copy()
    late.iloc[:300, 2] = np.nan                          # an asset that starts later is not a gap
    assert battery.data_problems(Market(late, late.notna(), market.rf, late)) == []


def test_a_gap_on_the_first_or_the_last_session_of_a_window_is_seen():
    market, _ = synthetic_market(7)
    prices = market.prices.copy()
    first_2012, last_2022, first_2023 = prices.loc["2012"].index[0], prices.loc["2022"].index[-1], prices.loc["2023"].index[0]
    prices.loc[first_2012, "S1"] = prices.loc[last_2022, "S2"] = prices.loc[first_2023, "S3"] = np.nan
    gapped = Market(prices, prices.notna(), market.rf, prices)
    assert battery.data_problems(gapped, slice(first_2012, last_2022)) == [
        "S1 has no price on 1 sessions of its life", "S2 has no price on 1 sessions of its life"]
    assert battery.data_problems(gapped, slice(first_2023, None)) == ["S3 has no price on 1 sessions of its life"]


def test_a_gap_in_the_prices_fails_the_gate_that_reads_them(planted):
    market, strategy, _ = planted
    prices = market.prices.copy()
    holdout = np.flatnonzero(prices.index >= battery.HOLDOUT[0])
    inside_day, holdout_day = prices.index[1001], prices.index[holdout[holdout % 5 == 2][10]]   # the rule holds there
    prices.loc[inside_day, "S2"] = prices.loc[holdout_day, "S3"] = np.nan
    verdict = judge(strategy, Market(prices, market.tradable, market.rf, prices.copy()))
    assert "the data: S2 has no price on 1 sessions of its life" in verdict.gates[0].reason
    assert "the holdout's data: S3 has no price on 1 sessions of its life" in verdict.gates[6].reason
    assert "S3" not in verdict.gates[0].reason and "S2" not in verdict.gates[6].reason


def test_a_gap_on_the_first_or_the_last_session_a_gate_reads_fails_it(planted):
    """Gates 1 and 7 take an asset's life from the whole series: a gap on the first session of a
    card's in-sample period, on its last, or on the holdout's first, is a gap."""
    market, strategy, _ = planted
    later = battery.Card("synthetic-12", EIGHT, ({"span": 10},), NEIGHBOURS, in_sample=("2012-01-01", "2022-12-31"))
    runs = [battery.targets(strategy, market.window(later.in_sample[0], end), {"span": 10}).fillna(0.0)
            for end in (later.in_sample[1], battery.HOLDOUT[1])]
    prices = market.prices.copy()
    gaps = {}
    for day in (prices.loc["2012"].index[0], prices.loc["2022"].index[-1], prices.loc["2023"].index[0]):
        bought = {t for run in runs if day in run.index for t in run.columns if run.at[day, t] > 0}
        gaps[day] = next(t for t in EIGHT if t not in bought and t not in gaps.values())   # the engine buys nothing without a price
        prices.loc[day, gaps[day]] = np.nan
    verdict = judge(strategy, Market(prices, prices.notna(), market.rf, prices.copy()), later)
    first, last, opening = gaps.values()
    assert verdict.gates[0].reason.count("has no price on 1 sessions of its life") == 2
    for ticker in (first, last):
        assert f"{ticker} has no price on 1 sessions of its life" in verdict.gates[0].reason
    assert f"the holdout's data: {opening} has no price on 1 sessions of its life" in verdict.gates[6].reason


def test_years_are_counted_from_the_first_holding(planted):
    market, strategy, _ = planted

    def late(market, span=10):
        out = strategy(market, span)
        out.loc[:"2011-12-31"] = out.loc[:"2011-12-31"].where(out.loc[:"2011-12-31"].isna(), 0.0)
        return out

    inside = market.window(*battery.IN_SAMPLE)
    first = battery.first_holding(battery.targets(late, inside, {"span": 10}))
    assert first.year == 2012
    years = judge(late, market).gates[0].figures["years in-sample"]
    assert years == len(inside.prices.loc[first:]) / battery.PERIODS


def test_the_first_holding_is_the_first_positive_weight():
    positions = pd.DataFrame({"A": [np.nan, 0.0, 0.0, 0.5, np.nan]}, index=pd.bdate_range("2020-01-06", periods=5))
    assert battery.first_holding(positions) == positions.index[3]
    assert battery.first_holding(positions.fillna(0.0) * 0) is None


def test_five_years_are_needed_unless_every_asset_is_crypto():
    coin = frozenset({"COIN"})
    assert battery.years_needed([*EIGHT, "COIN"], coin) == battery.MIN_YEARS
    assert battery.years_needed(["COIN"], coin) == battery.MIN_YEARS_CRYPTO


# --------------------------------------------------------------------------- gate 3

def test_the_placebo_at_offset_zero_is_the_strategy_itself(planted):
    market, strategy, _ = planted
    inside = market.window(*battery.IN_SAMPLE)
    positions = battery.targets(strategy, inside, {"span": 10})
    result = engine.run(inside.prices, positions, battery.fees(inside, 1, NO_CRYPTO), inside.rf)
    period = slice(battery.first_holding(positions), pd.Timestamp(battery.IN_SAMPLE[1]))
    own, _ = battery.placebo_sharpes(result, inside, period, np.array([300]))
    assert own == pytest.approx(stats.sharpe(battery.excess(result, inside.rf, period).iloc[1:]), rel=1e-9)


def test_the_placebo_at_offset_zero_is_the_strategy_itself_when_an_asset_starts_late():
    inside = late_market().window(*battery.IN_SAMPLE)
    positions = battery.targets(momentum(1), inside, {"span": 10})
    result = engine.run(inside.prices, positions, battery.fees(inside, 1, NO_CRYPTO), inside.rf)
    period = slice(battery.first_holding(positions), pd.Timestamp(battery.IN_SAMPLE[1]))
    assert battery.late_assets(result.weights, inside.tradable, period) == ["S8"]
    own, _ = battery.placebo_sharpes(result, inside, period, np.array([300]))
    assert own == pytest.approx(stats.sharpe(battery.excess(result, inside.rf, period).iloc[1:]), rel=1e-9)


def test_placebos_are_shifted_a_year_or_more_each_way_and_need_two_years_and_two_sessions(planted, monkeypatch):
    market, strategy, _ = planted
    inside = market.window(*battery.IN_SAMPLE)
    positions = battery.targets(strategy, inside, {"span": 10})
    result = engine.run(inside.prices, positions, battery.fees(inside, 1, NO_CRYPTO), inside.rf)
    sessions = inside.prices.index[inside.prices.index >= battery.first_holding(positions)]
    drawn, placebos = [], battery.placebo_sharpes

    def watched(result, market, period, offsets):
        drawn.append(offsets)
        return placebos(result, market, period, offsets)

    monkeypatch.setattr(battery, "placebo_sharpes", watched)
    for years in (3, 9):
        period = slice(sessions[0], sessions[years * 252 - 1])
        gate, _ = battery.significance(result, inside, period, np.random.default_rng(years))
        assert gate.figures["placebos"] == battery.PLACEBOS and gate.figures["placebo sessions"] == years * 252
        assert drawn[-1].min() >= battery.MIN_SHIFT and drawn[-1].max() <= years * 252 - battery.MIN_SHIFT
    for count, computed in ((2 * battery.MIN_SHIFT + 1, False), (2 * battery.MIN_SHIFT + 2, True)):
        gate, _ = battery.significance(result, inside, slice(sessions[0], sessions[count - 1]), np.random.default_rng(1))
        assert (gate.figures["placebos beaten"] is not None) == computed, count


def test_placebos_of_a_signal_with_no_edge_rank_it_at_random():
    market, _ = synthetic_market(5, tickers=EIGHT[:4])
    inside = market.window(*battery.IN_SAMPLE)
    rng = np.random.default_rng(11)
    ranks = []
    for draw in range(40):
        noise = pd.DataFrame(rng.normal(size=inside.prices.shape), index=inside.prices.index,
                             columns=inside.prices.columns)
        positions = signal_strategy(noise)(inside, span=10)
        result = engine.run(inside.prices, positions, battery.fees(inside, 1, NO_CRYPTO), inside.rf)
        period = slice(battery.first_holding(positions), pd.Timestamp(battery.IN_SAMPLE[1]))
        own, placebos = battery.placebo_sharpes(result, inside, period,
                                                stats.placebo_offsets(len(inside.prices.loc[period]), 200, 252, rng))
        ranks.append(np.mean(placebos < own))
    assert 0.35 < np.mean(ranks) < 0.65      # a no-edge rule sits anywhere among its placebos
    assert np.mean(np.array(ranks) >= 0.9) < 0.25


def test_a_strategy_that_is_its_own_placebo_beats_none_of_them(planted):
    inside = planted[0].window(*battery.IN_SAMPLE)
    weights = pd.DataFrame(1 / 8, index=inside.prices.index, columns=inside.prices.columns)    # never moves
    returns = (weights.shift(1).fillna(0.0) * battery.asset_returns(inside)).sum(axis=1)
    result = engine.Result(returns, pd.DataFrame(), returns * 0, weights)
    gate, placebos = battery.significance(result, inside, slice(None), np.random.default_rng(20))
    assert np.all(placebos == placebos[0]) and gate.figures["placebos beaten"] == 0.0


def late_market(seed=8, tickers=EIGHT, drift=0.001):
    """The synthetic market, with its last asset trading from 2014 only, and climbing."""
    market, _ = synthetic_market(seed, tickers=tickers)
    prices = market.prices.copy()
    start = prices.index.get_loc(pd.Timestamp("2014-01-02"))
    steps = np.random.default_rng(seed).normal(drift, 0.01, len(prices) - start)
    prices.iloc[:start, -1] = np.nan
    prices.iloc[start:, -1] = 100 * np.exp(np.cumsum(steps))
    return Market(prices, prices.notna(), market.rf, prices)


def test_a_placebo_shifts_a_weight_where_its_asset_trades_on_both_days_and_fills_the_rest_with_the_strategy_s_own():
    rng = np.random.default_rng(4)
    n, shifts = 700, np.array([0, 150, 380, 600])
    T = np.ones((n, 4), bool)
    T[:250, 3] = False                                                  # the fourth asset starts later
    T[620:, 0] = False                                                  # and the first stops: both on one day
    W = rng.random((n, 4)) * (rng.random((n, 4)) < 0.6) * T
    W = W / np.maximum(W.sum(axis=1, keepdims=True), 1.0) * rng.choice([0.0, 0.5, 1.0], size=(n, 1))
    held = battery.placebo_weights(W, T, shifts)
    days = np.arange(1, n)
    before = (days[None, :] - 1 - shifts[:, None]) % n
    source, own = W[before], np.broadcast_to(W[days - 1][None], held.shape)
    today = np.broadcast_to(T[days - 1][None], held.shape)
    np.testing.assert_allclose(held[0], W[days - 1], rtol=0, atol=1e-15)   # offset zero: the strategy itself
    assert (held[~today] == 0).all()                                   # never an asset that does not trade
    kept = today & ~T[before]                                          # a weight whose other day came before its start
    np.testing.assert_array_equal(held[kept], own[kept])
    both = today & T[before]
    shifted, mine = np.where(both, source, 0.0), np.where(both, own, 0.0)
    kept_total = np.where(kept, held, 0.0).sum(axis=2)
    wanted = np.maximum(source.sum(axis=2), kept_total)                # what the day shifted from held
    short = source.sum(axis=2) - kept_total - shifted.sum(axis=2) > 1e-12   # it held assets not trading yet
    filled = short & (mine.sum(axis=2) > 0)
    invested = filled | (shifted.sum(axis=2) > 0)
    np.testing.assert_allclose(held.sum(axis=2)[invested], wanted[invested], rtol=1e-12)
    # filled: the shifted weights whole, and the rest in proportion to the strategy's own of the day
    rest = np.where(both, held, 0.0) - shifted
    np.testing.assert_allclose((rest * mine.sum(axis=2)[..., None])[filled],
                               (mine * rest.sum(axis=2)[..., None])[filled], atol=1e-15)
    assert (rest[filled] >= -1e-15).all()
    # elsewhere the shifted weights, scaled to the room left
    others = invested & ~filled
    np.testing.assert_allclose((np.where(both, held, 0.0) * shifted.sum(axis=2)[..., None])[others],
                               (shifted * np.where(both, held, 0.0).sum(axis=2)[..., None])[others], atol=1e-15)
    alone = short & ~filled & (shifted.sum(axis=2) == 0)                # nothing to shift, nothing of its own to fill
    np.testing.assert_array_equal(held[alone], np.where(kept, own, 0.0)[alone])
    assert kept.any() and filled.any() and (short & ~filled & (shifted.sum(axis=2) > 0)).any()   # each case reached
    assert (others & (kept_total > 0)).any() and alone.any()


def test_each_placebo_day_earns_its_weights_less_the_bill_rate_on_them_and_the_costs_of_the_day_shifted_from():
    inside = late_market().window(*battery.IN_SAMPLE)
    positions = battery.targets(momentum(1), inside, {"span": 10})
    result = engine.run(inside.prices, positions, battery.fees(inside, 1, NO_CRYPTO), inside.rf)
    period = slice(battery.first_holding(positions), pd.Timestamp(battery.IN_SAMPLE[1]))
    W = result.weights.loc[period]
    T = inside.tradable.loc[period].to_numpy()
    returns, rf, paid = battery.asset_returns(inside).loc[period], inside.rf.loc[period].fillna(0.0), result.costs.loc[period]
    shifts = np.array([400, 2000])
    _, placebos = battery.placebo_sharpes(result, inside, period, shifts)
    held = battery.placebo_weights(W.to_numpy(), T, shifts)
    n = len(W)
    for k, shift in enumerate(shifts):
        days = [(t, (t - shift) % n) for t in range(1, n)]              # each day, and the day its costs come from
        x = pd.Series([held[k, t - 1] @ returns.iloc[t].to_numpy() - held[k, t - 1].sum() * rf.iloc[t] - paid.iloc[c]
                       for t, c in days])
        assert placebos[k] == pytest.approx(stats.sharpe(x), rel=1e-9)


def test_the_report_names_the_assets_that_start_late():
    inside = late_market().window(*battery.IN_SAMPLE)
    positions = battery.targets(momentum(1), inside, {"span": 10}) * 0.4       # a late asset held lightly is named
    result = engine.run(inside.prices, positions, battery.fees(inside, 1, NO_CRYPTO), inside.rf)
    period = slice(battery.first_holding(positions), pd.Timestamp(battery.IN_SAMPLE[1]))
    evidence = {}
    battery.significance(result, inside, period, np.random.default_rng(5), evidence)
    assert evidence["placebo late assets"] == ["S8"] and 0 < result.weights["S8"].max() < 0.5


def null_ranks(inside, positions_of, draws, rng):
    """The rank among 200 placebos of `draws` rules without skill, each drawn by positions_of(rng)."""
    ranks = []
    for _ in range(draws):
        positions = positions_of(rng)
        result = engine.run(inside.prices, positions, battery.fees(inside, 1, NO_CRYPTO), inside.rf)
        period = slice(battery.first_holding(positions), pd.Timestamp(battery.IN_SAMPLE[1]))
        own, placebos = battery.placebo_sharpes(result, inside, period,
                                                stats.placebo_offsets(len(inside.prices.loc[period]), 200, 252, rng))
        ranks.append(np.mean(placebos < own))
    return np.array(ranks)


def test_placebos_rank_a_slow_rule_with_no_skill_at_random_when_an_asset_starts_late_and_climbs():
    """A monthly rule on a persistent signal with no skill, among four assets, one of which starts in
    2014 and climbs fast. Every asset shifted, its weights would sit in cash before its start (a third
    of the draws beat 90% of their placebos); kept in place, the placebo is invested more or less than
    the strategy (15%); scaled down beside the others, it holds less of the climbing asset (28%)."""
    inside = late_market(tickers=EIGHT[:4], drift=0.002).window(*battery.IN_SAMPLE)

    def slow_rule(rng):
        noise = calibration.latent(inside.prices.index, inside.prices.columns, rng, 0.995).where(inside.tradable)
        return signal_strategy(noise)(inside, span=10, every=21)

    ranks = null_ranks(inside, slow_rule, 200, np.random.default_rng(12))
    assert 0.45 < ranks.mean() < 0.55 and np.mean(ranks >= 0.9) < 0.14


def test_placebos_rank_a_rotation_without_skill_between_early_and_late_assets_at_random():
    """Always fully invested, each month a random share on three assets that trade from the start and
    the rest on one that starts in 2014: with the late asset's weights kept in place, a placebo held
    anything from nothing to twice the strategy's exposure, and three draws in four beat 90% of their
    placebos."""
    inside = late_market(tickers=EIGHT[:4]).window(*battery.IN_SAMPLE)
    first = pd.Series(np.r_[True, inside.prices.index.month[1:] != inside.prices.index.month[:-1]], index=inside.prices.index)

    def rotation(rng):
        early = pd.Series(rng.random(len(first)), index=first.index).where(inside.tradable["S4"], 1.0)
        weights = pd.DataFrame({t: early / 3 for t in EIGHT[:3]} | {"S4": 1 - early})
        return weights.where(first, axis=0)

    ranks = null_ranks(inside, rotation, 100, np.random.default_rng(31))
    assert 0.4 < ranks.mean() < 0.65 and np.mean(ranks >= 0.9) < 0.14


LATE_RULES = {
    "binary rotation": (("SPY", "QQQ", "XLRE", "XLC"),
                        lambda inside, rng: calibration.rotation(int(rng.integers(2 ** 31)), binary=True)(inside, span=10)),
    "top two": (("SPY", "XLRE", "XLC", "BTC-USD"),
                lambda inside, rng: calibration.top(calibration.latent(inside.prices.index, inside.prices.columns, rng,
                                                                       calibration.SLOW_RHO), k=2)(inside, span=10)),
}


@real_snapshot
@pytest.mark.parametrize("name, below", [("binary rotation", 0.1), ("top two", 0.14)])
def test_placebos_rank_rules_without_skill_at_random_where_the_snapshot_s_assets_start_late(name, below):
    """From 2012, in a rising market, before XLRE, XLC and bitcoin trade: each month all on SPY and
    QQQ or all on XLRE and XLC, a coin's toss; or the two of four assets with the highest noise.
    Where a placebo's day came from after a late start, the assets it could not hold yet were left
    in cash or piled onto the others, and a third of the rotations, a quarter of the top two, beat
    90% of their placebos."""
    universe, rule = LATE_RULES[name]
    inside = battery.restrict(data.load(), universe).window(calibration.LATE_START, battery.IN_SAMPLE[1])
    ranks = null_ranks(inside, lambda rng: rule(inside, rng), 100, np.random.default_rng(50))
    assert 0.4 < ranks.mean() < 0.65 and np.mean(ranks >= 0.9) < below


# --------------------------------------------------------------------------- gate 4

def months(n=216):
    return pd.date_range("2005-01-31", periods=n, freq="ME")


def test_more_trials_raise_the_bar(planted, verdict):
    alone = verdict.gates[3]
    rng = np.random.default_rng(12)
    history = [battery.Trial(f"old-{k}", pd.Series(rng.normal(0, 0.03, 216), index=months()), 0.3) for k in range(30)]
    crowded = judge(planted[1], planted[0], history=history).gates[3]
    assert crowded.figures["effective trials"] > alone.figures["effective trials"]
    assert crowded.figures["Sharpe expected by luck"] > alone.figures["Sharpe expected by luck"]
    assert crowded.figures["DSR"] <= alone.figures["DSR"]


def test_the_trials_variance_is_never_below_what_luck_gives_one_trial():
    rng = np.random.default_rng(13)
    x = pd.Series(rng.normal(0.0005, 0.01, 3000))
    same = [battery.Trial(f"t{k}", pd.Series(rng.normal(0, 0.03, 216), index=months()), 0.5) for k in range(2)]
    gate = battery.multiple_testing(x, [], same)
    assert gate.figures["effective trials"] == 2
    assert gate.figures["Sharpe expected by luck"] == pytest.approx(
        stats.expected_max_sharpe(2, 1 / len(x)) * np.sqrt(battery.PERIODS), rel=1e-12)


def test_near_clones_enter_the_variance_once():
    rng = np.random.default_rng(14)
    common = rng.normal(0, 0.03, 216)
    clones = [battery.Trial(f"c{k}", pd.Series(common + rng.normal(0, 0.001, 216), index=months()), sharpe)
              for k, sharpe in enumerate((0.1, 0.2, 0.3))]
    other = battery.Trial("o", pd.Series(rng.normal(0, 0.03, 216), index=months()), 3.0)
    x = pd.Series(rng.normal(0.0005, 0.01, 3000))
    gate = battery.multiple_testing(x, [], [*clones, other])
    by_cluster = np.var([0.2 / np.sqrt(252), 3.0 / np.sqrt(252)], ddof=1)      # a cluster enters with its mean
    assert gate.figures["effective trials"] == 2
    assert gate.figures["Sharpe expected by luck"] == pytest.approx(
        stats.expected_max_sharpe(2, by_cluster) * np.sqrt(battery.PERIODS), rel=1e-12)


# --------------------------------------------------------------------------- gate 5

def business_days(first="2005-01-03", last="2022-12-30"):
    return pd.bdate_range(first, last)


def test_each_block_is_judged_on_its_own_sessions_and_short_ones_do_not_count():
    days = business_days()
    rng = np.random.default_rng(15)
    b = pd.Series(rng.normal(0.0003, 0.01, len(days)), index=days)
    crisis = (days.year == 2008) | (days.year == 2009)
    x = b + np.where(crisis, 0.001, -0.0001)
    alphas = battery.block_alphas(x, b)
    assert [k for k, a in alphas.items() if a > 0] == ["2008-2009"]
    in_2007 = days[days.year == 2007]
    for sessions, counted in ((battery.MIN_BLOCK_SESSIONS - 1, False), (battery.MIN_BLOCK_SESSIONS, True)):
        late = days[days >= in_2007[-sessions]]
        assert (battery.block_alphas(x.loc[late], b.loc[late])["2005-2007"] is not None) == counted


def test_the_best_year_is_the_year_of_the_largest_edge():
    days = business_days()
    rng = np.random.default_rng(16)
    b = pd.Series(rng.normal(0.0002, 0.01, len(days)), index=days)
    b[days.year == 2009] += 0.004                              # the market's best year
    x = b + np.where(days.year == 2015, 0.002, 0.0)            # the strategy's own best year
    assert battery.edge_by_year(x, b).idxmax() == 2015
    assert ((1 + x).groupby(x.index.year).prod()).idxmax() == 2009
    short = business_days("2005-11-01")                        # two months of 2005, at twice 2015's daily edge
    b = pd.Series(rng.normal(0.0002, 0.01, len(short)), index=short)
    x = b + np.where(short.year == 2005, 0.004, 0.0) + np.where(short.year == 2015, 0.002, 0.0)
    assert battery.edge_by_year(x, b).idxmax() == 2015        # what the year added, not its daily average


def test_the_walk_forward_reads_only_the_years_before_the_one_it_trades():
    days = pd.bdate_range("2005-01-03", "2012-12-31")
    rng = np.random.default_rng(17)
    steady = pd.Series(rng.normal(0.0005, 0.01, len(days)), index=days)
    burst = pd.Series(rng.normal(-0.0005, 0.01, len(days)), index=days) + np.where(days.year == 2011, 0.02, 0.0)
    frame = pd.DataFrame({"A": 1.0}, index=days)
    market = Market(frame, frame.astype(bool), pd.Series(0.0, index=days), frame)
    legs = [battery.Leg(frame * w, engine.Result(r, pd.DataFrame(), r * 0, frame * w), None, None, None)
            for w, r in ((0.1, steady), (0.2, burst))]
    spliced, _ = battery.walk_forward(legs, market, slice(days[0], days[-1]))
    assert (spliced.loc["2011", "A"] == 0.1).all()             # 2011 is chosen on 2005 to 2010
    assert (spliced.loc["2005":"2007", "A"] == 0.1).all()      # the base runs the first three years


def test_the_walk_forward_trades_its_pick_from_the_first_session_of_each_year():
    days = pd.bdate_range("2005-01-03", "2010-12-31")
    rng = np.random.default_rng(19)
    frame = pd.DataFrame({"A": 1.0}, index=days)
    market = Market(frame, frame.astype(bool), pd.Series(0.0, index=days), frame)
    monthly = pd.Series(np.arange(len(days)) % 21 == 7, index=days)
    legs = []
    for w, drift in ((0.1, -0.0003), (0.2, 0.0006)):
        r = pd.Series(rng.normal(drift, 0.01, len(days)), index=days)
        legs.append(battery.Leg((frame * w).where(monthly, axis=0), engine.Result(r, pd.DataFrame(), r * 0, frame * w),
                                None, None, None))
    spliced, wfe = battery.walk_forward(legs, market, slice(days[0], days[-1]))
    x = pd.concat({k: leg.result.returns for k, leg in enumerate(legs)}, axis=1)
    chosen, outside = [], []
    for year in (2008, 2009, 2010):
        first = days[days.year == year][0]
        scores = [stats.sharpe(x.loc[x.index.year < year, k]) for k in (0, 1)]
        pick = int(np.argmax(scores))
        assert not monthly[first] and spliced.loc[first, "A"] == (0.1, 0.2)[pick]    # no target that day: rebalanced
        chosen.append(scores[pick])
        outside.append(x.loc[x.index.year == year, pick])
    assert len(set(chosen)) == 3
    assert wfe == pytest.approx(stats.sharpe(pd.concat(outside)) / np.mean(chosen), rel=1e-12)


def sided(signal):
    def positions(market, span=10, side="with"):
        return signal_strategy(signal if side == "with" else -signal)(market, span)
    return positions


def test_a_variant_that_reads_the_signal_upside_down_fails_stability(planted):
    market, _, signal = planted
    variants = ({"span": 10, "side": "with"}, {"span": 10, "side": "against"})
    verdict = judge(sided(signal), market, card("upside-01", variants))
    mine = own_runs(sided(signal), market, variants)
    sharpes = [stats.sharpe(above(r, mine.inside, mine.period)) for r in mine.result]
    f = verdict.gates[4].figures
    assert f["worst variant Sharpe"] == pytest.approx(min(sharpes), rel=1e-12) and min(sharpes) < 0 < max(sharpes)
    assert verdict.gates[1].passed and verdict.gates[3].passed       # the base alone passes gates 2 and 4
    assert not f["blend passes gate 2"] and not f["blend passes gate 4"] and not verdict.gates[4].passed


def test_the_blend_trades_on_every_day_a_variant_trades(planted):
    market = planted[0].window("2005-01-01", "2006-12-31")
    base = pd.DataFrame(np.nan, index=market.prices.index, columns=market.prices.columns)
    one, two = base.copy(), base.copy()
    one.iloc[::10], two.iloc[5::10] = 1 / 8, 1 / 8
    legs = [battery.Leg(p, *battery.strategy_runs(market, p, NO_CRYPTO), *battery.benchmarks(market, p, NO_CRYPTO))
            for p in (one, two)]
    trading = battery.blended(legs, market, NO_CRYPTO).positions.notna().any(axis=1)
    assert trading.equals(one.notna().any(axis=1) | two.notna().any(axis=1))


def test_a_card_that_chooses_is_judged_on_its_walk_forward_choices(planted):
    market, strategy, _ = planted
    variants = ({"span": 10}, {"span": 40}, {"span": 80})
    verdict = judge(strategy, market, card("synthetic-02", variants, choose=True))
    assert verdict.gates[4].figures["walk-forward efficiency"] > battery.MIN_WFE
    # the neighbours move the base variant, and are compared with the base, not with the choices
    inside = market.window(*battery.IN_SAMPLE)
    period = slice(battery.first_holding(battery.targets(strategy, inside, {"span": 10})),
                   pd.Timestamp(battery.IN_SAMPLE[1]))
    sharpe = {span: stats.sharpe(battery.excess(battery.at_cost(inside, battery.targets(strategy, inside, {"span": span}),
                                                                NO_CRYPTO), inside.rf, period)) for span in (10, 12)}
    assert verdict.evidence["neighbours"]["span=12"] == pytest.approx(sharpe[12] / sharpe[10], rel=1e-9)


# --------------------------------------------------------------------------- gate 6

def test_an_edge_carried_by_one_asset_fails_robustness():
    market, signal = synthetic_market(6, beta=0.0)
    edge, planted_signal = synthetic_market(1, beta=0.08)
    prices = market.prices.copy()
    prices["S1"] = edge.prices["S1"]           # S1 comes from the planted market; the other seven have no edge
    one = Market(prices, market.tradable, market.rf, prices.copy())
    signal = signal.copy()
    signal["S1"] = planted_signal["S1"]
    gate = judge(signal_strategy(signal), one).gates[5]
    assert gate.figures["asset with the largest share"] == "S1"
    assert gate.figures["largest P&L share"] > battery.MAX_ASSET_SHARE and not gate.passed


@pytest.mark.parametrize("choose", [False, True])
def test_a_neighbour_that_sets_the_base_s_targets_fails_robustness(planted, choose):
    """A count written as a real number takes real neighbours; a rule that rounds its count holds
    the base itself at 1.5 and 2.5, which test nothing. So does a neighbour that differs from the
    base only before its first holding. One that differs by 0.0025% on the first holding or on the
    last in-sample session, that starts holding later, that goes to cash for a session where the
    base holds, or that sets again the base's target where the base lets its weights drift, moves
    it. A card that chooses compares them with its base, not with the choices it trades."""
    market, _, signal = planted
    last = market.prices.index[market.prices.index <= battery.IN_SAMPLE[1]][-1]

    def top(market, k=2.0, span=10, side="with", early=1.0, bump=1.0, wait=1.0, first=1.0, gap=1.0, again=1.0):
        score = signal.reindex(market.prices.index)[market.prices.columns].ewm(span=span).mean().shift(1)
        score = score if side == "with" else -score
        chosen = (score.rank(axis=1, ascending=False, method="first") <= round(k)).astype(float)
        weights = chosen.div(chosen.sum(axis=1).where(chosen.sum(axis=1) > 0), axis=0).fillna(0.0)
        out = weights.where(pd.Series(np.arange(len(weights)) % 5 == 0, index=weights.index), axis=0)
        out.iloc[:int(40 * wait)] = np.nan
        out.iloc[int(10 * early)] = 0.0                     # a row of no holding, before the first
        start = int(40 * wait)                              # the first holding, 0.0025% less
        out.iloc[start] = weights.iloc[start] * (1 - 1e-4 * abs(first - 1))
        if gap != 1:
            out.iloc[start + 1] = 0.0                       # cash, where the base holds
        if again != 1:
            out.iloc[start + 2] = out.iloc[start]           # the base's target set again, where it drifts
        if last in out.index:
            out.loc[last] = weights.loc[last] * (1 - 1e-4 * abs(bump - 1))
        return out

    base = {"k": 2.0, "early": 1.0, "bump": 1.0, "wait": 1.0, "first": 1.0, "gap": 1.0, "again": 1.0}
    variants = ({**base, "side": "against"}, {**base, "side": "with"}) if choose else (base,)
    moves = {"k": {25: [1.5, 2.5], 50: [1.0, 3.0]}, "early": {25: [0.75, 1.25], 50: [0.5, 1.5]},
             "bump": {25: [0.75, 1.25], 50: [0.5, 1.5]}, "wait": {25: [0.75, 1.25], 50: [0.5, 1.5]},
             "first": {25: [0.75, 1.25], 50: [0.5, 1.5]}, "gap": {25: [0.75, 1.25], 50: [0.5, 1.5]},
             "again": {25: [0.75, 1.25], 50: [0.5, 1.5]}}
    counted = battery.Card("counted-01", EIGHT, variants, moves, choose=choose)
    verdict = judge(top, market, counted)
    if choose:                                             # it trades the other variant from its fourth year
        inside = market.window(*battery.IN_SAMPLE)
        base = battery.targets(top, inside, variants[0])
        legs = [battery.Leg(p, r, r, r, r) for p in (base, battery.targets(top, inside, variants[1]))
                for r in [battery.at_cost(inside, p, NO_CRYPTO)]]
        period = slice(battery.first_holding(base), pd.Timestamp(battery.IN_SAMPLE[1]))
        assert not battery.same_rows(battery.walk_forward(legs, inside, period)[0].loc[period], base.loc[period])
    gate = verdict.gates[5]
    assert gate.figures["neighbours that hold the base"] == ["k=1.5", "k=2.5", "early=0.75", "early=1.25",
                                                             "early=0.5", "early=1.5", "wait=0.75", "wait=0.5"]
    assert "k=1.5, k=2.5, early=0.75, early=1.25, early=0.5, early=1.5, wait=0.75, wait=0.5 set the base's " \
           "targets on every " \
           "session from its first holding" in gate.reason and not gate.passed


def test_an_edge_that_lives_in_one_cluster_fails_when_it_is_left_out():
    market, signal = synthetic_market(6, beta=0.0)
    edge, planted_signal = synthetic_market(1, beta=0.08)
    prices, signal = market.prices.copy(), signal.copy()
    for ticker in ("S1", "S2", "S3"):          # cluster a
        prices[ticker], signal[ticker] = edge.prices[ticker], planted_signal[ticker]
    gate = judge(signal_strategy(signal), Market(prices, market.tradable, market.rf, prices.copy())).gates[5]
    assert gate.figures["worst cluster out"] == "a"
    assert gate.figures["worst cluster out ratio"] < battery.CLUSTER_OUT and not gate.passed


def test_a_cluster_left_out_is_not_held_but_still_read():
    """Gate 6, version 2: a rule that trades cluster b on cluster a's signal keeps its signal when a is
    left out, and holds nothing of a; left out itself, b takes the rule's profit with it."""
    market, signal = synthetic_market(6, beta=0.0)
    edge, planted_signal = synthetic_market(1, beta=0.08)
    prices = market.prices.copy()
    for lag in ("S4", "S5", "S6"):                                  # b's returns reward a planted signal
        prices[lag] = edge.prices[lag]
    read = signal.copy()
    for lead, lag in (("S1", "S4"), ("S2", "S5"), ("S3", "S6")):   # which a's signal carries: a leads b
        read[lead] = planted_signal[lag]

    def cross(market, span=10, every=5):
        s = read.reindex(market.prices.index)[["S1", "S2", "S3"]].ewm(span=span).mean().shift(1)
        lead = market.signal_prices[["S1", "S2", "S3"]]                          # read, never held
        score = pd.DataFrame(s.clip(lower=0).to_numpy(), index=s.index, columns=["S4", "S5", "S6"])
        score = score.where(market.tradable[["S4", "S5", "S6"]] & lead.notna().to_numpy(), 0.0).fillna(0.0)
        total = score.sum(axis=1)
        weights = score.div(total.where(total > 0), axis=0).fillna(0.0).reindex(columns=market.prices.columns,
                                                                                   fill_value=0.0)
        out = weights * np.nan
        out.iloc[::every] = weights.iloc[::every]
        return out

    whole = Market(prices, market.tradable, market.rf, prices.copy())
    clusters_out = judge(cross, whole).evidence["clusters out"]
    assert clusters_out["a"] == pytest.approx(1.0, rel=1e-9)                 # a is read, never held: nothing moves
    assert clusters_out["b"] == 0.0                                          # b held the profit: none is left
    inside = whole.window(*battery.IN_SAMPLE)
    unheld = battery.unheld(inside, ["S1", "S2", "S3"])
    assert not unheld.tradable[["S1", "S2", "S3"]].any().any() and unheld.prices.equals(inside.prices)


def test_a_clone_of_a_survivor_fails_robustness(planted, verdict):
    mine = verdict.trials[0]
    survivor = battery.Trial("old-01/0@000000000000", mine.monthly, mine.sharpe, survivor=True)
    gate = judge(planted[1], planted[0], history=[survivor]).gates[5]
    assert gate.figures["highest correlation with a survivor"] > battery.MAX_CORRELATION and not gate.passed
    assert "old-01/0@000000000000" in gate.reason


def test_only_a_survivor_counts_as_a_clone_and_only_for_its_bets(planted, verdict):
    mine = verdict.trials[0]
    rejected = battery.Trial("old-02/0@000000000000", mine.monthly, mine.sharpe)             # the same bets, rejected
    market = battery.Trial("old-03/0@000000000000", battery.monthly(verdict.evidence["benchmark excess"]), 0.5,
                           survivor=True)                                                    # the market's returns
    gate = judge(planted[1], planted[0], history=[rejected, market]).gates[5]
    assert gate.figures["survivor most correlated"] == "old-03/0@000000000000"
    assert abs(gate.figures["highest correlation with a survivor"]) < 0.3


def test_gate_two_is_judged_again_without_bitcoin(verdict):
    market, signal = synthetic_market(4, coin=True)                       # no edge, with bitcoin or without
    signal = signal.assign(COIN=signal["S1"].to_numpy()[::-1])            # the rule holds the coin too
    strategy, coin, universe = signal_strategy(signal), frozenset({"COIN"}), (*EIGHT, "COIN")
    with_coin = judge(strategy, market, battery.Card("coin-03", universe, ({"span": 10},), NEIGHBOURS), crypto=coin)
    inside = battery.restrict(market, universe).window(*battery.IN_SAMPLE)
    assert battery.targets(strategy, inside, {"span": 10})["COIN"].gt(0).any()
    period = slice(battery.first_holding(battery.targets(strategy, inside, {"span": 10})), pd.Timestamp(battery.IN_SAMPLE[1]))
    rest = battery.restrict(inside, EIGHT)
    positions = battery.targets(strategy, rest, {"span": 10}, left_out=["COIN"])
    x = above(engine.run(rest.prices, positions, costs.per_side(EIGHT, 1, coin), rest.rf), rest, period)
    b = above(costs.benchmark(rest, positions, 1, coin), rest, period)
    without = with_coin.evidence["without bitcoin"]
    assert without["Sharpe"] == pytest.approx(stats.sharpe(x), rel=1e-9)
    assert without["alpha"] == pytest.approx(stats.alpha(x, b), rel=1e-9)
    assert with_coin.gates[5].figures["gate 2 without bitcoin"] is False
    assert "gate 2 without bitcoin" not in verdict.gates[5].figures


def test_each_asset_s_share_of_the_pnl_is_what_it_held_overnight_times_its_return():
    days = pd.bdate_range("2020-01-06", periods=4)
    prices = pd.DataFrame({"A": [100, 110, 110, 121], "B": [100, 100, 90, 90]}, index=days, dtype=float)
    weights = pd.DataFrame({"A": [1.0, 0.0, 1.0, 1.0], "B": [0.0, 1.0, 0.0, 0.0]}, index=days)
    returns = pd.Series([0.0, 0.10, -0.10, 0.10], index=days)
    market = Market(prices, prices.notna(), pd.Series(0.0, index=days), prices)
    shares = battery.pnl_shares(engine.Result(returns, pd.DataFrame(), returns * 0, weights), market, slice(None))
    a, b = 1e6 * 0.10 + 0.99e6 * 0.10, 1.1e6 * -0.10
    assert shares["A"] == pytest.approx(a / (a + b)) and shares["B"] == pytest.approx(b / (a + b))


def test_a_ratio_to_a_base_that_lost_is_zero():
    assert battery.ratio(0.3, 0.6) == 0.5
    assert battery.ratio(0.5, 0.0) == 0.0 and battery.ratio(0.5, -0.1) == 0.0


# --------------------------------------------------------------------------- gate 7

def test_the_holdout_stays_sealed_until_gate_seven(planted):
    market, strategy, _ = planted

    def sealed(market, span=10, every=5):
        if market.prices.index[-1] > pd.Timestamp(battery.IN_SAMPLE[1]):
            raise RuntimeError("reads the holdout")
        return strategy(market, span, every)

    verdict = judge(sealed, market)
    assert all("reads the holdout" not in g.reason for g in verdict.gates[:6])
    assert not verdict.gates[6].passed and "reads the holdout" in verdict.gates[6].reason


def test_an_edge_that_turns_in_the_holdout_fails_gate_seven():
    market, signal = synthetic_market(1, beta=0.08, holdout_beta=-0.08)
    gate = judge(signal_strategy(signal), market).gates[6]
    assert gate.figures["holdout Sharpe"] < gate.figures["Sharpe floor"] and not gate.passed


def test_a_variant_that_changes_its_past_when_it_sees_the_holdout_fails_gate_seven(planted):
    market, strategy, _ = planted

    def rewrites(market, span=10, past="kept"):
        out = strategy(market, span)
        if past == "rewritten" and market.prices.index[-1] > pd.Timestamp(battery.IN_SAMPLE[1]):
            out = out * 0.5
        return out

    variants = ({"span": 10, "past": "kept"}, {"span": 10, "past": "rewritten"})
    for choose in (False, True):
        gate = judge(rewrites, market, card("rewrite-01", variants, choose=choose)).gates[6]
        assert gate.figures["variants rewritten"] == 1 and not gate.passed, choose


def test_a_rewrite_of_the_last_in_sample_weeks_alone_fails_gate_seven(planted):
    market, strategy, _ = planted

    def rewrites_december(market, span=10, past="kept"):
        out = strategy(market, span)
        if past == "rewritten" and market.prices.index[-1] > pd.Timestamp(battery.IN_SAMPLE[1]):
            december = (out.index >= pd.Timestamp("2022-12-01")) & (out.index <= pd.Timestamp(battery.IN_SAMPLE[1]))
            out.loc[december] = out.loc[december] * 0.5
        return out

    variants = ({"span": 10, "past": "kept"}, {"span": 10, "past": "rewritten"})
    gate = judge(rewrites_december, market, card("rewrite-02", variants)).gates[6]
    assert gate.figures["variants rewritten"] == 1 and not gate.passed


def test_every_variant_is_checked_for_look_ahead_inside_the_holdout(planted):
    market = planted[0]

    def peeks_later(market, span=10, timing="clean"):
        out = momentum(1)(market, span)
        if timing == "tomorrow":
            after = out.index > pd.Timestamp(battery.IN_SAMPLE[1])
            out.loc[after] = momentum(-1)(market, span).loc[after]
        return out

    verdict = judge(peeks_later, market, card("peek-01", ({"span": 10, "timing": "clean"},
                                                          {"span": 10, "timing": "tomorrow"})))
    assert verdict.gates[0].figures["look-ahead breaks"] == 0
    assert verdict.gates[6].figures["look-ahead breaks"] > 0 and not verdict.gates[6].passed


def test_a_card_that_chooses_trades_the_variant_with_the_best_in_sample_sharpe_in_the_holdout(planted):
    market, _, signal = planted
    for variants, best in ((({"span": 10, "side": "against"}, {"span": 10, "side": "with"}), 1),
                           (({"span": 10, "side": "with"}, {"span": 10, "side": "against"}), 0)):
        gate = judge(sided(signal), market, card("sided-01", variants, choose=True)).gates[6]
        assert gate.figures["variant traded"] == best


def test_the_holdout_keeps_the_in_sample_choices_and_trades_its_pick_from_its_first_session():
    days = pd.bdate_range("2022-01-03", "2023-06-30")
    tickers = list(EIGHT[:4])
    choosing = battery.Card("splice-01", tuple(tickers), ({"k": "a"}, {"k": "b"}), choose=True)
    monthly = pd.Series(np.arange(len(days)) % 21 == 10, index=days)
    runs = [pd.DataFrame(w, index=days, columns=tickers).where(monthly, axis=0) for w in (0.25, 0.1)]
    rng = np.random.default_rng(22)
    legs = [battery.Leg(None, engine.Result(pd.Series(rng.normal(mu, 0.01, len(days)), index=days), None, None, None),
                        None, None, None) for mu in (0.0, 0.002)]
    choices = pd.DataFrame(0.2, index=days, columns=tickers).where(monthly, axis=0)     # what the walk-forward chose
    period = slice(days[0], pd.Timestamp(battery.IN_SAMPLE[1]))
    positions, pick = battery.splice_holdout(choosing, runs, legs, choices, pd.Series(0.0, index=days), period)
    before = positions.index <= pd.Timestamp(battery.IN_SAMPLE[1])
    assert pick == 1 and battery.same_rows(positions.loc[before], choices.loc[before])
    first = positions.index[~before][0]
    assert not monthly[first] and (positions.loc[first] == 0.1).all()                # rebalanced into the pick
    later = positions.index > first
    assert battery.same_rows(positions.loc[later], runs[1].loc[later])


def test_the_holdout_s_pick_is_measured_over_the_evaluation_period_alone():
    days = pd.bdate_range("2021-01-04", "2023-06-30")
    tickers = list(EIGHT[:4])
    choosing = battery.Card("splice-02", tuple(tickers), ({"k": "a"}, {"k": "b"}), choose=True)
    runs = [pd.DataFrame(w, index=days, columns=tickers) for w in (0.25, 0.1)]
    start = pd.Timestamp("2022-01-03")                                  # the base's first holding
    before, noise = days < start, np.random.default_rng(24).normal(0, 0.01, len(days))
    returns = [np.where(before, 0.01, -0.001) + noise, np.where(before, -0.01, 0.001) + noise]
    legs = [battery.Leg(None, engine.Result(pd.Series(r, index=days), None, None, None), None, None, None)
            for r in returns]
    period = slice(start, pd.Timestamp(battery.IN_SAMPLE[1]))
    _, pick = battery.splice_holdout(choosing, runs, legs, runs[0], pd.Series(0.0, index=days), period)
    assert pick == 1                                                    # the better before the period does not count


def test_the_bootstrap_draws_paths_of_its_window_in_blocks_of_a_month_on_average(monkeypatch):
    seen, statistics = {}, battery.path_statistics

    def watched(x, b):
        seen["x"] = x
        return statistics(x, b)

    monkeypatch.setattr(battery, "path_statistics", watched)
    n = 4000
    positions = pd.Series(np.arange(n, dtype=float))                    # each value is its own index
    battery.bootstrap(positions, positions, np.random.default_rng(23))
    paths = seen["x"].astype(int)
    assert paths.shape == (battery.BOOTSTRAPS, battery.WINDOW)
    starts = (np.diff(paths, axis=1) % n != 1).mean()                  # a block starts where a path does not step on
    assert 1 / starts == pytest.approx(battery.MEAN_BLOCK, rel=0.05)


def test_the_bootstrap_keeps_each_day_s_strategy_and_benchmark_returns_together():
    rng = np.random.default_rng(18)
    b = pd.Series(rng.normal(0.0003, 0.01, 4000))
    sharpes, alphas = battery.bootstrap(2 * b, b, rng)
    assert len(sharpes) == battery.BOOTSTRAPS and np.abs(alphas).max() < 1e-12   # beta 2, no alpha, on every path
    x = 0.0002 + 1.5 * b + pd.Series(rng.normal(0, 0.005, 4000))
    one_sharpe, one_alpha = battery.path_statistics(x.to_numpy()[None], b.to_numpy()[None])
    assert one_sharpe[0] == pytest.approx(stats.sharpe(x), rel=1e-12)
    assert one_alpha[0] == pytest.approx(stats.alpha(x, b), rel=1e-9)


# --------------------------------------------------------------------------- targets and cards

def test_targets_on_assets_or_dates_outside_the_market_are_refused(planted):
    market, strategy, _ = planted

    def extra(market, span=10, every=5):
        return strategy(market, span, every).assign(ZZZ=0.0)

    def month_ends(market, span=10, every=5):
        return strategy(market, span, every).resample("ME").last()  # calendar month ends, weekends included

    def text_dates(market, span=10, every=5):
        out = strategy(market, span, every)
        return out.set_axis([str(day.date()) for day in out.index])  # compared with the sessions, never aligned

    assert "outside its market: ZZZ" in judge(extra, market).gates[0].reason
    assert "not sessions" in judge(month_ends, market).gates[0].reason
    assert "not sessions" in judge(text_dates, market).gates[0].reason


def test_an_asset_left_out_is_sold_where_the_strategy_names_it(planted):
    inside = planted[0].window(*battery.IN_SAMPLE)
    first, rest = EIGHT[0], list(EIGHT[1:])

    def all_in_first(market):
        out = pd.DataFrame(np.nan, index=market.prices.index, columns=[first])
        out.iloc[::20] = 1.0
        return out

    kept = battery.targets(all_in_first, battery.restrict(inside, rest), {}, left_out=[first])
    assert list(kept.columns) == rest
    assert (kept.iloc[::20] == 0.0).all().all() and kept.drop(kept.index[::20]).isna().all().all()
    with pytest.raises(ValueError, match="outside its market"):
        battery.targets(all_in_first, battery.restrict(inside, rest), {})


def test_a_card_has_one_to_three_variants_and_declared_neighbours():
    with pytest.raises(ValueError, match="one to three"):
        battery.Card("x", EIGHT, ({"span": 1},) * 4)
    with pytest.raises(ValueError, match="the base's parameters"):
        battery.Card("x", EIGHT, ({"span": 10}, {"spna": 20}), NEIGHBOURS)
    for neighbours in ({**NEIGHBOURS, "lag": {25: [1, 2]}}, {"span": {**NEIGHBOURS["span"], 75: [3, 18]}}):
        with pytest.raises(ValueError, match="a base parameter, at ±25% and ±50%"):
            battery.Card("x", EIGHT, ({"span": 10},), neighbours)
    for steps in ({25: [8, 12], 50: [4, 15]}, {25: [10, 12], 50: [5, 15]}, {25: [8, 12]}, {25: [9, 11], 50: [5, 15]}):
        with pytest.raises(ValueError, match="neighbours of 'span'"):
            battery.Card("x", EIGHT, ({"span": 10},), {"span": steps})
    battery.Card("x", EIGHT, ({"span": 10},), NEIGHBOURS)
    with pytest.raises(ValueError, match="one on each side"):     # 1.5 rounds to 2: the base itself, not a neighbour
        battery.Card("x", EIGHT, ({"span": 2},), {"span": {25: [2, 3], 50: [1, 3]}})
    battery.Card("x", EIGHT, ({"span": 2},), {"span": {25: [1, 3], 50: [1, 3]}})
    battery.Card("x", EIGHT, ({"lag": 1},), {"lag": {25: [2], 50: [2]}})     # below 1, a count rounds to 1 or to 0
    for steps in ({25: [0, 2], 50: [0, 2]}, {25: [1, 2], 50: [2]}, {25: [2], 50: [3]}, {25: [2, 2], 50: [2]}, {25: [2]}):
        with pytest.raises(ValueError, match="at ±(25|50)%: 2 alone"):
            battery.Card("x", EIGHT, ({"lag": 1},), {"lag": steps})
    with pytest.raises(ValueError, match="neighbours of 'lag' are numbers"):
        battery.Card("x", EIGHT, ({"lag": 1},), {"lag": {25: ["zero", 2], 50: [0, 2]}})
    with pytest.raises(ValueError, match="neighbours of 'span' are numbers"):
        battery.Card("x", EIGHT, ({"span": 10},), {"span": {25: [True, 12], 50: [5, 15]}})
    for base, steps in ((1, {25: [0.75, 1.25], 50: [0.5, 1.5]}), (2, {25: [1.0, 3], 50: [1, 3]})):
        with pytest.raises(ValueError, match=f"whole numbers, like its base {base}"):   # a whole number moves whole
            battery.Card("x", EIGHT, ({"span": base},), {"span": steps})
    battery.Card("x", EIGHT, ({"span": 2.0},), {"span": {25: [1.5, 2.5], 50: [1.0, 3.0]}})   # 2.0 is a real number
    with pytest.raises(ValueError, match="1.5 and 2.5, within 1% of the base"):
        battery.Card("x", EIGHT, ({"span": 2.0},), {"span": {25: [1, 3], 50: [1, 3]}})
    battery.Card("x", EIGHT, ({"rate": 0.5},), {"rate": {25: [0.371, 0.629], 50: [0.25, 0.75]}})   # within 1% of the base
    for below in (0.36, 0.366):
        with pytest.raises(ValueError, match="neighbours of 'rate' at ±25%: 0.375 and 0.625, within 1% of the base"):
            battery.Card("x", EIGHT, ({"rate": 0.5},), {"rate": {25: [below, 0.625], 50: [0.25, 0.75]}})
    for text in ("1", "0.5"):
        with pytest.raises(ValueError, match=f"'k' is the text '{text}': a number is written as a number"):
            battery.Card("x", EIGHT, ({"k": text},))
    battery.Card("x", EIGHT, ({"how": "fast"},))


def test_a_card_s_in_sample_period_ends_where_the_lab_s_does():
    battery.Card("x", EIGHT, ({},), in_sample=("2010-01-01", "2022-12-31"))
    battery.Card("x", EIGHT, ({},), in_sample=("2014-06-30", "2022-12-31"))
    battery.Card("x", EIGHT, ({},), in_sample=("2014-07-09", "2022-12-31"))    # 126 weekdays left in 2014
    with pytest.raises(ValueError, match="leaves 2 blocks of 126 sessions or more, and gate 5 needs 3"):
        battery.Card("x", EIGHT, ({},), in_sample=("2014-07-10", "2022-12-31"))    # gate 5 could never pass
    for dates in (("2004-01-01", "2022-12-31"), ("2005-01-01", "2015-12-31"), ("2005", "2022")):
        with pytest.raises(ValueError, match="ends on 2022-12-31"):
            battery.Card("x", EIGHT, ({},), in_sample=dates)
    with pytest.raises(ValueError, match="holdout is 2023-01-01"):
        battery.Card("x", EIGHT, ({},), holdout=("2024-01-01", "2025-12-31"))


def test_a_card_holds_four_assets_at_least_each_named_once():
    with pytest.raises(ValueError, match="4 assets at least"):
        battery.Card("x", EIGHT[:3], ({},))
    battery.Card("x", EIGHT[:4], ({},))
    with pytest.raises(ValueError, match="once"):
        battery.Card("x", (*EIGHT[:4], "S1"), ({},))


def equal_parts(every):
    """Every asset that trades, in equal parts, reset every `every` sessions: its benchmark, or, where
    an asset starts off its grid, its benchmark again from its next reset."""
    def positions(market, span=10):
        w = market.tradable.astype(float)
        w = w.div(w.sum(axis=1).where(w.sum(axis=1) > 0), axis=0).fillna(0.0)
        return w.where(pd.Series(np.arange(len(w)) % every == 0, index=w.index), axis=0)
    return positions


def test_the_battery_reads_nothing_in_a_strategy_that_is_its_benchmark():
    """Gates 2, 4 and 5 read exact zeros, whatever the rounding of a beta computed near 1."""
    market, _ = synthetic_market(21)
    verdict = judge(equal_parts(5), market)
    gates, ev = {g.number: g for g in verdict.gates}, verdict.evidence
    assert (ev["excess"] - ev["benchmark excess"]).abs().max() <= stats.SAME
    assert gates[2].figures["alpha"] == 0.0 and gates[2].figures["alpha at 2x costs"] == 0.0 and not gates[2].passed
    assert gates[4].figures["appraisal ratio"] == 0.0 and not gates[4].passed
    assert all(a is None or a == 0.0 for a in ev["blocks"].values()) and gates[5].figures["positive blocks"] == 0
    assert gates[5].figures["alpha without the best year"] == 0.0
    assert (ev["edge"] == 0.0).all() and (ev["edge by year"] == 0.0).all() and (ev["blend edge"] == 0.0).all()
    assert all(t.sharpe == 0.0 for t in verdict.trials)


def test_after_a_late_start_the_blocks_where_the_rule_is_its_benchmark_to_rounding_read_zero():
    """An asset starts off the rule's grid of 21 sessions: once the rule has caught up, it is its
    benchmark to rounding, not exactly, and gate 5's blocks there are zero."""
    market, _ = synthetic_market(21)
    prices = market.prices.copy()
    prices.loc[prices.index < prices.index[21 * 60 + 7], "S8"] = np.nan
    verdict = judge(equal_parts(21), Market(prices, prices.notna(), market.rf, prices))
    x, b = verdict.evidence["excess"], verdict.evidence["benchmark excess"]
    for block, (first, last) in (("2015-2019", ("2015", "2019")), ("2020-2022", ("2020", "2022"))):
        assert 0 < (x.loc[first:last] - b.loc[first:last]).abs().max() <= stats.SAME
        assert verdict.evidence["blocks"][block] == 0.0
    assert {g.number: g for g in verdict.gates}[7].figures["holdout alpha"] == 0.0

