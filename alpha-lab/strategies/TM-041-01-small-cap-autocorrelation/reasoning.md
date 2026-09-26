# TM-041-01 — Small capitalisations' weekly continuation against large ones: reasoning

## Why this theory now

TM-041 is next in the trend-and-momentum family, taken in number order. It holds that momentum is
stronger for small capitalisations than for large ones: small firms are covered by fewer analysts
and traded less, their information circulates more slowly, their prices take longer to adjust, and
fewer sophisticated investors arbitrage them; by analogy, futures on small-capitalisation indices
and small commodity markets. Its prediction: return autocorrelation larger for small firms than for
large ones, Lo and MacKinlay (1990) reporting a weekly autocorrelation of about 42% for small
capitalisations against 9% for large ones, over weeks to months (the 9% is the bank's; the library's
tables give 14% for the largest quintile, and 0.044 for its own lag-one autocorrelation over 1962 to
1987, Lo and MacKinlay's table 5.4). Its refutations: momentum and return autocorrelation no larger
in small capitalisations than in large ones, or no larger among small firms with little analyst
coverage and trading. The bank names stocks, equity indices and commodities.

**Its sources.**

- **Lo and MacKinlay** (*A Non-Random Walk Down Wall Street*, 1999, chapter 2, table 2.2): weekly
  returns of equal-weighted size quintiles of NYSE-AMEX stocks, September 1962 to December 1985: the
  smallest quintile's first-order autocorrelation 42% over the whole sample and 49% from 1974, the
  largest quintile's 14%, significant — a difference of 0.28; value-weighted portfolios give the
  same, except the largest quintile, whose random walk is generally not rejected; at a four-week
  base the smallest quintile keeps 23%, and no variance ratio of the largest is significant. In
  their preface: an update of the weekly market indexes on 1986 to 1996 "conforms more closely to
  the random walk", which they tie to statistical arbitrage.
- **Campbell, Lo and MacKinlay** (*The Econometrics of Financial Markets*, 1997, section 2.8, table
  2.6): the same test from July 1962 to December 1994: the smallest quintile's two-week variance
  ratio 1.35 over the whole sample (a weekly autocorrelation of about 35%), 1.34 to 1978 and 1.37
  from October 1978 to 1994; the central quintile's 1.20, 1.21 and 1.19; the largest quintile's
  1.06, 1.11 and 1.01, its evidence against the random walk "limited only to the first half of the
  sample period". The difference between the smallest and largest quintiles is 0.29 over the whole
  sample, 0.23 in the first half and 0.36 in the second: it widened as the large stocks'
  autocorrelation vanished. The equal-weighted index rejects the random walk and the value-weighted
  one does not (table 2.5); the size-sorted portfolios' cross-autocorrelations are asymmetric, large
  stocks' returns leading small ones', and "unrealistically high probabilities of nontrading are
  required" to generate them (section 2.8, after table 2.8).
- **Foerster and Keim** (in Keim and Ziemba, *Security Market Imperfections in Worldwide Equity
  Markets*, 2000): nontrading implies a weekly autocorrelation of 0.059 for the smallest portfolio,
  against Lo and MacKinlay's 0.46; the daily autocorrelations of the smallest and largest quintiles
  declined from 1973 to 1990, which they tie to more trading of whole portfolios and to index
  futures. The stale part of the sources' autocorrelation is contested: the papers "do not agree on
  the level", though all three "conclude that nontrading cannot completely account for the observed
  autocorrelations" (Campbell, Lo and MacKinlay, chapter 3).
- **Madhavan** (*Exchange-Traded Funds and the New Dynamics of Investing*, 2016, chapter 3): the net
  asset value of a high-yield bond fund, HYG, had a daily autocorrelation of 0.33 in 2014 from stale
  bond prices, while the fund's own price returns showed essentially none; in his model staleness
  gives the value a positive autocorrelation, and liquidity shocks give the fund's price a negative
  one. A bond fund, where stale prices are far more common than among stocks.
- **Hong, Lim and Stein** (2000), as Barberis and Thaler report them (Thaler, *Advances in
  Behavioral Finance, Volume II*, 2005): momentum stronger among small firms and among firms with
  low analyst coverage, a slow diffusion of information; Jegadeesh and Titman (2001) finding small
  stocks' momentum larger than large stocks' (Zacks, *The Handbook of Equity Market Anomalies*,
  2011). Against them, **Bali, Engle and Murray** (*Empirical Asset Pricing*, 2016, chapter 11,
  table 11.5): sorted first on size, the medium-term momentum of stocks "does not exist at all for
  small stocks" in equal-weighted portfolios, and the one-month reversal is strong in small stocks
  and weak in large ones (chapter 12). These are cross-sections of single stocks, long and short.

**The form this card tests.** The size contrast in its time-series form, on the two funds of the lab
that hold the US market by size: IWM, the Russell 2000's small capitalisations, and SPY, the S&P
500's large ones. The claim: IWM's weekly return is more strongly continued the next week than SPY's
— its first-order weekly autocorrelation larger. The sources' portfolios were built from the last
trades of their stocks, and a stock that did not trade late in the week shows a stale price the next
week corrects: nonsynchronous trading makes a portfolio's returns autocorrelated with no slow
diffusion of information (**LL-004**'s claim). A fund's price is its own market's; Madhavan's case
shows a fund's price free of the staleness of its holdings' values, on bonds, and after 2005 the
stocks of the Russell 2000 trade nearly every day. The contrast on the funds therefore reads mostly
the part of the size effect that stale prices do not make, the part TM-041's mechanism claims. The
Russell 2000, weighted by capitalisation, sits in the card's judgment nearer the sources' central
quintile than their smallest, and SPY near their largest, value-weighted, whose random walk was not
rejected: the sources' central-against-largest difference is 0.14 over 1962 to 1994 and 0.18 from
1978.

## From the claim to a signal

- **The blocks**: the sessions are cut into consecutive blocks of `period` sessions, counted from
  the session of 2005-01-03, the snapshot's first; a block's return is from the close of its first
  session to the close of the next block's first session. Blocks of 5 sessions are about a trading
  week; each holiday moves the weekday on which they start.
- **The universe**: the fourteen US equity funds, SPY, QQQ, IWM and the eleven sector funds — all of
  large capitalisations but IWM. The lab refuses a universe of fewer than four funds, whose gate 6
  would fail by construction.
- **The rule**: on the first session of each block, each fund trading holds 1/N of the portfolio, N
  the funds trading, when its own return over the last `period` sessions to the session before beats
  the bill's over the same sessions; its share is in cash otherwise, and while it has fewer than
  `period` + 1 closes (XLRE and XLC, in their first blocks). Everything is read up to the session
  before; targets are traded at the close.
- **The variant**: `period` 20, Lo and MacKinlay's four-week base.
- **Parameters**: `period`, 5; neighbours 4 and 6, 3 and 8.
- **Memory**: 21 sessions, the variant's 20 returns and the close before them.

**What the rule is, and what a pass would mean.** The rule is the plainest trade on each fund's own
weekly continuation, thirteen of its fourteen funds large: it trades **TM-043**'s claim, the
continuation of index returns over weeks, more than TM-041's. Its gates therefore judge weekly
continuation, and a pass of gates 1 to 7 proves TM-041 only with the clause's t statistic at +1.65
or above; otherwise a pass is read for TM-043, not for size.

## What the battery judges, and what to expect

**The size predicted — a judgment.** The sources' central-against-largest difference, 0.14 to 0.18,
is the nearest to IWM against SPY; a part of it was stale prices, which a fund's price carries
little of; Foerster and Keim find the quintiles' daily autocorrelations declining to 1990, and Lo's
*Adaptive Markets* (2017, figure 8.8) the US indices' daily autocorrelation turning negative after
2008. Against those, Campbell, Lo and MacKinlay's second half shows the difference widening, the
      large
side vanishing first. On two funds priced continuously, from 2005, the card judges IWM's weekly
autocorrelation to exceed SPY's by about 0.02 to 0.10, and both to be near zero. The rule's alpha
over the fourteen funds held in equal parts about −2 to +1% a year: a weekly continuation near zero
leaves a weekly switch paying for its moves, MR-032-01's weekly rule having paid 3.27% a year in
costs.

**The gates.** Weekly decisions on fourteen funds: gate 1 passes on its count. The card expects the
base to fail gate 2 or 3, a timing rule on correlated funds with little continuation to read, and
gate 4; gate 5 with them, as it fails when the blend fails gate 2, 3 or 4. Gate 6's one-day delay
compares Sharpe ratios, which exposure largely makes: the card does not expect it to fail on it.

**The clause.** Judged before costs, on the market's closes, over the in-sample blocks of the base,
each block of 5 sessions from the close of its first session to the close of the next block's first
session, from the first block with a full block before it to the last block whose end falls on or
before 2022-12-30: each fund's block return less the bill's over the same sessions, stacked for SPY
and IWM, regressed by ordinary least squares on the fund's own return less the bill's over the block
before, with one constant and one slope for each fund; the standard errors clustered by block, the
two funds' returns in a block one cluster. The graded quantity is IWM's slope less SPY's; the t
statistic is computed apart from the battery. The theory is refuted in this form if it is −0.35 or
below: IWM's weekly continuation no larger than SPY's. Between, not proven, not refuted. A base that
passes gates 1 to 7 proves the theory in this form only if the clause's t statistic is +1.65 or
above; with the clause refuting, it leaves the theory refuted in this form.

**The test's power.** About 905 in-sample blocks. SC-001-01 published the daily standard errors of
SPY's, IWM's and their difference's weekday effects — 0.050%, 0.061% and 0.026% — which put the two
funds' daily correlation at about 0.91. At that correlation the standard error of the difference of
two weekly slopes over independent weeks is about √(2 × (1 − 0.91²) / 905), 0.020. The sources'
robust statistics against 1/√n widen such errors by 1.3 to 1.6 (Campbell, Lo and MacKinlay's table
2.5, value-weighted index; their table 2.6 and Lo and MacKinlay's table 2.2, largest quintile); the
card takes 0.026 to 0.032, possibly 0.04 with 2008 and 2020. At 0.03 the clause refutes about 36% of
the time with no effect, about 1% at +0.06, the middle of the prediction, and about 15% at +0.02,
its low end.

**What was published, and what it tells.** No verdict has published SPY's or IWM's weekly
autocorrelation, nor a split of their weeks by the week before.

- **SC-001-01** published the funds' returns by weekday; **SC-009-01** those of sessions −10 to −6
  of every month, with a split at quarter-ends; **SC-002-01** IWM's in-sample beta to SPY, 1.135.
- **MR-032-01** published its weekly reversal within groups: the equity-markets group's (SPY, QQQ,
  IWM, EFA, EEM) weekly rank correlation across its funds, +0.0182 (0.0178); the decay of its bet on
  the first session held, −0.0229 (t −2.00); the lag-one autocorrelation of its own weekly series,
  −0.001; its costs, 3.27% a year. These are relative, across funds, not each fund's own
  continuation.
- **The registry** holds the trials' monthly returns, from which no weekly autocorrelation can be
  computed.

None is the graded quantity. This card publishes in turn each fund's weekly autocorrelation and
slope and SPY's and IWM's cross-autocorrelations, which later cards of **TM-043** and **LL-001**
will disclose.

**The data.** The snapshot's cross-check lists SPY's close of 2009-07-16 as 1.1% too low. That
session is never a block boundary of the base or the variant; the blocks shifted by one session read
it at one boundary. It is kept, as the lab keeps its closes.

**TM-041's refutations, and what the card can grade.**

1. *Momentum and return autocorrelation no larger in small capitalisations than in large ones*:
   graded in its weekly autocorrelation form, IWM against SPY; its four-week form reported by the
   variant; its cross-sectional form, momentum within small stocks, needs single stocks.
2. *No larger among small firms with little analyst coverage and trading*: analyst coverage is not
   held.

**Measures stated before the run**, reported, not graded:

- the variant, blocks of 20 sessions: the same regression;
- the slopes of all fourteen funds from their stacked regression, each over its own blocks, and each
  fund's first-order weekly autocorrelation; IWM's slope less QQQ's, and less the average of the
  thirteen others' slopes;
- the same regression with the other fund's return over the block before as a regressor too — SPY's
  last block for IWM and IWM's for SPY, the cross-autocorrelation that is **LL-001**'s claim;
- the same regression with the block grid shifted forward by one to four sessions, the blocks
  starting on the second to fifth session, under the same end rule;
- the clause over the blocks starting in 2005 to 2013, in 2014 to 2022, without those of 2008 and
  2009, and over the holdout, 2023 to 2025;
- the base's alpha before and after costs, and the neighbours', the variant's and the one-day-late
  rule's alphas and appraisal ratios.

## What was considered, and why each is set aside

- **A rule that carries the contrast**: the thirteen large funds held always and IWM alone timed on
  its own week, or IWM and SPY timed against the rest. The battery judges a rule's alpha over its
  funds held in equal parts: such a rule's alpha would read IWM's own continuation, not its excess
  over SPY's, and on one fund of fourteen its timing would be a fourteenth of the portfolio, below
  any gate's resolution. The clause carries the contrast; the rule is the plain trade the lab can
  judge.
- **Momentum over months on IWM against SPY**, a time-series trend on each: the sources' months are
  a cross-section of single stocks, and Bali's table finds none among the smallest; TM-017-01 held
  SPY, not IWM. Left.
- **Large capitalisations leading small ones**, SPY's week predicting IWM's: **LL-001**'s claim
  (Lo and MacKinlay, 1990), reported here as a control, not graded. Nonsynchronous trading as its
  cause, **LL-004**'s; volume leading, **LL-002**'s.
- **The continuation of index returns over two to sixteen weeks**, with the equal-weighted index
  against the value-weighted one among its refutations: **TM-043**'s claim, which this card's rule
  trades and its reported measures touch; RSP, an equal-weighted S&P 500 fund, is not in the
  snapshot.
- **Weekly autocorrelation by liquidity and horizon in stocks**: **MR-007**'s claim, on single
  stocks; this card's funds are both liquid.
- **More funds by size**, QQQ or the sector funds: QQQ is large and technology, the sector funds are
  large; neither splits the market by size.
- **Small commodity markets**: the lab holds DBC, a basket, and GLD and SLV; no measure of a
  market's size.

## Implementation

Long only, the fourteen US equity funds, with European (UCITS) funds that track them; one decision
about a week, the block read up to the session before and traded at the close, a day's delay. The
blocks are counted in sessions from 2005-01-03: a feed that gained or lost a session would move
every later block, a risk for paper trading, whose calendar is fetched again, stated here.
