"""What trading costs, and the benchmark that pays the same.

Costs are a fraction of the value traded, per side: 5 bps on ETFs, 20 bps on bitcoin. Gate 2 runs
every strategy again at twice these costs (`multiplier=2`).

The benchmark is the equal weight of the assets tradable at each date, set back to equal weights on
each session where the strategy sets a target and on each change of the tradable set, and charged
the same costs.
"""
from __future__ import annotations

import pandas as pd

from lab import engine
from lab.data import Market, benchmark_weights
from lab.universe import UNIVERSE

PER_SIDE = {"etf": 0.0005, "crypto": 0.0020}
CRYPTO = frozenset(asset.ticker for asset in UNIVERSE if asset.cluster == "crypto")


def per_side(tickers, multiplier: float = 1.0, crypto=CRYPTO) -> pd.Series:
    return pd.Series({t: PER_SIDE["crypto" if t in crypto else "etf"] * multiplier for t in tickers})


def benchmark(market: Market, strategy_positions: pd.DataFrame, multiplier: float = 1.0,
              crypto=CRYPTO) -> engine.Result:
    """The equal-weight benchmark, set back to equal weights on each session where the strategy sets
    a target and on each change of the tradable set."""
    weights = benchmark_weights(market.tradable)
    trades = strategy_positions.reindex(market.prices.index).notna().any(axis=1)
    entries = market.tradable.ne(market.tradable.shift()).any(axis=1)
    targets = weights.where(trades | entries)
    return engine.run(market.prices, targets, per_side(market.prices.columns, multiplier, crypto), market.rf)
