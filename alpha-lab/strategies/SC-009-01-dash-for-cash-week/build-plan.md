# SC-009-01 — build plan

1. **The calendar**: the exchange's scheduled sessions, weekdays less its holidays derived from their
   rules, as SC-008-01 built it (`ScheduledHolidays`, `scheduled_sessions`), from 45 days before the
   market's first session to 62 after its last, so that the month after the market's last session is
   whole.
2. **The window** (`in_window`): each scheduled session counted back within its month from its last,
   1 the last; in the window from `end + length - 1` to `end`.
3. **The targets**, as in SC-008-01 but inverted: on each session of the market, the five funds that
   trade in equal parts if the next scheduled session is outside the window, nothing otherwise; a
   target only on the sessions on which the state changes, and on the first.
4. **Checks**: `--try`; by hand, the returns out of the market and the switches against the count
   made before the card (1,080 window returns in-sample, the first on 2005-01-18, 432 switches, as
   many for every neighbour).
