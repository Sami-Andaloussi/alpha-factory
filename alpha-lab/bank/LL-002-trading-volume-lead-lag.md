---
id: LL-002
title: Trading-volume lead-lag
family: lead-lag and information diffusion
mechanism: [information, microstructure]
asset_classes: [stocks]
horizon: [days, weeks, months]
data: [daily prices, trading volumes, market capitalisation]
status: untouched
---

## Mechanism

This is a specific form of the differential speed of price adjustment: stocks with high trading volume
incorporate information before stocks with low trading volume. The lead-lag does not come from a mere
size artefact; it is read as a difference in the speed of price discovery that depends on the intensity
of trading.

Heavily traded stocks concentrate more attention, more informed orders, more market making, more
revisions of opinion and a stronger economic incentive to arbitrage price misalignments. Thinly traded
stocks react late, either because the information reaches them later or because it enters their prices
more slowly for lack of counterparties and participation. Volume is thus the channel through which
information is absorbed. Common information is discovered first in "central" stocks and then spreads
to peripheral ones.

The mechanism can combine with other dimensions of the lead-lag: size, analyst coverage, ETF ownership
and centrality within a sector. When flows are driven by non-informational shocks, such as
liquidity-driven trading or uninformed rebalancing, volume can also transmit a temporary price pressure
that has no fundamental content.

## Prediction

The literature shows that past returns of high-volume stocks predict the returns of low-volume stocks,
even after the standard controls; the pattern is not a mere size artefact. It has been documented mainly
in US equities, at short to intermediate horizons.

## What would refute it

- Once size and the standard controls are accounted for, the returns of high-volume stocks no longer
  predict those of low-volume stocks.
- High-volume stocks do not incorporate information before low-volume stocks: the speed of price
  discovery does not depend on the intensity of trading.
- What high-volume stocks pass on to low-volume stocks later reverses, as a temporary price pressure
  without fundamental content would, instead of persisting as information does.

## References

- Chordia, Tarun and Bhaskaran Swaminathan (2000). Trading Volume and Cross-Autocorrelations in Stock Returns. Journal of Finance.
- Lo, Andrew W. and A. Craig MacKinlay (1990). When Are Contrarian Profits Due to Stock Market Overreaction? Review of Financial Studies.
