# CA-006-01 — The sector funds held after a month of financials leading them: reasoning

## Why this theory now

CA-006, "do industries lead stock markets?", holds that some industries react before the aggregate
market because they are closer to changes in real activity — household spending, business
investment, credit, production costs — and that investors are slow to draw the implication of their
returns for the broad market: the lagged returns of those industries predict the market's next
returns at short horizons. It is a lead-lag between an industry and the market that contains it,
not between two markets (LL-042, tested) nor within a group of peers (the momentum rules).

**The bank's neighbours.** **LL-009**, industry information diffusion, and **LL-011** and
**LL-012**, vertical and horizontal links between industries, predict one industry from another;
**CA-028**, oil shocks and sector rotation, reads oil prices. This card predicts the whole market
from an industry.

**What the lab already knows.** No verdict published by the lab reads one sector fund's past month
against the market's next; SC-017-01's table of monthly averages and the momentum rules' records
bear on the sector funds' returns, not on this lead. The card is as blind as the lab's cards get.

**The sources.** The lab has neither study the bank names in its library. Hong, Torous and Valkanov
(2007) are known to it through Johnson (*Algorithmic Trading and DMA*, 2010, the chapter on
co-movement): in the US, the returns of over a dozen industries showed a significant lead of about a
month over the market; in economic significance banking led, followed by real estate, printing,
apparel and services; some resource industries, petroleum and metals, had a negative relation; the
leading industries were those that act as indicators of economic activity; similar effects appeared
in the UK, Canada, Germany and Japan, with more variation in the industries. Johnson gives a ranking
and "around a month", no size. Tse (2015), a re-examination, is known only through the bank's
reference list; the card does not know its finding. No other text in the library says that banks or
financials lead or predict the market.

## From the claim to a signal

- **The market**: the lab has no index of all US stocks built from its industries, but it holds the
  eleven sector funds, which together are the S&P 500 by sector. The card takes them, held in equal
  parts, as the market the industries lead, and as the benchmark: the rule holds them all or none,
  so that its alpha is its timing alone. The source's market is value-weighted; this one is the
  sectors in equal parts.
- **The leading industry**: banking, the strongest lead in the source; the lab's fund is XLF, the
  financial sector — banks, insurers, capital markets, and real estate until XLRE's split in 2016,
  so that before 2016 it holds the source's two strongest leaders — the closest it holds.
- **The signal**, base: on the first session of each month, XLF's return over the last 21 sessions,
  to the session before, less the average return of the sector funds trading over the same sessions:
  the lead beyond the market's own move, in part. XLF's beta on the sector funds' average, about 1.3
  over the signal's windows, leaves about a third of the market's own month in the signal (their
  correlation is about 0.4), so the clause grades the slope that holds the market's month fixed — a
  regression in the manner the source's title and field suggest, which no text in the lab describes
  — Johnson's summary does not state it — and which the card adopts as its own choice. When the
  signal is positive, every sector fund trading is held in equal parts; otherwise the portfolio
  holds the bill.
- **Variants.** First, XLF's own return over the bill over the same 21 sessions, the industry's
  return as the source's regression reads it, its own momentum and the market's included. Second,
  the source's leaders together against its negative leads: the average return of XLF, XLY (consumer
  discretionary, the apparel and services the study ranks, in part — business services sit in XLK
  and XLI, and printing in XLC and XLY) and XLRE (real estate, in the signal from 2016-11-01, once
  it has 21 sessions) less that of XLE and XLB (petroleum and metals). The minus-XLE leg borders on
  CA-028's oil shocks, which read oil prices to rotate sectors; here energy's month only times the
  whole market.
- **The horizon**: a month, the source's lead; monthly targets, the core's pace.
- **The memory**: 21 sessions.

The pace was counted before the card by a scratch script outside the repository (`pace.py`, in the
session's scratch folder) that reads the past returns alone: 214 monthly targets from 2005-03-01;
the base invested in 96 of them with 97 switches, the absolute variant in 123 with 104, the
composite in 106 with 92.

## What the battery judges, and what to expect

**The size predicted — a judgment, not derived.** The source reports significance and ranks, not a
size the lab can read. A lead of about a month by banking, the strongest, would show as a higher
market return after months when financials led than after months when they lagged; the card judges a
difference of about 0.3 to 0.8% a month plausible over the long record, a slope of about 0.06 to
0.16 on XLF's relative month. A rule in the market about half the time, at a beta of about one half,
earns roughly a quarter of twelve times that difference over the market held always: an alpha of
about 1 to 2.5% a year before costs of about 0.3% a year, at an appraisal ratio of about 0.1 to 0.3
before costs (the timing's hedged volatility, √(p(1 − p)) of the market's 16% at p about 0.45, some
8%). The card expects less from 2005 to 2022 than over the source's years, which it does not know.

**The clause.** Judged before costs on the source's claim, that financials' past month predicts the
market's next beyond the market's own past month: on each monthly target session from the base's
first, 2005-03-01, whose next target session is on or before 2022-12-30 (213 months), the equal
average of the returns of the sector funds trading on the target session, each from the target's
close to the next target's close, less the bill's return compounded over the same sessions,
regressed by ordinary least squares, with a constant, on XLF's relative return over the base's
21-session window and on the funds' average return over that window; the slope on XLF's relative
return — equal to the slope on XLF's own return with the market's past month held fixed — and its t
statistic from the usual standard error. The theory is refuted in this form if that t statistic is
−0.35 or below. Above it, short of passing gates 1 to 7, the theory is not proven, not refuted; a
base that passes gates 1 to 7 while the clause refutes leaves the theory refuted in this form. The
difference of the market's mean return after positive and non-positive signals, the rule's own
split, is reported: with no lead from financials, it moves with the market's own autocorrelation,
which the signal partly carries — at a monthly autocorrelation of −0.1 it would fall at or below
zero 69% of the time, at +0.1 it would show a difference of about 0.26% a month.

Of CA-006's refutation criteria, the first (lagged industry returns carry no information) is graded,
and the third (the market incorporates the information as fast) is the same test; the second (the
leaders are not the activity-tied industries) is reported through the single-fund measures; the
source's other countries are not tested.

**The test's power.** A synthetic simulation by the logic audit — no lead, a market monthly
volatility of about 4.5 to 5% — gives the clause's rates: about 36% with no lead, 18% at a slope of
0.05 and 8% at 0.10, where a slope of 0.06 to 0.16 is the prediction (0.3 to 0.8% a month over the
gap, about 5.2% measured on the signal's own past — 4.6% for its part apart from the market's month
— between the two sign groups' average relative signal; about 15% at 0.06). The band keeps a small
lead of the predicted sign from being called refuted; it can refute only a lead gone or reversed.

**Measures stated before the run**, reported, not graded:

- the difference of the market's mean return after positive and non-positive base signals, with its
  standard error, the square root of the sum of each group's variance over its count; the same for
  the two variants; the market's own coefficient in the graded regression;
- the slope and the difference by the targets set in 2005–2010 (70 months), 2011–2016 (72) and
  2017–2022 (71), and without the twelve months whose target is set in 2008;
- each variant's alpha before and after costs, and its months invested;
- the same difference and slope with each of XLF, XLY, XLRE (from 2016-11, 73 months), XLE and XLB
  alone, its return less the funds' average in XLF's place, the same sign rule; the source's sign is
  positive for the first three and negative for XLE and XLB.

**Risks named before the run.**

- **Crises**: 2008, when financials led the market down, and 2020 decide much of an 18-year record
  of monthly switches.
- **Few decisions**: about a hundred switches; gate 1 needs thirty clustered decisions.
- **Gate 6**: a rule holding all eleven or none is unlikely to fail gate 6 on one fund's share
  unless its total profit is thin, and fails it if the total is not positive; the eleven form one
  cluster, so gate 6 leaves none out. Its neighbours, windows of 16, 26, 10 and 32 sessions, change
  the base's in or out in 40, 20, 53 and 36 months.

## Choices, and the options rejected

- **SPY as the market**: a universe of one fund cannot pass gate 6; the sector funds are the same
  market, in equal parts.
- **Holding the leading industry itself**: the claim is about the market.
- **A weekly lead**: the source's lead is about a month.
- **Bonds instead of the bill when out**: another claim, LL-042's.

## Implementation

Long only, the eleven sector funds, each with a European (UCITS) fund that tracks it, or cash,
monthly targets filled at the close of the session on which they are set; gate 6 adds a day's delay.
