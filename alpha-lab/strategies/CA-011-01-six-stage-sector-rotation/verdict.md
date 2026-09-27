# CA-011-01 — Sector rotation through the six stages of the cycle: verdict

**Stops at gate 3, significance. Not refuted, not proven: the sectors Pring's stage names, held in
turn, earned an appraisal ratio of 0.145 against the sector funds held in equal parts — inside the
predicted 0 to 0.2 — but not by earning more: over the same sessions they returned 0.17% a year
less than those funds, with a beta of 0.85 to them, and the alpha of 1.29% a year is what the lower
beta leaves.** Holding, each week, the sectors and asset classes Murphy names for the stage that the
trends of bonds, stocks and commodities give earns a Sharpe ratio of 0.51 in-sample against 0.51 for
the fifteen funds held in equal parts, and an alpha of 1.21% a year, 0.54% at twice the costs: it
passes gate 2. It beats 80.1% of its placebos, where 90% are needed. Thresholds, version 4; the
battery's figures are the notebook's, [report.ipynb](report.ipynb), and the clause, the tilt, the
stages and the registry's correlation are computed apart from it, on the same closes, with the
lab's Sharpe ratio as corrected before the run (a series whose spread is rounding alone has none).
The theory is [CA-011](../../bank/CA-011-sector-rotation.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 300 dates; the targets do not change when the prices older
   than the declared memory of 301 sessions are scrambled, on 150 dates; 149 decisions, once
   clustered, over 16.1 years in-sample, from the first target on 2006-11-20.
2. **Economic edge: passes.** A Sharpe ratio of 0.513 against the benchmark's 0.507, an alpha of
   1.21% a year; at twice the costs, 0.466 and 0.54%. Costs are 0.70% a year, 0.047 of a Sharpe
   unit, at the bottom of the predicted 0.7 to 0.9%.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.988, but the rule beats only 80.1%
   of 1,000 placebos, its own weights shifted in time, where 90% are needed.
4. **Multiple testing: fails.** The appraisal ratio is 0.156, inside the predicted 0 to 0.2, against
   0.614 expected from the best of 69 effective trials by luck: a deflated Sharpe ratio of 0.038.
5. **Stability: fails.** The blend of the three variants passes gates 2 and 3 but fails gate 4. The
   alpha is positive in two of the five blocks; by the registry's hedged monthly returns, summed,
   about −0.6% in 2006–07, −1.9% in 2008–09, +12.6% in 2010–14, −3.5% in 2015–19 and +11.6% in
   2020–22. Without its best year, 2008, the alpha is 0.05% a year.
6. **Robustness: passes.** The neighbours of the average, 150, 250, 100 and 300 sessions, keep a
   median of 98% of the base's Sharpe ratio, at least 94% at ±25%, and none holds the base's
   targets; with the sector funds left out, 84%; the largest share of the profit is XLE's, 21.7%; a
   day's delay keeps 101%.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.87 and an alpha of 0.77% a
   year, both above the tenth percentile of the in-sample paths (−0.18 and −4.96%).

The variants, by the registry's appraisal ratios against the fifteen funds: the base, "all", 0.156;
"sectors", 0.101; "assets", 0.350. All three fail gate 3.

## The card's refutation, clause by clause

The clause judges the variant "sectors" from its first holding, on 2006-11-21, to 2022-12-31, 4,055
sessions, against the sector funds that trade held in equal parts, reset when the variant sets
targets and when XLRE and XLC start to trade, at the lab's costs.

- *Refuted if the appraisal ratio is zero or below*: it is **0.145**, an alpha of **1.29%** a year
  on a tracking error of 8.9%, all three inside the card's predicted ranges. The theory is **not
  refuted**; short of gates 1 to 7, it is **not proven**.
- **What the ratio is made of.** The variant's excess returns averaged 9.36% a year against the
  benchmark's 9.52%, with volatilities of 19.0% and 19.8%: a raw difference of −0.17% a year. Its
  beta to the benchmark is 0.85; hedged with it, the alpha is 1.29%. The sectors of the stages held
  less of the sector funds' common move and gave up almost none of their return; they did not earn
  more. The bank's first refutation reads "earned nothing over the sectors held always": raw, they
  earned slightly less; hedged, as the card grades, more.
- **The second refutation**, sectors adjusting at once, is not graded: a day's delay keeps 101% of
  the base's Sharpe ratio, which reads the speed only coarsely. **The third** is not graded.

## Measures stated before the run

- **Tilt against timing.** The variant's average weights — XLY 17.9%, XLU 16.1%, XLE 12.9%, XLB
  11.0%, XLP 10.2%, XLI and XLK 10.2% each, XLF 9.1%, XLV 1.4%, XLRE 1.2%, XLC none — held fixed
  and reset on the same weeks, over the funds that trade, against the same benchmark: an appraisal
  ratio of 0.099 and an alpha of **+0.16%** a year. The reasoning expected the tilt to lose about
  0.2 to 0.4% a year from TM-002-01's published sector alphas; it earned a little instead, outside
  the estimate but within noise. The timing, the rest, is about 1.1% of the 1.29%.
- **The stages.** Share of the sessions and the mean daily difference between the variant's and
  the benchmark's returns, annualised, over the sessions held under each:

  | stage | sessions | difference a year |
  |---|---|---|
  | out of sequence | 12.5% | −0.83% |
  | 1, bonds up alone | 13.2% | −5.78% |
  | 2, bonds and stocks up | 23.2% | −0.00% |
  | 3, all three up | 26.4% | +0.08% |
  | 4, stocks and commodities up | 19.2% | +0.21% |
  | 5, commodities up alone | 3.8% | +14.34% |
  | 6, all three down | 1.8% | +5.22% |

  Out of sequence the variant holds the eleven sector funds, like its benchmark, and differs from it
  only by the resets. Stage 1's defensive sectors, held while the bonds' trend was up alone, gained
  10.8% over its 80 sessions of 2008 and gave it back, −10.6%, over 99 sessions of 2009, then lost
  a little in most later years. Stage 5 is almost one episode: 150 of its 155 sessions fall in 2022,
  where energy and staples gained 6.2%; stage 6's 71 sessions gained in 2016 and lost in 2022. The
  raw differences, weighted by the stages' shares, sum to about −0.2% a year, as the whole sample
  does.
- **The six stages alone**: the clause's hedged series, with the whole-sample beta, over the
  sessions held under a stage, 0.130.
- **By halves**: 2006 to 2013, −0.008; 2014 to 2022, +0.256.
- **The variant "assets" against the fifteen funds**: 0.350, the registry's figure to the fourth
  decimal.
- **The registry's series**: the variant "sectors"'s monthly returns hedged of its sector benchmark
  correlate at 0.455 with CA-014-01's variant "stocks", hedged of its nine funds, over their 194
  common months: nearly half of their timing's gains and losses go together, as two rules reading
  the same trends of bonds and commodities should.
- **The alpha by year**, the clause's hedged series annualised: 2006 −11.0% (six weeks), 2007
  +1.6%, 2008 +7.1%, 2009 −13.7%, 2010 +5.8%, 2011 +0.6%, 2012 −1.8%, 2013 +1.2%, 2014 +4.5%, 2015
  −2.8%, 2016 +11.9%, 2017 −1.2%, 2018 −11.9%, 2019 +4.3%, 2020 −0.2%, 2021 +6.6%, 2022 +10.2%;
  nine years of gain and eight of loss.

## What was learned

- **About the theory.** On the lab's sector funds, the sectors Murphy and Stovall name for each of
  Pring's stages, read weekly from three 200-session trends, did not earn more than the sectors held
  always. They carried less of the sectors' common risk at almost the same return, and the rotation's
  measured edge is that lower beta: an appraisal ratio of 0.145, at the size the card expected and
  of noise. Its best years were 2008, 2016 and 2022, its worst 2009 and 2018; the defensive stage
  gained in the crash and gave it back in the rebound, and the stage Murphy reserves for commodities
  rising alone came once, in 2022. The first half of the sample gave nothing; the second gave 0.26.
- **About the market.** The asset classes the stages name carried more than the sectors did: the
  variant "assets" reached 0.35 against the fifteen funds, most of it in 2008, 2020 and 2022, the
  years the lab's trend rules earned. Within stocks, choosing the sector by the cycle's stage added
  little that holding them all did not.
- **About the lab.** The logic audit found a defect in the lab itself: a series whose spread was
  rounding alone, such as a run that held only cash, received a noise Sharpe ratio instead of none.
  It was corrected, with a test, before the run. The audit also moved the base from the sectors
  alone, certain to fail gate 6 when the sector funds are left out, to the sectors with the asset
  classes, as CA-014-01 had, with the sectors alone graded.

## Status

CA-011 is `tested-inconclusive`: CA-011-01, the one strategy drawn, stops at gate 3; its clause
neither refutes the theory nor supports it beyond noise, and what it measures is a lower beta more
than a higher return.
