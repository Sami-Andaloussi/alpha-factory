---
id: FP-003
title: Metaorders, order splitting and latent liquidity
family: flows and positioning
mechanism: [microstructure, flows]
asset_classes: [stocks, equity indices, crypto]
horizon: [intraday, days, weeks]
data: [trade and quote data, metaorder execution records, signed market orders, limit order book data, order imbalances, trading volumes, index rebalancing dates]
status: untouched
---

## Mechanism

A large institutional order is generally not executed at once. It is split into a sequence of child
orders to reduce its market impact, because the visible liquidity is only a small fraction of the
liquidity actually available. This splitting produces persistent directional pressure: often
discreet at the level of each trade, but powerful once aggregated. The long-range persistence of
order flow is the aggregate, observable form of stealth trading and metaorders, and the splitting of
large parent orders into long series of child orders, sometimes reinforced by herding, is its
favoured explanation: Bouchaud and his co-authors document that the signs of market orders are
positively autocorrelated over very long sequences, buys following buys and sells following sells,
often over horizons far longer than white noise would allow. Dealers and other liquidity providers
learn from the order flow, but they cannot tell immediately whether it is informed or driven only by
a need for liquidity. Prices therefore move progressively in the net direction of purchases or
sales. The books also stress that the price change is path-dependent: the same net volume does not
have the same effect depending on the sequence of the orders. When information or a trading
intention is executed in stages, its diffusion into prices, and across linked assets, is necessarily
gradual.

Bouchaud also shows that the persistence creates an apparent paradox of efficiency: for prices to
remain roughly diffusive while order signs are so predictable, the impact has to decay, or be offset
by the resilience of the order book.

The mechanism is not fully arbitraged for several reasons. A trader who leans against it too early
risks being crushed by the part of the parent order that has not yet been executed. The parent order
cannot be seen, and the displayed depth does not reveal the true size of the flow. Latent liquidity
only appears as the price moves, and liquidity providers react late or change their supply only
gradually. The persistence is itself produced by impact costs, adverse selection and the imperfect
observation of order flow. The conditions for the effect are a need to trade in size, a constraint
on execution, and insufficient instantaneous depth.

The phenomenon has been documented mainly in equities, and the mechanism is particularly plausible
in equity futures, exchange-traded funds and other electronic markets; by analogy, it can carry over
to large crypto spot order books whenever an execution algorithm spreads a big order over time. The
metaorder is often the concrete form taken by institutional flows, index rebalancing, ETF creations
and redemptions, or fund outflows. It gives an economic basis to part of the continuation observed
from very short to medium horizons, particularly in less liquid stocks, around portfolio
rebalancings and during institutional executions. It does not claim that all momentum is
microstructural, only that a non-negligible component can come from the inertia of price impact and
from the difficulty the market has in separating information from liquidity needs. Not every price
rise tied to a metaorder carries information about value.

## Prediction

The signs of successive orders are autocorrelated, and the autocorrelation decays slowly, over long
sequences of trades; the literature shows that the persistence can last days or even weeks. Net
order imbalances, and the price moves they cause, continue in the same direction over the following
trades, days and weeks while large orders are being executed: the price impact of a metaorder builds
up during its execution, and the effect is stronger in less liquid stocks, around rebalancing dates
and during periods of heavy institutional execution. The literature also shows that the aggregate
price impact of a metaorder is a concave function of its size, typically close to a square-root law
rather than a linear one. As the books stress, the impact of a given net volume depends on the
sequence in which the orders arrive. Part of the impact decays after the metaorder ends, so prices
partly revert once execution is complete. The predictability of order flow does not translate
one-for-one into predictability of raw returns, because liquidity adjusts endogenously: the impact
of each trade decays or is absorbed by the resilience of the book. The information carried by these
orders diffuses gradually into prices and into the prices of linked assets. These patterns concern
stocks and, where the mechanism is particularly plausible, equity futures, exchange-traded funds and
other electronic markets; by analogy, they concern large crypto spot order books.

## What would refute it

- Order signs with no autocorrelation beyond the very short term, as with white noise, or a sign
  persistence that does not come from the splitting of parent orders into child orders.
- Order imbalances that are fully reflected in prices at once, with no subsequent drift in their
  direction; no relation between the execution of large split orders and the continuation of
  returns; the same effect in liquid and illiquid stocks, and no concentration around rebalancings
  and institutional executions.
- An aggregate impact that grows linearly, or not at all, with the size of the metaorder; price
  impact that depends only on net volume and not on the order sequence; large orders executed in one
  block with the same impact as the same quantity split over time.
- No decay of impact after the end of metaorders, or a full reversal that leaves no lasting impact
  at all.
- Returns as predictable as order signs, with no decay of impact and no resilience of the order
  book, contradicting the endogenous adjustment of liquidity.
- Information executed in stages that is nonetheless reflected at once in the prices of the traded
  asset and of linked assets.

## References

- Bouchaud, Jean-Philippe, Julius Bonart, Jonathan Donier and Martin Gould (2018). Trades, Quotes and Prices: Financial Markets Under the Microscope, ch. 10, p. 162; ch. 10 "Long-Range Persistence of Order Flow", pp. 187-220; ch. 10.4-10.5, pp. 193-198; ch. 12, pp. 239-241; ch. 12 "The Impact of Metaorders", pp. 248-260; ch. 13 "The Propagator Model", pp. 268-286. Cambridge University Press.
- Hasbrouck, Joel (2007). Empirical Market Microstructure: The Institutions, Economics, and Econometrics of Securities Trading, ch. 7, pp. 65-66, for the strategic root of order slicing; ch. 15, pp. 155-156. Oxford University Press.
- Harris, Larry (2002). Trading and Exchanges: Market Microstructure for Practitioners, ch. 10, pp. 226-228, for the logic of stealth trading; ch. 10, 15 and 21, on price impact, the role of order flow and path dependence, PDF pp. 321-359, 337-338 and 427-448. Oxford University Press.
- Glosten, L. R. & Harris, L. E. (1988). Estimating the Components of the Bid/Ask Spread. Journal of Financial Economics.
- O'Hara, M. (1995). Market Microstructure Theory. Blackwell.
- Hasbrouck, J. & Seppi, D. J. (2001). Common Factors in Prices, Order Flows, and Liquidity. Journal of Financial Economics.
- Campbell, J. Y., Lo, A. W. & MacKinlay, A. C. (1997). The Econometrics of Financial Markets. Princeton University Press. Orders, transactions and event studies, PDF pp. 77-80.
- Lo, A. W. & MacKinlay, A. C. (1999). A Non-Random Walk Down Wall Street. Princeton University Press. Chap. 10-12, on price impact and order imbalances, PDF pp. 299-359.
- Bali, T. G., Engle, R. F. & Murray, S. (2016). Empirical Asset Pricing: The Cross Section of Stock Returns. Wiley. Price impact and order flow, PDF pp. 295 and 329-337.
