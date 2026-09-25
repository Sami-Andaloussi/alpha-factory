---
id: MR-011
title: Volume-conditioned short-horizon reversals
family: mean reversion and relative value
mechanism: [microstructure, information]
asset_classes: [stocks, equity indices, bonds, commodities, currencies]
horizon: [days, weeks]
data: [daily prices, trading volumes, futures open interest]
status: untouched
---

## Mechanism

Trading volume is not only an amplifier of volatility: it helps tell an informational move, which is more permanent, from a liquidity move, which is more transitory. In the model of Campbell, Grossman and Wang (1993), which links trading volume to the autocorrelation of returns, episodes of high volume driven by liquidity flows (rebalancing, needs for immediacy) raise the probability that part of the price move reverses once the pressure has been absorbed.

The natural dynamics are short: from one or a few days to one or two weeks. In futures, indicators of trading activity, volume and open interest, can help tell a move that reverses from a lasting one, for example a shock to speculative appetite from a lasting displacement of the futures curve.

## Prediction

Returns that come with high volume from liquidity flows tend to be followed by a partial reversal over the next days to one or two weeks, once the pressure has been absorbed; informational moves are more permanent. In futures, volume together with open interest can help tell the same moves apart.

## What would refute it

- Return autocorrelation that does not decline, or that rises, in episodes of high volume driven by liquidity flows.
- High-volume moves known to be driven by liquidity flows (rebalancing, needs for immediacy) that do not partly reverse within days to a couple of weeks.
- In futures, volume and open-interest patterns that do not separate reverting moves from lasting displacements of the curve.

## References

- Campbell, J. Y., Grossman, S. J. and Wang, J. (1993). Trading Volume and Serial Correlation in Stock Returns. Quarterly Journal of Economics.
