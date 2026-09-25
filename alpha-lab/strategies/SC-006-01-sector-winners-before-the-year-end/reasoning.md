# SC-006-01 — The year's winning sectors over December's last sessions: reasoning

## Why this theory now

SC-006, the December or new December effect, holds that the year's big winners rise in December
because their holders postpone selling them until January: a gain realised a few days later is
taxed almost a year later. It is the mirror image of tax-loss selling on losers, which SC-002 and
FP-026 hold, and it needs no rise of the whole market, only less selling pressure on recent winners
at the year's end; if anticipated, it can be pushed earlier.

**The source.** The lab read it in the library's books; it is the only one in the library that
measures the effect.

- Singal (*Beyond the Random Walk*, 2003, chapter 2), on all NYSE, AMEX and Nasdaq stocks from 1988
  to 2000, after the Tax Reform Act of 1986 moved mutual funds' tax year to October: winners are the
  stocks with the smallest drop from the year's highest price to the twelfth-last trading day of the
  year, roughly mid-December — his lowest decile of the potential for tax-loss selling, 1.6% below
  their high on average, high-priced but not necessarily the largest stocks (a median size of $176
  million). Over the five sessions from the close of the seventh-last trading day to the close of
  the second-last, they gained 2.16% on average, and lost 0.85% over the first five sessions of
  January: 3.01% more in December, on lower turnover in December and higher in January, as
  postponed selling predicts. Over the whole of December, large winners earned 0.163% a day against
  0.040% in January (his Table 2.4). Over the same five December sessions and years, the S&P 500's
  total return was 1.88%, about 0.3% less than the winners, in ten years of thirteen; S&P 500
  futures, which leave out the interest on cash, gained 1.56% and the Nasdaq-100 3.17% from 1988 to
  2001 (his Tables 2.5 and 2.6). He finds no explanation of the December effect other than taxes,
  expects the 2003 cut in the tax on capital gains to weaken it slightly, and expects it to be
  arbitraged away as it becomes known. The worth of deferral is the interest on the tax deferred.
- Ilmanen (*Expected Returns*, 2011, §25.2): momentum and trend-following strategies tend to
  outperform in December and to reverse in January, which he explains by tax-loss selling and window
  dressing; both predict the same sign as deferral, so a positive result here cannot isolate it. He
  also notes that the January effect now works in late December, which lifts the year's losers in
  this card's window (Singal's losers gained 1.11% in it).
- Odean, as the library's *Advances in Behavioral Finance II* reports him, finds December the only
  month in which individual investors sell losers more readily than winners — indirect support for
  the deferral of gains.

Singal's years end in 2001: all of the lab's years lie outside the source's sample.

**What the lab already knows.** SC-002-01 published IWM's return less SPY's and less QQQ's from 15
December to December's third-to-last session (+0.83% and +1.14% a year), and SPY's own (+0.86%): a
window overlapping this card's, between size classes, not between the year's winners and losers.
The card is blind to its measure, not to the market's level in those sessions, nor to QQQ trailing
SPY by about 0.3% a year over them (IWM less SPY, +0.83%, less IWM less QQQ, +1.14%), nor to the
small caps' lead; both point against the year's winners, and the growth-heavy Nasdaq-100 was
Singal's best December instrument. The momentum cards (TM-003-01, TM-002-01 and others) rank the
sector funds by past returns without a calendar. No verdict reads the year's winning sectors in
late December.

**The bank's neighbours.** **SC-002**, the January effect of small losers, and **FP-026**, tax-loss
selling, hold the other side of the same tax calendar; **SC-007**, the Santa Claus rally, holds the
whole market over the last five sessions of December and the first two of January; **TM-023**,
momentum's seasonality, holds the whole year's winners by a return ranking and a month's calendar,
where this card ranks by the drop from the high and holds five sessions. This card reads the year's
winners against the other sectors of the same market, not the market's level.

## From the claim to a signal

- **The market**: the eleven sector funds, the S&P 500 by industry, held in equal parts, the
  benchmark. A sector fund is a coarse unit for a claim about single stocks: a sector near its high
  holds many of the year's winner stocks, but others too, so that the effect is diluted. They are
  large caps, where the bank places the effect.
- **The winners**, Singal's measure: on the market's last session on or before the twelfth-last
  scheduled session of December, each sector fund that traded on the market's first session of the
  year has a drop from its highest close since that first session; the winners are the three funds
  with the smallest drop, ties at the cut all included. Ties happen only at a drop of zero, a fund
  closing at its year's high: several funds did so in five of the eighteen years, but the tie
  reached the cut only in 2021, with four winners. A fund that began trading during the year — XLRE
  in 2016, XLC in 2018 — is not ranked that year, since its stocks' high for the year may predate
  it; it is held in the benchmark and outside the window.
- **The window**, Singal's: from the close of the seventh-last scheduled session of December to the
  close of the second-last, the returns of five sessions, on the New York Stock Exchange's calendar
  of scheduled sessions derived from its holiday rules alone, as SC-008-01 built it.
- **The rule**: over the window, the winners in equal parts; outside it, the funds that trade in
  equal parts, set back to equal parts on the market's first session of each month, when the
  benchmark is set back too. Its alpha over the funds held always is the winners' return less all
  the funds' over the window, about seven tenths of the winners' return less the other funds' (eight
  elevenths with eleven funds, six ninths with nine).
- **The winners' beta.** On sector funds, a small drop from the high mostly marks a fund that moves
  little: the logic audit, reading the ranking alone, found XLP among the winners in twelve years of
  eighteen, XLU in seven and XLV in six, with betas on the sector funds' average of 0.61, 0.73 and
  0.74, against 1.39 for XLF and 1.29 for XLE; the winners less the others had a daily beta of −0.17
  on average over the year to the ranking, and −0.3 to −0.64 in six years. The market usually rises
  in the window, so that the raw difference would carry a drag of about −0.1 to −0.3% a year from
  beta alone, enough to refute half the time or more with no effect. The clause removes it, each
  year, with that year's beta measured before the ranking.
- **The parameters for gate 6**: the number of winners, 3, with its neighbours 2 and 4 at both
  steps; the window's entry, the seventh-last session (−7), with its neighbours −5 and −9, −4 and
  −10; its exit, the second-last (−2), with its neighbours −1 and −3 at both steps. All change the
  targets, and they pass the card's checks.
- **The memory**: the ranking at the entry reads back to the year's first session, at most about 245
  sessions (248 for the neighbour at −4); the default memory of 252 covers it.

The windows were counted before the card by a scratch script outside the repository (`pace.py`, in
the session's scratch folder) that reads the calendar and the market's dates alone: eighteen windows
from 2005 to 2022, each of five sessions (in 2005, ranked on 2005-12-14, entered at the close of
2005-12-21 and left at the close of 2005-12-29); nine funds ranked until 2016, ten in 2017 and 2018,
eleven from 2019. Gate 1 counts about 37 to 39 clustered decisions, against 30 needed: the monthly
resets set the same targets and count none, and the window's entry and exit count as two only
because they are five sessions apart, the clustering gap.

## What the battery judges, and what to expect

**The size predicted — a judgment, from the source.** Singal's winner stocks gained about 0.3% more
than the S&P 500's total return over the window from 1988 to 2000. A sector fund dilutes its winners
among its other stocks; the 2003 cut in the tax on capital gains, which Singal expected to weaken
the effect, the bill's rate near zero in 2009–2015 and 2020–2021, which makes deferral worth little,
and the effect's publication all argue for less. The card judges the winners' return less the other
sector funds', adjusted for beta, at about 0 to +0.25% a year from 2005 to 2022, positive in
somewhat more than half the years. The rule's alpha, about seven tenths of it, is about 0 to 0.18% a
year before costs of about 0.14% a year (two moves of about three quarters of the portfolio at 5
basis points a side, and the monthly resets, which the benchmark pays too), so about −0.14 to +0.04%
after costs: the card expects the rule to fail gate 2 or 3. Its tracking error comes from five
sessions a year, about 1% a year, for an appraisal ratio of about 0 to 0.2 before costs; gate 4,
which needs a ratio near 0.95, is out of reach, and the verdict's content will rest on the clause.

**The clause.** Judged before costs: for each of the eighteen Decembers from 2005 to 2022, the
winners' average return, the three funds with the smallest drop as the rule ranks them, ties at the
cut all included, less the average return of the other funds ranked, less b times the average return
of all the funds ranked, each from the close of the seventh-last scheduled session of December to
the close of the second-last, b being the least-squares slope, with an intercept, of the daily
difference between the winners' average return and the others' on the daily average of all the funds
ranked, over that year's sessions from the market's first to the ranking session; the mean over the
years, its standard error, the standard deviation over the years (with n − 1) over the square root
of eighteen, and its t statistic. The theory is refuted in this form if that t statistic is −0.35 or
below. Above it, short of passing gates 1 to 7, it is not proven, not refuted; a base that passes
gates 1 to 7 while the clause refutes leaves the theory refuted in this form.

Of SC-006's refutation criteria, the first, no December outperformance of the year's winners, is
graded; the fourth, a December rise spread over the whole market, is reported through the funds' own
return over the window; the second, strength unrelated to the size of the unrealised gains or
present where gains are not taxed, is reported in part through the years whose winners had gains to
defer and the years of a meaningful bill rate, and is otherwise beyond the lab's data, as is the
third, the winners' sales in early January, which is reported only through their returns in
January's first five sessions.

**The test's power.** Three sector funds less the rest have an overall daily standard deviation of
about 0.57 to 0.61% (random thirds over all in-sample sessions, figures read by the pace script and
the logic audit, not of any window; a spread chosen by the signal is about 7% more volatile); over
five sessions, about 1.3 to 1.4%, so the standard error of the mean over eighteen years is about
0.30 to 0.35%. The clause then refutes about 36% of the time with no effect (a Student t with
seventeen degrees of freedom), about 10% at +0.3%, and about 3% at +0.5%; fat-tailed synthetic years
kept these rates. It cannot tell an effect of the predicted size from none.

**Measures stated before the run**, reported, not graded, each return compounded over its sessions:

- the graded difference year by year, with the years positive, and b year by year; the same
  difference without the beta adjustment;
- the graded difference in the years when the bill's rate on the ranking session was 1% a year or
  more, against the others, and in the years whose winners had risen from the year's first session
  to the ranking session, against the others;
- the winners' return less the other funds' over January's first five scheduled sessions, from the
  close of December's last scheduled session to the close of January's fifth, over the seventeen
  Decembers 2005 to 2021 whose Januaries are in-sample, and the December window's difference less
  it, Singal's own contrast; the 2022 December's January apart, after the run;
- the losers' return, the three funds with the largest drop, ties at the cut all included, less the
  other funds' over the window and over January's first five sessions — the tax-loss side;
- the ranked funds' average return over the window less the bill's, the market's own;
- the winners' return less the other funds' from the close of the ranking session to the close of
  December's last scheduled session;
- the winners' average drop from their high and the other funds', year by year;
- the rule's alpha before and after costs, and the neighbours' and the one-day-late rule's alphas
  and appraisal ratios, since gate 6 compares Sharpe ratios that are the benchmark's for a tilt this
  small.

**Risks named before the run.**

- **The winners' low beta**: removed from the clause, not from the rule, whose alpha the battery
  measures against the benchmark with its own beta over the whole sample.
- **Few years and a coarse unit**: eighteen windows of five sessions, and sectors in place of single
  stocks; a sector's news in a window weighs as much as the effect.
- **Momentum's crashes**: a year's winners can reverse in a rebound, as in late 2008 and 2009; in a
  year like 2008, when every sector stood 20 to 60% below its high, the winners had no gains to
  defer.
- **Gates 2 to 4**: costs about equal to the predicted alpha, and gates 3 and 4 out of reach at that
  size, as SC-002-01's smaller tilt showed.
- **Gate 6**: the monthly resets keep the equal weights from drifting; equal-weight sector cards
  gave the largest share 13 to 17% of the profit (XLK in MR-032-01 and LL-023-01, XLY in CA-006-01).

## Choices, and the options rejected

- **The broad equity funds, or the whole universe**: the claim is about the year's winners within a
  market; drops from the high are not comparable across volatilities, bond funds sit near their
  highs by construction, and the broad five mix countries with IWM's small-cap effect of the
  opposite sign. The sector funds are the lab's cross-section of one market.
- **A share of the funds rather than a count**: nine to eleven funds are ranked; three is a third of
  nine and about a quarter of eleven, and a count keeps gate 6's neighbours simple.
- **The winners alone in the window and cash outside it, or all of December**: they would time the
  market's level; the five sessions are Singal's, where the effect concentrated.
- **Ranking on the year's return rather than the drop from the high**: the drop is Singal's measure,
  his potential for tax-loss selling, the winners the funds least exposed to it; the year's return
  would measure a January holder's gain more directly, but is not the source's.
- **The raw difference as the graded measure**: its beta drag on low-beta winners would refute a
  theory with no effect half the time or more; it is reported.

## Implementation

Long only, the eleven sector funds, each with a European (UCITS) fund that tracks it; two orders in
the last days of each year on sessions known ahead, and a monthly reset. A weekly portfolio holds it
only if it places the two orders on those sessions; a monthly one cannot: a calendar effect enters a
portfolio only if it passes the battery. The targets are filled at the close of the session on which
they are set; gate 6 adds a day's delay.
