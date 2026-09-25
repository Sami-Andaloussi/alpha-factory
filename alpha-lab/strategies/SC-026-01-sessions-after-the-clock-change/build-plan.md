# SC-026-01 — Build plan

The card is locked (`card: SC-026-01-sessions-after-the-clock-change`). One function,
`positions(market, sessions)`, in four steps, each commented in `strategy.py` by its number, with
three helpers: `scheduled_sessions`, the exchange's calendar, copied from SC-025-01's code since a
strategy imports nothing from the lab, `nth_sunday` and `clock_changes`.

1. **The calendar**: weekdays less the New York Stock Exchange's scheduled holidays by rule, from 45
   days before the market's first session to 62 days after its last, read from no price.
2. **The changes of the clocks**: for each year, by the United States' rule in force — from 2007 the
   second Sunday of March and the first Sunday of November, before it the first Sunday of April and
   the last Sunday of October. The sessions out are the `sessions` first scheduled sessions after
   each change's Sunday.
3. **Holding**: on each session of the market, whether the next scheduled session is not out.
4. **The targets**: while holding, the funds that trade, in equal parts; otherwise nothing. A target
   is set on the market's first session and on each session on which the target changes — holding
   changes, or a fund starts trading (XLRE in 2015, XLC in 2018) — NaN elsewhere, every fund named,
   so that the funds drift with prices while held.

Why in this order: steps 1 and 2 are the calendar and the dates the card states, step 3 turns them
into the sessions held, step 4 into targets. Nothing reads a price but the funds' tradability, and the
calendar reads no date of the market: cut at any session, the targets up to it are the same. Before
the run, by `python -m lab.report --try`, gate 1's timing and ten dates for the neighbour; and, apart
from the battery, the thirty-six sessions out in-sample listed with their weekdays.
