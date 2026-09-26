# AS-030-01 — Staking ratio, float scarcity and unstaking fragility: reasoning, not testable as a theory of its own

## The theory, and the forms its sources give it

AS-030 holds that proof-of-stake tokens with a high staking ratio have an effective float much
smaller than their circulating supply, and that the high ratio can support their price over
intermediate horizons — through the float's scarcity, the holders' commitment and stronger security
— while the same tokens can go through stress when staking yields, governance, slashing risk or exit
conditions change, the market discovering that part of the locked stock was deferred supply once
holders unstake to sell. Its refutations: tokens with a high staking ratio showing no difference in
liquidity, depth or price behaviour from comparable tokens with a low one; changes in yields,
governance, slashing risk or exit conditions triggering no wave of unstaking and no price stress;
large unstaking episodes followed by no selling pressure. The bank names proof-of-stake
cryptoassets, over days, weeks and months, and staking ratios, circulating supply, unstaking queues,
staking yields and daily prices; its references are Cong, He and Tang's working paper *The
Tokenomics of Staking* (2025) and Catalini, Jagadeesan and Kominers's *Markets for Crypto Tokens,
and Security under Proof of Stake* (2020), neither of which the library holds.

**Its sources, as the lab read them in the library.** The two references are not in the library, and
the lab does not read papers outside it. The library's crypto books describe staking and its
incentives — tokens locked for rewards, validators' deposits slashed on a violation (Harvey,
Ramachandran and Santoro, *DeFi and the Future of Finance*, 2021; Li, Niyato and Han,
*Cryptoeconomics*, 2023; Voshmgir, *Token Economy*, second edition, 2020). The theory's mechanism is
stated once: staked or collateralised tokens are less liquid than their circulating count suggests,
and can come back to trading within days or months if holders unstake or withdraw them, while a
shrinking circulating supply typically raises a token's value (Huang and others, *Web3*, 2024,
section 6.3.2, "Token Supply Analysis") — untimed, with no ratio threshold or window, on tokens the
lab does not hold.

**Return signs near the theory**, several recorded in AS-029-01: staking rewards among what sets a
token's demand and price, and a staking reward in the same token guarding against dilution rather
than paying income (Huang and others, section 6.3.3); rewards drawing users and possibly raising a
native token's value, and burns or buybacks creating scarcity (section 7.2.2) — untimed; LUNA
soaring on a yield of nearly 20% for stakers and collapsing in May 2022 (Huang and others, section
7.2.3), which Schianchi and Mantovi (*The Economics of Cryptocurrencies and Digital Money*, 2023,
section 5.3.3) tell as capital fleeing the stablecoin that paid a 20% deposit rate, the peg lost on
7 and 9 May and LUNA down 96% on 12 May — a past episode on tokens the lab does not hold,
**AS-039**'s, with no unstaking described. None gives a timed sign on a staking ratio.

## What the lab can read of it

The lab holds the daily bars and volumes of twenty-two funds and bitcoin — the funds from 2005 or
their later start, bitcoin from September 2014 — adjusted for dividends and splits, which encode the
funds' distributions, though no strategy reads them until a point-in-time reading with its own test
is built; the Treasury bill's yield from 2005 and two franc exchange rates; the funds' prices, never
their holdings' prices; and no other cryptoasset and no on-chain series; its snapshot is closed, an
asset or a series being added only before the first card. Nothing was computed from the bars for
this judgement. On those data:

- **The staking ratio, the effective float and unstaking episodes**, the claim and every refutation:
  the lab's one token, bitcoin, is secured by proof of work and has no staking ratio, no unstaking
  queue and no staking yield; no proof-of-stake token is in the lab's universe. The library dates
  Ethereum's move to proof of stake to September 2022 (Schianchi and Mantovi, section 2.1.5) and
  Terra's collapse to May 2022 (section 5.3.3), and no unstaking event in the holdout; a rule
  entering and leaving around them makes at most five decisions, certain to fail gate 1's thirty
  (RUNBOOK step 9).
- **Bitcoin's own dormant supply**, the nearest idea the lab's one token could carry: the library
  gives at least 55% of bitcoins dormant between 2010 and 2013, hoarded for their expected
  appreciation (Tarasiewicz and Newman, chapter 10 in Chuen, ed., *Handbook of Digital Currency*,
  2015), a dormant share near 60% (Bhaskar and Chuen, chapter 28, same book), and a forecast share
  held for investment or dormant (Burniske and Tatar, *Cryptoassets*, 2017, chapter 12) — static
  figures before bitcoin's lab years or a forecast, with no timed rule; reading them needs on-chain
  series of coins' ages, which the lab does not hold. Illiquid supply and long-term holders are
  **FP-027**'s form, holding periods **EF-040**'s, holders' concentration **AS-035**'s.
- **The funds' float**: the funds' shares are created and redeemed on demand, so they have no locked
  float; free-float and lock-up effects on single stocks, which the lab does not hold, are
  **AS-003**'s and **FP-011**'s.

**The bank's siblings, and how AS-030 differs.** **AS-029**, staking and slashing, the mechanics of
reward, penalty and exit, recorded not testable, where AS-030 claims the price support of a high
ratio and its fragility; **EF-045**, proof-of-stake staking valuation, the trade-off between
security and dilution; **EF-047**, the proof-of-work security budget, bitcoin's own; **FP-027**,
exchange reserves and on-chain flows, which names illiquid supply and long-term holders; **EF-040**,
velocity and holding periods; **EF-044**, issuance, whose data include staking; **AS-003**, lock-up
expirations after initial public offerings, recorded not testable, the same deferred supply on
shares; **FP-011**, index inclusion; **AS-028**, vesting and unlocks, recorded not testable,
scheduled releases of allocated supply where AS-030's are holders' choices to unstake; **AS-035**,
supply and validator concentration; **AS-021**, the native network token, and **AS-026**, token
design, recorded not testable; all untouched but AS-003, AS-021, AS-026, AS-028 and AS-029.

What would make it testable: proof-of-stake tokens with their staking ratios, yields, unstaking
queues and prices over the lab's years — outside the lab's data — and a timed rule in the library.

## Status

AS-030 is recorded `not-testable`: its claim and every refutation read proof-of-stake tokens and
their staking data, while the lab's one token, bitcoin, has no staking and no proof-of-stake token
is in its universe; its references are not in the library, and the library's signs near it are
untimed or a past episode on tokens the lab does not hold. No card is drawn, and no trial is spent.
