---
id: FP-036
title: Correlated factor bets
family: flows and positioning
mechanism: [flows, limits to arbitrage]
asset_classes: [stocks, equity indices, bonds, commodities, currencies]
horizon: [days, weeks]
data: [institutional holdings, hedge fund returns, factor returns, position data, daily prices, futures basis, margin requirements]
status: untouched
---

## Mechanism

Ang shows that a large part of institutional risk lies not in individual portfolio positions but in
the correlation of the factor bets that many managers take at the same time. A hundred different
managers "reaching for yield", or loaded on the same illiquidity factor, do not make a hundred
independent bets but a single crowded trade. More generally, a crowded trade is a situation in which
many participants, often leveraged, hold similar positions, which makes the system vulnerable to
synchronised liquidations. As the assets involved grow, returns to scale fall, positions become more
homogeneous, and an adverse shock can force synchronised reductions. Ang also discusses the
procyclicality of institutions that do not rebalance.

The dynamic is a violent deviation, as a spread or basis widens sharply, during a funding or margin
shock, followed by a rebound or reversion when the forced liquidation ends and the arbitrage can be
financed again. It is often endogenous: it depends not only on fundamentals but on the structure of
funding, on risk-management policies (stop-outs, value-at-risk limits) and on the liquidity
available. Pedersen gives the dynamic version of the mechanism with the quant event of 2007: forced
sales of similar positions, losses unrelated to fundamentals, then a partial snapback, the signature
of an unwind driven by liquidity. Narang (2024) analyses the quant crisis of August 2007 in detail
as a textbook case of regime risk for mean-reversion strategies. In August 2007 the forced
liquidation of a large quantitative fund set off a cascade of sales across statistical arbitrage
positions, which momentarily reversed every mean-reverting signal: the assets that should have risen
(the long positions) kept falling, and vice versa, and well-diversified, unleveraged mean-reversion
funds suffered large temporary losses, then partly recovered when conditions returned to normal. The
chain runs from crowding, as all quantitative funds held similar positions, to a forced liquidation,
to mean-reverting signals turning anti-predictive for three to five days, amplified by leverage, to
losses that force further liquidations.

The driver is not only that many people like the same thing, but the combination of delegated
management, benchmark constraints, similar signals, the size of assets under management, and
funding. The phenomenon persists because incentives and the architecture of asset management push
portfolios towards similar exposures, especially when some factors or styles have a long history of
success. Prices then become vulnerable to a collective unwind, even if each participant, taken in
isolation, believes it is diversified.

The mechanism has been observed in quantitative equity, among hedge funds, in style factors and in
delegated management; by analogy, the logic can carry over to futures when many holders use the same
signals or the same risk overlays. In futures, the mechanism explains many relative-value
dislocations (bases, spreads, curve trades) that widen more than expected and then normalise. It is
related to Markov switching, liquidity spirals, crisis correlations and tail risk.

## Prediction

When many managers hold the same positions or factor exposures, an adverse funding, margin or
performance shock is followed by synchronised reductions of those exposures: the crowded positions
show sharp deviations or losses unrelated to fundamentals, over days to weeks, followed by a partial
snapback once forced selling stops and the arbitrage becomes financeable again. When the crowded
positions are statistical-arbitrage positions, mean-reversion signals become anti-predictive for
several days (three to five days in August 2007), followed by a partial recovery as conditions
normalise. Returns to scale fall as the assets committed to a factor grow.

## What would refute it

- Sharp losses in crowded positions or factor portfolios that show no partial snapback afterwards
  and match news about fundamentals; dislocations fully explained by fundamental news rather than by
  the structure of funding and risk management.
- Crowded positions that do not widen more than comparable uncrowded ones during funding or margin
  shocks; losses during forced liquidations no larger for crowded and leveraged positions than for
  others.
- Reductions of factor exposures that are not synchronised across managers holding similar
  positions.
- Factors held by many managers no more vulnerable to sudden unwinds than factors held by few.
- Forced liquidations of crowded quantitative positions that do not turn mean-reversion signals
  anti-predictive.
- Returns to a factor that do not decline as the assets committed to it grow.

## References

- Ang, A. (2014). Asset Management: A Systematic Approach to Factor Investing. Oxford University Press. Chap. 10, p. 312; chap. 4, p. 129.
- Pedersen, L. H. (2015). Efficiently Inefficient: How Smart Money Invests and Market Prices Are Determined. Princeton University Press. Chap. 9, Quantitative Equity Investing, pp. 146-148; preface, pp. xii-xiii.
- European Central Bank (2005). Hedge funds and the crowding of trades. Financial Stability Review (box).
- Pericoli, M. et al. (2010). Crowded Trades among Hedge Funds. Banca d'Italia working paper.
- Narang, R. K. (2024). Inside the Black Box (3rd edition). Wiley. Chapter on risks and the 2007 quant crisis, pp. 150-200 (approximately).
- Khandani, A. E. and Lo, A. W. (2007). What Happened to the Quants in August 2007? Journal of Investment Management.
