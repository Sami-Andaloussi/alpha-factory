# SC-010-01 — build plan

1. **The code**: SC-008-01's `strategy.py` unchanged but for its description — the calendar of
   scheduled sessions (`ScheduledHolidays`, `scheduled_sessions`), the window (`in_window`, the last
   `-start` and the first `end` scheduled sessions of each month) and the targets (the five funds
   that trade in equal parts if the next scheduled session is in the window, nothing otherwise; a
   target only on the sessions on which the state changes, and on the first); the card's window, -1
   to +9, is its parameters.
2. **Checks**: `--try`; by hand, the returns held and the switches against the count made before the
   card (2,156 returns held in-sample, 432 switches, as many for every neighbour).
