# TM-028-01 — Build plan

The card is locked (`card: TM-028-01-low-turnover-momentum`). One function,
`positions(market, window, volume)`, in four steps, each commented in `strategy.py` by its number,
taken from TM-017-01's shape with its trend replaced by the quiet sessions' index.

1. **The quiet sessions**: a session is quiet when its deciding volume is below the session
   before's — each fund's own volume for `own`, SPY's for every fund for `market`; a missing volume,
   or an equal one, makes no session quiet. A value of `volume` outside these two is refused. The
   fund volumes in `market.signal_volumes` are each session's own, so every read is shifted a
   session, as the closes are.
2. **The index's trend**: at the target's session, over the sessions to the session before, the
   log return of each quiet session and zero for the others; the index up when it stands above its
   average over the last `window` sessions to the session before. The ratio of the index to that
   average reads only the window's sessions: with D_k the summed log returns of the last k sessions,
   the average over the index is (1 + Σ_{k=1}^{window−1} exp(−D_k)) / window, and the index is up
   when that is below 1. It is computed on each window's own values (a sliding window, not a running
   sum), so that nothing older than the window moves it, not even by rounding: gate 1's memory
   check is then exact.
3. **Defined**: a fund whose price the session `window` sessions before the session before is
   missing, or with any missing return or volume inside the window, has no trend; it holds its 1/N.
4. **The targets**: on the first session of each month, each fund trading holds 1/N, N the funds
   trading, when its index is up or not defined, and 0 otherwise, its share left in cash; every fund
   named, NaN elsewhere so that positions drift.

Why in this order: steps 1 and 2 are the index the card names, step 3 the funds too new to have it,
step 4 TM-017-01's monthly rebalancing. Nothing is estimated; nothing reads beyond the session
before. The earliest read is the close `window` sessions before the session before, within the
card's memory of 256. Before the run, by `python -m lab.report --try`, gate 1's timing and ten dates
for a neighbour, the memory checked. The clause's regression and the reported measures are computed
apart from the battery, after the run, on the same closes and volumes.
