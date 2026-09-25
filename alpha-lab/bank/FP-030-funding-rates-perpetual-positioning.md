---
id: FP-030
title: Funding rates and aggregate positioning in perpetual futures
family: flows and positioning
mechanism: [flows]
asset_classes: [crypto]
horizon: [days, weeks, months]
data: [funding rates, open interest, futures basis, liquidation data, spot trading volumes, daily prices]
status: untouched
---

## Mechanism

The funding rate and the open interest of perpetual futures reveal an aggregate imbalance of
positions between leveraged longs and leveraged shorts, and this imbalance can be transmitted to the
spot market. A strongly positive funding rate generally signals that demand for long leverage
dominates; a strongly negative one signals the reverse. Such states of positioning can precede
squeezes, unwinds of crowded long or short positions, and spot flows induced by arbitrage, hedging
or liquidations.

The mechanism rests on the growing integration of the derivatives and spot markets, which
cash-and-carry desks, market makers, basis traders and arbitrageurs connect. When positioning in
derivatives becomes extreme, an adverse price move can trigger liquidations or reductions in
leverage that spread to the spot market through hedges and imbalances between counterparties. The
funding rate is therefore not merely a gauge of sentiment: it is an equilibrium price between
populations of position holders, and it tells how potential pressure is structured.

The funding rate can stay extreme for a long time, and it can reflect arbitrage strategies rather
than outright directional conviction.

## Prediction

Extreme positioning, shown by a strongly positive funding rate (dominant demand for long leverage)
or a strongly negative one, with the open interest, can precede squeezes, unwinds of crowded long or
short positions, and spot flows induced by arbitrage, hedging or liquidations; an adverse price move
can then trigger liquidations or deleveraging that spread to the spot market. The horizon is short
to intermediate, and the episodes concerned in particular are those of high leverage.

## What would refute it

- Extreme funding rates followed by unwinds, squeezes or liquidations no more often than neutral
  funding rates.
- Liquidations and deleveraging in perpetual futures leaving spot prices and spot flows unaffected.
- Spot returns after episodes of extreme funding no different from spot returns after neutral
  episodes, even when open interest and leverage are high.

## References

- Akyildirim, E., Corbet, S., Efthymiou, M. et al. (2020). Work on cryptocurrency derivatives and price discovery.
- Doan, T., Pham, H. and Nguyen Thanh, B. (2022). Work on funding rates and crypto returns.
- Augustin, P., Rubtsov, A. and Shin, D. (2023). Work on price discovery and crypto derivatives.
