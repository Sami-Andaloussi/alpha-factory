# TM-023-01 — Build plan

The card is locked (`card: TM-023-01-quarter-end-momentum`). One function,
`positions(market, lookback, skip, months)`, in four steps, each commented in `strategy.py` by its
number, taken from TM-006-01's code with its market state replaced by the calendar.

1. **CA-001-01's weights**: within each group, the funds ranked by the return from `lookback` to
   `skip` sessions before the session before the target, ranked when trading on the session and on
   the window's first session; the top third, rounded half to even, one at least, share the group's
   n/N; a fund trading but not yet ranked holds 1/N.
2. **The tilt**: those weights less the neutral weights, 1/N for each fund trading.
3. **The calendar**: k = 1 when the target's month is one the variant names — March, June,
   September and December for `quarter-ends`, every month but January for `all-but-january` — and 0
   otherwise; a value of `months` outside these two is refused.
4. **The targets**: the neutral weights plus k times the tilt, on the first session of each month on
   which a fund is ranked, every fund named, NaN elsewhere so that positions drift.

Why in this order: steps 1 and 2 are CA-001-01's rule, step 3 the calendar the card adds, step 4
the rebalancing. Nothing is estimated, and nothing reads beyond the session before; the calendar
reads the target's own month, known in advance. Before the run, by `python -m lab.report --try`,
gate 1's timing and ten dates for a neighbour, the memory of 252 sessions checked. The clause's
regression and the reported measures are computed apart from the battery, after the run.
