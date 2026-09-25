"""TM-039-01, momentum held while returns are dispersed (build-plan.md): CA-001-01's weights in a
group while the dispersion of its ranked funds' returns over the month just past is above its own
average, the group's ranked funds in equal parts otherwise, set on the first session of each
month."""
import numpy as np
import pandas as pd

GROUPS = {
    "sectors": ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY"],
    "equity markets": ["SPY", "QQQ", "IWM", "EFA", "EEM"],
    "commodities": ["GLD", "SLV", "DBC"],
}
SCOPES = ("group", "all")


def dispersion(month: pd.DataFrame, ranked: pd.DataFrame) -> pd.Series:
    """Each session's standard deviation of the ranked funds' returns over the month, n - 1 in the
    denominator; NaN on a session with fewer than two ranked funds."""
    held = month.where(ranked)
    return held.std(axis=1, ddof=1).where(ranked.sum(axis=1) >= 2)


def dispersed(month: pd.DataFrame, ranked: pd.DataFrame) -> pd.Series:
    """True on a session whose reading is above the average of the readings from the first through
    the session before; False without a reading or before one exists."""
    reading = dispersion(month, ranked)
    line = reading.expanding().mean().shift(1)
    return (reading > line).fillna(False)


def positions(market, lookback, skip, scope):
    if scope not in SCOPES:
        raise ValueError(f"scope is one of {', '.join(SCOPES)}, not {scope!r}")
    prices, tradable = market.signal_prices, market.tradable
    # 1. the ranking return, as CA-001-01: from `lookback` to `skip` sessions before the session before
    past = prices.shift(1 + skip) / prices.shift(1 + lookback) - 1
    # 2. ranked on each session, as CA-001-01 ranks on a target
    began = tradable.shift(1 + lookback, fill_value=False).astype(bool)
    ranked = tradable & began & past.notna()
    # 3. the month just past: the return from the close 1 + skip sessions before to the session before
    month = prices.shift(1) / prices.shift(1 + skip) - 1
    members = {name: [t for t in tickers if t in prices.columns] for name, tickers in GROUPS.items()}
    grouped = {t for tickers in members.values() for t in tickers}
    stray = [t for t in prices.columns if t not in grouped]
    if stray:
        raise ValueError(f"assets in no group: {', '.join(stray)}")
    # 4. the state: each group's own dispersion, or that of all ranked funds for every group
    if scope == "all":
        every = dispersed(month, ranked)
        state = {name: every for name in members}
    else:
        state = {name: dispersed(month[t], ranked[t]) for name, t in members.items() if t}
    # 5. the weights: a fund trading but not ranked holds 1/N; a group in the state holds
    #    CA-001-01's weights, n/N among its top third, and out of it its n ranked funds at 1/N
    trading = tradable.sum(axis=1).astype(float)
    per_fund = 1.0 / trading.where(trading > 0)
    weights = (tradable & ~ranked).astype(float).mul(per_fund, axis=0).fillna(0.0)
    for name, tickers in members.items():
        if not tickers:
            continue
        n = ranked[tickers].sum(axis=1)
        leaders = np.maximum(1, np.rint(n / 3))
        order = past[tickers].where(ranked[tickers]).rank(axis=1, ascending=False, method="first")
        chosen = order.le(leaders, axis=0) & ranked[tickers]
        tilted = chosen.astype(float).mul((n * per_fund / leaders).fillna(0.0), axis=0)
        equal = ranked[tickers].astype(float).mul(per_fund.fillna(0.0), axis=0)
        on = state[name].reindex(weights.index).fillna(False).astype(bool)
        weights[tickers] = weights[tickers] + tilted.where(on, equal, axis=0)
    # 6. targets on the first session of each month in which a fund is ranked, every fund named
    index = weights.index
    first = pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)
    return weights.where(first & ranked.any(axis=1), axis=0)
