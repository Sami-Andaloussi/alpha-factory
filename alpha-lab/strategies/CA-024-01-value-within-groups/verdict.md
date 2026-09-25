# CA-024-01 — Value within sectors, equity markets and commodities: verdict

**Stops at gate 2, economic edge. Not refuted, not proven — though the clause's first condition is
met: the cheapest third of each group by its past five years earned 0.63% a year less than the
groups held in equal parts from 2010 to 2022, and only its rank among its placebos, 92.4%, kept the
clause from refuting it.** The placebos, the rule's own weights shifted in time, lost more than the
rule: the composition it held, mostly the foreign equity markets, the commodity basket and energy,
lost to the groups at almost any timing, and the rule's ranking lost less than the same rankings
moved further away in time (found after the result, below). Its appraisal ratio, −0.130, is 0.9 to
1.4 standard errors below the predicted 0.12 to 0.25, and 0.5 below zero: this run can tell neither
from the other. Of the measures stated before the run, the equity markets carried the loss, value
and momentum were negatively correlated as the sources find, and the value tilt's hedged returns
were positively correlated across the three groups, as the theory claims. Thresholds, version 3; the
battery's figures are the notebook's, [report.ipynb](report.ipynb), and the variants' alphas before
costs and betas, the groups' alphas, the correlations, the years, the funds held and the placebos'
alphas are computed apart from it, on the same sessions and costs. The theory is
[CA-024](../../bank/CA-024-value-momentum-everywhere.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 300 dates; the targets do not change when the prices older
   than the declared memory of 1,260 sessions are scrambled, on 150 dates; 70 decisions, once
   clustered, over 12.9 years in-sample, from the first holding on 2010-02-01.
2. **Economic edge: fails.** A Sharpe ratio of 0.579, below the benchmark's 0.644, and an alpha of
   −0.63% a year; at twice the costs, 0.572 and −0.73%. Costs are 0.12% a year, 0.007 of a Sharpe
   unit.
3. **Significance: passes.** The probabilistic Sharpe ratio is 0.986; the rule beats 92.4% of 1,000
   placebos, its own weights shifted in time by a year or more, kept beyond the signal's memory past
   their wrap, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is −0.130, against 0.569 expected
   from the best of twenty-eight effective trials by luck: a deflated Sharpe ratio of 0.006.
5. **Stability: fails.** The blend of the three variants passes gate 3 but fails gates 2 (a Sharpe
   ratio of 0.584 against 0.644, an alpha of −0.65%) and 4 (a deflated Sharpe ratio of 0.005). The
   base holds nothing before 2010, so that 2005–07 and 2008–09 count as not positive; its alpha is
   −0.46% a year in 2010–14, −2.97% in 2015–19 and +2.52% in 2020–22: one positive block of the
   three it needed. Without its best year, 2022, the alpha is −2.30% a year.
6. **Robustness: passes.** The neighbours, 945, 1,575, 630 and 1,890 sessions, keep a median of 99%
   of the base's Sharpe ratio and at least 72% at ±25%; with the sector funds left out, 54%; the
   largest share of the profit is XLE's, 22.8%; a day's delay keeps 98%.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 1.07 and an alpha of 1.43% a
   year, both above the tenth percentile of the in-sample paths (−0.14 and −4.92%).

## Verdict

The strategy stops at gate 2, and fails gates 4 and 5 as well.

## The card's refutation, clause by clause

Judged on the base, from its first holding on 2010-02-01: its alpha over the same funds held in
equal parts is −0.63% a year, as gate 2 measures it; it beats 92.4% of its placebos.

- *The alpha zero or less*: met.
- *Half of the placebos beaten or fewer*: not met. The theory is **not refuted**; short of gates 1
  to 7, it is **not proven**. The clause needed both conditions, and the verdict keeps the clause
  as it was locked; what spared the refutation is read below, under "About the placebos".

**The test's power.** The card estimated that the clause would refute about 34% of the time with no
edge and 24% at the low end of the prediction. The run measured an appraisal ratio of −0.130, where
thirteen years measure it to about ±0.28: 0.46 standard errors below zero, 0.9 below the low end of
the prediction (0.12) and 1.4 below its top (0.25). The run cannot tell a vanished premium from the
low end of the long record's.

Reported, not graded, as the card stated them:

- **The variants.** The three-year window: an alpha of −0.21% a year, −0.05% before costs, an
  appraisal ratio of −0.04, a beta of 1.06. Five years with the last year skipped: −1.11%, −0.98%
  before costs, −0.24, a beta of 1.01. The base: −0.51% before costs, a beta of 1.02.
- **By group**, the value tilt against its own group's ranked members held in equal parts, a beta
  for each, from the groups' daily returns with the weights held from each target (their drift
  ignored, so that the groups' shares do not add up exactly to the base's alpha): the sector funds
  +0.98% a year (a standard error of 1.88%), a beta of 1.04; the equity markets −3.24% (1.67%), a
  beta of 0.96; the commodities +0.05% (3.52%), a beta of 0.80. Only the equity markets' is more
  than a standard error from zero, 1.9 below it.
- **The common structure.** The tilt's hedged monthly returns, over 155 months, correlate at 0.29
  between the sector funds and the equity markets, 0.24 between the equity markets and the
  commodities, and 0.13 between the sector funds and the commodities: positive, as the theory
  claims, the first two three to four standard errors from zero. With CA-001-01's momentum rule, its
  base run over the same sessions, the value rule's hedged monthly returns correlate at −0.28,
  negative as the sources find; the momentum rule's alpha over those sessions is 0.90% a year.
- **By year**, the value rule's return hedged of the benchmark, in points: 2010 −0.2, 2011 −0.8,
  2012 +4.7, 2013 −2.6, 2014 −3.1, 2015 −3.9, 2016 +0.4, 2017 +0.6, 2018 −5.9, 2019 −4.2, 2020
  −9.5, 2021 −0.9, 2022 +17.3: positive in four years of thirteen, 2022 the largest by far. The
  2010 figure carries the first session's −1.9 points (below, under "About the battery").
- **In 2020**, −9.5 points, the worst year, of which the crash from 19 February to 23 March cost
  1.8, the seven weeks before it 4.8 and the rest of the year 2.9: the loss was not in the
  deleveraging the sources warn about.

## What was learned

- **About the theory.** On the lab's nineteen funds from 2010 to 2022, value measured by price — the
  cheapest third of each group by its past five years — earned less than the groups, −0.63% a year,
  within noise of zero and of the low end of the prediction, and short of the long record's premium
  in every form the card named: the three-year window lost less, the form that skips the last year
  lost more. The loss sat in the equity markets, where the cheapest members were the foreign funds
  (EFA held in 97% of the months, EEM in 79%), which fell further behind the US through the decade
  (measured after the result against the group's ranked members: EFA −4.2% a year, EEM −6.4%);
  the sector funds' tilt earned about +1% a year and the commodities' nothing, both within noise.
  The structure the theory claims appeared: the tilt's hedged returns were positively correlated
  across the three groups, and negatively with momentum's. The card named the decade before the
  run: the result says that value by price within these groups earned nothing from 2010 to 2022, not
  that it never does. The mechanisms the bank names — underreaction, overreaction, funding
  constraints, risk aversion, segmentation — are not tested.
- **About the placebos, found after the result.** Gate 3's placebos, drawn as it draws them (400
  here) and priced as it prices them, where the rule itself comes to −0.50% a year: their alphas had
  a median of −1.57% a year, 90% of them below −0.62%, and 1.8% of them above zero. The further the
  weights were moved in time, back or, past the wrap, forward, the more they lost: a median of
  −1.10% for shifts of one to three years, −1.54% for three to six, −1.81% for six to eight.
  Shifting the weights in time keeps their average, and this rule's average is far from equal weight
  — EFA, EEM, DBC and XLE held among the cheapest in 66% to 97% of the months, XLK and QQQ never;
  that composition lost to the groups at almost any timing, and the rule's rank among its placebos
  measures its timing within it, not whether the cheap members beat their groups. Two readings fit:
  the ranking carries information that decays, so that a ranking beats the same rankings moved in
  time; or, in a decade in which the same funds stayed cheap and kept losing, a ranking nearer in
  time had shed some of the losers. Read after the result, it grades nothing.
- **About the market.** The rule's best years against the benchmark were 2022 (+17.3 points,
  energy's year) and 2012 (+4.7); its worst 2020 (−9.5), 2018 (−5.9) and 2019 (−4.2). Over the
  holdout, 2023 to 2025, it earned an alpha of 1.43% a year, above the in-sample floor.
- **About the lab.** A refutation clause that asks for a non-positive alpha *and* a rank at or below
  half of the placebos assumes that the placebos earn about the benchmark. Shifting the weights in
  time keeps their average: a slow rule whose holdings persist averages far from equal weight, and
  if that average loses at every timing, the placebos lose too, and the placebo condition spares a
  theory on which the first condition alone would count. The runbook now says so: a card for such a
  rule says which condition carries the claim, and why. No code enforces it: the lab has no check
  that tells a clause's conditions apart, and the logic audit is where it is caught.
- **About the battery, found by the review.** Gate 2's period, like every gate's, began on the
  session of the first target, 2010-02-01, on which the rule held nothing into the day, its orders
  filled at the close, while the benchmark, invested since 2005, rose 1.8%: that one session costs
  the alpha 0.15% a year and 2010 1.9 points. Without it, the alpha is −0.49% a year (an appraisal
  ratio of −0.10), 2010 +1.7 points, five years of thirteen positive, and 2010–14 −0.11%; the
  placebos, priced from the next session, set the rule at −0.50%. The clause's condition is met
  either way. The battery's version 4 counts every return the gates judge from the first session
  the rule holds into, the targets still judged from the first target; this card's figures are
  version 3's, as its run was.

CA-024 is `tested-inconclusive`: on the lab's nineteen funds from 2010 to 2022, the cheapest third
of each group by its past five years' price earned 0.63% a year less than the groups, within noise
of zero and of the low end of the prediction; the clause's placebo condition, not met because the
rule's own weights, moved in time, lost more, kept it from a refutation; the value tilt's returns
correlated positively across the groups and negatively with momentum's, as the theory claims. Its
momentum half is CA-001-01's, refuted in its base form.
