"""The one module between the lab and its backtest engine.

`run()` takes prices, daily target positions, the cost per side of each asset and the daily
Treasury-bill rate, and returns the daily portfolio returns, the trades, the costs and the weights
held overnight; `run_many()` does the same for several position sets in one pass. vectorbt does the
work underneath; nothing else in the lab imports it, so another engine can replace it in an
afternoon.

Conventions, the same for every strategy and for the benchmark:
- the target weights of session t are set from the market up to t-1 (bitcoin through its signal
  prices, a day late), traded at the close of t, and earn the returns from t to t+1;
- a row of NaN means "hold": no order that day, and the weights drift with prices;
- a row with any target sells every asset it does not name;
- long only, no leverage: weights are at least 0 and sum to at most 1;
- no target on a day an asset has no price; an asset held through a missing price keeps its last;
- what is not invested is cash, and cash earns the Treasury-bill rate, compounded: the engine
  works in units of the bill, in which cash stays constant; the first session, and a session
  without a rate, earn nothing;
- a trade pays its cost per side on the value traded; when the weights sum to 1, the day's costs
  come out of the last purchase, which is that much smaller.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
import vectorbt as vbt

INITIAL = 1_000_000.0


@dataclass(frozen=True)
class Result:
    returns: pd.Series      # daily portfolio return, cash interest and costs included
    trades: pd.DataFrame    # one row per order: date, asset, value traded (positive when bought), cost paid
    costs: pd.Series        # costs paid that day over the portfolio's value at the close before
    weights: pd.DataFrame   # each asset's share of the portfolio from the close of t to that of t+1


def run(prices: pd.DataFrame, positions: pd.DataFrame, cost: pd.Series, rf: pd.Series) -> Result:
    """Simulate one strategy. positions: target weights on some or all of the prices' sessions and
    assets, matched by name, NaN to hold."""
    return run_many(prices, [positions], cost, rf)[0]


def run_many(prices: pd.DataFrame, many: list[pd.DataFrame], cost: pd.Series, rf: pd.Series) -> list[Result]:
    """Simulate several position sets on the same prices in one pass (variants, parameter neighbours)."""
    columns = list(prices.columns)
    targets = [check_positions(p, prices) for p in many]
    rate = rf.reindex(prices.index)
    if rate.count() != rf[(rf.index >= prices.index[0]) & (rf.index <= prices.index[-1])].count():
        raise ValueError("a bill rate on dates that are not sessions of the prices")
    rate = rate.fillna(0.0).to_numpy().copy()
    rate[0] = 0.0
    bill = np.cumprod(1 + rate)                                      # what 1 held in bills is worth
    close = prices.ffill().bfill().to_numpy() / bill[:, None]        # prices in units of the bill
    width = len(columns)
    portfolio = vbt.Portfolio.from_orders(
        close=np.tile(close, (1, len(targets))),
        size=np.concatenate([t.to_numpy() for t in targets], axis=1),
        size_type="targetpercent",
        direction="longonly",
        fees=np.tile(cost.reindex(columns).to_numpy(), len(targets)),
        group_by=np.repeat(np.arange(len(targets)), width),
        cash_sharing=True,
        call_seq="auto",
        init_cash=INITIAL,
        freq="1D",
    )
    days = len(prices.index)
    value = portfolio.value().to_numpy().reshape(days, -1)            # one column per set, in bills
    held = portfolio.asset_value(group_by=False).to_numpy()            # one column per asset and set
    in_bills = portfolio.returns().to_numpy().reshape(days, -1)
    records = portfolio.orders.records
    col, day, size, price, fees, side = (np.asarray(records[f]) for f in ("col", "idx", "size", "price", "fees", "side"))
    results = []
    for k in range(len(targets)):
        returns = pd.Series((1 + in_bills[:, k]) * (1 + rate) - 1, index=prices.index, name="returns")
        mine = col // width == k
        dollars = bill[day[mine]]                                      # bills back into dollars
        trades = pd.DataFrame({
            "date": prices.index[day[mine]],
            "asset": [columns[c % width] for c in col[mine]],
            "value": size[mine] * price[mine] * dollars * np.where(side[mine] == 0, 1.0, -1.0),
            "cost": fees[mine] * dollars,
        })
        paid = np.bincount(day[mine], weights=fees[mine], minlength=days)
        before = np.concatenate([[INITIAL], value[:-1, k]])
        costs = pd.Series(paid / before * (1 + rate), index=prices.index, name="costs")
        weights = pd.DataFrame(held[:, k * width:(k + 1) * width] / value[:, k:k + 1], index=prices.index,
                               columns=columns)
        results.append(Result(returns, trades, costs, weights))
    return results


def check_positions(positions: pd.DataFrame, prices: pd.DataFrame) -> pd.DataFrame:
    """The targets on the prices' sessions and assets, refused when they break a convention, and
    each row that names a target completed with zeros: an asset not named is sold."""
    unknown = sorted(set(positions.columns) - set(prices.columns))
    if unknown:
        raise ValueError(f"positions on assets without prices: {', '.join(map(str, unknown))}")
    aligned = positions.reindex(index=prices.index, columns=prices.columns)
    if len(positions.index.difference(prices.index)) or aligned.count().sum() != positions.count().sum():
        raise ValueError("positions on dates that are not sessions of the prices")  # or labels that only look like them
    positions = aligned
    held = positions.dropna(how="all")
    if (held < -1e-12).any().any():
        raise ValueError("long only: a weight is negative")
    if (held.sum(axis=1) > 1 + 1e-9).any():
        raise ValueError("no leverage: the weights of a day sum to more than 1")
    if (positions.fillna(0.0).gt(0.0) & prices.isna()).any().any():
        raise ValueError("an asset is held on a day it has no price (before it starts trading)")
    filled = positions.copy()
    named = positions.notna().any(axis=1)
    filled.loc[named] = positions.loc[named].fillna(0.0)
    return filled
