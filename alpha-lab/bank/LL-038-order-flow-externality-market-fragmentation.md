---
id: LL-038
title: Order flow externality and market fragmentation
family: lead-lag and information diffusion
mechanism: [microstructure, structural, information, limits to arbitrage]
asset_classes: [stocks]
horizon: [intraday]
data: [venue market shares, venue-level quotes and trades, post-trade reports]
status: untouched
---

## Mechanism

Between several venues or closely related markets, information does not diffuse symmetrically. Traders
want to be where liquidity and order flow already are, because being there gives them free trading
options and better chances of execution. Harris calls this the order flow externality: it pushes one
market in a set of close markets to dominate the others. Foucault, Pagano and Röell find the same core
in the literature on fragmentation and liquidity: liquidity begets liquidity. Lehalle and Laruelle add
the modern form of the mechanism: latency, smart order routing, the degradation of pre-trade
information, and the need for post-trade transparency.

The lead-lag is then structural: the dominant venue, or the more transparent and more liquid one,
receives information earlier, and the others follow with a delay. The pattern persists because of search
costs, hidden orders, priority rules, the difficulty of linking markets, the risk of double execution
and network effects. It is not fully arbitraged away because, even if prices converge in the end, access
to the right local information is not uniform.

## Prediction

Order flow concentrates in one dominant venue among close markets, and price moves appear there first
before the other venues follow. The leading venue can change with volatility, technology and regulation.

## What would refute it

- Order flow does not concentrate: liquidity spreads evenly across close venues instead of attracting
  more liquidity.
- The dominant or most transparent venue does not move first; smaller venues lead as often as it does.
- Where venues are fully linked and pre-trade and post-trade information is complete, the dominant venue
  still leads by the same margin.

## References

- Harris, Larry (2002). Trading and Exchanges: Market Microstructure for Practitioners, ch. 1 "Introduction", pp. 7-8, and ch. 26 "Competition Within and Among Markets", pp. 525-530. Oxford University Press.
- Foucault, Thierry, Marco Pagano and Ailsa Röell (2013). Market Liquidity: Theory, Evidence, and Policy, introduction, pp. 7-9, and ch. 7 "Market Fragmentation", pp. 236-238. Oxford University Press.
- Lehalle, Charles-Albert and Sophie Laruelle (2018). Market Microstructure in Practice, 2nd edition, introduction, pp. 22-28, and appendix A.2 "Information Seeking and Price Discovery", pp. 250-253. World Scientific.
