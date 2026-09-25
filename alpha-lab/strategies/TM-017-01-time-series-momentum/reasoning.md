# TM-017-01 — Time-series momentum in its plainest form: reasoning

## Why this theory now

Time-series momentum is the simplest theory of the bank that the lab's data can test in the form
its sources state: one signal per asset, the asset's own past return, with no ranking against other
assets, no estimate and no model. It is also the most documented: Moskowitz, Ooi and Pedersen find
it on 58 futures and forwards over 25 years, and Hurst, Ooi and Pedersen over a century. Taken first
and plainest, what the battery finds is about the idea, not about choices layered on it.

The bank holds its neighbours. TM-001, cross-sectional momentum, ranks assets against each other;
this one never compares two assets. TM-018, market divergence and crisis alpha, explains when trends
pay and measures them against volatility; this one takes the plain sign of the past return. TM-047,
volatility-targeted momentum, scales each position by its risk; this one holds equal shares. Each is
a card of its own, later.

## From the mechanism to a signal

The theory says that an asset keeps moving in the direction of its own past return over an
intermediate horizon, because information spreads slowly, institutional capital reallocates
slowly, and trend followers add to the move once it is seen. Its standard form holds an asset whose
past 12-month return is positive and sells short one whose return is negative. The lab is long
only: an asset whose trend is down is not sold short but left, its share kept in cash, which earns
the Treasury bill. This long-only form is what Antonacci calls absolute momentum, and it keeps the
theory's prediction: the trend's sign says when to hold.

- **The signal** is the asset's return over the lookback in excess of the Treasury bill over the
  same sessions: Moskowitz, Ooi and Pedersen take the sign of the excess return, and a trend that
  earns less than cash is no reason to hold an asset instead of cash.
- **The lookback** is 252 sessions, twelve months, the theory's standard form. The second variant
  is 126 sessions, six months, inside the three to six months the sources give as the empirical
  optimum. Two variants, not three: each variant is a trial every later card pays for.
- **The universe** holds the theory's classes wherever the lab has them: equity indices (SPY, EFA,
  EEM), Treasury bonds (IEF, TLT) and commodities (GLD, DBC). The sources' point is a diversified
  portfolio of trends, "the repetition of trends across many markets". The lab has no currencies.
- **Equal shares**: each asset in trend holds one seventh of the portfolio; an asset out of trend
  leaves its seventh in cash. This is the plainest portfolio of trends: no volatility estimate, and
  no asset's weight depending on another's trend.
- **Monthly**: the targets are set on the first session of each month, from prices up to the
  session before, the monthly rebalancing of the sources' standard construction.
- **A late asset** is held only once it has a full lookback of prices: DBC trades from February 2006,
  and its share stays in cash until then.

## Options rejected

- **Short positions**: the lab is long only; the short side of the theory is not tested here.
- **Volatility scaling** of each position, as the sources' futures portfolios do: it adds an
  estimate and a parameter, and it is TM-047's hypothesis.
- **The EWMAC crossovers at several speeds**, Carver's implementation: several parameters and a
  combination; a later card may test them against this plain signal.
- **The cash of assets out of trend spread over those in trend**: it would concentrate the
  portfolio in fewer assets as trends fade, a different and more levered bet than the theory's.
- **QQQ and IWM** beside SPY, **SLV** beside GLD, and **SHY**: they repeat an asset already held, and
  SHY's return over cash is too small for its trend to mean anything. **Bitcoin and the sectors**
  are outside the theory's classes.

## What the battery judges

The benchmark holds the same seven assets in equal parts, set back to equal parts whenever the
strategy trades: the strategy's alpha is what its timing adds, holding an asset only while it trends,
to holding it always. The theory predicts that it adds, above all by stepping aside from long
declines.
