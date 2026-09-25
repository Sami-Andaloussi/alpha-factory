# SC-014-01 — build plan

1. **The calendar**: the exchange's scheduled sessions, weekdays less its holidays derived from their
   rules, as SC-008-01 built it (`ScheduledHolidays`, `scheduled_sessions`), from 45 days before the
   market's first session to 62 after its last.
2. **The sessions held** (`pre_holiday`): for each scheduled holiday that falls on a weekday, the
   scheduled session `offset` places before it, found by its position in the calendar; a New Year's
   Day on a Saturday, not observed, holds none.
3. **The targets**, as in SC-008-01: on each session of the market, the five funds that trade in equal
   parts if the next scheduled session is held, nothing otherwise; a target only on the sessions on
   which the state changes, and on the first.
4. **Checks**: `--try`; by hand, the sessions held over and the switches against the count made before
   the card (161 pre-holiday sessions in-sample, the first held on 2005-01-14, 322 switches, as many
   for offsets 2 and 3), none of the closures outside the rules among the sessions held.
