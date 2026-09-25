# CA-014-01 — Build plan

One function, `positions(market, average, legs)`, in four steps, each commented in `strategy.py` by
its number.

1. **The ratio and its trend**: DBC's close over IEF's on the session before, from
   `market.signal_prices`, whether or not either trades; its mean over the last `average` sessions
   up to the session before, requiring all of them; rising when the ratio is above the mean. The
   trend is known once the mean exists.
2. **The side**: under `legs` "all", XLE, XLB, GLD and DBC while the ratio rises, XLP, XLV, XLF, XLU
   and IEF otherwise; under "stocks", XLE and XLB, or XLP, XLV, XLF and XLU. A fund of the card not
   in the market is skipped; a fund that does not trade on the session is not held. Any other `legs`
   is refused.
3. **The weights**: the funds held share the portfolio equally; none held, every weight is zero.
4. **Weekly**: the targets of the first session of each week, from the first week whose session
   before has the mean, NaN elsewhere, every fund named, so that the other side is sold at a switch
   and the holdings drift with prices within the week.

Why in this order: step 1 is the signal, step 2 the source's two sides, step 3 the portfolio, step 4
the pace. Nothing reads beyond the session before.
