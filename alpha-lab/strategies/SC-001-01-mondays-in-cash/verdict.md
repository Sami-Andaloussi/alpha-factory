# SC-001-01 — The equity funds out of the market over each week's first session: verdict

**Stops at gate 2, economic edge. Not refuted, not proven: IWM's weekend effect, its week's last
session less its next first, was +0.075% a weekend, at the low end of the predicted 0.07 to 0.17%
and 1.05 standard errors from zero; the rule that sat out each week's first session earned 3.56% a
year before costs and lost it all to them.** Out of the five equity funds over each week's first
session and in them otherwise, the base earned an alpha of −1.66% a year over the five held always,
+3.56% before costs of 5.22% a year for two switches a week; an appraisal ratio of −0.17, +0.37
before costs, against a predicted 0 to 0.8% and 0 to 0.1 before costs. The week's first session was
weaker than the card predicted in every fund, most in EFA and EEM, which the card had expected at
about zero; the small caps' Monday was not weaker than the large caps'. Thresholds, version 4; the
battery's figures are the notebook's, [report.ipynb](report.ipynb), and the weekday measures,
alphas before costs and years are computed apart from it, on the same sessions. The theory is
[SC-001](../../bank/SC-001-day-of-the-week-effect.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; the targets read no price, only the calendar of
   scheduled sessions; 864 decisions, once clustered, over 18.0 years in-sample, from the first
   holding on 2005-01-03.
2. **Economic edge: fails.** A Sharpe ratio of 0.254, below the 0.4 required and the benchmark's
   0.396, with an alpha of −1.66% a year; at twice the costs, −0.022 and −6.86%. Costs are 5.22% a
   year, 0.277 of a gross Sharpe ratio of 0.531, more than a third.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.893, below 0.95; the rule beats
   94.5% of 1,000 placebos, its own weights shifted in time, which pay the same costs.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is −0.174, against 0.644 expected
   from the best of thirty-nine effective trials by luck: a deflated Sharpe ratio of 0.000.
5. **Stability: fails.** The blend of the two variants fails gates 2, 3 and 4, and the variant's
   Sharpe ratio is −0.452. The base's alpha is positive in one block of five, 2008–09 (+4.1% a
   year), and negative in 2005–07 (−3.5%), 2010–14 (−3.7%), 2015–19 (−2.2%) and 2020–22 (−1.7%);
   without its best year, 2009, it is −2.42% a year.
6. **Robustness: fails.** The neighbour, out over each week's first two sessions, keeps −35% of the
   base's Sharpe ratio, below 70% and 50%; a day's delay, out over Tuesday instead of Monday, keeps
   −57%, below 70%. The largest share of the profit is QQQ's, 23.8%; the five funds form one
   cluster, so none is left out.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.29 and an alpha of −8.86% a
   year, both above the tenth percentile of the in-sample paths (−0.44 and −9.26%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 6 as well.

## The card's refutation, clause by clause

Over the 938 pairs of a calendar week's last scheduled session and the next week's first, from
2005-01-07 and 2005-01-10 to 2022-12-23 and 2022-12-27, each placed by the market session whose
return spans it, IWM's return less the bill's rate over the last session less the same over the next
first: a mean of +0.0746% a weekend, a standard error of 0.0708% from the pairs, t +1.05.

- *A t statistic of −0.35 or below*: not met. The theory is **not refuted**; short of gates 1 to 7,
  it is **not proven**.

**The test's power.** The card gave the clause about a 36% chance of refuting with no effect, 9% at
+0.07% and 5% at +0.09%; the standard error came out at 0.071%, as the card expected (0.072%). The
effect measured lies at the low end of the prediction and within noise of zero: the run can tell
neither an effect of the sources' recent size from none, nor refute it.

Reported, not graded, as the card stated them, each gap with the standard error from the two groups'
variances:

- **The week's first session against the other sessions**, a day, before costs: SPY −0.049%
  (standard error 0.050%, t −0.98), QQQ −0.031% (0.053%), IWM −0.066% (0.061%, t −1.09), EFA −0.101%
  (0.056%, t −1.81), EEM −0.133% (0.071%, t −1.87); the five funds' average −0.076% (0.055%, t
  −1.39); IWM less SPY −0.017% (0.026%, t −0.68).
- **The week's last session against the other sessions**: SPY −0.017%, QQQ −0.085% (t −1.78), IWM
  +0.028%, EFA −0.014%, EEM +0.024%; the average −0.013% (0.046%); IWM less SPY +0.044% (0.025%, t
  +1.77).
- **The weekend effect**, a weekend: SPY +0.026%, QQQ −0.043%, IWM +0.075%, EFA +0.070%, EEM +0.126%
  (0.082%, t +1.53); the average +0.051% (0.063%, t +0.80); IWM less SPY +0.049% (0.033%, t +1.46).
- **By block of pairs**, placed by their last session: IWM +0.071% (t +0.51), +0.067% (t +0.73) and
  +0.086% (t +0.65) in 2005–2010, 2011–2016 and 2017–2022, 313, 313 and 312 pairs; the average
  +0.013%, +0.049% and +0.089%.
- **Long weekends**: over the 122 pairs whose first session's return spans four calendar days or
  more, IWM +0.176% (0.177%, t +0.99) and the average +0.149%, against +0.059% and +0.036% over the
  816 others.
- **Without the pairs whose last session falls in 2008 or 2020**: IWM +0.055% (0.063%, t +0.87),
  over 833 pairs. **Scaled** by IWM's standard deviation over the 21 sessions before each pair's
  last session, over the 934 pairs that have them: +0.023 of a standard deviation (t +0.47).
- **The alphas**: the base −1.66% a year after costs, +3.56% before, costs 5.22%, an appraisal ratio
  of −0.17 and +0.37; the variant, held over each week's last session only, −5.33% and −0.11%, costs
  5.22%, an appraisal ratio of −0.67 and −0.01.

## What was learned

- **About the theory.** On the lab's funds from 2005 to 2022, IWM's weekend effect stayed at about
  the size the futures showed from 1993 to 2011, some 0.07% a weekend, in each of the three blocks —
  the two later ones outside all the sources' samples — larger over long weekends, as Singal found;
  all within noise. It did not take the shape the sources gave it. The weakness sat in the week's
  first session in every fund, the large caps included, against the sources' finding that the large
  caps' Monday had become no lower than their other days; the small caps' Monday was no weaker than
  the large caps' (IWM less SPY −0.017%), and IWM's edge over SPY came from Friday instead. The
  bank's second criterion, an effect larger in small caps, is not borne out on Mondays.
- **About the rule.** Sitting out the week's first session earned 3.56% a year before costs over the
  five funds held always, four times the top of the prediction, most of it from EFA's and EEM's
  Mondays; two switches a week at 5 basis points a side cost 5.22% a year and left −1.66%. With a
  day's delay, out over Tuesday, the rule lost; out over Monday and Tuesday, it lost too. The Friday
  half, held alone, earned nothing before costs.
- **About the market.** The rule's best years against the benchmark, after costs, were 2009 (+9.9
  points of hedged return), 2011 (+6.3) and 2022 (+4.7); its worst 2010 (−17.8), 2005 (−11.6) and
  2016 (−7.3). Over the holdout it lost 8.86% a year of alpha, above the in-sample floor.
- **About the lab.** The card's largest error was EFA's and EEM's first session, which it predicted
  at about zero from European cash markets of 1997 to 2004: funds that hold foreign markets and
  trade in New York had no source of their own, and the card said so only by leaving them at zero.
  No code catches a prediction borrowed from a different market; the logic audit is where it is
  asked.

SC-001 is `tested-inconclusive`: on the lab's equity funds from 2005 to 2022, the small caps'
weekend effect held at about the size the sources last measured, within noise; the week's first
session was weak in every fund, not in the small caps alone, and a rule built on it paid more in
costs than it gained.
