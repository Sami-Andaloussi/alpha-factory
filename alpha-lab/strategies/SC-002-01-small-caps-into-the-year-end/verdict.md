# SC-002-01 — The small caps for the S&P 500 from mid-December: verdict

**Stops at gate 3, significance. Not refuted, not proven: IWM beat SPY from the first session on or
after 15 December to the third-to-last session of December by +0.83% a year on average, 2.7
standard errors from zero and in fourteen years of eighteen, inside the predicted +0.5 to +1.5%; but
most of it came in the turns of the year inside the sources' data, and the rule built on it, with a
fifth of the portfolio moved, beat 84.6% of its placebos where 90% are needed.** Moving SPY's fifth
to IWM over those sessions earned an alpha of +0.12% a year over the five funds held always, +0.17%
before costs of 0.05% a year, an appraisal ratio of 0.34, against a predicted 0.1 to 0.3% and 0.25
to 0.8. Thresholds, version 4; the battery's figures are the notebook's,
[report.ipynb](report.ipynb), and the windows' returns, alphas before costs and the neighbours'
alphas are computed apart from it, on the same sessions. The theory is
[SC-002](../../bank/SC-002-january-effect.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 100 dates; the targets read no price, only the calendar of
   scheduled sessions; 37 decisions, once clustered, over 18.0 years in-sample, from the first
   holding on 2005-01-03.
2. **Economic edge: passes.** A Sharpe ratio of 0.4005, at the 0.4 required and above the
   benchmark's 0.3951, with an alpha of +0.12% a year; at twice the costs, 0.398 and +0.08%. Costs
   are 0.05% a year.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.98, the market's; the rule beats
   84.6% of 1,000 placebos, its own weights shifted in time, fewer than the 90% required.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.340, against 0.648 expected
   from the best of forty effective trials by luck: a deflated Sharpe ratio of 0.161.
5. **Stability: fails.** The blend of the variants, the base alone, fails gates 3 and 4. The alpha
   is positive in three blocks of five — 2005–07 (+0.18% a year), 2008–09 (+0.63%), 2010–14 (+0.13%)
   — and negative in 2015–19 (−0.03%) and 2020–22 (−0.07%); without its best year, 2008, it is
   +0.08% a year.
6. **Robustness: fails.** QQQ carries 34% of the profit, more than 30%, although the equal weights
   were set back each month. The neighbours keep 99.9% of the base's Sharpe ratio at the median and
   at least 98.7% at ±25%, and a day's delay 100.8%: for a tilt this close to the benchmark those
   are the benchmark's ratios, as the card said. Their alphas, computed apart: start 11, +0.08% a
   year (appraisal ratio 0.19); start 19, −0.00% (−0.00); start 8, −0.02% (−0.03); start 22, −0.10%
   (−0.52); end −2, +0.14% (0.40); end −4, +0.17% (0.53); the targets a session late, +0.21% (0.36).
7. **Sealed holdout: fails.** Over 2023 to 2025, a Sharpe ratio of 0.98 and an alpha of −0.23% a
   year, below the tenth percentile of the in-sample paths (−0.10%).

## Verdict

The strategy stops at gate 3, and fails gates 4 to 7 as well.

## The card's refutation, clause by clause

Over the eighteen turns of the year from 2005–06 to 2022–23, from the close of the first scheduled
session on or after 15 December (2005-12-15 the first, 2022-12-15 the last) to the close of the
third-to-last scheduled session of December, IWM's return less SPY's, each compounded over the
window: a mean of +0.830% a year, a standard error of 0.310% from the eighteen years, t +2.67;
fourteen years positive.

- *A t statistic of −0.35 or below*: not met. The theory is **not refuted**; short of gates 1 to 7,
  it is **not proven**.

**The test's power.** The card gave the clause about a 36% chance of refuting with no effect, about
7% at +0.5% and under 1% at +1%, with a standard error of about 0.41 to 0.46%; it came out at 0.31%,
the years less dispersed than the funds' overall volatility implied. The mean lies inside the
prediction and clears zero at the 5% level with seventeen degrees of freedom.

Reported, not graded, as the card stated them, each return compounded over its sessions:

- **Year by year**, IWM less SPY over the window: 2005 +0.35%, 2006 +0.61%, 2007 +2.81%, 2008
  +4.11%, 2009 +2.60%, 2010 +0.85%, 2011 +0.07%, 2012 +1.22%, 2013 +0.53%, 2014 +1.81%, 2015 +0.89%,
  2016 +0.22%, 2017 +0.66%, 2018 −1.03%, 2019 −0.34%, 2020 −1.06%, 2021 +0.67%, 2022 −0.05%.
- **Inside and outside Ziemba's data**: over the turns 2005–06 to 2011–12, +1.63% a year (0.58%, t
  +2.80), seven of seven positive; over 2012–13 to 2022–23, +0.32% (0.27%, t +1.19), seven of
  eleven.
- **Beyond IWM's beta**: IWM less 1.135 times SPY, its in-sample beta, +0.71% (0.30%, t +2.38),
  fourteen of eighteen; IWM less QQQ, +1.14% (0.40%, t +2.87), fourteen of eighteen.
- **The market's own window**, less the bill's: SPY +0.86% (0.48%, t +1.81), eleven of eighteen
  positive; IWM +1.69% (0.64%, t +2.66).
- **The last sessions of December**, from the window's end to the last session: IWM less SPY +0.02%
  (0.14%), nine of eighteen positive.
- **The classic January effect**, over the seventeen turns 2005–06 to 2021–22: IWM less SPY from
  December's last session to January's tenth, +0.07% (0.58%), eight of seventeen positive; to
  January's last, −0.05% (0.75%), seven of seventeen. The 2022–23 turn, read apart after the run in
  the holdout's data: +3.13% to January's tenth session, +3.53% to its last.
- **The alphas**: the rule +0.12% a year after costs, +0.17% before, costs 0.05%, an appraisal ratio
  of 0.34; the neighbours' and the delayed rule's in gate 6 above.

## What was learned

- **About the theory.** On the lab's funds from 2005 to 2022, the Russell 2000 beat the S&P 500 in
  the second half of December, before its last three sessions, by about 0.8% a year, in fourteen
  years of eighteen and beyond IWM's beta — Ziemba's migrated effect, where the sources placed it.
  It faded: +1.6% a year in every one of the seven turns inside Ziemba's data, +0.3% and within
  noise over the eleven after it, with four of the last five years negative. The classic January
  effect did not appear in IWM against SPY, as the sources' latest years had found; its one strong
  January, 2023, fell in the holdout.
- **About the rule.** A fifth of the portfolio moved for eight sessions a year gave an appraisal
  ratio of 0.34, about what the card expected, and no chance at gates 3 and 4, as the logic audit
  had simulated: the edge sits in 146 sessions of 4,500, and its placebos, the same tilt at other
  dates, beat it about one time in six or seven. The start was fragile: from 19 December or 8
  December the alpha was nil, from 22 December negative; the end at two or four sessions before
  December's last did as well as three.
- **About the market.** QQQ's gains made it 34% of the profit of a portfolio set back to equal parts
  every month: an equal weight of five equity funds, one of them the Nasdaq-100 from 2005 to 2022,
  fails gate 6 on QQQ unless it is reset more often, whatever the rule's own bet.
- **About the lab.** A calendar tilt this small is judged by gates built for rules with a whole
  year's exposure: its Sharpe ratio is the benchmark's, and gate 6's neighbour and delay ratios read
  the benchmark, not the tilt. The card said so before the run and reported the neighbours' alphas;
  the battery still compares Sharpe ratios. No code measures a neighbour's alpha in gate 6: the card
  and the verdict carry it.

SC-002 is `tested-inconclusive`: on the lab's funds from 2005 to 2022, small caps beat the S&P 500
in the second half of December, significantly over the eighteen years and inside the prediction, but
mostly in the years the sources had already seen; the classic January effect did not appear, and the
rule built on the December effect was too small a bet to pass gate 3.
