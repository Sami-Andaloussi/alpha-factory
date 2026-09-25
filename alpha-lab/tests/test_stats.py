"""The formulas, against published values and series whose answer is known."""
import numpy as np
import pandas as pd
import pytest

from lab import stats


def test_the_deflated_sharpe_ratio_reproduces_its_published_example():
    # Bailey & Lopez de Prado (2014), section on a numerical example: 100 trials whose annual Sharpe
    # ratios vary by 0.5, a selected ratio of 2.5 a year over 1,250 days, skewness -3, kurtosis 10.
    bar = stats.expected_max_sharpe(100, 0.5 / 250)
    assert bar == pytest.approx(0.1132, abs=5e-5)
    assert stats.psr(2.5 / np.sqrt(250), 1250, -3.0, 10.0, benchmark=bar) == pytest.approx(0.9004, abs=5e-5)


def test_one_trial_sets_no_bar():
    assert stats.expected_max_sharpe(1, 0.01) == 0.0


def test_a_series_with_a_known_sharpe_ratio():
    z = np.random.default_rng(3).normal(size=2520)
    z = (z - z.mean()) / z.std(ddof=1)
    excess = pd.Series(0.0004 + 0.01 * z)
    assert stats.sharpe(excess) == pytest.approx(0.04 * np.sqrt(252), rel=1e-12)


def test_the_psr_of_a_zero_sharpe_ratio_is_one_half():
    assert stats.psr(0.0, 1000, 0.0, 3.0) == pytest.approx(0.5)


def test_lo_factor_is_the_square_root_of_q_without_autocorrelation():
    white = pd.Series(np.random.default_rng(4).normal(0, 0.01, 200_000))
    assert stats.lo_factor(white) == pytest.approx(np.sqrt(252), rel=0.02)


def ar1(rho, n, seed):
    rng = np.random.default_rng(seed)
    shocks = rng.normal(0, 0.01, n)
    x = np.empty(n)
    x[0] = shocks[0]
    for t in range(1, n):
        x[t] = rho * x[t - 1] + shocks[t]
    return pd.Series(x)


def test_lo_factor_shrinks_under_positive_autocorrelation_as_the_formula_says():
    rho, x = 0.3, ar1(0.3, 400_000, 5)
    for q in (12, 252):                  # at twelve periods, (q - k) and q differ by several percent
        expected = q / np.sqrt(q + 2 * sum((q - k) * rho ** k for k in range(1, 11)))
        assert stats.lo_factor(x, q=q) == pytest.approx(expected, rel=0.005)
        assert expected < np.sqrt(q)


def test_lo_factor_reads_ten_autocorrelations_and_no_more():
    x = ar1(0.6, 400_000, 6)
    assert stats.lo_factor(x) == stats.lo_factor(x, lags=10)
    assert stats.lo_factor(x, lags=1) > stats.lo_factor(x, lags=10) * 1.01


def test_lo_factor_reads_the_tenth_autocorrelation():
    shocks = np.random.default_rng(11).normal(size=400_010)
    x = pd.Series(shocks[10:] + 0.9 * shocks[:-10])                  # correlated at lag ten alone
    assert stats.lo_factor(x) < stats.lo_factor(x, lags=9) * 0.8


def test_the_adjusted_psr_is_the_psr_of_lo_s_sharpe_ratio():
    x = ar1(0.3, 5000, 7) + 0.0008
    n, s, k = stats.moments(x)
    assert stats.adjusted_psr(x) == pytest.approx(stats.psr(stats.lo_sharpe(x) / np.sqrt(252), n, s, k), rel=1e-12)
    assert stats.adjusted_psr(x) < stats.psr(stats.sharpe(x) / np.sqrt(252), n, s, k)


def test_an_edge_that_never_moves_is_no_evidence():
    nothing = pd.Series(np.zeros(500))          # no bets: no Sharpe ratio, and no moments to weigh it
    assert stats.adjusted_psr(nothing) == 0.0
    assert stats.dsr(nothing, 10, 1 / 500) == 0.0


def test_near_clones_count_as_one_trial():
    rng = np.random.default_rng(6)
    bases = rng.normal(0, 0.01, (1000, 3))
    clones = {f"{b}-{c}": bases[:, b] + rng.normal(0, 0.001, 1000) for b in range(3) for c in range(5)}
    assert stats.near_clone_clusters(pd.DataFrame(clones)).max() == 3
    independent = pd.DataFrame(rng.normal(0, 0.01, (1000, 15)))
    assert stats.near_clone_clusters(independent).max() == 15
    opposite = pd.DataFrame({"long": bases[:, 0], "short": -bases[:, 0]})      # the same bets, the other way
    assert stats.near_clone_clusters(opposite).max() == 2


def test_every_pair_inside_a_cluster_is_a_near_clone():
    rng = np.random.default_rng(8)
    a, c = rng.normal(0, 1, 2000), rng.normal(0, 1, 2000)
    b = (a + c) / np.sqrt(2)                     # 0.71 with each end, which do not correlate with each other
    a_ = (0.9 * b + 0.44 * a) / np.hypot(0.9, 0.44)
    c_ = (0.9 * b + 0.44 * c) / np.hypot(0.9, 0.44)
    chain = pd.DataFrame({"a": a_, "b": b, "c": c_})
    corr = chain.corr()
    assert corr.loc["a", "b"] > 0.9 and corr.loc["b", "c"] > 0.9 and corr.loc["a", "c"] < 0.9
    assert stats.near_clone_clusters(chain).max() == 2   # a chain is not one cluster


def test_trials_with_fewer_than_24_months_in_common_are_never_clones():
    months = pd.date_range("2005-01-31", periods=48, freq="ME")
    series = pd.Series(np.random.default_rng(9).normal(0, 0.03, 48), index=months)
    first, second = series.copy(), series.copy()
    first.iloc[30:], second.iloc[:18] = np.nan, np.nan          # 12 months in common, identical there
    assert stats.near_clone_clusters(pd.DataFrame({"a": first, "b": second})).max() == 2


def test_the_stationary_bootstrap_draws_blocks_of_the_stated_mean_length():
    paths = stats.stationary_bootstrap(5000, 2000, 20.0, 50, np.random.default_rng(7))
    continues = (np.diff(paths, axis=1) == 1) | (np.diff(paths, axis=1) == -4999)
    assert 1 / (1 - continues.mean()) == pytest.approx(20.0, rel=0.05)
    assert paths.min() >= 0 and paths.max() < 5000


def test_a_block_that_reaches_the_end_of_the_series_wraps_to_its_start():
    paths = stats.stationary_bootstrap(10, 1000, 100.0, 20, np.random.default_rng(10))
    at_end = paths[:, :-1] == 9
    assert np.mean(paths[:, 1:][at_end] == 0) > 0.9


def test_placebo_shifts_stay_at_least_a_year_away_each_way():
    offsets = stats.placebo_offsets(3000, 1000, 252, np.random.default_rng(8))
    assert offsets.min() >= 252 and offsets.max() <= 3000 - 252
    small = stats.placebo_offsets(10, 2000, 3, np.random.default_rng(8))     # both bounds are shifts it draws
    assert set(small) == {3, 4, 5, 6, 7}
    with pytest.raises(ValueError, match="too short"):
        stats.placebo_offsets(504, 10, 252, np.random.default_rng(8))


def test_placebo_shifts_keep_the_signal_s_memory_before_the_wrap():
    """A shift s holds, on the first s days, the weights of n - s days later: that distance stays
    beyond the memory the signal reads, so that no placebo holds weights that read its own day."""
    offsets = stats.placebo_offsets(3000, 2000, 252, np.random.default_rng(8), forward=1262)
    assert offsets.min() >= 252 and offsets.max() <= 3000 - 1262 and offsets.max() > 3000 - 1300
    with pytest.raises(ValueError, match="memory"):
        stats.placebo_offsets(1514, 10, 252, np.random.default_rng(8), forward=1262)
    assert len(stats.placebo_offsets(1515, 10, 252, np.random.default_rng(8), forward=1262)) == 10


def test_decisions_close_in_time_are_one_episode():
    positions = pd.DataFrame(np.nan, index=range(60), columns=["A"])
    for day, weight in [(0, 1.0), (2, 0.5), (3, 0.7), (20, 0.0), (40, 1.0), (41, 0.9)]:
        positions.loc[day, "A"] = weight
    assert stats.decision_clusters(positions, gap=5) == 3


def test_decisions_are_grouped_within_five_sessions_unless_told_otherwise():
    positions = pd.DataFrame(np.nan, index=range(30), columns=["A"])
    for day, weight in [(0, 1.0), (7, 0.5), (14, 0.2)]:
        positions.loc[day, "A"] = weight
    assert stats.decision_clusters(positions) == stats.decision_clusters(positions, gap=5) == 3
    assert stats.decision_clusters(positions, gap=10) == 2


def test_a_strategy_that_changes_its_targets_every_week_decides_once_a_week():
    positions = pd.DataFrame(np.nan, index=range(100), columns=["A"])
    positions.iloc[::5, 0] = np.linspace(0.1, 0.9, 20)
    assert stats.decision_clusters(positions, gap=5) == 20
    daily = pd.DataFrame({"A": np.linspace(0.1, 0.9, 100)})
    assert stats.decision_clusters(daily, gap=5) == 20


def test_alpha_is_the_annual_intercept_over_the_benchmark():
    x = pd.Series(np.random.default_rng(9).normal(0, 0.01, 2000))
    y = 0.0002 + 1.5 * x
    assert stats.alpha(y, x) == pytest.approx(0.0002 * 252, rel=1e-9)


def test_a_strategy_that_is_its_benchmark_has_nothing_left_exactly():
    """Its alpha is zero, not the rounding of a beta computed near 1, whatever the series."""
    for seed in range(20):
        benchmark = pd.Series(np.random.default_rng(seed).normal(0.0004, 0.012, 700))
        assert (stats.hedged(benchmark.copy(), benchmark) == 0.0).all() and stats.alpha(benchmark.copy(), benchmark) == 0.0
        assert stats.alpha(benchmark + 1e-13, benchmark) == 0.0
    assert stats.alpha(benchmark + 1e-9, benchmark) != 0.0                 # a strategy that differs is judged
    assert stats.alpha(benchmark + 1e-11, benchmark) != 0.0
    assert stats.alpha(benchmark - 1e-6, benchmark) == pytest.approx(-252e-6, rel=1e-6)   # below it on every session
    once = benchmark.copy()
    once.iloc[300] += 1e-10                                                # on one session of 700
    assert stats.alpha(once, benchmark) != 0.0


def test_the_hedged_returns_hold_no_benchmark_and_average_to_the_alpha():
    rng = np.random.default_rng(10)
    benchmark = pd.Series(rng.normal(0.0003, 0.01, 2000))
    strategy = 0.0002 + 0.6 * benchmark + rng.normal(0, 0.005, 2000)
    left = stats.hedged(strategy, benchmark)
    assert np.cov(left, benchmark)[0, 1] == pytest.approx(0.0, abs=1e-12)
    assert left.mean() * 252 == pytest.approx(stats.alpha(strategy, benchmark), rel=1e-12)


# Pardo (2008) measures profits; the lab measures Sharpe ratios.
def test_walk_forward_efficiency_is_zero_when_the_choices_lost_in_sample():
    assert stats.walk_forward_efficiency(0.4, 0.8) == 0.5
    assert stats.walk_forward_efficiency(0.4, 0.0) == 0.0 and stats.walk_forward_efficiency(0.4, -0.2) == 0.0
