---
id: LL-035
title: Market fragmentation and latency lead-lag
family: lead-lag and information diffusion
mechanism: [microstructure, structural, information]
asset_classes: [stocks]
horizon: [intraday]
data: [venue-level quotes and trades, exchange timestamps, trade-through records]
status: untouched
---

## Mechanism

In a fragmented market, information does not enter every venue at the same moment: order books are
separate, flows are routed by different intermediaries, and observers do not all have the same latency
or the same view of the market. A price move can therefore appear first on one venue and then migrate to
the others through smart order routing, arbitrage, the withdrawal of stale quotes or the updating of
market makers' quotes. Trade-throughs and incomplete access to venues are symptoms of this imperfect
diffusion.

The mechanism is maintained by very concrete frictions: there is no consolidated order book on which one
can act perfectly, technology is costly, data feeds differ in quality, the rules that protect orders
against trade-throughs are incomplete or imperfect, and part of the liquidity is hidden. Some
short-horizon lead-lag signals between venues come from this routing microstructure rather than from
fundamental information.

## Prediction

Price moves can appear first on one venue and reach the others with a delay. Trade-throughs occur, and
quotes on the slower venues go stale before being withdrawn or updated. The lead-lag between venues
depends on latency, on the quality of data feeds and on the routing of orders.

## What would refute it

- All venues update their prices at the same moment, with no trade-throughs and no stale quotes.
- The order in which venues react bears no relation to their latency, to the quality of their data feeds
  or to the routing of orders.
- The lead-lag between venues persists unchanged where a consolidated, fully actionable book and
  complete order protection exist.

## References

- Foucault, Thierry, Marco Pagano and Ailsa Röell (2013). Market Liquidity: Theory, Evidence, and Policy, ch. 7 "Market Fragmentation", pp. 264-267. Oxford University Press.
- Lehalle, Charles-Albert and Sophie Laruelle (2018). Market Microstructure in Practice, 2nd edition, sections on fragmentation, latency and smart order routing, pp. 45, 49-52 and 54-55. World Scientific.
- Hasbrouck and Saar (2010).
- Hendershott, Jones and Menkveld (2011).
