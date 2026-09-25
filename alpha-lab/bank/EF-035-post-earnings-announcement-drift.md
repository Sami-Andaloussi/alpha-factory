---
id: EF-035
title: Post-earnings announcement drift (PEAD)
family: earnings and fundamentals
mechanism: [information, behavioural, limits to arbitrage]
asset_classes: [stocks, equity indices, sectors, bonds, commodities, currencies]
horizon: [days, weeks, months]
data: [earnings announcement dates, reported earnings, analyst forecasts, daily prices, trading volumes, market capitalisation, commodity inventory reports]
status: untouched
---

## Mechanism

After an earnings surprise, the price keeps moving in the direction of the surprise: upwards after
good surprises, downwards after bad ones. After an announcement better than expected, the price does
not make its whole adjustment on the day of the announcement but, on average, keeps drifting in the
same direction for several weeks or months; the symmetric anomaly exists after bad surprises. The
main mechanism in the books is underreaction to material public information: the market does not
deny the information but incorporates it too slowly, and the drift is consistent with a gradual
incorporation of the implications of current earnings for future earnings. The drift is thus a form
of slow diffusion of fundamental information, and the event-driven form of momentum.

The standard mechanism is underreaction to accounting information. Investors do not instantly update
their expectations of future earnings, because of limited attention, because the persistence of the
information is hard to interpret, or because arbitraging against that slowness is risky or costly.
The economic mechanism the library proposes is that the market does not properly recognise the
autocorrelation of certain earnings changes, or wrongly believes that earnings revert to the mean
faster than they actually do. Bernard and Thomas (1989, 1990) show that the drift is consistent with
an underreaction to a seasonal random-walk model of earnings: investors seem not to anticipate the
seasonal correlation of earnings correctly, so they are surprised by good announcements, which
creates a drift. Inference from accounting data is imperfect, and the books tie the drift to
investors' underreaction to these complex data, which they sometimes mistake for temporary noise.

The causes put forward are cognitive and structural. Theories suggest that the drift reflects the
time needed to assimilate the information: investors find it hard to interpret the news at once,
need the validation of the market consensus and seek to confirm their reading, and are reluctant to
revise their beliefs quickly; they are sometimes heterogeneous, some updating fast and others
slowly, which spreads the adjustment over time. Limited attention when many announcements arrive
together is also mentioned among the causes, and the structural reasons put forward are that
announcements often come after the market close or in periods of low attention, that small
capitalisations and firms with little analyst coverage incorporate the information more slowly, and
that institutional investors reposition progressively over the weeks after the announcement. The
drift is also linked to analysts: part of it resolves through subsequent forecast revisions and
later announcements. The mechanism can also be prolonged by the sequential diffusion of analysts'
revisions and of model updates, and by organisational constraints that keep fundamental investors
from reallocating all at the same time. During this phase some traders, "chasers", buy the past
winners and prolong the rise; once the market has fully understood the news, a gradual return
towards the mean follows. As long as the interpretation of announcements remains complex and
investors' reaction incomplete, a residual drift can survive.

The drift shows that continuation need not be purely "technical": it can arise from an institutional
calendar and a real process of information handling. It also shows why arbitrage does not always
erase visible anomalies: even a well-known effect can survive when it is fragmented, repetitive,
event-driven, sometimes costly to capture and exposed to execution risk or short-selling risk. The
frictions are similar to those of momentum in general: transaction costs, market risk, and
constraints on short selling stocks with negative announcements. The drift is not fully arbitraged
away because accounting information is costly to process, the size of the surprise is uncertain, and
building positions across a large universe of stocks consumes capital and research capacity; for
small capitalisations, the lack of liquidity prevents full exploitation. The literature discusses
whether the drift is a delayed response or a risk premium.

The drift is tied to earnings momentum but differs from it: the drift is the delayed reaction to one
announcement, earnings momentum the persistence of series of surprises over several quarters. The
drift makes momentum self-sustaining over the short horizon after the announcement (a few days to
three to six months), and is a specific manifestation of an underlying momentum linked to
fundamental information. The books also link earnings momentum and price momentum: a large part of
price momentum may be a derived expression of the slow incorporation of earnings surprises, although
the literature cited does not agree that earnings momentum fully subsumes the rest. In accounting
form the drift concerns equities, and it has no direct equivalent in assets without an earnings
calendar such as crypto-assets. By analogy, in futures, the channel of underreaction to fundamental
news is a generic source of trend, and any repeated public release rich in information can produce a
drift if the market absorbs it gradually: aggregated earnings surprises of the constituents of
sector index futures, single-stock futures, and surprises in inventory or production reports for
commodity futures.

## Prediction

Stocks with strong positive earnings surprises continue to outperform after the announcement, and
stocks with strong negative surprises continue to underperform: the drift has the sign of the
surprise. Its horizon runs from a few days to several months after the announcement (a few days to
three to six months), with a natural horizon of one to six months. Stocks in the top quartile of
standardised unexpected earnings (SUE) outperform those in the bottom quartile by 7% to 10% over the
six months after the announcement. The drift has been observed on equities for decades, and studied
mainly on US equity markets. Chan, Jegadeesh and Lakonishok (1996) show that the drift and price
momentum capture different information and that their combination predicts returns better than
either alone. The drift is generally stronger where attention and liquidity are low: for small
capitalisations, firms with little coverage, and announcements made when attention is low, such as
days with many simultaneous announcements. It has often been found weaker in more recent periods,
but it has not cleanly disappeared across the literature, and competition among arbitrageurs has
probably reduced part of the raw premium on the most followed large capitalisations.

## What would refute it

- No drift after earnings surprises: prices that complete their adjustment on the announcement day,
  with no abnormal return in the direction of the surprise over the following weeks and months; or a
  drift that bears no relation to the sign and the size of the surprise.
- Earnings changes that show no autocorrelation, so that the market's belief in fast mean reversion
  is correct; earnings seasonality that investors anticipate correctly, so that seasonal surprises
  carry no subsequent drift.
- A drift that disappears once risk is properly measured, consistent with a risk premium rather than
  a delayed response; a drift that has disappeared entirely in recent periods.
- A drift no stronger where attention and liquidity are low, among small or little-covered firms, or
  on days of many simultaneous announcements, than among the most followed and most liquid stocks.
- A drift no part of which resolves through subsequent forecast revisions and later announcements.

## References

- Bernard, V. L., Thomas, J. K. (1989). Post-Earnings-Announcement Drift: Delayed Price Response or Risk Premium? Journal of Accounting Research.
- Mendenhall, R. R. (2004). Arbitrage Risk and Post-Earnings-Announcement Drift. Journal of Business.
- Fink, J. (2021). A Review of the Post-Earnings-Announcement Drift. Journal of Behavioral and Experimental Finance.
- Shleifer, A. (2000). Inefficient Markets: An Introduction to Behavioral Finance. Oxford University Press. Chapter 5, "A Model of Investor Sentiment", pp. 115-123, pp. 124-126 and p. 143.
- Bernard, V. L. (1992). Stock Price Reactions to Earnings Announcements: A Summary of Recent Anomalous Evidence and Possible Explanations. In R. H. Thaler (ed.), Advances in Behavioral Finance. Russell Sage Foundation.
- Bernard, V. L., Thomas, J. K. (1990). Evidence That Stock Prices Do Not Fully Reflect the Implications of Current Earnings for Future Earnings. Journal of Accounting and Economics.
- Ball, R., Brown, P. (1968). An Empirical Evaluation of Accounting Income Numbers. Journal of Accounting Research.
- Chan, L. K. C., Jegadeesh, N., Lakonishok, J. (1996). Momentum Strategies. Journal of Finance.
- Hirshleifer, D., Lim, S. S., Teoh, S. H. (2009). Driven to Distraction: Extraneous Events and Underreaction to Earnings News. Journal of Finance.
- Correia, M., Barbosa, A. (2019). Can Post-Earnings Announcement Drift and Momentum Explain Reversal? MPRA Paper.
- Thaler, R. H. (ed.) (2005). Advances in Behavioral Finance, Volume II. Princeton University Press. Chapter 1, "A Survey of Behavioral Finance", pp. 64-70; chapter 10, section "Earnings Momentum", pp. 378-385; chapter 10, "Momentum", pp. 405-411.
- Ilmanen, A. (2011). Expected Returns: An Investor's Guide to Harvesting Market Rewards. Wiley. Chapter 6, "Behavioral Finance", pp. 156-158.
- Bali, T. G., Engle, R. F., Murray, S. (2016). Empirical Asset Pricing: The Cross Section of Stock Returns. Wiley. Chapter 18, "Other Stock Return Predictors", section on PEAD and attention, pp. 480-481.
- Gray, W. R., Vogel, J. R. (2016). Quantitative Momentum: A Practitioner's Guide to Building a Momentum-Based Stock Selection System. Wiley. Section "How Is Momentum Related to Fundamentals?", pp. 156-158.
- Novy-Marx, R. (2015). Fundamentally, Momentum Is Fundamental Momentum. NBER Working Paper No. 20984.
