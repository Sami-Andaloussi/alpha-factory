"""Gate 8: the paper account's one address, its keys kept out of sight, and a day of paper trading
on a fake broker and a synthetic market: the next session's targets, the orders, the log, and the
live signal compared with the backtest's."""
import ast
import hashlib
import http.server
import io
import json
import re
import sys
import threading
import urllib.error
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from lab import paper, registry

SOURCE = Path(paper.__file__)
TICKERS = ("SPY", "EFA", "IEF", "GLD")
DAYS = pd.bdate_range("2019-01-01", "2020-06-30")


def momentum(market, span):
    """Daily: each asset whose close before the session beats its close `span` sessions earlier."""
    prices = market.prices
    up = (prices.shift(1) > prices.shift(1 + span)) & market.tradable
    return up.astype(float) / prices.shape[1]


def peeking(market, span):
    """The same, reading the session's own close: a look-ahead gate 8 must see."""
    prices = market.prices
    up = (prices > prices.shift(span)) & market.tradable
    return up.astype(float) / prices.shape[1]


def monthly(market, span):
    weights = momentum(market, span)
    first = pd.Series(np.r_[True, weights.index.month[1:] != weights.index.month[:-1]], index=weights.index)
    return weights.where(first, axis=0)


def strategy(function, name="demo-01"):
    return paper.Paper(name, "test of the chain", TICKERS, {"span": 20}, function)


@pytest.fixture
def bars():
    rng = np.random.default_rng(7)
    full = {t: pd.DataFrame({"Open": p, "High": p, "Low": p, "Close": p, "Volume": 1.0}, index=DAYS)
            for t, p in ((t, 100 * np.exp(np.cumsum(rng.normal(0.0003, 0.01, len(DAYS))))) for t in TICKERS)}
    irx = pd.DataFrame({"Close": 2.0}, index=DAYS)

    def drawn(tickers, through):
        cut = pd.Timestamp(through)
        return {t: full[t].loc[:cut] for t in tickers}, irx.loc[:cut]
    return drawn


class Broker:
    """A fake paper account: the exchange's sessions, and orders filled as sent."""

    def __init__(self):
        self.held, self.sent = {}, []

    def calendar(self, start, end):
        return {d.date(): pd.Timestamp(f"{d.date()} 16:00", tz="America/New_York") for d in DAYS
                if start <= d.date() <= end}

    def equity(self):
        return 100_000.0

    def holdings(self):
        return dict(self.held)

    def pending(self):
        return 0

    def send(self, orders):
        self.sent.append(orders)
        for order in orders:
            if order.get("whole"):
                self.held.pop(order["symbol"])
            else:
                sign = 1 if order["side"] == "buy" else -1
                self.held[order["symbol"]] = self.held.get(order["symbol"], 0.0) + sign * order["notional"]
        return ["accepted"] * len(orders)


# --------------------------------------------------------------------------- the address and the keys


def test_the_paper_address_is_the_only_one_and_is_written_in_the_file():
    assert paper.PAPER == "https://paper-api.alpaca.markets"
    tree = ast.parse(SOURCE.read_text())
    texts = [node.value for node in ast.walk(tree) if isinstance(node, ast.Constant) and isinstance(node.value, str)]
    assert set(re.findall(r"[\w.-]*alpaca\.markets", SOURCE.read_text(), re.I)) == {"paper-api.alpaca.markets"}
    assert [t for t in texts if "alpaca.markets" in t.lower()] == [paper.PAPER]         # no other host of Alpaca's
    assert [t for t in texts if t.startswith("APCA_")] == list(paper.KEYS)             # the keys, and no base URL
    assert "getenv" not in SOURCE.read_text() and "BASE_URL" not in SOURCE.read_text().upper()
    requests = [node for node in ast.walk(tree) if isinstance(node, ast.Call) and getattr(node.func, "attr", "") == "Request"]
    assert requests and all(isinstance(r.args[0], ast.BinOp) and isinstance(r.args[0].left, ast.Name)
                            and r.args[0].left.id == "PAPER" for r in requests)   # every request goes to PAPER
    bound = [node for node in ast.walk(tree) if isinstance(node, (ast.Name, ast.Attribute)) and
             (getattr(node, "id", None) or getattr(node, "attr", None)) == "PAPER" and isinstance(node.ctx, ast.Store)]
    assert len(bound) == 1 and not any(isinstance(n, (ast.Global, ast.Nonlocal)) for n in ast.walk(tree))
    assert any(isinstance(n, ast.Assign) and n.targets == [bound[0]] and isinstance(n.value, ast.Constant)
               and n.value.value == paper.PAPER for n in tree.body)           # once, at the top, to the literal
    request = requests[0].args[0]
    assert len(requests) == 1 and isinstance(request.op, ast.Add) and isinstance(request.right, ast.Name) \
        and request.right.id == "path"                                    # PAPER + path, and nothing between
    call = next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "_call")
    assert not [n for n in ast.walk(call) if isinstance(n, ast.Name) and n.id == "path" and isinstance(n.ctx, ast.Store)]
    assert not re.search(r"__import__|importlib|getattr\(os", SOURCE.read_text())
    reads = [n for n in ast.walk(tree) if isinstance(n, ast.Subscript) and getattr(n.value, "id", "") == "environ"]
    reads += [n for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
              and getattr(n.func.value, "id", "") == "environ"]
    for read in reads:                                                    # the environment is read for the keys alone
        key = read.slice if isinstance(read, ast.Subscript) else read.args[0]
        assert (isinstance(key, ast.Name) and key.id == "key") or (isinstance(key, ast.Subscript)
                                                                    and getattr(key.value, "id", "") == "KEYS")
    loops = [n for n in ast.walk(tree) if isinstance(n, ast.comprehension) and getattr(n.target, "id", "") == "key"]
    assert loops and all(getattr(n.iter, "id", "") == "KEYS" for n in loops)
    environ = [n for n in ast.walk(tree) if isinstance(n, ast.Name) and n.id == "environ"]
    alpaca = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "Alpaca")
    inside = {id(n) for n in ast.walk(alpaca)}
    assert environ and all(id(n) in inside for n in environ)          # the environment is read by the adapter alone
    assert "os.environ" not in SOURCE.read_text().replace("environ=os.environ", "")


class Answers:
    """Alpaca's paper account as canned answers: every request's address is kept."""

    def __init__(self, refuse=()):
        self.urls, self.sent, self.refuse = [], [], refuse

    def open(self, request, timeout):
        self.urls.append(request.full_url)
        self.sent.append((request.get_method(), json.loads(request.data) if request.data else None))
        path = request.full_url.split(".markets", 1)[1]
        if any(path.startswith(r) for r in self.refuse):
            raise urllib.error.HTTPError(request.full_url, 422, "Unprocessable", {}, io.BytesIO(b'{"message":"no"}'))
        answer = {"/v2/account": {"equity": "100000.5"},
                  "/v2/positions": [{"symbol": "SPY", "market_value": "2500.25"},
                                    {"symbol": "BTCUSD", "market_value": "99.5"}],
                  "/v2/orders?status=open": [],
                  "/v2/calendar": [{"date": "2026-11-27", "open": "09:30", "close": "13:00"},
                                   {"date": "2026-11-30", "open": "09:30", "close": "16:00"}],
                  "/v2/orders": {"status": "accepted"}, "/v2/positions/SPY": {"status": "pending_new"},
                  "/v2/positions/BTCUSD": {"status": "pending_new"}}
        body = next(value for key, value in answer.items() if path == key or path.startswith(key + "?")
                    or (key == "/v2/calendar" and path.startswith(key)))
        return io.BytesIO(json.dumps(body).encode())


def test_every_request_goes_to_the_paper_address_and_no_redirect_is_followed(monkeypatch):
    assert any(isinstance(handler, paper.Refused) for handler in paper.OPENER.handlers)
    answers = Answers()
    monkeypatch.setattr(paper, "OPENER", answers)
    broker = paper.Alpaca({"APCA_API_KEY_ID": "KEY-ID-123", "APCA_API_SECRET_KEY": "SECRET-456"})
    assert broker.equity() == 100000.5 and broker.holdings() == {"SPY": 2500.25, "BTC-USD": 99.5}
    assert broker.pending() == 0
    days = broker.calendar(date(2026, 11, 26), date(2026, 11, 30))
    assert days[date(2026, 11, 27)] == pd.Timestamp("2026-11-27 13:00", tz="America/New_York")   # a half day
    assert broker.send([{"symbol": "SPY", "side": "sell", "whole": True},
                        {"symbol": "IEF", "side": "buy", "notional": 1234.5}]) == ["pending_new", "accepted"]
    assert answers.sent[-2:] == [("DELETE", None), ("POST", {"symbol": "IEF", "side": "buy", "type": "market",
                                                               "time_in_force": "day", "notional": "1234.50"})]
    assert broker.send([{"symbol": "BTC-USD", "side": "sell", "whole": True},              # bitcoin, as Alpaca names it
                        {"symbol": "BTC-USD", "side": "buy", "notional": 50.0}]) == ["pending_new", "accepted"]
    assert answers.urls[-2].endswith("/v2/positions/BTCUSD")
    assert answers.sent[-1] == ("POST", {"symbol": "BTC/USD", "side": "buy", "type": "market", "time_in_force": "gtc",
                                         "notional": "50.00"})
    assert answers.urls and all(url.startswith("https://paper-api.alpaca.markets/v2/") for url in answers.urls)
    assert paper.Refused().redirect_request(None, None, 302, "Found", {}, "https://elsewhere.example/") is None


def test_the_opener_stops_at_a_redirect():
    class Moved(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(302)
            self.send_header("Location", "http://127.0.0.1:9/elsewhere")
            self.end_headers()

        def log_message(self, *args):
            pass

    server = http.server.HTTPServer(("127.0.0.1", 0), Moved)
    thread = threading.Thread(target=server.handle_request, daemon=True)
    thread.start()
    try:
        with pytest.raises(urllib.error.HTTPError) as stopped:
            paper.OPENER.open(f"http://127.0.0.1:{server.server_port}/v2/account", timeout=5)
        assert stopped.value.code == 302
    finally:
        thread.join(5)
        server.server_close()


def test_an_order_the_broker_refuses_is_said_and_the_others_are_sent(monkeypatch):
    answers = Answers(refuse=("/v2/positions/SPY",))
    monkeypatch.setattr(paper, "OPENER", answers)
    broker = paper.Alpaca({"APCA_API_KEY_ID": "KEY-ID-123", "APCA_API_SECRET_KEY": "SECRET-456"})
    said = broker.send([{"symbol": "SPY", "side": "sell", "whole": True},
                        {"symbol": "IEF", "side": "buy", "notional": 10.0}])
    assert said[0].startswith("refused: the broker answered 422") and said[1] == "accepted"
    assert "KEY-ID-123" not in str(said) and "SECRET-456" not in str(said)
    with pytest.raises(RuntimeError, match="would leave the paper account's address"):
        broker._call("GET", "@elsewhere.example/v2/account")                  # checked as it runs, too
    assert not any("elsewhere" in url for url in answers.urls)


def test_the_keys_are_never_shown(monkeypatch):
    secret = {"APCA_API_KEY_ID": "KEY-ID-123", "APCA_API_SECRET_KEY": "SECRET-456"}
    broker = paper.Alpaca(secret)
    seen = []

    class Refusing:
        def open(self, request, timeout):
            seen.append(request.full_url)
            raise urllib.error.HTTPError(request.full_url, 403, "Forbidden", {}, io.BytesIO(b'{"message":"forbidden"}'))

    class Failing:                                                      # a header refused as it is sent
        def open(self, request, timeout):
            raise ValueError(f"Invalid header value {secret['APCA_API_SECRET_KEY']!r}")
    monkeypatch.setattr(paper, "OPENER", Refusing())
    with pytest.raises(RuntimeError) as said:
        broker.equity()
    shown = str(said.value) + repr(broker) + repr(said.value.__cause__) + repr(said.value.__context__)
    assert "403" in shown and "KEY-ID-123" not in shown and "SECRET-456" not in shown
    assert seen == ["https://paper-api.alpaca.markets/v2/account"]
    monkeypatch.setattr(paper, "OPENER", Failing())
    with pytest.raises(RuntimeError) as said:
        broker.holdings()
    assert "ValueError" in str(said.value) and said.value.__cause__ is None and said.value.__context__ is None
    assert "SECRET-456" not in str(said.value)
    for wrong in ({"APCA_API_KEY_ID": "KEY-ID-123"}, {**secret, "APCA_API_SECRET_KEY": "SECRET-456\n"},
                  {**secret, "APCA_API_SECRET_KEY": " SECRET-456"}):
        with pytest.raises(RuntimeError, match="APCA_API_SECRET_KEY") as refused:
            paper.Alpaca(wrong)
        assert "KEY-ID-123" not in str(refused.value) and "SECRET-456" not in str(refused.value)


# --------------------------------------------------------------------------- orders


def test_orders_reach_the_targets_sales_first_and_skip_what_is_too_small():
    orders = paper.to_orders({"SPY": 0.5, "IEF": 0.25, "GLD": 0.0}, 100_000,
                             {"SPY": 20_000, "GLD": 10_000, "EEM": 5_000, "IEF": 24_990})
    assert orders == [{"symbol": "EEM", "side": "sell", "whole": True}, {"symbol": "GLD", "side": "sell", "whole": True},
                      {"symbol": "SPY", "side": "buy", "notional": 30_000.0}]        # IEF: $10 is too small
    orders = paper.to_orders({"AAA": 0.3, "ZZZ": 0.1}, 100_000, {"ZZZ": 25_000})
    assert orders == [{"symbol": "ZZZ", "side": "sell", "notional": 15_000.0},       # a part sold, and first
                      {"symbol": "AAA", "side": "buy", "notional": 30_000.0}]


# --------------------------------------------------------------------------- a day


def test_a_day_logs_the_next_session_s_targets_and_sends_their_orders(tmp_path, bars):
    broker = Broker()
    lines = paper.day(broker, bars, tmp_path, date(2020, 3, 2), [strategy(momentum)])
    assert [line["session"] for line in lines] == ["2020-03-03"]
    assert lines[0]["targets"] is not None and broker.sent and all(o["side"] == "buy" for o in broker.sent[0])
    assert lines[0]["fidelity"] == {"compared": 0, "identical": 0, "gaps": []}
    later = paper.day(broker, bars, tmp_path, date(2020, 3, 3), [strategy(momentum)])
    assert later[0]["fidelity"] == {"compared": 1, "identical": 1, "gaps": []}   # the live signal is the backtest's
    assert later[0]["live"]["since"] == "2020-03-03"
    log = paper.read_log(tmp_path / "log.jsonl")
    assert [line["session"] for line in log] == ["2020-03-03", "2020-03-04"]
    shown = json.loads((tmp_path / "live.json").read_text())["demo-01"]
    assert (shown["role"], shown["sessions"], shown["identical"], shown["compared"]) == ("test of the chain", 2, 1, 1)
    assert "| demo-01 | test of the chain | 2020-03-03 | 2 | 1 of 1 |" in (tmp_path / "README.md").read_text()


def test_a_strategy_that_reads_its_session_s_close_is_caught(tmp_path, bars):
    broker = Broker()
    paper.day(broker, bars, tmp_path, date(2020, 3, 2), [strategy(peeking)])
    lines = paper.day(broker, bars, tmp_path, date(2020, 3, 3), [strategy(peeking)])
    assert lines[0]["fidelity"]["gaps"] == ["2020-03-03"]


def test_a_session_that_holds_sends_no_order(tmp_path, bars):
    broker = Broker()
    lines = paper.day(broker, bars, tmp_path, date(2020, 3, 10), [strategy(monthly)])
    assert lines[0]["targets"] is None and broker.sent == []
    assert "| 2020-03-11 | holds |" in (tmp_path / "README.md").read_text()


def test_a_strategy_that_holds_beside_one_that_sets_targets_still_trades(tmp_path, bars):
    broker = Broker()
    lines = paper.day(broker, bars, tmp_path, date(2020, 3, 10), [strategy(monthly), strategy(momentum, "demo-02")])
    assert lines[0]["targets"] is None and lines[1]["targets"] and len(broker.sent) == 1


def test_the_bars_are_drawn_through_the_day_asked(monkeypatch):
    asked = []

    class Yahoo:
        __version__ = "0"

        @staticmethod
        def download(ticker, start, end, **options):
            asked.append((ticker, end))
            index = pd.bdate_range("2026-09-21", end, inclusive="left")
            return pd.DataFrame({field: 1.0 for field in ("Open", "High", "Low", "Close", "Volume")}, index=index)
    monkeypatch.setitem(sys.modules, "yfinance", Yahoo)
    raw, irx = paper.yahoo(["SPY", "IEF"], date(2026, 9, 24))
    assert asked == [("SPY", "2026-09-25"), ("IEF", "2026-09-25"), ("^IRX", "2026-09-25")]   # Yahoo's end is exclusive
    assert sorted(raw) == ["IEF", "SPY"] and irx.index[-1] == pd.Timestamp("2026-09-24")


def test_no_session_no_line_and_a_close_not_yet_known_is_refused(tmp_path, bars):
    assert paper.day(Broker(), bars, tmp_path, date(2020, 3, 7), [strategy(momentum)]) == []   # a Saturday
    assert not (tmp_path / "log.jsonl").exists()

    def late(tickers, through):
        return bars(tickers, pd.Timestamp(through) - pd.Timedelta(days=1))
    with pytest.raises(RuntimeError, match="the close is not known yet"):
        paper.day(Broker(), late, tmp_path, date(2020, 3, 3), [strategy(momentum)])

    def one_late(tickers, through):
        raw, irx = bars(tickers, through)
        return {t: frame.iloc[:-1] if t == "GLD" else frame for t, frame in raw.items()}, irx
    with pytest.raises(RuntimeError, match="the bars of GLD end before 2020-03-03"):
        paper.day(Broker(), one_late, tmp_path, date(2020, 3, 3), [strategy(momentum)])


def test_the_session_ahead_has_no_price_and_the_last_close_s_tradable_assets(bars):
    raw, irx = bars(TICKERS, date(2020, 3, 2))
    market = paper.live(raw, irx, pd.Timestamp("2020-03-03"))
    assert market.prices.index[-1] == pd.Timestamp("2020-03-03") and market.prices.iloc[-1].isna().all()
    assert market.tradable.iloc[-1].all() and market.rf.iloc[-1] == pytest.approx(2.0 / 100 / 252)


# --------------------------------------------------------------------------- which strategies


def line(card, variant=0, survivor=False, card_hash=None):
    return registry.compact({"time": "2026-01-01T00:00:00Z", "card": card, "card_hash": card_hash or card[0] * 64,
                             "variant": variant, "sharpe": 0.1, "monthly": {"2020-01": 0.01}, "gates": {},
                             "failed": None if survivor else 3, "survivor": survivor})


def test_the_first_strategy_is_a_test_of_the_chain_until_a_survivor(tmp_path):
    for card in ("a-01", "b-01"):
        folder = tmp_path / "strategies" / card
        folder.mkdir(parents=True)
        (folder / "card.yaml").write_text(f"id: {card}\nuniverse: [SPY, IEF]\nvariants:\n  - {{span: 20}}\n  - {{span: 10}}\n")
        (folder / "strategy.py").write_text("def positions(market, span):\n    return None\n")
    held = {card: hashlib.sha256((tmp_path / "strategies" / card / "card.yaml").read_bytes()).hexdigest()
            for card in ("a-01", "b-01")}
    trials = tmp_path / "registry" / "trials.jsonl"
    trials.parent.mkdir()
    trials.write_text("\n".join([line("a-01", card_hash=held["a-01"]), line("a-01", 1, card_hash=held["a-01"]),
                                 line("b-01", card_hash=held["b-01"])]) + "\n")
    chosen = paper.papered(tmp_path, trials)
    assert [(p.id, p.role, p.universe, p.parameters) for p in chosen] == [("a-01", "test of the chain", ("SPY", "IEF"),
                                                                           {"span": 20})]
    trials.write_text("\n".join([line("a-01", card_hash=held["a-01"]),
                                 line("b-01", survivor=True, card_hash=held["b-01"])]) + "\n")
    assert [(p.id, p.role) for p in paper.papered(tmp_path, trials)] == [("b-01", "survivor")]
    (tmp_path / "strategies" / "b-01" / "gate-8.md").write_text("Gate 8 passes.\n")          # its gate 8 concluded
    assert paper.papered(tmp_path, trials) == []
    (tmp_path / "strategies" / "b-01" / "gate-8.md").unlink()
    (tmp_path / "strategies" / "b-01" / "card.yaml").write_text("id: b-01\nuniverse: [SPY]\nvariants:\n  - {span: 9}\n")
    with pytest.raises(RuntimeError, match="differs from the one that ran"):
        paper.papered(tmp_path, trials)


def test_two_strategies_share_the_account_in_equal_parts(tmp_path, bars):
    def cash(market, span):
        return momentum(market, span) * 0.0

    broker = Broker()
    lines = paper.day(broker, bars, tmp_path, date(2020, 3, 2), [strategy(momentum), strategy(cash, "demo-02")])
    alone = sum(w for w in lines[0]["targets"].values()) * 100_000
    assert sum(o["notional"] for o in broker.sent[0]) == pytest.approx(alone / 2, abs=0.05)   # the other half in cash
    assert [line["strategy"] for line in lines] == ["demo-01", "demo-02"]
    later = paper.day(broker, bars, tmp_path, date(2020, 3, 3), [strategy(momentum), strategy(cash, "demo-02")])
    assert all(np.isfinite(line["live"]["return"]) for line in later)


def test_the_day_is_the_last_close_past_and_a_session_is_written_once(tmp_path, bars):
    broker = Broker()
    assert paper.settled(broker, pd.Timestamp("2020-03-03 15:59", tz="America/New_York")) == date(2020, 3, 2)
    assert paper.settled(broker, pd.Timestamp("2020-03-03 16:00", tz="America/New_York")) == date(2020, 3, 3)
    assert paper.settled(broker, pd.Timestamp("2020-03-08 09:00", tz="America/New_York")) == date(2020, 3, 6)
    assert paper.day(broker, bars, tmp_path, date(2020, 3, 2), [strategy(momentum)])
    assert paper.day(broker, bars, tmp_path, date(2020, 3, 2), [strategy(momentum)]) == []     # run twice
    assert len(paper.read_log(tmp_path / "log.jsonl")) == 1 and len(broker.sent) == 1


def test_the_board_shows_each_strategy_under_paper_trading_as_the_branch_did(tmp_path, bars):
    folder = tmp_path / "strategies" / "demo-01"
    folder.mkdir(parents=True)
    (folder / "card.yaml").write_text("id: demo-01\ntheory: DEMO-1\nuniverse: [SPY, IEF]\nvariants:\n  - {span: 20}\n")
    (tmp_path / "bank").mkdir()
    (tmp_path / "registry").mkdir()
    (tmp_path / "registry" / "trials.jsonl").write_text(line("demo-01", card_hash=hashlib.sha256(
        (folder / "card.yaml").read_bytes()).hexdigest()) + "\n")
    branch = tmp_path / "branch"
    paper.day(Broker(), bars, branch, date(2020, 3, 2), [strategy(momentum)])
    paper.day(Broker(), bars, branch, date(2020, 3, 3), [strategy(momentum)])
    board = paper.take(tmp_path, (branch / "live.json").read_text())
    shown = board.read_text()
    assert json.loads((tmp_path / "paper" / "live.json").read_text()) == json.loads((branch / "live.json").read_text())
    assert "1 under paper trading" in shown
    assert "gate 8 since 2020-03-03, a test of the chain: 1 of 1 signals identical" in shown
    assert "[log](https://github.com/Sami-Andaloussi/alpha-factory/blob/paper/paper/README.md)" in shown
    (folder / "gate-8.md").write_text("Gate 8 passes.\n")                  # concluded, and the branch not yet told
    shown = paper.take(tmp_path, (branch / "live.json").read_text()).read_text()
    assert "under paper trading" not in shown and "gate 8 from 2020-03-03 to 2020-03-04, a test of the chain" in shown


def test_the_book_earns_what_its_live_targets_hold_and_a_strategy_that_stops_is_shown_so(tmp_path, bars):
    def spy(market, span):
        weights = momentum(market, span) * 0.0
        weights["SPY"] = 1.0
        return weights

    broker = Broker()
    for day in (date(2020, 3, 2), date(2020, 3, 3), date(2020, 3, 4)):
        lines = paper.day(broker, bars, tmp_path, day, [strategy(spy)])
    raw, _ = bars(TICKERS, date(2020, 3, 4))
    close = raw["SPY"]["Close"]
    grew = close.loc["2020-03-04"] / close.loc["2020-03-03"] * (1 - 0.0005) - 1
    assert lines[0]["live"] == {"since": "2020-03-03", "return": pytest.approx(grew, abs=2e-4)}
    paper.day(broker, bars, tmp_path, date(2020, 3, 5), [strategy(momentum, "demo-02")])       # the first one stops
    shown = json.loads((tmp_path / "live.json").read_text())
    assert (shown["demo-01"]["trading"], shown["demo-02"]["trading"]) == (False, True)
    assert "| demo-01 | test of the chain | 2020-03-03 to 2020-03-05 |" in (tmp_path / "README.md").read_text()


def test_orders_wait_while_an_earlier_run_s_are_pending(tmp_path, bars):
    broker = Broker()
    broker.pending = lambda: 3
    lines = paper.day(broker, bars, tmp_path, date(2020, 3, 2), [strategy(momentum)])
    orders = lines[0]["account"]["orders"]
    assert broker.sent == [] and orders and all(o["status"].startswith("not sent: 3 order(s)") for o in orders)
    assert f"({len(orders)} order(s) not sent)" in (tmp_path / "README.md").read_text()


def test_a_strategy_that_holds_keeps_its_book_while_another_trades(tmp_path, bars):
    def spy_monthly(market, span):
        weights = market.prices * 0.0
        weights["SPY"] = 1.0
        first = pd.Series(np.r_[True, weights.index.month[1:] != weights.index.month[:-1]], index=weights.index)
        return weights.where(first, axis=0)

    def gld_daily(market, span):
        weights = market.prices * 0.0
        weights["GLD"] = 1.0
        return weights

    broker = Broker()
    papers = [strategy(spy_monthly), strategy(gld_daily, "demo-02")]
    for day in (date(2020, 2, 28), date(2020, 3, 2), date(2020, 3, 3)):
        lines = paper.day(broker, bars, tmp_path, day, papers)
    assert lines[0]["targets"] is None and lines[1]["targets"]["GLD"] == 1.0         # the monthly one holds
    assert broker.held["SPY"] > 40_000 and len(broker.sent) == 3                     # and keeps its half
    assert not any(order["symbol"] == "SPY" and (order.get("whole") or order["notional"] > 5_000)
                   for orders in broker.sent[1:] for order in orders)


def test_the_job_says_what_was_not_sent_and_never_a_key(tmp_path, bars, monkeypatch, capsys):
    class Refusing(Broker):
        _headers = {"APCA-API-SECRET-KEY": "SECRET-456"}

        def send(self, orders):
            return ["refused: the broker answered 403 to POST /v2/orders: {}"] * len(orders)
    monkeypatch.setattr(paper, "Alpaca", Refusing)
    monkeypatch.setattr(paper, "yahoo", bars)
    monkeypatch.setattr(paper, "settled", lambda broker, now: date(2020, 3, 2))
    monkeypatch.setattr(paper, "papered", lambda: [strategy(momentum)])
    assert paper.main(["--log", str(tmp_path)]) == 0
    said = capsys.readouterr()
    assert "refused: the broker answered 403" in said.out and "SECRET-456" not in said.out + said.err


def test_a_registry_line_whose_folder_is_gone_stops_the_job_and_says_so(tmp_path):
    trials = tmp_path / "registry" / "trials.jsonl"
    trials.parent.mkdir()
    trials.write_text(line("gone-01") + "\n")
    with pytest.raises(RuntimeError, match="gone-01: its registry line names a folder that holds no card"):
        paper.papered(tmp_path, trials)
