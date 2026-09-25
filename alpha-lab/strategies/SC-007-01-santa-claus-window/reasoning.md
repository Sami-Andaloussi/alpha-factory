# SC-007-01 — The equity funds over the Santa Claus window, cash otherwise: reasoning

## Why this theory now

SC-007, the Santa Claus rally, holds that stocks rise over a short window: the last five trading
days of December and the first two of January. The mechanisms proposed overlap: holiday optimism and
a lower aversion to risk, the retreat of institutions, which leaves the field to individuals,
year-end flows and bonuses, the anticipation of the January effect, and cosmetic adjustments of
portfolios. The bank records an average gain of about 1.3% for the S&P 500 over the window since
1950, with a rise in about 80% of years, and a larger effect in small caps in some studies, and
holds the rally distinct from the whole January effect and from the pre-holiday effect.

**The sources.** The bank names Hirsch's *Stock Trader's Almanac* (1972), Nippani, Washer and
Johnson (2015, 2016), Nippani and Shetty (2021) and an Investopedia note (2024); none is in the
library, which cites Hirsch without a figure for the window. The library measures the window in
pieces:

- Lakonishok and Smidt (1988), on the Dow Jones Industrials from 1897 to 1986: the rise of the last
  half of December is concentrated from the last session before Christmas, 0.386% a day on the two
  sessions before Christmas and New Year's Day and 0.248% a day between them, about 1.6% over the
  week, 1.2% after 1952.
- McConnell and Xu (2008), on value-weighted US stocks from 1926 to 2005, at the December-to-January
  turn of the month: 0.34% on the last session of December, 0.03% on the first of January and 0.51%
  on the second, 0.23% a day over −1 to +3 against 0.15% at the other turns of the month and 0.10%
  on the other days of December and January (t 1.87 against those other days of December and
  January).
- Singal (*Beyond the Random Walk*, 2003, chapter 2): over the last five sessions of December before
  its last, from 1988 to 2001, the S&P 500's total return was 1.88% and its futures' 1.56% on
  average; he holds it a December effect of the year's winners and proposes holding the S&P 500 for
  about a week at the year's end.
- Ziemba (*Calendar Anomalies and Arbitrage*, 2012): the pre-holiday effect, strong over the
  twentieth century, has diminished greatly in S&P 500 and Russell 2000 futures from 1993, moving to
  the third session before a holiday (§1.5, Table 1.6); his update of the turn of the month on the
  same futures from 1993 to 2010 finds the positive span at −5 to +2, this window's shape, pooled
  over all months, but for small losses on −2 and −1 in the S&P 500 (§1.10).

**What the lab already knows, and is not blind to.** SC-008-01, the turn of each month on the same
five funds: its base, −1 to +3, holds three of this window's sessions (+0.034% a day over the other
sessions, a standard error of 0.050%); its variant, −5 to +2 of every month, is this window's shape
in all twelve months: +0.0970% a day over 1,508 sessions against +0.0035% over 3,022 (a difference
of +0.0935%, a standard error of 0.0429%, t 2.18), about half its edge from October and November
2008; by session, all months together, −4 +0.229%, −3 +0.118%, −2 +0.123%, −1 −0.059%, +1 +0.215%,
+2 +0.102% (each to about ±0.08 to ±0.10%). This card's 124 sessions are among the variant's; the
other months' same sessions, about 1,380, are about a third of this clause's other sessions.
SC-006-01 published the sector funds ranked each year (nine to eleven) over December's sessions −6
to −2: +0.49% a year over the bill (a standard error of 0.27%, t +1.78, twelve years of eighteen
positive), four of this window's seven sessions. SC-002-01 published, from 15 December to December's
third-to-last session, which overlaps this window's sessions −5 to −3, SPY +0.86% over the bill and
IWM +1.69% (0.64%, t +2.66), and IWM less SPY over December's last two sessions +0.02% (0.14%).
SC-017-01 published the five funds' average daily excess return in December (+0.054%, a standard
error of 0.062%) and January (−0.016%, 0.064%). With sessions −5 to −2 near SC-006-01's +0.1% a day
and the other three at the other sessions' mean, the expected difference is about +0.04% a day, or
+0.06% at SC-008-01's means by session; a refutation then has about a 12 to 22% chance, not 36%. The
clause is not decided, but it rests mostly on sessions −1, +1 and +2 and on EFA and EEM, and a
refutation would be weaker evidence than the rate alone suggests. What no published figure gives is
December and January against the other months' same sessions, reported below. The card's prediction
is taken from the sources, not from these figures.

**The holdout is new only for this rule.** Every earlier card on the five funds opened 2023 to 2025,
and SC-002-01's and SC-006-01's verdicts report the 2022–23 turn of the year (IWM less SPY +3.13% to
January's tenth session; the sector winners less the others −2.16% over January's first five). The
market's path over those years is public.

**The bank's neighbours.** **SC-002**, the January effect, whose anticipation the window may hold;
**SC-006**, the December effect of the year's winners; **SC-008**, the turn of the month;
**SC-014**, the pre-holiday effect, of which Christmas Eve and New Year's Eve are cases. This card
reads the whole market's level over the seven sessions, not a cross-section.

## From the claim to a signal

- **The market**: the lab's five equity funds, SPY, QQQ, IWM, EFA and EEM, in equal parts, as
  SC-008-01 took them: the bank's claim is the US market's, and the studies it cites extend it to
  other markets and to small caps. The three US funds' average is reported apart.
- **The window**: the last five scheduled sessions of December and the first two of January, on the
  New York Stock Exchange's calendar of scheduled sessions derived from its holiday rules alone, as
  SC-008-01 built it. A session's return is taken from the previous session's close, so that the
  window's returns run from the close of December's sixth-last session to the close of January's
  second.
- **The rule**: the five funds in equal parts over the window's sessions, and the bill otherwise:
  SC-008-01's rule with a yearly window. Its alpha over the five held always is the window's excess
  return less about 7/252 of the benchmark's — about, since the regression's beta is the window's
  share of the benchmark's variance, not of its sessions.
- **The parameters for gate 6**: the December sessions in the window, 5, with its neighbours 4 and
  6, 2 and 8; the January sessions, 2, with its neighbours 1 and 3 at both steps. All change the
  targets and pass the card's checks.

The windows were counted before the card by a scratch script outside the repository (`pace.py`, in
the session's scratch folder) that reads the calendar and the market's dates alone, and the logic
audit corrected its count: 124 returns in-sample in eighteen windows, the first one partial (the
window of 2004–05, whose last session, 2005-01-04, is the first in-sample return held), the last one
partial too (2022–23, whose January sessions are in the holdout), and 2006–07 of six returns, the
exchange having closed on 2 January 2007; 36 switches. The neighbours hold 106, 142, 70 and 178
returns (December 4, 6, 2, 8) and 107 and 142 (January 1, 3). Gate 1 finds about 36 decisions once
clustered, against 30 needed.

## What the battery judges, and what to expect

**The size predicted — a judgment, from the sources.** About 1.3% for the S&P 500 over the seven
sessions since 1950, per the bank, 1.2% for the Dow's last week of December after 1952, and 1.9% for
the S&P 500's last five December sessions but one from 1988 to 2001: a window's excess return of
about 0.5 to 1.3% a year for the five funds from 2005 to 2022, less than in the sources' years since
the effect is known and the pre-holiday effect has faded, positive in about 55 to 70% of the years.
At about 0.03% a day for an ordinary session, the window's mean daily excess return exceeds the
other sessions' by about 0.04 to 0.16% a day. The rule's alpha is about the window's return less
about 0.24% (7/252 of the benchmark's excess return), about 0.3 to 1.1% a year, before costs of
about 0.1% a year (two switches of the whole portfolio at 5 basis points a side); its volatility,
seven sessions a year at about 1.4% a day, is about 3.7% a year, for a Sharpe ratio of about 0.1 to
0.3 and an appraisal ratio of about 0.05 to 0.25: the card expects the rule to fail gate 2, a Sharpe
ratio of 0.4 needing a window's return of about 1.6% before costs.

**The clause.** Judged before costs, in SC-008-01's form: over the in-sample sessions from the
base's first held, the five funds' average daily return less the bill's rate, each from the market's
previous close; the mean over the sessions whose return spans a scheduled session of the window,
less the mean over the other sessions, with the standard error of that difference, the square root
of the sum of each group's variance over its count, and its t statistic. The theory is refuted in
this form if that t statistic is −0.35 or below. Above it, short of passing gates 1 to 7, it is not
proven, not refuted; a base that passes gates 1 to 7 while the clause refutes leaves the theory
refuted in this form.

Of SC-007's refutation criteria, the first, no excess return over the window against other
seven-session windows, is graded; the second, a frequency of rises no higher than any seven-session
window's, is reported; the third, an outperformance spread over the whole of December or January, is
reported through the window against the rest of December and of January; the fourth, the rally's
link to institutional activity, announcements and sentiment, is beyond the lab's data. The bank's
claim that the rally is distinct from the turn of the month is reported through the window against
the other months' same sessions.

**The test's power.** At a daily standard deviation of about 1.38% for the five funds' average (its
figure over all in-sample sessions, with fat tails), and 124 window sessions against 4,406 others,
the standard error of the difference is about 0.13% a day. The clause then refutes about 36% of the
time with no effect, about 12% at a difference of +0.10% a day, and about 5% at +0.16%; the logic
audit's simulations with fat tails, clustered volatility and serial correlation within a window kept
these rates. It cannot tell an effect at the low end of the prediction from none.

**Measures stated before the run**, reported, not graded:

- the window's excess return year by year, compounded, over the seventeen full windows, 2005–06 to
  2021–22, with the years positive, against the share positive of all spans of seven consecutive
  in-sample market returns, overlapping, one starting at each session, the window's own included,
  excess compounded (a share from seventeen years has about ±12 points of noise); the partial
  windows apart;
- the same difference, and year by year, for each of the five funds, for the three US funds'
  average, and for IWM less SPY;
- the window's daily mean less the rest of December's (its sessions up to the sixth-last), and less
  the rest of January's (the sessions after its second), with their standard errors; and each part
  of December and January against the sessions outside those two months;
- the December part (the returns from the close of −6 to the close of −1) and the January part (from
  the close of −1 to the close of +2), each as a daily mean less the other sessions', with its
  standard error, and compounded year by year;
- the window's daily mean less the other months' sessions −5 to +2, with its standard error, the
  bank's claim that the rally is distinct from the turn of the month; and each of the seven
  sessions' mean, beside SC-008-01's, McConnell and Xu's and Lakonishok and Smidt's;
- the rule's alpha before and after costs, and the neighbours' and the one-day-late rule's alphas
  and appraisal ratios.

**Risks named before the run.**

- **Few windows**: eighteen windows of seven sessions; one crash inside a window, as in December
  2018, weighs much.
- **Gate 2**: a rule in the market seven sessions a year earns a small return with a small
  volatility; in the logic audit's simulations, noise alone reached a Sharpe ratio of 0.4 in 11 to
  41% of runs across the predicted sizes.
- **Gate 3**: its placebos shift the weights by a year or more; for a yearly rule about 5% of the
  shifts land partly on other years' windows, which makes the gate slightly harder.
- **Gate 6**: the five funds are held together, so each fund's share is its own gain over the
  windows; in the audit's simulations no fund exceeded 30% of the profit in only 27 to 70% of runs.

## Choices, and the options rejected

- **A tilt of the equity funds rather than in or out**: the claim is about the market's level, not a
  cross-section; the rule must time the market to hold it.
- **SPY alone**: a universe of one asset cannot pass gate 6; the five funds hold the US market and
  the others the bank's studies extend it to.
- **The eleven sector funds**: closer to the S&P 500's claim, but SC-006-01 has published their
  sessions −6 to −2, and they leave out the small caps the bank names.
- **Windows of the sources' other definitions** (Singal's five sessions before the last): they are
  SC-006's; the window here is the bank's, and its December and January parts are reported apart.

## Implementation

Long only, the five equity funds, each with a European (UCITS) fund that tracks it, or cash; two
orders a year on sessions known ahead. A weekly portfolio holds it only if it places the two orders
on those sessions; a monthly one cannot: a calendar effect enters a portfolio only if it passes the
battery. The targets are filled at the close of the session on which they are set; gate 6 adds a
day's delay.
