# LL-023-01 — Continuous momentum within groups: verdict

**Stops at gate 2, economic edge. Refuted in this form: among each group's leading funds, the more
continuous half earned 2.04% a year less alpha than the more discrete half, where the card predicted
about 1% more; the predicted gain is rejected, a loss suggested but not shown.** Holding, each
month, the half of each group's pool — its funds ranked in the top two thirds or so by the past
year's return, the last month left out — whose daily returns were most often positive earns an alpha
of −0.65% a year over the nineteen funds held in equal parts; holding the other half of the same
pool earns 1.39%. The difference, −2.04% a year with a standard error of 1.44%, is below −1% and
more than one standard error below zero, as the card's clause requires. It is negative in each of
the three groups, none by more than about one standard error, and in thirteen of seventeen years; by
a split found after the result, most of it lies in the months in which the pool held funds that had
lost over the window, where the card's score departs from the source's measure — months that are
also, mostly, those after falling markets. Thresholds, version 2; the battery's figures are the
notebook's, [report.ipynb](report.ipynb), and the comparisons, the blocks, the years, the groups and
the fixed mixes are computed apart from it, on the same sessions and costs. The theory is
[LL-023](../../bank/LL-023-frog-in-the-pan.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; 164 decisions, once clustered, over 16.9 years
   in-sample, from the first holding on 2006-02-01.
2. **Economic edge: fails.** A Sharpe ratio of 0.40 against the benchmark's 0.46, and an alpha of
   −0.65% a year; at twice the costs, 0.39 and −0.89%. Costs are 0.25% a year, 0.014 of a Sharpe
   unit.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.97; the rule beats 7.3% of 1,000
   placebos, its own weights shifted in time by a year or more, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is −0.13, against 0.44 expected
   from the best of seventeen effective trials by luck: a deflated Sharpe ratio of 0.008.
5. **Stability: fails.** The blend of the two halves — the whole pool — passes gate 2 but fails
   gates 3 and 4 (67.2% of its placebos beaten, a deflated Sharpe ratio of 0.10), as the reasoning
   foresaw. The base's alpha is positive in three of the five blocks, 2010–14 (0.2% a year),
   2015–19 (0.4%) and 2020–22 (1.5%), and negative in 2005–07 (−2.8%) and 2008–09 (−6.6%); without
   its best year, 2015, it is −1.01% a year.
6. **Robustness: passes.** The neighbours keep a median of 108% of the base's Sharpe ratio and
   about 100% at ±25%; without the sectors, the worst cluster to lose, 86% remains; the largest
   share of the profit is XLK's, 17%; a day's delay keeps 101%.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.94 and an alpha of −0.77% a
   year, both above the tenth percentile of the in-sample paths (−0.30 and −3.95%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 5 as well.

## The card's refutation, clause by clause

`python -m lab.compare` with the card named twice, `--variant 0 --reference-variant 1`, over the
base's sessions from 2006-02-01 to 2022-12-30 at the stated costs: the continuous half's alpha is
−0.653% a year, the discrete half's 1.390%, their betas 0.965 and 0.951. The difference is −2.043% a
year with a standard error of 1.435% (a t-statistic of −1.42): below −1% and more than one standard
error below zero. The claim that the more continuous of a group's leading funds continue more than
the more discrete is **refuted in this form**. It says nothing about the source's stocks, sorted
within a quintile of past return.

Reported, not graded: the continuous half's alpha less CA-001-01's, over the same sessions, is
−0.85% a year with a standard error of 0.94%. CA-001-01's alpha, recomputed by the same code on the
same snapshot, is 0.198% a year, as its verdict recorded (0.20%); the change of the battery's
version, which touched gate 6 only, cannot move it. The source's tables put this trade for a pool of
the top two thirds at −1.4% to +0.4% a year on stocks; the lab's figure lies inside.

**The test's power.** The standard error came in at 1.44%, below the 1.5 to 2.2% the reasoning
estimated. At that noise, the clause would refute a true difference of zero about 16% of the time,
a true +0.5%, the prediction's low end, about 9%, and the predicted +1% about 4.5%. The data reject
the predicted gain more firmly than they show a loss: −2.04% lies 2.1 standard errors below the
predicted +1% (a one-sided probability of 1.7%) and 1.4 below zero (7.7%). The refutation says the
path did not add what the card predicted on these funds; that it subtracted is suggested, not
shown.

## What was learned

- **About the theory.** On the lab's nineteen funds, the path did not add what the source's story
  predicts. The difference is negative in each group, hedged of the benchmark and before costs:
  −1.16% a year in the sectors (a standard error of 1.21%), −0.53% in the equity markets (0.57%) and
  −0.44% in the commodities (0.90%), none by more than about one standard error. It is negative in
  most years: the continuous half lost to the discrete in thirteen of seventeen, most in 2008 (−11.4
  points of hedged return), 2012 (−9.8), 2010 (−8.3), 2021 (−6.9) and 2007 (−6.4); it won in 2011
  (+9.3), 2018 (+8.6), 2015 (+3.3) and 2017 (+2.7). - **Where the difference lies, found after the
  result.** 19.3% of the pool's fund-months (483 of 2,507) had a negative window return, in 118 of
  the 203 months — the months in which the card's score, for those funds, departs from the source's
  measure and prefers the discrete loser. In those months the difference was about −3.4% a year (a
  standard error of 1.9%); in the other 85, where the score is exactly minus the source's measure
  for every pool fund, about −0.2% (2.1%). The rule for losers acts in those months: scoring losers
  by the source's measure instead would change the continuous half's choice in 91 of the 118, and
  the continuous half held 189 losing fund-months against the discrete half's 294. But those months
  are mostly the months after falling markets, and the split cannot tell the rule for losers from
  that state of the market. In the months where the source's measure applies alone, the difference
  is near zero, measured to about ±2%. This split was chosen after the result; it informs the
  reading and grades nothing. - **What the halves held.** The continuous half held 64.4% of
  CA-001-01's leaders (812 of 1,260 fund-months), the discrete half 36.6%; the pool funds the
  continuous half held had a higher past return over the window, 16.8% on average against 11.1%
  (CA-001-01's leaders, 20.2%). Within the groups, the score leaned as the reasoning expected in two
  of three: in the sectors towards utilities, staples and health care and away from financials,
  energy and materials, the pool funds it held less volatile (18.9% a year against 20.2%); among the
  equity markets towards SPY and away from IWM and EEM (20.6% against 21.6%); in the commodities the
  other way, towards silver and away from gold (22.3% against 20.0%).
- **The mix and the choice.** The continuous half's average mix, held fixed and reset each month,
  earns an alpha of 1.16% a year — it held more QQQ, SPY and XLK — and the discrete half's −0.01%.
  What each half chose month by month added −1.8% a year to the first and +1.4% to the second. The
  fixed mixes are computed from the whole sample's weights, after the result; they describe the
  halves and grade nothing. - **About the discrete half.** Its alpha of 1.39% a year, an appraisal
  ratio of 0.33, is the highest of the six trials the lab has run on these nineteen funds. It was
  the counterfactual, not a hypothesis, and it is a trial of gate 4, where its series would need an
  appraisal ratio of about 0.67 (a deflated Sharpe ratio of 0.39 as it stands); read after the
  result, it is not a finding. A card that holds the discrete half as its thesis would need a
  mechanism of its own and a new lock.
- **About the market.** The continuous half's worst months against the discrete were July 2008
  (−5.5 points), November 2022 (−5.4), November 2016 (−3.8), October 2014 (−3.5), July 2020 (−3.5)
  and March 2009 (−3.4); its best, March 2020 (+5.7), August 2018 (+3.6), June 2022 (+3.5), July
  and August 2011 (+3.5 and +3.4) and May 2018 (+3.1).
- **About the lab.** The card's first draft compared the continuous half with CA-001-01's leaders,
  a comparison of the path with the past return the pool gives up; the logic audit found the source
  predicts about zero or a loss for it, and moved the judgement to the two halves of the same pool,
  Gray and Vogel's split. The comparison ran through `lab.compare` with one card named twice, the
  first card to use the tool. Drafts of the strategy, its build plan and its checks were written in
  the scratchpad before the card's audit; none was run, and the code was written again from the
  committed card, a departure from the order the runbook sets, recorded here.

LL-023 is `tested-inconclusive`: its tradable form on the lab's funds — the smoother half of each
group's leaders — is refuted in this form, the predicted gain rejected and the discrete half having
done better, mostly in months when the pool held losing funds; the source's claim on individual
stocks, within a quintile of past return, and the role of attention are not tested.
