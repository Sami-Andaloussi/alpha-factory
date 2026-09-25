# SC-023-01 — Build plan

The card is locked (`card: SC-023-01-same-month-across-assets`). The code follows it step by step,
in `strategy.py`, one function `positions(market, years, top)`, with two helpers:
`scheduled_sessions`, the exchange's calendar, copied from SC-019-01's code since a strategy imports
nothing from the lab, and `monthly_returns`.

1. **The calendar of scheduled sessions**, as SC-017-01 built it: weekdays less the New York Stock
   Exchange's holidays by rule, from 45 days before the market's first session to 62 days after its
   last, read from no price. On each session of the market, the month of the next scheduled session;
   a session whose next scheduled session falls in a new calendar month m is a decision session for
   month m.
2. **The monthly returns**: for each calendar month of the market and each asset, the return from
   its close on the market's last session of the month before to its close on the market's last
   session of the month, raw, not less the bill; unknown where either close is missing. The
   average's return in a month is the mean of the returns known in it, the universe's assets that
   have one in equal parts.
3. **The window**, on a decision session for month m: the calendar months m − 12 × `years` to
   m − 2, `12 × years − 1` months (59 for the base). Month m − 1, the month in progress, is left
   out: its return ends at the decision session's own close, which the signal does not read. Every
   close the window reads is the last close of month m − 2 or earlier.
4. **The ranking**: an asset is ranked when it trades on the decision session and its returns in
   every month of the window are known. Its beta is the ordinary least-squares slope, with an
   intercept, of its monthly returns on the average's over the window; its residual in each month of
   the window is its return less its beta times the average's; its signal is the mean of its
   residuals in the window's months whose calendar month is m, the lags of 12, 24, …, 12 × `years`
   months.
5. **The targets**: on each decision session, the `top` assets ranked highest on the signal in equal
   parts, all those ranked when fewer, every other asset at zero; when no asset is ranked, nothing,
   a row of zeros. Ties, which continuous signals make unlikely, are broken by the universe's order.
   No target is set on the other sessions, a row of NaN holding, so that the holdings drift with
   prices over the month.
6. **Checks before the run**, by `python -m lab.report --try`: gate 1's timing and memory for the
   base, ten dates for the neighbour. And, apart from the battery, the calendar's decision sessions
   against the market's month ends from 2005 to 2025; the first month with an asset ranked
   (February 2010) and the count of ranked assets by month; and one decision recomputed by hand from
   the closes.

Why in this order: steps 1 to 3 are the dates and returns the card names, step 4 its signal, step 5
its targets. The window stops at month m − 2, so a market cut at any session gives the same targets
up to it; the memory of 1,290 sessions covers the oldest close read, the last of month m − 61, about
1,260 sessions before a decision.
