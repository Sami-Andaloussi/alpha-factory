# SC-001-01 — The equity funds out of the market over each week's first session: reasoning

## Why this theory now

SC-001, the day-of-the-week or weekend effect, holds that returns differ by weekday: in the US,
Mondays were abnormally weak and Fridays relatively strong. No single mechanism accounts for it:
the non-trading interval, speculative short sellers who close their positions before a weekend and
reopen them after, individual investors who sell more on Mondays while institutions trade less,
news released after Friday's close, and the bid-ask bounce. The effect was larger in small
capitalisations and equally weighted indices, and it is costly to trade, since it asks for two
trades a week.

**The sources.** The lab read them in the library's books.

- French (1980), on the S&P composite from 1953 to 1977, finds Monday's mean return negative and
  the other days' positive, which refutes both returns accruing in calendar time and returns
  accruing in trading time; Keim and Stambaugh (1984) extend the negative Mondays back to 1928, for
  firms of every size (as reported by the Zacks *Handbook of Equity Market Anomalies*, 2011,
  chapter 9).
- Singal (*Beyond the Random Walk*, 2003, chapter 3) defines the weekend effect as the last session
  of a week's return less the next week's first session's, whatever their weekdays, and measures it
  on all NYSE, AMEX and Nasdaq stocks from July 1962 to 2001 (his Table 3.1): 0.339% a weekend on
  the equally weighted index, from a Monday of −0.093% and a Friday of +0.246%, and nearly the same
  in every decade (0.304% in 1991–2001, the Monday then close to zero and the Friday essentially
  unaltered); 0.153% on the value weighted index, falling from 0.255% in the 1960s to −0.013% in
  1991–2001, when every weekday earned about 0.05 to 0.06%. Over 1992–2001 (his Table 3.2) the
  Russell 2000's weekend effect is 0.167%, significant over the ten years and in none of the
  two-year spans but one, and the Russell 1000's −0.057%. He explains it chiefly by speculative
  short sellers, who moved to options where options are cheap, so that the effect left the large and
  actively traded stocks; he judges it larger around long weekends, and the Russell 2000's fund,
  IWM, the best tradable vehicle, whose bid-ask spread of about 0.10% took most of the 0.17%.
- The Zacks handbook (chapter 9, its Table 9.5, 1993–2010) and Ziemba (*Calendar Anomalies and
  Arbitrage*, 2012, §1.6, its Table 1.10, 1993–2011) update the effect on S&P 500 and Russell 2000
  futures. For the S&P 500, Monday is above the average day (+0.04% and +0.03% against +0.02%),
  Tuesday the highest, Thursday about zero; the week's last session less its next first is about
  −0.03% and −0.02%. For the Russell 2000, Monday is the only negative day, −0.03% and −0.05%, gaps
  to the other days of about −0.07% and −0.09% a day, and Friday +0.04%: a weekend effect of about
  0.07% and 0.09%. Their daily standard deviations are about 1.2 to 1.4% and 1.4 to 1.6%. Both books
  summarise the cash evidence as strong for the classic samples, the effect diminished, possibly
  data snooping, and reversed in the futures markets through anticipation. The Zacks handbook adds
  that the Monday decline is strongest in stocks held least by institutions (Chan, Leung and Wang,
  2004) — against Singal, for whom the effect is larger where institutions are more active — and,
  from Chukwuogor-Ndu (2006), that in fifteen European markets from 1997 to 2004 Fridays were
  positive and Mondays mixed.
- Ilmanen (*Expected Returns*, 2011, §25.3): average equity returns were negative on Mondays, a
  regularity that disappeared soon after it became widely known in the 1970s.

The sources' samples end in 2001, 2010 and 2011: the years 2012 to 2022, nearly all of the lab's
blocks 2011–2016 and 2017–2022, lie outside all of them.

**What the lab already knows.** No verdict published by the lab reads the weekday of a return;
SC-008-01, the turn of the month on the same five funds, and MR-032-01, a weekly rule whose weeks
start on their first session, bear on other days (MR-032-01's first session held is a rank
correlation within groups, not a mean return). The card is as blind as the lab's cards get.

**The bank's neighbours.** **SC-014**, the pre-holiday effect, and **SC-024**, the overnight return
premium, are about the same closures from the other side; **SC-008** and **SC-010**, the turn of the
month and the semi-month, are calendar effects of the month. This card reads only the week.

## From the claim to a signal

- **The market**: the five equity funds of the lab, SPY, QQQ, IWM, EFA and EEM, held in equal parts,
  as SC-008-01 took them: the US large caps, growth, small caps, developed markets outside North
  America and emerging markets, all traded in New York. The benchmark is the five held always.
- **The week's first and last sessions**, Singal's Monday and Friday: the first and the last
  scheduled sessions of each calendar week, Monday to Sunday — a Monday, or a Tuesday after a Monday
  holiday; a Friday, or a Thursday before Good Friday — on the New York Stock Exchange's calendar of
  scheduled sessions derived from its holiday rules alone, as SC-008-01 built it, so that a rule
  knows ahead which session opens or closes a week without reading a price. A session's return is
  taken from the previous session's close: the first session's holds the weekend.
- **The base**: the five funds in equal parts over every session but each week's first, and the bill
  over that one: the target falls to nothing at the close of the last session before a week's first,
  and returns to the five at that first session's close. Its alpha over the five held always is its
  avoidance of Monday.
- **The variant**: the five funds over each week's last scheduled session only, the bill otherwise:
  the Friday half of the weekend effect, which Singal finds unaltered in 1991–2001 while Monday came
  close to zero.
- **A parameter for gate 6**: the count of the week's first sessions left out (the base) or last
  sessions held (the variant), 1; its neighbour 2 leaves out Monday and Tuesday, or holds Thursday
  and Friday. No in-sample week has fewer than four scheduled sessions, so the neighbour always
  changes the targets.
- **Unscheduled closures**: a scheduled session on which the exchange does not open — 2007-01-02,
  2012-10-29 and 30, 2018-12-05 in-sample, 2025-01-09 in the holdout — counts as the calendar counts
  it and is absent from the market, so that the base is out over the return that spans it.

The pace was counted before the card by a scratch script outside the repository (`pace.py`, in the
session's scratch folder) that reads the calendar and the market's dates alone: 4,531 in-sample
sessions from 2005-01-03, of which 937 are the first of their week, 848 Mondays and 89 Tuesdays; the
returns that span a week's first scheduled session, once 2005-01-03, which has none, is set aside
and the two that span a closed first session (2007-01-03, 2012-10-31) are counted, number 938,
against 3,592 others, and 122 of them span four calendar days or more; 312, 312 and 313 first
sessions fall in the blocks 2005–2010, 2011–2016 and 2017–2022. The base and the variant switch
1,877 and 1,878 times, twice a week.

## What the battery judges, and what to expect

**The size predicted — from the sources' recent samples.** Taken where they measured it last, the
sources locate the effect in small caps: the Russell 2000's weekend effect about 0.07% and 0.09% in
futures from 1993 to 2011 and 0.167% in cash over 1992–2001, its Monday about 0.07 to 0.09% a day
below its other days; the large caps' weekend effect about −0.01 to −0.06% and their Monday no lower
than their other days, or higher; Europe's Mondays mixed. The card predicts, before costs, IWM's
weekend effect at about +0.07 to +0.17% a weekend; a gap between the week's first session and the
other sessions of about −0.04 to −0.09% a day for IWM, about 0 to +0.02% for SPY and QQQ, about 0
for EFA and EEM, about −0.02 to 0% for the five funds' average. Out one session in five, the base's
alpha over the five held always is 0.2 × 0.8 of the average's gap, reversed, times 252: about 0 to
0.8% a year before costs, an appraisal ratio of about 0 to 0.1 (the timing's hedged volatility,
√(0.2 × 0.8) of about 21% a year, some 8.5%). The variant's alpha, from Fridays about +0.02% above
the other days in IWM, about −0.01% in the large caps and about 0 elsewhere, is about zero before
costs. Two switches a week at the lab's 5 basis points a side cost about 5.2% a year, which the
effect cannot pay: the card expects the base and the variant to fail gate 2, as Singal expected of
every instrument he had.

**The clause.** Judged before costs on the form of the claim the sources hold for the recent years,
the small caps', and on the effect as Singal defines it, which holds both its halves: for each pair
of a calendar week's last scheduled session and the next week's first, from the base's first held
session, IWM's return less the bill's rate over the market session whose return spans the week's
last scheduled session, less the same over the market session whose return spans the next week's
first scheduled session, each from the market's previous close; the mean over the pairs, its
standard error, the standard deviation of the pairs' differences over the square root of their
count, and its t statistic. The theory is refuted in this form if that t statistic is −0.35 or
below: IWM's week's last session no higher than its next first, beyond a third of a standard error.
Above it, short of passing gates 1 to 7, the theory is not proven, not refuted; a base that passes
gates 1 to 7 while the clause refutes leaves the theory refuted in this form. Grading Monday's gap
alone could refute while Friday stayed high, the half Singal found intact.

Of SC-001's refutation criteria, the first, Mondays no lower and Fridays no higher, is graded on IWM
through Singal's weekend effect and reported half by half and on the other funds; the second, as
large in large caps as in small, is reported through IWM's gap less SPY's; the third, the trading of
individuals and short sellers, and the fifth, less liquid stocks, are beyond the lab's data; the
fourth, the local trading week, holds one calendar here; the sixth is about crypto, not tested.

**The test's power.** With IWM's daily standard deviation about 1.55%, its overall figure in the
lab's data, and 938 pairs, the standard error of the weekend effect is about 1.55% × √2 / √937, some
0.072%. The clause then refutes about 36% of the time with no effect, 9% at +0.07% (the Zacks
handbook's), 5% at +0.09% (Ziemba's) and under 1% at +0.167% (Singal's). The logic audit's
simulations with fat-tailed and volatility-clustered daily returns kept the t statistic's
calibration. The clause keeps an effect of the predicted size from being called refuted, and cannot
tell a small one from none.

**Measures stated before the run**, reported, not graded, each session placed as the clause places
it, by the market session whose return spans the scheduled one:

- the gap of the week's first session against the other sessions, IWM's daily return less the bill's
  rate, with its standard error, the square root of the sum of each group's variance over its count;
  the same for each of the other four funds and for the five funds' average;
- the same gap for IWM's daily return less SPY's, whose standard error is about 0.025%, the bank's
  second criterion;
- the gap of the week's last session against the other sessions, and the weekend effect, for each
  fund and for the five funds' average;
- IWM's weekend effect and the average's by the blocks 2005–2010, 2011–2016 and 2017–2022, a pair
  placed by the date of its last session; over the pairs whose first session's return spans four
  calendar days or more against the others; without the pairs whose last session falls in 2008 or
  2020, which carry about a third of IWM's variance; and with both returns of each pair divided by
  the standard deviation of IWM's daily returns over the 21 market sessions before the pair's last
  session;
- the base's and the variant's alphas before and after costs.

**Risks named before the run.**

- **Costs**: two switches a week, about 5.2% a year, many times the predicted alpha; gates 2 to 4
  fail whatever the effect.
- **Crises**: 2008 and 2020 carry about a third of the in-sample variance of IWM's daily returns,
  and a few weekends in them could decide the effect's sign.
- **Gate 6**: the base holds the five four sessions in five, so each fund's share of the profit is
  its own gain; as SC-017-01 did on QQQ's 33%, it may fail on one fund's share whatever the effect.

## Choices, and the options rejected

- **IWM alone as the rule's universe**: the theory's strongest remaining form, but a universe of one
  asset cannot pass gate 6; the rule trades the five, the clause grades IWM.
- **The five funds' average as the graded measure**: the sources predict it at about zero, so that a
  refutation there would refute a claim they no longer make.
- **Monday's gap alone as the graded measure**: it is half of the bank's first criterion, and could
  refute while Friday stayed high; requiring both halves to fail would refute an effect gone only
  about 13% of the time.
- **IWM less SPY as the graded measure**: more precise, but it tests the bank's second criterion,
  not the first; it is reported.
- **Calendar Mondays**: the week's first session carries the weekend, as in Singal's definition,
  whether a Monday or a Tuesday.
- **Bitcoin**: it trades every day, and the lab reads it a day late; its weekday effects are another
  claim.

## Implementation

Long only, the five equity funds, each with a European (UCITS) fund that tracks it, or cash, targets
filled at the close of the session on which they are set; gate 6 adds a day's delay, with which the
rule sits out Tuesday's return instead of Monday's. A portfolio rebalanced weekly or monthly, orders
typed by hand, cannot hold a rule that trades twice a week: the theory is tested as a calendar
theory of the lab, and its verdict rests on the clause. The targets are known from the calendar
weeks ahead, so orders could be placed in advance; filled a day later at a European close, the rule
would sit out Tuesday rather than Monday.
