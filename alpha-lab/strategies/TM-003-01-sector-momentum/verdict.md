# TM-003-01 — Sector momentum: verdict

**Stops at gate 3, significance. Not proven, not refuted; an edge of the source's size is ruled
out.** Holding, each month, the three sector funds with the highest return over the past six months,
in six overlapping monthly tranches, earns a Sharpe ratio of 0.52 in-sample against 0.49 for the
sector funds held in equal parts, and an alpha of 1.13% a year, 1.00% at twice the costs: it passes
gate 2. But it beats only 66.7% of its placebos, where 90% are needed. Its appraisal ratio, 0.18,
lies half a standard error below the card's prediction of 0.3 and two and a half below the source's
long side, near 0.8. Ranked on twelve months instead, the variant earns 0.49% a year, an appraisal
ratio of 0.07, both measured over the base's period, which includes the variant's first six months
in cash. Thresholds, version 2; the battery's figures are the notebook's,
[report.ipynb](report.ipynb), and the variant's own figures, the blocks by variant, the years and the
holdings are computed apart from it, on the same sessions and costs. The theory is
[TM-003](../../bank/TM-003-industry-momentum.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; 205 decisions, once clustered, over 17.4 years
   in-sample, from the first holding on 2005-08-01.
2. **Economic edge: passes.** A Sharpe ratio of 0.52 against the benchmark's 0.49, an alpha of 1.13%
   a year; at twice the costs, a Sharpe ratio of 0.51 and an alpha of 1.00%. Costs are 0.14% a year,
   0.007 of a Sharpe unit.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.99; the rule beats 66.7% of 1,000
   placebos, its own weights shifted in time by a year or more, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.18, against 0.36 expected
   from the best of nine effective trials by luck: a deflated Sharpe ratio of 0.24. The registry now
   holds twelve trials; this card's two count as two more effective ones, as the reasoning expected.
5. **Stability: fails.** The blend of the two variants passes gate 2 and fails gates 3 and 4 (59.2%
   of its placebos beaten, a deflated Sharpe ratio of 0.18). The alpha is positive in three of the
   five blocks — 2005–07 (0.3% a year), 2015–19 (0.7%) and 2020–22 (6.8%) — and negative in 2008–09
   (−4.8%) and 2010–14 (−1.5%). Without its best year, 2020, it stays positive, 0.58% a year. The
   worst variant's Sharpe ratio is 0.48, the variant's.
6. **Robustness: passes.** The neighbours of the lookback and the holding keep a median of 98% of
   the base's Sharpe ratio, and at least 92% at ±25%; no fund carries more than 24% of the profit
   (XLK); a day's delay costs nothing. The check of a cluster left out does not apply: the sectors
   are one cluster, the whole universe.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.72 and an alpha of −0.51% a
   year, both above the tenth percentile of the in-sample paths (−0.07 and −2.86%).

## Verdict

The strategy stops at gate 3, and fails gates 4 and 5 as well.

## The card's refutation, clause by clause

The card judges the base by its appraisal ratio over the sector funds held in equal parts, measured
to about ±0.24 over these years.

- *A ratio of −0.1 or less, with half of its placebos beaten or fewer*: not met. The ratio is 0.18,
  and the rule beats 66.7% of its placebos. The theory is **not refuted**.
- *A ratio of 0.3 or less*: **met**. An edge of the source's size is ruled out: the long side of the
  source's IM(6,6) earned an annual ratio near 0.8, 2.5 standard errors above the 0.18 measured.
- *Any other result short of passing gates 1 to 7*: met — fewer than 90% of placebos beaten, and
  failures at gates 4 and 5. The base is **not proven**.
- *The variant, read by its appraisal ratio alone against the same prediction*: 0.07, 1.0 standard
  error below the prediction and above the −0.1 of the refutation: **not proven** either.

**The test's power.** The base's ratio of 0.18 is measured to ±0.24: it is consistent with the
card's prediction of 0.3, half a standard error above it, and with no edge at all, 0.7 below it. The
test could tell the source's size from zero, and has ruled it out; it could not tell the predicted,
halved edge from luck, and did not, as the reasoning expected: a true 0.3 would have passed gate 4
about 7 to 9% of the time, the reasoning's estimate before the run and the registry's bar after it. The bets moved by 6.3% a year, a little more than the 5.6% the reasoning took
from the source; with an alpha of 1.13% a year, below the predicted 1.5 to 2%, that makes a ratio
of 0.18.

## What was learned

- **About the theory.** Ranked and held as its source ranks and holds, long only, sector momentum
  earned a positive alpha on the lab's sector funds, below the predicted size and about a third of
  the source's long side once diluted among eleven funds (3.1% a year; 2.9% among the nine funds
  before September 2016). It is one of at least four forms of momentum the lab has now run on these
  funds, five counting TM-024-01's crash-managed rule: CA-001-01's past year less its last month and
  its past year whole, both with the top third rebuilt each month, and this card's two. Measured
  alike — each rule run on the eleven sector funds alone, hedged of their equal weight, after costs
  — CA-001-01's base earns an appraisal ratio of −0.015 over this card's sessions; measured as
  CA-001-01's verdict measured its sector group, before costs and unhedged within the nineteen
  funds, CA-001-01's base scores −0.07 and its variant −0.10, where this card's base scores 0.11 and
  its variant 0.00. This base is the best of the four forms measured, on either measure: an edge the lab cannot
  tell from luck, and the best of several tries.
- **About the market.** The rule's years are uneven. It lost most in 2009 (−6.7% of edge) and 2011
  (−3.9%) and 2012 (−3.6%), and gained most in 2020 (+9.9%), 2022 (+8.9%), 2013 (+7.9%) and 2007
  (+5.2%): years of strong sector trends — 2020 with its crash and rebound — as for CA-001-01. The crash the reasoning named came: in
  February to April 2009 the base held staples, health care and utilities, the crash's leaders, for
  more than four fifths of the portfolio, into the rebound; by August its tranches had turned to
  technology, materials and consumer discretionary. In 2022 it held energy, which it held in 92% of
  the months of 2021–22. Technology carried the largest share of the profit, 24%, energy 12%. The
  twelve-month variant did worse: it held the crash's leaders longer — staples, health care and
  utilities were still two thirds of it in August 2009 — and it lost 6.3% of edge in 2021 and 6.1% in
  2016, and won back more than all of it in 2022 (+16.7%; energy gave about 12 of the 17 points of its active return that year).
- **About the holdout.** Over 2023–25 the base's alpha was −0.51% a year: no sign of an edge, and
  three years, with a standard error of about 3.6% a year, cannot tell. The holdout judges decay against the in-sample paths, not the edge, and it passed.
- **About the lab.** The clause's two thresholds — −0.1 to refute the theory, 0.3 to rule out the
  source's size — separated what the test could say from what it could not: the source's size is
  ruled out, the prediction is neither shown nor excluded, and nothing is refuted. A card in which one universe is
  one cluster leaves gate 6 with one check fewer; the verdict says so rather than count it as passed.

TM-003 is `tested-inconclusive`: industry momentum among the eleven US sector funds, in the source's
six-month form and long only, earned a small positive alpha that the lab cannot tell from luck; an
edge of the source's size is ruled out on these funds and years; the halved prediction is neither
shown nor excluded.
