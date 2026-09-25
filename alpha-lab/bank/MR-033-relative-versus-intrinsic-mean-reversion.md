---
id: MR-033
title: Relative versus intrinsic mean reversion
family: mean reversion and relative value
mechanism: [structural, macroeconomic]
asset_classes: [equity indices, bonds, commodities, currencies]
horizon: [weeks, months, years]
data: [futures prices, commodity spreads, bond futures prices, marginal production costs]
status: untouched
---

## Mechanism

Narang (2024) proposes a taxonomy of mean-reversion strategies in two kinds.

- Intrinsic reversion: an asset returns towards its own historical or fundamental value, as when the price of oil returns towards its marginal cost of production over the long run. This kind of reversion is exposed to changes in the macroeconomic regime, which can shift the equilibrium level itself.
- Relative reversion: an asset returns towards its value relative to its peers, as when WTI crude returns towards Brent after an unusual gap. This kind is market-neutral with respect to the common macroeconomic factors, and so much less exposed to changes of regime: a change of macro regime affects both assets at the same time and leaves the relative relationship intact.

In futures, relative-value spreads between close instruments, such as WTI/Brent, corn/soybeans or Euro-Bund/Euro-Bobl (GBL/GBM), are thus market-neutral by construction, whereas the directional reversion of a single asset towards its own history (oil bought because it is low relative to its past) carries the risk that the equilibrium itself has moved. Fundamental changes in the relationship between peers, such as new sources of supply or regulatory changes, can break relative value.

## Prediction

Deviations of spreads between close peers revert more reliably across macroeconomic regimes than deviations of a single asset from its own history or fundamental value; intrinsic reversion is exposed to changes of regime that can shift the equilibrium level structurally. It is related to pairs trading, cointegration, statistical arbitrage, sector reversion and calendar spreads.

## What would refute it

- Relative spreads between close peers that break as often as single-asset levels during changes of macroeconomic regime.
- Intrinsic reversion that is as stable across regimes as relative reversion.
- Changes of macro regime that shift the relative value between close peers as much as their absolute levels.

## References

- Narang, R. K. (2024). Inside the Black Box (3rd edition). Wiley. Chapter on the taxonomy of reversion strategies, pp. 100-140 (approximately).
