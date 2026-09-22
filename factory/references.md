[Up: Factory](README.md)

# References

## TL;DR

The books and papers the blueprint's methods come from, each with what the factory takes from it.
Sub-section pages cite an entry by its anchor; a method with no checked reference names its origin in plain words.

## Books

Eight books underpin the blueprint. The table gives each in a line, with the sections whose pages
cite it; below it, what the blueprint takes from each.

| Reference | In one line | Cited in |
|---|---|---|
| <a id="lopez-de-prado-2018"></a>López de Prado, M. (2018). *Advances in Financial Machine Learning*. Wiley. | The research factory and its toolkit against overfitting. | S1–S7 |
| <a id="kleppmann-2017"></a>Kleppmann, M. (2017). *Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems*. O'Reilly Media. | Immutable logs, replay and schema evolution: the data architecture. | S1–S7 |
| <a id="grinold-kahn-1999"></a>Grinold, R. C., & Kahn, R. N. (1999). *Active Portfolio Management: A Quantitative Approach for Producing Superior Returns and Controlling Risk* (2nd ed.). McGraw-Hill. | The fundamental law, alpha refinement and cost-aware portfolio construction. | S2–S5, S7 |
| <a id="ilmanen-2011"></a>Ilmanen, A. (2011). *Expected Returns: An Investor's Guide to Harvesting Market Rewards*. Wiley. | Documented return sources and why they pay; simple rules over data mining. | S3–S5 |
| <a id="kissell-2013"></a>Kissell, R. (2013). *The Science of Algorithmic Trading and Portfolio Management*. Academic Press. | Transaction cost analysis, market impact and the efficient trading frontier. | S1–S7 |
| <a id="carver-2015"></a>Carver, R. (2015). *Systematic Trading: A Unique New Method for Designing Trading and Investing Systems*. Harriman House. | Modular design, volatility targeting and robust weights. | S2–S5, S7 |
| <a id="narang-2013"></a>Narang, R. K. (2013). *Inside the Black Box: A Simple Guide to Quantitative and High-Frequency Trading* (2nd ed.). Wiley. | The reference decomposition of a quantitative trading system. | S3, S5 |
| <a id="jansen-2020"></a>Jansen, S. (2020). *Machine Learning for Algorithmic Trading: Predictive Models to Extract Signals from Market and Alternative Data for Systematic Trading Strategies with Python* (2nd ed.). Packt. | The end-to-end machine-learning workflow for trading. | S1–S4 |

### What each book brings

- **López de Prado (2018).** The research factory itself: specialised stations instead of
  isolated researchers. Event-based sampling, the triple-barrier method and meta-labelling, sample
  weights for overlapping labels, fractional differentiation, structural-break tests and
  microstructural features, multicollinearity and feature importance with its substitution
  effects, purged and embargoed cross-validation and its combinatorial form, the deflated Sharpe
  ratio and backtest-overfitting statistics, and a strategy lifecycle running from embargo and
  paper trading to graduation, re-allocation and decommissioning.
- **Kleppmann (2017).** The data architecture: an immutable, append-only event log as the system
  of record, derived data rebuilt by replaying it, schemas that evolve without breaking their
  readers, idempotent processing, one code path for batch work (research, backtests) and
  streaming (live), and the limits of clocks and ordering across machines. A second edition, with
  C. Riccomini, appeared in 2026; the blueprint cites the first.
- **Grinold & Kahn (1999).** The language of active management: the information ratio as the
  measure of active performance, the fundamental law linking it to skill (the information
  coefficient) and breadth, the refinement of raw signals into alphas (volatility × IC × score),
  information analysis and signal decay, portfolio construction from alphas, covariances, costs
  and constraints, multi-factor risk models, and performance attribution.
- **Ilmanen (2011).** A map of documented return sources (asset-class premia, style premia such
  as value, carry and momentum, and the macro and liquidity factors beneath them) with their
  economic rationale; expected returns that vary over time; how risk, leverage and liquidity
  interact in crises; and a standing preference for simple, well-validated rules over data
  mining.
- **Kissell (2013).** Transaction costs as a first-class input: cost analysis before, during and
  after trading, with costs broken into components; market impact models and their calibration;
  volume and volatility forecasts for execution; the efficient trading frontier between market
  impact and timing risk; cost-aware portfolio optimisation; principal component analysis and
  orthogonalised factors in risk models; and benchmarks for comparing execution algorithms.
- **Carver (2015).** A modular system whose parts meet through standard interfaces (forecasts on
  a common scale), volatility targeting, position sizing with inertia so that small changes are
  not traded, hand-set weights and bootstrapped uncertainty instead of fragile optimisation,
  trading speed matched to costs, and a strict budget on degrees of freedom against overfitting.
- **Narang (2013).** Alpha, risk and transaction-cost models feeding a portfolio construction
  model, then an execution model, all fed by data and driven by research. The portfolio
  constructor is the arbiter between the optimist (alpha), the pessimist (risk) and the
  accountant (costs).
- **Jansen (2020).** Sourcing and storing market, fundamental and alternative data; researching
  alpha factors and judging them by information coefficient and turnover; model selection with
  cross-validation suited to time series; and backtests that account for costs and the order of
  events.

## Papers

The founding article of each method the pages use by name, checked on 21 September 2026 against
its DOI record at Crossref and, where that record was incomplete, the publisher's own page. Each
is cited on the pages whose method it founded; a method with no single founding article keeps its
book, or its origin in plain words.

| Reference | In one line | Cited in |
|---|---|---|
| <a id="acerbi-tasche-2002"></a>Acerbi, C., & Tasche, D. (2002). On the coherence of expected shortfall. *Journal of Banking & Finance*, 26(7), 1487–1503. [doi:10.1016/S0378-4266(02)00283-2](https://doi.org/10.1016/S0378-4266%2802%2900283-2) | Expected shortfall as a coherent measure of tail risk, the measure the risk budgets cap. | S5, S7 |
| <a id="almgren-chriss-2000"></a>Almgren, R., & Chriss, N. (2000). Optimal execution of portfolio transactions. *Journal of Risk*, 3(2), 5–39. [doi:10.21314/JOR.2001.041](https://doi.org/10.21314/JOR.2001.041) | The optimal path of a trade between market impact and timing risk, with temporary and permanent impact kept apart. | S4, S5 |
| <a id="bailey-et-al-2017"></a>Bailey, D. H., Borwein, J. M., López de Prado, M., & Zhu, Q. J. (2017). The probability of backtest overfitting. *Journal of Computational Finance*, 20(4), 39–69. [doi:10.21314/JCF.2016.322](https://doi.org/10.21314/JCF.2016.322) | The probability that the in-sample winner fails out of sample, estimated by combinatorially symmetric cross-validation. | S3, S4 |
| <a id="bailey-lopez-de-prado-2012"></a>Bailey, D. H., & López de Prado, M. (2012). The Sharpe ratio efficient frontier. *Journal of Risk*, 15(2), 3–44. [doi:10.21314/JOR.2012.255](https://doi.org/10.21314/JOR.2012.255) | The probabilistic Sharpe ratio: the probability that a Sharpe ratio beats a threshold, given the length, skewness and kurtosis of the record. | S4 |
| <a id="bailey-lopez-de-prado-2014"></a>Bailey, D. H., & López de Prado, M. (2014). The deflated Sharpe ratio: Correcting for selection bias, backtest overfitting, and non-normality. *Journal of Portfolio Management*, 40(5), 94–107. [doi:10.3905/jpm.2014.40.5.094](https://doi.org/10.3905/jpm.2014.40.5.094) | The deflated Sharpe ratio: the probabilistic Sharpe ratio corrected for the number of trials. | S3, S4 |
| <a id="ben-tal-nemirovski-1998"></a>Ben-Tal, A., & Nemirovski, A. (1998). Robust convex optimization. *Mathematics of Operations Research*, 23(4), 769–805. [doi:10.1287/moor.23.4.769](https://doi.org/10.1287/moor.23.4.769) | Convex optimisation that holds for every value in a set of uncertainty. | S5 |
| <a id="benjamini-hochberg-1995"></a>Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B (Methodological)*, 57(1), 289–300. [doi:10.1111/j.2517-6161.1995.tb02031.x](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x) | Control of the false discovery rate: the share of false findings among the discoveries, across many tests. | S3, S4 |
| <a id="breiman-2001"></a>Breiman, L. (2001). Random forests. *Machine Learning*, 45(1), 5–32. [doi:10.1023/A:1010933404324](https://doi.org/10.1023/A:1010933404324) | Random forests, and the importance of a feature measured by permuting it (the mean decrease in accuracy). | S2 |
| <a id="charnes-cooper-1959"></a>Charnes, A., & Cooper, W. W. (1959). Chance-constrained programming. *Management Science*, 6(1), 73–79. [doi:10.1287/mnsc.6.1.73](https://doi.org/10.1287/mnsc.6.1.73) | Chance constraints: constraints that must hold with a stated probability. | S5 |
| <a id="clark-1973"></a>Clark, P. K. (1973). A subordinated stochastic process model with finite variance for speculative prices. *Econometrica*, 41(1), 135–155. [doi:10.2307/1913889](https://doi.org/10.2307/1913889) | Prices driven by trading activity rather than calendar time: the idea behind sampling on activity. | S1, S2 |
| <a id="clarke-et-al-2002"></a>Clarke, R., de Silva, H., & Thorley, S. (2002). Portfolio constraints and the fundamental law of active management. *Financial Analysts Journal*, 58(5), 48–66. [doi:10.2469/faj.v58.n5.2468](https://doi.org/10.2469/faj.v58.n5.2468) | The transfer coefficient: the share of the information ratio a portfolio keeps once its constraints bind, added to the fundamental law. | S4 |
| <a id="cohn-et-al-1994"></a>Cohn, D., Atlas, L., & Ladner, R. (1994). Improving generalization with active learning. *Machine Learning*, 15(2), 201–221. [doi:10.1007/BF00993277](https://doi.org/10.1007/BF00993277) | Active learning: asking for the labels that teach a model most. | S1 |
| <a id="easley-et-al-2012"></a>Easley, D., López de Prado, M. M., & O'Hara, M. (2012). Flow toxicity and liquidity in a high-frequency world. *Review of Financial Studies*, 25(5), 1457–1493. [doi:10.1093/rfs/hhs053](https://doi.org/10.1093/rfs/hhs053) | Order-flow toxicity measured in volume time (VPIN). | S2 |
| <a id="efron-1979"></a>Efron, B. (1979). Bootstrap methods: Another look at the jackknife. *Annals of Statistics*, 7(1), 1–26. [doi:10.1214/aos/1176344552](https://doi.org/10.1214/aos/1176344552) | The bootstrap: uncertainty estimated by resampling the data. | S3, S4 |
| <a id="efron-2004"></a>Efron, B. (2004). Large-scale simultaneous hypothesis testing: The choice of a null hypothesis. *Journal of the American Statistical Association*, 99(465), 96–104. [doi:10.1198/016214504000000089](https://doi.org/10.1198/016214504000000089) | The empirical null: what "no effect" looks like, learnt from thousands of tests at once. | S3 |
| <a id="efron-et-al-2001"></a>Efron, B., Tibshirani, R., Storey, J. D., & Tusher, V. (2001). Empirical Bayes analysis of a microarray experiment. *Journal of the American Statistical Association*, 96(456), 1151–1160. [doi:10.1198/016214501753382129](https://doi.org/10.1198/016214501753382129) | Local false discovery rates, by empirical Bayes. | S3 |
| <a id="grinold-1989"></a>Grinold, R. C. (1989). The fundamental law of active management. *Journal of Portfolio Management*, 15(3), 30–37. [doi:10.3905/jpm.1989.409211](https://doi.org/10.3905/jpm.1989.409211) | The fundamental law of active management: the information ratio grows with skill and with the square root of breadth. | S4, S7 |
| <a id="grinold-1994"></a>Grinold, R. C. (1994). Alpha is volatility times IC times score. *Journal of Portfolio Management*, 20(4), 9–16. [doi:10.3905/jpm.1994.409482](https://doi.org/10.3905/jpm.1994.409482) | The refinement of a raw signal into an alpha: volatility times information coefficient times score. | S3–S5 |
| <a id="hampel-1974"></a>Hampel, F. R. (1974). The influence curve and its role in robust estimation. *Journal of the American Statistical Association*, 69(346), 383–393. [doi:10.1080/01621459.1974.10482962](https://doi.org/10.1080/01621459.1974.10482962) | The influence curve: how far one observation can move an estimate, and estimators that bound it. | S1–S4 |
| <a id="hansen-2005"></a>Hansen, P. R. (2005). A test for superior predictive ability. *Journal of Business & Economic Statistics*, 23(4), 365–380. [doi:10.1198/073500105000000063](https://doi.org/10.1198/073500105000000063) | The test for superior predictive ability, a sharper test of whether the best of many models beats a benchmark. | S4 |
| <a id="harvey-et-al-2016"></a>Harvey, C. R., Liu, Y., & Zhu, H. (2016). … and the cross-section of expected returns. *Review of Financial Studies*, 29(1), 5–68. [doi:10.1093/rfs/hhv059](https://doi.org/10.1093/rfs/hhv059) | Multiple testing applied to the discovery of return factors: the threshold of significance rises with the number of trials. | S3, S4 |
| <a id="hosking-1981"></a>Hosking, J. R. M. (1981). Fractional differencing. *Biometrika*, 68(1), 165–176. [doi:10.1093/biomet/68.1.165](https://doi.org/10.1093/biomet/68.1.165) | Fractional differencing: a series made stationary while it keeps its memory. | S2 |
| <a id="hotelling-1933"></a>Hotelling, H. (1933). Analysis of a complex of statistical variables into principal components. *Journal of Educational Psychology*, 24(6), 417–441. [doi:10.1037/h0071325](https://doi.org/10.1037/h0071325) | Principal components: independent axes drawn from correlated variables. | S2, S5 |
| <a id="huber-1964"></a>Huber, P. J. (1964). Robust estimation of a location parameter. *Annals of Mathematical Statistics*, 35(1), 73–101. [doi:10.1214/aoms/1177703732](https://doi.org/10.1214/aoms/1177703732) | Robust estimation: estimators that a few outliers cannot move far. | S1–S4 |
| <a id="james-stein-1961"></a>James, W., & Stein, C. (1961). Estimation with quadratic loss. In *Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability* (Vol. 1, pp. 361–379). University of California Press. [Project Euclid](https://projecteuclid.org/euclid.bsmsp/1200512173) | Shrinkage: pulling many estimates towards a common value lowers their total error. | S3 |
| <a id="ledoit-wolf-2004"></a>Ledoit, O., & Wolf, M. (2004). A well-conditioned estimator for large-dimensional covariance matrices. *Journal of Multivariate Analysis*, 88(2), 365–411. [doi:10.1016/S0047-259X(03)00096-4](https://doi.org/10.1016/S0047-259X%2803%2900096-4) | A covariance matrix estimated by shrinkage, well conditioned even with many assets and few observations. | S5 |
| <a id="lee-ready-1991"></a>Lee, C. M. C., & Ready, M. J. (1991). Inferring trade direction from intraday data. *Journal of Finance*, 46(2), 733–746. [doi:10.1111/j.1540-6261.1991.tb02683.x](https://doi.org/10.1111/j.1540-6261.1991.tb02683.x) | Trade signing: whether a trade was a buy or a sell, read from the prevailing quote. | S1 |
| <a id="lo-2002"></a>Lo, A. W. (2002). The statistics of Sharpe ratios. *Financial Analysts Journal*, 58(4), 36–52. [doi:10.2469/faj.v58.n4.2453](https://doi.org/10.2469/faj.v58.n4.2453) | The standard error of a Sharpe ratio, and how to annualise it when returns are serially correlated. | S4 |
| <a id="magill-constantinides-1976"></a>Magill, M. J. P., & Constantinides, G. M. (1976). Portfolio selection with transactions costs. *Journal of Economic Theory*, 13(2), 245–263. [doi:10.1016/0022-0531(76)90018-1](https://doi.org/10.1016/0022-0531%2876%2990018-1) | With a cost on every trade, a portfolio is best left alone inside a no-trade region. | S5 |
| <a id="meucci-2009"></a>Meucci, A. (2009). Managing diversification. *Risk*, 22(5), 74–79. [risk.net](https://www.risk.net/derivatives/structured-products/1500233/managing-diversification) | The effective number of bets: how many independent sources of risk a portfolio really holds, from the entropy of its principal components. | S3, S5 |
| <a id="page-1954"></a>Page, E. S. (1954). Continuous inspection schemes. *Biometrika*, 41(1–2), 100–115. [doi:10.1093/biomet/41.1-2.100](https://doi.org/10.1093/biomet/41.1-2.100) | The CUSUM test: a lasting change in a series detected soon after it happens. | S1, S2, S6 |
| <a id="perold-1988"></a>Perold, A. F. (1988). The implementation shortfall: Paper versus reality. *Journal of Portfolio Management*, 14(3), 4–9. [doi:10.3905/jpm.1988.409150](https://doi.org/10.3905/jpm.1988.409150) | Implementation shortfall: the cost of trading measured against the price when the decision was taken. | S4–S6 |
| <a id="phillips-et-al-2011"></a>Phillips, P. C. B., Wu, Y., & Yu, J. (2011). Explosive behavior in the 1990s Nasdaq: When did exuberance escalate asset values? *International Economic Review*, 52(1), 201–226. [doi:10.1111/j.1468-2354.2010.00625.x](https://doi.org/10.1111/j.1468-2354.2010.00625.x) | Tests of explosive behaviour, by unit-root tests run on expanding windows. | S2, S6 |
| <a id="politis-romano-1994"></a>Politis, D. N., & Romano, J. P. (1994). The stationary bootstrap. *Journal of the American Statistical Association*, 89(428), 1303–1313. [doi:10.1080/01621459.1994.10476870](https://doi.org/10.1080/01621459.1994.10476870) | The stationary bootstrap: blocks of random length resampled from a dependent series. | S3, S4 |
| <a id="rubin-1984"></a>Rubin, D. B. (1984). Bayesianly justifiable and relevant frequency calculations for the applied statistician. *Annals of Statistics*, 12(4), 1151–1172. [doi:10.1214/aos/1176346785](https://doi.org/10.1214/aos/1176346785) | Posterior predictive checks: a model judged by comparing the data it would generate with the data observed. | S2 |
| <a id="shannon-1948"></a>Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423. [doi:10.1002/j.1538-7305.1948.tb01338.x](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x) | Entropy: how much information a distribution carries, and how evenly its outcomes spread. | S2 |
| <a id="sharpe-1966"></a>Sharpe, W. F. (1966). Mutual fund performance. *Journal of Business*, 39(1, Part 2), 119–138. [doi:10.1086/294846](https://doi.org/10.1086/294846) | The reward-to-variability ratio, since called the Sharpe ratio. | S4 |
| <a id="snodgrass-ahn-1985"></a>Snodgrass, R. T., & Ahn, I. (1985). A taxonomy of time in databases. In *Proceedings of the 1985 ACM SIGMOD International Conference on Management of Data* (pp. 236–246). ACM. [doi:10.1145/318898.318921](https://doi.org/10.1145/318898.318921) | Valid time and transaction time: the two clocks of a temporal database, and the queries as of either. | S1, S7 |
| <a id="stone-1974"></a>Stone, M. (1974). Cross-validatory choice and assessment of statistical predictions. *Journal of the Royal Statistical Society: Series B (Methodological)*, 36(2), 111–133. [doi:10.1111/j.2517-6161.1974.tb00994.x](https://doi.org/10.1111/j.2517-6161.1974.tb00994.x) | Cross-validation: a model chosen and assessed on data it was not fitted on. | S2, S4 |
| <a id="white-2000"></a>White, H. (2000). A reality check for data snooping. *Econometrica*, 68(5), 1097–1126. [doi:10.1111/1468-0262.00152](https://doi.org/10.1111/1468-0262.00152) | The reality check: whether the best of many strategies beats a benchmark once the search that found it is counted. | S4 |
