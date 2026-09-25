# SC-007-01 — build plan

1. **The calendar**: the exchange's scheduled sessions, weekdays less its holidays derived from their
   rules, as SC-008-01 built it (`ScheduledHolidays`, `scheduled_sessions`), from 45 days before the
   market's first session to 62 after its last.
2. **The window** (`in_window`): each scheduled session counted within its month from its first and
   from its last; in the window if among December's last `december` or January's first `january`.
3. **The targets**, as in SC-008-01: on each session of the market, the five funds that trade in equal
   parts if the next scheduled session is in the window, nothing otherwise; a target only on the
   sessions on which the state changes, and on the first.
4. **Checks**: `--try`; by hand, the sessions held over and the switches against the count made before
   the card (125 held-over sessions in the in-sample market, the last of which, 2022-12-30, holds a
   holdout return, and 36 switches), the 2006–07 window around the closure of 2 January 2007.
