# AS-037-01 — Asset-collateralised stablecoins: reasoning, not testable as a theory of its own

## The theory, and the forms its sources give it

AS-037 holds that an asset-collateralised stablecoin owes its price behaviour to the credibility of
a stock of external reserves — cash, commodities or securities held off-chain — through the promise
of redemption, the legal quality of the claim, the frequency of audits and the capacity to redeem
under stress; arbitrage is not frictionless, since access to redemption is unequal and information
on the reserve opaque or delayed, so that a stablecoin with an opaque or politically vulnerable
reserve behaves less like tokenised cash and more like a claim on an intermediary. Its refutations:
the stablecoin's price not reacting to news about its reserves, audits or redemption terms, in calm
or under stress; any gap closed at once by arbitrage whatever the access and the opacity;
stablecoins with opaque reserves trading exactly like those with transparent, audited ones. The bank
names crypto, over days and weeks, and stablecoin prices, reserve attestations, issuance and
redemptions; its references are Voshmgir's *Token Economy*, whose second edition (2020) is the one
the library holds, not the third the bank names, Schianchi and Mantovi's *The Economics of
Cryptocurrencies and Digital Money* (2023; the bank says 2024) and Caton's edited *The Economics of
Blockchain and Cryptocurrency* (2022).

**Its sources, as the lab read them in the library.**

- **Voshmgir** (*Token Economy*, second edition, 2020):
  - Part 3, "Asset-Collateralized Stable Tokens": tokens backed by off-chain assets — Tether and
    TrueUSD by dollars, Digix by gold — easy to build but centralised, trust placed in a single
    custodian and exposed to its counterparty risk; Tether never fully audited, its terms changed to
    admit loans among its reserves and its counsel admitting that 74% was backed by cash and
    equivalents, while TrueUSD and Digix publish audits — the theory's opacity contrast, told with
    no price.
  - The Annex, "Libra & Celo": Libra as a plain asset-collateralised token, issued and burned
    against demand, its reserve to be held in low-risk assets.
- **Schianchi and Mantovi** (*The Economics of Cryptocurrencies and Digital Money*, 2023):
  - Section 5.3: reserve-backed stablecoins as a kind of narrow banking, Tether and USD Coin found
    improperly collateralised, and Tether fined $41 million by the Commodity Futures Trading
    Commission.
  - Section 5.3.2: redemption terms — notice periods and fees — as the gauge of a coin's moneyness,
    Tether in June 2021 charging 1% with a $1,000 minimum and a $150 verification fee (Gorton and
    Zhang, 2023); and only a government guarantee truly preventing runs on stablecoins (Allen,
    section 5.3.1).
  - Section 5.2.1: Libra announced in June 2019 as a stablecoin fully backed by cash and liquid
    assets, and its successor Diem selling its assets in January 2022.
  - Section 6.1:
    - Tether declared fully backed by dollars from 2014 until February 2019;
    - Tether not backed one to one from 1 June to 15 September 2017, without telling its clients;
    - Crypto Capital holding over a billion dollars of Bitfinex's clients' funds by mid-2018, and a
      freeze of those funds, undated, causing a liquidity crisis and delayed withdrawals — the
      capacity to redeem under stress;
    - a New York prosecution from April 2019, settled for $18.5 million.
  - Section 6.3: the free-banking era from 1837, when banknotes meant to be worth a dollar traded at
    discounts that varied with the perceived riskiness of the issuing bank, and money-market funds
    from the late 1970s as deposit-like claims (Gorton and Zhang, 2023) — the theory's claim with
    its sign, a past episode long before the lab's years, on notes the lab does not hold.
- **Glasner** (chapter 3 in Caton, ed., *The Economics of Blockchain and Cryptocurrency*, 2022,
  section 7): Tether's peg kept by an undisclosed mechanism, with Bitfinex repeatedly accused of
  misconduct — an untimed claim.
- **Burns** (chapter 5 in Caton, ed., section 2): dollar-pegged stablecoins such as Tether, USD Coin
  and BUSD offered to Africans as a more reliable store of value than their currencies, a
  market-driven move towards dollarisation — an untimed claim on currencies the lab does not hold.

**Return signs near the theory.**

- **Harvey, Ramachandran and Santoro** (*DeFi and the Future of Finance*, 2021):
  - Chapter III, "DeFi Infrastructure", section "Stablecoins": fiat-collateralised stablecoins as
    the largest class, Tether the largest and not audited — its one-time attestation of 30 March
    2021 in the chapter's note 6 — and USD Coin audited and redeemable one to one without fee on
    Coinbase, both centrally controlled and able to blacklist accounts.
  - Chapter VI: arbitrageurs buying USD Coin at a discount and redeeming it at a dollar, a strategy
    sure as long as Coinbase stays solvent — the redemption-anchored arbitrage of the second
    refutation.
  - These are untimed claims, with no price.
- **Huang and others** (*Web3*, 2024):
  - Sections 6.2.3 and 6.2.5: fiat-backed and gold-backed tokens.
  - Section 10.4: regulation to require proof of reserves, regular audits and deposit insurance
    against runs.
  - Section 10.4.2: the act introduced on 7 June 2022 requiring reserves of 100% in liquid assets,
    disclosure and redemption at par, reintroduced in July 2023.
  - Section 10.5.1: the European Central Bank's view that stablecoins lost their perceived
    stability.
  - Section 10.8: the Federal Reserve's report of 9 May 2022 calling stablecoins prone to runs and
    unclear about their assets; a draft bill of April 2023 requiring insured issuers and sufficient
    reserves; Japan lifting its ban on foreign stablecoins in 2023; and the European Union's rules
    from 2024.
  - These are the mechanism, untimed, and dated regulatory events with no price given.
- **Voshmgir** (Part 3): much of bitcoin's trading done in Tether, unbacked tokens possibly used to
  buy bitcoin and push its price up, and serious doubt on Tether's backing possibly collapsing its
  price and bitcoin's with it; and Glasner (section 7): demand for Tether creating a derived demand
  for bitcoin — untimed conditionals on bitcoin, **FP-028**'s form, stablecoin supply as buying
  power.
- **Off crypto**:
  - the Reserve Primary Fund breaking the buck on 16 September 2008, the day after Lehman's failure
    (Lo, *Adaptive Markets*, 2017, chapter 9);
  - narrow banking as a way to end bank runs that might move them elsewhere, and Argentina's
    currency board from 1991 to 2001, its peso rates rising as investors feared its end (Blanchard,
    *Macroeconomics*, 2017, chapters 6 and 20);
  - E-Gold, a gold-backed digital currency founded in 1996, indicted in 2007 and its reserve
    liquidated (Chuen, ed., *Handbook of Digital Currency*, 2015, chapter 17);
  - these are past episodes and untimed claims on instruments the lab does not hold.

None gives a timed rule the lab could read.

## What the lab can read of it

The lab holds the daily bars and volumes of twenty-two funds and bitcoin — the funds from 2005 or
their later start, bitcoin from September 2014 — adjusted for dividends and splits, which encode the
funds' distributions, though no strategy reads them until a point-in-time reading with its own test
is built; the Treasury bill's yield from 2005 and two franc exchange rates; the funds' prices, never
their holdings' prices; and no stablecoin price, no reserve attestation, no issuance or redemption
series and no money-market fund; its snapshot is closed, an asset or a series being added only
before the first card. Nothing was computed from the bars for this judgement. On those data:

- **A stablecoin's price against its reserves, audits and redemption terms**, the claim and every
  refutation: the lab holds no stablecoin and no reserve data; a stablecoin's gap to its peg cannot
  be read from bitcoin or the funds.
- **Bitcoin around reserve news**, the one form the lab's data could carry: inside bitcoin's
  in-sample years the library dates about fifteen events on reserve-backed stablecoins:
  - Tether's unbacked months of 2017, which the market learnt of only later;
  - the change of its terms in February 2019 and the New York prosecution in April 2019;
  - four reports of 2018 and 2019 dated only by the articles Voshmgir's reading list cites;
  - Libra's announcement in June 2019 and its partners' exit in October 2019;
  - the Financial Stability Board's report of 13 October 2020, cited in a note;
  - Tether's attestation of 30 March 2021 and its redemption terms of June 2021;
  - Diem's sale in January 2022;
  - the Federal Reserve's report of 9 May 2022;
  - the act of 7 June 2022.
  
  In the holdout it dates about four: the bill of April 2023, the act's reintroduction in July 2023,
  Japan's change in 2023 and the European rules from 2024. A rule entering and leaving bitcoin
  around the in-sample events makes at most about thirty-one decisions, fewer once events within
  five sessions are grouped and the articles that repeat the 2019 events are merged — around gate
  1's thirty, so the count alone cannot settle it. What settles it:
  - a rule on bitcoin alone breaks the RUNBOOK's rule of at least four assets, and gate 6 fails it
    whatever the prices;
  - no source gives bitcoin a sign or a window around reserve news, Voshmgir's and Glasner's being
    untimed conditionals;
  - bitcoin's response would be FP-028's form, not the stablecoin's price.
- **The funds**: the lab holds no money-market fund and no net asset value to set against a price,
  and the Treasury bill's yield carries no information on any issuer's reserve.
- **A fixed stance on bitcoin** makes one decision.

**The bank's siblings, and how AS-037 differs.** AS-037 claims the stablecoin's own price behaviour,
set by its off-chain reserve.
- **AS-038**, crypto-collateralised stablecoins, whose reserve is on-chain, over-collateralised
  crypto.
- **AS-039**, algorithmic stablecoins, whose peg rests on reflexive design, Terra's.
- **FP-028**, stablecoin supply shocks as buying demand for crypto.
- **LL-026**, ETF arbitrage through creation and redemption, a price held to its reserve by a
  redemption open only to authorised participants, the theory's unequal access.
- **MR-025**, limits to arbitrage, the theory's mechanism.
- **MR-026**, closed-end fund discounts, another wrapper's gap to its assets.
- **LL-039**, cross-cryptocurrency return predictability.
- **AS-021**, the native network token, recorded not testable.

All are untouched but AS-021.

What would make it testable: stablecoins' prices at short horizons with their reserve attestations,
issuance and redemptions over the lab's years — outside the lab's data — and a timed rule in the
library.

## Status

AS-037 is recorded `not-testable`:
- its claim and every refutation read stablecoins' prices against their reserves, and the lab holds
  no stablecoin and no reserve data;
- the library's signs are its mechanism, past episodes on Tether, free banking, a money-market fund
  and a currency board, with no stablecoin price given, and untimed conditionals on bitcoin that are
  FP-028's;
- the one readable form, bitcoin around about fifteen dated reserve events, is certain to fail
  through the RUNBOOK's rule of at least four assets, and is given no sign or window.

No card is drawn, and no trial is spent.
