# TM-047-01 — Build plan

One function, `positions(market, risk, vol_window)`, in five steps, each commented in `strategy.py`
by its number. Steps 1, 2 and the in-trend test of step 3 are TM-017-01's, unchanged, with its
lookback of 252 sessions, so that the two rules differ only by the size of each position.

1. **The asset's past return**: the close of the session before over the close 252 sessions
   earlier, less one, on `market.signal_prices`.
2. **The bill's return over the same sessions**: `market.rf` compounded, over the same sessions.
3. **In trend**: an asset whose past return beats the bill's and that trades on the session.
4. **The size**: the asset's daily volatility is the standard deviation of its daily returns over
   the `vol_window` sessions up to the session before; an asset in trend with a volatility gets
   `risk` divided by it, every other asset nothing. When the weights add up to more than one, each is
   divided by their sum, so that they add up to one and keep their ratios.
5. **Monthly**: the targets of the first session of each month, NaN elsewhere, so that positions
   drift with prices between two first sessions; every row with a target names every asset, so an
   asset that leaves the trend is sold.

Why in this order: steps 1 to 3 are the unscaled rule, step 4 the scaling the card tests, step 5
the pace both rules share. Nothing reads beyond the session before.
