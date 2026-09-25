# TM-024-01 — Momentum with its crashes managed: reasoning

## Why this theory now

TM-024 explains why momentum can pay on average and still be dangerous: its losses come in rare,
violent crashes, in "panic" states — after a market decline, when volatility is high — as the market
rebounds and the past losers, beaten down, rebound most. Daniel and Moskowitz (2016) show that these
crashes are partly forecastable from a bear-market indicator and the market's recent volatility,
and that a momentum strategy weighted by forecasts of its own mean and variance about doubles the
static strategy's Sharpe ratio; Barroso and Santa-Clara (2015) reach much the same by scaling
momentum by its own recent volatility, in US stocks and in international stock markets. Daniel and
Moskowitz find it in futures too: in equity index futures, momentum's Sharpe ratio rises from 0.71,
static, to 0.80 scaled to a constant volatility and 0.84 managed dynamically; in commodities, from
0.59 to 0.69 and 0.80 (their Table 10). The constant-volatility figures use only past data; the
dynamic ones use coefficients estimated over the whole sample, and read less as a forecast.

CA-001-01's verdict records such a crash. CA-001-01 held, each month, the top third of three groups — the
eleven sector funds, five equity markets, three commodity funds — by their past year's return; its
worst block was 2008–09, when it held the crash's leaders into the rebound of 2009 and trailed the
crash's losers. Its result as a whole was no edge: an alpha of 0.20% a year. TM-024 predicts that
managing the crash risk of the same rule improves it. This card keeps CA-001-01's rule and changes
only how much of its momentum tilt is held, so that what the battery finds, set beside CA-001-01,
is what managing the crashes adds.

The bank's neighbours: **CA-001**, the momentum rule itself; **TM-047**, volatility scaling of
trend positions, tested by TM-047-01; **TM-003**, industry momentum. The theory's asset classes are
stocks and crypto: the lab holds neither a stock universe nor several crypto assets, and its closest
cross-section is CA-001-01's groups of funds. The sources find the same option-like crashes in index
futures and commodities, which are what those groups hold.

## From the mechanism to a signal

A long-only portfolio cannot hold the losers short, whose rebound is the crash. What it holds is a
tilt: more of each group's leaders than the group held in equal parts, less of the others. In a
rebound after a crash the tilt loses, as CA-001-01's did in 2009. The rule therefore holds, in each
group, the equal-weighted group plus a fraction k of CA-001-01's tilt — k = 1 is CA-001-01, k = 0 the
group held in equal parts — and sets k from the sources' forecasts:

- **The base, panic states** (Daniel and Moskowitz). A group is in a panic state when its market —
  its funds held in equal parts — has lost money over the past 504 sessions, two years, and the
  volatility of its daily returns over the past 126 sessions is above its own average up to then:
  the bear-market indicator and the high market volatility whose interaction forecasts the crashes.
  In a panic state the group's tilt is off, k = 0; otherwise, and while the group has not yet 504
  sessions of history, it is held in full, k = 1: without a forecast, the rule is CA-001-01's. The
  group's market is the average of the daily returns of its funds trading on each session, chained,
  so that a fund joining the group joins its market on the day it starts to trade. The volatility is
  the standard deviation of those returns, not their variance as in the sources, since only its rank
  against its own past matters, and its average runs over all sessions up to then, expanding, as the
  sources' forecasts use all the data available at each date. The sources'
  dynamic weight is continuous; long only, it cannot go beyond the full tilt or below none, and the
  switch keeps the part of it that matters to a long-only book: stepping aside when crashes are
  forecast. Daniel and Moskowitz compute the indicator for each asset class from that class's own
  market, as this card does for each group.
- **The variant, constant volatility** (Barroso and Santa-Clara). Each group's tilt is scaled by the
  inverse of its own volatility: k is the average of the tilt's past 126-session volatilities, up to
  then, divided by the current one, and at most 1. The tilt's volatility is that of its realised
  daily returns as the unmanaged rule held it — its weights less the group's equal weights, times
  the funds' returns — Barroso and Santa-Clara's form, which scales momentum by the volatility of
  momentum's own returns. The bear window plays no part. The tilt is cut when its own risk rises, and
  never levered: the cap at 1 keeps the scaled tilt at or below CA-001-01's, so that in calm times,
  when the sources would lever momentum up, this variant cannot, and its gain can only come from
  cutting risk. That biases it against the theory, and the verdict will say so. Scaling to the
  tilt's own average, not to a fixed target, keeps the tilt at its usual size in ordinary times: the
  sources' 12% target is set for a long-short portfolio of stocks, a scale this tilt does not share.
- **Everything else is CA-001-01's**: the ranking by the return from 252 to 21 sessions before the
  session before, the top third of each group's ranked funds, each group at its share of the
  portfolio, a fund not yet ranked held at its benchmark weight, the targets on the first session of
  each month, from closes up to the session before. The portfolio is always fully invested.

Two variants, not three.

## What the battery judges, and what to expect

The benchmark holds the nineteen funds in equal parts: the alpha is what the managed tilt adds, the
same comparison as CA-001-01's.

**The size predicted.** In the sources' index futures and commodities, scaling momentum to a
constant volatility raised its Sharpe ratio by about 0.1 (0.71 to 0.80, 0.59 to 0.69); the dynamic
figures are higher but use the whole sample. The long-only tilt is a weaker instrument: it cannot hold
the losers short, whose rebound is the crash, so it both loses less in a crash and gains less from
managing it; and the sector funds carry most of its weight, eleven of nineteen funds, where the
sources give no figure. CA-001-01's appraisal ratio was 0.03 with an alpha of 0.20% a year. The card
predicts an appraisal ratio of 0.05 to 0.2 for the base, an alpha about 0.3 to 1% a year above
CA-001-01's, and a positive alpha in the block where CA-001-01's was most negative, 2008–09.

**What the battery can and cannot say.** Gates 2 to 4 judge the managed rule against the funds held
in equal parts and against the whole registry; at the predicted size, a rule this close to CA-001-01
is unlikely to pass them whether or not the theory holds. The verdict therefore rests on the
difference from CA-001-01's alpha over the same sessions, as the refutation clause states. Gate 2
computes the alpha the same way under the battery's versions 1 and 2, so the two figures compare.
The noise of that difference: CA-001-01's tilt had a residual volatility of about 6% a year, and
the managed rule departs from it only in the months a group is in a panic state, perhaps a tenth to
a fifth of them; the difference's volatility is then about 2–3% a year, and its standard error over
17 years about 0.5–0.6% a year. A band of 0.5% is one standard error: inside it, nothing is proven.
The lower half of the predicted gain, 0.3 to 0.5% a year, lies inside the band: the test can
confirm only a gain in the upper half of the prediction, and a smaller true gain would read as
not proven.

**The test's power.** The crash states are few. The two-year bear indicator turns negative late in a
decline — from about October 2008 for the equity groups — so the switch misses the crash's first
year and, in the months it holds, also gives up the tilt's gains in the crash's last legs, before
the rebound of 2009. Other panic states are likely brief: in 2020, and in 2022 for some groups. Gate 3's placebos, which shift the
strategy's own weights in time, judge mostly the momentum selection, which CA-001-01 already found
no better than chance; a managed rule that differs from it in a handful of months may beat no more
of them. A real improvement concentrated in 2009 is what the sources predict, and what gate 5's test
without the best year may reject — though the best year is likely still 2022, as it was for
CA-001-01. At gate 4 the two rules are near clones: the registry's effective trials will count them
as barely more than one. The verdict will say how many months each group spent in a panic state, how
many group-months each neighbour of the windows changes, and what the tests could detect.

## Choices, and the options rejected

- **A continuous dynamic weight**, from the sources' regression of momentum's returns on the
  indicator: its coefficients are estimated on the sources' data, not the lab's, and the long-only
  bounds would clip most of its range.
- **One market indicator for all groups** (SPY): the sources compute it per asset class; a
  commodity crash is not a US equity crash.
- **A fixed volatility target**, as Barroso and Santa-Clara's 12%: set for long-short stock momentum.
- **Cash instead of the group in equal parts** when the tilt is off: that would add a market-timing
  bet the theory does not make.

## Implementation

Long only, fully invested, nineteen funds, each with a European (UCITS) fund or an exchange-traded
commodity that tracks it, rebalanced monthly on closes with the orders filled at the next close: the
signals read the session before, so a day of delay is built in, and gate 6 adds another.
