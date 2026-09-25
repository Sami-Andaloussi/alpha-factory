---
id: AS-039
title: Algorithmic stablecoins and mint-burn reflexivity
family: asset-specific mechanisms
mechanism: [structural, limits to arbitrage]
asset_classes: [crypto]
horizon: [days, months]
data: [stablecoin prices, companion token prices and market capitalisation, mint and burn volumes]
status: untouched
---

## Mechanism

The idea of algorithmic stablecoins is to stabilise the price not through a full exogenous reserve but
through automatic rules that adjust supply, sometimes with a companion token or an auxiliary debt that
absorbs the variations. The stability of these stablecoins, or quasi-stablecoins, rests partly on an
endogenous architecture of minting and burning between several tokens rather than on simple external
reserves. The mechanism is highly reflexive: the stability of asset A depends on the expected value of
the token or debt B, which itself depends on the credibility of A's peg. The value of one token rests
on the belief that another token will absorb or redistribute the changes in demand. As long as
confidence holds and expectations remain coordinated, the mechanism can work locally, but the design
is structurally vulnerable to regimes of loss of confidence; when confidence breaks, the structure
becomes reflexive and can produce a self-reinforcing selling spiral. The price therefore depends on
the internal mechanics of convertibility and on the elasticity of supply.

The mechanism is deeply structural: it is not a universal external shock but the design of the
protocol that creates the fragility. The actors are arbitrageurs, holders of the stablecoin, holders
of the token that absorbs the losses, market makers, and possibly DeFi protocols that use the
stablecoin as collateral. The phenomenon persists because the equilibria are multiple: a regime of
confidence can coexist with a regime of run. The arbitrage that is meant to stabilise the system itself
becomes destructive when the residual capitalisation of the "buffer" token is no longer sufficient.
Ex ante, these systems persist because they promise stability without a central intermediary; ex
post, their fragility comes from reflexivity. Part of a token's price behaviour can thus be entirely
determined by its place in an internal monetary architecture, independently of any generic trend or
relative-value dynamics.

## Prediction

The horizon of algorithmic stablecoins is latent, then abrupt: a long phase of apparent stability,
then a non-linear break. As long as confidence holds, the mint-burn mechanism can work; when confidence
breaks, the structure becomes reflexive and can produce a self-reinforcing selling spiral, and the
arbitrage meant to stabilise the system itself becomes destructive when the residual capitalisation
of the buffer token is no longer sufficient. The most evident setting is crypto, notably episodes of the
Terra-Luna type.

## What would refute it

- Algorithmic stablecoins keep their peg through losses of confidence, with no self-reinforcing spiral
  between the stablecoin and its absorbing token.
- Their breaks are caused by external shocks unrelated to their mint-burn design, and hit
  reserve-backed stablecoins in the same way.
- Arbitrage keeps stabilising the system even when the residual capitalisation of the buffer token is
  no longer sufficient.

## References

- Voshmgir, Shermin (2025). Token Economy, 3rd edition. Token Kitchen. Algorithmic Stable Tokens, PDF pp. 196-200.
- Harvey, Campbell R., Ashwin Ramachandran, Joey Santoro (2021). DeFi and the Future of Finance. Wiley. Taxonomy of stablecoins and mint/burn primitives, PDF pp. 29, 44 and 49.
- Schianchi, Augusto, Andrea Mantovi (2024). The Economics of Cryptocurrencies and Digital Money: A Monetary Framework with a Game Theory Approach. Springer. Chapter 5, Stablecoins, section Terra and Luna, PDF p. 144.
- Caton, James L. (ed.) (2022). The Economics of Blockchain and Cryptocurrency: A Transaction Costs Revolution. Edward Elgar. Discussion of Basis and algorithmic pegs, PDF pp. 55-57.
- Liu, Jiageng, Igor Makarov, Antoinette Schoar (2023). Anatomy of a Run: The Terra Luna Crash. NBER Working Paper No. 31160.
- Aldasoro, Iñaki, Perry Mehrling, Daniel Neilson (2023). On Par: A Money View of Stablecoins. BIS Working Paper No. 1146.
