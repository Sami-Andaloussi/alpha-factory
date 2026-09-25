"""What a card adds to a rule the lab has run: two rules' alphas over the same sessions.

    python -m lab.compare strategies/<card> strategies/<reference> [--variant N] [--reference-variant M]

A card that refines a rule already run — the same universe, one choice changed — is judged by its
alpha less the reference rule's: both over the card's in-sample sessions from the first holding of
the card's base variant, as the battery counts every variant's sessions, at the lab's stated costs,
each hedged of its own benchmark with its whole-sample beta, as gate 4 hedges it. The difference's
standard error comes from the monthly differences of the two hedged series; it ignores the error in
estimating each beta.

Both cards must have run as they stand: each folder in the lab's own strategies/, its card the one a
registry line of its id recorded, and its strategy unchanged since the commit that line names. A
comparison reads in-sample returns, which no card may see before its run, and the holdout is never
handed to either rule. A reference that first holds later than the card is refused: its days in cash would count
as a hedge. A card that chooses among its variants is refused: the battery judges its walk-forward
composite, which this measure does not rebuild.

A measure that lets the beta follow a state of the rule is not computed here: a card that needs it
states it, with its states read from the signal, before its run.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from lab import battery, costs, data, registry, stats
from lab.data import Market

PERIODS = stats.PERIODS
STRATEGIES = Path(__file__).resolve().parent.parent / "strategies"


def legs(market: Market, positions: pd.DataFrame, period, crypto=costs.CRYPTO):
    """The rule's excess returns and its benchmark's over `period`, at the stated costs."""
    result = battery.at_cost(market, positions, crypto)
    bench = costs.benchmark(market, positions, 1, crypto)
    return battery.excess(result, market.rf, period), battery.excess(bench, market.rf, period)


def beta(excess: pd.Series, benchmark_excess: pd.Series) -> float:
    """The regression slope of the rule's excess returns on its benchmark's, NaN without spread."""
    both = pd.concat([excess, benchmark_excess], axis=1).dropna()
    spread = both.iloc[:, 1].var(ddof=1)
    return float(both.cov(ddof=1).iloc[0, 1] / spread) if spread > 0 else float("nan")


def difference(market: Market, strategy, parameters: dict, reference, reference_parameters: dict,
               end, start=None, crypto=costs.CRYPTO) -> dict:
    """The rule's alpha less the reference's, on `market`, already restricted to the universe and
    window both rules share, over the sessions from `start` — the rule's own first holding when it
    is not given — to `end`. Refused when the reference first holds after `start`."""
    positions = battery.targets(strategy, market, parameters)
    reference_positions = battery.targets(reference, market, reference_parameters)
    start = battery.first_holding(positions) if start is None else pd.Timestamp(start)
    if start is None:
        raise ValueError("the rule never holds an asset")
    reference_start = battery.first_holding(reference_positions)
    if reference_start is None or reference_start > start:
        raise ValueError(f"the reference first holds on {reference_start:%Y-%m-%d}, after the rule's "
                         f"{start:%Y-%m-%d}: its days in cash would count as a hedge"
                         if reference_start is not None else "the reference never holds an asset")
    period = slice(start, pd.Timestamp(end))
    x, b = legs(market, positions, period, crypto)
    rx, rb = legs(market, reference_positions, period, crypto)
    h, rh = stats.hedged(x, b), stats.hedged(rx, rb)
    both = pd.concat([h, rh], axis=1).dropna()
    gap = both.iloc[:, 0] - both.iloc[:, 1]
    monthly = battery.monthly(gap)
    years = len(gap) / PERIODS
    spread = float(monthly.std(ddof=1) * np.sqrt(12)) if len(monthly) > 1 else float("nan")
    error = spread / np.sqrt(years) if years > 0 else float("nan")
    estimate = float(gap.mean() * PERIODS)
    return {"from": start, "reference from": reference_start, "to": pd.Timestamp(end), "years": years,
            "alpha": stats.alpha(x, b), "reference alpha": stats.alpha(rx, rb),
            "appraisal ratio": stats.sharpe(h), "reference appraisal ratio": stats.sharpe(rh),
            "beta": beta(x, b), "reference beta": beta(rx, rb),
            "excess return": float(x.mean() * PERIODS), "reference excess return": float(rx.mean() * PERIODS),
            "difference": estimate, "standard error": error,
            "t": estimate / error if np.isfinite(error) and error > 0 else float("nan"),
            "difference's volatility": spread,
            "correlation of the bets": float(both.corr().iloc[0, 1]) if len(both) > 2 else float("nan")}


def ran(folder: Path, lines: list[dict]) -> str | None:
    """Why the card of `folder` cannot be read as run, or None when it ran as it stands: its folder
    in the lab's own strategies/, its card the one a registry line of its id recorded, and its
    strategy unchanged since the commit that line names."""
    from lab import report   # imported where it is used, as in main: report imports the whole run's chain
    folder = Path(folder).resolve()
    if folder.parent != STRATEGIES:
        return f"{folder.name}: a card compared lies in the lab's own strategies/"
    card_hash = report.card_hash_of(folder / "card.yaml")
    runs = [line for line in lines if line.get("card") == folder.name and line.get("card_hash") == card_hash]
    if not runs:
        ran_before = any(line.get("card") == folder.name for line in lines)
        return (f"{folder.name}: its card differs from the one that ran" if ran_before
                else f"{folder.name}: not in the registry; no comparison before a run")
    commit = runs[0].get("commit")
    if not commit:
        return f"{folder.name}: the commit of its run is not recorded"
    try:
        changed = report.git("diff", "--name-only", commit, "--", "strategy.py", cwd=folder)
    except RuntimeError as error:
        return f"{folder.name}: the commit of its run cannot be read ({error})"
    if changed:
        return f"{folder.name}: its strategy changed after the commit of its run, {commit[:12]}"
    return None


def main(argv: list[str] | None = None) -> int:
    from lab import report   # the card and strategy readers of a run
    parser = argparse.ArgumentParser(prog="python -m lab.compare", description=__doc__.split("\n\n")[0])
    parser.add_argument("card")
    parser.add_argument("reference")
    parser.add_argument("--variant", type=int, default=0)
    parser.add_argument("--reference-variant", type=int, default=0)
    args = parser.parse_args(argv)
    folders = [Path(args.card).resolve(), Path(args.reference).resolve()]
    try:
        card, reference = (report.read_card(folder)[1] for folder in folders)
    except RuntimeError as error:
        print(f"refused: {error}", file=sys.stderr)
        return 1
    lines = registry.lines()
    refusals = [why for why in (ran(folder, lines) for folder in folders) if why]
    for chosen, spec, name in ((args.variant, card, "--variant"), (args.reference_variant, reference, "--reference-variant")):
        if not 0 <= chosen < len(spec.variants):
            refusals.append(f"{name} {chosen}: {spec.id} has variants 0 to {len(spec.variants) - 1}")
    if card.choose or reference.choose:
        refusals.append("a card that chooses among its variants is judged on its walk-forward composite, not rebuilt here")
    if tuple(card.universe) != tuple(reference.universe):
        refusals.append("the two cards do not hold the same universe in the same order: their benchmarks differ")
    if refusals:
        for why in refusals:
            print(f"refused: {why}", file=sys.stderr)
        return 1
    market = battery.restrict(data.load(end=battery.IN_SAMPLE[1]), card.universe).window(*card.in_sample)
    strategy, reference_strategy = (report.strategy_of(folder / "strategy.py") for folder in folders)
    start = battery.first_holding(battery.targets(strategy, market, dict(card.variants[0])))
    try:
        result = difference(market, strategy, dict(card.variants[args.variant]), reference_strategy,
                            dict(reference.variants[args.reference_variant]), card.in_sample[1], start)
    except ValueError as error:
        print(f"refused: {error}", file=sys.stderr)
        return 1
    print(f"{card.id} (variant {args.variant}) against {reference.id} (variant {args.reference_variant}), "
          f"{result['from']:%Y-%m-%d} to {result['to']:%Y-%m-%d}, {result['years']:.1f} years; "
          f"the reference first holds on {result['reference from']:%Y-%m-%d}")
    for name in ("alpha", "appraisal ratio", "beta", "excess return"):
        mine, theirs = result[name], result[f"reference {name}"]
        form = ".3%" if name in ("alpha", "excess return") else ".3f"
        print(f"  {name:16s} {mine:{form}}  against  {theirs:{form}}")
    print(f"  difference       {result['difference']:.3%} a year, standard error {result['standard error']:.3%}, "
          f"t {result['t']:.2f}")
    spread = result["difference's volatility"]
    print(f"  the difference moves by {spread:.2%} a year; the bets correlate at {result['correlation of the bets']:.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
