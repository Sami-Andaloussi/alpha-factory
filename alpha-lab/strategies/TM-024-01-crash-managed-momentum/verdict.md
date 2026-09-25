# TM-024-01 — Momentum with its crashes managed: verdict

**Stops at gate 2, economic edge. Not proven, not refuted: managing the crashes of CA-001-01's
momentum tilt changed its alpha by less than the noise of the difference, in both forms.** Switching
each group's tilt off in its panic states — its market down over two years, its volatility above its
own average — earns a Sharpe ratio of 0.44 in-sample against 0.46 for the nineteen funds held in
equal parts, and an alpha of 0.09% a year, where CA-001-01, the same rule unmanaged, earned 0.20%.
Scaling the tilt by the inverse of its own volatility, the variant, earns 0.38%. Both lie within
the card's band of 0.5% a year around CA-001-01's alpha. Before hedging, the switch did what the
sources say in 2009, and paid for it in the months before and after; hedged of the market, its gain
is the market's. Thresholds, version 2; the battery's figures
are the notebook's, [report.ipynb](report.ipynb), and the comparisons with CA-001-01 are computed
apart from it, on the same sessions and costs. The theory is
[TM-024](../../bank/TM-024-momentum-crashes.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; 149 decisions, once clustered, over 16.9 years
   in-sample, from the first holding on 2006-02-01. With k held at 1 the rule gives CA-001-01's
   targets exactly, checked before the run.
2. **Economic edge: fails.** A Sharpe ratio of 0.44 against the benchmark's 0.46, and an alpha of
   0.09% a year; at twice the costs, 0.43 and −0.14%. Costs are 0.25% a year.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.98; the rule beats 52.3% of its
   placebos, its own weights shifted in time by a year or more, where 90% are needed — CA-001-01
   beat 47.6%.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.016, against 0.34 expected
   from the best of seven effective trials by luck: a deflated Sharpe ratio of 0.09. The registry
   now holds ten trials and still counts seven effective: the two rules of this card and CA-001-01's
   move together closely enough to count as one, as the reasoning expected.
5. **Stability: fails.** The blend of the two rules fails gates 2, 3 and 4. The alpha is positive
   in two of the five blocks, 2010–14 and 2020–22, as CA-001-01's was, and negative in 2005–07,
   2008–09 and 2015–19; without its best year, 2022, it is −0.43% a year. The worst variant's
   Sharpe ratio is 0.44, the base's.
6. **Robustness: passes.** The neighbours of the two windows keep a median of 101% of the base's
   Sharpe ratio, and at least 97% at ±25%; without the sectors, the worst cluster to lose, 93%
   remains; no fund carries more than 13% of the profit (QQQ); a day's delay costs nothing.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 1.00 and an alpha of −0.03% a
   year, both above the tenth percentile of the in-sample paths (−0.22 and −3.84%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 5 as well.

## The card's refutation, clause by clause

The card judges the managed rule by its alpha's difference from CA-001-01's, 0.20% a year over the
same in-sample sessions, with a band of 0.5% a year, about one standard error of the difference.

- *Short of CA-001-01's by more than 0.5% a year*: not met. The base's difference is −0.11% a year,
  with a standard error of 0.46% measured on the monthly differences (a t-statistic of −0.24); the
  variant's is +0.18%, with a standard error of 0.33% (+0.54).
- *Within 0.5% either way*: **met by both rules**, which are therefore **not proven**.
- *More than 0.5% above*: not met, so the clauses on placebos, clusters, one fund and the best year
  do not decide; for the record, the base beats 52.3% of its placebos, keeps 93% of its Sharpe ratio
  with a cluster out, has no fund above 13% of the profit, and turns negative without 2022.

**The test's power.** The reasoning estimated the difference's standard error at 0.5–0.6% a year,
from a volatility of the difference of 2–3% a year. It came in at 0.46% for the base (a volatility
of 1.89%), at the low edge of that estimate, and 0.33% for the variant (1.37%), well below it: for
the variant the band of 0.5% is one and a half standard errors, not one. The panic states were also
fewer than assumed: 41 of 609 group-months, 7%.

At these standard errors, a true gain of 1% a year, the prediction's upper end, would have cleared
the band's upper edge with a probability of 0.86 for the base and 0.93 for the variant; a true gain
of 0.3%, its lower end, only 0.33 and 0.27; a true difference of zero would have read as refuted
14% and 7% of the time. The measured differences lie 2.4 and 2.5 standard errors below a gain of
1%: the prediction's upper end is unlikely on these data. A gain of 0.3% lies 0.9 and 0.4 standard
errors above them: the lower half of the prediction is neither shown nor excluded, as the reasoning
said before the run.

## What was learned

- **About the theory.** The panic states were where the sources put them. Each group's market was
  in a panic state in these months:
  - the sectors: October 2008 to November 2009, July to September 2010, and April 2020, 18 months;
  - the equity markets: October 2008 to September 2009, August and September 2010, April and May
    2020, and October 2022, 17 months;
  - the commodities: December 2008, August to October 2013, and April and May 2020, 6 months.

  With the tilt off, the base's daily returns, before any hedging, summed to 7.7 points more than
  CA-001-01's in 2009 — 9.3 from March to November, after −1.4 in January and February — when the
  beaten funds led the rebound: the crash the theory describes, and avoided. It had given up 3.4
  points in the last months of 2008, when the tilt was still earning on the way down, as the
  reasoning warned, and later 0.6 in 2010 and 0.8 in 2022, in brief panic states whose markets did
  rebound (in September 2010 the equity markets rose 11.3% and the sectors 8.4%; in October 2022 the
  sectors 8.2% and the equity markets 5.4%) but whose beaten funds did not lead the rebound. It
  gained 1.1 points in 2013 and 2.2 in 2020.

  Over the whole sample the base returned 0.37% a year more than CA-001-01, and the variant 0.39%.
  But both carried more of the market: a beta of 1.01 and 0.97 against CA-001-01's 0.95. Holding a
  group in equal parts instead of its leaders means holding its beaten, riskier funds. The hedged
  alpha counts more than all of the base's gain as the market's — 0.058 more beta times the
  benchmark's premium of 8.2% a year is 0.48% a year, against a gain of 0.37% — and 55% of the
  variant's. The crash risk the theory names is, for a long-only tilt, a shortfall of market
  exposure in a rebound; turning the tilt off restores the exposure, and a benchmark regression
  pays for exposure only as beta. In the block where CA-001-01's alpha was worst, 2008–09, managing
  the tilt halved the loss (−2.3% a year for the base, −2.0% for the variant, against −4.8%, each
  regressed on the block alone, as gate 5 does) but did not turn it positive, which the reasoning
  had predicted.
- **About the market.** The variant cut the commodity tilt most: it averaged 0.84 of CA-001-01's
  there, against 0.91 for the sectors and 0.96 for the equity markets, and dropped as low as 0.08.
  Most of its gains are of 2008–09 (+0.9 and +4.5 points before hedging, 5.4 of the 7.9 points of
  its years of gain), and most of its losses of 2022 (−0.9 of −1.2 points).
- **About the neighbours.** The windows move the switch by little around the base. Shortening the
  volatility window to 94 or 63 sessions changes 9 and 17 of the base's 41 panic group-months, and
  lengthening it to 158 or 189 changes 10 and 12. The bear window matters more: 26 changed at 378
  sessions, 9 at 630, 52 at 252, where the panic states double, and 14 at 756. Gate 6's neighbours
  keep the Sharpe ratio all the same: a switch that acts in a few months moves the whole sample
  little, whichever months it acts in.
- **About the lab.** Block by block, the base's alpha is equal to CA-001-01's in the two blocks
  without a panic state, 2005–07 and 2015–19, and above it in the three with one (2008–09 by 2.5
  points a year, with a standard error of about 3.6 over the block; 2010–14 and 2020–22 by 0.2 and
  0.4), yet over the whole sample it is 0.11% a year below. That is not the whole-sample regression
  being harsh on a rule whose exposure changes with the states it forecasts. Letting the beta differ
  only in the months the two rules differ, the base's beta is 0.17 higher there, and the benchmark
  earned 27.4% a year in those months against 5.8% elsewhere: the alpha difference is then −0.17% a
  year, lower than the regression's −0.11%. The extra exposure was held in a strongly rising market,
  and a measure that pays for it only as beta leaves no alpha. The blocks look better for another
  reason: the 2008–09 block's benchmark earned −1.9% a year, its first nine months shared by both
  rules, so that its extra beta is credited there, not charged. A managed rule and its unmanaged
  parent differ in a few months, and gates 2 to 4 judge each against the benchmark, not against the
  other; the card said so before the run and judged the theory by the difference from its parent,
  with a band set from the parent's noise. The band's standard error came in at or below the
  estimate, so the band was, if anything, cautious. One detail of the variant: its tilt's return
  holds each month's target weights fixed through the month, as the card states, where the
  reasoning's "as the unmanaged rule held it" could be read as the holdings drifting with prices; the
  difference between the two was not measured.

TM-024 is `tested-inconclusive`: managing momentum's crashes, in the long-only form the lab can
hold on its groups of funds, is not proven to add alpha. The prediction's upper end, 1% a year, is
unlikely here. The sources' constant-volatility gain in futures, about 0.1 of Sharpe ratio, would be
about 0.6% a year on the tilt's residual volatility of about 6%, about 1.5 and 1.3 standard errors above
what the two rules measured: it is not excluded, nor is a smaller one.
