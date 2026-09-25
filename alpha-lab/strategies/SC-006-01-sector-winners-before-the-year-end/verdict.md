# SC-006-01 — The year's winning sectors over December's last sessions: verdict

**Stops at gate 2, economic edge. Not refuted, not proven: the three sector funds nearest their
year's high, less the other sector funds and adjusted for their beta, earned −0.03% a year on
average over December's last sessions but one, 0.14 of a standard error from zero, at the bottom of
the predicted 0 to +0.25% and positive in six years of eighteen; unadjusted, the winners trailed by
0.21% a year, the drag of their low beta in a rising market.** Holding the winners over the window
and the eleven funds in equal parts otherwise earned an alpha of −0.26% a year over the funds held
always, −0.11% before costs of 0.15% a year, an appraisal ratio of −0.29, against a predicted 0 to
0.18% before costs and 0 to 0.2. Thresholds, version 4; the battery's figures are the notebook's,
[report.ipynb](report.ipynb), and the windows' returns, betas, alphas before costs and the
neighbours' alphas are computed apart from it, on the same sessions. The theory is
[SC-006](../../bank/SC-006-december-effect.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 100 dates; 39 decisions, once clustered, over 18.0 years
   in-sample, from the first holding on 2005-01-03.
2. **Economic edge: fails.** A Sharpe ratio of 0.477, below the benchmark's 0.491, with an alpha of
   −0.26% a year; at twice the costs, 0.469 and −0.39%. Costs are 0.15% a year.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.99, the market's; the rule beats
   16.1% of 1,000 placebos, its own weights shifted in time.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is −0.293, against 0.652 expected
   from the best of forty-one effective trials by luck: a deflated Sharpe ratio of 0.000.
5. **Stability: fails.** The blend of the variants, the base alone, fails gates 2, 3 and 4. The
   alpha is positive in three blocks of five — 2005–07 (+0.16% a year), 2010–14 (+0.04%), 2020–22
   (+0.00%) — and negative in 2008–09 (−0.93%) and 2015–19 (−0.65%); without its best year, 2014, it
   is −0.32% a year.
6. **Robustness: passes.** The neighbours keep 101% of the base's Sharpe ratio at the median and at
   least 98.5% at ±25%, and a day's delay 99.1%: for a tilt this small, the benchmark's ratios. The
   largest share of the profit is XLK's, 14.7%; the eleven funds form one cluster. Their alphas,
   computed apart: two winners −0.19% a year (appraisal ratio −0.19), four −0.20% (−0.27); entry at
   −5, −0.11% (−0.14), at −9, −0.13% (−0.13), at −4, −0.10% (−0.20), at −10, +0.06% (+0.05); exit at
   −1, −0.40% (−0.44), at −3, −0.14% (−0.18); the targets a session late, −0.32% (−0.36).
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.78 and an alpha of −0.52% a
   year, both above the tenth percentile of the in-sample paths (−0.20 and −0.90%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 5 as well.

## The card's refutation, clause by clause

Over the eighteen Decembers from 2005 to 2022, from the close of the seventh-last scheduled session
to the close of the second-last, the winners' average return, the three funds with the smallest drop
from their year's high on the ranking session (four in 2021, a tie at the cut), less the other
ranked funds', less that year's beta times the ranked funds' average return: a mean of −0.030% a
year, a standard error of 0.220% from the eighteen years, t −0.14; six years positive.

- *A t statistic of −0.35 or below*: not met. The theory is **not refuted**; short of gates 1 to 7,
  it is **not proven**.

**The test's power.** The card gave the clause about a 36% chance of refuting with no effect, about
10% at +0.3% and 3% at +0.5%, with a standard error of about 0.30 to 0.35%; it came out at 0.22%,
the years less dispersed than the funds' overall volatility implied. The mean lies at the
prediction's lower end, 1.3 standard errors below its top: the run cannot tell no effect from a
small one, and finds none.

Reported, not graded, as the card stated them, each return compounded over its sessions:

- **Year by year**, the adjusted difference and the winners' beta: 2005 +0.13% (beta −0.22), 2006
  −0.13% (+0.05), 2007 +1.29% (−0.12), 2008 −0.20% (−0.50), 2009 −0.88% (−0.14), 2010 −0.28%
  (−0.14), 2011 +0.89% (−0.44), 2012 −0.14% (−0.09), 2013 −0.31% (+0.17), 2014 +1.40% (−0.35), 2015
  −0.25% (−0.08), 2016 −1.06% (+0.11), 2017 −0.33% (+0.20), 2018 −2.36% (−0.61), 2019 −0.10%
  (+0.02), 2020 +0.27% (−0.11), 2021 +1.55% (−0.52), 2022 −0.02% (−0.31). The winners' beta averaged
  −0.17, and was below −0.3 in six years.
- **Unadjusted**, the winners less the other funds: −0.207% a year (0.215%, t −0.96), eight years
  positive — it would have met the clause's bar, carried by the low-beta winners (XLP twelve times,
  XLU seven, XLV six) in a window where the ranked funds rose +0.49% a year over the bill (0.27%, t
  +1.78), in twelve years of eighteen.
- **The bill's rate**: in the seven years when it stood at 1% a year or more on the ranking session,
  when deferral is worth most, the adjusted difference was −0.22% (0.41%), two years positive; in
  the eleven others, +0.09% (0.26%), four positive. **Gains to defer**: the winners had risen since
  the year's first session in seventeen years, −0.02% (0.23%); not in 2008 alone, −0.20%.
- **January**, the winners less the other funds over its first five scheduled sessions, over the
  Decembers 2005 to 2021: −0.40% (0.50%), eight of seventeen positive; December's unadjusted
  difference less January's, Singal's contrast, +0.18% (0.49%). The 2022 December's January, read
  apart after the run in the holdout's data: −2.16%.
- **The losers**, the three funds furthest from their high, less the other funds: +0.06% (0.22%)
  over the window, +0.23% (0.57%) over January's first five sessions.
- **From the ranking session to December's last**, the winners less the other funds: −0.18% (0.26%).
- **The drops**: the winners averaged 0 to 3.4% below their year's high on the ranking session (28%
  in 2008), the other funds 1 to 19% (46% in 2008).
- **The alphas**: the rule −0.26% a year after costs, −0.11% before, costs 0.15%, an appraisal ratio
  of −0.29; the neighbours' and the delayed rule's in gate 6 above.

## What was learned

- **About the theory.** On the lab's sector funds from 2005 to 2022, the year's winners did not beat
  the other sectors over December's last sessions but one once their beta was taken out: −0.03% a
  year, no better where deferral was worth most, when the bill paid 1% or more; their loss in
  January's first sessions, −0.40% a year, where postponed sales would fall, was within noise.
  Singal's effect, about 0.3% a year on single stocks from 1988 to 2000, left no trace at the level
  of sector funds after the 2003 tax cut and the effect's publication; whether it lives in single
  stocks is beyond the lab's funds.
- **About the measure.** The winners a drop from the high picks among sector funds are mostly the
  defensive ones, of low beta; in a window where the market rose most years, their raw difference
  trailed by 0.21% a year and would have refuted the theory on beta alone. The logic audit named
  that drag before the lock, and the clause removed it with each year's beta measured before the
  ranking.
- **About the rule.** Moving the whole portfolio into three sectors for five sessions a year cost
  0.15% a year and earned −0.11% before it; every neighbour but the earliest entry lost too.
- **About the lab.** A ranking by a price level, here the drop from a high, selects on volatility as
  much as on the claim; a clause that compares the selected funds with the rest must remove the
  exposure the selection brings, or it grades the market. No code checks a clause for it; the logic
  audit is where it is asked, and here it was.

SC-006 is `tested-inconclusive`: on the lab's sector funds from 2005 to 2022, the year's winners did
not outperform the other sectors over December's last sessions once their low beta was removed, and
fell back in January only within noise; the clause, unable at the level of sectors to tell a small
effect from none, left the theory not refuted and not proven.
