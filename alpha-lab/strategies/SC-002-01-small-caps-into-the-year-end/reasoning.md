# SC-002-01 — The small caps for the S&P 500 from mid-December: reasoning

## Why this theory now

SC-002, the January or turn-of-the-year effect, holds that small capitalisations, and often the
previous year's losers, outperform large ones around the turn of the year: historically in January,
above all its first days. The forces named are several: tax-loss selling of losers in December and
their buying back in January, window dressing and the rebalancing of delegated managers, new money
at the start of the year, and illiquidity. Once the effect was known and could be traded through
small-minus-large index futures, part of it moved earlier, into the second half of December. The
effect is irregular from year to year and costly to trade in the small stocks themselves.

**The sources.** The lab read them in the library's books.

- Booth and Keim ("Is there still a January effect?", in Keim and Ziemba, *Security Market
  Imperfections in Worldwide Equity Markets*, 2000, chapter 8): the smallest NYSE decile less the
  largest earned 10.8% a month in January against −0.10% in the other months from 1926 to 1981;
  from 1982 to 1995 the January premium was still 4.48% (t 2.83) on the decile portfolios, but 2.00%
  (t 1.68) on a live small-cap fund, which excludes the lowest-priced and least liquid stocks that
  carry much of the effect.
- Hensel and Ziemba (same book, chapter 9): on monthly CRSP data, the smallest quintile beat the
  largest by 2.47% a month in the Januaries of 1983 to 1998, less consistently than before, while
  large caps beat small ones in December over 1927–97 and after 1982 — little evidence of the effect
  moving into December in the cash market's monthly returns. Their daily series show a small-cap
  advantage from about the seventh session before the turn of the year to the fifth after it, which
  in the 1990s, in futures, lay solely in the second half of December; the last session of December
  (−1) gained in the cash spread but lost in futures once anticipation set in.
- Singal (*Beyond the Random Walk*, 2003, chapter 2), from 1963 to 2001: small losers earned about
  1% a day in January and lost in October to December, while the whole market's January was not
  special in value-weighted returns (0.070% a day against 0.053% on average); he judges the January
  effect not arbitrageable with the instruments of his time, a matter of tax-loss selling in small
  losers. He also measures the December strength of large winners (SC-006): over the last five
  sessions of December before its last, from 1988 to 2001, +3.17% for the Nasdaq-100 against +1.56%
  for S&P 500 futures and +1.88% for the index (+2.00% for an index fund), the gap largest in 2000
  (11.51% against 5.51%).
- Ziemba (*Calendar Anomalies and Arbitrage*, 2012, §1.2 and §1.2.1; its text to 2010, without the
  tables, also in the Zacks *Handbook of Equity Market Anomalies*, 2011, chapter 9): Clark and
  Ziemba (1987) bought a small-minus-large futures spread from 15 December and sold it on 15
  January, fourteen winning turns of the year from 1982–83 to 1995–96; Rendon and Ziemba (2007) and
  the update to 2011 find the Russell 2000 minus S&P 500 futures spread positive in December and
  negative in January, and write of a large-cap advantage in the second half of January. Over the
  eighteen turns of the year from 1993–94 to 2010–11 (his Table 1.1), the spread gained from 15
  December to the third-to-last session of December (−3) in every year, a mean of 8.77 index points
  against a standard deviation of 8.86, a t statistic of about 4.2 over the eighteen years; it lost
  a mean of 2.03 points from (−1) to 15 January and gained 0.99 from 15 January to the month's end.
  Ziemba concludes, from Rendon and Ziemba's twelve turns to 2004–05, that the trade should be
  unwound at the (−3) session; from his Tables 1.1 and 1.3, the futures spread from (−3) to (−1)
  averaged about zero over the twelve turns to 2004–05 that both tables hold. The table counts
  points of the spread, not percentages, its two legs unequal in dollars.
- Easterday, Sen and Stephan (2008) and Haug and Hirschey (2006), as Ziemba reports them, and
  Ilmanen (*Expected Returns*, 2011, §25.2), whose small-cap premium stays much higher in January
  over the forty years to about 2010 and who notes that the effect has been known to work in late
  December, find the January effect still robust in small firms' cash returns; Booth and Keim place
  much of it in the microcaps that the Russell 2000 and IWM leave out.

The sources' samples end in 1995, 1998, 2001 and 2011: the lab's turns of the year from 2012–13 to
2022–23 lie outside all of them, and those from 2005–06 to 2011–12 are in Ziemba's data.

**What the lab already knows.** No verdict published by the lab reads IWM against SPY around the
turn of the year. SC-017-01 published the five equity funds' average daily return in December
(+0.054%) and January (−0.016%), the market's level, not the spread; SC-008-01 and SC-001-01 read
the turn of each month and the weekdays of the same funds together. The card is as blind as the
lab's cards get.

**The bank's neighbours.** **SC-006**, the December effect of large winners, which Singal places in
the last days of December and strongest in the Nasdaq-100; **SC-007**, the Santa Claus rally of the
whole market in the last five sessions of the year and the first two of the next; **FP-026**,
tax-loss selling; **FP-018**, window dressing; **SC-008**, the turn of the month, of which the turn
of the year is a case. This card reads small caps against the S&P 500, not the market's level.

## From the claim to a signal

- **The market**: the five equity funds of the lab, SPY, QQQ, IWM, EFA and EEM, held in equal parts,
  the benchmark, as the lab's calendar cards took them. IWM is the Russell 2000, the small-cap leg
  of the sources' futures spread; SPY is the S&P 500, its large-cap leg.
- **The window**, from the sources' dates: from the close of the first scheduled session on or after
  15 December to the close of the third-to-last scheduled session of December, on the New York Stock
  Exchange's calendar of scheduled sessions derived from its holiday rules alone, as SC-008-01 built
  it. A window holds eight or nine sessions' returns.
- **The rule**: over the window, SPY's fifth moves to IWM, so that the portfolio holds IWM at two
  fifths and QQQ, EFA and EEM at a fifth each; outside the windows, the five in equal parts, set
  back to equal parts on the market's first session of each month, when the benchmark is set back
  too. It is the long-only form of the sources' spread, long the Russell 2000 and short the S&P 500,
  and its alpha over the five held always is a fifth of IWM's return less SPY's over the windows.
  QQQ stays at its fifth: its December strength is SC-006's, of the opposite sign, and no source
  measured it against the Russell 2000.
- **One variant, the base**: Clark and Ziemba's original rule, to 15 January, would add the first
  half of January, which the sources' latest years find lost to the large caps; it could only lower
  the blend that gate 5 judges, and its half-month is reported instead.
- **The parameters for gate 6**: the day of December from which the window starts, 15, with its
  neighbours 11 and 19, 8 and 22; the session of December at which it ends, counted back from the
  last, −3, with its neighbours −2 and −4 at both steps.

The pace was counted before the card by a scratch script outside the repository (`pace.py`, in the
session's scratch folder) that reads the calendar and the market's dates alone: eighteen windows,
from 2005–06 to 2022–23, holding 146 sessions' returns in all, eight or nine each (in 2005, from
2005-12-16 to 2005-12-28; in 2022, from 2022-12-16 to 2022-12-28, inside the in-sample years), with
two switches a year. The neighbours hold 198, 96, 236 and 56 sessions (start 11, 19, 8, 22) and 164
and 128 (end −2, −4). No unscheduled closure falls in a window.

## What the battery judges, and what to expect

**The size predicted — a judgment, from the sources.** Ziemba's spread gained in all eighteen turns
of the year from 1993 to 2011 between 15 December and (−3), its mean about one standard deviation
across years. Read on the Russell 2000's level in those years, about 250 to 800 points, 8.77 points
is roughly 1 to 2% — rough: the table counts the spread's index points, its legs were not equal in
dollars (the S&P 500 leg 0.45 to 0.61 of the trade weights), and the (−3) exit was chosen on the
turns to 2004–05, twelve of the table's eighteen. The six later turns, 2005–06 to 2010–11, average
10.7 points, three of them in the crisis of 2007 to 2009. Against that, Hensel and Ziemba found no
move into December in the cash market's monthly returns. The card judges that IWM's return less
SPY's over the window is about +0.5 to +1.5% a year in 2005–2022, less than in the futures of the
sources' years, since the effect is known and traded, and positive in most years. The rule's alpha
is a fifth of it, about 0.1 to 0.3% a year, before costs of about 0.04% a year (two moves of a fifth
of the portfolio at 5 basis points a side, and the monthly resets, which the benchmark pays too).
Its tracking error comes from eight sessions a year: at a daily standard deviation of about 0.68%
for IWM less SPY, a fifth of it over eight sessions is about 0.4% a year, so the appraisal ratio
would be about 0.25 to 0.8, and the Sharpe ratio about the benchmark's.

**The clause.** Judged before costs, on the effect's form in the sources' latest years, the
migration into December: for each of the eighteen turns of the year from 2005–06 to 2022–23, IWM's
return less SPY's from the close of the first scheduled session on or after 15 December to the close
of the third-to-last scheduled session of December, each compounded over the window's sessions; the
mean over the years, its standard error, the standard deviation over the years (with n − 1) over the
square root of eighteen, and its t statistic. The theory is refuted in this form if that t statistic
is −0.35 or below. Above it, short of passing gates 1 to 7, it is not proven, not refuted; a base
that passes gates 1 to 7 while the clause refutes leaves the theory refuted in this form.

Of SC-002's refutation criteria, the fourth, no shift into late December, is graded; the first, no
excess return for small caps in January or its first days, is reported through IWM less SPY over the
first half of January and over the month; the second, as large in large caps as in small, is the
measure itself, IWM against SPY; the fifth, a broad rally without concentration in small caps, is
reported through SPY's own return over the window and through IWM less SPY scaled by IWM's beta; the
third, the tax calendar, holds one calendar here and is not tested; the past losers within the small
caps are beyond the lab's funds.

**The test's power.** At a standard deviation of IWM less SPY over a window of about 1.7 to 1.9%
(0.68% a day over eight sessions, the funds' overall figure, a little less over non-overlapping
blocks), the standard error of the mean over eighteen years is about 0.41 to 0.46%. The clause then
refutes about 36% of the time with no effect (a Student t with seventeen degrees of freedom), about
7% at +0.5%, and under 1% at +1%; it would find an effect of 1% significant at the 5% level about
two times in three. The logic audit's simulations, with each year's volatility drawn from the lab's
yearly figures and fat tails, kept these rates: the t statistic uses the years' own spread.

**Measures stated before the run**, reported, not graded, each return compounded over its sessions:

- IWM less SPY over the window, year by year, and the number of years positive; IWM less 1.13 times
  SPY, IWM's beta on SPY from the in-sample daily returns; IWM less QQQ;
- over the seventeen turns 2005–06 to 2021–22, whose Januaries are in-sample, IWM less SPY from the
  close of the last scheduled session of December (−1) to the close of the tenth scheduled session
  of January, and over the whole of January, from (−1) to January's last session, with their means,
  standard errors and years positive — the classic effect; the 2022–23 turn's January reported
  apart, after the run;
- IWM less SPY from the close of the window's end to the close of (−1), the last sessions of
  December;
- SPY's and IWM's own returns over the window less the bill's;
- the graded mean over the turns 2005–06 to 2011–12, inside Ziemba's data, and 2012–13 to 2022–23,
  outside it;
- the rule's alpha before and after costs, and the neighbours' and the one-day-late rule's alphas
  and appraisal ratios: gate 6 compares their Sharpe ratios, which for a tilt this close to the
  benchmark are the benchmark's.

**Risks named before the run.**

- **Gates 3 and 4**: the probabilistic Sharpe ratio is the market's; the deflated Sharpe ratio needs
  an appraisal ratio near 0.95 against about 0.64 expected by luck, above the size predicted. The
  logic audit's simulations, on the earlier design of two fifths moved (the appraisal ratio does not
  depend on the tilt's size), passed gate 4 in none of 24 runs at an effect of 1 to 1.5% a window:
  the verdict's content will rest on the clause.
- **Few years**: eighteen windows of eight sessions; a single year's crash or rally inside a window
  weighs much, and IWM's beta of about 1.13 on SPY lets a year-end rally of the whole market
  (SC-007) raise IWM less SPY with no size effect, which the beta-scaled measure reports.
- **Gate 2**: the rule's Sharpe ratio is about the benchmark's, whose own was about 0.4 over the
  lab's years; whether it clears 0.4 depends on the benchmark as much as on the effect.
- **Gate 6**: the monthly resets keep the equal weights from drifting for a year, as SC-017-01's
  drifted for ten months, when QQQ carried 33% of its profit; SC-001-01's weekly resets kept QQQ at
  23.8%.

## Choices, and the options rejected

- **IWM alone in the window, the rest in cash**: it would time the market's level, which the theory
  does not claim; the move from the S&P 500 to the small caps keeps the exposure.
- **Moving QQQ's fifth too**: it would add the Nasdaq-100's December strength, SC-006's effect of
  the opposite sign, which no source measured against the Russell 2000.
- **The whole portfolio in IWM over the window**: it would add EFA's and EEM's returns against IWM's
  to the alpha, noise to the claim.
- **Grading the classic January effect, or both halves**: the sources' latest years find January
  gone or reversed in the Russell 2000 against the S&P 500, the effect's January strength left in
  microcaps the lab does not hold; it is reported.
- **Clark and Ziemba's rule to 15 January as a variant**: see above.
- **Other small-cap funds, or past losers**: the lab holds one small-cap fund and no single stocks.

## Implementation

Long only, the five equity funds, each with a European (UCITS) fund that tracks it; two orders a
year on sessions known a year ahead, and a monthly reset. A weekly portfolio holds it only if it
places the two orders on those sessions; a monthly one cannot: a calendar effect enters a portfolio
only if it passes the battery. The targets are filled at the close of the session on which they are
set; gate 6 adds a day's delay.
