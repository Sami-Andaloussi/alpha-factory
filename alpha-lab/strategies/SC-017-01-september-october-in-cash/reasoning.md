# SC-017-01 — Out of equities in September and October: reasoning

## Why this theory now

SC-017 holds that average equity returns differ from one calendar month to another, in a pattern
that recurs: historically January very strong, September and October weak, November to February
solid. It is a broad and diffuse family, with several possible causes rather than one — taxes, the
calendar of flows, holidays, year-end balance sheets, seasonal cycles in risk appetite — and the
bank itself warns that these monthly regularities are less clean and less stable than the narrower
calendar effects. The bank's neighbours cut narrower pieces out of the same year: **SC-002**, the
January effect, about small stocks at the turn of the year; **SC-018**, the Halloween effect, the
half-year from November to April against May to October; **SC-019**, the January barometer. This
card tests the piece of SC-017 that none of them tests: the two months the sources name as weak.

**The sources.** The lab read them in the library's books.

- Ilmanen (*Expected Returns*, 2011, §25.1–25.2) writes that average equity market returns have
  historically been high in December and January and negative in September and October, and warns
  that seasonal patterns in average returns are often weak, possibly spurious, and costly to
  exploit. His Figure 25.1 plots the average return of the US equity premium by calendar month from
  1927 to 2009. Read from the chart by eye, to about a tenth of a percent: January 1.3% a month,
  February 0.15, March 0.35, April 1.0, May 0.35, June 0.65, July 1.15, August 1.1, September −1.15,
  October −0.2, November 1.2, December 1.45. September is the one deeply negative month, and October
  the only other month below zero. He adds that January's edge over the other months reversed over
  the last twenty years of his sample: for the equity premium, January returns were below average.
- Ziemba (*Calendar Anomalies and Arbitrage*, 2012, §1.4), citing Gultekin and Gultekin (1983) and
  the Keim and Ziemba volume (2000), writes that September and October have historically had low
  returns, with many crashes in October, and November to February higher than average returns, which
  suggests avoiding the bad months and holding cash in them. The same section, on S&P 500 and
  Russell 2000 futures from 1993 to 2011, finds October positive and September only slightly
  negative over that span and no reliable monthly effect: September and October were like other
  months except for their frequent big declines (September 2001, 2002 and 2008, October 2008), and
  from 1998 to 2010 both were positive on average.
- Dzhabarov and Ziemba's chapter on the same futures from 1993 to 2010 (the Zacks *Handbook of
  Equity Market Anomalies*, 2011, chapter 9) finds a very negative October in the recent S&P 500
  data but November, January and February negative, and concludes that the monthly effect has become
  noise with no predictive value. Their table of September and October returns for the S&P 500
  futures from 1993 to 2010 averages, by the lab's sum of its eighteen years, about +0.2% a month
  for September and +0.8% for October: in those years neither month was weak on average.
- On Japan, Ziemba (2012, chapter 11) finds January with by far the highest returns on the Nikkei
  from 1949 to 1988, every month positive but September, just slightly negative, and, with January
  excluded, no rejection of equal mean returns in all months; the pattern changes from decade to
  decade. Comolli and Ziemba's update (the Keim and Ziemba volume, chapter 20) counts May, July,
  September and October among the months of very low returns to 1988, then finds the ranking
  overturned from 1990 to 1994: January indistinguishable from zero, May, October and December
  highest, November, June and September most negative.

The sources thus give a long history in which September and October were weak, and a recent one in
which the broad monthly pattern looks like noise. The card takes the long history's claim and lets
the lab's years judge it.

## From the claim to a signal

- **The months**: the base holds cash in September and October, the two months the sources name as
  weak and the only two below zero in Ilmanen's long US record. The **variant** holds cash in
  September alone, the month that record shows as the deepest, by about 1.9% a month against the
  other eleven; the Nikkei does not single September out, its average there being about as low as
  May's, July's and October's and indistinguishable from zero. Both are taken from the sources, not
  from the lab's data. The lab's own monthly returns were not computed before the card, but two
  things were known: the sources' futures table gives the S&P 500's September and October for six of
  the in-sample years, 2005 to 2010, with −9.8% and −20.1% in 2008; and SC-008-01's verdict, already
  written, reports the five funds' fall in October and November 2008. September and October 2008
  alone, by public figures, add something like 0.04% a day to the clause's difference, about four
  fifths of its standard error; the difference without 2008 is stated below, before the run, so that
  it is not chosen after it.
- **The other months**: the five equity funds in equal parts. The claim's strong side — January,
  November to February — cannot be bought more of by a long-only rule without leverage, which the
  lab does not use: a rule out of the weak months is the claim's long-only trade.
- **The funds**: the five equity markets the lab holds — US large caps, US growth, US small caps,
  developed markets outside North America and emerging markets. The sources' evidence is on US
  indices and on Japan, and the bank reports the pattern with large differences across countries;
  the foreign funds trade in New York and carry their own markets' months.
- **The calendar**: to earn nothing in September, the portfolio must leave equities at the close of
  August's last session, so the rule must know, on that session, that the next one is in September.
  As SC-008-01 did, it reads this from the New York Stock Exchange's calendar of scheduled sessions,
  weekdays less the exchange's holidays derived from their rules, which any investor knows ahead,
  and reads no date of the market. Its code is SC-008-01's calendar, copied: a strategy imports
  nothing from the lab. Only the month of the next scheduled session matters, so the unscheduled
  closures, none of them on a month's last scheduled session in these years, change nothing.
- **Targets**: set only on the sessions on which the state changes — August's last session to leave,
  October's last to return — so that the portfolio drifts with prices while it holds. The data's
  first session, 3 January 2005, is in a month held, and the rule holds from it.

No count of the market's data was made before the card: the rule is a calendar, one exit and one
entry a year, 37 clustered decisions in-sample (a first entry, 18 exits and 18 returns), above gate
1's 30.

Two variants, not three: the sources name two weak months and single out one of them; a third, from
the months they call strong, would be SC-018's test or a short position.

## What the battery judges, and what to expect

**The size predicted.** The benchmark holds the five funds always. A rule out of equities in two
months of twelve has a beta of about 10/12; its alpha is about (2/12) × (10/12) × twelve times the
gap between the other months' average return and the two months', about 1.67 times the monthly gap.
From Ilmanen's figure the gap is about 0.87% a month for the ten other months against −0.7% for
September and October, 1.54% a month: an alpha of about 2.6% a year before costs if the lab's years
kept the whole of it, about 1.3% if they kept half, about 2.5% and 1.1% after costs. The card takes
that range, from half to all of the long history's gap. The recent futures data Ziemba gives points
below it, to about none. Costs are about 0.1% a year: one round trip of the whole portfolio at 5
basis points a side. The rule's bets, hedged of the benchmark, should move by about the benchmark's
volatility times √(2/12 × 10/12), about 7% a year: an appraisal ratio of about 0.15 to 0.35. For the
variant, out of September alone, the gap is about 1.9% a month and the alpha about 0.9 to 1.8% a
year before costs.

**The clause.** The theory is judged on the base, before costs, which are small, on the mean daily
excess return of the five funds over the sessions of the other ten months less that over the
sessions of September and October. Over about 18 years, some 750 sessions in September and October
and 3,780 others, at a daily volatility of about 1.2%, the difference is measured to about ±0.048% a
day; the whole long-history gap, 1.54% a month over 21 sessions, would make it about 0.073% a day,
about one and a half standard errors. The theory is refuted in this form if that difference is zero
or less — September and October no worse than the other months — and the base beats half of its
placebos or fewer. The placebos shift the rule's own weights in time by a year or more, so that its
two months in cash land mostly on other months, keeping its exposure, its pace and its costs. Any
other result short of passing gates 1 to 7 is not proven, not refuted.

**The test's power.** A synthetic simulation made for the card — daily returns drawn at random, not
the lab's — gives the clause's rates. With no gap left, it refutes about 45% of the time: a vanished
effect is found no more than half the time. At half the long history's gap it refutes about 21% of
the time, a false refutation of a real effect; at three quarters, about 14%; at the whole gap, about
4%. The clause can refute a vanished effect about one time in two, and cannot tell a gap of half the
long history's from none. These rates draw the months at random; the lab's years hold 2008, known to
be among the worst Septembers and Octobers, which by itself moves the difference by about four
fifths of a standard error towards the claim: in the lab's years a refutation is less likely than
the simulation's rates, and the difference without 2008 is read beside the clause.

**What the gates can pass.** In the same simulation, gate 4, which needs an appraisal ratio of about
0.7, passes about one time in twenty even at the whole gap; the placebo check of gate 3 passes about
half the time at the whole gap. "Not proven" is the expected verdict even if the theory holds; a
refutation or a clear gap is what the card can show.

**Measures stated before the run**, reported, not graded:

- the difference for the variant, September against the other eleven months;
- the five funds' average daily excess return in each of the twelve calendar months, in-sample, with
  its standard error, and the rank correlation of those twelve averages with the order of Ilmanen's
  figure, near-ties taking the order read and exact ties average ranks — the bank's second
  refutation reads a ranking that changes from one period to the next;
- the difference by fund and by year, and the difference without 2008;
- the base's alpha with its two months moved a month earlier, August and September, and a month
  later, October and November: gate 6 cannot move a month's name, so this is read beside it.

**Risks named before the run.**

- **Crises.** Eighteen Septembers and Octobers decide the test; September and October 2008 alone can
  move it by several points, and the long history's weakness itself rests on crashes (1929, 1987,
  2008).
- **One fund's share.** The five funds form one of the lab's clusters, so gate 6 leaves no cluster
  out, but no fund may carry more than 30% of the profit; the volatile funds, small caps and
  emerging markets, may carry most of the months' gap.
- **The neighbours.** The first month is named, not counted: moving a month's number by a quarter,
  September to July or November, would test the claim's contrast — cash in months the sources call
  good — not the rule's robustness. Gate 6 moves the number of months out, one or three — September
  alone, the variant, or September to November, adding a month the sources call strong — and the
  months moved a month either way are reported beside it. The claim itself predicts that these do
  worse than the base, since October is weak and November strong: gate 6 may fail here without
  speaking against the theory.
- **A day's delay.** Gate 6 delays the rule by a session: it then leaves on September's first
  session and returns on November's first, a small change.
- **The overlap with SC-018.** SC-018's half-year out of equities contains these two months; a
  result here tells SC-018 about its September and October only.

## Choices, and the options rejected

- **A rule over the twelve months, weighted by their long-history averages**: it would need the
  figure's twelve values, read by eye to a tenth of a percent, as parameters, and a long-only rule
  can only scale down; the two named months carry the claim's sharpest statement.
- **Holding only from November to February**: the bank's "solid" months, but the rule would then be
  out six months of the year and very close to SC-018's test of the Halloween effect.
- **January alone**: SC-002's claim, about small stocks at the turn of the year.
- **A short position in the weak months**: the lab is long only.
- **Bitcoin**: the sources' evidence is on equity indices, and the bank's asset classes do not
  include it.

## Implementation

Long only, five equity funds, each with a European (UCITS) fund that tracks it, or cash, one round
trip a year on a calendar known in advance, with the orders filled at the close of the session on
which they are set; gate 6 adds a day's delay.
