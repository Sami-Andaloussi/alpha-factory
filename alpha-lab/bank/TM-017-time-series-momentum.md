---
id: TM-017
title: Time-series momentum (trend following, absolute momentum)
family: trend and momentum
mechanism: [behavioural, information, flows, limits to arbitrage, risk premium]
asset_classes: [equity indices, bonds, currencies, commodities]
horizon: [days, weeks, months]
data: [daily prices, futures positioning reports]
status: in-progress
---

## Mechanism

Time-series momentum is the tendency of an asset to keep moving in the direction of its own past
return over an intermediate horizon. The signal does not compare an asset with other assets: it is
built on the instrument's own history, typically the sign, and sometimes the size, of its past
return. In its standard form, a positive return over the past 12 months calls for a long position
and a negative one for a short position. It is the core of managed-futures trend following: buy the
markets whose trend is up, sell those whose trend is down, let winners run and cut losers. It is
distinct from cross-sectional momentum, which ranks assets against each other; the two can coexist
and complement each other.

The mechanism is composite rather than a single closed theory. The first channel is underreaction.
When new fundamental information arrives (a monetary policy shock, a macroeconomic release, a supply
shock in a commodity), prices do not absorb it at once: the most reactive traders, informed
institutions, reposition first, and the information spreads slowly to the rest of the market,
especially when a shock travels through several asset classes and several categories of
participants, or when attention is limited. Prices then drift in the direction of the shock for
weeks or months. More broadly, prices react progressively to changes in the economic environment,
in policies, in monetary regimes or in balance-sheet constraints; investors do not all adjust at the
same speed, and the participants who provide liquidity or carry risk are not synchronous.

The second channel is the inertia of institutional capital. Pension funds, insurers and sovereign
funds work under mandates, investment committees and structural decision delays, and constraints of
risk, leverage, liquidity and calendar; they do not reallocate in one move. This slow-moving capital
creates a persistent demand or supply that supports the trend even after the initial underreaction
has been corrected. Hedgers matter too: Moskowitz, Ooi and Pedersen (2012) find that speculators,
trend followers and commodity trading advisers, profit at the expense of hedgers (agents who need to
hedge, or long-only investors). The mechanism put forward is that hedgers, inelasticities and
regulatory constraints produce slow directional moves; a hedger facing losses may delay a hedge,
feeding a fall, and come back late, while speculators build positions until the trend turns.
Intermediation frictions, such as limited capital and margins, prevent shocks from being absorbed at
once and can spread the directional adjustment over time.

The third channel is self-reinforcement by systematic trend followers. Once a trend forms,
commodity trading advisers enter in its direction through moving-average crossovers or momentum
signals, and their aggregated entries add price pressure that lengthens and amplifies the trend, a
flow feedback documented in the managed-futures literature; the more a trend is established, the
more it is detected and carried by participants who follow prices.

The exponentially weighted moving average crossover (EWMAC) is the technical trend-following rule
most used by systematic commodity trading advisers, and a specific implementation of time-series
momentum. It gives a long signal when a fast exponentially weighted moving average of prices,
typically over 8 to 64 days, crosses above a slow one, typically over 32 to 256 days, and a short
signal when it crosses below; the difference between the fast and the slow average measures the
recent trend. Carver (2015) formalises it in a quantitative framework in which the forecast of
expected return is proportional to this difference, normalised by the volatility of the instrument.
The rule captures the inertia of prices by detecting changes in the regime of the trend: when the
short-term average exceeds the long-term one, recent prices are on average higher than older prices,
which signals an uptrend. Its economic basis is the underreaction of prices and the slow movement of
capital, which make trends persist after they are detected. Carver stresses combining variants at
different speeds, such as EWMAC(2,8), EWMAC(8,32) and EWMAC(32,128), to capture trends at different
horizons: in his account, because short and long trends are not perfectly correlated, the
diversification of speeds makes the signal more robust. It is the standard implementation of the
managed-futures industry.

Greyserman and Kaminski argue that "momentum" is a descriptive label rather than the cause: the
causal variable is market divergence, the persistence of directional moves fed by real imbalances,
and trends become tradable when price divergence lasts long enough. A theoretical layer comes from
the adaptive markets hypothesis and from a speculative risk premium: carrying disciplined
directional positions in uncertain environments earns a premium that many investors cannot hold. The
literature stresses that the phenomenon appears particularly cleanly in futures, which allow short
selling, the hedging of multi-asset macroeconomic shocks and directional positions without the
frictions of cash equities. In the same literature, a diversified portfolio of trends is more robust
than a trend in a single asset, because the returns come less from a single market than from the
repetition of trends across many markets, which do not always trend at the same time. The effect can
persist despite its fame because holding it has behavioural and institutional costs: strict
discipline over leverage and diversification, and long flat periods.

## Prediction

The sign, and sometimes the size, of an asset's past return positively predicts its future returns,
across equity indices, interest rates, currencies and commodities. Moskowitz, Ooi and Pedersen
(2012) document it on 58 futures and forward instruments over 25 years, with persistence over 1 to
12 months; Greyserman and Kaminski (2014) document the persistence over long histories, several
centuries for some markets, with periods of success and failure correlated with economic regimes.
The natural horizon is intermediate, typically a few weeks to a few months: 1 to 12 months, often 3
to 12, with an empirical optimum around 3 to 6 months for lookback signals. Signal horizons run from
a few months, in the academic construction, to shorter variants, with signals such as return
lookbacks, moving averages or breakouts. For the EWMAC rule, a fast average crossing above a slow
one is followed by returns in the direction of the crossover, and the horizon depends on the
parameters: EWMAC(2,8) captures trends lasting a few days, EWMAC(64,256) trends lasting several
months; for Carver, a combination of speeds forecasts returns more robustly than any single speed.

Trend following has been present for centuries, earns gains when trends set in, and is often
profitable during stress. It is often described as having positive convexity with respect to market
returns: it tends to capture positive returns in strong trends, up or down, and to underperform in
consolidations.

It performs well when macroeconomic or policy trends persist (interest-rate cycles, commodity cycles,
regimes of risk appetite). It underperforms in range-bound markets, in periods of high intraday
volatility without direction, in whipsaws and at abrupt reversals. The effect is degraded when too
much capital crowds into the strategy.

## What would refute it

The sign of past 1- to 12-month returns carrying no information about the next months' returns
across futures markets, or only in isolated markets and periods. Profits that do not depend on the
persistence of macroeconomic trends and are as large in range-bound markets as in trending ones.
Returns without convexity with respect to the market, doing no better in large up or down moves than
in calm periods. Institutional allocations and hedgers' positions that adjust at once to shocks.
Diversified portfolios of trends no more stable than single-market trends. Crossovers of fast and
slow moving averages followed by returns no different from those after the opposite crossovers;
signals at different speeds so highly correlated that combining them adds nothing, or a combination
no more robust than a single speed.

## References

- Lo, A. W. (2004). The Adaptive Markets Hypothesis: Market Efficiency from an Evolutionary Perspective. Journal of Portfolio Management.
- Moskowitz, T. J., Ooi, Y. H. & Pedersen, L. H. (2012). Time Series Momentum. Journal of Financial Economics.
- Hurst, B., Ooi, Y. H. & Pedersen, L. H. (2017). A Century of Evidence on Trend-Following Investing. Journal of Portfolio Management (also circulated as a research paper).
- Antonacci, G. Work on absolute momentum.
- Ilmanen, A. (2011). Expected Returns: An Investor's Guide to Harvesting Market Rewards, part III, ch. 14 "Commodity Momentum and Trend Following", p. 390, with "Why Does Momentum Such a Naive Strategy Work?", p. 398, and "Momentum in Other Asset Classes", p. 400; syntheses on trend and momentum styles, PDF pp. 62, 170, 562-569, 624-627 and 644-651. Wiley.
- Greyserman, A. & Kaminski, K. (2014). Trend Following with Managed Futures: The Search for Crisis Alpha, ch. 1 "A Multicentennial View of Trend Following", p. 3 (PDF pp. 33-53); ch. 2-4, including ch. 3 "Systematic Trend Following Basics", p. 45, with "The Basic Building Blocks of a Trend Following System", p. 47, and ch. 4 "Adaptive Markets and Trend Following" (PDF pp. 95-117); ch. 7 "Properties of Trend Following Returns" (PDF pp. 173-189); ch. 10 on the macroeconomic factors of divergence (PDF pp. 239-259); discussion of systematic rules. Wiley.
- Carver, R. (2015). Systematic Trading: A Unique New Method for Designing Trading and Investing Systems, chapters on the EWMAC rules and the design of trend signals; ch. 2 "Systematic Trading Rules", p. 41, and "Why Certain Rules Are Profitable", p. 46. Harriman House.
- Gray, W. R. & Vogel, J. R. (2016). Quantitative Momentum: A Practitioner's Guide to Building a Momentum-Based Stock Selection System, appendix A, section on absolute momentum and time-series momentum, PDF pp. 184-192. Wiley.
- Clenow, A. F. (2023). Following the Trend: Diversified Managed Futures Trading (2nd edition), ch. 1 "Cross-Asset Trend Following with Futures", p. 1; ch. 3-5, pp. 45-105. Wiley.
