---
id: FP-027
title: Exchange reserves and on-chain netflows
family: flows and positioning
mechanism: [flows, structural, information]
asset_classes: [crypto]
horizon: [days, weeks, months]
data: [on-chain data, exchange reserves, exchange inflows and outflows, daily prices]
status: untouched
---

## Mechanism

In crypto markets, changes in the reserves that exchanges hold, and on-chain net flows of coins to
or from trading platforms, reflect changes in potential selling or buying pressure. Not all coins
"in circulation" are equally saleable in the short term: a token held in a private wallet, locked in
long-term storage or kept off the trading platforms does not exert the same potential pressure as a
token already on an exchange. Exchange reserves are therefore a measure of the supply that can be
mobilised immediately. An inflow of coins to exchanges is often read as an increase in the inventory
that can be sold at once; a withdrawal to cold wallets, private wallets or custodians can signal a
reduction of the supply that floats in the short term, a scarcity of liquid supply. Not every
deposit leads to a sale: the point is that where the coins are held changes the propensity and the
ability to trade them quickly.

The mechanism rests on the separation between the stock that is held and the stock that is
available: between total supply, circulating supply, liquid supply and the supply actually "at the
point of sale". It depends on the custody and trading architecture of the asset, and this
liquid-supply overhang has little equivalent in traditional equity markets. In a market where a
large share of the supply is illiquid or dormant, moving coins onto trading platforms can make that
supply effective. The actors are long-term holders, traders, centralised platforms, OTC desks and
arbitrageurs. The episodes concerned in particular are stress, profit-taking, contagion between
platforms, and changes in the behaviour of large holders. It is conceptually close to institutional
holdings in equities: what counts is who holds, where the units are stored, and under what
constraint they can be mobilised. The phenomenon persists because the location of supply really
matters for the capacity to sell immediately, and because the market does not always correctly
identify the intention behind flows to exchanges.

Deposits and withdrawals can also reflect internal reorganisations, collateral management,
over-the-counter transfers or custody operations.

## Prediction

Rising exchange reserves and net inflows of coins to exchanges can signal a rise in the supply
available for sale, and so in potential selling pressure on prices; net outflows to private wallets,
cold wallets or custodians can signal a scarcer liquid supply, and so potential buying pressure. The
horizon is short to medium term, and the setting is mainly Bitcoin and the large tokens.

## What would refute it

- Net inflows to exchanges followed by no more selling, and no weaker prices, than net outflows;
  changes in exchange reserves and net flows to and from exchanges bearing no relation to subsequent
  prices.
- Changes in exchange reserves unrelated to subsequent selling or prices even where reserves are
  well observed and organic flows are separated from internal reorganisations, collateral movements,
  over-the-counter transfers and custody operations.
- Coins held on exchanges sold no more readily than coins held in private wallets or long-term
  storage.

## References

- Hoang, Lai, Dirk G. Baur (2022). Loaded for Bear: Bitcoin Private Wallets, Exchange Reserves and Prices. Journal of Banking and Finance.
- Ante, L., Fiedler, I. and Strehle, E. (2021). Work on on-chain metrics and market information.
- Cerutti, E. et al. (2026). IMF work on crypto intermediation, flows and risks. International Monetary Fund.
- Work on the supply-demand balance of Bitcoin and on the measurement of liquid supply (authors and titles not specified).
