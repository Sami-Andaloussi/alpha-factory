---
id: FP-015
title: Daily rebalancing of leveraged and inverse ETFs
family: flows and positioning
mechanism: [flows, structural]
asset_classes: [equity indices, crypto]
horizon: [intraday]
data: [leveraged and inverse ETF assets, intraday prices, closing volumes]
status: untouched
---

## Mechanism

Leveraged and inverse ETFs must readjust their exposure every day to return to their target
multiple. This creates a mechanical flow, independent of any new fundamental information. After a
market rise, a long leveraged ETF must buy exposure to bring its leverage back up; after a fall, it
must sell. Inverse products must readjust their exposure every day as well, and the aggregate
result is a procyclical flow, often concentrated towards the close, which can amplify moves already
under way when the assets under management are large and volatility is high. Today's price path
mechanically changes the target position for tomorrow, or for the close.

The flow persists because it follows from the design of the product, not from a manager's
judgment. It is not fully arbitraged because the execution window is short, the size of the flows
is often known only imperfectly in real time, and absorbing them requires balance sheet at a moment
when many participants want to trade the same way. In equities the link is most direct for indices
and large baskets; in crypto it can arise through some wrappers, exchange-traded products or
synthetic products.

## Prediction

The daily rebalancing of leveraged and inverse ETFs adds buying after market rises and selling after
falls: an aggregate procyclical flow, often concentrated towards the close, which can amplify the
moves already under way when the assets under management of these products are large and volatility
is high. It concerns equity indices and large baskets and, through some wrappers, exchange-traded
products or synthetic products, crypto assets.

## What would refute it

- No relation between the day's return, scaled by the assets of leveraged and inverse ETFs, and the
  price moves or volumes near the close.
- Rebalancing flows absorbed without any price effect even when the assets of these products are
  large and volatility is high.
- End-of-day moves no more pronounced on days when the required rebalancing is large than on days
  when it is small.

## References

- Madhavan, A. (2016). Exchange-Traded Funds and the New Dynamics of Investing. Oxford University Press. Chap. 16, sections "Rebalancing" and "Impact of Rebalancing Activity", pp. 201-203.
