# SC-008-01 — The turn of the month: reasoning

## Why this theory now

SC-008 holds that equity returns concentrate in a few sessions around the turn of the month, from
the last trading day of a month to the first few of the next, and are low or negative on the other
days. The explanations are several and synchronised rather than one: salaries, pension
contributions, interest and bill payments fall at the turn of the month and part of that cash is put
into equities; institutions buy and rebalance on the same days; and news tends to be released
favourably at the start of the month and unfavourably late in it. The flows persist because the
payment calendars behind them are institutional and do not move with prices.

**The sources.** The lab read them in the library's books.

- Ariel (1987), on all NYSE stocks from 1963 to 1981, finds the whole of the period's gain in the
  first half of the trading month, the last half flat or negative, and the five sessions from -1 to
  +4 carrying a large part of it (as reported by Ziemba, *Calendar Anomalies and Arbitrage*, 2012,
  §1.10, and by the Zacks *Handbook of Equity Market Anomalies*, 2011, chapter 9).
- Lakonishok and Smidt (1988), on the price of the Dow Jones Industrials from 1897 to 1986, find a
  rise of 0.475% over the four sessions from -1 to +3 each month, against 0.061% for an average
  four-session span and 0.349% for a whole month: outside those four sessions the index fell (same
  sources).
- Hensel, Sick and Ziemba (1994), on the S&P 500 and the Value Line index from 1982 to 1992, find
  about two thirds of the month's gain on sessions -1 to +4 and the rest on +5 to +9, with partial
  anticipation in the futures market on sessions -4 to -2.
- McConnell and Xu (2008), on the US market from 1926 to 2005, find all of the equity market's
  excess return earned over the four sessions from the last of a month to the third of the next, and
  the other sessions' average slightly negative; the pattern is not confined to year ends, quarter
  ends or the United States (as reported by Ilmanen, *Expected Returns*, 2011, §25.3). Ilmanen adds
  that returns tend to be higher over the week before the turn as well as the week after, that the
  effect has shifted earlier, that mutual fund inflows do not show the regularity the flow
  explanation needs, and that Grimbacher, Swinkels and Van Vliet find the effect in every decade
  from the 1960s to the 2000s.
- Ziemba's update on S&P 500 and Russell 2000 futures from 1993 to 2010 finds the effect still
  present with a little anticipation: over the span from session -5 to +2, every session's average
  is positive except, for the S&P 500, -1 and -2, which show small losses (§1.10 and the tables of
  its appendix).

The effect is also reported in many other markets, with the window shifted where local salary dates
differ — in Japan, sessions -5 to +2 — and, recently, in some cryptocurrencies.

The lab has run no calendar rule yet; calendar effects are tested as theories like any other.

The bank's neighbours: **SC-011**, announcement clustering, which would explain part of this effect
by the dates of macroeconomic releases and which the lab records as not testable; **SC-017** and
**SC-018**, the month of the year and the Halloween effect, the other calendar effects of the bank.

## From the claim to a signal

- **The window, base**: the four sessions from -1 to +3, Lakonishok and Smidt's and McConnell and
  Xu's, the window with the longest record. **Variant**: -5 to +2, the span over which Ziemba's
  update reports US index futures from 1993 to 2010 — not a window he estimates, but the span he
  reads, earlier than the base, as Ilmanen finds the effect has shifted and the bank predicts;
  Hensel, Sick and Ziemba and Ziemba's update find the futures anticipating it, a related but
  different thing, the futures moving ahead of the cash index. The update's years overlap the lab's
  first six in-sample years, and it was read on futures; the card applies it to exchange-traded
  funds. Its window is taken from the source, not from the lab's data.
- **The calendar**: to earn the return of session -1 a portfolio must hold equities at the close of
  session -2, so the rule must know, on session -2, that the month ends two sessions later. The
  runbook asks a periodic rule to set its targets on the first session of a period, not the last,
  because knowing that a session is the last of its month means knowing the next session's date,
  which the lab's check of look-ahead counts as reading the future when the rule reads it from the
  data. This rule reads it from no data: it counts sessions on the New York Stock Exchange's
  calendar of scheduled sessions, weekdays less the exchange's holidays, derived from their rules,
  which are published years ahead and which any investor knows on session -2. Gate 1 cannot tell a
  calendar built from rules from one copied from the data's own dates, so the code derives it from
  the rules alone and a check before the run compares it with the market's sessions: the rules
  should give every session of the market and five scheduled sessions the market does not have — the
  unscheduled closures of 2 January 2007, 29 and 30 October 2012 and 5 December 2018 in-sample, and
  9 January 2025 in the holdout, each announced a few days or a day ahead. The rule counts them as
  the calendar does; around them it holds equities over the sessions the calendar places in the
  window, not exactly the market's: in October 2012 it misses the month's real last session, and in
  December 2018 it holds one session more.
- **The funds**: the five equity markets the lab holds — US large caps, US growth, US small caps,
  developed markets outside North America and emerging markets — in equal parts in the window. The
  sources' evidence is on US indices, large and small, and the effect is reported worldwide; the
  foreign funds trade in New York at the US close, so that their prices carry the US turn of the
  month over their own markets' closes. Their local windows may differ, a risk named below.
- **Out of the window**, nothing: cash at the bill's rate, the portfolio's excess return zero. The
  claim is that the other sessions earn little or less; holding cash there is its trade.
- **Targets**: set only on the sessions on which the state changes — on session -2 to enter, on the
  window's last session to leave — so that the portfolio drifts with prices inside the window. The
  data's first session, 3 January 2005, is session +1 of January, and the rule holds from it.

No count of the signal was made before the card: it is a calendar, whose pace is known — one entry
and one exit a month, twelve round trips a year.

Two variants, not three.

## What the battery judges, and what to expect

**The size predicted.** The benchmark holds the five funds always. A rule in equities over about a
fifth of the sessions has a beta of about a fifth; its alpha is the premium it earns in the window
less a fifth of the whole premium. With an equity premium of about 6% a year over the bill, an
assumption, not a source's figure: if the window carried all of it, as McConnell and Xu find to
2005, the alpha would be about (1 − 0.19) × 6% ≈ 4.9% a year before costs; if it carried about half,
about 1.9%. The card takes that range, from all to about half: the effect has held in every decade
to the 2000s, Ilmanen finds the effect shifted earlier, which a fixed window may partly miss, and
the lab's years are those of exchange-traded funds that make it cheap to trade. Costs are about 1.2%
a year: twelve round trips of the whole portfolio at 5 basis points a side. After costs, about 0.7
to 3.7% a year. The rule's bets, hedged of the benchmark, should move by about the benchmark's
volatility times √(0.19 × 0.81), some 7% a year: an appraisal ratio of about 0.1 to 0.5.

**The clause.** The theory is judged on the effect before costs, as the bank's first refutation
reads it: the mean daily excess return of the five funds over the window's sessions less that over
the other sessions. Over the base's four window sessions a month for about 18 years, some 860 of
them, and some 3,650 others, at a daily volatility of about 1.2%, the difference is measured to
about ±0.045% a day; if the window carried all of a 6% premium, its sessions would average about
0.12% a day more than the others, some two and a half standard errors. For the variant's seven
sessions a month, the full premium would make the difference about 0.07% a day. The theory is
refuted in this form if that difference is zero or less and the base beats half of its placebos or
fewer. The placebos shift the rule's own weights in time by a year or more, so that the window lands
mostly on other days of the month — about a fifth of a shifted window's sessions still fall on a
turn of the month — keeping its exposure, its pace and its costs: a rule whose window earns no more
than other days beats about half of them, whatever the costs. Any other result short of the gates is
not proven.

**The test's power.** A synthetic simulation made for the card's audit — daily returns drawn at
random, not the lab's — gives the clause's rates. With no effect left, it refutes about 47% of the
time: a vanished effect is found no more than half the time, since the difference and the placebos
then fall either side of their centre by chance. At the prediction's low end, about half of the
premium in the window, it refutes about 15 to 20% of the time, a false refutation of a real effect;
at 60% of the premium, about 7%; at the full effect, almost never. The clause can refute a vanished
effect about one time in two, and cannot tell a weak surviving effect from none.

**What the gates can pass.** In the same simulation, gate 2 at twice the costs passes about 15 to
20% of the time at the low end and about 73% at the full effect; gate 4 needs an appraisal ratio of
about 0.7 over some twenty effective trials, above the prediction's top of 0.5, so that even the
sources' full effect passes it only about one time in eight. "Not proven" is the expected verdict
even if the theory holds; a refutation or a clear difference is what the card can show.

**Risks named before the run.**

- **Costs.** About 1.2% a year at the lab's costs, 2.4% at twice them: gate 2's check at twice the
  costs may fail a rule whose gross edge is real.
- **A day's delay.** Gate 6 delays the rule by a session; the base then holds from +1 to +4, losing
  session -1, which Lakonishok and Smidt and McConnell and Xu find among the best, and gaining +4:
  it must keep 70% of the Sharpe ratio.
- **One fund's share.** The five funds form one of the lab's clusters, so gate 6 leaves no cluster
  out, but no fund may carry more than 30% of the profit: if EFA and EEM add little, SPY, QQQ and
  IWM carry about a third each and the gate fails.
- **The foreign funds.** EFA and EEM hold markets whose salary dates, and local windows, differ from
  the US's; their New York prices blend the two.
- **Decay.** Ziemba's update finds sessions -1 and -2 with small losses on S&P 500 futures from 1993
  to 2010: the base's window may have lost its first session.
- **Crises.** A handful of turns of the month in 2008 and 2020 can decide an 18-year average of
  about 216 windows.
- **The neighbours.** The start's neighbour, -2, only widens the window; a later start is tested
  only by the delay.

## Choices, and the options rejected

- **Ariel's and Hensel, Sick and Ziemba's -1 to +4**: one session more than the base, much the same
  test; the variant tests the earlier shift the bank predicts instead.
- **Counting the data's own sessions**: it would read the future, as above.
- **Holding the sector funds, or SPY alone**: SPY alone is one asset, which the runbook refuses; the
  sectors are SPY's parts, and the sources' evidence is on broad indices.
- **A short position out of the window**: the lab is long only, and the claim is that the other
  sessions earn little, not that they lose.
- **Bitcoin**: its reported effect is recent and rests on a few years, and it trades on weekends,
  which the exchange's calendar does not place.

## Implementation

Long only, five equity funds, each with a European (UCITS) fund that tracks it, or cash, twelve
round trips a year on a calendar known in advance, with the orders filled at the close of the
session on which they are set; gate 6 adds a day's delay. European exchanges keep other holidays, so
that a European implementation would place some turns of the month a session apart.
