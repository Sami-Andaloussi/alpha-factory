# SC-026-01 — Out of the US sector funds on the session after each change of the clocks: verdict

**Stops at gate 2, economic edge. Not refuted by the clause, and not supported: over the thirty-six
sessions after the United States' changes of the clocks from 2005 to 2022, the sector funds earned
0.016% a day less than on the other Friday-to-Monday sessions, 0.06 standard errors below zero, on
the claim's side of the line only through 2020-03-09, the Monday after the change of 8 March 2020,
on which they fell 8.4%, a session the card named before the run as tilting the clause; without it
the sessions after the changes earned 0.22% a day more than the comparable ones, 1.71 standard
errors above zero, the opposite of the claim, and the spring's, the library's firmest sign, about
the same as the others.** Out of the funds on those sessions and in them otherwise, the rule earned
an alpha of −0.02% a year over the sector funds held always, +0.18% before costs of 0.20% a year, an
appraisal ratio of −0.01 and a Sharpe ratio of 0.492 against the benchmark's 0.496; without
2020-03-09 the alpha is −0.58% a year. Thresholds, version 4; the battery's figures are the
notebook's, [report.ipynb](report.ipynb), and the sessions' returns, the reported gaps and the
alphas with and without 2020-03-09 are computed apart from it, on the same sessions and costs. The
theory is [SC-026](../../bank/SC-026-daylight-saving-time-anomaly.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 100 dates; the targets read no price, only the calendar of
   scheduled sessions, the rule's dates of the clocks and the funds' tradability; 39 decisions, once
   clustered, over 18.0 years in-sample, the first entry, 36 changes and the entries of XLRE and
   XLC. The thirty-six sessions out are all Mondays, from 4 April 2005 to 7 November 2022.
2. **Economic edge: fails.** A Sharpe ratio of 0.492, above the 0.4 required but below the
   benchmark's 0.496, with an alpha of −0.02% a year; at twice the costs, 0.481 and −0.21%. Before
   costs the Sharpe ratio is 0.502; costs are 0.20% a year, 0.011 of a Sharpe unit.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.994; the rule beats 64.4% of 1,000
   placebos, its own weights shifted in time, fewer than 90%.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is −0.009, against 0.637 expected
   from the best of fifty-one effective trials by luck: a deflated Sharpe ratio of 0.003.
5. **Stability: fails.** The blend of the variants, the base alone, fails gates 2, 3 and 4. The
   battery's block alphas: 2005–07 −0.42% a year, 2008–09 +0.99%, 2010–14 −0.30%, 2015–19 −1.32%,
   2020–22 +2.21%; two positive blocks of five. Without its best year, 2020, the alpha is −0.50% a
   year, as the card expected.
6. **Robustness: passes.** The neighbour, `sessions` 2, keeps 88% of the base's Sharpe ratio, and a
   day's delay 88%; the largest share of the profit is XLE's, 14.7%, as the card expected of eleven
   funds; the sector funds form one cluster. The neighbour's and the delayed rule's alphas, computed
   apart: −1.07% a year (appraisal ratio −0.33) and −1.19% (−0.49): both sit out 2020-03-10, which
   rose, and the delayed rule every Election Day of the autumn changes from 2008.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.86 and an alpha of 0.55% a
   year, both above the tenth percentile of the in-sample paths (−0.17 and −1.39%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 5 as well.

## The card's refutation, clause by clause

Over the in-sample sessions from 2005-01-04, the sector funds' average daily excess return over the
36 sessions whose return spans the Sunday of a change of the clocks, −0.023%, less that over the 780
other sessions from a Friday's close to a Monday's, −0.007%: −0.016% a day, a standard error of
0.270%, t −0.06.

- *A t statistic of +0.35 or above*: not met. The theory is **not refuted** by the clause, and not
  proven.

**How the clause came out below the line.** The card named 2020-03-09 before the run as a session no
source ties to sleep that would tilt the clause toward "not refuted", and said the gap without it is
the one read against the predicted range. The sector funds fell 8.37% that day. Without it, the
other 35 sessions earned 0.216% a day against the comparable sessions' −0.007%: +0.222% a day
(0.130%, t +1.71), past the refutation's line by more than a standard error and the opposite of the
predicted 0 to −0.2%. Without 2020: +0.188% (0.123%, t +1.52). The clause does not refute, as
written and locked; the lab's data does not support the claim either.

**The test's power.** The card gave the clause about a 36% chance of refuting with no effect and 12
to 16% at −0.2% a day, with a standard error of about 0.24%, 0.32% with the crash day. The standard
error came out at 0.270%.

Reported, not graded, as the card stated them, each gap with the standard error from the two groups'
variances, for the sector funds' average unless stated:

- **The seasons**: the spring changes −0.496% (0.488%, t −1.02, 18 sessions), which without
  2020-03-09 is about −0.032%, a fifth of a standard error; the autumn changes +0.463% (0.175%, t
  +2.65), and without the seven election eves +0.302% (0.153%, t +1.98, 11 sessions). The spring
  change, the library's firmest sign, left no trace but the crash; the autumn Mondays rose.
- **By fund**: the sector funds from XLE −0.330% (0.625%) and XLY −0.151% (0.249%) to XLV +0.158%
  (0.221%) and XLRE +0.212% (0.676%, 13 sessions); XLC −0.357% over 9 sessions. The broad funds: SPY
  −0.022% (0.255%), QQQ +0.029%, IWM −0.167% (0.330%), EFA −0.122% (0.265%), EEM +0.090% (0.316%).
- **Against all other sessions**: −0.061% (0.267%, t −0.23).
- **The second session after each change**, the Tuesday, the neighbour's, against the other
  Tuesdays: +0.532% (0.270%, t +1.97): 2020-03-10's rebound and the autumn's Election Days among
  them.
- **EFA on its European markets' changes**, the last Sundays of March and October, on the New York
  session from a Friday's close to a Monday's, 32 sessions (four others, whose New York session did
  not span Friday to Monday, left out): −0.277% (0.301%, t −0.92), against its other such sessions.
- **By period**: 2007–2022 −0.044% (0.303%); 2005–2006, four sessions, too few to inform.
- **The holdout**, 2023 to 2025: −0.500% (0.250%, t −2.00), over six sessions.
- **The alphas**: the rule −0.02% a year after costs, +0.18% before, costs 0.20%, an appraisal ratio
  of −0.01; without 2020-03-09, −0.58% a year, an appraisal ratio of −0.55. The hedged return by
  year: 2020 +6.6 points, 2008 +1.2; 2016 −2.0, 2015 −1.6, 2019 −1.5.

## What was learned

- **About the theory.** On the US sector funds from 2005 to 2022, the sessions after the changes of
  the clocks were not weak. The spring's, the change the library signs, averaged about what other
  Mondays did once 2020-03-09 is set aside; the autumn's rose, by more than two standard errors,
  with seven of its eighteen falling on the eve of a federal election. The clause does not refute
  SC-026 in this form, by the margin of one crash day that fell on a Monday after a change of the
  clocks in a pandemic's first weeks; read without it, as the card said it would be read against its
  range, the sessions after the changes did better than the comparable ones.
- **About the rule.** Out of the market two sessions a year, the rule's alpha was the crash day's:
  with it about zero after costs, without it −0.58% a year. Its neighbour and its delayed form, out
  on the Tuesday, lost about 1% a year, missing the rebound of 2020-03-10.
- **About the market.** The holdout's six sessions after the changes were weak, 0.50% a day below
  the other Mondays, two standard errors over six sessions: too few to reopen the question.
- **About the lab.** The card was drawn with its one known extreme session named, and with the gap
  without it stated as the reading against the range; the run then split exactly along that line. A
  clause on thirty-six sessions is at the mercy of any one of them, and the disclosure before the
  run is what lets the verdict say so.

SC-026 is `tested-inconclusive`: its one strategy failed gates 2 to 5, and the theory is not refuted
in the one form the lab can test, the US sector funds out of the market on the session after each
change of the clocks, though without the one crash day the sessions after the changes were stronger
than comparable ones; investors' sleep is out of the lab's reach.
