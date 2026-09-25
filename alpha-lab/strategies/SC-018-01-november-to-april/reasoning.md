# SC-018-01 — Equities from November to April, cash from May to October: reasoning

## Why this theory now

SC-018, the Halloween effect or "sell in May and go away", holds that equity returns have been
higher from November to April than from May to October: most of the equity premium is earned in the
winter half-year. It is a half-year seasonality, slower than the effects within the week or the
month, and the bank lists several explanations, none of which has prevailed: a cycle of optimism
about the year ahead that fades by summer (Doeswijk), seasonally high risk appetite around the New
Year shared with the January effect, summer holidays and lower participation, seasonal mood, and a
few weak Septembers and Octobers. The bank's neighbours: **SC-017**, whose SC-017-01 tested
September and October alone, two months inside this card's summer half; **SC-002** and **SC-019**,
the January effect and the January barometer, which Ilmanen relates to this one through the same
seasonal risk appetite.

**The sources.** The lab read them in the library's books; Bouman and Jacobsen (2002) and Jacobsen
and Zhang (2021), the studies that named and tested the effect across countries, are known to the
lab only through these books.

- Ilmanen (*Expected Returns*, 2011, §25.2) writes that equity returns in the US and many other
  countries have been high from November to April and low from May to October. His Figure 25.6 plots
  the US equity premium's average monthly return over the two halves from 1927 to 2009 (its caption
  misprints them as November–May and April–October; its legend and text give November–April and
  May–October): read by eye, about 0.90% a month from November to April and 0.32% from May to
  October, a gap of about 0.58% a month. His Figure 25.1, read for SC-017-01, gives the same gap
  month by month (about 0.91% against 0.32%). He finds the pattern echoed in small-cap,
  high-volatility, credit and carry strategies, and warns that several famous October crashes fell
  just before Halloween, which skeptics may read as coincidence or data mining.
- Ziemba (*Calendar Anomalies and Arbitrage*, 2012, §1.4) tests a rule on S&P 500 and Russell 2000
  futures: sell on the first trading day of May and buy on the sixth trading day before the end of
  October, cash earning the fed funds rate in between. From February 1993 to December 2011 it turned
  a dollar into $4.03 on the S&P 500 against $1.91 for buying and holding with dividends, and $5.35
  against $1.83 on the Russell 2000. Dzhabarov and Ziemba (the Zacks *Handbook of Equity Market
  Anomalies*, 2011, chapter 9) give the same rule to December 2010: $3.73 against $1.96, and $4.94
  against $2.04. Ziemba cites Bouman and Jacobsen's finding of the effect in 36 of 37 countries, the
  southern hemisphere included, which counts against the holiday explanation.

## What the lab already knew

The card cannot be blind, and says so before anything else.

- **The in-sample clause is decided before the run.** SC-017-01's verdict, published before this
  card, gives the five funds' average excess return in each calendar month from 2005 to 2022 and its
  count of sessions. Weighted by sessions, they give the base's difference, the sessions from
  November to April less those from May to October, as about +0.030% a day, known to within the
  table's rounding: about the long record's gap, and about 0.7 of the clause's standard error. The
  clause's first condition for a refutation, a difference of zero or less, is known to fail:
  in-sample, the clause can only return "not refuted". The same table implies an alpha of about 1.9%
  a year before costs at a beta of one half (three times a gap of about 0.62% a month), just
  above the top of the predicted range.
- **The neighbours and the months shifted are largely known.** From the same table, the difference
  for five months out (May to September) is about +0.035% a day, for seven (May to November)
  +0.017%, for three (May to July) about nil, for nine (May to January) +0.035%; with the months
  shifted a month earlier (April to September) +0.010%, a month later (June to November) +0.006%.
  SC-017-01's verdict also gives September's and October's difference by year and without 2008,
  which partly informs this card's.
- **The holdout is new only for this rule.** Every earlier card on the five funds opened 2023 to
  2025, and SC-017-01's verdict reports that holding cash in September and October over those years
  earned an alpha of 2.82% a year: two months of this card's summer half were weak there. The
  market's path over those years is public. Over three years the difference is measured to about
  ±0.1% a day, against a gap of about 0.03%: the holdout cannot tell the effect from none either.
- **Ziemba's futures results** cover 2005 to 2011, seven of the eighteen in-sample years.

What is not known is the placebos' rank and gates 3 to 5 and 6's other checks, which turn on the
rule's whole path rather than on monthly averages; the variant's timing, Ziemba's rule, on the lab's
funds; and the half-year split by fund. The verdict will read the in-sample clause as decided before
the run, not as evidence, and SC-018 will be `tested-inconclusive` unless a gate surprises.

Why run the card at all: the data can test the theory, so recording it as not testable would misuse
the status and hide the lab's own earlier reading rather than disclose it; the gates and the variant
are still unread; and the bank's theory would otherwise stay `untouched`.

## From the claim to a signal

- **The halves**, base: the five equity funds from November to April and cash from May to October,
  the calendar halves of Bouman and Jacobsen and of Ilmanen's figure. **Variant**: Ziemba's timing,
  sell on May's first trading day and buy on the sixth trading day before the end of October. His
  captions give the entry at the close and no hour for the exit; the lab reads them as out at the
  close of May's first session and back in at the close of the sixth-last session of October, so
  that the portfolio holds May's first session and October's last five. Both halves come from the
  sources, the variant's two readings from the lab.
- **The parameters**: the first month out, named (May), and the number of months out (six), as in
  SC-017-01, which the card reuses; and two counts of sessions, `late`, the sessions of the first
  month out still held (0 in the base, 1 in the variant), and `early`, the sessions before the end
  of the last month out from which equities are held again (0 in the base, 5 in the variant).
- **The funds**: the five equity markets the lab holds, in equal parts. The sources' evidence is on
  US indices and across countries; the foreign funds carry their markets' halves.
- **The calendar**: to be out of equities from May's first session, the rule must know on April's
  last session that the next is in May. As SC-008-01 and SC-017-01 did, it reads this from the New
  York Stock Exchange's calendar of scheduled sessions, derived from its holiday rules alone and
  copied from SC-017-01's code; the variant counts sessions on the same calendar. From 2005 to 2025
  every market session is scheduled, the month of the next scheduled session always equals the month
  of the next market session, and the variant's entry and exit sessions are market sessions every
  year. In October 2012 the five sessions it then holds include the two on which the storm closed
  the exchange, the 29th and 30th, so that it held three market sessions after entering on the 24th,
  as a follower of the rule counting on the calendar would have.
- **Targets**: set only on the sessions on which the state changes, twice a year.

No count of the market's data was made for the card beyond what SC-017-01's verdict had published:
the rule is a calendar, one exit and one entry a year, 37 clustered decisions in-sample.

Two variants, not three: the sources give two timings, the calendar halves and Ziemba's rule; a
third would be chosen by the lab.

## What the battery judges, and what to expect

**The size predicted.** The benchmark holds the five funds always. A rule in equities half of the
year has a beta of about a half; its alpha is about (6/12) × (6/12) × twelve times the gap between
the winter and summer halves' monthly returns, three times the monthly gap: at the long record's
0.58% a month, about 1.7% a year before costs, about 0.9% at half of it. Costs are about 0.1% a
year, one round trip. The rule's bets, hedged of the benchmark, move by about the benchmark's
volatility times √(1/2 × 1/2), some 11% a year: an appraisal ratio of about 0.08 to 0.16. Ziemba's
futures rule did far better from 1993 to 2011, about four points a year above buying and holding on
the S&P 500 with half the exposure. The card takes the long record's range; SC-017-01's table, as
above, puts the in-sample alpha at about 1.9% before costs at a beta of one half, just above its
top.

**The clause.** The theory is judged on the base, before costs, on the mean daily excess return of
the five funds over the sessions from November to April less that over the sessions from May to
October. Over about 18 years, some 2,220 sessions in the winter half and 2,310 in the summer half,
at a daily volatility of about 1.38% (the figure SC-017-01's run measured), the difference is
measured to about ±0.041% a day; the long record's gap would make it about 0.028% a day, some 0.7
standard errors. The theory is refuted in this form if that difference is zero or less and the base
beats half of its placebos or fewer. Any other result short of passing gates 1 to 7 is not proven,
not refuted. As above, the first condition is known to fail in-sample: a refutation is excluded
before the run.

**What a blind test would have had.** A synthetic simulation made for the card — daily returns drawn
at random, not the lab's — gives the clause's rates for a test run without prior knowledge. With no
gap left, it would refute about 47% of the time; at half the long record's gap, about 37%; at the
whole gap, about 23%. Eighteen years cannot tell the long record's gap from none, and the clause
would refute a real effect of that size about one time in four.

**What the gates can pass.** In the same simulation, an appraisal ratio of 0.7, which gate 4 needs
over some twenty trials, comes about one time in a hundred even at the whole gap, and gate 3's
placebo check passes about one time in five. "Not proven" is the expected verdict whatever the
truth.

**Measures stated before the run**, reported, not graded:

- the same difference for the variant, its sessions held against the others;
- the difference by fund and by year, and without 2008;
- the base's alpha with its months shifted a month earlier (cash from April to September) and a
  month later (cash from June to November), since gate 6 cannot move a month's name — their
  differences known, as above;
- the holdout's difference, 2023 to 2025, new for this rule only and too short to judge.

**Risks named before the run.**

- **Crises.** September and October 2008 fall in the summer half and the months from November 2008
  to February 2009 in the winter half; 2020's spring crash falls in the winter half; 2022 spans
  both: a few episodes decide an 18-year average.
- **One fund's share.** The five funds form one cluster; no fund may carry more than 30% of the
  profit.
- **The neighbours.** Five or seven months out, or months shifted, land on months the sources call
  strong or weak; gate 6 may fail without speaking against the theory. The three-month neighbour is
  known to hold about no edge.
- **A day's delay.** Gate 6 delays the rule by a session, a small change for a half-year rule.

## Choices, and the options rejected

- **Declaring the theory not testable** because its in-sample result is known: the data can test it,
  and the status would hide the lab's own reading rather than disclose it.
- **Grading the clause on the holdout** instead: three years, partly read already, would make it
  close to a coin flip.
- **A different sample to restore blindness**: the lab's data begins in 2005, and the sector funds
  share the five funds' market factor, so that they are not blind either.
- **The strong half alone against a short summer position**: the lab is long only.
- **Bitcoin**, which the bank names: the bank reports that tests there find no Halloween effect, and
  the claim is about equity markets.

## Implementation

Long only, five equity funds, each with a European (UCITS) fund that tracks it, or cash, one round
trip a year on a calendar known in advance, with the orders filled at the close of the session on
which they are set; gate 6 adds a day's delay.
