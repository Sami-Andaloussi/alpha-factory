# MR-032-01 — Last week's laggards within sectors, equity markets and commodities: verdict

**Stops at gate 2, economic edge. Refuted in this form — on the lab's liquid funds, over a week,
within their groups: a fund's past five sessions against its group did not predict its next week
with a negative sign; the weekly rank correlation came out at +0.0106, with a standard error of
0.0114, above the clause's +0.004.** Holding each group's laggards of the last week earned 1.14% a
year less than the funds held in equal parts before costs, and 4.42% less after costs of 3.27% a
year. The prediction, a correlation of about −0.01, was a judgment the sources gave little ground
for among these funds, and the run leaned the other way: continuation, strongest among the
commodities, as Chan and Ilmanen expect for futures and industries. The refutation says nothing of
the theory's own domain — single stocks, small capitalisations, days — which the lab cannot reach.
Thresholds, version 4; the battery's figures are the notebook's, [report.ipynb](report.ipynb), and
the rank correlations, the alphas before costs and the years are computed apart from it, on the
same sessions. The theory is [MR-032](../../bank/MR-032-cross-sectional-mean-reversion.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 300 dates; the targets do not change when the prices older
   than the declared memory of 21 sessions are scrambled, on 150 dates; 790 decisions, once
   clustered, over 17.9 years in-sample, from the first target on 2005-01-18.
2. **Economic edge: fails.** A Sharpe ratio of 0.240, below the 0.4 required and the benchmark's
   0.483, and an alpha of −4.42% a year; at twice the costs, 0.075 and −7.65%. Costs are 3.27% a
   year, 0.165 of a gross Sharpe ratio of 0.405, more than the third allowed.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.89; the rule beats 16.4% of 1,000
   placebos, its own weights shifted in time.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is −0.782, against 0.615 expected
   from the best of thirty-four effective trials by luck: a deflated Sharpe ratio of 0.000.
5. **Stability: fails.** The blend of the three variants fails gates 2, 3 and 4. The base's alpha is
   positive in one block of five, 2008–09 (+1.26% a year), and negative in 2005–07 (−4.09%),
   2010–14 (−7.15%), 2015–19 (−5.07%) and 2020–22 (−2.95%); without its best year, 2008, it is
   −5.02% a year.
6. **Robustness: passes.** The neighbours, windows of 4, 6, 2 and 8 sessions, keep a median of 126%
   of the base's low Sharpe ratio and at least 111% at ±25%; with the sector funds left out, 70%;
   the largest share of the profit is XLK's, 13.0%; a day's delay keeps 96%.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.73 and an alpha of −3.98% a
   year, both above the tenth percentile of the in-sample paths (−0.42 and −8.53%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 5 as well.

## The card's refutation, clause by clause

On the 937 weekly target sessions from 2005-01-18 whose next window ends by 2022-12-30, the rank
correlation within each group between the members' last five sessions and their next week, from the
close of the session before the target to the close of the session before the next target, averaged
each week over the groups with three ranked members or more, weighted by their members: a mean of
+0.0106, a standard error of 0.0114 (t +0.93); the weekly series' lag-one autocorrelation is −0.001.

- *A mean of +0.004 or above*: met. The theory is **refuted in this form**: on the lab's funds, over
  a week, within their groups, no negative relation between a member's past relative return and its
  next.

**The test's power.** The standard error came in at 0.0114, above the 0.008 the logic audit's
simulation assumed: the weekly average of the groups' correlations moved by about 0.35, not 0.25,
the groups' correlations moving together more than independent draws do. At that error the clause
refutes about 36% of the time with no relation, 11% at a correlation of −0.01 and 2% at −0.02. The
mean measured lies 1.8 standard errors above the prediction's centre, −0.01, and 0.9 above zero: the
run makes a reversal of the predicted size unlikely, and cannot tell a continuation from none.

Reported, not graded, as the card stated them:

- **The groups weighted equally**: +0.0202 (a standard error of 0.0121, t +1.67), the commodities'
  weight raised.
- **Over the returns the rule holds**, from the target's close to the next target's close, 936
  weeks: +0.0092 (0.0115).
- **The variants**: the monthly one, over 21 sessions and the month after, −0.0005 (0.0237) over 214
  months; the pooled one, the nineteen as one basket, −0.0011 (0.0123).
- **The decay**: the base's signal against (a) the target session's own return, which the rule
  cannot hold, +0.0095 (0.0115); (b) the first session held, −0.0229 (0.0114, t −2.00); (c) the week
  after next, +0.0012 (0.0114).
- **By group**: the sector funds −0.0043 (0.0141), the equity markets +0.0182 (0.0178), the
  commodities +0.0460 (0.0243, t +1.89) over the 869 weeks they had three ranked members.
- **In 2008 and 2020**, the years of high volatility: +0.008 and +0.010, each with a standard error
  of 0.056.
- **The alphas**: the base −4.42% a year after costs, −1.14% before, costs 3.27%; the monthly
  variant −2.23% and −1.46%, costs 0.77%; the pooled variant −4.14% and −0.78%, costs 3.36%.

## What was learned

- **About the theory.** On the lab's liquid funds, over a week, a fund's lag against its group did
  not revert: the correlation leaned positive, most among the commodities (+0.046), where Chan
  writes that most futures portfolios show no cross-sectional mean reversion and Ilmanen finds
  momentum at short horizons; the sector funds, where Ilmanen expects industry momentum, were about
  nil. The monthly and pooled forms were about nil too. The refutation is scoped: the theory's
  domain is single stocks, days and small capitalisations, and its own third criterion expects a
  weaker effect in liquid instruments; a rule the core could hold, weekly and long only, found none,
  and its costs, 3.3% a year, would have needed a correlation near −0.09 to pass gate 2.
- **About the decay, read after the result.** Of the pre-stated decay measures, the first session
  held is the only one with a negative sign, −0.023, two standard errors from zero: a reversal
  lasting about a day, as the theory's decay "within days" would have it, and gone by the week's
  end. One figure of several at two standard errors is what chance gives often; and a rule that
  could use it would trade daily, which the core cannot. It grades nothing.
- **About the market.** The rule's only positive year against the benchmark was 2008 (+8.2 points of
  hedged return); its worst 2010 (−11.8), 2016 (−10.8) and 2013 (−9.9). Over the holdout it lost
  3.98% a year of alpha, above the in-sample floor.
- **About the lab.** The audit's simulation drew each group's correlation independently, and the
  standard error came out a third lower than the run's: groups of funds share a market, and their
  weekly rank correlations move together. A power estimate for a measure averaged over groups draws
  them correlated, or states the assumption. No code enforces it; the logic audit is where it is
  checked.

MR-032 is `tested-inconclusive`: its one strategy failed gates 2 to 5, and the theory is refuted in
the form the lab can test — on liquid funds, over a week, within their groups, no cross-sectional
reversal — while its domain, single stocks over days, is out of the lab's reach.
