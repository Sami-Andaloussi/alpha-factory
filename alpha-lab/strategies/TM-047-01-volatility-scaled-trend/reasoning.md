# TM-047-01 — Trend with positions scaled by volatility: reasoning

## Why this theory now

TM-047 claims that the same momentum rule earns a higher Sharpe ratio when each position is sized by
the inverse of its asset's recent volatility: each position then carries about the same risk, and
the portfolio takes less risk when volatility is high — when momentum suffers its worst drawdowns —
and more when it is low. It is, as the theory says, an implementation mechanism rather than a theory
of the market, and its test is a comparison: the scaled rule against the same rule unscaled.

The lab already holds the unscaled rule. TM-017-01 holds SPY, EFA, EEM, IEF, TLT, GLD and DBC, each
in an equal seventh while its past year beats the Treasury bill, decided monthly; it reached gate 3
with a Sharpe ratio of 0.495 in-sample, against 0.41 for the seven held always, and one asset, SPY,
carried a third of its profit. This card keeps everything of that rule but the size of each
position, so that what the battery finds, set beside TM-017-01, is what the scaling adds.

The bank's neighbours: **TM-017**, the trend itself, unscaled; **TM-024**, momentum crashes, which
scales a momentum portfolio by forecasts of its own crash risk; **TM-018**, trend as crisis alpha.
Each is a card of its own.

## From the mechanism to a signal

- **The trend** is TM-017-01's, unchanged: an asset is in trend when its return over the past 252
  sessions, read up to the session before, beats the Treasury bill's over the same sessions; out of
  trend, its share stays in cash. The sources' trend rules differ (Clenow's crossing of moving
  averages, Carver's EWMAC), but changing the trend rule too would leave the comparison without
  meaning.
- **The size** is the managed-futures rule the theory names: each position is set so that one
  day's typical move costs the portfolio the same fraction of its value. Clenow's core system aims at
  a daily impact of 20 basis points per position, measured by a 100-day average true range. The lab
  has closes, not highs and lows, so the daily volatility is the standard deviation of the asset's
  daily returns over the past 100 sessions, read up to the session before. A day's range is wider
  than its standard deviation: for a random walk, the expected range between high and low is
  √(8/π), about 1.6, standard deviations (Parkinson, 1980), and the true range is wider still. So
  Clenow's 20 basis points of range become 0.002 × √(π/8), about 0.00125, of standard deviation: a
  position's weight is 0.00125 divided by its daily volatility. With typical daily volatilities —
  about 1.2% for US equities, 0.45% for intermediate Treasuries, 1.8% for emerging markets — that is
  some 10%, 28% and 7%; the seven together add up to about 0.9 when all are in trend in a calm
  market.
- **Re-scaled every month**: Clenow sizes a position when it opens; re-scaling every position each
  month to its current volatility is Moreira and Muir's construction, which scales by the volatility
  of the month before.
- **No leverage**: when the weights of the assets in trend add up to more than one, all are cut in
  the same proportion until they add up to one, which keeps their risks equal. Moreira and Muir
  (2017) cap the weights of their volatility-managed market portfolio at one, a hard no-leverage
  constraint, and find the same Sharpe ratio as without the cap (0.52, Table 5): the scaling's gain
  survives a long-only, unlevered book. While the cap binds, though, the portfolio is fully invested
  whatever the level of volatility, and the scaling only moves weight between assets; exposure falls
  with volatility only once the weights add up to less than one. With 0.00125, that is most months:
  the seven add up to about 0.9 in a calm market, and less as volatility rises or assets leave the
  trend. The value of `risk` sets how often the cap binds, and so how much of the timing is kept.
- **Monthly**: the weights are set on the first session of each month, as TM-017-01's, so that both
  rules trade on the same days.

**The variant** measures volatility over the past 21 sessions instead of 100: Moreira and Muir scale
each portfolio by its realized volatility of the preceding month, a faster estimate that cuts
exposure sooner when volatility rises and restores it sooner. Two variants, not three: each is a
trial every later card pays for.

## What the battery judges, and what to expect

The benchmark holds the seven assets in equal parts, set back to equal parts whenever the strategy
trades: the alpha is what the trend and the scaling together add to holding the seven always. The
theory's own claim is judged beside TM-017-01, run on the same assets, years and days: the verdict
compares the two.

**The size predicted.** Moreira and Muir give the gain of a scaled portfolio over the unscaled one as
its appraisal ratio against it: the new Sharpe ratio is the square root of the old one squared plus
that appraisal ratio squared. They find an appraisal ratio of 0.875 for the scaled momentum factor
and 0.34 for the scaled market, 1926 to 2015, and 0.30 for the market scaled without leverage (Table
5). A long-only, unlevered trend rule on seven funds is closer to the capped market than to a
long-short factor; with 0.30, the unscaled rule's 0.495 becomes about 0.58. The card predicts a
Sharpe ratio of about 0.58 in-sample, above TM-017-01's 0.495, and a positive alpha over the seven
held always.

**What each figure can tell.** The scaling does two things at once. It tilts the portfolio for good
toward the calmest assets, the bonds, whose weights rise from two sevenths to about half of what is
invested; and it times the exposure, cutting it when volatility rises. Moreira and Muir scale a whole
portfolio and test the timing alone; scaling asset by asset mixes the two. A Sharpe ratio above
TM-017-01's, and an alpha over an equal-weight benchmark heavy in equities, could come from the tilt
alone. Gate 3 is the test of the timing: its placebos hold the strategy's own weights shifted in time
by a year or more, and so keep its average tilt toward the bonds; beating them means the scaling's
timing, not its tilt, adds. The verdict compares its rank among placebos with TM-017-01's 81.7%.

**The comparison's power.** The two rules trade the same assets on the same days and will move
together closely; over about seventeen years, the difference between their Sharpe ratios is known to
about ±0.1. The predicted gain, 0.08, is within that: the refutation therefore counts as refuted
only a Sharpe ratio more than 0.1 below TM-017-01's, and a difference within 0.1 either way as not
proven. If the strategy passes gates 1 to 7 with a Sharpe ratio at or below 0.495, it passes as a
strategy, and the theory's comparative claim is not proven by it.

**The test's power.** Seven assets and a monthly decision gave TM-017-01 too few independent trends
for gate 3: 117 clustered decisions, 81.7% of its placebos beaten. The scaling changes the weights
every month, so this rule will count more decisions, but not more independent trends: gate 3 may
again judge the timing of seven assets too few to tell from luck. The verdict will say so if it
happens, and whether the scaled rule does better than the unscaled one at that gate.

**Risks the scaling brings.** IEF and TLT together will hold about 45% of what is invested when all
seven are in trend. Gate 6 judges each asset's share of the profit, not of the capital, and equal risk
tends to even out the shares of profit; but its limit of 30% on one asset, and its test without the
bond cluster, may fall where TM-017-01's fell on SPY. The neighbours of `risk` test little: while the
cap does not bind, moving `risk` scales every weight and the cash together, and leaves the Sharpe
ratio unchanged, cash earning the bill; they differ from the base only through the months when the
cap binds.

## Choices, and the options rejected

- **The universe** is TM-017-01's, for the comparison. The sources' portfolios hold dozens of
  futures across all classes; the lab has seven distinct markets for these classes, and QQQ, IWM and
  SLV would repeat SPY and GLD. **SHY** is left out: its volatility is a fifth of the others', so the
  scaling would put most of the portfolio in a fund that barely beats cash. **Bitcoin** is not one of
  the theory's classes.
- **Scaling by variance** rather than volatility, as Moreira and Muir's baseline does: they report
  that volatility gives weights far less extreme with about the same Sharpe ratio, and the managed-
  futures rule the theory names sizes by volatility.
- **A target for the whole portfolio's volatility**, estimated from the covariance of the assets:
  it adds an estimate of correlations and a target, two choices the sources make differently; the
  equal daily impact per position is the theory's stated rule.
- **Leverage** to raise exposure when volatility is low: the lab is long only and unlevered; the
  cap at one keeps the half of the timing that cuts risk, and gives up the half that adds it.
- **Weekly or daily rebalancing**, as managed futures often trade: monthly keeps the comparison
  with TM-017-01 exact.

## Implementation

Long only, never levered, seven funds, each with a European (UCITS) fund or an exchange-traded
commodity that tracks it, rebalanced monthly on closes with the orders filled at the next close: the
signal and the volatility read the session before, so a day of delay is built in, and gate 6 adds
another.
