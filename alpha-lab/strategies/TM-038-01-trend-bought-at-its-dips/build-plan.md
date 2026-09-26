# TM-038-01 — Build plan

The card is locked (`card: TM-038-01-trend-bought-at-its-dips`). One function,
`positions(market, dip)`, in four steps, each commented in `strategy.py` by its number, the book
taken from TM-017-01's rule as TM-018-01 recomputed it.

1. **The book**: on each month's first session, each fund whose return over the past 252 sessions,
   read up to the session before, beats the bill's over the same sessions and that trades holds a
   seventh; every fund named.
2. **Its record**: each session's return of the book less the bill's. The holdings set at the close
   of a month's first session drift with the funds' closes, the cash with the bill, until the next
   first session; the session's excess return is the holdings times the funds' returns less the
   bill's, over the book's value the session before. While the book holds nothing it is zero. Each
   month's holdings start afresh from its targets, so a session's excess return reads only the closes
   since its month's first session and that target's own reads.
3. **The dip**: at row t, whether the sum of the excess returns of rows t−dip to t−1 is below zero,
   summed on each window's own values (a sliding window, not a running sum), so that nothing older
   than the window's months moves it, not even by rounding: gate 1's memory check is then exact.
   False while fewer than dip rows precede t.
4. **The targets**: on the first session of each month, the book's weights times k, 1 in a dip and
   0.5 otherwise, the rest in cash; NaN elsewhere so that positions drift.

Why in this order: steps 1 and 2 are the book and its record the card names, step 3 its state, step
4 the monthly rebalancing. Nothing is estimated; nothing reads beyond the session before. The
earliest read is the close 275 sessions before the oldest session of the window, within the card's
memory of 530 for dips up to 255. Before the run, by `python -m lab.report --try`, gate 1's timing
and ten dates for a neighbour, the memory checked. The clause's regression and the reported measures
are computed apart from the battery, after the run, on the same closes and costs.
