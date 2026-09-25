# TM-040-01 — build plan

The code is CA-024-01's construction, the groups, the ranked members and the weights unchanged, with
the selection within each group replaced by the card's two forms.

1. **The two measures**, read to the session before the target: value, the return from `value`
   sessions before it to it (`prices.shift(1) / prices.shift(1 + value) - 1`); momentum, the return
   from `momentum` sessions before it to `skip` sessions before it
   (`prices.shift(1 + skip) / prices.shift(1 + momentum) - 1`). Both on `market.signal_prices`.
2. **Ranked members**: trading on the session and on the session `value` sessions before the session
   before it, with both returns. The value window is the longer in every variant and neighbour, so
   that it alone decides when a fund is ranked.
3. **Places**: a group of n ranked members holds k = the top third of n, rounded, one at least; each
   place weighs (n / N) / k, N the funds trading.
4. **Composite**: value rank (1 the lowest return) and momentum rank (1 the highest), each among the
   ranked members; the average of the two; the k-th lowest average is the cut. Members below the cut
   take a place each; members at the cut share the places left, k less the number below, equally.
   Averages of whole ranks are halves, so the equality is exact.
5. **Screen**: the ranked members whose value rank is at most n / 2 rounded up are kept; the k of
   them with the highest momentum take a place each.
6. **Not ranked**: a fund trading but not ranked holds 1/N, its benchmark weight.
7. **Targets** on the first session of each month in which a fund is ranked, every fund named.
8. **Checks** by `--try`: the look-ahead and memory checks, the neighbours' targets, and by hand on a
   few dates that the weights of each group sum to n/N, that tied members share, and that the screen
   holds only cheaper-half members.
