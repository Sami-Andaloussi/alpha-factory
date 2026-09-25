# SC-025-01 — Build plan

The card is locked (`card: SC-025-01-equinox-to-solstice`). One function, `positions(market, days)`,
in four steps, each commented in `strategy.py` by its number, with two helpers: `scheduled_sessions`,
the exchange's calendar, copied from SC-017-01's code since a strategy imports nothing from the lab,
and `in_window`.

1. **The calendar**: weekdays less the New York Stock Exchange's scheduled holidays by rule, from 45
   days before the market's first session to 62 days after its last, read from no price, as in
   SC-017-01.
2. **The window**: a date is in it when it falls on 22 September of its own year or of the year
   before, or on one of the `days` − 1 days after it — for the base, 22 September to 20 December.
3. **Holding**: on each session of the market, whether the next scheduled session's date is outside
   the window; the portfolio then holds the funds over the sessions outside it and the bill's rate
   over the sessions in it.
4. **The targets**: while holding, the funds that trade, in equal parts; otherwise nothing. A target
   is set on the market's first session and on each session on which holding changes, NaN elsewhere,
   every fund named, so that the funds drift with prices while held.

Why in this order: steps 1 and 2 are the calendar and the window the card states, step 3 turns them
into the days the portfolio holds, step 4 into targets. Nothing reads a price, and the calendar reads
no date of the market: cut at any session, the rule's targets up to it are the same. Before the run,
by `python -m lab.report --try`, gate 1's timing for the base and ten dates for a neighbour; and,
apart from the battery, the window's first and last sessions in each year from 2005 to 2025, and the
count of sessions in the window.
