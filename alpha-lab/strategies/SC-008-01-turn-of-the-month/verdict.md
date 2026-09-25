# SC-008-01 — The turn of the month: verdict

**Stops at gate 2, economic edge. Not refuted, not proven: the four sessions from -1 to +3 earned a
little more than the other sessions, within noise, and the trade's costs took most of it.** Holding
the five equity funds in equal parts over sessions -1 to +3 of each turn of the month, and cash
otherwise, earns an alpha of 0.28% a year over the five held always, 1.48% before its costs of 1.20%
a year: below the prediction of 1.9 to 4.9% before costs, and an appraisal ratio of 0.03 against the
0.1 to 0.5 predicted. Before costs, the window's sessions averaged 0.034% a day more than the
others, with a standard error of 0.050%, and, at the lab's costs, the rule beats 75.1% of its
placebos: the clause's two conditions for a refutation are not met. The variant, the span from -5 to
+2, did much better — an alpha of 4.15% a year after costs, an appraisal ratio of 0.41 — but about
half of its edge came from two months, October and November 2008, and the variant is reported, not
graded. Thresholds, version 2; the battery's figures are the notebook's,
[report.ipynb](report.ipynb), and the clause's differences, the alphas before costs, the variant's
alpha, beta and figures without 2008, the blocks, the years, the funds, the sessions by place and
the window's share of the return are computed apart from it, on the same sessions and costs. The
theory is [SC-008](../../bank/SC-008-turn-of-the-month-effect.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; 217 decisions, once clustered, over 18.0 years
   in-sample, from the first holding on 2005-01-03. The rule reads a calendar derived from the
   exchange's holiday rules, not the market's dates: cut at any session, its targets are the same.
2. **Economic edge: fails.** A Sharpe ratio of 0.19, below the 0.4 required and the benchmark's
   0.39, and an alpha of 0.28% a year; at twice the costs, 0.06 and −0.92%. Costs are 1.20% a year,
   0.13 of a gross Sharpe ratio of 0.33: more than the third the gate allows.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.82; the rule beats 75.1% of 1,000
   placebos, its own weights shifted in time by a year or more, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.03, against 0.45 expected
   from the best of twenty-one effective trials by luck: a deflated Sharpe ratio of 0.04.
5. **Stability: fails.** The blend of the two variants passes gates 2 and 3 but fails gate 4 (a
   deflated Sharpe ratio of 0.26). The base's alpha is positive in three of the five blocks —
   2005–07 (1.1% a year), 2010–14 (1.9%) and 2020–22 (2.9%) — and negative in 2008–09 (−2.4%) and
   2015–19 (−2.9%); without its best year, 2010, it is −0.52% a year.
6. **Robustness: fails.** EEM carries 41% of the profit, above the 30% any one fund may. The
   neighbours keep a median of 102% of the base's Sharpe ratio and at least 79% at ±25%; a day's
   delay, which holds sessions +1 to +4, keeps 120%. The five funds form one cluster, so none is
   left out.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of −0.16 and an alpha of −4.17% a
   year, both above the tenth percentile of the in-sample paths (−0.54 and −5.76%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 6 as well.

## The card's refutation, clause by clause

Computed apart from the battery, from the in-sample sessions from 2005-01-03: the five funds'
average daily return less the bill's rate averaged 0.0622% a day over the 861 sessions of the base's
window and 0.0282% over the 3,669 others — the first session, which has no previous close, left out.
The difference is +0.0341% a day, with a standard error of 0.0501% from the daily returns (t 0.68).
The base beats 75.1% of its placebos.

- *The difference zero or less, and half of the placebos beaten or fewer*: neither is met. The
  theory is **not refuted**; short of gates 1 to 7, it is **not proven**.

Reported, not graded:

- **The variant's window**, -5 to +2: 1,508 sessions averaging 0.0970% a day against 0.0035% for the
  3,022 others, a difference of +0.0935% a day (a standard error of 0.0429%, t 2.18), above the
  0.07% a day the card gave for its sessions carrying the whole of an assumed 6% premium, since the
  funds earned 8.7% a year: about 93% of the realised premium in the window. Without 2008, +0.0573%
  (0.0391%, t 1.47). Its alpha is 4.15% a year after costs, 5.35% before, an appraisal ratio of
  0.41, at a beta of 0.32.
- **The base's alpha before costs**: 1.48% a year, the 0.28% of gate 2 with its 1.20% a year of
  costs added back.

**The test's power.** The difference's standard error came in at 0.050% a day, near the 0.045% the
reasoning estimated. The base's +0.034% lies 0.7 standard errors above zero and 1.8 below the 0.125%
that would carry the whole of an assumed 6% premium; the funds in fact earned 8.7% a year over the
bill, and all of it in the window would make the difference about 0.18% a day, 3.0 standard errors
above the result, which the run does reject. Half of the realised premium, about 0.09% a day, lies
1.1 standard errors away: the run cannot tell a vanished effect from half of one. The simulation
behind the card put a refutation at about one chance in two had the effect vanished; it did not
come.

## What was learned

- **About the theory.** Over 2005 to 2022 the base's four sessions carried 3.0% a year of the five
  funds' 8.7% a year of excess return, about a third of it in a fifth of the sessions: more than
  their share, less than the sources found before 2005, and within noise. The variant's seven
  sessions, from -5 to +2, carried 8.1% of the 8.7% in a third of the sessions, the other sessions
  earning almost nothing: the sources' pattern, earlier than their classic window, as Ilmanen
  reports the effect has shifted; Ziemba's update reads the same span on futures. That reading rests
  on the variant, reported and not graded, and on one year above all: in 2008 the variant's edge was
  +37.9 points of hedged return, about half of its 74.7 points summed over the years, and October
  and November 2008 alone gave +40.6 points: 22.4 on the window's sessions, the rebounds of 28
  October and of 21 to 26 November among them, and 18.2 in cash, out of the funds while they fell.
  Without 2008 its alpha is 2.20% a year, an appraisal ratio of 0.24, and its window's difference
  +0.057% a day (a standard error of 0.039%, t 1.47): within noise.
- **By session of the month, found after the result.** The five funds' average excess return was
  0.229% a day on session -4, 0.118% on -3, 0.123% on -2 and −0.059% on -1, then 0.215% on +1,
  0.102% on +2, −0.009% on +3 and −0.015% on +4, each measured to about ±0.08 to ±0.10%. The base's
  window took in -1 and +3, the weakest of its four sessions, and left out -4 to -2; a day's delay,
  which drops -1 and adds +4, kept 120% of its Sharpe ratio. The loss on -1 echoes Ziemba's on S&P
  500 futures from 1993; his small loss on -2 does not recur here (+0.123%). The pattern was read
  after the result and grades nothing.
- **By fund, found after the result.** Before costs, the base's difference was largest in EEM
  (+0.120% a day, a standard error of 0.067%) and about nil in the other four: SPY +0.017%, QQQ
  +0.018%, IWM −0.010%, EFA +0.025% (each about ±0.05%). EEM carried 41% of the base's profit and
  failed gate 6 on its own: the risk the reasoning named, the foreign funds adding little and the
  three US funds carrying a third each, came out reversed.
- **About the trade.** Twelve round trips a year of the whole portfolio cost 1.20% a year, most of
  the base's gross alpha: a turn-of-the-month rule on funds needs an effect well above a percent a
  year to survive its own costs, and the base's window did not have it in these years.
- **About the market.** The base's best years against the benchmark were 2010 (+14.0 points of
  hedged return), 2020 (+8.7) and 2012 (+6.1); its worst 2008 (−10.5), 2014 (−6.9) and 2016 (−5.2).
  Over the holdout, 2023 to 2025, it lost 4.17% a year of alpha, within the in-sample range.
- **About the lab.** The rule needed a calendar known in advance, which the runbook's rule against
  knowing a month's last session would otherwise forbid; derived from the exchange's holiday rules
  and checked against the market's sessions before the run — every market session scheduled, five
  unscheduled closures missing — it passed gate 1's check of look-ahead on 200 dates. The card
  judged the theory on its effect before costs and the trade on the gates, which kept the refutation
  from turning on the costs.

SC-008 is `tested-inconclusive`: the classic window from -1 to +3 earned more than the other
sessions on the lab's five equity funds only within noise and not enough to pay for trading it; the
earlier span from -5 to +2, reported and not graded, carried nearly all of the funds' return in
these years, but about half of its edge over the benchmark came from October and November 2008. The
reasons the bank gives for the effect — pay and contribution flows, their local calendars — are not
tested.
