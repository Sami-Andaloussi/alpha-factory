---
id: FP-001
title: Order imbalance
family: flows and positioning
mechanism: [microstructure]
asset_classes: [stocks, crypto]
horizon: [intraday, days]
data: [trade and quote data, order book depth]
status: untouched
---

## Mechanism

A net excess of buy orders, or of sell orders, reveals a temporary imbalance between the immediate
demand for liquidity and the capacity of liquidity providers to absorb it. The imbalance can be
observed in two ways: through signed trades (each trade classified as buyer- or seller-initiated),
or through the imbalance of the depth displayed in the limit order book.

The claim is not merely that the price rises when people buy. It is that the composition of the
order flow carries information about future orders, about the arrival of market orders, and about
the likely size of the next price adjustments. The effect persists because order flow is neither
symmetric nor independent over time: a sequence of purchases statistically calls for further
purchases, or forces liquidity providers to revise their quotes. It is not fully arbitraged away
because whoever takes the other side must bear inventory risk, adverse-selection risk, and the risk
of being hit by the rest of the same flow.

In equities, order imbalance is a central channel through which institutional flows and liquidity
needs reach prices. By analogy, in crypto, the equivalent is the imbalance of the order book and the
serial arrival of aggressive orders on the main trading venues. The effect may be weaker when depth
is abundant, when market makers are very well capitalised, or when the imbalance is only local noise
with no continuation. Order imbalance is the elementary building block behind metaorders,
the inventory pressure of intermediaries, and part of stop-loss cascades.

## Prediction

Prices move with the net order imbalance, and the composition of the current order flow carries
information about the orders to come, the arrival of market orders and the likely size of the next
price adjustments: a sequence of purchases statistically calls for further purchases, or forces
liquidity providers to revise their quotes. The effect plays out mainly intraday; it can extend over
a few days when the imbalance reflects a larger execution programme. It concerns individual stocks
and, by analogy, the order books of the main crypto venues.

## What would refute it

- Signed order flow, or order-book depth imbalance, carrying no information about the sign of the
  following orders or about subsequent price changes.
- Purchases and sales arriving independently over time, with no tendency for buys to follow buys or
  sells to follow sells.
- Imbalances followed by no price adjustment even where depth is thin and market makers are thinly
  capitalised.

## References

- Hasbrouck, J. (2007). Empirical Market Microstructure: The Institutions, Economics, and Econometrics of Securities Trading. Oxford University Press. Chap. 5-6, pp. 48-49 and 51-53.
- Cartea, Á., Jaimungal, S. and Penalva, J. (2015). Algorithmic and High-Frequency Trading. Cambridge University Press. Chap. 12, pp. 295-297.
- Bouchaud, J.-P., Bonart, J., Donier, J. and Gould, M. (2018). Trades, Quotes and Prices: Financial Markets Under the Microscope. Cambridge University Press. Chap. 10.3-10.4, pp. 191-193.
