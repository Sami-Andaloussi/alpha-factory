"""The battery: gates 1 to 7.

Each gate removes one way of being fooled. It computes its figures, then decides from its figures
alone, with a one-line reason; every gate is computed every time, and the verdict is the first gate
failed. Gate 8, paper trading, runs on its own clock.

A strategy is a function `positions(market, **parameters)` returning target weights for each
session of `market`, NaN to hold (`lab/engine.py`). The weights set for session t are traded at the
close of t, so they may read the market up to t-1 only: every estimate on windows ending at t-1,
and bitcoin through `signal_prices`, whose close is one day late. Gate 1 checks both, for every
variant.

The thresholds below were set before any card. `THRESHOLDS` is the battery's version, written with
every verdict: changing a threshold, or how a gate computes its figures, is a versioned decision that
applies only to later cards. Version 2 (2026-09-25): gate 6 leaves a cluster out by making its assets
untradable, their prices still read, where version 1 removed them from the market; a rule that trades
one market on another's signal keeps its signal when the market it reads is left out. Version 3
(2026-09-25): a card declares its signal's memory, the sessions it reads back from the session before
a target, a year unless it says more; gate 1 checks it, the targets unchanged when the prices older
than the memory are scrambled, and gate 3 draws no placebo shift that would hold, past the circular
wrap, weights whose signal read the day they are paid on: shifts back of a year at least, and
forward, past the wrap, of the memory and two sessions at least — two sessions more than version 2
for a signal of a year. Version 4 (2026-09-25): every return the gates judge is counted from the
first session the strategy holds an asset into, the session after its first target, whose orders
fill at that target's close; version 3 counted the target's own session, on which a strategy that
starts late holds nothing while its benchmark, invested from the first session, earns the day. That
session, and the entry's cost paid on it, count in no return: at the data's first session both the
strategy and the benchmark lose their entry, and for a late start neither entry is counted. The
targets are still judged from the first target: gate 1's checks and count, and gate 6's neighbours
that set the base's targets; gate 3's placebos, which price each day but their window's first, run
from it too, and are version 3's.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from lab import costs, engine, stats
from lab.data import Market
from lab.universe import cluster_of

THRESHOLDS = 4
IN_SAMPLE = ("2005-01-01", "2022-12-31")
HOLDOUT = ("2023-01-01", "2025-12-31")
BLOCKS = (("2005-01-01", "2007-12-31"), ("2008-01-01", "2009-12-31"), ("2010-01-01", "2014-12-31"),
          ("2015-01-01", "2019-12-31"), ("2020-01-01", "2022-12-31"))
PERIODS = stats.PERIODS

# Gate 1: hygiene
CHECKED_DATES = 50            # per variant: dates where it sets a target, and as many where it holds
HOLDOUT_CHECKED_DATES = 10    # the same checks inside the holdout (gate 7)
MIN_DECISIONS = 30            # clustered decisions, in-sample
MIN_YEARS, MIN_YEARS_CRYPTO = 5, 4
# Gate 2: economic edge
MIN_SHARPE, MIN_SHARPE_DOUBLED, MAX_COST_SHARE = 0.4, 0.3, 1 / 3
# Gate 3: significance
MIN_PSR, PLACEBOS, MIN_BEATEN, MIN_SHIFT = 0.95, 1000, 0.90, 252
# Gate 4: multiple testing
MIN_DSR = 0.90
# Gate 5: stability
MIN_POSITIVE_BLOCKS, MIN_BLOCK_SESSIONS, MIN_WFE, WALK_FORWARD_START = 3, 126, 0.5, 3
# Gate 6: robustness
NEIGHBOUR_MEDIAN, NEIGHBOUR_FLOOR, CLUSTER_OUT = 0.7, 0.5, 0.5
MAX_ASSET_SHARE, DELAY_KEEP, MAX_CORRELATION = 0.30, 0.7, 0.7
# Gate 7: sealed holdout
WINDOW, BOOTSTRAPS, PERCENTILE, MEAN_BLOCK = 630, 1000, 10, 21


@dataclass(frozen=True)
class Card:
    """What the battery reads from a hypothesis card: the universe, the variants (the base first,
    three at most, each setting the base's parameters), the parameter neighbours of gate 6 as
    {parameter: {25: [..], 50: [..]}}, which every numeric base parameter must have, one on each
    side of the base (a whole number of 1 takes 2 alone), the split dates, which are the lab's (the
    holdout never moves, and the in-sample period ends where the lab's does, and may start later),
    and whether the card picks one variant by walk-forward selection. A number written as text is
    refused, since gate 6 would not move it. Two kinds of card would fail whatever their edge, and
    are refused: a universe of fewer than four assets, one of which would always carry more than
    30% of the profit (gate 6), and an in-sample period that starts too late for three blocks of
    126 weekdays (gate 5); weekdays outnumber sessions, so only a start that cannot pass is
    refused."""
    id: str
    universe: tuple[str, ...]
    variants: tuple[dict, ...]
    neighbours: dict = field(default_factory=dict)
    in_sample: tuple[str, str] = IN_SAMPLE
    holdout: tuple[str, str] = HOLDOUT
    choose: bool = False
    memory: int = MIN_SHIFT   # sessions the signal reads back from the session before a target

    def __post_init__(self):
        if isinstance(self.memory, bool) or not isinstance(self.memory, int) or self.memory < 1:
            raise ValueError("a card's memory is a whole number of sessions, one at least")
        if not 1 <= len(self.variants) <= 3:
            raise ValueError("a card has one to three variants, the base first")
        if any(set(v) != set(self.variants[0]) for v in self.variants[1:]):
            raise ValueError("every variant sets the base's parameters, and no other")
        if len(set(self.universe)) != len(self.universe):
            raise ValueError("a card's universe names each asset once")
        if len(self.universe) * MAX_ASSET_SHARE < 1:
            raise ValueError(f"a card's universe holds {math.ceil(1 / MAX_ASSET_SHARE)} assets at least: with fewer, "
                             f"one of them carries more than {MAX_ASSET_SHARE:.0%} of the profit, and gate 6 fails")
        if tuple(self.holdout) != HOLDOUT:
            raise ValueError(f"the holdout is {HOLDOUT[0]} to {HOLDOUT[1]} for every card")
        start, end = (pd.Timestamp(d) for d in self.in_sample)
        if not pd.Timestamp(IN_SAMPLE[0]) <= start < end == pd.Timestamp(IN_SAMPLE[1]):
            raise ValueError(f"the in-sample period ends on {IN_SAMPLE[1]}, and starts on {IN_SAMPLE[0]} or later")
        after = start + pd.Timedelta(days=1)          # the first target's session counts in no return
        blocks = sum(1 for first, last in BLOCKS
                     if len(pd.bdate_range(max(after, pd.Timestamp(first)), last)) >= MIN_BLOCK_SESSIONS)
        if blocks < MIN_POSITIVE_BLOCKS:
            raise ValueError(f"an in-sample period from {start:%Y-%m-%d} leaves {blocks} blocks of {MIN_BLOCK_SESSIONS} "
                             f"sessions or more, and gate 5 needs {MIN_POSITIVE_BLOCKS}: start earlier")
        for parameter, steps in self.neighbours.items():
            if parameter not in self.variants[0] or set(steps) - {25, 50}:
                raise ValueError(f"neighbours of '{parameter}': a base parameter, at ±25% and ±50%")
        for parameter, base in self.variants[0].items():
            if isinstance(base, str) and numeric(base):
                raise ValueError(f"'{parameter}' is the text '{base}': a number is written as a number, so that "
                                 f"gate 6 moves it")
            if isinstance(base, bool) or not isinstance(base, (int, float)) or base == 0:
                continue
            steps = self.neighbours.get(parameter, {})
            for step in (25, 50):
                given = steps.get(step, [])
                if any(isinstance(g, bool) or not isinstance(g, (int, float)) for g in given):
                    raise ValueError(f"neighbours of '{parameter}' are numbers, like its base {base:g}")
                if isinstance(base, int) and not all(isinstance(g, int) for g in given):
                    raise ValueError(f"neighbours of '{parameter}' are whole numbers, like its base {base}")
                if abs(base) == 1 and isinstance(base, int):
                    if list(given) != [2 * base]:
                        raise ValueError(f"neighbours of '{parameter}' at ±{step}%: {2 * base} alone, the next whole "
                                         f"number past the base {base}, since 0 counts nothing")
                    continue
                wanted, given = sorted(base * (1 + sign * step / 100) for sign in (-1, 1)), sorted(given)
                near = len(given) == 2 and all(neighbour(g, w, base) for g, w in zip(given, wanted))
                if not near or not given[0] < base < given[1]:
                    how = "rounded" if isinstance(base, int) else "within 1% of the base"
                    raise ValueError(f"neighbours of '{parameter}' at ±{step}%: {wanted[0]:g} and {wanted[1]:g}, "
                                     f"{how}, one on each side of the base {base:g}")


def numeric(text: str) -> bool:
    try:
        float(text)
    except ValueError:
        return False
    return True


def neighbour(given: float, wanted: float, base) -> bool:
    """A neighbour of gate 6: within 1% of the base from the value asked for; for a whole-number
    base, that value rounded. A whole number of 1, whose neighbours below would round to the base or
    to 0, takes 2 alone, and is checked by the card."""
    if not isinstance(base, int):
        return abs(given - wanted) <= 0.01 * abs(base)
    return abs(given - wanted) <= 0.5 + 1e-9


@dataclass(frozen=True)
class Trial:
    """One trial of the registry as gates 4 and 6 read it."""
    key: str                  # card and variant
    monthly: pd.Series        # monthly returns hedged of the benchmark, in-sample: its own bets
    sharpe: float             # annual Sharpe ratio of those hedged returns: its appraisal ratio
    survivor: bool = False    # its card passed gates 1 to 7


@dataclass
class Gate:
    number: int
    name: str
    passed: bool | None       # None: not computed, and the reason says why
    reason: str
    figures: dict = field(default_factory=dict)


@dataclass
class Verdict:
    card: str
    gates: list[Gate]
    trials: list[Trial]       # this card's variants, for the registry
    evidence: dict            # the series behind the figures, for the report
    thresholds: int = THRESHOLDS

    @property
    def failed(self) -> int | None:
        """The first gate not passed, or None when gates 1 to 7 all pass."""
        return next((g.number for g in self.gates if not g.passed), None)


@dataclass
class Leg:
    """A strategy's run on one market: at the stated costs and at twice them, and the benchmark
    traded like it at both."""
    positions: pd.DataFrame
    result: engine.Result
    doubled: engine.Result
    bench: engine.Result
    bench_doubled: engine.Result


@dataclass
class Timing:
    """The timing checks of one variant: the dates checked, and those where the positions changed
    when the future was cut off (look-ahead) or when the bar being traded was scrambled."""
    checked: int
    look_ahead: list
    same_day: list


GATES = {1: "Hygiene", 2: "Economic edge", 3: "Significance", 4: "Multiple testing",
         5: "Stability", 6: "Robustness", 7: "Sealed holdout"}


# --------------------------------------------------------------------------- the battery

def run(card: Card, strategy, market: Market, history=(), seed: int = 0,
        crypto=costs.CRYPTO, cluster=cluster_of) -> Verdict:
    """Judge a card: every gate is computed, and the verdict is the first gate failed. `history`
    holds the registry's earlier trials; `seed` makes every random draw repeatable, each gate
    drawing from a stream of its own."""
    streams = dict(zip(GATES, (np.random.default_rng(s) for s in np.random.SeedSequence(seed).spawn(len(GATES)))))
    universe = restrict(market, card.universe)
    inside = universe.window(*card.in_sample)
    gates: list[Gate] = []
    evidence: dict = {}
    try:
        variants = [targets(strategy, inside, p) for p in card.variants]
        results = engine.run_many(inside.prices, variants, fees(inside, 1, crypto), inside.rf)
        doubled = engine.run_many(inside.prices, variants, fees(inside, 2, crypto), inside.rf)
    except Exception as error:  # a strategy the engine refuses breaks hygiene; nothing else can be judged
        gates.append(Gate(1, GATES[1], False, f"the strategy cannot run: {error}"))
        gates += [Gate(n, GATES[n], None, "not computed: the strategy cannot run") for n in range(2, 8)]
        return Verdict(card.id, gates, [], evidence)

    start, held = first_holding(variants[0]), first_held(variants[0])
    if held is None:
        gates.append(Gate(1, GATES[1], False, "the base variant never holds an asset"))
        gates += [Gate(n, GATES[n], None, "not computed: nothing is held") for n in range(2, 8)]
        return Verdict(card.id, gates, [], evidence)
    period = slice(held, pd.Timestamp(card.in_sample[1]))      # the returns, from the first session held into
    decided = slice(start, pd.Timestamp(card.in_sample[1]))    # the targets, from the first
    trials: list[Trial] = []
    try:
        legs = [Leg(p, r, d, *benchmarks(inside, p, crypto)) for p, r, d in zip(variants, results, doubled)]
        trials = [trial(f"{card.id}/{k}", leg, inside.rf, period) for k, leg in enumerate(legs)]
        main, wfe = legs[0], None
        if card.choose and len(legs) > 1:
            composite, wfe = walk_forward(legs, inside, period)
            main = Leg(composite, *strategy_runs(inside, composite, crypto), *benchmarks(inside, composite, crypto))
        evidence["exposure"] = main.result.weights.loc[period].sum(axis=1)
        evidence["assets held"] = main.result.weights.loc[period].gt(1e-9).sum(axis=1)
    except Exception as error:  # the runs every gate judges: without them, no gate can be computed
        reason = f"cannot be computed: {type(error).__name__}: {error}"
        return Verdict(card.id, [Gate(n, GATES[n], False, reason) for n in GATES], trials, evidence)
    gates.append(guarded(1, hygiene, strategy, card, universe, inside, legs, main, decided, crypto, streams[1], evidence))
    gates.append(guarded(2, economic, main, inside.rf, period, evidence))
    gates.append(guarded(3, lambda: significance(main.result, inside, period, streams[3], evidence,
                                                 card.memory, decided)[0]))
    gates.append(guarded(4, lambda: multiple_testing(edge(main, inside.rf, period), trials, history, evidence)))
    gates.append(guarded(5, stability, legs, main, wfe, inside, period, trials, history, crypto, streams[5], evidence,
                         card.memory, decided))
    gates.append(guarded(6, robustness, card, strategy, inside, legs[0], main, period, history, crypto, cluster,
                         evidence, decided))
    gates.append(guarded(7, holdout, card, strategy, universe, legs, main, period, crypto, streams[7], evidence))
    return Verdict(card.id, gates, trials, evidence)


def guarded(number: int, gate, *args) -> Gate:
    """A gate whose runs break is failed, with the error as its reason: every gate is computed."""
    try:
        return gate(*args)
    except Exception as error:
        return Gate(number, GATES[number], False, f"cannot be computed: {type(error).__name__}: {error}")


# --------------------------------------------------------------------------- the gates: figures

def hygiene(strategy, card, universe, market, legs, main, period, crypto, rng, evidence) -> Gate:
    """Gate 1 protects against look-ahead, bad data and too little evidence; it decides whether the
    backtest can be believed at all. Every variant's timing is checked, since every variant counts
    in gates 4 and 5; the evidence is counted on the positions the other gates judge."""
    timing = [timing_breaks(strategy, parameters, market, leg.positions, period, rng, CHECKED_DATES)
              for parameters, leg in zip(card.variants, legs)]
    memory = [memory_breaks(strategy, parameters, market, leg.positions, period, rng, CHECKED_DATES, card.memory)
              for parameters, leg in zip(card.variants, legs)]
    problems = data_problems(universe, slice(*map(pd.Timestamp, card.in_sample)))
    figures = {"dates checked": sum(t.checked for t in timing),
               "look-ahead breaks": sum(len(t.look_ahead) for t in timing),
               "same-day breaks": sum(len(t.same_day) for t in timing),
               "memory": card.memory, "memory dates checked": sum(m[0] for m in memory),
               "memory breaks": sum(len(m[1]) for m in memory),
               "data problems": problems,
               "clustered decisions": stats.decision_clusters(main.positions.loc[period]),
               "years in-sample": len(market.prices.loc[period]) / PERIODS,
               "years needed": years_needed(market.prices.columns, crypto)}
    evidence["timing breaks"] = {k: {"look-ahead": t.look_ahead, "same-day": t.same_day, "memory": m[1]}
                                 for k, (t, m) in enumerate(zip(timing, memory))}
    evidence["target days"] = main.positions.loc[period].dropna(how="all").index
    return decide_hygiene(figures)


def economic(leg: Leg, rf, period, evidence=None) -> Gate:
    """Gate 2 protects against an edge explained by costs or by market exposure; it decides whether
    there is anything worth testing further."""
    x, b = excess(leg.result, rf, period), excess(leg.bench, rf, period)
    x2, b2 = excess(leg.doubled, rf, period), excess(leg.bench_doubled, rf, period)
    paid = leg.result.costs.loc[period]
    vol = x.std(ddof=1) * np.sqrt(PERIODS)
    figures = {"Sharpe": stats.sharpe(x), "benchmark Sharpe": stats.sharpe(b), "alpha": stats.alpha(x, b),
               "Sharpe at 2x costs": stats.sharpe(x2), "alpha at 2x costs": stats.alpha(x2, b2),
               "gross Sharpe": stats.sharpe(x + paid), "costs a year": float(paid.mean() * PERIODS),
               "costs in Sharpe units": float(paid.mean() * PERIODS / vol) if vol > 0 else float("inf")}
    if evidence is not None:
        evidence["excess"], evidence["benchmark excess"] = x, b
    return decide_economic(figures)


def significance(result: engine.Result, market: Market, period, rng, evidence=None,
                 memory: int = MIN_SHIFT, decided=None) -> tuple[Gate, np.ndarray]:
    """Gate 3 protects against luck, and against being paid only for being invested; it decides
    whether the edge is more than noise and more than exposure. A placebo shifted back by s holds,
    on the period's first s days, the weights of days later by n - s: that distance is kept beyond
    the signal's memory and two sessions, so that no placebo holds weights whose signal read the
    day they are paid on. The placebos run over `decided`, from the first target, since they price
    each day but the first: their returns, like the PSR's, start on the first session held into.
    Without `decided`, `period` must start on the first target."""
    x = excess(result, market.rf, period)
    decided = period if decided is None else decided
    sessions = len(market.prices.loc[decided])
    forward = max(MIN_SHIFT, memory + 2)
    figures = {"PSR": stats.adjusted_psr(x), "placebo sessions": sessions, "placebos": 0, "placebos beaten": None}
    placebos = np.array([])
    if sessions > MIN_SHIFT + forward + 1:
        offsets = stats.placebo_offsets(sessions, PLACEBOS, MIN_SHIFT, rng, forward)
        own, placebos = placebo_sharpes(result, market, decided, offsets)
        figures["placebos"], figures["placebos beaten"] = len(placebos), float(np.mean(placebos < own))
        if evidence is not None:
            evidence["placebos"], evidence["placebo own Sharpe"] = placebos, own
            evidence["placebo window"] = (market.prices.loc[decided].index[0], market.prices.loc[decided].index[-1])
            evidence["placebo late assets"] = late_assets(result.weights, market.tradable, decided)
    return decide_significance(figures), placebos


def multiple_testing(x: pd.Series, card_trials, history, evidence=None) -> Gate:
    """Gate 4 protects against the best of many tries; it decides whether the edge survives the
    number of trials the whole registry has made. `x` is the edge: the strategy's excess returns
    hedged of the benchmark. A long-only rule on these assets earns the market's Sharpe ratio
    without any edge, so its raw Sharpe ratio, deflated against tries worth zero, would test the
    market, not the rule."""
    trials = [*history, *card_trials]
    frame = pd.concat([t.monthly for t in trials], axis=1, keys=range(len(trials)))  # by position: names may repeat
    labels = stats.near_clone_clusters(frame)
    count = int(labels.max())
    daily = pd.Series([t.sharpe / np.sqrt(PERIODS) for t in trials]).groupby(labels).mean()
    spread = float(daily.var(ddof=1)) if len(daily) > 1 else 0.0
    variance = max(spread, 1.0 / len(x))       # never less than what luck alone gives one trial
    figures = {"trials": len(trials), "effective trials": count, "appraisal ratio": stats.sharpe(x),
               "Sharpe expected by luck": float(stats.expected_max_sharpe(count, variance) * np.sqrt(PERIODS)),
               "DSR": stats.dsr(x, count, variance)}
    if evidence is not None:
        evidence["edge"] = x
    return decide_multiple_testing(figures)


def stability(legs, main, wfe, market, period, card_trials, history, crypto, rng, evidence,
              memory: int = MIN_SHIFT, decided=None) -> Gate:
    """Gate 5 protects against an edge that lives in one variant or one episode; it decides whether
    the edge is a property of the idea rather than of one draw."""
    rf = market.rf
    blend = blended(legs, market, crypto)
    blend_edge = edge(blend, rf, period)
    checks = [economic(blend, rf, period), significance(blend.result, market, period, rng, memory=memory,
                                                         decided=decided)[0],
              multiple_testing(blend_edge, card_trials, history)]
    x, b = excess(main.result, rf, period), excess(main.bench, rf, period)
    blocks = block_alphas(x, b)
    by_year = edge_by_year(x, b)
    best = int(by_year.idxmax())
    figures = {**{f"blend passes gate {g.number}": g.passed for g in checks},
               "worst variant Sharpe": min(stats.sharpe(excess(leg.result, rf, period)) for leg in legs),
               "positive blocks": sum(1 for a in blocks.values() if a is not None and a > 0),
               "best year": best,
               "alpha without the best year": stats.alpha(x[x.index.year != best], b[b.index.year != best])}
    if wfe is not None:
        figures["walk-forward efficiency"] = wfe
    evidence["blocks"], evidence["edge by year"], evidence["blend edge"] = blocks, by_year, blend_edge
    evidence["blend"] = {g.number: g.reason for g in checks}
    return decide_stability(figures)


def robustness(card, strategy, market, base_leg, main, period, history, crypto, cluster, evidence,
               decided=None) -> Gate:
    """Gate 6 protects against a peak, one asset, timing too tight and a clone; it decides whether
    the edge survives what live trading will change. Neighbours, clusters left out and the market
    without bitcoin move the base variant, and are compared with it; the delay, the P&L shares and
    the clones judge the positions the other gates judge. A cluster left out is not held, but its
    prices are still read (`unheld`); bitcoin left out is removed from the market. `decided` is the
    span whose targets a neighbour must change, from the base's first target; `period` the returns'."""
    rf, base = market.rf, card.variants[0]
    decided = period if decided is None else decided
    base_sharpe, sharpe = (stats.sharpe(excess(leg.result, rf, period)) for leg in (base_leg, main))
    figures: dict = {}

    # parameter neighbours, one parameter at a time
    named = [(p, step, v) for p, steps in card.neighbours.items() for step, values in steps.items() for v in values]
    figures["neighbour median ratio"] = figures["lowest ±25% ratio"] = None
    figures["neighbours that hold the base"] = []
    if named:
        moved = [targets(strategy, market, {**base, p: v}) for p, _, v in named]
        runs = engine.run_many(market.prices, moved, fees(market, 1, crypto), rf)
        ratios = [ratio(stats.sharpe(excess(r, rf, period)), base_sharpe) for r in runs]
        near = [q for (_, step, _), q in zip(named, ratios) if step == 25]
        figures["neighbour median ratio"] = float(np.median(ratios))
        figures["lowest ±25% ratio"] = min(near) if near else None
        figures["neighbours that hold the base"] = [f"{p}={v}" for (p, _, v), m in zip(named, moved)
                                                    if same_rows(m.loc[decided], base_leg.positions.loc[decided])]
        evidence["neighbours"] = {f"{p}={v}": q for (p, _, v), q in zip(named, ratios)}

    # one cluster out at a time
    kept = {}
    clusters = sorted({cluster(t) for t in market.prices.columns})
    if len(clusters) > 1:
        for c in clusters:
            out = [t for t in market.prices.columns if cluster(t) == c]
            others = [t for t in market.prices.columns if t not in out]
            positions = targets(strategy, unheld(market, out), base)[others]
            result = at_cost(restrict(market, others), positions, crypto)
            kept[c] = ratio(stats.sharpe(excess(result, rf, period)), base_sharpe)
    worst = min(kept, key=kept.get) if kept else None
    figures["worst cluster out"], figures["worst cluster out ratio"] = worst, kept.get(worst)
    evidence["clusters out"] = kept

    # no single asset carries the result
    shares = pnl_shares(main.result, market, period)
    evidence["P&L shares"] = shares
    figures["largest P&L share"] = float(shares.iloc[0]) if len(shares) else None
    figures["asset with the largest share"] = shares.index[0] if len(shares) else None

    # without bitcoin, gate 2 still passes
    held = set(market.prices.columns)
    if held & set(crypto) and held - set(crypto):
        rest = restrict(market, sorted(held - set(crypto)))
        positions = targets(strategy, rest, base, left_out=held & set(crypto))
        without = economic(Leg(positions, *strategy_runs(rest, positions, crypto), *benchmarks(rest, positions, crypto)),
                           rf, period)
        figures["gate 2 without bitcoin"] = without.passed
        evidence["without bitcoin"] = without.figures

    # one extra day of delay
    late = at_cost(market, main.positions.shift(1), crypto)
    figures["one day late ratio"] = ratio(stats.sharpe(excess(late, rf, period)), sharpe)

    # not a clone of an earlier survivor: the same bets, beyond what the benchmark holds
    mine = monthly(edge(main, rf, period))
    survivors = {t.key: mine.corr(t.monthly, min_periods=24) for t in history if t.survivor}
    survivors = {k: v for k, v in survivors.items() if pd.notna(v)}
    closest = max(survivors, key=survivors.get) if survivors else None
    figures["highest correlation with a survivor"] = survivors.get(closest)
    figures["survivor most correlated"] = closest
    return decide_robustness(figures)


def holdout(card, strategy, universe, legs, main, period, crypto, rng, evidence) -> Gate:
    """Gate 7 protects against bugs and large decay, on 2023-2025 opened once; it decides whether
    the strategy still behaves on data kept aside. Every variant runs once on 2005 to 2025: none may
    change its in-sample positions when it sees the holdout, and each is checked for timing inside
    the holdout, whose data is checked as gate 1 checks the in-sample's."""
    whole = universe.window(card.in_sample[0], card.holdout[1])
    sealed = slice(pd.Timestamp(card.holdout[0]), pd.Timestamp(card.holdout[1]))
    inside_end = pd.Timestamp(card.in_sample[1])
    try:
        runs = [targets(strategy, whole, p) for p in card.variants]
        if card.choose and len(runs) > 1:
            positions, pick = splice_holdout(card, runs, legs, main.positions, whole.rf, period)
        else:
            positions, pick = runs[0], 0
        result = at_cost(whole, positions, crypto)
        bench = costs.benchmark(whole, positions, 1, crypto)
    except Exception as error:
        return Gate(7, GATES[7], False, f"the strategy cannot run on the holdout: {error}")
    rewritten = [k for k, (r, leg) in enumerate(zip(runs, legs))
                 if not same_rows(r.loc[:inside_end].reindex(leg.positions.index), leg.positions)]
    timing = [timing_breaks(strategy, p, whole, r, sealed, rng, HOLDOUT_CHECKED_DATES)
              for p, r in zip(card.variants, runs)]
    xh, bh = excess(result, whole.rf, sealed), excess(bench, whole.rf, sealed)
    sharpes, alphas = bootstrap(excess(main.result, whole.rf, period), excess(main.bench, whole.rf, period), rng)
    figures = {"holdout Sharpe": stats.sharpe(xh), "Sharpe floor": float(np.percentile(sharpes, PERCENTILE)),
               "holdout alpha": stats.alpha(xh, bh), "alpha floor": float(np.percentile(alphas, PERCENTILE)),
               "variants rewritten": len(rewritten), "dates checked": sum(t.checked for t in timing),
               "look-ahead breaks": sum(len(t.look_ahead) for t in timing),
               "same-day breaks": sum(len(t.same_day) for t in timing),
               "data problems": data_problems(universe, sealed)}
    if card.choose and len(runs) > 1:
        figures["variant traded"] = pick
    evidence["holdout excess"], evidence["holdout benchmark excess"] = xh, bh
    evidence["bootstrap"] = {"Sharpe": sharpes, "alpha": alphas}
    return decide_holdout(figures)


# --------------------------------------------------------------------------- the gates: decisions

def failing(number: int, figures: dict, failures: list[str]) -> Gate:
    return Gate(number, GATES[number], False, "; ".join(failures), figures)


def decide_hygiene(f: dict) -> Gate:
    failures = []
    if f["look-ahead breaks"]:
        failures.append(f"positions change when the future is cut off ({f['look-ahead breaks']} of "
                        f"{f['dates checked']} dates)")
    if f["same-day breaks"]:
        failures.append(f"positions read the bar they trade on ({f['same-day breaks']} of {f['dates checked']} dates)")
    if f.get("memory breaks"):
        failures.append(f"positions change when the prices older than the card's memory of {f['memory']} sessions "
                        f"are scrambled ({f['memory breaks']} of {f['memory dates checked']} dates): the card declares "
                        f"the memory its signal reads")
    if f["data problems"]:
        failures.append("the data: " + "; ".join(f["data problems"]))
    if not f["clustered decisions"] >= MIN_DECISIONS:
        failures.append(f"{f['clustered decisions']} clustered decisions, fewer than {MIN_DECISIONS}")
    if not f["years in-sample"] >= f["years needed"]:
        failures.append(f"{f['years in-sample']:.2f} years in-sample, fewer than {f['years needed']}")
    if failures:
        return failing(1, f, failures)
    return Gate(1, GATES[1], True, f"no look-ahead on {f['dates checked']} dates, {f['clustered decisions']} decisions "
                                   f"over {f['years in-sample']:.1f} years", f)


def decide_economic(f: dict) -> Gate:
    failures = []
    if not f["Sharpe"] >= MIN_SHARPE:
        failures.append(f"Sharpe {f['Sharpe']:.3f} below {MIN_SHARPE}")
    if not (f["Sharpe"] >= f["benchmark Sharpe"] and f["alpha"] > 0):
        failures.append(f"Sharpe {f['Sharpe']:.3f} against the benchmark's {f['benchmark Sharpe']:.3f}, "
                        f"alpha {f['alpha']:.2%}")
    if not (f["Sharpe at 2x costs"] >= MIN_SHARPE_DOUBLED and f["alpha at 2x costs"] > 0):
        failures.append(f"at twice the costs, Sharpe {f['Sharpe at 2x costs']:.3f} and alpha {f['alpha at 2x costs']:.2%}")
    if not (f["gross Sharpe"] > 0 and f["costs in Sharpe units"] <= f["gross Sharpe"] * MAX_COST_SHARE):
        failures.append(f"costs take {f['costs in Sharpe units']:.3f} of a gross Sharpe of {f['gross Sharpe']:.3f}, "
                        f"more than a third")
    if failures:
        return failing(2, f, failures)
    return Gate(2, GATES[2], True, f"Sharpe {f['Sharpe']:.2f} against the benchmark's {f['benchmark Sharpe']:.2f}, "
                                   f"alpha {f['alpha']:.2%}, {f['Sharpe at 2x costs']:.2f} at twice the costs", f)


def decide_significance(f: dict) -> Gate:
    failures = []
    if not f["PSR"] >= MIN_PSR:
        failures.append(f"PSR {f['PSR']:.3f} below {MIN_PSR}")
    if f["placebos beaten"] is None:
        failures.append(f"{f['placebo sessions']} sessions: too short for placebos shifted a year each way, "
                        f"beyond the signal's memory")
    elif not f["placebos beaten"] >= MIN_BEATEN:
        failures.append(f"beats {f['placebos beaten']:.1%} of its shifted placebos, fewer than {MIN_BEATEN:.0%}")
    if failures:
        return failing(3, f, failures)
    return Gate(3, GATES[3], True, f"PSR {f['PSR']:.3f}, beats {f['placebos beaten']:.0%} of {f['placebos']} "
                                   f"shifted placebos", f)


def decide_multiple_testing(f: dict) -> Gate:
    if not f["DSR"] >= MIN_DSR:
        return failing(4, f, [f"DSR {f['DSR']:.3f} below {MIN_DSR} over {f['effective trials']} effective trials"])
    return Gate(4, GATES[4], True, f"DSR {f['DSR']:.3f} over {f['effective trials']} effective trials of "
                                   f"{f['trials']}", f)


def decide_stability(f: dict) -> Gate:
    failures = []
    blend = [n for n in (2, 3, 4) if not f[f"blend passes gate {n}"]]
    if blend:
        failures.append(f"the blend of the variants fails gate{'s' if len(blend) > 1 else ''} "
                        + " and ".join(", ".join(map(str, blend)).rsplit(", ", 1)))
    if not f["worst variant Sharpe"] > 0:
        failures.append(f"the worst variant's Sharpe is {f['worst variant Sharpe']:.3f}")
    if not f["positive blocks"] >= MIN_POSITIVE_BLOCKS:
        failures.append(f"alpha positive in {f['positive blocks']} of {len(BLOCKS)} blocks, "
                        f"fewer than {MIN_POSITIVE_BLOCKS}")
    if not f["alpha without the best year"] > 0:
        failures.append(f"alpha {f['alpha without the best year']:.2%} without its best year, {f['best year']}")
    if "walk-forward efficiency" in f and not f["walk-forward efficiency"] >= MIN_WFE:
        failures.append(f"walk-forward efficiency {f['walk-forward efficiency']:.0%}, below {MIN_WFE:.0%}")
    if failures:
        return failing(5, f, failures)
    return Gate(5, GATES[5], True, f"the blend passes gates 2-4, alpha positive in {f['positive blocks']} of "
                                   f"{len(BLOCKS)} blocks and without {f['best year']}", f)


def decide_robustness(f: dict) -> Gate:
    failures = []
    median, near = f["neighbour median ratio"], f["lowest ±25% ratio"]
    if f["neighbours that hold the base"]:
        failures.append(f"{', '.join(f['neighbours that hold the base'])} set the base's targets on every session "
                        f"from its first holding: a neighbour that does not move the strategy tests nothing")
    if median is not None and not median >= NEIGHBOUR_MEDIAN:
        failures.append(f"median neighbour keeps {median:.0%} of the Sharpe, below {NEIGHBOUR_MEDIAN:.0%}")
    if near is not None and not near >= NEIGHBOUR_FLOOR:
        failures.append(f"a ±25% neighbour keeps {near:.0%}, below {NEIGHBOUR_FLOOR:.0%}")
    kept = f["worst cluster out ratio"]
    if kept is not None and not kept >= CLUSTER_OUT:
        failures.append(f"without {f['worst cluster out']} the Sharpe keeps {kept:.0%}, below {CLUSTER_OUT:.0%}")
    share = f["largest P&L share"]
    if share is None:
        failures.append("no positive P&L to share out")
    elif not share <= MAX_ASSET_SHARE:
        failures.append(f"{f['asset with the largest share']} carries {share:.0%} of the P&L, "
                        f"more than {MAX_ASSET_SHARE:.0%}")
    if f.get("gate 2 without bitcoin") is False:
        failures.append("without bitcoin, gate 2 fails")
    if not f["one day late ratio"] >= DELAY_KEEP:
        failures.append(f"one day late keeps {f['one day late ratio']:.0%} of the Sharpe, below {DELAY_KEEP:.0%}")
    correlation = f["highest correlation with a survivor"]
    if correlation is not None and not correlation <= MAX_CORRELATION:
        failures.append(f"correlates {correlation:.2f} with the survivor {f['survivor most correlated']}, "
                        f"above {MAX_CORRELATION}")
    if failures:
        return failing(6, f, failures)
    return Gate(6, GATES[6], True, "neighbours, clusters, assets, bitcoin, delay and survivors all hold", f)


def decide_holdout(f: dict) -> Gate:
    failures = []
    if not f["holdout Sharpe"] >= f["Sharpe floor"]:
        failures.append(f"holdout Sharpe {f['holdout Sharpe']:.2f} below the in-sample {PERCENTILE}th percentile "
                        f"{f['Sharpe floor']:.2f}")
    if not f["holdout alpha"] >= f["alpha floor"]:
        failures.append(f"holdout alpha {f['holdout alpha']:.2%} below the in-sample {PERCENTILE}th percentile "
                        f"{f['alpha floor']:.2%}")
    if f["variants rewritten"]:
        failures.append("given the holdout, the strategy changes its in-sample positions")
    if f["look-ahead breaks"] or f["same-day breaks"]:
        failures.append(f"in the holdout, {f['look-ahead breaks']} look-ahead and {f['same-day breaks']} same-day "
                        f"breaks on {f['dates checked']} dates")
    if f["data problems"]:
        failures.append("the holdout's data: " + "; ".join(f["data problems"]))
    if failures:
        return failing(7, f, failures)
    return Gate(7, GATES[7], True, f"holdout Sharpe {f['holdout Sharpe']:.2f} and alpha {f['holdout alpha']:.2%}, "
                                   f"both above the in-sample {PERCENTILE}th percentile", f)


# --------------------------------------------------------------------------- the pieces

def restrict(market: Market, tickers) -> Market:
    tickers = list(tickers)
    return Market(market.prices[tickers], market.tradable[tickers], market.rf, market.signal_prices[tickers])


def unheld(market: Market, tickers) -> Market:
    """The market with `tickers` never tradable, their prices still there to be read: a cluster as
    gate 6 leaves it out. A weight the strategy sets on them anyway is dropped, as on any asset
    `left_out` (`targets`)."""
    tradable = market.tradable.copy()
    tradable[list(tickers)] = False
    return Market(market.prices, tradable, market.rf, market.signal_prices)


def targets(strategy, market: Market, parameters: dict, left_out=()) -> pd.DataFrame:
    """The strategy's target weights on the market's sessions and assets. A weight on a date that
    is not one of its sessions, or on an asset it does not hold, is refused, except on the assets
    `left_out` of it (gate 6): a row that named them sells them, and they stay out. The strategy gets
    a copy of the market's frames (`handed`)."""
    positions = strategy(handed(market), **parameters)
    if not isinstance(positions, pd.DataFrame):
        raise TypeError("a strategy returns a DataFrame of target weights")
    unknown = sorted(set(positions.columns) - set(market.prices.columns) - set(left_out))
    if unknown:
        raise ValueError(f"the strategy names assets outside its market: {', '.join(map(str, unknown))}")
    inside = positions[[c for c in positions.columns if c in set(market.prices.columns)]]
    kept = inside.reindex(index=market.prices.index, columns=market.prices.columns).astype(float)
    if len(positions.index.difference(market.prices.index)) or kept.count().sum() != inside.count().sum():
        raise ValueError("the strategy sets targets on dates that are not sessions of its market")
    named = positions.notna().any(axis=1).reindex(market.prices.index, fill_value=False)
    kept.loc[named] = kept.loc[named].fillna(0.0)
    return kept


def handed(market: Market) -> Market:
    """The market as a strategy gets it: each frame copied, which costs nothing until the strategy
    edits one, so that an edit through pandas changes nothing the battery prices."""
    return Market(market.prices.copy(deep=False), market.tradable.copy(deep=False), market.rf.copy(deep=False),
                  market.signal_prices.copy(deep=False))


def fees(market: Market, multiplier: float, crypto) -> pd.Series:
    return costs.per_side(market.prices.columns, multiplier, crypto)


def at_cost(market: Market, positions: pd.DataFrame, crypto, multiplier: float = 1) -> engine.Result:
    return engine.run(market.prices, positions, fees(market, multiplier, crypto), market.rf)


def strategy_runs(market: Market, positions: pd.DataFrame, crypto) -> tuple[engine.Result, engine.Result]:
    once, twice = (engine.run(market.prices, positions, fees(market, m, crypto), market.rf) for m in (1, 2))
    return once, twice


def benchmarks(market: Market, positions: pd.DataFrame, crypto) -> tuple[engine.Result, engine.Result]:
    once, twice = (costs.benchmark(market, positions, m, crypto) for m in (1, 2))
    return once, twice


def first_holding(positions: pd.DataFrame):
    """The session of the strategy's first target to hold an asset: its targets are judged from it."""
    held = positions.fillna(0.0).gt(0).any(axis=1)
    return held.idxmax() if held.any() else None


def first_held(positions: pd.DataFrame):
    """The first session the strategy holds an asset into, the session after its first holding,
    whose orders fill at the close: its returns are judged from it. On the first holding's own
    session it holds nothing, and a benchmark invested before would earn the day against it."""
    start = first_holding(positions)
    later = positions.index[positions.index > start] if start is not None else []
    return later[0] if len(later) else None


def excess(result: engine.Result, rf: pd.Series, period) -> pd.Series:
    """Daily returns above the bill rate over the period."""
    return (result.returns - rf.reindex(result.returns.index).fillna(0.0)).loc[period]


def monthly(x: pd.Series) -> pd.Series:
    return (1 + x).resample("ME").prod() - 1


def edge(leg: Leg, rf, period) -> pd.Series:
    """The strategy's excess returns hedged of the benchmark: its own bets. Long-only strategies on
    the same assets all carry the market, so their raw returns correlate, and earn, whatever their
    bets."""
    return stats.hedged(excess(leg.result, rf, period), excess(leg.bench, rf, period))


def trial(key: str, leg: Leg, rf, period) -> Trial:
    bets = edge(leg, rf, period)
    return Trial(key, monthly(bets), stats.sharpe(bets))


def ratio(value: float, base: float) -> float:
    return value / base if base > 0 else 0.0


def same_rows(a: pd.DataFrame, b: pd.DataFrame, tol: float = 1e-9) -> bool:
    """Equal targets, NaN where the other is NaN."""
    x, y = a.to_numpy(dtype=float), b.to_numpy(dtype=float)
    both_nan = np.isnan(x) & np.isnan(y)
    close = np.isclose(x, y, rtol=0.0, atol=tol)
    return bool(np.all(both_nan | close))


def years_needed(tickers, crypto) -> int:
    """Five years in-sample; four when every asset of the universe is crypto, whose history is
    shorter."""
    return MIN_YEARS_CRYPTO if set(tickers) <= set(crypto) else MIN_YEARS


def data_problems(market: Market, window=slice(None)) -> list[str]:
    """What gates 1 and 7 check in the prices of their window: a price at or below zero, and a
    session without a price within an asset's life, which the engine would hold through. The life
    runs from the asset's first price to its last in the whole series, so that a gap on the first or
    the last session of the window is seen."""
    problems = []
    for ticker in market.prices.columns:
        prices = market.prices[ticker]
        first, last = prices.first_valid_index(), prices.last_valid_index()
        if first is None:
            continue
        life = prices.loc[first:last].loc[window]
        if (life <= 0).any():
            problems.append(f"{ticker} has {int((life <= 0).sum())} prices at or below zero")
        if life.isna().any():
            problems.append(f"{ticker} has no price on {int(life.isna().sum())} sessions of its life")
    return problems


def timing_breaks(strategy, parameters, market: Market, positions, period, rng, dates) -> Timing:
    """Dates where the positions change when the future is cut off (look-ahead), and dates where,
    the future cut off, they change when the bar being traded is scrambled (same-day data): that
    bar, and bitcoin's own close of the day before, which the US close does not know yet. `dates`
    are drawn among the sessions where the strategy sets a target, and as many among those where it
    holds: a rule that reads the future to decide when to hold breaks only there."""
    rows = positions.loc[period]
    setting = rows.notna().any(axis=1).to_numpy()
    chosen = []
    for sessions in (rows.index[setting], rows.index[~setting]):
        if len(sessions):
            chosen += list(rng.choice(sessions, size=min(dates, len(sessions)), replace=False))
    lagged = [t for t in market.prices.columns if not market.prices[t].equals(market.signal_prices[t])]
    look_ahead, same_day = [], []
    for day in sorted(pd.Timestamp(d) for d in chosen):
        seen = market.asof(day)
        cut = targets(strategy, seen, parameters).loc[[day]]
        if not same_rows(cut, positions.loc[[day]]):
            look_ahead.append(day)
        if not same_rows(targets(strategy, scrambled(seen, lagged, rng), parameters).loc[[day]], cut):
            same_day.append(day)
    return Timing(len(chosen), look_ahead, same_day)


def memory_breaks(strategy, parameters, market: Market, positions, period, rng, dates, memory: int) -> tuple[int, list]:
    """Dates where a target changes when the prices older than the signal's memory are scrambled:
    every price before the one `memory` sessions before the session before the target moved at
    random, the dates, the assets that trade and the bill rate kept, the future cut off. `dates` are
    drawn among the sessions where the strategy sets a target with older prices to scramble. Returns
    the number of dates checked and those that broke."""
    index = market.prices.index
    rows = positions.loc[period]
    setting = rows.index[rows.notna().any(axis=1).to_numpy()]
    usable = setting[index.get_indexer(setting) >= memory + 2]
    if not len(usable):
        return 0, []
    chosen = sorted(pd.Timestamp(d) for d in rng.choice(usable, size=min(dates, len(usable)), replace=False))
    breaks = []
    for day in chosen:
        seen = market.asof(day)
        cut = index.get_loc(day) - memory - 1                       # the oldest price the signal may read
        prices, signal = seen.prices.copy(), seen.signal_prices.copy()
        width = prices.shape[1]
        prices.iloc[:cut] = prices.iloc[:cut].to_numpy() * rng.uniform(0.5, 1.5, (cut, width))
        signal.iloc[:cut] = signal.iloc[:cut].to_numpy() * rng.uniform(0.5, 1.5, (cut, width))
        moved = Market(prices, seen.tradable, seen.rf, signal)
        if not same_rows(targets(strategy, moved, parameters).loc[[day]], positions.loc[[day]]):
            breaks.append(day)
    return len(chosen), breaks


def scrambled(market: Market, lagged, rng) -> Market:
    """The market with its last bar moved at random, and the close before it of assets whose signal
    is lagged: what the strategy may not have read. The bill rate of the last session stays: it was
    set the session before."""
    prices, signal = market.prices.copy(), market.signal_prices.copy()
    width = prices.shape[1]
    prices.iloc[-1] = prices.iloc[-1].to_numpy() * rng.uniform(0.5, 1.5, width)
    signal.iloc[-1] = signal.iloc[-1].to_numpy() * rng.uniform(0.5, 1.5, width)
    if len(prices) > 1 and lagged:
        prices.loc[prices.index[-2], lagged] = prices.loc[prices.index[-2], lagged].to_numpy() * rng.uniform(0.5, 1.5, len(lagged))
    return Market(prices, market.tradable, market.rf, signal)


def asset_returns(market: Market) -> pd.DataFrame:
    return market.prices.ffill().pct_change().fillna(0.0)


def late_assets(weights: pd.DataFrame, tradable: pd.DataFrame, period) -> list[str]:
    """The assets the strategy holds that start trading after the evaluation period begins."""
    held = weights.loc[period].gt(1e-9).any()
    first = tradable.loc[period].iloc[0]
    return [t for t in weights.columns if held[t] and not first[t]]


def placebo_weights(W: np.ndarray, T: np.ndarray, shifts: np.ndarray) -> np.ndarray:
    """What each placebo holds into each day of the period but the first (placebos x days x
    assets), from W, the strategy's weights held into each day, and T, whether each asset trades on
    each day. An asset takes its weight from the day `shift` sessions before, circularly, where it
    trades on both days. Where it trades on the day held only, its weight on the other day was no
    choice but a later start, and it keeps its own weight, whole; the shifted weights are scaled down
    to what the day they come from held beyond the weights kept. Where the day they come from held
    assets that do not trade yet on the day held, that share is filled with the strategy's own
    weights of the day held, on the assets shifted, in proportion: neither left in cash nor piled
    onto the assets that remain. Where the strategy holds none of them that day, the shifted weights
    fill it instead, and where nothing is shifted either, the placebo holds what the strategy
    holds."""
    days = np.arange(1, len(W))
    before = (days[None, :] - 1 - shifts[:, None]) % len(W)       # the day the weights come from
    today = T[days - 1][None]
    both = today & T[before]
    shifted = np.where(both, W[before], 0.0)
    kept = np.where(today & ~T[before], W[days - 1][None], 0.0)
    own = np.where(both, W[days - 1][None], 0.0)
    room = np.clip(W[before].sum(axis=2) - kept.sum(axis=2), 0.0, None)
    total, mine = shifted.sum(axis=2), own.sum(axis=2)
    gap = room - total
    filled = (gap > 1e-12) & (mine > 1e-12)                        # a share that cannot be shifted, filled
    scale = np.where(filled, 1.0, np.divide(room, total, out=np.zeros_like(total), where=total > 1e-12))
    fill = np.divide(gap, mine, out=np.zeros_like(mine), where=filled)
    return shifted * scale[..., None] + kept + own * fill[..., None]


def placebo_sharpes(result: engine.Result, market: Market, period, offsets) -> tuple[float, np.ndarray]:
    """The strategy's own weights, held overnight, and its costs, shifted in time by each offset
    over the evaluation period (`placebo_weights`): placebos invested as the strategy was, but timed
    at random. The costs are the strategy's own, each day's shifted whole. Returns the Sharpe ratio
    of the unshifted weights, computed the same way, and one per placebo. A rule without skill
    beats 90% of its placebos not on exactly the 10% a random rank gives: on 0% to 13% of draws, by
    case, for rules that hold few of their assets where assets start late; on up to about 30% for
    rules that hold nearly every asset that trades, close to their benchmark, whose placebos differ
    from them by little, so that details of the path decide the rank, not timing; on some
    universes the equal weight itself beats 90% of its placebos on every offset. Gates 2, 4 and 5
    judge such rules. The equal weight's targets change only when an asset starts to trade, and no
    parameter moves it: gates 1 and 6 stop it. Where assets start late, its alpha is not zero, since
    the benchmark buys a new asset on its first day and the rule at its next reset."""
    W = result.weights.loc[period].to_numpy()
    C = result.costs.loc[period].to_numpy()
    R = asset_returns(market).loc[period].to_numpy()
    f = market.rf.loc[period].fillna(0.0).to_numpy()
    T = market.tradable.loc[period].reindex(columns=result.weights.columns, fill_value=False).to_numpy(dtype=bool)
    days = np.arange(1, len(W))

    def sharpes(shifts: np.ndarray) -> np.ndarray:
        today = (days[None, :] - shifts[:, None]) % len(W)        # the costs paid that day
        held = placebo_weights(W, T, shifts)
        x = (held * R[days][None]).sum(axis=2) - held.sum(axis=2) * f[days][None] - C[today]
        sd = x.std(axis=1, ddof=1)
        return np.where(sd > 0, x.mean(axis=1) / np.where(sd > 0, sd, 1.0) * np.sqrt(PERIODS), 0.0)

    own = float(sharpes(np.array([0]))[0])
    chunks = [sharpes(part) for part in np.array_split(offsets, max(1, len(offsets) // 50))]
    return own, np.concatenate(chunks)


def block_alphas(x: pd.Series, b: pd.Series) -> dict:
    """The alpha of each pre-declared block; None for a block with fewer than 126 sessions of
    returns, which counts as not positive."""
    blocks = {}
    for first, last in BLOCKS:
        xs, bs = x.loc[first:last], b.loc[first:last]
        blocks[f"{first[:4]}-{last[:4]}"] = stats.alpha(xs, bs) if len(xs) >= MIN_BLOCK_SESSIONS else None
    return blocks


def edge_by_year(x: pd.Series, b: pd.Series) -> pd.Series:
    """The edge, the excess returns hedged of the benchmark, summed over each calendar year: what
    each year added to the alpha. The largest is the best year."""
    left = stats.hedged(x, b)
    return left.groupby(left.index.year).sum()


def pnl_shares(result: engine.Result, market: Market, period) -> pd.Series:
    """Each asset's share of the profit over the period: the value held in it overnight times its
    return, summed. Empty when the assets lost money in total."""
    value = engine.INITIAL * (1 + result.returns).cumprod()
    held = result.weights.shift(1).fillna(0.0).mul(value.shift(1).fillna(engine.INITIAL), axis=0)
    pnl = (held * asset_returns(market)).loc[period].sum()
    total = pnl.sum()
    return (pnl / total).sort_values(ascending=False) if total > 0 else pd.Series(dtype=float)


def bootstrap(x: pd.Series, b: pd.Series, rng) -> tuple[np.ndarray, np.ndarray]:
    """The Sharpe ratios and alphas of 1,000 paths of 630 sessions drawn from the in-sample excess
    returns of the strategy and of its benchmark together, in stationary blocks of 21 sessions on
    average."""
    paths = stats.stationary_bootstrap(len(x), WINDOW, MEAN_BLOCK, BOOTSTRAPS, rng)
    return path_statistics(x.to_numpy()[paths], b.to_numpy()[paths])


def path_statistics(x: np.ndarray, b: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Annual Sharpe ratio and alpha of each bootstrap path (one path per row)."""
    sd = x.std(axis=1, ddof=1)
    sharpes = np.where(sd > 0, x.mean(axis=1) / np.where(sd > 0, sd, 1.0) * np.sqrt(PERIODS), 0.0)
    xc, bc = x - x.mean(axis=1, keepdims=True), b - b.mean(axis=1, keepdims=True)
    var = (bc ** 2).sum(axis=1)
    beta = np.where(var > 0, (xc * bc).sum(axis=1) / np.where(var > 0, var, 1.0), 0.0)
    alphas = (x.mean(axis=1) - beta * b.mean(axis=1)) * PERIODS
    return sharpes, alphas


def blended(legs: list[Leg], market: Market, crypto) -> Leg:
    """The variants in equal parts, rebalanced to equal parts every day, each paying its own costs."""
    if len(legs) == 1:
        return legs[0]

    def mean(results: list[engine.Result]) -> engine.Result:
        return engine.Result(sum(r.returns for r in results) / len(results),
                             pd.concat([r.trades for r in results], ignore_index=True),
                             sum(r.costs for r in results) / len(results),
                             sum(r.weights for r in results) / len(results))

    trading = pd.concat([leg.positions.notna().any(axis=1) for leg in legs], axis=1).any(axis=1)
    union = pd.DataFrame(0.0, index=market.prices.index, columns=market.prices.columns).where(trading, axis=0)
    return Leg(union, mean([leg.result for leg in legs]), mean([leg.doubled for leg in legs]),
               *benchmarks(market, union, crypto))


def walk_forward(legs: list[Leg], market: Market, period) -> tuple[pd.DataFrame, float]:
    """Pick, at the start of each year, the variant with the best Sharpe ratio on the years before,
    from the fourth year on; the base variant runs before. Returns the spliced targets and the
    walk-forward efficiency: the Sharpe ratio of the choices out of sample over their average
    Sharpe ratio on the years that chose them."""
    x = pd.concat({k: excess(leg.result, market.rf, period) for k, leg in enumerate(legs)}, axis=1)
    years = sorted(set(x.index.year))
    spliced = legs[0].positions.copy()
    chosen_in_sample, outside = [], []
    for year in years[WALK_FORWARD_START:]:
        past = x[x.index.year < year]
        scores = [stats.sharpe(past[k]) for k in range(len(legs))]
        pick = int(np.argmax(scores))
        chosen_in_sample.append(scores[pick])
        days = spliced.index.year == year
        held = legs[pick].positions.ffill()
        spliced.loc[days] = legs[pick].positions.loc[days]
        first = spliced.index[days][0]
        spliced.loc[first] = held.loc[first]
        outside.append(x.loc[x.index.year == year, pick])
    if not outside:
        return spliced, 0.0
    return spliced, stats.walk_forward_efficiency(stats.sharpe(pd.concat(outside)), float(np.mean(chosen_in_sample)))


def splice_holdout(card, runs, legs, spliced_inside: pd.DataFrame, rf, period) -> tuple[pd.DataFrame, int]:
    """For a card that chooses: the in-sample choices, then for the holdout the variant with the best
    Sharpe ratio over the evaluation period, which is returned with the targets."""
    pick = int(np.argmax([stats.sharpe(excess(leg.result, rf, period)) for leg in legs]))
    positions = runs[pick].copy()
    inside = slice(None, period.stop)
    positions.loc[inside] = spliced_inside.reindex(positions.loc[inside].index)
    first = positions.index[positions.index >= pd.Timestamp(card.holdout[0])][0]
    positions.loc[first] = runs[pick].ffill().loc[first]
    return positions, pick
