# TM-006-01 — Build plan

The card is locked (`card: TM-006-01-momentum-after-market-gains`). One function,
`positions(market, bear_window)`, in five steps, each commented in `strategy.py` by its number,
taken from TM-024-01's code with its rule "panic" less the volatility condition, and its rule
"scale" removed.

1. **CA-001-01's weights**: within each group, the funds ranked by the return from 252 to 21
   sessions before the session before the target, ranked when trading on the session and on the
   window's first session; the top third, rounded half to even, one at least, share the group's
   n/N; a fund trading but not yet ranked holds 1/N.
2. **The tilt**: those weights less the neutral weights, 1/N for each fund trading.
3. **Each fund's daily return**, and each group's market: the average of the daily returns of its
   funds trading on the session, chained from its first return.
4. **The state**: a group is in a down state when its market, on the session before, is below its
   level `bear_window` sessions before that; k = 0 then, and 1 otherwise, including while the
   market has not `bear_window` sessions of history.
5. **The targets**: each group in equal parts plus k times its tilt, on the first session of each
   month on which a fund is ranked, every fund named, NaN elsewhere so that positions drift.

Why in this order: steps 1 and 2 are CA-001-01's rule, steps 3 and 4 the state the card adds, step
5 the rebalancing. Nothing is estimated, and nothing reads beyond the session before. Before the
run, by `python -m lab.report --try`, gate 1's timing and ten dates for a neighbour, the memory of
504 sessions checked.
