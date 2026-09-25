# SC-023-01 — The assets that beat their beta in a calendar month in past years: verdict

**Stops at gate 2, economic edge. Refuted in this form, narrowly: from February 2010 to December
2022, the two assets ranked highest on their past residual returns in the same calendar month,
beyond their beta to the universe's average, earned 0.10% a month less than the ranked assets'
average residual, 0.40 standard errors below zero, just past the clause's −0.35; the test could not
tell an effect of the predicted size from none, and the rank correlation over the whole
cross-section, reported, leaned the other way, 1.45 standard errors above zero.** Holding the two in
equal parts each month earned an alpha of −0.99% a year over the universe's tradable assets held
always in equal parts, +0.05% before costs of 1.03% a year, an appraisal ratio of −0.08 and a Sharpe
ratio of 0.385, inside the predicted 0 to +3% before costs and −0.12 to +0.18, at their lower end.
Thresholds, version 4; the battery's figures are the notebook's, [report.ipynb](report.ipynb), and
the monthly returns, residuals, the clause, the reported gaps and the neighbours' alphas are
computed apart from it, on the same closes and costs. The theory is
[SC-023](../../bank/SC-023-return-seasonalities.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 100 dates, and none over 50 dates at the memory of 1,290
   sessions; 154 decisions, once clustered, over 12.9 years in-sample, from the first target on
   2010-01-29. The decision sessions are the market's 252 month ends from 2005 to 2025, none missing
   and none added; 17 to 20 assets ranked each month, 19 in 125 of the 155; SLV ranked from May
   2011, DBC from March 2011, XLRE from October 2021, XLC from July 2023, outside the sample. One
   decision, the end of June 2016, recomputed apart from the strategy, holds the same two funds.
2. **Economic edge: fails.** A Sharpe ratio of 0.385, below the 0.4 required and the benchmark's
   0.674, with an alpha of −0.99% a year; at twice the costs, 0.325 and −2.02%. Before costs the
   Sharpe ratio is 0.446; costs are 1.03% a year, 0.060 of a Sharpe unit.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.930, below 0.95; the rule beats
   42.9% of 1,000 placebos, its own weights shifted in time.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is −0.076, against 0.645 expected
   from the best of forty-nine effective trials by luck: a deflated Sharpe ratio of 0.005.
5. **Stability: fails.** The blend of the variants, the base alone, fails gates 2, 3 and 4. The
   battery's block alphas: 2005–07 and 2008–09 hold nothing, 2010–14 −1.36% a year, 2015–19
   +3.00%, 2020–22 −7.79%; one positive block of five. Without its best year, 2020, the alpha is
   −2.92% a year.
6. **Robustness: fails.** A ±25% neighbour, `top` 1, keeps −4% of the base's Sharpe ratio, below
   50%; the neighbours keep 117% at the median, and a day's delay 84%. The largest share of the
   profit is IWM's, 24%, under 30%; without the bonds, the worst cluster, the rule keeps 79%. The
   neighbours' alphas, computed apart: `years` 4 −0.71% a year (appraisal ratio −0.05), 6 +0.24%
   (0.02), 2 +1.98% (0.15), 8 +0.77% (0.06); `top` 1 −9.31% (−0.51), 3 −0.37% (−0.04); the targets a
   session late −1.99% (−0.15). The neighbours at 6 and 8 years sit in cash for their first 12 and
   36 months, as the card said. The card expected the base to fail gate 2 or 3, and gates 4 and 5,
   and perhaps gate 6 on one asset's share of the profit: it failed gates 2 to 5 as expected, and
   gate 6 not on a share, which passed, but on the `top` 1 neighbour. Its tracking error came out at
   13.0% a year, against the card's estimate of about 10%.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.99 and an alpha of 6.03% a
   year, both above the tenth percentile of the in-sample paths (−0.38 and −12.45%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 6 as well.

## The card's refutation, clause by clause

Over the 155 calendar months from February 2010 to December 2022, each ranked asset's raw return in
the month less its pre-month beta times the average's return: the two assets the base ranks highest,
less all the assets it ranks, −0.102% a month, a standard deviation of 3.18% across months, a
standard error of 0.255%, t −0.40.

- *A t statistic of −0.35 or below*: met. The theory is **refuted in this form**, by 0.05 of a
  standard error.

**The test's power.** The card gave the clause about a 36% chance of refuting with no effect and 5
to 9% at +0.25% a month, the top of its range, with a standard error of 0.2 to 0.25%. The standard
error came out at 0.255%, the ranking favouring assets whose residuals move more than a random
pair's (a standard deviation of 3.18% a month against about 2.4%). The gap lies 0.10% below the
range's floor and 1.4 standard errors below its top: the clause's refutation is the lab's
convention, and does not set the gap apart from nothing.

Reported, not graded, as the card stated them, each with the standard error across the 155 months:

- **The raw ranking**, on raw past same-month returns, graded on raw returns: −0.594% a month
  (0.280%, t −2.12). Ranking on raw returns across classes picked worse, not better. The raw gap
  splits exactly into the raw picks' residual gap, −0.389% (t −1.45), and their beta times the
  average's return, −0.205% (t −1.69): about a third of the shortfall came through exposure, the
  market's and the classes' calendars that the residual removes, and the rest from the raw picks
  lagging beyond their beta.
- **The rank correlation** between the signal and the month's residuals across the ranked assets: a
  mean of +0.038 (0.026, t +1.45); on raw returns, −0.040 (0.030, t −1.37). Over the whole
  cross-section the residual signal leaned toward the claim, while its two highest did not: the two
  lowest did worse than the average, the two highest no better, and whatever order the signal held
  was not at its top.
- **The short side**, the two ranked lowest less the average: −0.222% (0.284%, t −0.78), as the
  claim predicts but inside a standard error; the top two less the bottom two, +0.12% (0.425%, t
  +0.28).
- **The one-year lag alone**: +0.094% (0.289%, t +0.33). **The demeaned signal**, less each asset's
  mean residual over the window: −0.200% (0.242%, t −0.83).
- **Momentum**: ranked on the residual return over months m − 13 to m − 2, the months the rule can
  read, +0.374% (0.291%, t +1.29); its rank correlation with the signal, +0.239 (0.026, t +9.0). The
  same-month signal shares some of its order with residual momentum (0.24), partly by construction,
  since momentum's window holds month m − 12, the signal's one-year lag; momentum's top two beat the
  signal's by 0.48% a month, month by month (0.351%, t +1.36).
- **Reversals outside the matching month**: the top group's residual over the other eleven months
  of the same year, less the ranked assets', +0.041% a month (0.100%, t +0.41): no offsetting
  weakness. Its beta to the average, 0.970 in the matching months against 0.937 in the others; its
  pre-month beta 0.86 on average against the ranked assets' 1.00.
- **The average weights held fixed**: the rule less its own average weights, gross, −0.134% a month
  (0.272%, t −0.49): the month-by-month choice added nothing to where the rule sat on average.
- **By group**: within the sector funds alone, +0.028% (0.166%, t +0.17); across the other assets
  alone, +0.163% (0.247%, t +0.66).
- **By period**: 2010–2016 −0.054% (0.362%); 2017–2022 −0.158% (0.360%); **without 2020** −0.161%
  (0.265%, t −0.61).
- **The holdings**: gold in 41 months, silver 34, TLT 31, XLU 26, QQQ 24, XLK 23, and twelve others
  fewer; a Treasury fund in 32 of the 155. Each asset's share of the gross profit, measured apart on
  the months' raw returns at the month's start weights, and not the battery's measure at gate 6 (IWM
  24%): QQQ 16.3%, IWM 14.5%, gold 12.9%, EEM 10.0%, XLF 9.1%, silver 8.7%, XLB 7.9%, XLU 7.5%, XLI
  7.4%, XLV 6.5%, TLT 5.9%, IEF 5.9%, XLY 3.0%, XLK 2.1%, EFA 0.7%, XLP −3.8%, DBC −6.8%, XLE −7.8%.
- **The alphas**: the rule −0.99% a year after costs, +0.05% before, costs 1.03%, an appraisal ratio
  of −0.08, a regression beta of 0.82 and a tracking error of 13.0% a year; the neighbours' and the
  delayed rule's in gate 6 above. The hedged return by year: 2020 +16.5 points, 2010 +9.5, 2017
  +8.0; 2022 −21.8, 2013 −21.0, 2021 −19.0.

## What was learned

- **About the theory.** Across the lab's twenty-one funds of five classes, from 2010 to 2022, an
  asset's past returns in a calendar month, beyond its exposure to the others' average, did not pick
  the assets that beat that average in the month again: the two ranked highest did slightly worse,
  the two ranked lowest worse still, and the ranking as a whole leaned faintly toward the claim,
  1.45 standard errors from nothing. The same-month signal shared some of its order with residual
  momentum, which ranked better, by 1.4 standard errors, and the top group showed no reversal in the
  other months. SC-023 is refuted in this form, narrowly and with little power: the lab's funds are
  few and far less dispersed than the stocks of the sources, and Chan had already found the stock
  form gone after 2002.
- **About the rule.** Two funds a month, most months replaced, the rule paid about 1% a year in
  costs for an alpha before them of nearly nothing; 2013, 2021 and 2022 cost about twenty points of
  hedged return each. Ranked on raw returns the rule would have done worse, a third of it through
  the classes' calendar, which the raw ranking picks and which lost, and the rest beyond the picks'
  beta. The holdout, 2023 to 2025, added 6% a year of alpha, above every in-sample block but not a
  reason to reopen a refuted form.
- **About the lab.** Across asset classes a raw same-month ranking grades the market's month-of-year
  pattern, SC-017's claim, through the assets' betas; the card ranked and graded residuals beyond
  each asset's beta for that reason, and reported the raw form. The raw form came out at −2.1
  standard errors and the residual at −0.4: removing the exposure changed the size of the gap, not
  the verdict.

SC-023 is `tested-inconclusive`: its one strategy failed gates 2 to 6, and the theory is refuted,
narrowly, in the one form the lab can test — the lab's funds across asset classes ranked on their
own calendar month beyond their beta; the weekday form is out of reach of a rule held with a day's
delay.
