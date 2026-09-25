# SC-013-01 — Infrequent rebalancing: reasoning, not testable

## The theory, and the form its sources give it

SC-013 holds that investors who rebalance at set calendar horizons, monthly, quarterly or otherwise,
rather than continuously, release their orders in batches when the date comes, so that demand and
price pressure return at regular intervals: returns show autocorrelation and seasonality at the
frequencies of rebalancing, with an autocorrelation whose sign can vary, and the cross-sectional
dispersion of expected returns can rise in rebalancing periods. It is a mechanism that would link
several families of anomalies — seasonality, autocorrelation, calendar patterns in turnover — and
the bank's refutations name what sets it apart from them: no recurring pressure, autocorrelation or
rise in dispersion at the frequencies of rebalancing; holdings and trading data showing no batching
of orders at rebalancing dates, or return patterns unrelated to it; and seasonal patterns that
vanish once known although the routines behind them continue.

**Its sources.** The bank names Bogousslavsky (2016), *Infrequent Rebalancing, Return
Autocorrelation, and Seasonality*, and Harvey, Mazzoleni and Melone (2025), *The Unintended
Consequences of Rebalancing*. Neither is in the library, which cites Bogousslavsky nowhere and
Mazzoleni only for other work. The theory corpus from which the bank was built names them and gives
no figure and no sign; its ranking adds one frequency, intramonth autocorrelation, and calls the
theory testable on QuantConnect's native data (prices, volume, calendar) and a frame for
turn-of-the-month and quarter-end strategies, while its own report on the theory calls it hard to
test directly without fine holdings and trading data.

**What the library holds on rebalancing.**

- Ilmanen (*Investing Amid Low Expected Returns*, 2022): box 11.1 on how and how often an investor
  should rebalance, rebalancing being defensively contrarian, selling past gainers and buying past
  laggards; the rebalancers, the fast-growing target-date fund industry among them, counted among
  the market's stabilising, contrarian participants (chapter 8); and, in Figure 8.4, monthly and
  quarterly return autocorrelations positive — momentum — across twenty premium series from 1990 to
  2020, a sign at SC-013's frequencies that he attributes to momentum.
- Ilmanen (*Expected Returns*, 2011, chapter 28): an investor should not rebalance at month ends,
  when the crowd is likely to act — batched month-end rebalancing and its cost of impact, with no
  sign for returns.
- Athanassakos and Schnabel (1994), in Keim and Ziemba's *Security Market Imperfections in Worldwide
  Equity Markets* (2000): a theory of portfolio rebalancing by managers with a calendar-year
  horizon, equities favoured early in the year, with Canadian mutual funds' equity investing
  significant in the first quarter from 1973 to 1992 (in Athanassakos and Foerster's chapter on
  Canadian anomalies).
- Madhavan (*Exchange-Traded Funds and the New Dynamics of Investing*, 2016): leveraged funds'
  rebalancing at every close, always with the market.
- McConnell and Xu (2008): the turn of the month no stronger at quarter-ends in value-weighted
  returns, so not a quarterly batch, and NYSE volume no higher at the turn.

## Why the lab cannot test it

What the theory claims beyond the regularities it would explain is that they come from orders
batched at rebalancing dates. Its second and third refutations need the holdings and trading of the
rebalancers, or their routines over time, which the lab's data does not hold: the snapshot holds the
daily prices and traded volumes of twenty-two funds and bitcoin, the bill rate and two exchange
rates of the Swiss franc. Its first refutation can be read on prices, but no form of it that carries
a sign the library gives is this theory's own, and the one form that is its own meets a gate built
to fail it.

**What was considered, and why it does not rescue the test:**

- **Recurrence at the same point of the month or quarter, asset by asset**, the form closest to the
  theory's own: an asset's return on a given session of the month would predict its return on that
  session in later months — seasonality at the rebalancing period itself, which the corpus reads as
  intramonth autocorrelation. No library source gives its sign at a monthly or quarterly period;
  Keloharju, Linnainmaa and Nyberg's positive sign is for the calendar month and the weekday,
  SC-023's, and would be carried over by analogy. A rule that holds each asset on the sessions where
  it did well changes its holdings from one session to the next; gate 6's day of delay moves it onto
  the next session's phase and fails it by construction, as SC-011-01 argued for a one-day rule, a
  failure on which the lab does not spend a trial. Coarsened to weeks of the month, asset by asset —
  each asset held in the week where its past same-week returns were best — it would survive a day's
  delay; but its only sign is SC-023's, carried from the calendar month and the weekday to a week of
  the month that no source measures, and SC-023 claims a calendar signature "at several
  frequencies": it is SC-023's to draw with that theory's sources, not this theory's. Coarsened
  further, to windows common to every asset, it becomes the windows SC-008-01, SC-009-01 and
  SC-010-02 have read.
- **Autocorrelation at the frequencies of rebalancing, with its sign left open**, as the bank gives
  it. A rule needs a sign, fixed on the card before any backtest (the lab's framing, §6), and the
  lab's cards take their parameters and signs from the sources, not from the lab's data. The sign
  the library gives at monthly and quarterly lags is momentum's (Ilmanen 2022, Figure 8.4),
  **TM-017**'s, while rebalancers trade against the move; no source gives the sign of the part
  rebalancing contributes. The bank names the frequencies but not whether the batch shows at a lag
  of one period or at the same point of successive periods; a two-sided test grades no strategy,
  since the battery grades positions.
- **A sign estimated as the rule goes**, each asset's trailing autocorrelation at 21 or 63 sessions
  from data up to the session before: a signal, not a parameter, which gate 1 allows. But no source
  says the sign persists long enough for a trailing estimate to catch it — the bank calls it
  variable; over a five-year window, about sixty monthly observations (a standard error of about
  0.13) or twenty quarterly ones (about 0.22), so the sign it caught would mostly be noise; and what
  it caught would be TM-017's momentum or the reversal of the mean-reversion theories, **MR-007**
  for a sign that varies, with nothing to tell rebalancing apart.
- **Recurrence in the same calendar month over years, or on the same weekday**: **SC-021**'s and
  **SC-023**'s claims, with their own sources (Heston and Sadka; Keloharju, Linnainmaa and Nyberg),
  which the lab will read as theories of their own; SC-021 names a stable investor base with
  calendar routines among its explanations.
- **Pressure at the month's end and the quarter's end, with a sign**: that balanced, pension and
  target-date funds sell equities after they rise and buy them after they fall is **FP-023**'s
  claim, whose main clause gives the sign (it also allows the reverse), and which a card could read
  as SPY against TLT after large moves; month-end, quarter-end and year-end window dressing is
  **FP-018**'s; the rebalancing of leveraged funds at every close **FP-015**'s, daily and not
  infrequent; index rebalancing FP-011's and FP-012's. The recurring pressure at monthly and
  quarterly frequencies that SC-012-01 left to this theory lands, unconditioned, on the windows
  SC-008-01, SC-009-01 and SC-010-02 read, and, conditioned on the preceding move, on FP-023. The
  lab's own readings of month-ends — SC-009-01's long Treasury fund rising while the equity funds
  fell before the month's end, its months that end a quarter no weaker — are the lab's data and
  cannot give a card its sign.
- **Calendar-year rebalancing into equities**: Athanassakos and Schnabel's form is a rebalancing
  form with a sign, at the yearly horizon: the whole market stronger in the first quarter, measured
  on Canada, which the lab does not hold. It is a month-of-the-year claim, SC-017's family, with the
  rebalancing at the turn of the year SC-002 names among its forces; neither SC-017-01 (September
  and October) nor SC-002-01 (small caps in late December) read it, and both theories are closed. A
  first-quarter card would be SC-017's to reopen, not this theory's.
- **A rise in the cross-sectional dispersion of expected returns in rebalancing periods**: a
  dispersion is a measure, not a position; it becomes one only once it is known which assets gain.
  It could be reported beside a card of FP-023's, whose rebalancing dates it would share.
- **Batching seen in volume**: the snapshot's files hold the funds' traded volumes, but the lab
  passes a strategy its closes only, and a fund's volume is its own shares changing hands, not the
  rebalancers' orders in the stocks and bonds it holds; a volume rise at month-ends would not tell
  rebalancers from the other month-end flows SC-012 names, and McConnell and Xu found NYSE volume no
  help to the payday hypothesis either.

What would make it testable: holdings or trading data of rebalancing investors — balanced, pension
and target-date funds' allocations over time, or dated order flows — beside the prices; a new kind
of data, and a decision for the lab's framing, not for a card. Its sources, added to the library,
might fix a sign for recurrence at the same point of the month, the one form that is this theory's
own; at a daily phase that form would still meet gate 6's delay. A sign for month-end pressure would
be FP-023's.

## Status

SC-013 is recorded `not-testable`. Its prediction leaves the sign of the autocorrelation open, and
the forms of it that carry a sign in the library are other theories' claims: SC-021 and SC-023
(recurrence over the same period), FP-023 and FP-018 (month-end and quarter-end pressure), TM-017
(monthly and quarterly autocorrelation), SC-017 (calendar-year rebalancing into equities, a
first-quarter card being its to reopen) and FP-015 (leveraged funds' daily rebalancing). The form
that is its own, recurrence at the same point of the month, has no sign in the library at any phase
of the month; at a daily phase it also fails gate 6's delay, and at a weekly phase its only sign is
SC-023's. What it claims beyond them — that the patterns come from orders batched at rebalancing
dates — needs holdings or trading data the lab does not hold. No card is drawn, and no trial is
spent.
