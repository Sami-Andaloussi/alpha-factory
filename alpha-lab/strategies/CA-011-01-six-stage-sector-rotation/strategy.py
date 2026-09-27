"""CA-011-01, sector rotation through the six stages of the cycle (build-plan.md): each week, the
trends of bonds (IEF), stocks (SPY) and commodities (DBC) against their `average`-session means
give Pring's stage, and the portfolio holds the sectors, the asset classes, or both, that Murphy
and Stovall name for it."""
import numpy as np
import pandas as pd

SECTORS = ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY"]
# (IEF up, SPY up, DBC up) -> Pring's stage; the two other combinations are out of sequence
STAGES = {(1, 0, 0): 1, (1, 1, 0): 2, (1, 1, 1): 3, (0, 1, 1): 4, (0, 0, 1): 5, (0, 0, 0): 6}
FUNDS = {
    "sectors": {1: ["XLP", "XLU", "XLRE"], 2: ["XLU", "XLF", "XLY"], 3: ["XLK", "XLI", "XLY"],
                4: ["XLE", "XLB"], 5: ["XLE", "XLP"], 6: ["XLP", "XLU"]},
    "assets": {1: ["IEF"], 2: ["SPY"], 3: ["SPY", "GLD"], 4: ["DBC", "GLD"], 5: ["DBC", "GLD", "XLE"],
               6: []},
}
# each fund once: XLE is both a sector and an oil share in stage 5
FUNDS["all"] = {k: list(dict.fromkeys(FUNDS["sectors"][k] + FUNDS["assets"][k])) for k in range(1, 6)} | {6: ["XLP", "XLU"]}


def stages(signal, average):
    """Pring's stage at every session, from the closes up to the session before: 1 to 6, 0 out of
    sequence, NaN while a mean is missing."""
    # 2. each market up if its close on the session before is above its mean up to that session
    ups = {}
    for ticker in ("IEF", "SPY", "DBC"):
        close = signal[ticker]
        mean = close.rolling(average, min_periods=average).mean()
        up = (close > mean).astype(float).where(mean.notna() & close.notna())
        ups[ticker] = up.shift(1)
    ups = pd.DataFrame(ups)
    # 3. the three signs give the stage
    known = ups.notna().all(axis=1)
    codes = [STAGES.get(tuple(int(v) for v in row), 0) if ok else np.nan
             for row, ok in zip(ups.fillna(0).to_numpy(), known.to_numpy())]
    return pd.Series(codes, index=signal.index, dtype=float)


def positions(market, average, holdings):
    signal, tradable = market.signal_prices, market.tradable
    for ticker in ("IEF", "SPY", "DBC"):
        if ticker not in signal.columns:
            raise ValueError(f"the stage reads {ticker}, which the market lacks")
    # 1. the first session of each week
    iso = signal.index.isocalendar()
    week = pd.Series((iso.year * 100 + iso.week).to_numpy(), index=signal.index)
    first = week.ne(week.shift(1))
    stage = stages(signal, average)
    # 4. the funds named for the stage that trade, in equal parts
    named = pd.DataFrame(False, index=signal.index, columns=signal.columns)
    for k, funds in FUNDS[holdings].items():
        cols = [t for t in funds if t in signal.columns]
        if cols:
            named.loc[stage == k, cols] = True
    out = SECTORS if holdings == "sectors" else list(signal.columns)
    cols = [t for t in out if t in signal.columns]
    named.loc[stage == 0, cols] = True
    held = named & tradable
    count = held.sum(axis=1)
    weights = held.astype(float).div(count.where(count > 0), axis=0).fillna(0.0)
    return weights.where(first & stage.notna(), axis=0)
