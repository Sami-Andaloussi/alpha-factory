# TM-028-01 — The trend of the quiet sessions: reasoning

## Why this theory now

TM-028 is next in the trend-and-momentum family, taken in number order. It holds that among assets
with strong price momentum, those that trade on low volume do better than those that trade on high
volume: high volume signals that the good news is already widely known and the move near its end,
low volume a move still "under the radar", with more room to run; by analogy, in futures, a trend
carried on moderate volume is at its start, one on explosive volume near its end. The bank quotes
O'Shaughnessy (2011): over US data from 1926 to 2009 (the book's figures run from 1964, with
Compustat's volumes, below), strong momentum with low volume compounded 13.16% a year against 8.09%
with high volume. Its refutations: high-momentum stocks with low volume earning no more than
high-momentum stocks with high volume over the following months; high volume during a rise followed
by continuation as strong as, or stronger than, low volume. The bank names stocks, equity indices,
bonds, currencies and commodities, and daily prices and trading volumes.

A first judgement drew TM-028 as not testable: its signs on stocks read each stock's own turnover,
and the lab passed a strategy its closes only. Its independent reader found a form on an index, with
a sign, that no verdict has read and no theory of the bank claims — Fosback's negative volume index
— and that needs only a fund's daily volume, which the snapshot held and the lab did not pass. The
lab's data module was extended to pass it (`market.signal_volumes`, lagged as the closes are, gate 1
moving it wherever it moves the prices), and this card is drawn on it.

**Its sources, as the lab read them in the library.**

- **Fosback's negative and positive volume indices**, as Aronson (*Evidence-Based Technical
  Analysis*, 2007, chapter 8, p. 411, and note 30, p. 510) and Kaufman (*Trading Systems and
  Methods*, chapter 12, p. 542) report them. The negative volume index accumulates a stock index's
  daily changes on the sessions whose volume is below the session before's, and stands still on the
  others; the positive volume index accumulates them on the sessions whose volume is above. Their
  reading: unsophisticated trading comes on days of rising volume, informed buying and selling on
  the quieter days of falling volume, so that the direction the market takes on its quiet sessions
  reflects the accumulation or distribution of those who know. Fosback, over 1941 to 1975, the trend
  of each index judged against its 6-month (127-session) or 1-year (255-session) moving average
  (Kaufman): with the negative volume index above its average, a bull market held 96% of the time,
  against a base rate of 70% (both give the 96%; the base rate is Aronson's); with the positive
  volume index above its, 79% (Kaufman). With the negative volume index below its average a bear
  market held 50% of the time, with the positive volume index below its, 67% (Kaufman): the quiet
  sessions' trend is the better sign of a bull market, the loud sessions' the better sign of a bear.
  Kaufman attaches these figures to the variant of the indices that is decided by the close's
  direction, not by the volume; Aronson, whose definition is the volume's, and Fosback's name for
  the index follow the volume. The card follows Aronson and states the conflict.
- **Aronson's own test**, the contrary evidence: the S&P 500 from November 1980 to July 2005, with
  NYSE volume, 6,402 rules, those on the cumulative negative volume index and its 10- and 30-day
  averages among them (his indicators 18 to 20): no rule significant once his correction for data
  mining was applied, the trend rules on the negative volume index among his hundred best (table
  9.1, pp. 445-446) were inverse ones (TI-20-41, TI-18-8), beside extreme-value rules on it
  (E-1-19-10-60, E-1-18-20-60, E-2-19-10-60, E-5-20-10-30, E-1-18-10-60) and inverse trend rules on
  the positive volume index (TI-21-8, TI-21-12, TI-23-5, TI-23-41, TI-21-5), none significant. His
  trend rules were channel breakouts over 3 to 205 sessions, long or short the S&P 500: a prior
  against the form, on a later sample than Fosback's, not a test of Fosback's rule.
- **On stocks**, TM-028's own figures, which the lab cannot read. Jegadeesh and Titman, in *Advances
  in Behavioral Finance, Volume II* (Thaler, ed., 2005, chapter 10, table 10.9), after Lee and
  Swaminathan (2000), NYSE and AMEX stocks from 1964 to 1995: among the past six months' winners the
  lowest-turnover third earns 1.67% a month, the middle 1.78% and the highest 1.55% (the highest
  less the lowest −0.12%, t −0.67) — TM-028's sign among the winners, not significant, and not
  monotone; among the losers high turnover does far worse (−1.04%, t −5.19), so that momentum as a
  whole is stronger with high turnover, TM-027's reading. The Zacks *Handbook of Equity Market
  Anomalies* (2011), after the same Lee and Swaminathan: low-volume winners beat high-volume winners
  by 0.26% a month in the nine-month/six-month strategy, over the next year, which "holds for
  numerous momentum strategies". Gray and Vogel (*Quantitative Momentum*, 2016, chapter 6):
  high-momentum stocks split on trading volume "yield similar results" to their other measures of
  attention, the less traded doing better, with no figures (their note 15 is Lee and Swaminathan).
- **O'Shaughnessy** (*What Works on Wall Street*, 4th edition, 2011, chapter 20, "Relative Price
  Strength: Winners Continue to Win", in "Additional Metrics to Consider with Price Momentum"; the
  bank's "Trading Volume Refinement" is not in the library's copy): the figures the bank quotes sort
  stocks on their six-month average dollar volume alone, from 1964 to 2009 with Compustat's volumes,
  13.16% a year for the lowest decile and 8.09% for the highest against 11.24% for all stocks; he
  proposes adding points to the seventh to tenth volume deciles beside price momentum, which "might
  allow you to smooth out your ride", with no figure. A sort on volume alone is the illiquidity
  premium's form, **CA-029**'s.

**The form this card tests.** Of TM-028's forms, one is readable on the lab's funds and has a sign:
the trend of an index made on its quiet sessions against the trend made on its loud ones. A fund's
volume is its own shares changing hands on the exchange among hedge funds, traders and institutions,
about four times the creations and redemptions over all ETFs, and not the trading of the stocks it
holds (Madhavan, *Exchange-Traded Funds and the New Dynamics of Investing*, 2016, chapters 1 and 2);
but ETFs make up just under a third of US equity volume, SPY's shares turning over about 2,700% a
year (Madhavan, chapter 1), and the lab already read SPY's, QQQ's and IWM's volume as a crude
measure of the market's participation (SC-016-01, SC-027-01). No verdict has published a return
split by a fund's volume: SC-016-01 and SC-027-01 reported the mean log volume of SPY, QQQ and IWM
over calendar windows, with no return split by it; no part of the graded contrast has been
published. The card reads each US equity fund's quiet and loud sessions by its own volume, and, in
its variant, by SPY's, the market's.

## From the claim to a signal

- **The universe**: the fourteen US equity funds — SPY, QQQ and IWM, and the eleven sector funds.
  EFA and EEM are left out: their volume is their US shares' trading, not the trading in their home
  markets, whose sessions it does not follow (SC-015-01); the commodity and Treasury funds are left
  out, as the library signs the form on a stock index only.
- **The indices**: for each fund, on each session from its first, the day's return counts in its
  *quiet* index when the volume that decides it is below that volume on the session before, and in
  its *loud* index when it is above; an equal volume counts in neither. The indices are the
  cumulative products of one plus the returns they count. The deciding volume is the fund's own in
  the base, SPY's in the variant. Aronson's index sums the daily percentage changes; the card
  compounds them, the usual form of the index, a difference of the second order over a year.
- **The trend**: an index is *up* when, at the session before the target, it stands above its
  average over the last `window` sessions to that session; the ratio of the index to its average
  reads only the returns and volumes of those sessions and of the session before the first, so that
  nothing older counts.
- **The rule**: on the first session of each month, each fund trading holds 1/N of the portfolio,
  N the funds trading, when its quiet index is up; its 1/N is held in cash when its quiet index is
  not up; a fund without `window` sessions and the session before them holds its 1/N, as the funds
  held always do. Everything is read up to the session before; targets are traded at the close.
- **The variant**: the same rule with SPY's volume deciding every fund's quiet sessions, the
  market's quiet days, as in Fosback's index, whose volume is the market's.
- **Parameters**: `window`, 255 sessions, Fosback's one-year average; its neighbours for gate 6,
  191 and 319, and 127 — Fosback's six-month average — and 383. `volume`, a text naming the
  variant, "own" or "market", with no neighbours.
- **Memory**: 256 sessions, the window and the session before its first, whose close and volume
  decide the first return.

## What the battery judges, and what to expect

**The size predicted — a judgment.** Fosback's figures are probabilities of a bull market, not
returns: with a bull month earning perhaps 1.5% and a bear month losing 2.5% on a stock index, a
bull probability of 0.96 against 0.79 when each index is up (the 0.79 Kaufman's, which he attaches
to the close-decided variant) is worth about 0.7% a month to the quiet trend over the loud one, some
8% a year, on 1941 to 1975. Aronson's test on 1980 to 2005 found nothing, and the inverse rules at
the top of his list; the fund's own volume is a weaker measure of the market's than the NYSE's; the
two indices move together most of the time, so that their difference rests on the months in which
they disagree. The card judges the fund-months with the quiet index up to earn, in excess of the
bill, about +0.5 to +5% a year more than the fund-months with the loud index up. For the rule, a
trend filter on funds whose trend on prices alone the lab found weak on another universe (TM-017-01,
which beat 81.7% of its placebos, its edge less exposure for its return), an alpha over the fourteen
funds in equal parts of about −1 to +1.5% a year, a Sharpe ratio close to theirs.

**The gates.** The rule steps out of a fund for a month at a time, and the card expects it to fail
gate 3 and gate 4 (an appraisal ratio of about 0.6 or more is expected by luck from the best of the
lab's effective trials), and likely gate 2 and gate 5 with them.

**The clause.** Judged before costs, on the market's closes, over the in-sample fund-months of the
base, each from the close of a target's session to the close of the next target's session, the first
target on the first session of February 2006 and the last on the first session of December 2022,
whose month ends at the close of 2022-12-30, the last in-sample session, over the fund-months with
both indices defined: each fund-month's return less the bill's over the same sessions. The
fund-months with the quiet index up and those with the loud index up are stacked, a fund-month with
both up entering both sets, and the stacked excess returns are regressed by ordinary least squares
on an indicator of the quiet set and one constant for each fund, the standard errors clustered by
month, the funds' months in each of the 203 months one cluster, since they move together; the t
statistic computed apart from the battery. The theory is refuted in this form if the indicator's t
statistic is −0.35 or below: the trend of the quiet sessions no better a sign than the trend of the
loud ones, the continuation after a rise on high volume as strong as or stronger than after a rise
on low volume. Between, short of passing gates 1 to 7, not proven, not refuted; a base that passes
gates 1 to 7 while the clause refutes leaves the theory refuted in this form.

**The test's power.** Twelve funds trade from the start; XLRE's indices are defined from about
October 2017 and XLC's from about July 2019: about 2,540 fund-months, counted from the calendar and
the funds' first sessions, which read no return; the states, which read returns, are not counted
before the run. A fund-month with both indices up adds little to the difference, entering both sets,
which rests on the fund-months in which one index is up and the other not; with monthly swings of
about 4.5% for the market (the figure CA-006-01's audit used; the three US funds' average moved
1.33% a day over the in-sample sessions, SC-014-01, about 6% a month were the days independent), the
funds of a month moving together, perhaps two months in three with a quiet index up and three
fund-months in ten discordant, the standard error of the difference is about 2 to 4% a year, up to
5% at the larger swings. At 3% the clause refutes about 36% of the time with no effect and about 10%
at +2.75% a year, the middle of the range (about 4% at an error of 2%, 15% at 4%, 18% at 5%): the
test can barely tell the prediction from none, and a refutation is weak evidence.

**TM-028's refutations, and what the card can grade.**

1. *High-momentum stocks with low volume earning no more than high-momentum stocks with high volume
   over the following months*: graded in its index form, the funds' months after their quiet trend
   is up against those after their loud trend is up. On stocks, by each stock's own turnover, it
   cannot be read.
2. *High volume during a rise followed by continuation as strong as, or stronger than, low volume*:
   the same contrast from TM-027's side, graded by the same clause. TM-027's index form, the trend
   of the loud sessions the better sign, is refuted in this form by the same t statistic at +0.35 or
   above; TM-027 draws no card of its own.

**The volumes' bad bars.** The volumes are read as Yahoo reports them. `python -m lab.data check`
lists seven of IWM's as far below their median, six in 2008 (25 and 28 March, 4, 22 and 24 April, 3
July) and one on 2019-07-30 at 1,200 shares: each makes its session quiet and the next loud. They
are kept, as a rule that cleaned them would choose its cleaning; the clause without the IWM
fund-months whose indices read one of them is reported. None of the other thirteen funds has a bar
listed.

**Measures stated before the run**, reported, not graded:

- the variant, SPY's volume deciding every fund's quiet sessions: the same regression;
- the bear side, Fosback's other half: for each index, the fund-months with it up less those with it
  not up, with one constant for each fund, and the difference of the two indices' spreads;
- the trend on every session, each fund's close above its average over the window, as a reference:
  its fund-months up against the quiet index's and the loud index's;
- the share of sessions quiet, loud and equal, by fund, and the share of fund-months with each index
  up, and with the two in disagreement;
- by group: SPY, QQQ and IWM, and the sector funds;
- the clause without IWM's fund-months whose indices read one of its listed bars;
- the clause over the months of 2006 to 2013, over those of 2014 to 2022, over the in-sample months
  without 2008 and 2009, and over the holdout, 2023 to 2025;
- the rule's alpha before and after costs, and the neighbours' and the one-day-late rule's alphas
  and appraisal ratios.

## What was considered, and why each is set aside

- **Recording TM-028 not testable**: the first judgement's conclusion, overturned by its reader: the
  index form reads a fund's volume, which the snapshot holds; the lab now passes it.
- **Each stock's own turnover among momentum winners** (Lee and Swaminathan, the Zacks handbook,
  Gray and Vogel): the lab holds no stocks. The funds split by their own volume within their groups
  would read a quantity the stock sources do not measure, a fund's shares' trading, and the library
  gives that cross-section no sign.
- **O'Shaughnessy's low-volume stocks**: a sort on volume alone, not a momentum form; CA-029's.
- **Aronson's cumulative negative volume index and its 10- and 30-day averages on the S&P 500**:
  tested by him and found wanting; the card takes Fosback's windows, whose figures are the sign, and
  states Aronson's result as its prior.
- **Kaufman's price-direction variant of the indices**, which adds each session's volume to one
  index or the other by the direction of its close: it splits the sessions by price, not by their
  volume, so it reads no quiet or loud session, TM-028's claim; that Kaufman attaches Fosback's
  figures to it is the conflict stated above.
- **EFA, EEM, the commodities and the Treasuries**: above. **Bitcoin**: one asset, whose volume the
  library does not sign.
- **Futures by volume or liquidity** (Greyserman and Kaminski, *Trend Following with Managed
  Futures*, 2014, chapter 15, fifty markets ranked by their average daily dollar volume over the
  past ten years, their trend-following returns over more than twenty years): a static ranking of
  markets, not a signal read when the trend is formed, whose less liquid markets gave slightly lower
  returns and a better Sharpe ratio only through diversification; and the lab trades no futures.
  Kaufman's reading of a rise on falling volume as weak support to be reversed is the practitioners'
  contrary view, with no test.
- **The short horizon** (Singal, *Beyond the Random Walk*, chapter 4: large price changes without
  high volume slightly reverse over one to twenty days): a reversal over days, MR-011's family, not
  TM-028's months.
- **A cross-sectional form**, the funds ranked on their quiet index's trend within their group: the
  library signs the index's trend against its average, a time-series reading; a ranking would be a
  second rule on the same claim.

## Implementation

Long only, the fourteen US equity funds, with European (UCITS) funds that track them; one decision a
month, the signal read up to the session before and traded at the close, a day's delay; each fund
held or in cash by its own quiet trend. The volume is the US trading of each fund's shares,
consolidated across venues, as Yahoo reports it; a UCITS fund's own volume would be another
quantity, and the rule reads the US fund's.
