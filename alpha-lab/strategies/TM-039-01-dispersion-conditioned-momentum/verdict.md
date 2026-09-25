# TM-039-01 — Momentum held while returns are dispersed: verdict

**Stops at gate 2, economic edge. Refuted in this form: holding CA-001-01's momentum tilt only after
months in which its group's returns were more dispersed than usual lost 1.72% a year of alpha
against holding it always.** CA-001-01's rule, recomputed over the same sessions, earns 0.20% a year
over the nineteen funds held in equal parts; switched off in each group after its less dispersed
months, it earns −1.52%, a difference of −1.72% a year with a standard error of 0.88% (a t-statistic
of −1.96). The loss is in the returns, not in the hedge: the raw excess return, net of costs, fell
by 1.59% a year, of which the higher costs of switching are 0.13%, while the beta rose by only
0.016. The measures stated before the run point the same way in each group — CA-001-01's tilt lost
after dispersed months and earned after the others, the sign Stivers and Sun found on US stocks,
against the bank's — but the split is clear only in the equity markets, and, by a check found after
the result, two years, 2020 and 2022, carry more than half the difference. Thresholds, version 2;
the battery's figures are the notebook's, [report.ipynb](report.ipynb), and the comparisons, the
pre-stated measures, the blocks and the years are computed apart from it, on the same sessions and
costs. The theory is [TM-039](../../bank/TM-039-return-dispersion-momentum.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; 175 decisions, once clustered, over 16.9 years
   in-sample, from the first holding on 2006-02-01.
2. **Economic edge: fails.** A Sharpe ratio of 0.36, below the 0.4 required and the benchmark's
   0.46, and an alpha of −1.52% a year; at twice the costs, 0.34 and −1.88%. Costs are 0.37% a year,
   0.021 of a Sharpe unit, against CA-001-01's 0.24%: the switches cost about 0.13% a year.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.96; the rule beats 2.3% of 1,000
   placebos, its own weights shifted in time by a year or more, where 90% are needed.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is −0.35, against 0.46 expected
   from the best of nineteen effective trials by luck: a deflated Sharpe ratio of 0.000.
5. **Stability: fails.** The blend of the two variants fails gates 2, 3 and 4 (a Sharpe ratio of
   0.35, an alpha of −1.67% a year, 0.1% of its placebos beaten). The base's alpha is negative in
   all five blocks: 2005–07 (−2.1% a year), 2008–09 (−4.6%), 2010–14 (−0.1%), 2015–19 (−1.5%) and
   2020–22 (−3.4%); without its best year, 2007, it is −1.72% a year.
6. **Robustness: passes.** The neighbours keep a median of 116% of the base's Sharpe ratio and at
   least 103% at ±25%; without the sectors, the worst cluster to lose, 78% remains; the largest
   share of the profit is QQQ's, 16%; a day's delay keeps 102%.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 1.12 and an alpha of 1.06% a
   year, both above the tenth percentile of the in-sample paths (−0.32 and −4.68%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 5 as well.

## The card's refutation, clause by clause

`python -m lab.compare` against CA-001-01's base, over the base's sessions from 2006-02-01 to
2022-12-30 at the stated costs: the base's alpha is −1.523% a year, CA-001-01's 0.198% — the same
code on the same snapshot gives CA-001-01's recorded 0.20% again — their betas 0.963 and 0.947. The
difference is −1.720% a year with a standard error of 0.876%: below −1% and more than one standard
error below zero. The claim that momentum's profit rises with the dispersion of the returns it
ranks is **refuted in this form**: switching CA-001-01's tilt off after its groups' less dispersed
months lost alpha. It says nothing against the relation over the same period, which the lab does
not test.

The variant, one state for every group read from the dispersion of all nineteen funds, reported, not
graded: an alpha of −1.818% a year (a beta of 0.965), −2.016% against CA-001-01 with a standard
error of 0.899% (t −2.24); it too would meet the clause's thresholds.

**Which way the alpha was lost.** The clause names three: the tilt's own months, the market exposure
the switch adds, the costs of switching. The beta rose by 0.016, a charge of about 0.13% a year at
the benchmark's premium of about 8%, and the costs by 0.13% a year: together about 0.26%, below the
0.3 to 0.7% the reasoning allowed. The rest, about 1.46% a year, is the tilt's own months: the
tilt's raw contributions in the months out of the state, measured below, sum to about 1.4% a year
before costs.

**The test's power.** The standard error came in at 0.88%, below the 1.2% the reasoning estimated:
the difference moved by 3.60% a year against the 5.0% assumed, the two rules' bets correlating at
0.78. The standard error ignores the error in estimating each rule's beta, a small addition. At that
noise, a true difference of zero would read as refuted about 13% of the time, and a true −0.26%, the
measured charge alone, about 20%. The measured −1.72% lies 1.96 standard errors below zero (a
one-sided probability of 2.5%) and 1.67 below the charge alone (4.8%). Found after the result, and
used only to temper the reading: 2020 and 2022 carry −16.2 of the −28.9 points of hedged difference
summed over the years; without 2020 the difference is −1.27% a year (0.86%), and without both years
−0.86%, which would not meet the clause.

## The measures stated before the run

Reported, not graded, as the card stated them; each month's weights are counted from the session
after the target, when the engine holds them.

- **How often the switch acted.** Out of the state, as the reasoning's count foresaw: the sectors
  and the equity markets in 62% of the months, the commodities in 56%, counting as out the 13 months
  in which they had one ranked fund, where the two rules are the same, and 53% of the 190 months
  with a reading; the reasoning's 60% for the commodities was a slip, the three groups' overall
  share of group-months out of the state. The variant was out in 61%. The groups switched 4.6, 5.8
  and 4.9 times a year.
- **Where the switch acted.** In the 175 months (86% of the sessions) in which the base's weights
  differ from CA-001-01's in some group, each rule given its own beta there, the base's alpha is
  −1.30% a year and CA-001-01's 0.65% (betas 0.997 and 0.975): −1.95% a year in those sessions,
  −1.68% of the whole. In the 28 months in which the two hold the same weights, −2.87% and −2.62%
  (betas 0.880 each), −0.04% of the whole, the extra costs. Nearly all the loss lies where the
  switch acted.
- **Each group's tilt by its own state**, CA-001-01's weights less its equal parts, 1/N on every
  fund trading, measured raw, the month held from the session after each target to the next:

  | Group | After dispersed months | After the others | The others less the dispersed |
  |---|---|---|---|
  | Sectors | −2.36% a year (1.83%), 77 months | +0.70% (1.02%), 126 months | +3.06% (2.10%) |
  | Equity markets | −1.17% (0.58%), 77 months | +1.21% (0.46%), 126 months | +2.37% (0.74%) |
  | Commodities | −0.51% (0.92%), 89 months | +0.37% (0.66%), 114 months | +0.88% (1.13%) |

  Standard errors in brackets. The commodities' 114 other months include the 13 with one ranked
  fund, where the tilt is zero. In each group the tilt lost after dispersed months and earned after
  the others; the split is clear in the equity markets (about three standard errors) and within
  about one and a half in the sectors and the commodities.
- **CA-001-01's edge by the variant's state**, a beta for each state: after months in which the
  dispersion of all nineteen funds was above its average, 39% of the sessions, an alpha of −4.26% a
  year there (a standard error of 1.80%, a beta of 0.935); after the others, 3.00% a year (1.27%,
  0.962). Their contributions, −1.67% and +1.83% a year, sum to 0.16%, near CA-001-01's 0.20%; with
  a beta for each state they need not add up.

## What was learned

- **About the theory.** On the lab's funds, momentum within groups did not earn after dispersed
  months: it lost there and earned after calm ones, in each group and in the variant's single state.
  CA-001-01's near-zero alpha hid a split by state — about 7% a year between the two sides of the
  variant's state (−4.3% against +3.0%), 1 to 3% a year within each group — in the direction Stivers
  and Sun found on US stocks, where dispersion leads as a countercyclical state and momentum is
  procyclical, and against the bank's. On these funds, the sort's winners did worse, on average, in
  the months after dispersed months — clearly in the equity markets, within noise in the other two
  groups. The base lost to CA-001-01 in eleven of seventeen years, most in 2020 (−8.8 points of
  hedged return), 2022 (−7.4), 2013 and 2015 (−4.9 each), and 2011 and 2021 (−3.0 each); it gained
  most in 2016 (+4.2), 2017 (+2.4) and 2012 (+1.7). The crisis risk the reasoning named — the tilt
  switched on just before a rebound — is not what hurt most: one of the two worst months, March 2020
  (−3.9 points, with September 2021 at −3.9), found the sectors and the equity markets out of the
  state, after a February whose dispersion was at or below its average — the sectors' only just —
  holding their equal parts where CA-001-01 held its leaders.
- **About the opposite rule.** The split suggests holding the tilt only after calm months. That rule
  was not tested: it is the variant's complement, read after the result, a hypothesis with a source
  (Stivers and Sun) and an in-sample hint, which would need a card of its own and a new lock; gate 4
  counts this card's trials already.
- **About the sources.** The bank's attribution of the claim to Greyserman and Kaminski does not
  hold (their chapter on return dispersion measures dispersion between trend following programmes);
  the lab read the three studies of the relation only in their abstracts. The trend following half
  of TM-039 is untested, as the campaign's decisions record.
- **About the lab.** The card's first draft read the dispersion over the ranking's own twelve-month
  window, and justified it by the bet's size, which rank-only weights do not have; the logic audit
  moved the reading to the month just past, argued from the claim alone. The charge of the switch
  was estimated from TM-024-01's record before the run, and the measures that separate it from the
  tilt's months were stated before the run: here they show the loss is the tilt's, which TM-018-01's
  clause could not tell until its review.

TM-039 is `tested-inconclusive`: its cross-sectional form on the lab's funds — momentum within
groups held only after dispersed months — is refuted in this form, the tilt having earned after calm
months instead; the relation over the same period, the trend following half, and the sources' own
stock and currency markets are not tested.
