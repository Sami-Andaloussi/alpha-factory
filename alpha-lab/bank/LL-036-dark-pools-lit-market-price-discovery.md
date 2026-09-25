---
id: LL-036
title: Dark pools and lit-market price discovery
family: lead-lag and information diffusion
mechanism: [microstructure, structural, information]
asset_classes: [stocks]
horizon: [intraday]
data: [dark pool trades, lit-market quotes and trades, midpoint prices, dark trading market shares]
status: untouched
---

## Mechanism

Dark pools generally do not form their own reference price: they import price discovery from lit
markets, often through the midpoint or another external price. This creates a structural lead-lag
between venues: the lit venue leads and the dark venue follows.

The economic reason is simple. The hidden counterparty in a dark pool answers a need for discreet
execution, not a need to display information publicly, so information is mostly produced where quotes
are visible and can be contested. The pattern persists because opacity is precisely the service dark
pools sell: it lowers the market impact of certain blocks, but it also keeps these venues from becoming
the main producers of public prices.

The books stress that the overall effect of dark trading on the quality of price discovery is not
one-directional. A moderate share of dark trading can improve the execution of some orders, while too
large a share can degrade the informational quality of lit markets by drawing order flow away from
them.

## Prediction

Prices of dark-pool executions generally follow the prices of lit markets, often their midpoint, and
price discovery takes place mostly on the lit venues. When the share of dark trading grows too large,
the informational quality of lit-market prices can deteriorate.

## What would refute it

- Prices in dark pools move before lit-market prices, or dark venues contribute a large share of price
  discovery.
- The informational quality of lit-market prices does not deteriorate when the share of trading that
  migrates to dark venues becomes large.
- Dark pools set execution prices independently of lit-market quotes.

## References

- Baker, H. Kent and Halil Kiymaz (eds.) (2013). Market Microstructure in Emerging and Developed Markets, ch. 12 "Dark Trading", pp. 214-225, notably pp. 223-225 on external reference prices and the effects on price discovery. Wiley.
- Lehalle, Charles-Albert and Sophie Laruelle (2018). Market Microstructure in Practice, 2nd edition, section "Dark pools and price discovery", pp. 54-55. World Scientific.
- Sarkar, Schwartz and Klagge (2009).
- Degryse, de Jong and Van Kervel (2011).
