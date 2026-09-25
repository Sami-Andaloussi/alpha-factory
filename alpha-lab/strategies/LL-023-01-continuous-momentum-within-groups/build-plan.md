# LL-023-01 — Build plan

One function, `positions(market, lookback, skip, half)`, which calls `choose(market, lookback, skip,
half, pool)` with the pool the card states, twice the funds held; `choose` works in five steps, each
commented in `strategy.py` by its number. With a pool of once the funds held, under half
"continuous", it is CA-001-01's rule, which the checks before the run verify.

1. **The ranking return**, as CA-001-01: for each fund, the close `1 + skip` sessions before the
   target over the close `1 + lookback` sessions before it, less one, on `market.signal_prices`.
2. **Who is ranked**, as CA-001-01: a fund trading on the session and on the window's first
   session (`market.tradable`, shifted by `1 + lookback`), with a return over the window.
3. **The path score**: each fund's daily return, the close over the close before, less one, on the
   signal prices; over the `lookback - skip` daily returns of the window — those of the sessions
   from `lookback - 1` to `skip` sessions before the session before, the first of them measured
   from the window's first close — the count of positive returns less the count of negative ones,
   divided by `lookback - skip`. A return of zero counts in neither.
4. **The weights**: N funds trading; a fund trading but not ranked holds 1/N. On each first session
   of a month in which a fund is ranked, each group's n ranked funds give k, the top third of n
   rounded half to even, one at least; the pool is the min(2k, n) highest window returns, ties to
   the universe's order, as CA-001-01's ranking breaks them. The continuous half is the pool's k
   highest scores, ties to the higher window return, then to the universe's order; the discrete
   half is the rest of the pool when it holds 2k, and otherwise — a group of one ranked fund — its
   k lowest scores, with the same ties. Each fund held holds n/N/k. A ranked fund of the pool
   without a score, or a fund of the market in no group, is refused.
5. **Monthly**: the targets of the first session of each month in which a fund is ranked, NaN
   elsewhere, every fund named, so that a fund that leaves the half is sold.

Why in this order: steps 1 and 2 are CA-001-01's ranking, step 3 the path the card adds, step 4
the choice within the pool and CA-001-01's weights, step 5 its pace. Nothing is estimated, and
nothing reads beyond the session before. Under gate 6's cluster left out, the funds of that cluster
do not trade and are not ranked; their group holds nothing, as in CA-001-01.
