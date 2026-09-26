# TM-038-01 — Trend following bought at its own dips: reasoning

## Why this theory now

TM-038 is next in the trend-and-momentum family, taken in number order. It is Lo's adaptive markets
hypothesis (2004, 2017): markets are an evolving ecosystem, strategies are species, and regularities
of continuation appear, disappear and reappear as participants adapt to regimes, competition,
regulation and constraints; trend followers are well adapted to high macroeconomic uncertainty and
crises, less so to calm, choppy markets, and a strategy's profitability varies in cycles, degrading
when too much capital follows it and returning when capital leaves. Its refutations: trend-following
profitability constant across regimes, or unrelated to the capital following it; returns that do not
recover after capital leaves, or do not degrade when it crowds in; regularities that disappear
instantly and completely once exploited, or never change. The bank names equity indices, bonds,
currencies and commodities, and daily prices and the assets under management of managed futures.

A first judgement drew TM-038 as not testable as a theory of its own. Its reader found a signed form
the lab's closes can read and no verdict had read: trend following's own returns revert, so that its
months after a losing stretch earn more than its months after a winning one. The first judgement had
handed it to CA-003, whose factor momentum claims the opposite sign; TM-015-01's reasoning had
handed "a strategy's life cycle of inflows and crowding" to TM-038. This card draws that form.

**Its sources.**

- **Greyserman and Kaminski** (*Trend Following with Managed Futures*, 2014). Chapter 4, "Adaptive
  Markets and Trend Following": the hypothesis as the frame of trend following's crisis alpha, the
  institutional restrictions, market functionality and behavioural biases (table 4.1) that hinder
  other players' adaptation in crises, and "the inevitable degradation of alpha" (Lo, 2012; figure
  4.3, a schematic). Chapter 17, "Dynamic Allocation to Trend Following": fund flows into managed
  futures chase performance — 2008 a record year, 2009 a year of high inflows — while "the serial
  autocorrelation of trend following returns is shown to be negative" in monthly index returns from
  1993 to 2013 (figure 17.2), a Newedge study (2012) finding it at lags of up to five months in
  trend-following managers; trend following applied to a trend follower's own returns does not beat
  holding it (figure 17.5); a buying-at-the-dips allocation — x percent held always and the rest
  added as the trend of the strategy's cumulative returns turns down, in proportion to its strength,
  total leverage never above that of holding it in full, the worked example half and half — raises
  the Sharpe ratio when the autocorrelation is negative enough. In their simulations (table 17.1)
  the average total return difference over holding always is 3.14 percent at a Sharpe ratio of 0.4
  and an autocorrelation of −0.16, and turns negative as the autocorrelation goes to zero and the
  Sharpe ratio rises; "a typical trend following program" in their worked optimization has an
  autocorrelation of −0.1. They place a return profile like the point estimates of actual trend
  following — a Sharpe ratio of 0.9 and slightly negative autocorrelation — in their scenario A, in
  which holding it always is the favourable allocation; buying at the dips is their scenario B, a
  low Sharpe ratio and a more negative autocorrelation (table 17.2). They warn that manager indices
  carry survivorship bias, which can make any surviving track record look mean-reverting, and they
  derive a negative autocorrelation mechanically too, from trend following's likeness to a lookback
  straddle (Fung and Hsieh), whose variance ratio falls below one (the chapter's appendix).
- **Ilmanen** (*Expected Returns*, 2011): section 5.3 calls the hypothesis "not a disciplined theory
  but a collection of interesting ideas", among them the copying of successful strategies and
  profitability that competition erodes and later renews; section 20.2, figure 20.2, a strategy's
  life cycle — success attracts inflows, crowding eats the opportunity, the liquidation waits for
  bad times, and "plummeting performance revives the strategy's ex ante attractiveness". His figure
  20.1 leans the other way: adjacent months' returns correlate at +0.20 on average across asset
  classes and strategies, commodity trend following one of the two exceptions with a mild negative
  correlation, and "even the two exceptions" show mild positive autocorrelations over longer
  samples.
- **Lo** (*Adaptive Markets*, 2017, the 2019 printing, held in full), chapter 8: the first-order
  daily autocorrelation of US stock indices over 750-day rolling windows, 1926 to 2014 (figure 8.8),
  waxing and waning, significantly negative after 2008, "positive returns today predicting negative
  returns tomorrow"; the index scaled to a volatility target (table 8.2); the quant meltdown of
  August 2007 and liquidity spirals, contrarian strategies as liquidity provision; hedge-fund alpha
  becoming "commoditized". **Lo** (*Hedge Funds: An Analytic Perspective*, chapters 9 and 10): the
  hypothesis's cycles read through hedge-fund entries and exits in the TASS database, and contrarian
  profits falling from 1995 to 2007 as long/short equity assets grew — both on stocks and assets
  under management.

**The form this card tests.** TM-038's prediction that a strategy's profitability returns after
capital leaves it, and its refutation, returns that do not recover after capital leaves, read
through the one trace of the cycle the lab's closes give: the strategy's own past performance. The
lab holds no assets under management; Greyserman and Kaminski show the flows chasing performance, so
a losing stretch is the stretch in which capital leaves, and Ilmanen's life cycle revives the
strategy after it. The strategy is the lab's trend rule, TM-017-01's: each of the seven funds held
in a seventh while its past year's return beats the bill. The claim: TM-017-01's rule earns more, at
the same exposure to the seven funds, in the months after its own losing stretch than in the months
after a winning one.

Three limits are stated. Greyserman and Kaminski's chapter 17 does not name the adaptive markets
hypothesis; the link is TM-038's cycle and their chapter 4, and it is the card's. A positive
contrast would not tell the capital cycle from the mechanical reversion of a lookback straddle,
which predicts the same sign; the card grades the sign both readings share. And their evidence is on
long-short programmes of managed futures, while the lab's book is long only, on seven funds, with a
beta of about 0.4 to them (TM-018-01); the transfer is the card's, though the lab's book, a rule and
not a surviving manager, carries no survivorship bias.

## From the claim to a signal

- **The book**: TM-017-01's rule, recomputed as TM-018-01 recomputed it: on the first session of
  each month, each fund whose return over the past 252 sessions, read up to the session before,
  beats the bill's over the same sessions and that trades holds a seventh; the rest in cash; the
  weights drift with the funds' closes and the bill until the next target.
- **The book's own record**: each session's return of the book less the bill's, from the drifting
  weights, before costs — the funds held times their returns less the bill's, zero before the book's
  first holding; the sum of these daily excess returns over the last `dip` sessions to the session
  before the target.
- **The state**: the book is *in a dip* when that sum is below zero — its return over the stretch
  below the bill's, Greyserman and Kaminski's cumulative trend turned down.
- **The rule**: on the first session of each month, the book's weights are held at a scale k: one
  half always, Greyserman and Kaminski's x of 50%, and the other half added while the book is in a
  dip, so k is 1 in a dip and 0.5 otherwise; the rest in cash. The total never exceeds the book held
  in full, their cap. While fewer than `dip` sessions precede the target, k is 0.5; a window that
  reaches before the book's first holding sums only the sessions after it.
- **The variant**: `dip` 252, the book's own lookback, a choice of the lab's; the base takes 105,
  five months, the lags of the Newedge study.
- **Parameters**: `dip`, 105; neighbours 79 and 131, 53 and 158. The book's lookback, 252, is
  TM-017-01's, and the half held always is the sources' example; both are fixed.
- **Memory**: 530 sessions: the book's returns over the last `dip` sessions depend on the targets of
  the months they fall in, up to 22 sessions earlier, which read 253 sessions back; 252 + 275 for
  the variant, rounded up.

The binary state stands for Greyserman and Kaminski's allocation "proportional to the strength of a
trend signal based on cumulative trend following returns", whose full strength they do not give; a
card that chose it would choose a scale from nothing in the library. Adding the whole second half at
any dip, however small, is the most aggressive reading of their scheme.

## What the battery judges, and what to expect

**The size predicted — a judgment.** The card judges the book's hedged monthly returns — its return
less the bill's, net of its exposure to the seven funds — to carry an autocorrelation of about −0.02
to −0.05 at each of the first five lags, a sum of −0.1 to −0.25, around the −0.1 of Greyserman and
Kaminski's typical programme, which they do not say is by lag or summed; they give no value by lag.
With such an autocorrelation, the months after a losing five months earn over the months after a
winning five months about 0.14 of a month's volatility per 0.04 of autocorrelation; on the book's
hedged volatility, from the tracking error TM-017-01 published, about 5.2% a year (an alpha of 1.55%
at an appraisal ratio of 0.30), 1.5% a month, that is 1.3 to 3.2% a year. The card widens it for the
transfer from long-short programmes to a long-only book: the months after a dip earn about 0.5 to
3.5% a year more than the months after none, at the same exposure to the seven funds. The rule's
alpha over the seven funds held in equal parts, holding the book at two-thirds to three-quarters on
average, about 0 to 2% a year; its return is expected below the book's held in full, as Greyserman
and Kaminski's table gives at a Sharpe ratio of 0.5 and an autocorrelation of −0.02 to −0.05.

**The gates.** The rule decides monthly on seven funds, as TM-017-01 did: gate 1 should pass. The
card expects the base to fail gate 3, as TM-017-01 did at 81.7% of its placebos, and gate 4, the
registry now holding some sixty effective trials; gate 6 likely on SPY's share of the profit,
TM-017-01's 33%; gate 2 and gate 5 possibly, TM-017-01's best year, 2008, carrying more than half
its alpha.

**The clause.** Judged before costs, on the market's closes, over the in-sample months from the
first target whose 105 sessions before it all fall on or after the session of the book's first
holding, the first session of July 2006, to December 2022, the last month ending at the close of
2022-12-30, each month from the close of a target's session to the close of the next target's
session: the book's return over the month held in full (k = 1), less the bill's, regressed by
ordinary least squares on an indicator of the dip state at the target (`dip` 105) and on the return
less the bill's of the seven funds held in equal parts from the same closes, with standard errors
robust to heteroskedasticity; the t statistic computed apart from the battery. The theory is refuted
in this form if the indicator's t statistic is −0.35 or below: the book no better after its own
losing stretch than after a winning one. Between, short of passing gates 1 to 7, not proven, not
refuted; a base that passes gates 1 to 7 while the clause refutes leaves the theory refuted in this
form.

**The test's power.** 198 months. The book's monthly hedged return has a standard deviation of about
1.5%; with a third to a half of the months in a dip, the standard error of the difference is about
0.21 to 0.23% a month, some 2.5 to 2.7% a year. At 2.7% the clause refutes about 36% of the time
with no effect and about 14% at +2% a year, the middle of the prediction: the test can barely tell
the predicted effect from none, and a refutation is weak evidence.

**What was published, and what it tells.** No verdict has published the book's returns after its own
losing stretches against those after winning ones.

- **TM-017-01** published the rule's Sharpe ratio, alpha and appraisal ratio, its blocks (four of
  five positive, the best 2020–22), its best year, 2008, and the months of 2009 it missed, from
  March to the autumn, GLD and DBC held into the autumn of 2008; **TM-047-01** the rule scaled by
  volatility, its appraisal ratio 0.42, 0.53 after Lo's correction for autocorrelation.
- **TM-018-01** published TM-017-01's hedged edge by state: 1.10% a year in its divergent months and
  1.95% out of them; −1.75% in its equity-crisis months, the months after an unbroken run of SPY's
  falling months that lost 5% or more, and 2.15% out of them; the years in which TM-017-01's edge
  was positive, 2007, 2008, 2013, 2015, 2020 and 2022; and 2009's rebound, from April to July.
- **The registry** holds, in each trial's line, its monthly hedged returns — TM-017-01's,
  TM-018-01's and TM-047-01's among them — from which the book's autocorrelations and an
  approximation of the graded contrast could be computed. Nothing was computed from them for this
  card.

None is the graded quantity. Whether TM-018-01's crisis months, or its divergent months, fall across
the dip and no-dip sets reads the book's own returns and is known only after the run; each state is
judged apart. If 90% or more of a state's months among the 198 fall in one set, they are a published
subset of that set: they leave the graded clause, the graded months fewer by as many, and the clause
with them is reported. Otherwise they stay in the graded sample, disclosed, and the clause without
them is reported. The divergent months, 47% of all, are likely to fall across both sets. The
calendar years above fall across the sets and stay.

**TM-038's refutations, and what the card can grade.**

1. *Profitability constant across regimes, or unrelated to the capital following it*: the regime
   form is TM-018's, read by TM-018-01; the capital, not held.
2. *Returns that do not recover after capital leaves the strategy*: graded, in its own-performance
   form, by the clause. *Or that do not degrade when capital crowds in*: its mirror, the months
   after a winning stretch, is the other side of the same contrast.
3. *Regularities that disappear instantly and completely once exploited, or never change*: every
   verdict's blocks and holdout report the change of a rule's edge; the decay after publication is
   read on stocks (below).

**Measures stated before the run**, reported, not graded:

- the variant, `dip` 252: the same regression over its own months, from the first target whose 252
  sessions before it all fall on or after the book's first holding, the first session of March 2007,
  190 months;
- the same regression without the seven funds as a regressor, and with a beta for each state;
- the share of months in a dip, the base's average scale, and the autocorrelations at lags 1 to 5,
  and their sum, of the book's hedged monthly returns (its excess return less its beta times the
  seven funds' excess return);
- where TM-018-01's crisis months and its divergent months fall, and the clause without or with
  each, as above;
- the clause over the months of 2006 to 2013, over those of 2014 to 2022, and over the holdout,
  2023 to 2025;
- the Sharpe ratios before costs of the base and of the book held in full; the alpha and the return
  of the book held constantly at the base's average scale, against the base's;
- `python -m lab.compare` against TM-017-01, the rule held in full;
- the base's alpha before and after costs, and the neighbours' and the one-day-late rule's alphas
  and appraisal ratios.

## What was considered, and why each is set aside

- **Recording TM-038 not testable**: the first judgement's conclusion, overturned by its reader.
- **Trend following switched by the market's own autocorrelation** (Lo's figure 8.8): Lo's sign is
  on the next day's return, a reversal from one day to the next after 2008; a rule reading it holds
  for a day, and fails the one-day-delay check of gate 6 by construction (SC-011-01); Lo gives no
  sign linking the daily autocorrelation to trend returns over months. The autocorrelation of index
  returns is **TM-043**'s claim (Lo and MacKinlay's variance ratios), reversion conditioned on
  regimes **MR-043**'s, and the daily reversals of indices **MR-001**'s (as liquidity provision;
  **MR-002** holds stocks only).
- **The decay of alpha after publication**: Lo's commoditized alpha and Greyserman and Kaminski's
  degradation (chapter 4, figure 4.3) are general, and give no date or sign the funds can read; the
  only signed evidence in the library is Ilmanen's (*Investing Amid Low Expected Returns*, 2022,
  note 14): McLean and Pontiff's decay of US stock factors after publication, which Ilmanen reads as
  nearer overfitting than learning, noting that Jacobs and Müller find no decay outside the US — on
  stocks, which the lab does not hold. On the funds, a split at a publication date is one decision,
  which gate 1 refuses; the halves of the trend rule's record are already published by TM-017-01's
  blocks.
- **Crowding measured by capital**: assets under management of trend followers, TASS entries and
  exits (Lo's own tests), and crowded factor bets, **FP-036**'s: not held.
- **Trend following in crises and divergent regimes**: **TM-018**'s, read by TM-018-01, refuted in
  its narrow form; the crisis form TM-031-01 and TM-011-01 handed here is that one; the convexity of
  trend following in large equity moves (Greyserman and Kaminski, figure 4.15) is TM-018's too,
  untested. Dispersion as a reading of the market's ecology is **TM-039**'s, read by TM-039-01.
- **Performance chasing, trend following squared**: the opposite sign, which Greyserman and
  Kaminski's figure 17.5 finds no better than holding; a second rule on one sign, left. The momentum
  of factors and styles in stocks and indices is **CA-003**'s.
- **Volatility management** (Lo's table 8.2, and his reading of risk punished when investors are
  "freaking out", figure 8.4): **TM-047**'s, read by TM-047-02.
- **A proportional allocation**: above; its scale is not in the library.

## Implementation

Long only, the seven funds, with European (UCITS) funds that track them; one decision a month, the
book's record read up to the session before and traded at the close, a day's delay; the book at half
or in full by one state.
