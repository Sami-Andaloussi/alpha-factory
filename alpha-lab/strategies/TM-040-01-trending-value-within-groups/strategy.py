"""TM-040-01, value and momentum together within groups (build-plan.md): in each of three groups of
comparable funds, the top third by the average of a value rank and a momentum rank (form composite),
or by momentum among the cheaper half by value (form screen), held in equal places of the group's
share of the portfolio, set on the first session of each month; CA-024-01's construction otherwise."""
import numpy as np
import pandas as pd

GROUPS = {
    "sectors": ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY"],
    "equity markets": ["SPY", "QQQ", "IWM", "EFA", "EEM"],
    "commodities": ["GLD", "SLV", "DBC"],
}
FORMS = ("composite", "screen")


def positions(market, value, momentum, skip, form):
    if form not in FORMS:
        raise ValueError(f"form is one of {', '.join(FORMS)}, not {form!r}")
    prices, tradable = market.signal_prices, market.tradable
    # 1. the two measures, read to the session before the target
    cheapness = prices.shift(1) / prices.shift(1 + value) - 1
    trend = prices.shift(1 + skip) / prices.shift(1 + momentum) - 1
    # 2. ranked: trading today and on the value window's first session, with both returns
    began = tradable.shift(1 + value, fill_value=False).astype(bool)
    ranked = tradable & began & cheapness.notna() & trend.notna()
    members = {name: [t for t in tickers if t in prices.columns] for name, tickers in GROUPS.items()}
    grouped = {t for tickers in members.values() for t in tickers}
    stray = [t for t in prices.columns if t not in grouped]
    if stray:
        raise ValueError(f"assets in no group: {', '.join(stray)}")
    # 6. a fund trading but not yet ranked holds 1/N, its benchmark weight
    trading = tradable.sum(axis=1).astype(float)
    weights = (tradable & ~ranked).astype(float).div(trading.where(trading > 0), axis=0).fillna(0.0)
    for tickers in members.values():
        if not tickers:
            continue
        mine = ranked[tickers]
        # 3. k places, the top third of the n ranked members, rounded, one at least, each (n/N)/k
        n = mine.sum(axis=1)
        k = np.maximum(1, np.rint(n / 3))
        place = (n / trading.where(trading > 0) / k).fillna(0.0)
        value_rank = cheapness[tickers].where(mine).rank(axis=1, ascending=True, method="first")
        trend_rank = trend[tickers].where(mine).rank(axis=1, ascending=False, method="first")
        if form == "composite":
            # 4. the average of the two ranks; members at the k-th lowest share the places left
            score = (value_rank + trend_rank) / 2
            ordered = np.sort(score.to_numpy(), axis=1)                    # NaN last
            rows = np.arange(len(score))
            cut = pd.Series(ordered[rows, np.clip(k.to_numpy().astype(int) - 1, 0, len(tickers) - 1)],
                            index=score.index)
            below = score.lt(cut, axis=0) & mine
            at = score.eq(cut, axis=0) & mine
            left = (k - below.sum(axis=1)) / at.sum(axis=1).where(at.sum(axis=1) > 0)
            held = below.astype(float) + at.astype(float).mul(left.fillna(0.0), axis=0)
        else:
            # 5. the cheaper half, rounded up, then the k of them with the highest momentum
            cheaper = value_rank.le(np.ceil(n / 2), axis=0) & mine
            order = trend[tickers].where(cheaper).rank(axis=1, ascending=False, method="first")
            held = (order.le(k, axis=0) & cheaper).astype(float)
        weights[tickers] = weights[tickers] + held.mul(place, axis=0)
    # 7. targets on the first session of each month in which a fund is ranked, every fund named
    index = weights.index
    first = pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)
    return weights.where(first & ranked.any(axis=1), axis=0)
