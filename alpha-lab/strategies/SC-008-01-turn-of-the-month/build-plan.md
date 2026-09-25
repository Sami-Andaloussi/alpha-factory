# SC-008-01 — Build plan

One function, `positions(market, start, end)`, in four steps, each commented in `strategy.py` by its
number, with two helpers: `scheduled_sessions`, the exchange's calendar, and `in_window`.

1. **The calendar**: weekdays less the New York Stock Exchange's scheduled holidays, from pandas'
   holiday rules — New Year's Day (Sunday to Monday, not observed from a Saturday), Martin Luther
   King Jr. Day, Washington's Birthday, Good Friday, Memorial Day, Juneteenth from 2022, Independence
   Day, Labor Day, Thanksgiving, Christmas (the fixed dates of Juneteenth, Independence Day and
   Christmas to the nearest weekday). It reads no price and no date of the market; it runs from 45
   days before the market's first session to 62 days after its last, so that every session has a
   next scheduled session.
2. **The window**: a scheduled session is in it when it is among the last `-start` sessions of its
   month or the first `end` sessions of its month.
3. **Holding**: on each session of the market, whether the first scheduled session after it is in
   the window; the portfolio then holds equities over the window's sessions.
4. **The targets**: while holding, the funds that trade, in equal parts; otherwise nothing. A target
   is set on the market's first session and on each session on which holding changes, NaN elsewhere,
   every fund named, so that the funds drift with prices inside the window.

Why in this order: steps 1 and 2 are the calendar the card states, step 3 turns it into the days
the portfolio holds, step 4 into targets. Nothing reads a price, and the calendar reads no date of
the market: cut at any session, the rule's targets up to it are the same. Before the run, the
calendar is compared with the market's sessions from 2005 to 2025: every market session should be a
scheduled session, and the scheduled sessions the market lacks should be the five unscheduled
closures.
