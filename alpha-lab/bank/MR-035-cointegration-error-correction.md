---
id: MR-035
title: Cointegration and error correction
family: mean reversion and relative value
mechanism: [limits to arbitrage, structural, flows]
asset_classes: [stocks, equity indices, bonds, commodities, currencies, crypto]
horizon: [days, weeks, months]
data: [daily prices, futures prices, ADR and local share prices, ADR and share class listings, ETF and constituent prices, ETF holdings, industry classifications, prices across exchanges]
status: untouched
---

## Mechanism

Two prices can each be non-stationary and still share a stable equilibrium relation. Cointegration is not simply correlation: it is a long-run equilibrium imposed by a common economic logic. It arises when two assets refer, directly or indirectly, to the same economic risk: the same company through several share lines, a local share and its ADR, an ETF and its basket, securities with very close exposures, the same productive complex or physical chain, spot and futures, the legs of an industrial spread, or instruments linked by an economic identity; also stocks in the same industry or value chain, twin securities, securities exposed to the same latent factor, and closely linked crypto-assets. The relation need not be a risk-free arbitrage: it can come from substitutability, common fundamental exposures, capital constraints, investor preferences or a common factor structure, and the mechanism concerns in particular assets with close fundamental or factor exposures. The theory spans everything from simple statistical convergence to cointegration grounded in an explicit economic link. Formally (Engle and Granger 1987), two or more series integrated of order one admit a linear combination that is stationary: p1 and p2 are cointegrated if there is a β such that e_t = p1_t − β·p2_t is stationary; the prices share a common stochastic trend. The spread is then not mere noise but a measure of the deviation from equilibrium, and the series cannot drift apart indefinitely without violating an economic or structural coherence.

The error-correction model (ECM) describes the return to equilibrium: the future change of the prices depends on the past deviation from the equilibrium relation, and the model parametrises the speed of adjustment of cointegrated spreads. The economic mechanism behind it is generally the law of one price with imperfect arbitrage. Prices can diverge in the short run through idiosyncratic shocks, noise, flow pressure, forced flows, indexing misalignments, hedging errors, transient changes of liquidity or information lags, but a restoring force exists because arbitrageurs, hedgers, processors, dealers and relative-value investors act against the deviation once it is wide enough to pay for the frictions: when the gap becomes too large, selling the rich asset and buying the cheap one becomes economically attractive. Their intervention does not keep the gap at zero, but it creates the pull back. The traders involved are statistical arbitrage funds, long/short funds and spread traders.

Arbitrage is never instantaneous because it is costly and risky: funding, execution, short selling, inventory constraints, mismatches of quality or location, delays before convergence, the risk of a structural break and uncertainty about the true equilibrium relation. The deviation is also kept open by the limited inventory capacity of arbitrageurs, model risk, temporary noise in flows, the non-synchronous arrival of orders, forced sales and changing regimes; convergence takes time, the relation can break, selecting pairs or clusters is delicate, and carrying the position can be costly. Cointegration is thus less a strategy than a general theory of relative equilibrium, which explains why spreads can be structurally mean-reverting without either price being stationary. The mechanism concerns pairs of securities, many basket spreads, some futures/cash relations, inter-commodity spreads and part of macro and cross-asset convergence; in futures, it covers spot-futures dynamics, spreads between maturities, spreads between commodities and crypto spreads across venues.

## Prediction

Spreads between cointegrated assets are stationary and revert towards equilibrium, the future change depending on the past deviation from it. When the relative gap deviates too far from the relation, part of the move is transitory and the gap tends to close: the asset that has lagged tends to outperform the one that has led. The pattern concerns sector peers, ADRs and their home shares, ETFs and their constituents, share classes of the same company, and sometimes major crypto-assets against smaller ones. The relation must be stable over time. Correlation does not imply cointegration. The equilibrium parameter β can drift, and relations can be unstable over time (changes of regime, mergers, restructurings).

## What would refute it

- Spreads between economically linked assets that are not stationary, or whose cointegrating vector β drifts without bound.
- Past deviations from equilibrium that do not predict later changes of opposite sign, i.e. an adjustment coefficient of zero.
- Apparent extremes that turn out to be regime changes, a transition to a new equilibrium rather than a return to the old mean, through mergers, restructurings or other structural breaks, a risk the books stress.

## References

- Engle, R. F. and Granger, C. W. J. (1987). Co-Integration and Error Correction: Representation, Estimation, and Testing. Econometrica.
- Johansen, S. (1991). Estimation and Hypothesis Testing of Cointegration Vectors in Gaussian Vector Autoregressive Models. Econometrica.
- Stock, J. H. and Watson, M. W. (1988). Testing for Common Trends. Journal of the American Statistical Association.
- Tsay, R. S. (2010). Analysis of Financial Time Series (3rd edition). Wiley. Cointegration, common trends and pairs trading, pp. 455-457, 469 and 473; chap. 8.5, Unit-Root Nonstationarity and Cointegration, pp. 455 ff.; section 8.5.1, An Error Correction Form, pp. 458 ff.; section 8.8, Pairs Trading, pp. 473 ff.; chap. 8, pp. 300-340; chap. 8.5-8.6, pp. 428-438, above all pp. 431-434 on the error-correction form and common stochastic trends.
- Vidyamurthy, Ganapathy (2004). Pairs Trading: Quantitative Methods and Analysis. Wiley. Chapter 6, "Pairs Selection in Equity Markets", pp. 85-97, including "Common Trends Cointegration Model" and "Common Trends Model and APT", pp. 85-90; chapter 7, "Testing for Tradability", pp. 104-129; chapter 5, "Overview", including "Cointegration", pp. 73-75, and pp. 77-80, 84, 91, 105-109; chapters 3-6, pp. 40-120.
- Chan, E. P. (2013). Algorithmic Trading: Winning Strategies and Their Rationale. Wiley. Chap. 2, The Basics of Mean Reversion, in particular Mean Reversion and Stationarity, p. 59, and Cointegration, p. 68; chap. 4, Mean Reversion of Stocks and ETFs, pp. 105 ff.; chap. 3-4, pp. 60-110.
- Cartea, Á., Jaimungal, S. and Penalva, J. (2015). Algorithmic and High-Frequency Trading. Cambridge University Press. Chap. 11, Pairs Trading and Statistical Arbitrage Strategies, pp. 290 ff.
- Enders, W. (2014). Applied Econometric Time Series (4th edition). Wiley. Chap. 6, pp. 320-400; chap. 6, pp. 344-353, above all "Cointegration and Common Trends" and "Cointegration and Error Correction".
- Rao, B. B. (ed.) (1994). Cointegration for the Applied Economist. Macmillan. Chapters 1-5, pp. 1-120; pp. 9 and 74-80.
- Lütkepohl, H. (year and edition not specified). Introduction to Multiple Time Series Analysis. Springer. Chap. 11, pp. 351-384.
- Gatev, Evan, William N. Goetzmann and K. Geert Rouwenhorst (2006; working-paper version 1999). Pairs Trading: Performance of a Relative-Value Arbitrage Rule. Review of Financial Studies.
- Avellaneda, Marco and Jeong-Hyun Lee (2010). Statistical Arbitrage in the U.S. Equities Market. Quantitative Finance.
- Campbell, John Y., Andrew W. Lo and A. Craig MacKinlay (1997). The Econometrics of Financial Markets. Princeton University Press. Cointegration and common trends, around pp. 306-310.
