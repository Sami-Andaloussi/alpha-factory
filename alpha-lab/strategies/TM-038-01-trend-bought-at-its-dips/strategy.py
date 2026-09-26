"""TM-038-01, trend following bought at its own dips (build-plan.md): TM-017-01's rule, the book, held
in full in the months after the sum of its own daily returns over the bill across the last `dip`
sessions fell below zero, and at half otherwise, the rest in cash; set on the first session of each
month."""
import numpy as np
import pandas as pd
from numpy.lib.stride_tricks import sliding_window_view

LOOKBACK, HALF = 252, 0.5   # TM-017-01's lookback and the share held always, fixed by the card


def book(market):
    """Step 1: TM-017-01's weights, a seventh for each fund in trend that trades, and the months'
    first sessions."""
    prices = market.signal_prices
    past = prices.shift(1) / prices.shift(1 + LOOKBACK) - 1
    bill = (1 + market.rf.fillna(0.0)).cumprod()
    cash = bill.shift(1) / bill.shift(1 + LOOKBACK) - 1
    trend = past.gt(cash, axis=0) & market.tradable
    index = prices.index
    first = np.r_[True, index.month[1:] != index.month[:-1]]
    return trend.astype(float) / prices.shape[1], first


def excess(prices: np.ndarray, rf: np.ndarray, weights: np.ndarray, first: np.ndarray) -> np.ndarray:
    """Step 2: each session's return of the book less the bill's: the holdings set at the close of a
    month's first session drift with the funds' closes, the cash with the bill, until the next; zero
    while the book holds nothing."""
    rows, funds = prices.shape
    out = np.zeros(rows)
    held, cash = np.zeros(funds), 1.0
    for t in range(rows):
        if t > 0:
            r = np.where(held > 0, np.nan_to_num(prices[t] / prices[t - 1] - 1), 0.0)
            value = held.sum() + cash
            out[t] = (held * (r - rf[t])).sum() / value
            held, cash = held * (1 + r), cash * (1 + rf[t])
        if first[t]:
            value = held.sum() + cash
            held = weights[t] * value
            cash = value - held.sum()
    return out


def in_dip(daily: np.ndarray, dip: int) -> np.ndarray:
    """Step 3: row t, whether the sum of rows t-dip to t-1 is below zero, summed on each window's own
    values; False while fewer than dip rows precede t."""
    out = np.zeros(len(daily), dtype=bool)
    if len(daily) <= dip:
        return out
    sums = sliding_window_view(daily, dip).sum(axis=1)       # row i covers rows i to i+dip-1
    out[dip:] = sums[:len(daily) - dip] < 0                   # row t reads rows t-dip to t-1
    return out


def positions(market, dip):
    # 1. the book: TM-017-01's weights on each month's first session
    weights, first = book(market)
    # 2. its daily return over the bill, from its drifting holdings
    daily = excess(market.signal_prices.to_numpy(dtype=float), market.rf.fillna(0.0).to_numpy(dtype=float),
                   weights.to_numpy(dtype=float), first)
    # 3. the dip: the last `dip` sessions' sum below zero, to the session before
    k = np.where(in_dip(daily, dip), 1.0, HALF)
    # 4. the targets: the book at scale k, the rest in cash, on each month's first session
    return weights.mul(k, axis=0).where(pd.Series(first, index=weights.index), axis=0)
