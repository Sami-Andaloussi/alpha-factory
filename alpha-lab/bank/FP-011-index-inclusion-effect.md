---
id: FP-011
title: Index inclusion effect
family: flows and positioning
mechanism: [flows, limits to arbitrage, structural]
asset_classes: [stocks, equity indices, sectors, bonds, commodities, currencies, crypto]
horizon: [days, weeks, months]
data: [index membership changes, announcement and effective dates, daily prices, trading volumes, indexed assets, institutional holdings]
status: untouched
---

## Mechanism

When an index adds, removes or reweights securities, a mass of index-tracking and benchmark-aware
capital must buy and sell at almost the same moment. The best-known case is the price rise of a
security added to an index followed by passive or benchmarked investors. The most direct mechanism
is a demand shock unrelated to fundamentals: index managers must buy the security to replicate the
index, and benchmarked active managers may also reduce their underweight. Demand for the security
rises mechanically, without any information about its future cash flows being needed. The mechanism
depends on a mandate, not on an opinion: additions are bought because they must enter the portfolio,
and deletions are sold because they must leave it.

More broadly, part of a stock's price behaviour comes from the stock becoming an input of a
reference portfolio rather than a stand-alone asset. Once it enters a major index, or becomes
important for benchmarked mandates, the demand for it is also created by investors who must hold it
to replicate an index, to limit their tracking error, to respect the constraints of their mandate,
or to provide liquidity on indexed products: a demand that is structurally inelastic and not
entirely informational. The actors are index funds, ETFs, benchmarked managers and market makers on
passive products, together with the arbitrageurs who internalise these flows partly, but not fully.
Because the index trades are largely predictable, concentrated in time and only partly informative
about fundamental value, they generate price moves that are often followed by a partial reversal.
The announcement of an addition, for example to the S&P 500, triggers purchases by index managers
and by arbitrage strategies (the "S&P game"), which lifts the price around the announcement and the
implementation. The counterparties who take the other side demand compensation, especially when the
operation is known in advance and must be executed on an imposed date. The mechanism thus combines
inelastic demand, tracking-error constraints, synchronised execution and imperfect arbitrage. Its
origin is institutional: it is tied to the architecture of delegated asset management and cannot be
reduced to simple momentum.

The literature debates how much of the effect is transitory and how much is permanent. A strictly
microstructural reading sees mainly temporary price pressure, tied to the need to absorb the orders
and to the timing of implementation, so that a later correction is expected. Other work points to
more persistent channels: better liquidity, lower monitoring costs, analyst coverage, a broader
investor base, greater attention and visibility, and holding constraints for benchmark-aware
managers. The effect then has two components: an event component around the announcement of the
inclusion and the stock's actual entry into the index, and a more durable component that runs
through the stock's ownership structure and its comovement with the reference basket. Even if the
pure announcement effect fades as the market becomes more sophisticated, the demand tied to the
benchmark keeps subsidising some stocks and altering their price dynamics (the benchmark inclusion
subsidy). Whatever the exact split, indexing and benchmarking create a partly predictable demand
that follows from the index composition rules.

The effect persists because benchmark rules are public, the amounts are massive, and benchmarked
active managers take part in the flow in practice even though they are not passive in the strict
sense. It is not fully arbitraged because supplying the index buyers in advance (shorting additions,
buying deletions) requires predicting the announcements, bearing the risk of being wrong, and
absorbing the imbalance against investors who are insensitive to price in the short run. Arbitrage
against benchmarked demand takes capital and means bearing tracking-error risk, timing risk, the
costs of lending and borrowing securities, and sometimes regulatory or balance-sheet constraints; it
must often be carried out against a calendar that is known but risky, and even when part of the move
is anticipated, the whole reversal cannot be positioned for in advance without the risk of crowding,
of a timing error or of an institutional change. It is one of the purest forms of forced
institutional order, close to inelastic demand, institutional clientele and the compression of the
risk premium; it combines with index rebalancing, ETF flows and inelastic markets, and often with
trades timed around the effective date, anticipation of squeezes and tracking-error pressure. By
analogy, in futures, the corresponding cases are the rebalancing and roll of commodity indices,
reconstitutions and sector rebalancing on equity futures, and rebalancing by systematic portfolios
that use futures as low-cost instruments. By analogy, in crypto, the equivalents are index products,
tokenised baskets, lists of assets included in investment products, and changes in the collateral
that protocols and platforms accept.

## Prediction

Securities added to an index rise, and deleted securities fall, between the announcement and the
effective date, with abnormal trading volume. Part of the move reverts over the following days or
weeks of normalisation; part can persist when membership improves liquidity, attention and the
investor base. Beyond the event, an included stock shows a lasting change in its ownership towards
passive and benchmarked holders and a higher comovement with the other members of the benchmark. The
literature shows effects on price levels, volume, liquidity and comovement, and it distinguishes a
purely temporary price-pressure component, a possibly more durable component linked to liquidity,
analyst coverage or visibility, and a part of the move anticipated before the effective date. The
size of the effect varies with the relative size of the names, the predictability of the changes and
the amount of benchmarked assets.

The effect has been documented on the S&P 500 and above all on the Russell indices, where the
relatively small size of the constituents accentuates the price pressure, and in other indices as
well. It is observed on US stocks around inclusions in the S&P 500 and, more broadly, with the rise
of passive management. The literature documents price and volume effects around index changes and
discusses the price-pressure hypothesis explicitly. Other work suggests that the pure announcement
and inclusion effect may have weakened as the market became more sophisticated, while
benchmark-linked demand continues to subsidise the stocks concerned.

## What would refute it

- No abnormal price move or volume for additions and deletions between announcement and effective
  date, compared with similar securities that are not added or deleted.
- An effect no larger for small constituents, as in the Russell indices, than for large ones, as in
  the S&P 500.
- No relation between the size of the effect, or of the later reversal, and the amount of indexed
  or benchmarked assets relative to the size of the security, or the concentration of the forced
  demand on the effective date.
- Price changes at inclusion that are entirely explained by news about future cash flows, or by
  changes in information, liquidity or analyst coverage, with no temporary component tied to index
  demand; index demand absorbed in full by arbitrageurs at inclusion.
- For the temporary component: price rises at inclusion that show no reversal at all after the
  effective date.
- For the durable component: included stocks that show no lasting shift of their ownership towards
  index funds, ETFs and benchmarked managers, and no rise in their comovement with the index basket,
  compared with similar stocks outside the index; or a price change that reverses entirely once the
  index trades are done, leaving no difference in valuation between included stocks and comparable
  stocks outside the index.

## References

- Harris, L. and Gurel, E. (1986). Price and Volume Effects Associated with Changes in the S&P 500 List: New Evidence for the Existence of Price Pressures. Journal of Finance.
- Shleifer, A. (1986). Do Demand Curves for Stocks Slope Down? Journal of Finance.
- Greenwood, R. (2005). Short- and Long-Term Demand Curves for Stocks: Theory and Evidence on the Dynamics of Arbitrage. Journal of Financial Economics.
- Harris, L. (2002). Trading and Exchanges: Market Microstructure for Practitioners. Oxford University Press. Chap. 23, pp. 487-488.
- Siegel, L. B. (2003). Benchmarks and Investment Management. Research Foundation of AIMR. Chap. 7, pp. 52-55, and above all pp. 69-71.
- Goetzmann, W. N. and Garry, M. (1986). Does Delisting from the S&P 500 Affect Stock Price? Financial Analysts Journal.
- Jain, P. C. (1987). The Effect on Stock Price of Inclusion in or Exclusion from the S&P 500. Financial Analysts Journal.
- Madhavan, A. (year and title not specified). Cited by Harris on the reconstitution of the Russell indices.
- Lynch, A. W. and Mendenhall, R. R. (1997). New Evidence on Stock Price Effects Associated with Changes in the S&P 500 Index. Journal of Business.
- Beneish, M. D. and Whaley, R. E. (1996). An Anatomy of the "S&P Game": The Effects of Changing the Rules. Journal of Finance.
- Chen, H., Noronha, G. and Singal, V. (2004). The Price Response to S&P 500 Index Additions and Deletions: Evidence of Asymmetry and a New Explanation. Journal of Finance.
- Kashyap, Anil K., Natalia Kovrijnykh, Jian Li, Anna Pavlova (2021). The Benchmark Inclusion Subsidy. Journal of Financial Economics.
- Greenwood, Robin, Samuel G. Hanson, Gaston Illanes, Adi Sunderam (2022). The Disappearing Index Effect. NBER Working Paper.
