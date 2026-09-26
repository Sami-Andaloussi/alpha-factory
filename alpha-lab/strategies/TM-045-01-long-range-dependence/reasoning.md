# TM-045-01 — Long-range dependence: reasoning, not testable as a theory of its own

## The theory, and the forms its sources give it

TM-045 holds that returns carry a long memory, measured by the Hurst exponent H: above 0.5, past
returns predict future ones of the same sign even at very long horizons, "persistent trends at every
horizon", attributed to secular cycles, technological change and demography; at 0.5, a random walk;
below, anti-persistence. Its prediction is a debate: Peters (1994) finds H significantly above 0.5
for many indices with the classical rescaled-range (R/S) method; Lo (1991) shows that method biased
by short-range dependence and, with a modified statistic that allows for it, finds no long-range
dependence in US stock indices. Its refutations: Hurst exponents that fall to 0.5 once short-term
dependence is accounted for, as with the modified R/S statistic on US stock indices; persistence
that disappears at long horizons, or is explained entirely by short-term autocorrelation. The bank
names equity indices, months and years, and daily prices.

**Its sources, as the lab read them in the library.** The library holds Lo's test and its results,
not Peters' books; Peters is read through others.

- **Lo** (*A Non-Random Walk Down Wall Street*, 1999, chapter 6, his 1991 paper): the classical R/S
  statistic cannot tell long-range from short-range dependence — where a portfolio's first-order
  autocorrelation is as large as 0.5, as for some, its mean is biased upward by 73%, enough to
  reject at any conventional level; the modified statistic divides the range by a standard deviation
  that allows for autocorrelation up to a lag q. On the CRSP indexes a 5% test accepts inside
  [0.809, 1.862] (table 6.2). Daily, July 1962 to December 1987, 6,409 sessions (table 6.3): the
  equal-weighted index's classical statistic 2.63, significant, its modified statistic 1.45 to 1.50
  for q of 90 to 360 days, not significant; the value-weighted index's classical 1.55, not
  significant over the whole sample (1.97, significant, in its first half), its modified 1.26 to
  1.33; no modified statistic of either index significant in any half or quarter. Monthly, January
  1926 to December 1987, 744 months, q of 3 to 12 months (table 6.4): no modified statistic
  significant for either index in any period or sub-period. Annual, 1872 to 1986, 115 years: neither
  statistic significant. His conclusion: "little support for long-term memory in U.S. stock
  returns"; with Kandel and Stambaugh, the long-run predictability of Fama and French (1988) and
  Poterba and Summers (1988) may be short-range dependence rather than long-range, though he also
  shows that an anti-persistent long-memory component could produce Poterba and Summers' variance
  ratios below one at 96 weeks and more. His Monte Carlo (table 6.6a), against a fractionally
  differenced alternative with d of 1/3: little power at 100 observations; at q of 5, 33.5% at 250,
  62.8% at 500 and 84.6% at 1,000; at 1,000, 32.2% at q of 25 and 5.2% at q of 50 — the power falls
  steeply as the lags allowed for lengthen.
- **Campbell, Lo and MacKinlay** (*The Econometrics of Financial Markets*, 1997, section 2.6):
  long-range dependence is detected by the classical statistic, but its sensitivity to short-range
  dependence means that a rejection "need not come from long-range dependence"; what the earlier
  literature took for long-range dependence in US stock returns may be "quickly decaying short-range
  dependence instead".
- **Bacon** (*Practical Portfolio Performance Measurement and Attribution*, third edition, 2023,
  "Hurst index"), after Clarkson (2001) and Qian and Rasheed (2004): the Hurst index as the slope of
  log(R/S) on log(n), the classical statistic in its regression form, the intercept assumed zero;
  "equity markets have a Hurst index of around 0.7", the Nile's floods 0.9 — no index, period,
  horizon or rule.
- **Tvede** (*Business Cycles*, chapters 16 and 25): Hurst's H, 0.5 for a random series; Peters
  (1994), applying R/S to gold from January 1968 to December 1992, found "modest signs" of two gold
  cycles, of about 48 and 248 weeks, and Tweedie (1994) suggested that a long-term dependence may
  exist in gold prices, with cycles of about 80 to 100 days and 240 weeks — cycle lengths, with no
  direction or phase.
- **Aronson** (*Evidence-Based Technical Analysis*, 2007): Peters and Lo and MacKinlay found
  financial series not to behave as random walks, citing Peters' two books (1991, 1994) — a report
  of non-randomness, with no exponent, index or horizon. **Zaremba** (*The Financialization of
  Commodity Markets*, 2015) lists Peters (1994) among books on trading systems.
- **Dacorogna, Gençay, Müller, Olsen and Pictet** (*An Introduction to High-Frequency Finance*,
  2001, table 5.8 and section 7.3.2): drift exponents of four exchange rates against the dollar and
  of gold, 1987 to 1995, about 0.57 with mean absolute returns and about 0.48 to 0.51 with squared
  ones; they reject Peters' reading of an exponent above 0.5 as fractional noise in returns, which
  show no significant autocorrelation, and find it in volatility, H about 0.86 to 0.87 for USD-DEM.
- **Chan** (*Algorithmic Trading*, 2013): the Hurst exponent as a test of stationarity and, in
  chapter 6, of trending; USD.CAD's H 0.49; the two-year Treasury note future's H 0.44, its variance
  ratio not rejecting the random walk, while the correlations of its past returns with its future
  ones are positive for most pairs of lookback and holding period (table 6.1: +0.17 to +0.26 for 60
  days back and 10 to 25 forward) — momentum and reversion "at different time frames", which one
  exponent does not see. **Halls-Moore** (*Successful Algorithmic Trading*): Amazon's H about 0.45,
  "close to 0.5".
- **Tsay** (*Analysis of Financial Time Series*, third edition, section 2.11) and **Bouchaud,
  Bonart, Donier and Gould** (*Trades, Quotes and Prices*, 2018, chapter 2): the long memory in the
  data is in the absolute returns and the volatility — the CRSP indexes' daily absolute returns
  autocorrelated beyond 300 lags, 1970 to 2008 — while the returns themselves are nearly
  uncorrelated, the volatility signature plots of liquid assets almost flat from seconds to a few
  months.
- **Bitcoin**: the library gives no Hurst exponent or long-memory sign for it; the crypto books cite
  such studies (Urquhart; Nadarajah and Chu; Bariviera) by title only.

## What the lab can read of it, and where each form already stands

The lab holds the daily closes of funds from 2005, the in-sample years 2005 to 2022, eighteen of
them, and no currency fund. On those data:

- **H above 0.5 on the returns of equity indices**: the library's one test that allows for
  short-range dependence, Lo's, finds none on either CRSP index at daily, monthly or annual
  frequency. The figures above 0.5 are the classical statistic's — Lo's equal-weighted daily 2.63,
  Bacon's "around 0.7" from the regression form, which Lo, after Davies and Harte, finds biased
  toward rejection — and Peters', reported by others without a figure for an equity index. The lab
  could compute an exponent or the modified statistic on its funds, whose short-range
  autocorrelation is near zero (TM-041-01's weekly slopes), so the bias Lo corrects would matter
  less here than on the equal-weighted index; but a statistic of long memory gives no horizon at
  which to hold or leave a fund, and no source in the library turns it into a rule. On the months of
  eighteen years, at most 216, the modified test's power against d of 1/3 lies below Lo's 33.5% at
  250 even at q of 5, and falls further with the lags; on the funds' 4,500 or so sessions it is
  higher at short lags only, Lo's simulations stopping at 1,000 observations and 50 lags.
- **Persistence at months**: the sign of past returns over 1 to 12 months predicting the next is
  **TM-017**'s, read by TM-017-01 at six and twelve months and by TM-017-02 at one; the pooled
  one-month slope +0.045, not refuted, not proven, positive in the Treasuries and the commodity
  basket, flat in the equity markets. Long memory adds no lookback of its own: "every horizon" names
  none.
- **Persistence at years**: the library's direct test at years, Lo's annual one over 115 years, is
  null, and the library's sign at three to five years is the opposite, reversal — Poterba and
  Summers' transitory component of index prices, Fama and French (1988), De Bondt and Thaler — which
  is **MR-021**'s, untouched; Lo, after Kandel and Stambaugh, holds that even that reversal may be
  short-range dependence rather than long. The time-series form, an equity index fund's return over
  years on its own past years, is one regression for both theories: MR-021 predicts it negative,
  TM-045 positive. It is left to MR-021's card, which reads TM-045's positive sign as its rival and
  reports it, rather than drawn here, which would spend a second trial on the same regression; a
  one-sided clause of MR-021 refutes MR-021 at a small positive t and does not prove TM-045.
  **CA-024-01** published a relative form on the lab's funds: the cheapest third of each group by
  its past five years earned 0.63% a year less than its group from 2010 to 2022, a continuation, not
  a reversal, and not significant; it is a return within groups, not a fund's own series.
- **Persistence explained by short-term autocorrelation**: the short-term autocorrelation of the
  lab's funds is published — TM-041-01's weekly slopes of the fourteen US equity funds, near zero,
  eleven of fourteen slightly negative; TM-017-02's monthly slopes of six funds — and it is
  **TM-043**'s claim, recorded not testable, and TM-017's.
- **Cycles of about 48 and 248 weeks in gold** (Peters, Tweedie): cycle lengths with no direction or
  phase, on one asset outside the bank's equity indices; the lab refuses a universe of fewer than
  four funds, and a cycle's timing would have to be set from the lab's own prices.
- **The long memory of volatility**, which the library documents (Tsay, Bouchaud, Dacorogna): not
  TM-045's claim, which is about the sign of returns; volatility persistence is what a
  volatility-scaled or volatility-managed rule reads, **TM-047**'s, read by TM-047-01 and TM-047-02.
  The long memory of order flow (Bouchaud, chapter 10; Hens and Schenk-Hoppé, *Handbook of Financial
  Markets*, chapter 2) is **FP-003**'s. Kaufman's fractal efficiency and fractal dimension measure
  noise and give no long-memory sign.

**The bank's siblings.** **TM-017**, time-series momentum, in progress, at one to twelve months;
**MR-021**, long-term reversal, untouched, at twelve to sixty months; **TM-043**, positive return
autocorrelation, recorded not testable; **TM-047**, volatility scaling, tested inconclusive;
**FP-003**, metaorders and order splitting, untouched.

**What was considered, and why it does not rescue a card of TM-045's own:**

- **A modified R/S test on the funds' daily returns as the clause, a trend rule as the strategy**:
  the statistic tests for long memory, not its sign at a horizon a rule could trade; its only test
  in the library that allows for short-range dependence finds none; and any trend rule on the funds
  is TM-017's at months or MR-021's rival at years.
- **A Hurst exponent estimated on the funds, holding a fund while it is above 0.5**: Bacon's "around
  0.7" is a level for equity markets, not a threshold or a lookback; Chan's and Halls-Moore's
  exponents are near or below 0.5; the library gives no rule, and the exponent of a series is not
  the modified test Lo corrects.
- **Persistence at years, graded here with TM-045's positive sign**: the same regression as
  MR-021's, one trial for both, drawn under MR-021, whose sources give the sign.
- **Gold's cycles**: no direction, one asset, and a phase that only the lab's prices could set.
- **Commodities or currencies**, where the older R/S literature applied the classical statistic
  (Booth and Kaen on gold, Booth, Kaen and Koveos on exchange rates, cited by Lo): the bank names
  equity indices, the lab holds no currency, and Dacorogna's exponents above 0.5 are read by their
  own authors as no memory in returns.

What would make it testable as its own: a source in the library that gives, for
capitalisation-weighted indices and after short-range dependence is allowed for, a Hurst exponent
above 0.5 together with a horizon or a rule that is neither TM-017's months nor MR-021's years —
Peters' own books, ingested, if they give one.

## Status

TM-045 is recorded `not-testable` as a theory of its own: the library's one test of long-range
dependence that allows for short-range dependence, Lo's, finds none on US stock indices at daily,
monthly or annual frequency; its figures above 0.5 for equity markets, Bacon's "around 0.7" and the
classical statistic's, give a level but no horizon or rule, and Peters' gold cycles give no
direction; its persistence at months is TM-017's, read by TM-017-01 and TM-017-02; at years the
library's sign is MR-021's reversal, whose card reads TM-045's positive sign as its rival in the
same regression; its short-term autocorrelation is TM-043's and TM-017's, published; the long memory
the library documents is in volatility, TM-047's, and in order flow, FP-003's. No card is drawn, and
no trial is spent.
