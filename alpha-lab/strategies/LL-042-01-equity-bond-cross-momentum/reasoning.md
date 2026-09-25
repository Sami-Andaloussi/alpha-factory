# LL-042-01 — Cross-asset momentum between equities and Treasuries: reasoning

## Why this theory now

LL-042 claims that one asset class's past returns predict another's, because capital and
information move between markets at different speeds: the classic example is the delayed
reallocation between equities and bonds. Its prediction names three channels: past equity returns
predicting corporate bond returns, lags between currencies and bonds, and lags between the equity
indices of different countries.

The lab can test one of them faithfully, and now can: the Treasury funds the universe gained before
the first card give it, beside its equity indices, the second market this theory needs. It holds no
corporate bond fund and trades no currency, and its universe was fixed before the first card; the
firm-level spillover from a company's stock to its own bonds, the strongest evidence for the first
channel, needs data the lab does not have. The country channel is LL-017's theory, cross-country
information diffusion, a card of its own. For equity indices and government bonds, the cross-asset
evidence is direct: Pitkäjärvi, Suominen and Vaittinen (2020, Journal of Financial Economics 136(1),
63–85), over 20 developed countries from 1980 to 2015, find that past bond market returns predict
future equity market returns positively, and past equity market returns predict future bond market
returns negatively — "cross-asset time series momentum" — and attribute both to slow-moving capital
in the two markets. This card tests that channel; its result speaks for the Treasury channel only.
The corporate and currency channels stay untested, and the verdict will say so beside the theory's
status.

The sign differs from the corporate channel's, and does not contradict it: good news for growth
lifts corporate bonds, whose default risk falls, and lowers Treasuries, whose yields rise with it.

The bank's neighbours: **TM-017**, time-series momentum, reads each asset's own past return only;
TM-017-01 tested it on seven funds and stopped at gate 3. **LL-017**, cross-country diffusion, and
**LL-034**, credit to equity, are other channels. This card differs from TM-017 by the other market's
signal, and from LL-017 because every equity fund here reads a bond, never another equity market.

## From the mechanism to a signal

The two legs test the two directions the sources find:

- **Bonds leading equities.** A year of rising bond prices — falling yields — has still to reach
  equity prices: the capital that would reprice equities for lower discount rates and easier
  financing moves slowly. The equity legs read the bond market's past year.
- **Equities leading bonds.** A year of rising equities has still to reach bonds, whose prices then
  fall as the capital that fled to them in weaker times returns slowly to risk. This is LL-042's own
  ordering, equities first; the bond legs read the equity market's past year, and are held only in
  the rare years when US equities trend down.

- **The rule** is the sources' cross-asset time-series momentum in its long legs: an equity index is
  held when its own past year's return and the bond market's are both positive; the bond is held
  when its own past year's return is positive and the equity market's is negative; when the two
  signs point different ways, the sources take no position. The short legs are dropped: the lab is
  long only.
- **The past return** is over 252 sessions, read up to the session before, in excess of the Treasury
  bill over the same sessions: the sources' twelve-month lookback on returns in excess of the bill.
  Their one-month holding becomes a decision on the first session of each month.
- **The markets.** The sources pair each country's equity index with its own government bond, of five
  years' constant maturity. The lab has one bond market, the US one. **SPY, QQQ and IWM**, the lab's
  three US equity indices, are paired with it, as the sources would pair them; **EFA and EEM** are
  paired with it too — a departure, since their own bond markets are not in the lab, resting on a
  judgement, not a source: that US yields move most bond markets. The bond whose past return is the
  signal is **IEF**, seven to ten years, the lab's nearest fund to the sources' five-year bond (SHY's
  return over cash is too small for its sign to mean much). The bonds held are **IEF and TLT**, each
  on its own past return and on SPY's.
- **Equal shares**: each of the seven funds held takes a seventh of the portfolio; a fund not held
  leaves its seventh in cash, as in TM-017-01, so that the two rules differ only by the other
  market's signal. All five of the lab's equity indices are in the universe: the sources hold one
  index per country, and the lab's US market has three; with three equity funds only, the largest
  would carry at least a third of what the bonds do not, above gate 6's limit of 30% of the profit
  on one asset, whatever the edge. QQQ may carry the largest share among the seven.

**The variant** isolates the lead and lag: under the rule "cross", an equity index is held when IEF's
past year is positive, whatever its own; a bond when SPY's past year is negative, whatever its own.
It is the pure form of the predictability the sources document, before its combination with each
asset's own trend. Two variants, not three.

## What the battery judges, and what to expect

The benchmark holds the seven funds in equal parts, set back to equal parts whenever the strategy
trades: the alpha is what the timing adds to holding the seven always.

**The size predicted.** The sources' portfolio diversified over 20 countries earns a Sharpe ratio 45%
higher than the standard time-series momentum portfolio on the same markets; on the lab's funds,
the own-trend rule, TM-017-01, earned 0.495 in-sample, and 0.495 × 1.45 is about 0.72. But the
sources' gain comes from diversifying across countries, and for the United States they report the
improvement as modest; the lab has one bond market and its long legs only. The card therefore
predicts a Sharpe ratio of about 0.55 in-sample and a positive alpha over the seven held always: a
judgement scaled from a 20-country long-short result, not a figure the sources give for this form.

**What each figure can tell.** A positive alpha could come from the funds' own trends alone, which
TM-017-01 already found. The verdict will therefore report, beside the battery, the own-trend rule
on the same seven funds and days, computed apart from it; and the variant "cross", which reads no
fund's own trend, is the battery's own test of the lead and lag.

**The test's power.** Seven funds, the five equity funds reading one bond signal under the rule
"cross" and that signal beside their own under "both", decided monthly: no more
independent bets than TM-017-01, which gate 3 judged too few at 81.7% of its placebos. The bond legs
are held only when US equities trend down, a few episodes in seventeen years, and add few
decisions. Gate 1 needs 30 clustered decisions; its figure is not measured before the card is
committed. The verdict will say how many independent decisions the rule made, and what gates 3 and
4 could detect with that many.

**Gate 6.** It leaves each cluster out in turn by making its funds untradable, their prices still
read: without the bonds, the equity legs keep their signal; without the equity indices, the bond
legs keep theirs, but trade only in the rare years they are held, so that the Sharpe ratio kept may
fall below half. Gate 6 then fails, and the card counts such a result as not proven.

## Choices, and the options rejected

- **The firm-level stock-to-bond spillover and the currency channel**: not testable on the lab's
  data, as above.
- **Treasury maturities as separate bond markets**: IEF and TLT are one market; the signal is
  IEF's.
- **SHY** as a fund held: its return over cash is too small for its trend to mean anything, as
  TM-017-01's reasoning said.
- **Volatility scaling of the positions**, as the sources scale their portfolios to a volatility of
  10%: it is TM-047's hypothesis, tested apart.
- **The short legs**: the lab is long only.

## Implementation

Long only, seven funds, each with a European (UCITS) fund that tracks it, rebalanced monthly on
closes with the orders filled at the next close: the signals read the session before, so a day of
delay is built in, and gate 6 adds another.
