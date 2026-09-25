"""TM-047-01, trend with positions scaled by volatility (build-plan.md): TM-017-01's rule, each
asset held while its past year beats the Treasury bill, each position sized to the same daily move,
never levered, set on the first session of each month."""
import numpy as np
import pandas as pd

LOOKBACK = 252   # TM-017-01's lookback, unchanged


def positions(market, risk, vol_window):
    prices = market.signal_prices
    # 1. the asset's return over the past year, up to the session before
    past = prices.shift(1) / prices.shift(1 + LOOKBACK) - 1
    # 2. the Treasury bill's return over the same sessions
    bill = (1 + market.rf.fillna(0.0)).cumprod()
    cash = bill.shift(1) / bill.shift(1 + LOOKBACK) - 1
    # 3. in trend: beats the bill and trades today
    trend = past.gt(cash, axis=0) & market.tradable
    # 4. the size: `risk` over the daily volatility of the past `vol_window` sessions, up to the
    #    session before; the weights cut in proportion when they add up to more than one
    volatility = (prices / prices.shift(1) - 1).shift(1).rolling(vol_window).std()
    weights = (risk / volatility).where(trend & volatility.gt(0)).fillna(0.0)
    total = weights.sum(axis=1)
    weights = weights.div(np.maximum(total, 1.0), axis=0)
    # 5. targets on the first session of each month, every asset named
    index = weights.index
    first = pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)
    return weights.where(first, axis=0)
