"""TM-023-01, momentum in the months that end a quarter (build-plan.md): CA-001-01's momentum within
groups, each group holding its funds in equal parts plus its momentum tilt, the tilt held only in
the target months the variant names, set on the first session of each month."""
import numpy as np
import pandas as pd

GROUPS = {
    "sectors": ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY"],
    "equity markets": ["SPY", "QQQ", "IWM", "EFA", "EEM"],
    "commodities": ["GLD", "SLV", "DBC"],
}
MONTHS = {"quarter-ends": {3, 6, 9, 12}, "all-but-january": set(range(2, 13))}


def positions(market, lookback, skip, months):
    if months not in MONTHS:
        raise ValueError(f"months must be one of {', '.join(MONTHS)}, not {months!r}")
    prices, tradable = market.signal_prices, market.tradable
    members = {name: [t for t in tickers if t in prices.columns] for name, tickers in GROUPS.items()}
    members = {name: tickers for name, tickers in members.items() if tickers}
    grouped = {t for tickers in members.values() for t in tickers}
    stray = [t for t in prices.columns if t not in grouped]
    if stray:
        raise ValueError(f"assets in no group: {', '.join(stray)}")
    # 1. CA-001-01's weights: the top third of each group's ranked funds share the group's n/N
    past = prices.shift(1 + skip) / prices.shift(1 + lookback) - 1
    began = tradable.shift(1 + lookback, fill_value=False).astype(bool)
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
    # 3. the calendar: k = 1 in the target months the variant names, 0 in the others
    k = pd.Series(np.where(index.month.isin(sorted(MONTHS[months])), 1.0, 0.0), index=index)
    # 4. the targets: each group in equal parts plus k times its tilt, on the first session of each
    #    month on which a fund is ranked, every fund named
    weights = neutral + tilt.mul(k, axis=0)
    return weights.where(targeted, axis=0)
