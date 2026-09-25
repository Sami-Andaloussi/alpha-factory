---
id: FP-014
title: ETF flows and the creation-redemption mechanism
family: flows and positioning
mechanism: [flows, structural, microstructure]
asset_classes: [stocks, equity indices, crypto]
horizon: [intraday, days, weeks]
data: [ETF creations and redemptions, ETF holdings, ETF premiums to NAV, daily prices, trading volumes]
status: untouched
---

## Mechanism

Exchange-traded funds pass the flows of end investors on to the underlying market through the
creation and redemption of shares. Investors trade ETF shares on the secondary market, but when net
demand persists, authorised participants create shares by delivering the underlying basket, or
redeem shares and receive the basket. Flows into an ETF can thus reach the cash market of its
constituents, either directly through the primary market or indirectly through arbitrage, market
making and hedging adjustments. The wrapper links a change in the demand for "exposure" to a flow of
underlying securities, and aggregate demand shocks can be transmitted to individual securities,
particularly when the ETF is large or the underlying is less liquid. ETFs are therefore not merely
neutral passive vehicles: they are channels through which liquidity shocks and flows are transmitted
between the aggregate product and its constituents. When an ETF is traded intensely, the adjustment
of the basket can inject demand or supply that bears no relation to the fundamental information
specific to each stock, and the constituents become partly "components of a package", no longer only
assets valued in isolation.

The key actors are ETF investors, authorised participants, market makers and cross-market
arbitrageurs. The strength of the channel depends on the liquidity of the ETF itself, on the ability
of authorised participants to absorb the imbalance for a while, on the liquidity of the underlying
basket, and on the persistence of the flows. ETFs can also serve as an instrument of liquidity
transformation: trading concentrates at the level of the wrapper, while part of the pressure is
eventually passed on to the cash market. Not every ETF flow forces an equivalent trade in the
underlying in real time; part of the adjustment can stay with the intermediaries. When flows
persist, exceed the intermediaries' inventory capacity or concentrate in periods of stress, the
channel to the underlying becomes economically significant. The mechanism is related to indexation,
but it is more microstructural: what matters is not only passive ownership but the mechanics of the
basket and the role of the intermediaries. A stock that is heavily held through ETFs can therefore
behave differently from an economically similar stock that is little integrated into these vehicles.
By analogy, the mechanism may carry over to other basket structures, tokenised or synthetic.

The channel is not fully arbitraged because ETF-cash arbitrage consumes capital, depends on
operational frictions, and deteriorates in stress: the cost of assembling and disassembling the
basket, operational delays, inventory risk, liquidity imbalances between the ETF and its
constituents, and the capital constraints of intermediaries. It relies on accurate pricing of the
underlying securities, on the voluntary participation of authorised participants, on the true
liquidity of the basket, and on market transparency working properly. In stress, if the quotes of
the constituents become unreliable, the link between the ETF price and its net asset value can
loosen temporarily and ETF prices can be dominated by flows.

## Prediction

Persistent net flows into or out of an ETF are followed by creations or redemptions; the flows can
reach the underlying basket and move the prices of its constituents, particularly for large ETFs and
less liquid underlyings. Stocks with a high ETF ownership show more non-fundamental volatility, more
comovement with the other constituents, more pronounced return autocorrelation, and a stronger
transmission of liquidity stress from the ETF layer than economically similar stocks with little ETF
ownership. In less liquid segments the channel can amplify comovement, volatility or price
dislocations. The literature cited by Madhavan discusses several possible effects: higher
correlations, higher comovement, a possible deterioration of price quality in some small
capitalisations, but also the addition of a further layer of liquidity. The effect is recurrent,
with more visible episodes during extreme flows or volatility shocks; it has been observed mainly in
equities, and it is particularly strong in less liquid stocks, in thematic segments, in small
capitalisations, and in periods of stress when the ETF becomes the dominant trading layer. In
stress, if the constituents' quotes become unreliable, the link between ETF prices and net asset
values can loosen temporarily.

## What would refute it

- ETF flows, creations, redemptions and ETF arbitrage trades followed by no trading, and no price
  change, in the underlying constituents once the news about each stock's fundamentals is taken into
  account, even when the flows are persistent and large relative to the basket's liquidity.
- Securities with high ETF ownership showing no more volatility, comovement or return
  autocorrelation than economically similar securities with low ETF ownership.
- Liquidity shocks in an ETF that do not spread to the stocks it holds, including in periods of
  stress when the ETF is the dominant trading layer.
- An effect no stronger for large ETFs, illiquid underlyings, thematic segments and small
  capitalisations than for small ETFs on liquid baskets and large, liquid stocks.
- ETF prices staying tied to net asset value through stress episodes in which the constituents'
  quotes become unreliable.

## References

- Ben-David, I., Franzoni, F. and Moussawi, R. (2018). Do ETFs Increase Volatility? Journal of Finance; earlier version NBER Working Paper No. 20071 (2014).
- Ben-David, Itzhak, Francesco Franzoni, Rabih Moussawi (2017). Exchange Traded Funds (ETFs). NBER Working Paper No. 22829.
- Israeli, D., Lee, C. M. C. and Sridharan, S. A. (2017; working-paper version 2015). Is There a Dark Side to Exchange Traded Funds? An Information Perspective. Review of Accounting Studies.
- Todorov, K. (2021). Passive Funds Actively Affect Prices: Evidence from the Largest ETFs and Mutual Funds. BIS Working Papers.
- Madhavan, A. (2016). Exchange-Traded Funds and the New Dynamics of Investing. Oxford University Press. Chap. 2, pp. 19-21; chap. 15, pp. 191-196; chap. 17, pp. 212-216; chap. 18, pp. 231-233.
- Sullivan, R. N. and Xiong, J. X. (2012). How Index Trading Increases Market Vulnerability. Financial Analysts Journal.
- Da, Z. and Shive, S. (2013). Exchange Traded Funds and Asset Return Correlations.
- Madhavan, A. and Morillo, D. (2016) (title not specified).
