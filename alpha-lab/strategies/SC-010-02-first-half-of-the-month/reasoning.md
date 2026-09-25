# SC-010-02 — The equity funds over the first half of the trading month: reasoning

## Why a second card

SC-010-02 is SC-010-01's hypothesis, unchanged, under a new id. SC-010-01's lock commit held a card
whose prediction had lost a line break in an edit, so that it did not parse; the lab's check refused
it, but the refusal did not stop the commit, and the line break was restored in a second commit. A
card changed after its lock is a new card, and the run refused SC-010-01: it never ran and has no
trial. The hook `tools/hooks/pre-commit` now runs the check on every card a commit stages. This card
differs from SC-010-01's by its id and its parent alone; its reasoning is SC-010-01's, and so are
its logic audit and closing check, the closing check's fixes applied after it and checked once more
before this card's lock. SC-010-01's code, SC-008-01's rule with only its description changed, was
written and committed before this card's lock; this card's code is that file copied after the lock,
the hypothesis unchanged — a departure from the order of the work, written in the verdict.

## Why this theory now

SC-010, the semi-month effect, holds that returns are higher in the first half of the month than in
the second: Ariel's version puts most of the equity return in the last session of the previous month
and the first half of the next, the second half close to zero. It extends the turn of the month: the
strong segment is wider than a few sessions around the change of month, and the explanations named
are composite — cash received at the start of the month, individuals investing their income,
rebalancing routines, macroeconomic releases, and, in Japan, flows received from the 20th to the
25th deployed over several sessions. The bank's second refutation criterion is the one that
separates it from the turn of the month: a difference that disappears once the turn's few sessions
are removed.

**The sources.** The lab read them in the library's books.

- Ariel, in his own chapter of Dimson's *Stock Market Anomalies* (1988; the paper, 1987), on the
  CRSP equally and value weighted indices from 1963 to 1981: a "trading month" runs from a month's
  last session to the next month's second-to-last, split evenly in two, the odd middle session to
  the last half. The first half's days averaged 0.144% against 0.004% for the last half's on the
  equally weighted index (t 6.07), 0.085% against −0.013% on the value weighted (t 4.34), with
  virtually identical standard deviations; the first nine sessions compounded 1.411% and 0.826% a
  month against −0.021% and −0.182% for the last nine; the first half led in 155 and 150 of 228
  months, in every subperiod; over the nineteen years the first halves compounded to 2,552% and
  565%, the last halves to −0.25% and −33.8%. He rules out the release of information as the cause,
  the variance being the same in both halves, and suggests monthly buying programmes of large
  investors and pension contributions.
- Lakonishok and Smidt (1988), on the Dow Jones Industrials from 1897 to 1986, without dividends,
  with calendar halves (the first to the fifteenth day of the month, or to the next session when the
  fifteenth is not one): the first half beat the second by 0.237% a month on average, far less than
  Ariel's 1%; both halves rose; the difference was not significant by the t test in any of their
  ten periods, practically nil from 1976 to May 1986 (0.029%), though the first half was higher in
  55.4% of months, significant at 1% by the sign test. Ariel's result, they conclude, came partly
  from his period and partly from counting the previous month's last session in the first half. By
  session, −0.032% a day from −9 to −5 and −0.001% from +5 to +9, while the four sessions from −1 to
  +3 rose 0.473%.
- Hensel, Sick and Ziemba, in Keim and Ziemba's *Security Market Imperfections in Worldwide Equity
  Markets* (2000), on the S&P 500 from 1928 to 1993, read Ariel's halves as fixed segments, as Ogden
  (1990) does — the turn of the month from −1 to +4, the first half from −1 to +9, the rest of the
  month from +10 to −2: 0.1236% a day at the turn (t 5.94 against the average of 0.0186%), 0.0703%
  over the first half (t 4.13), −0.0235% over the rest of the month (t −3.71), so that the second
  week, +5 to +9, averaged about 0.017% a day. Their postscript on July 1993 to December 1996 found
  the rest of the month rising too, the turn and first-half strategies behind the index, nothing
  significant. Hensel, Sick and Ziemba (1994), as Ziemba reports them, put about a third of the
  month's gain on +5 to +9 from 1982 to 1992; Hensel and Ziemba (1996), reprinted in Ziemba's book,
  0.07% a day in the first half and −0.02% in the second.
- Ziemba's update on S&P 500 and Russell 2000 futures (*Calendar Anomalies and Arbitrage*, 2012,
  §1.10, Table A.8), by session of the month: from 1993 to 2011, the second week, +5 to +9, averaged
  about 0.00% and −0.03% a day, the rest of the month, +10 to −2, about +0.02% and +0.04%, gaps of
  −0.026% and −0.068%; from 2004 to 2011, years that overlap the lab's 2005 to 2011, gaps of −0.016%
  and −0.091%; sessions −4 and −3 among the strongest, −2 flat on the S&P 500. The first half beat
  the second by +0.002% and −0.025% a day on the S&P 500 and Russell 2000 from 1993 to 2011. In
  Japan, from 1949 to 1988 (Ziemba, 1991), the turn ran from −5 to +2, with +3 to +7 the rest of the
  first half, "all the gains" in the first half.

Mills and Coutts (1995), on the London indices, is not in the library. Weighted as the three US
funds are, two parts large caps to one part small, the futures put the second week about 0.04% a day
below the rest of the month, in both of their samples, the only ones that overlap the lab's years;
2012 to 2022 lie outside all the sources.

**What the lab already knows, and is not blind to.**

- SC-008-01 published, for the five funds, the means by session of the month from −4 to +4 (−4
  +0.229%, −3 +0.118%, −2 +0.123%, −1 −0.059%, +1 +0.215%, +2 +0.102%, +3 −0.009%, +4 −0.015%), and
  its span from −5 to +2 at 0.0970% a day against 0.0035% over the other sessions.
- SC-009-01 published, for the three US funds, the gap of each session from −10 to +3 against its
  mid-month group, the sessions from +6 to the eleventh-last (0.0515% a day), and for the five funds
  in part. Those gaps fix 1,942 of this card's 2,373 second-half returns at an average of 0.011% a
  day below the mid-month; the mid-month group pools 864 of the 1,080 second-week returns with 431
  second-half ones, from +10 to −11. Only session +5, and the split of the mid-month between +6 to
  +9 and +10 to −11, are unpublished.
- SC-014-01's sessions before holidays are inside those figures already: 86 of the 91 pre-holiday
  sessions of the second half, and 102 of its 109 third sessions before a holiday, lie from −10 to
  −2.
- SC-002-01 published IWM less SPY in the second half of December, about 0.10% a day over some 144
  second-half sessions, which tilts the reported IWM-less-SPY gap by about −0.006%.

Were the unpublished parts alike, the graded gap would be about +0.009% a day, 0.18 of a standard
error toward the second week. With their own noise, about 0.036% a day, the clause refutes about 22%
of the time with no further effect (about 30% taken unconditionally at that centre), not 36%. The
reported gap without −5 to −2 is fixed before the run at about +0.048% a day, t about +0.9, and the
turn against the second half, for the US funds, at about +0.005% plus session +4's share and that of
the mid-month's split. The card's prediction is taken from the sources.

**The bank's neighbours.** **SC-008**, the turn of the month, which this theory extends; **SC-009**,
the payday cycle, its explanation; **SC-011**, announcement clustering, `not-testable` in the lab,
which is this theory's fourth criterion; **SC-012**, institutions' rebalancing windows. This card
reads the first half of the month, and grades what it adds to the turn.

## From the claim to a signal

- **The market**: the lab's five equity funds, SPY, QQQ, IWM, EFA and EEM, in equal parts, as
  SC-008-01 took them. The clause grades the three US funds' average, the market of every source but
  Ziemba's Japanese one; the five funds' average is reported, and the battery holds the five.
- **The calendar**: SC-008-01's calendar of scheduled sessions, derived from the New York Stock
  Exchange's holiday rules alone; the last scheduled session of a month is −1, the one before it −2,
  the first of a month +1, the next +2. A session's return is taken from the previous session's
  close, and placed on the scheduled sessions it spans.
- **The halves**, Hensel, Sick and Ziemba's fixed reading of Ariel's, and Ogden's: the first half
  from −1 to +9, the turn from −1 to +4, the second week from +5 to +9, the rest of the month, the
  second half, from +10 to −2. It matches Ariel's even split in 120 of the 216 in-sample months;
  in 71 his first half takes in +10 as well, in 25 it ends at +8. Ariel's own halves are reported.
- **The rule**: SC-008-01's rule with the first half as its window — the five funds in equal parts
  over the sessions from −1 to +9, and the bill over the rest of the month.
- **The parameters for gate 6**: SC-008-01's, the window's first session counted back from the
  month's last, `start` −1, with its neighbour −2 at both steps; its last session counted from the
  month's first, `end` 9, with 7 and 11 at ±25% and 4 and 14 at ±50%. All change the targets.

The sessions were counted before the card by a scratch script outside the repository (`pace.py`, in
the session's scratch folder) that reads the calendar and the market's dates alone, and the logic
audit confirmed them: 2,156 returns held in-sample, 432 switches, as many for every neighbour; 1,080
second-week returns and 2,373 second-half ones, the return of 2012-10-31, which spans −3, −2 and −1
after the closures of 29 and 30 October, left out as spanning a session outside its group; 2,313
and 2,217 returns in Lakonishok and Smidt's calendar halves.

## What the battery judges, and what to expect

**The size predicted — a judgment, from the sources.** The second week beat the rest of the month by
about 0.04% a day on the S&P 500 from 1928 to 1993 and fell about 0.04% a day short of it on the
futures, weighted as the three funds, from 1993 to 2011 and from 2004 to 2011, the only samples that
overlap the lab's years. The card judges the three US funds' second week at about −0.06 to +0.04% a
day against the second half from 2005 to 2022: the theory's positive gap at the top, the recent
evidence near the lower end, which the Russell 2000's gaps, −0.068% and −0.091%, set.

**The rule.** In the market 120 sessions a year, the rule's alpha over the five funds held always is
about 120 times the first half's daily excess return less 0.476 of the funds' premium. On the
futures' halves, about +0.2% a year for the S&P 500 and −1.6% for the Russell 2000 before costs. At
the lab's published figures, SC-008-01's sessions from −1 to +4 sum to 0.234% a month, 2.8% a year,
and the hedge charges 0.476 of the published 8.7% premium, 4.1%: the alpha before costs is about
−1.3% plus 0.6% for each 0.01% a day of the five funds' second-week mean, before costs of about 1.2%
a year (24 switches of the whole portfolio at 5 basis points a side). With the second half near
0.043% a day, as the published figures put it for the US funds, the judged gap means a second-week
mean of about −0.02 to +0.08% a day, and an alpha of about −2.5 to +3.5% a year before costs, an
appraisal ratio of about −0.35 to +0.2 after costs; about −1 to +2% and −0.2 to +0.07 at the range's
centre. A Sharpe ratio of 0.4 needs a second-week mean of about 0.074% a day, twice the funds'
all-session mean: the card expects the rule to fail gate 2 at the range's centre; at its top the
second week would reach gate 2's threshold.

**The clause.** Judged before costs: over the in-sample sessions from the base's first held, the
three US funds' (SPY, QQQ, IWM) average daily return less the bill's rate, each from the market's
previous close; the mean over the sessions whose return spans a scheduled session from +5 to +9 of
its month, less the mean over the sessions whose return spans a scheduled session from +10 of a
month to −2 of that month, a return spanning a scheduled session outside its group left out, the
same rule for every gap reported, with the standard error of that difference, the square root of the
sum of each group's variance over its count, and its t statistic. The theory is refuted in this form
if that t statistic is −0.35 or below: the first half, the turn's sessions removed, no stronger than
the second half. Above it, short of passing gates 1 to 7, it is not proven, not refuted; a base that
passes gates 1 to 7 while the clause refutes leaves the theory refuted in this form.

Of SC-010's refutation criteria, the second, a difference that disappears once the turn's sessions
are removed, is graded, since it is the one that tells this theory from the turn of the month; the
first, a first half no higher than the second, is reported, in Hensel, Sick and Ziemba's halves,
Ariel's and Lakonishok and Smidt's, and a reported first-criterion gap at −0.35 standard errors or
below would be written as the first criterion met in that form, the grade resting on the second. The
third, a window in Japan no longer than in the United States, and the fourth, a link to
announcements, income and rebalancing flows, need data the lab does not have.

**The test's power.** At a daily standard deviation of about 1.33% for the three US funds' average
over all in-sample sessions, and 1,080 second-week sessions against 2,373 second-half ones, the
standard error of the difference is about 0.049% a day. The clause then refutes about 36% of the
time with no effect, about 22% at +0.02% a day and about 12% at +0.04%, and about 52% at −0.02%;
given the published figures, about 22%, 9%, 3% and 42%. It cannot tell the judged gap from none.

**Measures stated before the run**, reported, not graded, each gap with the standard error from the
two groups' variances, for the three US funds' average unless stated:

- the same gap for each of the five funds, for the five funds' average, and for IWM less SPY;
- the second week against the part of the second half that no verdict has published, +10 to −11;
- the first half, −1 to +9, against the second half, for the US funds' and the five funds' averages;
  Ariel's halves, each trading month from −1 to the next month's −2 split evenly, the odd middle
  session to the last half; and Lakonishok and Smidt's calendar halves;
- the turn, −1 to +4, and each session from +5 to +9, against the second half;
- the second week against the second half without its sessions from −5 to −2;
- the gap over 2005–2011, inside the futures' years, and 2012–2022, outside every source; and
  without 2008;
- the rule's alpha before and after costs, and the neighbours' and the one-day-late rule's alphas
  and appraisal ratios.

**Risks named before the run.**

- **Gate 2**: the rule leaves out the week before the turn, which SC-008-01 found strong, and holds
  the second week, which the recent sources find flat.
- **Costs**: 24 switches a year, about 1.2% a year.
- **Gate 5**: the alpha without its best year; SC-008-01's span drew half its edge from October and
  November 2008.
- **Gate 6**: the neighbours move the window's end by two to five sessions; the −50% neighbour,
  `end` 4, is the turn alone, so the gate partly reads the claim itself; the start's neighbour takes
  in −2. The five funds are held together over half the sessions; EEM carried 41% of SC-008-01's
  profit, above 30%.

## Choices, and the options rejected

- **Grading the second week rather than the halves**: the halves hold the turn, which SC-008-01 has
  tested; only the second week tells the semi-month effect from it, as the bank's second criterion
  says.
- **Fixed halves rather than Ariel's even split**: Hensel, Sick and Ziemba, Ogden and Ziemba's
  futures tables read the halves as fixed segments, which the sources after Ariel measured; a fixed
  end also gives gate 6 a count to move. Ariel's split, knowable ahead from the same calendar, and
  Lakonishok and Smidt's calendar halves are reported.
- **Japan's longer window**: the lab holds no Japanese fund; EFA's share of Japan is not a test of
  it.

## Implementation

Long only, the five equity funds, each with a European (UCITS) fund that tracks it, or cash; 24
orders a year on sessions known ahead. A weekly portfolio holds it only if it places the two orders
on those sessions; a monthly one cannot: a calendar effect enters a portfolio only if it passes the
battery. The targets are filled at the close of the session on which they are set; gate 6 adds a
day's delay.
