---
id: SC-001
title: Day-of-the-week effect (weekend effect)
family: seasonality and calendar effects
mechanism: [microstructure, behavioural, information, limits to arbitrage]
asset_classes: [stocks, equity indices, crypto]
horizon: [days]
data: [daily prices, market capitalisation, trading volumes, trades by investor type]
status: tested-inconclusive
---

## Mechanism

Returns differ systematically according to the day of the week. Historically, US equities earned abnormally low returns on Mondays and, in many samples, relatively high returns on Fridays. Variants follow the local structure of the trading week: in Japan, Tuesdays were negative while Saturday was still a half trading day. The effect is not a pure artefact of the civil calendar; it reflects the way market time is split between open and closed hours.

No single mechanism accounts for it. The literature sets a purely statistical explanation, the non-trading interval, against microstructural and behavioural explanations. Other work ties the effect to the composition of order flow, and the explanations the books discuss also turn on the timing of news releases, the processing of information over the weekend, institutional trading practices and the behaviour of individual investors: individual investors sell more on Mondays, after the weekend, while institutional activity is lower on Mondays; short sellers cover their positions on Fridays and reopen them on Mondays; market depth is lower; news accumulated over the weekend is digested with a delay; order-book dynamics play a part too. The books show that the effect was much stronger in equally weighted indices and in small capitalisations than in large stocks, which points to a microstructure and clientele origin. Arbitrage stays incomplete because the effect is small, varies over time and is costly to exploit after transaction costs.

The conditions under which it appears are markets dominated by retail investors, asymmetries of attention, inventory costs for market makers, and news accumulating during a market closure or an institutional pseudo-closure. The effect is closely related to sentiment, liquidity and funding constraints. It has also been re-examined in the cross-section: the returns of some anomaly spreads concentrate on Mondays or on Fridays depending on whether their speculative leg is long or short, which suggests an interaction with sentiment and limits to arbitrage.

In crypto markets, which trade around the clock, a "Monday effect" has its own literature. What it finds makes the mechanism there closer to a mix of attention, lower institutional participation outside the working week, and the segmentation between the civil calendar and a market open 24/7, than to a simple copy of the equity effect.

## Prediction

Monday returns are lower than those of the other weekdays, and Friday returns are often relatively high; the gap is larger in small capitalisations and equally weighted indices than in large capitalisations. The effect shapes the distribution of returns within the trading week.

Where and when it has been observed: first in equity indices, then in individual stocks, with large variation across countries, periods, firm sizes and market structures; in Japan on Tuesdays while Saturday was still a half trading day. Several books report that it weakened or disappeared in large capitalisations as institutional investors and options markets grew, but lasted longer in less liquid stocks, and the books note that it has often weakened or changed its dominant day. It has also been studied on S&P 500 and Russell 2000 index futures. In Bitcoin, some studies find positive Mondays in the early years, while other work mostly finds no return anomaly, together with lower trading activity at weekends.

## What would refute it

- Average returns that do not differ by weekday: Monday returns no lower than those of the other days and Friday returns no higher, in recent samples as in the classic historical ones.
- A Monday effect as large in large capitalisations and value-weighted indices as in small capitalisations and equally weighted indices, which would contradict the microstructure and clientele explanation.
- Weak Mondays that coincide with no excess selling by individual investors, no Friday short covering followed by Monday reshorting, and no lower market depth.
- A weak day that does not follow the local trading week, for example no weak Tuesday in Japan while Saturday was still a half trading day.
- An effect that fades as fast in less liquid stocks as in large capitalisations.
- In crypto markets, no difference in trading activity between weekdays and weekends, which would remove the attention and participation channel proposed there.

## References

- Cross (1973). The Behavior of Stock Prices on Fridays and Mondays.
- French (1980). Stock Returns and the Weekend Effect.
- Gibbons and Hess (1981).
- Lakonishok and Levi (1982).
- Keim and Stambaugh (1984).
- Kato (1990).
- Lakonishok and Maberly (1990). The Weekend Effect: Trading Patterns of Individual and Institutional Investors.
- Abraham and Ikenberry (1994).
- Kamara (1997).
- Wang, Li and Erickson (1997).
- Chen and Singal (2003).
- Birru (2018). Day of the Week and the Cross-Section of Returns.
- Aharon and Qadan (2019). Bitcoin and the Day-of-the-Week Effect.
- Kinateder and Papavassiliou (2021). Calendar Effects in Bitcoin Returns and Volatility.
- Mueller et al. (2024). Revisiting Seasonality in Cryptocurrencies.
- Jaffe and Westerfield (n.d.).
- Dimson (ed.) (1988). Stock Market Anomalies, part II, chapters 3 to 7, pp. 43-109.
- Singal (2003). Beyond the Random Walk: A Guide to Stock Market Anomalies and Low-Risk Investing, chapter 3, pp. 59-62.
- Ilmanen (2011). Expected Returns: An Investor's Guide to Harvesting Market Rewards, chapter 25.3, p. 583.
- Zacks (ed.) (2011). The Handbook of Equity Market Anomalies: Translating Market Inefficiencies into Effective Investment Strategies, chapter 9, pp. 232-237 of the chapter, that is pp. 251-256 of the book, especially pp. 251-255; pp. 254-256 for the results on S&P 500 and Russell 2000 futures.
- Ziemba (2012). Calendar Anomalies and Arbitrage, chapter 1.6, pp. 54-58; chapter 13, pp. 342-361; chapter 14, pp. 364-371.
