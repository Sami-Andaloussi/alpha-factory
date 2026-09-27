# CA-014-02 — Build plan

One function, `positions(market, average, legs)`, in four steps, each commented in `strategy.py` by
its number.

1. **The dollar and its trend**: USDCHF over EURCHF from `market.signal_rates`, each already the
   close of the last day before the session, so read on the session itself without a further shift;
   a market without rates is refused. Its mean over the last `average` sessions up to and including
   the session, over the readings that exist, when at least nine tenths of them exist (180 of 200);
   falling when the reading is below the mean. The trend is known on a session with a reading and a
   mean.
2. **The side**: under `legs` "all", XLE, XLB, GLD and DBC while the dollar falls, XLP, XLV, XLF, XLU
   and IEF otherwise; under "classes", GLD and DBC, or IEF. A fund of the card not in the market is
   skipped; a fund that does not trade on the session is not held. Any other `legs` is refused.
3. **The weights**: the funds held share the portfolio equally; none held, every weight is zero.
4. **Weekly**: the targets of the first session of each week on which the trend is known, NaN
   elsewhere, every fund named, so that the other side is sold at a switch and the holdings drift
   with prices within the week; a first session without a reading (EURCHF's gap of August 2008) sets
   no target, and the portfolio holds.

Why in this order: step 1 is the signal, step 2 the source's two sides, step 3 the portfolio, step 4
the pace. Nothing reads a rate later than the close of the day before the session.
