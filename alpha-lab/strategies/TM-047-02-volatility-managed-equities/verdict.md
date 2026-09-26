# TM-047-02 — Equities managed by their own volatility: verdict

**Stops at gate 3, significance. Not proven, not refuted: the five equity index funds scaled each
month by the inverse of their realized variance, capped at full investment, earned an alpha of 1.56%
a year before costs over the same five held always (standard error 1.74%, t +0.90), an appraisal
ratio of 0.22, inside the predicted +0.3 to +2% and 0.05 to 0.35, and short of the −0.35 that
refutes.** After costs the rule's alpha is 1.25% a year and its Sharpe ratio 0.42 against the five's
0.40; but it beats 78.1% of its placebos, its own weights shifted in time, where 90% are needed, and
QQQ carries 37% of its profit, as the card expected. The gain came from 2008 and 2009. Thresholds,
version 4; the battery's figures are the notebook's, [report.ipynb](report.ipynb), and the clause,
the reported measures and the neighbours' alphas are computed apart from it, on the same closes and
costs. The theory is [TM-047](../../bank/TM-047-volatility-targeted-momentum.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; the memory of 22 sessions holds on 100; 132
   decisions, once clustered — the months in which the scale moved — over 18.0 years in-sample.
2. **Economic edge: passes.** A Sharpe ratio of 0.415 against the benchmark's 0.395, an alpha of
   1.25% a year; at twice the costs, 0.409 and 1.17%. Costs are 0.09% a year.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.979, but the rule beats 78.1% of
   1,000 placebos, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.160, against 0.62 expected
   from the best of fifty-eight effective trials by luck: a deflated Sharpe ratio of 0.041.
5. **Stability: fails.** The blend of the two variants fails gates 3 and 4. The block alphas:
   2005–07 −0.25% a year, 2008–09 −2.02%, 2010–14 +0.84%, 2015–19 −1.45%, 2020–22 −1.93%; one
   positive block of five, each block's own beta taking the scale's cut into the market. Without its
   best year, 2017, the alpha is 0.70% a year.
6. **Robustness: fails.** QQQ carries 37% of the profit, above the 30% limit, as SC-002-01 found for
   the five in equal parts set back monthly. The neighbours keep a median of 94% of the base's
   Sharpe ratio and at least 91% at ±25%; the test without a cluster does not run, the five being
   one; a day's delay keeps 98%. The neighbours' alphas, computed apart: `window` 16 1.41% a year
   (appraisal ratio 0.18), 26 0.79% (0.10), 10 1.01% (0.13), 32 0.59% (0.08); `target` 0.12 0.90%
   (0.13), 0.20 1.39% (0.17), 0.08 0.56% (0.11), 0.24 1.67% (0.20); the targets a session late 1.14%
   (0.15); the variant 1.18% (0.18).
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.91 and an alpha of −0.88% a
   year, both above the tenth percentile of the in-sample paths (−0.28 and −4.03%).

## Verdict

The strategy stops at gate 3, and fails gates 4, 5 and 6 as well.

## The card's refutation

Over the 214 months from March 2005 to December 2022, each from the close of a target's session to
the close of the next, the last ending at the close of 2022-12-30, as the card counted: the rule's
monthly return less the bill's, before costs, regressed on the five funds' in equal parts:

- **The equity premium managed by its own volatility against held always**: an alpha of +1.56% a
  year, a standard error of 1.74% (robust to heteroskedasticity), t +0.90; a beta of 0.479; an
  appraisal ratio of 0.224. *A t statistic of −0.35 or below*: not met. **Not refuted, not proven**:
  the alpha lies inside the predicted range, 0.90 standard errors from zero.

**The test's power.** The card judged the appraisal ratio's standard error at about 0.24; with 214
months it is. At that error the clause refutes about 36% of the time with no effect and about 11% at
an appraisal ratio of 0.2; the estimate, 0.22, lies close to the predicted middle and 0.90 standard
errors above zero: neither the prediction nor no effect is excluded.

**Where the alpha came from.** The scale was below one in 48% of the months and averaged 0.78; by
year it fell to 0.45 in 2008, 0.38 in 2009, 0.49 in 2022 and 0.61 in 2020, and stayed at 0.94 or
more in 2005, 2013, 2014, 2017 and 2021. The regression's beta, 0.48, lies well below the average
scale: the rule held least of the funds in the months whose returns moved most. That is the theory's
reading — the premium does not rise with volatility, so cutting exposure when volatility is high
sheds more risk than return — and the alpha at a beta equal to the average scale, which isolates the
months' own timing and which the theory does not claim, is −0.91% a year (2.15%). The clause's alpha
rests on 2008 and 2009: 2005–2013 +3.03% a year (2.74%, t +1.11), 2014–2022 −0.24% (1.72%, t −0.14);
without 2008 and 2009 +0.39% (1.33%, t +0.29).

Reported, not graded, as the card stated them:

- **The variant**, scaled by volatility: +1.40% a year (1.44%, t +0.97), a beta of 0.628, an
  appraisal ratio of 0.247; the scale below one in 48% of months, averaging 0.86; the alpha at a
  beta equal to it −0.50% (1.71%).
- **The Sharpe ratios before costs**: the base 0.471, the variant 0.485, the five held always 0.420.
- **Without TM-024-01's 17 equity panic months**: +0.53% a year (1.21%, t +0.44), a beta of 0.675.
  The two versions agree in sign; without the panic months the alpha is a third as large, as the
  months in which the rule acts most, 2008–09 among them, are gone.
- **By period**: above; **the holdout**, 2023 to 2025: −1.35% a year (1.04%, t −1.29), a beta of
  0.912, over 36 months.
- **SPY alone, managed by its own risk**: +2.67% a year (1.64%, t +1.63), a beta of 0.530, an
  appraisal ratio of 0.416 — the sources' market, closer to their figures than the five.
- **The alphas**: the base 1.25% a year after costs, 1.35% before; the neighbours', the variant's
  and the delayed rule's in gate 6 above.

## What was learned

- **About the theory.** On the lab's five equity index funds from 2005 to 2022, scaling the equity
  premium by the inverse of its own recent variance, capped at full investment, raised its Sharpe
  ratio before costs from 0.42 to 0.47 and earned an alpha of 1.56% a year, an appraisal ratio of
  0.22 — near Moreira and Muir's 0.30 for the capped market, as TM-047-01 reported them, and within
  the card's range — but at 0.90 standard errors, and from 2008 and 2009 above all: without them,
  0.39% a year. On SPY alone the appraisal ratio was 0.42. The risk-premium form of TM-047's third
  refutation is not refuted and not proven; in the holdout the sign turned (t −1.29). Where
  TM-047-01 found the timing worth nothing inside a trend rule, which already stepped out of falling
  markets, the timing here, on equities held always, earned about what the sources say, and earned
  it in 2008–09.
- **About the rule.** It held the five funds in full in about half the months and cut them to a
  third or less in the worst of 2008–09, 2020 and 2022. Its placebos, the same scales at other
  dates, did as well 22% of the time; four of five blocks gave a negative alpha against each block's
  own beta. QQQ's share of the profit fails gate 6 for any rule close to the five in equal parts, as
  SC-002-01 found.
- **About the lab.** The theory had been recorded tested-inconclusive with a form its own verdict
  named untested; TM-035's reader found it, and the lab reopened TM-047 rather than leave the form
  between a closed theory and one that could not tell itself apart by it. The decision is written
  down, with no code to enforce it: the readers and the logic audit are the barrier.

TM-047 is `tested-inconclusive`: its two strategies failed gate 3, the first also gates 4 and 5, the
second gates 4 to 6; the trend form's timing added nothing, and the risk-premium form is not proven
and not refuted. A third trial on SPY alone, whose figure is reported above, would be chosen from
this result.
