# CA-001-01 — Build plan

One function, `positions(market, lookback, skip)`, in five steps, each commented in `strategy.py`
by its number.

1. **The ranking return**: for each asset, the close `1 + skip` sessions before the target over the
   close `1 + lookback` sessions before it, less one, on `market.signal_prices`. The window ends
   `skip` sessions before the session before and starts `lookback` sessions before it, so that a
   target never reads its own session's close, whatever the skip.
2. **Who is ranked**: an asset trading on the session, whose window lies wholly in the sessions it
   traded: trading on the session and on the window's first session (`market.tradable`, shifted by
   `1 + lookback`). An asset whose prices start before its first tradable session, as XLRE's do, is
   ranked only a full lookback after that first session.
3. **The leaders of each group**: the three groups are named in the code — the eleven sector funds,
   the five equity markets, the three commodity funds — and each keeps the members its market holds,
   since gate 6 hands the strategy markets without a cluster. An asset of the market in no group is
   refused. In each group, the ranked members are ordered by their ranking return, and the top third,
   rounded half to even, one at least, are its leaders.
4. **The weights**: N is the number of assets trading on the session. A group of n ranked members
   holds n/N, split equally among its leaders; an asset trading but not ranked holds 1/N, its weight
   in the benchmark; every other asset holds nothing. The weights add up to one whenever an asset is
   ranked.
5. **Monthly**: the targets of the first session of each month in which an asset is ranked, NaN
   elsewhere, so that the positions drift with prices between two first sessions. Every row with a
   target names every asset, so an asset that leaves the leaders is sold.

Why in this order: step 1 is the signal, steps 2 and 3 turn it into a choice within each group,
step 4 into weights that keep each group's share of the benchmark, step 5 is the rebalancing the
card states. Nothing is estimated, and nothing reads beyond the session before.
