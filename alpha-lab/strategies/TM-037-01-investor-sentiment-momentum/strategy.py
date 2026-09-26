"""TM-037-01, market turnover as a contrarian sign of sentiment (build-plan.md): the fourteen US
equity funds in equal parts, the whole portfolio in cash in the months after SPY's log volume over
the window stood above its five-year average; set on the first session of each month."""
import numpy as np
import pandas as pd
from numpy.lib.stride_tricks import sliding_window_view

DETREND = 1260   # sessions of the five-year average, fixed by the card


def trailing_mean(values: np.ndarray, window: int) -> np.ndarray:
    """Row t: the mean of rows t-window to t-1, NaN-skipping; NaN where fewer than window rows
    precede t or all of them are NaN."""
    out = np.full(len(values), np.nan)
    if len(values) <= window:
        return out
    views = sliding_window_view(values, window)              # row i covers rows i to i+window-1
    known = (~np.isnan(views)).sum(axis=1)
    sums = np.where(np.isnan(views), 0.0, views).sum(axis=1)
    means = np.where(known > 0, sums / np.maximum(known, 1), np.nan)
    out[window:] = means[:len(values) - window]              # row t reads rows t-window to t-1
    return out


def positions(market, window):
    prices, tradable = market.signal_prices, market.tradable
    # 1. SPY's log volume, a missing or zero volume NaN
    volume = market.signal_volumes["SPY"].to_numpy(dtype=float)
    logs = np.log(np.where(volume > 0, volume, np.nan))
    # 2. the measure: the window's mean less the five years' mean, both to the session before
    measure = trailing_mean(logs, window) - trailing_mean(logs, DETREND)
    # 3. the state: high when the measure is above zero; not defined before 1,260 sessions
    high = pd.Series(np.where(np.isnan(measure), False, measure > 0), index=prices.index)
    # 4. the targets: 1/N for each fund trading unless turnover is high, on each month's first session
    trading = tradable.sum(axis=1).astype(float)
    weights = tradable.astype(float).div(trading.where(trading > 0), axis=0).fillna(0.0)
    weights = weights.mul((~high).astype(float), axis=0)
    index = prices.index
    first = pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)
    return weights.where(first, axis=0)
