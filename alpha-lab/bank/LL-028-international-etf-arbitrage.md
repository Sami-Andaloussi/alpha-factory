---
id: LL-028
title: International ETF arbitrage
family: lead-lag and information diffusion
mechanism: [information, limits to arbitrage, structural]
asset_classes: [equity indices, stocks]
horizon: [intraday, days]
data: [ETF prices, indicative intraday values, constituent prices, exchange rates, exchange trading hours]
status: untouched
---

## Mechanism

When the local market of its basket is closed, an ETF holding international constituents can become the
main place of price discovery. Its published indicative value (IIV) then often rests on local prices
that are already stale, so a discount or premium relative to the IIV is not automatically an anomaly.
Trading desks rather use an estimated NAV (eNAV): a real-time estimate of the basket's economic value
built from correlated proxies, exchange rates and the macroeconomic information of markets that are
still open.

The lead-lag here is explicitly geographic: the ETF, listed on a market that is open, incorporates
information that will show in the prices of its components only at the next local open. It is
information diffusion between markets that do not trade at the same time. The gap persists because no
perfect real-time arbitrage against a closed market exists; the frictions are time zones, hedging with
proxies, basis risk, currency risk and financing costs.

## Prediction

While the local market is closed, the ETF price moves away from its stale IIV in the direction the
components will take at the next local open. What looks like a mispricing against the IIV may then be
only a rational anticipation of the next local prices of the components, and the components catch up
with the ETF at the open.

## What would refute it

- The premium or discount of the ETF against its IIV, built while the local market is closed, does not
  predict the moves of the components at the next local open.
- At the local open, the ETF price reverts towards the stale IIV instead of the components moving
  towards the ETF price.

## References

- Abner, David J. (2016). The ETF Handbook: How to Value and Trade Exchange Traded Funds, 2nd edition, chapter "ETFs with International Constituents", pp. 225-239 (notably pp. 225-235); "Estimated NAV Trading", pp. 172-173; the latency of the IIV and the use of eNAV, pp. 221-223. Wiley.
