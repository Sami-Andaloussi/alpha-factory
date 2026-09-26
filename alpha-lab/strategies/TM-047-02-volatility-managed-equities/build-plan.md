# TM-047-02 — Build plan

The card is locked (`card: TM-047-02-volatility-managed-equities`). One function,
`positions(market, window, target, scaling)`, in four steps, each commented in `strategy.py` by its
number.

1. **The portfolio's daily return**: on each session, the average of the daily returns of the funds
   that traded it (tradable on that session, with a close on it and the session before).
2. **Its risk**: at each target's session, the standard deviation (one degree of freedom) of the
   last `window` of those daily returns to the session before, annualized by √252, computed on each
   window's own values (a sliding window, not pandas' running sums), so that nothing older than the
   window moves it, even by rounding; NaN while the window has fewer than `window` returns or a gap.
3. **The scale**: k = min(1, (target / risk)²) for `variance`, min(1, target / risk) for
   `volatility`, and 1 where the risk is not defined; a value of `scaling` outside these two is
   refused.
4. **The targets**: on the first session of each month, each fund trading holds k/N, N the funds
   trading, the rest in cash; every fund named, NaN elsewhere so that positions drift.

Why in this order: steps 1 and 2 are the portfolio and its risk the card names, step 3 the scale,
step 4 TM-017-01's monthly rebalancing. Nothing is estimated beyond the window; nothing reads beyond
the session before. The earliest read is the close `window` sessions before the session before,
within the card's memory of 22. Before the run, by `python -m lab.report --try`, gate 1's timing and
ten dates for a neighbour, the memory checked. The clause's regression and the reported measures are
computed apart from the battery, after the run.
