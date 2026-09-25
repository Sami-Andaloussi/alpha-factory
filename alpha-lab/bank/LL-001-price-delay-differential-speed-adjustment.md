---
id: LL-001
title: Price delay and differential speed of adjustment
family: lead-lag and information diffusion
mechanism: [information, microstructure, limits to arbitrage]
asset_classes: [stocks, sectors, equity indices, bonds, commodities, currencies, crypto]
horizon: [intraday, days, weeks, months]
data: [daily prices, weekly returns, intraday transaction prices, market capitalisation, trading volumes, analyst coverage, bid-ask spreads, bond prices, macroeconomic releases, futures prices by contract and maturity, prices across venues]
status: untouched
---

## Mechanism

Information is not incorporated into all securities at the same time. Large, liquid, heavily traded
stocks that many analysts follow absorb it faster than small stocks, illiquid securities or
securities with little information coverage. The pattern is therefore not only "large leads small"
but, more broadly, a gradient in the speed at which prices adjust. The same hierarchy appears across
asset classes: the asset that is larger, more liquid, more closely followed, more actively traded or
further upstream in the chain of information leads the one that is smaller, less liquid or further
downstream. Examples of a leader and a related but less reactive laggard are large stocks and small
stocks, a main index and a peripheral basket, a leading sector and its subcontractors, a central
market and a less liquid one. Large capitalisations, the most followed stocks or sector leaders may
reprice first, then small capitalisations, related stocks or the other members of an industry follow
with a delay: the lead-lag is an observable manifestation of the incomplete diffusion of information.

The cause lies in frictions in the processing and transmission of information: the cost of
attention, the cost of collecting information, the time needed to interpret news, the segmentation of
the investor base and of clienteles, liquidity and arbitrage constraints, and weak economic incentives
to arbitrage small gaps in securities that are costly to trade. Even when public information is
available to everyone, it is assimilated unevenly, so the market is not instantly efficient security
by security: investors' attention is limited, trading is not synchronous, trading costs and analyst
coverage differ from one asset to another, and many participants react with a delay. Flows,
attention, liquidity and the speed of information processing create a hierarchy of reaction: the
leaders quickly synthesise the common information, and the followers adjust only afterwards.

The gap is not only a matter of how many analysts follow a stock. Trading is itself the vehicle
through which information enters prices: a security that trades rarely cannot quickly reveal the
state of marginal beliefs. Large and frequently traded stocks thus become the first receivers of
macroeconomic, sector or sentiment information, while small, less traded stocks adjust their prices
later. Information enters first where costs are low, depth is large, market makers and arbitrageurs
are numerous and informed traders can take positions quickly. The followers then adjust to the
leader's moves through arbitrage, informational imitation, portfolio reallocation or simply by
updating their quotes. The frictions that keep the gap open are wider spreads, inventory risk, low
turnover, the lack of an immediate counterparty, transaction costs, structural latencies, the
heterogeneity of participants and, often, weaker institutional attention. The core of the theory is
thus not a raw statistical relation but a hierarchy in the speed of information incorporation set by
liquidity: a fast-to-slow diffusion between instruments that are close but differ in liquidity, in
which the leader is the market that adjusts first (leadership as speed of adjustment). The same
gradient underlies several variants of lead-lag: the size lead-lag, the industry lead-lag, the
geographic lead-lag and the analyst-network lead-lag.

The literature holds that the lead-lag can also account for part of the profits of contrarian
strategies, which do not necessarily come from pure, stock-by-stock overreaction. If large stocks or the
most liquid assets react to news first and the others afterwards, the laggards catch up after a move by
the leaders, which can look like a contrarian reversal while it is in fact the lead-lag, even if
individual returns are not strongly negatively autocorrelated. A "winners minus losers" portfolio can
show negative autocorrelation because the winners, often the more liquid assets, move first and the
losers catch up, which creates a correction in the relative spread. What is out of step is not each
asset reverting to its own mean but the timing relation between several assets: the gap is not
necessarily an excess of absolute valuation but a temporary inconsistency between economically close
assets. At short horizons this generates cross signals that may resemble convergence or catch-up, and a
mean-reversion signal can in reality be a signal of relative informational catch-up. The effect is
intertwined with industry lead-lag, economic networks, the relation between large and small stocks and a
large part of statistical arbitrage.

The lead-lag is likewise a structural explanation of part of momentum: assets do not incorporate the
same common information at the same pace, and momentum emerges because an investor can use the
reactions already observed in the fast segments to anticipate the future adjustments of the slow
ones. Part of momentum can come from a genuine continuation specific to the asset, but another part
can come from the sequential propagation of a common factor: a sector leads and another follows,
large capitalisations reprice first and smaller ones afterwards, a liquid market takes the shock first
and related markets follow. This suggests that continuation may lie not only in an asset's own
persistence but in the ordered propagation of a shock through a network of assets. The explanation
concerns in particular futures universes linked by macroeconomic themes, sectors or physical chains.

Non-synchronous trading adds a measurement component. In a portfolio or index made of assets whose last
trades are not simultaneous, particularly illiquid ones, returns computed from last traded prices
introduce an artificial positive autocorrelation in the index and spurious cross-autocorrelations
between assets; for individual assets, non-synchronous trading contributes to the measured
autocorrelation. Campbell, Lo and MacKinlay (1997) give a formal model that splits the autocorrelation
of individual and index returns into components attributable to non-synchronous trading. This part is a
measurement artefact, stronger for illiquid assets (small capitalisations, some commodities, emerging
markets) and weaker for liquid futures that trade continuously. The econometric books add that part of a
measured lead-lag can be artificially amplified by non-synchronous trading, but that non-synchronous
trading does not explain the whole phenomenon. By analogy, the mechanism carries over to futures, where
the more liquid contracts discover prices before adjacent markets, and to multi-venue markets such as
crypto, where information and order flow are not absorbed simultaneously across venues.

## Prediction

The returns of large, liquid, widely followed and heavily traded securities lead those of small,
illiquid and little-followed ones: past returns of the fast group predict later returns of the slow
group, in the same direction. The laggard is the less liquid, less followed, smaller or more downstream
member of the pair: small stocks after large ones, the peripheral basket after the main index,
subcontractors after the leading sector, the less liquid market after the central one. The pattern
appears as cross-autocorrelations between returns, one asset's return being correlated with another
asset's lagged return, and it is stronger when the differences in liquidity and in the speed of price
discovery between assets are large. In US equities, "delay" measures capture the share of a stock's
price variation that responds late to market or industry information; stocks with a high delay also
often have higher expected returns, which suggests that the delay reflects structural frictions rather
than statistical noise. The horizon observed in the literature is typically daily to monthly; the
lead-lag is documented mostly on stocks, in particular on US stocks, at very short to short horizons,
from days to a few weeks.

Lo and MacKinlay (1990) document that US large capitalisations tend to lead small capitalisations by
about a week: the weekly returns of large stocks positively predict the next week's returns of small
stocks, with a significantly positive lagged cross-correlation. Part of the profit of contrarian
portfolio strategies, which buy past losers and sell past winners, comes from these lagged
cross-correlations: in the results of Lo and MacKinlay (1990), a substantial part of contrarian
profits comes from cross-autocorrelations rather than from the isolated rebound of losers. The lead-lag
also gives rise to a cross-sectional momentum: the followers move after, and in the direction of, an
earlier move by the leaders. The chapters on momentum recall that broad-market lead-lag is not enough
to explain all momentum profits, while lead-lag effects at the level of industries and finer factors
matter more. Index returns built from stale prices show positive autocorrelation, and variance-ratio
tests computed on such indices are biased.

In futures, lead-lag relations are documented between broad equity index futures and sector index
futures, between futures on major commodities (WTI) and their sector derivatives, and between the
maturities of one curve, where the front contract leads the deferred contracts. These relations are more
robust than among stocks, because liquidity is even more heterogeneous across futures markets. In
another asset class, Foucault, Pagano and Röell show that US Treasuries react to macroeconomic
announcements faster than municipal bonds, because the Treasury market is more liquid and more active.
The leader is not fixed: it can change with the volatility regime, the time of day or the structure of
order flows.

## What would refute it

- No lead-lag relation between large or liquid assets and small or illiquid ones: the lagged returns
  of the leaders do not predict those of the followers.
- The lead of large, liquid securities over small, illiquid ones disappears once prices are sampled
  synchronously: part of a measured lead-lag can come from non-synchronous trading (the stale prices
  of rarely traded securities), a measurement artefact rather than the economic mechanism, and
  cross-autocorrelations that vanish entirely under synchronous sampling would reduce the effect to
  that artefact. Likewise, lagged returns of large, liquid or leading assets that carry no information
  about the next returns of small, illiquid or following assets once non-synchronous trading is
  corrected for.
- The predictability exists only at very short horizons, where it is a microstructural artefact
  rather than an economic relation, and vanishes at longer horizons.
- The measured delay is fully accounted for by other effects it can capture: information
  discreteness, microstructure noise, or common exposures that are slow to be recognised.
- The speed of adjustment and the order of reaction bear no relation to liquidity, trading frequency,
  size, analyst coverage, attention, flows or position in the chain of information; the lead-lag is as
  strong between unrelated assets as between economically close ones, or no stronger where
  differences in liquidity and in the speed of price discovery are larger; or the ranking of leaders
  and followers changes so often with the volatility regime, the time of day or order flows that no
  stable hierarchy remains.
- Contrarian profits that come entirely from the own-autocorrelation of individual returns, with no
  contribution from lagged cross-correlations between assets.
- No part of momentum profits comes from lead-lag between assets: after a move by the leaders, the
  followers show no later move in the same direction.
- Stocks with a high delay do not earn higher expected returns than stocks with a low delay.
- A more liquid market reacts to the same announcement no faster than a less liquid one, for example
  Treasuries and municipal bonds adjusting to macroeconomic news at the same speed.
- Front futures contracts, broad equity index futures and major commodity futures not leading their
  deferred, sector or related contracts.

## References

- Hou, Kewei and Tobias J. Moskowitz (2005). Market Frictions, Price Delay, and the Cross-Section of Expected Returns. Review of Financial Studies.
- Chordia, Tarun and Bhaskaran Swaminathan (2000). Trading Volume and Cross-Autocorrelations in Stock Returns. Journal of Finance.
- Lo, Andrew W. and A. Craig MacKinlay (1999). A Non-Random Walk Down Wall Street, ch. 5 "When Are Contrarian Profits Due to Stock Market Overreaction?", p. 117 ff., notably "Trading on White Noise and Lead-Lag Relations" and sec. 5.3.4 "Lead-Lag Effects and Nonsynchronous Trading", pp. 126-142 (sec. 5.3.4: pp. 127-130); ch. 2-5; ch. 4-5 on nonsynchronous trading, lead-lag effects and cross-autocorrelations, PDF pp. 99-119 and 139-155. Princeton University Press.
- Lehalle, Charles-Albert and Sophie Laruelle (2018). Market Microstructure in Practice, 2nd edition, appendix A.13.2 "Correlation and Epps Effect", p. 318. World Scientific.
- Foucault, Thierry, Marco Pagano and Ailsa Röell (2013). Market Liquidity: Theory, Evidence, and Policy, chapter "Trading Mechanics and Market Structure", p. 32. Oxford University Press.
- Hasbrouck, Joel (2007). Empirical Market Microstructure: The Institutions, Economics, and Econometrics of Securities Trading, ch. 10, pp. 100-103. Oxford University Press.
- Lo, Andrew W. and A. Craig MacKinlay (1990). When Are Contrarian Profits Due to Stock Market Overreaction? Review of Financial Studies.
- Lo, Andrew W. and A. Craig MacKinlay (1990). An Econometric Analysis of Nonsynchronous Trading. Journal of Econometrics.
- Hou, Kewei (2007). Industry Information Diffusion and the Lead-Lag Effect in Stock Returns. Review of Financial Studies.
- Campbell, John Y., Andrew W. Lo and A. Craig MacKinlay (1997). The Econometrics of Financial Markets. Princeton University Press. Ch. 2, pp. 27-66, including sec. 2.2.2 "Sequences and Reversals, and Runs", p. 34 ff.; pp. 45-50 (cross-autocorrelations and non-synchronous trading) and PDF pp. 45-58 and 220-223 (cross-autocorrelations and lead-lag relations); ch. 3, sec. 3.1-3.2, pp. 62-79 (non-synchronous trading); pp. 153-164 (predictable variation in returns), p. 217 (integration and term premia), pp. 306-310 and p. 409.
- Cochrane, John H. (2005). Asset Pricing. Revised edition. Princeton University Press. P. 409.
- Murphy, John J. (2004). Intermarket Analysis: Profiting from Global Market Relationships. Wiley. Chapter 6, pp. 101-103.
- Tsay, R. S. (2010). Analysis of Financial Time Series (3rd edition), ch. 5, sec. 5.1 "Nonsynchronous Trading", p. 259 ff. Wiley.
- Thaler, Richard H. (ed.) (2005). Advances in Behavioral Finance, Volume II, ch. 10 "Momentum", pp. 366-368, section "Lead-lag Effects and Momentum Profits", p. 393, and the transition to "Industry Momentum", p. 395. Princeton University Press.
- Ilmanen, Antti (2011). Expected Returns: An Investor's Guide to Harvesting Market Rewards, ch. 14 "Momentum in Other Asset Classes", pp. 400-401. Wiley.
- Jegadeesh, N. and S. Titman (1993). Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency. Journal of Finance.
- Moskowitz, T. J. and M. Grinblatt (1999). Do Industries Explain Momentum? Journal of Finance.
