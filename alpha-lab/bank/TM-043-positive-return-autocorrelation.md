---
id: TM-043
title: Positive return autocorrelation (variance ratio)
family: trend and momentum
mechanism: [behavioural, information, microstructure]
asset_classes: [equity indices, stocks]
horizon: [weeks, months]
data: [daily prices]
status: not-testable
---

## Mechanism

Positive autocorrelation of returns is the statistical basis of momentum. The variance ratio test of
Lo and MacKinlay (1988) compares the variance of returns over q periods with q times the variance of
one-period returns: a ratio above 1 indicates positive autocorrelation, a trending series, and a ratio
below 1 negative autocorrelation, a mean-reverting series.

Positive autocorrelation can come from three mechanisms that reinforce each other: underreaction, as
prices drift gradually towards fundamental value; positive feedback trading, as trend followers
create self-reinforcing loops; and lead-lag relations between assets. Microstructure effects, the
bid-ask bounce and nonsynchronous trading, can create spurious autocorrelation at very short
horizons.

## Prediction

Variance ratios of US stock indices are significantly above 1 at horizons of 2 to 16 weeks, which
rejects the random walk: weekly and monthly returns show significant positive autocorrelation,
especially for equally weighted indices, which are dominated by small capitalisations (Lo and
MacKinlay, 1988).

## What would refute it

Variance ratios of stock indices not significantly different from 1 at horizons of 2 to 16 weeks, or
positive autocorrelation that vanishes once bid-ask bounce and nonsynchronous trading are accounted
for. No difference between equally weighted and value-weighted indices.

## References

- Lo, A. W. & MacKinlay, A. C. (1988). Stock Market Prices Do Not Follow Random Walks: Evidence from a Simple Specification Test. Review of Financial Studies.
- Lo, A. W. & MacKinlay, A. C. (1990).
- Campbell, J. Y., Lo, A. W. & MacKinlay, A. C. (1997). The Econometrics of Financial Markets, ch. 2, sec. 2.4-2.5, pp. 27-66. Princeton University Press.
- Lo, A. W. & MacKinlay, A. C. (1999). A Non-Random Walk Down Wall Street, ch. 2-3 (variance ratio test). Princeton University Press.
