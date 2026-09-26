"""TM-047-02, equities managed by their own volatility (build-plan.md): the five equity index funds
in equal parts, the whole portfolio scaled each month by the inverse of its realized variance, or
volatility, over the window, capped at full investment, the rest in cash."""
import numpy as np
import pandas as pd
from numpy.lib.stride_tricks import sliding_window_view

SCALINGS = ("variance", "volatility")


def trailing_risk(daily: np.ndarray, window: int) -> np.ndarray:
    """Step 2: at row t, the annualized standard deviation of rows t-window to t-1; NaN where the
    window is short or has a gap."""
    out = np.full(len(daily), np.nan)
    if len(daily) <= window:
        return out
    views = sliding_window_view(daily, window)              # row i covers rows i to i+window-1
    risk = views.std(axis=1, ddof=1) * np.sqrt(252)         # NaN if any return in it is NaN
    out[window:] = risk[:len(daily) - window]                # row t reads rows t-window to t-1
    return out


def positions(market, window, target, scaling):
    if scaling not in SCALINGS:
        raise ValueError(f"scaling must be one of {', '.join(SCALINGS)}, not {scaling!r}")
    prices, tradable = market.signal_prices, market.tradable
    # 1. the portfolio's daily return: the average of the funds that traded the session
    returns = prices / prices.shift(1) - 1
    daily = returns.where(tradable).mean(axis=1)
    # 2. its risk over the window to the session before
    risk = pd.Series(trailing_risk(daily.to_numpy(), window), index=prices.index)
    # 3. the scale, capped at full investment, 1 while the risk is not defined
    ratio = target / risk
    k = (ratio ** 2 if scaling == "variance" else ratio).clip(upper=1.0).fillna(1.0)
    # 4. the targets: k/N for each fund trading, the rest in cash, on each month's first session
    trading = tradable.sum(axis=1).astype(float)
    weights = tradable.astype(float).div(trading.where(trading > 0), axis=0).fillna(0.0).mul(k, axis=0)
    index = prices.index
    first = pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)
    return weights.where(first, axis=0)
