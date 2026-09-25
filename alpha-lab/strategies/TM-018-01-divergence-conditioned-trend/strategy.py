"""TM-018-01, trend following switched on by divergence or crisis (build-plan.md): TM-017-01's rule in
a divergent or crisis state, the seven funds in equal parts otherwise, set on the first session of
each month."""
import numpy as np
import pandas as pd

EQUITY, DEPTH = "SPY", 0.05


def positions(market, condition, mdi_window, lookback):
    if condition not in ("divergence", "crisis"):
        raise ValueError(f"condition '{condition}': 'divergence' or 'crisis'")
    prices, tradable = market.signal_prices, market.tradable
    index = prices.index
    # 1. the state, read on the session before
    if condition == "divergence":
        # the market divergence index: each fund's signal to noise ratio over its last `mdi_window`
        # daily changes up to the session before, averaged over the funds that have them, above the
        # average of its daily values up to then
        change = (prices - prices.shift(mdi_window)).abs()
        path = prices.diff().abs().rolling(mdi_window, min_periods=mdi_window).sum()
        snr = (change / path.where(path > 0)).shift(1)
        mdi = snr.mean(axis=1)
        state = mdi > mdi.expanding().mean()
        known = mdi.notna()
    else:
        # an equity crisis: SPY fell over the month just ended, in an unbroken run of falling months
        # that lost DEPTH or more in all; the month just ended is the one of the session before
        month = pd.Series(index.to_period("M"), index=index)
        closes = prices[EQUITY].groupby(month.values).last()
        change = closes / closes.shift(1) - 1
        crisis, run = {}, 1.0
        for period, r in change.items():
            run = run * (1 + r) if r < 0 else 1.0
            crisis[period] = bool(r < 0 and run - 1 <= -DEPTH)
        before = month.shift(1)
        state = before.map(crisis).fillna(False).astype(bool)
        known = before.map(change.notna()).fillna(False).astype(bool)
    # 2. TM-017-01's rule: each fund whose past return beats the bill's, a seventh each
    past = prices.shift(1) / prices.shift(1 + lookback) - 1
    bill = (1 + market.rf.fillna(0.0)).cumprod()
    cash = bill.shift(1) / bill.shift(1 + lookback) - 1
    trend = past.gt(cash, axis=0) & tradable
    in_trend = trend.astype(float) / prices.shape[1]
    # 3. out of the state: the funds that trade, in equal parts
    count = tradable.sum(axis=1)
    equal = tradable.astype(float).div(count.where(count > 0), axis=0).fillna(0.0)
    weights = in_trend.where(state & known, equal, axis=0)
    # 4. targets on the first session of each month, from the first in which the state is known and a
    #    fund has `lookback` + 1 closes, every fund named
    first = pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)
    ready = (known & past.notna().any(axis=1)).cummax()
    return weights.where(first & ready, axis=0)
