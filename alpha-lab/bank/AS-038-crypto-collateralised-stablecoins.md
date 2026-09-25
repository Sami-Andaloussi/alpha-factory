---
id: AS-038
title: Crypto-collateralised stablecoins
family: asset-specific mechanisms
mechanism: [structural, limits to arbitrage]
asset_classes: [crypto]
horizon: [days]
data: [collateralisation ratios, oracle prices, liquidation events, stablecoin prices, governance token prices]
status: untouched
---

## Mechanism

Here stability depends not on an off-chain bank account but on on-chain overcollateralisation. The
price behaviour of the stable asset, and also that of the associated governance token or collateral,
depends on the collateralisation ratios, the oracles, the liquidation mechanisms and the incentives of
the keepers. The mechanism is deeply asset-specific: the same fall in the collateral does not have the
same consequences depending on the overcollateralisation margin, the speed of the oracle and the
architecture of liquidation.

The phenomenon persists because capital frictions are real: a lot of collateral must be locked up to
issue a little stablecoin, which makes the system structurally sensitive to market stress. The
efficiency of the peg requires a collateral volatility compatible with the haircuts, and a responsive
governance.

## Prediction

The price behaviour of a crypto-collateralised stablecoin, and that of its governance token or of the
associated collateral, depends on the collateralisation ratios, the oracles, the liquidation
mechanisms and the incentives of the keepers: the same fall in the collateral has different
consequences depending on the overcollateralisation margin, the speed of the oracle and the
liquidation architecture. Because a lot of collateral must be locked up to issue a little stablecoin,
the system is structurally sensitive to market stress. The efficiency of the peg requires a collateral
volatility compatible with the haircuts, and a responsive governance. The typical setting is MakerDAO,
DAI and Synthetix.

## What would refute it

- A fall in the collateral has the same effect on the peg and on the governance token whatever the
  overcollateralisation margin, the speed of the oracle and the liquidation design.
- Crypto-collateralised systems show no particular sensitivity to market stress despite their large
  collateral requirements.
- The peg holds when the volatility of the collateral exceeds what the haircuts cover, or when
  governance fails to respond.

## References

- Voshmgir, Shermin (2025). Token Economy, 3rd edition. Token Kitchen. Crypto-Collateralized Stable Tokens, PDF pp. 193-196.
- Harvey, Campbell R., Ashwin Ramachandran, Joey Santoro (2021). DeFi and the Future of Finance. Wiley. Maker, Synthetix and collateral ratios, PDF pp. 71, 79 and 121-123; table on the permissionless issuance of DAI, PDF p. 79.
