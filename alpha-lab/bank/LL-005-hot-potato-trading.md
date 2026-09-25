---
id: LL-005
title: Hot potato trading
family: lead-lag and information diffusion
mechanism: [microstructure, information]
asset_classes: [currencies]
horizon: [intraday]
data: [interdealer order flow, customer order flows, dealer inventories]
status: untouched
---

## Mechanism

Hot potato trading is the rapid passing of unwanted inventory from one dealer to another after a client
trade. The initial client trade can carry information, but that information is not aggregated cleanly at
once: it travels through a chain of interdealer trades that also recycle inventory risk. The result is
twofold. On one side, the information spreads from market to market; on the other, it is blurred by
intermediated noise trading. Lyons stresses that the passing of the potato lowers the signal-to-noise
ratio of interdealer order flow and slows or distorts the aggregation of information. Dealers offload
the inventory they take on from informed client trades.

The process persists because dealers face risk constraints and inventory limits and cannot condition at
once on the positions of all the others. No omniscient dealer arbitrages it away once and for all. In
dealer, over-the-counter and semi-over-the-counter markets, the following price is slow not only because
it is less informed but because the information reaches it as inventory imbalances that are
redistributed step by step.

## Prediction

A client trade is followed by a chain of interdealer trades as the unwanted position is passed on.
Interdealer order flow carries the information of the client trade diluted by this inventory recycling,
so it is less informative than the client flow that started it. Prices in the markets and at the dealers
reached later adjust gradually, as the inventory imbalance travels. The mechanism is documented mainly
in foreign exchange.

## What would refute it

- Client trades are not followed by chains of interdealer trades; dealers keep the inventory instead of
  passing it on.
- Interdealer order flow is as informative about later prices as the client order flow behind it, with
  no dilution.
- Prices at the dealers and markets reached later adjust at once to the client trade rather than
  gradually as the inventory is redistributed.

## References

- Lyons, Richard K. (2001). The Microstructure Approach to Exchange Rates, ch. 4 "Multiple Dealers: The Simultaneous-Trade Model", pp. 95-103, notably pp. 102-103 on hot potato trading and the dilution of information. MIT Press.
- Baker, H. Kent and Halil Kiymaz (eds.) (2013). Market Microstructure in Emerging and Developed Markets, chapter "The Microstructure of Currency Markets", pp. 92-93. Wiley.
