# CA-024-01 — Value within sectors, equity markets and commodities: reasoning

## Why this theory now

CA-024, "value and momentum everywhere", holds that within each asset class cheap assets outperform
expensive ones and recent winners outperform recent losers, and that these value and momentum
returns share a common structure across asset classes: correlated with each other class by class,
losing together in the same drawdowns, value and momentum negatively correlated with each other. The
theory is a framework rather than one channel; the bank names underreaction, overreaction, funding
constraints, risk aversion and segmentation.

Its momentum half has been tested: CA-001-01 held the top third of each of three groups — the eleven
sector funds, the five equity markets and the three commodity funds — by its past year's return, and
was refuted in its base form, an alpha of 0.20% a year over the same funds held in equal parts. The
value half has not. This card tests it on the same groups and funds, so that the common structure
the theory claims can be read beside CA-001-01's record. The combination of the two, a single
portfolio of value and momentum, is the claim of **TM-040**, trending value, left to that theory.
The C1 decision on cards that reuse an earlier card's construction does not apply: value neither
refines nor replaces momentum's signal, and the benchmark is the groups held in equal parts, not
CA-001-01.

**The bank's other theories this card touches**, all untouched, and how it differs from each:

- **MR-021**, long-term overreaction and reversal, three to five years, on stocks and on sector or
  geographic indices: on the equity groups, which hold 16 of the 19 funds, this card's price-only
  value is that reversal. The card tests it as CA-024's value measure within groups, with CA-024's
  claim of a common structure; MR-021's claim of a transitory component in each index's own price,
  and its reversal on the extremes of past performance, are its own.
- **CA-019**, mean reversion across national stock markets, and **CA-018**, country value: this
  card's equity-markets group is three overlapping US baskets and two foreign ones, not a set of
  countries.
- **CA-021**, value across sectors, countries and asset classes on price against fundamentals: this
  card uses no fundamental.

Under the C1 decision on published results, this card's verdict will be known to those theories'
cards, and they will say so.

**The sources.** The lab read them in the library's books; Asness, Moskowitz and Pedersen's study
(2013; its 2009 working version in Ilmanen and the Zacks handbook) is known to the lab through them.

- The Zacks *Handbook of Equity Market Anomalies* (2011) describes the study's construction: for
  commodities, value is the spot price five years ago divided by the latest, the inverse of the
  five-year return; for currencies, the negative of the five-year return with interest; for country
  bond indices, the real yield; for stocks and country indices, book to market. Within each asset
  class the securities are sorted into thirds, equally weighted outside stocks. The value premium
  was about 3.5% a year in stock selection in the US, the UK and Europe, 3.8% in currencies and 5.8%
  in commodities from 1975 to 2008; value returns were positively correlated across asset classes
  and negatively with momentum's.
- Ilmanen (*Expected Returns*, 2011, §12.5) reports the same study: deliberately naive value
  measures, chosen to avoid overfitting; every strategy with a positive Sharpe ratio, from 0.1 to
  0.9; the commodity and currency measures close to long-term reversal; and "if no obvious ex ante
  value indicator is available, multi-year average return is often a reasonable substitute". He
  warns there that in crises in which levered positions are unwound "cheap assets get cheaper",
  autumn 1998 and autumn 2008 the most extreme, that value strategies are short a structural break,
  and that a lasting rerating of emerging markets against developed ones would cost contrarians. In
  §12.6 he writes that long-run reversal buys assets whose prices are low against their own history
  three to five years earlier, and that value and momentum, natural opposites, combine to much
  steadier returns.
- Ilmanen (*Investing Amid Low Expected Returns*, 2022) gives the five-year reversal of US stocks
  (Ken French's long-term reversal factor) a Sharpe ratio of 0.27 against 0.34 for value by book to
  price, with a correlation of 0.6 between them: the price-only form is value's weaker cousin. He
  shows value premia by decade in several asset classes: positive over the whole sample, negative in
  the 2010s in several of them; US value by book to price fell 63% from its 2007 peak to its 2020
  trough.
- Pedersen (*Efficiently Inefficient*, 2015) calls the past five-year return the simplest measure of
  value (De Bondt and Thaler, 1985), and long-run reversal a value trade that "also works in all the
  other asset classes".
- Cochrane (*Asset Pricing*, 2005) reports Fama and French's reversal strategies on US stocks formed
  on the returns of months 60 to 13, the last year left out.
- Ang (*Asset Management*, 2014) reports Israel and Moskowitz: value and momentum premia remain when
  an investor cannot short, but 50 to 60% smaller.

## From the claim to a signal

- **The measure**: the lab has prices only, so value is measured as the sources measure it where no
  fundamental ratio is used — the price some years ago against today's, the return over the window
  reversed: the cheapest are the members whose price fell most, or rose least, over it. For
  commodities this is the study's own measure; for sector funds and equity markets, where the study
  uses book to market, it is the substitute Ilmanen names, the multi-year return, whose US record is
  weaker than book to price's. The card says so: on the equity groups this tests long-run reversal,
  the price-only form of value.
- **The window**, base: five years, 1,260 sessions, the study's anchor for commodities and
  currencies. **Variants**: three years, 756 sessions, the short end of Ilmanen's three to five
  years; and five years with the last year left out, `skip` 252 sessions, the form of Fama and
  French's reversal strategies, which keeps the momentum year, with its opposite sign, out of the
  measure. All from the sources, not from the lab's data.
- **The groups and the weights**: CA-001-01's, unchanged, so that the two halves are measured alike.
  On the first session of each month, within each group, the members trading and with a price at the
  window's start are ranked by their return from the window's start to `skip` sessions before the
  session before the target; the bottom third of each group's ranked members, rounded, one at least,
  is held. Of the N funds trading, a group of n ranked members holds n/N of the portfolio, split
  equally among its cheapest; a fund trading but not yet ranked is held at 1/N, its benchmark
  weight.
- **What the groups are**: the study has no sector class, and the sector group carries 11 of the 19
  funds: it is a test of the claim's reach, the study's measure applied where it did not look. The
  equity-markets group is three overlapping US baskets, large, growth and small, and two foreign
  ones, not the study's set of countries. The commodity group is three funds, one of them a basket.
- **Bonds and bitcoin**: left out, as in CA-001-01; SHY, IEF and TLT are one country's maturities,
  not a set of countries' bonds, and the two exchange rates of the franc are not a group.
- **The start**: a fund is ranked after five years of prices, so that the base's first targets are
  on 2010-02-01, the three-year variant's on 2008-02-01. The in-sample period is five years shorter
  than CA-001-01's, and gate 5's blocks from the first holding are three — 2010–14, 2015–19, 2020–22
  — of which it needs three positive: all of them. The card names this as a handicap of the window,
  not a reason to shorten it.
- **The memory**: the signal reads 1,260 sessions back from the session before a target, so the card
  declares it. The battery's placebos then keep that distance past their circular wrap (version 3):
  a cheapness rule's placebos, shifted within it, would hold weights that read the day they are paid
  on, which counts against them and would make gate 3 too easy.

The pace was counted before the card, on the signal alone, no return read: 155 monthly targets and
70 clustered decisions for the base, 108 for the three-year variant, 74 with the year skipped.

Three variants: the sources give the anchor of five years, the short end of three, and the form that
skips the momentum year.

## What the battery judges, and what to expect

**The size predicted**, group by group, from the sources' long record. The study's long-short
premium between the cheapest and dearest thirds was about 5.8% a year in commodities and about 3.5%
in stock selection; the price-only form keeps about four fifths of book to price's Sharpe ratio on
US stocks (0.27 against 0.34), and a long-only tilt keeps 40 to 50% of a long-short premium (Israel
and Moskowitz). With the groups' shares of the portfolio: commodities, 3/19 of 5.8% × 0.45, about
0.4% a year; sectors, 11/19 of 3.5% × 0.8 × 0.45, about 0.7%; equity markets, 5/19 of the same,
about 0.35%: about 1.5% a year over the funds held in equal parts if the lab's years kept the long
record, about 0.7% if they kept half. At CA-001-01's tracking error on the same groups, about 6% a
year (its alpha of 0.20% at an appraisal ratio of 0.033), an appraisal ratio of about 0.12 to 0.25.
Costs are small, a slow ranking changing a few holdings in a month out of two: about 0.1% a year.

**The decade.** The long record is not the lab's. From 2010 to 2022, value lost in several asset
classes and US value had the worst drawdown of its history; the leaders rose further for years —
technology among the sectors, the US among the equity markets. The card predicts the long record's
premium, and names the decade as the likely reason for a shortfall: a refutation would say that
value by price within these groups earned nothing from 2010 to 2022, not that it never does.

**The clause.** Judged on the base, by its alpha over the same funds held in equal parts, as gate 2
measures it, and by the share of its placebos, shifted in time, that it beats at the lab's costs.
The theory is refuted in this form if the alpha is zero or less and the base beats half of its
placebos or fewer: the cheapest members of the groups would then have earned no more than the
groups, as the bank's first refutation reads for these asset classes. Any other result short of
passing gates 1 to 7 is not proven, not refuted.

**The test's power.** Over about thirteen years an appraisal ratio is measured to about ±0.28. With
no edge, the alpha is zero or less about half the time; at an appraisal ratio of 0.12, the low end,
about 33%; at 0.25, about 18%. The placebo condition, its placebos kept beyond the signal's memory,
overlaps the first less than it might (the two correlate at about 0.7), so that the clause refutes
less often: the logic audit's synthetic check with version 3's placebos gives about 34% with no
edge, 24% at the low end and 12% at the top. It can refute a vanished premium about one time in
three, and a real one at the low end about one time in four. Gate 4, over some twenty-seven trials
and thirteen years, needs an appraisal ratio of about 0.9, far beyond the prediction.

**Measures stated before the run**, reported, not graded:

- the two other variants, the three-year window and the year skipped;
- the value tilt's alpha in each group, a beta for each, with its standard error;
- the common structure the theory claims: the correlation of the value tilt's hedged monthly returns
  between the three groups; and the correlation of the value tilt with CA-001-01's momentum tilt
  over the same months, which the sources find negative;
- the alpha by year, and in 2020, the one deleveraging crash inside the base's window.

**Risks named before the run.**

- **The decade**, above.
- **Three blocks, all needed.** Gate 5 needs three positive blocks and the base has only three.
- **Few members.** The commodity group has three funds, SLV and DBC ranked only from 2011; the
  equity markets five: the cheapest third is one or two funds. XLRE is ranked only from late 2020,
  XLC not in-sample.
- **One fund's share.** The value tilt may hold one cheap fund for years — energy, emerging markets
  — and gate 6 refuses more than 30% of the profit in one fund.
- **The neighbours' start.** The ±25% neighbours, 945 and 1,575 sessions, set their first targets on
  2008-11-03 and 2011-05-02, the ±50% ones, 630 and 1,890, on 2007-08-01 and 2012-08-01. Gate 6
  compares their Sharpe ratios with the base's; the 1,575 and 1,890 neighbours sit in cash, earning
  the bill's rate, from the base's first holding to their own, which lowers theirs, and 1,575 faces
  the floor of half the base's.

## Choices, and the options rejected

- **Value by fundamental ratios**: the study's measure for stocks and equity indices, book to
  market, and for bonds, the real yield; the lab holds prices only.
- **The combination with momentum**: TM-040's claim, and a card of its own.
- **A short leg**: the lab is long only.
- **A shorter window**, a year or two: short-term reversal and momentum, other claims.
- **Reading the variants in 2008 and 2009**: every variant is judged from the base's first holding,
  so the three-year variant's first two years count in no gate.

## Implementation

Long only, nineteen funds, each with a European (UCITS) fund that tracks it, monthly targets filled
at the close of the session on which they are set; gate 6 adds a day's delay.
