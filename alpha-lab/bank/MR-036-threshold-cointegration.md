---
id: MR-036
title: Threshold cointegration
family: mean reversion and relative value
mechanism: [limits to arbitrage, microstructure]
asset_classes: [stocks, equity indices, bonds, commodities, currencies]
horizon: [intraday, days, weeks]
data: [index futures prices, spot index prices, transaction costs, bid-ask spreads, funding rates]
status: untouched
---

## Mechanism

Standard cointegration assumes that the spread reverts symmetrically and continuously. Threshold cointegration holds that the spread does not revert all the time: while the gap stays small, transaction costs, execution risk, constraints on short selling, market noise and uncertainty about the hedge ratio prevent arbitrage from stepping in. There is a zone of inaction, a no-arbitrage band, within which no one arbitrages aggressively. As long as the gap is below transaction costs, the cost of balance sheet, execution risk, the risk of a short squeeze or a convergence risk premium, the correction is weak or absent. When the gap exceeds a threshold τ, arbitrage is triggered and the adjustment becomes much stronger, sometimes abrupt. The threshold autoregressive (TAR) model captures this non-linearity: the restoring coefficient α is close to zero for |e_t| < τ, with no reversion inside the band, and negative for |e_t| > τ, with active reversion outside it.

The band of inaction is tied directly to transaction costs: the higher the costs, the wider τ. It is the economic theory underlying cash-and-carry arbitrage on futures, and the mechanism bears in particular on futures/cash spreads, parities, spreads between inter-listed securities and any relative-value relation subject to fixed or quasi-fixed frictions. An arbitrageur does not act on every small gap but waits for a deviation large enough to cover slippage, commission, the spread, funding, margin and timing risk. In periods of stress the effective threshold rises further, so the adjustment is non-linear, asymmetric and dependent on the regime.

Many relative relations are real, but only beyond a certain degree of dislocation. This explains why many spreads look erratic around the centre and revert strongly at the extremes, and why spreads can seem "sticky" for a long time and then close abruptly; it also lets dislocations be read as regimes: normality, acceptable noise, then a gap large enough to trigger arbitrage. The theory predicts not a smooth mean reversion but a mean reversion conditional on the size of the dislocation.

## Prediction

Inside the band, deviations of the spread show little or no reversion; outside it, reversion is strong. Tsay (2010) gives the example of S&P 500 futures against the cash index, with two regimes according to the basis: cointegration holds, but the dynamics depend on whether the gap is wide enough to make index arbitrage profitable. Tsay cites Balke and Fomby (1997), Threshold Cointegration, and Dwyer, Locke and Yu (1996) on the non-linear dynamics between S&P 500 futures and cash. The band widens with transaction costs and in periods of stress; it depends on volatility, liquidity and costs, so it is not fixed, and the thresholds can vary over time. Tong (1978), Chan (1993) and Enders and Granger (1998) set out the theory of threshold models; Tsay (2010) and Enders (2014) apply it empirically.

## What would refute it

- Reversion that is linear, with the same speed for small and large deviations, and no band of inaction.
- A band whose width is unrelated to transaction costs, funding costs or stress.
- Spreads outside the band that stop reverting, which can signal a structural break in the economic relation.

## References

- Tsay, R. S. (2010). Analysis of Financial Time Series (3rd edition). Wiley. Chap. 8.7, Threshold Cointegration and Arbitrage, pp. 469-472; chap. 4, TAR and SETAR, the S&P 500 example, pp. 140-175; chap. 8.7, pp. 442-445, and pp. 443-445 on the threshold model applied to arbitrage between S&P 500 futures and cash.
- Vidyamurthy, G. (2004). Pairs Trading: Quantitative Methods and Analysis. Wiley. Chap. 7, Testing for Tradability, pp. 104-112.
- Pole, A. (2007). Statistical Arbitrage: Algorithmic Trading Insights and Techniques. Wiley. Chap. 4, Law of Reversion, pp. 94-117; chap. 7, Quantifying Reversion Opportunities, pp. 140 ff.
- Enders, W. (2014). Applied Econometric Time Series (4th edition). Wiley. Chap. 7, TAR and MTAR, pp. 420-470; chap. 7, pp. 408-420 on linear versus non-linear adjustment and TAR models.
- Tong, H. (1978). On a Threshold Model. In Chen, C. H. (ed.), Pattern Recognition and Signal Processing. Sijthoff & Noordhoff.
- Chan, K. S. (1993). Consistency and Limiting Distribution of the Least Squares Estimator of a Threshold Autoregressive Model. Annals of Statistics.
- Enders, W. and Granger, C. W. J. (1998). Unit-Root Tests and Asymmetric Adjustment with an Example Using the Term Structure of Interest Rates. Journal of Business & Economic Statistics.
- Balke, N. S. and Fomby, T. B. (1997). Threshold Cointegration. International Economic Review.
- Dwyer, G. P., Locke, P. and Yu, W. (1996). Index Arbitrage and Nonlinear Dynamics Between the S&P 500 Futures and Cash. Review of Financial Studies.
