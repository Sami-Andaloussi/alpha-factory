"""The lab's ground truth: one frozen snapshot of public daily data.

`download()` fetches the universe and the Treasury-bill rate from Yahoo Finance once, adjusted for
dividends and splits, and writes a dated snapshot under `alpha-lab/data/<date>/` with its manifest:
one sha256 per file and the integrity findings. The snapshot is never committed; the manifest is.

`extend()` fetches what the universe gained after that, assets or exchange rates, and freezes it in
a dated folder of its own, listed in the manifest as an addition: the files already frozen never
change, so no result computed on them moves.

`load()` reads the snapshot the manifest names and its additions, refuses any file whose hash
changed, and returns
the market on the ETF calendar: prices, the tradable mask, the daily risk-free rate, and the
prices and traded volumes a signal may read at each close, in which bitcoin is lagged one day. An
asset has no price, and no volume, before the session the universe lets the lab trade it.

    python -m lab.data download             # once: the snapshot and its manifest
    python -m lab.data extend               # what the universe gained since, in a folder of its own
    python -m lab.data check                # the hashes, the first sessions and the findings
    python -m lab.data crosscheck <folder>  # compare with closes saved by hand from stooq.com
"""
from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from lab.universe import CHF_RATES, END, LAGGED, RISK_FREE, START, TICKERS, TRADING_DAYS, UNIVERSE

DATA = Path(__file__).resolve().parent.parent / "data"
FIELDS = ("Open", "High", "Low", "Close", "Volume")
# Integrity: a gap of more than three sessions (three calendar days for bitcoin, which trades every
# day), a run of three zero returns or more, and a daily move above 15% on an ETF or 40% on bitcoin
# are written into the manifest, each with its first date and its length or its size.
MAX_GAP = 3
ZERO_RUN = 3
MAX_MOVE = {"etf": 0.15, "crypto": 0.40}
# Volume: a session whose volume is missing or zero while the asset has a price, or below 1% or above
# 20 times the median of the 21 sessions before it, is listed by `check`. It is not written into the
# manifest, whose findings were frozen with the snapshot, nor refused by gate 1, which would change
# the figures of cards that read no volume: a card that reads volumes says what it does with them.
LOW_VOLUME, HIGH_VOLUME, VOLUME_MEDIAN = 0.01, 20, 21
# A sample is compared with Stooq: SPY, and the four assets with integrity findings. stooq.com
# answers scripted requests with a JavaScript verification page, which the lab does not get around,
# so the closes are saved by hand and compared by `crosscheck`. An asset is confirmed when its daily
# returns differ by 10 bps or less on 95% of the common days, and by 2% at most on any day: a source
# that does not add back dividends differs on ex-dividend days, a bad print or a missed split by far
# more. An asset that is not confirmed has its days examined before a card uses it.
CROSS_CHECKED = ("SPY", "XLF", "XLE", "EEM", "SLV")
WITHIN_10BPS, MAX_DIFFERENCE = 0.95, 0.02
CROSS_CHECK = {"source": "Stooq", "status": "not run", "tickers": list(CROSS_CHECKED),
               "reason": "stooq.com answers scripted requests with a JavaScript verification page: its daily "
                         "closes are saved by hand, then compared by python -m lab.data crosscheck <folder>"}


def file_name(ticker: str) -> str:
    return ticker.replace("^", "") + ".csv"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# --------------------------------------------------------------------------- the market

@dataclass(frozen=True)
class Market:
    """Everything a strategy may know, on the ETF calendar.

    prices         adjusted closes (total return), NaN before an asset is traded; bitcoin's close
                   of a day comes about four hours after the US close of that day
    tradable       True where the asset is traded and has a price
    rf             the Treasury-bill return that cash earns overnight into each session, at the
                   rate of the session before
    signal_prices  what a signal may read at each close: bitcoin's close of the day before
    signal_volumes each asset's traded volume as a signal may read it, lagged as `signal_prices`
                   is: a fund's own shares traded across the US venues (consolidated), in shares,
                   split-adjusted, and bitcoin's in dollars, as Yahoo reports them; None where the
                   bars carry no volume

    A strategy reads bitcoin through `signal_prices`, never through `prices`. A fund's volume is
    its own shares' trading, not the trading of what it holds.
    """
    prices: pd.DataFrame
    tradable: pd.DataFrame
    rf: pd.Series
    signal_prices: pd.DataFrame
    signal_volumes: pd.DataFrame | None = None

    def window(self, start=None, end=None) -> "Market":
        cut = slice(pd.Timestamp(start) if start else None, pd.Timestamp(end) if end else None)
        volumes = None if self.signal_volumes is None else self.signal_volumes.loc[cut]
        return Market(self.prices.loc[cut], self.tradable.loc[cut], self.rf.loc[cut], self.signal_prices.loc[cut],
                      volumes)

    def asof(self, when) -> "Market":
        """No session after `when`. Bitcoin's close of `when`, in `prices`, is still to come at
        the US close of `when`: a signal reads `signal_prices`."""
        return self.window(None, when)


def benchmark_weights(tradable: pd.DataFrame) -> pd.DataFrame:
    """The equal weight of the assets tradable at each date."""
    count = tradable.sum(axis=1)
    return tradable.astype(float).div(count.where(count > 0), axis=0).fillna(0.0)


def load(start=None, end=None, root: Path = DATA) -> Market:
    """The market between start and end, from the snapshot the manifest names and its additions."""
    manifest = json.loads((root / "manifest.json").read_text())
    held = verified(manifest, root)
    raw = {ticker: read(root / held[ticker] / file_name(ticker)) for ticker in listed(manifest, "tickers")}
    market = assemble(raw, read(root / held[RISK_FREE] / file_name(RISK_FREE)), listed(manifest, "lagged"))
    return traded_from(market, {a.ticker: a.first_session for a in UNIVERSE}).window(start, end)


def listed(manifest: dict, key: str) -> list[str]:
    """The snapshot's tickers, or its lagged ones, then each addition's."""
    return [*manifest[key], *(t for addition in manifest.get("additions", []) for t in addition.get(key, []))]


def holdings(manifest: dict) -> dict[str, str]:
    """The folder that holds each frozen series: an asset, the bill rate or an exchange rate."""
    held = dict.fromkeys([*manifest["tickers"], manifest["risk_free"]], manifest["snapshot"])
    for addition in manifest.get("additions", []):
        held.update(dict.fromkeys([*addition["tickers"], *addition["rates"]], addition["snapshot"]))
    return held


def verified(manifest: dict, root: Path) -> dict[str, str]:
    """The holdings, once every file the manifest lists has the hash it lists."""
    parts = [(manifest["snapshot"], manifest["files"]),
             *((addition["snapshot"], addition["files"]) for addition in manifest.get("additions", []))]
    for snapshot, files in parts:
        if not (root / snapshot).is_dir():
            raise RuntimeError(f"the snapshot {snapshot} is not in data/{snapshot}/: copy that folder from the "
                               f"machine that froze it (see the runbook)")
        for name, meta in files.items():
            if not (root / snapshot / name).is_file():
                raise RuntimeError(f"{name}: not in data/{snapshot}/; copy that folder whole from the machine that "
                                   f"froze it")
            if sha256(root / snapshot / name) != meta["sha256"]:
                raise ValueError(f"{name}: its hash differs from the manifest; the snapshot was altered")
    return holdings(manifest)


def traded_from(market: Market, first: dict) -> Market:
    """No price, no signal and no volume for an asset before the session the universe lets the lab
    trade it."""
    prices, signal = market.prices.copy(), market.signal_prices.copy()
    volumes = None if market.signal_volumes is None else market.signal_volumes.copy()
    for ticker, when in first.items():
        if ticker in prices.columns:
            before = prices.index < pd.Timestamp(when)
            prices.loc[before, ticker] = np.nan
            signal.loc[before, ticker] = np.nan
            if volumes is not None:
                volumes.loc[before, ticker] = np.nan
    return Market(prices, prices.notna(), market.rf, signal, volumes)


def read(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, index_col="Date", parse_dates=["Date"])


def assemble(raw: dict[str, pd.DataFrame], irx: pd.DataFrame, lagged) -> Market:
    """Align every close, and every volume, on the ETF calendar; bitcoin's weekend moves land on
    Monday, and its volume, as its close, is the calendar day before's: Monday reads Sunday's, and
    Friday's and Saturday's, and the volume of the day before a holiday, are read by no session."""
    etfs = [t for t in raw if t not in lagged]
    calendar = pd.DatetimeIndex(sorted(set().union(*(raw[t].index for t in etfs))))
    closes = {t: raw[t]["Close"] for t in raw}
    prices = pd.DataFrame({t: closes[t].reindex(calendar) for t in raw})
    signal = prices.copy()
    for t in lagged:  # the close of the calendar day before is the last one known at the US close
        signal[t] = closes[t].reindex(calendar - pd.Timedelta(days=1)).to_numpy()
    volumes = None
    if all("Volume" in raw[t] for t in raw):
        volumes = pd.DataFrame({t: raw[t]["Volume"].reindex(calendar).where(prices[t].notna()) for t in raw},
                               dtype=float)
        for t in lagged:
            day_before = calendar - pd.Timedelta(days=1)
            volumes[t] = (raw[t]["Volume"].reindex(day_before).where(closes[t].reindex(day_before).notna())
                          .to_numpy(dtype=float))
    rate = irx["Close"].reindex(calendar).ffill(limit=5).shift(1)  # cash held overnight earns the rate set before
    rf = (rate / 100.0 / TRADING_DAYS).rename("rf")
    return Market(prices, prices.notna(), rf, signal, volumes)


# --------------------------------------------------------------------------- integrity

def runs(flags: pd.Series) -> list[tuple[pd.Timestamp, int]]:
    """Each run of consecutive True values: its first date and its length."""
    found, start, length = [], None, 0
    for when, flag in flags.items():
        if flag:
            start, length = (when, 1) if length == 0 else (start, length + 1)
        elif length:
            found.append((start, length))
            length = 0
    if length:
        found.append((start, length))
    return found


def integrity(raw: dict[str, pd.DataFrame], lagged) -> list[dict]:
    """Gaps, runs of zero returns and outsized moves, one finding per case, dated at its start."""
    findings = []
    etfs = [t for t in raw if t not in lagged]
    calendar = pd.DatetimeIndex(sorted(set().union(*(raw[t].index for t in etfs))))
    for ticker, frame in raw.items():
        close = frame["Close"].dropna()
        if ticker in lagged:   # bitcoin trades every day: its gaps are missing calendar days
            days = pd.date_range(close.index[0], close.index[-1])
        else:                  # an ETF's gaps are missing sessions of the calendar, within its life
            days = calendar[(calendar >= close.index[0]) & (calendar <= close.index[-1])]
        missing = pd.Series(~days.isin(close.index), index=days)
        for when, length in runs(missing):
            if length > MAX_GAP:
                findings.append({"ticker": ticker, "check": "gap", "date": str(when.date()), "value": length})
        returns = close.pct_change().dropna()
        for when, length in runs(returns == 0):
            if length >= ZERO_RUN:
                findings.append({"ticker": ticker, "check": "zero returns", "date": str(when.date()),
                                 "value": length})
        limit = MAX_MOVE["crypto" if ticker in lagged else "etf"]
        for when, move in returns[returns.abs() > limit].items():
            findings.append({"ticker": ticker, "check": "large move", "date": str(when.date()),
                             "value": round(float(move), 4)})
    return findings


def volume_findings(market: Market) -> list[dict]:
    """The sessions whose volume, as a signal reads it, is missing or zero while the asset has a
    price, or far from the median of the sessions before it: bars to examine before a card reads
    them."""
    if market.signal_volumes is None:
        return []
    findings = []
    for ticker in market.signal_volumes.columns:
        volume = market.signal_volumes[ticker][market.signal_prices[ticker].notna()]
        for when, value in volume[volume.isna() | (volume <= 0)].items():
            findings.append({"ticker": ticker, "check": "no volume", "date": str(when.date()), "value": value})
        ratio = volume / volume.rolling(VOLUME_MEDIAN, min_periods=VOLUME_MEDIAN).median().shift(1)
        for when, value in ratio[(ratio < LOW_VOLUME) | (ratio > HIGH_VOLUME)].items():
            findings.append({"ticker": ticker, "check": "volume outlier", "date": str(when.date()),
                             "value": round(float(value), 4)})
    return findings


def cross_check(ours: pd.Series, theirs: pd.Series) -> dict:
    """Compare two close series of one asset on their common dates: how far their daily returns
    differ, and whether the asset is confirmed."""
    common = ours.index.intersection(theirs.index)
    a, b = ours.loc[common].pct_change().dropna(), theirs.loc[common].pct_change().dropna()
    gap = (a - b).abs()
    within = float((gap <= 1e-3).mean()) if len(gap) else 0.0
    largest = float(gap.max()) if len(gap) else 0.0
    return {"days": int(len(gap)), "within_10bps": round(within, 4), "max_abs_bps": round(largest * 1e4, 3),
            "days_over_10bps": [str(d.date()) for d in gap[gap > 1e-3].index],
            "confirmed": bool(len(gap) and within >= WITHIN_10BPS and largest <= MAX_DIFFERENCE)}


def stooq_ticker(stem: str) -> str:
    """The asset of a file saved from stooq.com: spy.csv, spy_us_d.csv or spy.us.csv is SPY, and
    btcusd_d.csv is BTC-USD."""
    name = stem.lower()
    for suffix in ("_d", "_us", ".us"):
        name = name.removesuffix(suffix)
    return "BTC-USD" if name == "btcusd" else name.upper()


def cross_check_folder(folder: Path, root: Path = DATA, source: str = "Stooq") -> dict:
    """Compare the snapshot's closes with each CSV of `folder` (a Date and a Close column), and write
    the result into the manifest. A file that names no asset of the snapshot is refused."""
    manifest = json.loads((root / "manifest.json").read_text())
    market = load(root=root)
    files = sorted(Path(folder).glob("*.csv"))
    unknown = [p.name for p in files if stooq_ticker(p.stem) not in market.prices.columns]
    if unknown or not files:
        raise ValueError(f"{folder}: no asset of the snapshot for {', '.join(unknown) or 'any file'}")
    found = {}
    for path in files:
        ticker = stooq_ticker(path.stem)
        theirs = pd.read_csv(path, index_col="Date", parse_dates=["Date"])["Close"]
        found[ticker] = cross_check(market.prices[ticker].dropna(), theirs.dropna())
    manifest["cross_check"] = {"source": source, "status": "run", "checked": date.today().isoformat(),
                               "tickers": found}
    (root / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    return manifest["cross_check"]


def unexamined(manifest: dict) -> list[str]:
    """The assets the last cross-check did not confirm and whose days no review examined: the
    manifest's `cross_check_review` names each such asset, with what its flagged days are, and
    carries the date of the cross-check it examined, so that a new cross-check asks for a new one."""
    checked = manifest.get("cross_check", {})
    if checked.get("status") != "run":
        return []
    review = manifest.get("cross_check_review", {})
    examined = review.get("tickers", {}) if review.get("checked") == checked["checked"] else {}
    return sorted(t for t, result in checked["tickers"].items() if not result["confirmed"] and t not in examined)


# --------------------------------------------------------------------------- the snapshot

def download(root: Path = DATA, snapshot: str | None = None) -> dict:
    """Fetch the universe and the Treasury-bill rate once, then freeze them; returns the manifest.
    Refused when a snapshot is already frozen: the lab's ground truth does not change."""
    import yfinance as yf

    snapshot = snapshot or date.today().isoformat()
    if (root / "manifest.json").exists() or (root / snapshot).exists():
        raise RuntimeError(f"{root}: a snapshot is already frozen; the lab's data do not change")
    return freeze(fetch(yf, (*TICKERS, RISK_FREE)), source_of(yf), root, snapshot)


def fetch(yf, tickers, last=END) -> dict[str, pd.DataFrame]:
    """Daily bars adjusted for dividends and splits, from the lab's start to `last`, as the snapshot
    was drawn; paper trading draws the days after it the same way."""
    end = (pd.Timestamp(last) + pd.Timedelta(days=1)).date().isoformat()  # Yahoo's end is exclusive
    raw = {}
    for ticker in tickers:
        frame = yf.download(ticker, start=START, end=end, auto_adjust=True, progress=False,
                            multi_level_index=False)
        frame = frame[list(FIELDS)].dropna(how="all")
        if frame.empty:
            raise RuntimeError(f"{ticker}: Yahoo returned no data")
        raw[ticker] = frame
    return raw


def source_of(yf) -> str:
    return f"Yahoo Finance through yfinance {yf.__version__}, daily bars adjusted for dividends and splits"


def extend(root: Path = DATA, snapshot: str | None = None) -> dict:
    """Fetch the assets and exchange rates of the universe that no frozen folder holds, and freeze
    them in a folder of their own; returns the manifest. Refused when nothing is missing."""
    import yfinance as yf

    held = holdings(json.loads((root / "manifest.json").read_text()))
    tickers = [t for t in TICKERS if t not in held]
    rates = [r for r in CHF_RATES if r not in held]
    if not tickers and not rates:
        raise RuntimeError("every asset and rate of the universe is already frozen; the lab's data do not change")
    return add(fetch(yf, (*tickers, *rates)), source_of(yf), root, snapshot or date.today().isoformat(),
               tickers=tickers, rates=rates, lagged=[t for t in tickers if t in LAGGED])


def add(raw: dict[str, pd.DataFrame], source: str, root: Path, snapshot: str, tickers, rates=(),
        lagged=()) -> dict:
    """Freeze assets or rates added to the universe after the snapshot, under root/<snapshot>/, and
    list them in the manifest as an addition. A series already frozen is refused: none is replaced."""
    manifest = json.loads((root / "manifest.json").read_text())
    held = holdings(manifest)
    again = [t for t in raw if t in held]
    if again:
        raise RuntimeError(f"{', '.join(again)}: already frozen in data/{held[again[0]]}/; the lab's data do not change")
    folder = root / snapshot
    folder.mkdir(parents=True, exist_ok=False)
    frames = {}
    for ticker, frame in raw.items():
        frame = frame.copy()
        frame.index.name = "Date"
        frame.to_csv(folder / file_name(ticker), float_format="%.10g")
        frames[ticker] = read(folder / file_name(ticker))
    manifest.setdefault("additions", []).append({
        "snapshot": snapshot,
        "source": source,
        "downloaded": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "tickers": list(tickers),
        "rates": list(rates),
        "lagged": list(lagged),
        "files": {file_name(t): {"sha256": sha256(folder / file_name(t)), "rows": len(frames[t]),
                                 "first": str(frames[t].index[0].date()), "last": str(frames[t].index[-1].date())}
                  for t in frames},
        "integrity": [*(integrity({t: frames[t] for t in tickers}, lagged) if tickers else []),
                      *(integrity({r: frames[r] for r in rates}, ()) if rates else [])],
    })
    (root / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    return manifest


def freeze(raw: dict[str, pd.DataFrame], source: str, root: Path, snapshot: str,
           tickers=TICKERS, lagged=LAGGED) -> dict:
    """Write the snapshot under root/<snapshot>/ and its manifest at root/manifest.json."""
    folder = root / snapshot
    folder.mkdir(parents=True, exist_ok=False)
    frames = {}
    for ticker, frame in raw.items():
        frame = frame.copy()
        frame.index.name = "Date"
        frame.to_csv(folder / file_name(ticker), float_format="%.10g")
        frames[ticker] = read(folder / file_name(ticker))
    manifest = {
        "snapshot": snapshot,
        "source": source,
        "period": [START, END],
        "downloaded": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "tickers": list(tickers),
        "risk_free": RISK_FREE,
        "lagged": list(lagged),
        "files": {file_name(t): {"sha256": sha256(folder / file_name(t)), "rows": len(frames[t]),
                                 "first": str(frames[t].index[0].date()), "last": str(frames[t].index[-1].date())}
                  for t in frames},
        "integrity": integrity({t: frames[t] for t in tickers}, lagged),
        "cross_check": CROSS_CHECK,
    }
    (root / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    return manifest


def check(root: Path = DATA) -> int:
    manifest = json.loads((root / "manifest.json").read_text())
    market = load(root=root)
    additions = manifest.get("additions", [])
    files = {**manifest["files"], **{name: meta for addition in additions for name, meta in addition["files"].items()}}
    first = {asset.ticker: asset.first_session for asset in UNIVERSE}
    problems = []
    if listed(manifest, "tickers") != list(TICKERS) or listed(manifest, "lagged") != list(LAGGED):
        problems.append("the manifest's tickers or lagged assets differ from the universe's: "
                        "python -m lab.data extend freezes what the universe gained")
    missing = [r for r in CHF_RATES if r not in holdings(manifest)]
    if missing:
        problems.append(f"{', '.join(missing)}: not frozen; python -m lab.data extend freezes them")
    for t in listed(manifest, "tickers"):
        starts = files[file_name(t)]["first"]
        if starts > first[t]:
            problems.append(f"{t}: the data start on {starts}, after the universe's first session {first[t]}")
        if str(market.tradable[t].idxmax().date()) != first[t]:
            problems.append(f"{t}: first traded on {market.tradable[t].idxmax().date()}, not {first[t]}")
    for t in unexamined(manifest):
        problems.append(f"{t}: not confirmed by the cross-check, and its days not examined in the "
                        "manifest's cross_check_review")
    print(f"snapshot {manifest['snapshot']}: {len(manifest['files'])} files, hashes match")
    for addition in additions:
        print(f"addition {addition['snapshot']}: {len(addition['files'])} files, hashes match")
    print(f"{len(market.prices)} sessions, {market.prices.index[0].date()} to {market.prices.index[-1].date()}")
    for finding in [*manifest["integrity"], *(f for addition in additions for f in addition["integrity"])]:
        print(f"  {finding['ticker']:8} {finding['check']:13} {finding['date']}  {finding['value']}")
    for finding in volume_findings(market):
        print(f"  {finding['ticker']:8} {finding['check']:13} {finding['date']}  {finding['value']}  (volume, not frozen)")
    for problem in problems:
        print(f"  mismatch: {problem}")
    return 1 if problems else 0


def main(argv: list[str], root: Path = DATA) -> int:
    command = argv[0] if argv else "check"
    if command == "download":
        print(json.dumps(download(), indent=1)[:2000])
    elif command == "extend":
        print(json.dumps(extend()["additions"][-1], indent=1)[:2000])
    elif command == "crosscheck":
        print(json.dumps(cross_check_folder(Path(argv[1])), indent=1))
    else:
        try:
            return check(root)
        except (RuntimeError, ValueError) as error:          # one line, never a trace
            print(f"refused: {' '.join(str(error).split())}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
