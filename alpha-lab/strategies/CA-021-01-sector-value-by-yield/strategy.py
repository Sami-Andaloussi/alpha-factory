"""CA-021-01, value by yield within the sector funds (build-plan.md): on the first session of each
month, the top third of the ranked sector funds by their trailing yield, the cash their
distributions paid over `months` calendar months over the close of the session before, held in
equal shares of the ranked funds' share of the portfolio; CA-024-01's construction on its sector
group, ranked on the yield."""
import numpy as np
import pandas as pd

SECTORS = ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY"]
OWN_MONTHS = 60


def trailing_yield(dates, close, paid, i, lo):
    """One fund's yield read on the target's session, row i: over the distributions given after
    `lo` and up to row i-1, each one's cash over the close of i-1; NaN when the fund is not ranked."""
    read = np.flatnonzero(~np.isnan(paid[:i]))
    if not len(read) or dates[read[0]] > lo:                    # the reading starts after the window
        return np.nan
    first = np.searchsorted(dates, lo, side="right")            # the window's first row, after lo
    window = paid[first:i]
    known = np.flatnonzero(~np.isnan(window))
    last = known[-1] if len(known) else -1
    if np.isnan(window[:last + 1]).any():                       # a NaN that does not end on t-1
        return np.nan
    given = first + np.flatnonzero(window[:last + 1] > 0)       # the rows c_j, oldest first
    if not len(given):
        return 0.0
    f = paid[given]
    scaled = np.cumprod((1 - f)[::-1])[::-1]                    # prod over c_j <= c_k <= t-1 of (1 - f_k)
    cash = f * close[given - 1] / close[i - 1] / scaled
    return float(cash.sum())


def positions(market, months, measure):
    prices, paid, tradable = market.signal_prices, market.signal_distributions, market.tradable
    if paid is None:
        raise ValueError("the market carries no distributions")
    stray = [t for t in prices.columns if t not in SECTORS]
    if stray:
        raise ValueError(f"not a sector fund: {', '.join(stray)}")
    index = prices.index
    dates = index.to_numpy()
    # 1. the targets' sessions: the first of each month, after the market's first session
    first = pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)
    rows = [i for i in np.flatnonzero(first.to_numpy()) if i > 0]
    # 2. each fund's trailing yield on them, annualised: the cash of `months` calendar months,
    #    from the day after the same date `months` months before t-1, over the close of t-1
    level = pd.DataFrame(np.nan, index=index[rows], columns=prices.columns)
    for c in prices.columns:
        close, cash = prices[c].to_numpy(dtype=float), paid[c].to_numpy(dtype=float)
        for r, i in enumerate(rows):
            lo = (index[i - 1] - pd.DateOffset(months=months)).to_datetime64()
            level.iloc[r, level.columns.get_loc(c)] = trailing_yield(dates, close, cash, i, lo)
    level = level * 12 / months
    # 3. the score: the yield itself, or over its mean on the sixty targets up to this one
    if measure == "level":
        score = level
    elif measure == "own":
        score = level / level.rolling(OWN_MONTHS, min_periods=OWN_MONTHS).mean()
    else:
        raise ValueError(f"unknown measure: {measure}")
    # 4. the weights: of the N funds trading, the n ranked hold n/N among the top third of their
    #    yields, rounded, one at least; a fund trading but not ranked holds 1/N
    trade = tradable.loc[score.index, score.columns]
    ranked = trade & score.notna()
    trading = trade.sum(axis=1).astype(float)
    weights = (trade & ~ranked).astype(float).div(trading.where(trading > 0), axis=0).fillna(0.0)
    n = ranked.sum(axis=1)
    highest = np.maximum(1, np.rint(n / 3))
    order = score.where(ranked).rank(axis=1, ascending=False, method="first")
    chosen = order.le(highest, axis=0) & ranked
    share = (n / trading.where(trading > 0) / highest).fillna(0.0)
    weights = weights + chosen.astype(float).mul(share, axis=0)
    # 5. targets from the first month in which a fund is ranked, every fund named, NaN elsewhere
    started = ranked.any(axis=1).cummax()
    out = pd.DataFrame(np.nan, index=index, columns=prices.columns)
    out.loc[weights.index[started]] = weights[started].to_numpy()
    return out
