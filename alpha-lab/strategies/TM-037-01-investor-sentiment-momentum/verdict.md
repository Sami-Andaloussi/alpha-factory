# TM-037-01 — Market turnover as a contrarian sign of sentiment: verdict

**Stops at gate 1, hygiene, on its count of decisions, as the card expected, and fails gates 2 to 5
as well. Not refuted, not proven: the fund-months after high market turnover earned 3.82% a year
more over the bill than those after low (standard error 13.17%, t +0.29), the opposite of the
predicted sign, short of the +0.35 that refutes.** Holding the fourteen US equity funds in equal
parts, and cash in the months after SPY's log volume over the past year stood above its five-year
average, earned an alpha of −1.21% a year after costs over the funds held always, a Sharpe ratio of
0.39 against 0.49, just below the predicted −1 to +2%. The high state fell in 29 of the 155 months
from February 2010, in three stretches — February 2010 to May 2011, November 2020 to March 2021, May
to December 2022 — and 19 of the 25 graded high months were months of high volatility: the proxy
read stress more than optimism, the risk the card named. Thresholds, version 4; the battery's
figures are the notebook's, [report.ipynb](report.ipynb), and the clause, the reported measures and
the neighbours' alphas are computed apart from it, on the same closes, volumes and costs. The theory
is [TM-037](../../bank/TM-037-investor-sentiment-momentum.md).

## Gate by gate

1. **Hygiene: fails.** No look-ahead on 200 dates, the volumes moved with the prices; the memory of
   1,260 sessions holds on 100; but 8 decisions, once clustered, over 18.0 years in-sample, fewer
   than 30, among them the first holding, the four turns of the state and the entries of XLRE and
   XLC. The card had put 5 to 20.
2. **Economic edge: fails.** A Sharpe ratio of 0.392 against the benchmark's 0.492 and the 0.4
   required, an alpha of −1.21% a year; at twice the costs, 0.391 and −1.22%. Costs are 0.03% a
   year.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.970; the rule beats 14.9% of 1,000
   placebos, its own weights shifted in time by a year or more, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is −0.187, against 0.612 expected
   from the best of sixty effective trials by luck: a deflated Sharpe ratio of 0.000.
5. **Stability: fails.** The blend of the two variants fails gates 2, 3 and 4: a Sharpe ratio of
   0.402 against 0.491, an alpha of −0.77% a year, beating 19.8% of its placebos. The alpha is
   positive in one block of five; until February 2010 the rule holds the benchmark itself, as the
   card said. Without its best year, 2009, the alpha is −1.37%.
6. **Robustness: passes.** The neighbours keep a median of 107% of the base's Sharpe ratio and at
   least 88% at ±25%; without the sector funds 98%; XLK carries 13% of the profit; a day's delay
   keeps 103%. The neighbours' alphas after costs, computed apart: `window` 189 −1.84% a year
   (appraisal ratio −0.25), 315 +0.99% (0.13), 126 −1.06% (−0.14), 378 +0.26% (0.04); the targets a
   session late −0.99% (−0.15); the variant, `window` 21, −0.33% (−0.04).
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.48 and an alpha of −2.66% a
   year, both above the tenth percentile of the in-sample paths (−0.26 and −5.66%).

## Verdict

The strategy stops at gate 1, and fails gates 2 to 5 as well.

## The card's refutation

Over the 149 months from February 2010 to December 2022 left once TM-024-01's six panic months are
out, each from the close of a target's session to the close of the next, the last ending at the
close of 2022-12-30, as the card counted: each fund-month's return less the bill's, regressed on an
indicator of high turnover at the target and one constant for each fund, the standard errors
clustered by month:

- **The months after high market turnover against those after low**: +3.82% a year, a standard
  error of 13.17%, t +0.29, over 324 fund-months after high turnover, in 25 months, and 1,587 after
  low. *A t statistic of +0.35 or above*: not met. **Not refuted, not proven**: the estimate has the
  sign opposite to the prediction, 0.29 standard errors from zero.

**The test's power.** The card took the standard error at 10 to 15%, from TM-028-01's published
13.10%; it came out at 13.17%. At that error the clause refutes about 36% of the time with no effect
and about 24% at the predicted middle, −4.5% a year; the estimate lies 0.63 standard errors above
that middle: neither the prediction nor no effect is excluded.

**What the high state was.** Over the 155 months the state was high in 29 (19%): February 2010 to
May 2011, when the five-year average still held the crisis years and a year of their volume stood
above it; November 2020 to March 2021; and May to December 2022. It turned four times, and was never
high from June 2011 to October 2020. Of TM-024-01's six panic months, the four of 2010 and 2022 fell
in the high state, those of April and May 2020 in the low one. Of the 25 graded high months, 19 were
months in which TM-047-02's scale was below one, its five equity funds' volatility over 21 sessions
above 16% — 19 of that rule's 60 volatile graded months.

Reported, not graded, as the card stated them:

- **The variant**, the month's turnover, `window` 21: −3.62% a year (12.88%, t −0.28), over 530
  high fund-months — the predicted sign, as far from zero as the base on the other side.
- **With TM-024-01's six panic months**: +7.02% a year (12.65%, t +0.56), over 155 months; the two
  whose returns TM-024-01 published, September 2010 and October 2022, rose, both in the high state.
- **With SPY's past year's return as a control**: +3.27% a year (13.27%, t +0.25); the control's own
  coefficient −0.018 a month per unit of return (t −0.54).
- **The measure itself as the regressor**, per unit of log volume: +8.94% a year (22.39%, t +0.40).
- **Without TM-047-02's volatile months**: +6.59% a year (10.86%, t +0.61), over 89 months, 74 high
  fund-months among them.
- **By group**: SPY, QQQ and IWM +3.87% a year (14.59%, t +0.27); the sector funds +3.81% (12.90%,
  t +0.30).
- **By period**: 2010–2016 −0.75% a year (15.51%, t −0.05), 80 months; 2017–2022 +8.33% (21.11%, t
  +0.39), 69 months. **The holdout**, 2023 to 2025: +8.42% a year (14.47%, t +0.58), over 36 months,
  210 high fund-months and 294 low.
- **The alphas**: the base −1.21% a year after costs, −1.18% before, an appraisal ratio of −0.187;
  the neighbours', the variant's and the delayed rule's in gate 6 above.

## What was learned

- **About the theory.** On the lab's fourteen US equity funds from 2010 to 2022, the months after
  SPY's volume over the past year stood above its five-year level were no worse than the months
  after it stood below: 3.82% a year better in the point estimate, 0.29 standard errors, short of
  refuting the contrarian sign and far from proving it. The month's turnover, the variant, gave the
  predicted sign at the same distance from zero, and the neighbours' alphas fell on both sides of
  zero: nothing in the lab's data separates the sign from none. TM-037's second refutation, in its
  market-turnover form, is neither refuted nor proven; its other proxies and its first refutation,
  anomalies stronger after high sentiment, remain unread. Jones's sign and Ilmanen's −0.11 describe
  the whole market's turnover over decades; one fund's share volume over thirteen years gives three
  stretches of high state.
- **About the proxy.** The high state read mostly stress: 19 of its 25 graded months were volatile
  ones, as Ilmanen's chapter 18 warned — liquidity crises coincide with high turnover. The one
  stretch that looks like optimism, late 2020 to early 2021, is five months. The state stayed low
  for nine years, from June 2011 to October 2020, as the card expected of a five-year average that
  held the crisis years' volume.
- **About the rule.** It held the funds in 126 of 155 months from 2010, and the benchmark before.
  Its alpha, −1.21% a year, came from its 29 months in cash, 2010–11 and 2022 above all; its
  placebos, the same weights at other dates, did better 85% of the time.
- **About the lab.** The theory was first drafted not testable; its reader found a form with a sign
  the lab's volumes could read, handed to TM-037 by an earlier reasoning and never taken up. The
  card was drawn knowing that gate 1 would likely fail on its few decisions (SC-019-01), for the
  clause's sake.

TM-037 is `tested-inconclusive`: its one strategy failed gates 1 to 5, and its market-turnover form
is not proven and not refuted. A second trial, the month's turnover or the Baker–Wurgler seesaw on
funds, would be chosen from this result: the variant is reported above, on the predicted side, as
far from zero as the base.
