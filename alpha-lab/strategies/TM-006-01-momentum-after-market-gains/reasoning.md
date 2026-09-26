# TM-006-01 — Momentum after market gains: reasoning

## Why this theory now

TM-006 is Daniel, Hirshleifer and Subrahmanyam's model: investors overconfident about the precision
of their private information, whose confidence rises when public news confirms their trades more
than it falls when news contradicts them, push prices too far in the direction of their signal and
keep pushing as confirming news arrives, before public information pulls prices back. Returns are
positively autocorrelated in the short run and negatively in the long run. Its refutations: no
positive autocorrelation under six months, or no later reversal; momentum fully explained by the
slow incorporation of information, with no overshooting later corrected; traders whose confidence
does not rise after successes more than it falls after failures, or whose rising confidence brings
no further trading in the same direction.

**Its sources, as the lab read them in the library's books.**

- **Daniel, Hirshleifer and Subrahmanyam**, "Investor psychology and security market under- and
  overreaction", in *Advances in Behavioral Finance, Volume II* (Thaler, ed., 2005, chapter 13),
  which Barberis and Thaler's survey in the same volume (chapter 1) summarises. With confidence
  fixed (their Propositions 1 to 3), prices overreact to private signals and underreact to public
  ones, price moves on private information are partly reversed in the long run, and overconfidence
  adds volatility around private signals. With confidence moved by self-attribution (Proposition 7
  and their simulations), the average price after a favourable private signal rises and then falls;
  short-lag autocorrelations are positive and long-lag ones negative, and momentum is then a
  continuing overreaction rather than a slow reaction. Their stated empirical implications, "either
  untested or ... tested only on a subset of possible events", concern firm events — the drift after
  events a firm chooses and none after events it does not, the correlation of an event's size and
  date return with what follows, the run-up before it — and "greater average long-term reversal of
  price moves occurring on dates when there are no public news events about a firm". Overvaluation
  "may be measured by recent increases in firm, industry or aggregate stock market prices".
  Mispricing and momentum should be stronger in firms that are hard to value, and in small, illiquid
  securities. Across cultures, momentum is strong in the United States and Europe and weak in Japan,
  where studies find essentially no self-enhancing attribution; they predict it weak in other Asian
  markets.
- **Confidence after the market's gains**: Gervais and Odean, in the survey, have investors who
  succeed grow more confident; Statman, Thorley and Vorkink, in Shefrin's *A Behavioral Approach to
  Asset Pricing* (2008), find turnover rising after the market has gone up and read it as evidence
  of overconfidence, and the rise after a security's own gains as the disposition effect.
- **Momentum by the market's state**: Ilmanen (*Expected Returns*, 2011, chapter 14, the notes on
  momentum in stock selection): "Momentum profits appear to be larger after market gains and when
  investors are optimistic. Positive sentiment can accentuate overconfidence among stock-pickers,
  which (with short-selling constraints) leads to upward momentum (and later reversals). Momentum
  profits are lower after market losses, turning points, and periods of heightened volatility".
  Shefrin (*Beyond Greed and Fear*) reports Cooper, Gutierrez and Hameed's finding "that momentum
  profits exclusively follow market gains and that contrarian profits are stronger following market
  losses". The Zacks *Handbook of Equity Market Anomalies* (2011) reports Huang (2006), momentum
  among the broad indices of seventeen countries "but only in up markets", with no definition of the
  market's state, and Chordia and Shivakumar, momentum profits positive only in expansions, as a
  business-cycle explanation. Ang (*Asset Management*, 2014, chapter 7) puts momentum's dependence
  on the state of the stock market among its macroeconomic, rational explanations. The library gives
  none of these a window for the market's state, nor a size.
- **Against it**: Ilmanen (*Investing Amid Low Expected Returns*, 2022) writes that stock-selection
  momentum "tended to perform well during these major bear markets", with crashes just after the
  turn, as in spring 2009, and that there is "little evidence to suggest momentum and trend can be
  profitably timed".

**The form this card tests.** The market's state is the one prediction tied to overconfidence that
reads prices alone: after the market has risen, confidence is high and momentum strong; after it
has fallen, confidence has fallen and momentum is weak, absent or reversed. The bank's refutation —
confidence that does not rise after successes more than it falls after failures — reads, in prices,
as a consequence of it: momentum stronger after the market's gains than after its losses, which the
model with biased self-attribution predicts once confidence is aggregated over the market; the
asymmetry itself is not read. The direction is shared by rivals — the crashes of TM-024, the
business cycle, a rational story — so a clause that does not refute cannot favour TM-006 over them;
one that refutes counts against all of them in this form.

- **TM-024-01** switched CA-001-01's momentum tilt off in a group's *panic* states, Daniel and
  Moskowitz's crash forecast: the group's market down over the past two years *and* its volatility
  above its own average — 41 of 609 group-months, 7%. Those are down states of this card, on the
  same markets and the same 504 sessions, and their outcome is published (below); the down state
  without the panic was never switched, nor graded, and TM-024's claim is the crash in the joint
  state. This card grades the down states outside the panic ones, and leaves those out.
- **TM-037**, investor sentiment and momentum, conditions momentum on sentiment proxies that are not
  prices — issues, closed-end fund discounts, turnover, flows; Ilmanen's "when investors are
  optimistic" is its claim, his "after market gains" this card's.

**What the lab already knows, and is not blind to** — estimates, not the sample's figures (the
runbook's step 3):

- **CA-001-01**, the unmanaged rule: an alpha of 0.20% a year over the nineteen funds in equal
  parts, its bets hedged of the benchmark moving by about 6% a year; its block alphas negative in
  2005–07, 2008–09 and 2015–19 and positive in 2010–14 and 2020–22, its best year 2022; by group, an
  appraisal ratio of +0.19 among the equity markets, 0.00 among the commodities and −0.07 among the
  sectors.
- **TM-024-01**: the panic switch left the alpha at 0.09% a year, 0.11% below CA-001-01's (standard
  error 0.46%). Its 41 panic group-months: the sectors from October 2008 to November 2009, July to
  September 2010 and April 2020; the equity markets from October 2008 to September 2009, August and
  September 2010, April and May 2020 and October 2022; the commodities in December 2008, August to
  October 2013 and April and May 2020. Before hedging, switching the tilt off there returned 0.37% a
  year more than CA-001-01, about 6.2 points (+7.7 in 2009, −3.4 in late 2008, −0.6 in 2010, −0.8
  in 2022, +1.1 in 2013, +2.2 in 2020): the tilt lost there on the whole, in the prediction's
  direction. Hedged, the gain was the market's: the beta rose from 0.95 to 1.01. The two-year bear
  indicator turns late in a decline — from about October 2008 for the equity groups, as TM-024-01's
  reasoning expected and its panic months confirm.
- **TM-039-01** measured CA-001-01's tilt by its group's dispersion state: after dispersed months
  −2.36% a year (1.83%) among the sectors, −1.17% (0.58%) among the equity markets, −0.51% (0.92%)
  among the commodities; after the others +0.70% (1.02%), +1.21% (0.46%), +0.37% (0.66%); by one
  state for all nineteen funds, CA-001-01's alpha was −4.26% a year after dispersed months against
  +3.00% after the others. Dispersed months and down states likely overlap, in 2008–09 and perhaps
  2022.
- **TM-001-01** reported, between asset classes and not graded, the leaders' gap to the seven funds
  in the months after the seven had fallen over the past year, −5.93% a year (9.33%, 43 months),
  against +3.85% (3.12%) in the others.
- **Known episodes**, a judgment from the markets' history: the rebound of March to December 2009,
  after the equity groups' two-year losses, when past losers led; the commodities' long fall from
  2011 and 2013 to 2016, when the commodity group's market was likely down over two years for long
  spans, and perhaps again in 2019–20.

**The form was chosen knowing these results.** TM-001-01's, TM-024-01's and TM-039-01's, on the same
years and on funds this card holds, all lean the claim's way; the reason given below for not drawing
the between-class form applies to this one in part. The card handles it by grading only the down
states TM-024-01 did not read, and by what its clause can do, which is refute: a clause that does
not refute is weak evidence for TM-006, the lab's own results having made that outcome likely
before the lock.

**The bank's siblings.** **TM-005**, Barberis, Shleifer and Vishny's model, recorded not testable as
a theory of its own; **TM-036**, extrapolative expectations; **TM-008**, gradual information
diffusion, which predicts the same continuation and, through its momentum traders, an overshoot too
— slow incorporation with no overshoot is the reading of **TM-007**'s underreaction; **TM-024**,
momentum's crashes; **TM-037**, sentiment; **TM-039**, dispersion.

## From the claim to a signal

- **The momentum**: CA-001-01's, unchanged — within each of three groups (the eleven sector funds;
  SPY, QQQ, IWM, EFA and EEM; GLD, SLV and DBC), the top third by the return from 252 to 21 sessions
  before the session before the target, the group's n/N shared among its leaders, a fund trading but
  not yet ranked at 1/N. Its tilt is those weights less the group held in equal parts, 1/N for each
  fund trading. Holding the momentum fixed makes the market's state the only change, and lets the
  rule be compared with CA-001-01 and TM-024-01 over the same sessions.
- **The state**: each group's market is the average of the daily returns of its funds trading on
  each session, chained, TM-024-01's measure; the group is in a *down state* when its market, read
  on the session before the target, is below its level `bear_window` sessions earlier. The base is
  504 sessions, two years: the library gives no window for the market's state; the lab's one
  precedent is TM-024-01's two years, Daniel and Moskowitz's bear-market indicator as TM-024-01 read
  it, and the card keeps it, so that it differs from TM-024-01's base only by leaving out the
  volatility condition. Each group reads its own market, as Daniel and Moskowitz compute their
  indicator for each asset class from that class's market, and as TM-024-01 did. Neighbours: 378 and
  630, 252 and 756.
- **The rule**: each group holds its funds in equal parts plus k times its tilt, k = 0 in a down
  state and 1 otherwise, including while the group's market has not `bear_window` sessions of
  history; targets on the first session of each month from the first on which a fund is ranked,
  fully invested, read up to the session before. The rule switches in every down state, the panic
  ones included; only the clause leaves those out. One variant: the library gives the window no
  alternative, and gate 6 moves it by a quarter and a half either way.
- **Memory**: 504 sessions, the state's window, declared on the card.

## What the battery judges, and what to expect

**The size predicted — a judgment.** The library gives the direction — momentum stronger after
gains, weak or absent after losses, contrarian profits stronger after losses — and no size. The card
judges the leaders' gap to their group's ranked funds, over the month after each target, at about 1
to 5% a year lower in the down states than in the others: CA-001-01's long-only top third, whose gap
to its groups CA-001-01's verdict could not tell from zero, shrinks the sources' long-short
differences, and a momentum that is absent or reversed after losses and modest after gains leaves a
difference of that order. For the rule, the raw return rises over CA-001-01's by the tilt's loss in
the down states: if about a fifth of the group-months are down states (a judgment from the markets'
history, not a count of the signal) and the tilt's gap there is 0 to −3% a year, about 0 to +0.6% a
year. But switching the tilt off restores market exposure, which the regression charges as beta —
TM-024-01's +0.37% raw became −0.11% of alpha on only 7% of the group-months — so the rule's alpha
over CA-001-01's is judged at about −0.8 to +0.4% a year, of uncertain sign.

**The gates.** The rule is CA-001-01 in about four group-months of five, and the card expects it to
fail gate 2 (CA-001-01's Sharpe ratio was 0.44 against the benchmark's 0.46), gate 3 (CA-001-01
beat 47.6% of its placebos, TM-024-01 52.3%), gate 4 (the best of some fifty effective trials
reaches an appraisal ratio of about 0.63 by luck) and gate 5 with them. Gate 4's clusters of
near-clone trials may count it with CA-001-01 and TM-024-01 as one.

**The clause.** Judged before costs, on the market's closes, over the in-sample months from the
first target on which a group's state is known, each group-month from the close of the month's first
session to the close of the next month's first session, the last ending at the close of 2022-12-30,
over the group-months with two ranked funds or more: the return of the group's leaders — CA-001-01's
top third of the group's ranked funds, bought in equal parts at the first session's close and held —
less the return of all the group's ranked funds bought and held the same way, the tilt's own
comparison. The down set is the group-months in a down state other than TM-024-01's 41 panic
group-months, which are left out; the others are the group-months not in a down state. The
coefficient on the down-set indicator in an ordinary least-squares regression of the gaps on that
indicator and one constant for each group — the groups' gaps differ, and their down states fall in
different years — its standard error clustered by calendar month, since the groups' down months
coincide and their gaps move together, and its t statistic, computed apart from the battery. The
theory is refuted in this form if that t statistic is +0.35 or above: momentum no weaker after the
market's losses than after its gains, outside the panic states. Below it, short of passing gates 1
to 7, it is not proven, not refuted; a base that passes gates 1 to 7 while the clause refutes leaves
the theory refuted in this form.

**The test's power.** The group markets start on 2005-01-04, so a state is first known for the
target of 2007-02-01: about 191 months in each of three groups, about 573 group-months; if about a
fifth are down states (a judgment), about 115, of which TM-024-01's 41 are left out, leaving about
75 against about 460. A group's leaders move against the group's ranked funds by about 5.5% a year
among the equity markets, 6 to 8% among the sectors and 12 to 15% among the commodities, about 9%
pooled — derived from TM-039-01's published standard errors, each scaled by the square root of its
months over twelve, then divided by the group's share of the portfolio —: a standard error of about
3.9% a year on the difference, more with the clustering. The clause refutes about 36% of the time
with no effect, more if the clustering is too weak, and about 13% at −3% a year, the middle of the
range. It cannot tell an effect of the predicted size from none.

**TM-006's refutations, and what the card can grade.**

1. *No positive autocorrelation under six months, or no later reversal*: the continuation is read by
   TM-017-01, CA-001-01, TM-003-01 and TM-001-01; the reversal is **MR-021**'s claim, long-term
   overreaction and reversal, read as value within groups by **CA-024-01** (the cheapest third by
   the past five years, 0.63% a year below the groups from 2010 to 2022, stopped at gate 2, not
   refuted, not proven).
2. *Momentum explained by slow incorporation, with no overshoot*: on closes the overshoot shows only
   as the later reversal, MR-021's.
3. *Confidence that does not rise after successes more than it falls after failures*: graded, in
   prices, through its consequence by the clause — momentum no weaker after the market's losses than
   after its gains; the asymmetry itself is not read. *Rising confidence that brings no further
   trading*: turnover, which the lab does not pass a strategy (below).

**Measures stated before the run**, reported, not graded:

- the same regression over every down-state group-month, and over the 41 panic group-months alone
  against the others;
- the gap by group, and the number of down-set group-months in each;
- the gap hedged of its group's market, with one beta for each state, to tell leaders that are
  defensive in a rebound from a momentum that is weaker;
- the unmanaged tilt's contribution to the portfolio in down and in other group-months;
- the managed rule against CA-001-01 and against TM-024-01, by `lab.compare`: the alpha's difference
  and its standard error on the monthly differences; and the difference with each rule's beta
  allowed to differ in the months in which any group is in a down state;
- the clause over 2007–2013 and 2014–2022, without the months whose target falls in 2009, and over
  the holdout, 2023 to 2025;
- the alpha before and after costs, the neighbours' and the one-day-late rule's alphas and
  appraisal ratios.

## What was considered, and why each is set aside

- **Recording TM-006 not testable**: a first draft did, reading the market's state as TM-024-01's;
  TM-024-01 switched only in the joint panic state, and the down state alone, with its sign in
  Ilmanen, Shefrin, Zacks and Ang, was not graded.
- **Grading every down state**: a third of them are TM-024-01's panic group-months, whose outcome is
  published and in the prediction's direction; they are reported apart.
- **Grading the rule's alpha difference from CA-001-01**: it mixes the claim with the beta the
  switch restores (TM-024-01, TM-039-01); reported.
- **One market for all groups** — the nineteen funds, or SPY: the commodities' momentum would then
  be switched by the equity market; each group's own market is Daniel and Moskowitz's form as
  TM-024-01 read it.
- **The state as the past year, or three years**: the library gives no window; gate 6 moves the two
  years to one and three.
- **Between asset classes**, TM-001-01's leaders switched off after the seven fell: its split was
  reported after its run, and a card built on it would choose its form from a published result on
  the same years; the form drawn here was chosen knowing the same result and TM-024-01's and
  TM-039-01's, and differs from them in universe, window or state, not in years.
- **The whole sequence on one ranking**, continuation then reversal: the reversal is MR-021's.
- **Volume**: turnover after gains is a claim about trading, not returns; the snapshot's files hold
  the funds' volumes, but the lab passes a strategy its closes only (SC-013-01, SC-015-01). Momentum
  conditioned on turnover (Lee and Swaminathan, in Jegadeesh and Titman's chapter and the Zacks
  handbook) is **TM-027**'s claim, and its opposite **TM-028**'s.
- **Hard-to-value and small securities**: the lab holds no book values, research spending, analyst
  coverage or spreads; small caps are **TM-041**'s, coverage **TM-025**'s and **TM-008**'s; momentum
  with value was read by **TM-040-01** (stopped at gate 2, not proven); price ratios are
  **EF-008**'s and **EF-009**'s. Fund-level analogues, such as trend in technology against
  utilities, have no sign in the library.
- **Culture**: the prediction reads stocks ranked within each country, which a country's index fund
  cannot. The library is divided on Asia: the Zacks handbook reports Chui, Titman and Wei finding
  momentum in every Asian market they study but Japan, while Jegadeesh and Titman's chapter reports
  them finding it not reliably greater than zero there, and Griffin, Ji and Martin not significant
  in Asia. Country-index momentum is **CA-017**'s.
- **The firm events and the reversal of moves without news**: firm events and news dates, which the
  lab does not hold (SC-011-01 found the same of macroeconomic release dates); the post-earnings
  drift is **EF-035**'s, issues **AS-005**'s, **EF-027**'s and **EF-028**'s, repurchases
  **EF-029**'s, analysts' revisions **EF-034**'s, and the general drift **TM-007**'s.
- **Crypto-assets**: the source reads none, the library gives bitcoin's trend no sign (TM-005-01),
  and a card of one asset is not drawn.
- **Scaling k by the size of the market's gain**: the library gives the state, not a slope.

## Implementation

Long only, the nineteen funds in their groups, with European (UCITS) funds that track them; one
decision a month, the signal read up to the session before and traded at the close, a day's delay;
the rule departs from CA-001-01 only in the months a group's market is down over two years.
