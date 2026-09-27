"""CA-014-02, rotation on the dollar's trend (build-plan.md): while the dollar in euros stands below
its `average`-reading mean, the inflation side is held, otherwise the rate-sensitive side, in equal
parts, set on the first session of each week."""
import numpy as np
import pandas as pd

SIDES = {
    "all": (("XLE", "XLB", "GLD", "DBC"), ("XLP", "XLV", "XLF", "XLU", "IEF")),
    "classes": (("GLD", "DBC"), ("IEF",)),
}
PRESENT = 0.9       # the share of the last `average` sessions that must have a reading


def positions(market, average, legs):
    if legs not in SIDES:
        raise ValueError(f"legs '{legs}': 'all' or 'classes'")
    prices, tradable, rates = market.signal_prices, market.tradable, market.signal_rates
    if rates is None:
        raise ValueError("the dollar is read from the market's exchange rates, which it does not carry")
    # 1. the dollar's price in euros, each rate the close of the last day before the session, so read
    #    on the session itself; its mean over the readings that exist among the last `average`
    #    sessions, when nine tenths of them exist
    dollar = (rates["USDCHF"] / rates["EURCHF"]).reindex(prices.index)
    mean = dollar.rolling(average, min_periods=int(np.ceil(PRESENT * average))).mean()
    known = mean.notna() & dollar.notna()
    falling = dollar < mean
    # 2. the side held: the inflation side while the dollar falls, the rate-sensitive side otherwise
    inflation, rate_sensitive = SIDES[legs]
    held = pd.DataFrame(False, index=prices.index, columns=prices.columns)
    for fund in inflation:
        if fund in held:
            held[fund] = falling & known
    for fund in rate_sensitive:
        if fund in held:
            held[fund] = ~falling & known
    held &= tradable
    # 3. the funds of that side that trade share the portfolio equally; none trading, nothing held
    count = held.sum(axis=1)
    weights = held.astype(float).div(count.where(count > 0), axis=0).fillna(0.0)
    # 4. targets on the first session of each week that has a reading and its mean; a week whose
    #    first session has none sets no target and holds
    index = prices.index
    week = index.to_period("W")
    first = pd.Series(np.r_[True, week[1:] != week[:-1]], index=index)
    return weights.where(first & known, axis=0)
