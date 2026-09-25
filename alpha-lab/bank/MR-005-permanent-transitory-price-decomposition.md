---
id: MR-005
title: Permanent-transitory price decomposition (generalised Roll model)
family: mean reversion and relative value
mechanism: [microstructure]
asset_classes: [stocks]
horizon: [intraday]
data: [transaction prices, bid and ask quotes, signed order flow]
status: untouched
---

## Mechanism

Any shock to the price of an asset can be split into a permanent component, associated with fundamental information, and a transitory component, associated with market frictions: the spread, dealers' inventory, noise. By definition the transitory component has a mean of zero over the long run: it disappears, and its disappearance is the reversion. Harris (2002) distinguishes transitory volatility from fundamental volatility.

Roll's (1984) model is the elementary case: the spread generates a negative autocovariance of successive price changes equal to −(s/2)², where s is the effective spread. Hasbrouck (2007) generalises the framework into a multivariate vector moving-average (VMA) decomposition, which identifies the permanent share of the price variance and so measures how much a market contributes to price discovery (its information share).

The participants are market makers, who manage their inventory and set the spread; informed arbitrageurs, whose trading pulls the price back towards fundamental value; and investors who demand liquidity through market orders. The frictions that feed the transitory component are adverse selection, order-processing costs and inventory costs: the stronger they are, the larger the transitory component and the larger the potential reversion. The framework is linked to the bid-ask bounce, to the distinction between permanent and temporary market impact, to price discovery and to Kyle's model.

## Prediction

Price changes contain a component that reverses, and the stronger the frictions (adverse selection, order-processing costs, inventory costs), the larger this transitory component and the wider the potential reversion. Roll (1984) and Hasbrouck (1993) formalise the decomposition, and Hasbrouck (2007) estimates it on intraday data for US equities.

## What would refute it

- Transaction-price changes in assets with sizeable frictions that behave like a pure random walk, with no reverting component.
- A transitory component that does not grow with adverse selection, order-processing costs or inventory costs.

## References

- Roll, R. (1984). A Simple Implicit Measure of the Effective Bid-Ask Spread in an Efficient Market. Journal of Finance.
- Hasbrouck, J. (1993). Assessing the Quality of a Security Market: A New Approach to Transaction-Cost Measurement. Review of Financial Studies.
- Hasbrouck, J. (2007). Empirical Market Microstructure. Oxford University Press. Chap. 3-6, generalised Roll model, VMA decomposition, information share measures, pp. 30-100 (approximately).
- Harris, L. (2002). Trading and Exchanges: Market Microstructure for Practitioners. Oxford University Press. Sections on transitory versus fundamental volatility.
