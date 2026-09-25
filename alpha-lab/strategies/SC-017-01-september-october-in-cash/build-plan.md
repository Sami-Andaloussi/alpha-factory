# SC-017-01 — Build plan

One function, `positions(market, first, months)`, in four steps, each commented in `strategy.py` by
its number, with two helpers: `scheduled_sessions`, the exchange's calendar, copied from
SC-008-01's code since a strategy imports nothing from the lab, and `months_out`.

1. **The calendar**: weekdays less the New York Stock Exchange's scheduled holidays, from pandas'
   holiday rules, as in SC-008-01. It reads no price and no date of the market; it runs from 45
   days before the market's first session to 62 days after its last, so that every session has a
   next scheduled session.
2. **The months out**: the `months` consecutive calendar months from the month named `first`,
   wrapping past December; `first` is an English month name.
3. **Holding**: on each session of the market, whether the first scheduled session after it falls
   in a month held; the portfolio then holds equities over the sessions of the months held.
4. **The targets**: while holding, the funds that trade, in equal parts; otherwise nothing. A target
   is set on the market's first session and on each session on which holding changes, NaN
   elsewhere, every fund named, so that the funds drift with prices while held.

Why in this order: steps 1 and 2 are the calendar and the months the card states, step 3 turns them
into the days the portfolio holds, step 4 into targets. Nothing reads a price, and the calendar
reads no date of the market: cut at any session, the rule's targets up to it are the same. Before
the run, the calendar is compared with the market's sessions from 2005 to 2025, and the month of the
next scheduled session with the month of the next market session.
