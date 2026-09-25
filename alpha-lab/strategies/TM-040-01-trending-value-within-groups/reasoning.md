# TM-040-01 — Value and momentum together within sectors, equity markets and commodities: reasoning

## Why this theory now

TM-040, the combination of value and momentum ("trending value"), holds that selecting on both value
and momentum earns more, for its risk, than selecting on either alone: the two are negatively
correlated, momentum stocks tend to be dear and value stocks recent losers, so that their
combination diversifies each one's risk and avoids both value traps, cheap assets that keep falling,
and momentum bubbles. Its two halves have been tested within the same three groups of funds:
CA-001-01 held the top third of each group by its past year, CA-024-01 the bottom third by its past
five years. This card tests their combination, on the same funds and groups, against each of them.

**What the lab already knows, before anything else.** The two halves' verdicts are published, so
that the card cannot be blind:

- CA-001-01's verdict gives its base's alpha over 2006 to 2022, 0.20% a year, and its record by
  year; CA-024-01's gives its base's, −0.63% a year from 2010 to 2022, its hedged return by year,
  and, over the same sessions, CA-001-01's alpha, 0.90% a year, and the correlation of the two
  rules' hedged monthly returns, −0.28.
- From these, an equal blend of the two rules would have earned about 0.13% a year (about 0.20%
  under the battery's version 4, which CA-024-01's verdict reports: value's alpha −0.49%, its
  appraisal ratio −0.10), at a tracking error of about 3.3% given the halves' tracking errors,
  about 6% for momentum and 4.9% for value, and their correlation: an appraisal ratio of about
  0.04 to 0.07, against about 0.15 for momentum over the same sessions — about half a standard
  error below it. A rule that behaves like the blend is thus known to land, in-sample, below
  momentum and short of a refutation.
- Both halves lost to the benchmark in 2015–19 (CA-001-01's block and CA-024-01's, −2.97% a year):
  a rule that behaves like the blend is known to fail gate 5, which needs all three of its blocks
  positive.
- The holdout, 2023 to 2025, has been opened by every earlier card on these funds, and the halves'
  holdout alphas are published, −0.44% and +1.43% a year: a blend's would be about +0.5%.

What is not known is how a rule that selects on both at once, in each fund, differs from that blend
— the one part of the claim this card can still test — and the placebos. The card is written with
this knowledge declared; the verdict will read the in-sample result against it, and the blend is
reported beside the base.

**The bank's other theories this card touches**, all untouched: **CA-021**, value across sectors,
countries and asset classes, uses fundamental ratios; **MR-021**, long-term reversal, is value's
price-only measure alone; **CA-022**, value spreads, conditions value on its own dispersion. None is
this card's combination.

**The sources.** The lab read them in the library's books; Asness, Moskowitz and Pedersen's study
(2013; its 2009 working version) is known to the lab through them.

- O'Shaughnessy (*What Works on Wall Street*, 4th edition, 2011, chapter 27) builds "Trending
  Value": from the decile of US stocks with the best composite of six value ratios, buy the 25 or
  50 with the best six-month price appreciation, held in equal parts, each portfolio held a year and
  the twelve monthly start dates composited. From 1964 to 2009 the 25-stock version earned 21.19% a
  year against 17.30% for the value decile alone, 14.52% for the six-month momentum decile alone
  and 11.22% for all stocks, with a lower standard deviation than all stocks (17.44% against
  18.99%); it beat all stocks in every rolling five- and ten-year period. He names the years it lags
  — 1998 and 1999, when speculative winners soared.
- Ilmanen (*Expected Returns*, 2011, §12.6) calls value and momentum the two most popular equity
  selection indicators and "natural opposites", whose negative correlation means that combining
  them "can sharply reduce portfolio volatility and boost Sharpe ratios"; he adds the aphorism that
  when value and momentum clash, value almost always loses first. In §24.2 he describes the
  simplest way to combine indicators across assets: rank the assets on each indicator and hold
  those with the best average rank, which "works surprisingly well".
- Pedersen (*Efficiently Inefficient*, 2015) writes that combining value and momentum delivers
  higher risk-adjusted returns than either alone, the two being negatively correlated, and that an
  asset with both — "a cheap stock on the rise" — has a better chance of continuing its trend and
  of delivering its value; he shows Asness, Moskowitz and Pedersen's combination of the two signals
  in equity country indices, currencies, bonds and commodities, calling it powerful, and warns that
  it is unintuitive to look for a cheap country trending upward, since by definition one misses
  the bottom.
- The Zacks *Handbook of Equity Market Anomalies* (2011) reports the same study: value returns
  negatively correlated with momentum's, and, "because the value and momentum strategies both earn
  positive returns", combinations with significantly better risk and return than either alone.
  In-sample, value by price within these groups did not earn a positive return: the source's
  premise fails here.
- Ilmanen (*Investing Amid Low Expected Returns*, 2022) puts the correlation of value and momentum
  strategies often near −0.5, and the best blend near 50/50 unless their standalone Sharpe ratios
  are very different — which they are in-sample.
- Gray and Vogel (*Quantitative Momentum*, 2016) test long-only portfolios half in value and half in
  momentum across markets from 1982 to 2014: the risk-adjusted statistics improve, but only
  marginally.

## From the claim to a signal

- **The two measures, as the halves measured them**: value is the return over the past five years,
  1,260 sessions, to the session before the target, reversed (CA-024-01's base, the price-only
  measure the sources name where no fundamental ratio is used); momentum is the return over the
  past year skipping the last month, 252 and 21 sessions (CA-001-01's base, the study's measure). On
  the equity groups the lab's value is long-run reversal, the weaker cousin of value by book to
  price, as CA-024-01's card said.
- **The combination**, base: within each group, every ranked member gets its rank by value (1 the
  cheapest) and its rank by momentum (1 the strongest); the members with the best average of the two
  ranks, the top third of the group, rounded, one at least, are held — Ilmanen's composite ranking,
  and Pedersen's "cheap stock on the rise". Averages of two ranks tie often, at the cut in about 40%
  of months in a synthetic draw: the members whose average equals the k-th lowest share equally the
  places not taken by members with a lower average, so that neither measure breaks a tie. A
  tie-break by momentum, from Ilmanen's aphorism that value loses first when the two clash, was set
  aside: the aphorism counsels patience with value signals, not a rule for ties, and it would lean
  the base to momentum (in a group of three, in a synthetic draw, it would hold momentum's pick
  about four times in five).
- **Variants.** First, the same composite with momentum measured over six months, 126 sessions,
  without a skip: O'Shaughnessy's measure. Second, O'Shaughnessy's construction itself, adapted to
  groups of three to eleven funds: the cheaper half of each group by value, rounded up, then among
  those the top third of the group by six-month momentum. His screen is a decile of thousands of
  stocks; in groups this small a decile is one fund or none, so the lab reads his screen as the
  cheaper half, the smallest screen that leaves momentum a choice in every group — a reading, not a
  figure from the source. Both variants' horizons come from the sources.
- **The groups and the weights**: CA-001-01's and CA-024-01's, unchanged, so that the combination
  is compared with its halves on equal terms. A member is ranked when it trades and has five years
  of prices; of the N funds trading, a group of n ranked members holds n/N of the portfolio, split
  equally among its chosen members, and a fund trading but not ranked is held at 1/N, its benchmark
  weight. Targets on the first session of each month; the first on 2010-02-01, as CA-024-01's.
- **Monthly, not yearly**: O'Shaughnessy holds each portfolio a year, in twelve overlapping
  tranches; the core rebalances monthly, and both halves did; the card keeps their pace.
- **The memory**: 1,260 sessions, the value window, which is longer than every momentum window of
  the variants and neighbours (the shortest value window, 630, against the longest momentum one,
  378): a member is ranked when it has five years of prices.
- **Members ranked in-sample**: the sectors nine, then ten once XLRE has five years, in late 2020
  (three held; the screen keeps five); XLC is ranked only in the holdout. The commodities one, then
  two, then three from 2011 (SLV and DBC start in 2006); with two members the composite holds one,
  and a tie at the cut shares it.

The pace was counted before the card by a scratch script outside the repository (`pace.py`, in the
session's scratch folder) that reads the signals alone, no return, under the tie-sharing rule: 155
monthly targets for each rule, and about 145 months in which the base's or the six-month
composite's selection changes, about 120 for the screen.

## What the battery judges, and what to expect

**The benchmark and the references.** The battery judges the base against the nineteen funds held in
equal parts. The claim is judged against the two halves: CA-001-01's base and CA-024-01's base,
each rebuilt from its own locked code over this base's evaluation sessions, from the first session
it holds into, at the same costs, by `python -m lab.compare` against each.

**Where the card departs from the bank's refutation.** The bank refutes the theory by a
combination that earns no more than the better factor alone, or with no reduction in volatility.
The card does not judge the return: a combination's alpha in-sample is known to lie below
momentum's, since value lost, and the sources' own claim (Ilmanen, Pedersen, the Zacks handbook) is
the risk-adjusted one. The volatility side is reported, not graded: the base's tracking error
against each half's.

**The size predicted**, from the long record. CA-001-01's card predicted about 2% a year of alpha
for momentum within these groups at a tracking error of about 6%, CA-024-01's 0.7 to 1.5% for value,
and the sources put the correlation between the two often near −0.5. A composite earns about the
average of the two alphas, 1.3 to 1.8% a year; at a tracking error lowered as a blend's, by √((1 +
ρ)/2), about 0.5 at ρ = −0.5, an appraisal ratio of about 0.45 to 0.6, but a composite that holds a
third of each group, as each half does, keeps more of either's tracking error — 0.85 of it or more,
a reading, where its appraisal ratio would be about 0.25. That is an appraisal ratio of about 0.25
to 0.6 against about 0.33 for momentum alone: a gain only if the composite's tracking error falls
near a blend's, and long-only evidence (Gray and Vogel) shows the gain as marginal. At half the long
record's premia, about 0.7 to 0.9% a year of alpha. O'Shaughnessy's selection on both did better
than either alone in return as well, about 4% a year above his better half; a screen on nineteen
funds cannot be expected to repeat it, and the card predicts no gain in return over momentum alone.
Costs: a selection that changes most months, about 0.2% a year, between CA-024-01's 0.12% and
CA-001-01's 0.24%.

**The clause.** Judged on the base's appraisal ratio, its alpha over the same funds held in equal
parts divided by the tracking error of its hedged returns, against the better half's: the half with
the higher appraisal ratio over the same sessions, fixed on the whole sample before any draw. The
difference and its standard error are `lab.compare`'s, from 1,000 paired draws of whole calendar
months of the two hedged daily series, from a fixed seed. The theory is refuted in this form if the
base's appraisal ratio is below the better half's by more than one standard error of the
difference. Any other result short of passing gates 1 to 7 is not proven, not refuted: an
appraisal ratio above the better half's is reported with its standard error, as the sources
predict, not as proof. Should the base pass gates 1 to 7 while the clause refutes, the theory is
refuted in this form and the verdict says so beside the pass; the bank's status follows the
runbook's step 9 all the same, `tested-conclusive` for a strategy that passed, with the refutation
named in the verdict. A first draft also asked the base to
fall below the other half's ratio; the logic audit showed that, with value's ratio known to be
about −0.10, it would refute only a combination worse than value alone — the flaw the runbook names
for a second condition — and it was dropped.

**The test's power.** A synthetic simulation made by the logic audit — Gaussian daily returns over
155 months, the halves' tracking errors about 6% and 4.9% and their correlation −0.28, the base's
correlation 0.55 to 0.8 with momentum and 0.3 to 0.55 with value — gives the clause's rates. With a
combination no better than its better half it refutes about 20% of the time; at a gain of 0.05,
11 to 16%; at 0.15, 4 to 8%; with a combination worse by 0.1, 33 to 45%. The bootstrap's standard
error matches the spread of a fixed pair's difference; the simulation's wider figure, about 0.22 to
0.27, comes from choosing the better half after the fact. It can show the claim false only if the
combination does clearly worse than its better half. Gate 4, over some thirty trials, needs an
appraisal ratio of about 0.9.

**Measures stated before the run**, reported, not graded:

- the variants, the six-month composite and O'Shaughnessy's screen, by the same comparison;
- each rule's alpha and tracking error, and the two halves', over the same sessions — the base's
  tracking error against each half's is the bank's test of a reduced volatility; the alpha of the
  base less each half's (`lab.compare`), with its standard error;
- an equal blend of the two halves, the average of their hedged daily returns: the base's
  appraisal ratio less the blend's, with its standard error, by `lab.compare.ratio_difference` of
  the base's hedged series against the blend's — whether
  selecting on both at once does better than blending, the part of the claim not already known;
- the correlation of the base's hedged monthly returns with each half's, and of the halves' with
  each other over these sessions;
- the base's alpha by group, as CA-024-01 measured its own;
- the alpha by year, and in 2020 and 2022, the years that decided CA-024-01's record.

**Risks named before the run.**

- **Known halves.** Momentum earned more than value from 2010 to 2022, and a blend's appraisal ratio
  is known to lie about half a standard error below momentum's; the composite's is not known, but a
  composite that behaves like the blend lands short of a refutation and of a proof.
- **Three blocks, all needed.** As in CA-024-01, the base's first holding in 2010 leaves gate 5
  three blocks, all of which must be positive.
- **Few members.** The commodities hold one place, the equity markets two, shared among tied
  members; in a group of two or three the composite often holds the same fund as one of the measures
  alone.
- **The neighbours' start.** The value window moved to 1,575 or 1,890 sessions starts the
  neighbour's targets in 2011 or 2012, which lowers its Sharpe ratio against the base's, as in
  CA-024-01.

## Choices, and the options rejected

- **An equal blend of the two halves' portfolios as the base** — Gray and Vogel's combination, half
  in each: its in-sample figures are close to known from the two published verdicts, and it is
  reported beside the base; the composite selects on both in each fund, as Ilmanen and Pedersen
  describe, and is not known.
- **Value by fundamental ratios**: the lab holds prices only.
- **O'Shaughnessy's decile screen**: one fund or none in groups this small.
- **Annual holding with monthly tranches**: the core rebalances monthly.
- **A short leg**: the lab is long only.

## Implementation

Long only, nineteen funds, each with a European (UCITS) fund that tracks it, monthly targets filled
at the close of the session on which they are set; gate 6 adds a day's delay.
