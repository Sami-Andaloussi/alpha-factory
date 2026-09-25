---
id: LL-032
title: Cash-futures price discovery
family: lead-lag and information diffusion
mechanism: [information, microstructure, limits to arbitrage, structural]
asset_classes: [equity indices, stocks]
horizon: [intraday, days]
data: [index futures prices, cash index and constituent prices, tick-by-tick trades and quotes]
status: untouched
---

## Mechanism

Futures contracts on an index or on an aggregate asset can incorporate information before the cash, or
spot, market. The futures market then leads, and the information spreads from it to the cash basket or
to the constituents.

The structural mechanism is classic: low transaction costs, high implicit leverage, easier short
selling, concentrated liquidity, fast execution, and a preference of informed and macro traders for
futures. When information concerns the index or systematic risk, the future often reacts before the cash
market. Index-futures arbitrage then passes the signal on, with a delay that can be non-zero when there
are operational frictions, desynchronised quotes or balance-sheet constraints. Common information is
thus discovered first in the more efficient vehicle and then spreads to the underlying assets.

## Prediction

Index futures prices often lead the cash index and its constituents. The lead has been studied in the
literature on price discovery (Chan, 1992; Chu et al., 1999; Stoll and Whaley, 1990; Hasbrouck, 2003);
many of the results place the lead at intraday horizons, often close to microstructure. The direction of
causality depends on periods of stress, on the opening and closing of markets and on the structure of
quotation.

## What would refute it

- The cash market leads the futures market as often as the reverse, for news about the index or about
  systematic risk.
- The lead of futures over the cash index comes entirely from stale quotes of the index components
  rather than from faster incorporation of information in the futures market.
- The lead does not depend on the cost, leverage, short-selling and liquidity advantages of futures over
  the cash basket.

## References

- Chan, Kalok (1992). A Further Analysis of the Lead-Lag Relationship Between the Cash Market and Stock Index Futures Market. Review of Financial Studies.
- Hasbrouck, Joel (2003). Intraday Price Formation in U.S. Equity Index Markets. Journal of Finance.
- Stoll, Hans R. and Robert E. Whaley (1990). Work on stock index futures and the cash market.
- Chu et al. (1999). Work on futures versus spot price discovery.
