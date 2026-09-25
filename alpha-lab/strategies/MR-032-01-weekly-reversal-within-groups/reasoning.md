# MR-032-01 — Last week's laggards within sectors, equity markets and commodities: reasoning

## Why this theory now

MR-032, cross-sectional mean reversion, holds that the assets that most outperformed their universe
over a short period tend to underperform it over the next, and the reverse: the extremes return
towards the centre, the predictive power decaying within days, more strongly in small and mid
capitalisations than in large, liquid instruments. The mechanism the sources give is price
pressure: a laggard fell under selling pressure, a leader rose under buying pressure, and whoever
buys the one and sells the other supplies liquidity and is paid for it. It is the only short-horizon
contrarian theory the lab has taken up; the momentum rules it has run ranked over a year.

**The bank's neighbours.** **MR-001** and **MR-002**, short-term reversal as liquidity provision and
as overreaction to news, name daily and intraday forms and data the lab does not hold (quotes,
volumes, news); **MR-011** conditions the reversal on volume. **MR-031**, reversion within groups of
economically close assets, overlaps this card: its asset classes include sectors, equity indices and
commodities, and its second refutation criterion, reversal within groups no stronger than across
the market, is what this card's base (within groups) against its pooled variant (the nineteen
together) measures. The card is drawn from MR-032 because it tests reversion to a basket's centre,
Chan's form, with the groups as the baskets; under the C1 decision on published results, its verdict
will be known to any MR-031 card on these funds, which will say so.

**What the lab already knows.** CA-001-01 kept the last month in a 12-month ranking (its variant):
an appraisal ratio of 0.11 against 0.03 over the whole portfolio, within noise (±0.24), but −0.10
against −0.07 among the sector funds (TM-003-01's verdict); its gate 6 moved the skipped month to
16 or 26 sessions at no cost, and to 10 or 32 within a median of 106% of its Sharpe ratio. The last month is a twelfth of that window; the evidence on a
one-month reversal in these groups is weak and mixed, and nothing published bears on a week.

**The sources.** The lab read them in the library's books; Khandani and Lo (2007) is known to it
through Chan and Ilmanen.

- Chan (*Algorithmic Trading*, 2013, chapter 4) calls cross-sectional mean reversion the tendency
  of the returns of the members of a basket to revert to the basket's return, "prevalent in
  baskets of stocks", and gives Khandani and Lo's linear long-short model: each day, hold each stock
  in proportion to minus its return less the basket's average, normalised to a gross of one. On the
  S&P 500 from 2007 to 2011 it earned 13.7% a year at a Sharpe ratio of 1.3, before costs. At the
  opening of his next chapter he writes that most portfolios of currencies or futures do not show
  cross-sectional mean reversion, which bears on the commodity group.
- Ilmanen (*Expected Returns*, 2011) reports that last month's winners among stocks strongly
  underperform last month's losers over the next month, most compellingly explained by price
  concessions to large trades; that reversals are stronger over a day or a week, for less liquid
  stocks, with industry-adjusted returns and amid high volatility; that on paper, in his table of
  equity strategies, short-term reversal fared even better than momentum and value, and that its
  double-digit gross returns are estimated to have been negative after costs; that liquidity
  providers' profits from it have declined over time; that across studies returns continue except
  over windows of a week or shorter and of two to five years, where reversal may dominate; that,
  unlike stock-specific momentum, industry momentum works over very short horizons too; and that
  the equity pattern does not travel well to other asset classes.
- Ilmanen (*Investing Amid Low Expected Returns*, 2022) repeats that single stocks reverse over a
  week or a month, from liquidity provision and price pressure, gives a five-day reversal as his
  example of a signal with strong gross and negative net alpha, and adds that in more liquid futures
  markets assets show momentum also at short horizons.
- Grinold and Kahn (*Advances in Active Portfolio Management*, 2020) model a signal whose forecasting
  power decays exponentially: in their Exhibit 5, a signal with a one-day half-life keeps 29% of its
  skill when updated weekly and 7% monthly; one with a one-week half-life, 72% and 32%.

The sources thus expect, among the lab's funds, reversal at most over a week, and momentum among
the sector funds and the commodities — fourteen of the nineteen — over short horizons as well.

## From the claim to a signal

- **The basket**: the claim is reversion to the centre of a set of comparable assets. The lab's
  nineteen funds are not one such set — a sector fund and a silver fund share no centre — so the
  base takes the three groups CA-001-01 and CA-024-01 used as three baskets, Chan's basket read as
  a group of comparable funds. Ilmanen finds reversals stronger for stock returns net of their
  industry, and industry returns themselves trending at short horizons: ranking sector funds
  against one another ranks exactly the industry component that trends, so the sources expect no
  reversal there. **Variant 2**: the nineteen as one basket, the bank's "median of the universe"
  read literally.
- **The horizon**: the claim decays within days, but the core rebalances weekly at the fastest, and
  its orders are filled at the close of the session they are set on, after the signal read up to
  the session before. The base is weekly: on the first session of each calendar week, the return
  over the last five sessions to the session before, the "day and week" horizon Ilmanen names and
  his five-day reversal. **Variant 1**: the return over the last 21 sessions, on the first session of
  each month, the one-month reversal Ilmanen reports for stocks. The daily form, Chan's, is out of
  the core's reach and not tested; a result for a week says little of a day.
- **The selection**: long only, the laggards: within each group, the bottom third of the ranked
  members by that return, rounded, one at least, a tie at the cut held by the member listed first
  in the card's universe — CA-001-01's construction, the ranking reversed and the window shortened. Chan's weights
  proportional to the relative return need a short side; the lab holds the laggards in equal parts,
  against the funds held in equal parts: a relative bet all the same.
- **The weights**: a group of n ranked members of N funds trading holds n/N of the portfolio,
  equally among its laggards; a fund trading but not ranked, in its first sessions, holds 1/N. In
  the pooled variant the nineteen are one group.
- **The week**: Monday to Sunday; its first session is a Monday 846 times in-sample, a Tuesday 89
  times and a Wednesday twice.
- **The memory**: 21 sessions, the monthly variant's window.

The pace was counted before the card by a scratch script outside the repository (`pace.py`, in the
session's scratch folder) that reads the signals alone: 937 weekly targets from 2005-01-18, 214
monthly from 2005-03-01; the weekly selection changes by about 62% of its weight a week, which at
the lab's 5 bps a side costs about 3.2% a year, the monthly about 0.75%.

## What the battery judges, and what to expect

**The size predicted — a judgment, not derived.** No source gives a figure for funds like these:
the long record's reversal is a stock-level effect, strongest in small and illiquid stocks, over
days, and the sources expect momentum, not reversal, among fourteen of the nineteen funds. The card
predicts a weekly rank correlation, within groups, of about −0.01, between −0.02 and a little below
zero. The within-group spread of the funds' five-session returns, about 1.0 to 1.8%, turns a
correlation of −0.01 to −0.02 into a gross alpha of about 0.5 to 1.5% a year over the funds held in
equal parts; after costs of about 3.2% a year, 0.2 or so of a Sharpe unit at the strategy's
volatility, the alpha is clearly negative. A correlation near −0.045 would break even at the lab's
costs; gate 2, which asks a positive alpha at twice the costs, would need one near −0.09. These
figures hold for the correlation over the returns the rule holds, from the target's close; the
graded correlation, one session earlier, is larger if the reversal decays within days, so the alpha
may be up to half of what the graded figure suggests.

**The clause.** The theory's own statement is a negative relation between an asset's past relative
return and its next. The card measures it directly, before costs, on the weeks of the in-sample
years: on each weekly target session from the base's first, 2005-01-18, whose next window ends on or
before 2022-12-30, within each group with three ranked members or more, the rank correlation
(Spearman's) between the members' returns over the five-session window, to the close of the session
before the target, and their returns from that close to the close of the session before the next
weekly target session — the week that follows the window, no session left out; each week the
groups' correlations averaged, each weighted by its number of ranked members; the mean over the
weeks, with its standard error, the weekly series' standard deviation over the square root of the
number of weeks. The theory is refuted in this form if that mean is +0.004 or above, about half its
expected standard error: no negative relation, or the short-horizon momentum the sources expect
among industries and futures. A mean below +0.004 short of passing gates 1 to 7 is not proven, not
refuted; a base that passes gates 1 to 7 while the clause refutes leaves the theory refuted in this
form. Of MR-032's refutation criteria, the first is graded; the second, a decay within days, is
reported through the decay measures; the third, the effect in small against large capitalisations,
cannot be tested on these funds.

**The test's power.** A synthetic simulation by the logic audit — groups of about ten, five and
three members, the weekly average weighted by members — puts the weekly series' standard deviation
at about 0.25 and the mean's standard error at about 0.008 over 937 weeks. The clause then refutes
about 31% of the time with no relation, 13% at a correlation of −0.005, 4% at −0.01 and 0.2% at
−0.02. A point threshold at zero would have refuted a true −0.005 about 27% of the time; the band
keeps a weak reversal of the long record's sign from being called refuted. At −0.01 the clause
refutes 4% of the time against 31% with none; it tells −0.02 from none reliably, and a correlation
between −0.01 and zero hardly at all.

**Measures stated before the run**, reported, not graded:

- the same correlation with the groups weighted equally; the reported measures use the same weeks,
  less those whose window ends after 2022-12-30 (936 for the tradable measure);
- the same correlation over the returns the rule can hold, from the target's close to the next
  target's close;
- the monthly variant's correlation (21 sessions, the month that follows, measured as the base's)
  and the pooled variant's (the nineteen as one basket);
- the decay: the base's correlation with (a) the target session's own return, from the close of the
  session before to the target's close, which the rule cannot hold; (b) the first session held, from
  the target's close to the next session's close; (c) the week after next, from the next weekly
  target's close to the close of the target after it;
- the correlation by group, and in 2008 and 2020, the years of high volatility where the sources
  expect the reversal strongest; the weekly series' lag-one autocorrelation;
- each variant's alpha before and after costs, and its costs.

**Risks named before the run.**

- **Costs**: about 3.2% a year for the weekly rule, some 0.2 of a Sharpe unit, against a gross edge
  predicted small; gate 2 fails a rule whose costs take more than a third of its gross Sharpe ratio.
- **Few members**: the commodities hold one laggard of three; the equity markets two of five. A rank
  correlation over three members takes four values; weighting by members keeps the commodity group
  from dominating the weekly average.
- **The neighbours**: windows of 4, 6, 2 and 8 sessions on a weekly pace change most selections;
  gate 6 compares their Sharpe ratios with the base's.

## Choices, and the options rejected

- **Recording the theory not testable**: its sources' domain is stocks, daily, but the bank names
  equity indices and commodities at days and weeks, its first refutation criterion is a sign test
  that holds in any universe, and its third expects a weaker, not a nil, effect in liquid
  instruments; the verdict will be scoped to liquid funds at a weekly pace.
- **A daily rule**, Chan's form: the core rebalances weekly at the fastest.
- **Chan's linear weights with a short side**: the lab is long only.
- **A point threshold at zero**: it would refute a true weak reversal too often.
- **Skipping a session between the signal and the trade**: the lab's fill at the close of the
  target session already follows the signal by one session; gate 6 adds another.

## Implementation

Long only, nineteen funds, each with a European (UCITS) fund that tracks it, weekly targets filled
at the close of the session on which they are set; gate 6 adds a day's delay.
