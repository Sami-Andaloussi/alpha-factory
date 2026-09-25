---
id: MR-025
title: Limits to arbitrage
family: mean reversion and relative value
mechanism: [limits to arbitrage, behavioural, flows]
asset_classes: [stocks, equity indices, bonds, commodities, currencies, crypto]
horizon: [days, weeks, months]
data: [daily prices, relative value spreads, fund flows, margin requirements, funding spreads, closed-end fund prices and net asset values, investor sentiment measures, market capitalisation, trading volumes, short interest, securities lending fees, hedge fund flows, hedge fund returns]
status: untouched
---

## Mechanism

Mispricings can persist, and sometimes worsen, even though arbitrage exists in theory. The point is
not that arbitrageurs ignore the gap but that they cannot always absorb it, or not fast enough.
Ilmanen explains that arbitrage is riskless only in the limiting case of perfect substitutes and
frictionless markets; in practice most arbitrages are "good deals" that can go against the
arbitrageur before they pay off. Real arbitrage bears fundamental risk, noise-trader risk, funding
risk, redemption risk, margin risk, and the risk that the spread widens before it normalises.

The noise-trader approach serves as the mechanistic foundation (De Long, Shleifer, Summers and
Waldmann 1990; Shleifer and Summers 1990). Irrational but persistent sentiment, fed by false
rumours, the media or noise traders, creates a risk for arbitrageurs. Noise traders hold erroneous
but stochastic beliefs: they can push prices in one direction and hold them at wrong levels for long
periods, and their beliefs can become more extreme and push the mispricing wider before it corrects.
Even rational investors who recognise that an asset is underpriced or overpriced therefore face the
risk of an adverse continuation before the correction: the risk of further flows and sentiment, the
risk of liquidation and the risk of underperformance. Rational arbitrageurs are risk-averse and
limit the size of their positions, which lets the gaps persist: a mispricing can widen before it
closes. As a result, the imbalances last and translate into a structural momentum.

Shleifer and Vishny (1997) discuss the general limits: transaction costs, and constraints of
leverage and of time, which prevent the quick elimination of anomalies. Real arbitrage consumes
capital and risk capacity, carries fundamental and non-fundamental risks, and is often carried out
by professional arbitrageurs with other people's money, which brings agency frictions: withdrawals,
mandate constraints, relative-performance risk. When positions move against them, their investors
and lenders do not observe the quality of the trade directly; they observe poor performance, and
they may withdraw capital, refuse to add more, or cut the leverage they grant, precisely when the
mispricing has become more attractive. Shleifer calls this "performance-based arbitrage": the
arbitrageur is forced to cut the position exactly when the opportunity is largest, and becomes a
seller when prices move further away from fundamental value, which widens the dislocation instead of
correcting it. This persists because of the principal-agent relation, the opacity of the strategies,
and the fact that investors update their beliefs about a manager's competence from past returns.
Arbitrage is not riskless when the horizon is finite, funding is constrained, performance is marked
to market and investors are evaluated over short periods: a manager can be right in the end and
still be forced to cut the position before convergence, and arbitrageurs with short horizons or
drawdown limits are forced out before the correction.

The other limits are transaction costs, which in illiquid markets cancel part or all of the signal,
and the frictions the books stress: short-selling constraints, the availability and cost of
borrowing stock, which prevent pessimists from expressing their views; the costs of information and
of risk management; and differences of opinion, which can keep valuations too high when optimists
dominate the long positions. The dynamic mechanism runs through funding: when funding deteriorates,
liquidity providers and leveraged funds must deleverage, which widens the gap further. Broad-based
redemptions and the forced liquidation of long/short portfolios are particularly destructive for
convergence trades, because they hit both legs of the spread at once. When several funds hold
similar positions, the result is crowding and synchronised unwinds: in the quant episode of August
2007, as described by Pedersen, "cheap got cheaper, expensive got more expensive" under the pressure
of liquidations by other quantitative funds. The mechanism thus feeds fire sales, liquidity spirals
and contagion between strategies. In futures markets short-sale constraints often bind less severely
than in cash equities, but limits on capacity, leverage, variation margin and correlations in crises
remain: with high leverage, noise-trader-driven overshoots and fragile margins can stop arbitrageurs
out before convergence, and convergence trades can be structurally attractive yet vulnerable to
margin calls and to the timing of liquidation. Limits to arbitrage and slow-moving capital are two
faces of the same phenomenon: the participants able to correct mispricings cannot do it immediately,
which maintains trends.

The limits to arbitrage do not create mean reversion or continuation by themselves, but they explain
why the correction of a mispricing is
not instantaneous and why gaps can recur, why signals arising from other mechanisms (reversion,
underreaction, trends) are not trivially arbitraged away, and why so many mean-reversion and
relative-value phenomena have long half-lives and potentially large drawdowns along the way. A gap
to value is not enough; the capacity of the market to stay irrational or constrained matters as
well. Shleifer and Vishny (1997) model the phenomenon and show that under these constraints
significant mispricings can persist for a long time, even in a market populated by rational agents.
When an informational or flow-driven pressure pushes prices, arbitrageurs may be unable, or not
motivated, to trade against it early enough and in sufficient size, which lets a trend develop over
an intermediate window; momentum can emerge as an episode in which the directional pressure of noise
traders spreads, through imitation, attention and extrapolation, faster than arbitrageurs can
neutralise it. The limits are also a source of deviations: forced sales, the unwinding of crowded
positions, fire sales and liquidity spirals create temporary deviations that are sometimes much
larger than fundamentals justify. The later reversal comes when balance sheets become available
again, when redemption pressure fades, or when longer-horizon investors finally absorb the shock:
the phenomenon is fully mean-reverting, but with a more violent and slower dynamic than a simple
transitory shock. The principle cuts across all asset classes, crypto-assets being a frequent
illustration of noise risk.

## Prediction

Mispricings driven by noise-trader sentiment can persist, sometimes widen before they converge, and
correct later rather than at once; the duration of a mispricing varies with the duration of the
sentiment that drives it. Relative spreads that look cheap can become cheaper still before they
recover: deviations widen when funding deteriorates, when arbitrage funds lose money and face
withdrawals and leverage cuts, and when leveraged holders deleverage; funds holding similar
positions unwind at the same time, so that cheap securities get cheaper and expensive ones more
expensive; and the deviations reverse when balance sheets, capital and longer-horizon buyers return.
These overshoots last from several days to several weeks, or from days to months around drawdowns.
Anomalies, continuation patterns included, can persist; momentum is stronger and more durable where
the limits bind more: in small capitalisations, in illiquid markets and where short selling is
constrained.

The theory applies to closed-end funds, vehicles whose net asset value is observable (Lee, Shleifer
and Thaler 1991; Pontiff 1996), and more widely to value against growth, crowded trades, benchmark
dislocations, sector euphorias, squeezes and some retail-dominated episodes in crypto markets.
Transaction costs, risk aversion and redemptions limit the correction of gaps. Tests of noise
effects and theoretical models, among them De Long et al. (1990), show that the absence of perfect
information can generate persistent autocorrelations.

## What would refute it

- Identified mispricings that close at once, without ever widening first, whatever the state of
  funding; mispricings driven by sentiment that close quickly even when arbitrage capital is scarce
  or has recently suffered losses.
- Deviations from value unrelated to measures of noise-trader sentiment; closed-end fund discounts
  that close at once.
- Arbitrageurs whose position sizes show no sensitivity to the risk that the mispricing widens;
  arbitrageurs who trade against trends early and in size, or increase their positions as
  mispricings widen during drawdowns, without being forced out by interim losses or redemptions.
- Capital flowing into arbitrage funds, rather than out, after they lose money on widening
  mispricings; no further widening of mispricings when arbitrageurs suffer losses and withdrawals,
  or when funding deteriorates and margins rise; unwinds that are not synchronised across funds
  holding similar positions.
- Convergence trades unaffected by broad-based redemptions and by the forced liquidation of
  long/short portfolios; no reversal once funding stress eases and balance sheets become available
  again.
- Momentum no stronger in small, illiquid or hard-to-short securities than in large, liquid and
  easily shorted ones; removal of short-sale constraints leaving the persistence of overvaluation
  unchanged.

## References

- Shleifer, A. and Vishny, R. W. (1997). The Limits of Arbitrage. Journal of Finance.
- Brunnermeier, M. K. and Pedersen, L. H. (2009). Market Liquidity and Funding Liquidity. Review of Financial Studies.
- Ilmanen, A. (2011). Expected Returns: An Investor's Guide to Harvesting Market Rewards. Wiley. Chap. 6, Behavioral Finance, section Limits to Arbitrage, pp. 135-137; pp. 149-150, 186-187, 529, 534 and 544.
- Market Liquidity (authors and year not specified). Pp. 17-19 and 336-339.
- Pole, A. (2007). Statistical Arbitrage: Algorithmic Trading Insights and Techniques. Wiley. Pp. 141-150 and 175-177.
- Narang, R. K. (year and edition not specified). Inside the Black Box. Wiley. Pp. 202 and 229.
- De Long, J. B., Shleifer, A., Summers, L. H. and Waldmann, R. J. (1990). Noise Trader Risk in Financial Markets. Journal of Political Economy.
- Shleifer, A. and Summers, L. H. (1990). The Noise Trader Approach to Finance. Journal of Economic Perspectives.
- Lee, C. M. C., Shleifer, A. and Thaler, R. H. (1991). Investor Sentiment and the Closed-End Fund Puzzle. Journal of Finance.
- Pontiff, J. (1996). Costly Arbitrage: Evidence from Closed-End Funds. Quarterly Journal of Economics.
- Chen, J., Hong, H. and Stein, J. C. (2002). Breadth of Ownership and Stock Returns. Journal of Financial Economics.
- Jones, C. M. and Lamont, O. A. (2002). Short-Sale Constraints and Stock Returns. Journal of Financial Economics.
- Gromb, D. and Vayanos, D. (2010). Limits of Arbitrage: The State of the Theory. Annual Review of Financial Economics.
- Thaler, R. H. (ed.) (2005). Advances in Behavioral Finance, Volume II. Princeton University Press. Chap. 2, The Limits of Arbitrage, p. 104; chap. 1, pp. 29-35 and 71-72.
- Gray, W. R. and Vogel, J. R. (2016). Quantitative Momentum: A Practitioner's Guide to Building a Momentum-Based Stock Selection System. Wiley. Preface, pp. ix-x; chap. 2, Why Can Active Investment Strategies Work?, pp. 33-39; chap. 3-4.
- Shleifer, A. (2000). Inefficient Markets: An Introduction to Behavioral Finance. Oxford University Press. Chap. 4, pp. 89-107, and the postscript on LTCM, pp. 108-111.
- Pedersen, L. H. (2015). Efficiently Inefficient: How Smart Money Invests and Market Prices Are Determined. Princeton University Press. Preface, pp. xii-xiv.
- Cumming, D., Dai, N. and Johan, S. (2013). Hedge Fund Structure, Regulation, and Performance around the World. Oxford University Press. Chap. 10, pp. 278 ff.
