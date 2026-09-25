"""CA-014-01, sector rotation on the commodity/bond ratio (build-plan.md): while DBC over IEF stands
above its `average`-session mean, the inflation side is held, otherwise the rate-sensitive side,
in equal parts, set on the first session of each week."""
import numpy as np
import pandas as pd

SIDES = {
    "all": (("XLE", "XLB", "GLD", "DBC"), ("XLP", "XLV", "XLF", "XLU", "IEF")),
    "stocks": (("XLE", "XLB"), ("XLP", "XLV", "XLF", "XLU")),
}
COMMODITIES, BONDS = "DBC", "IEF"


def positions(market, average, legs):
    if legs not in SIDES:
        raise ValueError(f"legs '{legs}': 'all' or 'stocks'")
    prices, tradable = market.signal_prices, market.tradable
    # 1. the ratio of the commodity fund to the bond fund on the session before, from prices alone,
    #    and its trend: above its mean over the last `average` sessions up to the session before
    ratio = (prices[COMMODITIES] / prices[BONDS]).shift(1)
    mean = ratio.rolling(average, min_periods=average).mean()
    rising = ratio > mean
    known = mean.notna() & ratio.notna()
    # 2. the side held: the inflation side while the ratio rises, the rate-sensitive side otherwise
    inflation, rate_sensitive = SIDES[legs]
    held = pd.DataFrame(False, index=prices.index, columns=prices.columns)
    for fund in inflation:
        if fund in held:
            held[fund] = rising & known
    for fund in rate_sensitive:
        if fund in held:
            held[fund] = ~rising & known
    held &= tradable
    # 3. the funds of that side that trade share the portfolio equally; none trading, nothing held
    count = held.sum(axis=1)
    weights = held.astype(float).div(count.where(count > 0), axis=0).fillna(0.0)
    # 4. targets on the first session of each week, from the first week whose session before has the
    #    mean, every fund named
    index = prices.index
    week = index.to_period("W")
    first = pd.Series(np.r_[True, week[1:] != week[:-1]], index=index)
    return weights.where(first & known.cummax(), axis=0)
