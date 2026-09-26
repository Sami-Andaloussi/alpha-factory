# TM-041-01 — Build plan

The card is locked (`card: TM-041-01-small-cap-autocorrelation`). One function,
`positions(market, period)`, in four steps, each commented in `strategy.py` by its number, taken
from TM-017-01's shape with its lookback set to one block and its monthly targets replaced by blocks.

1. **The fund's own return**: over the last `period` sessions, up to the session before, from the
   closes.
2. **The bill's return** over the same sessions.
3. **The weights**: each fund that trades holds 1/N, N the funds trading, when its return beats the
   bill's; its share is in cash otherwise, and while it has fewer than `period` + 1 closes, its
   return then missing. The funds trading count in N whether they are held or not.
4. **The targets**: on the first session of each block of `period` sessions, counted from the
   session of 2005-01-03 (located by its date, so that the grid does not depend on where the market
   handed to the rule begins, as long as it holds that session); every fund named, NaN elsewhere so
   that positions drift.

Why in this order: steps 1 to 3 are the rule the card names, step 4 its blocks. Nothing is
estimated; nothing reads beyond the session before. The earliest read is the close `period` + 1
sessions before the target, within the card's memory of 21. Before the run, by
`python -m lab.report --try`, gate 1's timing and ten dates for a neighbour, the memory checked. The
clause's regression and the reported measures are computed apart from the battery, after the run, on
the same closes and costs.
