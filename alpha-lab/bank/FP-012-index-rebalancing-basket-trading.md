---
id: FP-012
title: Index rebalancing and basket trading
family: flows and positioning
mechanism: [flows, structural]
asset_classes: [stocks]
horizon: [days, weeks]
data: [index weights, rebalancing dates, daily prices, trading volumes]
status: untouched
---

## Mechanism

Beyond the addition or deletion of a security, indices impose purchases and sales through the
periodic change of their weights. When the relative capitalisation of a security changes, or when
the index rules are reapplied, passive funds and part of the benchmarked assets must execute orders
on a known calendar. The result is concentrated and often synchronised flows on whole baskets of
securities.

The mechanism has several effects. It creates predictable price pressure around the rebalancing
dates. It can generate excess comovement among the members of the same index, because the orders
bear on the basket and not on the fundamentals of each security. And it increases the influence of
the intermediaries able to supply basket liquidity. The cost of arbitrage does not disappear:
positions must be financed, the risk that the estimated final weights are wrong must be managed,
and flows that are sometimes very large must be absorbed within a short time.

Indexing is largest in equities. More generally, any public rule of basket reallocation, known in
advance and carried out by large holders, creates a flow unrelated to fundamentals. The theory is
closely linked to ETF flows, to comovement induced by common ownership, and to the inelastic markets
hypothesis.

## Prediction

Securities whose index weight rises are bought, and those whose weight falls are sold, around the
rebalancing dates, with predictable price pressure in the direction of the required trades. Members
of the same index can comove more than their fundamentals warrant, the comovement being tied to the
basket trading of index investors.

## What would refute it

- No abnormal price pressure or volume around index rebalancing dates for the securities whose
  weights change.
- Members of an index comoving no more with one another than comparable non-members with similar
  fundamentals.
- Excess comovement that does not change when a security enters or leaves an index.

## References

- Greenwood, R. and Sosner, N. (2007). Trading Patterns and Excess Comovement of Stock Returns. Financial Analysts Journal.
- Wurgler, J. (2010). On the Economic Consequences of Index-Linked Investing. NBER Working Paper.
- Ben-David, I., Franzoni, F. and Moussawi, R. (2018). Do ETFs Increase Volatility? Journal of Finance.
