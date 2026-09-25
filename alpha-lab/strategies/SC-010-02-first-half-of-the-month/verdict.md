# SC-010-02 — The equity funds over the first half of the trading month: verdict

**Stops at gate 2, economic edge. Refuted in this form — on the lab's equity funds from 2005 to
2022, the second week of the month, the turn's sessions removed, earned 0.046% a day less than the
second half in the three US funds, 0.92 standard errors below it, past the clause's −0.35; the first
half as a whole, in every definition, earned less than the second.** Holding the five funds over the
sessions from −1 to +9 and the bill otherwise earned an alpha of −2.31% a year over the five held
always, −1.11% before costs of 1.20% a year, an appraisal ratio of −0.21, at the bottom of the
predicted −2.5 to +3.5% and −0.35 to +0.2. The refutation reads the US-listed funds over eighteen
years; it says nothing of Ariel's years, nor of Japan, whose window the lab cannot reach.
Thresholds, version 4; the battery's figures are the notebook's, [report.ipynb](report.ipynb), and
the halves' returns, alphas before costs and the neighbours' alphas are computed apart from it, on
the same sessions. The theory is [SC-010](../../bank/SC-010-semi-month-effect.md); this card is
[SC-010-01](../SC-010-01-first-half-of-the-month/verdict.md)'s hypothesis under a new id, SC-010-01
having never run.

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 100 dates; the targets read no price, only the calendar of
   scheduled sessions; 433 decisions, once clustered, over 18.0 years in-sample, from the first
   holding on 2005-01-03.
2. **Economic edge: fails.** A Sharpe ratio of 0.122, below the 0.4 required and the benchmark's
   0.395, with an alpha of −2.31% a year; at twice the costs, 0.043 and −3.50%. Costs are 1.20% a
   year and take 0.079 of a gross Sharpe ratio of 0.201, more than a third.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.733, below 0.95; the rule beats
   30.9% of 1,000 placebos, its own weights shifted in time.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is −0.212, against 0.650 expected
   from the best of forty-six effective trials by luck: a deflated Sharpe ratio of 0.000.
5. **Stability: fails.** The blend of the variants, the base alone, fails gates 2, 3 and 4. The
   alpha is negative in all five blocks — 2005–07 (−4.34% a year), 2008–09 (−2.50%), 2010–14
   (−0.73%), 2015–19 (−2.82%), 2020–22 (−2.98%); without its best year, 2010, it is −3.59% a year.
6. **Robustness: fails.** QQQ carries 33% of the profit, more than 30%. The neighbours keep 115% of
   the base's Sharpe ratio at the median and at least 86% at ±25%, and a day's delay 133%. Their
   alphas, computed apart: the start at −2 −1.33% a year (appraisal ratio −0.12); the end at +7
   −1.70% (−0.16), at +11 −2.92% (−0.27), at +4, the turn alone, −0.33% (−0.04), at +14 −3.92%
   (−0.40); the targets a session late −1.76% (−0.16). The longer the window, the larger the loss.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.73 and an alpha of −0.58% a
   year, both above the tenth percentile of the in-sample paths (−0.62 and −10.33%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 6 as well.

## The card's refutation, clause by clause

Over the in-sample sessions from 2005-01-04, the three US funds' average daily excess return over
the 1,080 sessions whose return spans only scheduled sessions from +5 to +9, 0.0080%, less that over
the 2,373 sessions whose return spans only scheduled sessions from +10 to −2, 0.0543%: −0.0463% a
day, a standard error of 0.0503%, t −0.92.

- *A t statistic of −0.35 or below*: met. The theory is **refuted in this form**: the first half of
  the month, the turn's sessions removed, was no stronger than the second half.

**The test's power.** The card gave the clause about a 36% chance of refuting with no effect, 22% at
+0.02% a day and 12% at +0.04%; given the published figures, which it read as leaning toward the
second week by about +0.009%, about 22%, 9% and 3%. The standard error came out at 0.050%. The gap
lies inside the judged range, near its lower end, where the futures from 1993 to 2011 had put it;
1.3 standard errors below the theory's +0.02%, 1.7 below +0.04%.

Reported, not graded, as the card stated them, each gap with the standard error from the two groups'
variances, for the three US funds' average unless stated:

- **By fund**: SPY −0.035% (0.047%), QQQ −0.047% (0.052%), IWM −0.057% (0.059%), EFA −0.030%
  (0.053%), EEM −0.021% (0.069%); the five funds' average −0.038% (0.052%, t −0.73); IWM less SPY
  −0.022% (0.026%).
- **Against +10 to −11**, the only part of the second half no verdict had published, 431 sessions
  at 0.115% a day: −0.107% (0.081%, t −1.33). The card had taken the mid-month's two parts as
  alike; the later one rose more.
- **The first criterion**, the first half against the second: Hensel, Sick and Ziemba's halves,
  −1 to +9 against +10 to −2, −0.029% (0.040%, t −0.74), the five funds −0.017% (t −0.41);
  Ariel's halves, each trading month split evenly, −0.032% (0.040%, t −0.79), the five −0.022%;
  Lakonishok and Smidt's calendar halves −0.015% (0.040%, t −0.37), the five −0.024%. In every
  definition the first half earned less than the second, at or past −0.35 standard errors: the first
  criterion is met in these forms too.
- **The turn**, −1 to +4, against the second half: −0.012% (0.048%); the five funds +0.004%. **By
  session** of the second week: +5 −0.093%, +6 −0.016%, +7 −0.033%, +8 −0.121%, +9 +0.032%, each to
  about ±0.09 to ±0.12%.
- **Without the week before the turn**, the second half from +10 to −6 alone: −0.015% (0.054%, t
  −0.28). The card had put this gap at about +0.048% from the published figures, on the same
  assumption of a uniform mid-month.
- **By period**: 2005–2011, inside the futures' years, −0.008% (0.093%); 2012–2022, outside every
  source, −0.071% (0.057%, t −1.24); **without 2008**, −0.055% (0.047%, t −1.17).
- **The alphas**: the rule −2.31% a year after costs, −1.11% before, costs 1.20%, an appraisal ratio
  of −0.21; the neighbours' and the delayed rule's in gate 6 above. The hedged return by year: 2010
  +19.8 points, 2021 +5.3, 2013 +4.6; 2006 −17.0, 2014 −13.0, 2011 −12.0, 2022 −10.3.

## What was learned

- **About the theory.** On the lab's funds from 2005 to 2022, the month's second week, which the
  semi-month effect adds to the turn of the month, was weaker than the second half, not stronger, in
  every fund and most of all from 2012 to 2022, after every source's sample; and the first half as a
  whole, in Hensel, Sick and Ziemba's, Ariel's and Lakonishok and Smidt's definitions alike, earned
  less than the second. What the lab's funds kept of the month's calendar lies in the turn and in
  the week before it, which fall on both sides of the halves, as SC-008-01 found; the semi-month
  effect, Ariel's from 1963 to 1981, is refuted in this form on these funds. Lakonishok and Smidt
  had found it practically nil on the Dow from 1976 to 1986, and the futures below nil from 1993.
- **About the rule.** In the market over half the sessions, the first half, the rule lost to the
  funds held always in every block of five years, 1.11% a year before costs and 2.31% after; every
  longer window lost more, and the turn alone, the end at +4, lost least.
- **About the market.** The rule's best year against the benchmark was 2010, its worst 2006, 2014
  and
  2011. Over the holdout it lost 0.58% a year of alpha.
- **About the lab.** Two things. The card's disclosure read the published figures on the assumption
  that the unpublished sessions of the mid-month were alike; they were not, and the two gaps the
  card fixed in advance from that reading, +0.009% and +0.048%, came out at −0.046% and −0.015%. A
  disclosure that computes a gap from pooled published figures is an estimate under an assumption,
  and should say so as loudly as the figure; no code checks it. And this card's hypothesis first ran
  under SC-010-01, whose lock held a card that did not parse: the check refused it, but its refusal
  was piped into another command and did not stop the commit. The hook `tools/hooks/pre-commit` now
  runs the check on every card a commit stages and stops the commit it refuses.
- **The order of the work.** The code was copied from SC-010-01's, written and committed before this
  card's lock and after SC-010-01's; the hypothesis and the code are unchanged.

SC-010 is `tested-inconclusive`: its one strategy failed gates 2 to 6, and the theory is refuted in
the form the lab can test — on the lab's US-listed equity funds from 2005 to 2022, the first half of
the trading month, with or without the turn's sessions, earned no more than the second half.
