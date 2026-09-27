# CA-003-01 — Style momentum within sectors and equity markets: verdict

**Stops at gate 3, significance. Not refuted, not proven: in the month after a style had earned, it
earned 0.16% more than after a month it had not (standard error 0.31%, t +0.52) — inside the
predicted 0 to 1.1% a month, near its bottom; a persistence of Ilmanen's size, about 1.1% a month,
lies three standard errors above the estimate, and once each style's own markets are taken into the
regression the difference is nil.** Holding each of three styles built from the funds' closes —
momentum, value and defensive, within the sector funds and within the equity markets — in its long
leg after a month it earned, and in the funds held in equal parts otherwise, earns a Sharpe ratio of
0.47 in-sample against 0.44 for the sixteen funds held in equal parts, and an alpha of 0.53% a year,
0.26% at twice the costs: it passes gate 2. It beats 72.4% of its placebos, where 90% are needed.
Thresholds, version 4; the battery's figures are the notebook's, [report.ipynb](report.ipynb), and
the clause, the styles' records, their correlations and the registry's correlations and years are
computed apart from it, on the same closes. The theory is
[CA-003](../../bank/CA-003-factor-momentum.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; the targets do not change when the prices older
   than the declared memory of 1,600 sessions are scrambled, on 100 dates; 182 decisions, once
   clustered, over 16.7 years in-sample, from the first target on 2006-04-03.
2. **Economic edge: passes.** A Sharpe ratio of 0.468 against the benchmark's 0.445, an alpha of
   0.53% a year; at twice the costs, 0.454 and 0.26%. Costs are 0.28% a year, 0.014 of a Sharpe
   unit, inside the predicted 0.2 to 0.4%.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.988, but the rule beats only 72.4%
   of 1,000 placebos, its own weights shifted in time, where 90% are needed.
4. **Multiple testing: fails.** The appraisal ratio is 0.202, inside the predicted 0 to 0.7, against
   0.616 expected from the best of 66 effective trials by luck: a deflated Sharpe ratio of 0.057.
5. **Stability: fails.** The blend of the two variants passes gate 2 but fails gates 3 and 4. The
   alpha is positive in two of the five blocks; by the registry's hedged monthly returns, summed,
   about −1.2% in 2006–07, −1.3% in 2008–09, +4.5% in 2010–14, −3.7% in 2015–19 and +10.4% in
   2020–22. Without its best year, 2022, the alpha is 0.23% a year.
6. **Robustness: passes.** The neighbours of the window, 16, 26, 10 and 32 sessions, keep a median
   of 95% of the base's Sharpe ratio, at least 94% at ±25%, and none holds the base's targets; with
   the sector funds left out, 76%; the largest share of the profit is XLE's, 19.1%; a day's delay
   keeps 100%.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.88 and an alpha of −0.06% a
   year, both above the tenth percentile of the in-sample paths (−0.18 and −1.40%).

## The card's refutation, clause by clause

The clause pools the three styles' months, each from its own first formation with a 21-session
record — momentum and defensive from April 2006, value from April 2010 — to December 2022: 555
style-months over 201 months. Each style's long/short return over the month is regressed on a
constant for each style and an indicator that the style had earned at the formation, the standard
errors clustered by month.

- *Refuted if the indicator's coefficient is zero or below*: it is **+0.16% a month**, standard
  error 0.31%, t +0.52. The theory is **not refuted**; short of gates 1 to 7, it is **not proven**.
- **TM-024-01's panic group-months.** Twenty of the momentum style's months fall in a panic state of
  either group — October 2008 to November 2009, July to September 2010, April and May 2020 and
  October 2022 — nine of them after the style had earned, eleven after it had not: 55% in one set,
  below the card's 90%. They stay in the graded sample, disclosed. Without them the coefficient is
  +0.24% a month (standard error 0.29%, t +0.81).
- **The second refutation** is not graded. Its industry half, the clause over the equity markets
  alone, where no industry enters, gives +0.23% a month (standard error 0.27%, t +0.85); over the
  sector funds alone, +0.13% (0.40%, t +0.32). In both, each group's long/short return is read
  against the style's own state, which both groups set.

**The test's power.** The coefficient is measured to ±0.31% a month, as the card estimated. The
estimate, +0.16%, is half a standard error above zero and three below the 1.1% a month that
Ilmanen's +0.20 would give on a style volatility of 3.5% a month: a correlation of about +0.03
between a style's adjacent months, at the bottom of the predicted 0 to +0.2. A persistence of +0.1,
about 0.55% a month, lies 1.25 standard errors above the estimate and cannot be ruled out.

## Measures stated before the run

- **Each style apart**: momentum −0.21% a month (standard error 0.43%, t −0.49), earned in 54% of
  its 201 months; value +0.48% (0.41%, t +1.16), earned in 44% of its 153 months; defensive +0.30%
  (0.45%, t +0.67), earned in 49% of its 201 months. Their monthly long/short returns autocorrelate
  at lag 1 at +0.025, +0.155 and −0.019; at lag 2 at −0.126, −0.035 and −0.097; at lag 3 at −0.095,
  +0.038 and +0.038.
- **The styles' correlations** over their common months: momentum with value −0.28, as CA-024-01
  published for the same tilts; momentum with defensive +0.40; value with defensive −0.13.
- **With each style's markets as a further regressor**, the month's return of its groups' ranked
  members held in equal parts, a slope for each style: the coefficient is **0.00%** a month
  (standard error 0.26%, t −0.00). What persistence the styles showed went with their markets' own
  months; which style carried it was not computed.
- **The variant, a window of 252 sessions**: −0.11% a month over its 523 style-months (standard
  error 0.30%, t −0.37); its appraisal ratio in the battery, 0.137.
- **Without value**: +0.01% a month over 2006 to 2013 (0.64%, t +0.02), +0.07% over 2014 to 2022
  (0.42%, t +0.18). **The holdout**, 2023 to 2025: +0.34% a month (0.75%, t +0.45), over 108
  style-months.
- **The cross-sectional reading**, the style with the highest last-21-session return less the style
  with the lowest, held over the next month: +0.10% a month over 201 months (standard error 0.28%).
- **The registry's series**: the base's hedged monthly returns correlate at 0.36 with CA-001-01's
  and at 0.33 with TM-003-01's over their 201 common months: a third of its timing's gains and
  losses go with members' and industries' momentum.
- **The alpha by year**, by the registry's hedged monthly returns summed: 2009 −3.3%, the year of
  momentum's crash, and 2020 +4.7%; the best, 2022, +4.9%; the worst, 2009; ten years of gain and
  seven of loss.

## What was learned

- **About the theory.** On the lab's funds, three styles built within two groups did not persist
  from one month to the next by a measurable amount. The sign came out as predicted, at the size of
  noise; a persistence as strong as Ilmanen reports across asset classes and strategies from 1990 to
  2009 is ruled out here, a weaker one is not. With the markets' own months in the regression,
  nothing is left: the defensive style is short the market, as the reasoning warned, and the one
  sizable autocorrelation, value's +0.155 at lag 1, over 153 months, is about two standard errors
  from zero on its own.
- **About the market.** The lab's published books now agree at one month: TM-038-01's trend book
  reverted slightly, TM-017-02's funds and MR-032-01's members barely continued, and these styles
  sit between. What earned in 2020 and 2022 — the rule's two best years — earned in months when the
  styles and their markets moved together.
- **About the lab.** The first judgement drew this theory as not testable by reading "factor" too
  narrowly; its reader found the form the library supports and four earlier judgements had handed
  here. The chain held: the card was audited, locked, run once, and its clause computed apart, as
  TM-038-01's was. `lab.compare` refuses cards whose universes differ; the audit replaced the
  comparisons the first draft promised with the registry's correlations.

## Status

CA-003 is `tested-inconclusive`: CA-003-01, the one strategy drawn, stops at gate 3; its clause
neither refutes the theory nor supports it beyond noise.
