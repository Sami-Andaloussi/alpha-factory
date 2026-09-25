---
id: FP-024
title: Positive feedback trading, portfolio insurance and stop-loss cascades
family: flows and positioning
mechanism: [flows, behavioural, limits to arbitrage]
asset_classes: [stocks, equity indices, bonds, commodities, currencies, crypto]
horizon: [days, weeks, months]
data: [intraday prices, daily prices, trading volumes, fund flows, institutional holdings]
status: untouched
---

## Mechanism

Positive feedback trading is buying after prices rise and selling after they fall, outside any
fundamental consideration. Some investors do so not because they reassess fundamental value but
because their management or risk-control rules require it. Historically, portfolio insurance
involved dynamic selling after declines to maintain a protection profile. More broadly, stop-loss
orders, which add selling pressure when a price level is crossed on the way down; volatility
overlays; trend-following rules, including those of systematic trend followers such as commodity
trading advisers and quantitative funds, which enter in the direction of the move once their signals
(moving averages, breakouts) are triggered; discretionary or systematic cuts in risk; and, more
mechanically, liquidations triggered by margin calls, can turn an initial shock into additional
flows of the same sign. Other sources are explicit momentum traders and extrapolative expectations;
performance followers and imitators of flows; managers who align with what has worked so as not to
appear "behind"; and herding driven by the fear of missing out or the fear of losses, among retail
and institutional investors; more generally, the logic that "the move validates the move". The key
point is that past prices change future flows in the same direction: a feedback loop between past
returns and current demand amplifies moves instead of stabilising them. The mechanism does not
assume that these traders are right about fundamentals, only that their rules of behaviour amplify
the move in place.

Orders are endogenous: a fall produces new sales because it changes investors' internal constraints.
Even without high leverage, risk policies can impose a mechanical reduction of exposure. The
mechanism is not confined to the crash of 1987. Its condition is an identifiable
population that adjusts its exposure according to the price move itself. Shleifer argues that it
describes some bubbles and crashes better than simple under-reaction to information does.

De Long, Shleifer, Summers and Waldmann (1990) model such traders: when they buy recent winners,
they push prices still higher regardless of fundamentals, and as long as their optimistic or
pessimistic sentiment lasts, prices drift away from their fundamental anchor; this can lead to large
gaps between price and true value, creating long episodes of momentum as long as the sentiment
persists. An uninformed trader can set off an avalanche of purchases after an initial rise, and
prices can keep climbing without any new information. The strength of the phenomenon comes from the
fact that it can be anticipated, and even rational traders can be drawn to ride it in the short run:
arbitrageurs or "smart money" traders can buy ahead of the expected flow of the followers, which
amplifies the initial rise further and can feed bubbles in the short run, and then sell to them at
higher prices; the directional persistence can last until fundamentals re-anchor prices. The theory
assumes a sufficient volume of trend-following trading.

The mechanism links two stages of a trend. A piece of information or a shock first produces an
initial underreaction; traders who do not necessarily read fundamental information, but read the
price, then take over and prolong the trend. The momentum traders of Hong and Stein (1999) arrive
after the newswatchers, and in Barberis and Thaler's survey the positive-feedback traders turn the
initial inertia into a more visible continuation. Shleifer (2000), Ilmanen (2011), Ang (2014) and
Thaler (ed.) (2005) link it to bubbles, to destabilising rational speculation, to herding and to
short- to medium-term continuation. Its institutional form is the managed futures industry, and
Carver (2015) notes that a growing dominance of trend followers can reinforce trends, although it
can also make exits more synchronised. Stop-loss orders, squeezes, predatory trading and
deleveraging can all plug into this loop between price and flow.

The mechanism persists because part of the market follows rules or heuristics that bypass
fundamental valuation, and because the capacity of contrarian capital is limited. The rules are
often considered prudent beforehand and remain institutionally entrenched despite their
destabilising aggregate potential. Arbitrage against a move fed by crowding is dangerous: noise
traders add volatility and short-term risk, and De Long et al. show that under these conditions the
rational arbitrageur hesitates to step in, since persistent noise increases the risk of arbitrage;
the frictions include timing risk, the capital required and noise trader risk, prices being able to
move further away before converging; arbitrageurs may be right in the end and still be forced to
cut their positions before, because of margins, interim losses or redemptions; and the exact trigger
and final size of a cascade are uncertain, so arbitrageurs hesitate to stand against it too early.
This is why apparently obvious moves can last much longer than an efficient-market view allows. It
concerns liquid equity markets and any market where the flows of systematic or benchmarked
participants become price drivers in their own right.

## Prediction

Price declines can be followed by further selling from investors who follow protection, stop-loss,
trend or risk rules, or who face margin calls, and the added selling can deepen the decline into
cascades; rises can be followed by further buying. Trends can continue beyond what the information
justifies. In the model of De Long et al. (1990), the momentum strategy of the feedback traders does
earn additional profits and creates momentum; empirically, institutions such as mutual funds and
trend-following advisers buy recent winners more readily than they sell losers, and their positive
feedback trading contributes to momentum profits. Anticipatory buying ahead of the expected flow of
followers can amplify the initial rise, the anticipators then selling to the followers at higher
prices. The horizon is variable: the mechanism can operate over days (stop-loss triggers) to months
(flows of trend-following advisers). The theory suggests strong effects in volatile markets.

The same mechanism makes trends fragile: once enough feedback traders have bought, no marginal buyer
is left and the trend reverses violently. Momentum can thus turn into overreaction and set up style
crashes at turning points; it is a conditional engine of persistence, not an endless continuation.
It has been documented on stocks, bonds and commodities, and it is particularly visible on crypto
futures, where the share of highly leveraged retail traders is high. In equities and in crypto, it
concerns in particular phases of euphoria, breaks of support levels and technical cascades.

## What would refute it

- Price moves not followed by flows of the same sign from investors bound by protection, stop-loss,
  trend or margin rules; investor demand that does not respond to past returns, or institutions that
  buy past winners no more than they sell past losers.
- Declines that do not deepen more when the share of rule-following or leveraged investors is large
  than when it is small; effects no stronger in markets with a high share of leveraged retail
  traders.
- No continuation of prices beyond the information content of news, even where trend-following,
  leveraged or stop-loss-driven trading is heavy; sharp moves in bubbles and crashes fully accounted
  for by fundamental news, with no trace of a loop between price and flow.
- No anticipatory buying ahead of the expected flows of trend followers.
- Trends that do not end in sharper reversals when trend-following positions are crowded.

## References

- De Long, J. B., Shleifer, A., Summers, L. and Waldmann, R. (1990). Positive Feedback Investment Strategies and Destabilizing Rational Speculation. Journal of Finance.
- Gennotte, G. and Leland, H. (1990). Market Liquidity, Hedging, and Crashes. American Economic Review.
- Shiller, R. (1988). Portfolio Insurance and Other Investor Fashions as Factors in the 1987 Stock Market Crash. NBER Macroeconomics Annual.
- Shleifer, A. (2000). Inefficient Markets: An Introduction to Behavioral Finance. Oxford University Press. Chap. 6, pp. 154-157; chap. 6, "Positive Feedback Investment Strategies", PDF pp. 163-179.
- Harris, L. (2002). Trading and Exchanges: Market Microstructure for Practitioners. Oxford University Press. Chap. 8, pp. 195-196, for the role of sentiment-driven technical traders.
- Pedersen, L. H. (2015). Efficiently Inefficient: How Smart Money Invests and Market Prices Are Determined. Princeton University Press. Chap. 5, pp. 83-84, for mechanical liquidation and predatory trading.
- Grinblatt, M., Titman, S. & Wermers, R. (1995). Momentum Investment Strategies, Portfolio Performance, and Herding: A Study of Mutual Fund Behavior. American Economic Review.
- Hong, H. & Stein, J. C. (1999). A Unified Theory of Underreaction, Momentum Trading, and Overreaction in Asset Markets. Journal of Finance.
- Lo, A. W. & MacKinlay, A. C. (1999). A Non-Random Walk Down Wall Street. Princeton University Press. Discussion of feedback trading.
- Thaler, R. H. (ed.) (2005). Advances in Behavioral Finance, Volume II. Princeton University Press. Chapter 1, "A Survey of Behavioral Finance" (Barberis and Thaler), pp. 69-70; chapter 12, p. 434, on De Long et al. (1990); chapter 14, "A Unified Theory of Underreaction, Momentum Trading, and Overreaction in Asset Markets", pp. 541-544; discussions of positive feedback traders, PDF pp. 34, 69-70, 526 and 535-538.
- Ilmanen, A. (2011). Expected Returns: An Investor's Guide to Harvesting Market Rewards. Wiley. Discussion of positive-feedback trading and overreaction, pp. 150 and 157-158; feedback effects and the fashionability of assets, PDF pp. 46, 207-209 and 519-526.
- Ang, A. (2014). Asset Management: A Systematic Approach to Factor Investing. Oxford University Press. Momentum as a positive-feedback strategy, and institutional presentations, PDF pp. 249-252 and 528-529.
- Greyserman, A. & Kaminski, K. (2014). Trend Following with Managed Futures: The Search for Crisis Alpha. Wiley. Preface, p. xii; chapter 2, "Review of the Managed Futures Industry", pp. 34-36.
- Carver, R. (2015). Systematic Trading: A Unique New Method for Designing Trading and Investing Systems. Harriman House. "Why Certain Rules Are Profitable", pp. 46-54.
