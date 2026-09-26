"""The snapshot, the calendar, the universe."""
import json
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
