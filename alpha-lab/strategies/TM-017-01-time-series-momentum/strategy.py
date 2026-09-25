"""TM-017-01, time-series momentum in its plainest form (build-plan.md): each asset held in an equal
share while its past return beats the Treasury bill, set on the first session of each month."""
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
