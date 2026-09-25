# TM-002-01 — Build plan

One function, `positions(market, high_window, hold)`, in five steps, each commented in `strategy.py`
by its number. It is TM-003-01's, the ranking measure and the ties apart.

1. **The nearness**: on `market.signal_prices`, the close of the session before over the highest of
   the `high_window` closes up to it, the session before included; 1 when that close is the high. A
   fund with fewer than `high_window` closes has none: prices are missing before a fund's first
   session.
2. **Ranked**: a fund trading on the session (`market.tradable`) with a nearness.
3. **The tranche** of each first session of a month on which a fund is ranked: the three ranked
   funds nearest their high, together with any fund tied with the third (a rank by the minimum, kept
   at 3 or less), or all of them if fewer are ranked; its funds in equal parts.
4. **The portfolio**: on each such session, the tranches of the last `hold` months, the current one
   included, or those formed so far before `hold` exist, each keeping only its funds trading on the
   session, which share its part equally; the tranches share the portfolio equally.
5. **Monthly**: the targets of those sessions, NaN elsewhere, every fund named, so that a fund no
   longer held is sold and the holdings drift with prices between targets.

Why in this order: steps 1 and 2 are the signal, step 3 the source's top 30% as three funds, step 4
its overlapping holding, step 5 the pace. Nothing reads beyond the session before.
