# SC-028-01 — The sunshine effect: reasoning, not testable

## The theory, and the form its sources give it

SC-028 holds that average stock returns differ with the amount of sunshine, through its effect on
collective mood and the appetite for risk, more strongly far from the equator. Its refutations: no
difference in returns between sunny and overcast days; an effect no stronger far from the equator
than near it; a pattern found only in the samples in which it was first found.

**Its sources, as the lab read them in the library's books.** Saunders (1993) and Hirshleifer and
Shumway (2003) are not in the library; what it holds of them is second-hand, as these books report
them.

- **Hirshleifer and Shumway (2003)**, following Saunders (1993), as Dzhabarov and Ziemba report them
  in the Zacks *Handbook of Equity Market Anomalies* (2011, chapter 9, "Weather: Sun, Rain, Snow,
  Moon, and the Stars") and in Ziemba's *Calendar Anomalies and Arbitrage* (2012, §1.12.1): the
  morning sunshine at a country's leading stock exchange against that day's index return at 26
  exchanges from 1982 to 1997; sunshine "strongly positively correlated with daily stock returns",
  and, once it is controlled for, rain and snow unrelated to returns. The same pages cite Roll
  (1992) on weather as a "genuinely exogenous" and "unambiguously observable" variable, and Kramer
  and Runde's study, titled as an exercise in data mining or yet another anomaly. Tulchinsky and
  others (*Finding Alphas*, 2020) report the same finding, morning sunshine predicting the index's
  return that day.
- **Keef and Roush (2007)**, in the same pages: on 26 exchanges, the effect "monotone stronger the
  further one is from the equator and the per capita GDP", none at the equator and large on the
  northern exchanges.
- **Singal** (*Beyond the Random Walk*, 2003, "The Influence of Weather on Prices") reports prices
  rising on sunny days in New York and other centres, judges it "probably a bit early to term it an
  anomaly", with differences too small to trade profitably, and cites Goetzmann and Zhu (2002) and
  Pardo and Valor (2003), which ask where the weather effect is; earlier in the book, the weather in
  New York is his example of data mining.
- **Ilmanen** (*Expected Returns*, 2011, §6.2.2, among the moods): US stocks fare better on days
  with better New York weather, among patterns most of which are weak, likely partly data-mined, and
  too small to exploit after costs. The bank's §25.2–25.3 and the Zacks page it gives point
  elsewhere; the weather is in the places named here.

The claim is about the day's weather at the exchange: a sunny morning against an overcast one.

## Why the lab cannot test it

Every refutation the bank names reads the weather: sunny days against overcast ones, at exchanges
nearer or farther from the equator. The lab's data holds no weather: the snapshot and its addition
hold daily prices of twenty-two funds and bitcoin, the bill rate and two exchange rates of the Swiss
franc, and its code fetches and checks only the universe's tickers and rates (`lab.data extend` and
`check`). The universe's list was fixed before the first card (the lab's framing, §5); a series of
New York's cloud cover or sunshine would be a new kind of data, and dates or values copied into a
card by hand would be data with no hash, which the rule of a frozen snapshot exists to prevent
(SC-011-01).

**What was considered, and why it does not rescue the test:**

- **The season's sunshine, read from the calendar**: the library gives it no sign of its own. The
  one remark it holds, Dzhabarov and Ziemba's, is that Sell in May means "being out of the stock
  market in the sunniest time of the year": a calendar form of the sunshine claim would be
  SC-018-01's rule reversed, whose in-sample result the lab has published (the winter half +0.030% a
  day above the summer half, t 0.74), on the other side; SC-025-01 reported the half year from
  equinox to equinox and the winter against the spring and summer. And it is not the sources' claim,
  which reads the day's weather.
- **The latitude**, Keef and Roush's gradient, read on EFA's markets against the US funds: it needs
  the weather at each exchange first, and EFA's markets, from Europe to Japan and Australia, are
  priced at New York's close; SC-025-01 reported that measure for its own claim, −0.001% a day
  (0.025%).
- **Bitcoin**, traded at every hour and in no one place: the claim ties the mood to the weather at
  the exchange where prices are made, which a coin traded worldwide has not.

What would make it testable: the daily weather at the exchanges whose prices the lab holds — New
York's cloud cover or sunshine each morning from 2005, and the same for EFA's and EEM's markets for
the latitude — frozen as a new part of the snapshot, a decision for the lab's framing, not for a
card.

## Status

SC-028 is recorded `not-testable`: its claim and refutations read the day's weather at the
exchanges, which the lab's data does not hold; a calendar form has no sign in the library beyond
Sell in May's, which SC-018-01 read; the latitude needs the weather too. No card is drawn, and no
trial is spent.
