---
id: LL-041
title: Cross-impact
family: lead-lag and information diffusion
mechanism: [microstructure, information, limits to arbitrage]
asset_classes: [stocks, equity indices]
horizon: [intraday]
data: [tick-by-tick trades and quotes for several assets, signed order flow]
status: untouched
---

## Mechanism

Cross-impact is the mechanism by which trades in one asset also move the prices of other, correlated
assets. It links microstructure to the transmission of information across assets. Information about a
common factor, a hedge, a basket, an inventory constraint or a portfolio imbalance appears first in the
order flow of one asset and is then passed on to other assets by market makers, arbitrageurs, hedging
desks and spread-trading algorithms; high-frequency arbitrage propagates the impact of one asset to the
others.

Bouchaud stresses two points: the off-diagonal propagators, which describe the impact of trades in one
asset on the price of another, also decay over time, and a large part of the correlation between the
prices of different assets seems to be mediated by the trades themselves, rather than by a residual of
news that involves no trading. This makes cross-impact a structural mechanism of diffusion, not merely a
correlation in reduced form. It is not fully arbitraged away because hedges are executed in sequence,
venues are fragmented, inventories are limited and clocks are not synchronised.

## Prediction

Signed order flow in one asset moves the prices of the assets correlated with it, with an impact that
decays over time. A large part of the co-movement of prices across assets seems to be mediated by
trades, and the price of the second asset adjusts after the trades in the first.

## What would refute it

- Order flow in one asset has no effect on the prices of correlated assets once common news is accounted
  for.
- The correlation between asset prices is explained by news that involves no trading, with no part
  mediated by trades.
- The impact of trades in one asset on the price of another does not decay over time.

## References

- Bouchaud, Jean-Philippe, Julius Bonart, Jonathan Donier and Martin Gould (2018). Trades, Quotes and Prices: Financial Markets Under the Microscope, sec. 14.5.3 "Cross-Impact", pp. 283-284. Cambridge University Press.
- Lehalle, Charles-Albert and Sophie Laruelle (2018). Market Microstructure in Practice, 2nd edition, introduction, pp. 27-28, on the propagation of impact from one asset to others through high-frequency arbitrage. World Scientific.
