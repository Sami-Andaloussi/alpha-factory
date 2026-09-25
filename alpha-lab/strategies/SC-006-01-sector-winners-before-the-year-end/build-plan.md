# SC-006-01 — build plan

1. **The calendar**: the exchange's scheduled sessions, weekdays less its holidays derived from their
   rules, as SC-008-01 built it (`ScheduledHolidays`, `scheduled_sessions`), from two months before
   the market's first session to two months after its last.
2. **The ranking**, each year: on the market's last session on or before December's twelfth-last
   scheduled session, each fund that traded on the market's first session of the year and trades
   that day has a drop from its highest close since that first session (`ranked`); the `winners`
   funds with the smallest drop, ties at the cut included.
3. **The window**: the sessions whose next scheduled session falls after December's `entry` session
   and up to its `exit` session, counted back from December's last; over them, the winners that trade
   in equal parts.
4. **The weights otherwise**: the funds that trade in equal parts; a target where the state changes,
   on the market's first session of each month outside the windows, and on the first session.
5. **Checks**: `--try`; by hand, the winners of a few years against the drops, the windows' sessions
   (five a year, eighteen windows), the ties of 2021 (four winners), XLRE's and XLC's first years left
   unranked, and the monthly resets.
