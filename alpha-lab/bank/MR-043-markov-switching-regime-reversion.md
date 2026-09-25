---
id: MR-043
title: Markov switching and regime-conditional reversion
family: mean reversion and relative value
mechanism: [macroeconomic, limits to arbitrage]
asset_classes: [stocks]
horizon: [days, weeks, months]
data: [daily prices, realised volatility, macroeconomic releases]
status: untouched
---

## Mechanism

Markov-switching models (Hamilton 1989) let a series switch discretely between regimes following a hidden Markov chain. In the mean-reverting regime, the autoregressive coefficient is negative and the variance low; in the trending or crisis regime, the autoregressive coefficient can be positive and the variance high. Narang (2024) stresses the risk that the market moves from the mean-reverting regime into the trending or crisis regime as the main tail risk of reversion strategies, as in the quant crisis of August 2007.

The probabilities of moving between regimes depend on macroeconomic conditions; in periods of stress, the probability of staying in the crisis regime is high. The regime is latent: it cannot be observed directly. The model is related to smooth-transition (STAR) and GARCH models, to the 2007 quant crisis and to regime risk.

## Prediction

Returns alternate between a mean-reverting regime, with a negative autoregressive coefficient and low variance, and a trending or crisis regime, in which the autoregressive coefficient can be positive and the variance is high. Crisis regimes are persistent under stress, and transition probabilities move with macroeconomic conditions.

## What would refute it

- Autocorrelation and variance that do not differ across identified regimes, a single autoregressive coefficient fitting calm and crisis periods alike.
- Mean reversion as strong in high-variance, crisis periods as in calm ones.
- Transition probabilities unrelated to macroeconomic or stress conditions, or crisis regimes that are no more persistent under stress than in calm times.

## References

- Hamilton, J. D. (1989). A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle. Econometrica.
- Tsay, R. S. (2010). Analysis of Financial Time Series (3rd edition). Wiley. Chap. 4, Markov switching, pp. 165-185.
- Narang, R. K. (2024). Inside the Black Box (3rd edition). Wiley. Regime risk and the 2007 quant crisis, pp. 150-180 (approximately).
