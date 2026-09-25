"""TM-002-01, nearness to the 52-week high (build-plan.md): each month the three sector funds whose
close is nearest the highest of their past `high_window` closes form a tranche, and the portfolio
holds the tranches of the last `hold` months in equal shares, set on the first session of each
month; TM-003-01's construction, the ranking measure apart."""
import numpy as np
import pandas as pd

LEADERS = 3


def positions(market, high_window, hold):
    funds = list(market.signal_prices.columns)
    prices, tradable = market.signal_prices, market.tradable
    # 1. the nearness: the close of the session before over the highest of the `high_window` closes
    #    up to it
    past = prices.shift(1) / prices.shift(1).rolling(high_window, min_periods=high_window).max()
    # 2. ranked: trading on the session, with `high_window` closes
    ranked = tradable & past.notna()
    index = prices.index
    first = pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)
    months = index[first & ranked.any(axis=1)]
    # 3. each month's tranche: the three nearest their high, with any fund tied with the third, or
    #    all the ranked funds if fewer, in equal parts
    order = past.where(ranked).rank(axis=1, ascending=False, method="min")
    tranches = (order.le(LEADERS) & ranked).loc[months]
    # 4. the portfolio: the tranches of the last `hold` months in equal shares, those formed so far
    #    before `hold` exist; within a tranche, a fund not trading on the session is dropped and the
    #    others share its part
    weights = pd.DataFrame(np.nan, index=index, columns=funds)
    for i, day in enumerate(months):
        live = tranches.iloc[max(0, i - hold + 1): i + 1] & tradable.loc[day]
        count = live.sum(axis=1)
        shares = live.astype(float).div(count.where(count > 0), axis=0).dropna(how="all")
        weights.loc[day] = shares.sum() / len(shares)
    # 5. targets on the first session of each month from the first in which a fund is ranked, every
    #    fund named
    return weights
