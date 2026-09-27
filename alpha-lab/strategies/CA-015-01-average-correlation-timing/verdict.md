# CA-015-01 — The sector funds' average correlation as a forecast of their market: verdict

**Stops at gate 2, economic edge. Not refuted, not proven: after the sector funds' average
correlation stood high against its past three years, they earned more over the next month than after
it stood low — a slope of +1.30 percentage points of monthly excess return per unit of the reading's
percentile (standard error 1.64, t +0.79), inside the predicted 0 to 2 and 0.8 standard errors from
zero.** Holding the eleven sector funds in the proportion of that percentile, the rest in cash,
earns a Sharpe ratio of 0.43 in-sample against 0.50 for the funds held always, and an alpha of
−0.29% a year: the share is highest when the sectors are most volatile, so the rule carried a beta
of 0.66, above its average share of 0.47, and its hedged alpha paid for it, as the card warned. It
beats 42.7% of its placebos. Thresholds, version 4; the battery's figures are the notebook's,
[report.ipynb](report.ipynb), and the clause and the reported measures are computed apart from it,
on the same closes. The theory is
[CA-015](../../bank/CA-015-tactical-forecasting-conditional-factor-premia.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; the targets do not change when the prices older
   than the declared memory of 1,240 sessions are scrambled, on 100 dates; 173 decisions, once
   clustered, over 14.7 years in-sample, from the first target on 2008-05-01.
2. **Economic edge: fails.** A Sharpe ratio of 0.430 against the benchmark's 0.500, an alpha of
   −0.29% a year; at twice the costs, 0.424 and −0.36%. Costs are 0.08% a year, 0.006 of a Sharpe
   unit, below the predicted 0.1%.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.962, but the rule beats only 42.7%
   of 1,000 placebos, its own shares shifted in time, where 90% are needed.
4. **Multiple testing: fails.** The appraisal ratio is −0.045, below the predicted 0 to 0.35,
   against 0.629 expected from the best of 71 effective trials by luck: a deflated Sharpe ratio of
   0.005.
5. **Stability: fails.** The blend of the two variants fails gates 2, 3 and 4. By the registry's
   hedged monthly returns, summed, the base's blocks: 2008–09 +3.4%, 2010–14 −5.0%, 2015–19 −0.2%,
   2020–22 −3.6%, 2005–07 empty; without its best year, 2008, the alpha is −1.34% a year.
6. **Robustness: passes.** The neighbours of the window, 47, 79, 32 and 94 sessions, and of the
   lookback, 567, 945, 378 and 1,134, keep a median of 99.9% of the base's Sharpe ratio, at least
   94% at ±25%, and none holds the base's targets; the largest share of the profit is XLK's, 15.1%;
   a day's delay keeps 98%; the universe is one cluster, which the battery does not leave out.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 1.27 and an alpha of 3.57% a
   year, both above the tenth percentile of the in-sample paths (−0.16 and −4.26%).

## The card's refutation, clause by clause

The clause runs over the 176 in-sample months from the base's first target, 2008-05-01, to December
2022, the last ending at the close of 2022-12-30: each month's excess return of the sector funds
that trade at its first session, bought in equal parts at its close and held to the next month's
first close, less the bill compounded, regressed on the base's percentile set at the month's first
session.

- *Refuted if the slope is zero or less*: over the 174 months left once the two months whose sector
  return TM-024-01 published (September 2010, October 2022) are set aside, the slope is **+1.30**
  percentage points a month per unit of percentile, a robust standard error of 1.64, t +0.79. The
  theory is **not refuted**; short of gates 1 to 7, it is **not proven**.
- **With the two published months**: +1.48 (1.61, t +0.92), 176 months.
- **TM-024-01's sector panic months**: 17 of its 18 are in the graded sample, September 2010 being
  one of the two set aside; 15 of the 18 had a percentile above 0.5. Without them, +0.97 (1.46, t
  +0.66), 157 months: the slope does not live in the crisis months alone.
- **The first refutation**, premia constant across regimes, is read by the same slope; **the
  third**, crowding, is not graded.

**The test's power.** The slope's standard error came in at 1.64, above the 1.5 the card estimated;
the share's deviation was 0.308, as counted. The estimate, 1.30, is 0.8 standard errors above zero;
the card's upper figure, about 2.0 for a monthly correlation of 0.1, lies 0.4 standard errors above
it. Neither the sources' strength nor nothing is excluded.

## Measures stated before the run

- **The base's figures**: a beta of 0.655 to the sector funds held always, within the predicted 0.5
  to 0.7; a residual volatility, hedged of them, of 6.4% a year, against about 6% predicted; the
  rule's excess return 6.26% a year against their 9.99%, on a volatility of 14.6% against 20.0%.
- **The variant "median"**, all or nothing against the median: the months after a reading above the
  median earned 1.42% of excess return on average, the others 0.21%, a difference of +1.22% a month
  (0.84%, t +1.44), over 79 and 95 months. In the battery it earned an alpha of +1.98% a year at a
  beta of 0.635, an appraisal ratio of 0.206, on a residual volatility of 9.6%.
- **Pollet and Wilson's quarter**: the excess return over the next 63 sessions from every month's
  first session, on the percentile: +5.96 percentage points per unit (Newey-West with two lags,
  2.64; t +2.26), 173 windows ending by 2022-12-30. The same reading, measured over the source's own
  horizon, is larger and clearer than over the month the rule holds.
- **The average variance**, the other half: its percentile alone, −0.40 (1.38, t −0.29); with the
  correlation's, the correlation +2.16 (1.69, t +1.28) and the variance −1.47 (1.34, t −1.10). The
  two percentiles correlate at 0.54. The signs are Pollet and Wilson's, as Ilmanen reports them: the
  correlation predicts a higher return, the variance, once the correlation is held, a lower one;
  neither is measured to within its noise.
- **By halves**: 2008 to 2014, +1.39 (2.66), 79 months; 2015 to 2022, +1.22 (2.02), 95 months: the
  same sign and size in each.
- **The holdout**, 2023 to 2025: +3.51 (1.83, t +1.92), 36 months.
- **The registry's series**: the base's monthly returns hedged of its benchmark correlate at −0.58
  with TM-047-02's over their 176 common months, and at −0.23 with CA-006-01's. Scaling the market
  down in its volatile months, TM-047-02's rule, and scaling it up in its correlated ones, this
  one's, are near opposites; which of the two volatility parts carried either was not computed.

## What was learned

- **About the theory.** On the lab's sector funds, from 2008 to 2022, the market's average
  correlation carried the sign Pollet and Wilson found, in every half, at the month and more clearly
  at the quarter, and again in the holdout; its variance carried the opposite sign once the
  correlation was held. None of these estimates is two standard errors from zero at the month the
  card grades; the quarter's is, on overlapping windows. The reading forecast the market's premium
  weakly, out of the sources' sample: the theory's second refutation is not met.
- **About the market.** A forecast of the premium is not an alpha against the market. The rule held
  more of the sectors when they were most volatile, and its whole-sample beta of 0.66 charged it for
  exposure it held in the crises that followed. The median rule, cruder, earned an alpha where the
  percentile did not, at almost the same beta; why was not computed, and a variant chosen after the
  result would be a new trial. The battery grades the edge; the theory's claim is the forecast.
- **About the lab.** The theory was first drawn as not testable; its reader showed that the one
  predictor no sibling owns, the correlation among a market's components, had been routed away by a
  misread sentence, and the card was drawn instead. The audit found that the source's 0.20 carries
  no horizon or sample in the library, that TM-024-01 had published a pooled return for its panic
  months, and that CA-006-01 had published a regression of the clause's own dependent variable; all
  were written into the card before its lock. It also foresaw the beta above the average share,
  which is why the card grades the slope and not the alpha.

## Status

CA-015 is `tested-inconclusive`: CA-015-01, the one strategy drawn, stops at gate 2; its clause
neither refutes the theory nor supports it beyond noise, and what it measures is a forecast of the
sector funds' premium with the sources' sign, not an edge over holding them.
