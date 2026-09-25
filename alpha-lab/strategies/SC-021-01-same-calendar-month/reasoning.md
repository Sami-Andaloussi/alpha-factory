# SC-021-01 — Same-calendar-month seasonality across stocks: reasoning, not testable

## The theory, and the form its sources give it

SC-021 holds that seasonality lives in the cross-section of individual stocks: a stock that did well
in a given calendar month in past years tends to beat other stocks again in that month, year after
year, and one that did badly tends to lag again, over many annual lags, apart from momentum and
long-term reversal. Its mechanisms: recurring cycles of demand, a stable investor base with calendar
routines, seasonal exposure to risk factors, recurring calendars of information, trade, taxes or
constraints. Its refutations: no relation between a stock's past returns in a calendar month and its
relative return in that month later; a relation fully accounted for by momentum and reversal; one
that holds at a one-year lag but vanishes at longer ones; one that disappears once industry is
controlled for, which would make it "an industry pattern rather than a property of individual
stocks".

**Its sources, as the lab read them in the library's books.**

- **Heston and Sadka's international study**, dated 2007 in the books (the bank names its 2010
  version), as Dzhabarov and Ziemba report it in the same text in the Zacks *Handbook of Equity
  Market Anomalies* (2011, chapter 9, section "Same Month Next Year") and in Ziemba's *Calendar
  Anomalies and Arbitrage* (2012, §1.4.1): on the stocks of twelve European countries, Canada and
  Japan from 1985 to 2006, cross-sectional regressions of monthly returns find a positive relation
  at a one-year lag with a reversal in the months between, and at every twelfth month up to 120, not
  all significant at the longer lags; decile spreads sorted on it; neither liquidity nor country
  explains it; the countries' seasonal returns are correlated in the short run, and over longer
  horizons still positively but "notably weaker and sometimes statistically insignificant", which
  the authors read as seasonal risks specific to countries, or seasonal news, and a reason to
  diversify across them.
- **Heston and Sadka's US study**, which the bank names first: Chan (*Quantitative Trading*, 2008,
  chapter 7) gives its rule — each month, buy the stocks that did best in that month a year earlier
  and short those that did worst — and reports more than 13% a year before costs before 2002, an
  effect he found "has disappeared since then" on S&P 500 stocks, with survivorship bias; Ilmanen
  (*Investing Amid Low Expected Returns*, 2022, box 5.2): the pattern reported for individual
  stocks, found "even stronger in systematic factors" and documented in other asset classes by
  Keloharju, Linnainmaa and Nyberg, its explanation by earnings announcements, dividends or risk
  tolerance debated, and calendar strategies often too costly to implement; Campbell (*Financial
  Decisions and Markets*) cites it beside Keloharju and others.
- **Ilmanen** (*Expected Returns*, 2011, box 14.1 and §25.3): a periodicity of past monthly returns
  at quarterly and yearly cycles, the return twelve months ago the strongest link to the current
  month's, with comparable ones at 6, 9, 24, 36, 48 and 60 months, which he reports not
  concentrated in the months of earnings announcements.

## Why the lab cannot test it

The claim ranks individual stocks against each other, and the lab's data holds none: the snapshot
and its addition hold daily prices of twenty-two funds and bitcoin, the bill rate and two exchange
rates of the Swiss franc. Each refutation the bank names reads a stock against other stocks — its
own past month, its momentum, its lags, its industry.

**What was considered, and why it does not rescue the test:**

- **The eleven sector funds ranked on their own past returns in the same calendar month.** A result
  on them could neither support SC-021 nor refute it: a recurrence among sector funds is what the
  theory's own fourth refutation calls an industry pattern, set apart from its claim, and a
  recurrence of stocks net of their industry, the claim, cannot be seen in funds that hold whole
  industries. The lab has read single-stock claims on sector funds before, as a coarse unit
  (SC-006-01's year-end winners) — but those claims did not set the industry form apart; this one
  does. No theory of the bank claims an industry form of the recurrence: SC-022 names sectors, as an
  explanation that needs disclosure dates; SC-023 claims it for other asset classes and
  international indices, and would reach industries only by extension.
- **The lab's assets across classes ranked on their own same-month history**, the sector funds among
  equity indices, commodities, gold, bonds and bitcoin: the claim that relative returns recur by
  calendar month in other asset classes and indices is **SC-023**'s, Keloharju, Linnainmaa and
  Nyberg's, which the lab will read as a theory of its own and to which SC-013-01 already left a
  recurrence at the same week of the month. It is left to SC-023, with Heston and Sadka's lags,
  their countries' weakening correlation over long horizons and Chan's post-2002 finding as
  sources for its card.
- **The market's own same-month pattern**, the whole index stronger in some calendar months: the
  month-of-the-year effect, **SC-017**'s, which SC-017-01 read on the five equity funds; SC-021's
  claim is relative, not the market's level.
- **The information calendar**, earnings announced in the same months each year: **SC-022**'s
  explanation of this effect, which needs announcement dates and single stocks too; Ilmanen (2022)
  calls it debated.

What would make it testable: a stock universe, which the lab's framing provides for "used only by
theories that need one, with its survivorship bias stated", with monthly history from about 1995, so
that lags of up to ten years are available from 2005 — a new snapshot, and a decision for the lab's
framing, not for a card. Chan's finding would make its first question whether the effect outlived
2002.

## Status

SC-021 is recorded `not-testable`: its claim ranks individual stocks against each other, and the
lab holds no single stocks; ranked on the sector funds, the recurrence becomes the industry pattern
the theory's own refutation sets apart, which a result could neither support nor refute; ranked
across the lab's asset classes, it is SC-023's claim, and is left to it. No card is drawn, and no
trial is spent.
