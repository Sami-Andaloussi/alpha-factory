# SC-009-01 — The equity funds out of the market over the month-end dash for cash: verdict

**Stops at gate 4, multiple testing. Not refuted, not proven: over sessions −10 to −6 of each month,
the three US funds earned 0.065% a day less than in the middle of the month, inside the predicted
−0.02 to −0.07%, 1.18 standard errors from zero; but most of the gap came from 2005 to 2011, 2008
above all, and the turn that should absorb the pressure did not beat the middle of the month in the
US funds.** Holding the five funds on every session but those and the bill over them earned an alpha
of +2.02% a year over the five held always, +3.23% before costs of 1.20% a year, an appraisal ratio
of 0.22, a Sharpe ratio of 0.45, inside the predicted 2.4 to 4.2%, 0.13 to 0.32 and 0.41 to 0.50; it
passed gates 2 and 3 and failed gate 4, as the card expected. Thresholds, version 4; the battery's
figures are the notebook's, [report.ipynb](report.ipynb), and the sessions' returns, the bill's
yield, alphas before costs and the neighbours' alphas are computed apart from it, on the same
sessions. The theory is [SC-009](../../bank/SC-009-payday-hypothesis-dash-for-cash.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 100 dates; the targets read no price, only the calendar of
   scheduled sessions; 433 decisions, once clustered, over 18.0 years in-sample, from the first
   holding on 2005-01-03.
2. **Economic edge: passes.** A Sharpe ratio of 0.455 against the benchmark's 0.396, an alpha of
   +2.02% a year; at twice the costs, 0.392 and +0.83%. Costs are 1.20% a year, 0.062 of a gross
   Sharpe ratio of 0.517.
3. **Significance: passes.** The probabilistic Sharpe ratio is 0.990; the rule beats 94.8% of 1,000
   placebos, its own weights shifted in time.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.224, against 0.650 expected
   from the best of forty-five effective trials by luck: a deflated Sharpe ratio of 0.035.
5. **Stability: fails.** The blend of the variants, the base alone, fails gate 4. The alpha is
   positive in three blocks of five — 2008–09 (+17.03% a year), 2010–14 (+0.47%), 2020–22 (+4.36%)
   — and negative in 2005–07 (−2.77%) and 2015–19 (−0.90%); without its best year, 2008, it is
   +0.46% a year.
6. **Robustness: passes.** The neighbours keep 70% of the base's Sharpe ratio at the median and at
   least 61% at ±25%, and a day's delay 101%; the largest share of the profit is QQQ's, 27.7%. Their
   alphas, computed apart, tell otherwise: the window ending at −4 −0.39% a year (appraisal ratio
   −0.04), at −8 −1.33% (−0.15), at −3 −1.14% (−0.13), at −9 −1.64% (−0.18); four sessions long
   +1.05% (0.13), six −0.54% (−0.06), two +1.25% (0.20), eight +0.47% (0.05); the targets a session
   late, out over −9 to −5, +2.07% (0.23). The gate's ratios of Sharpe ratios read the benchmark the
   rule holds most of the time; the neighbours' alphas are the rule's own.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 1.03 and an alpha of +1.86% a
   year, both above the tenth percentile of the in-sample paths (−0.28 and −4.80%).

## Verdict

The strategy stops at gate 4, and fails gate 5 as well.

## The card's refutation, clause by clause

Over the in-sample sessions from 2005-01-04, the three US funds' average daily excess return over
the 1,080 sessions whose return spans a scheduled session from −10 to −6, −0.0138%, less that over
the 1,295 mid-month sessions, from the sixth scheduled session to the eleventh-last, 0.0515%:
−0.0652% a day, a standard error of 0.0554%, t −1.18.

- *A t statistic of +0.35 or above*: not met. The theory is **not refuted**; short of gates 1 to 7,
  it is **not proven**.

**The test's power.** The card gave the clause about a 36% chance of refuting with no effect (42%
with the sessions before holidays placed as they are), 24% at −0.02% a day and 5% at −0.07%, with a
standard error of about 0.055%; it came out at 0.055%. The gap lies at the strong end of the
prediction, 1.2 standard errors from zero: the run cannot tell it from none.

Reported, not graded, as the card stated them, each gap against the mid-month sessions with the
standard error from the two groups' variances, for the three US funds' average unless stated:

- **By fund**: SPY −0.071% (0.052%, t −1.37), QQQ −0.076% (0.057%, t −1.34), IWM −0.049% (0.065%),
  EFA −0.042% (0.058%), EEM −0.062% (0.076%); the five funds' average −0.060% (0.058%, t −1.04); IWM
  less SPY +0.022% (0.029%).
- **By session**, the US funds: −10 −0.080%, −9 −0.024%, −8 −0.006%, −7 −0.117%, −6 −0.099%, −5
  −0.091%, −4 +0.161%, −3 +0.069%, −2 +0.090%, −1 −0.142%, +1 +0.117%, +2 +0.032%, +3 −0.023%, each
  to about ±0.06 to ±0.09%; the five funds' much the same (−4 +0.191%, +1 +0.178%). **The summed
  gaps from −10 to +3**, pressure and absorption: −0.113% (0.606%) for the US funds, +0.064%
  (0.628%) for the five. **The turn from −1 to +3**: −0.004% (0.059%) for the US funds, +0.024%
  (0.061%) for the five.
- **The other readings**: −8 to −4 −0.030% (0.056%, t −0.55); −9 to −5 −0.068% (0.055%, t −1.23).
- **The Treasury funds**, over the window: SHY +0.000% (0.004%), IEF +0.004% (0.017%), TLT +0.059%
  (0.038%, t +1.55) — the long bonds rose while the equities fell. **The bill's yield**, ^IRX's
  daily change: +0.05 basis points a day over the window against the mid-month (0.22), and by
  session within ±0.8 basis points, no pattern of a cash need before the month's end.
- **The months that end a quarter**: −0.068% (0.103%) against their own mid-month sessions; the
  other months −0.064% (0.065%).
- **By period**: 2005–2011, inside Ziemba's panels, −0.127% (0.103%, t −1.23); 2012–2022, outside
  every source, −0.026% (0.063%, t −0.42); **without 2008**, −0.031% (0.052%, t −0.60). The five
  funds −0.106%, −0.031% and −0.024%.
- **The alphas**: the rule +2.02% a year after costs, +3.23% before, costs 1.20%, an appraisal ratio
  of 0.22; the neighbours' and the delayed rule's in gate 6 above. The hedged return by year: 2008
  +29.1 points, 2014 −11.5 and 2016 −11.6, 2007 −10.1.

## What was learned

- **About the theory.** On the lab's funds from 2005 to 2022, the week before the month's last week
  was weaker than the middle of the month, by about the size the index futures showed to 2011 and in
  every fund; within noise. It did not take the whole shape the dash for cash gives it. The weakness
  fell mostly in 2005 to 2011, 2008 above all, and was a fifth of that size from 2012 to 2022,
  outside every source, within noise of nothing; it was no larger in the months that end a quarter.
  The pressure was not absorbed at the turn in the US funds: sessions −4 to −2 rose, as SC-008-01
  had found, −1 fell, and the turn from −1 to +3 earned what the middle of the month earned; summed
  from −10 to +3 the month's end came to nothing against its middle. The cost of capital did not
  move: the bill's yield showed no rise before the month's end, as McConnell and Xu found, and the
  long Treasury fund rose over the window rather than being sold.
- **About the rule.** Sitting out five sessions a month earned 3.23% a year before costs, as the
  card computed, most of it the hedge's charge of only its share of a premium earned elsewhere, and
  2008; without 2008 its alpha was 0.46% a year. Every neighbour that moved the window's end lost
  after costs; the delayed rule, out over −9 to −5, the long records' place, did as well as the
  base.
- **About the market.** The rule's best year was 2008, its window taking in the crash's falls; its
  worst, 2014, 2016 and 2007. The holdout earned 1.86% a year of alpha.
- **About the lab.** The card first said that no source in the library gave the window's size; the
  logic audit found the library's tables by session, in Ziemba's and McConnell and Xu's books, which
  the card had read, and in Lakonishok and Smidt's and Hensel, Sick and Ziemba's, and the card was
  rewritten on them before the lock. A card that reads a calendar effect's sessions must read the
  sources' tables by session before it says the sources are silent; no code checks it, and the audit
  is where it is caught. The window itself was moved from a first reading while a published figure
  on the lab's funds was known: the card discloses it, the first reading became a neighbour and was
  reported: −0.030% a day, half the base's gap, the difference mostly session −4, which the
  published figures had shown strong. Gate 6 passed on ratios of Sharpe ratios while every neighbour
  moving the window's end lost: for a rule in the market most of the time the ratios read the
  benchmark, as recorded before; the neighbours' alphas are written in the verdict, and no code
  judges them.
- **The order of the work.** The card was locked before any code was written.

SC-009 is `tested-inconclusive`: on the lab's equity funds from 2005 to 2022, the week before the
month's last week was weaker than the middle of the month within noise, mostly before 2012, with no
absorption at the turn in the US funds and no move of the bill's yield; the rule's edge failed the
lab's test of multiple trials.
