# SC-023-01 — The assets that beat their beta in a calendar month in past years: reasoning

## Why this theory now

SC-023, return seasonalities, generalises the same-calendar-month recurrence of stocks (SC-021) to a
calendar signature at several frequencies — the same calendar month, the same weekday — in other
asset classes and international indices as well as stocks, often offset by seasonal reversals
outside the matching period; risk, mispricing and flows compete to explain it. Its refutations: no
predictive power of past same-season returns for relative returns in the same season, monthly or
weekday; seasonalities fully explained by momentum or other known factors; for the risk reading,
seasonal gains fully offset by reversals elsewhere in the year, and for the mispricing reading,
seasonal returns matching seasonal variations in exposure to risk.

Three of the lab's `not-testable` judgements left this theory a form: SC-021-01, the same-month
recurrence read across the lab's asset classes rather than across stocks, with Heston and Sadka's
lags; SC-013-01, a recurrence at the same week of the month; SC-022-01, the sector funds' own
recurrence. This card draws the first; the others are answered below, and this card is SC-023's
only form.

**The sources, as the lab read them in the library's books.** Keloharju, Linnainmaa and Nyberg's
papers are in the library only as others report them.

- **Keloharju, Linnainmaa and Nyberg (2016)**: Ilmanen (*Investing Amid Low Expected Returns*, 2022,
  box 5.2) reports them finding the same-month recurrence "even stronger in systematic factors" than
  in stocks and documenting it in other asset classes, its explanation debated and calendar
  strategies often too costly to implement; Gray and Vogel (*Quantitative Momentum*, 2016) report
  seasonalities that "exist in almost every asset class, are remarkably persistent over time, and
  are extremely large", after warning, with Novy-Marx and with Zhang and Jacobsen's three centuries
  of UK data, that seasonal claims call for scepticism, and they report Sias's finding that momentum
  is itself seasonal. The library does not say whether the other asset classes were read each
  within itself or across classes: the ranking across the lab's classes is this card's
  construction.
- **Heston and Sadka**, as Dzhabarov and Ziemba report their international study in the Zacks
  *Handbook of Equity Market Anomalies* (2011, chapter 9) and Ziemba's *Calendar Anomalies and
  Arbitrage* (2012, §1.4.1): on the stocks of twelve European countries, Canada and Japan from 1985
  to 2006, a positive relation at a one-year lag, a reversal in the months between, and a positive
  relation at every twelfth month up to 120, not all significant at the longer lags, used in decile
  spreads; the countries' seasonal returns correlated in the short run and less over long horizons.
  Ilmanen (*Expected Returns*, 2011, box 14.1) on stocks: the return twelve months ago the strongest
  link to the current month's, with comparable ones at 24, 36, 48 and 60 months (and at 6 and 9).
  Chan (*Quantitative Trading*, 2008, chapter 7) reports Heston and Sadka's US rule — each month
  long the decile of stocks that did best in that month a year earlier, short the worst — at more
  than 13% a year before costs before 2002, and finds it losing after, −0.92% a year with a Sharpe
  ratio of −0.11 on S&P 500 stocks, "even worse" over his last five years; he finds equity seasonals
  weakened and those of commodity futures "alive and well".
- **Seasonals across asset classes with a sign**: Ilmanen (2011, §25.1 and figure 25.3) finds
  equities and risky assets strong in December and January and weak in September and October, and
  government bonds, and oil in January, the other way; in §25.3, seasonal supply and demand in
  commodities "often already in the price" of futures. These are the market's and the classes'
  calendars, the month of the year across classes, SC-017's kind of claim, not an asset's own
  signature beyond its exposure; this card removes them (below).
- **Cryptocurrencies**: Kaiser (2018), *Seasonality in Cryptocurrencies*, in the library, finds no
  consistent calendar effects in the returns of ten coins; Long, Sun, Wu and Zhang (2020), on 151
  coins' weekdays, named by the bank, are not in the library.

**What the lab already knows, and is not blind to.** SC-017-01 published the five equity funds'
average by calendar month, from −0.41% to +2.41% a month in its extremes, and their ranking;
SC-018-01 each fund's winter less its summer; SC-019-01 each fund's count of positive Januarys and
the US funds' January return by year; SC-002-01 IWM less SPY over January. These describe the
market's and the funds' calendars, which the card's signal removes through each asset's beta; no
verdict ranks the lab's assets on their own past returns in a calendar month, beyond their beta or
otherwise.

**The bank's neighbours.** **SC-021**, the same recurrence across stocks, and **SC-022**, its
information-cycle explanation, both `not-testable`; **SC-017**, the month of the year, the market's
level; the momentum theories of the TM family, which the second refutation names.

## From the claim to a signal

- **The market**: the lab's assets across its classes — the eleven sector funds, the five equity
  funds, gold, silver, the commodity basket, and the two Treasury funds of longer duration, IEF and
  TLT: twenty-one, each entering the ranking once it has the history the signal reads. From
  February 2010 to December 2022, 17 to 20 are ranked each month: SLV from May 2011, DBC from March
  2011, XLRE from October 2021, XLC never in-sample. Bitcoin is left out: the monthly recurrence is
  reported for stocks, factors and other asset classes, not for cryptocurrencies, where the
  library's one study finds no consistent calendar effect; its volatility, several times any fund's,
  would dominate a ranking; and its prices, from September 2014, would rank it only from late 2019.
  SHY is left out as near cash, a fund whose monthly standard deviation is a twentieth of silver's,
  which a ranking would pick only when the risky assets' months were bad, timing the market's
  calendar.
- **The asset's own calendar, beyond its exposure.** Across classes, a raw ranking on past
  same-month returns picks high-beta funds in the months the market rose in past years and the
  Treasury funds in the others: its gap over the average would carry the market's month-of-year
  pattern, SC-017's claim, which SC-017-01 has published on these funds, and the third refutation's
  "seasonal variations in exposure to risk". So each asset's monthly return is taken beyond its beta
  to the average: its return less its beta times the equal-weighted return of the universe's assets
  that month, the beta estimated before the month on the asset's monthly returns over the `years`
  years before it, all months together, the month in progress left out since its return ends at the
  target's own close, and applied to every month of that window; returns, betas and residuals are
  raw, not less the bill, which would otherwise leave in the gap the bill times the difference of
  the two groups' betas. The signal is the mean of those residual returns in the same calendar month
  m over the previous `years` years — lags of 12, 24, … months, Heston and Sadka's and Ilmanen's
  annual lags. An asset is ranked for month m once it has all `years` of them and trades. The raw
  ranking is reported.
- **The rule**: over each calendar month, hold in equal parts the `top` assets with the highest
  signal among those ranked, the long side of Heston and Sadka's decile spread (about a tenth of
  seventeen to twenty); the target is set at the close of the last session before the month, read
  from the calendar of scheduled sessions, from closes up to the session before, and holds for the
  month. Long only: the short side is reported, not traded.
- **Parameters for gate 6**: `years`, 5 for the base, the annual lags to 60 months Ilmanen lists,
  with neighbours 4 and 6, 2 and 8; `top`, 2, with 1 and 3 at both steps, the runbook's rule for a
  small count. No variant. The neighbours at 6 and 8 years first rank in February 2011 and 2013, and
  sit in cash for 12 and 36 months of the period gate 6 judges them on, which lowers their Sharpe
  ratios by construction.
- **Memory**: 1,290 sessions, above the base's five years and a month; the runbook asks it of the
  variants, not of the neighbours.
- **The first target**: the prices begin in January 2005, which has no close before it, so its
  return is unknown; February 2010 is the first month with five known returns in the same month
  before it and fifty-nine known months for the beta, January 2010 lacking January 2005's. The first
  target falls at the end of January 2010, and the in-sample months held run from February 2010 to
  December 2022, 155 months.

## What the battery judges, and what to expect

**The size predicted — a judgment, from the sources.** No source in the library gives the
recurrence's size across asset classes, and none beyond exposure: Keloharju and others' "extremely
large", as Gray and Vogel report it, comes without a figure; Chan reports about 1.1% a month long
short on single stocks before 2002, whose long side against the average this card takes, by its own
assumption, as about half, and a loss after 2002. The lab's funds are far less dispersed than single
stocks, and their residuals less still, so the card judges the top group's monthly residual return
at about 0 to +0.25% above the average residual of the ranked assets from 2010 to 2022. The rule's
alpha over the benchmark, the universe held in equal parts, is then about 0 to +3% a year before
costs of about 1.0 to 1.2% a year (most months replacing most of its two holdings, at 5 basis points
a side); at a dispersion of about 3% a month for the residuals the ranking picks, a tracking error
of about 10% a year and an appraisal ratio of about −0.12 to +0.18 after costs. The card expects the
base to fail gate 2 or gate 3; gate 4, which asks an appraisal ratio near 0.65 after 48 effective
trials, above the predicted range; gate 5, whose 2005–07 and 2008–09 blocks hold nothing and count
as not positive, so that all three later blocks must be; and gate 3's placebos, some of whose shifts
of about a whole number of years hold the same calendar month's targets from other years, a
same-month signal at longer lags that caps the rank the rule can reach near 90% if the effect is
real and stable. Two assets at a time, the ranking may return to a few volatile ones and fail gate 6
on one asset's share.

**The clause.** Judged before costs, over the in-sample calendar months from February 2010 to
December 2022: each month's return of each ranked asset, compounded from the daily returns of the
market's sessions in it, less its beta, estimated before the month as in the signal, times the
equal-weighted return of the universe's assets that month; the equal-weighted residual of the `top`
assets the base ranks highest for the month, less the equal-weighted residual of all the assets it
ranks; the mean of that difference over the months, its standard error, the standard deviation of
the monthly differences over the square root of their number, and its t statistic, computed apart
from the battery, on raw returns. The theory is refuted in this form if that t statistic is −0.35 or
below. Above it, short of passing gates 1 to 7, it is not proven, not refuted; a base that passes
gates 1 to 7 while the clause refutes leaves the theory refuted in this form.

The top two against the average grade the sources' own measure, the decile spread's long side that
the rule trades; the rank correlation over the whole cross-section, which uses every asset and
weighs volatile ones less, is reported beside it. Of SC-023's refutation criteria, the first is
graded at the monthly frequency on the asset's own calendar; the weekday frequency is out of reach
(below); the second is reported through momentum's ranking; the third through the top group's
returns in the months that do not match and its beta in the matching month against the others.

**The test's power.** A random pair's residual less the average residual has a standard deviation of
about 2.4% a month over 2010–2022; the ranking, favouring assets whose residuals move most, may
raise it to about 3%. Over 155 months the standard error of the difference is then about 0.2 to
0.25% a month. The clause refutes about 36% of the time with no effect, about 5 to 9% at +0.25% a
month, the top of the range. It cannot tell an effect of the predicted size from none.

**Measures stated before the run**, reported, not graded:

- the raw ranking: the same gap with the assets ranked on their raw past same-month returns and
  graded on raw returns — the classes' and the market's calendar, SC-017's kind, included;
- each month's rank correlation between the signal and the month's residual returns across the
  ranked assets, its mean and t statistic, and the same for the raw ranking;
- the short side: the `top` assets ranked lowest, less the average;
- the one-year lag alone: the same gap with the signal read on the last year only;
- the signal less the asset's own mean residual over all months of the same years, a seasonal
  without the asset's level;
- momentum: the same gap with the assets ranked on their residual return over the twelve months
  before the month, and the rank correlation of that ranking with the signal;
- reversals outside the matching period: for each month's top group, its average residual over the
  other eleven months of the same year, less the ranked assets' average over them; and its beta to
  the average in the matching month against its beta in the other months;
- the rule's average weights held fixed over the period, against the rule;
- within the sector funds alone and across the other assets alone;
- over 2010–2016 and 2017–2022, and without 2020;
- how often each asset was held, the months a Treasury fund was, and each asset's share of the
  profit;
- the base's alpha before and after costs; the neighbours' and the one-day-late rule's alphas and
  appraisal ratios.

**Risks named before the run.**

- **Beta estimated on five years**: an asset whose beta moved within them leaves part of its
  exposure in the residual.
- **Costs**: about 1.0 to 1.2% a year, against a predicted gap of at most 3% a year before them.
- **Two assets at a time**: the rule's return depends on few holdings; gate 6's clusters and its
  share of the profit may catch it.

## Choices, and the options rejected

- **The raw ranking as the base**: across classes it grades the market's and the classes' calendars
  through their betas, SC-017's claim and the third refutation's alternative; it is reported.
- **The rank correlation as the graded measure**: more power over the whole cross-section, but not
  the sources' decile spread nor what the rule trades; it is reported.
- **The weekday frequency**, the same weekday's past returns: a rule that changes its holdings each
  day meets gate 6's day of delay, which moves it onto the next weekday's ranking — a failure built
  in, on which the lab does not spend a trial (the runbook's step 9) — and would pay about 2 × 5
  basis points a day, a quarter of its capital a year.
- **A recurrence at the same week of the month**, which SC-013-01 left here: no source in the
  library measures it, and SC-013-01 could give it only a sign carried by analogy.
- **The sector funds alone**: no source signs an industry form (SC-021-01, SC-022-01); the sector
  funds are ranked among the other assets, and reported apart.
- **Bitcoin and SHY**: left out, as above.
- **Ranking on returns scaled by volatility**: no source in the library reads the recurrence so.
- **Longer lags, to ten years**: the lab's data from 2005 would leave four in-sample years.

## Implementation

Long only, two of the lab's funds at a time, each with a European (UCITS) fund that tracks it;
twelve rebalances a year, on dates known ahead. The targets are filled at the close of the session
on which they are set; gate 6 adds a day's delay, which holds the month from its first session's
close.
