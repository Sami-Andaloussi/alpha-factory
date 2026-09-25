---
id: AS-029
title: Staking and slashing
family: asset-specific mechanisms
mechanism: [structural]
asset_classes: [crypto]
horizon: [weeks, months]
data: [staking ratios, staking rewards, slashing events, exit queues, daily prices]
status: untouched
---

## Mechanism

Staking turns the token into productive and disciplining capital: the asset must be locked up to
secure the network, to validate, to take part in certain distributions, or to guarantee correct
behaviour in smart contracts. Slashing introduces the punitive symmetry: the staked token can be cut
if behaviour is invalid, if collateral becomes insufficient, or if certain security conditions are no
longer met.

This architecture creates price and circulation behaviour specific to the assets concerned: a lower
free float, a nominal yield, possible penalties, exit queues, and a sensitivity to collateralisation
ratios and to the design of the reward. The phenomenon persists because it is embedded in the protocol;
it does not depend on an external convention. A high nominal yield can be no more than a dilutive
redistribution, and a strong concentration of the stake can reduce the decentralised character of the
system.

## Prediction

Assets with staking show a reduced free float, a nominal staking yield, penalties when slashing
occurs, and exit queues when holders withdraw, and their prices and circulation are sensitive to
collateralisation ratios and to the design of the reward. These features follow from the rules of
each protocol, so they differ from one staked asset to another with the design of its staking,
slashing and reward.

## What would refute it

- Tokens with a large staked share show the same free float, liquidity and price behaviour as
  comparable tokens without staking.
- Changes in slashing rules, collateralisation ratios, reward design or exit queues leave the price
  and the circulation of the token unchanged.
- Slashing events leave the behaviour of stakers and the price of the token unchanged.

## References

- Harvey, Campbell R., Ashwin Ramachandran, Joey Santoro (2021). DeFi and the Future of Finance. Wiley. Section "DeFi Primitives", PDF pp. 23, 50-51, 62-64, 123, 140 and 170-171.
- Li, Jing, Dusit Niyato, Zhu Han (2023). Cryptoeconomics: Economic Mechanisms Behind Blockchains. Cambridge University Press. Passages on Ethereum staking, validators and security deposits, PDF pp. 16, 99-102, 185 and 193.
- Voshmgir, Shermin (2025). Token Economy, 3rd edition. Token Kitchen. "Alternative Consensus Mechanisms to PoW" and "Monetary & Fiscal Policy of DAOs", PDF pp. 59-60 and 136.
