---
id: LL-037
title: Fragmented crypto venue price discovery
family: lead-lag and information diffusion
mechanism: [microstructure, limits to arbitrage, structural, information]
asset_classes: [crypto]
horizon: [intraday, days]
data: [exchange-level crypto prices, exchange order books, transfer times between exchanges]
status: untouched
---

## Mechanism

In crypto markets, information is not integrated at the same time across the different spot trading
platforms. Some venues discover the price before others because of their liquidity, their speed, their
user base or their institutional role. The "aggregate" price of an asset is thus the result of a
non-instantaneous diffusion across exchanges.

The market is fragmented, global and open around the clock. Exchanges differ in the quality of their
liquidity, the type of investors they serve, their constraints on fiat on-ramps and off-ramps, the
indirect leverage they offer, their operational quality, their counterparty risk and their regulatory
geography. News can therefore be incorporated first on a dominant platform and passed
on to the others through arbitrage. That arbitrage is not frictionless: transfer delays, inventory risk,
the cost of capital, credit constraints, operational fragmentation and platform risk all limit the
synchronisation of prices.

## Prediction

The literature on crypto price discovery shows a hierarchy between venues, with dominant exchanges
leading the others, and stresses that price gaps between exchanges can persist longer than in
traditional markets. Much of the effect plays out at very short horizons, and some episodes reflect
market and settlement frictions more than the diffusion of fundamental information.

## What would refute it

- No exchange leads: prices of the same crypto asset move at the same time on all platforms.
- Price gaps between exchanges close as fast as gaps between venues in traditional markets.
- The ranking of venues in price discovery bears no relation to their liquidity, speed, user base or
  institutional role, or to the frictions that limit arbitrage between them.

## References

- Makarov, Igor and Antoinette Schoar (2019). Price Discovery in Cryptocurrency Markets. AEA Papers and Proceedings.
- Makarov, Igor and Antoinette Schoar (2020). Trading and Arbitrage in Cryptocurrency Markets. Journal of Financial Economics.
- Dimpfl, Thomas and Fabian Peter (2021). Nothing but Noise? Price Discovery Between Cryptocurrency Exchanges in the Presence of Market Microstructure Noise.
