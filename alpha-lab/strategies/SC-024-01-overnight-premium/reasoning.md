# SC-024-01 — The overnight return premium: reasoning, not testable

## The theory, and the form its sources give it

SC-024 holds that a large part of the return on equities is earned while the market is closed,
overnight, from one close to the next open, whereas the return from the open to the close is weak or
of the opposite sign; the books attribute it to the way market makers, specialists and the opening
mechanisms handle the imbalance of orders that accumulates overnight, which the public does not see.
Its prediction: close-to-open returns account for a large share of equity returns, open-to-close
returns are weak and can be of the opposite sign, and the overnight change is strongly and
negatively correlated with the intraday change that follows it. Its refutations: overnight and
intraday returns of similar average size; no negative autocorrelation between the overnight change
and the following intraday change; a premium and reversal unrelated to the order imbalance handled
at the open; the same pattern where the information on opening orders is available to everyone.

**Its sources, as the lab read them in the library's books.**

- **Cooper, Cliff and Gulen (2008)**, as Dzhabarov and Ziemba report them in the Zacks *Handbook of
  Equity Market Anomalies* (2011, chapter 9, section "Open/Close Daily Trade on the Open") and in
  Ziemba's *Calendar Anomalies and Arbitrage* (2012, §1.11): the US equity premium from 1993 to 2006
  earned entirely overnight, the intraday return close to zero; the difference between night and day
  returns between 2.61 and 7.61 basis points a day, robust across asset types, subperiods and
  markets, among them the Chicago Mercantile Exchange's; risk, earnings surprises and illiquidity do
  not substantially explain it, which they read as an inefficiency of the opening and closing
  mechanisms, with tradable implications for those "with low marginal trading costs".
- **Branch and Ma (2006)**, in the same two places: a very strong negative autocorrelation between
  the overnight return and the intraday return, in NYSE, AMEX and NASDAQ stocks over two periods
  from 1994 to 2005 and in every size group; they trace it to how specialists and market makers open
  their stocks against the previous close, and conclude that only market makers, who know the
  balance of overnight orders, can exploit it; for the public, their actionable conclusion is to
  avoid orders executed at the open.
- **Lou, Polk and Skouras (2019)**, as Ilmanen reports them (*Investing Amid Low Expected Returns*,
  2022, box 5.2): much of the equity premium and all of momentum's profits earned overnight, many
  defensive strategies better during the day; overnight returns predicting the next overnight
  returns positively and the next intraday returns negatively; explanations in market makers'
  compensation for overnight inventory, a tug of war between retail investors trading in the morning
  and institutions near the close, and persistent execution flows.
- **Harris (1986)**, the bank's first reference, in *Stock Market Anomalies* (Dimson, ed., 1988,
  chapter 7): on NYSE transactions from December 1981 to January 1983, the Monday decline of large
  firms accrues before the open and that of small firms mostly during Monday's trading; weekday
  differences appear only in the first 45 minutes of trading; prices rise on the day's last trade.
  Lo and MacKinlay (*A Non-Random Walk Down Wall Street*, 1999) mention calendar effects in passing
  and note that overnight price changes behave differently from intraday ones.
- **Japan**: Kato, Schwartz and Ziemba (*Calendar Anomalies and Arbitrage*, chapter 13) find on the
  TOPIX from January 1982 to June 1987 a close-to-open return of +0.0855% a day (t 10.47) and an
  open-to-close return of −0.0135%, "all gains overnight", which they trace to orders collected
  after the close; in chapter 18, Bell and Ziemba (1993) find that the only anomaly left in Japan
  from 1990 to 1993 was that all the market's gains came at night, close to open.
- **Against the claim for large US stocks**: Keim and Smirlock (1987), in Keim and Ziemba's
  *Security Market Imperfections in Worldwide Equity Markets* (2000): from April 1982 to December
  1986 the S&P 500 made most of its gains during the day, while the Value Line index of small stocks
  made all of its gains at night. And the weekend's closed period, Rogalski (1984) as Dimson's
  volume reports him, carried a negative return, from Friday's close to Monday's open (t −3.46),
  over years in which the close-to-close Monday was only weakly negative (t −0.62): Monday's trading
  recovered, as Branch and Ma's reversal would have it, the opposite sign to a premium; Harris, and
  Smirlock and Starks, as the same volume reports them, find part of the Monday loss during trading.
- **The gap's continuation**: Kaufman (*Trading Systems and Methods*, chapter 15) finds S&P futures
  from 2000 to May 2011 making most of their move overnight and in the first bar, with the gap's
  direction continuing during the day, against Branch and Ma; Chan (*Algorithmic Trading*, 2013,
  chapter 7) trades the opening gap's momentum on index futures, and in chapter 4 its reversal on
  stocks, the buy-on-gap model, each entering at the open and leaving at the close.

The library thus reports an overnight premium in US stocks from 1993 to 2006 and in Japan in the
1980s and early 1990s, but not in the S&P 500 from 1982 to 1986, and both a reversal and a
continuation of the overnight move during the day.

## Why the lab cannot test it

The claim divides each day at the open, and the lab's backtest cannot. Its market holds one price
per asset and session, the close; its engine takes targets set at a close, from data up to the
session before, and fills them at that close; its returns run from close to close. The snapshot's
files carry each fund's opening price beside its close, but nothing in the lab's code reads it, and
no rule the battery can judge holds a fund from a close to the next open and not during the day, or
the reverse. Every refutation the bank names sets a close-to-open return against an open-to-close
one, or against the order imbalance at the open, which the lab's data does not hold. The lab has
held single sessions (SC-001-01's variant, SC-014-01): the hold shorter than a session is what is
new, and the wall is the engine's fills and a market without opens.

**What was considered, and why it does not rescue the test:**

- **A rule held from the close to the next open**, the premium's own trade, on SPY or the equity
  funds: it needs fills at the open, a change to the engine, not a card. At the lab's costs it would
  also fail gate 2 at any overnight return the library reports: a round trip each session at 5 basis
  points a side costs 10 basis points a day, about 25% a year, and 20 at gate 2's doubled costs,
  against at most 7.61 basis points a day for Cooper, Cliff and Gulen's night-less-day difference
  and 8.55 for Tokyo's close-to-open return from 1982 to 1987. That failure depends on the prices,
  so the judgement does not rest on it; the sources themselves put the trade's use with those whose
  marginal costs are low.
- **Trading the reversal or the continuation**, Branch and Ma's pattern or Kaufman's, Chan's
  buy-on-gap or opening-gap models: each enters at the open and leaves at the close, with the same
  needs and a round trip a day; Branch and Ma themselves see the reversal open to market makers
  only.
- **Ranking or timing the funds on their past overnight returns and holding them from close to
  close**, Lou, Polk and Skouras's persistence read over several days, or Carver's "Close to Open"
  forecast (*Systematic Trading*), the gap scaled by volatility, which he offers untested: the
  signal would read the openings, which the lab's market does not hold, and the holding would earn
  both halves of the day, which Lou, Polk and Skouras sign opposite ways — the next overnight return
  positive, the next intraday negative — so that no source in the library gives the close-to-close
  return a sign.
- **The closures a close-only rule can hold**: the weekend, which SC-001-01 read on close-to-close
  returns and which stopped at gate 2; the sessions before holidays, SC-014-01's. No source in the
  library says that sessions spanning longer closures earn more, and the part of the weekend that
  lies before the open is the same division of the day.

What would make it testable: an engine that fills at the open as well as at the close, and a market
that carries the opens, both beyond a card; costs below the premium, as the sources say, which a
fund's round trip each day does not have; and, for the third and fourth refutations, the order
imbalance at the open, a new kind of data. The lab's paper trading already sends its orders for the
next open, but it compares signals, not fills.

## Status

SC-024 is recorded `not-testable`: its claim and its refutations divide the day at the open, and the
lab's backtest holds only closes and fills only at them; the forms a close-only rule could hold read
the openings and have no sourced sign from close to close, or are SC-001-01's and SC-014-01's
closures. No card is drawn, and no trial is spent.
