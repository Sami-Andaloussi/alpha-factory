---
id: LL-006
title: Stealth trading
family: lead-lag and information diffusion
mechanism: [information, microstructure]
asset_classes: [stocks]
horizon: [intraday, days]
data: [tick-by-tick trades and quotes, order sizes, hidden orders]
status: untouched
---

## Mechanism

Informed traders, and traders whose orders would have a large market impact, choose to trade slowly, to
split their orders and to reveal as little information as possible while executing. The economic reason
is that revealing private information, or a large intention to buy or sell, at once destroys the
trader's own informational rent by moving the price against them. Traders therefore optimise a trade-off
between speed and camouflage.

This behaviour mechanically creates non-simultaneous diffusion: the information exists before it is
fully reflected in prices, but it is released gradually through the child orders. Harris treats
stealth trading as a rational strategy of informed traders; Hasbrouck links it to strategic trading
models of the Kyle type; Lehalle and Laruelle show that it extends in practice to liquidity-seeking
algorithms and to the use of market fragmentation to reduce information leakage.

The behaviour persists because displayed liquidity is small compared with the sizes traders actually
want to trade, because impact costs are convex, and because markets punish orders that are too visible.

## Prediction

Private information and large trading intentions reach prices gradually, over the execution of split
orders, rather than at once. The behaviour shows up in observed order splitting, in the use of hidden
liquidity and in execution profiles. In the simplest strategic models, total order flow can remain hard
to predict at short horizons despite the splitting, because the informed trader hides behind noise
trading.

## What would refute it

- Informed traders and traders with large orders execute in single visible blocks rather than splitting
  their orders over time.
- Private information is fully reflected in prices at the first child order, so that the rest of the
  execution moves prices no further.
- Order splitting and hidden liquidity are unrelated to the size of the intended position or to the
  information the trader holds.

## References

- Harris, Larry (2002). Trading and Exchanges: Market Microstructure for Practitioners, ch. 10 "Informed Traders and Market Efficiency", pp. 226-228. Oxford University Press.
- Hasbrouck, Joel (2007). Empirical Market Microstructure: The Institutions, Economics, and Econometrics of Securities Trading, ch. 7 "Strategic Trade Models", pp. 65-66. Oxford University Press.
- Lehalle, Charles-Albert and Sophie Laruelle (2018). Market Microstructure in Practice, 2nd edition, ch. 3 "Optimal Organizations for Optimal Trading", pp. 229-230. World Scientific.
