# TM-018-01 — Build plan

One function, `positions(market, condition, mdi_window, lookback)`, in four steps, each commented in
`strategy.py` by its number.

1. **The state**, read on closes up to the session before, from `market.signal_prices`, whether the
   funds trade or not.
   - Under `condition` "divergence": each fund's absolute change over its last `mdi_window` daily
     changes, over the sum of their absolute values, requiring all of them; the index is the
     average over the funds that have it; divergent when above the expanding mean of its daily
     values through the session before.
   - Under "crisis": SPY's month closes, the last session of each month; a crisis month is one in
     which SPY fell and the unbroken run of falling months ending with it lost 5% or more; the state
     on a session is that of the month of the session before, so that on the first session of a
     month it is the month just ended.
   Any other condition is refused.
2. **TM-017-01's rule**, its code unchanged: a fund that trades and whose return over the past
   `lookback` sessions beats the bill's over the same sessions takes a seventh; a fund without
   `lookback` + 1 closes is out of trend.
3. **Out of the state**, the funds that trade in equal parts; the weights are the rule's in the
   state and these otherwise.
4. **Monthly**: the targets of the first session of each month, from the first in which the state is
   known and a fund has `lookback` + 1 closes, NaN elsewhere, every fund named.

Why in this order: step 1 is what the theory adds, step 2 the rule it conditions, step 3 the
neutral, step 4 TM-017-01's pace. Nothing reads beyond the session before.
