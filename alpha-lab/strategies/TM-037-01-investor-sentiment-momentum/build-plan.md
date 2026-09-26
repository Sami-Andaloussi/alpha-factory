# TM-037-01 — Build plan

The card is locked (`card: TM-037-01-investor-sentiment-momentum`). One function,
`positions(market, window)`, in four steps, each commented in `strategy.py` by its number, taken
from TM-047-02's shape with its scale replaced by one state read from SPY's volume.

1. **SPY's log volume**: `market.signal_volumes["SPY"]`, each session's own consolidated volume; a
   missing or zero volume is NaN, so that it is left out of both averages.
2. **The measure**: at row t, the mean of the log volumes of rows t−window to t−1 less the mean of
   those of rows t−1260 to t−1, NaN-skipping, each computed on its own window's values (a sliding
   window, not a running sum), so that nothing older than 1,260 sessions before the session before
   moves it, not even by rounding: gate 1's memory check is then exact.
3. **The state**: defined from the row with 1,260 sessions before it, and where both means have a
   value; turnover high when the measure is above zero. Before that, not defined.
4. **The targets**: on the first session of each month, each fund trading holds 1/N, N the funds
   trading, when turnover is not high or not defined, and 0 when it is high, the portfolio then in
   cash; every fund named, NaN elsewhere so that positions drift.

Why in this order: steps 1 to 3 are the measure and state the card names, step 4 its monthly
rebalancing. Nothing is estimated; nothing reads beyond the session before. The earliest read is the
volume 1,260 sessions before the target, the card's memory. Before the run, by
`python -m lab.report --try`, gate 1's timing and ten dates for a neighbour, the memory checked. The
clause's regression and the reported measures are computed apart from the battery, after the run,
on the same closes and volumes.
