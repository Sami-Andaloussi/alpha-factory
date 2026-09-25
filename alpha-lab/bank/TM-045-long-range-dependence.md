---
id: TM-045
title: Long-range dependence (Hurst exponent)
family: trend and momentum
mechanism: [macroeconomic]
asset_classes: [equity indices]
horizon: [months, years]
data: [daily prices]
status: untouched
---

## Mechanism

The Hurst exponent H measures long-term dependence in a time series. For financial returns, H above
0.5 indicates long-term persistence, past positive returns predicting positive future returns even at
very long horizons; H equal to 0.5 corresponds to a random walk; H below 0.5 indicates
anti-persistence, or mean reversion.

If confirmed, long-range dependence would be consistent with markets that "remember" past shocks over
very long periods, creating persistent trends at every horizon. The economic mechanism would be
linked to very long-term structural factors: secular economic cycles, technological change and
demographic transitions.

## Prediction

Peters (1994) applies Hurst exponent analysis, through the rescaled-range (R/S) method, to financial
markets and finds values of H significantly above 0.5 for many indices, which would suggest long-term
dependence in financial returns. Lo (1991) criticises the standard R/S method for financial data: it
is strongly biased by short-term dependence, the autocorrelation at low lags; with a modified R/S
method that allows for short-term dependence, he finds no evidence of long-term dependence in US
stock indices, and Lo and MacKinlay conclude that long-range dependence is probably not a feature of
financial returns.

## What would refute it

Hurst exponents that fall to 0.5 once short-term dependence is accounted for, as with the modified
R/S statistic applied to US stock indices. Persistence that disappears at long horizons, or that is
explained entirely by short-term autocorrelation.

## References

- Lo, A. W. (1991). Long-Term Memory in Stock Market Prices. Econometrica.
- Peters, E. E. (1994). Fractal Market Analysis: Applying Chaos Theory to Investment and Economics. Wiley.
- Campbell, J. Y., Lo, A. W. & MacKinlay, A. C. (1997). The Econometrics of Financial Markets, ch. 2, sec. 2.5 (rescaled range statistic). Princeton University Press.
- Lo, A. W. & MacKinlay, A. C. (1999). A Non-Random Walk Down Wall Street, chapter on R/S analysis. Princeton University Press.
