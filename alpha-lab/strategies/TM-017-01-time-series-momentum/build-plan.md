# TM-017-01 — Build plan

One function, `positions(market, lookback)`, in four steps, each commented in `strategy.py` by its
number.

1. **The asset's past return**: the close of the session before over the close `lookback` sessions
   earlier, less one, on `market.signal_prices`. Read up to the session before, so that a target
   set on a session never reads that session's close.
2. **The bill's return over the same sessions**: `market.rf` compounded, taken over the same
   sessions as step 1.
3. **In trend**: an asset whose past return beats the bill's and that trades on the session
   (`market.tradable`). An asset without a full lookback of prices has no past return and is not in
   trend. Each asset in trend gets one share of the portfolio, the number of assets the market
   holds giving the share: a seventh on the card's universe, and a larger share on the smaller
   markets gate 6 hands it; the rest is cash.
4. **Monthly**: the targets of the first session of each month, NaN elsewhere, so that the
   positions are held, drifting with prices, between two first sessions. Every row with a target
   names every asset, so an asset out of trend is sold.

Why in this order: steps 1 and 2 are the signal, step 3 turns it into weights, step 4 is the
rebalancing the card states. Nothing is estimated and nothing reads beyond the session before.
