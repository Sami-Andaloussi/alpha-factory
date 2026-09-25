---
id: LL-008
title: Information shares and the common efficient price
family: lead-lag and information diffusion
mechanism: [information, limits to arbitrage, microstructure]
asset_classes: [stocks, equity indices, bonds, commodities, currencies]
horizon: [intraday]
data: [tick-by-tick trades and quotes, multi-venue prices, futures prices, ETF prices]
status: untouched
---

## Mechanism

One asset, or several tightly linked assets, share a latent common efficient price that is revealed
non-simultaneously by several markets, venues, quotes or instruments. When several prices bear on the
same fundamental economic value they are cointegrated, but they do not all adjust at the same speed.
Observed prices can diverge temporarily because each market incorporates information at its own pace.
The lead-lag is therefore not accidental: it is the transitory sign of an error-correction process
around a common fundamental value.

The leading market is the one that absorbs innovations in information first and incorporates what is
relevant to the fundamental value; the following markets then close the gap through arbitrage, routing
between venues or quote adjustment. The information share measures what proportion of the innovations in
the efficient price comes from each trading venue. The pattern is produced by the combination of
informed traders, arbitrageurs and market makers with structural differences between venues: depth,
costs, transparency, clientele, speed of execution, and how much more easily the common factor can be
traded in one venue than in another.

The gap does not close instantly because the bounds of arbitrage are not zero: fees, latency, short-sale
constraints, trading hours and differences in liquidity and depth prevent immediate equalisation.
Arbitrage takes time, ties up capital, bears execution costs and relies on imperfectly timestamped data.

The theory covers futures against cash, competing venues, multiple quotes, cross-listings and the home
market, ETFs against their baskets, and any situation in which a common price is discovered in one place
before spreading to others. What it asserts is that there is a common value around which speeds of
incorporation differ.

## Prediction

Prices of the same economic value in different markets move together in the long run (they are
cointegrated), while in the short run one market's innovations lead and the others adjust towards it.
Leadership can be measured by vector error-correction models and by information shares, which measure
what proportion of the innovations in the efficient price comes from each venue. The approach is applied
to price discovery between futures and cash markets, between futures markets, between venues and between
international listings.

## What would refute it

- Prices bearing on the same fundamental value are not cointegrated and drift apart durably.
- With precise timestamps, innovations reach all prices at the same time and no market leads.
- Gaps between the prices persist beyond what fees, latency, short-sale constraints and trading hours
  allow.
- Leadership is unrelated to the structural differences between venues (depth, costs, transparency,
  clientele, speed).

## References

- Hasbrouck, Joel (2007). Empirical Market Microstructure: The Institutions, Economics, and Econometrics of Securities Trading, ch. 10 "Multiple Securities and Multiple Prices", pp. 94-99; pp. 94-105, notably pp. 100-105 on leadership, VECM and information shares. Oxford University Press.
- de Jong, Frank and Barbara Rindi (2009). The Microstructure of Financial Markets, sec. 9.4 "Price Discovery in Multiple Markets", pp. 169-172. Cambridge University Press.
- Baker, H. Kent and Halil Kiymaz (eds.) (2013). Market Microstructure in Emerging and Developed Markets, ch. 16 "Price Discovery in International and Emerging Asset Markets", pp. 287-293, and chapter "Microstructure Developments in Derivative Markets", pp. 68-73. Wiley.
- Hasbrouck, Joel (1995).
- Hasbrouck, Joel (2002).
- Gonzalo and Granger (1995).
- Engle and Granger (1987).
