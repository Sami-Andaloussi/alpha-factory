# CA-006-01 — The sector funds held after a month of financials leading them: verdict

**Stops at gate 2, economic edge. Not refuted, not proven: financials' past month, apart from the
market's own, predicted the sector funds' next month with a slope of +0.083, inside the predicted
0.06 to 0.16 but 0.8 of a standard error from zero; the rule built on it gained nothing.** Holding
the eleven sector funds after a month in which XLF beat their average, and the bill otherwise,
earned an alpha of 0.13% a year over the funds held always, 0.41% before costs of 0.28% a year, an
appraisal ratio of 0.01; the card predicted 1 to 2.5% before costs, a ratio of 0.1 to 0.3. The
market after a positive signal did no better than after a negative one (−0.06% a month): the signal
carries a third of the market's own month, whose coefficient was negative (−0.07), and the two
cancelled. Thresholds, version 4; the battery's figures are the notebook's,
[report.ipynb](report.ipynb), and the regressions, differences, alphas before costs and years are
computed apart from it, on the same sessions. The theory is
[CA-006](../../bank/CA-006-do-industries-lead-stock-markets.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 300 dates; the targets do not change when the prices older
   than the declared memory of 21 sessions are scrambled, on 150 dates; 97 decisions, once
   clustered, over 17.7 years in-sample, from the first holding on 2005-05-02.
2. **Economic edge: fails.** A Sharpe ratio of 0.311, below the 0.4 required and the benchmark's
   0.500, with an alpha of 0.13% a year; at twice the costs, 0.287 and −0.14%. Costs are 0.28% a
   year, 0.024 of a Sharpe unit.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.945; the rule beats 49.7% of 1,000
   placebos, its own weights shifted in time — what a rule without skill beats.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.014, against 0.601 expected
   from the best of thirty-seven effective trials by luck: a deflated Sharpe ratio of 0.007.
5. **Stability: fails.** The blend of the three variants fails gates 2, 3 and 4. The base's alpha is
   positive in four blocks of five — 2005–07 (+7.3% a year), 2008–09 (+0.9%), 2010–14 (+2.6%),
   2020–22 (+1.7%) — and negative in 2015–19 (−6.9%); without its best year, 2020, it is −1.26% a
   year.
6. **Robustness: passes.** The neighbours, windows of 16, 26, 10 and 32 sessions, keep a median of
   147% of the base's low Sharpe ratio and at least 139% at ±25%; the eleven funds form one cluster,
   so none is left out; the largest share of the profit is XLY's, 16.4%; a day's delay keeps 123%.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.12 and an alpha of −3.69% a
   year, both above the tenth percentile of the in-sample paths (−0.34 and −6.52%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 5 as well.

## The card's refutation, clause by clause

Over the 213 monthly targets from 2005-03-01 whose next target falls by 2022-12-30, the sector
funds' average excess return from the target's close to the next target's close, regressed on XLF's
relative return over the 21 sessions before and on the funds' own average return over them: a slope
of +0.083 on XLF's relative return (a standard error of 0.102, t +0.81), and of −0.068 on the
market's own month (t −0.82).

- *A t statistic of −0.35 or below*: not met. The theory is **not refuted**; short of gates 1 to 7,
  it is **not proven**.

**The test's power.** The card gave the clause about a 36% chance of refuting with no lead, 15% at a
slope of 0.06 and 8% at 0.10. The slope measured lies inside the prediction and within noise of
zero: the run can tell neither a lead of the predicted size nor its absence.

Reported, not graded, as the card stated them:

- **The rule's own split**: the market's mean excess return after a positive base signal less after
  a non-positive one, −0.063% a month (a standard error of 0.663%, 95 and 118 months). The absolute
  variant's, −0.56% (0.74%, 122 and 91 months); the composite's, −0.13% (0.68%, 106 and 107).
- **By block of targets**: 2005–2010, a slope of +0.130 (t +0.80) and a difference of +1.47% a month
  (1.44%); 2011–2016, +0.071 (t +0.43) and −0.99% (0.87%); 2017–2022, −0.185 (t −0.79) and −0.74%
  (1.20%). Without the twelve months whose target is set in 2008, a slope of +0.163 (t +1.54) and a
  difference of −0.06% (0.64%).
- **Each fund alone**, its relative return in XLF's place: XLF +0.083 (t +0.81); XLY −0.108 (t
  −0.78); XLRE −0.147 (t −0.71, 73 months); XLE −0.024 (t −0.37); XLB +0.123 (t +0.90). The source's
  signs — positive for the first three, negative for the last two — hold for XLF and XLE, not for
  XLY, XLRE and XLB, all within noise.
- **The alphas**: the base 0.13% a year after costs, 0.41% before, costs 0.28%, invested 96 months;
  the absolute variant 0.22% and 0.52%, costs 0.30%, 123 months; the composite −1.23% and −0.97%,
  costs 0.26%, 106 months.

## What was learned

- **About the theory.** On the lab's sector funds from 2005 to 2022, financials' month apart from
  the market's predicted the market's next with the source's sign, at about the predicted size, but
  within noise: 0.8 of a standard error, 1.5 without 2008, and negative in the last six years. The
  other industries the study ranks did not line up: consumer discretionary, real estate and
  materials leaned against the source's signs, energy with it, all within noise. A lead that shows
  as a small positive slope in one fund and nowhere else is not the pattern of economically tied
  industries the theory describes; nor is it refuted.
- **About the rule.** A regression that holds the market's own month fixed and an in-or-out rule
  that cannot do so measure different things: the rule's signal carried a third of the market's
  month, whose own coefficient was negative, and the rule's split came out at −0.06% a month while
  the slope it was built on was positive. The logic audit had named this leak before the lock; it is
  why the clause graded the slope.
- **About the market.** The rule's best years against the benchmark were 2020 (+11.8 points of
  hedged return), 2005 (+7.3) and 2007 (+7.0); its worst 2015 (−13.4), 2022 (−8.4) and 2018 (−7.9).
  Over the holdout it lost 3.69% a year of alpha, above the in-sample floor.
- **About the lab.** A timing rule on one market read from a member of it carries the market's own
  momentum unless it is removed; the card removed the average and still left a third, since the
  member's beta is not one. The card graded the regression and not the rule's split, and the verdict
  shows why. No code enforces it; the logic audit is where it is caught.

CA-006 is `tested-inconclusive`: on the lab's sector funds from 2005 to 2022, financials' relative
month predicted the market's next with the source's sign at about the predicted size, within noise;
the other industries did not follow the source's pattern, and the rule built on the lead gained
nothing.
