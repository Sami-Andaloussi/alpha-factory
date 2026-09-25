"""The engine adapter, the costs and the benchmark."""
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from lab import costs, data, engine

DAYS = pd.bdate_range("2024-01-01", periods=4)
PRICES = pd.DataFrame({"A": [10.0, 11.0, 10.5, 12.0], "B": [20.0, 19.0, 21.0, 22.0]}, index=DAYS)
FEE = pd.Series({"A": 0.0005, "B": 0.0005})
FREE = pd.Series({"A": 0.0, "B": 0.0})
NO_RATE = pd.Series(0.0, index=DAYS)


def hold_from_first_day(weights):
    positions = pd.DataFrame(np.nan, index=DAYS, columns=PRICES.columns)
    positions.iloc[0] = weights
    return positions


def value(result):
    return engine.INITIAL * (1 + result.returns).cumprod()


def turnover(result):
    """The value traded each day over the portfolio's value at the close before."""
    traded = result.trades["value"].abs().groupby(result.trades["date"]).sum()
    return traded.reindex(result.returns.index, fill_value=0.0) / value(result).shift(1).fillna(engine.INITIAL)


def test_a_two_asset_example_computed_by_hand_matches_to_the_cent():
    # 1,000,000 in cash; 40% in A at 10 (40,000 shares) and 40% in B at 20 (20,000 shares), each
    # paying 5 bps on 400,000, that is 200: 199,600 stay in cash, and nothing trades after.
    result = engine.run(PRICES, hold_from_first_day([0.4, 0.4]), FEE, NO_RATE)
    by_hand = [40_000 * a + 20_000 * b + 199_600 for a, b in zip(PRICES["A"], PRICES["B"])]
    assert value(result).round(2).tolist() == pytest.approx(by_hand, abs=0.005)
    assert result.trades["cost"].tolist() == [200.0, 200.0]
    assert turnover(result).tolist() == pytest.approx([0.8, 0.0, 0.0, 0.0])


def test_a_row_with_any_target_sells_what_it_does_not_name():
    # Day 2 opens at 420,000 in A, 420,000 in B and 199,600 in cash, 1,039,600 in all. The row
    # [0.5, NaN] takes A to 519,800 (99,800 bought, 49.90 paid) and sells B (420,000, 210 paid).
    positions = hold_from_first_day([0.4, 0.4])
    positions.iloc[2] = [0.5, np.nan]
    result = engine.run(PRICES, positions, FEE, NO_RATE)
    day2 = result.trades[result.trades["date"] == DAYS[2]].set_index("asset")
    assert day2.loc["B", "value"] == pytest.approx(-420_000.0)
    assert day2.loc["A", "value"] == pytest.approx(99_800.0)
    cash = 199_600 + 420_000 - 210 - 99_800 - 49.90
    assert value(result).iloc[-1] == pytest.approx(519_800 / 10.5 * 12 + cash, abs=0.005)


def test_a_switch_when_fully_invested_sells_first_and_reaches_its_target():
    positions = hold_from_first_day([0.0, 1.0])
    positions.iloc[1] = [1.0, 0.0]
    result = engine.run(PRICES, positions, FEE, NO_RATE)
    assert result.weights.iloc[1].tolist() == pytest.approx([1.0, 0.0])


def test_a_position_held_from_start_to_end_is_buy_and_hold():
    result = engine.run(PRICES, hold_from_first_day([1.0, 0.0]), FREE, NO_RATE)
    assert value(result).iloc[-1] == pytest.approx(engine.INITIAL * 12.0 / 10.0)
    charged = engine.run(PRICES, hold_from_first_day([1.0, 0.0]), FEE, NO_RATE)
    assert value(charged).iloc[-1] == pytest.approx(engine.INITIAL / 1.0005 * 12.0 / 10.0)


def test_costs_scale_with_turnover():
    rng = np.random.default_rng(2)
    days = pd.bdate_range("2023-01-02", periods=250)
    prices = pd.DataFrame(100 * np.exp(np.cumsum(rng.normal(0, 0.01, (250, 2)), axis=0)), index=days,
                          columns=["A", "B"])
    rate = pd.Series(0.0004, index=days)          # trades and costs in dollars once the bills have grown
    weekly = pd.DataFrame(np.nan, index=days, columns=prices.columns)
    weekly.iloc[::5] = rng.dirichlet([1, 1], len(weekly.iloc[::5])) * 0.9
    once = engine.run(prices, weekly, costs.per_side(prices.columns), rate)
    twice = engine.run(prices, weekly, costs.per_side(prices.columns, multiplier=2), rate)
    assert np.allclose(once.costs, 0.0005 * turnover(once), rtol=0, atol=1e-12)
    assert twice.costs.sum() == pytest.approx(2 * once.costs.sum(), rel=1e-3)


def test_costs_are_matched_to_assets_by_name():
    reversed_fees = pd.Series({"B": 0.0020, "A": 0.0005})
    result = engine.run(PRICES, hold_from_first_day([0.4, 0.4]), reversed_fees, NO_RATE)
    assert result.trades.set_index("asset")["cost"].to_dict() == pytest.approx({"A": 200.0, "B": 800.0})


def test_a_strategy_fully_in_cash_earns_the_treasury_bill_rate():
    rate = pd.Series([0.0001, 0.0002, 0.00015, 0.0001], index=DAYS)
    result = engine.run(PRICES, hold_from_first_day([0.0, 0.0]), FEE, rate)
    assert result.returns.iloc[0] == 0.0
    assert np.allclose(result.returns.iloc[1:], rate.iloc[1:])
    assert (result.weights.sum(axis=1) == 0).all()


def test_cash_left_aside_compounds_at_the_bill_rate():
    # 500,000 in A at 10 (50,000 shares) and 500,000 in bills, held four days: the bills grow by
    # 1.01, then 1.02, then 1.01, and the weights follow what the bills are worth.
    rate = pd.Series([0.0, 0.01, 0.02, 0.01], index=DAYS)
    result = engine.run(PRICES, hold_from_first_day([0.5, 0.0]), FREE, rate)
    shares = 50_000 * PRICES["A"]
    bills = 500_000 * pd.Series(np.cumprod([1.0, 1.01, 1.02, 1.01]), index=DAYS)
    assert value(result).tolist() == pytest.approx((shares + bills).tolist(), abs=0.005)
    assert result.weights["A"].tolist() == pytest.approx((shares / (shares + bills)).tolist(), abs=1e-12)


def test_a_day_is_the_weights_held_overnight_times_the_returns_plus_cash_less_costs():
    rng = np.random.default_rng(3)
    days = pd.bdate_range("2023-01-02", periods=120)
    prices = pd.DataFrame(100 * np.exp(np.cumsum(rng.normal(0, 0.01, (120, 3)), axis=0)), index=days,
                          columns=["A", "B", "C"])
    rate = pd.Series(rng.uniform(0.0, 0.0005, 120), index=days)
    positions = pd.DataFrame(np.nan, index=days, columns=prices.columns)
    positions.iloc[::10] = rng.dirichlet([1, 1, 1], 12) * 0.8
    result = engine.run(prices, positions, costs.per_side(prices.columns), rate)
    held = result.weights.shift(1).fillna(0.0)
    rebuilt = (held * prices.pct_change().fillna(0.0)).sum(axis=1) + (1 - held.sum(axis=1)) * rate - result.costs
    assert np.allclose(result.returns.iloc[1:], rebuilt.iloc[1:], rtol=0, atol=1e-12)
    paid = result.trades.groupby("date")["cost"].sum().reindex(days, fill_value=0.0)
    assert np.allclose(paid / value(result).shift(1).fillna(engine.INITIAL), result.costs, rtol=0, atol=1e-15)


def test_several_sets_in_one_pass_are_the_single_runs():
    rate = pd.Series([0.0001, 0.0002, 0.00015, 0.0001], index=DAYS)
    fees = pd.Series({"A": 0.0005, "B": 0.0020})
    switch = hold_from_first_day([0.0, 1.0])
    switch.iloc[2] = [0.6, np.nan]
    sets = [hold_from_first_day([0.4, 0.4]), switch, hold_from_first_day([0.0, 0.0])]
    for one, many in zip([engine.run(PRICES, s, fees, rate) for s in sets], engine.run_many(PRICES, sets, fees, rate)):
        pd.testing.assert_series_equal(one.returns, many.returns)
        pd.testing.assert_frame_equal(one.weights, many.weights)
        pd.testing.assert_series_equal(one.costs, many.costs)
        pd.testing.assert_frame_equal(one.trades, many.trades)


def test_positions_are_matched_by_name_on_any_subset_of_sessions_and_assets():
    full = hold_from_first_day([0.3, 0.5])
    full.iloc[2] = [0.6, 0.0]
    base = engine.run(PRICES, full, FEE, NO_RATE)
    for other in (full[["B", "A"]], full.dropna(how="all")):
        same = engine.run(PRICES, other, FEE, NO_RATE)
        pd.testing.assert_series_equal(base.returns, same.returns)
        pd.testing.assert_frame_equal(base.trades, same.trades)
    only_a = engine.run(PRICES, hold_from_first_day([0.3, 0.0])[["A"]], FEE, NO_RATE)
    both = engine.run(PRICES, hold_from_first_day([0.3, 0.0]), FEE, NO_RATE)
    pd.testing.assert_series_equal(only_a.returns, both.returns)


def test_a_weight_within_the_tolerance_of_zero_never_opens_a_short():
    result = engine.run(PRICES, hold_from_first_day([0.5, -9e-13]), FEE, NO_RATE)
    assert list(result.trades["asset"]) == ["A"]
    assert (result.weights >= 0).all().all()


def test_positions_must_be_long_only_unlevered_priced_and_on_known_assets_and_sessions():
    with pytest.raises(ValueError, match="long only"):
        engine.run(PRICES, hold_from_first_day([-0.1, 0.5]), FEE, NO_RATE)
    with pytest.raises(ValueError, match="leverage"):
        engine.run(PRICES, hold_from_first_day([0.7, 0.7]), FEE, NO_RATE)
    unpriced = PRICES.copy()
    unpriced.iloc[0, 1] = np.nan
    with pytest.raises(ValueError, match="no price"):
        engine.run(unpriced, hold_from_first_day([0.5, 0.5]), FEE, NO_RATE)
    with pytest.raises(ValueError, match="assets without prices: C"):
        engine.run(PRICES, hold_from_first_day([0.4, 0.4]).assign(C=0.1), FEE, NO_RATE)
    saturday = hold_from_first_day([0.4, 0.4]).rename(index={DAYS[1]: pd.Timestamp("2024-01-06")})
    with pytest.raises(ValueError, match="not sessions"):
        engine.run(PRICES, saturday, FEE, NO_RATE)
    text = hold_from_first_day([0.4, 0.4]).set_axis([str(d.date()) for d in DAYS])
    with pytest.raises(ValueError, match="not sessions"):
        engine.run(PRICES, text, FEE, NO_RATE)
    at_noon = pd.Series(0.0001, index=DAYS + pd.Timedelta(hours=12))  # a rate that matches no session
    with pytest.raises(ValueError, match="bill rate on dates"):
        engine.run(PRICES, hold_from_first_day([0.4, 0.4]), FEE, at_noon)


def test_bitcoin_costs_four_times_an_etf_and_doubles_like_it():
    fees = costs.per_side(["SPY", "BTC-USD"])
    assert fees["SPY"] == 0.0005 and fees["BTC-USD"] == 0.0020
    doubled = costs.per_side(["SPY", "BTC-USD"], multiplier=2)
    assert doubled["SPY"] == pytest.approx(0.0010) and doubled["BTC-USD"] == pytest.approx(0.0040)


def test_the_benchmark_trades_on_the_strategy_s_days_and_on_each_entry(snapshot):
    market = data.load(root=snapshot)
    index = market.prices.index
    second = index.to_series().groupby(index.to_period("M")).nth(1)  # never 2019-07-01, when CCC enters
    positions = pd.DataFrame(np.nan, index=index, columns=market.prices.columns)
    positions.loc[second.values, "AAA"] = 0.5
    result = costs.benchmark(market, positions, crypto={"COIN"})
    assert set(result.trades["date"]) == set(second) | {index[0], pd.Timestamp("2019-07-01")}
    assert np.allclose(result.weights.sum(axis=1), 1.0)  # fully invested
    first = result.trades[result.trades["date"] == index[0]]
    assert sorted(first["asset"]) == ["AAA", "BBB", "COIN"]  # CCC is not tradable yet
    spread = first["value"].abs().max() - first["value"].abs().min()
    assert spread <= first["cost"].sum() + 1e-6  # equal weights, less the day's costs
    rate = (first["cost"] / first["value"].abs()).set_axis(first["asset"])
    assert rate["COIN"] == pytest.approx(0.0020) and rate["AAA"] == pytest.approx(0.0005)  # charged alike
    doubled = costs.benchmark(market, positions, multiplier=2, crypto={"COIN"}).trades
    rate = (doubled["cost"] / doubled["value"].abs()).groupby(doubled["asset"]).mean()
    assert rate["COIN"] == pytest.approx(0.0040) and rate["AAA"] == pytest.approx(0.0010)


def test_nothing_outside_the_engine_imports_the_engine_library():
    package = Path(__file__).resolve().parent.parent / "lab"
    importers = [p.relative_to(package).as_posix() for p in package.rglob("*.py") if "vectorbt" in p.read_text()]
    assert importers == ["engine.py"]
