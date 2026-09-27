"""CA-003-01, style momentum within groups (build-plan.md): three styles -- momentum, value and
defensive -- built within the sector funds and within the equity markets from the funds' closes;
each style holds a third of the portfolio in its long leg when its own long/short return over the
last `window` sessions was above zero, and in the funds held in equal parts otherwise, set on the
first session of each month."""
import numpy as np
import pandas as pd

GROUPS = {
    "sectors": ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY"],
    "equity markets": ["SPY", "QQQ", "IWM", "EFA", "EEM"],
}
STYLES = ("momentum", "value", "defensive")


def formations(index):
    # 1. the first session of each month
    return pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)


def scores(prices, tradable):
    """Each style's score and whether a member is ranked, at every row, from closes up to the
    session before; higher is better for the long leg."""
    # 2. the scores, each reading the session before and further back
    returns = prices / prices.shift(1) - 1
    momentum = prices.shift(22) / prices.shift(253) - 1
    value = -(prices.shift(1) / prices.shift(1261) - 1)
    volatility = returns.shift(1).rolling(252, min_periods=252).std()
    defensive = -volatility
    out = {}
    for name, score, first in (("momentum", momentum, 253), ("value", value, 1261),
                               ("defensive", defensive, 253)):
        began = tradable.shift(first, fill_value=False).astype(bool)
        ranked = tradable & began & score.notna()
        out[name] = (score, ranked)
    return out, returns


def legs(score, ranked, members):
    """The long and short legs of one style in each group, and each group's number of ranked
    members, at every row."""
    # 3. a third of the ranked members, one at least, half to even; two ranked members at least
    long = pd.DataFrame(False, index=score.index, columns=score.columns)
    short = long.copy()
    counts = {}
    for name, tickers in members.items():
        n = ranked[tickers].sum(axis=1)
        k = np.maximum(1, np.rint(n / 3))
        has = n >= 2
        order = score[tickers].where(ranked[tickers])
        best = order.rank(axis=1, ascending=False, method="first")
        worst = order.rank(axis=1, ascending=True, method="first")
        long[tickers] = (best.le(k, axis=0) & ranked[tickers]).mul(has.astype(int), axis=0).astype(bool)
        short[tickers] = (worst.le(k, axis=0) & ranked[tickers]).mul(has.astype(int), axis=0).astype(bool)
        counts[name] = n.where(has, 0)
    return long, short, pd.DataFrame(counts)


def style_returns(long, short, counts, returns, first, members):
    """Each session's long/short return of one style, from the legs of the last formation
    strictly before it; NaN where no group has legs."""
    # 4. legs written on formation rows, carried forward, then read one row later
    carry = lambda frame: frame.where(first, axis=0).ffill().shift(1)
    long_held = carry(long.astype(float))
    short_held = carry(short.astype(float))
    n_held = carry(counts.astype(float))
    total = pd.Series(0.0, index=returns.index)
    weight = pd.Series(0.0, index=returns.index)
    for name, tickers in members.items():
        r = returns[tickers]
        lg, sh = long_held[tickers] > 0.5, short_held[tickers] > 0.5
        gap = r.where(lg).mean(axis=1) - r.where(sh).mean(axis=1)
        n = n_held[name].fillna(0.0)
        usable = (n > 0) & gap.notna()
        total = total + (gap * n).where(usable, 0.0)
        weight = weight + n.where(usable, 0.0)
    return (total / weight.where(weight > 0)).rename(None)


def earned(daily, window):
    """At each row, whether the style's returns on each of the last `window` sessions up to the
    session before exist and sum above zero; NaN where the record is short."""
    # 5. a sliding sum on each window's own values, never a running sum
    values = daily.to_numpy(dtype=float)
    out = np.full(len(values), np.nan)
    if len(values) > window:
        windows = np.lib.stride_tricks.sliding_window_view(values, window)[:-1]
        sums = windows.sum(axis=1)
        full = ~np.isnan(windows).any(axis=1)
        out[window:] = np.where(full, (sums > 0).astype(float), np.nan)
    return pd.Series(out, index=daily.index)


def build(market, window):
    """The styles, their legs, daily returns and earned states, as the clause reads them too."""
    prices, tradable = market.signal_prices, market.tradable
    members = {name: [t for t in tickers if t in prices.columns] for name, tickers in GROUPS.items()}
    grouped = {t for tickers in members.values() for t in tickers}
    stray = [t for t in prices.columns if t not in grouped]
    if stray:
        raise ValueError(f"assets in no group: {', '.join(stray)}")
    members = {name: tickers for name, tickers in members.items() if tickers}
    first = formations(prices.index)
    styles, returns = scores(prices, tradable)
    built = {}
    for name in STYLES:
        score, ranked = styles[name]
        long, short, counts = legs(score, ranked, members)
        daily = style_returns(long, short, counts, returns, first, members)
        built[name] = {"long": long, "short": short, "counts": counts, "ranked": ranked,
                       "daily": daily, "earned": earned(daily, window)}
    return built, members, first


def positions(market, window):
    built, members, first = build(market, window)
    tradable = market.tradable
    trading = tradable.sum(axis=1).astype(float)
    equal = tradable.astype(float).div(trading.where(trading > 0), axis=0).fillna(0.0)
    # 6. each style's third: its long leg when earned, the funds in equal parts otherwise
    total = pd.DataFrame(0.0, index=tradable.index, columns=tradable.columns)
    defined = pd.Series(False, index=tradable.index)
    for name in STYLES:
        style = built[name]
        state = style["earned"]
        defined = defined | state.notna()
        legged = pd.DataFrame(False, index=tradable.index, columns=tradable.columns)
        tilt = pd.DataFrame(0.0, index=tradable.index, columns=tradable.columns)
        for group, tickers in members.items():
            n = style["counts"][group]
            k = style["long"][tickers].sum(axis=1)
            share = (n / trading.where(trading > 0) / k.where(k > 0)).fillna(0.0)
            tilt[tickers] = style["long"][tickers].astype(float).mul(share, axis=0)
            legged[tickers] = np.repeat((n > 0).to_numpy()[:, None], len(tickers), axis=1)
        others = tradable & ~(legged & style["ranked"])
        third = tilt + others.astype(float).div(trading.where(trading > 0), axis=0).fillna(0.0)
        on = (state == 1.0)
        total = total + third.where(on, equal, axis=0) / 3
    start = defined & first
    begun = start.cumsum() > 0
    return total.where(first & begun, axis=0)
