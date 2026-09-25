"""CA-006-01, financials lead the sectors (build-plan.md): the eleven sector funds held in equal parts
for the month after one in which financials led them, the bill otherwise, set on the first session
of each month."""
import numpy as np
import pandas as pd

LEADS = ("relative", "absolute", "composite")
LEADERS, LAGGARDS = ("XLF", "XLY", "XLRE"), ("XLE", "XLB")


def positions(market, lookback, lead):
    if lead not in LEADS:
        raise ValueError(f"lead is one of {', '.join(LEADS)}, not {lead!r}")
    prices, tradable = market.signal_prices, market.tradable
    # 1. each fund's return over the window, to the session before; the bill's over the same sessions
    began = tradable.shift(1 + lookback, fill_value=False).astype(bool)
    past = (prices.shift(1) / prices.shift(1 + lookback) - 1).where(tradable & began)
    growth = (1 + market.rf.reindex(prices.index).fillna(0.0)).cumprod()
    bill = growth.shift(1) / growth.shift(1 + lookback) - 1
    # 2. the signal
    if lead == "relative":
        signal = past["XLF"] - past.mean(axis=1)
    elif lead == "absolute":
        signal = past["XLF"] - bill
    else:
        leaders = past[[t for t in LEADERS if t in past.columns]].mean(axis=1)
        laggards = past[[t for t in LAGGARDS if t in past.columns]]
        signal = (leaders - laggards.mean(axis=1)).where(laggards.notna().all(axis=1))
    # 3. every fund trading in equal parts when the signal is positive, the bill otherwise
    trading = tradable.sum(axis=1).astype(float)
    held = tradable.astype(float).div(trading.where(trading > 0), axis=0).fillna(0.0)
    weights = held.mul((signal > 0).astype(float), axis=0)
    index = weights.index
    first = pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)
    return weights.where(first & signal.notna(), axis=0)
