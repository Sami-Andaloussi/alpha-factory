# TM-028-01 — The trend of the quiet sessions: verdict

**Stops at gate 3, significance. Not proven, not refuted, on either side: the fund-months with the
quiet sessions' trend up earned 1.25% a year less over the bill than those with the loud sessions'
trend up (standard error 3.91%, t −0.32), short of the −0.35 that refutes TM-028 in this form and of
the +0.35 that refutes TM-027's index form.** Holding each of the fourteen US equity funds in an
equal share while its negative volume index stands above its one-year average, its share in cash
otherwise, earned an alpha of 1.00% a year over the funds held always in equal parts, a Sharpe ratio
of 0.52 against 0.49, inside the predicted −1 to +1.5%; but it beats 84.3% of its placebos, its own
weights shifted in time, where 90% are needed. Thresholds, version 4; the battery's figures are the
notebook's, [report.ipynb](report.ipynb), and the clause, the reported measures and the neighbours'
alphas are computed apart from it, on the same closes, volumes and costs. The theory is
[TM-028](../../bank/TM-028-low-turnover-momentum.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates, the volumes moved with the prices; the memory of
   256 sessions holds on 100; 63 decisions, once clustered, over 18.0 years in-sample.
2. **Economic edge: passes.** A Sharpe ratio of 0.518 against the benchmark's 0.492, an alpha of
   1.00% a year; at twice the costs, 0.516 and 0.98%. Costs are 0.03% a year: the rule steps out of
   a fund in about one fund-month in eleven.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.994, but the rule beats 84.3% of
   1,000 placebos, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.166, against 0.62 expected
   from the best of fifty-seven effective trials by luck: a deflated Sharpe ratio of 0.029.
5. **Stability: fails.** The blend of the two variants passes gates 2 and 3 and fails gate 4. The
   block alphas: 2005–07 +0.34% a year, 2008–09 −6.67%, 2010–14 −0.24%, 2015–19 −0.14%, 2020–22
   −1.89%; one positive block of five, while the whole sample's alpha, with one beta over all the
   blocks, is positive. Without its best year, 2013, the alpha is 0.80% a year.
6. **Robustness: passes.** The neighbours keep a median of 101% of the base's Sharpe ratio and at
   least 98.7% at ±25%; without the sector funds, the worst cluster to lose, 96% remains; the
   largest share of the profit is XLK's, 11.4%; a day's delay keeps 101%. The neighbours' alphas,
   computed apart: `window` 191 1.49% a year (appraisal ratio 0.23), 319 0.87% (0.15), 127 1.29%
   (0.20), 383 0.66% (0.12); the targets a session late 1.12% (0.19); the variant, SPY's volume
   deciding, 1.14% (0.21).
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.80 and an alpha of −1.19% a
   year, both above the tenth percentile of the in-sample paths (−0.15 and −2.43%).

## Verdict

The strategy stops at gate 3, and fails gates 4 and 5 as well.

## The card's refutation

Over the 203 months from February 2006 to December 2022, each fund-month from the close of a
target's session to the close of the next, the last ending at the close of 2022-12-30: 2,541
fund-months with both of the fund's indices defined, 203 for each of the twelve funds trading from
the start, 63 for XLRE and 42 for XLC, as the card counted. The quiet index was up in 2,307 of them,
the loud index in 627. Stacked, regressed on an indicator of the quiet set and one constant for each
fund, the standard errors clustered by month (203 clusters):

- **The quiet sessions' trend against the loud sessions'**: −1.25% a year, a standard error of
  3.91%, t −0.32. *A t statistic of −0.35 or below*: not met. **TM-028 not refuted, not proven** in
  this form: the difference lies below the predicted +0.5 to +5%, 0.32 standard errors below zero.
- **TM-027's index form**, the same statistic read from the other side: *+0.35 or above*: not met.
  **Not refuted, not proven.**

**The test's power.** The card judged the standard error at about 2 to 4% a year, up to 5%; it came
out at 3.91%. At that error the clause refutes TM-028 about 36% of the time with no effect and about
15% at +2.75% a year, the middle of the predicted range; it refutes TM-027's index form about 36% of
the time with no effect. The estimate lies 1.02 standard errors below the predicted middle and 0.45
below the end of the range nearest zero: the prediction is not excluded, and neither is no effect,
nor an effect of the same size the other way.

**What the indices did.** The two indices do not split the sessions' returns evenly: each fund's
sessions were about half quiet and half loud (49.8% to 51.6% quiet, one equal volume in 18 years,
XLY's), but the quiet index was up in 90.8% of the fund-months and the loud index in 24.7%, the
trend on every session in 75.9%. Over these years the funds rose on their quiet sessions and fell on
their loud ones, so that the quiet index trends up almost always and the loud index mostly down. The
clause's contrast rests on the 75.2% of fund-months in which the two disagree, 70.7% with the quiet
index alone up and 4.6% with the loud index alone up: the rule is out of a fund only in the 9.2% of
fund-months with its quiet index down.

Reported, not graded, as the card stated them:

- **The variant**, SPY's volume deciding every fund's quiet sessions: −1.00% a year (6.09%, t
  −0.16), 2,432 fund-months with the quiet index up and 266 with the loud index up.
- **The bear side**, each index up less not up, one constant for each fund: the quiet index −4.82%
  a year (19.79%, t −0.24), over 234 fund-months not up; the loud index +1.44% (5.12%, t +0.28); the
  difference −6.26% (19.69%, t −0.32). Fosback's reading, the quiet trend the better sign of a bull
  market and the loud trend of a bear, is not visible: both spreads are within a third of a standard
  error of zero.
- **The trend on every session**, the fund's close above its average over the window: up less not
  up −1.19% a year (13.10%, t −0.09); the quiet set against it −0.16% (2.36%, t −0.07), the loud set
  +1.12% (3.09%, t +0.36).
- **By group**: SPY, QQQ and IWM +0.53% a year (8.17%, t +0.06), 570 and 78 fund-months; the sector
  funds −1.54% (3.63%, t −0.42), 1,737 and 549.
- **Without IWM's 29 fund-months whose indices read one of its seven listed bars**: −1.06% (3.74%, t
  −0.28).
- **By period**: 2006–2013 −4.19% (5.07%, t −0.83), 2014–2022 +2.53% (5.26%, t +0.48); without 2008
  and 2009 +3.86% (3.56%, t +1.08), 179 months. The sign turned between the halves of the sample;
  the crisis years carried the negative estimate.
- **The holdout**, 2023 to 2025: +8.10% a year (8.05%, t +1.01), 490 and 82 fund-months over 36
  months, the prediction's sign.
- **The alphas**: the base 1.00% a year after costs, 1.03% before, costs 0.03%; the neighbours', the
  variant's and the delayed rule's in gate 6 above. The hedged return by year: 2013 +5.0 points,
  2021 +4.8, 2019 +3.9, 2010 +3.8; 2009 −13.6, 2022 −2.6, 2020 −2.1.

## What was learned

- **About the theory.** On the lab's fourteen US equity funds from 2006 to 2022, the trend a fund
  makes on its quiet sessions was no better a sign of its next month than the trend it makes on its
  loud sessions: 1.25% a year worse in the point estimate, a third of a standard error. The one
  index form of TM-028 the lab can read is neither refuted nor proven, and neither is TM-027's, read
  from the other side; the stock forms of both, by each stock's own turnover, remain unread. The
  estimate was negative over 2006–2013 and in 2008 and 2009, positive after and in the holdout.
  Fosback's figures describe 1941 to 1975 on the market's volume; Aronson's test on 1980 to 2005
  found nothing either.
- **About the rule.** It held the funds nine fund-months in ten: its quiet index, made of the
  sessions of falling volume, on which the funds mostly rose, stood above its average almost always,
  and the rule stepped into cash in a fund only in the few months its quiet sessions fell. Its alpha
  of 1.00% a year and its Sharpe ratio of 0.52 came from being out of a fund in a few bad months,
  2008 among them (+3.3 points against the funds' market), less 2009, whose rebound it partly missed
  (−13.6, its worst year); its placebos, the same weights at other dates, did as well 16% of the
  time; four of five blocks gave a negative alpha.
- **About the lab.** The theory was first drafted not testable; its reader found a form with a sign
  that only the funds' volumes would open, which the snapshot held and the lab did not pass. The lab
  now passes them (`market.signal_volumes`), gate 1 checking them as the prices, and a card that
  reads none keeps every figure it had, which the independent audit of the change confirmed on four
  earlier cards. The volume check it added lists seven of IWM's bars as Yahoo misprints; the card
  kept them and reported the clause without them, which changed little.

TM-028 is `tested-inconclusive`: its one strategy failed gates 3 to 5, and its index form is not
proven and not refuted. A second trial, the market's volume or another window, would be chosen from
this result: the variant and the neighbours are reported above, and none departs from the base.
