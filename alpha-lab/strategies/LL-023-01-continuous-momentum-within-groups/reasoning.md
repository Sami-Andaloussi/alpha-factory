# LL-023-01 — Continuous momentum within groups: reasoning

## Why this theory now

LL-023, the frog-in-the-pan, holds that information is underweighted not because it is missing but
because it arrives quietly. Da, Gurun and Warachka (2014) argue that many small changes draw less
attention than a few dramatic ones, so that investors underreact to information that arrives
continuously. Two stocks with the same past year's return did not receive the same news if one rose
through many small gains and the other through a few jumps; the first has been priced more slowly
and keeps moving longer.

They measure the path by information discreteness, ID: the sign of the formation return times the
share of the formation period's daily returns that are negative less the share that are positive,
over the twelve months before the last one, the window of the momentum return. A past winner with
many more positive days than negative ones has a low ID, continuous information; one whose return
came from a few large days has a high ID. Sorting US stocks from 1927 to 2007 first into quintiles
of past return and then, within each, into quintiles of ID, they find that the momentum profit over
the next six months falls from 5.94% for the most continuous stocks to −2.07% (a t-statistic of
−2.01) for the most discrete (their Table 2, Panel A), that the profit of continuous momentum
persists for about eight months where discrete momentum's fades, and, from 1980, that the disparity
is larger where attention is lower: 7.17% among small stocks against 4.92% among large ones, 6.83%
with low analyst coverage against 3.41% with high. Their simulation adds a limit: ID tells
continuation apart only for stocks with a large past return, and says little when it is near zero.

The long side, which is all a long-only rule holds, carries a smaller part of the disparity. Among
the winners of 1927 to 2007, the six-month returns of the five ID quintiles run from 7.53% for the
most discrete to 9.48%, 10.01%, 9.98% and 9.56% for the most continuous; from 1980, from 7.60% to
9.53%, 10.86%, 10.57% and 10.54%. The more continuous half of the winners beat the more discrete
half by about 1.0% over six months from 1927 and 1.6% from 1980, about 2 to 3% a year, before any
adjustment for risk. Gray and Vogel (*Quantitative Momentum*, 2016, chapter 6) split the top decile
of mid- and large-cap stocks by past return in half by ID, from 1927 to 2014: the continuous half
compounded at 17.14% a year and the discrete half at 13.02%, gross of fees, about 4% apart. Their
own system (chapter 8) keeps the screen: the top tenth by past return, then its more continuous
half, with the path measured over the past 252 days.

The lab has run momentum within groups of funds: CA-001-01 held the top third of each group by its
past year's return, and its choice of funds beat 47.6% of its placebos. This card keeps its groups,
ranking, weights and pace, and asks the source's own question within them: of each group's leading
funds, do the more continuous continue more than the more discrete?

The bank's neighbours: **CA-001**, momentum within groups, whose construction this card reuses;
**TM-024**, the crash risk of the same rule; **TM-002**, nearness to the 52-week high, another
reading of a price's path; **LL-024**, media-limited diffusion, and **LL-025**, information
discreteness and lead-lag, the same attention mechanism in other forms; **TM-047**, momentum scaled
by its volatility.

## From the claim to a signal

- **The universe and the groups**: CA-001-01's, the eleven sector funds, five equity markets and
  three commodities, ranked within their group. The bank extends the mechanism, by analogy, to
  markets whose trends are fed by a sequence of macroeconomic data, flows and reports rather than by
  a single shock; the funds are that form, not the source's stocks.
- **The window**: Da, Gurun and Warachka's, the past twelve months less the last one, 252 sessions
  ending 21 before the session before the target, for both the return and the path. Gray and Vogel
  measure the path over the last 252 days, the last month included; the card follows the paper.
- **The pool and the two halves**: Gray and Vogel's split, scaled to a group. Their pool is the top
  tenth of a thousand stocks by past return, split in half by the path; the lab's groups hold two to
  eleven funds, so the pool is the group's 2k highest-ranked funds, twice the k that CA-001-01
  holds, and each half holds k funds in CA-001-01's weights. The base holds the more continuous
  half, the variant the more discrete half of the same pool: the two are chosen by the path alone,
  from the same funds, though the continuous half may hold the higher past returns (below). In the
  commodities the pool is the best two of three funds, in the equity markets the best four of five,
  in the sectors the best six while nine or ten are ranked and the best eight of eleven from 2019,
  when XLC is first ranked.
- **The score**: the count of the window's positive daily returns less the count of its negative
  ones, divided by the window's 231 returns. For a fund whose window return is positive, it is minus
  the source's ID, and the most continuous winners score highest, as Gray and Vogel rank theirs. For
  a fund whose window return is negative — the pool can hold such funds in a falling year — a high
  score marks a discrete loser, which the source finds falls less than a continuous one: the
  continuous half then holds the funds the theory expects to fall least. Ties, which counting days
  makes possible, go to the higher window return. Days of zero return count in the denominator and
  on neither side, as in the source's first measure.
- **The pace**: CA-001-01's, the first session of each month, a one-month holding of a signal the
  source finds persistent for about eight. Gray and Vogel rebalance quarterly to save costs, and the
  source holds six months; the card keeps CA-001-01's pace, so that the halves differ only in the
  path.

Drafts of the strategy, of its build plan and of the checks the code will get before the run were
written in the session's scratchpad before this card's audit; none was run, and none is used: the
code is written again from the committed card. No count of the signal was made before the card. The
verdict will report how many funds the two halves hold in common with CA-001-01's leaders, and how
often a pool fund had a negative window return.

Two variants, not three.

## What the battery judges, and what to expect

**The halves against each other.** Gates 2 to 4 judge the base against the nineteen funds held in
equal parts, as they judged CA-001-01. The theory is judged by the base's alpha less the variant's,
over the base's sessions and costs, by `python -m lab.compare` with the card named twice. The base's
alpha less CA-001-01's is reported as well, not graded: it mixes the path with the past return the
pool gives up, and the source's own tables, from 1980, put that trade for a pool of the top two
thirds at between −1.4% and +0.4% a year on stocks before any scaling, depending on the subsample.

**The size predicted.** On stocks, the sources' halves of their winners differ by 2 to 4% a year:
the paper's halves of its top quintile of past return by about 2% from 1927 and 3% from 1980, Gray
and Vogel's halves of their top decile by about 4%. A pool as wide as the lab's reaches further
down the ranking, where ID says less: reproducing the card's split on the paper's Table 3, from 1980
— a pool of the top two thirds by past return, each quintile of it split in half by ID — gives a
difference of 1.0% a year among stocks with low analyst coverage, 1.6% among large stocks and up to
2.5% among stocks with high institutional ownership; a pool of four of five, as in the equity
markets, gives 0.8 to 2.3%. The card halves about 1 to 2.5% a year to about 0.5 to 1.25%: an
assumption, not the source's. A fund is a basket whose daily returns average its members'
paths, and the news that moves a sector or a market is among the most watched; the paper finds the
long-short disparity among large stocks about two thirds of that among small ones and, with high
coverage, about half of that with low. And the paper's sample ends in 2007, before its publication,
where the lab's runs from 2006 to 2022; no source measures the decay since.

**What the score also measures.** For daily returns drawn from a normal law of mean μ and volatility
σ, with μ/σ small, the share of positive days less the share of negative days is about 0.8 μ/σ; fat
tails raise the factor, to about 1.06 for a Student law with four degrees of freedom. Among funds of
similar window return, the score prefers the one with the lower volatility. In the sectors it will
lean towards staples, health care and utilities, among the equity markets towards SPY over EEM and
IWM, among the commodities towards gold over silver. The paper controls for each stock's
idiosyncratic volatility, its residual from a four-factor model, in its regressions; nineteen funds
cannot separate the two. TM-002-01's alpha, over its sectors, came from such a tilt towards the
steadier funds, which its average mix held fixed earned. The verdict will report the two halves'
betas and the alpha of each half's average mix held fixed, so that a difference made by a steadier
mix is not read as the path's.

**The noise of the difference.** CA-001-01's bets, hedged of its benchmark, moved by about 6 to 7%
a year (0.20% of alpha at an appraisal ratio of 0.03, a rounded figure). The two halves hold
disjoint funds of each pool; their difference holds each group's chosen k long and its other k
short, in weights half again as large as CA-001-01's tilt, between funds closer in return. By a
rough estimate it moves by 6 to 9% a year: a standard error of about 1.5 to 2.2% a year over 16.9
years. The clause refutes only below −1% a year and more than one measured standard error below
zero. At a standard error of 1.8%, a true difference of zero would be refuted about 16% of the time,
the predicted +1% about 6% of the time, and a true −3% about 75% of the time. The predicted
gain lies within one standard error of zero: the card can refute a clear reversal of the claim, and
cannot show the gain it predicts.

**The test's power.** Gate 4 will count about sixteen effective trials; an appraisal ratio of about
0.7 would be needed to pass it, where CA-001-01's was 0.03. Gate 5 blends the two halves, which
together hold the whole pool: it judges the pool held in equal parts more than the theory, and is
likely to fail for that reason alone. The comparison of the halves is the informative test.

**Risks named before the run.**

- **A small pool.** In the commodities the halves are one fund each, in the equity markets two
  each: the score decides between close neighbours, and a year of 231 daily returns separates two
  funds' scores by a handful of days.
- **A steadier mix**, above: the difference may be a tilt, not the path.
- **Past return.** In a pool that spans most of a group, the continuous half is also likely to hold
  the higher past returns, since the score tracks μ/σ; the difference then carries some of
  CA-001-01's momentum, which the paper's sorts within a quintile of return exclude.
- **2008 and 2009.** In a falling year most of the pool has a negative window return and the
  continuous half holds the discrete losers; in the rebound of 2009 the smoother funds are likely
  to be the defensive ones.
- **XLC**, first ranked in 2019, raises the sectors' k from three to four and their pool from six to
  eight; XLRE, ranked from late 2016, leaves them at three and six.

## Choices, and the options rejected

- **CA-001-01's top third as the reference**, the continuous half of the pool against the funds
  CA-001-01 holds: set aside after the card's audit. It compares the path with the past return the
  pool gives up, which neither source claims, and the source's own tables predict about zero or a
  loss for it; it is reported, not graded.
- **The lowest ID for every fund**, as Gray and Vogel rank their winners: identical for funds whose
  window return is positive; for those whose return is negative, the continuous half would hold the
  continuous losers the source finds fall most.
- **One scale across signs**: the score ranks a discrete loser against a continuous winner on the
  same scale, which the source never does; rare, since a winner's score is mostly positive and a
  loser's negative. Set aside: ranking every winner before any loser, which the source does not do
  either and which adds a rule of its own.
- **A pool of the top half of each group**: closer to a decile in spirit, but it changes the number
  of funds each half holds from CA-001-01's.
- **Ranking the whole group by the score**: drops the past return from the choice, which the source
  keeps first; a test of a smooth path alone.
- **Market-adjusted daily returns**, which the paper finds give similar results: within a group the
  adjustment by a common market mostly counts the days a fund beat its group, another measure.
- **The paper's measure without zero-return days**, which drops them from the denominator: its
  winners change little under it, its long-short profit more (8.01% falls to 4.75% from 1927); the
  card keeps the first measure, the paper's and Gray and Vogel's.
- **A six-month or quarterly holding**: above.
- **A cost accepted: a variant built to do worse.** The discrete half is the theory's
  counterfactual, not a strategy offered to the factory: it spends a trial of gate 4 on a rule
  expected to do worse, and gate 5's blend of the two halves holds the whole pool, so the card is
  unlikely to pass gates 1 to 7 whatever the path is worth. The card tests the theory. Set aside: a
  separate card for the discrete half, which would spend the same trial and add a card; and
  CA-001-01 as the reference, above.

## Implementation

Long only, nineteen funds, each with a European (UCITS) fund or an exchange-traded commodity that
tracks it, rebalanced monthly on closes with the orders filled at the next close: the signals read
the session before, so a day of delay is built in, and gate 6 adds another.

This card addresses the first of the bank's refutations, continuous winners continuing no more than
discrete ones; the second, the speed at which the same news enters prices in increments or at once,
and the third, a disparity larger where attention is lower, are not tested: the lab holds no
measure of attention across its funds.
