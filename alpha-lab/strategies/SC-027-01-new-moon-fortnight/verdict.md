# SC-027-01 — The equity funds held in the fortnight around the new moon: verdict

**Stops at gate 2, economic edge. Not refuted, not proven: from 2005 to 2022 the five equity funds
earned 0.024% a day more in the fortnight around the new moon than in the other sessions, in the
claim's direction and a little above the predicted 0 to +0.020%, but 0.58 standard errors from zero;
the gap lay in the week before the new moon rather than around it, half of it went with the sessions
at the turn of the month, and the new-moon fortnights were calmer, with lower volume and variance,
where the sources had found none.** Holding the five funds in the new-moon fortnight and the bill in
the other earned an alpha of 0.64% a year over the five held always, 1.87% before costs of 1.24% a
year, an appraisal ratio of 0.06 and a Sharpe ratio of 0.312, against the benchmark's 0.394; at a
beta equal to the 0.51 of sessions held, rather than the regression's 0.47, the alpha after costs is
0.26% a year. Thresholds, version 4; the battery's figures are the notebook's,
[report.ipynb](report.ipynb), and the fortnights' returns, the reported gaps, volumes and variances,
the neighbours' alphas and the alpha at a beta equal to the share held are computed apart from it,
on the same sessions and costs. The theory is [SC-027](../../bank/SC-027-lunar-cycle-effect.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 100 dates; the targets read no price, only the calendar of
   scheduled sessions, the formula's mean new moons and the funds' tradability; 446 decisions, once
   clustered, over 18.0 years in-sample. The new-moon fortnights hold 2,311 of the 4,534 scheduled
   in-sample sessions, the count the card gave.
2. **Economic edge: fails.** A Sharpe ratio of 0.312, below the 0.4 required and the benchmark's
   0.394, with an alpha of 0.64% a year; at twice the costs, 0.229 and −0.60%. Before costs the
   Sharpe ratio is 0.395; costs are 1.24% a year, 0.083 of a Sharpe unit.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.925, below 0.95; the rule beats
   71.9% of 1,000 placebos, its own weights shifted in time, fewer than 90%.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.058, against 0.633 expected
   from the best of fifty-two effective trials by luck: a deflated Sharpe ratio of 0.008.
5. **Stability: fails.** The blend of the variants, the base alone, fails gates 2, 3 and 4. The
   battery's block alphas: 2005–07 +3.65% a year, 2008–09 −7.68%, 2010–14 +3.04%, 2015–19 −1.34%,
   2020–22 +2.50%; three positive blocks of five. Without its best year, 2006, the alpha is −0.13% a
   year.
6. **Robustness: passes.** The neighbours keep 92% of the base's Sharpe ratio at the median and at
   least 75% at ±25%, and a day's delay 132%; the largest share of the profit is QQQ's, 23.8%, under
   30%, where the card had expected one fund's share likely to fail the gate. The neighbours'
   alphas, computed apart: `days` 5 1.93% a year (appraisal ratio 0.19), 9 −1.30% (−0.12), 4 1.54%
   (0.16), 10 −1.81% (−0.18); the targets a session late 2.12% (0.20). The narrower windows, nearer
   the new moon, did better, and the wider ones worse; the neighbours hold from 30% to 71% of the
   sessions, so their Sharpe ratios mostly read their exposure.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.28 and an alpha of −4.43% a
   year, both above the tenth percentile of the in-sample paths (−0.45 and −7.67%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 5 as well.

## The card's refutation, clause by clause

Over the in-sample sessions from 2005-01-04, the five funds' average daily excess return over the
2,310 sessions within 7 days of the nearest new moon's date, 0.0463%, less that over the 2,220 other
sessions, 0.0225%: +0.0238% a day, a standard error of 0.0410%, t +0.58.

- *A t statistic of −0.35 or below*: not met. The theory is **not refuted**, and not proven.

**The test's power.** The card gave the clause about a 36% chance of refuting with no effect and
about 20% at +0.020% a day, the top of its range, with a standard error of about 0.040%; it came out
at 0.041%. The gap lies just above the range's top, and 0.58 standard errors from nothing: the test
cannot tell it from none. The disclosed pull of SC-016-01's window, about −0.006% a day, was against
it.

Reported, not graded, as the card stated them, each gap with the standard error from the two groups'
variances, for the five funds' average unless stated:

- **By fund**: SPY +0.017% (0.037%), QQQ +0.005% (0.041%), IWM +0.028% (0.046%), EFA +0.053%
  (0.041%, t +1.29), EEM +0.016% (0.055%): every fund in the claim's direction, none by more than
  1.3 standard errors. The sector funds' average +0.024% (0.036%); GLD +0.021% (0.034%), SLV +0.037%
  (0.062%), DBC +0.001% (0.038%).
- **The moon's quarters**, each against the other sessions: the week before the new moon, days −7 to
  −1, +0.079% (0.047%, t +1.68); the week from the new moon, days 0 to +7, −0.042% (0.044%, t
  −0.95); the full moon's side before the full moon +0.017% (0.048%), after it −0.052% (0.050%, t
  −1.04). The strength lay in the days leading to the new moon, and the days just after it were
  weak: not the sources' symmetric fortnight.
- **Kaufman's halves**, the waning half, from a full moon to the next new moon, less the waxing
  half: the five funds +0.070% (0.041%, t +1.72), GLD +0.050% (0.034%, t +1.50), SLV +0.134%
  (0.062%, t +2.17), DBC +0.021% (0.038%). In these years the waning half rose more than the waxing
  half, in equities and in the metals alike, the direction of Kaufman's 1972 futures, which the card
  had read as predicting no fortnight gap.
- **Volatility and volume**, lunar month by lunar month over 222 months, the new-moon fortnight less
  the adjacent full-moon fortnight: the log of the five funds' realised variance −0.096 (0.056, t
  −1.72); the mean log traded volume of SPY, QQQ and IWM −0.028 (0.016, t −1.69). The new-moon
  fortnights were calmer and traded less, where Yuan, Zheng and Zhu had found no change: the bank's
  second refutation, a pattern that comes with changes in volatility or volume, leans toward being
  met, though neither difference is past two standard errors.
- **The turn of the month**: without its sessions −1 to +3, +0.057% (0.046%, t +1.23); without −5 to
  +2, +0.012% (0.051%, t +0.23). The card had estimated, from SC-008-01's published gaps and the
  fortnights' shares of those sessions (34.4% and 32.2% for −5 to +2), that leaving them out would
  move the gap by 0.001 to 0.002% a day; the second exclusion moved it by 0.012%, half the gap, the
  turn of the month's own sessions having been stronger in the new-moon fortnight than out of it.
  The third refutation is not met, but the gap does not survive the wider control whole.
- **By period**: 2005–2013 +0.029% (0.066%); 2014–2022 +0.019% (0.049%); without 2008 +0.034%
  (0.038%, t +0.91); without 2020 +0.025% (0.041%).
- **The holdout**, 2023 to 2025: −0.058% (0.071%, t −0.82), the other way.
- **The alphas**: the rule 0.64% a year after costs, 1.87% before, costs 1.24%, an appraisal ratio
  of 0.06; at a beta equal to the share of sessions held, 0.510, rather than the regression's 0.467,
  0.26% after costs: the calmer fortnight held lowered the beta and carried about three fifths of
  the alpha, as the card warned it might. The neighbours' and the delayed rule's in gate 6 above.
  The hedged return by year: 2006 +13.8 points, 2010 +9.9, 2015 +7.7; 2016 −13.8, 2008 −12.3, 2005
  −4.6.

## What was learned

- **About the theory.** On the lab's five equity funds from 2005 to 2022, the fortnight around the
  new moon earned a little more than the rest of the lunar month, in every fund and in both halves
  of the period, by about the size the sources reported for their earlier samples, but at 0.58
  standard errors, with the holdout's three years the other way. The pattern was not the sources':
  its strength lay in the week before the new moon, not around it; half of it went with the sessions
  of the turn of the month; and the new-moon fortnights were calmer and traded less, which the
  sources had found they were not. SC-027 is not refuted in this form, and the lab's data gives it
  no support it can tell from chance.
- **About the rule.** In the market half the time and switching every fortnight, the rule paid 1.24%
  a year for a gap worth about 1.9% before costs, three fifths of what was left the lower beta of
  the calmer half; its narrower neighbours, and the same rule a session late, did better, which a
  real fortnight effect would not predict.
- **About the market.** Over 2023 to 2025 the full moon's fortnight earned more than the new moon's.
- **About the lab.** The card estimated the turn of the month's effect on the gap from the shares of
  its sessions in each fortnight and the published average gaps, and the run moved it by six times
  the estimate: the turn of the month's sessions were not alike across the fortnights. A disclosure
  built from published averages is an estimate, as the runbook's step 3 now says, and here again it
  was smaller than the sample's own figure.

SC-027 is `tested-inconclusive`: its one strategy failed gates 2 to 5, and the theory is not refuted
in the one form the lab can test, the equity funds held in the fortnight around the mean new moon.
