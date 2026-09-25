---
id: MR-010
title: Temporary price pressure (transitory price impact)
family: mean reversion and relative value
mechanism: [microstructure, flows]
asset_classes: [stocks, equity indices, bonds, commodities, currencies]
horizon: [intraday, days]
data: [intraday transaction prices, bid and ask quotes, order book data, block trades]
status: untouched
---

## Mechanism

A temporary imbalance between buy and sell orders can push the price beyond its short-term fundamental value simply because market depth is finite. An aggressive buying flow consumes the available liquidity, lifts the price and can attract further orders; a selling flow does the opposite. The observed price change then has two components: a permanent one, tied to information, and a transitory one, tied to the cost of absorbing the flow. When the imbalance disappears, the transitory component is reabsorbed. The books stress that prices often move in response to orders themselves, even without news.

A large order, especially one that carries no information or only part of it, moves the price beyond its immediate equilibrium level, and the displacement is then at least partly reabsorbed. The orders come from institutional investors, block traders, funds with liquidity needs, hedgers, rebalancers and sometimes forced sellers; the correction comes from liquidity suppliers, value traders, block intermediaries and opportunistic arbitrageurs. The structural cause is that the depth of the order book and of intermediaries' balance sheets is finite: to absorb a large quantity, the market demands a price concession. The concession is larger when counterparties fear they face private information, when the order is opaque, or when displayed liquidity is insufficient. If the order is motivated mainly by liquidity rather than information, part of the move is excessive and then reverses.

The central friction is uncertainty about the nature of the flow, information or liquidity, together with the limited capacity of liquidity providers to absorb order flow instantly without moving the price. Taking the other side of a flow requires capital, exposes the provider to adverse selection and is never riskless, because an arbitrageur cannot tell at once whether the flow is purely mechanical or carries private information; liquidity providers therefore protect their balance sheets with an excessive price concession. The reversal happens when the imbalance resolves (the execution programme ends, opposite orders arrive) and/or when the market updates its inference that the flow was non-informational: once the doubt is lifted or the order absorbed, market makers and arbitrageurs rebalance and the price returns towards a value closer to consensus. In standard models the transitory component of impact decays exponentially; Kissell (2013) writes the post-trade price as P(t) = P_fundamental + α·e^(−λt), where α is the initial impact and λ the speed of reversion. Only the permanent component reflects the information the order conveys. In the microstructure literature, models of continuous auctions (Kyle 1985, a model of linear impact) and vector autoregressions estimated on trades and quotes serve to separate the permanent and transitory components. In futures, the same mechanism works through the resilience of the order book and the compensation of market makers' inventory, especially on very liquid electronic markets.

## Prediction

Large trades, especially liquidity-motivated ones, are followed by a partial reversal of their price impact. The larger the impact (thin market, large order), the larger the potential reversal, provided the market has some depth and traders willing to take the other side. The phenomenon is documented for block trades; Kraus and Stoll (1972), cited in Market Liquidity, study block trades and the partial reversal of prices. Almgren et al. (2005) and Kissell (2013) estimate the permanent and temporary components of impact. The mechanism has been observed in stocks, indices, ETFs and electronic markets in general, mostly from intraday to a few days. It concerns in particular stress days, forced sales, index flows and synchronised withdrawals, and it bears on rebounds after sell-offs, gaps around rebalances, basket moves and post-stress corrections. It can extend beyond the day when execution is split into several tranches, when others front-run the order, when flow on the same side accelerates, or during forced liquidations.

## What would refute it

- Price impact of large liquidity-motivated orders that is fully permanent, with no decay.
- No relation between the size of the reversal and the size of the order or the depth of the market.
- No partial reversal after block trades.
- Reversals no larger after opaque orders or when displayed liquidity is thin.
- Impact that turns out to be almost entirely permanent.

## References

- Cartea, Á., Jaimungal, S. and Penalva, J. (2015). Algorithmic and High-Frequency Trading. Cambridge University Press. Chap. 12, Order Imbalance, pp. 312 ff.
- Foucault, T., Pagano, M. and Röell, A. (2013). Market Liquidity: Theory, Evidence, and Policy. Oxford University Press. Chapter Order Flow, Liquidity, and Securities Price Dynamics, pp. 79 ff.; transitory impact and resilience, pp. 130-180 (approximately).
- Market Liquidity (authors and year not specified). Introduction, pp. 15-17.
- de Jong, F. and Rindi, B. (2009). The Microstructure of Financial Markets. Cambridge University Press. Chap. 6, Price Effects of Trading, pp. 109 ff.; chap. 9, Price Discovery, pp. 159 ff.
- Lo, A. W. and MacKinlay, A. C. (1999). A Non-Random Walk Down Wall Street. Princeton University Press. Section 12.3.4, Return Reversals, pp. 385-386.
- Kyle, A. S. (1985). Continuous Auctions and Insider Trading. Econometrica.
- Hasbrouck, J. (1991). Measuring the Information Content of Stock Trades. Journal of Finance.
- Hasbrouck, J. (2007). Empirical Market Microstructure. Oxford University Press. Kyle model, VAR decomposition, pp. 50-80 (approximately).
- Kissell, R. (2013). The Science of Algorithmic Trading and Portfolio Management. Academic Press. Chap. 3-5, permanent and transitory impact model, exponential decay function, pp. 60-120 (approximately).
- Almgren, R., Thum, C., Hauptmann, E. and Li, H. (2005). Direct Estimation of Equity Market Impact. Risk.
- Harris, L. (2002). Trading and Exchanges: Market Microstructure for Practitioners. Oxford University Press. Chap. 15, Block Traders, pp. 322-336; chap. 16, Value Traders, pp. 338-339.
- Kraus, A. and Stoll, H. R. (1972). Price Impacts of Block Trading on the New York Stock Exchange. Journal of Finance.
