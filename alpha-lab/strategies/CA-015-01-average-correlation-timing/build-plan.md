# CA-015-01 — Build plan

The card is locked (`card: CA-015-01-average-correlation-timing`). One function, `positions(market,
window, lookback, rule)`, in four steps, each commented in `strategy.py` by its number, and a
helper, `readings`, for the first.

1. **The reading**: on every session, over the sector funds that trade on that session and have
   window daily returns in the signal prices up to and including the session before, the average of
   the correlations of every pair's returns; none while fewer than two such funds exist.
2. **The share**: on every session with a reading and lookback readings before it, all present,
   under "scaled" the share of those readings at or below the reading; under "median" one when the
   reading is above their median, zero otherwise.
3. **The months**: the first session of each month, where the calendar month differs from the
   previous session's.
4. **The targets**: on each month's first session with a share, each sector fund that trades holds
   the share divided by the number of sector funds trading, the rest in cash; NaN on every other
   session, so that positions drift.

Why in this order: steps 1 and 2 are the card's reading and scale, steps 3 and 4 its pace and
holdings. Nothing is estimated; nothing reads beyond the session before. The earliest close read is
lookback plus window sessions before the session before, the first return's extra close included:
1,197 for the largest neighbour, within the card's memory of 1,240. Before the run, `python -m
lab.report --try` checks gate 1's timing for the two variants, ten dates for each neighbour, and the
memory. The clause and the reported measures are computed apart from the battery, after the run, on
the sector funds held in equal parts and the base's share, as the card states.
