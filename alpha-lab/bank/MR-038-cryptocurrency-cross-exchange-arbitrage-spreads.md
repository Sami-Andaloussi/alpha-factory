---
id: MR-038
title: Cryptocurrency market segmentation and cross-exchange arbitrage spreads
family: mean reversion and relative value
mechanism: [limits to arbitrage, structural]
asset_classes: [crypto]
horizon: [days, weeks]
data: [cryptocurrency prices by exchange, fiat exchange rates, perpetual and dated futures prices]
status: untouched
---

## Mechanism

Cryptocurrency markets show recurring price deviations between trading venues, often larger across countries than within them, and these deviations can persist for days or weeks. They signal market segmentation and frictions in deploying arbitrage capital: regulations, capital controls, operational risks and funding limits. The mechanism is an imperfect law of one price: spreads exist because arbitrage is costly and risky, and when arbitrage becomes possible, or when the pressure fades, the spreads narrow, which produces a dynamic of normalisation. In futures markets these frictions add to margin and funding constraints, which can produce relative-value deviations (perpetual swaps against dated futures, futures across venues) but also the risk that spreads last.

## Prediction

Prices of the same cryptocurrency differ across exchanges, with gaps often larger across countries than within them; the gaps recur, can persist for days to weeks, and narrow when arbitrage becomes possible or when the pressure fades. The deviations and their persistence have been documented empirically and interpreted as market segmentation (Makarov and Schoar 2020).

## What would refute it

- Cross-exchange deviations no larger across countries with capital controls than within a single country.
- Spreads that do not narrow when the frictions on moving capital ease.
- Deviations that disappear within minutes, leaving no persistence over days or weeks.
- Spreads that persist indefinitely even once arbitrage becomes possible.

## References

- Makarov, I. and Schoar, A. (2020). Trading and Arbitrage in Cryptocurrency Markets. Journal of Financial Economics.
