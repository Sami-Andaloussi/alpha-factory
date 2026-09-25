"""CA-001-01, momentum within groups (build-plan.md): in each of three groups of comparable funds,
the top third by the past year's return, the last `skip` sessions left out, held in equal shares
of the group's share of the portfolio, set on the first session of each month."""
import numpy as np
import pandas as pd

GROUPS = {
    "sectors": ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY"],
    "equity markets": ["SPY", "QQQ", "IWM", "EFA", "EEM"],
    "commodities": ["GLD", "SLV", "DBC"],
}


def positions(market, lookback, skip):
    prices, tradable = market.signal_prices, market.tradable
    # 1. the ranking return: from `lookback` to `skip` sessions before the session before
    past = prices.shift(1 + skip) / prices.shift(1 + lookback) - 1
    # 2. ranked: trading today and on the window's first session, with a return over the window
    began = tradable.shift(1 + lookback, fill_value=False).astype(bool)
    ranked = tradable & began & past.notna()
    # 3. the leaders of each group: its top third of ranked members, rounded, one at least
    members = {name: [t for t in tickers if t in prices.columns] for name, tickers in GROUPS.items()}
    grouped = {t for tickers in members.values() for t in tickers}
    stray = [t for t in prices.columns if t not in grouped]
    if stray:
        raise ValueError(f"assets in no group: {', '.join(stray)}")
    # 4. the weights: a group of n ranked members of N trading holds n/N among its leaders;
    #    an asset trading but not yet ranked holds 1/N, its benchmark weight
    trading = tradable.sum(axis=1).astype(float)
    weights = (tradable & ~ranked).astype(float).div(trading.where(trading > 0), axis=0).fillna(0.0)
    for tickers in members.values():
        if not tickers:
            continue
        n = ranked[tickers].sum(axis=1)
        leaders = np.maximum(1, np.rint(n / 3))
        order = past[tickers].where(ranked[tickers]).rank(axis=1, ascending=False, method="first")
        chosen = order.le(leaders, axis=0) & ranked[tickers]
        share = (n / trading.where(trading > 0) / leaders).fillna(0.0)
        weights[tickers] = weights[tickers] + chosen.astype(float).mul(share, axis=0)
    # 5. targets on the first session of each month in which an asset is ranked, every asset named
    index = weights.index
    first = pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)
    return weights.where(first & ranked.any(axis=1), axis=0)
