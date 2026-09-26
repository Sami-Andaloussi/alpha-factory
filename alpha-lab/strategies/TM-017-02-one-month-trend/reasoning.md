# TM-017-02 — Time-series momentum at one month: reasoning

## Why this card now

TM-017 holds that the sign, and sometimes the size, of an asset's past return positively predicts
its future returns across equity indices, interest rates, currencies and commodities, with
persistence over 1 to 12 months; its first refutation: the sign of past 1- to 12-month returns
carrying no information about the next months' returns, or only in isolated markets and periods.
TM-017-01 read six and twelve months on seven funds and stopped at gate 3; it trades on paper only
as the test of the lab's chain, not as a survivor. The one month was left unread, though several
judgements placed it with TM-017 (TM-005-01, TM-036-01, TM-007-01, TM-015-01), three of them with
TM-043 too. TM-043's judgement (TM-043-01's reasoning) handed it here and recorded that it is drawn
next, so that one trial reads it. The rule is TM-017-01's with its lookback at a month; what makes
this a different form of TM-017, drawn with `parent: null`, is the one-month clause, the
continuation of a month into the next, not the rule. Its trial counts in gate 4.

**Its sources, for the sign.**

- **Ilmanen** (*Expected Returns*, 2011, figure 20.1): adjacent months' returns correlated at +0.20
  on average across asset classes and strategies, 1990 to 2009, "a part of it" illiquidity and
  return smoothing; its bars, read off the figure, about +0.13 for developed equity markets (the US
  among them), +0.21 for emerging ones, +0.22 for commodities (the S&P GSCI, not DBC's index) and
  +0.08 to +0.09 for Treasury duration; no bar for gold; commodity trend following and the size
  effect the two exceptions, mildly negative.
- **Pedersen** (*Efficiently Inefficient*, 2015, chapter 12, after Hurst, Ooi and Pedersen, 2013):
  time-series momentum on 58 futures and forwards, currencies among them, 1985 to 2012, long and
  short, scaled to a volatility target, gross of costs: the average Sharpe ratio by instrument 0.29
  with a one-month lookback, 0.36 with three months and 0.38 with twelve; the diversified one-month
  strategy 1.26. A sign rule's Sharpe ratio of 0.29 corresponds to a monthly autocorrelation of
  about 0.29 / (√12 × √(2/π)), some 0.10.
- **Shleifer** (*Inefficient Markets*, 2000, chapter 5), after Cutler, Poterba and Summers, 1960 to
  1988: the average one-month autocorrelation of excess stock index returns about 0.1 across the
  world and in the US alone; of excess bond returns about 0.2, "and around zero in the United
  States". **Poterba and Summers** (1988, in Lo, ed., *Market Efficiency*, 1997): positive serial
  correlation at horizons under a year "pervasive" across fifteen national indices, capital gains
  only, no single country's result significant.
- **Chan** (*Algorithmic Trading*, 2013, table 6.1): the two-year Treasury note future's return over
  25 days against the next 25, a correlation of +0.20 (p 0.09).

**Its sources, against.**

- **Lo** (*Hedge Funds: An Analytic Perspective*, updated edition, table 2.2), January 1994 to July
  2007, the monthly first-order autocorrelation: the S&P 500 −0.6%, gold −9.3%, oil −5.2%, the
  Lehman bond index +20.8%.
- **Chevallier and Ielpo** (*The Economics of Commodity Markets*, 2013, table 1.5), monthly, 2004 to
  2012, a span the lab's sample overlaps: gold −0.23 (−0.16 over 1995 to 2012), both significant;
  the GSCI's precious metals −0.23, energy +0.27, industrial metals +0.29, agriculture −0.01; the
  S&P 500 +0.24, the Euro Stoxx 50 +0.18, the Hang Seng +0.14 — "weak evidence exists that the
  alleged trends in commodities come from persistent shocks".
- **Campbell, Lo and MacKinlay** (*The Econometrics of Financial Markets*, 1997, table 2.4): the US
  value-weighted index's monthly autocorrelation 6.4% from 1962 to 1978, 1.3% from 1978 to 1994.
- **CA-006-01**'s verdict: the US sector funds' average monthly return on its own previous 21
  sessions, with XLF's relative return held fixed, −0.068 (t −0.82), over 213 months from 2005 to
  2022.

**The form this card tests.** On TM-017-01's funds outside the US equity market — developed and
emerging equity markets, intermediate and long Treasuries, gold and a commodity basket — a fund's
return over its last month predicts its return over the next, positively, on average across them.

## From the claim to a signal

- **The rule**: TM-017-01's, with its lookback at one month: on the first session of each month,
  each fund whose return over the past `lookback` sessions, read up to the session before, beats
  the Treasury bill's over the same sessions and that trades holds a seventh of the portfolio; the
  rest in cash, and a fund's seventh while it has fewer than `lookback` + 1 closes.
- **Parameters**: `lookback`, 21, a month; neighbours 16 and 26, 11 and 32. One variant, the base
  alone.
- **Memory**: 22 sessions.

## What the battery judges, and what to expect

**The size predicted — a judgment.** Fund by fund, from the sources above: EFA about +0.13 to +0.18
(Ilmanen's developed markets, the Euro Stoxx); EEM about +0.14 to +0.21 (Ilmanen's emerging markets;
the Hang Seng, a developed market, as the nearest to EEM's Chinese holdings); IEF and TLT near zero
in the US over 1960 to 1988 (Cutler, Poterba and Summers), +0.08 to +0.21 in later US data
(Ilmanen's Treasuries over 1990 to 2009, Lo's Lehman index over 1994 to 2007, Chan's two-year note);
GLD negative, −0.09 to −0.23 (Lo, Chevallier and Ielpo); DBC mixed, energy and metals positive in
Chevallier and Ielpo, oil negative in Lo, agriculture nil, about +0.1 to +0.2, a judgment. Equally
weighted, about +0.05 to +0.10; cut in its middle for the fading of the equity sign after 1990 in
the US and for the funds' prices, which carry none of the index data's smoothing, and widened for
the spread of the sources. The card judges the pooled slope, each fund's returns scaled by its own
recent volatility so that the funds weigh alike, at about +0.02 to +0.12. The rule's alpha over the
seven in equal parts about −1.5 to +1.0% a year: it is long only, keeps half of a long-short
strategy's timing, holds SPY, whose own month TM-041-01's variant and CA-006-01 found near zero or
negative, and GLD, whose month the sources find reverting; TM-041-01's variant, a twenty-session
version of the rule on the fourteen US equity funds, earned −1.05% a year after costs.

**The gates.** Monthly decisions on seven funds: gate 1 passes on its count. The card expects the
base to fail gate 2 about half the time on its alpha alone, gate 3, as TM-017-01 did, gate 4, some
sixty effective trials, and gate 5 with them; possibly gate 6 on SPY's share of the profit,
TM-017-01's 33%.

**The clause.** Judged before costs, on the market's closes, over the in-sample months from the
first target with 64 closes and a month before it, the first session of May 2005, to December 2022,
the last month ending at the close of 2022-12-30, 212 months, each month from the close of a
target's session to the close of the next target's session, for EFA, EEM, IEF, TLT, GLD and DBC
(SPY's months left out, below), each fund in the months it traded at both the month's and the
previous month's targets with 64 closes before the month's target: each fund-month's return less the
bill's compounded over the same sessions, divided by the standard deviation of the fund's daily
returns over the 63 sessions to the session before the month's target, regressed by ordinary least
squares on the same fund's return less the bill's over the previous month, divided by the same
standard deviation, with one constant for each fund and one slope for all, the standard errors
clustered by month; the t statistic computed apart from the battery. The theory is refuted in this
form if it is −0.35 or below: a fund's month no better after a rising month than after a falling
one. Between, short of passing gates 1 to 7, not proven, not refuted; a base that passes gates 1 to
7 while the clause refutes leaves the theory refuted in this form. Scaling by the fund's own
volatility, known before the month, weighs the six funds alike, as the sources' claim is an average
across classes; the unscaled regression, which weighs them by their variance, EEM, DBC and EFA most,
is reported.

**The test's power.** A count: 212 months, one fund's slope known to about 1/√212, 0.069. EFA and
EEM move together, the others less so; the six funds count as about two and a half to three
independent ones, and the pooled slope's standard error is about 0.04 to 0.05. At 0.045 the clause
refutes about 36% of the time with no effect, about 3% at +0.07, the middle of the prediction, and
about 21% at +0.02, its low end. No return was computed for this estimate. An earlier draft of this
card built it from standard errors of TM-041-01's twenty-session slopes that no verdict published —
figures from that card's own computation apart from its battery — and the audit removed them.

**What was published, and what it tells.**

- **TM-041-01** published SPY's slope on its previous twenty sessions, +0.019, over blocks of twenty
  sessions counted from 2005-01-03; and its variant, the same one-month rule on the fourteen US
  equity funds, SPY among them, −1.05% a year after costs, an appraisal ratio of −0.13.
  **CA-006-01** published the US sector funds' average own-month slope, with XLF's relative return
  held fixed, −0.068 (t −0.82). SPY's own month is therefore a published part of the graded sample:
  its fund-months leave it, and the clause with them is reported.
- **TM-017-01** published its rule's figures at six and twelve months; **TM-001-01** its momentum
  between the same seven asset classes over twelve months; **MR-032-01** a weekly reversal within
  groups, with a twenty-one-session variant, relative across funds, EFA, EEM, GLD and DBC among
  them; **SC-019-01** the rest of the year after January for EFA and EEM, pooled over eleven months;
  **TM-024-01** the equity markets' returns in some of its panic months. None is a graded fund's
  month on its own previous month; they stay, disclosed, and the clause without TM-024-01's equity
  panic months is reported.
- **The registry** carries each trial's monthly returns hedged of its benchmark, and no fund's own
  returns or weights: no graded fund's one-month autocorrelation can be read from it. The series
  nearest are TM-017-01's, TM-001-01's and TM-047-01's on these funds, TM-041-01's variant on the US
  equity funds, MR-032-01's twenty-one-session variant within groups and CA-006-01's on the sectors;
  nothing was computed from them for this card.

**TM-017's refutations, and what the card can grade.** The first, at one month, on the funds outside
the US equity market; its six- and twelve-month forms were read by TM-017-01, its regime form by
TM-018-01; its other criteria are not this card's.

**Measures stated before the run**, reported, not graded:

- the clause unscaled, each fund weighed by its variance;
- the clause with SPY's fund-months;
- each fund's own slope, from the same regression with one slope for each fund;
- the equity funds (EFA, EEM) and the others apart;
- the same regression with each fund's return over the 252 sessions to the session before the
  month's target, less the bill's and scaled alike, as a control, from the first target with 253
  closes before it, the first session of February 2006, on its own sample, so that the one month is
  told from TM-017-01's year;
- the clause without TM-024-01's equity panic months;
- the clause over the months of 2005 to 2013, over those of 2014 to 2022, without 2008 and 2009, and
  over the holdout, 2023 to 2025;
- the base's alpha before and after costs, and the neighbours' and the one-day-late rule's alphas
  and appraisal ratios.

## What was considered, and why each is set aside

- **More funds** — QQQ, IWM, the sectors, SLV, SHY, bitcoin: the card keeps TM-017-01's seven asset
  classes, so that the one month is read where the six and twelve were; the US equity funds' own
  month is published.
- **A one-month rule scaled to a volatility target, long and short**: Pedersen's strategies; the lab
  is long only, and volatility scaling of the trend is TM-047's, read by TM-047-01.
- **A separate slope for each asset class as the graded quantity**: the claim is an average across
  classes; each fund's slope is reported.
- **The weekly continuation**: TM-043's, recorded not testable; the plain weekly trade was
  TM-041-01's.

## Implementation

Long only, the seven funds, with European (UCITS) funds that track them; one decision a month, the
month read up to the session before and traded at the close, a day's delay.
