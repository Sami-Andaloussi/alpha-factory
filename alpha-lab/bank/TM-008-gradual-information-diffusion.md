---
id: TM-008
title: Gradual information diffusion (newswatchers and momentum traders)
family: trend and momentum
mechanism: [information, behavioural, limits to arbitrage]
asset_classes: [stocks, equity indices, bonds, commodities, currencies]
horizon: [months]
data: [daily prices, market capitalisation, analyst coverage, futures prices]
status: untouched
---

## Mechanism

Momentum here comes from the incomplete speed at which information spreads through the market:
information neither reaches all investors nor is processed by them at the same time. The problem is
not only that investors process information badly: they do not all receive, read, understand and
relay the same information at the same time. Hong and Stein (1999) formalise this with two kinds of
agents. Newswatchers (non-speculating analysts, brokers), focused on fundamentals, observe private
or semi-public signals, process the news slowly and temporarily ignore prices; the information
spreads gradually among them, and because they do not perfectly infer each other's information from
prices, the first price move stays incomplete: the price jumps after good news but remains below its
fair level. Momentum traders (trend followers, trend-following funds) use simple univariate rules
and observe only recent price changes, inferring information from the price dynamics. One might
expect such traders, like unlimited arbitrageurs, to eliminate the inefficiency. Instead they add to
the impulse in the initial direction, prolonging the continuation at short to medium horizons, and
then push the price beyond its equilibrium value, from which a final correction brings it back
towards its true value. The result is a gradual rise rather than an instantaneous adjustment. The
model is built to generate underreaction and then momentum at intermediate horizons, with the
possibility, depending on its parameters, of overreaction and reversal at longer horizons: it
explains both the birth of momentum and why momentum can end in overreaction.

The mechanism is structural: participants and their signals are heterogeneous, information passes
through indirect channels (prices influence behaviour), and frictions such as the cost of
information, limited attention, the segmentation of information and trading constraints prevent
instantaneous arbitrage, so arbitrageurs fail to correct the misalignment quickly. By analogy, in
futures markets the same gradual diffusion can concern macroeconomic, political, inventory, credit
or regime news.

## Prediction

Returns show positive correlation over roughly 1 to 12 months (an intermediate momentum typically
lasting a few months), followed by a partial reversal at longer horizons. Empirical tests report
underreaction at short horizons and overreaction at longer ones, and the model has been extended to
cross-sectional momentum. The books recall that momentum is stronger where diffusion is slowest, in
small stocks and in stocks with low analyst coverage; it is also stronger where attention is
limited.

## What would refute it

No drift after news in stocks with slow diffusion (small, little covered, little followed), or
momentum no stronger there than elsewhere. Momentum not followed by a partial reversal at longer
horizons, or reversal that appears without prior underreaction.

## References

- Hong, H. & Stein, J. C. (1999). A Unified Theory of Underreaction, Momentum Trading, and Overreaction in Asset Markets. Journal of Finance (NBER working paper, 1997).
- Hong, H., Lim, T. & Stein, J. C. (2000). Bad News Travels Slowly: Size, Analyst Coverage, and the Profitability of Momentum Strategies. Journal of Finance.
- Thaler, R. H. (ed.) (2005). Advances in Behavioral Finance, Volume II, ch. 14 "A Unified Theory of Underreaction, Momentum Trading, and Overreaction in Asset Markets", p. 529, pp. 530-544 (newswatchers and momentum traders), PDF pp. 529-538; ch. 1 "A Survey of Behavioral Finance", pp. 70-72. Princeton University Press.
- Ilmanen, A. (2011). Expected Returns: An Investor's Guide to Harvesting Market Rewards, ch. 6 "Behavioral Finance", p. 158. Wiley.
- Gray, W. R. & Vogel, J. R. (2016). Quantitative Momentum: A Practitioner's Guide to Building a Momentum-Based Stock Selection System, ch. 6 "Maximizing Momentum: The Path Matters", pp. 100-103 and p. 121, PDF pp. 111-124. Wiley.
