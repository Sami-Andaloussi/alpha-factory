---
id: MR-013
title: Liquidity imbalance overshoot
family: mean reversion and relative value
mechanism: [microstructure]
asset_classes: [stocks]
horizon: [intraday, days]
data: [intraday transaction prices, trading volumes, order book depth]
status: untouched
---

## Mechanism

When a one-sided flow of buying or selling consumes the available liquidity, the price temporarily overshoots its equilibrium value. Market makers and opportunistic liquidity providers recognise the overshoot and trade in the opposite direction, earning the liquidity premium and bringing the price back to equilibrium. Narang (2024) identifies this as one of the two basic drivers of short-term reversion strategies. It is distinct from the informational overshoot: no fundamental signal is involved, and it is the demand for liquidity itself that causes the move that later reverses.

The participants are the traders who demand liquidity and create the overshoot, the liquidity providers and market makers who supply the reverting force, and very short-term arbitrageurs. The effect is more pronounced in markets where the order book is thin and at peaks of volume. The theory is related to transitory price impact, market resilience, the bid-ask bounce and the informational overshoot.

## Prediction

During one-sided flows that consume liquidity, prices move beyond their equilibrium value and then revert over a very short horizon, from intraday to a few days at most. The overshoot and the reversal are larger in thin order books and at volume peaks.

## What would refute it

- Moves on volume peaks in thin order books that do not reverse within a few days.
- Overshoots no larger in thin books than in deep ones.
- Reversals that turn out to follow fundamental news, showing the initial move to be informational rather than a liquidity overshoot.
- No sign of liquidity providers trading against the overshoot.

## References

- Narang, R. K. (2024). Inside the Black Box (3rd edition). Wiley. Chapter on short-term reversion strategies, basic mechanisms, pp. 100-140 (approximately).
