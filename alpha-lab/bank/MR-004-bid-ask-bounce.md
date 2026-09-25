---
id: MR-004
title: Bid-ask bounce
family: mean reversion and relative value
mechanism: [microstructure]
asset_classes: [stocks, equity indices, bonds, commodities, currencies]
horizon: [intraday, days, weeks]
data: [intraday transaction prices, bid and ask quotes, bid-ask spreads, daily closing prices, trading volumes]
status: untouched
---

## Mechanism

Part of the reversal observed at very short horizons comes from the mechanics of transaction prices, not from overreaction. When an asset trades with a strictly positive bid-ask spread, successive trades alternate between the bid and the ask even when no new information arrives. A trade at the bid followed by a trade at the ask can produce an apparent negative autocorrelation of returns, a false mean reversion, while the fundamental value and the midprice have not moved: only the transaction price oscillates on either side of the mid. The reversion is a mechanical correction of microstructure noise.

The cause is structural. Observed prices are transaction prices, not perfect estimates of the instantaneous fundamental value. When sampling is too fine, or when returns are measured from prices subject to quote errors, to bounces between bid and ask or to stale prices, part of the mean-reversion signal is purely microstructural. Market makers set the spread deliberately to cover their order-processing, inventory and adverse-selection costs, and impatient buyers and sellers using market orders generate the alternating trades. The market is quoted around an intermediate value and traders pay for immediacy, so as long as aggressive orders alternate between buys and sells, transaction prices oscillate around the mid. The books show that the negative covariance of returns can come from the spread itself, from an imbalance in the direction of orders, or from the serial correlation of trades when orders are sliced. Roll (1984) formalised the link between the spread and the negative autocovariance of price changes, and the decomposition of the spread ties the bounce to its order-processing component. The bounce is the most elementary transitory component of transaction prices, distinct from the permanent component that carries information.

The same mechanics reach returns measured over a month. A large move at the end of a month can partly reflect a trade at the ask, which inflates the month's return; a trade at the bid the next month then shows an apparent fall. This creates negative autocorrelation at the one-month horizon, which coexists with intermediate momentum over 3 to 12 months. A complementary mechanism at that horizon is the liquidity rebound: market makers who took large positions against a forced move rebalance them the following month, which creates an opposite move.

A related source of spurious reversion is non-synchronous trading: when some securities do not trade at every instant, their last observed prices are stale, and the update at the next trade can create an appearance of mean reversion or predictability that does not exist in the efficient price.

The effect persists because it is not an arbitrageable inefficiency but a property of how prices are measured, the visible form of the cost of liquidity: "arbitraging" it means paying the spread. It persists as long as the observer looks at transaction prices, at very short horizons, and at assets with non-trivial quoting frictions.

## Prediction

Returns computed from transaction prices show a negative autocovariance at very short horizons, of a size tied to the spread. The effect:

- is larger when the spread is wide, as in illiquid assets, and it decreases as liquidity increases; on very liquid markets with a minimal spread it is small but persists;
- matters above all at intraday to daily horizons, in illiquid assets, with wide spreads, discrete quoting and irregular trading, and it matters particularly in small capitalisations and in historical databases with imperfect quote quality; in less liquid securities or contracts it can contaminate even lower-frequency data;
- for many very-short-term reversal signals, disappears or weakens sharply when returns are measured from midquotes instead of transaction prices, when the spread effect is corrected, or when illiquid securities are filtered out.

The literature has shown that the bid-ask bounce explained a substantial part of the apparent reversal, especially in some NASDAQ databases of the 1990s. On modern organised markets the spread is often a single tick; on liquid futures the effect is close to zero. In futures it affects mainly intraday to one- or two-day returns computed from transaction or settlement prices rather than from midquotes. Its intensity depends on liquidity, tick size and the microstructure regime. Ilmanen (2011) explicitly ties some very-short-term reversals to the bid-ask bounce and to temporary price concessions.

At the monthly horizon, the stocks that rose most over the previous month tend to underperform the following month, and vice versa, while intermediate momentum over 3 to 12 months coexists with this reversal. Jegadeesh (1990), Lehmann (1990) and Lo and MacKinlay (1990) document the one-month reversal. In some less liquid futures markets the effect can be more pronounced.

## What would refute it

- Short-horizon reversals as large in midquote returns as in transaction-price returns, or unchanged after correcting for the spread.
- Negative autocovariance of transaction-price changes unrelated to the width of the spread, the tick size or the liquidity of the asset.
- Reversals of the same size in liquid, narrow-spread assets as in illiquid, wide-spread ones.
- Returns from trading against the bounce that survive paying the spread, which would contradict its reading as the cost of liquidity.
- Negative autocovariance larger than the spread can generate, which would point to other causes (inventory effects, overreaction).
- No negative relation between one month's return and the next month's return, or a one-month reversal as strong in midquote returns, where the bounce is absent, and unrelated to liquidity provision.

## References

- Roll, R. (1984). A Simple Implicit Measure of the Effective Bid-Ask Spread in an Efficient Market. Journal of Finance.
- Glosten, L. R. and Milgrom, P. R. (1985). Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders. Journal of Financial Economics.
- Harris, L. (1990). Statistical Properties of the Roll Serial Covariance Bid/Ask Spread Estimator. Journal of Finance.
- Kaul, G. and Nimalendran, M. (1990). Price Reversals: Bid-Ask Errors or Market Overreaction? Journal of Financial Economics.
- Lo, A. W. and MacKinlay, A. C. (1990). When Are Contrarian Profits Due to Stock Market Overreaction? Review of Financial Studies.
- Lehmann, B. N. (1990). Fads, Martingales, and Market Efficiency. Quarterly Journal of Economics.
- Blume, M. E. and Stambaugh, R. F. (1983). Biases in Computed Returns: An Application to the Size Effect. Journal of Financial Economics.
- Glosten, L. R. (1987). Components of the Bid-Ask Spread and the Statistical Properties of Transaction Prices. Journal of Finance.
- Glosten, L. R. and Harris, L. E. (1988). Estimating the Components of the Bid/Ask Spread. Journal of Financial Economics.
- Harris, L. (2002). Trading and Exchanges: Market Microstructure for Practitioners. Oxford University Press. Chapter on microstructure, sections on spreads and transitory volatility, pp. 296-320 (approximately).
- Hasbrouck, J. (2007). Empirical Market Microstructure. Oxford University Press. Chap. 3-4, the Roll model and its generalisation, pp. 30-60 (approximately); pp. 67-71 on the generalised Roll model.
- Campbell, J. Y., Lo, A. W. and MacKinlay, A. C. (1997). The Econometrics of Financial Markets. Princeton University Press. Chap. 3, section 3.2, pp. 62-84.
- Lo, A. W. and MacKinlay, A. C. (1999). A Non-Random Walk Down Wall Street. Princeton University Press. Chap. 2, section 2.3, Spurious Autocorrelation Induced by Nontrading, pp. 34-37.
- Tsay, R. S. (2010). Analysis of Financial Time Series (3rd edition). Wiley. Chap. 5, High-Frequency Data Analysis and Market Microstructure, sections 5.1 Nonsynchronous Trading and 5.2 Bid-Ask Spread, pp. 259-262.
- de Jong, F. and Rindi, B. (2009). The Microstructure of Financial Markets. Cambridge University Press. Chap. 6, Empirical Models of Market Microstructure, in particular Estimating the Bid-Ask Spread, p. 105, and Price Effects of Trading, p. 109; chap. 9, Price Discovery, pp. 159 ff.
- Market Liquidity (authors and year not specified). Pp. 59 and 62-64.
- Ilmanen, A. (2011). Expected Returns: An Investor's Guide to Harvesting Market Rewards. Wiley. P. 186.
- Jegadeesh, N. (1990). Evidence of Predictable Behavior of Security Returns. Journal of Finance.
- Thaler, R. H. (ed.) (2005). Advances in Behavioral Finance, Volume II. Princeton University Press. Chap. 10.
- Bali, T. G., Engle, R. F. and Murray, S. (2016). Empirical Asset Pricing: The Cross Section of Stock Returns. Wiley. Chap. 12, Short-Term Reversal Effect, p. 242.
- Gray, W. R. and Vogel, J. R. (2016). Quantitative Momentum: A Practitioner's Guide to Building a Momentum-Based Stock Selection System. Wiley. Chap. 3, on skipping the last month.
