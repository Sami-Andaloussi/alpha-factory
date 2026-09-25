---
id: MR-006
title: Glosten-Milgrom adverse-selection reversion
family: mean reversion and relative value
mechanism: [microstructure, information]
asset_classes: [stocks, equity indices, bonds, commodities, currencies]
horizon: [intraday]
data: [tick-by-tick transaction prices, bid and ask quotes, trade direction]
status: untouched
---

## Mechanism

In the sequential trade model of Glosten and Milgrom (1985), a market maker deals one at a time with traders who may be informed or uninformed. The market maker is Bayesian: each trade updates its belief about the fundamental value. After a series of trades in the same direction, which signals information, the midprice moves for good: this is the permanent component. After uninformed trades, the midprice corrects slightly in the opposite direction: this is a transitory component created by adverse selection. Adverse selection thus leaves a measurable transitory component in the dynamics of the price, and that component is the source of a partial reversion.

The participants are the Bayesian market maker, informed traders, and uninformed traders (noise traders or liquidity traders). The mechanism needs a mixed population of the two, and it disappears if every trader is informed (the no-trade theorem). It is strong in markets with little public information, and in some specialised futures markets. It is related to the decomposition of prices into permanent and transitory components, to Kyle's model and to the bid-ask spread.

## Prediction

Quote revisions after trades have a permanent part and a transitory part: after uninformed trades, part of the move of the midprice reverses, while after sequences of informed trades it does not. The transitory adverse-selection component is strong where public information is scarce. The model is that of Glosten and Milgrom (1985), and Hasbrouck (2007) formalises it empirically.

## What would refute it

- Midprice moves after trades that are entirely permanent, with no partial reversal after trades later revealed to be uninformed.
- A transitory component that is no larger in markets with scarce public information.
- Reversals of quote revisions fully explained by inventory or order-processing effects, leaving nothing attributable to the market maker's updating of beliefs about informed trading.

## References

- Glosten, L. R. and Milgrom, P. R. (1985). Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders. Journal of Financial Economics.
- Hasbrouck, J. (2007). Empirical Market Microstructure. Oxford University Press. Chap. 5, the Glosten-Milgrom model, pp. 55-75 (approximately).
