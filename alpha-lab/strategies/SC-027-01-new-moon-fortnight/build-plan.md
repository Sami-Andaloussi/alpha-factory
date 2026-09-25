# SC-027-01 — Build plan

The card is locked (`card: SC-027-01-new-moon-fortnight`). One function, `positions(market, days)`,
in four steps, each commented in `strategy.py` by its number, with three helpers:
`scheduled_sessions`, the exchange's calendar, copied from SC-026-01's code since a strategy imports
nothing from the lab, `new_moons` and `in_fortnight`.

1. **The calendar**: weekdays less the New York Stock Exchange's scheduled holidays by rule, from 45
   days before the market's first session to 62 days after its last, read from no price.
2. **The new moons**: for every whole k whose mean new moon falls between 40 days before the
   calendar's first date and 40 days after its last, JDE = 2451550.09765 + 29.530588853 k +
   0.0001337 T² − 0.000000150 T³ + 0.00000000073 T⁴, T = k / 1236.85; each taken as universal time,
   on the date of floor(JDE + 0.5), counted from Julian day 2451545, 1 January 2000. k = 0 gives 6
   January 2000, checked by a test in the code.
3. **Holding**: a date is in the new moon's fortnight when it lies within `days` days of the nearest
   new moon's date; on each session of the market, whether the next scheduled session's date is in
   it.
4. **The targets**: while holding, the funds that trade, in equal parts; otherwise nothing. A target
   is set on the market's first session and on each session on which the target changes, NaN
   elsewhere, every fund named, so that the funds drift with prices while held.

Why in this order: steps 1 and 2 are the calendar and the phases the card states, step 3 turns them
into the sessions held, step 4 into targets. Nothing reads a price but the funds' tradability, and
neither the calendar nor the phases read a date of the market: cut at any session, the targets up to
it are the same. Before the run, by `python -m lab.report --try`, gate 1's timing and ten dates for a
neighbour; and, apart from the battery, the count of in-sample sessions in each fortnight against the
card's 2,311 and 2,223.
