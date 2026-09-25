# MR-032-01 — build plan

CA-001-01's construction, the ranking reversed, the window shortened, the pace weekly or monthly,
and the baskets either the three groups or the nineteen funds together.

1. **The return that ranks**: from `lookback` sessions before the session before the target to that
   session (`prices.shift(1) / prices.shift(1 + lookback) - 1`), on `market.signal_prices`.
2. **Ranked members**: trading on the session and on the window's first session, with a return.
3. **Baskets**: with `basket` groups, the three groups of the card; with `basket` universe, the
   nineteen in the card's order. Any other value, or a fund in no group, is refused.
4. **Laggards**: in each basket of n ranked members, the k = n/3, rounded, one at least, with the
   lowest returns; a tie at the cut goes to the member listed first (`rank(method="first")` over the
   columns in the card's order).
5. **Weights**: a basket of n ranked members of N funds trading holds n/N, equally among its
   laggards; a fund trading but not ranked holds 1/N.
6. **Pace**: targets on the first session of each calendar week, Monday to Sunday (the ISO year and
   week of the session differ from the session before's), or of each month, from the first period
   in which a fund is ranked; every fund named.
7. **Checks**: `--try` (look-ahead, memory, neighbours); by hand, on a few dates, that the laggards
   are the lowest returns of each basket and the weights sum to one.
