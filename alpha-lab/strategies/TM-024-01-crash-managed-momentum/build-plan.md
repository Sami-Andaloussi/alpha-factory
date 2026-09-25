# TM-024-01 — Build plan

One function, `positions(market, rule, vol_window, bear_window)`, in six steps, each commented in
`strategy.py` by its number.

1. **CA-001-01's weights**, its rule unchanged, lookback 252 and skip 21 as constants: in each
   group, the top third of the ranked funds, rounded, one at least, share the group's n/N; a fund
   trading but not yet ranked holds 1/N. Computed every session from `market.signal_prices` up to
   the session before; the targets start, as CA-001-01's, on the first month in which a fund is
   ranked.
2. **The neutral weights and the tilts**: 1/N for each of the N funds trading
   (`market.tradable`); each group's tilt is CA-001-01's weights on its funds less those. A tilt
   sums to zero within its group.
3. **Each fund's daily return**: the close over the close before, less one, on the signal prices.
4. **k under "panic"**: each group's market return is the average of the daily returns of its
   funds trading that session, NaN when none does; its level is that return compounded, from its
   first session. The group is in a panic state when its level at the session before is below its
   level `bear_window` sessions earlier, and the standard deviation of its returns over the
   `vol_window` sessions up to the session before is above the average of that standard deviation
   over all sessions up to then. k is 0 in a panic state, 1 otherwise, and 1 while either measure
   is missing.
5. **k under "scale"**: each group's unmanaged tilt return on a session is the tilt set on the last
   first session of a month before it, as held from that session's close, times the funds' returns
   of the session, summed over the group; NaN before the first target. Its standard deviation over
   `vol_window` sessions, read up to the session before, is σ; k is the average of σ over all
   sessions up to then, divided by σ, at most 1, and 1 where σ is missing or zero. `bear_window`
   is not read.
6. **The targets**: the neutral weights plus each group's k times its tilt, on the first session of
   each month in which a fund is ranked, NaN elsewhere, every fund named. Any other rule, or a fund
   in no group, is refused.

Why in this order: steps 1 and 2 rebuild CA-001-01 and split it into what is held anyway and what is
bet; steps 3 to 5 are the two ways the card sets how much of the bet is held; step 6 is CA-001-01's
pace. Nothing reads beyond the session before. Under gate 6's cluster left out, the funds of that
cluster do not trade: they leave N, the neutral weights, the tilts and the group markets, and their
prices are read by nothing but their own ranking.
