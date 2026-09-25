"""TM-001-01, momentum between asset classes (build-plan.md): the `top` assets of the seven ranked
by their past return, the last `skip` sessions left out, held in equal parts, set on the first
session of each month."""
import numpy as np
import pandas as pd


def positions(market, lookback, skip, top):
    prices, tradable = market.signal_prices, market.tradable
    # 1. the ranking return: from `lookback` to `skip` sessions before the session before
    past = prices.shift(1 + skip) / prices.shift(1 + lookback) - 1
    # 2. ranked: trading today and on the window's first session, with a return over the window
    began = tradable.shift(1 + lookback, fill_value=False).astype(bool)
    ranked = tradable & began & past.notna()
    # 3. the leaders: the `top` highest, ties to the asset listed first, in equal parts
    order = past.where(ranked).rank(axis=1, ascending=False, method="first")
    chosen = order.le(top) & ranked
    count = chosen.sum(axis=1).astype(float)
    weights = chosen.astype(float).div(count.where(count > 0), axis=0).fillna(0.0)
    # 4. targets on the first session of each month on which an asset is ranked, every asset named
    index = weights.index
    first = pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)
    return weights.where(first & ranked.any(axis=1), axis=0)
