# SC-007-01 — The equity funds over the Santa Claus window, cash otherwise: verdict

**Stops at gate 2, economic edge. Not refuted, not proven: over December's last five sessions and
January's first two, the five equity funds earned 0.097% a day more than on the other sessions,
inside the predicted 0.04 to 0.16%, 1.05 standard errors from zero; but the rise came from the
foreign funds, not from the US market the claim is about, and it was no larger than at the other
months' same sessions.** Holding the five over the window and the bill otherwise earned an alpha of
+0.66% a year over the five held always, +0.76% before costs of 0.10% a year, an appraisal ratio of
0.25, inside the predicted 0.3 to 1.1% and 0.05 to 0.25; its Sharpe ratio, 0.30, fell short of 0.4,
as the card expected. Thresholds, version 4; the battery's figures are the notebook's,
[report.ipynb](report.ipynb), and the window's returns, alphas before costs and the neighbours'
alphas are computed apart from it, on the same sessions. The theory is
[SC-007](../../bank/SC-007-santa-claus-rally.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 87 dates; the targets read no price, only the calendar of
   scheduled sessions; 36 decisions, once clustered, over 18.0 years in-sample, from the first
   holding on 2005-01-03.
2. **Economic edge: fails.** A Sharpe ratio of 0.300, below the 0.4 required and the benchmark's
   0.398, with an alpha of +0.66% a year; at twice the costs, 0.261 and +0.56%. Costs are 0.10% a
   year.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.916, below 0.95; the rule beats
   85.0% of 1,000 placebos, its own weights shifted in time, fewer than the 90% required.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.254, against 0.652 expected
   from the best of forty-two effective trials by luck: a deflated Sharpe ratio of 0.040.
5. **Stability: fails.** The blend of the variants, the base alone, fails gates 2, 3 and 4. The
   alpha is positive in three blocks of five — 2008–09 (+3.24% a year), 2010–14 (+1.13%), 2020–22
   (+0.87%) — and negative in 2005–07 (−0.58%) and 2015–19 (−0.51%); without its best year, 2018, it
   is +0.42% a year.
6. **Robustness: fails.** EEM carries 42% of the profit, more than 30%. The neighbours keep 94% of
   the base's Sharpe ratio at the median and at least 78% at ±25%, and a day's delay 77%. Their
   alphas, computed apart: four December sessions +0.53% a year (appraisal ratio 0.21), six +0.73%
   (0.26), two +0.39% (0.18), eight +1.28% (0.41); one January session +0.93% (0.38), three +0.53%
   (0.18); the targets a session late +0.51% (0.18).
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of −0.29 and an alpha of −0.74% a
   year, both above the tenth percentile of the in-sample paths (−0.62 and −1.22%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 6 as well.

## The card's refutation, clause by clause

Over the in-sample sessions from 2005-01-04, the five funds' average daily excess return over the
124 sessions whose return spans a scheduled session of the window, 0.1289%, less that over the 4,406
others, 0.0320%: +0.0969% a day, a standard error of 0.0919%, t +1.05.

- *A t statistic of −0.35 or below*: not met. The theory is **not refuted**; short of gates 1 to 7,
  it is **not proven**.

**The test's power.** The card gave the clause about a 36% chance of refuting with no effect, 12% at
+0.10% a day and 5% at +0.16%, with a standard error of about 0.13%, and, from the lab's published
figures, a 12 to 22% chance as the lab stood; the standard error came out at 0.092%. The difference
lies inside the prediction and within noise of zero.

Reported, not graded, as the card stated them, each gap with the standard error from the two groups'
variances:

- **Year by year**, the window's excess return over the seventeen full windows, 2005–06 to 2021–22:
  +1.06% a year on average (0.61%), thirteen years positive — 2005 +1.85%, 2006 +0.83% (six
  sessions), 2007 −2.35%, 2008 +7.81%, 2009 +2.49%, 2010 +1.35%, 2011 +1.89%, 2012 +2.49%, 2013
  −0.40%, 2014 −2.80%, 2015 −3.41%, 2016 +1.84%, 2017 +1.94%, 2018 +1.37%, 2019 +0.23%, 2020 +1.81%,
  2021 +1.01% — against 58.7% of all 4,524 spans of seven in-sample returns positive: 76% against
  59%, within the ±12 points a share from seventeen years carries.
- **By fund**, the window's daily gap: SPY +0.064% (0.090%, t +0.71), QQQ +0.032% (0.110%), IWM
  +0.006% (0.105%), EFA +0.131% (0.087%, t +1.51), EEM +0.252% (0.116%, t +2.18); the three US
  funds' average +0.034% (0.098%, t +0.35); IWM less SPY −0.058% (0.047%, t −1.22). Year by year,
  SPY +0.76% (thirteen of seventeen positive), QQQ +0.69%, IWM +0.40% (ten), EFA +1.20% (fourteen),
  EEM +2.23% (twelve), the US funds +0.62%, IWM less SPY −0.37% (seven).
- **Against the rest of December and January**: the window's daily mean less the rest of December's
  +0.086% (0.118%), less the rest of January's +0.171% (0.111%, t +1.54); the rest of December less
  the sessions outside the two months +0.005% (0.080%), the rest of January −0.080% (0.070%).
- **Its two parts**: the December part, −5 to −1, +0.058% a day over the other sessions (0.089%),
  +0.47% a year compounded, twelve of seventeen positive; the January part, +1 and +2, +0.200% a day
  (0.234%), +0.58% a year, twelve of seventeen.
- **Against the turn of the other months**: the window's daily mean less the other months' sessions
  −5 to +2, 0.0942% over 1,384 sessions: +0.035% (0.097%, t +0.36).
- **By session**, the five funds' average: −5 +0.142%, −4 +0.289%, −3 −0.119%, −2 +0.218%, −1
  −0.081%, +1 +0.723% (seventeen, the exchange closed on 2 January 2007), +2 −0.229%, each measured
  to about ±0.15 to ±0.37%; beside SC-008-01's all-month means (−4 +0.229%, −1 −0.059%, +1 +0.215%)
  and McConnell and Xu's December-to-January turn (−1 0.34%, +1 0.03%, +2 0.51%).
- **The alphas**: the rule +0.66% a year after costs, +0.76% before, costs 0.10%, an appraisal ratio
  of 0.25; the neighbours' and the delayed rule's in gate 6 above.

## What was learned

- **About the theory.** On the lab's funds from 2005 to 2022, the Santa Claus window rose more than
  the other sessions, by about the size the sources' recent years suggest, and in thirteen years of
  seventeen; within noise. The rise did not take the shape the bank gives it. It lay in the foreign
  funds, EEM and EFA, while the three US funds, whose market the rally is claimed for, gained 0.03%
  a day more than usual, and the small caps less than the S&P 500. And it was no larger than at the
  turn of the other months, whose same sessions the lab had already found strong (SC-008-01): the
  bank's claim that the rally is distinct from the turn of the month is not borne out on these
  funds. What stands apart, within noise, is January after the window, weaker than the other
  sessions.
- **About the rule.** Seven sessions a year in the market earned an alpha of 0.66% a year and a
  Sharpe ratio of 0.30, as the card predicted; the neighbours earned 0.4 to 1.3% a year, a longer
  December stretch the most, which is the turn of the month's span again. The holdout lost.
- **About the market.** The rule's best year against the benchmark was 2018, whose window held the
  fall of Christmas Eve and the rebound after it; its worst windows, 2015 and 2014.
- **About the lab.** A calendar card on the same funds as an earlier one can find its measure half
  published: the logic audit found SC-008-01's month-by-month figures for this window's shape, which
  the card's first draft had not disclosed, and the card reported the one measure that no published
  figure gave, the window against the other months. No code finds a card's published neighbours; the
  audit is where it is done.

SC-007 is `tested-inconclusive`: on the lab's equity funds from 2005 to 2022, the Santa Claus window
beat the other sessions within noise, in the foreign funds rather than the US ones, and by no more
than the turn of the other months.
