"""The snapshot, the calendar, the universe."""
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from lab import data
from lab.universe import CHF_RATES, CLUSTERS, TICKERS, UNIVERSE
from tests.conftest import SYNTHETIC, bars, real_snapshot


def test_one_call_returns_prices_mask_and_rate(snapshot):
    market = data.load("2020-01-01", "2020-06-30", root=snapshot)
    assert list(market.prices.columns) == list(SYNTHETIC)
    assert market.prices.index.equals(market.tradable.index)
    assert market.prices.index.equals(market.rf.index)
    assert market.tradable.dtypes.eq(bool).all()
    assert market.rf.eq(2.0 / 100 / 252).all()  # cash earns the Treasury-bill rate, per session


def test_asof_never_returns_a_later_bar(snapshot):
    market = data.load(root=snapshot)
    rng = np.random.default_rng(1)
    for when in rng.choice(market.prices.index, 50):
        known = market.asof(when)
        for frame in (known.prices, known.tradable, known.rf, known.signal_prices):
            assert frame.index.max() <= when


def test_an_asset_enters_when_it_starts_trading(snapshot):
    tradable = data.load(root=snapshot).tradable
    assert not tradable.loc[:"2019-06-28", "CCC"].any()
    assert tradable.loc["2019-07-01":, "CCC"].all()


def test_benchmark_is_equal_weight_of_the_tradable_assets(snapshot):
    tradable = data.load(root=snapshot).tradable
    weights = data.benchmark_weights(tradable)
    assert np.allclose(weights.sum(axis=1), 1.0)
    assert (weights.to_numpy()[~tradable.to_numpy()] == 0).all()
    assert np.allclose(weights.loc["2019-03-01"][["AAA", "BBB", "COIN"]], 1 / 3)
    assert np.allclose(weights.loc["2020-03-02"], 1 / 4)


def test_bitcoin_signal_is_the_close_of_the_day_before(snapshot):
    market = data.load(root=snapshot)
    raw = data.read(snapshot / "2020-12-31" / "COIN.csv")["Close"]
    monday = pd.Timestamp("2020-03-09")
    assert market.signal_prices.loc[monday, "COIN"] == raw.loc["2020-03-08"]  # Sunday's close
    assert market.prices.loc[monday, "COIN"] == raw.loc["2020-03-09"]


def test_volumes_are_read_as_the_closes_are():
    days = pd.bdate_range("2020-03-02", "2020-03-13")
    every_day = pd.date_range("2020-03-01", "2020-03-13")
    etf = pd.DataFrame({"Close": np.arange(len(days)) + 100.0, "Volume": np.arange(len(days)) * 10.0 + 1}, index=days)
    coin = pd.DataFrame({"Close": np.arange(len(every_day)) + 5000.0, "Volume": np.arange(len(every_day)) + 0.5},
                        index=every_day)
    irx = pd.DataFrame({"Close": np.full(len(days), 2.0)}, index=days)
    market = data.assemble({"ETF": etf, "COIN": coin}, irx, ("COIN",))
    assert market.signal_volumes.index.equals(market.prices.index)
    assert market.signal_volumes.loc["2020-03-05", "ETF"] == etf.loc["2020-03-05", "Volume"]
    monday = pd.Timestamp("2020-03-09")
    assert market.signal_volumes.loc[monday, "COIN"] == coin.loc["2020-03-08", "Volume"]   # Sunday's, as its close
    assert market.signal_volumes.loc["2020-03-03", "COIN"] == coin.loc["2020-03-02", "Volume"]
    cut = market.window("2020-03-09", "2020-03-10")
    assert cut.signal_volumes.index.equals(cut.prices.index)
    late = data.traded_from(market, {"ETF": "2020-03-06"})
    assert late.signal_volumes.loc[:"2020-03-05", "ETF"].isna().all()
    assert late.signal_volumes.loc["2020-03-06", "ETF"] == etf.loc["2020-03-06", "Volume"]
    assert data.assemble({"ETF": etf[["Close"]]}, irx, ()).signal_volumes is None   # bars with no volume


def test_exchange_rates_are_read_as_the_close_of_the_day_before():
    days = pd.bdate_range("2020-03-02", "2020-03-31")
    etf = pd.DataFrame({"Close": np.arange(len(days)) + 100.0}, index=days)
    irx = pd.DataFrame({"Close": np.full(len(days), 2.0)}, index=days)
    fx_days = days.delete([5, 12, 13, 14, 15, 16, 17, 18, 19])     # a holiday, then eight days without a close
    usd = pd.DataFrame({"Close": np.arange(len(fx_days)) * 0.001 + 0.95}, index=fx_days)
    market = data.assemble({"ETF": etf}, irx, (), {"USDCHF=X": usd})
    rates = market.signal_rates
    assert list(rates.columns) == ["USDCHF"] and rates.index.equals(market.prices.index)
    assert np.isnan(rates.loc["2020-03-02", "USDCHF"])                      # no close before the first session
    assert rates.loc["2020-03-03", "USDCHF"] == usd.loc["2020-03-02", "Close"]
    assert rates.loc["2020-03-09", "USDCHF"] == usd.loc["2020-03-06", "Close"]   # Monday reads Friday's
    assert rates.loc["2020-03-10", "USDCHF"] == usd.loc["2020-03-06", "Close"]   # no close on the 9th: the one before
    assert np.isnan(rates.loc["2020-03-27", "USDCHF"])                      # the last close over seven days old
    assert data.assemble({"ETF": etf}, irx, ()).signal_rates is None
    cut = market.window("2020-03-09", "2020-03-10")
    assert cut.signal_rates.index.equals(cut.prices.index)
    late = data.traded_from(market, {"ETF": "2020-03-06"})
    assert late.signal_rates.equals(market.signal_rates)                    # a rate is no asset: nothing is cut


def test_integer_volumes_come_out_as_floats_and_outliers_are_listed():
    days = pd.bdate_range("2020-03-02", "2020-04-30")
    every_day = pd.date_range("2020-02-01", "2020-04-30")                  # the coin starts first
    volume = np.full(len(days), 1_000_000, dtype=np.int64)
    volume[30] = 1_200                                                     # a bad print
    etf = pd.DataFrame({"Close": np.linspace(100, 110, len(days)), "Volume": volume}, index=days)
    coin = pd.DataFrame({"Close": np.linspace(5000, 6000, len(every_day)),
                         "Volume": np.arange(len(every_day), dtype=np.int64) + 10}, index=every_day)
    irx = pd.DataFrame({"Close": np.full(len(days), 2.0)}, index=days)
    market = data.assemble({"ETF": etf, "COIN": coin}, irx, ("COIN",))
    assert (market.signal_volumes.dtypes == float).all()
    found = data.volume_findings(market)
    assert [(f["ticker"], f["check"], f["date"]) for f in found] == [("ETF", "volume outlier", str(days[30].date()))]


def test_the_snapshot_s_volumes_are_those_of_its_files(snapshot):
    market = data.load(root=snapshot)
    assert list(market.signal_volumes.columns) == list(SYNTHETIC)
    assert market.signal_volumes.index.equals(market.prices.index)
    assert market.signal_volumes["CCC"].isna().equals(market.prices["CCC"].isna())
    assert market.signal_volumes.loc["2020-03-09", "AAA"] == data.read(snapshot / "2020-12-31" / "AAA.csv").loc[
        "2020-03-09", "Volume"]


def test_a_weekend_move_lands_on_monday(snapshot):
    market = data.load(root=snapshot)
    raw = data.read(snapshot / "2020-12-31" / "COIN.csv")["Close"]
    monday_return = market.prices["COIN"].pct_change().loc["2020-03-09"]
    assert monday_return == pytest.approx(raw.loc["2020-03-09"] / raw.loc["2020-03-06"] - 1)


def test_an_altered_file_is_refused(snapshot):
    path = snapshot / "2020-12-31" / "AAA.csv"
    path.write_text(path.read_text().replace("\n2020-06-01,", "\n2020-06-01,1", 1))
    with pytest.raises(ValueError, match="hash"):
        data.load(root=snapshot)


def closes(days, moves=None):
    returns = pd.Series(0.001, index=days)
    for when, move in (moves or {}).items():
        returns.loc[when] = move
    return pd.DataFrame({"Close": 100 * (1 + returns).cumprod()})


def findings(raw, lagged=()):
    return {(f["ticker"], f["check"], f["date"], f["value"]) for f in data.integrity(raw, lagged)}


def test_a_gap_is_a_finding_from_its_fourth_missing_session():
    days = pd.bdate_range("2021-01-04", periods=60)
    full = closes(days)
    three, four = full.drop(days[20:23]), full.drop(days[30:34])
    found = findings({"REF": full, "THREE": three, "FOUR": four})
    assert not [f for f in found if f[0] == "THREE"]
    assert ("FOUR", "gap", str(days[30].date()), 4) in found


def test_bitcoin_gaps_count_missing_calendar_days():
    days = pd.bdate_range("2021-01-04", periods=60)
    every_day = pd.date_range("2021-01-04", periods=80)
    coin = closes(every_day)
    three, four = coin.drop(every_day[20:23]), coin.drop(every_day[40:44])
    found = findings({"REF": closes(days), "THREE": three, "FOUR": four}, lagged=("THREE", "FOUR"))
    assert not [f for f in found if f[0] == "THREE"]
    assert ("FOUR", "gap", str(every_day[40].date()), 4) in found


def test_moves_beyond_the_limits_are_findings():
    days = pd.bdate_range("2021-01-04", periods=60)
    etf = closes(days, {days[10]: 0.149, days[20]: 0.151})
    coin = closes(days, {days[10]: 0.39, days[20]: -0.41})
    moves = {(f[0], f[2]) for f in findings({"ETF": etf, "COIN": coin}, lagged=("COIN",)) if f[1] == "large move"}
    assert moves == {("ETF", str(days[20].date())), ("COIN", str(days[20].date()))}


def test_three_zero_returns_in_a_row_are_a_finding():
    days = pd.bdate_range("2021-01-04", periods=60)
    flat = closes(days, {days[10]: 0.0, days[11]: 0.0, days[20]: 0.0, days[21]: 0.0, days[22]: 0.0,
                         days[40]: 0.0, days[41]: 0.0, days[42]: 0.0, days[43]: 0.0, days[44]: 0.0})
    zero = {(f[2], f[3]) for f in findings({"ETF": flat}) if f[1] == "zero returns"}
    assert zero == {(str(days[20].date()), 3), (str(days[40].date()), 5)}


def test_cash_earns_the_rate_of_the_session_before_carried_five_sessions_at_most():
    days = pd.bdate_range("2021-01-04", periods=40)
    irx = pd.Series(2.0, index=days)
    irx.iloc[20:] = 4.0
    two, six = irx.drop(days[5:7]), irx.drop(days[10:16])
    rf = data.assemble({"ETF": closes(days)}, pd.DataFrame({"Close": irx}), ()).rf
    assert rf.iloc[20] == pytest.approx(2.0 / 100 / 252) and rf.iloc[21] == pytest.approx(4.0 / 100 / 252)
    assert data.assemble({"ETF": closes(days)}, pd.DataFrame({"Close": two}), ()).rf.iloc[1:].notna().all()
    holes = data.assemble({"ETF": closes(days)}, pd.DataFrame({"Close": six}), ()).rf.iloc[1:]
    assert holes.isna().sum() == 1 and holes.isna().idxmax() == days[16]  # the sixth missing session, a day on


def test_cross_check_confirms_a_source_that_differs_only_on_dividend_days():
    days = pd.bdate_range("2022-01-03", periods=400)
    ours = pd.Series(100 * np.cumprod(np.full(400, 1.0004)), index=days)
    price_only = ours.copy()
    for k in range(60, 400, 63):               # four dividends a year, of 0.4%, not added back
        price_only.iloc[k:] *= 0.996
    report = data.cross_check(ours, price_only)
    assert report["confirmed"] and len(report["days_over_10bps"]) == 6
    bad = ours.copy()
    bad.iloc[200] *= 1.03                      # a bad print
    assert not data.cross_check(ours, bad)["confirmed"]


def test_the_universe_has_its_clusters():
    assert len(TICKERS) == len(set(TICKERS)) == 23
    assert CLUSTERS == ("sectors", "broad", "metals", "commodities", "crypto", "bonds")
    assert sum(asset.cluster == "sectors" for asset in UNIVERSE) == 11
    assert [asset.ticker for asset in UNIVERSE if asset.cluster == "bonds"] == ["SHY", "IEF", "TLT"]
    assert CHF_RATES == ("USDCHF=X", "EURCHF=X")


@real_snapshot
def test_a_known_week_loads_to_the_right_shape():
    market = data.load("2020-04-06", "2020-04-13")   # Good Friday closed, and bitcoin's weekend is not a session
    assert market.prices.shape == (5, 23)
    assert market.tradable.all().all()
    assert market.rf.notna().all()


@real_snapshot
def test_the_snapshot_agrees_with_the_universe():
    assert data.check() == 0
    tradable = data.load().tradable
    for asset in UNIVERSE:
        assert str(tradable[asset.ticker].idxmax().date()) == asset.first_session
    assert not tradable.loc[:"2016-09-16", "XLRE"].any()


@real_snapshot
def test_bitcoin_after_a_midweek_holiday_is_read_from_the_day_before():
    manifest = json.loads((data.DATA / "manifest.json").read_text())
    raw = data.read(data.DATA / manifest["snapshot"] / "BTC-USD.csv")["Close"]
    market = data.load("2019-07-01", "2019-07-10")
    assert pd.Timestamp("2019-07-04") not in market.prices.index
    assert market.signal_prices.loc["2019-07-05", "BTC-USD"] == raw.loc["2019-07-04"]
    assert market.prices["BTC-USD"].pct_change().loc["2019-07-05"] == pytest.approx(
        raw.loc["2019-07-05"] / raw.loc["2019-07-03"] - 1)


def test_a_cross_check_on_closes_saved_by_hand_lands_in_the_manifest(snapshot, tmp_path):
    market = data.load(root=snapshot)
    theirs = market.prices["AAA"].dropna() * 1.0001          # a source that differs by a constant factor
    folder = tmp_path / "stooq"
    folder.mkdir()
    theirs.rename("Close").rename_axis("Date").to_frame().to_csv(folder / "aaa.csv")
    checked = data.cross_check_folder(folder, root=snapshot)
    assert checked["status"] == "run" and checked["tickers"]["AAA"]["confirmed"]
    assert json.loads((snapshot / "manifest.json").read_text())["cross_check"]["tickers"]["AAA"]["days"] > 400
    (folder / "zzz_us_d.csv").write_text("Date,Close\n2020-01-02,1\n")
    with pytest.raises(ValueError, match="zzz_us_d.csv"):
        data.cross_check_folder(folder, root=snapshot)


def test_an_asset_the_cross_check_did_not_confirm_waits_for_its_days_to_be_examined():
    manifest = {"cross_check": {"status": "run", "checked": "2026-09-25",
                                "tickers": {"AAA": {"confirmed": True}, "BBB": {"confirmed": False}}}}
    assert data.unexamined(manifest) == ["BBB"]
    manifest["cross_check_review"] = {"checked": "2026-09-24", "tickers": {"BBB": "dividend days"}}
    assert data.unexamined(manifest) == ["BBB"]                # a review of an earlier cross-check
    manifest["cross_check_review"]["checked"] = "2026-09-25"
    assert data.unexamined(manifest) == []
    assert data.unexamined({"cross_check": {"status": "not run"}}) == []


def test_files_saved_from_stooq_name_their_asset():
    assert [data.stooq_ticker(s) for s in ("spy", "spy_us_d", "spy.us", "btcusd_d", "XLF")] == \
        ["SPY", "SPY", "SPY", "BTC-USD", "XLF"]


def test_a_second_snapshot_is_refused(snapshot):
    with pytest.raises(RuntimeError, match="already frozen"):
        data.download(root=snapshot)


def later(tickers, days=pd.bdate_range("2019-01-01", "2020-12-31")):
    rng = np.random.default_rng(5)
    return {t: bars(100 * np.exp(np.cumsum(rng.normal(0, 0.005, len(days)))), days) for t in tickers}


def test_an_addition_is_frozen_beside_the_snapshot_which_does_not_change(snapshot):
    before = json.loads((snapshot / "manifest.json").read_text())
    market = data.load(root=snapshot)
    raw = later(("DDD", "FXX"))
    data.add(raw, "synthetic", snapshot, "2021-01-05", tickers=["DDD"], rates=["FXX"])
    manifest = json.loads((snapshot / "manifest.json").read_text())
    assert {k: manifest[k] for k in before} == before                 # what was frozen is listed as it was
    addition = manifest["additions"][0]
    assert (addition["snapshot"], addition["tickers"], addition["rates"]) == ("2021-01-05", ["DDD"], ["FXX"])
    assert set(addition["files"]) == {"DDD.csv", "FXX.csv"} and (snapshot / "2021-01-05" / "DDD.csv").exists()
    grown = data.load(root=snapshot)
    assert list(grown.prices.columns) == [*SYNTHETIC, "DDD"]            # a rate is no asset
    pd.testing.assert_frame_equal(grown.prices[list(SYNTHETIC)], market.prices)
    pd.testing.assert_series_equal(grown.rf, market.rf)
    assert grown.prices["DDD"].iloc[-1] == pytest.approx(raw["DDD"]["Close"].iloc[-1])
    assert data.holdings(manifest)["FXX"] == "2021-01-05" and data.holdings(manifest)["AAA"] == "2020-12-31"


def test_a_series_already_frozen_is_never_added_again(snapshot):
    with pytest.raises(RuntimeError, match="AAA: already frozen in data/2020-12-31/"):
        data.add(later(("AAA",)), "synthetic", snapshot, "2021-01-05", tickers=["AAA"])
    data.add(later(("DDD",)), "synthetic", snapshot, "2021-01-05", tickers=["DDD"])
    with pytest.raises(RuntimeError, match="DDD: already frozen in data/2021-01-05/"):
        data.add(later(("DDD",)), "synthetic", snapshot, "2021-01-06", tickers=["DDD"])


def test_a_missing_file_is_refused_in_one_line(snapshot, capsys):
    (snapshot / "2020-12-31" / "BBB.csv").unlink()
    with pytest.raises(RuntimeError, match="BBB.csv: not in data/2020-12-31/"):
        data.load(root=snapshot)
    assert data.main(["check"], root=snapshot) == 1
    said = capsys.readouterr().err.strip().splitlines()
    assert len(said) == 1 and said[0].startswith("refused: BBB.csv: not in data/2020-12-31/")


def test_an_altered_or_missing_addition_is_refused(snapshot):
    data.add(later(("DDD",)), "synthetic", snapshot, "2021-01-05", tickers=["DDD"])
    path = snapshot / "2021-01-05" / "DDD.csv"
    text = path.read_text()
    path.write_text(text.replace("\n2020-06-01,", "\n2020-06-01,1", 1))
    with pytest.raises(ValueError, match="DDD.csv: its hash differs"):
        data.load(root=snapshot)
    path.write_text(text)
    (snapshot / "2021-01-05").rename(snapshot / "elsewhere")
    with pytest.raises(RuntimeError, match="the snapshot 2021-01-05 is not in data/2021-01-05/"):
        data.load(root=snapshot)


def test_extend_fetches_only_what_no_folder_holds(snapshot, monkeypatch):
    fetched = []

    def fetch(yf, tickers):
        fetched.append(tuple(tickers))
        return later(tickers)

    monkeypatch.setattr(data, "fetch", fetch)
    monkeypatch.setattr(data, "TICKERS", (*SYNTHETIC, "DDD"))
    monkeypatch.setattr(data, "CHF_RATES", ("FXX",))
    manifest = data.extend(root=snapshot, snapshot="2021-01-05")
    assert fetched == [("DDD", "FXX")]
    assert (manifest["additions"][0]["tickers"], manifest["additions"][0]["rates"]) == (["DDD"], ["FXX"])
    with pytest.raises(RuntimeError, match="already frozen"):
        data.extend(root=snapshot, snapshot="2021-01-06")
    assert fetched == [("DDD", "FXX")]


def traded(seed=3, start="2020-01-02", sessions=320, halves=0.2, level=40.0, spread=0.3, moves=0.01):
    """Bars as a fund trades: open, high, low and close in whole cents, a share `halves` of the
    highs at the midpoint of a one-cent spread; `spread` bounds the day's range beyond the open and
    the close."""
    rng = np.random.default_rng(seed)
    days = pd.bdate_range(start, periods=sessions)
    close = np.round(level * np.exp(np.cumsum(rng.normal(0, moves, sessions))), 2)
    open_ = np.round(close * (1 + rng.normal(0, moves * 0.3, sessions)), 2)
    high = np.maximum(open_, close) + np.round(rng.uniform(0, spread, sessions), 2)
    low = np.minimum(open_, close) - np.round(rng.uniform(0, spread, sessions), 2)
    half = rng.random(sessions) < halves
    high = np.where(half, high + 0.005, high)
    return pd.DataFrame({"Open": open_, "High": high, "Low": low, "Close": close, "Volume": 1e6}, index=days)


def adjusted(raw, paid, splits=(), later=1.0, rounded=True):
    """The bars as Yahoo adjusts them: before each ex-date, scaled down by the cash over the close
    before it; before each split, divided by its ratio; all of them by `later`, what was paid after
    the last bar; kept to about seven digits, off by up to 3e-7 of the price, as Yahoo's are (the
    snapshot's bars lie a median 1.3e-7 of the price off their steps, 5e-7 at the 99th percentile)."""
    rng = np.random.default_rng(0)
    factor = pd.Series(later, index=raw.index)
    for day, cash in paid.items():
        before = raw.index < pd.Timestamp(day)
        factor[before] *= 1 - cash / raw["Close"][before].iloc[-1]
    for day, ratio in dict(splits).items():
        factor[raw.index < pd.Timestamp(day)] /= ratio
    out = raw.copy()
    for field in ("Open", "High", "Low", "Close"):
        values = raw[field] * factor
        noise = 1 + rng.uniform(-3e-7, 3e-7, len(values))
        out[field] = (values * noise).astype(np.float32).astype(float) if rounded else values
    return out


def fraction(raw, day, cash, late=3):
    """Where and what the reading gives of the cash paid on `day`: the session the bars as they
    stood confirm it on, its fourth bar, `late` sessions after it when every bar is on its steps;
    and the cash over the traded close before the ex-date."""
    ex = raw.index.get_loc(pd.Timestamp(day))
    return raw.index[ex + late], cash / raw["Close"].iloc[ex - 1]


def read_at(read, when, late=2):
    """The one distribution read from `when` to `late` sessions after it, nothing in the eight
    sessions before: a bar a hair off its steps may confirm it a session or two later, never
    earlier."""
    at = read.index.get_loc(when)
    assert read.iloc[max(0, at - 8):at].eq(0.0).all()
    shown = read.iloc[at:at + late + 1]
    shown = shown[shown != 0]
    assert len(shown) == 1
    return shown.iloc[0]


QUARTERLY = {"2020-02-20": 0.18, "2020-05-21": 0.21, "2020-08-20": 0.25, "2020-11-19": 0.01, "2021-02-18": 0.3}


def test_a_distribution_is_read_when_the_bars_confirm_it_and_never_before():
    raw = traded()
    read = data.distributions_of(adjusted(raw, QUARTERLY, later=0.99))
    for day, cash in QUARTERLY.items():
        when, value = fraction(raw, day, cash)
        expected = value if cash >= data.LEAST_STEPS * data.HALF else 0.0
        assert read[when] == pytest.approx(expected, rel=1e-4)
        assert read[raw.index[raw.index < when]].iloc[-8:].eq(0.0).all()   # nothing before it
    assert (read > 0).sum() == 4                                     # a cent is not told from a misreading
    assert read.index.equals(raw.index) and read.notna().all()


def test_a_high_priced_fund_is_read_through_the_rounding():
    """At $500, Yahoo's seven digits leave the bars a few hundredths of a cent off their steps."""
    raw = traded(seed=5, level=500.0, spread=2.0)
    paid = {"2020-03-19": 1.4, "2020-06-18": 1.6, "2020-09-17": 1.5, "2020-12-17": 1.8}
    read = data.distributions_of(adjusted(raw, paid, later=0.995))
    for day, cash in paid.items():
        when, value = fraction(raw, day, cash)
        assert read_at(read, when) == pytest.approx(value, abs=2 * data.HALF / 500)   # two half-cent steps
    assert (read > 0).sum() == 4


def test_a_fund_that_often_trades_at_the_half_cent_is_read():
    raw = traded(halves=0.8)
    paid = {d: c for d, c in QUARTERLY.items() if c > 0.1}
    read = data.distributions_of(adjusted(raw, paid))
    for day, cash in paid.items():
        when, value = fraction(raw, day, cash)
        assert read[when] == pytest.approx(value, rel=1e-4)
    assert (read > 0).sum() == 4 and read.notna().all()


def test_a_fund_that_barely_moves_is_never_read_before_its_ex_date():
    """A short bond fund's day ranges over a few cents, so that the bars around an ex-date may fit
    both factors: the reading is placed on the first bar only the later one fits, confirmed three
    bars later, or left unread."""
    raw = traded(seed=11, level=85.0, spread=0.02, moves=0.0005, sessions=400)
    months = pd.bdate_range("2020-02-01", periods=400, freq="BMS")[:18]
    paid = {day: 0.2 + 0.01 * k for k, day in enumerate(months)}
    read = data.distributions_of(adjusted(raw, paid))
    for day, cash in paid.items():
        start = raw.index.get_loc(day)
        assert read.iloc[start - 10:start + 3].fillna(0.0).eq(0.0).all()   # nothing before its confirmation
        shown = read.iloc[start + 3:start + 15]
        shown = shown[shown > 0]
        if len(shown):
            assert len(shown) == 1
            assert shown.iloc[0] == pytest.approx(cash / raw["Close"].iloc[start - 1], abs=0.03 / 85)
    assert (read > 0).sum() >= 12


def test_a_distribution_on_a_sub_cent_day_is_read_a_day_later():
    raw = traded()
    day = pd.Timestamp("2020-05-21")
    raw.loc[day, "Close"] += 0.0013                                  # off the steps
    read = data.distributions_of(adjusted(raw, {day: 0.21}))
    when, value = fraction(raw, day, 0.21, late=4)
    assert read[when] == pytest.approx(value, rel=1e-4)
    assert (read > 0).sum() == 1


def test_a_split_is_no_distribution():
    """A split the steps show: the shares before it traded at three times the price, a cent over."""
    raw = traded(sessions=260)
    split = pd.Timestamp("2020-07-01")
    before = raw.index < split
    raw.loc[before, ["Open", "High", "Low", "Close"]] = raw.loc[before, ["Open", "High", "Low", "Close"]] * 3 + 0.01
    paid = {"2020-03-19": 0.6, "2020-09-17": 0.2}
    read = data.distributions_of(adjusted(raw, paid, splits={split: 3}))
    assert read.loc[split:split + pd.Timedelta(days=10)].eq(0.0).all()
    for day, cash in paid.items():
        when, value = fraction(raw, day, cash)
        assert read_at(read, when) == pytest.approx(value, rel=1e-3)
    assert (read > 0).sum() == 2 and read.notna().all()


def test_what_the_bars_cannot_tell_is_nan():
    raw = traded()
    big = data.distributions_of(adjusted(raw, {"2020-05-21": 0.37 * raw["Close"].loc[:"2020-05-20"].iloc[-1]}))
    assert np.isnan(big["2020-05-21"]) and (big > 0).sum() == 0       # a 37% step: neither a distribution nor a split
    unread = raw.copy()
    off = np.random.default_rng(2).uniform(0.001, 0.004, (60, 4))   # the older bars off every step
    unread.iloc[:60, :4] = unread.iloc[:60, :4] + off
    read = data.distributions_of(adjusted(unread, {raw.index[60]: 0.2}))
    assert read.iloc[:61].isna().all() and read.iloc[70:].notna().all()


def test_a_fund_of_one_price_bars_is_not_read_and_costs_nothing():
    days = pd.bdate_range("2005-01-03", periods=5000)
    close = 3000 * np.exp(np.cumsum(np.random.default_rng(1).normal(0, 0.01, len(days))))
    started = time.perf_counter()
    read = data.distributions_of(bars(close, days))
    assert read.isna().all() and time.perf_counter() - started < 5


def test_the_bars_as_they_stood_read_nothing_the_full_bars_do_not():
    """Paper trading reads the bars Yahoo serves each day, the last factor one: on any session,
    what they read is what the full bars read, 0 where nothing is confirmed yet as there."""
    raw = traded(seed=9, sessions=320)
    full = data.distributions_of(adjusted(raw, QUARTERLY, later=0.99))
    ex = [raw.index.get_loc(pd.Timestamp(d)) for d in QUARTERLY]
    for c in sorted({e + k for e in ex for k in range(6)} | {60, 150, 250, 319}):
        cut = raw.iloc[:c + 1]
        stood = data.distributions_of(adjusted(cut, {d: v for d, v in QUARTERLY.items() if pd.Timestamp(d) <= cut.index[-1]}))
        assert stood.notna().all()
        assert stood.to_numpy() == pytest.approx(full.iloc[:c + 1].to_numpy(), abs=1e-5)


def test_an_ex_date_on_the_last_bar_waits_for_bars_after_it():
    raw = traded()
    day = raw.index.get_loc(pd.Timestamp("2020-05-21"))
    cut = raw.iloc[:day + 1]
    read = data.distributions_of(adjusted(cut, {"2020-02-20": 0.18, "2020-05-21": 0.21}))
    assert read.iloc[-1] == 0.0 and read.notna().all()                # nothing given yet, as the full bars
    assert read[read > 0].index.tolist() == [fraction(raw, "2020-02-20", 0.18)[0]]


def on_both(adjusted_bars, days, later, earlier, rng):
    """Set the bars of `days` on prices both factors put on the half-cent steps: at a ratio of
    0.995 between them, a whole dollar of traded price before the ex-date is 99.5 cents after it."""
    assert later * 0.995 == pytest.approx(earlier)
    for day in days:
        k = 40 + rng.integers(-1, 2, 4)
        adjusted_bars.loc[day, ["Open", "High", "Low", "Close"]] = earlier * np.array([k[0], k[1] + 1, k[2] - 1, k[3]], float)


def test_a_bar_a_hair_off_the_later_steps_is_no_ex_date():
    """A bar before the ex-date the later factor fits within its tolerance by chance, but not
    within half of it, followed by bars both factors fit, as SHY's of 2010-03: the ex-date is not
    placed on it, and nothing is given before the fourth bar from the true one."""
    raw = traded(sessions=200)
    day = raw.index.get_loc(pd.Timestamp("2020-05-21"))
    cash = 0.005 * raw["Close"].iloc[day - 1]                        # the factor before it, 0.995
    bars_ = adjusted(raw, {raw.index[day]: cash}, rounded=False)
    rng = np.random.default_rng(4)
    on_both(bars_, raw.index[day - 5:day], 1.0, 0.995, rng)
    hair = raw.index[day - 6]
    prices = bars_.loc[hair, ["Open", "High", "Low", "Close"]].to_numpy(dtype=float)
    bars_.loc[hair, ["Open", "High", "Low", "Close"]] = np.round(prices / data.HALF) * data.HALF + 0.7 * data.TOLERANCE / 100
    read = data.distributions_of(bars_)
    assert read.iloc[:day + 3].fillna(0.0).eq(0.0).all()            # nothing before the fourth bar
    assert read.iloc[day + 3] == pytest.approx(0.005, rel=1e-6)


def test_a_distribution_with_fewer_than_four_bars_from_its_ex_date_gives_nothing_yet():
    """The ex-date's bar a hair off the later steps, the ex-date placed a bar later: on the bars as
    they stood three bars after the ex-date, nothing is given; the fourth bar from the placement
    gives it, as the full bars do."""
    raw = traded(sessions=200)
    day = raw.index.get_loc(pd.Timestamp("2020-05-21"))
    bars_ = adjusted(raw, {raw.index[day]: 0.21}, rounded=False)
    prices = bars_.iloc[day, :4].to_numpy(dtype=float)
    bars_.iloc[day, :4] = np.round(prices / data.HALF) * data.HALF + 0.7 * data.TOLERANCE / 100
    stood = data.distributions_of(bars_.iloc[:day + 4])
    assert stood.notna().all() and (stood.iloc[day - 1:] > 0).sum() == 0
    full = data.distributions_of(bars_)
    assert full.iloc[day - 1:day + 4].eq(0.0).all() and full.iloc[day + 4] > 0


def test_a_step_whose_later_bars_fit_the_earlier_factor_too_is_nan():
    raw = traded(sessions=200)
    day = raw.index.get_loc(pd.Timestamp("2020-05-21"))
    cash = 0.005 * raw["Close"].iloc[day - 1]
    bars_ = adjusted(raw, {raw.index[day]: cash}, rounded=False).iloc[:day + 11].copy()
    rng = np.random.default_rng(6)
    on_both(bars_, [d for k, d in enumerate(bars_.index[day:]) if k != 1], 1.0 / 0.995 * 0.995, 0.995, rng)
    read = data.distributions_of(bars_)
    assert np.isnan(read.iloc[day + 3]) and (read.iloc[day - 1:] > 0).sum() == 0


def test_a_fund_whose_steps_fit_both_factors_is_not_read():
    days = pd.bdate_range("2020-01-02", periods=120)
    irx = pd.DataFrame({"Close": np.full(len(days), 2.0)}, index=days)
    etf = adjusted(traded(sessions=120), {"2020-03-19": 0.3})
    market = data.assemble({"ETF": etf, "SHY": etf.copy()}, irx, ())
    assert market.signal_distributions["SHY"].isna().all()
    assert market.signal_distributions["ETF"].gt(0).sum() == 1


def test_distributions_are_read_as_signals_are():
    days = pd.bdate_range("2020-01-02", periods=120)
    raw = traded(sessions=120)
    etf = adjusted(raw, {"2020-03-19": 0.3})
    irx = pd.DataFrame({"Close": np.full(len(days), 2.0)}, index=days)
    coin = bars(np.linspace(5000, 6000, 170), pd.date_range("2020-01-01", periods=170))
    market = data.assemble({"ETF": etf, "COIN": coin}, irx, ("COIN",))
    paid = market.signal_distributions
    assert paid.index.equals(market.prices.index) and list(paid.columns) == ["ETF", "COIN"]
    when = paid.index[paid.index.get_loc(pd.Timestamp("2020-03-19")) + 3]
    assert paid.loc[when, "ETF"] > 0 and paid["ETF"].gt(0).sum() == 1
    assert paid["COIN"].isna().all()                                 # a lagged asset's are not read
    late = data.traded_from(market, {"ETF": "2020-02-03"})
    assert late.signal_distributions.loc[:"2020-01-31", "ETF"].isna().all()
    assert late.signal_distributions.loc[when, "ETF"] == paid.loc[when, "ETF"]
    cut = market.window("2020-03-02", "2020-03-31")
    assert cut.signal_distributions.index.equals(cut.prices.index)
    assert data.assemble({"ETF": etf[["Close"]]}, irx, ()).signal_distributions is None   # bars with no open
