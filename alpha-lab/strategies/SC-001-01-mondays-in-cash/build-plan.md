# SC-001-01 — build plan

1. **The calendar**: the exchange's scheduled sessions, weekdays less its holidays derived from their
   rules, as SC-008-01 built it (`ScheduledHolidays`, `scheduled_sessions`), from two weeks before
   the market's first session to three weeks after its last, so that every session of the market has
   a next scheduled session.
2. **In or out**: each scheduled session numbered within its calendar week, Monday to Sunday, from
   its first and from its last; with `day` first, a session is out when it is among the first
   `count`, and in otherwise; with `day` last, in when it is among the last `count`, and out otherwise.
3. **The targets**: on each session of the market, the five funds that trade in equal parts if the
   next scheduled session is in, and nothing if it is out; a target only on the sessions on which the
   state changes, and on the first.
4. **Checks**: `--try`; by hand, the sessions held over and the switches against the count made before
   the card (3,592 of 4,531 held over and 1,877 switches for the base; 939 and 1,878 for the
   variant), and the four unscheduled closures.
