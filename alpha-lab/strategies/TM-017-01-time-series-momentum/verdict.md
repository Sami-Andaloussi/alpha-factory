# TM-017-01 — Time-series momentum in its plainest form: verdict

**Stops at gate 3, significance.** Holding each of the seven assets only while its past return
beats the Treasury bill gives a higher Sharpe ratio than holding them always, in equal parts,
in-sample (0.50 against 0.41), and a positive alpha in-sample and in the holdout; but it beats only
81.7% of the same weights shifted at random in time, short of the 90% that rules out luck. Holding
the assets always ended higher in both periods: the rule's edge is less exposure for its return,
not more return. Thresholds, version 1; the figures are the notebook's,
[report.ipynb](report.ipynb). The theory is [TM-017](../../bank/TM-017-time-series-momentum.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates, and 117 decisions, once clustered, over 16.9
   years in-sample, from the first holding on 2006-02-01: the monthly targets read the market up to
   the session before, and DBC, which trades from February 2006, is held only once it has a full
   lookback.
2. **Economic edge: passes.** A Sharpe ratio of 0.50 against 0.41 for the benchmark, the same seven
   assets held always in equal parts, and an alpha of 1.55% a year; at twice the costs, 0.48 and
   1.49%. Costs are small, 0.08% a year, a hundredth of a Sharpe unit: one decision a month on seven
   funds trades little. The card's predicted size, a Sharpe ratio of about 0.5, was written without
   a reason drawn from the sources, so that the rule's 0.50 confirms little.
3. **Significance: fails.** The strategy beats 81.7% of 1,000 placebos that shift its own weights
   in time by a year or more, where 90% are needed; its probabilistic Sharpe ratio is 0.99. At such
   shifts, a placebo holds the same assets as the rule on 53% of the asset-sessions, as often as two
   unrelated rules holding as often would (55%): the placebos are not copies of its timing. With
   seven assets and one decision a month, a few reversals of trend decide the rank, and the
   placebos' results spread widely.
4. **Multiple testing: fails.** The alpha against the benchmark, as an appraisal ratio, is 0.30,
   against 0.13 expected from the best of two trials by luck: a deflated Sharpe ratio of 0.833,
   below 0.9. Two trials only, both this card's: the registry held nothing before.
5. **Stability: fails,** on gate 3 alone: the blend of the two lookbacks beats 82.4% of its
   placebos. The blend passes gates 2 and 4, the worse variant keeps a Sharpe ratio of 0.50, four
   of the five blocks are positive, and the alpha stays positive without the best year, 2008
   (0.63% a year instead of 1.55%).
6. **Robustness: fails.** SPY carries 33% of the profit, above the 30% any one asset may. The rest
   holds: the neighbours of the lookback keep a median of 97% of the base's Sharpe ratio and at
   least 81% at ±25%; without the bonds, the worst cluster to lose, 77% remains; a day's delay
   costs nothing.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.89 and an alpha of 0.61% a
   year, both above the tenth percentile of the in-sample paths (−0.22 and −2.31%).

## Verdict

The strategy stops at gate 3. Gates 4, 5 and 6 fail too, so that a pass at gate 3 would not have
been enough: the edge is too small for two trials, the blend of the variants fails significance as
well, and one asset carries a third of the profit.

## The card's refutation, clause by clause

- *No alpha over the same seven assets held always, in equal parts*: not met. The alpha is 1.55% a
  year in-sample and 0.61% in the holdout.
- *No more of its placebos beaten than chance*: not met as worded, but not cleared either. The
  rule beats 81.7% of its placebos, more than the half a rule without skill beats on average; it is
  short of the 90% that rules out luck, so it is not shown to beat chance either.
- *Gains from one asset, one class or one episode*: not met outright. SPY carries 33% of the profit,
  above the lab's 30%; without the bonds, 77% of the Sharpe ratio remains; without its best year,
  the alpha stays positive.

The theory is not refuted; its plainest form is not proven here.

## What was learned

- **About the theory.** In its plainest long-only form, on seven funds, time-series momentum gives
  what a long-only trend rule can: less exposure in long declines, for a smaller return in long
  rises, and a positive alpha, in-sample and in the holdout. Its alpha is spread over the
  years, the best block being 2020 to 2022. What 2008 gave, when it left US and developed equities
  in February and emerging ones in August, 2009 took back: it stayed out of equities through their
  rebound, from March 2009 until October and November, while SPY rose 50%, EFA 66% and EEM 91% before
  it bought them back; this is the abrupt reversal the theory names as its weakness. It held gold
  and the commodity basket into the autumn of 2008, while DBC fell 45% and GLD 23% from July to
  early November. The shifted placebos show that seven assets decided once a month give too few
  independent trends for this edge to be told from luck. The sources' evidence comes from some
  fifty markets, short as well as long, with positions scaled by risk: this card tests the long side
  of seven, in equal shares. Its other forms are other cards: positions scaled by volatility
  (TM-047), the moving-average crossovers at several speeds, a wider universe.
- **About the market.** From 2006 to 2022, US equities carried the largest share of the rule's
  gains, a third, and bonds were the cluster it could least do without. The universe kept two
  Treasury funds, IEF and TLT, whose daily returns correlate at 0.91, as QQQ does with SPY, which
  the reasoning left out as a repetition: two maturities of one bond market, as the sources hold
  several maturities, but they gave bonds two sevenths of the portfolio.
- **About the lab.** The chain ran from the pick to the verdict with the steps the runbook names,
  and its commits are in the runbook's order: the card alone, then the reasoning, the build plan and
  the code, then the registry alone. The work was not in that order. The reasoning, the build plan
  and the code were drafted with the card by 2026-09-23 23:17 UTC; the card was committed on
  2026-09-24 at 22:03 UTC, and the strategy ran at 22:04 UTC, the registry's time. The card's
  refutation was reworded once before its commit, "its past year" becoming "its past return", so
  that it holds for both lookbacks. No return of the strategy was computed before the card's commit:
  the clone's record holds one run, 30 seconds after the card's commit, and `--try` shows no return.
  The lock proves the order of commits, not the order of work, which only the operator can keep. No
  bug was found after the run.
