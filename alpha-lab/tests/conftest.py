"""Fixtures: a small synthetic snapshot, frozen by the lab's own code, so that tests need no network."""
import json

import numpy as np
import pandas as pd
import pytest

from lab import data

SYNTHETIC = ("AAA", "BBB", "CCC", "COIN")  # COIN trades every day and is lagged, like bitcoin


def bars(close, index):
    return pd.DataFrame({"Open": close, "High": close, "Low": close, "Close": close, "Volume": 1e6}, index=index)


@pytest.fixture
def snapshot(tmp_path):
    rng = np.random.default_rng(0)
    days = pd.bdate_range("2019-01-01", "2020-12-31")
    raw = {}
    for ticker in ("AAA", "BBB", "CCC"):
        index = days if ticker != "CCC" else days[days >= "2019-07-01"]
        raw[ticker] = bars(100 * np.exp(np.cumsum(rng.normal(0, 0.01, len(index)))), index)
    every_day = pd.date_range("2019-01-01", "2020-12-31")
    raw["COIN"] = bars(5000 * np.exp(np.cumsum(rng.normal(0, 0.03, len(every_day)))), every_day)
    raw["^IRX"] = bars(np.full(len(days), 2.0), days)
    data.freeze(raw, "synthetic", tmp_path, "2020-12-31", tickers=SYNTHETIC, lagged=("COIN",))
    return tmp_path


def _frozen() -> bool:
    manifest = data.DATA / "manifest.json"
    return manifest.exists() and (data.DATA / json.loads(manifest.read_text())["snapshot"]).is_dir()


real_snapshot = pytest.mark.skipif(not _frozen(), reason="the snapshot the manifest names is not on this machine")


EIGHT = ("S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8")
CLUSTERS = {"S1": "a", "S2": "a", "S3": "a", "S4": "b", "S5": "b", "S6": "b", "S7": "c", "S8": "c",
            "COIN": "crypto"}


def synthetic_market(seed: int, tickers=EIGHT, beta: float = 0.0, rho: float = 0.95, coin: bool = False,
                     holdout_beta: float | None = None):
    """21 years of daily bars in which a persistent signal u predicts returns with strength beta: the
    return into t rewards u of t-2, which a strategy reads at the close of t-1. From 2023 on, the
    strength is `holdout_beta` when it is given. With `coin`, a lagged asset traded every day is
    added. Returns the market and the signal."""
    rng = np.random.default_rng(seed)
    days = pd.bdate_range("2005-01-03", "2025-12-31")
    n, k = len(days), len(tickers)
    u, shocks = np.zeros((n, k)), rng.normal(size=(n, k))
    for t in range(1, n):
        u[t] = rho * u[t - 1] + np.sqrt(1 - rho ** 2) * shocks[t]
    returns = rng.normal(0.0002, 0.01, (n, k))
    strength = np.where(days >= "2023-01-01", beta if holdout_beta is None else holdout_beta, beta)
    returns[2:] += strength[2:, None] * 0.01 * u[:-2]
    raw = {t: bars(100 * np.cumprod(1 + returns[:, j]), days) for j, t in enumerate(tickers)}
    if coin:
        every_day = pd.date_range(days[0], days[-1])
        raw["COIN"] = bars(5000 * np.exp(np.cumsum(rng.normal(0, 0.03, len(every_day)))), every_day)
    irx = bars(np.full(n, 2.0), days)
    return data.assemble(raw, irx, ("COIN",) if coin else ()), pd.DataFrame(u, index=days, columns=tickers)


def signal_strategy(signal):
    """Weights in proportion to the positive part of the signal's average over `span` sessions, read
    up to t-1 and set every `every` sessions."""
    def positions(market, span=10, every=5):
        s = signal.reindex(market.prices.index).reindex(columns=market.prices.columns)
        score = s.ewm(span=span).mean().shift(1).clip(lower=0).fillna(0.0)
        total = score.sum(axis=1)
        weights = score.div(total.where(total > 0), axis=0).fillna(0.0)
        out = weights * np.nan
        out.iloc[::every] = weights.iloc[::every]
        return out
    return positions
