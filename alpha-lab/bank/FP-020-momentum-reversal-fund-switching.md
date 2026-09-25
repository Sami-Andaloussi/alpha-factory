---
id: FP-020
title: Momentum and reversal from fund switching
family: flows and positioning
mechanism: [flows, limits to arbitrage, behavioural]
asset_classes: [stocks, crypto]
horizon: [weeks, months]
data: [fund flows, fund returns, fund holdings, institutional holdings, subscriptions and redemptions, monthly returns, daily prices, valuation ratios, stablecoin flows]
status: untouched
---

## Mechanism

End investors move their capital out of funds that have recently lost and into funds that have
recently won. The managers of the winning funds receive inflows and must buy; the losing funds face
redemptions and must sell. The securities held by the former can keep rising and those held by the
latter can keep falling, with no new fundamental information. Over time, part of these moves can
unwind as the flows return to normal. The mechanism links the relative performance of funds, the
allocation behaviour of their clients, and the comovement of securities according to who owns them;
it has been formalised as an engine of momentum and of reversal at different horizons.

Vayanos and Woolley (2013) formalise this as an institutional theory of momentum and reversal in a
world of delegated portfolio management. When a fund outperforms, for instance because an asset it
holds has risen strongly, or when a manager improves its performance, a signal of effectiveness,
investors progressively allocate more capital to it; an underperforming fund sees slow, late
withdrawals. Investors also reallocate progressively between active and index funds. Their flows are
inertial: they depend on past performance but arrive with a delay, because reallocating capital
takes time and has costs. When an asset has outperformed recently, investors' attention to the fund
pushes its price up further. Prices, even when they are set rationally, underreact to these
anticipated future flows: investors foresee the flows but do not yet have the capital, so today's
price incorporates only part of the expected effect of the inflows. When the capital actually flows
in, it keeps pushing the winners' prices up, and the trend continues as long as the expected flows
have not been incorporated. A change in performance thus generates asymmetric flows and an ex ante
underreaction. The same flows explain later reversals: they can push prices far from fundamentals,
and the subsequent opposite flows bring prices back towards fundamental value, which gives momentum
its cyclical character. The key actors are fund managers, whose holdings are underweight or
overweight relative to their benchmark, and the end investors who allocate to them.

Because the expected component of the flows is predictable, part of future returns is predictable
too: the chain runs from flows to the trades they induce, to price pressure, to drift (Lou 2012).
The pressure later dissipates and prices reverse, so a transient price pressure can mimic momentum
over a given window without being a structural trend.

The flows are a source of non-fundamental price pressure. Retail or less sophisticated investors
often allocate capital after good past performance, through funds and other collective vehicles.
They do not necessarily buy the stock directly: they fund managers who, by operational inertia,
scale up the positions they already hold, which creates positive contemporaneous pressure on prices,
followed by lower future returns as the excess demand fades. This side of the mechanism rests on
performance chasing, naive extrapolation, attention seeking and delegation. It bridges behavioural
finance and institutional microstructure: investors' extrapolative beliefs feed an effective demand
that distorts prices. It is not purely behavioural in the psychological sense, because it has a
mechanical translation in flows. It is close to fire sales, but on the side of euphoria rather than
distress.

The mechanism is not fully arbitraged because it stems from the constraints of delegation and from
the search behaviour of end investors, not from a disagreement that could easily be traded on.
Client flows are slow, autocorrelated and hard to arbitrage perfectly. Arbitrage against flow-driven
pressure is risky, in timing and in capital, and standing against retail or benchmarked demand too
early can be very costly; the structure of holdings and the overlap between fund portfolios make the
aggregate pressure hard to neutralise. The convex relation between flows and performance, herding
and benchmarking can reinforce it. The theory is essentially one of equities and pooled asset
management; by analogy, its intuition extends to any market in which competing pools of capital
attract flows according to their displayed performance. By analogy, the logic can extend to crypto
spot, where the retail base has historically been larger and delegation through platforms, baskets
and stablecoin inflows plays a major role.

## Prediction

Securities held by funds that have recently outperformed continue to rise, and those held by funds
that have recently underperformed continue to fall, while the delayed flows arrive: securities held
by funds expected to receive inflows, given the inertia of flows, earn positive returns over the
following months, and those held by funds expected to suffer outflows earn negative returns. The
flow phase can create a continuation over a few weeks or months; the horizon is of the order of a
few months, from the generation of the flows to their full execution. As the pressure dissipates and
the flows normalise, part of these moves reverses towards fundamentals. Securities owned by the same
funds comove. The effect concerns in particular large capitalisations and long-only strategies.

Stocks that receive heavy buying from funds with large inflows show positive contemporaneous price
pressure, followed by lower returns as the excess demand fades. The literature links this to the
value premium: "loved", over-funded stocks tend to be growth stocks, expensive and heavily held
after inflows, and they subsequently show lower returns.

## What would refute it

- Fund flows that respond immediately to performance rather than with a lag, or that do not respond
  to past performance at all; fund flows without inertia, so that the expected component of the
  flows carries no information.
- Prices that fully incorporate expected future flows, so that the returns of securities held by
  recently winning or losing funds show no continuation while capital switches between them.
- Trades induced by flows that leave no trace in the prices of the securities held; fund flows
  unrelated to the subsequent returns of the stocks the funds hold.
- No subsequent reversal once the flows normalise: stocks bought with the money of fund inflows that
  do not underperform afterwards, or flow-driven price pressure that is fully permanent.
- Continuation and reversal patterns unrelated to the flows between funds, equally strong in
  securities that funds do not hold; momentum unrelated to the flow-induced trades of the funds
  holding the securities.
- No relation between flow-driven ownership and growth or valuation characteristics.

## References

- Vayanos, D. and Woolley, P. (2013). An Institutional Theory of Momentum and Reversal. Review of Financial Studies.
- Lou, D. (2012). A Flow-Based Explanation for Return Predictability. Review of Financial Studies.
- Frazzini, A. and Lamont, O. A. (2008). Dumb Money: Mutual Fund Flows and the Cross-Section of Stock Returns. Journal of Financial Economics.
- Coval, J. and Stafford, E. (2007). Asset Fire Sales (and Purchases) in Equity Markets. Journal of Financial Economics.
- Akbas, F. et al. (2015). Smart Money, Dumb Money, and Capital Market Anomalies. Journal of Financial Economics.
