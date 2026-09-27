# CA-014-02 — Rotation on the dollar's trend: verdict

**Stops at gate 4, multiple testing. Not refuted, not proven: over the sessions where the dollar's
trend and the commodity/bond ratio's held different sides, or before the ratio's rule held anything,
taken together, the side the dollar chose led — an appraisal ratio of +0.61 over those 1,563
sessions (measured to about ±0.40, 1.5 standard errors above zero), +0.65 over their ordinary
monetary regimes.** Holding each week the inflation side — energy, materials, gold and commodities —
while the dollar in euros stood below its 200-session mean, and the rate-sensitive side — staples,
health care, financials, utilities and Treasury notes — otherwise, earns a Sharpe ratio of 0.69
in-sample against 0.53 for the nine funds held in equal parts, an alpha of 3.48% a year, an
appraisal ratio of 0.49, and beats 99.0% of its placebos. That is above the predicted 0.1 to 0.25
and 0.7 to 1.75%, and three and a half times CA-014-01's appraisal ratio on the same funds and
sides, over a longer sample; but seventy-three effective trials make 0.63 the figure the best of
them would reach by luck, and the rule fails gate 4. Thresholds, version 4; the battery's figures
are the notebook's, [report.ipynb](report.ipynb), and the clause, the reported figures, the blocks,
the years and the fixed mix are computed apart from it, over gate 4's sessions, from 2005-09-27, at
the same costs. The theory is [CA-014](../../bank/CA-014-intermarket-analysis.md).

## Gate by gate

1. **Hygiene: passes.** No look-ahead on 200 dates, and no memory break on 100; 53 decisions, once
   clustered, over 17.2 years in-sample, from the first target on 2005-09-26.
2. **Economic edge: passes.** A Sharpe ratio of 0.688 against the benchmark's 0.526, an alpha of
   3.48% a year; at twice the costs, 0.667 and 3.18%. Costs are 0.34% a year, 0.021 of a Sharpe
   unit, below the predicted 0.4 to 0.5%.
3. **Significance: passes.** The probabilistic Sharpe ratio is 0.999, and the rule beats 99.0% of
   1,000 placebos, its own weights shifted in time, where 90% are needed.
4. **Multiple testing: fails.** The appraisal ratio is 0.488, against 0.629 expected from the best
   of 73 effective trials (80 in all) by luck: a deflated Sharpe ratio of 0.367, where 0.9 is
   needed.
5. **Stability: fails.** The blend of the two variants passes gates 2 and 3 and fails gate 4 (a
   deflated Sharpe ratio of 0.410). The alpha is positive in all five blocks — 2005–07 +1.1% a year,
   2008–09 +3.7%, 2010–14 +3.4%, 2015–19 +5.1%, 2020–22 +2.2% — and 3.0% a year without its best
   year, 2007. The worst variant's Sharpe ratio is 0.60.
6. **Robustness: passes.** The neighbours of the average, 150, 250, 100 and 300 sessions, keep a
   median of 91% of the base's Sharpe ratio and at least 94% at ±25%, and none holds the base's
   targets; without the sectors, the worst cluster to lose, 88% remains; the largest share of the
   profit is DBC's, 17.8%; a day's delay keeps 96%.
7. **Sealed holdout: passes.** Over 2023 to 2025, a Sharpe ratio of 0.46 and an alpha of −0.67% a
   year, both above the tenth percentile of the in-sample paths (−0.01 and −2.53%).

## The card's refutation, clause by clause

The card grades the **new sessions**: those into which the side the base held, set by its last
target before the session, differed from the side CA-014-01's rule, rebuilt over the same market,
held into it, or into which that rule held nothing, up to its first holding — 1,814 sessions from
2005-09-27 to December 2022, of which the 251 of 2022, whose outcome CA-014-01's published edge for
that year mirrors, are left out: 1,563 sessions, 6.2 years, 829 of them in the ordinary monetary
regimes (the bill rate set the session before at 0.25% a year or more). The figure is the annualised
Sharpe ratio of gate 4's daily series — the base's excess returns hedged of the nine funds' with the
whole-sample beta, 1.01 — restricted to those sessions; over the whole sample it reproduces gate 4's
0.488.

- *The base — refuted if the ratio on the new sessions is −0.1 or less and its figure over their
  ordinary regimes zero or less*: the ratio is **+0.614**, and **+0.652** over the ordinary regimes.
  The clause is not met: the theory is **not refuted**; short of gates 1 to 7, it is **not proven**.
  With 2022 kept, +0.343 and +0.324: not met either.
- *The variant "classes", gold and commodities against the notes, hedged of GLD, DBC and IEF held in
  equal parts (those of the three that trade), reset when it sets targets — refuted if the same two
  figures are −0.1 or less and zero or less*: **+0.483**, and **+0.299** over the ordinary regimes.
  The clause is not met: the dollar relations alone are **not refuted, not shown**.

**The test's power.** The base's +0.61 on the new sessions lies 1.5 standard errors above zero and
0.9 above the card's upper figure, 0.25; over their ordinary years, +0.65, 1.2 standard errors above
zero. The clause could have refuted a rule with no edge about one time in three, and it did not; it
cannot tell the dollar's edge on these sessions from the size assumed, nor from twice it.

## Reported apart

The card named these figures for the base and for the variant against its three funds; the column of
the variant against the nine funds and the alphas' row were added after the run.

| Measure, annualised Sharpe ratio of the hedged series | base, against the nine funds | variant, against GLD, DBC and IEF | variant, against the nine funds (added) |
|---|---|---|---|
| New sessions, 2022 out (the clause), 1,563 sessions | +0.614 | +0.483 | +0.505 |
| The same, ordinary regimes, 829 sessions | +0.652 | +0.299 | +0.419 |
| The whole sample, from 2005-09-27 | +0.488 | +0.466 | +0.499 |
| The whole sample, ordinary regimes | +0.365 | +0.372 | +0.513 |
| The new sessions of 2022, 251 sessions | −1.047 | −1.366 | −1.469 |
| The same, ordinary regimes, 225 sessions | −0.667 | −0.968 | −1.175 |
| New sessions with 2022, 1,814 sessions | +0.343 | +0.144 | +0.266 |
| The same, ordinary regimes | +0.324 | −0.061 | +0.110 |
| New sessions without 2008, 2009, 2012, 2014, 2015 and 2016, 1,204 sessions | +0.420 | +0.335 | +0.385 |
| The same, ordinary regimes | +0.544 | +0.299 | +0.470 |
| Alpha, whole sample, % a year (added) | 3.48 | 4.11 | 5.88 |

**Computed after the run, not stated in the card.** On CA-014-01's own record — its hedged series,
against its own benchmark, with its own beta, from 2006-11-21 — the sessions into which the two
rules held the same side, 62.4% of them, earn an appraisal ratio of +0.58, and the others −0.68: the
ratio's rule earned its edge where the dollar agreed with it, and gave most of it back where the
dollar did not.

## What was learned

- **About the theory.** In this sample the dollar's trend told which side of the markets would lead
  better than the commodity/bond ratio did, by an estimate 1.5 standard errors from zero that gate 4
  cannot tell from luck: over the new sessions the dollar's side led in every view the card named
  but 2022's own sessions — with and without the published years, and over their ordinary regimes —
  and with 2022 kept it still led, by about half as much; over the whole sample the rule's appraisal
  ratio is 0.49 against CA-014-01's 0.14. The figure pools two kinds of session, those where the two
  rules disagreed and those before the ratio's rule held anything, and was not split. Read so,
  Murphy's chain from its first link, the dollar, did no worse than from the link after it, and its
  first refutation, markets moving in no stable order, is not met in this form. The exception is
  2022, when the dollar and commodities rose together, the relation reversed: on that year's
  sessions, all of them new, the base's ratio is −1.05 and its edge −8.3%, the mirror of CA-014-01's
  published +10.2%. The card left it out because its outcome was published; that its sign was
  against the rule could be foreseen before the lock, so the exclusion favoured the rule, and with
  2022 kept the clause is still not met. The card tests Murphy's order, the dollar first; it says
  nothing of the bank's, currencies last.
- **The variant.** Gold and commodities against the notes on the dollar earned an alpha of 4.1% a
  year against its three funds, an appraisal ratio of 0.47, and 5.9% against the nine; the commodity
  fund carries 58% of its profit, the notes 22% and gold 20% — the commodity fund carrying the edge
  again, as in CA-014-01. Its figure over the ordinary regimes of the new sessions, +0.30, is half
  the base's, and turns negative once 2022 is kept; its clause is not met, but by a smaller margin
  than the base's: on the new sessions the base, sectors included, did better than the variant
  against either benchmark; why was not computed.
- **About the market.** The rule spent half its sessions on each side, and its average mix — about
  12% in each inflation fund and 10% in each rate-sensitive one — held fixed and reset each week,
  earns −0.14% a year against the nine funds: its alpha is timing, as CA-014-01's was. Its best
  years are 2007 (+12.5% of edge), 2014 (+10.7%), 2018 (+10.2%) and 2008 (+9.6%); its worst 2022
  (−8.3%), 2013 (−5.9%) and 2012 (−3.4%). The profit is spread: DBC 17.8%, energy 16.6%, utilities
  13.7%, health care 13.0%, staples 12.0%. Its beta to the nine funds is 1.01, and its tracking
  error 7.1% a year, the 7% the card took from CA-014-01's published figures.
- **The risks the card named.** The delay Murphy warns of was not measured: the rule acts on the
  dollar's current trend, and a lagged form would be a new card. The euro stood for the dollar index
  throughout; a move against the yen alone was not seen. The foreign-earnings channel, which runs
  against the rate-sensitive side, was not separated. The largest share of the profit, 17.8%, stayed
  under the 30% limit.
- **About the holdout.** Over 2023–25 the rule earned a Sharpe ratio of 0.46 and an alpha of −0.67%
  a year, above both floors. The holdout was not blind to the writer: CA-014-01's verdict had
  published its own holdout, an alpha of −5.17% and the funds' returns, gold +134% among them; the
  two rules hold the same side on about a third of its sessions; and the dollar's switches in the
  holdout, 20, were counted before the lock. Three years say little about an edge.
- **About the lab.**
  - The lab's rates were passed to strategies for this card (cd2cfaa). The audit found paper trading
    without them, fixed before the lock (b22e94c); the first closing check found a failed draw of
    the rates able to stop every papered strategy, fixed before the lock (562999f); the second found
    the docstring promising more than the job did, corrected just after the lock and before the code
    (62b0705). Each change carries its tests.
  - The audit's blocking finding set the method: a rule on the same funds, sides and pace as a
    published one is, wherever their signals agree, that one's outcome, and its new information lies
    where they disagree; the clause was moved there before the lock, and its closing check made it
    say which side a session's return is judged by.
  - Departures from the order of the work, recorded here:
    - Before the lock, the dollar's side was compared with DBC's and GLD's own 200-session trends
      and with CA-014-01's rule rebuilt. Those comparisons read in-sample prices of funds the card
      holds, and whether a fund stands above its mean is a statement about its past returns: they
      measured the mechanism's first link on the graded data. The clause needs the second comparison
      to be defined.
    - The strategy and the build plan were drafted before the lock; the drafted strategy was run on
      the in-sample market to count the new sessions, reading its targets, not its returns.
    - The dollar's switches in the holdout were counted before the lock, reading the holdout's
      exchange rates before gate 7.
    - The card's first commit held its reasoning too, and the run refused it. The three local
      commits from that one on — the card with its reasoning, a docstring change and the code — were
      reset, never pushed, and made again: the card alone, from a folder holding only it and its
      reasoning, then the docstring change, then the code with the reasoning. The card's text is the
      one first committed.

## Status

CA-014 is `tested-inconclusive`. CA-014-01, the commodity/bond ratio, stopped at gate 3 with a small
edge. CA-014-02, the dollar's trend on the same sides, stops at gate 4: an appraisal ratio of 0.49
over seventeen years and +0.61 on the new sessions, where the dollar's side differed from the
ratio's or the ratio's rule held nothing, its clause not met. It is the strongest intermarket result
in the lab's registry, but seventy-three trials leave it within what luck would give their best, and
the year the dollar and commodities rose together cost it most. No other strategy is drawn: the
bond-to-stock relations are LL-042-01's, refuted in a narrow form; commodities into equities are
CA-028's; and the bank's own order, currencies turning last, would need a rule that reads the other
markets to time the currencies, which the lab cannot hold — it trades no currency, and its two rates
give one cross.
