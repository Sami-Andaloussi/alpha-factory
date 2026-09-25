# TM-018-01 — Trend following switched on by divergence or crisis: reasoning

## Why this theory now

TM-018 explains when trend following earns. Its source, Greyserman and Kaminski's *Trend Following
with Managed Futures* (2014), calls trend followers divergent risk takers: they take many small
losses and ride a few large trends, and they earn when markets diverge — when prices move
persistently and cleanly rather than oscillate — above all in crises, when deleveraging,
intervention and herding push assets apart for months. Two claims give it a tradable form, under
one assumption.

- **Divergence.** The source measures each market's signal-to-noise ratio over n sessions, the
  absolute change of its price over the n sessions divided by the sum of the absolute daily changes
  (1 for a perfect trend, near 0 for noise), and averages it over the markets of a portfolio into a
  market divergence index, the MDI, with n "roughly 100 days" for medium- to long-term trend
  followers (chapter 5). From 2001 to 2013, a representative trend-following system's return over
  100 days correlates at 0.74 with the MDI over the same 100 days; its return over a period is close
  to zero when that period's MDI is at its average, negative below, and rises roughly linearly
  above, most in crises.
- **Crisis alpha.** Decomposing managed-futures indices from 1993 to 2013 into equity crisis
  periods — runs of negative returns of the MSCI World that lose more than 5% — and the rest, the
  source finds that crises, some 20 to 25% of the time, often account for more than half of trend
  following's return, the rest earning little, about the bill's rate in those years (chapter 4).

**The assumption.** Both relations are measured over the same period as the returns: they say when
trend following earned, not when it will. A rule can only read the months just past. What supports
reading them is the source's finding that the MDI cycles — in its example a power-weighted period of
about fourteen months, favourable and unfavourable environments alternating about every half year —
so that a divergent recent past tends to run on; the index's stationarity, found by a test on six
agricultural markets from 1949 (a finding its authors hedge), says only that its long-run level is
stable. The source itself gives evidence the other way: after a drawdown, trend following's mean
return tends to be higher (chapter 8: after a negative six-month return, the next eighteen months
averaged 51.6% against 41.5%) — and low divergence is when it loses, so the months after low
divergence may be good ones. For crises, Greyserman and Kaminski write that trend followers do not
time a crisis's onset but profit after it (chapter 4), which supports a state read a month late.

The lab has run trend following already: TM-017-01, each of seven funds held while its past year's
return beats the bill, which stopped at gate 3 with an alpha of 1.55% a year over the funds held
always (under the battery's version 1). This card keeps TM-017-01's rule and holds it only in the
states the theory favours, read from the month just past, holding the seven funds in equal parts
otherwise, so that what the battery finds, set beside TM-017-01 recomputed over the same sessions,
is whether the edge lay in the months after divergence and crisis.

The bank's neighbours: **TM-017**, time-series momentum; **TM-047**, volatility-scaled trend;
**TM-024**, momentum's crashes, the reverse risk of cross-sectional momentum in the same states;
**TM-039**, return dispersion and momentum, the cross-sectional cousin of divergence.

## From the claims to a signal

- **The index.** Each of the seven funds' signal-to-noise ratio over its last 100 daily changes up
  to the session before, averaged over the funds that have them, read from prices whether the funds
  trade or not (as gate 6 hands a left-out cluster's prices to the strategy): the source's MDI, its
  window the 100 days of the evidence the card relies on. The source also uses 250 days elsewhere
  (chapter 8); the conditional-performance evidence is at 100.
- **Divergent.** The index above the average of its daily values from its first reading through the
  session before: the source finds trend following's return close to zero at the average and
  negative below it. Set aside: the source's threshold of 0.1, which it says suits its own portfolio
  only and is to be set for each portfolio; and the level of a random walk, about 1/√100 = 0.10, an
  absolute bar the source does not use for this.
- **Crisis**, the variant: the source's definition, a run of falling months of SPY that loses 5% or
  more in all, read on month closes through the month just ended; the state ends with the first
  month SPY rises. SPY stands for the MSCI World as the source's text on its figure of crises speaks
  of the S&P 500's drawdowns since 1980 (chapter 4). Read a month late, the state misses a run's
  months up to the one in which its loss reaches 5%, and flags the month after its last: 2009-03,
  2019-01 and 2020-04 among them, the months of a violent rebound that Greyserman and Kaminski name
  as a risk to crisis alpha.
- **In the state**, TM-017-01's rule unchanged, lookback 252: each fund whose past-year return beats
  the bill held in a seventh, the rest in cash. **Out of it**, the seven held in equal parts, the
  neutral of the comparison: the theory says trend positions earn nothing there, so the rule holds
  what the benchmark holds rather than bet on a direction, as TM-024-01 held a group in equal parts
  when its tilt was off. Cash out of the state would add a market-timing bet the theory does not
  make.
- **The pace**: TM-017-01's, the first session of each month.
- **DBC**, which starts trading in February 2006, is held in equal parts out of the state from its
  first monthly target after that (March 2006), in trend only once it has a full lookback (from
  February 2007), and it enters the index from 2006-06-29, changing the index's composition. The
  index's first reading is 2005-05-26, so that the first thresholds rest on about 170 sessions.

**A count made before the card.** The audit of this card counted the two states on the lab's data —
the funds' closes and SPY's only, no return of either rule — as the plan's decision on such counts
allows, and it is written here. On the first session of each month from 2006-02 to 2022-12, 203
months: the base is divergent in 95 (47%), in 30 spells, in state after an in-state month 68% of the
time and after an out-of-state month 27%, the index averaging 0.109; the source's crisis, read a
month late, holds in 31 months (15%), about 19 spells, where read after the fact it would cover 21%,
as the source's 20 to 25%. The count did not set any parameter: the window, the threshold and the
depth are the source's.

Two variants, not three.

## What the battery judges, and what to expect

**Against TM-017-01.** Gates 2 to 4 judge the rule against the seven funds held always, as they
judged TM-017-01. The theory is judged by the difference between this rule's alpha and TM-017-01's
rule's, recomputed over this base's sessions and costs — both first hold on 2006-02-01, so they are
TM-017-01's own sessions — as TM-024-01 was judged against CA-001-01 and TM-002-01 against
TM-003-01.

**The size predicted.** For the base, the source gives trend following nothing at the average
divergence and losses below it: turning the rule off in the months after low divergence should cost
nothing and may save its losses. The card predicts a difference at or above zero, and gives no upper
bound: the source's figures are for long-short futures portfolios, and chapter 8's contrary finding
makes even the sign uncertain. For the crisis variant, the source finds trend following earning
little outside crises, but something: holding the rule only in crisis months should leave a
difference near zero or slightly negative. The source's own claim, that crises carry more than half
of the return, allows a difference down to about half of TM-017-01's alpha, inside the band, so the
variant can refute only a larger shortfall, not tell the claim's own range from zero.

**What the long-only form cannot hold.** The source's crisis alpha comes from being long the rising
and short the falling. Its own comparison in equities finds a long-only trend system with the higher
Sharpe ratio (0.41 against 0.36 for the symmetric one, 1999 to 2013) but negative skewness where the
symmetric one has positive (chapter 14). In an uptrend, TM-017-01 and the equal parts hold the same
funds — in equities, uptrends are more than two thirds of the periods of high divergence, by the
source's count — so a long-only rule gains in a divergent state only in divergent declines, by
stepping out of falling funds into cash and holding the rising havens. The card tests when trend
following earns, within what a long-only book holds; it does not test the convexity of a long-short
programme.

**The noise of the difference.** TM-017-01's bets, hedged of its benchmark, moved by about 5.2% a
year (1.55% of alpha at an appraisal ratio of 0.30). This rule departs from it out of the state, 53%
of the months by the count; the difference of the two alphas also carries the difference of their
betas, about 0.35 in those months if TM-017-01's beta is about 0.65, an assumption, times √(0.53 ×
0.47) for the switching, times the benchmark's volatility of about 11%: about 1.9% a year. Together,
about √(0.53 × 5.2² + 1.9²) ≈ 4.2% a year, a standard error of about 1.0% a year over 16.9 years;
for the crisis variant, out of the state 85% of the time, about 1.2%. The clause refutes only below
−1% a year and more than one measured standard error below zero. At a standard error of 1%, it would
refute wrongly about 16% of the time if the true difference were zero, and would refute a true −1.5%
about 69% of the time. It cannot show a gain of any size; a difference above 1% is reported with its
standard error, not taken as proof.

**The test's power.** Gate 4 will count about fourteen effective trials; an appraisal ratio of about
0.7 would be needed to pass it, where TM-017-01's was 0.30. The comparison with TM-017-01 is the
informative test.

**Risks named before the run.**

- **Few spells.** The base is in state in 30 spells, the crisis variant in about 19: a handful of
  long ones decide the difference.
- **An index near noise.** The seven-fund index averages 0.109, barely above a random walk's 0.10
  over 100 changes; three of the funds are equities and two are Treasuries correlated at 0.91.
- **SPY above 30% of the profit**, as it was for TM-017-01 (33%).
- **2009.** TM-017-01 stayed out of equities through the rebound. The divergence rule is in state in
  March 2009 and out from April to July; the crisis rule is in state in February and March 2009.
- **The first thresholds** rest on a short history, and DBC's entry changes the index in 2006.

## Choices, and the options rejected

- **A continuous exposure scaled by the index**: the source's relation is roughly linear above the
  average, but a long-only book cannot scale a trend position beyond a seventh, and the scale would
  be fitted to the source's portfolio, not the lab's.
- **The distance of SPY below its high as the crisis**: it stays on through the whole recovery, 41%
  of the months, where the source's runs of falling months cover 20 to 25%.
- **The VIX-based crisis months of the source's chapters 7 and 14**: the lab holds no VIX.
- **Shorts**: the lab is long only.

## Implementation

Long only, seven funds, each with a European (UCITS) fund or an exchange-traded commodity that
tracks it, rebalanced monthly on closes with the orders filled at the next close: the signals read
the session before, so a day of delay is built in, and gate 6 adds another.
