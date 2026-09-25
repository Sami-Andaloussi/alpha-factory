---
id: AS-030
title: Staking ratio, float scarcity and unstaking fragility
family: asset-specific mechanisms
mechanism: [structural]
asset_classes: [crypto]
horizon: [days, weeks, months]
data: [staking ratios, circulating supply, unstaking queues, staking yields, daily prices]
status: untouched
---

## Mechanism

In proof-of-stake networks, part of the tokens is locked up to secure the protocol and to earn
rewards. This lock-up reduces the liquid supply immediately available, changes the depth of the spot
market, and alters the relation between the token's price, its security and its yield. An asset with a
large staked share does not have the same micro-economics as a fully liquid asset: the relevant
economic float can be much smaller than the displayed circulating supply.

The mechanism has two faces. On the positive side, a high staking ratio can support the price
through the scarcity of the float, the commitment of holders and the strengthening of the network's
security. On the side of fragility, the same structure can make the system vulnerable to coordinated
exits if expectations change: if holders want to unstake in order to sell, the market can discover
that part of the "locked stock" was only deferred supply. Theoretical work formalises this link
between staking, security, token supply, the cost of an attack and valuation. Arbitrage does not
remove the mechanism, because it is built into the design of the protocol itself. It is a mechanism
of the asset's architecture, very different from a simple universal carry.

## Prediction

Proof-of-stake tokens with a high staking ratio can have an effective float much smaller than their
circulating supply, and the high staking ratio can support their price over intermediate horizons,
through the scarcity of the float, the commitment of holders and the strengthening of security. The
same tokens can go through episodes of stress when staking yields, governance, slashing risk or exit
conditions change: if holders want to unstake in order to sell, the market can discover that part of
the locked stock was only deferred supply. The setting is proof-of-stake cryptoassets.

## What would refute it

- Tokens with a high staking ratio show no difference in liquidity, market depth or price behaviour
  from comparable tokens with a low staking ratio.
- Changes in staking yields, governance, slashing risk or exit conditions trigger no wave of unstaking
  and no price stress.
- Large unstaking episodes are not followed by selling pressure on the token.

## References

- Cong, Lin William, Zhiheng He, Ke Tang (2025). The Tokenomics of Staking. NBER Working Paper No. 33640.
- Catalini, Christian, Ravi Jagadeesan, Scott Duke Kominers (2020). Markets for Crypto Tokens, and Security under Proof of Stake. SSRN Working Paper.
