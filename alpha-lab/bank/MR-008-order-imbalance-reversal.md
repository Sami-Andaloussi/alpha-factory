---
id: MR-008
title: Order imbalance reversal
family: mean reversion and relative value
mechanism: [microstructure]
asset_classes: [stocks, equity indices, bonds, commodities, currencies, crypto]
horizon: [intraday, days]
data: [intraday transaction prices, signed trade volumes, order book data, daily prices, macroeconomic release dates]
status: untouched
---

## Mechanism

Order imbalances, especially non-informational ones that reflect a demand for liquidity, can move prices, and the moves can be followed by reversals once the imbalance disappears. A persistent imbalance between buy and sell orders creates a temporary price pressure. The imbalance is itself transitory: in most cases it reflects impatience (urgency) rather than fundamental information; once the one-sided flow is exhausted, the price returns towards its equilibrium level. The channel has three steps: the market must clear in the short run through a price adjustment; the pressure is then absorbed gradually as liquidity is supplied; and the price corrects when the market concludes that the order flow carried no lasting information. Foucault, Pagano and Röell (2013) model this movement explicitly as a reverting process.

The mechanism is double. Large investors often split their orders over several days, which creates persistent order imbalances: fragmented metaorders exert autocorrelated directional pressure. Market makers and other counterparties change their quotes and spreads to absorb this flow and control their inventory, but part of the resulting displacement is transitory, because it mostly pays for carrying inventory rather than reflecting fundamental information. As long as the flow continues, the price can drift in its direction; once the imbalance is absorbed or ends, the price partly reverses. The result is continuation conditional on the current flow, and reversal once the current flow is controlled for. In a more general microstructure reading, the market also partly anticipates future order flow, which ties the theory to the literature on market impact and metaorders.

The participants are directional traders, who create the imbalance; market makers, who absorb it; and arbitrageurs, who profit from the return to equilibrium. The effect is not fully arbitraged away because the arbitrageur must absorb flow in turn, bear the risk that the metaorder lasts longer than expected, and pay transaction costs; the costs of carrying inventory and the segmentation and limited capacity of natural counterparties keep it alive. It is structurally stronger when institutional investors fragment their trades, when the order book is shallow and when the flow is concentrated. Imbalances are more pronounced around macroeconomic announcements, market opens and news events, and the reversion is faster the more liquid the market. By analogy, the logic carries over to crypto spot markets, where order-book depth and the heterogeneity of participants make order-flow imbalance very central. By analogy, in futures, the imbalance takes the form of aggressive orders on the book, or market orders.

## Prediction

Price moves that accompany non-informational order imbalances can be followed by moves of opposite sign once the imbalance fades. In stocks, this logic is documented through the relation between order imbalance, current return and future return: the literature shows that, after controlling for the current imbalance, past imbalances predict price moves of opposite sign, consistent with a transitory price-pressure component. Order imbalance is correlated with price moves and with the dynamics of liquidity, both at the aggregate market level and in the cross-section. Harris (1989) studies order imbalances and stock price movements on 19 and 20 October 1987, and Anastasopoulos et al. (2026) study order flow and cryptocurrency returns. By analogy, in futures, the theory takes the form of a reversal after an imbalance or of a mean reversion after execution pressure.

## What would refute it

- Past order imbalances that do not predict opposite-sign returns once the current imbalance is controlled for.
- Price moves that follow non-informational imbalances and are fully permanent.
- Reversals no stronger when institutional investors fragment their orders, when the book is shallow, or when the flow is concentrated.
- Reversion no faster in more liquid markets.
- Imbalances that turn out to be mostly informed, so that the moves they cause persist.

## References

- Chordia, T., Roll, R. and Subrahmanyam, A. (2004). Order Imbalance and Individual Stock Returns: Theory and Evidence. Journal of Financial Economics.
- Chordia, T., Roll, R. and Subrahmanyam, A. (2002). Order Imbalance, Liquidity, and Market Returns. Journal of Financial Economics.
- Harris, L. (1989). Order Imbalances and Stock Price Movements on October 19 and 20, 1987. Journal of Finance.
- Jaisson, T. (2014). Market Impact as Anticipation of the Order Flow Imbalance.
- Anastasopoulos, A. et al. (2026). Order flow and cryptocurrency returns.
- Bozzetto, C. (undated). Cryptocurrency markets microstructure (survey or thesis).
- Foucault, T., Pagano, M. and Röell, A. (2013). Market Liquidity: Theory, Evidence, and Policy. Oxford University Press. Sections on order imbalances and temporary price reversion, pp. 130-180 (approximately).
- Harris, L. (2002). Trading and Exchanges: Market Microstructure for Practitioners. Oxford University Press. Sections on price pressure and large trades.
