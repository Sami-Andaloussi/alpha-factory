"""LL-023-01, continuous momentum within groups (build-plan.md): CA-001-01's rule, each group's k
funds drawn from its 2k highest-ranked by the path score, the share of the window's positive daily
returns less the share of its negative ones: the k highest under half "continuous", the k lowest
under half "discrete", set on the first session of each month."""
import numpy as np
import pandas as pd

GROUPS = {
    "sectors": ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY"],
    "equity markets": ["SPY", "QQQ", "IWM", "EFA", "EEM"],
    "commodities": ["GLD", "SLV", "DBC"],
}
POOL = 2   # the pool is twice the k funds held: Gray and Vogel's halves of their leaders
HALVES = ("continuous", "discrete")


def positions(market, lookback, skip, half):
    return choose(market, lookback, skip, half, POOL)


def choose(market, lookback, skip, half, pool):
    if half not in HALVES:
        raise ValueError(f"half is one of {', '.join(HALVES)}, not {half!r}")
    prices, tradable = market.signal_prices, market.tradable
    # 1. the ranking return: from `lookback` to `skip` sessions before the session before
    past = prices.shift(1 + skip) / prices.shift(1 + lookback) - 1
    # 2. ranked: trading today and on the window's first session, with a return over the window
    began = tradable.shift(1 + lookback, fill_value=False).astype(bool)
    ranked = tradable & began & past.notna()
    # 3. the path score: over the window's lookback - skip daily returns, the count positive less
    #    the count negative, divided by their number; a return of zero counts in neither
    daily = prices / prices.shift(1) - 1
    days = lookback - skip
    ups = daily.gt(0).astype(float).rolling(days).sum().shift(1 + skip)
    downs = daily.lt(0).astype(float).rolling(days).sum().shift(1 + skip)
    score = (ups - downs) / days
    members = {name: [t for t in tickers if t in prices.columns] for name, tickers in GROUPS.items()}
    grouped = {t for tickers in members.values() for t in tickers}
    stray = [t for t in prices.columns if t not in grouped]
    if stray:
        raise ValueError(f"assets in no group: {', '.join(stray)}")
    # 4. the weights: a fund trading but not ranked holds 1/N; on each target, a group of n ranked
    #    funds of N trading holds n/N among k funds of its pool, the min(pool * k, n) highest
    #    window returns, chosen by their score
    trading = tradable.sum(axis=1).astype(float)
    weights = (tradable & ~ranked).astype(float).div(trading.where(trading > 0), axis=0).fillna(0.0)
    index = weights.index
    first = pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)
    targets = index[first & ranked.any(axis=1)]
    for tickers in members.values():
        for day in targets:
            funds = [t for t in tickers if ranked.at[day, t]]
            n = len(funds)
            if not n:
                continue
            k = max(1, int(np.rint(n / 3)))
            by_return = sorted(funds, key=lambda t: (-past.at[day, t], tickers.index(t)))
            candidates = by_return[:min(pool * k, n)]
            if any(np.isnan(score.at[day, t]) for t in candidates):
                raise ValueError(f"{day:%Y-%m-%d}: a ranked fund without a path score")
            # the continuous half: the k highest scores, ties to the higher window return, then to
            # the universe's order; the discrete half: the rest of the pool when it holds 2k, else
            # the k lowest scores, with the same ties
            continuous = sorted(candidates, key=lambda t: (-score.at[day, t], -past.at[day, t],
                                                           tickers.index(t)))[:k]
            if half == "continuous":
                chosen = continuous
            elif len(candidates) >= 2 * k:
                chosen = [t for t in candidates if t not in continuous]
            else:
                chosen = sorted(candidates, key=lambda t: (score.at[day, t], -past.at[day, t],
                                                           tickers.index(t)))[:k]
            weights.loc[day, chosen] += n / trading[day] / k
    # 5. targets on the first session of each month in which a fund is ranked, every fund named
    return weights.where(first & ranked.any(axis=1), axis=0)
