---
id: FP-002
title: Dealer inventory pressure
family: flows and positioning
mechanism: [microstructure, limits to arbitrage]
asset_classes: [stocks, equity indices, bonds, commodities, currencies, crypto]
horizon: [intraday, days, weeks]
data: [trade and quote data, order book depth, dealer inventories, trading volumes]
status: untouched
---

## Mechanism

Dealers, market makers and other liquidity providers do not absorb order flow neutrally: they try
to keep their inventory manageable. In inventory models, liquidity providers temporarily absorb
one-sided client flows and end up holding an unwanted inventory that is risky and costly to carry. A
dealer has a preferred level, or at least a comfort zone, because carrying a position ties up
capital, raises its mark-to-market risk and can exceed its funding capacity or internal limits. When
dealers become too long or too short, they change their quotes, the width of the spread, the depth
or sizes they display, or their aggressiveness, so as to make one side of the market more attractive
and attract flow in the opposite direction: a dealer who is too long lowers its quotes to attract
buyers and discourage sellers, and one who is too short does the opposite. The observed price
therefore reflects not only fundamental information but also the balance-sheet and risk-management
constraints of the intermediaries: it moves away from the efficient price for inventory reasons,
then partly returns when the inventory normalises. This creates a transitory component in prices,
distinct from fundamental information.

The mechanism is structural. It depends neither on faulty psychology nor on a sophisticated
valuation model, but on the fact that providing liquidity consumes balance sheet, capital and risk
limits; dislocations can exist without any irrationality, provided balance sheets are scarce. When
liquidity shocks (investors who must trade quickly) meet market makers who accept to carry the
inventory for a while, price setters push the price beyond its instantaneous fundamental level, both
to be compensated for the inventory risk and to attract offsetting flow. The price thus temporarily
includes a premium for absorbing the flow, and it reverts as this stock of risk is gradually passed
on to final counterparties. The correction is not immediate: the dealer first absorbs the shock,
then adjusts prices to elicit the counterparty it needs.

The effect requires market makers who are averse to inventory risk, as in the models of Garman
(1976), Amihud and Mendelson (1980) and Ho and Stoll (1981), and markets that are thin or
temporarily one-directional. It is larger when liquidity is limited, when few intermediaries carry
the risk, when order-book depth is low, and when volatility or the cost of carrying inventory is
high; it can be neutralised quickly when several liquidity providers have ample balance sheet, and
it disappears if market makers can hedge instantly in other markets or with derivatives. It persists
because market-making capital is costly, risk limits are binding, funding is risky and transactions
are costly, so intermediaries cannot absorb a one-way flow indefinitely. On electronic markets the
main agents are active liquidity providers, high-frequency traders and market makers, and the effect
applies particularly to markets where a large share of liquidity comes from intermediaries who
explicitly use their balance sheets to smooth orders. In equities it shows in the episodes where
market makers step back or shade their quotes. By analogy, in crypto, it shows on fragmented order
books, or during bouts of volatility in which market makers abruptly cut the depth they offer. In
periods of stress the pressure combines with fire sales and becomes non-linear. Inventory pressure
partly counterbalances the persistence of order flow, but it also becomes a channel of propagation
once absorption is no longer possible. It is related to the bid-ask bounce, the Glosten-Milgrom
model, the price pressure of large orders and transitory price impact.

## Prediction

After absorbing a one-sided flow, dealers move their quotes and depth against their inventory, and
prices deviate temporarily in the direction of the flow, then partly revert as the inventory is
worked off and returns to target: if a large seller forces a dealer to accumulate stock, the dealer
concedes on price to unload it, and the price rises again when the inventory is back near its
target. An asset pushed down temporarily by an inventory imbalance can thus rise again even without
further fundamental news. The deviations are larger when liquidity is scarce, when inventory is
costly to carry, and when volatility is high. The speed of reversion depends on the size of the
accumulated inventory and on the overall liquidity of the market; it is faster in very competitive
markets with several market makers, and it depends on dealers' balance-sheet capacity, their access
to funding, volatility and competition among liquidity providers. The phenomenon is mainly intraday;
its natural horizon runs from intraday to a few days, depending on how fast the inventory can be
recycled. The model was developed on stocks; by analogy, the argument carries over to futures, where
market makers and proprietary trading firms supply immediacy, above all over horizons of days to
weeks when constrained flows must be absorbed. It concerns stocks and, by analogy, the order books
of crypto venues.

The inventory model also explains why serial correlation can depend on trading activity: on
high-volume days associated with non-informational trades, return autocorrelation becomes less
positive, or even negative, because a larger part of the move is transitory. Inventory effects have
been documented empirically in the trades of NYSE specialists (Hasbrouck and Sofianos 1993).

## What would refute it

- Quotes and displayed depth that do not respond to the size or sign of intermediaries' inventory.
- Flow-driven price deviations that show no partial reversal as inventories are unwound; prices that
  do not revert after dealers absorb large one-sided flows.
- Price deviations no larger when liquidity is scarce or inventory is costly to carry than when
  several liquidity providers have ample balance sheet; a reversion speed unrelated to the number of
  competing market makers, to dealers' balance-sheet and funding capacity, or to volatility.
- Inventory-driven price distortions that persist where dealers can hedge instantly in other
  markets.
- Stress episodes in which market makers keep their depth and the price response to one-sided flow
  stays linear.
- High-volume days with non-informational trading that do not show lower return autocorrelation.
- Price falls that follow dealers' inventory accumulation and never recover, showing them to be
  informative.

## References

- Hasbrouck, J. (2007). Empirical Market Microstructure: The Institutions, Economics, and Econometrics of Securities Trading. Oxford University Press. Chap. 7, inventory control (Garman, Amihud-Mendelson), pp. 90-115 approx.; chap. 11, "Dealers and Their Inventories", pp. 106-117; chap. 15, pp. 155-156, on the link between execution cost, sequencing and the gradual relief of inventory.
- Bouchaud, J.-P., Bonart, J., Donier, J. and Gould, M. (2018). Trades, Quotes and Prices: Financial Markets Under the Microscope. Cambridge University Press. Chap. 10.3, pp. 191-193.
- de Jong, F. and Rindi, B. (2009). The Microstructure of Financial Markets. Cambridge University Press. Chap. 5, "Inventory Models", p. 89 ff.; chap. 6, "Empirical Inventory Models", p. 116 ff.
- Harris, L. (2002). Trading and Exchanges: Market Microstructure for Practitioners. Oxford University Press. Section 13.6.1, "How Dealers Control Their Inventories", p. 284 ff.; chap. 19, "Liquidity", pp. 407-420, notably the example of the specialist who adjusts quotes after absorbing a large order.
- Cartea, Á., Jaimungal, S. and Penalva, J. (2015). Algorithmic and High-Frequency Trading. Cambridge University Press. Chap. 10, "Market Making", p. 263 ff.
- Foucault, T., Pagano, M. and Röell, A. (2013). Market Liquidity: Theory, Evidence, and Policy. Oxford University Press. Chapter "Order Flow, Liquidity, and Securities Price Dynamics", p. 79 ff.; the chapter on inventory and midprice reversion, pp. 80-130 approx.
- Market Liquidity (authors and year not specified). Pp. 18-19, on the link between funding liquidity and market makers' capacity.
- Grossman, S. J. and Miller, M. H. (1988). Liquidity and Market Structure. Journal of Finance.
- Campbell, J. Y., Grossman, S. J. and Wang, J. (1993). Trading Volume and Serial Correlation in Stock Returns. Quarterly Journal of Economics.
- Garman, M. B. (1976). Market Microstructure. Journal of Financial Economics.
- Amihud, Y. and Mendelson, H. (1980). Dealership Market: Market-Making with Inventory. Journal of Financial Economics.
- Ho, T. and Stoll, H. R. (1981). Optimal Dealer Pricing under Transactions and Return Uncertainty. Journal of Financial Economics.
- Hasbrouck, J. and Sofianos, G. (1993). The Trades of Market Makers: An Empirical Analysis of NYSE Specialists. Journal of Finance.
