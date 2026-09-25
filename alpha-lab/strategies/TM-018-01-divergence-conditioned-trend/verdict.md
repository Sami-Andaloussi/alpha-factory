# TM-018-01 — Trend following switched on by divergence or crisis: verdict

**Stops at gate 2, economic edge. Refuted in this narrow form, in both variants: holding TM-017-01's
trend rule only after divergent months, or only after crisis months, lost about 1.2% a year of alpha
against TM-017-01's rule held always.** TM-017-01's rule, recomputed over the same sessions, earns
1.55% a year over the seven funds held in equal parts; held only in the months after its market
divergence index stood above its average, and the seven in equal parts otherwise, it earns 0.34%, a
difference of −1.22% a year with a standard error of 1.02%. Held only after a run of falling months
of SPY that lost 5% or more, it earns 0.38%, −1.18% with a standard error of 1.08%. Both lie below
the band of 1% and more than one standard error below zero. The conditioned rules earned about the
same return as TM-017-01's rule with a beta higher by about a quarter (0.66 against 0.42): the
shortfall is in alpha, not in return. Thresholds, version 2; the battery's figures are the
notebook's, [report.ipynb](report.ipynb), and the comparison with TM-017-01, the diagnostic by
state, the years and the variant's figures are computed apart from it, on the same sessions and
costs. The theory is [TM-018](../../bank/TM-018-market-divergence-crisis-alpha.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; 86 decisions, once clustered, over 16.9 years
in-sample, from the first holding on 2006-02-01. 2. **Economic edge: fails.** A Sharpe ratio of
0.37, below the 0.4 required and below the benchmark's 0.41, and an alpha of 0.34% a year; at twice
the costs, 0.36 and 0.25%. Costs are 0.10% a year. 3. **Significance: fails.** The probabilistic
Sharpe ratio is 0.95; the rule beats 52.3% of 1,000 placebos, its own weights shifted in time by a
year or more, where 90% are needed. 4. **Multiple testing: fails.** The alpha, as an appraisal
ratio, is 0.06, against 0.43 expected from the best of fifteen effective trials by luck: a deflated
Sharpe ratio of 0.08. 5. **Stability: fails.** The blend of the two variants fails gates 2, 3 and 4
(a Sharpe ratio of 0.39, an alpha of 0.36% a year, 51.9% of its placebos beaten). The alpha is
positive in three of the five blocks — 2005–07 (0.5% a year), 2008–09 (5.9%) and 2010–14 (0.7%) —
and negative in 2015–19 and 2020–22 (−3.4% each); without its best year, 2009, it is −0.31% a year.
6. **Robustness: fails.** SPY carries 37% of the profit, above the 30% any one fund may, as it
carried 33% of TM-017-01's. The rest holds: the neighbours keep a median of 102% of the base's
Sharpe ratio and at least 74% at ±25%; without the bonds, the worst cluster to lose, 63% remains; a
day's delay keeps 94%. 7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.94 and
an alpha of 0.46% a year, both above the tenth percentile of the in-sample paths (−0.42 and −3.66%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 6 as well.

## The card's refutation, clause by clause

TM-017-01's rule, recomputed over the base's sessions from 2006-02-01 at the same costs, earns
1.554% a year, as its verdict recorded under version 1 (1.55%): version 2 changed nothing for it.

- *The base — a difference below −1% a year and more than one standard error of the monthly
  differences below zero*: the difference is −1.22% a year, the standard error 1.02% (a t-statistic
  of −1.20). Both conditions are met: the theory is **refuted in this form** — TM-017-01's edge
  lies, at least in part, in the months after the index was below its average, which the lagged
  reading says give none. This says nothing against the relation the source measures over the same
  period, which the lab does not test.
- *The variant — the crisis claim alone*: −1.18% a year, a standard error of 1.08% (−1.09). Both
  conditions are met: the claim that crises carry more than half of trend following's edge is
  **refuted in this form**, crises read a month late on SPY's runs of falling months.

The standard errors ignore the error in estimating each rule's beta, a small addition.

**Where the shortfall comes from.** The raw excess returns barely differ from TM-017-01's: −0.11% a
year for the base, +0.04% for the variant. The conditioned rules' betas are 0.66 and 0.68 against
TM-017-01's 0.42; the extra beta times the benchmark's premium of 4.6% a year, about 1.1% and 1.2%,
is the whole difference in alpha. Holding the seven in equal parts out of the state keeps the
return and adds the market's exposure, which a hedged alpha does not pay.

**A diagnostic, chosen after the result.** The card fixed the measure above, and the verdict rests
on it alone. After the run, TM-017-01's own hedged edge was split by the true state of each month —
read from the signal, as the reasoning's count before the card did: divergent in 95 of 203 months
(47%), in crisis in 31 (15%). At TM-017-01's single beta:

| | Months | TM-017-01's edge a year in those months | Its share of the 1.55% |
|---|---|---|---|
| Divergence, in the state | 47% | 1.10% | 0.52% |
| Divergence, out of it | 53% | 1.95% | 1.04% |
| Crisis, in the state | 15% | −1.75% | −0.27% |
| Crisis, out of it | 85% | 2.15% | 1.82% |

TM-017-01 earned more per month outside the divergent months than inside them, and none of its edge
in the months after crises. With each rule given a beta for each state, the differences are −0.97%
for the base, at the band's edge, and −1.41% for the variant: neither reads the shortfall as a gain.
An earlier table in the draft of this verdict inferred the states from the targets and misclassed
the 26 months in which TM-017-01 held all seven funds; the independent review found it.

**The test's power.** The standard errors came in as the reasoning estimated, 1.02% for the base and
1.08% for the variant, against about 1.0% and 1.2%. At that noise the clause refutes wrongly about
16% of the time if the true difference is zero.

## What was learned

- **About the theory.** On seven long-only funds from 2006 to 2022, trend following did not earn
  mostly after divergent months or after equity crises. The largest single difference was 2009: from
  April to July the base, out of the divergent state, held the seven in equal parts and caught the
  rebound TM-017-01 missed, +13.0 points of hedged return over those months (+15.8 over the year,
  2.8 of them from January and February, when the two rules held the same funds and only their hedge
  betas differed). The crisis variant gained less in 2009, +7.5, having held the seven in equal
  parts in January (−5.1). The base's largest losses were 2022 (−11.2 points), 2015 (−10.2), 2020
  (−5.6) and 2008 (−5.3); the variant's 2022 (−9.8), 2015 (−7.5), 2013 (−5.4) and 2007 (−3.1), while
  its 2020 gained 4.7. In those years TM-017-01's edge was positive and the conditioned rules spent
  part of the year in equal parts. The source's crisis alpha comes from shorting the falling as well
  as holding the rising; a long-only rule's months after a crisis carried none of its edge.
- **About the market.** SPY carried 37% of the base's profit, gold 19%, long Treasuries 18% and
  commodities 17%. The rule's alpha is positive in the blocks to 2014 and negative after, where
  TM-017-01's was positive in four blocks of five.
- **About the lab.** A clause that compares two whole-sample alphas measures a rule that switches
  between a low-beta and a full-beta portfolio with one beta, and charges it for the market exposure
  it adds; here the whole shortfall is that exposure, the returns being the same. TM-024-01's review
  used a state measure to show its clause was not harsh; here a state measure, done right, comes to
  about the same figure as the clause. Such a measure must read the states from the signal, give
  both rules a beta for each state, and say how it treats the months in which the two portfolios are
  the same; a later card of this kind should state it before its run. A diagnostic chosen after the
  result informs, and does not grade, the card's verdict.

TM-018 is `tested-inconclusive`: its two tradable forms on the lab's funds — TM-017-01's trend rule
held only after divergent months, or only after equity crises — are refuted as the card's clause
reads; the relation the source measures over the same period, and the convexity of a long-short
programme, are not tested.
