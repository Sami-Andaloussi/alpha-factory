# TM-047-02 — Equities managed by their own volatility: reasoning

## Why this theory now

TM-047 claims that momentum and risk-premium strategies scaled by volatility earn higher Sharpe
ratios than unscaled ones (Moreira and Muir, 2017; Carver, 2015; Clenow, 2023), and that momentum is
better rewarded when volatility is low. Its first card, TM-047-01, sized each position of
TM-017-01's trend rule by the inverse of its asset's volatility: a Sharpe ratio of 0.58 against the
unscaled rule's 0.495, which the battery could not tell from luck (83.9% of its placebos beaten),
and which a check apart from the battery traced to the tilt the scaling gives toward the calm
assets, not to its timing — an appraisal ratio of 0.02 (t 0.06) against the same rule at fixed
weights. Its verdict named the form it left untested: "Moreira and Muir's scaling of a whole
portfolio by its own recent volatility, capped at full investment". TM-047 was then recorded
tested-inconclusive. TM-035's reader, judging procyclical leverage not testable, found that form
signed by the library, claimed by TM-047's prediction and read by no verdict; TM-047 was reopened
for it, and this card draws it. It is a different form, not a changed hypothesis: `parent` is null.

**Its sources.**

- **Moreira and Muir** (2017), a paper the library cites (Ilmanen, Box 13.1, note 15; Campbell,
  *Financial Decisions and Markets*, among the studies that reject an equity premium proportional to
  variance) but does not hold; its figures here are TM-047-01's, which the library cannot confirm: a
  portfolio scaled each month by the inverse of its realized variance of the month before, its
  average exposure set to match the unscaled portfolio's volatility, earns an appraisal ratio
  against the unscaled one of 0.34 for the market, 1926 to 2015, and 0.30 with its weights capped at
  one, a hard no-leverage constraint, with a Sharpe ratio of 0.52 (their table 5); scaling by
  volatility rather than variance gives weights far less extreme with about the same Sharpe ratio.
- **Ang** (*Asset Management*, 2014, chapter 8, section 6, pp. 266–270): aggregate market volatility
  is "quite predictable" — the correlation of GARCH volatility at the start of a month with realized
  volatility over the month is 63%, against barely 5% for forecasts of the equity premium — and
  there is little direct relation between volatility and future returns. A mean-variance weight in
  equities, its numerator held at the sample's mean excess return and its denominator the VIX known
  at the start of each month, its cumulated return from January 1986 to December 2011 ending at
  3.06, against 2.14 for the static 60% equities and 40% bills, both scaled to 10% volatility; it
  moved into bills when the VIX was high and "partly avoided the low returns occurring when
  volatility spiked". Equity weights ranged from more than 1.5 to nearly zero. Ang reports the
  standard deviation of US equities' log returns, 1935 to 2010, at 16.0%.
- **Ilmanen** (*Investing Amid Low Expected Returns*, 2022, Box 13.1, pp. 216–217): volatility
  targeting "may improve the long-run SR compared to a constant-notional strategy. Empirically, it
  seems to work especially for the equity market premium and for momentum and trend strategies"; it
  improves the Sharpe ratio "if short-term expected returns do not rise when volatility rises", one
  month's volatility being autocorrelated at 0.6 to 0.7 with the next's.

**The form this card tests.** The equity market premium — the one the sources sign most clearly —
held in five equity index funds in equal parts, the whole portfolio scaled each month by its own
realized risk of the month before, capped at full investment: the half of the timing that cuts risk
when volatility rises; the half that would lever up when it is low is given up, as the lab is long
only and unlevered, and Moreira and Muir found the cap to keep most of the gain.

## From the claim to a signal

- **The universe**: SPY, QQQ, IWM, EFA and EEM, the lab's equity index funds. The sector funds would
  repeat SPY; the Treasuries, gold and the commodity basket are other premiums, which the sources
  sign less clearly for this timing.
- **The portfolio**: the funds trading on the target's session, in equal parts.
- **Its risk**: the standard deviation of the equal-weight portfolio's daily returns over the last
  `window` sessions to the session before, each day's return the average of the funds' that traded
  it, annualized by √252.
- **The scale**: k = min(1, (target / risk)²) when `scaling` is "variance" — the mean-variance
  weight, whose denominator is the variance, as in Ang's timing, which puts the VIX there, and
  Moreira and Muir's baseline — and min(1, target / risk) when it is "volatility", Ilmanen's
  volatility targeting. The target is 16% a year, Ang's standard deviation of US equities from 1935
  to 2010: a level fixed from the library, not estimated on the lab's data, which spares the rule an
  average over its own history. With it the portfolio is fully invested while its risk is at or
  below the long-run level of US equities, and cut in proportion to the square, or the ratio, of its
  excess.
- **The targets**: on the first session of each month, each fund trading holds k/N, N the funds
  trading, the rest in cash; k is 1 until the window has `window` returns.
- **Parameters**: `window`, 21 sessions, a month of daily returns: Ilmanen's one-month volatilities
  based on daily data, Ang's realized volatility over the month, Moreira and Muir's month;
  neighbours 16 and 26, 10 and 32. `target`, 0.16; neighbours 0.12 and 0.20, 0.08 and 0.24.
  `scaling`, a text naming the variant, with no neighbours.
- **Memory**: 22 sessions, the window and the close before its first return.

## What the battery judges, and what to expect

The benchmark holds the five funds in equal parts, set back to equal parts whenever the rule trades:
the unscaled portfolio. Its alpha is Moreira and Muir's test, the scaled portfolio against the
unscaled one.

**The size predicted — a judgment.** Moreira and Muir's capped market earned an appraisal ratio of
0.30 over 1926 to 2015; Ang's timed equities gained, by the lab's estimate from the figure's end
values read as wealth, about 1.4% a year over the static mix at 10% volatility over 1986 to 2011. On
five funds with the target at US equities' long-run level, below the funds' own, the cap binds in
calm months and the scale works only in turbulent ones, and TM-047-01 found the timing on the lab's
funds worth an appraisal ratio of 0.02 inside a trend rule. The card judges the rule's alpha over
the five funds held always at about +0.3 to +2% a year, an appraisal ratio of about 0.05 to 0.35,
and its Sharpe ratio above theirs; the rule is out of equities in part in many months: the five
funds' daily volatility over the in-sample years, 1.38% (SC-017-01), about 22% a year, lies a third
above the target, so the scale is below one whenever a month is not calm; how often is a count the
verdict reports.

**The gates.** A rule that moves one scale over five funds that move together has few independent
decisions: gate 3's placebos, the same weights shifted in time, keep its average exposure, and beat
it unless the timing itself earns; the card expects it to fail gate 3 or gate 4 (an appraisal ratio
of about 0.6 is expected by luck from the best of the lab's effective trials), and gate 2 if its
alpha falls short of zero after costs. Gate 6's test without a cluster does not run: the five funds
are one cluster. Gate 1 counts a decision only when the targets change: months at k = 1 repeat the
equal parts and count none, so its count is one plus the months in which k moves; with the five
funds' volatility above the target on average, more than thirty is likely, a count that depends on
the prices. Gate 2 asks 0.4, where the five held always stand (0.3951 set back monthly, SC-002-01;
0.40, SC-018-01). Gate 6's 30% limit is likely to fail on QQQ: rules close to the five in equal
parts gave it 32 to 34% of the profit (SC-002-01, SC-010-02, SC-016-01, SC-017-01), and SC-002-01
found a monthly equal weight of the five fails on QQQ whatever the rule's bet.

**The clause.** Judged before costs, on the market's closes, over the in-sample months from the
first target on which the window has 21 returns, the first session of March 2005 (the first of
February reads 19), to December 2022, the last month ending at the close of 2022-12-30, each month
from the close of a target's session to the close of the next: the rule's monthly return less the
bill's, regressed by ordinary least squares on the monthly return less the bill's of the five funds
held in equal parts from the same closes, with standard errors robust to heteroskedasticity; the
intercept's t statistic computed apart from the battery. The theory is refuted in this form if the t
statistic is −0.35 or below: the equity premium managed by its own volatility no better than held
always. Between, short of passing gates 1 to 7, not proven, not refuted; a base that passes gates 1
to 7 while the clause refutes leaves the theory refuted in this form. The intercept is Moreira and
Muir's reading of a higher Sharpe ratio: the scaled and unscaled portfolios together reach √(SR² +
AR²). A positive intercept from a beta, set by the turbulent months, below the average scale is the
theory's claim — the premium not rising with volatility — not an artefact, unlike SC-019-01's rule,
whose same gain was not its theory's. The alpha at a beta equal to the average scale, reported,
isolates the returns' own timing, which the theory does not claim. The rule's Sharpe ratio against
the five's is reported; a positive alpha with a Sharpe ratio below theirs leaves the clause's
reading, and the verdict says so.

**The test's power.** 214 months, counted from the calendar, 17.8 years; the appraisal ratio's
standard error is about 1/√17.8, 0.24. At the predicted middle, 0.2, the t statistic's expectation
is about 0.85: the clause refutes about 36% of the time with no effect and about 11% at 0.2, 5% at
0.3. The test can barely tell the predicted gain from none.

**What was published, and what it tells.** TM-047-01's appraisal ratio of 0.02 (t 0.06) for the
timing, on SPY, EFA and EEM among its seven funds inside a trend rule, was known when this card was
drawn and lowers its prediction; its verdict also found the per-asset scaling worse than the
unscaled rule in 2018 and 2020 (SPY at 23% and 25% into February and October 2018, near 4% through
the 2020 rebound). TM-024-01 published its equity group's panic months — the group's market down
over two years and its volatility above its own average: October 2008 to September 2009, August and
September 2010, April and May 2020, and October 2022 — and two of the group's monthly returns in
them (the equity markets rose 11.3% in September 2010 and 5.4% in October 2022); over the months in
which any of its groups was in panic, the nineteen funds held in equal parts earned 27.4% a year
against 5.8% in the others: the market rose most in the months after its turbulent falls, the
opposite of what this rule needs. Its variant, the momentum tilt scaled by the inverse of its own
volatility, added 0.18% a year of alpha over the unscaled tilt (t +0.54), its gains before hedging
mostly in 2008–09. SC-019-01, on these five funds, published an alpha of 1.69% a year over the five
held always for a rule that happened to be out of the funds in the most volatile years — its beta,
0.33, below its average share invested, 0.52; 0.03% at a beta equal to that share — and the US
funds' returns year by year, 2008 −31.7% and 2009 +46.2% from February to December among them.
SC-017-01 published the five funds' daily volatility over the in-sample years, 1.38%, about 22% a
year. TM-018-01 published SPY's crisis months, on the trend's edge; MR-032-01 the weekly reversal in
2008 and 2020. None published this rule's contrast, its scale against the five funds' next month:
the outcomes published are of other quantities (the tilt, the trend, a January rule), of the
nineteen funds pooled over every group's panic months, or of two single months. As RUNBOOK step 3
reads TM-023-01's case, these months stay in the graded sample, disclosed: the graded quantity was
not published on them, and leaving out the equity panic months would remove the months in which the
rule acts most, 2008–09 among them. Read literally, the two months whose returns were published
would leave; the clause without TM-024-01's equity panic months, which hold them, is reported, and
the verdict says whether the two versions agree.

**TM-047's refutations, and what the card can grade.**

1. *Momentum no more strongly rewarded when volatility is low than when it is high*, and 2.
   *momentum drawdowns that do not cluster when volatility is high*: momentum's, read in their
   panic-state form by TM-024-01 and TM-006-01; this card holds no momentum and does not grade them.
3. *Volatility-scaled momentum, risk-premium and trend strategies with Sharpe ratios no higher than
   their unscaled versions*: graded in its risk-premium form, the equity premium, by the clause; its
   trend form read by TM-047-01.

**Measures stated before the run**, reported, not graded:

- the variant, scaled by volatility: the same regression;
- the Sharpe ratios of the rule, the variant and the five funds held always, before costs;
- the share of months in which the scale is below one, the average scale, and the base's alpha at a
  beta equal to its average scale;
- the clause over the months of 2005 to 2013, over those of 2014 to 2022, over the in-sample months
  without 2008 and 2009, without TM-024-01's equity panic months, and over the holdout, 2023 to
  2025;
- the same regression for SPY alone, managed by its own risk, as the sources' market;
- the rule's alpha before and after costs, and the neighbours' and the one-day-late rule's alphas
  and appraisal ratios.

## What was considered, and why each is set aside

- **The VIX**, Ang's volatility: the lab does not hold it; the realized volatility of the month
  before is Moreira and Muir's measure, and volatility is forecast well from its own past (Ang).
- **A target estimated on the lab's history**, as Moreira and Muir's constant is set over their
  whole sample: it would read the future, or, bounded to a trailing window, add a parameter the
  sources do not give; Ang's long-run 16% is fixed from the library.
- **Leverage** when volatility is low: the lab is long only and unlevered.
- **The seven funds of TM-047-01, bonds and commodities included**: the sources sign the timing most
  clearly on the equity premium; a mixed portfolio would add the tilt between classes TM-047-01
  found to carry its gain.
- **Each fund scaled by its own volatility**: TM-047-01's construction, which mixes a tilt with the
  timing; the whole portfolio scaled as one keeps the timing alone.
- **The sector funds**: they repeat SPY.

## Implementation

Long only, the five equity index funds, with European (UCITS) funds that track them; one decision a
month, the risk read up to the session before and traded at the close, a day's delay; the whole
portfolio scaled by one number.
