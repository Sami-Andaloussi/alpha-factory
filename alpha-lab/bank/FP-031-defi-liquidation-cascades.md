---
id: FP-031
title: DeFi liquidation cascades
family: flows and positioning
mechanism: [flows, structural]
asset_classes: [crypto]
horizon: [intraday, days]
data: [on-chain lending positions, liquidation thresholds, liquidation data, on-chain depth, intraday prices]
status: untouched
---

## Mechanism

On-chain lending and margin protocols force sales when the value of collateral falls below set
thresholds. Liquidating smart contracts then automatically sell assets to repay the debt or to
restore the collateralisation ratio. The mechanism is structural, its rules are transparent, and it
can sometimes be observed almost in real time: it is one of the purest cases of mechanical forced
selling in crypto.

Its strength depends on the parameters of the protocol, the concentration of positions, the
correlation between the collateral and the borrowed assets, the on-chain depth, and the speed of
the liquidation bots. An initial fall in price can make many positions liquidatable; the resulting
sales deepen the fall, trip further thresholds, and set off a cascade. The result is analogous to
margin spirals in traditional finance, with more automation and more visibility.

The cascades persist because protocols give priority to the solvency of the system, not to
minimising the aggregate price impact. Arbitrageurs and liquidators take part in the equilibrium,
but they can also extract value through liquidation penalties, which makes the process very fast.

## Prediction

When collateral prices fall towards levels where many positions reach their liquidation thresholds,
automatic liquidations sell collateral, which deepens the fall and triggers further liquidations
within a very short time. Their size depends on the parameters of the protocol, the concentration of
positions, the correlation between collateral and borrowed assets, on-chain depth and the speed of
the liquidation bots.

## What would refute it

- Price declines through dense clusters of liquidation thresholds followed by no further decline.
- Liquidations absorbed without price impact even when on-chain depth is thin.
- Cascade sizes unrelated to the concentration of positions, to on-chain depth or to the parameters
  of the protocol.

## References

- Qin, K., Zhou, L., Afonin, D. et al. (2021). Work on DeFi liquidations and risks.
- Lehar, A. and Parlour, C. (2023). Work on decentralized lending.
- Ackerer, D., Hugonnier, J. and Jermann, U. (2024-2025). Theoretical and empirical work on DeFi liquidation dynamics.
