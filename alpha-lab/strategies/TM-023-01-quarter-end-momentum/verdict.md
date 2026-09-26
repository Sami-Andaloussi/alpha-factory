# TM-023-01 — Momentum in the months that end a quarter: verdict

**Stops at gate 2, economic edge. The January half refuted in this form; the quarter-end half not
refuted, not proven: within the lab's groups, the leaders' gap to their group was +1.88% a year
higher in the months that end a quarter than in the other months outside January (standard error
3.37%, t +0.56), inside the predicted +0.5 to +5%, and +5.16% a year higher in January (6.80%, t
+0.76), where the card predicted it lower — past the clause's +0.35.** Holding CA-001-01's momentum
tilt only in March, June, September and December earned an alpha of −0.00% a year over the nineteen
funds in equal parts, 0.51% before costs of 0.51% a year, an appraisal ratio of −0.001 and a Sharpe
ratio of 0.447 against the benchmark's 0.457, inside the predicted −0.3 to +0.6%. Thresholds,
version 4; the battery's figures are the notebook's, [report.ipynb](report.ipynb), and the
group-month gaps, the regressions, the comparisons and the neighbours' alphas are computed apart
from it, on the same closes and costs. The theory is
[TM-023](../../bank/TM-023-momentum-seasonality.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates, and the memory of 252 sessions holds on 100; 137
   decisions, once clustered, over 16.9 years in-sample, from the first session held, 2006-02-02.
2. **Economic edge: fails.** A Sharpe ratio of 0.447, below the benchmark's 0.457, with an alpha of
   −0.00% a year; at twice the costs, 0.419 and −0.49%. Before costs the Sharpe ratio is 0.476;
   costs are 0.51% a year, 0.028 of a Sharpe unit — the tilt taken for one month and dropped, four
   times a year.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.983, but the rule beats 66.7% of
   1,000 placebos, its own weights shifted in time, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is −0.001, against 0.62 expected
   from the best of fifty-five effective trials by luck: a deflated Sharpe ratio of 0.005.
5. **Stability: fails.** The blend of the two variants fails gates 2, 3 and 4. The block alphas:
   2005–07 +1.02% a year, 2008–09 −3.58%, 2010–14 +0.08%, 2015–19 −1.49%, 2020–22 +3.46%; three
   positive blocks of five. Without its best year, 2020, the alpha is −0.45% a year.
6. **Robustness: passes.** The neighbours keep a median of 101% of the base's Sharpe ratio and at
   least 98% at ±25%; without the sectors, the worst cluster to lose, 80% remains; the largest share
   of the profit is XLI's, 9.3%; a day's delay keeps 103%. The neighbours' alphas, computed apart:
   `lookback` 189 0.21% a year (appraisal ratio 0.06), 315 −0.13% (−0.04), 126 0.18% (0.05), 378
   −0.44% (−0.11); `skip` 16 0.25% (0.07), 26 0.30% (0.08), 10 −0.09% (−0.03), 32 −0.09% (−0.03);
   the targets a session late 0.24% (0.07).
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.96 and an alpha of −1.09% a
   year, both above the tenth percentile of the in-sample paths (−0.29 and −2.63%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 5 as well.

## The card's refutation, clause by clause

Over the 203 calendar months from February 2006 to December 2022, each from the close of the session
before its first session to the close of its last, the 596 group-months with two ranked funds or
more, less the sector group's 17 Decembers and 16 Januarys, left out: 563 — 183 in the months that
end a quarter, 31 Januarys and 349 others. The gap of each group's leaders to its ranked funds, both
bought and held over the month, regressed on the quarter-end and January indicators and one constant
for each group, the standard errors clustered by month (203 clusters):

- **The quarter-end half**: +1.88% a year, a standard error of 3.37%, t +0.56. *A t statistic of
  −0.35 or below*: not met. **Not refuted, not proven**: the difference lies in the predicted range,
  0.56 standard errors from zero.
- **The January half**: +5.16% a year, a standard error of 6.80%, t +0.76. *A t statistic of +0.35
  or above*: met. **Refuted in this form**: momentum within the groups was no weaker in January than
  in the other months outside the quarter-ends — in the point estimate, stronger.

**The test's power.** The card judged the standard errors at about 3.9% and 8% a year; they came out
at 3.37% and 6.80%. At those errors the quarter-end half refutes about 36% of the time with no
effect and about 12% at +2.75% a year; the January half refutes about 36% of the time with no effect
and about 20% at −3.25%. The quarter-end coefficient lies 0.26 standard errors below the predicted
middle and 0.56 above zero: neither is excluded. The January coefficient lies 1.24 standard errors
above the predicted middle of −3.25% and 0.83 above the end of the range nearest zero, −0.5%: the
prediction's middle is not excluded at conventional levels, but the clause, set before the run, is
met. January's error rests on 16 clusters of 31 group-months, too few for it to be trusted closely.
With no seasonal effect at all, the two coefficients correlated at about +0.18, at least one of the
two halves refutes about six times in ten: a refutation of one half is weak evidence.

Reported, not graded, as the card stated them:

- **The sector group's December and January**, left out: December +6.54% a year (4.66%) over 17
  group-months, January +0.83% (7.90%) over 16, against −2.48% over the sectors' 119 other months
  outside the quarter-ends: December +9.01% a year above them (standard error 5.0%, t +1.80),
  January +3.30% (7.9%, t +0.42). December leaned the quarter-end half's way, January not the
  January half's.
- **The rule's months**, from each month's first session to the next, the last, December 2022's,
  ending at the close of 2022-12-30, the last in-sample session: the quarter-end half +0.65% a year
  (3.57%, t +0.18), the January half +5.49% (6.33%, t +0.87). The offset session costs the
  quarter-end half most of its lead, as the reasoning warned; January's changed little.
- **Without TM-024-01's 39 panic group-months in the graded sample**: +1.02% (3.50%, t +0.29) and
  +4.97% (7.02%, t +0.71).
- **January against every other month**: +4.47% a year (6.68%, t +0.67).
- **By month of the year**, the gap pooled over every group-month, in % a year: January +3.59 (47
  group-months), February +0.59, March +5.75, April +1.38, May +2.15, June +1.52, July −2.41, August
  −2.91, September −3.44, October +0.08, November −3.74, December +3.08 (47 group-months in January,
  49 in February, 50 in each other month). By group, in % a year, January to December: the
  commodities +11.79, +5.46, +16.13, +17.39, +0.46, +8.38, −7.54, −5.85, −17.36, −6.89, −16.07,
  +3.77 (15 group-months in January and February, 16 in the others); the equity markets −1.34,
  −1.87, +3.08, +0.77, +0.75, −3.51, +4.01, +2.08, −0.41, +7.16, +2.74, −1.02 (16 in January, 17 in
  the others); the sectors +0.83, −1.24, −1.35, −13.09, +5.15, +0.10, −3.99, −5.12, +6.62, −0.43,
  +1.39, +6.54 (16 in January, 17 in the others). By group, the months that end a quarter against
  the other months outside January, averaged over the calendar months: the sectors about +1.8%
  against −2.5% (March to September only), the commodities about +2.7% against −1.9%, the equity
  markets about −0.5% against +2.2%. In January, the commodities +11.8%, the equity markets −1.3%,
  the sectors +0.8%. The quarter-end lead came from the sectors and the commodities; the equity
  markets leaned the other way. The January half's refutation came from the commodities.
- **December against the other months that end a quarter**, over the equity markets and the
  commodities: +0.29% a year (6.86%, t +0.04), 33 group-months.
- **Hedged of the group's market with one beta for each set**: +1.55% (3.32%, t +0.47) and +4.54%
  (6.55%, t +0.69). The gaps did not come from the leaders' market exposure.
- **Against CA-001-01**, by `lab.compare`: the base an alpha 0.21% a year lower (standard error
  1.05%, t −0.20), a beta of 0.981 against 0.947, the bets correlated at 0.585; the variant, the
  tilt held in every month but January, 0.36% lower (0.42%, t −0.87), correlated at 0.960.
- **By period**: 2006–2013 the quarter-end half +1.53% (4.86%, t +0.31), January −13.64% (8.88%, t
  −1.53, 13 group-months); 2014–2022 +2.17% (4.70%, t +0.46) and +18.85% (7.25%, t +2.60, 18);
  without 2008 and 2009 +1.25% (3.48%, t +0.36) and +7.74% (6.32%, t +1.22). January's sign turned
  between the halves of the sample, the earlier half the prediction's way, the later one strongly
  the other.
- **The holdout**, 2023 to 2025: −1.17% (9.15%, t −0.13) and −1.28% (8.21%, t −0.16), over 33 and 6
  group-months.
- **The alphas**: the base −0.00% a year after costs, 0.51% before; the variant −0.16% after costs,
  0.16% before, costs 0.32%; the neighbours' and the delayed rule's in gate 6 above. The hedged
  return by year: 2020 +6.1 points, 2007 +4.5, 2013 +2.9; 2018 −4.5, 2009 −4.3, 2012 −3.1.

## What was learned

- **About the theory.** On the lab's nineteen funds from 2006 to 2022, momentum within the groups
  was not weaker in January: the leaders' gap was 5.16% a year higher there than in the other months
  outside the quarter-ends, driven by the commodities and by the years after 2014, while the years
  to 2013 leaned the prediction's way. The January half of TM-023, which the library signs on stocks
  and among industries, is refuted in this form on the lab's funds. The quarter-end half is not
  refuted and not proven: the months that end a quarter showed a gap about 1.9% a year higher,
  inside the prediction, at a little over half a standard error, carried by the sectors and the
  commodities and absent among the equity markets. In the holdout neither coefficient can be told
  from zero: the quarter-end half −1.17% a year (t −0.13), against the prediction's sign, January
  −1.28% (t −0.16), the prediction's sign on six group-months.
- **About the rule.** Holding the tilt only in the months that end a quarter earned nothing over the
  groups in equal parts after costs of half a point a year; its gross 0.51% was the tilt's, taken
  four times a year. The variant, the tilt kept except in January, earned 0.36% a year less than
  CA-001-01 (standard error 0.42%): the January tilt it drops had earned, in the point estimate, the
  sign the January coefficient shows.
- **About the lab.** The card was drawn after four judgements handed their calendar forms to it, and
  graded the calendar months the sources measure rather than the rule's, which moved the quarter-end
  half from +0.65% to +1.88% a year. It left out the part SC-006-01 had published and kept states
  published only pooled, TM-024-01's panic group-months among them; read literally, RUNBOOK step 3
  would have graded the clause without them, which moves the quarter-end half from +1.88% to +1.02%
  a year and gives the same two conclusions. The reading is now written into step 3. The re-read of
  one rejected theory in ten fell on this card: an independent reviewer recomputed the clause and
  every reported figure from scratch and confirmed them.

TM-023 is `tested-inconclusive`: its one strategy failed gates 2 to 5; the theory's January half is
refuted in this form, and its quarter-end half is not proven, not refuted. The time-series trend by
calendar month, which the reasoning left open for a later strategy, is not drawn: the
cross-sectional form carried both halves, neither came out as predicted with any strength, and a
second trial on the same claim would be chosen from this result.
