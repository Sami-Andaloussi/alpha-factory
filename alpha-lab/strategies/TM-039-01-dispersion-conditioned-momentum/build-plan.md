# TM-039-01 — Build plan

One function, `positions(market, lookback, skip, scope)`, in six steps, each commented in
`strategy.py` by its number, with two helpers: `dispersion`, a set's reading on each session, and
`dispersed`, its state. With every group always in the state it is CA-001-01's rule, which the
checks before the run verify.

1. **The ranking return**, as CA-001-01: for each fund, the close `1 + skip` sessions before the
   session over the close `1 + lookback` sessions before it, less one, on `market.signal_prices`.
2. **Ranked on each session**, as CA-001-01 ranks on a target: trading on the session and on the
   window's first session (`market.tradable`, shifted by `1 + lookback`), with a window return.
3. **The month just past**: the close of the session before over the close `1 + skip` sessions
   before, less one, on the signal prices: the `skip` sessions the ranking leaves out.
4. **The state**: on each session, the standard deviation (n − 1 in the denominator) of the month's
   returns of the ranked funds of the set, NaN with fewer than two; the set is each group under
   scope "group", all nineteen funds under "all". The line is the average of the readings from the
   first through the session before (an expanding mean shifted by one session, NaN readings left
   out). In the state when the session's reading is above the line; out of it when at or below,
   without a reading, or before the line exists. Under "all", one state serves every group.
5. **The weights**: N funds trading; a fund trading but not ranked holds 1/N. A group in the state
   holds CA-001-01's weights: its n ranked funds hold n/N, split equally among its top third by the
   window return, rounded half to even, one at least, ties to the universe's order. A group out of
   the state holds each of its n ranked funds at 1/N. A fund in no group is refused.
6. **Monthly**: the targets of the first session of each month in which a fund is ranked, NaN
   elsewhere, every fund named.

Why in this order: steps 1 and 2 are CA-001-01's ranking, step 3 the month the card reads, step 4
the state the card adds, step 5 the weights in and out of it, step 6 CA-001-01's pace. Nothing is
estimated, and nothing reads beyond the session before: the reading on a target session uses closes
up to the session before, and the line readings before that. Under gate 6's cluster left out, the
funds of that cluster do not trade and are not ranked: a group left with no ranked fund holds
nothing, and under "all" the reading is taken over the funds that remain.
