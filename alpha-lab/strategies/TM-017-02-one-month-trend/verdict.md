# TM-017-02 — Time-series momentum at one month: verdict

**Stops at gate 2, economic edge, and fails gates 3 to 6 as well. Not refuted, not proven: across
EFA, EEM, IEF, TLT, GLD and DBC, a fund's month, scaled by its recent volatility, rose with its
previous month by a pooled slope of +0.045 (standard error 0.048, t +0.94), inside the predicted
+0.02 to +0.12, 0.94 standard errors from zero.** The positive part came from the Treasuries and the
commodity basket (IEF +0.106, TLT +0.090, DBC +0.110); the two equity markets were flat (EFA −0.007,
EEM −0.010) and gold slightly negative (−0.041), as the sources on gold had it. The rule,
TM-017-01's with its lookback at a month, earned an alpha of 0.48% a year after costs over the seven
funds in equal parts, a Sharpe ratio of 0.36 against their 0.45, and its neighbour at 16 sessions
kept a quarter of its Sharpe ratio. Thresholds, version 4; the battery's figures are the notebook's,
[report.ipynb](report.ipynb), and the clause, the reported measures and the neighbours' alphas are
computed apart from it, on the same closes and costs. The theory is
[TM-017](../../bank/TM-017-time-series-momentum.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 100 dates; the memory of 22 sessions holds on 50; 205
   decisions, once clustered, over 17.8 years in-sample, from the first holding on 2005-03-01.
2. **Economic edge: fails.** A Sharpe ratio of 0.355 against the benchmark's 0.454 and the 0.4
   required, an alpha of 0.48% a year; at twice the costs, 0.311 and 0.19%. Costs are 0.30% a year.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.957, but the rule beats 60.9% of
   1,000 placebos, its own weights shifted in time, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.093, against 0.621 expected
   from the best of sixty-four effective trials by luck: a deflated Sharpe ratio of 0.015.
5. **Stability: fails.** The base alone, the blend, fails gates 2, 3 and 4. The alpha is positive in
   two blocks of five; without its best year, 2020, it is −0.19% a year.
6. **Robustness: fails.** A neighbour at ±25% keeps 25% of the base's Sharpe ratio, below the 50%
   required; the median neighbour keeps 93%; without the broad equity funds 80%; EEM carries 23% of
   the profit; a day's delay keeps 79%. The neighbours' alphas after costs, computed apart:
   `lookback` 16 −1.59% a year (appraisal ratio −0.30), 26 +1.07% (0.20), 11 −0.89% (−0.17), 32
   +1.03% (0.20); the targets a session late −0.02% (−0.00).
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.45 and an alpha of −1.65% a
   year, both above the tenth percentile of the in-sample paths (−0.37 and −3.48%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 6 as well.

## The card's refutation

Over the 212 months from May 2005 to December 2022, each from the close of a target's session to the
close of the next, the last ending at the close of 2022-12-30, as the card counted, for EFA, EEM,
IEF, TLT, GLD and DBC (DBC from April 2006), 1,259 fund-months: each fund-month's return less the
bill's, scaled by the fund's daily volatility over the 63 sessions to the session before the target,
regressed on the fund's previous month scaled alike, with one constant for each fund and one slope
for all, the standard errors clustered by month:

- **A fund's month on its own previous month**: +0.0453, a standard error of 0.0481, t +0.94. *A t
  statistic of −0.35 or below*: not met. **Not refuted, not proven**: the estimate lies inside the
  predicted range, 0.94 standard errors from zero.

**The test's power.** The card took the standard error at 0.04 to 0.05 from a count; it came out at
0.048. At that error the clause refutes about 36% of the time with no effect and about 3% at +0.07,
the prediction's middle; the estimate lies 0.52 standard errors below that middle and 0.94 above
zero: neither is excluded. Dividing both months by a volatility that holds the previous month leaves
a small bias in the slope, about +0.005 by the audit's estimate, a tenth of the standard error.

Reported, not graded, as the card stated them:

- **Unscaled**, each fund weighed by its variance: +0.032 (0.069, t +0.46).
- **With SPY's fund-months**: +0.025 (0.048, t +0.51), 1,471 fund-months.
- **Each fund's own slope**, scaled: DBC +0.110 (0.075, t +1.47), IEF +0.106 (0.074, t +1.43), TLT
  +0.090 (0.076, t +1.17), EFA −0.007 (0.093), EEM −0.010 (0.074), GLD −0.041 (0.074, t −0.55).
- **The equity funds**, EFA and EEM: −0.008 (0.075, t −0.11); **the others**: +0.066 (0.050,
  t +1.33).
- **With the fund's past year as a control**, from February 2006, 203 months: the one-month slope
  +0.041 (0.049, t +0.84), the year's +0.003 (t +0.20) — the one month is not TM-017-01's year.
- **Without TM-024-01's 17 equity panic months**: +0.051 (0.052, t +0.99).
- **By period**: 2005–2013 +0.046 (0.068, t +0.67), 104 months; 2014–2022 +0.041 (0.066, t +0.62),
  108 months; without 2008 and 2009 +0.043 (0.052, t +0.83). **The holdout**, 2023 to 2025: −0.134
  (0.094, t −1.43), 36 months.
- **The alphas**: the base 0.48% a year after costs, 0.78% before, an appraisal ratio of 0.093; the
  neighbours' and the delayed rule's in gate 6 above.

## What was learned

- **About the theory.** On the lab's funds outside the US equity market, from 2005 to 2022, a
  month's return was continued into the next by a pooled slope of +0.045, the sign TM-017 and
  Ilmanen's adjacent-month correlations give, of about the predicted size and not distinguishable
  from zero. The continuation lived in the Treasuries and the commodity basket, as Ilmanen's bars
  and Lo's bond index had it, and not in the developed and emerging equity markets, where the
  sources' positive sign was expected to be strongest; gold reverted a little, as Lo and Chevallier
  and Ielpo found. It held in both halves of the sample and turned negative in the holdout. TM-017's
  one-month form is not refuted and not proven; its six- and twelve-month forms were read by
  TM-017-01.
- **About the rule.** Long only, a fund held a month after a rising month and cash after a falling
  one, it earned a lower Sharpe ratio than the seven funds held always, and its neighbours at 11 and
  16 sessions lost what those at 26 and 32 gained: the monthly sign is too weak on these funds to
  carry a rule that steps in and out each month.
- **About the lab.** The card was drawn because TM-043's reader required that the one-month form
  handed to TM-017 be drawn, not left between two theories. Its audit found that a draft of the
  power estimate rested on standard errors of TM-041-01's twenty-session slopes that no verdict
  published, taken from that card's own computation apart from its battery; the estimate was rebuilt
  from a count before the lock. The strategy file, TM-017-01's with its docstring changed, was
  drafted in the session's scratchpad while the card's audit ran, before the lock, and was not run;
  RUNBOOK step 4 writes the code after the lock, and this departure is recorded here.

TM-017 stays `in-progress`: TM-017-01 trades on paper as the test of the lab's chain; this card adds
a one-month form not refuted and not proven.
