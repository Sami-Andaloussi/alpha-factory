---
id: LL-026
title: ETF arbitrage and the creation-redemption tether
family: lead-lag and information diffusion
mechanism: [structural, limits to arbitrage, microstructure, information]
asset_classes: [equity indices, stocks]
horizon: [intraday, days]
data: [ETF prices, ETF net asset values, constituent prices, creations and redemptions]
status: untouched
---

## Mechanism

The key mechanism of exchange-traded funds is the tether between the fund and its underlying basket,
maintained by in-kind creation and redemption. As soon as a gap opens between the ETF's price and the
implied value of the basket, authorised participants and market makers can arbitrage it by trading the
basket and creating or redeeming fund units.

This makes ETFs a natural setting for a two-way lead-lag: sometimes the basket leads, and sometimes the
ETF leads, when its secondary-market liquidity and the concentration of orders in it are greater in the
short run. The link is not a mere accounting identity but an institutional, convertible relation, which
makes it very binding.

The gap is not fully arbitraged away instantly because there are basket costs, slippage on the
constituents, financing frictions, cash components, operational constraints on authorised participants
and sometimes short-selling costs. These frictions, however, normally keep the gap within bounds.

## Prediction

The ETF's price and the value of its basket normally stay within a band set by the frictions of
arbitrage through creation and redemption; authorised participants and market makers can arbitrage a
gap by trading the basket and creating or redeeming units. Information passes in both directions:
sometimes the basket leads, and sometimes the ETF leads, when its secondary-market liquidity and the
concentration of orders in it are greater in the short run.

## What would refute it

- Gaps between the ETF's price and the value of its basket persist beyond the band set by basket costs,
  financing, cash components and short-selling costs.
- Creations and redemptions do not respond to premiums and discounts of the ETF price over its basket.
- Which of the ETF and the basket leads bears no relation to their relative short-term liquidity and
  concentration of orders.

## References

- Abner, David J. (2016). The ETF Handbook: How to Value and Trade Exchange Traded Funds, 2nd edition, pp. 20-28 on the tether between the ETF and its net asset value and arbitrage against the basket, and sections "Creation and Redemption Process" and "Client-Driven Creation and Redemption", pp. 44-46. Wiley.
