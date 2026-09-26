# AS-026-01 — Valuation of token design characteristics: reasoning, not testable as a theory of its own

## The theory, and the forms its sources give it

AS-026 holds that across cryptoassets, design attributes — supply policy, utility, governance
rights, burns, consensus rules, privacy, the possibility of forks, the capture of fees — explain
differences in valuation and performance, mostly over the medium to long term, with abrupt repricing
when a token changes its tokenomics, its governance or its consensus. Its refutations: tokens
differing in these attributes showing no systematic differences in valuation or performance; tokens
that capture fees, burn supply or confer an indispensable utility no less sensitive to market
conditions than speculative or inflationary tokens; changes in tokenomics, governance or consensus
causing no repricing. The bank names crypto, over days, months and years, and token design
attributes, supply schedules and daily prices; its references are Eska, Shi, Theissen and
Uhrig-Homburg's working paper *Design and Valuation of Cryptocurrencies* (2022) and Freni and
others' *Tokenomics and Blockchain Tokens* (2022), neither of which the library holds.

**Its sources, as the lab read them in the library.** The two references are not in the library, and
the lab does not read papers outside it. What the library holds on token design:

- **Voshmgir** (*Token Economy*, second edition, 2020, the one the library holds): in the chapter
  "Tokens", a classification of tokens by morphological analysis — the method Freni and others name
  — protocol and application tokens, their purposes, rights and supply rules, and the untimed claim
  that a resilient network supports a relatively stable long-term token value.
- **Burniske and Tatar** (*Cryptoassets*, 2017): cryptoassets differing in their supply schedules —
  bitcoin and litecoin deflationary, Dogecoin's schedule keeping each coin's value small — with
  Dash, Monero and Zcash among the designs (chapter 4), and bitcoin's against the dollar's and
  gold's (chapter 8).
- **Antonopoulos and Harding** (*Mastering Bitcoin*, third edition, 2023): bitcoin's consensus
  changes and their activation — rules, with no price sign.
- **Cachanosky** (chapter 2, "Can Cryptocurrencies Become a Commonly Accepted Means of Exchange?",
  in Caton, ed., *The Economics of Blockchain and Cryptocurrency*, 2022): Bitcoin Cash as a hard
  fork of bitcoin with larger blocks — design, undated.
- **Schianchi and Mantovi** (*The Economics of Cryptocurrencies and Digital Money*, 2023, chapter
  1): bitcoin's hundred-odd forks as exceptional events that play no significant role in the system
  — the counter-view.

**Return signs near the theory.**

- **On forks**: a contentious hard fork can often sink the price of the units on both chains, as
  holders fear a lasting schism (Burniske and Tatar, chapter 5), Ethereum's fork after The DAO's
  hack in 2016 costing it dearly — on ether, which the lab does not hold; a politicised hard fork as
  a black-swan event for a token's value, Bitcoin Cash beginning to trade on 1 August 2017 at about
  240 dollars while bitcoin traded at about 2,700 (Voshmgir, Part 1, "Protocol Forks & Network
  Splits") — the one design sign on bitcoin, whose dated count is below.
- **On supply and distribution**: a shrinking supply tending to raise a token's value and a growing
  one to lower it, farmed airdrops sold as soon as trading opens, burns shaping value (Huang and
  others, *Web3*, 2024, sections 6.2.4, "Platform Tokens", and 6.3.2, "Token Supply Analysis") —
  untimed claims; most tokens from coin offerings soon worth less than the money raised (Voshmgir,
  Part 3, "Token Sales"); Monero's privacy making it 2016's best-performing coin, up 2,760%, Zcash's
  scarce initial supply spiking its price before it settled, AuroraCoin collapsing after its airdrop
  (Burniske and Tatar, chapter 4); Uniswap's governance token spiking above eight dollars after its
  airdrop before settling at four to five (Harvey, Ramachandran and Santoro, *DeFi and the Future of
  Finance*, 2021) — past episodes on tokens the lab does not hold.

None gives a timed return rule the lab could read on its one token.

## What the lab can read of it

The lab holds the daily bars and volumes of twenty-two funds and bitcoin — the funds from 2005 or
their later start, bitcoin from September 2014 — adjusted for dividends and splits, which encode the
funds' distributions, though no strategy reads them until a point-in-time reading with its own test
is built; the Treasury bill's yield from 2005 and two franc exchange rates; the funds' prices, never
their holdings' prices; and no other cryptoasset, no design attribute beyond bitcoin's own rules,
and no on-chain series; its snapshot is closed, an asset or a series being added only before the
first card. Nothing was computed from the bars for this judgement. On those data:

- **Differences in valuation across designs**, the claim and the first two refutations: a
  cross-section of tokens, of which the lab holds one; bitcoin's supply cap, the absence of a fee
  burn and proof of work stay the same over its years, its consensus changing only at the soft forks
  listed below, so it cannot be compared with itself.
- **Bitcoin against the funds as a design contrast**: Burniske and Tatar set bitcoin's capped supply
  against the dollar's and gold's; a stance of bitcoin against the gold fund on that design
  difference, which never changes, makes one decision, certain to fail gate 1; and a strategy on
  bitcoin alone breaks the RUNBOOK's rule of at least four assets.
- **Repricing when a token changes its design**, the third refutation: inside bitcoin's in-sample
  years the library dates five changes — the BIP65 soft fork in December 2015, the CSV soft fork in
  July 2016, SegWit in 2017, the Bitcoin Cash split on 1 August 2017 and taproot in November 2021 —
  and none in the holdout; a rule that enters and leaves around each makes at most ten decisions,
  fewer once gate 1 groups neighbours, certain to fail its thirty whatever the prices (RUNBOOK step
  9). The halvings, steps in supply that follow the design rather than change it, are **EF-044**'s,
  **FP-029**'s and **EF-047**'s, to which a recorded decision leaves bitcoin's schedule-based forms.

**The bank's siblings, and how AS-026 differs.** AS-026 claims the cross-section of designs and
repricing when a design changes; each sibling claims one mechanism. **AS-021**, the native network
token's price as payment for security, and **AS-017**, network effects, and **AS-020**, two-sided
platforms, recorded not testable; **AS-028**, vesting and unlocks; **AS-029** and **AS-030**,
staking; **AS-035**, supply and validator concentration, whose fork risk is one design consequence;
**AS-036**, governance tokens; **AS-037** to **AS-040**, stablecoins and bonding curves; **AS-043**,
blockspace scarcity, the dispute behind the Bitcoin Cash split; **AS-044**, decentralised exchanges'
design and its sensitivity to upgrades; **EF-036**, utility against speculative value; **EF-039**,
the Lindy effect of surviving networks; **EF-040**, velocity; **EF-041**, adoption-driven valuation;
**EF-042**, fee capture; **EF-043**, a purpose-driven token's value capture, the indispensable
utility of the refutations; **EF-044**, issuance; **EF-045**, staking and dilution, burns among
them; **EF-046**, network health; **EF-047**, the security budget; all untouched but AS-017, AS-020
and AS-021.

What would make it testable: a cross-section of tokens with their design attributes and many dated
changes of design over the lab's years — outside the lab's data — and a timed rule for them in the
library.

## Status

AS-026 is recorded `not-testable`: its claim and its first two refutations compare tokens of
different designs, and the lab holds one token, whose design barely changes; its third reads
repricing at design changes, of which the library dates five for bitcoin inside the in-sample years,
at most ten decisions around them; its nearby return signs are untimed claims or past episodes on
tokens the lab does not hold; its references are not in the library. No card is drawn, and no trial
is spent.
