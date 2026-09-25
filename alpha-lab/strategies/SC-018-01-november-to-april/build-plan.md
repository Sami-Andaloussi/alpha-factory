# SC-018-01 — Build plan

One function, `positions(market, first, months, late, early)`, in four steps, each commented in
`strategy.py` by its number, with two helpers: `scheduled_sessions`, the exchange's calendar, copied
from SC-017-01's code since a strategy imports nothing from the lab, and `held_sessions`.

1. **The calendar**: weekdays less the New York Stock Exchange's scheduled holidays, from pandas'
   holiday rules, as in SC-008-01 and SC-017-01. It reads no price and no date of the market; it
   runs from 45 days before the market's first session to 62 days after its last.
2. **The sessions held**: the `months` consecutive calendar months from the month named `first` are
   out, wrapping past December; a scheduled session is held if its month is not out, or if it is
   among the first `late` sessions of the first month out, or among the last `early` sessions of
   the last month out, counted on the scheduled calendar.
3. **Holding**: on each session of the market, whether the first scheduled session after it is
   held; the portfolio then holds equities over the sessions held.
4. **The targets**: while holding, the funds that trade, in equal parts; otherwise nothing. A target
   is set on the market's first session and on each session on which holding changes, NaN
   elsewhere, every fund named, so that the funds drift with prices while held.

Why in this order: steps 1 and 2 are the calendar and the halves the card states, step 3 turns them
into the days the portfolio holds, step 4 into targets. Nothing reads a price, and the calendar
reads no date of the market. Before the run, the targets' dates are checked: the base leaves on
April's last session and returns on October's; the variant leaves on May's first and returns on
October's sixth-last.
