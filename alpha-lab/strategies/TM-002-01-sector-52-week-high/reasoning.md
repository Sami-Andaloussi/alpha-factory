# TM-002-01 — Nearness to the 52-week high among sector funds: reasoning

## Why this theory now

TM-002 comes right after TM-003, whose card this one reuses so that only the ranking measure
differs, and with it the rule for ties. TM-002 holds that investors anchor on an asset's highest
price of the past year: near it, they hesitate to pay what the news already
justifies and the price adjusts slowly; far below it, they hesitate to sell. Its source, George and
Hwang (2004), ranks all US stocks each month from 1963 to 2001 by the ratio of the price at the end
of the month to the highest price of the twelve months ending then, buys the top 30% and sells the
bottom 30%, and holds each month's portfolio for six months, as Jegadeesh and Titman (JT) and
Moskowitz and Grinblatt (MG) do for past returns. Their Table I finds the three (6, 6) strategies
about equal before any control: 0.45% a month for the 52-week high (t = 2.00), its winners earning
1.51% a month, MG's 1.48% and JT's 1.53%. Their regressions (Table V), which skip a month and
separate the three signals, controlling for size and the last month's return, find the 52-week high
dominant: 0.65% a month from its pure winners less its pure losers (t = 4.08), against 0.38% for JT
and 0.25% for MG; 0.86% once the Fama and French factors are hedged. Their conclusion is that
nearness to the 52-week high predicts future returns better than past returns, and that its gains,
unlike those of past returns, do not reverse.

Most of that dominance is on the short side. The pure 52-week-high winners — a return over a
neutral portfolio, the other signals, size and the last month's return held apart — earn 0.16% a
month (t = 3.06), 0.27% hedged, where MG's pure industry winners earn 0.18% and 0.19%, and JT's
0.17% and 0.16%. The pure 52-week-high losers lose 0.48% a month, 0.59% hedged, far more than the
others' losers. A long-only form keeps the side where the 52-week high adds least.

The bank's neighbours: **TM-001**, stock momentum; **TM-003**, industry momentum, whose card
TM-003-01 this one reuses; **TM-017**, trend following, whose breakout form is the time-series
cousin of this ranking; **CA-001**, momentum within groups of funds.

## What the lab can test, and how

The source's unit is the single stock, and its mechanism is conceived for one: a salient quoted
price that investors watch. The lab holds no single stocks. The bank extends the analogy to futures
whose highs traders watch and lists equity indices among the theory's asset classes; the lab's
closest cross-section is the eleven sector funds, which TM-003-01 has just used — baskets closer in
risk than the lab's other assets, though not alike: staples and utilities move about half as much
as energy or financials. The source itself never ranks industries by nearness: its industries are
ranked by past return only. The lab's other cross-sections are worse for this signal: across
equities, bonds, metals and commodities the ratio mostly ranks volatility — a Treasury fund is
nearly always near its high, silver rarely — and the five equity markets are too few.

The card therefore takes TM-003-01's construction unchanged and changes only the ranking measure,
and with it the rule for ties, which TM-003-01's exact returns never needed:
the three sector funds nearest their 52-week high, where TM-003-01 took the three with the highest
six-month return. Three of eleven is 27%, close to the source's 30%. Each month's three form a
tranche held for six months, and the portfolio holds the last six tranches in equal shares, the
source's (6, 6). What the battery finds, set beside TM-003-01, tests both claims of the theory:
that nearness predicts, by the alpha over the funds held in equal parts, and that it predicts
better than past returns, by the difference from TM-003-01's base over the same sessions and costs.
The second is a transposition the source never made: on these funds the card can refute it or leave
it not shown, never show it.

- **The measure.** The close of the session before over the highest of the 252 closes up to it:
  the source's month-end price over its twelve-month high, read up to the session before, as all the
  lab's signals are. A fund is ranked once it has 252 closes.
- **Ties.** A fund whose last close is its high has a ratio of exactly 1, and in rising markets
  several funds often sit there together. Funds tied with the third are all held, in equal parts:
  a tie broken alphabetically would favour materials, communication, energy and financials, and one
  broken by the six-month return would pull the rule towards TM-003-01 and shrink the very
  difference the card measures. A tranche can then hold more than three funds, nearer the equal
  weight, in strongly rising months.
- **Adjusted closes.** The lab's prices are adjusted for dividends (its snapshot holds no other).
  Investors watch the quoted price, which falls on each ex-dividend date while the quoted high does
  not move; adjusted closes lower every earlier close instead, the high included. A fund that paid
  a dividend since its high therefore looks nearer to it by what it paid since, at most its year's
  dividend — 3 to 4% for utilities and real estate, about 1% for technology — enough to change which
  three are held when several funds sit within a few percent of their highs.
- **Variants.** The base holds each tranche for six months, the source's main strategy; the
  variant for twelve, its (6, 12), where the pure 52-week-high winners still earn 0.13% a month
  (t = 2.83), 0.23% hedged. The source's high is always of twelve months: the window is not a
  variant but a parameter whose neighbours gate 6 tries.
- **No month skipped.** The source's descriptive tables skip none; its regressions skip one against
  bid-ask bounce in single stocks, which liquid sector funds barely have.

**What this card does not test.** The anchor on a single stock's quoted price; the short side,
where most of the source's dominance lies; the claim that the gains do not reverse (the source's
Table VI); the source's controls for size and the last month's return. The verdict will speak for
nearness to the high among sector baskets only.

## What the battery judges, and what to expect

**The size predicted.** The pure long side of the source's 52-week high earned 0.16% to 0.27% a
month, raw and hedged, about 1.9 to 3.2% a year; halved for the years after publication and for
baskets coarser than stocks, as for TM-003-01, about 1 to 1.6%. The card predicts an alpha of about
1 to 2% a year over the funds held in equal parts; at the tracking of about 5.6% a year that
TM-003-01's reasoning took from its source, an appraisal ratio of about 0.2 to 0.3. The source's
own size, the raw pure winners' t of 3.06 over 38.5 years, is an annual ratio of about 0.5.

For the difference from past returns, the source's univariate winners earn about the same under
the three rankings (1.51%, 1.48% and 1.53% a month), and its pure winners give the 52-week high
between 0.02% a month less than MG's (0.16% against 0.18%, raw) and 0.08% more (0.27% against
0.19%, hedged). Outside January the pure winners earn 0.27% and 0.32% against MG's 0.17% and
0.19%, 1.2 to 1.6% a year more; sector funds, weighted by capitalisation, lack the small stocks'
January effect, so those figures may be the more relevant, and halved they give 0.6 to 0.8%. The
card predicts between nothing and about 1% a year more than TM-003-01's base.

**The two tests and their noise.** The alpha over the funds held in equal parts is measured, as an
appraisal ratio, to about ±0.24 over these 17 years. The clause refutes the first claim only when
the ratio is −0.1 or less and the placebos show no skill: from the prediction's low end, 0.2, that
is 1.25 standard errors, a chance of about 10% before the placebo condition, about 5% from 0.3.

The difference from TM-003-01 is less noisy than either alpha, as the two rules often hold the
same funds: the funds near their high are often those that rose most over six months. TM-003-01's
bets moved by 6.3% a year; if the two rules' bets are correlated at about 0.8, their difference moves
by about 6.3% × √(2 × 0.2) ≈ 4% a year, a standard error of about 1% a year over 17 years. If they
differ more, the standard error is larger — 1.3 to 1.5% a year if a third to a half of the holdings
differ — which is why the clause also asks the difference to lie more than one measured standard
error below zero. At a standard error of 1%, the clause would refute wrongly about 16% of the time
if the true difference were zero, 7% at +0.5%, the middle of the prediction, and 2% at +1%. Using
TM-003-01's measured spread to size a band borrows a noise, not a result, as TM-024-01 did against
CA-001-01; TM-003-01's mean plays no part in the prediction.

**The test's power.** A long-only test of the side where the source finds the 52-week high adds
least, on baskets rather than stocks, cannot show the source's dominance; it can refute the first
claim if nearness has no edge at all, and it can find nearness doing clearly worse than past
returns. Gate 4 will count about ten or eleven effective trials; an appraisal ratio of about 0.7
would be needed to pass it.

**Risks named before the run.**

- **A tilt to defensive funds.** Funds that move less sit nearer their highs for that reason alone,
  and dividends paid since the high push the high-yield ones nearer still. Both favour staples,
  utilities, health care and real estate. The battery's alpha is hedged of beta, so a lasting
  defensive tilt can make alpha without any anchoring. The verdict will report the base's beta and
  its share of months in XLP, XLU, XLV and XLRE against TM-003-01's; it cannot separate the
  volatility tilt from the dividend bias.
- **TM-003-01's risks, on the same funds.** The 2009 rebound, when the funds nearest their highs
  were the crash's leaders; energy in 2021–22; one fund above 30% of the profit; the sectors as one
  cluster, so that gate 6's cluster check does not apply; XLRE and XLC ranked only a year after they
  start trading, from about October 2017 and July 2019.
- **The variant** holds each tranche twice as long and turns over half as much; it starts with the
  base, since both need 252 closes.

## Choices, and the options rejected

- **A cross-asset ranking** of all the lab's assets: the ratio would rank volatility.
- **A time-series rule**, each asset held while near its high: a breakout rule, which is trend
  following (TM-017) rather than a ranking against a common anchor.
- **The top 30% as a share** rather than three funds: three is 27% of eleven and 33% of the nine
  funds ranked before October 2017, and keeps TM-003-01's construction, so that only the measure
  differs.
- **Unadjusted prices**: the lab's snapshot holds adjusted closes only; the bias is named above.

## Implementation

Long only, fully invested, eleven US sector funds, each with a European (UCITS) fund tracking the
same S&P sector index, rebalanced monthly on closes with the orders filled at the next close: the
ranking reads the session before, so a day of delay is built in, and gate 6 adds another. No fund
of the universe stops trading between 2005 and 2025; the rule for one that does is there for
gate 6's tests.
