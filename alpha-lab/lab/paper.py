"""Gate 8, paper trading: after every US close, each strategy under paper trading sets its targets
for the next session, the paper account gets the orders that reach them, and one log line per
strategy and session says what was decided and whether the live signal is the backtest's.

    python -m lab.paper --log <folder>      # the scheduled job: from the last close past
    python -m lab.paper --take              # its summary, from its branch, into paper/ and the board

Which strategies: every survivor of gates 1 to 7, its base variant; while there is none, the first
strategy the registry holds, as a test of the chain, whatever its verdict. They share the account
in equal parts, and the account holds the sum of their books.

The live signal of a session is computed after the close before it, on the market up to that close
with the session added, since a strategy's targets are set from the market up to the session
before. Its backtest signal is the same strategy's target for that session computed later, once
the session's own close is known. A strategy that reads its session's own close, or data that
change after the fact, make the two differ: each gap is logged, and gate 8 asks for none.

The broker is Alpaca's paper account, at the one address written below and read from nowhere else,
so that the job can never reach a real account. Its two keys are read from the job's environment
only, never printed, logged or committed; every test and every local run uses a fake broker. Orders
are market orders in dollars for the next open, where the backtest trades at the session's close:
gate 8 compares signals, not fills.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import yaml

from lab import battery, costs, data, engine, registry, status
from lab.data import Market
from lab.report import strategy_of
from lab.universe import LAGGED, RISK_FREE, UNIVERSE

PAPER = "https://paper-api.alpaca.markets"     # the paper account: never a variable, a setting or the environment
KEYS = ("APCA_API_KEY_ID", "APCA_API_SECRET_KEY")
LAB = Path(__file__).resolve().parent.parent
FIRST = {asset.ticker: asset.first_session for asset in UNIVERSE}
SAME = 1e-9          # two targets this close are the same signal
LEAST = 0.001        # an order below this share of the account is not sent
NEW_YORK = "America/New_York"
ENDED = status.ENDED  # a strategy's gate 8 concluded: it leaves paper trading
UNSENT = ("refused", "not sent", "rejected")   # an order's status when the broker did not take it
CRYPTO = {asset.ticker for asset in UNIVERSE if asset.cluster == "crypto"}   # Alpaca names them BTC/USD, BTCUSD


# --------------------------------------------------------------------------- the broker


class Refused(urllib.request.HTTPRedirectHandler):
    """No redirect is followed: the keys go to the paper account's address and nowhere else."""

    def redirect_request(self, *args, **options):
        return None


OPENER = urllib.request.build_opener(Refused())


class Alpaca:
    """Alpaca's paper account, through its REST API; the keys come from the environment."""

    def __init__(self, environ=os.environ):
        wrong = [key for key in KEYS if not environ.get(key) or not environ[key].isprintable()
                 or environ[key] != environ[key].strip()]
        if wrong:
            raise RuntimeError(f"the broker's keys are missing from the environment, or not one line of text: "
                               f"{', '.join(wrong)}")
        self._headers = {"APCA-API-KEY-ID": environ[KEYS[0]], "APCA-API-SECRET-KEY": environ[KEYS[1]]}

    def __repr__(self) -> str:
        return "Alpaca(paper)"

    def _call(self, method: str, path: str, body: dict | None = None):
        request = urllib.request.Request(PAPER + path, method=method, headers={**self._headers,
                                         "Content-Type": "application/json"},
                                         data=None if body is None else json.dumps(body).encode())
        if urllib.parse.urlsplit(request.full_url)[:2] != urllib.parse.urlsplit(PAPER)[:2]:
            raise RuntimeError(f"refused: {method} {path} would leave the paper account's address")
        try:
            with OPENER.open(request, timeout=30) as answer:
                return json.loads(answer.read() or b"null")
        except urllib.error.HTTPError as error:           # its body is the broker's message, never a key
            said = f"answered {error.code} to {method} {path}: {error.read()[:300].decode(errors='replace')}"
        except Exception as error:                        # whatever else, without its message, which may hold a header
            said = f"could not be reached for {method} {path} ({type(error).__name__})"
        raise RuntimeError(f"the broker {said}")          # raised outside, so that it carries no earlier error

    def equity(self) -> float:
        return float(self._call("GET", "/v2/account")["equity"])

    def holdings(self) -> dict[str, float]:
        crypto = {ticker.replace("-", ""): ticker for ticker in CRYPTO}
        return {crypto.get(p["symbol"].replace("/", ""), p["symbol"]): float(p["market_value"])
                for p in self._call("GET", "/v2/positions")}

    def pending(self) -> int:
        """The orders sent and not yet filled, by an earlier run."""
        return len(self._call("GET", "/v2/orders?status=open"))

    def calendar(self, start: date, end: date) -> dict[date, pd.Timestamp]:
        """The exchange's sessions between two days, each with its close, in New York."""
        days = self._call("GET", f"/v2/calendar?start={start.isoformat()}&end={end.isoformat()}")
        return {date.fromisoformat(day["date"]): pd.Timestamp(f"{day['date']} {day['close']}", tz=NEW_YORK)
                for day in days}

    def send(self, orders: list[dict]) -> list[str]:
        """Each order on its own: one the broker refuses is said, and the others are still sent."""
        said = []
        for order in orders:
            crypto = order["symbol"] in CRYPTO                   # traded around the clock, its orders last
            try:
                if order.get("whole"):
                    answer = self._call("DELETE", f"/v2/positions/{order['symbol'].replace('-', '')}")
                else:
                    answer = self._call("POST", "/v2/orders", {
                        "symbol": order["symbol"].replace("-", "/") if crypto else order["symbol"],
                        "side": order["side"], "type": "market", "time_in_force": "gtc" if crypto else "day",
                        "notional": f"{order['notional']:.2f}"})
                said.append((answer or {}).get("status", "sent"))
            except RuntimeError as error:
                said.append(f"refused: {error}")
        return said


def to_orders(weights: dict[str, float], equity: float, held: dict[str, float], least: float = LEAST) -> list[dict]:
    """The orders that take the account from what it holds to `weights` of its equity, sales first:
    an asset the weights leave at nothing is sold whole, and a change below `least` of the account
    is not sent."""
    wanted = {t: w * equity for t, w in weights.items()}
    orders = []
    for ticker in sorted(set(held) | set(wanted)):
        have, want = held.get(ticker, 0.0), wanted.get(ticker, 0.0)
        if want <= 0 < have:
            orders.append({"symbol": ticker, "side": "sell", "whole": True})
        elif abs(want - have) >= least * equity:
            orders.append({"symbol": ticker, "side": "buy" if want > have else "sell",
                           "notional": round(abs(want - have), 2)})
    return sorted(orders, key=lambda order: order["side"] != "sell")


# --------------------------------------------------------------------------- the strategies


@dataclass(frozen=True)
class Paper:
    id: str
    role: str               # "survivor", or "test of the chain" while no strategy has passed
    universe: tuple
    parameters: dict
    positions: object       # the strategy's function, compiled from its source


def papered(lab: Path = LAB, registry_path: Path = registry.REGISTRY) -> list[Paper]:
    """The strategies under paper trading: every survivor, its base variant, until its folder holds
    its gate 8's conclusion (`gate-8.md`); while there is no survivor, the first strategy the
    registry holds, as a test of the chain."""
    base = {}
    for line in registry.lines(registry_path):
        if line["variant"] == 0 and not line.get("void"):
            base.setdefault(line["card"], line)
    survivors = [line for line in base.values() if line["survivor"]]
    chosen, role = (survivors, "survivor") if survivors else (list(base.values())[:1], "test of the chain")
    papers = []
    for line in chosen:
        folder = lab / "strategies" / line["card"]
        if (folder / ENDED).exists():             # its gate 8 is concluded
            continue
        if not (folder / "card.yaml").exists():
            raise RuntimeError(f"{line['card']}: its registry line names a folder that holds no card; the job stops")
        if hashlib.sha256((folder / "card.yaml").read_bytes()).hexdigest() != line["card_hash"]:
            raise RuntimeError(f"{line['card']}: its card differs from the one that ran, and paper trading trades "
                               f"only the card the registry holds; the job stops")
        spec = yaml.safe_load((folder / "card.yaml").read_text())
        papers.append(Paper(line["card"], role, tuple(spec["universe"]), dict(spec["variants"][0]),
                            strategy_of(folder / "strategy.py")))
    return papers


# --------------------------------------------------------------------------- the market


def yahoo(tickers, through: date) -> tuple[dict, pd.DataFrame]:
    """The daily bars of `tickers` and the bill's rate from the lab's start to `through`, drawn from
    Yahoo as the snapshot was."""
    import yfinance as yf

    raw = data.fetch(yf, (*tickers, RISK_FREE), last=through.isoformat())
    return raw, raw.pop(RISK_FREE)


def live(raw: dict, irx: pd.DataFrame, session: pd.Timestamp | None = None) -> Market:
    """The market from the bars, by the snapshot's rules. With `session`, that session added after
    the last close, as it stands before it opens: no price yet, each asset tradable as at the last
    close, and the bill's rate set at that close."""
    if session is not None:
        raw = {t: frame.reindex(frame.index.append(pd.DatetimeIndex([session]))) for t, frame in raw.items()}
    market = data.traded_from(data.assemble(raw, irx, [t for t in raw if t in LAGGED]), FIRST)
    if session is None:
        return market
    tradable = market.tradable.copy()
    tradable.iloc[-1] = tradable.iloc[-2]
    return Market(market.prices, tradable, market.rf, market.signal_prices)


def targets(paper: Paper, market: Market) -> pd.DataFrame:
    return battery.targets(paper.positions, battery.restrict(market, paper.universe), paper.parameters)


def row(frame: pd.DataFrame, session) -> dict | None:
    """A session's targets, or None where the strategy holds."""
    if session not in frame.index or frame.loc[session].isna().all():
        return None
    return {t: float(w) for t, w in frame.loc[session].items()}


def same(a: dict | None, b: dict | None) -> bool:
    if a is None or b is None:
        return a is b
    return set(a) == set(b) and all(abs(a[t] - b[t]) <= SAME for t in a)


def compared(frame: pd.DataFrame, mine: list[dict], last: pd.Timestamp) -> dict:
    """The live signals logged for sessions whose close is known, against the backtest's."""
    done = [line for line in mine if pd.Timestamp(line["session"]) <= last]
    gaps = [line["session"] for line in done if not same(line["targets"], row(frame, pd.Timestamp(line["session"])))]
    return {"compared": len(done), "identical": len(done) - len(gaps), "gaps": gaps}


def book(paper: Paper, market: Market, mine: list[dict]) -> tuple[dict, float]:
    """The strategy's paper book at the last close: the weights it holds, from its live targets as
    the engine trades them, and its return since its first logged session."""
    last = market.prices.index[-1]
    done = [line for line in mine if pd.Timestamp(line["session"]) <= last]
    if not done:
        return {}, 0.0
    universe = battery.restrict(market, paper.universe)
    window = universe.prices.loc[pd.Timestamp(done[0]["session"]):]
    positions = pd.DataFrame(index=window.index, columns=window.columns, dtype=float)
    for line in done:
        if line["targets"] is not None and pd.Timestamp(line["session"]) in positions.index:
            positions.loc[pd.Timestamp(line["session"])] = pd.Series(line["targets"])
    if positions.isna().all().all():
        return {}, 0.0
    result = engine.run(window, positions, costs.per_side(window.columns), universe.rf.loc[window.index])
    held = result.weights.iloc[-1]
    return {t: float(w) for t, w in held.items() if w > 0}, float((1 + result.returns).prod() - 1)


# --------------------------------------------------------------------------- one day


def read_log(path: Path) -> list[dict]:
    return [json.loads(text) for text in path.read_text().splitlines() if text.strip()] if path.exists() else []


def settled(broker, now: pd.Timestamp) -> date:
    """The last session whose close is past at `now`."""
    closes = broker.calendar(now.date() - timedelta(days=10), now.date())
    return max(day for day, close in closes.items() if close <= now)


def day(broker, bars, folder: Path, today: date, papers: list[Paper] | None = None) -> list[dict]:
    """After the close of `today`: the next session's targets of every strategy under paper trading,
    the orders that reach them, and one log line each, in `folder` with its page and its summary.
    Nothing when `today` had no session, or for a strategy whose line of that session is written."""
    sessions = broker.calendar(today - timedelta(days=10), today + timedelta(days=10))
    if today not in sessions:
        return []
    session = pd.Timestamp(min(s for s in sessions if s > today))
    log = folder / "log.jsonl"
    logged = read_log(log)
    written = {line["strategy"] for line in logged if line["session"] == session.date().isoformat()}
    papers = [paper for paper in (papered() if papers is None else papers) if paper.id not in written]
    if not papers:
        return []
    raw, irx = bars(sorted({t for paper in papers for t in paper.universe}), today)
    now = live(raw, irx)
    late = [t for t in now.prices.columns if pd.Timestamp(today) not in raw[t].index]
    if now.prices.index[-1] != pd.Timestamp(today) or late:
        raise RuntimeError(f"the bars of {', '.join(late) or 'every asset'} end before {today}: the close is not known "
                           f"yet")
    before = live(raw, irx, session)
    lines, books = [], []
    for paper in papers:
        mine = [line for line in logged if line["strategy"] == paper.id]
        target = row(targets(paper, before), session)
        held, since = book(paper, now, mine)
        books.append(target if target is not None else held)
        lines.append({"session": session.date().isoformat(), "strategy": paper.id, "role": paper.role,
                      "targets": target, "fidelity": compared(targets(paper, now), mine, now.prices.index[-1]),
                      "live": {"since": (mine[0]["session"] if mine else session.date().isoformat()),
                               "return": round(since, 6)}})
    equity, orders, said = broker.equity(), [], []
    if any(line["targets"] is not None for line in lines):
        net = {}
        for weights in books:
            for ticker, weight in weights.items():
                net[ticker] = net.get(ticker, 0.0) + weight / len(books)
        orders = to_orders(net, equity, broker.holdings())
        waiting = broker.pending()                # an earlier run's orders, not yet filled: nothing is sent twice
        if waiting:
            said = [f"not sent: {waiting} order(s) of an earlier run pending"] * len(orders)
        else:
            said = broker.send(orders)
    for line in lines:
        line["account"] = {"equity": round(equity, 2), "orders": [{**o, "status": s} for o, s in zip(orders, said)]}
    folder.mkdir(parents=True, exist_ok=True)
    with log.open("a") as rows:
        rows.write("".join(json.dumps(line, separators=(",", ":")) + "\n" for line in lines))
    everything = read_log(log)
    (folder / "live.json").write_text(json.dumps(summary(everything), indent=1) + "\n")
    (folder / "README.md").write_text(page(everything))
    return lines


# --------------------------------------------------------------------------- what is shown


def summary(log: list[dict]) -> dict:
    """Each strategy's paper trading at its last line: its role, since when, whether it still trades,
    its sessions, its signals compared with the backtest's, and its return since its first session,
    which is shown, while gate 8 decides on the signals alone."""
    last = {}
    for line in log:
        last[line["strategy"]] = (line, last.get(line["strategy"], (None, 0))[1] + 1)
    latest = max((line["session"] for line in log), default=None)
    return {strategy: {"role": line["role"], "since": line["live"]["since"], "last": line["session"],
                       "trading": line["session"] == latest, "sessions": count,
                       "compared": line["fidelity"]["compared"], "identical": line["fidelity"]["identical"],
                       "gaps": line["fidelity"]["gaps"], "return": line["live"]["return"]}
            for strategy, (line, count) in last.items()}


def targets_text(targets: dict | None) -> str:
    if targets is None:
        return "holds"
    held = [f"{t} {w:.1%}" for t, w in targets.items() if w > 0]
    return ", ".join(held) if held else "cash"


def page(log: list[dict]) -> str:
    """The tracking page: each strategy's paper trading, then its sessions one by one."""
    out = ["# Paper trading", "",
           "Gate 8 of the lab: after every US close, each strategy under paper trading sets its targets for",
           "the next session on a paper account, and its live signal is compared with the backtest's signal",
           "for the same session once that session's close is known. Gate 8 asks for identical signals over",
           "two to four weeks. A test of the chain is a strategy traded only to prove the job, not a",
           "survivor.", "",
           "| Strategy | Role | Since | Sessions | Signals identical | Return |", "|---|---|---|---|---|---|"]
    for strategy, s in summary(log).items():
        since = s["since"] if s["trading"] else f"{s['since']} to {s['last']}"
        out.append(f"| {strategy} | {s['role']} | {since} | {s['sessions']} | {s['identical']} of "
                   f"{s['compared']} | {s['return']:+.2%} |")
    for strategy in summary(log):
        out += ["", f"## {strategy}", "", "| Session | Targets | Signals identical so far | Account |",
                "|---|---|---|---|"]
        for line in (line for line in log if line["strategy"] == strategy):
            fidelity = line["fidelity"]
            gaps = f" (gaps: {', '.join(fidelity['gaps'])})" if fidelity["gaps"] else ""
            unsent = sum(order["status"].startswith(UNSENT) for order in line["account"]["orders"])
            account = f"{line['account']['equity']:,.2f}" + (f" ({unsent} order(s) not sent)" if unsent else "")
            out.append(f"| {line['session']} | {targets_text(line['targets'])} | {fidelity['identical']} of "
                       f"{fidelity['compared']}{gaps} | {account} |")
    return "\n".join(out) + "\n"


def take(lab: Path = LAB, fetched: str | None = None) -> Path:
    """The job's summary, from its branch in the public repository, into `paper/live.json`, and the
    board regenerated: the board shows each strategy's paper trading as the branch did then."""
    if fetched is None:
        subprocess.run(["git", "fetch", "-q", f"{status.PUBLIC}.git", "paper"], cwd=lab, check=True,
                       capture_output=True)
        fetched = subprocess.run(["git", "show", "FETCH_HEAD:paper/live.json"], cwd=lab, check=True,
                                 capture_output=True, text=True).stdout
    kept = lab / "paper" / "live.json"
    kept.parent.mkdir(exist_ok=True)
    kept.write_text(json.dumps(json.loads(fetched), indent=1) + "\n")
    return status.write(lab, lab / "registry" / "trials.jsonl")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    which = parser.add_mutually_exclusive_group(required=True)
    which.add_argument("--log", type=Path, help="the folder of the log, its page and its summary")
    which.add_argument("--take", action="store_true", help="the job's summary into paper/, and the board")
    args = parser.parse_args(argv)
    if args.take:
        print(take(), file=sys.stderr)
        return 0
    broker = Alpaca()
    today = settled(broker, pd.Timestamp.now(tz=NEW_YORK))
    lines = day(broker, yahoo, args.log, today)
    if not lines:
        print(f"{today}: its lines are written, or no strategy is under paper trading; nothing to do")
    for line in lines:
        print(f"{line['strategy']} ({line['role']}), session {line['session']}: {targets_text(line['targets'])}; "
              f"signals identical {line['fidelity']['identical']} of {line['fidelity']['compared']}")
    for order in (lines[0]["account"]["orders"] if lines else []):
        if order["status"].startswith(UNSENT):
            print(f"{order['side']} {order['symbol']}: {order['status']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
