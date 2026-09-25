# LL-042-01 — Cross-asset momentum between equities and Treasuries: verdict

**Stops at gate 2, economic edge. The lead and lag between Treasuries and equities is refuted in
this narrow form, by the card's first clause, at an estimate indistinguishable from zero; the rule
that joins it to each fund's own trend is not proven, and adds nothing measurable to the own trend
alone.** Holding an equity index while both its own past year and the Treasury market's
beat the bill, and a Treasury fund while its own does and US equities' does not, gives a Sharpe
ratio of 0.43 in-sample against 0.44 for the seven funds held always, with an alpha of 1.50% a year
and 80.8% of its placebos beaten. The pure lead and lag — equities on the bonds' past year alone,
bonds on the equities' — earns an alpha of −0.37% a year. Thresholds, version 2; the battery's
figures are the notebook's, [report.ipynb](report.ipynb), and the own-trend reference is computed
from the in-sample weights, apart from it. The theory is
[LL-042](../../bank/LL-042-cross-asset-momentum-spillovers.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; 68 decisions, once clustered, over 16.1 years
   in-sample, from the first holding on 2006-12-01, the first month the Treasury market's past year
   beat the bill.
2. **Economic edge: fails.** A Sharpe ratio of 0.43 against the benchmark's 0.44: the rule does not
   match holding the seven always, though its alpha is 1.50% a year, 1.43% at twice the costs. It
   held 36% of the portfolio on average, no equity fund in 77 of its 193 months and nothing at all
   in 61: the alpha is a return for less exposure, not a better Sharpe ratio. Costs are 0.08% a
   year.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.98; the rule beats 80.8% of its
   placebos, the same weights shifted in time by a year or more, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.22, against 0.35 expected
   from the best of seven effective trials by luck: a deflated Sharpe ratio of 0.37.
5. **Stability: fails.** The blend of the two rules fails gates 2, 3 and 4 (an alpha of 0.57% a
   year, 77.2% of its placebos beaten), and the worse rule, the pure lead and lag, keeps a Sharpe
   ratio of 0.36. The alpha is positive in three of the five blocks, negative in 2010–14 and
   2015–19; without its best year, 2010, it stays at 1.24% a year.
6. **Robustness: fails,** three times. The neighbours of the lookback keep a median of 66% of the
   base's Sharpe ratio, below 70%, and at least 59.7% at ±25%. Without the equity indices, 23% of it
   remains: the bond legs, held in 26 months of 193, keep their signal but earn little, as the
   reasoning expected. QQQ carries 40% of the profit, above the 30% any one fund may, as the
   reasoning warned it might. A day's delay costs nothing; without the bonds, 97% remains.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.52 and an alpha of 0.81% a
   year, both above the tenth percentile of the in-sample paths (−0.21 and −4.35%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 6 as well.

## The card's refutation, clause by clause

The clause is read rule by rule: the reasoning declared, before the run, that the rule "cross",
which reads the other market's signal alone, is the battery's own test of the lead and lag.

- *An alpha of zero or less over the seven held always*: not met by the rule "both", 1.50% a year;
  **met by the rule "cross"**, −0.37% a year (an appraisal ratio of −0.06).
- *50% or fewer of its placebos beaten*: not met by "both", 80.8%. The battery does not rank "cross"
  alone among placebos; its blend with "both" beats 77.2%.
- *Beats more than 50% but fewer than 90%; keeps less than half its Sharpe ratio with one cluster
  left out; one fund above 30% of the profit*: all met by "both", which is therefore **not proven**.
- *Turns to zero or less without its best year*: not met, 1.24% a year.

**What the other market's signal adds.** The card declared a reference, computed apart from the
battery on the same seven funds and days: each fund held in a seventh while its own past year beats
the bill, TM-017-01's rule. It earns a Sharpe ratio of 0.58 and an alpha of 2.55% a year in-sample,
more than either rule of this card; against it, the rule "both" leaves an appraisal ratio of −0.06
(a t-statistic of −0.25), indistinguishable from zero: the Treasury market's signal adds nothing
measurable to each fund's own trend, and alone it earned nothing.

The Treasury channel of LL-042 is **refuted in this narrow form** — the lead and lag between the US
Treasury market and five equity indices, read over a year and traded monthly on the lab's funds from
2006 to 2022, long only — not in general. LL-042 is `tested-inconclusive`; its corporate bond and
currency channels are untested.

**The test's power.** The rule "both" made 68 independent decisions in-sample; its appraisal ratio
of 0.22 is measured to about ±0.25 over 16 years. The pure lead and lag's −0.06 lies within a
quarter of a standard error of zero; an edge of an appraisal ratio of 0.3 — a modest gain, as the
sources report for the United States — would lie 1.4 standard errors above what was measured, about
a one-in-fourteen chance: the data do not exclude a modest edge. What they show is no edge,
measured too loosely to exclude a modest one.

## What was learned

- **About the theory.** The sources find the bond market's past year predicting equities across 20
  countries; on the lab's funds it did the opposite of what it was meant to at the times that
  mattered most. In August and September 2011 Treasuries rose as investors fled to them (TLT +24%),
  the rule held all five equity indices, and equities fell (SPY −12%, IWM −19%, EFA −19%, EEM
  −26%): a rising bond market announced a crisis, not cheaper capital reaching equities. The
  Treasury market's past year turned negative in 2021 and the rule held nothing from April 2021 to
  the end of 2022: it missed the rest of 2021's rise and stood aside in 2022, when equities and
  bonds fell together — its second-best year of edge, after 2010. The
  bond legs, the theory's own direction from equities to bonds, were held in 26 months and earned
  little. What the cross-asset signal predicts on these funds is not separated from what each
  fund's own past predicts, which does better alone.
- **About the market.** US equities carried most of the rule's profit, QQQ 40% of it, SPY and IWM
  much of the rest, and EEM 14%; EFA and the bonds almost none. From 2006 to 2022 the bond market's trend
  and the equity market's often pointed the same way, and the rule then held equities and not bonds
  — or, when yields rose, nothing at all.
- **About the lab.** Gate 6 would have failed this rule whatever its edge under the battery's
  version 1: leaving out the bond cluster removed the prices the equity legs read. Version 2 leaves
  a cluster out by making it untradable, its prices still read, and this card is the first it
  judges. Its gate 6 now measures what it is meant to: without the equity indices, the rule keeps
  23% of its Sharpe ratio because its profit is theirs, not because it lost its signal.
