---
id: MR-007
title: Negative autocorrelation balance (microstructure versus information)
family: mean reversion and relative value
mechanism: [microstructure, information]
asset_classes: [stocks]
horizon: [intraday, days, weeks]
data: [daily prices, weekly prices, bid and ask quotes, trading volumes]
status: untouched
---

## Mechanism

Campbell, Lo and MacKinlay (1997) show formally that the autocorrelation of returns measured in the data is the net balance of two opposing effects.

- The first effect generates negative autocorrelation: the bid-ask bounce, the discreteness of prices (the tick) and dealers' inventory effects produce reversion at very short horizons.
- The second effect generates positive autocorrelation: informational momentum, as good news keeps being incorporated into prices gradually, produces short-term trends.

The measured autocorrelation is the balance of the two. Its sign and size depend on the horizon over which it is measured, on the liquidity of the asset and on the information regime.

## Prediction

- On very liquid assets at a daily horizon, microstructure effects dominate and autocorrelation can be slightly negative.
- On illiquid assets at a weekly horizon, informational momentum can dominate and autocorrelation can be positive.
- More generally, the sign and magnitude of return autocorrelation shift with the measurement horizon, the liquidity of the asset and the information regime, as the balance between the two effects shifts.

The decomposition is connected to price discreteness, to momentum and to variance-ratio measures of autocorrelation.

## What would refute it

- Autocorrelation whose sign does not vary with liquidity and horizon as described: for example strongly negative weekly autocorrelation in illiquid assets, or positive daily autocorrelation in very liquid ones, with no change in the information regime.
- Negative autocorrelation that persists once the bid-ask bounce, price discreteness, inventory effects and non-synchronous trading are removed, which would point to a cause outside the two effects, such as overreaction.
- Positive autocorrelation that does not weaken where information is incorporated faster.

## References

- Campbell, J. Y., Lo, A. W. and MacKinlay, A. C. (1997). The Econometrics of Financial Markets. Princeton University Press. Chap. 3, decomposition of autocorrelation, pp. 62-84.
