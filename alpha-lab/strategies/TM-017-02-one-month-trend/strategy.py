"""TM-017-02, time-series momentum at one month (build-plan.md): TM-017-01's rule with its lookback at
a month: each fund held in a seventh while its return over the last month beats the Treasury bill's,
set on the first session of each month."""
import numpy as np
import pandas as pd


def positions(market, lookback):
    prices = market.signal_prices
    # 1. the asset's return over the past `lookback` sessions, up to the session before
    past = prices.shift(1) / prices.shift(1 + lookback) - 1
    # 2. the Treasury bill's return over the same sessions
    bill = (1 + market.rf.fillna(0.0)).cumprod()
    cash = bill.shift(1) / bill.shift(1 + lookback) - 1
    # 3. in trend: beats the bill and trades today; one equal share of the portfolio each
    trend = past.gt(cash, axis=0) & market.tradable
    weights = trend.astype(float) / prices.shape[1]
    # 4. targets on the first session of each month, every asset named
    index = weights.index
    first = pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)
    return weights.where(first, axis=0)
