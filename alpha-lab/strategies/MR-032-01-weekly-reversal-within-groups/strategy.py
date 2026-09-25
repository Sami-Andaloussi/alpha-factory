"""MR-032-01, last week's laggards within groups (build-plan.md): in each basket of comparable funds,
the bottom third by the return over the last `lookback` sessions, held in equal shares of the
basket's share of the portfolio, set on the first session of each week or month; CA-001-01's
construction, the ranking reversed and the window shortened."""
import numpy as np
import pandas as pd

GROUPS = {
    "sectors": ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY"],
    "equity markets": ["SPY", "QQQ", "IWM", "EFA", "EEM"],
    "commodities": ["GLD", "SLV", "DBC"],
}
PACES, BASKETS = ("week", "month"), ("groups", "universe")


def positions(market, lookback, pace, basket):
    if pace not in PACES or basket not in BASKETS:
        raise ValueError(f"pace is one of {PACES} and basket one of {BASKETS}, not {pace!r}, {basket!r}")
    prices, tradable = market.signal_prices, market.tradable
    # 1. the return that ranks: from `lookback` sessions before the session before to that session
    past = prices.shift(1) / prices.shift(1 + lookback) - 1
    # 2. ranked: trading today and on the window's first session, with a return over the window
    began = tradable.shift(1 + lookback, fill_value=False).astype(bool)
    ranked = tradable & began & past.notna()
    # 3. the baskets, each in the card's order
    members = {name: [t for t in tickers if t in prices.columns] for name, tickers in GROUPS.items()}
    grouped = [t for tickers in members.values() for t in tickers]
    stray = [t for t in prices.columns if t not in grouped]
    if stray:
        raise ValueError(f"assets in no group: {', '.join(stray)}")
    baskets = list(members.values()) if basket == "groups" else [grouped]
    # 5. a fund trading but not yet ranked holds 1/N, its benchmark weight
    trading = tradable.sum(axis=1).astype(float)
    weights = (tradable & ~ranked).astype(float).div(trading.where(trading > 0), axis=0).fillna(0.0)
    for tickers in baskets:
        if not tickers:
            continue
        # 4. the laggards: the bottom third of the n ranked members, rounded, one at least
        n = ranked[tickers].sum(axis=1)
        laggards = np.maximum(1, np.rint(n / 3))
        order = past[tickers].where(ranked[tickers]).rank(axis=1, ascending=True, method="first")
        chosen = order.le(laggards, axis=0) & ranked[tickers]
        share = (n / trading.where(trading > 0) / laggards).fillna(0.0)
        weights[tickers] = weights[tickers] + chosen.astype(float).mul(share, axis=0)
    # 6. targets on the first session of each calendar week or month in which a fund is ranked
    index = weights.index
    if pace == "week":
        calendar = index.isocalendar()
        key = calendar["year"].to_numpy() * 100 + calendar["week"].to_numpy()
    else:
        key = index.year * 100 + index.month
    first = pd.Series(np.r_[True, key[1:] != key[:-1]], index=index)
    return weights.where(first & ranked.any(axis=1), axis=0)
