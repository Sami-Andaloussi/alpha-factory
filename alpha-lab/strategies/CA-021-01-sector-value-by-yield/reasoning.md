# CA-021-01 — Value by yield within the sector funds: reasoning

## Why this theory now

CA-021 holds that an asset can stay under- or overvalued against its fundamentals for a long time,
because investors extrapolate recent trends, overpay for growth stories and neglect the distant cash
flows of unloved assets, and because a professional who looks contrarian too early pays for it; so
that assets, sectors, countries and asset classes that are cheap on price against fundamentals
outperform those that are dear, over weeks to years. It refutes itself if cheap groups do not
outperform dear ones, whether among stocks, across countries or across asset classes; if low prices
against fundamentals are value traps or structural changes, so that cheapness predicts nothing; or
if dear assets outperform cheap ones over full samples, and not only in the long phases dominated by
momentum that are the effect's known limit.

Its measure is price against a fundamental. The lab held prices only until now, and the judgements
before this one placed CA-021's forms here on that ground: CA-024-01 tested value by price alone,
"this card uses no fundamental", and CA-016-01, CA-018-01 and CA-019-01 left CA-021 the valuation
and yield forms across sectors, countries and asset classes. The one fundamental the lab can read is
the cash its funds pay. The frozen bars are adjusted for distributions, and the step by which they
scale the past down on each ex-date is the distribution over the close before it; the lab's decision
of 2026-09-26 required the first theory that reads the funds' distributions to build a point-in-time
reading of them, tested, before any strategy reads them. CA-021 built it (the lab's decision of
2026-09-27): `market.signal_distributions` holds, on the session the bars as they stood confirm a
distribution — the fourth bar read from its ex-date, three sessions after it as a rule, as the paper
job drawing the bars each day could read it — its cash as a fraction of the close before its
ex-date; gate 1 checks a rule that reads it as one that reads prices. Two audits of the reading, on
the most capable model, found faults that were fixed before this card was locked.

**What this card tests, and what it sets aside.** The card ranks the eleven sector funds by their
yield. The three regions, SPY, EFA and EEM, which the lab's decision of 2026-09-27 names as a group
of CA-021's, are judged here and not graded (below): their yield ranking holds EFA in 189 of 203
months, and EFA's and EEM's standing against the United States from 2010 to 2022 is published.
Across asset classes, a stock fund's dividend yield, a bond fund's coupon and a commodity fund's
nothing are not one fundamental. The card is therefore CA-021's sector form alone, a test of the
claim's reach, since none of the sources ranks sector funds by their yield.

**The bank's other theories this card touches**, and how it differs from each:

- **CA-024**, value and momentum everywhere, tested inconclusive: CA-024-01 held the cheapest third
  of each of three groups by its past five years' return — the eleven sector funds, the five equity
  markets, the three commodity funds — and stopped at gate 2, an alpha of −0.63% a year over the
  groups held in equal parts from 2010 to 2022; by group, the sector funds' value tilt earned +0.98%
  a year (a standard error of 1.88%) and the equity markets' −3.24% (1.67%), its cheapest equity
  markets the foreign funds, EFA held in 97% of the months and EEM in 79%. This card measures value
  by a fundamental, the yield, not by price, on CA-024-01's sector group with its construction, so
  that the two measures can be read side by side.
- **CA-025**, carry, untouched. Pedersen (*Efficiently Inefficient*, 2015, §11.1): "The carry of an
  equity is its dividend yield", adding that "for equities, carry is closely related to value";
  Ilmanen (*Expected Returns*, 2011, §13.5) counts "stock or country selection based on dividend
  yields or other valuation ratios" among carry's cousins, and his later book (*Investing Amid Low
  Expected Returns*, 2022, chapter 6) reads "equity country allocation (based on the spread between
  dividend yield and cash rate)" as carry. Within a group of dollar funds, a yield less a common
  financing rate ranks the funds as the yield does: CA-025's within-group equity carry is this
  card's rule, and when CA-025 is picked its reasoning reads this card's result as published, on
  the sector funds, and the regions' as judged here.
- **MR-044**, countercyclical expected returns, and **EF-008**, the value premium, untouched: an
  index's own yield timing that index's exposure. The base ranks funds against each other; the
  variant ranks each fund's yield against its own past, but still across the group, holding the
  cheapest against their own history rather than timing any one fund.
- **MR-021**, long-term overreaction and reversal, untouched: the regions ranked by their past three
  to five years, its card's by the lab's decision of 2026-09-27.
- **CA-016**, **CA-017**, **CA-018** and **CA-019**, recorded not testable on the three regions.
- **CA-022**, value spreads, untouched: value timed on its own dispersion. With the yields read, a
  spread between the sector funds' highest and lowest yields is a form CA-022 can draw; it would
  time this card's rule, and read this card's result.

## The sources

The library holds Asness, Moskowitz and Pedersen's study through its readers; the books say the
following.

- Ilmanen (*Expected Returns*, 2011, §12.5), asked whether value works "beyond individual stock
  selection or in market or sector selection in other asset classes": "The short answer is 'Yes'".
  The study chose "deliberately naive value indicators to avoid overfitting", price to book for
  stock selection, and found "all strategies have positive Sharpe ratios, ranging between 0.1 and
  0.9"; "Value strategies worked especially well [...] for equity country allocation". The same
  section warns that misvaluations "can keep getting worse", that in crises "cheap assets get
  cheaper", autumn 1998 and 2008 the extremes, and that value strategies are "short a structural
  break".
- Ang (*Asset Management*, 2014, chapter 7, §3.6): "Value in essence buys assets with high yields
  (or low prices) and sells assets with low yields (or high prices)", a strategy that "works in all
  asset classes but goes by different names".
- Pedersen (§11.1) and Ilmanen (§13.5; 2022, chapter 6) on the dividend yield as equity carry,
  above.
- Faber (*Global Asset Allocation*, 2015, Figure 46): "You want the countries with the highest
  yield". The figure's title names developed markets and its caption, as the library holds it,
  "developing markets, 1976-2013"; either way, countries, not sectors.
- The Zacks *Handbook of Equity Market Anomalies* (2011, chapter 10, "Value Premium: Evidence from
  Alternative Asset Classes") reports the study's construction — country indices valued by the
  book-to-market ratio of their constituents, each asset class sorted into thirds, equally weighted
  outside stocks, a value premium of about 3.5% a year in stock selection in the US, the UK and
  Europe — and reports that Blitz and van Vliet (2008), ranking twelve asset classes on value, made
  "several asset-specific adjustments to correct for the slope of the yield curve, default risk, and
  structural difference between equity markets".
- Ilmanen (*Investing Amid Low Expected Returns*, 2022), as CA-024-01 read it: value premia negative
  in the 2010s in several asset classes, US value by book to price down 63% from its 2007 peak to
  its 2020 trough.

## From the claim to a signal

- **The measure**: each fund's trailing yield, the cash it paid over the year before the session
  before the target, over its price on that session. On the first session of each month t, for each
  distribution the reading gives on a session in the year to t−1 (after the same calendar date a
  year earlier, up to t−1), its cash over the close of t−1 is taken, on the adjusted closes, as its
  fraction f_j times the ratio of the close of the session before the one it is given on, c_j − 1,
  to the close of t−1, divided by the product, over that distribution and every later one given up
  to t−1, of one minus its fraction, the factors by which they scaled the past down: `f_j × A(c_j −
  1) / A(t−1) / Π_{k: c_j ≤ c_k ≤ t−1} (1 − f_k)`, each session the reading's own, before
  `.shift(1)`. The fraction is of the close before the ex-date, the ex-date three sessions before
  c_j as a rule, so that the price's change from that close to c_j − 1 is left in the cash, about a
  percent of it, the same in the backtest and in paper trading, which read the same sessions; and a
  distribution whose ex-date is on or before t−1 but which is given after it scales the others' cash
  by one minus its fraction, as the bars as they stood do (XLRE in January 2019, XLE and XLV in
  January 2020). The yield is the cash of a year over today's price, as the sources' dividend yield
  is; nothing after t−1 enters. The funds trading whose reading starts on or before the same
  calendar date `months` months before t−1 (and, for "own", with sixty readings) are ranked; a run
  of NaN that ends on t−1, a distribution not yet confirmed as the bars stood, counts as no
  distribution, as paper trading reads it, and any other NaN in the window leaves the fund unranked.
- **Why a calendar year**: the sector funds pay once a quarter, near the third Friday of March,
  June, September and December until 2019 and on the Monday after since March 2020; the targets are
  set on the first session of a month, so that a year counted from it holds each payment once. A
  window of 252 sessions could hold one payment twice or miss one as the calendar shifts.
- **The group and the rule**: the eleven sector funds, XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU,
  XLV and XLY, the lab's sector universe, which six cards have held (CA-006-01, CA-015-01,
  SC-006-01, SC-026-01, TM-002-01, TM-003-01). CA-024-01's construction, the ranking on the yield:
  on the first session of each month, the funds trading whose reading starts on or before the
  window's first day, as the measure says, are ranked by their yield, and the top third of the
  ranked funds, rounded, one at least, is held: three of nine until XLRE is ranked in October 2017,
  three of ten until XLC is ranked in July 2019, four of eleven after. Of the N funds trading, the n
  ranked hold n/N of the portfolio, split equally among the highest yields; a fund trading but not
  yet ranked is held at 1/N, its benchmark weight. The targets start on the first month in which a
  fund is ranked; from then the portfolio is always fully invested.
- **The variant**: the yield over its own mean, the fund's trailing yields on the first sessions of
  the sixty months up to this one — the fund cheap against its own history rather than against the
  group. Blitz and van Vliet adjusted for "structural difference between equity markets", and the
  sector funds' yields differ by construction: utilities and real estate pay out much of their
  earnings, technology little. The base ranks the level, which the sources use; the variant takes
  the structure out. It is reported, not graded.
- **The neighbours**: gate 6 moves the yield's window by a quarter and by a half — nine and fifteen
  months, six and eighteen — the cash annualised by twelve over the months. The sector funds pay
  quarterly, so that each window holds whole quarters. The eighteen-month neighbour starts on
  2006-08-01 and sits in cash before it.
- **The memory**: the base reads a year and a day back from the session before a target, eighteen
  months at its widest neighbour, 382 sessions; the variant reads six years, sixty monthly yields
  each over a year, 1,493 sessions at most. The card declares 1,530 sessions, and gate 1 checks it
  on both; the battery's placebos keep that distance past their circular wrap (the rule of version
  3, the battery now at version 4).

**The pace, counted before the card** on the signal alone, no return read, as the lab's decision of
2026-09-25 allows. The base's first targets are on 2006-02-01, a year after the lab's first session,
and 203 monthly targets follow to December 2022; gate 1 would count 33 clustered decisions, three
above its floor of thirty, four of them the entries of XLRE and XLC (trading in October 2016 and
July 2018, ranked in October 2017 and July 2019): the rule must follow the card's window and its NaN
exactly, since a lost change or two fails gate 1. The funds held are mostly the same: XLU in all 203
months, XLP in 145, XLE in 91, XLB in 70, XLRE in 62 of its 63 ranked months, XLF in 58, XLI in 21,
XLV in one; XLK, XLY and XLC never. XLU's weight averages 31% of the portfolio, never under a
quarter, a third of it in 137 months; XLP's 22%. The variant's first targets are on 2011-01-03, 144
months, 47 clustered decisions; XLE held in 110, XLK in 67, XLP in 62. The neighbours: nine months,
35 clustered decisions; fifteen, 37; six, 40; eighteen, 24.

**The overlap with CA-024-01**, counted on the signals alone: over the 155 months of CA-024-01's
base, from 2010-02-01, the two rules share the funds and the monthly pace, but their holdings are
never the same set in any month, and 43% of this card's picks are also CA-024-01's. The variant's
picks are CA-024-01's in 49% of them, the same set in 15 of 144 months: a fund cheap against its own
past yield is often one whose price fell, CA-024-01's measure. The published sector result, +0.98%
a year, is therefore not this card's outcome, and the lab's decision on cards that share a published
rule's funds, sides and pace, which grades where their signals disagree, does not bind it: here
they disagree in every month.

**What the lab has published on these funds and years.** TM-002-01's verdict published the sector
funds' own alphas over their equal weight from 2006 to 2022: staples +3.7% a year at a beta of 0.61,
health care +3.7% at 0.74, utilities +2.2% at 0.73; financials −5.7% at 1.40, energy −2.3% at 1.29,
materials −1.2% at 1.14; technology and communication made most of the rest of its alpha, their own
figures not given. A fixed mix at this card's average weights, against their equal share month by
month, would earn on those six figures about +0.9% a year from the utilities and staples held over
their share and about −0.4% from health care held under it, energy, materials and financials adding
about nothing together: some +0.5% in all. It leaves out the five funds not published, which the
base holds far from their share: technology and consumer discretionary 10.5 points under it each,
industrials 7.0 and communication 1.9 under, real estate 5.6 over. Technology and consumer
discretionary led the decade, and SC-006-01's and CA-015-01's verdicts, both rules near the equal
weight, published technology's share of their profit at 14.7% and 15.1% against a weight of about a
tenth: the part left out most likely lowers the estimate, perhaps below zero, so that +0.5% leans
high. The estimate is built from published figures, not the sample's; an alpha is linear in the
series it regresses, so that the gaps are the months' drift, the funds that trade only part of the
years, and the five funds left out. CA-011-01's reasoning estimated its variant's fixed mix, from
the same alphas, at −0.2 to −0.4% a year, and its verdict measured +0.16%: a miss of about half a
point, the size of this estimate. It excludes neither sign before the run, and does not settle the
claim: it says that much of the base's outcome is its fixed preference for utilities and staples,
whose years are published. TM-002-01's verdict also found that the placebos keep a rule's average
mix, and that its own mix, held fixed, earned 1.34% a year where its timing cost about 0.4 points.
Following the lab's decision of 2026-09-25 on published results that bear on a test, the verdict
reads the base's alpha with this known part, and reports the mix held fixed apart from the timing.

**The regions, judged.** Ranked by their yield as one group, SPY, EFA and EEM hold EFA in 189 of 203
months, SPY in 9 and EEM in 5: EFA's yield is above SPY's in 194 of them. That tilt is, month after
month, EFA against the other two, and CA-024-01's verdict published it for 2010 to 2022: EFA held as
the cheapest equity market in 97% of the months, the group's tilt −3.24% a year, EFA's own −4.2%
against its group. Graded again, the regions would grade a published outcome, which the lab's
decision of 2026-09-26 leaves out of any clause; reported beside the sector funds, they would add a
known loss to the portfolio the gates judge. The card does not hold them. Their yield form stays
CA-025's to read as judged here, and MR-021's reversal form its own.

## What the battery judges, and what to expect

**The size predicted.** The sources give no premium for a yield ranking of sector funds, and none
long only. The study's long-short value premium in stock selection was about 3.5% a year; a
long-only tilt keeps 40 to 50% of a long-short premium (Israel and Moskowitz, as CA-024-01 read
Ang). On the sector funds, about 3.5% × 0.45, about 1.6% a year over the eleven held in equal parts
if the lab's years kept the long record, about 0.8% if they kept half. The tracking error is
CA-024-01's sector tilt's, whose alpha's standard error of 1.88% over 12.9 years puts it near 6.8% a
year: an appraisal ratio of about 0.12 to 0.24. This card's concentration, a third of it in XLU for
most of its months, may raise it. Costs are small, a few changes a year: about 0.1% a year.

**The decade.** From 2010 to 2022 value lost in several asset classes; the highest-yield sectors
are the utilities, staples, energy and real estate, the lowest technology and consumer
discretionary, which led. The card predicts the long record's premium, and names the decade as the
likely reason for a shortfall.

**The clause, and which condition carries the claim.** Judged on the base by its alpha over the
eleven funds held in equal parts, as gate 2 measures it: the theory is refuted in this form if the
alpha is zero or less, the highest yields among the sector funds having earned no more than the
sector funds from 2006 to 2022, as the bank's first refutation reads for sectors. Any other result
short of passing gates 1 to 7 is not proven, not refuted. The alpha carries the claim alone. The
lab's rule (RUNBOOK step 4, after CA-024-01) asks a slow rule whose holdings persist to say so: this
one holds XLU in every month and XLP in most, and its placebos, its own weights moved in time, keep
that composition, so that their rank judges only the timing of some thirty changes, not whether the
high yields beat the group. The placebos' rank is reported, not graded.

**The test's power.** Over about seventeen years an appraisal ratio is measured to about ±0.24. With
no edge the alpha is zero or less about half the time; at 0.12, the low end, about 31%; at 0.24, the
top, about 16%. The clause refutes a vanished premium about one time in two, and a real one at the
low end about one time in three. Gate 4, over the registry's 80 trials, 73 of them effective, needs
an appraisal ratio of about 0.9 to 0.95, far beyond the prediction.

**Measures stated before the run**, reported, not graded:

- the variant, the yield against its own five-year mean;
- the base's average weights held fixed and reset on the same months, over the funds that trade
  (XLRE's and XLC's weights shared among the others before they trade, as CA-011-01 did), against
  the same funds held in equal parts: the mix's alpha, and the timing, the rest of the base's; with
  the estimate above;
- the placebos' rank, and the base against CA-024-01's sector tilt rebuilt from its card on the
  same funds and months: the correlation of the two tilts' monthly returns, each hedged of the
  sector funds held in equal parts;
- the alpha by year, and in 2008 and 2020;
- the share of the months each fund is held, and its share of the profit.

**Risks named before the run.**

- **The decade**, above.
- **A static tilt.** The base holds XLU in every month and XLP in most: much of it is a fixed
  preference for the funds that pay most, the structural difference the variant takes out. A result
  of the base is as much the high-yield sectors' as value's.
- **One fund's share.** XLU weighs 31% of the portfolio on average and never less than a quarter;
  gate 6 refuses more than 30% of the profit in one fund, and XLU's share will likely pass it. As a
  card only likely to fail gate 1 is still drawn (the lab's decision of 2026-09-25), so is this one,
  the likely failure written here before the run.
- **Gate 1's floor.** 33 clustered decisions, three above thirty, four of them funds' entries.
- **The blend.** Gate 5's blend holds the variant, which holds nothing before 2011-01-03: half the
  blend sits in cash from 2006 to 2010.
- **When the reading gives a distribution.** Three sessions after its ex-date as a rule, four to six
  for XLC and XLRE in a few; SPY's of 2025-06-20 is given on 07-09. A yield read on a month's first
  session holds each quarterly payment once while the payments are given in the same month each
  year; one given across a month's turn moves to the next month's yield: XLRE's of December 2018,
  given on 2019-01-02, leaves its January 2019 yield three payments, the one ranked month in which
  the base does not hold XLRE, and its January 2020 yield five; XLE's and XLV's steps of 2019-12-30,
  given in January 2020. Read on the bars as they stood each session, the paper job gives the sector
  funds' distributions from 2006 on the backtest's session in 850 of 859 and a session later in 9,
  none across a month's turn, so that every target of this card reads the same distributions, their
  cash moved by a session's price change at most; it once read XLRE's of 2016-12-21 as 26% for a
  session where the full bars read 1.8%: in paper trading, which reads the bars afresh each day, such
  a misreading on the session before a target would raise that month's yield.
- **What the reading does not see.** A distribution under three half-cent steps of the price as read
  (1.5 cents, or 3 cents for XLB, XLE, XLK, XLU and XLY, read at half their traded price) is not
  read. XLK reads one, two, two and three distributions in 2005 to 2008 where the others read four
  (XLY three in 2006, below); whether these are missed readings or XLK's payments is not settled,
  and its yield in those years may be understated: the variant holds XLK in its 67 months of 2011 to
  2016, when its sixty-month mean holds those years. XLY's distribution of March 2006 is not read,
  so that its yield holds three payments from April 2006 to March 2007, and the variant's
  sixty-month mean for XLY holds that year. XLF's 2016 spin-off of XLRE's shares reads as a
  distribution of 19%, merged with its regular one of 2016-09-16, and raises XLF's yield to about a
  quarter for a year, from October 2016 to September 2017, in which the base holds XLF; XLE's second
  step of 2019-12-30 reads as 2.9% and XLV's as 0.65%, both in the bars, given in January 2020 and
  raising their yields through January 2021. The card keeps what the bars encode, and says so.
- **Few ranked funds.** Nine until October 2017, ten until July 2019.

## Choices, and the options rejected

- **The regions**: judged above, not held.
- **Price to book or earnings**: the study's measures; the lab holds no balance sheet or earnings.
- **Across asset classes**: a stock fund's dividend yield, a bond fund's coupon and a commodity
  fund's nothing are not one fundamental; Blitz and van Vliet adjusted them, the library does not
  say how.
- **A short leg**: the lab is long only.
- **The highest yields held at their own weight, or a yield against a financing rate**: carry's
  forms, CA-025's, which rank the funds as this card does.
- **A window of 252 sessions**: above.
- **Leaving out XLF's spin-off**: a rule that drops distributions it judges special reads the bars
  selectively; the card keeps them, disclosed.

## Implementation

Long only, eleven sector funds, each with a European (UCITS) fund that tracks it, monthly targets
filled at the close of the session on which they are set; gate 6 adds a day's delay.
