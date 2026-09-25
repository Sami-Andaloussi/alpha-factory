---
id: TM-005
title: Conservatism and representativeness (investor sentiment model)
family: trend and momentum
mechanism: [behavioural, limits to arbitrage]
asset_classes: [stocks, crypto]
horizon: [months, years]
data: [daily prices, earnings announcement dates]
status: untouched
---

## Mechanism

Barberis, Shleifer and Vishny (1998) propose a model in which investors form their expectations with
two heuristics. Conservatism is the slow adjustment of beliefs to new information: after an isolated
piece of news, investors update too little and cling to their priors. Representativeness, in the
sense of Tversky and Kahneman (1974), is the tendency to judge the probability of a future event by
its resemblance to past cases while neglecting base rates: after a series of consecutive good (or
bad) news, investors generalise too quickly and assume that the trend will continue, whatever the
fundamentals.

In the one-asset version of the model, the fundamental follows a random walk, but the investor
wrongly believes that it alternates between a mean-reverting regime and a trending regime. The
biased Bayesian forecasts that result create a lasting spread between the market price and the
fundamental value. While the investor believes in the mean-reverting regime, conservatism produces
an underreaction to good news: the price adjusts only partly, which creates positive short-term
autocorrelation and a drift after announcements. After several shocks of the same sign, the investor
overweights the probability that the world is in the trending regime, extrapolates the series and
buys aggressively, pushing the price beyond fundamentals; the correction of this overreaction comes
later. The same heuristics therefore generate momentum first and reversal later, and the buying
driven by representativeness also amplifies the initial trend in the short run.

The distortion persists because prices reflect an aggregate equilibrium between agents who behave
differently, and complete correction is not instantaneous, so prices keep following their trend
despite attempts at arbitrage. The actors are individual investors and rational arbitrageurs.
Investors' expectations are wrong and unpredictable, and rational arbitrageurs hesitate to oppose
them for fear of noise-trader risk: facing these distortions they bear a risk of short-term losses,
and capital and risk constraints limit the size of their positions. The frictions are amplified by
institutional herding and positive feedback trading: when prices rise through representativeness,
trend followers enter and push the move further. The mechanism concerns traditional equities as well
as crypto-assets, where the lack of fundamentals reinforces the biases.

## Prediction

Prices underreact to news in the short run and overreact over longer horizons. Underreaction, driven
by conservatism, operates in the short run, over 1 to 12 months or 3 to 12 months, producing
positive autocorrelation and momentum, including drifts after announcements. Overreaction, driven by
representativeness after long series of news of the same sign, sets in over several quarters as
further information accumulates, and produces mean reversion over several years, roughly 2 to 5 or 3
to 5 years: the long-run reversal documented by De Bondt and Thaler (1985). The length of the
momentum phase, from about a semester to a few years, depends on how long the sentiment persists.
The model is built to reproduce this pattern of short-term continuation followed by long-term
reversal, and it aims to explain a set of regularities: post-announcement drifts and the return
patterns that follow series of good or bad news.

## What would refute it

Returns showing no positive autocorrelation over 1 to 12 months after news, and no reversal over 2
to 5 years. Prices that move by the full amount of an isolated announcement on the announcement
itself. Stocks with long series of good news performing no worse over the following years than
stocks with mixed news, or performing no better in the short run. Arbitrage capital that corrects
the spread between price and fundamental value quickly, even when sentiment is persistent.

## References

- Tversky, A. & Kahneman, D. (1974). Judgment under Uncertainty: Heuristics and Biases. Science.
- De Bondt, W. F. M. & Thaler, R. (1985). Does the Stock Market Overreact? Journal of Finance.
- Barberis, N., Shleifer, A. & Vishny, R. (1998). A Model of Investor Sentiment. Journal of Financial Economics.
- Thaler, R. H. (ed.) (2005). Advances in Behavioral Finance, Volume II, ch. 12 (Barberis, Shleifer and Vishny), pp. 433-449. Princeton University Press.
- Gray, W. R. & Vogel, J. R. (2016). Quantitative Momentum: A Practitioner's Guide to Building a Momentum-Based Stock Selection System, ch. 3. Wiley.
