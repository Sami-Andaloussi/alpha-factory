# TM-017-02 — Build plan

The card is locked (`card: TM-017-02-one-month-trend`). One function, `positions(market, lookback)`,
TM-017-01's, in its four steps, each commented in `strategy.py` by its number; only the docstring
differs from TM-017-01's file, and the lookback is the card's, 21 sessions.

1. **The fund's own return** over the past `lookback` sessions, up to the session before.
2. **The bill's return** over the same sessions.
3. **In trend**: the fund beats the bill and trades today; a seventh of the portfolio each, the rest
   in cash; a fund without `lookback` + 1 closes has no return and holds cash.
4. **The targets** on the first session of each month, every fund named, NaN elsewhere so that
   positions drift.

The earliest read is the close `lookback` + 1 sessions before the target, within the card's memory
of 22. Before the run, by `python -m lab.report --try`, gate 1's timing and ten dates for a
neighbour, the memory checked. The clause's regression and the reported measures are computed apart
from the battery, after the run, on the same closes and costs.

The file was drafted in the session's scratchpad before the card was locked, while its audit ran,
by copying TM-017-01's; it was not run, and it was placed here only after the lock (the verdict
records the departure from step 4's order).
