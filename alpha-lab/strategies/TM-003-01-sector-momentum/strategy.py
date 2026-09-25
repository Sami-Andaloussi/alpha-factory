"""TM-003-01, sector momentum (build-plan.md): each month the three sector funds with the highest
return over the past `lookback` sessions form a tranche, and the portfolio holds the tranches of the
last `hold` months in equal shares, set on the first session of each month."""
import numpy as np
import pandas as pd

LEADERS = 3


def positions(market, lookback, hold):
    funds = sorted(market.signal_prices.columns)
    prices, tradable = market.signal_prices[funds], market.tradable[funds]
    # 1. the ranking return: from the close `lookback` sessions before the session before to the
    #    close of the session before
    past = prices.shift(1) / prices.shift(1 + lookback) - 1
    # 2. ranked: trading on the session, with both closes
    ranked = tradable & past.notna()
    index = prices.index
    first = pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)
    months = index[first & ranked.any(axis=1)]
    # 3. each month's tranche: the three highest, or all the ranked funds if fewer; ties to the fund
    #    first in alphabetical order
    order = past.where(ranked).rank(axis=1, ascending=False, method="first")
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
    #    fund named, in the market's order
    return weights[list(market.signal_prices.columns)]
