# SC-019-01 — Build plan

The card is locked (`card: SC-019-01-january-barometer`). The code follows it step by step, in
`strategy.py`, one function `positions(market, months)`.

1. **The calendar of scheduled sessions**, as SC-017-01 built it: weekdays less the New York Stock
   Exchange's holidays by rule, from 45 days before the market's first session to 62 days after its
   last, read from no price. It places the sessions whose next scheduled session falls in the next
   year, on which the funds are bought back for January.
2. **The signal**: for each fund and year, its return over the year's first `months` calendar
   months, from its last close before the year to its last close of the last of those months, on
   the market's closes; from its first close in the market when it has none before the year. It is
   read on the market's first session of the next month, from closes up to the session before: the
   closes are shifted by one session, so that the session's own close is never read.
3. **The targets**: on the market's first session, and on each session whose next scheduled session
   falls in the next year, a fifth in each fund that trades; on the market's first session of the
   month after the signal's months, a fifth in each fund that trades and whose signal is positive,
   cash for the others; nothing on the other sessions, a row of NaN holding.
4. **Checks before the run**, by `python -m lab.report --try`: gate 1's timing and memory for the
   base, ten dates for the neighbour.
