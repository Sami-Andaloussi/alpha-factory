# CA-014-01 — Sector rotation on the commodity/bond ratio: verdict

**Stops at gate 3, significance. Not proven, not refuted; the sectors' own rotation not shown.**
Holding, each week, the inflation side — energy, materials, gold and commodities — while the ratio
of DBC to IEF stands above its 200-session mean, and the rate-sensitive side — staples, health
care, financials, utilities and Treasury notes — otherwise, earns a Sharpe ratio of 0.52 in-sample
against 0.51 for the nine funds held in equal parts, and an alpha of 0.98% a year: it passes gate 2.
It beats 87.4% of its placebos, close to but short of the 90% needed. Unlike TM-002-01's, its
alpha is timing, not a tilt: its average mix, held fixed, earns −0.16% a year. But the sector funds
alone, the variant and the purer test of the intermarket claim, earn an appraisal ratio of only
0.04 against the six sectors held in equal parts: most of the base's edge came from holding the
commodity fund on the side its own ratio favoured. The split between ordinary monetary regimes and
the zero-rate years is within noise, and points one way for the base and the other for the variant.
Thresholds, version 2; the battery's figures are the notebook's, [report.ipynb](report.ipynb), and
the figures the card asks the verdict to compute — over the ordinary regimes, and the variant
against the six sectors — are computed apart from it, on the same sessions and costs, as are the
fixed mix, the years and the holdings. The theory is
[CA-014](../../bank/CA-014-intermarket-analysis.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; 66 decisions, once clustered, over 16.1 years
   in-sample, from the first holding on 2006-11-20.
2. **Economic edge: passes.** A Sharpe ratio of 0.52 against the benchmark's 0.51, an alpha of 0.98%
   a year; at twice the costs, a Sharpe ratio of 0.49 and an alpha of 0.58%. Trading costs, with the
   weekly reset of drifted weights, are 0.45% a year, 0.027 of a Sharpe unit.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.99; the rule beats 87.4% of 1,000
   placebos, its own weights shifted in time by a year or more, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.14, against 0.42 expected
   from the best of thirteen effective trials by luck: a deflated Sharpe ratio of 0.13.
5. **Stability: fails.** The blend of the two variants fails gates 2, 3 and 4 (a Sharpe ratio of
   0.48 against 0.51, an alpha of 0.33% a year, 82.6% of its placebos beaten). The alpha is positive
   in two of the five blocks, 2010–14 (1.9% a year) and 2020–22 (5.5%), and negative in 2005–07
   (−0.7%), 2008–09 (−2.5%) and 2015–19 (−0.7%); without its best year, 2014, it is 0.29% a year.
   The worst variant's Sharpe ratio is 0.45, the variant's.
6. **Robustness: passes.** The neighbours of the average keep a median of 103% of the base's Sharpe
   ratio, and at least 95% at ±25%; without the sectors, the worst cluster to lose, 78% remains; the
   largest share of the profit is energy's, 29.0%, just under the 30% any one fund may carry; a
   day's delay costs nothing.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.02 and an alpha of −5.17% a
   year, both above the tenth percentile of the in-sample paths (−0.22 and −5.60%), the alpha barely.

## Verdict

The strategy stops at gate 3, and fails gates 4 and 5 as well.

## The card's refutation, clause by clause

The card judges the base by its appraisal ratio over the nine funds, measured to about ±0.25, and
by the same series over the ordinary monetary regimes — the sessions whose bill rate was 0.25% a
year or more, 42.6% of them from the first holding, 6.9 years.

- *The base — a whole-sample ratio of −0.1 or less, half of its placebos or fewer, and an
  ordinary-regime ratio of zero or less*: the whole-sample ratio is 0.14 and the rule beats 87.4% of
  its placebos, so the clause is not met, though the third condition is: the ordinary-regime ratio
  is −0.03. The theory is **not refuted**; short of gates 1 to 7, it is **not proven**.
- *The variant, the sector funds alone, against the six sectors held in equal parts — refuted if
  that ratio is −0.1 or less and its ordinary-regime figure zero or less*: the ratio is 0.04, and
  0.10 over the ordinary regimes. The claim that the other markets' trend moves the stock market's
  sectors is **not refuted, not shown**. Against the nine funds, as the battery measures it, the
  variant's ratio is −0.04.

**The test's power.** The base's ratio of 0.14 is measured to ±0.25: half a standard error below
the assumed 0.2 to 0.3, and half a standard error above zero. The variant's 0.04 against its
sectors, measured to ±0.25, lies about one standard error below 0.25 — the size the card assumed
for the base against the nine funds, and did not state for the variant against the six sectors.
Over the ordinary regimes, 6.9 years, the figures are measured to about ±0.38, and over the
zero-rate years, 9.2 years, to about ±0.33; neither the base's −0.03 nor the variant's 0.10 can be
told from zero or from 0.25. The test could have refuted a rule with no edge about one time in
five; it did not, and it could not have shown the assumed edge either.

## What was learned

- **About the theory.** The rule's alpha is timing: it spent half its sessions on each side, and its
  average mix — about 12% in each inflation fund and 10% in each rate-sensitive one — held fixed and
  reset each week, earns an alpha of −0.16% a year, an appraisal ratio of −0.24. What the ratio's
  trend chose added about 1.1% a year over that mix. But the part of it that the intermarket claim
  names, the sector funds' rotation, earned little: against the six sectors held in equal parts, the
  variant's appraisal ratio is 0.04, an alpha of 0.34% a year. More of the base's edge came from the
  legs the variant drops, and nearly all of that from one: timing the non-sector legs alone earns an
  alpha of 0.87% a year, timing the sectors alone 0.12%, and by the active weights about 58% of the
  edge is outside the sectors — nearly all of it the commodity fund (+0.85% a year), gold and the
  notes adding nothing. Holding DBC while DBC outruns IEF is the ratio's own trend, the part of the
  rule the intermarket claim does not need.

  The regime split is not a finding. Over the ordinary regimes the base's appraisal ratio was −0.03,
  and over the zero-rate years 0.29; the variant's, against its sectors, 0.10 and −0.01. The base
  leans against the theory's stated limits and the variant with them; each figure is within about
  one standard error of zero, and the two point in opposite directions.
- **About the market.** The base's best years were 2014 (+11.1% of edge), when commodities fell 28%
  and utilities and health care rose 29% and 25%, and the rule sat on the rate-sensitive side 80% of
  the time; 2015 (+9.0%), all of it on that side; and 2022 (+10.2%), 90% of it on the inflation side
  through the rise of energy and commodities. Its worst were 2009 (−10.8%), when it held the
  rate-sensitive side through the first quarter and most of the second, into the rebound that
  materials led (+48% over the year), and 2016 (−10.2%) and 2012 (−5.6%). The loss named for 2008
  did not come: the rule held the inflation side into late August, switched for good on 2 September,
  and held the rate-sensitive side — notes, staples, health care, utilities and financials — through
  the fourth quarter, when IEF rose and energy and materials fell with commodities; it gained 5.9% of
  edge over the year, though financials, on the side it held, fell 55%. Energy carried 29% of the
  base's profit and 52% of the variant's; commodities 16% of the base's.
- **About the holdout.** Over 2023–25 the rule earned an alpha of −5.17% a year, at the edge of the
  floor, mostly in 2024 (−5.6% of edge) and 2025 (−10.8%), after +0.9% in 2023. Among the nine funds
  gold led, rising 134%, but the rule held it only part of the time, and sat on the rate-sensitive
  side 79% of 2024; the inflation funds it held when it switched rose little over the three years
  (energy +13%, materials +24%, commodities +4%). Three years say little about an edge.
- **About the lab.** The pace was chosen from the source, and the count of the signal's switches was
  made before the card, a departure from the practice LL-042-01 set; the verdict records it. The run
  counted 66 decisions, close to the 64 switches foreseen. The card's figures computed apart — over
  the ordinary regimes, and the variant against its own sectors — were defined in the card before
  the run, so that the verdict could not choose them; they are what separated the ratio's own trend
  from the intermarket claim.

CA-014 is `tested-inconclusive`: rotating between the inflation and rate-sensitive sides on the
commodity/bond ratio's 200-session trend earned a small alpha from timing that the lab cannot tell
from luck, most of it from holding the commodity fund while the ratio of commodities to notes rose —
the ratio's own trend — rather than from the sectors whose rotation the theory names; the sectors
alone showed no edge, and the split between ordinary and zero-rate regimes is within noise. Its
currency and bond-to-stock relations are untested here, the second refuted in a narrow form by
LL-042-01.
