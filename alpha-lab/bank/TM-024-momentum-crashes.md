---
id: TM-024
title: Momentum crashes (state-dependent momentum risk)
family: trend and momentum
mechanism: [risk premium, limits to arbitrage]
asset_classes: [stocks, crypto]
horizon: [days, weeks, months]
data: [daily prices, market index returns, realised volatility]
status: tested-inconclusive
---

## Mechanism

This theory addresses not the birth of momentum but why it can persist on average while being
dangerous. Momentum strategies have a strongly negative skewness, a fat left tail: they earn regular
gains most of the time and suffer rapid, severe losses in rare episodes, the momentum crashes, which
are sequences of persistent losses. The risk of momentum is conditional and varies strongly, the
crashes being associated with market states of panic or high volatility and sometimes with rebounds.
The main explanation proposed by Barroso and Santa-Clara (2015) is that momentum is sensitive to
volatility regimes: in calm periods momentum positions perform well, but when volatility explodes,
in a stock market crash or a crypto crash, momentum produces massive losses.

These episodes were documented and analysed by Daniel and Moskowitz (2016). The mechanism of a crash
runs through rebounds. In a deep bear market, recent losers are often heavily oversold in the short
term. When the market rebounds sharply, these losers rebound disproportionately, their very low
valuations giving them a high implicit leverage, and the short positions of a momentum portfolio on
these losers suffer severe losses. Momentum therefore has an implicit short exposure to market
options, with a concave profile at turning points, and the losers behave like options.

Barroso and Santa-Clara (2015) and Daniel and Moskowitz (2016) link part of the reward of momentum to
a premium for bearing these tail risks, tied to the structure of the payoffs, which makes the
phenomenon compatible with a compensation for risk rather than a simple inefficiency: investors
demand a reward for carrying this risk. The existence of the crashes, and their partial
predictability, also explains why "smooth" arbitrage of momentum can be limited: the strategy can be
hard to hold through its tail risk, hence a constrained capacity for arbitrage. The actors are
momentum investors, such as quant funds, who take on this tail risk.

## Prediction

Barroso and Santa-Clara (2015) find that momentum has historically offered the highest Sharpe ratio
among the classic factors while suffering very severe crashes (negative skewness). The worst crashes
occurred in 1932, in the rebound after the 1929 crash, in 2001 and 2002, in the technology rebound,
and in 2009, in the rebound after the Lehman bankruptcy; the crashes are short-term, extreme events.
The profitability of momentum is highly variable and predictable from volatility. Daniel and
Moskowitz (2016) show that the probability of a momentum crash can be predicted: it is high when
market volatility is high and the market has recently been in a deep bear market. Crashes are
documented on US and international stocks; the drawdowns of trend-following advisers also often
come at abrupt reversals of trends.

## What would refute it

Momentum returns without negative skewness, or crashes that are as likely in calm markets as after
deep bear markets with high volatility. Past losers that rebound no more than past winners when the
market recovers sharply. Momentum profits that do not vary with the level of volatility. Momentum
returns that remain positive through market rebounds after crashes.

## References

- Barroso, P. & Santa-Clara, P. (2015). Momentum Has Its Moments. Journal of Financial Economics.
- Daniel, K. & Moskowitz, T. J. (2016). Momentum Crashes. Journal of Financial Economics.
- Ilmanen, A. (2011). Expected Returns: An Investor's Guide to Harvesting Market Rewards, discussion of the risks of momentum. Wiley.
- Gray, W. R. & Vogel, J. R. (2016). Quantitative Momentum: A Practitioner's Guide to Building a Momentum-Based Stock Selection System, ch. 5 (risk of momentum crashes, drawdown analysis). Wiley.
