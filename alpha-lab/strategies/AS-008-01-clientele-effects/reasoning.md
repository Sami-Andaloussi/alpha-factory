# AS-008-01 — Clientele effects: reasoning, not testable as a theory of its own

## The theory, and the forms its sources give it

AS-008 holds that investors differ in taxes, income needs and mandates, so that each stock draws a
clientele according to its payout policy, the stability of its payout and sometimes its legal
structure, and that the prices of the firms and sub-universes concerned show recurring behaviour
tied to those clienteles, the more so when the differences between investor types are large and
rotating a shareholder base is costly. Its refutations: a shareholder base that does not vary with
payout policy; no recurring price behaviour tied to the clientele; an effect no weaker where the
differences between investors or the costs of rotation are small. The bank names stocks, months and
years, and dividend payments, payout ratios, institutional holdings and daily prices.

**Its sources, as the lab read them in the library.**

- **Baker, ed.** (*Dividends and Dividend Policy*, 2009), chapter 6, "Dividend Irrelevance Theory",
  section "Clientele Effects": Miller and Modigliani (1961) grant that a firm may draw holders who
  like its payout, and deny that this changes its value; clienteles may be psychological (Shefrin
  and Statman, 1984) or tax-driven (Allen, Bernardo and Welch, 2000). Chapter 13 gives Baker and
  Wurgler's catering theory.
- **The same book, chapter 8, "Taxes and Clientele Effects"**: tax clienteles are tested through a
  variant of the CAPM or through the price on the ex-dividend day, with no consensus. The ex-day
  fall of the price has been found a little smaller than the dividend since Campbell and Beranek
  (1955); Elton and Gruber (1970) read the ratio of fall to dividend as the marginal long-term
  holder's relative tax on dividends and capital gains, and with Elton, Gruber and Rentzler (1984)
  find high-bracket investors preferring low yields. Kalay (1982) reads it as short-term traders'
  arbitrage; Miller and Scholes (1982) warn against reading short-run yield-return links as tax
  clienteles; Bali and Hite (1998) and Frank and Jagannathan (1998) read it as tick size and bid-ask
  bounce, which Graham, Michaely and Roberts (2003) find inconsistent with the ex-day after
  decimalisation. The sign, a fall smaller than the dividend on taxable dividends, is common to the
  rival causes; Elton, Gruber and Blake (2005) find it reversed on funds whose dividends were
  tax-advantaged. The chapter adds that the US taxes dividends and capital gains at the same rate
  "as is currently the case", when the tax clientele predicts indifference.
- **Chapter 10**: volume around dividend initiations (Richardson, Sefcik and Thompson, 1986) rises
  in the announcement week and barely until the ex-date, which they read as against a clientele
  shift. **Chapter 11**: older, retired and low-income households demand dividends and are net
  buyers of stocks before ex-dates (Graham and Kumar, 2006), on single stocks.
- **Harris** (*Trading and Exchanges*, 2003, chapter 8, "Dividend Capture"): Americans do little
  dividend capture, since dividends and short-term gains are taxed alike for most.

## What the lab can read of it

The lab holds the daily bars and volumes of twenty-two funds and bitcoin — the funds from 2005 or
their later start, bitcoin from September 2014 — adjusted for dividends and splits, with the
Treasury bill's yield; no single stock, no payout ratio and no holdings; its snapshot is closed, an
asset or a series being added only before the first card. The adjusted bars nonetheless encode each
fund's distributions: one scale factor a day turns a fund's open, high, low and close back into
whole cents, and it steps on each ex-date by the distribution over the price before it (SPY by about
0.4% on 2005-03-18, a third Friday; checked on dates and step sizes alone, no return read). On those
data:

- **The shareholder base by payout policy**, the claim and its first refutation: holdings by
  investor type are not held.
- **The ex-dividend day**, the one price test of tax clienteles the library gives: the funds'
  ex-dates and amounts are recoverable, and a fund's adjusted return over the ex-day is positive
  exactly when its price falls by less than the distribution, the theory's sign. But the premium is
  earned over one session, from the close before the ex-date to the ex-date's close, and gate 6's
  day of delay removes it by construction: like SC-011-01's one-day rule, the form is certain to
  fail a gate whatever the prices (RUNBOOK step 9), and no card is drawn for it. The library signs
  no wider window, and one wide enough to survive the delay would be a width the lab chose. It would
  also be confounded: SPY's and the sector funds' ex-dates fall in the week of the quarter's option
  expiry and rebalancing (SC-012, FP-012), the Treasury funds' on the month's first session, the
  turn of the month SC-008-01 and SC-009-01 read. And in the lab's years the tax clientele gives the
  equity funds' qualified dividends no sign, the rates being equal.
- **Sub-universes by payout, the income clientele's funds (XLU, XLP) against the others**: the
  library ties older and low-income households to utility stocks and to buying before ex-dates, on
  single stocks, and signs no return for a sector fund tied to its clientele; the sectors'
  differences across rates and the cycle are **CA-011**'s, **CA-012**'s and **CA-013**'s. The
  Baker–Wurgler seesaw on funds, XLU or XLP by sentiment state, TM-037-01's reasoning left for a
  later card and its verdict declined, as a trial chosen from its result; the dividend premium is
  one of the six measures of its composite, which TM-037's card recorded that the lab does not hold.
- **Yield as a predictor or a carry**: the payout yield is **EF-030**'s, the dividend yield
  predicting aggregate returns **MR-044**'s, yield as equity carry **CA-025**'s, managers reaching
  for yield **FP-036**'s; the funds' trailing distribution yields are recoverable from the bars,
  which those theories' picks must know.
- **Dividend signalling and the payout's life cycle**: **AS-012**'s and **AS-013**'s. **The tax
  calendar at the year's end**: **FP-026**'s and SC-002-01's.

**The bank's siblings.** **AS-012**, dividend signalling; **AS-013**, the firm's life cycle and
dividends; **EF-030**, net payout yield; **EF-029**, share repurchases; **MR-044**, countercyclical
expected returns; **CA-025**, carry; **CA-011** and **CA-013**, sector rotation; **FP-036**,
correlated factor bets; **FP-026**, tax-loss selling; **MR-026**, closed-end fund discounts;
**FP-012**, index rebalancing; **CA-023**, fundamental indexation; all untouched; **TM-037**,
investor sentiment, and **SC-008**, **SC-009** and **SC-002**, tested inconclusive; **CA-012**,
**SC-011** and **SC-012**, recorded not testable.

**What was considered, and why it does not rescue a card:**

- **The funds' ex-days, read from the bars**: a one-session position that gate 6's delay fails by
  construction; a wider window unsigned, confounded with expiry and the turn of the month; no tax
  sign for the equity funds in the lab's years. Locating ex-dates from volume spikes instead would
  read the effect from the data it is meant to test.
- **Utilities (XLU) and consumer staples (XLP) against technology (XLK), as the income clientele's
  funds**: no sign in the library for their returns tied to the clientele.

What would make it testable: holdings by investor type, with dividend policies, for single stocks —
outside the lab's funds — or a sign in the library for a window around the ex-day wider than a
session.

## Status

AS-008 is recorded `not-testable`: its claim and first refutation read shareholder bases by investor
type, which the lab does not hold; its one price test, the ex-dividend day, is readable from the
funds' adjusted bars but is a one-session position that gate 6's delay fails by construction, with
no wider window signed and no tax sign for the equity funds in the lab's years; the sector forms and
the yield forms are other theories', which must know the funds' distributions are recoverable. No
card is drawn, and no trial is spent.
