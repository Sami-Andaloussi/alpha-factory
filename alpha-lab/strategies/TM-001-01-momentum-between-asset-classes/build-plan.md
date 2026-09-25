# TM-001-01 — Build plan

The card is locked (`card: TM-001-01-momentum-between-asset-classes`). One function,
`positions(market, lookback, skip, top)`, in four steps, each commented in `strategy.py` by its
number.

1. **The ranking return**: for each asset, the close `1 + skip` sessions before the target over the
   close `1 + lookback` sessions before it, less one, on `market.signal_prices` — CA-001-01's
   window, which ends `skip` sessions before the session before and starts `lookback` sessions
   before it, so that a target never reads its own session's close, whatever the skip.
2. **Who is ranked**: an asset trading on the target's session and on the window's first session
   (`market.tradable`, shifted by `1 + lookback`), with a return over the window.
3. **The leaders**: the ranked assets ordered by their ranking return, highest first, ties to the
   asset listed first in the market's columns (`rank(method="first")`); the `top` first are held,
   or all those ranked when fewer, in equal parts, the weights adding up to one whenever an asset
   is ranked; every other asset holds nothing.
4. **Monthly**: the targets of the first session of each month on which an asset is ranked, NaN
   elsewhere, so that the positions drift with prices between two first sessions. Every row with a
   target names every asset, so an asset that leaves the leaders is sold.

Why in this order: step 1 is the signal, step 2 who may be chosen, step 3 the choice and its
weights, step 4 the rebalancing the card states. Nothing is estimated, and nothing reads beyond the
session before. Before the run, by `python -m lab.report --try`, gate 1's timing and ten dates for
a neighbour.
