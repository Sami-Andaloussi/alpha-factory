# CA-015-01 — The sector funds' average correlation as a forecast of their market: reasoning

## Why this theory, and why this form

CA-015 holds that expected returns are not constant: variables observed at a date predict the
returns of markets, styles and sectors over the following months, and the premia differ from one
regime to another. It refutes itself if the premia are constant across regimes, if the
conditioning variables do not predict out of sample, or if the predictability disappears as
investors crowd into it. Its sources list the predictors (Cochrane, *Asset Pricing*, revised
edition, 2005, chapter 20, §20.1; Ilmanen, *Expected Returns*, 2011, §8.6 for equities and §9.6
for Treasuries), turn a predictor into a position (Cochrane's chapter 8, §8.1: a managed
portfolio holds the asset "according to the value of" the variable), and combine several into a
forecasting model (Ilmanen's chapter 24).

A first judgement drew this theory as not testable, on the ground that every conditioning variable
the lab can read belongs to a sibling. Its reader found one that belongs to none: the average
correlation among the equities of a market. That judgement had routed it to MR-001 by misreading
TM-035-01, whose reasoning gives MR-001 the short-term reversals of the next clause and leaves the
correlation to no theory. It was withdrawn before any commit, and this card is drawn in its place.

The predictor is Pollet and Wilson's (2008), as Ilmanen reports it twice. In §8.6, among the risk
indicators, the relation between the market's volatility and its later returns "is famously
fragile", because volatility mixes two parts: "high intraequity-market correlation—typical during
market crises—predicts high future market returns (with a correlation of 0.20). In contrast, high
average time series variance of individual equities mildly predicts low future market returns".
In chapter 19 the average correlation "turns out to have a significantly positive relation to next
quarter equity market returns, while average variance has virtually no relation (and indeed a
negative one once the correlation's predictive ability is controlled for)". §8.6 gives the 0.20
as "the Pollet-Wilson (2008) finding", with no horizon and no sample; the average correlation is not
among the predictors of its Table 8.6, whose "stock market volatility (60-day)" correlates at 0.03
to 0.07 with later returns. Chapter 19 gives the horizon, the next quarter, without a figure. Pollet
and Wilson's paper is not in the library; this card reads them through Ilmanen alone.

The claim is CA-015's in the sense its bank file gives it — "the market's capacity to bear risk",
observed at a date, predicting the market's return over months — and it tests the theory's second
refutation where the sources leave it open: the lab's in-sample years run from 2008 to 2022, after
a sample that ends before the paper's 2008 date, so the lab's reading is out of it.

## From the mechanism to the signal

- **Equities**: the lab holds no single stocks. It holds the eleven sector funds of the US market,
  whose daily returns stand for the market's components; the average correlation among them is a
  coarser reading than Pollet and Wilson's among stocks, since each fund averages away its
  members' own moves. The proxy is disclosed, not hidden: a correlation among sectors is high when
  the market's common factor dominates, which is the state the sources describe, and it is lower
  and more stable in level than a correlation among stocks.
- **The reading**: on every session, the average, over every pair of sector funds that trade on the
  session and have window daily returns in the signal prices up to the session before, of the
  correlation of those returns; window is 63 sessions, a quarter, the horizon of the forecast
  Ilmanen reports; the library gives no measurement window. XLRE's and XLC's returns enter the
  reading once they have a window of returns after they start to trade, on 2016-12-19 and
  2018-09-19; the reading's level moves by 0.02 or less at each entry, counted from the signal
  alone.
- **The scale**: a correlation's level means little in itself — among sectors it averaged about
  0.6 in the lab's years, counted from the signal alone — and the sources give no threshold. Each
  reading is set against the readings of the past lookback sessions, 756, three years, up to the
  session before: its percentile among them, the share of them at or below it. A bounded window,
  not an expanding one, so that the memory is declared and gate 1 can check it.
- **The position**: on the first session of each month, the sector funds that trade are held in
  equal parts in the proportion that percentile gives, the rest in cash: Cochrane's managed
  portfolio, the position scaled by the variable, the reading of a linear predictor that a
  correlation with the next quarter's return describes. The month is a common pace for tactical
  models ("a monthly or weekly trading frequency is common", the opening summary of Ilmanen's
  chapter 24) and a third of the forecast's horizon, so each quarter's forecast is read three
  times.
- **The variant "median"** holds the sector funds in equal parts while the reading is above the
  median of the same trailing readings, and cash otherwise: Ilmanen's binary form, the "1/0" model
  of his chapter 24, which never sells short and holds cash on a bearish signal.
- **The benchmark** is the battery's: the eleven sector funds that trade, held in equal parts,
  always invested. The rule's edge is its timing: the months it is invested against the months it
  is not.

## The choices, and the options rejected

- **The sector funds, not the five equity markets.** Pollet and Wilson read the correlation among
  the components of one market; the sectors are the components of the US market, and SPY is
  their sum. The five equity markets (SPY, QQQ, IWM, EFA, EEM) mix countries and baskets that
  overlap — QQQ and IWM inside the US — so their correlation reads the world's common factor and
  the overlap's arithmetic. Holding the sectors, not SPY, keeps the universe at four assets or more,
  with no asset near 30% of the profit.
- **Cash, not Treasuries, when out**: the sources' timing is the equity premium against the bill;
  holding IEF would add the stock–bond relation, LL-042's.
- **The percentile over three years**: a trailing window long enough to hold a calm and a stress,
  short enough to follow the level's drift as XLRE and XLC join. The first percentile, on
  2008-05-01, ranks readings from April 2005 to April 2008, which hold the stress of 2007 but not
  the crash of autumn 2008; later percentiles rank against it. The neighbours move it from 378 to
  1,134.
- **The memory**: the signal reads lookback plus window sessions back from the session before, the
  first return's extra close included: 819 for the variants, 1,197 for the largest neighbour
  (1,134 + 63) and 850 for the window's at 94; the card declares 1,240, which covers even both moved
  at once (1,228). A bounded history of readings keeps within the memory rule. It has a cost: gate
  3's shifts must keep 1,242 sessions apart, and gate 1 checks the memory only on targets from about
  2010.
- **The reading from the session before, the trade at the target's close**: as every rule of the
  lab.
- **Cochrane's detrended bill rate**, the predictor TM-007-01 handed to this theory: the bill's
  yield less its average over the past year changes sign 26 times on the in-sample months' first
  sessions from 2006 to 2022, 24 of them with the yield below 0.25%, and 46 times over a six-month
  average, 32 of them below 0.25%, counted on the yield alone; a position scaled by it would clear
  gate 1 only on noise around the zero bound. Ilmanen finds the "Follow the Fed" patterns "not
  evident in data after the mid-1980s" (§8.6). Not drawn.
- **The average variance**, Pollet and Wilson's other half: the sources sign it weakly and
  negatively, and a rule scaled by the inverse of variance is TM-047-02's, run on the five equity
  markets. It is reported apart, not traded.
- **Ilmanen's composite for Treasuries** (Figure 24.1: equities' past six months, the bonds' own
  momentum and bond carry, which §9.6 describes as "information about curve steepness"): three
  Treasury funds, where the lab needs four assets, and a
  long yield the lab does not hold; its first two legs are LL-042-01's joint rule, run, whose gate 6
  neighbour at 126 sessions read Ilmanen's six months.
- **The other predictors**, each read elsewhere or not held: valuations and dividend yields,
  MR-044's and CA-022's, which wait for a point-in-time reading of the funds' distributions (the
  lab's decision of 2026-09-26); carry, CA-025's; the cycle and inflation, not held (CA-013); the
  policy rate, CA-012's; own momentum, TM-017's; sentiment, TM-037's; Murphy's allocation by
  Pring's six stages (chapter 12), CA-011-01's variant "assets".

## What the lab has already published about these years

- **TM-047-02** timed the five equity markets by the inverse of their own realized variance: an
  alpha of 1.56% a year before costs (standard error 1.74%, t +0.90), a beta of 0.48, an appraisal
  ratio of 0.22 over 214 months, stopped at gate 3; SPY alone managed so, +2.67% a year (1.64%);
  without TM-024-01's 17 equity panic months, +0.53% (1.21%); the holdout −1.35% a year. Its
  registry series, the monthly returns hedged of its benchmark, is the lab's closest published
  record to this card's; nothing was computed from it.
- **TM-024-01** published the months in which each group's market was in a panic state, its market
  down over two years and its volatility above its own average: for the sectors, October 2008 to
  November 2009, July to September 2010 and April 2020, 18 months — the months of high correlation
  the sources call "typical during market crises". It published the sectors' return in two of them:
  +8.4% in September 2010 and +8.2% in October 2022 (the latter outside its sector panic months).
- **TM-039-01** read the dispersion of the sector funds' returns, which falls as their correlation
  rises, and published CA-001-01's momentum tilt after more and less dispersed months, not the
  sectors' market return.
- **TM-017-01** and **TM-018-01** published trend following's outcomes in SPY's crisis months,
  runs of falling months losing 5% or more.
- **CA-011-01**, **CA-014-01** and **TM-002-01** published the sector funds' returns by year, stage
  and sector — 2008 financials −55%, 2009 materials +48% (CA-014-01); the sectors' betas to their
  equal parts from 0.61 for staples to 1.40 for financials (TM-002-01).
- **CA-006-01** published a regression of this clause's own dependent variable: over 213 monthly
  targets from 2005-03-01, the sector funds' average excess return from one target's close to the
  next, on XLF's relative return and on the market's own past month (−0.068, t −0.82), with splits
  by block and without the targets of 2008. Its registry series is named with TM-047-02's; nothing
  was computed from either.
- **TM-037-01** published the funds' returns after high against low market turnover, the sector
  funds +3.81% a year (12.90%), in months that overlap the volatile ones; **TM-041-01** and
  **SC-026-01** timed the sector funds, and published their returns in their states.
- **TM-024-01** also published a pooled figure: its nineteen funds in equal parts, eleven of them
  sectors, earned 27.4% a year in the months its rule differed from CA-001-01's — the months any
  group was in panic — against 5.8% elsewhere.

The graded clause below leaves out the two months whose sectors' return TM-024-01 published, and
reports it with them. TM-024-01's 18 sector panic months, whose market return it published only
pooled with the other groups', sit high on the signal: 15 of them (83%) have a percentile above 0.5,
counted from the signal alone, against 47% of all months. Under CA-003-01's 90% they stay in the
graded sample, disclosed, and the clause without them is reported.

## The bank's other theories this card touches

- **TM-047**, volatility-targeted momentum, tested inconclusive: TM-047-02's variance timing, the
  other half of the volatility this card splits.
- **TM-024**, momentum crashes, and **TM-039**, dispersion-conditioned momentum, tested
  inconclusive: the crisis states and the dispersion, read for momentum, not for the market.
- **MR-044**, countercyclical expected returns, untouched: higher expected returns in bad times,
  read from valuations; this card reads them from the market's correlation.
- **MR-001**, short-term reversal, untouched: days to weeks, across stocks.
- **MR-043**, Markov switching and regime-conditional reversion, untouched: calm and crisis regimes
  inferred from returns; this card reads the regime from the correlation, not a switching model.
- **FP-036**, correlated factor bets, and **FP-035**, fragile factor premia, untouched: the crowding
  of the theory's third refutation, which reads positions the lab does not hold.
- **CA-012** and **CA-013**, recorded not testable; **CA-011**, **CA-014**, **LL-042** and
  **TM-037**, tested inconclusive; **TM-017**, in progress: the other conditioning variables.

## The prediction and the test's power

Sign: positive — the sector funds earn more over the month after their correlation stood high
against its past three years than after it stood low. Size, a judgment: Ilmanen's 0.20, read here as
quarterly and presumably in-sample, is at least partly spent by publication; spread over a month it
is about 0.1. A share that moves from 0 to 1 with the reading's percentile, whose standard deviation
is about 0.3, on a market whose excess return's volatility was 19.8% a year from late 2006 to 2022
(the sector funds in equal parts, as CA-011-01's verdict published it), gives a residual volatility,
hedged of the benchmark, of about 6% a year; at a monthly correlation of 0 to 0.1, an appraisal
ratio of about 0 to 0.35 and an alpha of about 0 to 2% a year before costs. The average share is
about 0.47, counted from the signal alone, but the share is highest when the sectors are most
volatile — 0.99 to 1.00 from November 2008 to January 2009, 1.00 in July 2010, 0.98 in April 2020 —
so the rule's beta will come in above it, perhaps 0.5 to 0.7, the mirror of TM-047-02, whose beta of
0.48 lay below its average scale of 0.78. The battery's alpha then pays the premium on that extra
beta, and can fall below zero while the reading predicts. That is why the clause grades the slope,
the forecast itself, and not the base's appraisal ratio: the rule's return will be well below the
benchmark's, and its Sharpe ratio near it. Costs: the share changes by about 0.13 a month on
average, about 1.6 times the portfolio a year at 5 basis points a side, about 0.1% a year.

Power: TM-047-02's appraisal ratio carried a standard error of about 0.24 over 214 months; over this
card's 176 in-sample months, about 0.26. The clause's slope has a standard error of about 1.5
percentage points of monthly return per unit of share, on a monthly excess return's deviation of
about 5.7% and a share's of about 0.3: a monthly correlation of 0.1 gives a slope of about 2.0, 1.3
standard errors from zero. The test can tell the sources' in-sample strength from nothing only
weakly, and a half of it not at all. The clause refutes at a slope of zero or below: about half the
time if the reading predicts nothing.

## Risks at the gates, and the counts

- **Gate 1**: gate 1 counts the base. Its percentile changes in 172 of the 175 month-to-month
  transitions from the first target, 2008-05-01, about 173 clustered decisions, counted from the
  signal alone. The variant's median rule changes state 33 times, 33 decisions, since its first
  target is cash; at the ±25% neighbours the median rule changes 21 to 42 times. The base's ±25%
  and ±50% neighbours change their targets 157 to 190 times, and none sets the base's targets.
- **Gate 2**: a rule invested half the time against a benchmark always invested; its alpha must
  come from its timing, and at twice the costs, 0.2% a year, it loses little.
- **Gate 3**: placebos shift the rule's shares in time; a share that follows crises is shifted onto
  other years' crises and calms. Gate 4 deflates by the registry's trials.
- **Gate 5**: the first target falls in May 2008, so the block 2008–09 holds the crisis the
  sources describe, and its alpha may carry the blend; 2005–07 is empty and counts as not positive,
  so three of the other four blocks must be.
- **Gate 6**: eleven sector funds held in equal parts, no one near 30% of the profit. The universe
  is one cluster, the sectors, which the battery does not leave out (it leaves clusters out only
  when a universe holds two or more), as for TM-002-01, TM-003-01 and CA-006-01. The neighbours
  move the window and the lookback; a day's delay moves a monthly target by a session. The
  lookback's neighbours at 945 and 1,134 set their first targets on 2009-02-02 and 2009-11-02: they
  hold cash in the months from November 2008 in which the base is fully invested, yet their Sharpe
  ratios are judged over the base's span from 2008-05-02, a risk to the neighbours' median.
- **Gate 7**: 2023 to 2025, sealed; nothing about them is read before the run.
