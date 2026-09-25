---
id: MR-041
title: Cryptocurrency short-term reversal (illiquidity and retail dominance)
family: mean reversion and relative value
mechanism: [microstructure, behavioural]
asset_classes: [crypto]
horizon: [days]
data: [daily cryptocurrency prices, trading volumes, order book depth, exchange listings]
status: untouched
---

## Mechanism

In crypto spot markets, the general mechanism of liquidity provision takes a specific form. The dominant interpretation is that most crypto-assets are too shallow to absorb the aggressive flows of traders without overreacting. The mechanism combines thin order books, fragmentation across trading platforms, heavy retail participation, jumps in attention, and the absence of a stable base of market makers for many secondary tokens. Among the largest and most liquid assets the dynamics can switch to continuation, whereas in the illiquid long tail overreaction and correction dominate more; this internal heterogeneity of the crypto market is a central point of the literature.

The effect is not fully arbitraged away because crypto spot microstructure is less stable than that of equities: variable depth, listing risk, implementation costs, slippage, operational risks and extreme heterogeneity across assets.

## Prediction

The literature shows that, in the cross-section of cryptocurrencies, the last daily return is a strong predictor: coins that have fallen sharply often outperform on the next day or over very short horizons, especially among illiquid assets, while the most liquid large coins can show continuation instead. Related work covers returns from liquidity provision in cryptocurrency markets (Farag et al. 2025), the reversal in the cryptocurrency market before and during COVID-19 (Pham et al. 2024), and Bitcoin's reactions to large price swings in stock markets (Jia et al. 2024).

## What would refute it

- No next-day outperformance, among illiquid coins, of the coins that fell sharply.
- Reversal as strong among the largest, most liquid coins as in the illiquid long tail, or continuation in the long tail.
- Reversals unrelated to order-book depth, platform fragmentation or the share of retail trading.

## References

- Zaremba, A. et al. (2021). Up or Down? Short-Term Reversal, Momentum, and Liquidity Effects in Cryptocurrency Markets. International Review of Financial Analysis.
- Farag, H. et al. (2025). Returns from Liquidity Provision in Cryptocurrency Markets.
- Pham, H. et al. (2024). The Reversal in the Cryptocurrency Market before and during COVID-19.
- Jia, B. et al. (2024). Bitcoin Market Reactions to Large Price Swings of Stock Markets.
