---
id: TM-047
title: Volatility-targeted momentum (risk-adjusted momentum)
family: trend and momentum
mechanism: [risk premium]
asset_classes: [equity indices, bonds, currencies, commodities]
horizon: [weeks, months]
data: [daily prices, realised volatility]
status: in-progress
---

## Mechanism

Volatility targeting normalises the positions of a momentum portfolio by the historical volatility of
each instrument, so that each position contributes roughly equally to the total risk of the
portfolio. It is not, strictly speaking, a theory of the market but an implementation mechanism.
The mechanism is that momentum is better rewarded in periods of low volatility and suffers its worst
drawdowns in periods of high volatility. Reducing exposure when volatility is high and raising it
when volatility is low therefore improves the implicit timing of the exposure to the factor.

The scaling acts as an implicit form of market timing favourable to momentum: it cuts positions
automatically in crises, when volatility is high and a momentum crash is possible, and raises them in
calm, trending markets, when volatility is low and momentum persists better. Sizing positions in
proportion to the inverse of volatility has been the standard rule of the managed-futures industry
since the 1990s.

## Prediction

Momentum strategies and risk-premium strategies scaled by volatility have significantly higher Sharpe
ratios than unscaled versions (Moreira and Muir, 2017). Trend-following strategies on futures without
volatility scaling have lower Sharpe ratios than the same strategies with it (Carver, 2015; Clenow,
2023). Momentum is more strongly rewarded in periods of low volatility than in periods of high
volatility, when its most severe drawdowns occur.

## What would refute it

Momentum no more strongly rewarded in periods of low volatility than in periods of high volatility.
Momentum drawdowns that do not cluster in periods of high volatility. Volatility-scaled momentum,
risk-premium and trend-following strategies with Sharpe ratios no higher than their unscaled
versions.

## References

- Carver, R. (2015). Systematic Trading: A Unique New Method for Designing Trading and Investing Systems, chapters on position sizing and volatility normalisation. Harriman House.
- Moreira, A. & Muir, T. (2017). Volatility-Managed Portfolios. Journal of Finance.
- Clenow, A. F. (2023). Following the Trend: Diversified Managed Futures Trading (2nd edition), ch. 3 and 9. Wiley.
