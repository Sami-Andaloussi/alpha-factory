# TM-003-01 — Build plan

One function, `positions(market, lookback, hold)`, in five steps, each commented in `strategy.py` by
its number.

1. **The ranking return**: on `market.signal_prices`, the close of the session before over the close
   `lookback` sessions before it, less one. A fund without that earlier close has none: prices are
   missing before a fund's first session.
2. **Ranked**: a fund trading on the session (`market.tradable`) with a ranking return.
3. **The tranche** of each first session of a month on which a fund is ranked: the three ranked
   funds with the highest returns, or all of them if fewer are ranked; the funds are sorted
   alphabetically first, so that a tie goes to the fund first in alphabetical order.
4. **The portfolio**: on each such session, the tranches of the last `hold` months, the current one
   included, or those formed so far before `hold` exist, each keeping only its funds trading on the
   session, which share its part equally; the tranches share the portfolio equally. A tranche
   left with no fund trading would drop out and the others share the portfolio; no fund of the
   universe stops trading, so this only matters under gate 6's tests.
5. **Monthly**: the targets of those sessions, NaN elsewhere, every fund named, so that a fund no
   longer held is sold and the holdings drift with prices between targets.

Why in this order: steps 1 and 2 are the signal, step 3 the source's three winners, step 4 its
overlapping holding, step 5 the pace. Nothing reads beyond the session before.
