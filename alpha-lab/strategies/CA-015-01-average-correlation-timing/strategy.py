"""CA-015-01, the sector funds' average correlation as a forecast of their market (build-plan.md):
each month, the sector funds are held in the proportion of the percentile of their average pairwise
correlation over the past `window` sessions among its readings of the past `lookback` sessions
("scaled"), or all or none against the median of those readings ("median"), the rest in cash."""
import numpy as np
import pandas as pd

SECTORS = ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY"]


def readings(signal, tradable, window):
    """The average pairwise correlation, on each session, of the daily returns of the sector funds
    that trade on that session and have `window` returns up to and including the session before."""
    cols = [t for t in SECTORS if t in signal.columns]
    returns = signal[cols].pct_change(fill_method=None).to_numpy()
    trades = tradable[cols].to_numpy()
    out = np.full(len(signal), np.nan)
    for k in range(window + 1, len(signal)):
        block = returns[k - window:k]  # the returns up to and including the session before k
        ok = trades[k] & ~np.isnan(block).any(axis=0)
        if ok.sum() < 2:
            continue
        corr = np.corrcoef(block[:, ok].T)
        out[k] = corr[np.triu_indices(int(ok.sum()), 1)].mean()
    return pd.Series(out, index=signal.index)


def positions(market, window, lookback, rule):
    signal, tradable = market.signal_prices, market.tradable
    # 1. the reading on every session
    reading = readings(signal, tradable, window).to_numpy()
    # 2. its percentile, or its place against the median, among the lookback readings before it
    share = np.full(len(reading), np.nan)
    for k in range(lookback, len(reading)):
        past = reading[k - lookback:k]
        if np.isnan(reading[k]) or np.isnan(past).any():
            continue
        if rule == "scaled":
            share[k] = (past <= reading[k]).mean()
        elif rule == "median":
            share[k] = 1.0 if reading[k] > np.median(past) else 0.0
        else:
            raise ValueError(f"unknown rule {rule!r}")
    share = pd.Series(share, index=signal.index)
    # 3. the first session of each month
    month = pd.Series(signal.index.to_period("M"), index=signal.index)
    first = month.ne(month.shift(1))
    # 4. the sector funds that trade, in equal parts, in the proportion of the share
    held = tradable.reindex(columns=signal.columns, fill_value=False).copy()
    held[[t for t in held.columns if t not in SECTORS]] = False
    count = held.sum(axis=1)
    weights = held.astype(float).div(count.where(count > 0), axis=0).fillna(0.0).mul(share, axis=0)
    return weights.where(first & share.notna(), axis=0)
