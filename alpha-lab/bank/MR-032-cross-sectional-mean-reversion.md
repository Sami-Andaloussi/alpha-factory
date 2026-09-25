---
id: MR-032
title: Cross-sectional mean reversion
family: mean reversion and relative value
mechanism: [microstructure, behavioural]
asset_classes: [stocks, equity indices, bonds, commodities, currencies]
horizon: [days, weeks]
data: [daily prices, market capitalisation, trading volumes]
status: untouched
---

## Mechanism

Assets that have most outperformed their universe over a short period tend to underperform it over the next period, and those that have most underperformed tend to outperform. It is a reversion towards the median of the universe: the extremes return towards the centre. Chan (2013) and Grinold and Kahn (2020) present the mechanism as the basis of short-term cross-sectional alpha in portfolio optimisation models. A typical signal is the negative of the standardised past relative return, Signal_t(i) = −(r_{t−1}(i) − mean(r_{t−1})) / std(r_{t−1}).

The traders involved are statistical arbitrage funds, multi-strategy hedge funds and market-neutral funds. The predictive power of the signal decays fast, within a few days.

## Prediction

The deviation of an asset's return from the average of its universe over the last period predicts, with a negative sign, its relative return over the next period, and this predictive power decays within days. The effect is stronger in small and mid capitalisations than in large, liquid futures contracts. It is documented by the one-month reversal of stock returns (Jegadeesh 1990) and by cross-sectional reversion in futures (Chan 2013). It is related to signal decay, to pairs trading, and to the sequence of momentum followed by reversal.

## What would refute it

- No negative relation between an asset's past relative return and its next-period relative return.
- Predictive power that persists for long periods instead of decaying within days.
- An effect as strong in large, liquid instruments as in small and mid capitalisations.

## References

- Chan, E. P. (2013). Algorithmic Trading: Winning Strategies and Their Rationale. Wiley. Chap. 5-6, cross-sectional reversion in futures, pp. 120-160.
- Grinold, R. C. and Kahn, R. N. (2020). Advances in Active Portfolio Management. McGraw-Hill. Chapter on signal decay and the IC, pp. 100-150 (approximately).
- Jegadeesh, N. (1990). Evidence of Predictable Behavior of Security Returns. Journal of Finance.
