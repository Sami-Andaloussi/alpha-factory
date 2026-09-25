"""The battery tested before it judges anything.

Every case runs one rule: hold the assets whose signal is positive, in proportion to the signal
over the asset's volatility, reset every five sessions; or, in its slow form, in equal parts,
from a slower signal, reset every 21 sessions: it costs far less to trade, and favours no asset
on average. Only the signal differs.

- timing, slow timing: the signal is noise, on real prices. The rule earns what being invested
  pays, nothing more: the market-exposure null.
- selection, slow selection: ten such rules; the one with the best in-sample appraisal ratio (the
  Sharpe ratio of its returns hedged of the benchmark, which gates 2, 4, 5 and 7 judge) is judged,
  with the nine others in the registry: the selection null.
- planted 0.5, planted 0.8: real prices, plus a return that the signal predicts, strong enough
  for an expected in-sample appraisal ratio of 0.5 or 0.8. The rule earns what it detects, and
  what being invested pays.
- late slow timing, rotation, binary rotation, top sector: cards whose assets start trading
  inside the in-sample period, from 2012, where gate 3's placebos were weakest before they took
  the strategy's own weights for the share they cannot hold yet. The slow timing null on SPY,
  XLRE, XLC and bitcoin; a rule that is always fully invested, every two spans of sessions a random
  share on SPY and QQQ and the rest on XLRE and XLC once they trade, or, binary, all on one side or
  the other at a coin's toss; and a rule that holds the one sector fund of highest slow noise,
  reset every 21 sessions, among the eleven, two of which start late. Before XLRE starts, the two
  rotations hold SPY and QQQ in equal parts, the benchmark itself: their first block's alpha is
  zero, and gate 5 cannot pass them; their rows measure the gates before it, gate 3 above all.
- near benchmark: every sector fund that trades but the one of lowest fast noise, reset every 21
  sessions, from 2012: a rule close to its benchmark, never the benchmark itself, that costs little
  to trade, whose placebos differ from it by little, so that gate 3's rank judges it little.

The battery must pass at most 5% of each null and at least half of the planted edges at 0.8. The
planted edges are also deflated against registries of 10, 30 and 100 effective trials: the power
the battery keeps as the registry grows.

    python -m lab.calibration --draws 200 --workers 8     # results.csv, then the notebook run again
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd

from lab import battery, data, stats
from lab.data import Market
from lab.notebook import execute

RESULTS = Path(__file__).resolve().parent.parent / "calibration" / "results.csv"
NOTEBOOK = RESULTS.parent / "calibration.ipynb"
RHO, SLOW_RHO = 0.95, 0.995   # day-to-day persistence of the signal: half-lives of about two weeks, and six months
EVERY, SLOW_EVERY = 5, 21     # sessions between two resets
VOL_WINDOW = 60               # sessions of the volatility the rule divides by
VARIANTS = ({"span": 10}, {"span": 20})
NEIGHBOURS = {"span": {25: [8, 12], 50: [5, 15]}}
CHOICES = 10                  # rules the selection null picks from
TARGETS = {"planted 0.5": 0.5, "planted 0.8": 0.8}
LATE = ("late slow timing", "rotation", "binary rotation", "top sector", "near benchmark")
KINDS = ("timing", "slow timing", "selection", "slow selection", *TARGETS, *LATE)
NULLS = ("timing", "slow timing", "selection", "slow selection", *LATE)
LATE_START = "2012-01-01"     # an in-sample start the card accepts, before XLRE, XLC and bitcoin trade
EARLY, LATER = ("SPY", "QQQ"), ("XLRE", "XLC")
SECTORS = ("XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY")
UNIVERSES = {"late slow timing": ("SPY", "XLRE", "XLC", "BTC-USD"), "rotation": EARLY + LATER,
             "binary rotation": EARLY + LATER, "top sector": SECTORS, "near benchmark": SECTORS}
# The twenty assets of the snapshot the calibration ran on: the universe gained assets since, and
# a case run again must see the market its row was computed on.
CALIBRATED = ("XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY", "SPY", "QQQ", "IWM",
              "EFA", "EEM", "GLD", "SLV", "DBC", "BTC-USD")
REGISTRIES = (10, 30, 100)    # effective trials the planted edges are also deflated against
MAX_FALSE_PASS, MIN_POWER = 0.05, 0.5


def latent(index, columns, rng, rho: float = RHO) -> pd.DataFrame:
    """A standardised AR(1) signal per asset."""
    shocks = rng.normal(size=(len(index), len(columns)))
    u = np.empty_like(shocks)
    u[0] = shocks[0]
    scale = np.sqrt(1 - rho ** 2)
    for t in range(1, len(index)):
        u[t] = rho * u[t - 1] + scale * shocks[t]
    return pd.DataFrame(u, index=index, columns=columns)


def rule(signal: pd.DataFrame, every: int = EVERY, flat: bool = False):
    """The rule of every case, driven by `signal`, which it reads up to t-1: the assets whose
    signal is positive, in proportion to the signal over their volatility, or `flat`, in equal
    parts, reset every `every` sessions."""
    def positions(market: Market, span: int = 10) -> pd.DataFrame:
        s = signal.reindex(index=market.prices.index, columns=market.prices.columns)
        score = s.ewm(span=span).mean().shift(1).clip(lower=0)
        if flat:
            raw = score.gt(0).astype(float).where(market.tradable).fillna(0.0)
        else:
            vol = market.signal_prices.pct_change().rolling(VOL_WINDOW, min_periods=20).std().shift(1)
            raw = (score / vol).where(market.tradable).fillna(0.0)
        total = raw.sum(axis=1)
        weights = raw.div(total.where(total > 0), axis=0).fillna(0.0)
        out = weights * np.nan
        out.iloc[::every] = weights.iloc[::every]
        return out
    return positions


def null_rule(kind: str, market: Market, rng):
    slow = "slow" in kind
    signal = latent(market.prices.index, market.prices.columns, rng, SLOW_RHO if slow else RHO)
    return rule(signal, SLOW_EVERY, flat=True) if slow else rule(signal)


def rotation(seed: int, binary: bool = False):
    """A rule without skill that is always fully invested: every 2 x `span` sessions, a random share
    on the early funds, or, `binary`, all or nothing, a coin's toss, and the rest on the later ones,
    in equal parts among those that trade; all on the early funds before any later one trades."""
    def positions(market: Market, span: int = 10) -> pd.DataFrame:
        index = market.prices.index
        draws = np.random.default_rng(seed).random(len(index))
        share = pd.Series((draws < 0.5).astype(float) if binary else draws, index=index)
        early = [t for t in EARLY if t in market.prices.columns]
        later = market.tradable[[t for t in LATER if t in market.prices.columns]].astype(float)
        count = later.sum(axis=1)
        on_early = share.where(count > 0, 1.0) if early else pd.Series(0.0, index=index)
        weights = pd.DataFrame(0.0, index=index, columns=market.prices.columns)
        for ticker in early:
            weights[ticker] = on_early / len(early)
        for ticker in later.columns:
            weights[ticker] = ((1 - on_early) * later[ticker] / count.where(count > 0)).fillna(0.0)
        every = pd.Series(np.arange(len(index)) % (2 * span) == 0, index=index)
        return weights.where(every, axis=0)
    return positions


def top(signal: pd.DataFrame, k: int = 1, every: int = SLOW_EVERY):
    """A rule that holds the `k` assets that trade with the highest signal, read up to t-1, in equal
    parts, reset every `every` sessions, or, for a negative `k`, all those that trade but the `-k`
    of lowest signal: fully invested; concentrated when `k` is small, and close to the benchmark,
    never the benchmark itself, when it leaves one out."""
    def positions(market: Market, span: int = 10) -> pd.DataFrame:
        s = signal.reindex(index=market.prices.index, columns=market.prices.columns)
        score = s.ewm(span=span).mean().shift(1).where(market.tradable)
        count = market.tradable.sum(axis=1) + k if k < 0 else pd.Series(float(k), index=score.index)
        chosen = score.rank(axis=1, ascending=False, method="first").le(count, axis=0).astype(float)
        weights = chosen.div(chosen.sum(axis=1).where(chosen.sum(axis=1) > 0), axis=0).fillna(0.0)
        out = weights * np.nan
        out.iloc[::every] = weights.iloc[::every]
        return out
    return positions


def planted_market(market: Market, strength: float, rng) -> tuple[Market, pd.DataFrame]:
    """Real prices plus `strength` times each asset's volatility times the signal of two sessions
    before: the rule reads that signal at the close of the day before and holds through the day it
    pays. The prices keep their own drift, so the rule also earns what being invested pays."""
    returns = market.prices.pct_change()
    signal = latent(market.prices.index, market.prices.columns, rng)
    moved = returns + strength * returns.std() * signal.shift(2)
    prices = market.prices.copy()
    for ticker in prices.columns:
        first = prices[ticker].first_valid_index()
        path = (1 + moved[ticker].loc[first:].fillna(0.0)).cumprod()
        prices[ticker] = (prices.at[first, ticker] * path).reindex(prices.index)
    lagged = [t for t in prices.columns if not market.prices[t].equals(market.signal_prices[t])]
    signal_prices = prices.copy()
    signal_prices[lagged] = prices[lagged].shift(1)
    return Market(prices, market.tradable, market.rf, signal_prices), signal


def in_sample(market: Market, strategy, parameters) -> tuple[battery.Leg, slice]:
    """The rule's in-sample run, beside its benchmark, over its evaluation period."""
    inside = market.window(*battery.IN_SAMPLE)
    positions = battery.targets(strategy, inside, parameters)
    result = battery.at_cost(inside, positions, battery.costs.CRYPTO)
    leg = battery.Leg(positions, result, result, *battery.benchmarks(inside, positions, battery.costs.CRYPTO))
    return leg, slice(battery.first_held(positions), pd.Timestamp(battery.IN_SAMPLE[1]))


def appraisal(market: Market, strategy, parameters) -> float:
    leg, period = in_sample(market, strategy, parameters)
    return stats.sharpe(battery.edge(leg, market.rf, period))


def strength_for(market: Market, target: float, draws: int = 24) -> float:
    """The planted strength whose average in-sample appraisal ratio, over `draws` markets, is
    `target`. Every strength is tried on the same draws, so that the average moves smoothly with
    the strength, and secant steps find it: the relation is close to linear."""
    def mean_ratio(strength):
        rng = np.random.default_rng(7)
        runs = []
        for _ in range(draws):
            planted, signal = planted_market(market, strength, rng)
            runs.append(appraisal(planted, rule(signal), VARIANTS[0]))
        return float(np.mean(runs))
    low, high = 0.01, 0.02
    r_low, r_high = mean_ratio(low), mean_ratio(high)
    for _ in range(4):
        guess = low + (target - r_low) * (high - low) / (r_high - r_low)
        low, r_low, high, r_high = high, r_high, guess, mean_ratio(guess)
        if abs(r_high - target) < 0.01:
            break
    return float(high)


def against(verdict: battery.Verdict, trials: int) -> float:
    """The deflated Sharpe ratio a verdict's edge, and its blend's, would have against a registry of
    `trials` effective trials whose appraisal ratios vary as luck alone makes them vary: the lower
    of the two, which gates 4 and 5 read. Real registries, whose trials differ more than luck, set a
    higher bar."""
    edges = [verdict.evidence[key] for key in ("edge", "blend edge") if key in verdict.evidence]
    return min(stats.dsr(x, trials, 1.0 / len(x)) for x in edges) if edges else float("nan")


def selected(kind: str, draw: int, market: Market, rng):
    """The selection null: ten rules of `kind`, the one with the best in-sample appraisal ratio,
    which is judged, and the nine others, which the registry holds as earlier trials."""
    rules = [null_rule(kind, market, rng) for _ in range(CHOICES)]
    runs = [in_sample(market, r, VARIANTS[0]) for r in rules]
    best = int(np.argmax([stats.sharpe(battery.edge(leg, market.rf, period)) for leg, period in runs]))
    history = [battery.trial(f"{kind}-{draw}/rule-{k}", leg, market.rf, period)
               for k, (leg, period) in enumerate(runs) if k != best]
    return rules[best], history


def case(kind: str, draw: int, market: Market, strengths: dict) -> dict:
    """One case of `kind`, judged by the battery; one row of results."""
    rng = np.random.default_rng([KINDS.index(kind), draw])
    universe = UNIVERSES.get(kind, tuple(market.prices.columns))
    start = LATE_START if kind in UNIVERSES else battery.IN_SAMPLE[0]
    market = battery.restrict(market, universe)
    card = battery.Card(f"{kind}-{draw}", universe, VARIANTS, NEIGHBOURS, in_sample=(start, battery.IN_SAMPLE[1]))
    history, judged, strength = [], market, strengths.get(kind, 0.0)
    if kind.endswith("rotation"):
        strategy = rotation(int(rng.integers(2 ** 31)), binary=kind == "binary rotation")
    elif kind == "top sector":
        strategy = top(latent(market.prices.index, market.prices.columns, rng, SLOW_RHO))
    elif kind == "near benchmark":
        strategy = top(latent(market.prices.index, market.prices.columns, rng, RHO), -1, SLOW_EVERY)
    elif kind.endswith("timing"):
        strategy = null_rule(kind, market, rng)
    elif kind.endswith("selection"):
        strategy, history = selected(kind, draw, market, rng)
    else:
        judged, signal = planted_market(market, strength, rng)
        strategy = rule(signal)
    seed = int(np.random.SeedSequence([KINDS.index(kind), draw]).generate_state(1)[0])
    verdict = battery.run(card, strategy, judged, history, seed=seed)
    figures = {g.number: g.figures for g in verdict.gates}
    row = {"case": kind, "draw": draw, "strength": strength, "passed": verdict.failed is None,
           "failed": verdict.failed or 0}
    row.update({f"gate {g.number}": bool(g.passed) for g in verdict.gates})
    picks = {"Sharpe": (2, "Sharpe"), "alpha": (2, "alpha"), "costs a year": (2, "costs a year"),
             "appraisal ratio": (4, "appraisal ratio"), "effective trials": (4, "effective trials"), "DSR": (4, "DSR")}
    row.update({name: figures.get(g, {}).get(key) for name, (g, key) in picks.items()})
    row["neighbours holding the base"] = len(figures.get(6, {}).get("neighbours that hold the base") or [])
    planted = kind in TARGETS
    row.update({f"DSR against {n}": against(verdict, n) if planted else None for n in REGISTRIES})
    return row


def save(rows: list[dict], path: Path) -> pd.DataFrame:
    """The results table, its figures to five significant digits and the planted strengths in
    full, so that a planted row can be run again exactly."""
    table = pd.DataFrame(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    table.assign(strength=table["strength"].map(repr)).to_csv(path, index=False, float_format="%.5g")
    return table


_market: Market | None = None


def _start():
    global _market
    _market = battery.restrict(data.load(), CALIBRATED)


def _case(args):
    kind, draw, strengths = args
    return case(kind, draw, _market, strengths)


def main() -> int:
    parser = argparse.ArgumentParser(description="Calibrate the battery against nulls and planted edges.")
    parser.add_argument("--draws", type=int, default=200)
    parser.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2) - 2))
    parser.add_argument("--out", type=Path, default=RESULTS)
    args = parser.parse_args()
    market = battery.restrict(data.load(), CALIBRATED)
    began = time.time()
    strengths = {kind: strength_for(market, target) for kind, target in TARGETS.items()}
    print(f"planted strengths {strengths} ({time.time() - began:.0f}s)", flush=True)
    jobs = [(kind, draw, strengths) for draw in range(args.draws) for kind in KINDS]
    rows = []
    with ProcessPoolExecutor(args.workers, initializer=_start) as pool:
        for k, row in enumerate(pool.map(_case, jobs, chunksize=2), 1):
            rows.append(row)
            if k % 60 == 0:
                print(f"{k}/{len(jobs)} cases, {time.time() - began:.0f}s", flush=True)
    table = save(rows, args.out)
    rates = table.groupby("case")["passed"].mean()
    print(rates.to_string())
    ok = all(rates[k] <= MAX_FALSE_PASS for k in NULLS) and rates["planted 0.8"] >= MIN_POWER
    print("calibration", "passes" if ok else "fails")
    if args.out == RESULTS:
        execute(NOTEBOOK)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
