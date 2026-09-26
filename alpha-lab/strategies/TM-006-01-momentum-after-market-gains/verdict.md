# TM-006-01 — Momentum after market gains: verdict

**Stops at gate 2, economic edge. Not refuted, not proven, and not supported: outside the panic
states TM-024-01 had already read, momentum within the groups was no weaker after their markets had
fallen over two years than after they had not — +0.19% a year, 0.04 standard errors from zero, where
the card predicted 1 to 5% a year weaker; the weakness the lab had seen lay in the panic months
alone.** Switching CA-001-01's momentum tilt off in every down state earned an alpha of 0.03% a year
over the nineteen funds in equal parts, 0.26% before costs of 0.23% a year, an appraisal ratio of
0.007 and a Sharpe ratio of 0.441 against the benchmark's 0.457; its raw return rose over
CA-001-01's by 0.30% a year and its alpha fell by 0.17%, the switch restoring the market exposure
the regression charges as beta, as the card expected. Thresholds, version 4; the battery's figures
are the notebook's, [report.ipynb](report.ipynb), and the group-month gaps, the regressions, the
comparisons and the neighbours' alphas are computed apart from it, on the same closes and costs.
The theory is [TM-006](../../bank/TM-006-overconfidence-biased-self-attribution.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 100 dates, and the memory of 504 sessions holds on 50;
   147 decisions, once clustered, over 16.9 years in-sample, from the first holding on 2006-02-02.
2. **Economic edge: fails.** A Sharpe ratio of 0.441, below the benchmark's 0.457, with an alpha of
   0.03% a year; at twice the costs, 0.429 and −0.17%. Before costs the Sharpe ratio is 0.453; costs
   are 0.23% a year, 0.012 of a Sharpe unit.
3. **Significance: fails.** The probabilistic Sharpe ratio is 0.984, but the rule beats 50.4% of
   1,000 placebos, its own weights shifted in time, where 90% are needed — CA-001-01 beat 47.6% and
   TM-024-01 52.3%.
4. **Multiple testing: fails.** The alpha, as an appraisal ratio, is 0.007, against 0.63 expected
   from the best of fifty-four effective trials by luck: a deflated Sharpe ratio of 0.006.
5. **Stability: fails.** The single variant fails gates 2, 3 and 4. The block alphas: 2005–07
   −1.99% a year, 2008–09 −3.08%, 2010–14 +0.94%, 2015–19 −1.01%, 2020–22 +3.47%; two positive
   blocks of five, as CA-001-01's. Without its best year, 2022, the alpha is −0.48% a year.
6. **Robustness: passes.** The neighbours keep a median of 105% of the base's Sharpe ratio and at
   least 105% at ±25%; without the sectors, the worst cluster to lose, 94% remains; the largest
   share of the profit is XLY's, 12.3%; a day's delay keeps 102%. The neighbours' alphas, computed
   apart: `bear_window` 378 0.41% a year (appraisal ratio 0.08), 630 0.50% (0.10), 252 0.32% (0.07),
   756 0.21% (0.04); the targets a session late 0.19% (0.04). Every neighbour did better than the
   base, none by much.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.95 and an alpha of −0.82% a
   year, both above the tenth percentile of the in-sample paths (−0.24 and −3.94%).

## Verdict

The strategy stops at gate 2, and fails gates 3 to 5 as well.

## The card's refutation, clause by clause

From the first target on which a group's state is known, 2007-02-01, to the month ending at the
close of 2022-12-30, over the 572 group-months with two ranked funds or more (191 months): 125 were
in a down state, 41 of them TM-024-01's panic group-months, left out, and 84 in the down set,
against 447 others. The gap of each group's leaders to its ranked funds, both bought and held over
the month, regressed on the down-set indicator and one constant for each group: a coefficient of
+0.19% a year, a standard error of 5.08% clustered by calendar month (189 months), t +0.04.

- *A t statistic of +0.35 or above*: not met. The theory is **not refuted** in this form, and not
  proven: the down set's gap is as large as the others', not smaller.

**The test's power.** The card judged the standard error at about 3.9% a year, from about 75
down-set group-months against 460 and a gap moving by about 9% a year; it came out at 5.08%, over 84
against 447. At that error the clause refutes about 36% of the time with no effect, and about 17% at
−3% a year, the middle of the predicted range. The coefficient lies 0.6 standard errors above −3% a
year and 1.0 above −5%: the lower half of the prediction is neither shown nor excluded, and nothing
in the down set supports it.

Reported, not graded, as the card stated them:

- **Every down state**, the panic months included: −2.08% a year (4.17%, t −0.50), 125 group-months.
  **The panic months alone** against the others: −6.86% a year (7.17%, t −0.96), 41 group-months.
  What leaned the claim's way in the lab's earlier results lay in the panic months, which TM-024-01
  had read.
- **By group**, the down set's mean gap against the others', each with its standard error: the
  sectors +3.37% a year over 7 months (December 2009 to June 2010) against +0.07% over 166, a
  difference of +3.31% (10.98%); the equity markets −2.38% over 12 months (October 2009 to July
  2010, March and July 2016) against +1.34% over 162, −3.72% (4.56%); the commodities +1.27% over 65
  months (mostly March 2013 to July 2017, and July 2018 to June 2019) against +0.54% over 119,
  +0.73% (6.60%). Outside the panic months, the down states were the commodities' long fall — 65 of
  the 84 group-months — and the equity groups' slow exits from the 2008 crash; only the equity
  markets leaned the claim's way, within one standard error.
- **Hedged of the group's market with one beta for each state**: −0.11% a year (5.23%, t −0.02). The
  leaders were not defensive in the down set; the gap did not move with the state, raw or hedged.
- **The unmanaged tilt's contribution to the portfolio**: −4.53 points summed over the 125 down
  group-months — −6.30 in the panic ones, +1.77 in the down set — against +7.27 in the others.
- **Against CA-001-01**, by `lab.compare`: an alpha 0.17% a year lower (standard error 0.58%, t
  −0.29), a beta of 1.004 against 0.947, an excess return 0.30% a year higher, the bets correlated
  at 0.883. **Against TM-024-01**: 0.06% lower (0.36%, t −0.17), the bets correlated at 0.970.
  **With each rule's beta allowed to differ in the sessions in which any group was in a down
  state**, 43.8% of them: an alpha of 0.05% a year against CA-001-01's 0.28%, a difference of
  −0.23%; CA-001-01's beta fell to 0.873 in those sessions, this rule's to 0.988.
- **By period**: 2007–2013 +9.51% a year (7.02%, t +1.35, 30 down-set group-months); 2014–2022
  −9.86% (8.07%, t −1.22, 54); without the months whose target falls in 2009 −1.33% (5.51%, t
  −0.24). The two halves point opposite ways, each within about one and a quarter standard errors.
- **The holdout**, 2023 to 2025: +7.63% a year (5.61%, t +1.36), over 10 down-set group-months of
  104, the other way.
- **The alphas**: the base 0.03% a year after costs, 0.26% before; the neighbours' and the delayed
  rule's in gate 6 above. The hedged return by year: 2022 +7.3 points, 2020 +7.0, 2007 +4.2; 2021
  −5.3, 2012 −4.8, 2006 −4.8.

## What was learned

- **About the theory.** On the lab's nineteen funds from 2007 to 2022, momentum within the groups
  was no weaker after a group's market had fallen over two years than after it had not, once the
  panic months TM-024-01 had read were set aside: the gap of the leaders to their group was the same
  in both states, raw and hedged. The weakness of momentum after losses that the lab's earlier
  results had shown lay in the panic months — the crash of 2008 and the rebound of 2009, 2010, 2020
  and 2022 — which is TM-024's claim, the crash, rather than a confidence that falls with the
  market. TM-006 is not refuted in this form, the prediction's lower half not being excluded, and
  the lab's data gives it no support: outside the panics, the market's state did not move momentum.
- **About the rule.** Switching the tilt off after two years of losses raised the raw return by
  0.30% a year and lowered the alpha by 0.17%: in a long-only book, dropping the tilt restores
  exposure to the group's beaten funds, which the regression charges as beta, as TM-024-01 found.
- **About the market.** The down states outside the panics were mostly the commodities' long fall
  from 2013 to 2017, in which the commodity leaders did as well against their group as at other
  times.
- **About the lab.** The card was drawn after a reader overturned a not-testable draft, and chosen
  knowing three published splits that leaned the claim's way; its clause set aside the part already
  read, and the rest showed nothing. A form suggested by the lab's own reported measures, graded
  only where they had not looked, is a fair test — and the answer was that the published lean came
  from the months already read.

TM-006 is `tested-inconclusive`: its one strategy failed gates 2 to 5, and the theory is not refuted
in the one form the lab can test that no other verdict graded, momentum after market gains.
