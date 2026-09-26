"""TM-028-01, the trend of the quiet sessions (build-plan.md): each US equity fund held in an equal
share while its negative volume index, the compounded returns of the sessions whose volume fell,
stands above its average over the window, its share in cash otherwise; set on the first session of
each month."""
import numpy as np
import pandas as pd
from numpy.lib.stride_tricks import sliding_window_view

VOLUMES = ("own", "market")


def quiet(market, volume):
    """Step 1: the sessions whose deciding volume is below the session before's."""
    volumes = market.signal_volumes
    if volume == "market":
        volumes = pd.DataFrame({t: volumes["SPY"] for t in volumes.columns}, index=volumes.index)
    return volumes < volumes.shift(1)                       # a missing or equal volume: not quiet


def above_average(logs: np.ndarray, window: int) -> np.ndarray:
    """Step 2: row t, from the log returns counted on rows t-window+1 to t-1 (the window to the
    session before, less its first session, whose return does not move the ratio): whether the
    index stands above its average over the window; NaN where a return is missing."""
    rows, funds = logs.shape
    out = np.full((rows, funds), np.nan)
    if rows <= window:
        return out
    views = sliding_window_view(logs, window - 1, axis=0)   # (rows - window + 2, funds, window - 1)
    back = np.cumsum(views[..., ::-1], axis=2)              # D_k: the last k sessions' summed logs
    mean = (1 + np.exp(-back).sum(axis=2)) / window          # the average over the index, at 1
    up = np.where(np.isnan(mean), np.nan, (mean < 1).astype(float))
    out[window:] = up[1:rows - window + 1]                  # row t reads rows t-window+1 to t-1
    return out


def positions(market, window, volume):
    if volume not in VOLUMES:
        raise ValueError(f"volume must be one of {', '.join(VOLUMES)}, not {volume!r}")
    prices, tradable = market.signal_prices, market.tradable
    # 1. the quiet sessions, and each session's log return counted when quiet, zero otherwise
    returns = prices / prices.shift(1) - 1
    counted = np.log1p(returns.where(quiet(market, volume), 0.0).where(returns.notna()))
    # 2. the index above its average over the window to the session before
    up = pd.DataFrame(above_average(counted.to_numpy(), window), index=prices.index, columns=prices.columns)
    # 3. defined: a price `window` sessions before the session before, and no gap inside the window
    defined = prices.shift(1 + window).notna() & up.notna()
    # 4. the targets: 1/N while the index is up or not defined, cash otherwise, every month's first session
    held = tradable & (up.eq(1.0) | ~defined)
    trading = tradable.sum(axis=1).astype(float)
    weights = held.astype(float).div(trading.where(trading > 0), axis=0).fillna(0.0)
    index = prices.index
    first = pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)
    return weights.where(first, axis=0)
