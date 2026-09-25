"""LL-042-01, cross-asset momentum between equities and Treasuries (build-plan.md): equity funds held
while the bond market's past year beats the bill, bond funds while the equity market's does not,
with or without each fund's own trend agreeing, set on the first session of each month."""
import numpy as np
import pandas as pd

EQUITIES = ("SPY", "QQQ", "IWM", "EFA", "EEM")
BONDS = ("IEF", "TLT")
BOND_SIGNAL, EQUITY_SIGNAL = "IEF", "SPY"


def positions(market, lookback, rule):
    if rule not in ("both", "cross"):
        raise ValueError(f"rule '{rule}': 'both' or 'cross'")
    prices = market.signal_prices
    # 1. each fund's past return over `lookback` sessions, up to the session before, less the bill's
    bill = (1 + market.rf.fillna(0.0)).cumprod()
    cash = bill.shift(1) / bill.shift(1 + lookback) - 1
    excess = (prices.shift(1) / prices.shift(1 + lookback) - 1).sub(cash, axis=0)
    has_past = excess.notna()
    # 2. the two signals, from prices alone: bonds rising, equities falling
    off = pd.Series(False, index=prices.index)
    bonds_rise = excess[BOND_SIGNAL].gt(0) if BOND_SIGNAL in prices else off
    equities_fall = excess[EQUITY_SIGNAL].lt(0) if EQUITY_SIGNAL in prices else off
    # 3. who is held: the other market's signal, and under "both" the fund's own trend too
    held = pd.DataFrame(False, index=prices.index, columns=prices.columns)
    for fund in prices.columns:
        own = excess[fund].gt(0) if rule == "both" else has_past[fund]
        if fund in EQUITIES:
            held[fund] = bonds_rise & own
        elif fund in BONDS:
            held[fund] = equities_fall & own
        else:
            raise ValueError(f"{fund} is neither an equity fund nor a bond fund of the card")
    held &= market.tradable
    # 4. one share of the portfolio for each fund held; the rest is cash
    weights = held.astype(float) / prices.shape[1]
    # 5. targets on the first session of each month, every fund named
    index = weights.index
    first = pd.Series(np.r_[True, index.month[1:] != index.month[:-1]], index=index)
    return weights.where(first, axis=0)
