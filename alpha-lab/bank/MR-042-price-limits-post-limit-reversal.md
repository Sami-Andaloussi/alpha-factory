---
id: MR-042
title: Price limits and post-limit reversal
family: mean reversion and relative value
mechanism: [structural, microstructure]
asset_classes: [stocks, equity indices, bonds, commodities, currencies]
horizon: [days]
data: [daily futures prices, daily price limit rules, limit-hit dates, intraday prices]
status: untouched
---

## Mechanism

Price limits, and similar mechanisms such as circuit breakers, are a market friction that can create temporary imbalances. When a contract hits its daily limit, the adjustment of the price to information or to order pressure is interrupted or deferred. Two forces can follow: continuation, as price discovery is delayed until trading reopens, or reversal, if the initial move was overextended by liquidity pressure and counterparties can act once the constraint period ends. The mechanism is structural in futures markets because it depends on the rules of the market and on the dynamics of the orders blocked by the limit. It offers an explanation of "extreme move, then correction" patterns around limit episodes.

## Prediction

After a limit move, the price can either continue in the same direction when trading reopens, where the limit only delayed the adjustment, or reverse, where the initial move was overextended by liquidity pressure and counterparties can act once the constraint period ends. Ma, Rao and Sears (1989) study limit moves and price resolution in the Treasury bond futures market; Kim and Rhee (1997) discuss the effects of price limits and cite the futures evidence.

## What would refute it

- Price paths after limit moves no different from those after comparable large moves on days without a binding limit.
- No reversal after limit moves driven by liquidity pressure once trading resumes freely.
- Continuation and reversal after limit hits unrelated to whether the initial move was driven by information or by liquidity pressure.

## References

- Ma, C. K., Rao, R. P. and Sears, R. S. (1989). Limit Moves and Price Resolution: The Case of the Treasury Bond Futures Market. Journal of Futures Markets.
- Kim, K. A. and Rhee, S. G. (1997). Price Limit Performance: Evidence from the Tokyo Stock Exchange. Journal of Finance.
