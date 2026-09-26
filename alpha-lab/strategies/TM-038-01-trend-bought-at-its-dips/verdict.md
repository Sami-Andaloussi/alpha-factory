# TM-038-01 — Trend following bought at its own dips: verdict

**Stops at gate 3, significance, and fails gates 4 to 6 as well. Not refuted, not proven: in the
months after its own losing five months, TM-017-01's trend rule earned 1.54% a year more over the
bill than after a winning five months, at the same exposure to the seven funds (standard error
2.64%, t +0.58), inside the predicted +0.5 to +3.5%, short of the −0.35 that refutes and far from
proof.** Holding the rule's book in full after its dips and at half otherwise earned an alpha of
1.23% a year after costs over the seven funds in equal parts, a Sharpe ratio of 0.54 against their
0.41 and above the book's own, as Greyserman and Kaminski's buying at the dips does; but it beats
87.4% of its placebos, its own weights shifted in time, where 90% are needed, and SPY carries 33% of
its profit, as the card expected. The book's hedged monthly returns carried a negative
autocorrelation over the first two lags, a sum of −0.12 over five. The variant, the book's own year,
gave the opposite sign. Thresholds, version 4; the battery's figures are the notebook's,
[report.ipynb](report.ipynb), and the clause, the reported measures and the neighbours' alphas are
computed apart from it, on the same closes and costs. The theory is
[TM-038](../../bank/TM-038-adaptive-markets-hypothesis.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; the memory of 530 sessions holds on 100; 136
   decisions, once clustered, over 16.9 years in-sample, from the first holding on 2006-02-01.
2. **Economic edge: passes.** A Sharpe ratio of 0.54 against the benchmark's 0.41, an alpha of 1.23%
   a year; at twice the costs, 0.52.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.992, but the rule beats 87.4% of
   1,000 placebos, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.366, against 0.619 expected
   from the best of sixty-one effective trials by luck: a deflated Sharpe ratio of 0.212.
5. **Stability: fails.** The blend of the two variants passes gates 2 and 3 and fails gate 4, a
   deflated Sharpe ratio of 0.269. The alpha is positive in four blocks of five, and 1.00% a year
   without its best year, 2013; the worse variant keeps a Sharpe ratio of 0.54.
6. **Robustness: fails.** SPY carries 33% of the profit, above the 30% limit, as TM-017-01's did.
   The neighbours keep a median of 105% of the base's Sharpe ratio and at least 85% at ±25%; without
   the bonds, the worst cluster to lose, 71%; a day's delay keeps 102%. The neighbours' alphas after
   costs, computed apart: `dip` 79 0.97% a year (appraisal ratio 0.26), 131 1.47% (0.43), 53 1.31%
   (0.36), 158 1.49% (0.46); the targets a session late 1.26% (0.38); the variant, `dip` 252, 1.31%
   (0.41).
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.72 and an alpha of −0.25% a
   year, both above the tenth percentile of the in-sample paths (−0.20 and −1.33%).

## Verdict

The strategy stops at gate 3, and fails gates 4, 5 and 6 as well.

## The card's refutation

Over the 198 months from July 2006 to December 2022, each from the close of a target's session to
the close of the next, the last ending at the close of 2022-12-30, as the card counted: the book's
return held in full, less the bill's, regressed on an indicator of the dip state at the target and
on the seven funds' return in equal parts less the bill's, with standard errors robust to
heteroskedasticity:

- **The trend rule after its own losing stretch against after a winning one**: +1.54% a year, a
  standard error of 2.64%, t +0.58, over 57 months after a dip and 141 after none; the book's beta
  to the seven funds 0.37. *A t statistic of −0.35 or below*: not met. **Not refuted, not proven**:
  the estimate lies inside the predicted range, 0.58 standard errors from zero.

**TM-018-01's states.** Of its 31 equity-crisis months among the 198, 15 fell in the dip set and 16
out (48%); of its 91 divergent months, 25 in and 66 out (27%). Neither reached 90% in one set: both
stayed in the graded sample, as the card fixed.

**The test's power.** The card took the standard error at 2.5 to 2.7%, from TM-017-01's published
tracking error; it came out at 2.64%, with 29% of the months in a dip, fewer than the third to half
the card assumed. At that error the clause refutes about 36% of the time with no effect and about
14% at +2% a year; the estimate, +1.54%, lies 0.17 standard errors below the predicted middle and
0.58 above zero: neither is excluded.

Reported, not graded, as the card stated them:

- **The variant**, `dip` 252, over its 190 months from March 2007: −2.40% a year (3.38%, t −0.71),
  43 months after a dip — the opposite sign, as far from zero as the base on its side.
- **Without the seven funds as a regressor**: +0.72% a year (3.25%, t +0.22). **With a beta for each
  state**: +2.71% (2.54%, t +1.07); the book's beta 0.51 after no dip and 0.24 after a dip.
- **Without TM-018-01's crisis months**: +3.26% a year (2.67%, t +1.22), over 167 months; **without
  its divergent months**: +0.42% (3.27%, t +0.13), over 107.
- **The months in a dip**: 29%; the base's average scale 0.64. **The book's hedged monthly
  autocorrelations**, lags 1 to 5: −0.073, −0.069, −0.015, +0.034, 0.000; their sum −0.123, at the
  edge of the card's −0.1 to −0.25.
- **By period**: 2006–2013 +3.86% a year (4.77%, t +0.81), 90 months; 2014–2022 −0.10% (2.92%, t
  −0.04), 108 months. **The holdout**, 2023 to 2025: −3.49% (4.25%, t −0.82), 36 months, 14 after a
  dip.
- **Against holding the book constantly**, before costs: the base 0.559 Sharpe ratio, an alpha of
  1.30% a year, an excess return of 2.44%; the book held in full, TM-017-01's rule, 0.506, 1.63% and
  3.56%; the book held constantly at the base's average scale, 0.644, 0.504, 1.04% and
  2.28%. Buying at the dips raised the Sharpe ratio and, at the same average exposure, the alpha by
  0.26% a year; it gave up return against the book held in full, as Greyserman and Kaminski's table
  gives at such a Sharpe ratio and autocorrelation.
- **`python -m lab.compare` against TM-017-01**: the alpha difference −0.33% a year (standard error
  0.53%, t −0.63), the bets correlated at 0.91; the appraisal ratio 0.366 against 0.300, a
  difference of +0.067 (0.105).
- **The alphas**: the base 1.23% a year after costs, 1.30% before; the neighbours', the variant's
  and the delayed rule's in gate 6 above.

## What was learned

- **About the theory.** On the lab's seven funds from 2006 to 2022, TM-017-01's trend rule earned
  more after its own losing five months than after its winning ones, at the same exposure, by 1.54%
  a year — the sign TM-038's cycle and Greyserman and Kaminski's negative autocorrelation predict,
  0.58 standard errors from zero. Its hedged monthly returns reverted at one and two months, a sum
  of −0.12 over five lags, near their typical programme's −0.1. But the estimate came from 2006–2013
  and was nil after, negative in the holdout, and the book's own year gave the opposite sign.
  TM-038's second refutation, in its own-performance form, is neither refuted nor proven; its
  capital form, the assets that follow a strategy, is not held. A positive contrast would not have
  told the capital cycle from the mechanical reversion of a lookback straddle.
- **About the rule.** Holding the book at half and in full after its dips, 64% of it on average,
  gave the higher Sharpe ratio Greyserman and Kaminski describe, 0.56 against 0.51 before costs, and
  less return than the book in full; its placebos did as well 13% of the time, and SPY carried a
  third of its profit, as it did of TM-017-01's.
- **About the lab.** The theory was first drafted not testable, its reader finding the signed form
  and a sibling's hand-off to it; the audit of the card found that the registry holds every trial's
  monthly hedged returns, TM-017-01's among them, and the RUNBOOK now counts the registry among
  published results. Nothing was computed from it before the lock.

TM-038 is `tested-inconclusive`: its one strategy failed gates 3 to 6, and its own-performance form
is not proven and not refuted. A second trial, the book's allocation proportional to its drawdown,
would need a scale the library does not give.
