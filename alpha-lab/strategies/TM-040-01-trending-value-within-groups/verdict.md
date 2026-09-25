# TM-040-01 — Value and momentum together within sectors, equity markets and commodities: verdict

**Stops at gate 2, economic edge. Not refuted, not proven: the composite of a value rank and a
momentum rank earned an appraisal ratio of 0.075, 0.085 below momentum alone's 0.160, a third of a
standard error — as the card's disclosure foresaw, it behaved like an equal blend of the two halves
(0.069).** Holding, in each of the three groups, the top third by the average of the two ranks
earned an alpha of 0.28% a year over the funds held in equal parts from 2010 to 2022, at a tracking
error of 3.8%, below both halves' (5.4% for momentum, 4.8% for value): the lower volatility the
theory claims, bought with a smaller alpha. Its Sharpe ratio, 0.6352, fell 0.0003 short of the
benchmark's. The prediction, 0.7 to 1.8% of alpha and a ratio of 0.25 to 0.6, was not reached. Of
the variants, reported and not graded, O'Shaughnessy's own construction — the cheaper half by value,
then the best by six months' momentum — earned 2.50% a year at a ratio of 0.61 in-sample, and
nothing over the holdout; read after the result, it grades nothing (below). Thresholds, version 4;
the battery's figures are the notebook's, [report.ipynb](report.ipynb); the comparisons with the
halves are `python -m lab.compare`'s, and the blend, the correlations, the groups, the years and
the screen's examination are computed apart from it, on the same sessions and costs. The theory is
[TM-040](../../bank/TM-040-value-momentum-combination.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 300 dates; the targets do not change when the prices older
   than the declared memory of 1,260 sessions are scrambled, on 150 dates; 146 decisions, once
   clustered, over 12.9 years in-sample, from the first target on 2010-02-01.
2. **Economic edge: fails.** A Sharpe ratio of 0.6352 against the benchmark's 0.6355, with an alpha
   of 0.28% a year; at twice the costs, 0.618 and 0.02%. Costs are 0.28% a year, 0.017 of a Sharpe
   unit.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.995; the rule beats 79.3% of 1,000
   placebos, its own weights shifted in time, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.075, against 0.581 expected
   from the best of thirty-one effective trials by luck: a deflated Sharpe ratio of 0.034.
5. **Stability: fails.** The blend of the three variants passes gates 2 and 3 but fails gate 4 (a
   deflated Sharpe ratio of 0.190). The base's alpha is +0.48% a year in 2010–14, −2.32% in 2015–19
   and +3.62% in 2020–22, the earlier blocks empty: two positive of the three needed. Without its
   best year, 2022, the alpha is −1.00% a year.
6. **Robustness: passes.** The neighbours keep a median of 100% of the base's Sharpe ratio and at
   least 72% at ±25%; with the sector funds left out, 70%; the largest share of the profit is XLE's,
   21.0%; a day's delay keeps 98%.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 1.00 and an alpha of −0.24% a
   year, both above the tenth percentile of the in-sample paths (0.01 and −3.01%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 5 as well.

## The card's refutation, clause by clause

Over the base's evaluation sessions, from 2010-02-02, the two halves rebuilt from their locked code
earn appraisal ratios of 0.160 (CA-001-01's momentum) and −0.102 (CA-024-01's value): momentum is
the better half. `lab.compare` gives the base's ratio, 0.075, less momentum's as −0.085, with a
standard error of 0.251 from 1,000 paired draws of whole months.

- *Below the better half's by more than one standard error*: not met, the gap being a third of a
  standard error. The theory is **not refuted**; short of gates 1 to 7, it is **not proven**.

**The test's power.** The card gave the clause about a 20% chance of refuting a combination no
better than its better half, 11 to 16% at a gain of 0.05, and 33 to 45% for one worse by 0.1; the
standard error came in at 0.25, within the range the audit simulated. The gap measured, −0.085,
lies between no gain and a loss of 0.1: the run cannot tell the claim from its opposite. The card
also disclosed that a rule behaving like an equal blend of the halves would land about half a
standard error below momentum; the base landed a third of one below, its ratio within 0.006 of the
blend's (a standard error of 0.217).

Reported, not graded, as the card stated them:

- **Each rule, over the same sessions**: the base, an alpha of 0.28% a year at a tracking error of
  3.79%; momentum, 0.87% at 5.42%; value, −0.49% at 4.83%; the equal blend of the halves' hedged
  returns, 0.19% at 2.72%, a ratio of 0.069. The base's tracking error is 0.70 of momentum's and
  0.78 of value's — the reduced volatility the bank asks for — but its alpha fell further, to a
  third of momentum's.
- **The alphas' differences** (`lab.compare`): the base less momentum −0.58% a year (a standard
  error of 1.14%); less value +0.78% (1.44%).
- **The variants**, by the same comparison. The six-month composite: an alpha of 0.63% at 4.10%, a
  ratio of 0.152, −0.008 against momentum's (a standard error of 0.349), +0.084 against the blend's
  (0.322). O'Shaughnessy's screen: 2.50% at 4.07%, a ratio of 0.614, +0.454 against momentum's
  (0.359), +0.546 against the blend's (0.351).
- **Correlations** of the hedged monthly returns: the base with momentum 0.58, with value 0.26; the
  halves with each other −0.28, as CA-024-01 found.
- **By group**, the base's chosen members against the group's ranked members held in equal parts,
  their drift between targets ignored: the sector funds +1.38% a year (a standard error of 1.63%),
  the equity markets −1.38% (1.02%), the commodities +1.75% (2.68%).
- **By year**, the base's return hedged of the benchmark, in points: 2010 +1.8, 2011 +0.6, 2012
  −1.5, 2013 +5.2, 2014 −1.6, 2015 +0.5, 2016 −1.2, 2017 −0.8, 2018 −6.7, 2019 −2.4, 2020 −0.9, 2021
  −3.6, 2022 +14.3; without 2022 the alpha is −1.00% a year, without 2020 +0.20%.

## What was learned

- **About the theory.** On the lab's nineteen funds from 2010 to 2022, selecting within each group
  on the average of a value rank and a momentum rank lowered the tracking error below either half's,
  as the theory claims, but kept only a third of momentum's alpha: its appraisal ratio, 0.075, was
  about a blend's and below momentum's, within noise of both. The combination did not add what the
  sources find over the long record, and value's loss over these years, which the card named, is the
  likely reason: a combination with a half that lost cannot beat the half that won by much. The
  mechanisms the bank names — underreaction, long-run overreaction — are not tested.
- **About the screen, found after the result.** O'Shaughnessy's construction did far better
  in-sample than the base: an alpha of 2.50% a year, a Sharpe ratio of 0.77 against the benchmark's
  0.64, and, on one draw of 1,000 placebos made apart from the battery, beating all of them. Its
  gain came from the sector funds (+3.99% a year, a standard error of 1.62%) and the commodities
  (+7.03%, 3.46%), the equity markets losing (−1.58%); its blocks were +0.90%, −0.54% and +9.72% a
  year, two positive of three; without 2022 its alpha is 1.60% a year, without 2020 1.75%; XLE, XLI
  and SLV carry 18%, 16% and 13% of its profit. At thirty-one effective trials its deflated Sharpe
  ratio is 0.50, short of gate 4's 0.9. Over the holdout, 2023 to 2025, it earned an alpha of −0.11%
  a year. It is the best of three variants, seen after the result, with a holdout that shows
  nothing: it grades nothing, and a card built on it now could only be judged on years the lab has
  already read, its trials added to the count.
- **About the market.** The base's best years against the benchmark were 2022 (+14.3 points,
  energy's and value's year) and 2013 (+5.2); its worst 2018 (−6.7) and 2021 (−3.6). Over the
  holdout it lost 0.24% a year of alpha, above the in-sample floor.
- **About the lab.** A card whose halves have run is barely blind: the disclosure computed from two
  published verdicts — a blend's ratio about half a standard error below momentum's — foresaw the
  base's result to within 0.006 of a ratio. The one part the run could still add was how selecting
  on both at once differs from blending; for the composite, not at all. `lab.compare` now measures
  the difference of appraisal ratios with its standard error, which the card needed and the tooling
  lacked.

TM-040 is `tested-inconclusive`: on the lab's nineteen funds from 2010 to 2022, the composite of
value and momentum ranks within groups had a lower tracking error than either half but an appraisal
ratio of 0.075, a third of a standard error below momentum alone's, as a blend of the halves was
known to; O'Shaughnessy's screen, a variant, did much better in-sample and nothing over the holdout,
and grades nothing.
