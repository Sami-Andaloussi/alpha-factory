# AS-029-01 — Staking and slashing: reasoning, not testable as a theory of its own

## The theory, and the forms its sources give it

AS-029 holds that assets with staking show a smaller free float, a nominal staking yield, penalties
when slashing occurs and exit queues when holders withdraw, and that their prices and circulation
respond to collateralisation ratios and to the design of the reward — each protocol's rules making
one staked asset differ from another. Its refutations: tokens with a large staked share showing the
same free float, liquidity and price behaviour as comparable tokens without staking; changes in
slashing rules, collateralisation ratios, reward design or exit queues leaving the token's price and
circulation unchanged; slashing events leaving stakers' behaviour and the price unchanged. The bank
names crypto, over weeks and months, and staking ratios, staking rewards, slashing events, exit
queues and daily prices; its references are Harvey, Ramachandran and Santoro's *DeFi and the Future
of Finance* (2021), Li, Niyato and Han's *Cryptoeconomics* (2023) and Voshmgir's *Token Economy*,
whose second edition (2020) is the one the library holds, not the third the bank names.

**Its sources, as the lab read them in the library.**

- **Harvey, Ramachandran and Santoro** (*DeFi and the Future of Finance*, 2021, "DeFi Primitives",
  "Incentives"): staking as locking tokens to earn rewards, and slashing as a staked incentive
  turned negative, taking back part or all of the stake when a set condition is met; Synthetix's
  collateralisation ratio of 750% for its staking rewards, funded by new tokens (Part VI, "DeFi Deep
  Dive") — mechanisms, with no price sign; a burn used to raise price pressure is a supply sign,
  **EF-044**'s and **EF-045**'s.
- **Li, Niyato and Han** (*Cryptoeconomics*, 2023, sections 1.2.2, 3.2, 5.3 and 8.2): validators'
  deposits as a security incentive, slashed on a violation, a heavy fine; and Houy's attack, in
  which stakers selling to an attacker could destroy the chain's value (section 5.3.2) — security
  and incentives, a theoretical threat with no timing.
- **Voshmgir** (*Token Economy*, second edition, 2020): in Part 1, "Alternative Consensus Mechanisms
  to PoW", early proof-of-stake designs assuming that a dishonest validator's stake would lose
  value, an untimed assumption; in Part 2, "Institutional Economics of DAOs", the block reward,
  fees, the token's price and slashing among a network's incentives.
- **Burniske and Tatar** (*Cryptoassets*, 2017, chapter 14): dishonest validators losing their
  stake, and proof-of-stake systems paying stakers an interest rate, 5% for example — a yield level,
  with no price sign.

**Return signs near the theory.**

- **Huang and others** (*Web3*, 2024): raising a pool's rewards drawing more users and possibly
  raising the native token's demand and value (section 7.2.2) — a sign on reward design, untimed, on
  DeFi tokens the lab does not hold; a staking reward paid in the same token guarding against
  dilution rather than paying income, so that a 10% rate must be weighed against the token's fall
  (section 6.3.3) — **EF-045**'s form, untimed.
- **Terra**: LUNA soaring on a yield of nearly 20% for stakers and collapsing in May 2022 (Huang and
  others, section 7.2.3), the peg lost on 7 and 9 May and LUNA down 96% on 12 May (Schianchi and
  Mantovi, *The Economics of Cryptocurrencies and Digital Money*, 2023, section 5.3.3, which
  describe the 20% as a deposit rate on the stablecoin) — a past episode on tokens the lab does not
  hold, **AS-039**'s (algorithmic stablecoins).

None gives a timed rule the lab could read.

## What the lab can read of it

The lab holds the daily bars and volumes of twenty-two funds and bitcoin — the funds from 2005 or
their later start, bitcoin from September 2014 — adjusted for dividends and splits, which encode the
funds' distributions, though no strategy reads them until a point-in-time reading with its own test
is built; the Treasury bill's yield from 2005 and two franc exchange rates; the funds' prices, never
their holdings' prices; and no other cryptoasset and no on-chain series; its snapshot is closed, an
asset or a series being added only before the first card. Nothing was computed from the bars for
this judgement. On those data:

- **Staking, slashing, exit queues and their effect on price**, the claim and every refutation: the
  lab's one token, bitcoin, is secured by proof of work and has no staking, slashing or exit queue;
  no staked asset is in the lab's universe, and no staking ratio, reward or slashing event is held;
  bitcoin's own payment for security, by mining, is AS-021's and EF-047's.
- **Dated staking events**: the library dates Ethereum's move to proof of stake to September 2022,
  inside the in-sample years (Schianchi and Mantovi, section 2.1.5; the year alone in Huang and
  others, section 3.3.4), and Terra's collapse to May 2022; it dates no staking event in the
  holdout. Both are on tokens the lab does not hold; a rule entering and leaving around them on
  bitcoin or the funds makes at most five decisions, certain to fail gate 1's thirty whatever the
  prices (RUNBOOK step 9).
- **A staking yield against the bill's yield**: the lab holds the bill's yield but no staking yield;
  the library gives only illustrative levels — about 5%, a 10% example, nearly 20% on Terra — so a
  comparison would be a rule on the bill's yield against a constant, not this theory.

**The bank's siblings, and how AS-029 differs.** AS-029 claims the mechanics of reward, penalty and
exit and their effect on price and circulation. **AS-030**, the staking ratio and the float's
scarcity, the price support of a high ratio and its fragility; **EF-045**, proof-of-stake staking
valuation, the trade-off between security and dilution; **AS-021**, the native network token, paying
for security by mining or staking, and **AS-026**, token design, of which staking is one attribute,
recorded not testable; **AS-028**, vesting and unlocks, recorded not testable, supply released by a
schedule rather than by stakers' exits; **AS-035**, supply and validator concentration, the holders
rather than the rules; **AS-038**, crypto-collateralised stablecoins, whose collateral ratios and
liquidations Harvey and others liken to slashing; **AS-039**, algorithmic stablecoins, which holds
Terra; **EF-044**, issuance, whose data include staking but read the supply rule; **EF-046**,
network operating health; **EF-047**, the proof-of-work security budget; all untouched but AS-021,
AS-026 and AS-028.

What would make it testable: staked assets with their staking ratios, rewards, slashing events and
exit queues over the lab's years — outside the lab's data — and a timed rule in the library.

## Status

AS-029 is recorded `not-testable`: its claim and every refutation read staked assets and their
staking data, while the lab's one token, bitcoin, has no staking and no staked asset is in its
universe; the library's signs on staking are untimed claims or a past episode on tokens the lab does
not hold; its dated staking events are two, in 2022, at most five decisions. No card is drawn, and
no trial is spent.
