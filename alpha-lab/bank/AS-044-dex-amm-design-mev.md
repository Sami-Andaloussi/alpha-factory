---
id: AS-044
title: DEX and AMM design, MEV extraction and DeFi token economics
family: asset-specific mechanisms
mechanism: [microstructure, structural]
asset_classes: [crypto]
horizon: [days, months]
data: [DEX trading volumes, liquidity pool data, protocol fee revenue, MEV data, daily prices]
status: untouched
---

## Mechanism

For many DeFi tokens, part of the price behaviour depends on the market structure of the protocol
itself: an automated market maker or an order book, the concentration of liquidity, the remuneration
of liquidity providers, external arbitrage, fee capture, and the extraction of value by validators or
searchers through maximal extractable value (MEV). The token of a market protocol is not a generic
asset; it inherits the frictions, the rents and the vulnerabilities created by this design.

The economic mechanism comes from the fact that the protocol distributes or destroys value among
traders, liquidity providers, arbitrageurs, validators, developers and token holders. An AMM design
can attract volume but generate inventory losses for the liquidity providers; MEV can increase activity
while taxing some users; fee capture can support the token if it is actually passed on to the holders,
or instead benefit mostly other actors. The persistence comes from the fact that these effects are
endogenous to the protocol and do not disappear without a change of the market mechanism.

## Prediction

For the tokens of DEXs and trading infrastructures, part of the price behaviour depends on how the
design of the protocol distributes or destroys value among traders, liquidity providers, arbitrageurs,
validators, developers and token holders: fee capture can support the token if it is actually passed
on to the holders, or instead benefit mostly other actors; an AMM design can attract volume but
generate inventory losses for liquidity providers; MEV can increase activity while taxing some users.
The horizon is recurrent, with a high sensitivity to protocol upgrades, to changes in the fee
structure, to competition between protocols and to on-chain market conditions. The setting is DeFi
protocols and the tokens tied to DEXs and trading infrastructures.

## What would refute it

- The prices of DEX tokens bear no relation to the design choices of their protocol: AMM or order book,
  liquidity concentration, remuneration of liquidity providers, fee capture, exposure to MEV.
- Tokens whose protocol passes fees on to holders behave no differently from tokens whose protocol does
  not.
- Protocol upgrades and changes in the fee structure cause no repricing of the token.

## References

- Capponi, Agostino, Ruizhe Jia (2025). Liquidity Provision on Blockchain-Based Decentralized Exchanges. Review of Financial Studies.
- Azar, Pablo D., Adrian Casillas, Maryam Farboodi (2024). Information and Market Power in DeFi Intermediation. NBER Working Paper No. 32949.
- Lehar, Alfred, Christine A. Parlour (2022). Systemic Fragility in Decentralized Markets. BIS Working Paper No. 1062.
