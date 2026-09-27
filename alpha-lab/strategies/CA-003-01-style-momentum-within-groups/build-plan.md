# CA-003-01 — Build plan

The card is locked (`card: CA-003-01-style-momentum-within-groups`). One function,
`positions(market, window)`, in six steps, each commented in `strategy.py` by its number. The
styles are the card's: momentum and value are CA-001-01's and CA-024-01's rankings, read on the two
equity groups alone.

1. **The formations**: the first session of each month, where the month differs from the previous
   session's. Each fund's daily return is its signal close over the previous one, less one.
2. **The styles' scores**, at each formation, from closes up to the session before:
   - momentum, the close 22 sessions back over the close 253 sessions back, less one, the fund
     trading at the window's first session (CA-001-01's reading);
   - value, the close of the session before over the close 1,261 sessions back, less one, reversed
     by ranking it ascending (CA-024-01's);
   - defensive, the standard deviation of the 252 daily returns up to the session before, all of
     them present, the fund trading at the first close they read (253 sessions back), ranked
     ascending.
   A member is ranked if it trades at the formation and has its score.
3. **The legs**: in each group with two ranked members or more, a third k = rint(n / 3), one at
   least (half to even); the long leg the k best by the style's order, the short leg the k worst,
   ties to the order of the universe (`rank(method="first")` on columns in the universe's order).
4. **Each style's daily return**: the legs of each formation hold from the next session to the next
   formation, inclusive; so the legs are written on formation rows, carried forward, then shifted
   one row: a session reads the legs of the last formation strictly before it. On a session, each
   group with legs gives the mean return of its long leg less that of its short leg, and the groups
   are averaged with weights n, their numbers of ranked members at that formation. No legs, no
   return (NaN).
5. **Earned**: at each formation, a style has earned if its daily returns on each of the last
   `window` sessions up to the session before exist and sum above zero. The sum is taken on each
   window's own values (a sliding window over a NumPy array, not pandas' running sum), so that no
   value older than the window moves it, even by rounding: gate 1's memory check is then exact.
6. **The targets**: each style holds a third. Earned: of the N funds trading, each group with legs
   holds n/N of the third split among its long leg; every other trading fund holds 1/N of the
   third. Not earned, or no full record: the third in the N trading funds in equal parts. The three
   thirds are added and set on formation rows from the first formation at which any style has a
   full record; NaN elsewhere, so that positions drift.

Why in this order: steps 1 to 3 are the styles the card names, step 4 their record, step 5 the
state the card grades, step 6 the monthly holding. Nothing is estimated; nothing reads beyond the
session before. The earliest read is value's close 1,261 sessions before a formation whose legs
count in a window of up to 252 sessions, the formation up to 23 sessions before the window's first
session: about 1,536 sessions, within the card's memory of 1,600. Before the run, `python -m
lab.report --try` checks gate 1's timing for both variants, ten dates for each neighbour, and the
memory. The clause's regression and the reported measures are computed apart from the battery,
after the run, on the same closes, by a script that rebuilds the styles with this file's functions.
