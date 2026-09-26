# TM-037-01 — Market turnover as a contrarian sign of sentiment: reasoning

## Why this theory now

TM-037 is next in the trend-and-momentum family, taken in number order. It holds that investor
sentiment, the propensity to speculate (Baker and Wurgler, 2006), measured through the volume of
initial public offerings, closed-end fund premiums, market turnover and inflows into equity funds,
strengthens momentum and other anomalies after high sentiment, when the limits to arbitrage bind
more (Stambaugh, Yu and Yuan, 2012, 2014); by analogy, perpetual futures' funding rates and the
Commitments of Traders' positioning. Its refutations: momentum and other anomalies no stronger when
sentiment is high than when it is low; sentiment proxies — IPO volume, closed-end fund premiums,
turnover, fund inflows — carrying no information about subsequent returns. The bank names stocks,
crypto-assets and commodities.

A first judgement drew TM-037 as not testable, holding that the library signs turnover only inside a
composite. Its reader found the library signing market turnover on its own, with a direction and a
measured result, and no verdict reading it. TM-027-01's reasoning had handed this very form, market
turnover as a contrarian sentiment gauge, to TM-037; TM-036-01 had handed it the sentiment proxies
in general, and TM-006-01 momentum conditioned on them. Since the lab now passes a strategy the
funds' volumes (TM-028-01), the form is readable, and this card draws it.

**Its sources.** The source papers — Baker and Wurgler (2006), Stambaugh, Yu and Yuan (2012, 2014),
Baker and Stein (2004), Jones (2001) — are not in the library; they are read through these books.

- **Ilmanen** (*Expected Returns*, 2011, section 8.6, "Sentiment and technicals"): among "a host of
  contrarian sentiment indicators", Baker and Wurgler's include market turnover; their composite has
  a predictive correlation of −0.11 with the S&P 500's excess return, the horizon of the figure not
  legible in the library's copy of the section's table; section 14.5, momentum profits "appear to be
  larger after market gains and when investors are optimistic"; chapter 18, on liquidity: stocks
  with low past turnover earning more than high-turnover ones (Chen, Ibbotson and Hu, 2010), and
  "some liquidity crises coincide with high turnover (position unwinds despite high trading costs)
  whereas a persistent market decline tends to coincide with lower turnover"; the short-lived
  "abnormal" state of Watanabe and Watanabe (2008), "characterized by rising turnover, high
  volatility", which includes positive as well as negative liquidity developments.
- **Bali, Engle and Murray** (*Empirical Asset Pricing*, 2016, section 18.2, "Investor Sentiment",
  p. 479): Baker and Stein (2004), "Market liquidity as a sentiment indicator", in which high
  sentiment brings overvaluation; young, risky firms underperforming after high sentiment (Baker and
  Wurgler); stock anomalies stronger after high sentiment, "driven by the short positions"
  (Stambaugh, Yu and Yuan).
- **Shefrin** (*A Behavioral Approach to Asset Pricing*, 2nd edition, 2008): the Baker–Wurgler index
  of six measures — the closed-end fund discount, detrended log turnover, the number of IPOs, their
  first-day returns, the dividend premium and the equity share in new issues — and its seesaw: after
  high sentiment speculative, hard-to-arbitrage stocks earn less than safe ones, after low sentiment
  more (chapter 18, section 18.4); Statman, Thorley and Vorkink (2006), turnover rising after the
  market has gone up, which they read as overconfidence (chapter 29, section 29.3.3).
- **Acharya and Pedersen**, "Asset Pricing with Liquidity Risk", chapter 5 of Amihud, Mendelson and
  Pedersen's *Market Liquidity* (2013), section 3.2: "Jones (2001) finds empirically that the
  expected annual stock market return increases with the previous year's bid-ask spread and
  decreases with the previous year's turnover" — turnover alone, at the level of the market, a year
  ahead. They read it as a liquidity result, high illiquidity today predicting a high required
  return: the time-series form of **CA-029**'s illiquidity premium. Only Ilmanen and Baker and Stein
  give turnover a sentiment reading; the sign is the same in both readings.

**The form this card tests.** High market turnover, a sign of optimism, comes before low equity
returns: the contrarian reading of the one sentiment measure the lab's data reach. The bank's
refutation is two-sided — no information about subsequent returns — and the card grades the signed,
contrarian form the library gives; a strongly positive result would be information of the opposite
sign, refuting the contrarian form only. The turnover of a market is its shares traded over its
shares outstanding. The lab holds the funds' share volumes, not their shares outstanding, and ETFs
make up just under a third of US equity volume, SPY's shares turning over about 2,700% a year
(Madhavan, *Exchange-Traded Funds and the New Dynamics of Investing*, 2016, chapter 1). The card
reads the market's turnover through SPY's traded volume, as the lab already read SPY's, QQQ's and
IWM's volume as a crude measure of the market's participation (SC-016-01, SC-027-01), detrended over
five years: Baker and Wurgler's (2006) detrending as it is known from outside the library, which
gives only "detrended log turnover"; nothing in the library confirms the five years, and they are
taken as fixed for that reason.

## From the claim to a signal

- **The measure**: SPY's log traded volume, as `market.signal_volumes` gives it, averaged over the
  last `window` sessions to the session before the target, less its average over the last 1,260
  sessions to the session before, the five-year detrending. A missing or zero volume is left out of
  both averages; `python -m lab.data check` lists none of SPY's bars (TM-028-01).
- **The state**: turnover is *high* when the measure is above zero.
- **The universe**: the fourteen US equity funds, SPY, QQQ and IWM and the eleven sector funds — the
  US stock market the measure reads; EFA and EEM are left out, their home markets' trading not being
  SPY's.
- **The rule**: on the first session of each month, when turnover is high, the portfolio is in cash;
  otherwise each fund trading holds 1/N, N the funds trading. While the measure is not defined — the
  first 1,260 sessions — the funds are held in equal parts. Everything is read up to the session
  before; targets are traded at the close.
- **The variant**: `window` 21, the month's turnover, Baker and Wurgler's monthly series, where the
  base takes 252, Jones's previous year.
- **Parameters**: `window`, 252; neighbours 189 and 315, 126 and 378. The five-year detrending is
  fixed, with no neighbours: a parameter moved by gate 6 would test the detrending, not the sign.
- **Memory**: 1,260 sessions, the five years of volumes read back from the session before the
  target.

**What the proxy carries besides turnover.** SPY's share volume differs from the market's turnover
by SPY's shares outstanding, which creations raise, and by ETFs' share of all trading, which grew;
the five-year detrending removes the slow part of both. Two other things move it, and the first is
the proxy's main risk. Ilmanen's chapter 18: some liquidity crises, position unwinds, coincide with
high turnover, while a persistent decline coincides with low; the months in which the measure is
high may be months of stress, low sentiment, not optimism. The graded form is Jones's sign on
turnover, whatever turnover reads: a refutation driven by months of crisis and rebound speaks to
that sign on these years, and the verdict reports the clause without the months of high volatility
to tell turnover from stress. Second, Statman, Thorley and Vorkink find turnover rising after the
market's gains: the verdict reports the clause with SPY's past year's return as a control, knowing
that the control may remove part of the sentiment signal itself.

## What the battery judges, and what to expect

**The size predicted — a judgment.** Jones's sign is on the whole market over a year; Ilmanen's
composite correlates at −0.11 with the market's excess return; turnover alone, and SPY's share
volume as its proxy, should carry less. With the market's monthly volatility of about 4 to 5%, a
figure known in general and not computed on the sample, a correlation of −0.05 to −0.1, taken as the
quarter's, as the section's other figures are, is worth about 2 to 6% a year between the months
after high and low turnover. The card judges the fund-months after high turnover to earn about 1 to
8% a year less over the bill than those after low turnover, and the rule's alpha over the fourteen
funds held always about −1 to +2% a year: it steps out of the market for whole stretches of months,
and a wrong stretch costs its premium.

**The gates.** The rule moves all fourteen funds at once, and its state, read over a year against
five, changes rarely. Gate 1 counts the base's decisions: its first holding, the months its state
turns, and the entries of XLRE and XLC if the state holds the funds then; the card judges them
likely fewer than thirty, perhaps 5 to 20, and gate 1 likely to fail on them; the card is drawn all
the same (SC-019-01). Gate 1's years run from the first holding, 2005, eighteen in-sample. It
expects the base to fail gate 3, whose placebos keep its average exposure, and gate 4; gate 5 as
well: until February 2010 the rule holds the fourteen funds in equal parts, the benchmark itself, so
the blocks of 2005–07 and 2008–09 give no alpha, and gate 5's three positive blocks need all three
of 2010–14, 2015–19 and 2020–22; and possibly gate 2. The high-volume months of a crisis, followed
by a rebound, are the rule's likeliest cost.

**The clause.** Judged before costs, on the market's closes, over the in-sample fund-months from the
first target on which the measure is defined, the first session of February 2010, to December 2022,
the last month ending at the close of 2022-12-30, each fund-month from the close of a target's
session to the close of the next target's session, over the funds trading at the target, without the
months of TM-024-01's published panic states (below): each fund-month's return less the bill's over
the same sessions, regressed by ordinary least squares on an indicator of high turnover at the
target, with one constant for each fund, the standard errors clustered by month, the funds' months
in each month one cluster; the t statistic computed apart from the battery. The theory is refuted in
this form if the t statistic is +0.35 or above: the months after high turnover no worse than those
after low. Between, short of passing gates 1 to 7, not proven, not refuted; a base that passes gates
1 to 7 while the clause refutes leaves the theory refuted in this form. The clause bears on TM-037's
sentiment reading; it is not graded for CA-029, whose own card would read the illiquidity premium
through its own measure; the result is reported to it.

**The test's power.** The first target with five years of volumes is the first session of February
2010 (1,260 sessions from 2005-01-03 end on 2010-01-04, counted from the calendar), so 155 months to
December 2022, 149 without the six left out. The indicator is the same for every fund in a month,
and the errors are clustered by month, so the standard error is set by the fourteen funds' monthly
average. The nearest published figure is TM-028-01's: the fund-months of the fourteen funds with
their trend up less those with it not up, one constant for each fund, clustered by month, over 203
months, carried a standard error of 13.10% a year; its state was set fund by fund and differed
within a month, so a state common to the month has a larger error, and 13.10% is a lower anchor. The
card takes 10 to 15%. The clause then refutes about 36% of the time with no effect and about 21 to
26% at −4.5% a year, the middle of the prediction: the test cannot tell the predicted effect from
none, and a refutation is weak evidence. The split may be far from halves: SPY's share volume is
reported, outside the library and the lab's data and not checked, to have peaked in 2008 and 2009
and fallen for years after, a five-year average that still holds the crisis years reading most of
2010 to 2014 as low turnover; the card judges the high state likely to take a quarter of the months
or less. The months of high volatility in which it may bunch make its fund-months the more variable.
Nothing of the snapshot's volumes was computed before this card.

**What was published, and what it tells.** No verdict has published the funds' returns after high
market turnover against those after low.

- **TM-024-01** published the months of its panic states and some of their returns: the sectors in
  July to September 2010 and April 2020, the equity markets in August and September 2010, April and
  May 2020 and October 2022, inside this card's window; in September 2010 the equity markets rose
  11.3% and the sectors 8.4%, in October 2022 the sectors 8.2% and the equity markets 5.4%. They are
  months of high volatility, likely in the high-turnover set, with outcomes against the prediction.
  The six months — July, August and September 2010, April and May 2020, October 2022 — are left out
  of the graded clause for all fourteen funds, whichever set they fall in, and the clause with them
  is reported: the returns published for September 2010 and October 2022 are outcomes on those very
  months, whichever set holds them, and a graded sample that depended on the state would be harder
  to audit; TM-023-01 and TM-047-02 kept such months, published only pooled, and this card follows
  the literal rule, as TM-006-01 did.
- **TM-028-01** published that the fourteen funds rose on their quiet sessions and fell on their
  loud ones, the same sessions' returns, not the months after; and its variant, the fund-months with
  the trend of the sessions on which SPY's volume fell up against those with the trend of the
  sessions on which it rose up, −1.00% a year (t −0.16), a state read from the daily changes of
  SPY's volume, not its level against five years.
- **SC-016-01** and **SC-027-01** published the three US funds' log volume by calendar window, with
  no return split by it; **SC-019-01** the US funds' returns by year.
- **TM-047-02** published an alpha before costs of 1.56% a year over 2005 to 2022 for the five
  equity funds scaled down in volatile months, the gain mostly from 2008 and 2009; its alpha at a
  beta equal to the average scale, the timing of its exits, −0.91% a year (2.15%); and its scale by
  year, 0.61 in 2020 and 0.49 in 2022. Volume and volatility move together.

None of the last four is the graded quantity; their fund-months stay in the graded sample,
disclosed, and the verdict reports how far the high-turnover months coincide with TM-047-02's
volatile ones.

**TM-037's refutations, and what the card can grade.**

1. *Momentum and other anomalies no stronger when sentiment is high*: sentiment measured by the
   composite the lab does not hold, and the effect of Stambaugh, Yu and Yuan in single stocks' short
   legs; momentum after market gains, the nearest state the lab's closes give, was read by TM-006-01
   (momentum within groups switched off after a two-year fall, stopped at gate 2) and TM-024-01;
   momentum conditioned on turnover would compose two signs on one proxy, and is left.
2. *Sentiment proxies carrying no information about subsequent returns*: graded in its turnover
   form by the clause, from the contrarian side; IPOs, discounts, flows and issuance are not held.

**Measures stated before the run**, reported, not graded:

- the variant, the month's turnover: the same regression;
- the clause with TM-024-01's six panic months;
- the share of months in the high state, and the months in which the state turned;
- the same regression with SPY's return over the 252 sessions to the session before the target as a
  control;
- the same regression with the measure itself, not its sign, as the regressor;
- the months of high turnover that fall among TM-047-02's volatile months, where its scale, from the
  five equity funds' 21 sessions of risk, was below one, and the clause without those months;
- by group: SPY, QQQ and IWM, and the sector funds;
- the clause over the months of 2010 to 2016, over those of 2017 to 2022, and over the holdout, 2023
  to 2025;
- the rule's alpha before and after costs, and the neighbours' and the one-day-late rule's alphas
  and appraisal ratios.

## What was considered, and why each is set aside

- **Recording TM-037 not testable**: the first judgement's conclusion, overturned by its reader.
- **Momentum conditioned on sentiment** (Stambaugh, Yu and Yuan; Ilmanen, section 14.5): above.
- **The Baker–Wurgler seesaw on funds**, IWM against SPY, XLU or XLP by sentiment state: a relative
  rule on the same proxy, a second trial on one measure, and the seesaw's evidence is on single
  stocks sorted by age, size and volatility; left for a later card if this one's result calls for
  it.
- **Each fund's own detrended volume**: a fund's volume is its own shares' trading, not its market's
  sentiment; the sources' turnover is the market's.
- **Dollar volume**: it rises with the price at a constant turnover, while share volume does not;
  the card takes the share volume, nearer turnover.
- **A shorter detrending**, a year, to start in 2006: the five years are Baker and Wurgler's, as
  known from outside the library, and the card fixes them rather than choose a window of its own.
- **Closed-end fund discounts** are **MR-026**'s claim; **funding rates and perpetual positioning**
  **FP-030**'s; **the illiquidity premium**, in the cross-section and over time, through spreads and
  price impact, **CA-029**'s, whose time-series form claims Jones's result read as liquidity;
  **volume-conditioned reversals** over days **MR-011**'s — all untouched. **TM-027**, recorded not
  testable, and **TM-028**, tested-inconclusive, split momentum by each asset's own volume.

## Implementation

Long only, the fourteen US equity funds, with European (UCITS) funds that track them; one decision a
month, the measure read up to the session before and traded at the close, a day's delay; the whole
portfolio in the funds or in cash by one state. The measure reads the US trading of SPY's shares, as
Yahoo reports it, consolidated across venues.
