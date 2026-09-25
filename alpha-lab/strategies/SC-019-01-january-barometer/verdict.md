# SC-019-01 — Each equity fund after its own positive January, cash after a negative one: verdict

**Stops at gate 1, hygiene, on its count of decisions, as the card expected, and fails gates 2 to 6
as well. Not refuted, not proven: on the lab's funds from 2005 to 2022, the rest of the year earned
the same after a positive January as after a negative one — the three US funds 0.002% a day less
after the nine positive Januarys than after the nine negative ones, 0.05 standard errors below
zero, where the sources' size was +0.034%.** The rule, each fund held over January and kept for the
rest of the year only after its own positive January, earned an alpha of 1.69% a year over the five
held always, 1.75% before costs of 0.05% a year, an appraisal ratio of 0.19; but its regression
beta, 0.33, fell far below its average share invested, 0.52, because it was out in the volatile
years, and at a beta equal to that share the alpha is 0.03% a year: the whole alpha is the
mechanical gain the card named as a risk, not the barometer's. Thresholds, version 4; the battery's
figures are the notebook's, [report.ipynb](report.ipynb), and the years' returns, the gaps, the
regression, the neighbour's alpha and the alpha at a beta equal to the share held are computed apart
from it, on the same sessions and costs. The theory is
[SC-019](../../bank/SC-019-january-barometer.md).

## Gate by gate

1. **Hygiene: fails.** No look-ahead on 87 dates and no break of the memory of 45 sessions; but 25
   decisions, once clustered, over 18.0 years, fewer than 30: twelve of the eighteen years had a
   zero or negative January among the five funds, each adding a decision in February and one at
   the year's end. The card had put 21 to 28 decisions and a chance of 1 to 31% of reaching 30.
2. **Economic edge: fails.** A Sharpe ratio of 0.397, below the 0.4 required and the benchmark's
   0.398, with an alpha of 1.69% a year; at twice the costs, 0.393 and 1.64%. Costs are 0.05% a
   year.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.974; the rule beats 81.2% of 1,000
   placebos, its own weights shifted in time by a year or more, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.190, against 0.648 expected
   from the best of forty-eight effective trials by luck: a deflated Sharpe ratio of 0.034.
5. **Stability: fails.** The blend of the variants, the base alone, fails gates 2, 3 and 4. The
   battery's block alphas: 2005–07 −0.39% a year, 2008–09 −7.50%, 2010–14 +0.15%, 2015–19 −0.12%,
   2020–22 +2.23%; positive in two blocks of five. Without its best year, 2013, the alpha is 0.93%.
6. **Robustness: fails.** QQQ carries 46% of the profit, more than 30%. The neighbour, `months` at
   2, keeps 81% of the base's Sharpe ratio, and a day's delay 99%. Their alphas, computed apart:
   `months` 2 0.72% a year (appraisal ratio 0.08); the targets a session late 1.65% (0.19).
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 1.04 and an alpha of 1.06% a
   year, both above the tenth percentile of the in-sample paths (−0.31 and −5.16%).

## Verdict

The strategy stops at gate 1, and fails gates 2 to 6 as well.

## The card's refutation, clause by clause

For each year from 2005 to 2022, the three US funds' average daily excess return from February to
December, grouped by the sign of the mean of their three January returns: the nine years after a
positive January averaged 0.0442% a day, the nine after a zero or negative one (2005, 2008, 2009,
2010, 2014, 2015, 2016, 2020 and 2022) 0.0462%; the difference is −0.0020% a day, with a standard
error of 0.0373% from the years' own spread, t −0.05.

- *A t statistic of −0.35 or below*: not met. The theory is **not refuted**, and not proven: the
  gap sits at zero, about one standard error below the sources' size.

**The test's power.** The card gave the clause about a 37% chance of refuting with no effect, 23% at
+0.017% a day and 13% at +0.034%, on about seven negative Januarys; nine came, and the standard
error came out at 0.037%, a little below the card's 0.042%. The years' means were no more dispersed
than the daily errors say: the pooled gap on daily returns is the same, −0.0020% (0.0417%, t −0.05).

Reported, not graded, as the card stated them, for the three US funds' average unless stated:

- **By fund, each on its own January**: SPY −0.005% a day (0.032%, 8 positive Januarys, 10 not),
  QQQ +0.034% (0.047%, t +0.73, 10 and 8), IWM −0.015% (0.035%, t −0.43, 8 and 10), EFA −0.005%
  (0.036%, 9 and 9), EEM +0.018% (0.050%, t +0.36, 8 and 10); the five funds' average on its January
  −0.006% (0.038%, 9 and 9).
- **The asymmetry**: the rest of the year averaged 0.0452% a day over all eighteen years, 0.0442%
  after positive Januarys and 0.0462% after negative ones; it rose in 7 of 9 years after each sign.
  A negative January was as uninformative as a positive one — neither said anything.
- **The regression** of the rest of the year's return on January's: a slope of 0.50 (a standard
  error of 0.86, t 0.59), an intercept of 11.7% and an R² of 0.02.
- **The first five sessions**: grouped by their sign, the gap is +0.069% a day (0.040%, t +1.75),
  twelve positive starts against six negative ones (2005, 2008, 2014, 2015, 2016, 2022) averaging
  −0.001% a day over the rest of the year, 2008 and 2022 among them; one reading of several the card
  reported, not the claim graded.
- **By period**: 2005–2011 −0.030% (0.067%, t −0.45; 3 positive Januarys, 4 negative); 2012–2022
  +0.012% (0.043%, t +0.27; 6 and 5); without 2008 −0.025% (0.033%, t −0.76); without 2005 −0.005%
  (0.041%).
- **By year**, January's return and the rest of the year's, for the US funds' average: 2005 −3.3%
  and +8.3%, 2006 +4.9 and +8.5, 2007 +1.8 and +5.4, 2008 −8.2 and −31.7, 2009 −6.7 and +46.2, 2010
  −4.6 and +26.6, 2011 +1.6 and −1.1, 2012 +6.7 and +9.7, 2013 +4.7 and +29.9, 2014 −2.7 and +15.7,
  2015 −2.8 and +4.9, 2016 −6.8 and +21.9, 2017 +2.4 and +20.0, 2018 +5.7 and −10.3, 2019 +9.5 and
  +20.5, 2020 −0.03 and +29.1, 2021 +1.4 and +22.1, 2022 −7.9 and −17.4.
- **Decisions**: 25, from the twelve years with a zero or negative January among the five.
- **The alphas**: the rule 1.69% a year after costs, 1.75% before, costs 0.05%, an appraisal ratio
  of 0.19; at a beta equal to the share invested, 0.52, rather than the regression's 0.33, 0.03%.
  The neighbour's and the delayed rule's in gate 6 above. The hedged return by year: 2013 +15.8
  points, 2019 +15.4, 2017 +15.2; 2009 −21.2, 2016 −10.2, 2010 −9.7.

## What was learned

- **About the theory.** On the lab's funds from 2005 to 2022, the sign of January said nothing about
  the rest of the year: after nine positive and nine negative Januarys the US funds earned the same,
  the rest of the year rose in seven years of nine after each, and the regression's slope lay within
  a standard error of zero. The sources' own years inside the sample were mixed — 2008 a warning
  heeded, 2009 and 2010 rises after a fall — and the years after them, 2012 to 2022, no better. The
  barometer is not refuted by the clause's convention, its gap sitting at zero rather than below
  it, and it is not proven; what the lab can say is that, over these eighteen years, its signal
  carried none of the sources' spread.
- **About the rule.** Its alpha is an artefact of the regression: out of the funds in the most
  volatile years, its beta fell to 0.33 against an average share invested of 0.52, and the alpha
  the regression credits it with, 1.69% a year, is 0.03% at a beta equal to that share. The card
  named that gain as a risk and stated the measure that exposes it.
- **About the market.** Of the nine negative Januarys, seven were followed by a rising rest of the
  year, 2009, 2010, 2016 and 2020 by more than 20%.
- **About the lab.** A barometer read once a year cannot pass gate 1's floor of thirty decisions on
  five funds that move together unless nearly every year has a fall somewhere among them; the audit
  found it before the lock, and the card was locked with the failure written in, because the clause
  reads the theory whatever the battery finds. Grading on the years rather than the days, also the
  audit's, cost nothing here: the two agree.

SC-019 is `tested-inconclusive`: its one strategy failed gates 1 to 6, and the theory is not refuted
in the form the lab can test, each equity fund's rest of the year after its own January, while its
signal carried nothing over 2005 to 2022.
