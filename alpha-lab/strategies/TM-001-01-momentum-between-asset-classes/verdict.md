# TM-001-01 — Momentum between asset classes: verdict

**Stops at gate 2, economic edge. Not refuted, not proven: from 2006 to 2022 the two of the seven
funds with the best past year, the last month skipped, earned 1.78% a year more than the seven in
equal parts before costs, at the top of the predicted 0 to +2%, but 0.57 standard errors from zero;
held in the rule, they made a portfolio more volatile than the seven for the same Sharpe ratio, and
the gap came from the years in which markets did not fall, not from the rebounds.** Holding the top
two each month earned an alpha of 2.71% a year over the seven, 2.95% before costs of 0.24% a year,
an appraisal ratio of 0.20, and a Sharpe ratio of 0.394 against the benchmark's 0.407; at a beta of
one, rather than the regression's 0.79, the gap after costs is 1.72% a year. Thresholds, version 4;
the battery's figures are the notebook's, [report.ipynb](report.ipynb), and the monthly gaps, their
standard errors, the holdings, the neighbours' alphas and the comparison with TM-017-01 are computed
apart from it, on the same closes and costs. The theory is
[TM-001](../../bank/TM-001-cross-sectional-price-momentum.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; 75 decisions, once clustered, over 16.9 years
   in-sample, from the first holding on 2006-02-02; the ranking reads closes up to the session
   before, and DBC is ranked a full year after it starts trading. The holdings changed in 74 of 202
   months, about one month in three.
2. **Economic edge: fails.** A Sharpe ratio of 0.394, below the 0.4 required and the benchmark's
   0.407, with an alpha of 2.71% a year; at twice the costs, 0.379 and 2.49%. Before costs the
   Sharpe ratio is 0.409; costs are 0.24% a year, 0.015 of a Sharpe unit. The two funds held move by
   16.1% a year against the seven's 11.4%: the alpha is positive in the regression's sense, but it
   buys no better ratio of return to risk than the seven held always.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.958, above 0.95, but the rule beats
   74.2% of 1,000 placebos, its own weights shifted in time, fewer than 90%.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.20, against 0.63 expected
   from the best of fifty-three effective trials by luck: a deflated Sharpe ratio of 0.047.
5. **Stability: fails.** The blend of the two variants fails gates 2, 3 and 4 (a Sharpe ratio of
   0.365, an alpha of 2.13% a year, 70.5% of its placebos beaten); the worse variant, the last month
   kept, has a Sharpe ratio of 0.324. The block alphas: 2005–07 −4.77% a year, 2008–09 −1.61%,
   2010–14 +5.07%, 2015–19 −1.75%, 2020–22 +3.79%; two positive blocks of five. Without its best
   year, 2013, the alpha is 1.31% a year.
6. **Robustness: passes.** The neighbours keep a median of 103% of the base's Sharpe ratio and at
   least 69% at ±25%; without the metals, the worst cluster to lose, 88% remains; the largest share
   of the profit is GLD's, 23.8%, under 30%, where the card had expected one asset's share or the
   `top` 1 neighbour likely to fail; a day's delay keeps 103%. The neighbours' alphas, computed
   apart: `lookback` 189 2.21% a year (appraisal ratio 0.17), 315 0.40% (0.03), 126 3.50% (0.26),
   378 0.39% (0.03); `skip` 16 2.71% (0.22), 26 2.32% (0.19), 10 4.55% (0.35), 32 2.47% (0.20);
   `top` 1 3.09% (0.17), 3 2.12% (0.20); the targets a session late 2.90% (0.22). The longer
   windows, of fifteen and eighteen months, kept almost nothing of the alpha; the shorter ones kept
   it or more.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 1.20 and an alpha of 5.36% a
   year, both above the tenth percentile of the in-sample paths (−0.39 and −7.63%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 5 as well.

## The card's refutation, clause by clause

Over the 203 in-sample months from the first target, 2006-02-01, the last ending at the close of
2022-12-30, each from the close of a month's first session to the next's: the top two by the base's
signal, in equal parts, less the equal weight of the funds trading — +0.149% a month, +1.78% a
year, a standard error of 0.263% a month, t +0.57. The strategy's own targets held the same two
funds in every month.

- *A t statistic of −0.35 or below*: not met. The theory is **not refuted** in this form, and not
  proven.

**The test's power.** The card gave the clause about a 36% chance of refuting with no effect and 8
to 16% at +2% a year, with a monthly gap moving by about 7.7 to 13% a year; it moved by 13.0%, the
top of that range and SC-023-01's published figure, for a standard error of 3.15% a year. The gap
lies at the top of the predicted range and 0.57 standard errors from nothing: the test cannot tell
it from none.

Reported, not graded, as the card stated them, each a monthly mean with its standard error over the
months:

- **The variant**, the last month kept: +0.56% a year (3.12%, t +0.18), weaker than the base, the
  other way from CA-001-01, where keeping the last month did a little better.
- **The winners less the losers**, the top two less the bottom two: +3.32% a year (5.80%, t +0.57).
- **Ranked by the window's return over its daily volatility**: +0.74% a year (3.08%, t +0.24). Most
  of the raw ranking's gap went with the volatility it chose: ranked for risk, the leaders beat the
  seven by less than half as much.
- **The alpha at a beta of one**: the clause's gap, 1.78% a year before costs; after costs, 1.72%,
  against the regression's 2.71% at a beta of 0.79. The lower beta carried about a third of the
  alpha.
- **What was held**: GLD in 78 months, SPY 73, TLT 66, EEM 58, EFA 50, DBC 50, IEF 31. Both places
  went to one class in 94 of 203 months — the equity funds in 53, the Treasuries in 21, gold and the
  commodity basket in 20 — and IEF and TLT were held together in those 21, the duration bet the card
  named.
- **January**: −1.84% a year (7.24%, 16 months) against +2.09% (3.37%) in the other months — weaker,
  in TM-023's direction, on too few months to read.
- **After the seven fell over the past year**: −5.93% a year (9.33%, t −0.64, 43 months) against
  +3.85% (3.12%, t +1.24) in the others. From July to December 2008 −4.98% a year (6 months), the
  rule holding gold and the commodity basket through the autumn's fall, then the two Treasury funds;
  from March to December 2009 −21.6% a year (10 months, t −0.88), holding the Treasuries, then IEF
  with gold, through the equity rebound until October, and emerging equities only from November,
  developed ones from December. A long-only rule has no short side to lose on a rebound; it lost by
  trailing it, as the card said it would.
- **By period**: 2006–2013 +3.08% a year (5.43%); 2014–2022 +0.64% (3.53%); without the months of
  2008 +1.35% (2.93%); without those of 2020 +2.18% (3.16%). By year, the gap's largest sums were
  2013 +24.3 points and 2022 +13.9, and its worst 2009 −9.3, 2018 −9.3 and 2016 −8.7.
- **The holdout**, 2023 to 2025: +7.26% a year (3.29%, t +2.20), over 36 months.
- **Against TM-017-01**, on the same months: the two rules held exactly the same assets in 14 of 203
  months (6.9%), since TM-017-01 holds every asset in trend, often more than two; their monthly
  returns less the seven's correlate at 0.61. TM-017-01's return less the seven's, its cash earning
  the bill, was −1.15% a year (2.02%): the relative ranking, always invested, beat the seven where
  the absolute rule, often partly in cash, trailed them in return and won on risk.
- **The alphas**: the base 2.71% a year after costs, 2.95% before; the variant 1.55% and 1.79%; the
  neighbours' and the delayed rule's in gate 6 above. The hedged return by year: 2013 +25.7 points,
  2022 +12.6, 2007 +7.8; 2018 −10.5, 2009 −9.4, 2016 −8.3.

## What was learned

- **About the theory.** On seven funds of four classes from 2006 to 2022, ranking the classes by
  their past year and holding the two leaders earned about 1.8% a year more than holding all seven,
  at the top of what the card judged, in more years than not and in the holdout, but at 0.57
  standard errors, with a Sharpe ratio no better than the seven's: the leaders were mostly the more
  volatile funds, and ranked for their volatility they beat the seven by less than half as much.
  The gap lay in the years without a fall; after a fall it went the other way, the rule holding the
  refuges into the rebound. TM-001 is not refuted in the one form the lab's funds can test that no
  other verdict had read, and the lab's data gives it no support it can tell from chance.
- **About the rule.** Always invested in two funds, the rule was more volatile than the seven and
  paid little in costs, 0.24% a year for a change of holdings about one month in three. Its
  regression alpha, 2.71% a year, is larger than TM-017-01's 1.55% on the same seven, and a third of
  it came from a beta below one; the longer windows, of fifteen and eighteen months, kept almost
  none of it.
- **About the market.** Over 2023 to 2025 the leaders among these seven beat them by about 7% a
  year, holding gold in 27 of 36 months and SPY in 23.
- **About the lab.** Before this card, its writer computed on the in-sample closes the volatilities
  of the seven funds and of every pair's gap to the seven, for the test's power — second moments
  only, but in-sample data read before the lock, against the lab's practice, as the reasoning
  disclosed. The estimate, 7.7% at the median pair, fell short of the 13.0% the rule's gap moved by;
  SC-023-01 had already published 13.0% for a top-two rule across classes. A power estimate is built
  from published figures, and the runbook's step 3 now says nothing is computed on the in-sample
  returns before the lock.

TM-001 is `tested-inconclusive`: its one strategy failed gates 2 to 5, and the theory is not refuted
in the one form the lab can test that no other verdict read, momentum between asset classes.
