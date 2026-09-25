"""TM-024-01, momentum with its crashes managed (build-plan.md): CA-001-01's momentum within groups,
each group holding its funds in equal parts plus k times its momentum tilt, k switched off in the
group's panic states ("panic") or scaled by the inverse of the tilt's volatility ("scale"), set on
the first session of each month."""
import numpy as np
import pandas as pd

GROUPS = {
    "sectors": ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY"],
    "equity markets": ["SPY", "QQQ", "IWM", "EFA", "EEM"],
    "commodities": ["GLD", "SLV", "DBC"],
}
LOOKBACK, SKIP = 252, 21


def positions(market, rule, vol_window, bear_window):
    if rule not in ("panic", "scale"):
        raise ValueError(f"rule '{rule}': 'panic' or 'scale'")
    prices, tradable = market.signal_prices, market.tradable
    members = {name: [t for t in tickers if t in prices.columns] for name, tickers in GROUPS.items()}
    members = {name: tickers for name, tickers in members.items() if tickers}
    grouped = {t for tickers in members.values() for t in tickers}
    stray = [t for t in prices.columns if t not in grouped]
    if stray:
        raise ValueError(f"assets in no group: {', '.join(stray)}")
    # 1. CA-001-01's weights: the top third of each group's ranked funds share the group's n/N
    past = prices.shift(1 + SKIP) / prices.shift(1 + LOOKBACK) - 1
    began = tradable.shift(1 + LOOKBACK, fill_value=False).astype(bool)
    ranked = tradable & began & past.notna()
    trading = tradable.sum(axis=1).astype(float)
    per = 1 / trading.where(trading > 0)
    momentum = (tradable & ~ranked).astype(float).mul(per, axis=0).fillna(0.0)
    for tickers in members.values():
        n = ranked[tickers].sum(axis=1)
        leaders = np.maximum(1, np.rint(n / 3))
        order = past[tickers].where(ranked[tickers]).rank(axis=1, ascending=False, method="first")
        chosen = order.le(leaders, axis=0) & ranked[tickers]
        share = (n * per / leaders).fillna(0.0)
        momentum[tickers] = momentum[tickers] + chosen.astype(float).mul(share, axis=0)
    # 2. the neutral weights, 1/N for each fund trading, and the tilt: CA-001-01's weights less them
    neutral = tradable.astype(float).mul(per, axis=0).fillna(0.0)
    tilt = momentum - neutral
    index = prices.index
    first = pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)
    targeted = first & ranked.any(axis=1)
    # 3. each fund's daily return
    returns = prices / prices.shift(1) - 1
    # 4-5. each group's k, from what is known up to the session before
    k = {}
    for name, tickers in members.items():
        if rule == "panic":
            # 4. panic: the group's market below its level bear_window sessions before, and its
            #    volatility above its own average up to then
            daily = returns[tickers].where(tradable[tickers]).mean(axis=1)
            level = (1 + daily.fillna(0.0)).cumprod().where(daily.notna().cummax())
            bear = level.shift(1) < level.shift(1 + bear_window)
            vol = daily.rolling(vol_window).std().shift(1)
            high = vol > vol.expanding().mean()
            k[name] = pd.Series(np.where(bear & high, 0.0, 1.0), index=index)
        else:
            # 5. scale: the average volatility of the unmanaged tilt's return over its current one
            held = tilt[tickers].where(targeted, axis=0).ffill().shift(1)
            daily = held.mul(returns[tickers].fillna(0.0)).sum(axis=1, min_count=1)
            daily = daily.where(held.notna().any(axis=1))
            vol = daily.rolling(vol_window).std().shift(1)
            ratio = vol.expanding().mean() / vol.where(vol > 0)
            k[name] = ratio.clip(upper=1.0).fillna(1.0)
    # 6. the targets: the group in equal parts plus k times its tilt, on the first session of each
    #    month in which a fund is ranked, every fund named
    weights = neutral.copy()
    for name, tickers in members.items():
        weights[tickers] = weights[tickers] + tilt[tickers].mul(k[name], axis=0)
    return weights.where(targeted, axis=0)
