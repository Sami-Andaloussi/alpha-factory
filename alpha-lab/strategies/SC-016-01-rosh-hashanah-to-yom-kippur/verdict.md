# SC-016-01 — The equity funds out of the market from Rosh Hashanah to Yom Kippur: verdict

**Stops at gate 4, multiple testing. Not refuted, not proven: over the eighteen windows from the
last close before Rosh Hashanah to the last close before the eve of Yom Kippur, the three US funds
earned 0.191% a day less than on their other sessions, 1.34 standard errors below zero, a gap larger
than the source's; but 2008's window, the first week of the October crash, carried most of it —
without 2008 the gap is −0.076%, 0.65 standard errors — and the funds that do not keep the holiday
fell as much as their beta to the US funds says.** Holding the five funds on every session but the
window's and the bill over them earned an alpha of 1.05% a year over the five held always, 1.15%
before costs of 0.10% a year, an appraisal ratio of 0.29 and a Sharpe ratio of 0.44, above the
predicted 0 to +0.45% before costs, −0.03 to +0.11 and 0.39 to 0.42; it passed gates 2 and 3, which
the card expected it to fail, and failed gate 4, and gate 6 on QQQ's share of the profit, as the
card expected. Thresholds, version 4; the battery's figures are the notebook's,
[report.ipynb](report.ipynb), and the window's returns, the reported gaps, the volumes, the
neighbours' alphas and the alpha at a beta equal to the share held are computed apart from it, on
the same sessions and costs. The theory is
[SC-016](../../bank/SC-016-religious-and-cultural-calendar-effects.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 87 dates; the targets read no price, only the Hebrew
   calendar's rules and the calendar of scheduled sessions; 37 decisions, once clustered, over 18.0
   years in-sample, from the first holding on 2005-01-03. The strategy's Rosh Hashanah dates are the
   published ones for every in-sample year, from 4 October 2005 to 26 September 2022.
2. **Economic edge: passes.** A Sharpe ratio of 0.439, above the 0.4 required and the benchmark's
   0.396, with an alpha of 1.05% a year; at twice the costs, 0.434 and 0.96%. Costs are 0.10% a
   year, 0.005 of a Sharpe unit.
3. **Significance: passes.** The probabilistic Sharpe ratio is 0.991; the rule beats 92.2% of 1,000
   placebos, its own weights shifted in time.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.291, against 0.651 expected
   from the best of forty-seven effective trials by luck: a deflated Sharpe ratio of 0.056.
5. **Stability: fails.** The blend of the variants, the base alone, passes gates 2 and 3 and fails
   gate 4. The battery's block alphas: 2005–07 +0.01% a year, 2008–09 +7.66%, 2010–14 −0.23%,
   2015–19 +0.01%, 2020–22 +1.28%; without its best year, 2008, the alpha is 0.30% a year.
6. **Robustness: fails.** QQQ carries 32% of the profit, more than 30%. The neighbours keep 98% of
   the base's Sharpe ratio at the median and at least 95% at ±25%, and a day's delay 102%. Their
   alphas, computed apart: the window ending at `days` 6 0.56% a year (appraisal ratio 0.19), at 10
   1.52% (0.37), at 4 0.44% (0.18), at 12 1.18% (0.27); the targets a session late 1.26% (0.35).
7. **Sealed holdout: passes.** Over 2023 to 2025, three windows, a Sharpe ratio of 1.06 and an alpha
   of 1.17% a year, both above the tenth percentile of the in-sample paths (−0.15 and −1.20%).

## Verdict

The strategy stops at gate 4, and fails gates 5 and 6 as well.

## The card's refutation, clause by clause

Over the in-sample sessions from 2005-01-04, the three US funds' average daily excess return over
the 105 sessions of the windows, −0.146%, less that over the 4,425 other sessions, 0.045%: −0.191% a
day, a standard error of 0.142%, t −1.34.

- *A t statistic of +0.35 or above*: not met. The theory is **not refuted**, and not proven.

**The test's power.** The card gave the clause about a 36% chance of refuting with no effect, 21% at
−0.06% a day and 9% at −0.13%, and about 27% at the lean of the lab's published figures, carried by
2008. The standard error came out at 0.142%, between the card's two estimates, the window's sessions
more volatile than the others (1.44% a day against 1.33%). The gap lies 0.06% a day beyond the
source's size, about 0.4 standard errors, and without 2008 inside the card's range.

Reported, not graded, as the card stated them, each gap with the standard error from the two groups'
variances, for the three US funds' average unless stated:

- **By fund**: SPY −0.153% (0.128%), QQQ −0.184% (0.138%), IWM −0.235% (0.177%), EFA −0.150%
  (0.144%), EEM −0.245% (0.207%); the five funds' average −0.194% (0.150%, t −1.29); EFA and EEM
  together −0.198% (0.171%, t −1.16), and net of their beta to the US funds' average (1.02 over all
  in-sample sessions) −0.003% (0.077%). The funds whose investors do not keep the holiday fell as
  much as their beta to the US funds says: the control cannot tell a US effect passed on at New
  York's close from a weakness shared by every market.
- **The season**: the window against the season's other sessions from 1 September to 15 October,
  −0.153% (0.157%, t −0.97); those 455 other sessions against the sessions outside the season,
  −0.043% (0.073%). Most of the window's gap is its own, not September's.
- **The two eves**, against the sessions outside the window and the eves: the last session before
  Rosh Hashanah −0.608% (0.488%, t −1.25, 18 sessions); the eve of Yom Kippur, in the fifteen years
  it is a weekday, −0.249% (0.368%); both −0.445% (0.311%, t −1.43). Weak, not the pre-holiday
  strength Chan and others found before cultural holidays in Asia.
- **The bank's form**: the window's 30 sessions on Rosh Hashanah's two days −0.167% (0.207%); its 75
  later sessions −0.200% (0.181%). No improvement toward Yom Kippur: the weakness, where there is
  one, lasts through the window, the source's form.
- **Window by window**, the US funds' return over the window less the outside mean over as many
  sessions: 2005 −5.07%, 2006 +1.19, 2007 +2.80, 2008 −13.40, 2009 −2.57, 2010 +2.49, 2011 +1.27,
  2012 −1.03, 2013 +1.68, 2014 −2.96, 2015 +0.09, 2016 −0.13, 2017 +0.53, 2018 −0.26, 2019 −0.83,
  2020 −1.15, 2021 −2.65, 2022 −0.04: eleven of eighteen below zero, a mean of −1.11% and a standard
  deviation of 3.67% across windows.
- **By period**: 2005–2011 −0.315% (0.317%, t −0.99); 2012–2022, outside every source, −0.115%
  (0.123%, t −0.93); **without 2008** −0.076% (0.116%, t −0.65), the five funds −0.077% (0.114%).
- **After the window**, from the session after it to the year's last: +0.039% a day above the other
  sessions (0.047%, 1,180 sessions), about the funds' drift, as the card expected of the source's
  +1.99%.
- **Volume**: the mean log of SPY's, QQQ's and IWM's traded volume over the window less that over
  the season's other sessions of the same year, the third Friday and last session of September left
  out, +0.025 (0.044, t +0.57) over the eighteen years, ten of them above zero: no sign that the
  funds traded less over the window.
- **The alphas**: the rule 1.05% a year after costs, 1.15% before, costs 0.10%, an appraisal ratio
  of 0.29; at a beta equal to the share of sessions held, 0.977, rather than the regression's 0.972,
  1.01%: being out over 2008's week lowered the beta by little. The neighbours' and the delayed
  rule's in gate 6 above. The hedged return by year: 2008 +12.0 points, 2005 +4.5, 2014 +3.6; 2007
  −3.3, 2010 −2.5, 2013 −2.2.

## What was learned

- **About the theory.** On the lab's funds from 2005 to 2022, the days from Rosh Hashanah to Yom
  Kippur were weak, in every fund and in both halves of the period, by more than the source's
  retelling of the Dow since 1915; but one window, 2008's, the week in which the October crash
  began, carried most of the gap, eleven windows of eighteen fell short of the others, and without
  2008 the gap is 0.65 standard errors from nothing. What would set the theory apart — a weakness in
  the markets whose investors keep the holiday and not in the others, a change in participation — is
  not there: EFA and EEM fell as their beta says, the funds' volume did not fall, and the eves were
  weak where Chan and others' cultural holidays were strong. SC-016 is not refuted in the source's
  form, and the lab's data gives its mechanism no support.
- **About the rule.** Out of the market 2.3% of the time, the rule beat the funds held always by
  about 1% a year, nearly nine tenths of it in 2008 and 2005; it passed the edge and significance
  gates on those two years and failed the deflation of forty-seven trials. Every neighbour kept a
  positive alpha, the later ends more than the earlier.
- **About the market.** The holdout's three windows added 1.17% a year of alpha.
- **About the lab.** The card expected the rule to fail gate 2 or 3; a single crash week inside an
  18-window rule was enough to pass both, as the disclosure of 2008's weight warned, and gate 4, not
  the card's expectation, is what stopped it. The card's first draft ended the window on Yom
  Kippur's own eve; the audit found the source's words, "eight days later", and its dated years
  agreeing on the session before, and the base moved before the lock.
- **The order of the work.** The reasoning and card were drafted in the scratch folder while
  SC-013's and SC-015's chains ran, before the theory's pick, and moved into the folder at it; the
  code was written after the lock.

SC-016 is `tested-inconclusive`: its one strategy failed gates 4 to 6, and the theory is not refuted
in the one form the lab can test, US equity funds out of the market over Rosh Hashanah and Yom
Kippur; its Ramadan and Golden Week patterns are out of the lab's reach.
