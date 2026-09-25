# LL-042-01 — Build plan

One function, `positions(market, lookback, rule)`, in five steps, each commented in `strategy.py` by
its number.

1. **Each fund's past excess return**: the close of the session before over the close `lookback`
   sessions earlier, less one, on `market.signal_prices`, less the Treasury bill's return over the
   same sessions (`market.rf` compounded). A fund without `lookback` sessions of prices has none.
2. **The two signals**: the bond market rises when IEF's past excess return is positive; the equity
   market falls when SPY's is negative. Both are read from the prices alone, never from
   `market.tradable`: gate 6 hands the strategy markets where IEF or SPY cannot be traded, and the
   other funds keep their signal there. When the signal fund is not in the market at all, its
   signal is off.
3. **Who is held**: under `rule` "both", an equity fund (SPY, QQQ, IWM, EFA, EEM) when its own past
   excess return and the bond signal are both positive, a bond fund (IEF, TLT) when its own is
   positive and the equity signal negative; under "cross", the other market's signal alone, the fund
   needing only a past return of its own. A fund that does not trade on the session is never held.
   Any other rule is refused.
4. **The weights**: each fund held takes one share of the portfolio, the number of funds the market
   holds giving the share — a seventh on the card's universe, as gate 6 leaves every fund in the
   market; the rest is cash.
5. **Monthly**: the targets of the first session of each month, NaN elsewhere, every fund named, so
   that a fund no longer held is sold.

Why in this order: steps 1 and 2 are the signals, step 3 the rule the card states, steps 4 and 5
the portfolio and its pace, TM-017-01's. Nothing reads beyond the session before.
