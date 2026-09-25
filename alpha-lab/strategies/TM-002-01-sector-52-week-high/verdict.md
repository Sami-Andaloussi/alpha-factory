# TM-002-01 — Nearness to the 52-week high among sector funds: verdict

**Stops at gate 3, significance. Not proven, not refuted; its second claim not shown. In-sample, the alpha
is a tilt, not timing.** Holding, each month, the three sector funds nearest their 52-week high, in
six overlapping monthly tranches, earns a Sharpe ratio of 0.52 in-sample against 0.49 for the
sector funds held in equal parts, and an alpha of 0.96% a year: it passes gate 2. But it beats
44.0% of its placebos, about what a rule without skill beats, because its alpha comes from which
funds it holds on the whole — more of the steadier funds, less of the most volatile — rather than
from when it holds them: its average weights, held fixed, earn 1.34% a year. Against
the same rule ranked on six-month returns (TM-003-01's base), over the same sessions, it earns
0.21% a year less, with a standard error of 1.01%. Its holdout alpha, −2.60% a year, falls below
the in-sample floor. Thresholds, version 2; the battery's figures are the notebook's,
[report.ipynb](report.ipynb), and the comparison with TM-003-01, the variant's own figures, the
years and the holdings are computed apart from it, on the same sessions and costs. The theory is
[TM-002](../../bank/TM-002-52-week-high-momentum.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; 192 decisions, once clustered, over 17.0 years
   in-sample, from the first holding on 2006-01-03, once the funds had 252 closes.
2. **Economic edge: passes.** A Sharpe ratio of 0.52 against the benchmark's 0.49, an alpha of 0.96%
   a year; at twice the costs, 0.51 and 0.85%. Costs are 0.12% a year.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.99; the rule beats 44.0% of 1,000
   placebos, its own weights shifted in time by a year or more, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.17, against 0.39 expected
   from the best of eleven effective trials by luck: a deflated Sharpe ratio of 0.21.
5. **Stability: fails.** The blend of the two variants passes gate 2 and fails gates 3 and 4 (39.8%
   of its placebos beaten, a deflated Sharpe ratio of 0.18). The alpha is positive in three of the
   five blocks — 2010–14 (1.3% a year), 2015–19 (1.3%) and 2020–22 (1.3%) — and negative in 2005–07
   (−1.5%) and 2008–09 (−4.2%). Without its best year, 2013, it stays positive, 0.64% a year. The
   worst variant's Sharpe ratio is 0.51.
6. **Robustness: passes.** The neighbours of the window and the holding keep a median of 99% of the
   base's Sharpe ratio, and at least 99% at ±25%; no fund carries more than 24% of the profit
   (XLK); a day's delay costs nothing. The check of a cluster left out does not apply: the sectors
   are one cluster, the whole universe.
7. **Sealed holdout: fails.** Over 2023 to 2025, a Sharpe ratio of 0.58, above its floor of −0.15,
   but an alpha of −2.60% a year, below the tenth percentile of the in-sample paths, −2.36%.

## Verdict

The strategy stops at gate 3, and fails gates 4, 5 and 7 as well.

## The card's refutation, clause by clause

- *The first claim — an appraisal ratio of −0.1 or less, with half of its placebos beaten or
  fewer*: the placebo half is met, 44.0%, but the ratio is 0.17, 1.1 standard errors above −0.1:
  **not refuted**. Short of gates 1 to 7, the first claim is **not proven**.
- *The second claim — the base's alpha less TM-003-01's base, recomputed over this base's sessions
  from 2006-01-03 (1.17% a year there)*: −0.21% a year, with a standard error of 1.01% measured on
  the monthly differences (a t-statistic of −0.21). It lies within 1% either way: **not shown**, and
  not refuted.
- *The variant, by its appraisal ratio alone*: 0.13, above −0.1, below the predicted 0.2 to 0.3:
  **not proven**.

**The test's power.** The difference's standard error came in at 1.01% a year, as the reasoning
estimated, though for another reason than it assumed: the two rules' bets were correlated at 0.73,
not 0.8, and shared 67% of their weight — a third differing, for which the reasoning's band gave
1.3% — but this rule's bets moved by 5.6% a year, not 6.3%. At that noise, the clause could refute
nearness doing clearly worse than past returns, and could not tell the predicted gain, nothing to
1% a year, from zero. The base's appraisal ratio of 0.17, measured to ±0.24, sits just below the
prediction's range of 0.2 to 0.3, well within one standard error of it, and 0.7 standard errors
above zero; its alpha, 0.96%, is just below the predicted 1 to 2%.

## What was learned

- **About the theory.** On sector funds, nearness to the 52-week high picked the steadier funds
  and avoided the most volatile. Its average active weights, against the equal weight, were +8.7
  points of staples, +2.7 of health care, +2.0 of utilities and +3.1 of technology, and −5.6 of
  energy, −5.0 of financials and −4.2 of materials. XLP, XLU, XLV and XLRE held 48% of it on average,
  and more than half in 44% of the months, where the equal weight holds 35% and TM-003-01 held 36%,
  more than half in 26%. A hedged alpha does not come from a low beta itself — the regression takes
  the beta out — but from funds earning more than their beta implies. From 2006 to 2022 the steady
  funds did (staples +3.7% a year of alpha over the equal weight at a beta of 0.61, health care +3.7%
  at 0.74, utilities +2.2% at 0.73) and the volatile ones did not (financials −5.7% at 1.40, energy
  −2.3% at 1.29, materials −1.2% at 1.14); overweighting the first and underweighting the second
  each gave about 40% of the alpha, technology and communication most of the rest. Whether that is the low-volatility anomaly or these sectors'
  own history — the financial crisis, the oil slump — the verdict cannot tell.

  The mix explains the result. The rule's average weights, held fixed and reset monthly, earn an
  alpha of 1.34% a year, an appraisal ratio of 0.61, more than the rule's 0.96%. The placebos shift
  every fund's weights by the same offset, so each keeps the rule's average mix: their defensive
  share is 48%, as the rule's, and their median alpha 1.02%, which the rule's beats in 49% of 300 placebos drawn apart.
  Timing added nothing in-sample; it cost about 0.4 points a year. The rule's beta, 0.84, is lower than its mix's, 0.91, because it
  held the defensive funds most when markets were most volatile — 83% of it in 2009, 59% in 2008 —
  when a regression weighs most; so the beta is not a pure measure of the mix.

  The reasoning named this risk: funds that move less sit nearer their highs, and dividends paid
  since the high, which the lab's adjusted closes count, push the high-yield ones nearer still; the
  verdict cannot separate the two. What looks like the anchor is, on these funds, mostly the
  measure's own tilt.
- **About the market.** The rule gained most in 2011 (+3.9% of edge), when utilities, staples and
  health care rose 12 to 20% and financials fell 17%, and in 2013, 2015 and 2019 (+6.5%, +4.8% and
  +4.7%) — years in which it was not especially defensive: in 2013 its defensive share, 33%, was
  below the equal weight's, and 2019 was led by technology, financials and communication. It lost
  most in 2009 (−5.7%), when technology, materials and consumer discretionary led the recovery and
  staples and utilities trailed; in 2010 (−3.0%), led by industrials, consumer discretionary and
  energy, with health care and utilities trailing; and in 2006 (−4.0%). Against TM-003-01 it did
  better in 2011, 2014, 2017 and 2019, and much worse in 2020 and 2022 (−6.4 and −7.9 points of
  hedged return): in 2020 it held staples and health care, 42% of it, where TM-003-01 held technology
  and communication, 47%; in 2022 it held energy at 15%, where TM-003-01 held 26%, and staples and
  utilities at 47%, against 40%. Technology carried the largest share of its profit, 24%, consumer
  discretionary, health care and staples about 15% each.
- **About the holdout.** Over 2023–25 communication and technology more than doubled (+153% and
  +136%), consumer discretionary rose 90%, and staples, energy and health care 13 to 20%. The rule was
  not defensive then: staples, utilities and health care held 28% of it, about the equal weight's
  27%, and its beta was 0.97. Its edge was −8.6% in 2023, +3.1% in 2024 and −2.2% in 2025, an alpha
  of −2.60% a year, below the floor that gate 7 draws from the in-sample paths; 2023 alone was worse
  than any in-sample year. This loss was timing: the rule's own average mix of those years, held
  fixed, earned +2.42% a year, and its in-sample mix held through them −0.46%. Timing, which cost about
  0.4 points a year in-sample, cost about five in the holdout. Three years say little about an edge.
- **About the lab.** A ranking by a measure that also sorts assets by risk can pass gate 2 on the
  tilt alone. Gates 3 and 4 both stopped this one; the placebos, which keep the mix and shift the
  timing, are what showed that its alpha lies in the mix — though gate 3 would reject an alpha from
  the mix even if the mix earned a real premium. The comparison with TM-003-01 over the same
  sessions, sized before the run from its noise, came in at the noise estimated, and said what the
  lab could and could not tell.

TM-002 is `tested-inconclusive`: among the eleven US sector funds, long only, the funds nearest their
52-week high earned a small alpha that a tilt to the steadier funds explains better than the anchor, no better
than the six-month leaders; the anchor on single stocks' quoted highs, and the short side where the
source finds most of the effect, are untested.
