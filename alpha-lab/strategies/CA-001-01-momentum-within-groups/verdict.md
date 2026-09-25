# CA-001-01 — Momentum within sectors, equity markets and commodities: verdict

**Stops at gate 2, economic edge. Refuted in its base form; the sources' own form for these
markets not proven, its edge a third of the prediction.** Holding, each month, the top third of each
group by its past year's return, the last month left out, earns almost exactly what holding every
member of the groups does: a Sharpe ratio of 0.44 against 0.46 in-sample, an alpha of 0.20% a year
that turns negative at twice the costs, and a rank among its own placebos, shifted in time, of
47.6%, where a rule without skill lands at about half. Keeping the last month, the variant, does a
little better, and the blend of the two beats 56.6% of its placebos with an alpha of 0.43% a year.
The card predicted an alpha of about 2% a year. Thresholds, version 1;
the figures are the notebook's, [report.ipynb](report.ipynb). The theory is
[CA-001](../../bank/CA-001-momentum-sectors-countries-asset-classes.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates; 151 decisions, once clustered, over 16.9 years
   in-sample, from the first holding on 2006-02-01. The ranking reads closes up to the session
   before, and a fund is ranked only a full year after it starts trading.
2. **Economic edge: fails.** A Sharpe ratio of 0.44 against 0.46 for the benchmark, the same
   nineteen funds held in equal parts, and an alpha of 0.20% a year; at twice the costs, 0.43 and
   −0.02%. Costs are small, 0.24% a year, 0.013 of a Sharpe unit: the rule trades little, and what
   it lacks is an edge, not cheaper trading.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.98 — the strategy earns the
   market's premium, as its benchmark does — but it beats only 47.6% of 1,000 placebos holding its
   own weights shifted in time by a year or more, where 90% are needed. The placebos keep the
   strategy's mix of groups and change only which members it held when: its choice of members does
   no better than the same choices at random dates.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.03, against 0.26 expected
   from the best of four trials by luck: a deflated Sharpe ratio of 0.18.
5. **Stability: fails.** The blend of the two variants fails gates 2, 3 and 4 (an alpha of 0.43% a
   year, 56.6% of its placebos beaten). The alpha is positive in two of the five blocks, 2010–14 and
   2020–22, and negative in 2005–07, 2008–09 and 2015–19; without its best year, 2022, it is −0.28%
   a year. Years of gain and years of loss alternate: nine of gain, one of them near zero, and
   eight of loss.
6. **Robustness: passes.** The neighbours of the lookback and the skip keep a median of 106% of the
   base's Sharpe ratio, and at least 104% at ±25%; leaving out a cluster keeps at least 91% (the
   sectors, the worst to lose); no
   fund carries more than 17% of the profit (QQQ); a day's delay costs nothing. The two risks the
   reasoning named — the Sharpe ratio falling with the mix when the sectors leave, one fund carrying
   too much — did not occur. The rule is robust because it is close to its benchmark: moving its
   parameters moves little.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.97 and an alpha of −0.44% a
   year, both above the tenth percentile of the in-sample paths (−0.23 and −4.27%): no bug and no
   decay, since there was no edge to decay.

## Verdict

The strategy stops at gate 2. Gates 3, 4 and 5 fail too: even without costs, the rule's choice of
leaders is not told apart from the same choices made at random dates.

## The card's refutation, clause by clause

- *An alpha of zero or less over every member held in equal parts*: for the base, not met at the
  stated costs (0.20% a year, a tenth of the prediction), met at twice the costs (−0.02%).
- *About half of its placebos beaten, or fewer*: met by the base, 47.6%. The base form, MOM2–12, is
  **refuted** under the card's clause.
- *A positive alpha that beats more than half of its placebos but fewer than 90%*: the variant,
  MOM1–12, the form the reasoning named as the sources' own for markets outside individual stocks,
  earns an appraisal ratio of 0.11 against the base's 0.03, and the blend of the two an alpha of
  0.43% a year with 56.6% of its placebos beaten. The battery does not rank the variant alone among
  placebos; the blend falls in the band the card calls **not proven**. A rank of 57% is one a rule
  without skill reaches often, so the evidence for this small edge is weak: its appraisal ratio of
  0.11 is a third of the prediction's, and 0.9 standard errors below it.
- The theory's relative half is therefore refuted in its base form and not proven in its
  variant, on these groups and these years; nowhere does it show the size its sources report.

**The test's power.** The rule made 151 independent decisions in-sample. Its bets, hedged of the
benchmark, move by about 6% a year (0.20% of alpha for an appraisal ratio of 0.033), so that over 17
years an appraisal ratio is measured to about ±0.24. The sources' top third earned an appraisal
ratio of about 0.7 among country indices and 0.4 among commodities (Table I: alphas of 4.4% and
5.8% with t-statistics of 4.0 and 2.7 over 34 and 40 years). Measured group by group, on the run's
in-sample positions, as the active return of each group against the benchmark's holding of it, the
base earns an appraisal ratio of +0.19 among the equity markets, 2.1 standard errors below the
sources' country indices, 0.00 among the commodities, 1.8 below theirs, and −0.07 among the
sectors, for which the sources give no figure. An edge of the sources' size in the groups they
measure would likely have shown; the whole portfolio's 0.03 does not exclude the card's own, halved
prediction as firmly, an appraisal ratio of about 0.33 lying 1.2 standard errors above it. To pass
gate 4 with four trials, the edge would have needed an appraisal ratio of about 0.53, on the lab's
deflated Sharpe ratio for this series. What the test rules out is an edge of the sources' size in
these groups; a real but smaller one, an alpha around 1% a year, it could not have told from luck.

## What was learned

- **About the theory.** In the lab's groups from 2006 to 2022, the past year's leaders of each
  group did not keep leading on the whole: the relative momentum the sources find among eighteen
  countries and twenty-seven commodities from the 1970s to 2011 does not appear among eleven US
  sectors, five equity markets and three commodity funds after 2005. Its worst block is 2008–09.
  From before March 2009 the rule held the crash's leaders — staples, utilities, health care and
  gold — into the rebound, which they trailed from March to December (+37%, +32%, +44% and +18%) while the
  crash's losers led it (financials +107%, emerging markets +112%, materials +86%): the momentum
  crash that TM-024 names; it kept utilities until May, staples and gold until October, and health
  care until November. Its best years, 2022, 2013 and 2020, are years of long, one-sided moves. Keeping the most recent month in the ranking (the variant)
  did a little better, an appraisal ratio of 0.11 against 0.03, as the sources say for markets
  outside individual stocks: a small edge, not proven, a third of the size predicted. The time-series half of CA-001 is not
  tested here; it is TM-017's.
- **About the market.** The sectors carried the rule's weight, nine seventeenths of it until 2016
  and eleven nineteenths once XLRE and XLC traded, and no one of them its result: the sectors' own
  appraisal ratio was −0.07, and the rule held six funds most months, seven or eight in the others; the largest shares of the profit are QQQ's (17%), XLY's and GLD's. The
  groups the sources measure best are the lab's thinnest — three commodity funds, where a ranking
  picks one of three, and five equity markets, three of them overlapping US baskets.
- **About the lab.** The chain ran as the runbook says: the card audited, answered and committed
  alone, the reasoning, the build plan and the code after it, `--try` clean on its first attempt,
  one run, the registry committed alone. The first run was refused before it started: a check of the
  targets' structure — weights summing to one, the funds held on five dates, nothing held before it
  trades — done by importing the strategy outside the runner on the in-sample years only, with no
  return computed, had left a compiled file in the folder, and the runner refuses any file git
  ignores; the file was removed and the run started, the card unused by the refusal. Such a check
  belongs to `--try`, which reads the targets without leaving a file, or to a check run with
  `PYTHONDONTWRITEBYTECODE=1`. No bug was found after the run.
