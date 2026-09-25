---
id: MR-037
title: Temporary deviations from arbitrage prices
family: mean reversion and relative value
mechanism: [limits to arbitrage, structural]
asset_classes: [stocks, equity indices, bonds, commodities, currencies]
horizon: [days, weeks, months]
data: [dual-listed share prices, options prices, index futures prices, spot index prices, margin requirements]
status: untouched
---

## Mechanism

Two assets or structures that should respect a clear economic parity can deviate from each other temporarily. The principle is no-arbitrage: identical cash flows should command the same price. Yet the books show that temporary deviations exist between the two lines of dual-listed companies, in put-call parity and in futures/cash relations. The mechanism does not contradict arbitrage theory but completes it: the parity is the restoring force, but the adjustment is imperfect because arbitrage must be financed, executed and margined, sometimes hedged across several markets, and sometimes carried out with securities that are not perfectly fungible. Settlement constraints, the fragmentation of trading venues, timing risk, the availability of counterparties and the cost of margin allow deviations that are not negligible.

The parity gives a strong anchor, contractual or quasi-contractual, rather than a mere statistical average. The costlier or riskier the arbitrage, the wider the admissible gap. The mechanism connects naturally to threshold cointegration: the spread does not revert continuously, but mostly when the deviation becomes large enough to pay for all the frictions.

## Prediction

Prices of assets linked by a parity (the two lines of dual-listed "Siamese twin" companies, options and their underlying through put-call parity, futures and their cash market) deviate from the parity, and the deviations revert. Deviations are wider where arbitrage is more costly or risky, and they can become remarkable during episodes of liquidity stress. Market Liquidity cites Deville and Riva (2007) on put-call parity and de Jong, Rosenthal and van Dijk (2009) on dual-listed "Siamese twins"; Tsay (2010) discusses index arbitrage between S&P 500 futures and cash, and Hasbrouck (2007) linked prices, known bases and practical cointegrating vectors.

## What would refute it

- Deviations from parity that do not revert.
- Deviation sizes unrelated to the costs and risks of arbitrage: funding, margin, settlement constraints, fragmentation of venues.
- No widening of deviations during episodes of liquidity stress.
- Reversion that occurs continuously even for small deviations, rather than mostly once the deviation pays for the frictions.

## References

- Market Liquidity (authors and year not specified). P. 17, section on temporary deviations from arbitrage prices.
- Tsay, R. S. (2010). Analysis of Financial Time Series (3rd edition). Wiley. Pp. 443-445 on index arbitrage between S&P 500 futures and cash.
- Hasbrouck, J. (2007). Empirical Market Microstructure. Oxford University Press. Pp. 103-104 on linked prices, known bases and practical cointegrating vectors.
- Deville, L. and Riva, F. (2007). Liquidity and Arbitrage in Options Markets: A Survival Analysis Approach. Review of Finance.
- de Jong, A., Rosenthal, L. and van Dijk, M. A. (2009). The Risk and Return of Arbitrage in Dual-Listed Companies. Review of Finance.
