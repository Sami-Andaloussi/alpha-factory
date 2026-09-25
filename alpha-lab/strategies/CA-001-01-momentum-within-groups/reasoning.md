# CA-001-01 — Momentum within sectors, equity markets and commodities: reasoning

## Why this theory now

CA-001 states that within a group of comparable assets — sectors, countries, baskets or themes —
those with the strongest recent relative performance go on to outperform those with the weakest,
and that the continuation holds across asset classes. Its sources' strongest evidence is the
cross-asset study of Asness, Moskowitz and Pedersen (2013), whose third author wrote one of the
theory's references: the same momentum measure, ranked within each market and asset class, earns a
premium in almost every one of them, and the premia of the classes are correlated but distinct. The
lab holds three groups of that kind: eleven US sectors, five equity markets and three commodity
funds. Taken together, they test the theory where the lab is broadest.

The bank holds its neighbours, each a card of its own:

- **TM-003**, industry momentum, is the same ranking inside the sectors alone, explained by the
  diffusion of news along industries; this card ranks the sectors as one of three groups.
- **CA-017**, international momentum, ranks national and regional markets alone.
- **TM-001**, cross-sectional momentum, is the general relative form, first stated on individual
  stocks, which the lab does not hold.
- **CA-024**, value and momentum everywhere, adds value and the covariance of the two premia.
- **TM-017**, time-series momentum, which CA-001's prediction also names, compares an asset with
  cash, not with its peers: TM-017-01 tested it on the lab and stopped at gate 3.
- **TM-047** scales each position by its volatility.

This card tests the relative half of CA-001: winners against losers, within each group.

## From the mechanism to a signal

News, a change of regime or an imbalance of flows reaches the prices of a group's members at
different speeds, and capital reallocates slowly between them: a member that led over the past
year keeps leading for a while. The signal ranks each group's members by that past year, and the
portfolio holds the leaders.

- **The measure** is the one the sources use for every asset class: the return over the past
  twelve months, the most recent month left out, "MOM2–12" (Asness, Moskowitz and Pedersen, 2013,
  after Jegadeesh and Titman, 1993). In sessions, counted back from the session before the target,
  the last close the signal may read: the window starts 252 sessions before it and ends 21 sessions
  before it.
- **The groups** are the theory's comparable assets, each a class of its own in the sources:
  - **sectors**: the eleven US sector funds (XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV,
    XLY);
  - **equity markets**: US large caps, US large-cap growth, US small caps, developed markets outside
    North America and emerging markets (SPY, QQQ, IWM, EFA, EEM) — the countries and baskets of the
    theory, as far as the lab has them;
  - **commodities**: gold, silver and the commodity basket (GLD, SLV, DBC).
- **The top third of each group** is held, rounded, one at least: the sources rank each class into
  three equal groups and report the high one, P3, equal-weighted outside individual stocks. A long-
  only portfolio holds P3 and leaves P1; the sources measure P3's premium against the class's
  equal-weighted basket for commodities, and against the world index for country indices. Here: four sectors of eleven (three of nine or ten before XLRE
  and XLC have a year of prices), two equity markets of five, one commodity of three.
- **Each group keeps its share of the universe**: of the N assets trading, a group of n ranked
  members holds n/N of the portfolio, split equally among its leaders, and an asset trading but not
  yet ranked is held at 1/N. The benchmark holds every asset trading in equal parts, from its first
  session, so each group carries the same share of both: the strategy differs from the benchmark only
  by which ranked members of each group it holds, which is the theory's claim, and not by how much
  it puts in sectors, markets or commodities, which is not. The targets start on the first month in
  which an asset is ranked, early in 2006; from then the portfolio is always fully invested.
- **Monthly**: the targets are set on the first session of each month, from closes up to the session
  before, as the sources rebalance.
- **A late asset** is ranked only once it has 252 sessions of prices: DBC from about February
  2007, SLV from about May 2007, XLRE from about September 2017, XLC from about June 2019. Until
  then it is held at its benchmark weight and its group ranks the others; until DBC and SLV have a
  year, gold is the commodity group's only ranked member, and all three are held at 1/N.

**The variants.** The base is MOM2–12. The second keeps the most recent month, MOM1–12 (a skip of
0): the sources skip it only to avoid the one-month reversal of individual stocks, and report that
outside individual stocks — equity index futures and currencies, for instance — momentum is stronger
without the skip; their own form for such markets is a variant here, declared before any run. Two variants, not
three: each is a trial every later card pays for.

## What the battery judges, and what to expect

The benchmark holds the same nineteen funds in equal parts, set back to equal parts whenever the
strategy trades: the strategy's alpha is what choosing the leaders of each group adds to holding
the whole group: the sources' comparison of P3 with the class's equal-weighted basket, which they
make for commodities; for country indices they compare P3 with the world index.

**The size predicted.** The sources' top third earns an alpha of 4.4% a year against the world
index among 18 country indices (1978 to 2011), and 5.8% a year against the equal-weighted basket
among 27 commodities (1972 to 2011) (Asness, Moskowitz and Pedersen, 2013, Table I); among
government bonds, nothing, which is one reason bonds are not a group here. The portfolio's alpha is
the groups' alphas weighted by their shares: 11/19 for the sectors, 5/19 for the equity markets,
3/19 for the commodities. The sources' figures speak for the last two only, and there the lab is
narrower: three commodity funds instead of twenty-seven, and three overlapping US baskets beside two
foreign markets instead of eighteen countries. For the sectors, the sources give no figure; their
share of the prediction is an assumption, carried over from the other classes at the same discount.
The lab's years, 2005 to 2022, are also later than the sources'. The card therefore expects about
half the sources' premium: an alpha of about 2% a year, with a Sharpe ratio a little above the
benchmark's.

**The test's power.** The strategy trades once a month in three groups; its bets are few and
correlated. Gate 3 compares it with its own positions shifted in time by a year or more: a real
edge among so few assets can fall short of the 90% of placebos the gate asks. The verdict will say
how many independent decisions the strategy made, and whether a failure is the edge's absence or
the test's weakness. Two risks of gate 6 have nothing to do with momentum, and the verdict will
tell them apart from a missing edge:

- **Leaving the sectors out** compares Sharpe ratios, not alphas: without the sectors, the
  commodities rise from 3/19 to 3/8 of the portfolio, and the mix alone can halve the Sharpe ratio.
- **One asset's share of the profit**: the one commodity held carries 3/19 of the portfolio, and a
  fund that leads for years, XLK or QQQ, may be held for long stretches; the 30% limit is within
  reach, as SPY's 33% was for TM-017-01.

**What a verdict covers.** The sectors carry 11/19 of the portfolio, so a result they carry is
mostly industry momentum, TM-003's hypothesis. A later TM-003 card counts in gate 4 with this one:
the registry clusters trials whose bets are near-clones, so that the two cards are not counted as two
independent tries if they hold the same sectors. A failure here refutes or leaves unproven the
relative half of CA-001 on these groups; the time-series half is TM-017's.

## Choices, and the options rejected

- **Bonds** (SHY, IEF, TLT) are not a group: the theory's classes are stocks, sectors, equity indices
  and commodities, the sources find no momentum among government bonds, and the lab's three bond
  funds are one market at three maturities, where a ranking would be a bet on duration.
- **Bitcoin** is not a group: the theory does not name it, and a group of one asset ranks nothing.
- **One ranking across all nineteen funds** would compare a sector with gold by raw return, and
  hold whatever is most volatile after a rise; the theory compares comparable assets.
- **Groups weighted equally**, or by volatility as the sources' combined portfolio is: either would
  add a bet on the groups themselves — more commodities, fewer sectors than the benchmark — that the
  theory does not make, and whose result the battery would credit to momentum.
- **The absolute filter** (holding a leader only while its own trend beats cash) is time-series
  momentum, TM-017's hypothesis; combining the two is another card.
- **The six-month formation** of Jegadeesh and Titman is not a variant: gate 6 moves the lookback to
  126 and 378 sessions around the base in any case.
- **Weekly rebalancing**: the sources rebalance monthly, and a signal of a year moves little in a
  week.

## Implementation

Long only, fully invested, nineteen funds, each with a European (UCITS) fund or an exchange-traded
commodity that tracks it (sector funds, the five equity markets, gold, silver and a commodity
basket), six to eight held at a time, rebalanced monthly on closes with the orders filled at the
next close: the signal reads the session before, so a day of delay is built in, and gate 6 adds
another.
