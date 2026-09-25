# SC-027-01 — The equity funds held in the fortnight around the new moon: reasoning

## Why this theory now

SC-027, the lunar cycle effect, associates stock returns with the phases of the moon, lower around
the full moon than around the new moon, through mood, sleep or agitation that change risk-taking;
the effect is said to be moderate, independent of the classic calendar anomalies, found in many
countries and long periods, with no parallel change in volatility or volume. Its refutations:
returns around the full moon no lower than around the new moon; a pattern that comes with changes in
volatility or volume, pointing to information rather than mood; a pattern that disappears once the
turn of the month and other monthly effects are controlled for; an effect that does not replicate in
new samples, markets and periods.

**Its sources, as the lab read them in the library's books.**

- **Yuan, Zheng and Zhu (2006)**, as Dzhabarov and Ziemba report them in the Zacks *Handbook of
  Equity Market Anomalies* (2011, chapter 9) and in Ziemba's *Calendar Anomalies and Arbitrage*
  (2012, chapter 1): in 48 countries, stock returns lower on the days around a full moon than on the
  days around a new moon, a difference of 3 to 5% a year in equal- and value-weighted global
  portfolios; not due to changes in volatility or volume, not explained by macroeconomic
  announcements or major global shocks, and independent of the January, day-of-the-week,
  calendar-month and holiday effects. The library gives no width for their "days around".
- **Ilmanen** (*Expected Returns*, 2011, §25.3), citing Dichev and Janes (2003): average equity
  market returns higher in the fortnight around the new moon than in the fortnight around the full
  moon; in his section on moods, lunar cycles among the patterns with "some predictive ability",
  most of them weak, likely partly data-mined, and too small to exploit after costs.
- **Singal** (*Beyond the Random Walk*, 2003) reports returns around new moons much higher than
  around full moons, with differences too small for a trading strategy to profit.
- **Bandy** (*Quantitative Trading Systems*, chapter 11), on 513 US stocks: a lunar rule fitted from
  1995 to 2005, long over about four fifths of the cycle, the full moon included, and short from
  about three days after the full moon to just past the third quarter, was profitable in 96% of them
  in-sample on its long side; from 2005 to 2007, out of sample, the long side was profitable in 55%
  with a median gain of 2% a year, and about four fifths of the phase's slots had inverted: "there
  once was a pattern, but it has not been profitable lately". His rule does not measure the
  fortnights' gap, and his out-of-sample years, 2005 and 2006, lie inside the lab's in-sample.
- **Kaufman** (*Trading Systems and Methods*, chapter 14, "The Moon: Buy Full, Sell New") reports an
  experiment on five futures markets in 1972 — silver, wheat, cattle, cocoa, sugar — in which prices
  rose after a full moon and fell after a new moon: a claim about the waning half, from the full
  moon to the new, against the waxing half, a quarter of the cycle off the fortnights, which splits
  both of his halves evenly across them and predicts no fortnight gap. He gives the formula of the
  moon's mean phases (Meeus's) that this card uses. Narang and Kestner name the moon's phases as
  their example of spurious or irrelevant data.

**What the lab already knows, and is not blind to** — estimates, not the sample's figures (the
runbook's step 3):

- **SC-016-01**: Rosh Hashanah falls 0 to 2 days after a mean new moon every year, and 90 of its
  window's 105 sessions lie in this card's new-moon fortnight. Its published gap, the five funds
  −0.194% a day over the window, most of it 2008's, pulls this clause's gap by about −0.006% a day,
  about −0.16 of a standard error, against the claim.
- **SC-008-01**'s published rebounds of 28 October and 21 to 26 November 2008 fall in the new-moon
  fortnight, 20 November on its boundary at −7 days.
- **SC-026-01**: 2020-03-09, a fall of about 8% in US equities, and the next day's rebound fall in
  the full-moon fortnight.

**The bank's neighbours.** **SC-008**, the turn of the month, which the third refutation names;
**SC-025**, **SC-026** and **SC-028**, the other moods of nature.

## From the claim to a signal

- **The markets**: the five equity funds, SPY, QQQ, IWM, EFA and EEM, in equal parts among those
  that trade: Yuan, Zheng and Zhu's claim is on stock markets across many countries, which the lab
  holds as the US, developed and emerging funds. The sector funds would test Dichev and Janes's US
  form and spread the profit; the five funds keep the international form at the cost of a likely
  failure of gate 6 on one fund's share (QQQ carried 32 to 33% among them in SC-016-01 and
  SC-017-01), which no universe avoids while keeping the form; with gate 2 expected to fail across
  the predicted range, the five funds are kept. The sector funds' and the commodity funds' gaps are
  reported.
- **The phases**: the moon's mean new moons, by the formula Kaufman gives, JDE = 2451550.09765 +
  29.530588853 k + 0.0001337 T² − 0.000000150 T³ + 0.00000000073 T⁴, T = k / 1236.85; k = 0 gives 6
  January 2000. Each is taken as universal time, ΔT (about 65 to 69 seconds) neglected, on the date
  of floor(JDE + 0.5); a choice of universal time, so that a new moon between midnight and about
  five in the morning falls on the day after New York's date. Derived from the formula alone, read
  from no price. The mean phase differs from the true one by up to about 14 hours in these years,
  six on average; the date differs in about 28% of the lunations, and 92 of the 4,534 in-sample
  sessions, 2%, would change fortnight on the true phases. The library gives the mean formula, and
  the card keeps it.
- **The rule**: the funds in equal parts on the sessions whose date lies within `days` days of the
  nearest new moon's date, cash on the others: the new-moon fortnight held, the full-moon fortnight
  in cash, the long-only trade of a claim that the full moon's days earn less. `days` is 7, fifteen
  dates around each new moon, the fortnight of Ilmanen and Dichev and Janes, taken as Yuan, Zheng
  and Zhu's "days around"; its neighbours 5 and 9, and 4 and 10.
- **The calendar**: the rule leaves the funds at the close of the last scheduled session before the
  full-moon fortnight and returns at the close of its last scheduled session, reading the date of
  the next scheduled session on the New York Stock Exchange's calendar derived from its holiday
  rules alone; no unscheduled closure of these years falls on a fortnight's boundary. In-sample,
  2,311 scheduled sessions in the new-moon fortnight and 2,223 outside; 444 changes and the first
  entry, 445 decisions, the shortest run eight sessions, far above gate 1's 30.

## What the battery judges, and what to expect

**The size predicted — a judgment, from the sources.** Yuan, Zheng and Zhu's 3 to 5% a year is about
0.012 to 0.020% a day, if their window is the fortnight; Ilmanen's and Singal's warnings, and
Bandy's out-of-sample loss, point to less in the lab's years. The card judges the five funds'
average daily excess return over the new-moon fortnight at about 0 to +0.020% a day above the
full-moon fortnight's. Out of the funds about half the time, the rule's alpha over the five held
always is about a quarter of the annual gap, 0 to +1.25% a year before costs of about 1.24% a year —
a round trip of the whole portfolio each lunar month at 5 basis points a side —, −1.24 to 0% after;
on a hedged return that moves by about 10.5% a year, an appraisal ratio of about −0.12 to 0. If the
two fortnights' volatilities differ, the regression beta leaves the 0.51 of sessions held and moves
the alpha by about (β − 0.51) × 8.7% a year, half the predicted range for a shift of 0.07; the alpha
at a beta equal to the share held is reported. The card expects the base to fail gate 2 — a Sharpe
ratio of 0.4 would need a gap of about 0.044% a day, 2.2 times the top of the range —, gates 3 and 4
— gate 3's placebos sit at random phases and can be beaten, so its probabilistic Sharpe ratio binds
—, gate 5 with them, and likely gate 6 on one fund's share of the profit.

**The clause.** Judged before costs, over the in-sample sessions from 4 January 2005, each session's
return taken from the market's previous close: the five funds' average daily return less the bill's
rate over the sessions whose date is within 7 days of the nearest new moon's date, less the same
over the other sessions; the standard error of that difference from the two groups' daily variances,
and its t statistic, computed apart from the battery. The theory is refuted in this form if that t
statistic is −0.35 or below: the full moon's fortnight no weaker than the new moon's, the bank's
first refutation. Above it, short of passing gates 1 to 7, it is not proven, not refuted.

**The test's power.** 2,311 and 2,223 sessions, at a daily volatility of about 1.32 to 1.35%: a
standard error of about 0.040% a day. The clause refutes about 36% of the time with no effect and
about 20% at +0.020% a day, the top of the range. It cannot tell an effect of the predicted size
from none.

**SC-027's refutations, and what the card can grade.**

1. *The full moon no weaker than the new moon*: graded.
2. *A pattern with changes in volatility or volume*: reported, lunar month by lunar month, the
   new-moon fortnight's mean log traded volume of SPY, QQQ and IWM less the adjacent full-moon
   fortnight's, and the same for the log of each fortnight's realised variance of the five funds'
   average, each with its standard error across the lunar months.
3. *A pattern that disappears once the turn of the month is controlled for*: nearly settled by the
   calendar: the sessions −1 to +3 of the month are 20.0% of the new-moon fortnight's and 18.1% of
   the full-moon fortnight's, the sessions −5 to +2 34.4% and 32.3%; with SC-008-01's published gaps
   (+0.034 and +0.094% a day), leaving them out would move the lunar gap by about 0.001 to 0.002% a
   day, 0.05 of a standard error at most over the whole sample, about 0.005% a day in 2014–2022,
   when the −5 to +2 imbalance is 5.3 points. Both exclusions are reported.
4. *No replication in new samples*: the lab's years, 2005 to 2022, lie after Yuan, Zheng and Zhu's
   and Dichev and Janes's samples; the clause reads it.

**Measures stated before the run**, reported, not graded:

- the gap by fund; the eleven sector funds' average; GLD, SLV (from April 2006) and DBC (from
  February 2006);
- Kaufman's halves: the waning half, the dates from a full moon's to the next new moon's, less the
  waxing half, for the five funds and for GLD, SLV and DBC, the full moon's date the mean phase at k
  + 0.5;
- by the moon's quarter, each date placed by its days to the nearest new moon: the new moon's week
  before, days −7 to −1, and after, days 0 to +7; the full moon's side, days −15 to −8 and +8 to
  +15, split at the full moon's date;
- the volatility and volume measures above;
- the gap without the turn of the month's sessions −1 to +3, and without −5 to +2;
- over 2005–2013 and 2014–2022, without 2008, and without 2020;
- the same gap over the holdout, 2023 to 2025;
- the alpha before and after costs, at the regression beta and at a beta equal to the share of
  sessions held; the neighbours' and the one-day-late rule's alphas and appraisal ratios. The
  neighbours hold 30% to 71% of the sessions, so their Sharpe ratios mostly read their exposure;
  their alphas and appraisal ratios are the reading.

## Choices, and the options rejected

- **The true phases, with Meeus's periodic corrections**: 2% of the sessions would change fortnight;
  the library gives the mean formula, which is kept, and the difference is stated above.
- **A shorter window around each phase**, the few days of the full moon: the sources measure
  fortnights, and a few days a month would pay the same costs for less.
- **The sector funds**: they test the US form and spread the profit, but lose the international form
  the largest source reports; they are reported.
- **Kaufman's halves as the rule**: his is a claim about futures in one year, a quarter of the cycle
  off the equity claim; reported.
- **Shorting the full-moon fortnight**: the lab does not short.

## Implementation

Long only, five funds in equal parts or cash, with European (UCITS) funds that track them; about
twelve exits and twelve returns a year, on dates known ahead.
