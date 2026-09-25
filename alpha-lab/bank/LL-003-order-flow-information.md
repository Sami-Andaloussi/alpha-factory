---
id: LL-003
title: Order flow information
family: lead-lag and information diffusion
mechanism: [information, microstructure]
asset_classes: [currencies, stocks, equity indices, bonds, commodities]
horizon: [intraday, days]
data: [signed order flow, tick-by-tick trades and quotes, customer order flows]
status: untouched
---

## Mechanism

Information does not enter a price in one block, nor uniformly: it is aggregated through signed order
flow. Even when the initial information is public, the books explain that how that news should translate
into a price may not be common knowledge; the first investors to act reveal it partially through their
purchases and sales. Market makers, brokers and counterparties do not observe the fundamental state.
They observe orders that mix information with liquidity needs, hedging, rebalancing and strategic order
splitting. Prices therefore adjust sequentially, trade after trade, as the market infers what share of
the flow is informative.

Lyons stresses that in dealer markets the process has two stages. First, clients, funds, hedgers or
better-informed traders interpret the fundamentals; then dealers read that information in the order flow
and adjust their prices. Diffusion is gradual because dealers do not observe all the relevant
information at once, only its trace in transactions, mixed with noise. In currency markets, aggressive
trades that follow informed client flows are an explicit channel of price discovery. The channel matters
most when information is dispersed, private or interpreted in different ways.

This makes order flow a mechanism of non-simultaneous diffusion: the first instrument or participant
that concentrates the informative flow leads, and the others follow. It explains why one market, one
dealer, a futures contract, an ETF or a more liquid asset can receive information before another and
pass it on. By analogy, the mechanism documented in foreign exchange carries over to futures and to
electronic markets.

The effect is not fully arbitraged away because informed orders hide in the noise, orders are spread out
over time, the permanent impact of a trade has to be told apart from temporary inventory or
processing-cost effects, client flows are not transparent, and each intermediary sees only a local
window on aggregate demand.

## Prediction

Prices move in the direction of signed order flow, with a permanent component that reflects the
information the flow carries. The instrument, venue or dealer that concentrates the informative flow
moves first and the others follow. The effect concerns currency and equity markets, over horizons
from trade-by-trade to several days when an institutional order is executed progressively, and it is
documented above all in foreign exchange.

## What would refute it

- Order flow explains price changes no better when information is dispersed, private or interpreted in
  different ways than when it is public and uniformly observable; the theory expects its marginal role
  to shrink in the second case.
- The price impact of signed order flow is entirely temporary: prices revert fully after trades, as pure
  inventory or processing-cost effects would imply, with no permanent component.
- Dealers' prices move before, or independently of, the order flow they receive.
- The venue or instrument where the informative flow concentrates does not lead the others.

## References

- Lyons, Richard K. (2001). The Microstructure Approach to Exchange Rates, ch. 1 "Overview of the Microstructure Approach", pp. 6-11, and ch. 2 "The Economics of Order Flow Information", pp. 19-27 and 33-41. MIT Press.
- Foucault, Thierry, Marco Pagano and Ailsa Röell (2013). Market Liquidity: Theory, Evidence, and Policy, ch. 3 "Order Flow, Liquidity, and Securities Price Dynamics", pp. 78-104. Oxford University Press.
- de Jong, Frank and Barbara Rindi (2009). The Microstructure of Financial Markets, ch. 9 "Price Discovery", pp. 159-168. Cambridge University Press.
- Baker, H. Kent and Halil Kiymaz (eds.) (2013). Market Microstructure in Emerging and Developed Markets, chapter "The Microstructure of Currency Markets", pp. 92-93. Wiley.
- Hasbrouck, Joel (1988).
- Hasbrouck, Joel (1991a).
- Hasbrouck and Sofianos (1993).
