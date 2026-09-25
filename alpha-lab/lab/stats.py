"""The statistics the battery rests on, each with its reference on the line above it.

Sharpe ratios here are computed on returns above the Treasury-bill rate. A "daily" Sharpe ratio is
per session; an annual one multiplies it by the square root of 252, or by Lo's factor when the
returns are autocorrelated.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.spatial.distance import squareform
from scipy.stats import kurtosis, norm, skew

from lab.universe import TRADING_DAYS

PERIODS = TRADING_DAYS
EULER_GAMMA = 0.5772156649015329
LO_LAGS = 10          # autocorrelations used in Lo's factor; the ones beyond are taken as zero
NEAR_CLONE = 0.9      # two trials whose monthly bets correlate this much are one trial
SAME = 1e-12          # a daily return this close to the benchmark's is the benchmark's


def sharpe(excess: pd.Series, periods: int = PERIODS) -> float:
    """Annual Sharpe ratio of returns above the risk-free rate."""
    excess = excess.dropna()
    sd = excess.std(ddof=1)
    return float(excess.mean() / sd * np.sqrt(periods)) if sd > 0 else 0.0


# Lo, A. W. (2002). The statistics of Sharpe ratios. Financial Analysts Journal, 58(4), 36-52.
def lo_factor(excess: pd.Series, q: int = PERIODS, lags: int = LO_LAGS) -> float:
    """eta(q) = q / sqrt(q + 2 sum_{k<q} (q - k) rho_k): what replaces sqrt(q) when returns are
    serially correlated. The first `lags` autocorrelations are estimated; the others are zero."""
    x = excess.dropna().to_numpy()
    rho = [np.corrcoef(x[:-k], x[k:])[0, 1] for k in range(1, min(lags, q - 1) + 1)]
    inner = q + 2 * sum((q - k) * r for k, r in enumerate(rho, start=1))
    return float(q / np.sqrt(inner)) if inner > 0 else float(np.sqrt(q))


def lo_sharpe(excess: pd.Series) -> float:
    """Annual Sharpe ratio adjusted for autocorrelation (Lo 2002)."""
    excess = excess.dropna()
    sd = excess.std(ddof=1)
    return float(excess.mean() / sd * lo_factor(excess)) if sd > 0 else 0.0


# Bailey, D. H., & Lopez de Prado, M. (2012). The Sharpe ratio efficient frontier.
# Journal of Risk, 15(2), 3-44.
def psr(sr: float, n: int, skewness: float, kurt: float, benchmark: float = 0.0) -> float:
    """Probability that the true daily Sharpe ratio exceeds `benchmark`, given the estimate `sr`
    from n daily observations with that skewness and (non-excess) kurtosis."""
    denominator = 1 - skewness * sr + (kurt - 1) / 4 * sr ** 2
    if n < 2 or not denominator > 0:          # a constant series has no moments: no evidence at all
        return 0.0
    return float(norm.cdf((sr - benchmark) * np.sqrt(n - 1) / np.sqrt(denominator)))


def moments(excess: pd.Series) -> tuple[int, float, float]:
    x = excess.dropna().to_numpy()
    return len(x), float(skew(x)), float(kurtosis(x, fisher=False))


def adjusted_psr(excess: pd.Series, benchmark: float = 0.0) -> float:
    """PSR of the autocorrelation-adjusted Sharpe ratio: Lo's annual ratio brought back to a day."""
    n, s, k = moments(excess)
    return psr(lo_sharpe(excess) / np.sqrt(PERIODS), n, s, k, benchmark)


# Bailey, D. H., & Lopez de Prado, M. (2014). The deflated Sharpe ratio: Correcting for selection
# bias, backtest overfitting, and non-normality. Journal of Portfolio Management, 40(5), 94-107.
def expected_max_sharpe(trials: int, variance: float) -> float:
    """Expected maximum daily Sharpe ratio of `trials` independent trials of true ratio zero whose
    estimates have this variance: the bar the deflated Sharpe ratio sets."""
    if trials <= 1:
        return 0.0
    z = (1 - EULER_GAMMA) * norm.ppf(1 - 1 / trials) + EULER_GAMMA * norm.ppf(1 - 1 / (trials * np.e))
    return float(np.sqrt(variance) * z)


def dsr(excess: pd.Series, trials: int, variance: float) -> float:
    """Deflated Sharpe ratio: the adjusted PSR against the best of `trials` tries by luck."""
    return adjusted_psr(excess, benchmark=expected_max_sharpe(trials, variance))


def near_clone_clusters(returns: pd.DataFrame, threshold: float = NEAR_CLONE) -> np.ndarray:
    """The cluster of each trial (column of monthly returns): complete linkage on 1 - correlation,
    cut so that every pair inside a cluster correlates at `threshold` or more. Pairs with fewer than
    24 months in common are never clones."""
    if returns.shape[1] <= 1:
        return np.ones(returns.shape[1], dtype=int)
    corr = returns.corr(min_periods=24).fillna(0.0).to_numpy()
    distance = np.clip(1 - corr, 0, 2)
    np.fill_diagonal(distance, 0)
    tree = linkage(squareform(distance, checks=False), method="complete")
    return fcluster(tree, t=1 - threshold, criterion="distance")


# Politis, D. N., & Romano, J. P. (1994). The stationary bootstrap. Journal of the American
# Statistical Association, 89(428), 1303-1313.
def stationary_bootstrap(n: int, length: int, mean_block: float, draws: int, rng) -> np.ndarray:
    """`draws` index paths of `length` into a series of n: blocks of geometric length, wrapping."""
    start = rng.integers(0, n, size=(draws, length))
    new_block = rng.random((draws, length)) < 1 / mean_block
    new_block[:, 0] = True
    paths = np.empty((draws, length), dtype=np.int64)
    paths[:, 0] = start[:, 0]
    for t in range(1, length):
        paths[:, t] = np.where(new_block[:, t], start[:, t], (paths[:, t - 1] + 1) % n)
    return paths


def placebo_offsets(n: int, draws: int, minimum: int, rng) -> np.ndarray:
    """Random circular shifts of at least `minimum` sessions each way, for the exposure-matched
    placebo: the strategy's own positions, moved in time."""
    if n <= 2 * minimum:
        raise ValueError("the sample is too short for shifts of at least a year each way")
    return rng.integers(minimum, n - minimum + 1, size=draws)


def decision_clusters(positions: pd.DataFrame, gap: int = 5) -> int:
    """Decisions counted as independent episodes: a change of target within `gap` sessions of the
    first change of an episode belongs to that episode, so a strategy that changes its targets
    every day or every week counts one decision a week at most."""
    held = positions.ffill().fillna(0.0)
    changed = held.diff().abs().sum(axis=1).gt(1e-9)
    changed.iloc[0] = bool(held.iloc[0].abs().sum() > 1e-9)
    episodes, start = 0, None
    for day in np.flatnonzero(changed.to_numpy()):
        if start is None or day - start >= gap:
            episodes, start = episodes + 1, day
    return episodes


def hedged(excess: pd.Series, benchmark_excess: pd.Series) -> pd.Series:
    """The strategy's excess returns less beta times the benchmark's, beta from the regression of
    the one on the other: what is left once the benchmark exposure is taken out. Their mean is the
    alpha, their Sharpe ratio the appraisal ratio. A strategy that is its benchmark, to `SAME` on
    every session, has nothing left: zeros, not the rounding of a beta computed near 1, whose sign
    would be chance."""
    both = pd.concat([excess, benchmark_excess], axis=1).dropna()
    if len(both) < 3:
        return pd.Series(0.0, index=both.index)
    y, x = both.iloc[:, 0], both.iloc[:, 1]
    if (y - x).abs().max() <= SAME:
        return pd.Series(0.0, index=both.index)
    beta = float(np.cov(x, y, ddof=1)[0, 1] / np.var(x, ddof=1)) if np.var(x) > 0 else 0.0
    return y - beta * x


def alpha(excess: pd.Series, benchmark_excess: pd.Series, periods: int = PERIODS) -> float:
    """Annual intercept of the regression of the strategy's excess returns on the benchmark's."""
    left = hedged(excess, benchmark_excess)
    return float(left.mean() * periods) if len(left) else 0.0


# Pardo, R. (2008). The evaluation and optimization of trading strategies (2nd ed.). Wiley.
def walk_forward_efficiency(out_of_sample: float, in_sample: float) -> float:
    """Out-of-sample performance of the walk-forward choices over their in-sample performance, both
    measured by Sharpe ratios here, where Pardo measures profits: the variants of a card differ in
    risk as much as in return. A choice that lost in-sample has no efficiency: 0."""
    return float(out_of_sample / in_sample) if in_sample > 0 else 0.0
