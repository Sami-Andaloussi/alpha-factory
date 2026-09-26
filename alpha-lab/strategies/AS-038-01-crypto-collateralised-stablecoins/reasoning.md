# AS-038-01 — Crypto-collateralised stablecoins: reasoning, not testable as a theory of its own

## The theory, and the forms its sources give it

AS-038 holds that a crypto-collateralised stablecoin keeps its peg by on-chain
over-collateralisation rather than an off-chain reserve, so that its price behaviour, and that of
its governance token or collateral, depends on the collateralisation ratios, the oracles, the
liquidation mechanisms and the keepers' incentives: the same fall in the collateral has different
consequences depending on the margin, the oracle's speed and the liquidation design, and because
much collateral is locked to issue little stablecoin, the system is structurally sensitive to market
stress. Its refutations: a fall in the collateral having the same effect on the peg and the
governance token whatever the margin, the oracle's speed and the liquidation design;
crypto-collateralised systems showing no particular sensitivity to market stress; the peg holding
when the collateral's volatility exceeds what the haircuts cover, or when governance fails to
respond. The bank names crypto, over days, and collateralisation ratios, oracle prices, liquidation
events, stablecoin prices and governance-token prices; its references are Voshmgir's *Token
Economy*, whose second edition (2020) is the one the library holds, not the third the bank names,
and Harvey, Ramachandran and Santoro's *DeFi and the Future of Finance* (2021).

**Its sources, as the lab read them in the library.**

- **Voshmgir** (*Token Economy*, second edition, 2020, Part 3, "Crypto-Collateralized Stable
  Tokens"): stable tokens backed on-chain by bitcoin or ether, managed by a smart contract rather
  than a custodian, from BitUSD in 2013 to MakerDAO's DAI and Synthetix; DAI's 150%
  collateral-to-debt ratio, positions said to be liquidated automatically below it, and the risk
  that a crash fast enough leaves the system under-collateralised before enough positions close — a
  black swan many economists warn of — with oracles a patchwork of centralised feeds open to
  manipulation; DAI's collateral widened from 2019 to a basket of tokens that names no bitcoin — the
  theory's mechanism, untimed, with no price.
- **Harvey, Ramachandran and Santoro** (*DeFi and the Future of Finance*, 2021):
  - Chapter III, "Stablecoins": DAI as the most popular crypto-collateralised stablecoin,
    soft-pegged by incentives, such coins scaling poorly under their debt ceilings — the bank's
    "much collateral to issue little stablecoin".
  - Chapter IV, "DeFi Primitives": positions on Ethereum not liquidated automatically, a keeper paid
    a fee to trigger the liquidation — where the two books differ — and a liquidation on
    under-collateralisation among the conditions of slashing.
  - Chapter VI, "DeFi Deep Dive": DAI's vaults, a ratio of 1.5 whose breach is the equivalent of a
    margin call with no broker's notice or grace period, so that liquidation can follow at once;
    auctions with a liquidation penalty paying keepers to watch; protocol debt covered by a buffer
    and then by MKR; a liquidation selling ether for DAI and so pushing DAI's price up; DAI's supply
    bounded by the demand for loans against ether, with no redemption at a dollar to anchor
    arbitrage, unlike USD Coin's; Synthetix's collateral ratio of 750%; and wrapped bitcoin, which
    lets bitcoin serve as collateral on Ethereum's platforms.
  - Chapter VII, "Risks": oracles as the gravest risk to the protocols that depend on them, with
    outages at Chainlink and Maker that spread damage downstream, dated only in note 15 —
    Chainlink's six-hour delay reported on 13 March 2020 and a timeline of Maker's crisis of 24
    March 2020 — and front-running of Synthetix's oracle, dated only by note 14, of 16 September
    2019.
  - These are the theory's mechanism, one untimed sign on the peg, and episodes dated by notes, with
    no price of DAI or MKR given.

**Return signs near the theory.**

- **Voshmgir** (Part 3, "Flash Attacks"): the flash-loan attacks on bZx, a lending service, of 14
  and 18 February 2020, manipulating the oracle price of a token backed by bitcoin — a past episode
  on tokens the lab does not hold.
- **Schianchi and Mantovi** (*The Economics of Cryptocurrencies and Digital Money*, 2023): the
  collapse of November 2022 as largely a crisis of crypto as collateral (section 1.1.2) — a past
  episode, told of lenders and exchanges rather than of a stablecoin's peg, **FP-031**'s and
  **FP-006**'s forms; stablecoins backed by other tokens called algorithmic (section 5.3), where the
  bank separates AS-038 from AS-039; and reducing stablecoins to a matter of proper collateral as a
  "metallist view" blind to their market's liquidity (section 5.1) — untimed.
- **Huang and others** (*Web3*, 2024): MakerDAO founded in 2015 — Voshmgir says launched in 2017 —
  and DAI as the first decentralised stablecoin to hold its peg, governed by MKR (section 9.2.1);
  DAI minted above a dollar and repaid below it by over-collateralised loans (section 7.2.3);
  oracles manipulated through pool-priced feeds (section 7.3.1); DeFi protocols such as MakerDAO
  keeping their stability in 2022 while centralised lenders failed (section 7.2) — untimed claims
  and past episodes stated without prices.
- **Off crypto**: margins raised as markets turn illiquid, a margin spiral, the S&P futures' margins
  raised at the end of August and of November 2007 (Brunnermeier and Pedersen, chapter 6 in Amihud,
  Mendelson and Pedersen, eds., *Market Liquidity*, 2012); haircuts and repo as the terms of
  financing, and liquidity spirals as a drop followed by a rebound, lived in the week of 6 August
  2007 (Pedersen, *Efficiently Inefficient*, 2015, preface and sections 5.8 and 5.10) — untimed
  claims and past episodes on futures, bonds and single stocks, **FP-006**'s form, not a
  stablecoin's peg.

None gives a timed rule the lab could read.

## What the lab can read of it

The lab holds the daily bars and volumes of twenty-two funds and bitcoin — the funds from 2005 or
their later start, bitcoin from September 2014 — adjusted for dividends and splits, which encode the
funds' distributions, though no strategy reads them until a point-in-time reading with its own test
is built; the Treasury bill's yield from 2005 and two franc exchange rates; the funds' prices, never
their holdings' prices; and no stablecoin, no governance token, no ether, no collateralisation
ratio, no oracle feed and no liquidation series; its snapshot is closed, an asset or a series being
added only before the first card. Nothing was computed from the bars for this judgement. On those
data:

- **The peg and the governance token against the collateral's fall**, the claim and every
  refutation: the lab holds neither the stablecoin nor its governance token. The claim's third leg,
  the collateral's own price, reaches bitcoin only through wrapped bitcoin, while the library lists
  DAI's collateral without bitcoin, and no source dates or signs bitcoin's price under a
  stablecoin's liquidations — **FP-031**'s form.
- **Dated events on MakerDAO, Synthetix and their oracles**: inside bitcoin's in-sample years the
  library dates about eleven:
  - MakerDAO's founding in 2015 and its launch in 2017, as the two books tell them;
  - a critic's article of 11 January 2018 on DAI "breaking", cited in Voshmgir's reading list;
  - DAI's move to a basket of collateral in 2019;
  - the front-running of Synthetix's oracle, dated by a note of 16 September 2019;
  - the attacks on bZx's oracle of 14 and 18 February 2020 (Voshmgir, Part 3), four days apart;
  - the oracle outages of March 2020, dated by notes;
  - Synthetix's move to Chainlink's oracles on 1 September 2020 (Harvey and others, chapter VI, note
    32);
  - BProtocol's flash-loan vote on MakerDAO of 26 October 2020 and the vote of October 2022 with 15%
    of MKR (Huang and others, sections 9.3.5 and 9.2.1);
  - the crisis of crypto as collateral of November 2022.
  
  Several are dated to the year alone. In the holdout it dates MakerDAO's vote of March 2023 to
  invest more in Treasuries (section 11.1.3). A rule entering and leaving bitcoin around the
  in-sample ones makes at most about twenty-three decisions, fewer if events fall within five
  sessions of one another, short of gate 1's thirty whatever the prices (RUNBOOK step 9); a strategy
  on bitcoin alone also breaks the RUNBOOK's rule of at least four assets, and no source gives
  bitcoin a sign around them.
- **The funds under margin spirals**: the library's spirals of 2007 are on futures, bonds and single
  stocks, told as untimed claims and past episodes in 1987 and 2007 with no rule, and the lab holds
  no margin or haircut series; a form on the funds is **FP-006**'s, not this theory's peg.
- **A fixed stance on bitcoin** makes one decision.

**The bank's siblings, and how AS-038 differs.** AS-038 claims the peg's and the governance token's
sensitivity to collateral, oracles and liquidation design.
- **AS-037**, asset-collateralised stablecoins, recorded not testable, whose reserve is off-chain.
- **AS-039**, algorithmic stablecoins, whose peg rests on reflexive design and which some authors
  merge with this one.
- **FP-031**, DeFi liquidation cascades, the collateral's own price under forced sales.
- **FP-030**, funding rates and positioning in perpetual futures, where bitcoin's own leveraged
  positions are liquidated.
- **FP-024**, positive feedback trading and stop-loss cascades.
- **FP-005**, fire sales.
- **FP-006**, liquidity spirals and margin deleveraging.
- **TM-035**, procyclical leverage, recorded not testable.
- **MR-025**, limits to arbitrage, DAI's missing redemption.
- **FP-028**, stablecoin supply as buying power.
- **AS-036**, governance tokens and voting design, recorded not testable, MKR's governance.
- **AS-029**, staking and slashing, recorded not testable, among whose slashing conditions Harvey
  and others list a liquidation on under-collateralisation.
- **AS-044**, decentralised exchanges' design, where DAI trades.

All are untouched but AS-029, AS-036, AS-037 and TM-035.

What would make it testable: stablecoins' and governance tokens' prices with their collateralisation
ratios, oracle feeds and liquidations over the lab's years — outside the lab's data — and a timed
rule in the library.

## Status

AS-038 is recorded `not-testable`:
- its claim and every refutation read a crypto-collateralised stablecoin and its governance token
  against its collateral, oracles and liquidations, and the lab holds neither the stablecoin nor the
  token nor those series;
- the library's signs are the mechanism, one untimed sign on the peg and past episodes without
  prices;
- its dated events are about eleven in-sample, at most about twenty-three decisions, with no sign
  for bitcoin, and bitcoin alone breaks the rule of at least four assets.

No card is drawn, and no trial is spent.
