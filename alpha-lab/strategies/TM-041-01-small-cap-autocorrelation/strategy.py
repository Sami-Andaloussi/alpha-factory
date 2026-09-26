"""TM-041-01, small capitalisations' weekly continuation (build-plan.md): each US equity fund held in
an equal share for a block of `period` sessions after its own return over the last `period` sessions
beat the bill's, its share in cash otherwise; the blocks counted from the session of 2005-01-03."""
import numpy as np
import pandas as pd

ANCHOR = pd.Timestamp("2005-01-03")   # the snapshot's first session, where the blocks are counted from


def positions(market, period):
    prices = market.signal_prices
    # 1. the fund's return over the last `period` sessions, up to the session before
    past = prices.shift(1) / prices.shift(1 + period) - 1
    # 2. the Treasury bill's return over the same sessions
    bill = (1 + market.rf.fillna(0.0)).cumprod()
    cash = bill.shift(1) / bill.shift(1 + period) - 1
    # 3. each fund trading holds 1/N, N the funds trading, when it beats the bill; cash otherwise,
    #    and while it has fewer than `period` + 1 closes
    up = past.gt(cash, axis=0) & market.tradable
    trading = market.tradable.sum(axis=1).astype(float)
    weights = up.astype(float).div(trading.where(trading > 0), axis=0).fillna(0.0)
    # 4. targets on the first session of each block of `period` sessions counted from the anchor
    index = prices.index
    anchor = index.get_loc(ANCHOR)
    starts = pd.Series((np.arange(len(index)) - anchor) % period == 0, index=index) & (index >= ANCHOR)
    return weights.where(starts, axis=0)
