# SC-002-01 — build plan

1. **The calendar**: the exchange's scheduled sessions, weekdays less its holidays derived from their
   rules, as SC-008-01 built it (`ScheduledHolidays`, `scheduled_sessions`), from two months before
   the market's first session to two months after its last.
2. **The windows**: each December, the scheduled sessions after the first scheduled session on or
   after day `start`, up to and including December's `end` session counted back from its last.
3. **The weights**: the funds that trade in equal parts; on a session whose next scheduled session
   is in a window, SPY's part moved to IWM.
4. **The targets**: on the sessions on which the state changes, on the market's first session of
   each month outside the windows, and on the first session.
5. **Checks**: `--try`; by hand, the sessions held tilted and the switches against the count made
   before the card (146 sessions, 36 switches), the weights in and out of a window, and the monthly
   resets.
