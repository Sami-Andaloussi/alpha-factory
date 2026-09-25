---
id: AS-040
title: Bonding curves
family: asset-specific mechanisms
mechanism: [structural]
asset_classes: [crypto]
horizon: [days, months]
data: [bonding curve parameters, token supply, reserve pool balances, daily prices]
status: untouched
---

## Mechanism

A bonding curve explicitly links the mint or burn price of a token to its circulating supply, and
sometimes to the size of a reserve pool. The price is therefore partly an output of the contract, and
not only a market variable. These mechanics create very particular recursive behaviour: an advantage
for the first entrants, a convex or concave price profile, an endogenous treasury effect, and a
reflexivity between participation and valuation.

The phenomenon persists because it is encoded in the smart contract. It is found in some issuances, in
token-curated registries, and in architectures where a reserve fills or empties with use. The books
cited stress that these systems often rest on strong rationality assumptions; under stress, exits can
produce very unstable dynamics.

## Prediction

The price of a token issued on a bonding curve is partly an output of the contract, not only a market
variable, and shows the recursive behaviour the curve creates: an advantage for the first entrants, a
convex or concave price profile, an endogenous treasury effect, and reflexivity between participation
and valuation. Under stress, exits can produce very unstable dynamics. The mechanism is found in some
issuances, in token-curated registries, and in architectures where a reserve fills or empties with
use.

## What would refute it

- The prices of bonding-curve tokens bear no relation to the mint and burn prices of the curve as the
  supply changes.
- The first entrants gain no advantage, and participation and valuation do not reinforce each other.
- Exits under stress unwind smoothly along the curve, without unstable dynamics.

## References

- Harvey, Campbell R., Ashwin Ramachandran, Joey Santoro (2021). DeFi and the Future of Finance. Wiley. Section DeFi Primitives, PDF pp. 43-49.
- Voshmgir, Shermin (2025). Token Economy, 3rd edition. Token Kitchen. Monetary & Fiscal Policy of DAOs, and later discussion of bonding curves, PDF pp. 136 and 276.
