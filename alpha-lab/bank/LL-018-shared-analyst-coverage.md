---
id: LL-018
title: Shared analyst coverage
family: lead-lag and information diffusion
mechanism: [information, behavioural]
asset_classes: [stocks]
horizon: [months]
data: [daily prices, analyst coverage]
status: untouched
---

## Mechanism

Information diffuses gradually between firms that the same sell-side analysts follow. Analysts form
an information network: they compare peers, carry signals over from one firm to another, and act as
bridges between firms that are economically or thematically linked. If firms A and B are covered by
the same analyst, news that arrives at A is relevant for B; when the analyst does not immediately
update the forecasts for B, the price of B reacts only later, so the positive return of A predicts
that of B. Ali and Hirshleifer attribute the delay to a cognitive cost: analysts reuse the information
learned on one stock for the other only slowly, which produces a continuation of B's returns after A's.

The mechanism works at two levels. First, the analyst learns about one firm through another, because
he or she knows its cost structure, its demand, its comparables and its value chain. Second, the
investors who read sell-side research, including the institutional investors who rely on analysts'
recommendations, receive and process that information through clusters of coverage. The information
can therefore travel through the network of informational intermediaries before it is fully
reflected in prices. Firms linked by common analysts have common changes in information, which lead
to momentum spillovers. The notion has no counterpart in crypto-assets, which have no dedicated
analysts.

## Prediction

The literature shows that the past returns of firms that share analysts with a given firm predict that
firm's future returns over a few months, the effect being measured with lags of one to three months
after the news. This one observable channel unifies several momentum spillovers (industry, style,
customers and suppliers, among others): shared analyst coverage captures almost all the documented
cross-firm momentum spillover effects (Ali and Hirshleifer). In factor tests on long-short portfolios,
a momentum factor built on analyst-connected firms subsumes practically all the others (industry,
geographic, customer-supplier). The effect is most likely where the analyst network captures real
economic knowledge rather than an arbitrary grouping, and it can vary with the quality and incentives
of the analysts.

## What would refute it

- Returns of analyst-connected firms carrying no information about a firm's subsequent returns, or
  no more than the returns of unconnected firms; firms linked by common analysts showing no more
  lead-lag than firms with the same economic links but no analyst in common.
- Predictability that disappears once the pre-existing economic similarities between the firms are
  accounted for: the analyst network can be endogenous to those similarities.
- Industry, geographic, style or customer-supplier momentum spillovers that remain significant once
  connections through shared analysts are controlled for.
- Analysts updating their forecasts for connected firms at the same time as for the firm where the
  news arrived.

## References

- Ali, Usman and David Hirshleifer (2020). Shared Analyst Coverage: Unifying Momentum Spillover Effects. Journal of Financial Economics; earlier version NBER Working Paper No. 25201 (2019).
- Hameed, Allaudeen, Randall Morck, Jianfeng Shen and Bernard Yeung (2015). Information, Analysts, and Stock Return Comovement. Review of Financial Studies.
