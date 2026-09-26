# TM-041-01 — Small capitalisations' weekly continuation against large ones: verdict

**Stops at gate 2, economic edge, and fails gates 3 to 5 as well. Not refuted, not proven: IWM's
weekly return continued its previous week's no more than SPY's did — IWM's slope less SPY's −0.009
(standard error 0.034, t −0.26), just short of the −0.35 that refutes — and both funds' weekly
autocorrelations were near zero and negative, −0.020 and −0.011.** The estimate lies 2.0 standard
errors below the middle of the predicted +0.02 to +0.10 and 0.85 below its low end: the funds do not
show the size contrast the sources found in their size quintiles to 1994, and the clause does not
refute it only because the card set its threshold near zero. The rule, each of the fourteen US
equity funds held for a block of five sessions after its own week beat the bill, earned a Sharpe
ratio of 0.14 against their 0.49 held always, an alpha of −2.44% a year after costs of 1.28%.
Thresholds, version 4; the battery's figures are the notebook's, [report.ipynb](report.ipynb), and
the clause, the reported measures and the neighbours' alphas are computed apart from it, on the same
closes and costs. The theory is [TM-041](../../bank/TM-041-size-momentum-interaction.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; the memory of 21 sessions holds on 100; 864
   decisions, once clustered, over 17.9 years in-sample, from the first holding on 2005-01-18.
2. **Economic edge: fails.** A Sharpe ratio of 0.140 against the benchmark's 0.494 and the 0.4
   required, an alpha of −2.44% a year; at twice the costs, 0.025 and −3.71%. Costs are 1.28% a
   year, 0.115 of a gross Sharpe ratio of 0.255, more than a third.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.741, and the rule beats 7.1% of
   1,000 placebos, its own weights shifted in time, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is −0.319, against 0.624 expected
   from the best of sixty-three effective trials by luck: a deflated Sharpe ratio of 0.000.
5. **Stability: fails.** The blend of the two variants fails gates 2, 3 and 4: a Sharpe ratio of
   0.218, an alpha of −1.74% a year. The alpha is positive in no block of five; without its best
   year, 2019, it is −2.88%.
6. **Robustness: passes.** The neighbours keep a median of 80% of the base's Sharpe ratio and at
   least 67% at ±25%; without the sector funds 96%; XLE carries 24% of the profit; the targets a
   session late keep 158%. The neighbours' alphas after costs, computed apart: `period` 4 −2.82% a
   year (appraisal ratio −0.36), 6 −1.01% (−0.13), 3 −4.02% (−0.51), 8 −2.36% (−0.30); the targets a
   session late −1.57% (−0.21); the variant, `period` 20, −1.05% (−0.13).
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.29 and an alpha of −3.34% a
   year, both above the tenth percentile of the in-sample paths (−0.55 and −7.46%).

## Verdict

The strategy stops at gate 2, and fails gates 3, 4 and 5 as well.

## The card's refutation

Over the 905 blocks of five sessions from January 2005 to December 2022, each from the close of its
first session to the close of the next block's first session, the last ending at the close of
2022-12-30, as the card counted: each fund's block return less the bill's, stacked for SPY and IWM,
regressed on the fund's own return less the bill's over the block before, with one constant and one
slope for each fund, the standard errors clustered by block:

- **IWM's weekly continuation against SPY's**: IWM's slope −0.0201 (0.0571), SPY's −0.0111
  (0.0656); the difference −0.0090, a standard error of 0.0343, t −0.26. *A t statistic of −0.35 or
  below*: not met. **Not refuted, not proven**; nor would a pass of gates 1 to 7 have proved it, the
  t statistic being far below +1.65.

**The test's power.** The card took the standard error at 0.026 to 0.032, possibly 0.04 with 2008
and 2020; it came out at 0.034. At that error the clause refutes about 36% of the time with no
effect and about 2% at +0.06, the middle of the prediction. The estimate lies 2.0 standard errors
below that middle and 0.85 below the prediction's low end, +0.02: the predicted middle is unlikely,
its low end is not excluded, and no effect is well inside.

Reported, not graded, as the card stated them:

- **The variant**, blocks of 20 sessions, over 225 blocks: IWM's slope less SPY's −0.050 (0.049,
  t −1.02); SPY's +0.019, IWM's −0.031.
- **The fourteen funds' weekly slopes**, each over its own blocks — the same as their first-order
  weekly autocorrelations to the third decimal: SPY −0.011, QQQ −0.004, IWM −0.020, XLB −0.014, XLC
  −0.002 (227 blocks), XLE +0.078, XLF −0.068, XLI +0.014, XLK −0.026, XLP −0.045, XLRE +0.007 (315
  blocks), XLU −0.045, XLV −0.036, XLY −0.016; standard errors 0.05 to 0.15. IWM's slope less QQQ's
  −0.016 (0.032, t −0.51); less the average of the thirteen others −0.007 (0.034, t −0.21).
- **With the other fund's last block as a regressor too**: IWM's slope less SPY's +0.036 (0.193, t
  +0.18); SPY's last block for IWM +0.057 (0.134, t +0.42), IWM's last block for SPY +0.071 (0.079,
  t +0.89) — no sign of large capitalisations leading small ones, LL-001's claim, and the two funds'
  weeks too alike for the regression to part them.
- **The block grid shifted forward** by one to four sessions: −0.0065 (0.026, t −0.25), +0.046
  (0.031, t +1.50), −0.0064 (0.027, t −0.24), +0.014 (0.023, t +0.59).
- **By period**: blocks starting in 2005–2013 −0.034 (0.045, t −0.75), in 2014–2022 +0.030 (0.053,
  t +0.56); without 2008 and 2009 −0.017 (0.034, t −0.51). **The holdout**, 2023 to 2025: +0.003
  (0.066, t +0.05), 149 blocks.
- **The alphas**: the base −2.44% a year after costs, −1.15% before, an appraisal ratio of −0.319;
  the neighbours', the variant's and the delayed rule's in gate 6 above.

## What was learned

- **About the theory.** On the lab's funds from 2005 to 2022, the Russell 2000's small
  capitalisations continued their weeks no more than the S&P 500's large ones: both weekly
  autocorrelations were slightly negative, their difference −0.009, 2.0 standard errors below the
  predicted middle. The sources' contrast of 0.28 to 0.36 between the smallest and largest
  quintiles, and 0.14 to 0.18 between the central and largest, was on equal-weighted portfolios of
  single stocks to 1994, part of it stale prices, and was already fading by 1990 (Foerster and
  Keim); on two funds priced continuously it is not there. The four-week variant and the shifted
  grids agree: no size contrast in either direction beyond noise. TM-041's first refutation, in its
  weekly form on funds, is not refuted by the card's clause and not proven; its cross-sectional
  form, momentum within small stocks, which Bali's table contests, and its analyst-coverage form are
  not held.
- **About the rule.** Holding each fund for the week after its own positive week, the plain trade on
  a continuation near zero and slightly negative, earned a Sharpe ratio of 0.14 and paid 1.28% a
  year in costs; the rule a session late did better, 158% of its Sharpe ratio, which a continuation
  near zero leaves to chance.
- **About the lab.** The card was first drawn on SPY and IWM alone; the lab refused a universe of
  fewer than four funds, and its audit found that a rule on fourteen funds, thirteen large, would
  have proved TM-041 by a pass that read weekly continuation, TM-043's claim: the card tied a proof
  to its clause's t statistic as well. This verdict publishes the fourteen funds' weekly
  autocorrelations and SPY's and IWM's cross-autocorrelations, which later cards of TM-043 and
  LL-001 must disclose.

TM-041 is `tested-inconclusive`: its one strategy failed gates 2 to 5, and its weekly form on the
funds is neither refuted by the card's threshold nor proven, the estimate well below the prediction.
