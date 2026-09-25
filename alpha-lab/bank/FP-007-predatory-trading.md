---
id: FP-007
title: Predatory trading
family: flows and positioning
mechanism: [flows, microstructure]
asset_classes: [stocks, crypto]
horizon: [intraday, days]
data: [intraday prices, trading volumes, disclosed large positions, fund flows]
status: untouched
---

## Mechanism

Some traders react not to flows themselves but to the knowledge that another participant will have
to trade whatever happens. Predatory trading is the situation in which traders anticipate that a
large player is under constraint and will have to execute a sizeable order, and position themselves
ahead of it to profit from the expected price impact. The mechanism does not assume that the
predators create the initial constraint: they exploit information about the player's vulnerability,
and the expectation that others will not be able or willing to supply enough liquidity at once.
Their trading worsens the initial price move.

In the canonical version, when the market suspects that a large holder must liquidate, informed
traders sell or withdraw liquidity before the sale, so the price falls earlier and further. The
constrained seller then obtains worse execution, which can deepen its losses and tighten its
constraints. A forced flow can therefore have an impact larger than its volume alone, because other
participants rearrange their orders around the expected flow. The forced party is less sensitive to
price, which makes the demand or supply curve abnormally steep over a short window. The trader who
identifies the constraint can either position ahead of the flow or accelerate it.

Harris describes "squeezers" as traders who act on information about trades that others must make.
The field is broad: index reconstitutions, recalls of lent securities, stop-loss orders, margin
calls, forced liquidations, cash needs, mechanical hedging, and sales caused by fund redemptions.
The phenomenon is most likely in markets where positions, funding difficulties, rebalancing dates
or distress events are fairly observable. It is not arbitraged away because information about
positions and constraints is never fully public, because exact timing matters enormously, because
leaning against a liquidation too early can be very costly, and because the predatory strategy
itself needs capital, bears timing risk and depends on how credible the presumed constraint is.

A squeeze only exists when the free float, the capacity to borrow or the effective liquidity is
constrained. Some wrappers, such as exchange-traded funds, make a short squeeze much harder;
Gastineau gives the bound that exchange-traded funds are practically impossible to corner. Predatory
trading reinforces fire sales, short squeezes and deleveraging.

## Prediction

When a large forced trade is anticipated, prices move in its direction before it is executed, and
they can move further than the volume of the forced trade alone would imply; the constrained party
trades at worse prices. The effect plays out over a short window. It can appear around large fund
outflows, index events, fund liquidations and squeezes, and around public signals about wallets or
flows in crypto. In equities it appears in episodes of squeezes, stop-loss cascades or forced
reallocations; by analogy, in crypto, the equivalent appears in chains of liquidations, collateral
unwinds and sudden outflows from exchanges.

## What would refute it

- No abnormal price move ahead of forced trades whose existence and timing are predictable.
- Forced trades having no larger price impact than voluntary trades of the same size.
- Effects as large when positions and constraints are opaque as when they are observable.
- Squeezes occurring as often where the float, borrowing capacity and liquidity are ample as where
  they are constrained.

## References

- Brunnermeier, M. and Pedersen, L. H. (2005). Predatory Trading. Journal of Finance.
- Carlin, B., Lobo, M. and Viswanathan, S. (2007). Episodic Liquidity Crises: Cooperative and Predatory Trading. Journal of Finance.
- Harris, L. (2002). Trading and Exchanges: Market Microstructure for Practitioners. Oxford University Press. Chap. 8, pp. 195-196.
- Pedersen, L. H. (2015). Efficiently Inefficient: How Smart Money Invests and Market Prices Are Determined. Princeton University Press. Chap. 5, pp. 83-84.
- Shleifer, A. (2000). Inefficient Markets: An Introduction to Behavioral Finance. Oxford University Press. Chap. 6, pp. 154-157.
- Gastineau, G. (2004). Chapter 4 in Fabozzi, F. J. (ed.), Short Selling: Strategies, Risks, and Rewards. Wiley. Pp. 38-39.
