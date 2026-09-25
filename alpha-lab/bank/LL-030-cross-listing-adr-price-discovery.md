---
id: LL-030
title: Cross-listing and ADR-home market price discovery
family: lead-lag and information diffusion
mechanism: [information, limits to arbitrage, microstructure]
asset_classes: [stocks]
horizon: [intraday, days]
data: [ADR prices, home-market share prices, exchange rates, exchange trading hours]
status: untouched
---

## Mechanism

Assets that are economically identical, or nearly so, can be listed on several markets. Information can
be discovered first on one market and passed on to the other with a delay. The classic case is an
American depositary receipt (ADR) against the domestic share, or an international dual listing.

The mechanism rests on differences in time zones, liquidity, investor base, regulation, transaction
costs, the availability of local information and access to capital. The market that concentrates the
relevant information, the liquidity or the reaction of informed investors often leads price discovery;
the other follows through arbitrage, but not always instantly. Depending on the case, the domestic
market can lead because it has better local information, or the foreign market can lead because it has
more liquidity and a greater capacity to absorb global news. The two listings are a case of common
information integrated at different times in two trading venues.

## Prediction

For cross-listed stocks, one market often leads price discovery and the other follows through arbitrage,
but not always instantly. The leader can be the home market, through better local information, or the
foreign market, through greater liquidity and a greater capacity to absorb global news. The lead-lag is
often very short-lived and depends strongly on trading hours, and arbitrage between the listings is
sometimes fast. The price discovery of cross-listed stocks has been studied, for example for US-listed
Canadian stocks (Eun and Sabherwal, 2003) and for international cross-listings during overlapping
trading hours (Grammig, Melvin and Schlag, 2005).

## What would refute it

- Neither listing leads: news enters the prices of both listings at the same time during overlapping
  hours.
- Which listing leads bears no relation to where local information, liquidity and informed investors are
  concentrated.
- Price gaps between the two listings persist beyond what time zones and transaction costs allow.

## References

- Eun, Cheol S. and Sanjiv Sabherwal (2003). Cross-Border Listings and Price Discovery: Evidence from U.S.-Listed Canadian Stocks. Journal of Finance.
- Grammig, Joachim, Michael Melvin and Christian Schlag (2005). Internationally Cross-Listed Stock Prices During Overlapping Trading Hours: Price Discovery and Exchange Rate Effects. Journal of Empirical Finance.
- de Jong, Frank, Theo Nijman and Ailsa Röell (1995). Work on price discovery in dual listings.
