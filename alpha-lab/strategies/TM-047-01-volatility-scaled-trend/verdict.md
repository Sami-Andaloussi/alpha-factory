# TM-047-01 — Trend with positions scaled by volatility: verdict

**Stops at gate 3, significance. Not proven: a Sharpe ratio of the predicted size, which the battery
cannot tell from luck, and which, on an in-sample check apart from the battery, comes from the tilt the scaling gives rather than from its timing.**
Sizing each position of TM-017-01's trend rule by the inverse of its asset's volatility gives a Sharpe
ratio of 0.58 in-sample, as the card predicted, against 0.495 for the same rule in equal shares and
0.41 for the seven assets held always, an alpha of 2.03% a year and a positive alpha in all five
blocks; but it beats 83.9% of the same weights shifted at random in time, short of the 90% that rules
out luck, and hardly more than the unscaled rule's 81.7%. In the holdout the ranking reversed: 0.73
and an alpha of −0.41% a year, against the unscaled rule's 0.89 and +0.61%. Thresholds, version 1;
the battery's figures are the notebook's, and the weights and the tilt check are computed from the in-sample weights, apart from it; [report.ipynb](report.ipynb). The theory is
[TM-047](../../bank/TM-047-volatility-targeted-momentum.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; 203 decisions, once clustered, over 16.9 years
   in-sample, from the first holding on 2006-02-01. The volatility is re-estimated every month, so
   every first session is a decision, where the unscaled rule counted 117.
2. **Economic edge: passes.** A Sharpe ratio of 0.58 against 0.41 for the benchmark, the seven
   assets held always in equal parts, and an alpha of 2.03% a year; at twice the costs, 0.56 and
   1.93%. Costs are 0.11% a year, 0.018 of a Sharpe unit.
3. **Significance: fails.** The probabilistic Sharpe ratio is 1.00, but the strategy beats 83.9% of
   1,000 placebos holding its own weights shifted in time by a year or more, where 90% are needed.
   The placebos keep its average tilt toward the bonds and change only when it held what: its
   timing beats random timing with the same tilt about as often as the unscaled rule's did (81.7%).
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.42, against 0.29 expected
   from the best of five effective trials by luck (six in the registry, two of which count as one): a
   deflated Sharpe ratio of 0.840, below 0.9.
5. **Stability: fails,** on gates 3 and 4 alone. The blend of the two volatility windows passes gate
   2 and beats 87.3% of its placebos, with a deflated Sharpe ratio of 0.820. The rest holds: the
   worse variant keeps a Sharpe ratio of 0.56, the alpha is positive in all five blocks, and without
   the best year, 2008, it stays at 0.97% a year.
6. **Robustness: passes.** The neighbours keep a median of 100% of the base's Sharpe ratio and at
   least 96% at ±25%; without the bonds, the worst cluster to lose, 68% remains, above the 50%
   floor; SPY carries 28% of the profit, below the 30% limit; a day's delay costs nothing.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.73, above the tenth percentile
   of the in-sample paths (−0.09), and an alpha of −0.41% a year, above its floor (−1.56%): no bug,
   but no alpha in the three years kept aside, when equities rose and the rule's bonds and cash probably held it back against the seven in equal parts. The unscaled rule did better there, 0.89 and +0.61%:
   the in-sample ranking of the two reversed, continuing the scaled rule's shortfall of 2020–22.

## Verdict

The strategy stops at gate 3; gates 4 and 5 fail too, on the same ground: an edge of this size, on
seven assets decided monthly, is not told apart from luck.

## The card's refutation, clause by clause

- *A Sharpe ratio more than 0.1 below the unscaled rule's 0.495*: not met. It is 0.086 above, within
  the 0.1 the card set as one standard error of the difference: the Sharpe ratio came out at the
  predicted 0.58 — a match within that error, not a confirmation — and, as below, through the bond
  tilt rather than the timing. The comparative claim is **not proven**.
- *An alpha of zero or less over the seven held always*: not met. 2.03% a year in-sample.
- *About half of its placebos beaten, or fewer*: not met. 83.9%: more than chance, short of 90%.
- *A result resting on one cluster, one asset or one episode*: not met. All five blocks positive;
  SPY at 28% of the profit; 68% of the Sharpe ratio kept without the bonds.

The theory is **not proven, not refuted**: a Sharpe ratio in the predicted direction and of the
predicted size, which the battery cannot tell from luck.

**What the test could detect.** The appraisal ratio of 0.42 is measured to about ±0.24 over 17
years: some 1.7 standard errors from zero. Gate 4 deflates the ratio after Lo's correction for
autocorrelation, 0.53 here, against the luck of the best of five trials, 0.29: with the same
returns, it would have passed from an appraisal ratio of about 0.48, and it would pass against a
single trial. At gate 3, seven assets decided monthly leave the
placebos a wide spread: TM-017-01 met the same wall at 81.7%. What the test can say is that scaling is not harmful in-sample — though worse than the unscaled rule since 2020, the holdout included — and gives about the predicted Sharpe ratio; what it cannot say is that the gain is
more than chance.

**Timing, or tilt.** The scaling did two things. It tilted the portfolio toward the bonds, which
held on average 43% of what was invested against 29% for the unscaled rule (IEF 20% of the portfolio
against 9%), in years when Treasury yields mostly fell; and it timed the exposure. The cap at full
investment bound in 21% of the months (27% for the 21-day window), more often than the reasoning
expected; the portfolio held 68% of its value on average, against 63% for the unscaled rule. Gate
3's placebos keep the tilt and move the timing: that the scaled rule beats them about as often as
the unscaled rule beat its own says the timing added little the battery can see — a weak comparison
between two different sets of placebos. A check apart from the battery, on the in-sample years,
settles it more firmly: the same trend rule with each asset's weight fixed at `risk` over its
average volatility, the same cap, earns a Sharpe ratio of 0.60; against it, the scaled rule's
returns leave an appraisal ratio of 0.02 (a t-statistic of 0.06), where against the unscaled rule
they leave 0.33 (1.35). On this sample, the tilt accounts for about all of the gain, and the timing
the theory names for almost none.

## What was learned

- **About the theory.** On seven funds from 2006 to 2022, volatility scaling raised the Sharpe
  ratio of the trend rule from 0.495 to 0.58, with a positive alpha in every block, against four of
  five for the unscaled rule; the largest in 2008–09. From August 2008 both rules held no equities —
  the trend test did that, not the scaling; the scaled rule gained over the unscaled one by holding
  less of the commodity basket and of the emerging and developed markets as they fell, and more
  intermediate Treasuries. Its years of negative edge are 2009, 2016, 2018 and, barely, 2020. In
  2018 and 2020 the scaling did worse than the unscaled rule: after the calm of 2017 it went into
  February and October 2018 with larger equity weights (SPY 23% and 25%), and in 2020 the 100-day
  volatility of the crash kept SPY near 4% through the rebound. The faster 21-day window did no
  better than the 100-day one (0.56 against 0.58). The theory's own mechanism, the timing, is what
  the lab could not find; its sources' purest test of it — Moreira and Muir's scaling of a whole
  portfolio by its own recent volatility, capped at full investment — needs no estimate of
  correlations, and is the form of the theory this card left untested.
- **About the market.** The bonds were the cluster the rule could least do without, and US equities
  carried the largest share of its profit, 28%, less than TM-017-01's 33%: equal risk spread the
  profit more evenly. In 2023–25 the rule's Sharpe ratio held, 0.73, but its alpha did not, in a market that rewarded holding equities.
- **About the lab.** The chain ran without a refusal: the card committed alone, the reasoning, the
  build plan and the code after it, `--try` clean, one run, the registry committed alone. The build
  plan and the code were written in the seconds after the card's commit, from the design the card
  and its reasoning had fixed: no file of them existed before the lock, and no return was computed
  before it. Gate 4 grows harder as the registry grows: the Sharpe ratio expected from luck was 0.13 for
  TM-017-01's two trials and is 0.29 for five effective trials; an edge of 0.42 that would have
  passed first fails now. That is the gate doing its work — every trial the lab makes raises the bar
  for the next — and it is why each card keeps its variants to two.
