# CA-024-01 — Build plan

One function, `positions(market, lookback, skip)`, in five steps, each commented in `strategy.py` by
its number: CA-001-01's code, with the ranking reversed, the bottom third held rather than the top.

1. **The value window's return**, read on `signal_prices` from `lookback` sessions before the
   session before the target to `skip` sessions before it: the target set on session t reads
   prices up to t-1 at most.
2. **Ranked**: a fund trading on the target's session and on the window's first session, with a
   return over the window.
3. **The cheapest of each group**: its bottom third of ranked members by that return, rounded, one
   at least, ties broken by the groups' order (`method="first"`).
4. **The weights**: of the N funds trading, a group of n ranked members holds n/N, split equally
   among its cheapest; a fund trading but not yet ranked holds 1/N.
5. **The targets**: on the first session of each month in which a fund is ranked, every fund named,
   NaN elsewhere; the funds drift with prices between them.

Why in this order: the return, then who may be ranked, then the choice, then the weights, then the
dates, as CA-001-01, so that the two halves differ only in the sign of the ranking. Before the run,
`--try` checks the timing and the declared memory of 1,260 sessions, and the counts of targets and
decisions are compared with those made before the card (155 and 70 for the base).
