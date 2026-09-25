# SC-014-01 — The equity funds over the session before each market holiday: verdict

**Stops at gate 2, economic edge. Not refuted, not proven: on the session before a market holiday,
the three US funds earned 0.123% a day more than on the other sessions, above the predicted 0 to
0.08%, 1.50 standard errors from zero; the foreign funds, predicted at about nil, rose more still,
and the third session before rose more than the last, in the years after the sources' samples as
well.** Holding the five funds over each pre-holiday session and the bill otherwise earned an alpha
of +0.55% a year over the five held always, +1.45% before costs of 0.90% a year, an appraisal ratio
of 0.19 (0.49 before costs), above the predicted 0 to 0.45% and 0 to 0.11; its Sharpe ratio, 0.24,
fell short of 0.4, as the card expected. Thresholds, version 4; the battery's figures are the
notebook's, [report.ipynb](report.ipynb), and the sessions' returns, alphas before costs and the
neighbour's and variant's alphas are computed apart from it, on the same sessions. The theory is
[SC-014](../../bank/SC-014-pre-holiday-effect.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; the targets read no price, only the calendar of
   scheduled sessions; 161 decisions, once clustered, over 17.9 years in-sample, from the first
   holding on 2005-01-14.
2. **Economic edge: fails.** A Sharpe ratio of 0.241, below the 0.4 required and the benchmark's
   0.404, with an alpha of +0.55% a year; at twice the costs, −0.062 and −0.34%. Costs are 0.90% a
   year and take 0.303 of a gross Sharpe ratio of 0.541, more than a third.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.850, below 0.95; the rule beats
   94.7% of 1,000 placebos, its own weights shifted in time, more than the 90% required.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.189, against 0.651 expected
   from the best of forty-four effective trials by luck: a deflated Sharpe ratio of 0.024.
5. **Stability: fails.** The blend of the base and the variant passes gate 3 but fails gate 2 — at
   twice the costs a Sharpe ratio of 0.064 and an alpha of −0.05%, costs taking 0.379 of a gross
   Sharpe ratio of 0.817 — and gate 4, a deflated Sharpe ratio of 0.081. The base's alpha is
   positive in three blocks of five — 2005–07 (+0.52% a year), 2008–09 (+4.09%), 2020–22 (+0.51%) —
   and negative in 2010–14 (−0.19%) and 2015–19 (−0.18%); without its best year, 2008, it is +0.20%
   a year.
6. **Robustness: fails.** The neighbour, the second session before the holiday, keeps 38% of the
   base's Sharpe ratio at ±25% and ±50%, and a day's delay, the session after the holiday, −81%.
   EEM carries 29.7% of the profit, just under 30%. Their alphas, computed apart: the second session
   before +0.10% a year (appraisal ratio 0.03; +0.99% before costs); the targets a session late
   −1.09% (−0.27; −0.20% before costs).
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.73 and an alpha of +1.07% a
   year, both above the tenth percentile of the in-sample paths (−0.58 and −1.70%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 6 as well.

## The card's refutation, clause by clause

Over the in-sample sessions from 2005-01-14, the three US funds' average daily excess return over
the 161 sessions whose return spans the last scheduled session before a weekday holiday, 0.1595%,
less that over the 4,361 others, 0.0368%: +0.1227% a day, a standard error of 0.0816%, t +1.50.

- *A t statistic of −0.35 or below*: not met. The theory is **not refuted**; short of gates 1 to 7,
  it is **not proven**.

**The test's power.** The card gave the clause about a 36% chance of refuting with no effect, 21% at
+0.05% a day and 10% at +0.10%, with a standard error of about 0.107%, nearer 0.09 to 0.10% if the
sessions before holidays were calmer, as every source found; they were — a daily standard deviation
of 1.00% for the US funds' average against 1.33% over all sessions — and the standard error came out
at 0.082%. The difference lies above the prediction, 1.5 standard errors from zero: the run cannot
tell it from none, nor from an effect a third of its size.

Reported, not graded, as the card stated them, each gap with the standard error from the two groups'
variances, for the three US funds' average unless stated:

- **By fund**: SPY +0.100% (0.075%, t +1.32), QQQ +0.101% (0.082%), IWM +0.168% (0.099%, t +1.69),
  EFA +0.121% (0.077%, t +1.57), EEM +0.257% (0.109%, t +2.36); the five funds' average +0.149%
  (0.080%, t +1.86); IWM less SPY +0.068% (0.044%, t +1.54).
- **Around the holiday**, each session against the sessions outside its group: −3 +0.233% (0.099%,
  t +2.36), the five funds +0.227% (t +2.31), IWM +0.304% (t +2.67); −2 +0.073% (0.091%), the five
  +0.102%, IWM +0.160%; +1 +0.029% (0.107%), the five −0.025%, IWM −0.055%; +2 −0.045% (0.113%),
  the five −0.045%, IWM −0.123%. **The third session before over 2012–2022**, outside Ziemba's
  sample: +0.218% (0.097%, t +2.24), the five +0.212% (t +2.40), IWM +0.290% (t +2.58), over 99
  sessions.
- **Before Columbus Day and Veterans Day**, on which the exchange stays open, 31 sessions, all
  eighteen of the first on Fridays: +0.193% (0.277%) above the sessions that precede no holiday of
  either kind; the pre-holiday sessions less them −0.069% (0.288%).
- **Inside SC-008-01's span from −5 to +2**, the 97 pre-holiday sessions against the span's 1,410
  others: +0.039% (0.108%, t +0.36); **outside it**, the 64 against the 2,951 others: +0.200%
  (0.127%, t +1.57). **The pre-holiday Fridays**, 91, against the 816 other Fridays: +0.051%
  (0.098%, t +0.52).
- **Without the pre-holiday sessions of Christmas and New Year's Day**, 127 sessions: +0.173%
  (0.095%, t +1.82). **By holiday**, eighteen sessions each unless stated: Good Friday +0.597%
  (0.297%), Thanksgiving +0.352% (0.338%), Memorial Day +0.168%, Independence Day +0.144%,
  Washington's Birthday +0.069%, Martin Luther King Jr. Day +0.022%, Christmas +0.008%, New Year's
  Day −0.148% (sixteen), Labor Day −0.169%, each to about ±0.15 to ±0.34%; Juneteenth's one session,
  2022-06-17, +0.73%.
- **By period**: 2005–2011, inside Ziemba's sample, +0.126% (0.168%), 62 sessions; 2012–2022,
  outside it, +0.121% (0.082%, t +1.48), 99 sessions. The five funds +0.216% and +0.107%; IWM
  +0.128% and +0.192% (0.096%, t +2.01).
- **The alphas**: the base +0.55% a year after costs, +1.45% before, costs 0.90%, an appraisal ratio
  of 0.19 and 0.49; the variant, the third session before, +1.13% and +2.02%, costs 0.89%, an
  appraisal ratio of 0.31 and 0.55, a Sharpe ratio of 0.375 against the benchmark's 0.404, 0.132 at
  twice the costs: it fails gate 2 as the card expected, narrowly; the neighbour's and the delayed
  rule's in gate 6 above.

## What was learned

- **About the theory.** On the lab's funds from 2005 to 2022, the session before a market holiday
  rose more than the other sessions, about 0.12% a day in the US funds and 0.15% in the five, at the
  top of what the futures showed to 2010 and above the card's judgment; within noise, 1.5 standard
  errors in the graded form. The bank's shape held in part: larger in the small caps than in the S&P
  500 (IWM less SPY +0.07%, t 1.54), and not carried by the turn of the month — inside SC-008-01's
  span the pre-holiday sessions added little to its already strong sessions, outside it they stood
  0.20% a day above the rest. It did not hold on Fridays, where the pre-holiday sessions beat the
  other Fridays by only 0.05%: from the published figures, the 70 pre-holiday sessions that are not
  Fridays averaged about 0.29%, the eves of Good Friday and Thanksgiving foremost — found after the
  result, it grades nothing. The third session before, Ziemba's, rose 0.23% a day more than the
  others, and 0.22% over 2012–2022, after all the sources' samples: the strongest figure of the run,
  reported and not graded, and the best of the five sessions read. No reversal after the holiday can
  be measured (+1 +0.03%, a standard error of 0.107%), where a close lifted at the ask, the third
  criterion's artefact, would show one; the second criterion cannot be read, the 31 sessions before
  Columbus Day and Veterans Day scattering too widely.
- **About the rule.** Nine sessions a year in the market earned 1.45% a year before costs, three
  times the top of the prediction, and 0.55% after 0.90% of costs; the variant 2.02% and 1.13%, a
  Sharpe ratio of 0.375, just short of gate 2. The neighbour, the second session before, earned
  0.99% before costs, the session after the holiday nothing. The rule's volatility, 3.0% a year, was
  below the 4.1% the card computed from ordinary sessions. The holdout earned 1.07% a year of alpha.
- **About the market.** The foreign funds rose as much as the US ones, EEM most of all, against the
  card's judgment that their open home markets would leave them flat: EFA and EEM are listed in New
  York, and a US holiday closes them too; their close-to-close return on the eve is a New York
  session's. The largest pre-holiday sessions were rebounds after the crash, the eve of Thanksgiving
  2008 (+4.55% for the five funds) and of Good Friday 2009 (+3.99%) — the card had named the risk of
  a crash on such an eve; the worst, 15 January 2016 (−2.89%). The rule's best year against the
  benchmark was 2008.
- **About the lab.** Two of the card's claims were corrected by the logic audit and its closing
  check against the raw texts: a regression the Zacks and Ziemba text presents as the cash market's
  is Ziemba's own on the Nikkei, and a Japanese figure for the pre-holiday Fridays, taken from the
  first audit's reading, had been written as all pre-holidays'. A figure retold in a book can be
  another market's or another subset's; the audit reads the sources, and no code does. And the
  card's judgment, which the audit shared, that the foreign funds would show nothing reasoned from
  the underlying markets rather than from where the funds trade; no code checks a card's reasoning
  about where an asset is priced, and here neither the card nor the audit caught it — the run did.
- **The order of the work.** The card was locked before any code was written; the code followed the
  lock by a minute.

SC-014 is `tested-inconclusive`: on the lab's equity funds from 2005 to 2022, the session before a
market holiday beat the other sessions by about the size the recent sources found, in the US funds
and more in the foreign ones, and the third session before by more, within noise in the graded form;
the rule fails gate 2 on costs.
