# AS-028-01 — Vesting, unlocks and treasury overhang: reasoning, not testable as a theory of its own

## The theory, and the forms its sources give it

AS-028 holds that tokens come under supply pressure around the dates their vested allocations
unlock, and more structurally with the pace at which their float expands, the market reacting again
and again to a supply schedule known in advance; the reaction depends on the unlock's relative size,
the recipients and the depth of the market, mostly in initial coin offerings, venture-backed tokens
and protocols with long vesting. Its refutations: no abnormal decline around scheduled unlocks and
no relation to the float's pace; a reaction unrelated to the unlock's size, the recipients or the
market's depth; the whole effect priced when the schedule becomes known. The bank names crypto, over
days, weeks and months, and unlock schedules, circulating supply, treasury holdings and daily
prices; its references are Howell, Niessner and Yermack (2020) and Catalini and Gans (2018) on
initial coin offerings, and Brav and Gompers (2003) on lock-ups in initial public offerings — none
of which the library holds, the Brav and Gompers it cites being their 1997 paper on offerings' later
returns — with Harvey and others' *DeFi and the Future of Finance* (2021) and Voshmgir's *Token
Economy*, whose second edition (2020) is the one the library holds.

**Its sources, as the lab read them in the library.**

- **Harvey, Ramachandran and Santoro** (*DeFi and the Future of Finance*, 2021): Uniswap's token,
  43% of whose supply vests over four years to a treasury its governance controls — a distribution,
  with no price sign.
- **Voshmgir** (*Token Economy*, second edition, 2020): holders of a large stake able to move a
  token's price, like a quasi central bank (Part 2, "Monetary & Fiscal Policy of DAOs"); and, in
  Part 3, "Token Sales", cool-off periods freezing or vesting the tokens of large holders who bought
  at a discount, to stop them dumping, lest the market price crash — the theory's own mechanism with
  its sign, untimed, with no window or size, on tokens the lab does not hold. The concentration of
  Steem's stake is **AS-035**'s.
- **Huang and others** (*Web3*, 2024, section 6.3.2, "Token Supply Analysis", and section 6.3.4,
  "Token Financials"): unlocks rising fast over a short span causing selling pressure, large
  unlocking events able to move the market, and a token's value falling as unlocked tokens reach the
  market faster than the project grows — the library's one direct sign on unlocks, untimed, with no
  window, size threshold or evidence, on tokens the lab does not hold; and bitcoin's supply as the
  simple case, about 19 million of 21 million coins circulating in 2023, the rest released gradually
  until about 2140, with no investor unlocks, founders' treasury, cliffs or vesting.

**Return signs near the theory.**

- **Released supply in general**: farmed airdrops sold as soon as trading opens (Huang and others,
  section 6.3.2); most tokens from coin offerings soon worth less than the money raised (Voshmgir,
  Part 3); Uniswap's token spiking above eight dollars after its airdrop before settling at four to
  five (Harvey, Ramachandran and Santoro); AuroraCoin's network value falling from about 100 million
  dollars to under 20 million in the days after its airdrop of 25 March 2014, as recipients sold
  (Burniske and Tatar, *Cryptoassets*, 2017, chapter 4), and SpainCoin failing after its airdrop
  (Kristof, chapter 4 in Chuen, ed., *Handbook of Digital Currency*, 2015); a founding team holding
  much of the supply having great power over the price (Burniske and Tatar, chapter 11) — untimed
  claims and past episodes on tokens the lab does not hold, several recorded in AS-026-01.
- **The expiry of lock-ups after initial public offerings**: about −1.5% around the unlock, −3% for
  firms backed by venture capital (Singal, *Beyond the Random Walk*, 2003) — the same mechanism on
  shares, **AS-003**'s form, recorded not testable.

None gives a timed rule on unlock dates that the lab could read.

## What the lab can read of it

The lab holds the daily bars and volumes of twenty-two funds and bitcoin — the funds from 2005 or
their later start, bitcoin from September 2014 — adjusted for dividends and splits, which encode the
funds' distributions, though no strategy reads them until a point-in-time reading with its own test
is built; the Treasury bill's yield from 2005 and two franc exchange rates; the funds' prices, never
their holdings' prices; and no other cryptoasset, no unlock schedule, treasury or on-chain series;
its snapshot is closed, an asset or a series being added only before the first card. Nothing was
computed from the bars for this judgement. On those data:

- **Unlocks and the float's pace**, the claim and every refutation: the lab's one token, bitcoin,
  has no vesting, unlocks, cliffs or treasury; its float grows by a mining schedule fixed from the
  start and known to all, whose steps — the halvings, two inside the in-sample years and one in the
  holdout — are **EF-044**'s (token issuance and monetary policy), **FP-029**'s (miners' selling
  pressure) and **EF-047**'s (the security budget), to which a recorded decision leaves bitcoin's
  schedule-based forms; a rule around the two in-sample halvings makes at most five decisions, far
  fewer than gate 1's thirty.
- **Held-back supply released on bitcoin's market**: the one dated release the library gives inside
  bitcoin's in-sample years is the first unlock of the Grayscale Bitcoin Trust's privately placed
  shares, saleable after a year's hold, from 4 May 2015 (Burniske and Tatar, chapter 15) — shares of
  the trust, not bitcoin, whose premium the lab does not hold; the library dates no release of
  bitcoin holdings — seizures or bankruptcies' distributions — inside bitcoin's lab years, the Silk
  Road seizure (October 2013) and Mt. Gox's collapse (February 2014) falling before them, and none
  in the holdout. A rule around the one event makes at most three decisions, certain to fail gate 1
  (RUNBOOK step 9). Released holdings of bitcoin are **AS-035**'s form, as AS-003-01 recorded.
- **A fixed stance on bitcoin** makes one decision, and a strategy on bitcoin alone breaks the
  RUNBOOK's rule of at least four assets.

**The bank's siblings, and how AS-028 differs.** AS-028 claims the price's reaction to scheduled
releases of allocated supply. **AS-003**, lock-up expirations after initial public offerings,
recorded not testable, the same mechanism on shares; **AS-026**, token design, recorded not
testable, of which the vesting schedule is one attribute; **AS-035**, supply concentration and
whales' overhang, the holders rather than the schedule, which holds released bitcoin holdings;
**AS-030**, the staking ratio, supply locked by holders' choice rather than by a schedule;
**AS-036**, governance tokens, which govern the treasury's use; **EF-027**, net share issuance,
whose crypto analogue is supply entering through issuance, rewards or unlocks at a pace, on single
stocks and tokens; **EF-041**, adoption-driven token valuation, which reads issuance schedules,
sales and treasuries into value; **EF-044**, issuance, whose own data list vesting schedules, the
protocol's supply rule rather than allocated releases; **FP-027**, exchange reserves and on-chain
flows, supply reaching exchanges; **FP-029**, miners' selling; **EF-047**, the security budget; all
untouched but AS-003 and AS-026.

What would make it testable: tokens with vesting and their unlock schedules, circulating supply and
treasuries over the lab's years — outside the lab's data — and a timed rule in the library on the
reaction.

## Status

AS-028 is recorded `not-testable`: its claim and every refutation read tokens with vesting and
unlock schedules, while the lab's one token, bitcoin, has none; the library's signs on unlocks are
untimed and on tokens the lab does not hold; the one dated release inside bitcoin's in-sample years
is the trust's first unlock of shares, at most three decisions, and the halvings are EF-044's,
FP-029's and EF-047's; released bitcoin holdings are AS-035's, and the lock-up form on shares is
AS-003's. No card is drawn, and no trial is spent.
