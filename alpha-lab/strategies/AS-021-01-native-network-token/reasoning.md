# AS-021-01 — Native network token: reasoning, not testable as a theory of its own

## The theory, and the forms its sources give it

AS-021 holds that some cryptoassets are the internal currency of a protocol — paying its validators
or miners, funding its security, sometimes its unit of account, coordinating those who build it — so
that where that role is not cosmetic, the token's price is a function of its usefulness in paying
for the network's security and coordinating its participants, not only a belief about future cash
flows; where its use can be replaced at no cost by ether, a stablecoin or off-chain governance, its
capture of value weakens. Its refutations: native tokens' prices bearing no relation to the security
they fund or to the activity of the networks they coordinate; tokens whose role is replaceable at no
cost capturing as much value as tokens whose role is indispensable. The bank names crypto, over
months and years, and on-chain data, validators' and miners' rewards and daily prices; its
references are Voshmgir's *Token Economy*, whose second edition (2020) is the one the library holds,
not the third the bank names; Burniske and Tatar's *Cryptoassets* (2017); and Schianchi and
Mantovi's *The Economics of Cryptocurrencies and Digital Money*, held in its Palgrave edition of
2023.

**Its sources, as the lab read them in the library.**

- **Burniske and Tatar** (*Cryptoassets*, 2017): miners paid in bitcoin for each block they add, the
  cost of their machines standing guard against an attacker (chapter 2); a public blockchain needing
  a native asset to pay the miners who secure it, private blockchains needing none because they
  secure themselves by exclusivity, and miners' pay shifting over time from new coins to fees
  (chapter 3, "Blockchain, Not Bitcoin?").
- **Voshmgir** (*Token Economy*, second edition, 2020, chapter "Tokens", and Part 3, "Money or
  Not?"): protocol tokens such as ether beside the application tokens built on their network, native
  tokens being at once assets and access rights, needed to pay the network's fees; and the network
  token's price as a gauge of its payment network's soundness — an untimed claim.
- **Schianchi and Mantovi** (*The Economics of Cryptocurrencies and Digital Money*, 2023): consensus
  by proof of work and proof of stake and the native token as the reward (chapter 2); the mining
  reward valued as the exchange rate times the block reward in coins, after Budish (chapter 1); and
  Pagnotta's (2022) model of a game between users and miners in which bitcoin's price and the
  network's security depend on each other, with several equilibria (chapter 4) — the theory's claim
  in model form, untimed.
- **Others in the library**: bitcoin held only if fees stay low relative to currency growth once
  fees alone pay the miners (Hendrickson and Luther, chapter 4 in Caton, ed., *The Economics of
  Blockchain and Cryptocurrency*, 2022); fees becoming the larger part of the miners' reward
  (Antonopoulos and Harding, *Mastering Bitcoin*, third edition, 2023).

**Return signs near the theory.**

- **Kristof** (chapter 4, "National Cryptocurrencies", in Chuen, ed., *Handbook of Digital
  Currency*, 2015): AuroraCoin's price falling after its airdrop and the selling that followed, its
  miners leaving, partly over a large premine, its hash rate dropping far enough to invite a 51%
  attack, and its price falling further — a spiral of price and security told after the fact, on one
  coin the lab does not hold.
- **Burniske and Tatar** (chapter 13): the hash rate often following the price and sometimes
  leading it, when miners expect the asset to do well — a relation with no direction fixed and no
  timing, needing the hash rate.
- **Recorded elsewhere**: bitcoin's value held up by users' lock-in despite a likely loss of value
  at some point in the indefinite future (Glasner, chapter 3 in Caton, ed., 2022) and an adoption
  curve feeding periodic bubbles (Chuen, ed., 2015), untimed claims recorded in AS-017-01, answering
  the pointer AS-015-01 left to AS-017 and AS-021; bitcoin against the FANG stocks from 2012 to 2017
  (Burniske and Tatar, chapter 7), past returns recorded in AS-020-01.

Each is a model, an untimed claim or a past episode; none gives a timed return rule on the security
a token pays for or the activity it coordinates. The library holds no rule on a security budget, a
miners'-revenue multiple — the Puell multiple is named once, as a vendor's indicator with no rule
(Huang and others, *Web3*, 2024, section 7A.1.4) — a stock-to-flow ratio or the hash rate's ribbons.

## What the lab can read of it

The lab holds the daily bars and volumes of twenty-two funds and bitcoin — the funds from 2005 or
their later start, bitcoin from September 2014 — adjusted for dividends and splits, which encode the
funds' distributions, though no strategy reads them until a point-in-time reading with its own test
is built; the Treasury bill's yield from 2005 and two franc exchange rates; the funds' prices, never
their holdings' prices; and no single stock, no other cryptoasset and no on-chain series — hash
rate, fees, blocks, miners' revenue, transactions, users; its snapshot is closed, an asset or a
series being added only before the first card. Nothing was computed from the bars for this
judgement. On those data:

- **The price against the security it funds**, the first refutation's first half: the hash rate and
  the fees are not held. The block subsidy is known from the protocol, but the lab holds no count of
  blocks, so the subsidy valued at the day's price is the price itself times a step that changes
  only at the halvings; it cannot test the price against security, and its one independent move is
  the halving itself.
- **The price against the network's activity**, the first refutation's second half: the lab holds
  bitcoin's traded volume, which is exchange trading, not on-chain transactions or users, and is
  read with a day's delay; no source ties exchange volume to security or coordination, and Burniske
  and Tatar's chapter 13 gives chart-reading rules: its moving averages are recorded in TM-005-01,
  and its volume rules — a breakout on high volume as a buy signal, heavy volume confirming a trend
  or marking capitulation — are practitioners' advice with no evidence, in the form of **TM-027**,
  volume-conditioned momentum, recorded not testable.
- **Replaceable against indispensable tokens**, the second refutation: the lab holds one token,
  bitcoin, and no ether, stablecoin or other token to compare.
- **The halvings**: two fall inside the in-sample years, July 2016 and May 2020 — the third, in
  April 2024, is in the holdout — so a rule that enters and leaves around each makes at most five
  decisions, certain to fail gate 1's thirty. Forms whose count depends on prices or on the calendar
  — a weight that moves with the time since the last halving, a ratio of the subsidy's value to its
  own trailing mean — are not AS-021's but the issuance, miners' selling and security-budget forms
  of **EF-044**, **FP-029** and **EF-047**, which judge them when picked; the library holds no rule
  or sign for them.
- **A fixed stance on bitcoin**, the indispensable token held throughout, makes one decision; and a
  strategy on bitcoin alone breaks the RUNBOOK's rule of at least four assets, while gate 6 fails a
  strategy that passes gate 2 only with bitcoin, or whose profit rests more than 30% on one asset.

**The bank's siblings, and how AS-021 differs.** **EF-047**, the proof-of-work security budget and
the hash rate, the bank's theory of the first refutation's own relation, read with the hash rate,
block rewards and fees; **EF-044**, token issuance and monetary policy, and **FP-029**, miners'
selling pressure, which hold the halvings; **EF-046**, network operating health, which holds the
hash rate's link to the price; **EF-037** and **EF-038**, network value on users and active
addresses; **EF-040**, velocity, which asks whether the service could be paid for otherwise — the
second refutation's question; **EF-036**, utility against speculative value; **EF-045**,
proof-of-stake staking valuation, the validators' side of paying for security; **EF-042**, a token's
claim on fees; **EF-041**, adoption-driven valuation; **AS-026**, token design; **AS-029** and
**AS-030**, staking; **AS-036**, governance tokens, the coordination and off-chain governance the
theory contrasts with; **AS-043**, blockspace scarcity; all untouched; **AS-017**, network effects,
and **AS-020**, two-sided platforms, recorded not testable. AS-021 claims the price as payment for a
role — security and coordination — where its siblings claim the price of issuance, supply, adoption,
fees, design or governance.

What would make it testable: on-chain series — hash rate, fees, miners' revenue, transactions,
validators' stakes — and several native and non-native tokens over the lab's years, outside the
lab's data, with a timed rule for them in the library.

## Status

AS-021 is recorded `not-testable`: its claim and both refutations read the security a token funds,
the activity it coordinates and tokens whose roles differ, while the lab holds bitcoin's price and
exchange volume alone, no on-chain series and no other token; its sources give models, untimed
claims and past episodes, no timed rule; the halvings inside the in-sample years allow at most five
decisions around them, and the forms whose count depends on prices are EF-044's, FP-029's and
EF-047's. No card is drawn, and no trial is spent.
