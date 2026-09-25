# SC-017-01 — Out of equities in September and October: verdict

**Stops at gate 3, significance. Not refuted, not proven: September and October earned a little less
than the other months, within noise, and all of that came from 2008; without it they earned a little
more.** Holding the five equity funds in equal parts in every month but September and October, and
cash in those two, earns an alpha of 1.45% a year over the five held always, 1.55% before its costs
of 0.10% a year, and an appraisal ratio of 0.16: at the bottom of the predicted 1.1 to 2.5% after
costs and 0.15 to 0.35 only through a regression beta of 0.76, lowered by missing the fall of 2008;
at a beta equal to its time in the market, 0.83, the alpha is 0.84% a year, below the range. The gap
measured, about 0.5% a month, is about a third of the long record's 1.54%, below the card's half to
all. Before costs, the sessions of the ten months held averaged 0.025% a day more than those of
September and October, with a standard error of 0.063%, and, at the lab's costs, the rule beats
78.8% of its placebos: the clause's two conditions for a refutation are not met. Without 2008,
stated before the run, the difference is −0.009% a day and the alpha −0.69% a year. Thresholds,
version 2; the battery's figures are the notebook's, [report.ipynb](report.ipynb), and the clause's
differences, the variant's alpha, the alphas before costs and at the share of sessions held, the
betas, the months moved, the calendar months' averages and their ranking, the funds, the years, the
blocks and the figures without 2008 are computed apart from it, on the same sessions and costs. The
theory is [SC-017](../../bank/SC-017-month-of-the-year-effect.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 174 dates; 37 decisions, once clustered, over 18.0 years
   in-sample, from the first holding on 2005-01-03. The rule reads a calendar derived from the
   exchange's holiday rules, not the market's dates.
2. **Economic edge: passes.** A Sharpe ratio of 0.42, above the 0.4 required and the benchmark's
   0.40, and an alpha of 1.45% a year; at twice the costs, 0.42 and 1.35%. Costs are 0.10% a year,
   0.005 of a Sharpe unit.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.98; the rule beats 78.8% of 1,000
   placebos, its own weights shifted in time by a year or more, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.16, against 0.46 expected
   from the best of twenty-three effective trials by luck: a deflated Sharpe ratio of 0.12.
5. **Stability: fails.** The blend of the two variants passes gate 2 but fails gates 3 (85.2% of its
   placebos beaten) and 4 (a deflated Sharpe ratio of 0.13). The base's alpha is positive in three
   of the five blocks — 2008–09 (12.6% a year), 2015–19 (0.8%) and 2020–22 (3.5%) — and negative in
   2005–07 (−3.4%) and 2010–14 (−3.0%); without its best year, 2008, it is −0.69% a year.
6. **Robustness: fails.** QQQ carries 33% of the profit, above the 30% any one fund may. The
   neighbours keep a median of 94% of the base's Sharpe ratio and at least 87% at ±25%; a day's
   delay keeps 100%. The five funds form one cluster, so none is left out.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 1.12 and an alpha of 2.82% a
   year, both above the tenth percentile of the in-sample paths (−0.24 and −4.75%).

## Verdict

The strategy stops at gate 3, and fails gates 4 to 6 as well.

## The card's refutation, clause by clause

Computed apart from the battery, from the in-sample sessions after 2005-01-03, the first having no
previous close: the five funds' average daily return less the bill's rate averaged 0.0389% a day
over the 3,767 sessions of the ten months held and 0.0135% over the 763 sessions of September and
October. The difference is +0.0254% a day, with a standard error of 0.0634% from the daily returns
(t 0.40). The base beats 78.8% of its placebos.

- *The difference zero or less, and half of the placebos beaten or fewer*: neither is met. The
  theory is **not refuted**; short of gates 1 to 7, it is **not proven**.

Reported, not graded, as the card stated them:

- **The variant**, September alone: the other eleven months averaged 0.0394% a day over 4,162
  sessions and September −0.0196% over 368, a difference of +0.0590% a day (a standard error of
  0.0754%, t 0.78), 0.4 standard errors below the 0.09% of the long record's gap. Its alpha is 1.02%
  a year after costs, 1.12% before, an appraisal ratio of 0.17.
- **Without 2008**, stated before the run: the base's difference is −0.0092% a day (0.0471%, t
  −0.20), September and October averaging 0.054% a day against 0.045% for the other months; its
  alpha −0.69% a year, an appraisal ratio of −0.10. The variant's difference is +0.0384% (0.0624%, t
  0.62).
- **The months moved**, stated before the run: out in August and September, an alpha of 1.89% a
  year, 2.00% before costs, where Ilmanen's figure would give about 1.3% before costs, half the
  base's; out in October and November, −0.27%, where it would give about 0.2%.
- **The base's alpha before costs**: 1.55% a year.

**The test's power.** The difference's standard error came in at 0.063% a day, above the 0.048% the
reasoning estimated: the funds' daily volatility was 1.38%, not the 1.2% assumed, which alone gives
0.055%, and the sessions of September and October were more volatile than the others (1.65% against
1.32%) through 2008 alone; without it they were calmer (1.13% against 1.24%). The base's +0.025%
lies 0.4 standard errors above zero and 0.8 below the 0.073% of the long record's whole gap: the run
cannot tell the long record's gap from none, as the reasoning said it could not tell half of it. The
simulation behind the card put a refutation at about 45% had the effect vanished; it did not come.
The disclosure before the run — that 2008 alone would move the difference by about 0.04% a day
towards the claim — is what the figures without 2008 show: +0.025% with it, −0.009% without, a move
of 0.035% a day, about half of the standard error measured.

## The measures stated before the run

- **The calendar months**, the five funds' average excess return, in-sample, in percent a day with
  its standard error, and in percent a month at 21 sessions:

  | Month | % a day | % a month | Month | % a day | % a month |
  |---|---|---|---|---|---|
  | January | −0.016 (0.064) | −0.34 | July | 0.115 (0.052) | 2.41 |
  | February | 0.009 (0.064) | 0.20 | August | −0.011 (0.063) | −0.23 |
  | March | 0.063 (0.092) | 1.31 | September | −0.020 (0.072) | −0.41 |
  | April | 0.108 (0.061) | 2.26 | October | 0.044 (0.094) | 0.93 |
  | May | 0.002 (0.062) | 0.05 | November | 0.078 (0.084) | 1.64 |
  | June | −0.012 (0.064) | −0.26 | December | 0.054 (0.062) | 1.13 |

  September was the weakest month, but by little: January, June and August were within 0.01% a day
  of it, and every month's average is within about two standard errors of the others'. October was
  above the year's average. The rank correlation of the twelve with the order of Ilmanen's figure,
  March and May tied there and given average ranks, is 0.29 (a p-value of 0.35 against none): it
  cannot be told from none, the twelve averages being themselves within noise of one another (a test
  of equal means, found after the result, gives a p-value of 0.92), and January, among the long
  record's strongest months, was among the weakest here — the reversal Ilmanen notes over the last
  twenty years of his sample.

- **By fund**, the base's difference before costs: SPY +0.025% a day, QQQ +0.028%, IWM +0.036%, EFA
  +0.022%, EEM +0.016%, each with a standard error of 0.06 to 0.09%: the same small sign in every
  fund, none distinguishable from zero.
- **By year**, the base's difference, the months held less September and October, in percent a day:
  positive in ten of eighteen years, largest in 2008 (+0.588), 2020 (+0.231) and 2018 (+0.223), most
  negative in 2010 (−0.343), 2007 (−0.249) and 2013 (−0.164). The five funds' excess return summed
  over the two months was negative in seven years, most in 2008 (−28.5%), 2018 (−9.4%) and 2022
  (−5.3%).

## What was learned

- **About the theory.** On the lab's five equity funds from 2005 to 2022, September and October were
  not weak months, bar one year: with 2008 they earned a little less than the others, within noise;
  without it, a little more. September alone was a little weaker than the rest, within noise, and
  October earned more than the average month. Whether the long record's ranking of the twelve months
  recurred cannot be told (a rank correlation of 0.29), the months being within noise of one
  another; January did not. This is close to what Ziemba found on US futures from 1993 to 2011 —
  October positive, September slightly negative, no reliable monthly effect, the two months like the
  others but for their big declines. The test's power, a standard error of 0.063% a day against a
  long-record gap of 0.073%, could not tell the gap from none.
- **About the alpha, found after the result.** The regression gives the rule a beta of 0.76, below
  the 0.83 share of the sessions it holds: missing the fall of 2008 lowers the beta, and the hedge
  then charges less of the funds' premium of 8.7% a year. At a beta equal to its time in the market,
  the alpha is 0.84% a year rather than 1.45%. Without 2008 the beta is 0.86.
- **About the months moved.** Out in August and September the alpha would have been 1.89% a year,
  2.00% before costs, above the base's, where the long record gives about half of it: August, strong
  in the long record, was weak here (−0.23% a month); that is the sample's shape, not a finding, and
  it goes against the claim's months. Out in October and November, −0.27%, about the nil the long
  record gives. Found after the result, at a beta equal to the share of sessions held the three
  alphas are 0.84%, 2.02% and −1.14% a year. Read beside gate 6, not graded, since the month is a
  name.
- **About the market.** The rule's best years against the benchmark were 2008 (+19.1 points of
  hedged return), 2020 (+10.1) and 2018 (+7.1); its worst 2010 (−10.8), 2007 (−8.2) and 2015 (−4.6).
  Over the holdout, 2023 to 2025, it earned 2.82% a year of alpha, within the in-sample range.
- **About the lab.** The card named the month rather than counting it, since gate 6's rule of ±25%
  on a month's number would have moved September to July and November, a test of the claim's
  contrast rather than of the rule; the months moved were stated before the run and reported beside
  gate 6 instead. What was known before the card — 2008's September and October in the sources and
  in SC-008-01's verdict — was disclosed and turned into a measure stated before the run, and the
  result rests on it.

SC-017 is `tested-inconclusive`: on the lab's five equity funds from 2005 to 2022, September and
October earned less than the other months only through 2008, within noise, and whether the long
record's ranking of the calendar months recurred could not be told; the claim was not refuted in the
card's form, whose clause would refute it only if the two months earned no less than the others. The
broader claims — differences across all twelve months, reported here and not graded, and their ties
to taxes, flows and balance sheets — are not tested.
