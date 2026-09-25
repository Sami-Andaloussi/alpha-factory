# SC-025-01 — Out of the northern equity funds from the equinox to the solstice: verdict

**Stops at gate 2, economic edge. Not refuted, not proven: from 2005 to 2022 the four northern
equity funds earned 0.012% a day less from 22 September to 20 December than over the rest of the
year, 0.23 standard errors below zero, on the claim's side of the line; the card had expected a
refutation from the lab's published monthly figures, which put the gap at about +0.022% a day, but
the window's last days of September were weak and its December days short of the month's strong end,
which monthly averages spread evenly over their days could not show.** Holding the four funds
outside the window and the bill inside it earned an alpha of 1.20% a year over the four held always,
1.30% before costs of 0.10% a year, an appraisal ratio of 0.12 and a Sharpe ratio of 0.419, below
the benchmark's 0.427; at a beta equal to the three quarters of the sessions held, rather than the
regression's 0.67, the alpha is 0.46% a year, inside the predicted 0 to +1.1% before costs.
Thresholds, version 4; the battery's figures are the notebook's, [report.ipynb](report.ipynb), and
the window's returns, the reported gaps, the neighbours' alphas and the alpha at a beta equal to the
share held are computed apart from it, on the same sessions and costs. The theory is
[SC-025](../../bank/SC-025-seasonal-affective-disorder-effect.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 87 dates; the targets read no price, only the calendar of
   scheduled sessions and the window's dates; 37 decisions, once clustered, over 18.0 years
   in-sample, from the first holding on 2005-01-03. The window's sessions run from 22 September, or
   the first session after it, to 20 December, or the last session before it, 61 to 64 sessions a
   year, 1,135 in-sample.
2. **Economic edge: fails.** A Sharpe ratio of 0.419, above the 0.4 required but below the
   benchmark's 0.427, with an alpha of 1.20% a year; at twice the costs, 0.413 and 1.10%. Costs are
   0.10% a year, 0.006 of a Sharpe unit.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.975; the rule beats 78.2% of 1,000
   placebos, its own weights shifted in time, fewer than 90%.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.122, against 0.641 expected
   from the best of fifty effective trials by luck: a deflated Sharpe ratio of 0.018.
5. **Stability: fails.** The blend of the variants, the base alone, fails gates 2, 3 and 4. The
   battery's block alphas: 2005–07 −1.22% a year, 2008–09 +11.72%, 2010–14 −1.39%, 2015–19 +2.17%,
   2020–22 −6.02%; two positive blocks of five. Without its best year, 2008, the alpha is −1.17% a
   year.
6. **Robustness: fails.** QQQ carries 44% of the profit, more than 30%, as the card expected likely.
   The neighbours keep 98% of the base's Sharpe ratio at the median and at least 84% at ±25%, and a
   day's delay 91%. Their alphas, computed apart: the window of `days` 68, to 28 November, 1.14% a
   year (appraisal ratio 0.12), 112, to 11 January, 0.22% (0.02), 45, to 5 November, 1.00% (0.12),
   135, to 3 February, 1.01% (0.10); the targets a session late 0.58% (0.06).
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.86 and an alpha of −0.87% a
   year, both above the tenth percentile of the in-sample paths (−0.23 and −5.76%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 6 as well.

## The card's refutation, clause by clause

Over the in-sample sessions from 2005-01-04, the four funds' average daily excess return over the
1,135 sessions of the window, 0.0267%, less that over the 3,395 other sessions, 0.0384%: −0.0116% a
day, a standard error of 0.0497%, t −0.23.

- *A t statistic of +0.35 or above*: not met. The theory is **not refuted**, and not proven.

**What the card had expected.** The card read the lab's published monthly averages for the five
equity funds, weighted by the days of each month in the window, as a gap of about +0.022% a day, a t
statistic of about +0.43 to +0.50, and expected the clause to refute. The months were not even
within themselves: the window's days of September, from the 22nd, earned −0.177% a day in the four
funds, where September as a whole had averaged −0.020% in the five; its December days, to the 20th,
earned 0.010%, where December had averaged 0.054%, its strength lying in the days after the
solstice. Spreading a month's average evenly over its days, the card's assumption, moved the known
figure by about 0.03% a day, more than half a standard error, as the same assumption had moved
SC-010-01's.

**The test's power.** The card gave the clause about a 36% chance of refuting with no effect and 19
to 21% at −0.024% a day, the top of its range, with a standard error of 0.045 to 0.052%. The
standard error came out at 0.050%, the window's sessions more volatile than the others (1.52% a day
against 1.24%). The gap lies inside the predicted range, half-way to its top; the test cannot tell
it from none.

Reported, not graded, as the card stated them, each gap with the standard error from the two groups'
variances, for the four funds' average unless stated:

- **By fund**: SPY −0.005% (0.048%), QQQ −0.026% (0.051%), IWM −0.003% (0.058%), EFA −0.012%
  (0.054%); EEM −0.021% (0.075%); the five funds −0.014% (0.054%, t −0.25). Every fund was a little
  weaker in the window, none by more than half a standard error.
- **The latitude**: EFA less the US funds, in the window against outside, −0.001% (0.025%): no
  stronger effect in the markets farther north, in the one measure the lab has, which barely tests
  it.
- **The seasons**: the half year from 22 September to 20 March against the rest, −0.032% (0.039%, t
  −0.82); the winter alone, 21 December to 20 March, against the spring and summer, −0.040% (0.048%,
  t −0.84); the autumn window against the spring and summer, −0.024% (0.051%). The winter was weaker
  than the autumn, the opposite of the risk premium's timing the card read, and the lab's published
  monthly figures had put it so.
- **By month of the window**, against the sessions outside it: September's days −0.216% (0.134%, t
  −1.61, 116 sessions), October +0.006% (0.088%), November +0.046% (0.080%), December's days −0.028%
  (0.083%). The weakness lies in the window's first week and a half, the days around the equinox;
  October and November were ordinary.
- **By period**: 2005–2011 −0.026% (0.106%); 2012–2022 −0.002% (0.046%); **without 2008** +0.012%
  (0.040%, t +0.31). 2008's autumn carried the gap; without it the window earned slightly more than
  the rest of the year.
- **The holdout**, 2023 to 2025, the only new reading: −0.006% (0.078%, t −0.07).
- **The alphas**: the rule 1.20% a year after costs, 1.30% before, costs 0.10%, an appraisal ratio
  of 0.12; at a beta equal to the share of sessions held, 0.749, rather than the regression's 0.666,
  0.46%: being out over the autumn of 2008 lowered the beta and carried about three fifths of the
  alpha, as the card warned. The neighbours' and the delayed rule's in gate 6 above. The hedged
  return by year: 2008 +16.6 points, 2018 +15.9, 2009 +8.6; 2022 −9.7, 2020 −9.3, 2011 −6.6.

## What was learned

- **About the theory.** On the lab's four northern equity funds from 2005 to 2022, the weeks from
  the September equinox to the December solstice were a little weaker than the rest of the year, in
  every fund and in both halves of the period, but by a quarter of a standard error, and 2008's
  autumn carried it: without that year the window was slightly stronger. The weakness lay in the
  days just after the equinox, not through the shortening days; the winter after the solstice was
  weaker still, and EFA's markets, farther north, were no weaker than New York's. SC-025 is not
  refuted in this form, and the lab's data gives it no support that a single crash does not explain.
- **About the rule.** Out of the funds a quarter of the year, the rule beat them held always by
  about 1.2% a year, three fifths of it the lower beta of being out in October and November 2008,
  and lost to them in Sharpe ratio; QQQ, the strongest fund outside the window, carried 44% of the
  profit.
- **About the market.** Over 2023 to 2025 the window earned about what the rest of the year did.
- **About the lab.** A second card has now read the lab's published monthly figures as if each
  month's return were spread evenly over its days, and a second time the within-month pattern moved
  the figure by more than half a standard error: SC-010-01 against the mid-month, here against the
  last days of September and of December. A disclosure that weights monthly averages by days is a
  guess, not a known figure, and is written as one. The card's season was read three times from the
  same sources — the autumn, the half year, the autumn — and the disclosure of that choice, written
  before the run, is in the reasoning.

SC-025 is `tested-inconclusive`: its one strategy failed gates 2 to 6, and the theory is not refuted
in the one form the lab can test, the northern equity funds out of the market from the September
equinox to the December solstice; its hemispheres are out of the lab's reach.
