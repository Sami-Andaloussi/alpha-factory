# TM-027-01 — Volume-conditioned momentum: reasoning, not testable as a theory of its own

## The theory, and the forms its sources give it

TM-027 holds that the strength and persistence of momentum depend on the volume that accompanies the
price move: stocks, or futures contracts, whose past moves came with high volume show stronger
momentum than those whose moves came with low volume — Lee and Swaminathan (2000) report momentum
about three times larger among the highest-turnover stocks — and past volume would place momentum in
its life cycle, early or late, some configurations signalling its exhaustion. Its refutations:
momentum no stronger among high-volume stocks or contracts than among low-volume ones with the same
past return; the strength and persistence of momentum unrelated to turnover and volume; past volume
carrying no information about the phase of momentum. The bank names stocks, equity indices, bonds,
currencies and commodities, and as data daily prices, trading volumes and open interest.

**Its source, as the lab read it in the library.** The library holds Lee and Swaminathan in others'
reports.

- **Jegadeesh and Titman**, "Momentum", chapter 10 of *Advances in Behavioral Finance, Volume II*
  (Thaler, ed., 2005), table 10.9: NYSE and AMEX stocks from 1964 to 1995, sorted independently on
  their past six months' return into ten portfolios and on their past six months' average daily
  turnover into three. The winners less the losers earn 0.54% a month among the lowest-turnover
  stocks (t 2.07), 1.11% in the middle (t 4.46) and 1.46% among the highest (t 5.93), a difference
  of 0.91% a month (t 4.61). The difference comes from the losers: the high-turnover losers earn
  0.09% a month against 1.12% for the low-turnover ones (a difference of −1.04%, t −5.19), while the
  winners earn 1.55% among the highest-turnover stocks against 1.67% among the lowest (−0.12%, t
  −0.67). The authors read turnover as disagreement or attention; they note that high-turnover
  stocks have more analysts and institutions and trade more cheaply, which makes the finding
  surprising for them.
- **The Zacks *Handbook of Equity Market Anomalies*** (2011): conditional on past returns,
  low-volume firms outperform high-volume ones over the next year — low-volume losers by 1.02% a
  month and low-volume winners by 0.26% in a nine-month/six-month strategy — and high-volume winners
  and low-volume losers reverse faster; Lee and Swaminathan tie the life cycle of momentum to
  volume.
- **Gray and Vogel** (*Quantitative Momentum*, 2016, chapter 6), after Hong, Lim and Stein's larger
  momentum where attention is low, find that splitting high-momentum stocks on trading volume, more
  volume standing for more attention, gives similar results: among winners the less-traded do
  better; no figures.
- **Aronson** (*Evidence-Based Technical Analysis*, 2007, chapter 7 and its note 56) and **Shefrin**
  (*Beyond Greed and Fear*) read the paper as high-volume winners doing better than winners alone
  (Shefrin: "buy high-volume winners"); Aronson adds that at three years the low-volume winners
  persist on the upside. **O'Shaughnessy** (*What Works on Wall Street*, 4th edition, chapter 20),
  on his own data, finds the highest decile of six-month dollar volume compounding at 8.09% a year
  from 1964 to 2009 and the lowest at 13.16%, and suggests penalising high volume within momentum;
  **Campbell** (*Financial Decisions and Markets*, 2018, section 3.3.2) reports turnover negatively
  associated with returns at 3 to 12 months; *Finding Alphas* (chapter 21) cites Lee and
  Swaminathan's result.

The factor of three the bank reports is the winners-less-losers spread; among winners alone the
high-turnover ones earned less, 1.55% a month against 1.67% (−0.12%, t −0.67), and the Zacks
handbook reports low-volume winners ahead by 0.26%. The long side's sign, where the library gives
one with figures, favours low volume, TM-028's claim; Aronson's and Shefrin's reading of the long
side is not the table's. Every sign is on single stocks sorted by each stock's own turnover.

## What the lab can read of it, and where each form already stands

The lab holds the daily closes of funds and of bitcoin, and the Treasury bill's yield. The
snapshot's files hold the funds' traded volumes, but the lab passes a strategy its closes only
(SC-013-01, SC-015-01), and trades no futures, so holds no open interest. On those data, each of
TM-027's forms is unreadable, has no sign for funds, or is already read:

- **Momentum stronger with high turnover**: each stock's own turnover, among stocks. A fund's volume
  is its own shares changing hands on the exchange among hedge funds, traders and institutions,
  about four times the creations and redemptions over all ETFs, and often with none at all — EEM
  traded about $50 billion from 10 November to 9 December 2014 with none, and SPY's shares turn over
  about 2,700% a year against 12% for Vanguard's S&P 500 index mutual fund (Madhavan,
  *Exchange-Traded Funds and the New Dynamics of Investing*, 2016, chapters 1 and 2). It is not the
  turnover of the stocks the fund holds, by which Lee and Swaminathan sort; the library gives no
  sign for momentum by a fund's own volume. A fund's volume can serve as a crude market-wide measure
  of participation, reported beside a card (SC-016-01, SC-027-01), but TM-027's sign splits a
  cross-section of stocks by each one's turnover, and no source splits funds or indices by their
  own.
- **Momentum's life cycle, early or late, and its exhaustion**: the library's signs — high-volume
  winners and low-volume losers reversing faster (the Zacks handbook), low-volume winners persisting
  at three years (Aronson's note 56) — sort single stocks by their own turnover, unreadable on funds
  for the reason above; the reversal without the volume split is **MR-021**'s, read as value within
  groups by CA-024-01. Exhaustion at a volume spike, on indices and futures, is a practitioners'
  reading that Kaufman (*Trading Systems and Methods*, chapter 12) gives with "no comprehensive
  tests available"; its reversal over days is **MR-011**'s.
- **Trend confirmed by volume and open interest, on futures and indices**: the practitioners' rule —
  Kaufman (*Trading Systems and Methods*, chapters 9 and 12), Narang (*Inside the Black Box*,
  chapter 3), Gliner (*Global Macro Trading*, chapter 5) — with no measured sign: Kaufman finds
  little research relating volume to futures markets, and Narang reports the research he reviewed
  mostly contrarian. The library's one systematic test on an index, Aronson's 6,402 rules on the S&P
  500 from 1980 to 2005, fifteen price-volume indicators on NYSE volume among them, found none
  significant after his correction for data mining. The one index-level sign with volume, a larger
  reversal after high-volume days in aggregate US data (Campbell, Grossman and Wang, in Campbell's
  *Financial Decisions and Markets*, chapter 12), is **MR-011**'s, over days; market turnover as a
  contrarian sentiment gauge (Ilmanen, *Expected Returns*, section 8.6) is **TM-037**'s. Passing the
  snapshot's volumes to a strategy would therefore open no form of TM-027's: what is missing is a
  sign, not a path. The lab trades no futures.
- **Momentum without the volume split**: read on the lab's funds — TM-017-01, CA-001-01, TM-003-01
  and TM-001-01.

**The bank's siblings.** **TM-028**, momentum filtered by low volume, untouched, from
O'Shaughnessy's volume deciles: the long side's sign above; **MR-011**, the volume forms of
reversal; **TM-008**, **TM-025** and **TM-016**, recorded not testable, the diffusion, coverage and
disposition readings of the same cross-section; **MR-021**, the reversal.

**What was considered, and why it does not rescue a card of TM-027's own:**

- **The funds ranked by their past return, split by their own recent volume**: no sign for funds
  (above), and a long-only rule holds the winners, among whom the source finds no significant
  difference by turnover (−0.12% a month, t −0.67).
- **Volume as attention at the level of an index**: no source splits indices by their volume
  (above); attention forms on prices are read by LL-023-01 (the frog in the pan).
- **Continuation after large moves on high volume**, handed here by TM-011-01: Singal (*Beyond the
  Random Walk*, 2003, chapter 4, after Pritamani and Singal) finds single stocks' large moves on
  high volume continuing over twenty days, and clearly only with public news too; the lab holds no
  news, the sign is firm-specific, and over days, a horizon TM-027's months do not cover.
- **Bitcoin's volume**: one asset, and the library gives bitcoin's trend no sign (TM-005-01).

What would make it testable as its own: a stock universe with each stock's turnover, frozen in the
snapshot and passed to a strategy; futures' volume and open interest would open the futures form
only with a source that measures it, which the library does not hold.

## Status

TM-027 is recorded `not-testable` as a theory of its own: its signs are on single stocks sorted by
their own turnover, and lie mostly in the losers' side, which a long-only rule does not hold; a
fund's own volume measures its shares' trading, not its holdings' turnover, and the lab passes a
strategy no volume; its futures and index forms have no measured sign, so passing volumes would open
no form; on the winners' side the library's signs favour low volume, TM-028's claim; the volume
continuation handed by TM-011-01 needs news the lab does not hold; its reversal is MR-021's, and
over days MR-011's. No card is drawn, and no trial is spent.

## Addendum (2026-09-26)

Two statements above no longer hold: that no source splits funds or indices by their own volume, and
that the lab passes a strategy its closes only. TM-028's reader found Fosback's positive and
negative volume indices (Aronson, *Evidence-Based Technical Analysis*, 2007, chapter 8, p. 411 and
note 30; Kaufman, *Trading Systems and Methods*, chapter 12, p. 542): from 1941 to 1975, with an
index's trend made on its loud sessions, those of rising volume, above its average, a bull market
held 79% of the time, against 96% for the trend made on its quiet sessions and a base rate of 70%
(the 79% as Kaufman reports it, for the variant he says is decided by the close's direction; the 96%
in both; the base rate Aronson's). On an index the library's sign runs against TM-027 and for
TM-028. The lab now passes a strategy the funds' volumes, lagged as their closes. TM-027's index
form, the trend on high volume against the trend on low volume, is the contrast TM-028-01's clause
grades from the other side: a t statistic of +0.35 or above refutes it in this form; one of −0.35 or
below, which refutes TM-028 in this form, leans TM-027's way without proving it. TM-027 stays
`not-testable` as a theory of its own: its stock and futures forms remain unreadable, and its index
form is graded by TM-028-01.
