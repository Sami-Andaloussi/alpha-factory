# AS-040-01 — Bonding curves: reasoning, not testable as a theory of its own

## The theory, and the forms its sources give it

AS-040 holds that a token issued on a bonding curve, whose contract ties the price at which it mints
or burns the token to its circulating supply and sometimes to a reserve pool, has a price partly set
by the contract rather than by the market alone, and shows the recursive behaviour the curve
creates: an advantage for the first entrants, a convex or concave price profile, an endogenous
treasury effect and reflexivity between participation and valuation, with unstable dynamics when
holders exit under stress. Its refutations: bonding-curve tokens' prices unrelated to the curve's
mint and burn prices as supply changes; no advantage for the first entrants and no reinforcement
between participation and valuation; exits under stress unwinding smoothly along the curve. The bank
names crypto, over days and months, and bonding-curve parameters, token supply, reserve-pool
balances and daily prices; its references are Harvey, Ramachandran and Santoro's *DeFi and the
Future of Finance* (2021) and Voshmgir's *Token Economy*, whose second edition (2020) is the one the
library holds, not the third the bank names.

**Its sources, as the lab read them in the library.**

- **Harvey, Ramachandran and Santoro** (*DeFi and the Future of Finance*, 2021, chapter IV, "DeFi
  Primitives"):
  - "Bonding Curve: Pricing Supply": the curve as the contractual price of a token against its
    supply, investors usually selling back along the same curve; a constant curve, the simplest,
    pegging the token; a rising curve rewarding early buyers, a linear one generously if the token
    grows to a large enough supply, and a superlinear one extremely — the first token at 1 ether and
    the hundredth at 10,000 under a square law — while most projects, it says, would use a sublinear
    curve or a logistic one bounded above; a selling curve that can be set below the buying curve,
    the spread accruing to the contract as a fee or treasury, the contract solvent while it holds
    enough collateral to buy back down the whole selling curve.
  - "Supply Adjustment" and "Incentives": burns raising a token's scarcity to push its price up;
    and, in "Custody", market making along a bonding curve among its uses.
  - These are the theory's mechanism, stated as design arithmetic, untimed, with no project and no
    price.
- **Voshmgir** (*Token Economy*, second edition, 2020):
  - Part 2, "Monetary & Fiscal Policy of DAOs": reserve pools that fill or deplete through
    bonding-curve mechanisms among a network's fiscal variables; a bonding curve as a contract
    issuing its own tokens against collateral through buy and sell functions, in its simplest form
    an automated market maker, with qualities of both debt and equity; and bitcoin's supply fixed by
    its protocol before it was deployed — the theory's mechanism, untimed.
  - Part 3, "Token Sales": sales priced along a curve that changes over the sale, early buyers
    paying less when it rises, and continuous token models issuing and selling tokens over time —
    the bank's "found in some issuances", untimed.
  - Part 4, "Other Types of TCRs": continuous token-curated registries minting tokens along a
    predetermined curve; and, in "Behavioral Finance & Behavioral Game Theory", token bonding
    curves, like registries and algorithmic stable tokens, built on assumptions of rational agents
    that behavioural research says must be complemented — untimed.

**Return signs near the theory.**

- **Huang and others** (*Web3*, 2024):
  - Chapter 6, "The Tokenomics for Web3": sound designs aligning holders in a positive feedback loop
    of buying, holding and using, and poor ones dumping one round after another into a stampede —
    the theory's reflexivity and unstable exit, untimed; bonding curves among the components used to
    explain DeFi's token mechanisms.
  - Section 6.4.1: being early as the name of the game, holders of bitcoin from before 2016 hardly
    able to be at a loss — hindsight on the lab's own asset, a fixed stance, not a curve.
  - Section 6.4.2: early players paid by later ones, collapsing once inflows stop — untimed,
    **MR-023**'s form.
- **Harvey, Ramachandran and Santoro** (chapter VI, "DeFi Deep Dive"): Uniswap's pricing, which the
  authors call a bonding curve, leaving money for arbitrageurs on closely correlated pairs because
  it does not reshape its curve, and competitors such as Curve built for those pairs — the automated
  market maker's curve, **AS-044**'s form, untimed.
- **Off crypto**: Kyle's lambda, a price set linearly against the quantity traded, and its estimates
  for five Nasdaq stocks in 2013 (Cartea, Jaimungal and Penalva, *Algorithmic and High-Frequency
  Trading*, 2015, sections 2.1.3 and 4.3.5) — the market's curve, not a contract's, an untimed claim
  and a past estimate on stocks the lab does not hold, **MR-010**'s and **FP-003**'s form.

None gives a timed rule the lab could read.

## What the lab can read of it

The lab holds the daily bars and volumes of twenty-two funds and bitcoin — the funds from 2005 or
their later start, bitcoin from September 2014 — adjusted for dividends and splits, which encode the
funds' distributions, though no strategy reads them until a point-in-time reading with its own test
is built; the Treasury bill's yield from 2005 and two franc exchange rates; the funds' prices, never
their holdings' prices; and no token issued on a bonding curve, no curve parameter and no
reserve-pool balance; its snapshot is closed, an asset or a series being added only before the first
card. Nothing was computed from the bars for this judgement. On those data:

- **A bonding-curve token's price against its curve**, the claim and every refutation: the lab holds
  no such token. Bitcoin's supply is set by a schedule of issuance to miners, fixed in its protocol
  (Voshmgir, Part 2), not by a contract that mints and burns against buyers' payments, and its price
  is set only by the market — its issuance is **EF-044**'s form.
- **The funds**: their shares are created and redeemed at net asset value by authorised
  participants, a constant price in the supply — the simplest bonding curve, a peg with no
  first-entrant advantage and no convex or concave profile — so none of the theory's claims can be
  read on them; the tie to the basket is **LL-026**'s form, the flows **FP-014**'s and **FP-004**'s.
- **Dated events**: the library dates none on a token issued on a bonding curve. On contracts whose
  curve sets a price it dates about six inside bitcoin's in-sample years:
  - Bancor's token sale of June 2017 (Voshmgir, Part 3) and the front-running of its exchange, which
    priced tokens from each trade's size, documented in an article of 17 August 2017 (Harvey and
    others, chapter VII, note 14; Antonopoulos and Wood, *Mastering Ethereum*, 2018);
  - the continuous token-curated registry proposed on 21 October 2017 (Voshmgir, Part 4, reading
    list);
  - Balancer's bonding surface, dated 4 October 2019 by a note (Harvey and others, chapter VI);
  - Uniswap's third version, announced on 23 March and launched on 5 May 2021 (chapters VI and VII).
  
  None falls in the holdout. A rule entering and leaving bitcoin around them makes at most about
  thirteen decisions, short of gate 1's thirty whatever the prices (RUNBOOK step 9). With the dated
  articles of Voshmgir's reading list on token-curated registries, from September 2017 to July 2018,
  the count nears thirty. What settles it:
  - a rule on bitcoin alone breaks the RUNBOOK's rule of at least four assets, and gate 6 fails it
    whatever the prices;
  - no source gives bitcoin a sign around these events;
  - the exchanges' curves among them are **AS-044**'s form.
- **A fixed stance on bitcoin**, the early holder's that Huang and others describe, makes one
  decision.

**The bank's siblings, and how AS-040 differs.** AS-040 claims the price a contract's curve imposes
on a token's supply.
- **AS-044**, decentralised exchanges and automated market makers, the curve that prices a pool's
  trades rather than a token's issuance, a line Voshmgir's simplest bonding curve blurs.
- **AS-039**, algorithmic stablecoins, recorded not testable, minting and burning against a peg and
  a companion rather than along a curve.
- **EF-041**, dynamic tokenomics, whose token rewards its first participants in a loop between price
  and adoption.
- **AS-026**, token design, recorded not testable, of which issuance rules are one attribute.
- **AS-028**, vesting and unlocks, recorded not testable, supply released by schedule.
- **EF-044**, issuance and supply rules, which holds bitcoin's schedule and networks' reserve pools.
- **EF-043**, purpose-driven token value capture, what a curve's tokens are for.
- **MR-023**, positive feedback and Ponzi-like processes, and **FP-024**, positive feedback trading,
  the reflexivity without a curve.
- **MR-015**, downward-sloping demand curves, **MR-010**, temporary price pressure, and **FP-003**,
  metaorders, the price a market, not a contract, sets against quantity.
- **FP-014**, ETF flows through creation and redemption, and **FP-004**, open-end fund flows, the
  funds' own minting and burning at net asset value.
- **MR-025**, limits to arbitrage, which would let a curve's price stray from the market's.

All are untouched but AS-026, AS-028 and AS-039.

What would make it testable: at least four tokens issued on bonding curves, with their curves'
parameters, supplies, reserve balances and prices over the lab's years — outside the lab's data —
and a timed rule in the library.

## Status

AS-040 is recorded `not-testable`:
- its claim and every refutation read tokens priced by a bonding curve, and the lab holds none —
  bitcoin's supply follows a schedule, not a curve, and the funds' curve is flat;
- the library gives the curve's arithmetic, its mechanism and untimed signs, names no token issued
  on one, and dates a few events on contracts whose curve sets a price, too few to settle a rule and
  none with a sign for bitcoin;
- bitcoin alone breaks the rule of at least four assets.

No card is drawn, and no trial is spent.
