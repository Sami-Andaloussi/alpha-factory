# AS-044-01 — DEX and AMM design, MEV extraction and DeFi token economics: reasoning, not testable as a theory of its own

## The theory, and the forms its sources give it

AS-044 holds that the tokens of decentralised exchanges and trading infrastructures inherit the
frictions, rents and vulnerabilities of their protocol's market design — an automated market maker
or an order book, the concentration of liquidity, the remuneration of liquidity providers, external
arbitrage, fee capture and the value extracted by validators or searchers — because the protocol
distributes or destroys value among traders, liquidity providers, arbitrageurs, validators,
developers and holders: fee capture supports the token only if it reaches holders, an automated
design attracts volume but imposes inventory losses on liquidity providers, and extraction raises
activity while taxing some users, with sensitivity to upgrades, fee changes and competition between
protocols. Its refutations: DEX tokens' prices unrelated to their protocol's design choices; tokens
whose protocol passes fees to holders behaving no differently from those whose protocol does not;
upgrades and fee changes causing no repricing. The bank names crypto, over days and months, and DEX
volumes, liquidity-pool data, protocol fee revenue, extraction data and daily prices; its references
are Capponi and Jia (2025), Azar, Casillas and Farboodi (2024) and Lehar and Parlour (2022), none of
which the library holds; Schianchi and Mantovi cite another paper by Capponi and co-authors, on
mining technology and decentralisation.

**Its sources, as the lab read them in the library.** The three references are not in the library,
and the lab does not read papers outside it. The library describes the mechanism:

- **Harvey, Ramachandran and Santoro** (*DeFi and the Future of Finance*, 2021):
  - Chapter IV, "DeFi Primitives": impermanent loss, the automated market maker selling the
    appreciating asset and buying the depreciating one, which fees must exceed for a liquidity
    provider to profit; the mempool's visibility letting miners and others front-run, which is legal
    in decentralised finance since all information is public; and tokens such as ZRX paying
    application fees, and a governance token used to pay fees that are burned, as MKR once was.
  - Chapter V: "vampirism", forks copying a platform to poach its liquidity with larger incentives —
    the competition between protocols the theory names.
  - Chapter VI, "DeFi Deep Dive": Uniswap v2's constant-product pricing, liquidity providers earning
    in proportion to volume, its exposure to front-running at users' expense, set against the
    illegal front-running of centralised finance, its pricing leaving money for arbitrageurs on
    closely correlated pairs, where Curve may take its liquidity, its copy by Sushiswap and its
    generalisation by Balancer; UNI released in September 2020, opening near three dollars, spiking
    above eight and settling at four to five, recorded in AS-031-01 and AS-036-01; front-running
    revenues grown from hundreds of thousands of dollars when first shown publicly in 2017 to
    hundreds of millions by mid-2021; and bitcoin reaching Ethereum's exchanges as a wrapped token
    ("Wrapped Bitcoin").
  - Chapter VII, "DEX Risk": liquidity providers exposed to impermanent loss and arbitrage when
    pooled assets move sharply; Uniswap's third version, launched on 5 May 2021 (announced on 23
    March, chapter VI), letting liquidity providers concentrate funds in a range, somewhat like
    limit orders.
  - These are the mechanism, untimed, and past episodes on tokens the lab does not hold; no price is
    given around v3's launch.
- **Huang and others** (*Web3*, 2024):
  - Section 7.2.1, "DeFi's Basic Applications": constant-product pools, slippage and price impact by
    pool size, front-running, illegal in traditional finance and hard to rule out in decentralised
    finance, sandwich attacks, arbitrage between decentralised and centralised exchanges on a
    bitcoin–ether pair, fees paid to liquidity providers and yield farming, and impermanent loss —
    the library's fullest account of the mechanism, untimed.
  - Section 5.4, "MEV Risks and Mitigation": extraction by reordering, front-running and
    back-running transactions, likened to a tax miners levy on traders and called a systemic issue
    for decentralised finance, and exchanges designed against it, by batch auctions among others —
    untimed, with no token price sign.
- **Li, Niyato and Han** (*Cryptoeconomics*, 2023, section 10.1.2, "Miner or Maximal Extractable
  Value"): the term coined by Daian and others in "Flash Boys 2.0"; miners and searchers reordering
  transactions, sandwich attacks on decentralised exchanges, total extraction near 700 million, and
  an upgrade of automated market makers against it; and extraction less likely on bitcoin's network,
  which lacks Ethereum's complexity and statefulness — the mechanism, untimed, and a reason bitcoin
  carries none of it.
- **Voshmgir** (*Token Economy*, second edition, 2020, Part 3):
  - "Decentralized Exchanges": exchanges with order books on the chain, slow and costly, thin and so
    prone to manipulation — the order-book design the theory sets against automated makers, untimed.
  - "P2P Lending Protocols": Uniswap's liquidity pools, trading without an order book, and its
    upgrade of 2020 to swap tokens directly — the design, untimed.
  - "Flash Attacks": bZx's attacks of February 2020, a flash loan used to move the price of a
    bitcoin-backed token on a thin decentralised exchange.
- **Antonopoulos and Wood** (*Mastering Ethereum*, 2018, chapter 9, "Race Conditions/Front
  Running"): front-running on the public mempool, with ERC20 approvals and Bancor's exchange as
  real-world examples, recorded in AS-040-01; and, in its chapter on decentralised applications,
  Bancor's funds taken through a compromised administrator's account, undated — the mechanism.

**Return signs near the theory.**

- **Huang and others**:
  - Section 6.3.3: UNI, carrying governance and utility, more sought after than single-function
    tokens, and tokens whose cash flows rest on revenue such as transaction fees — untimed,
    **AS-036**'s and **EF-042**'s form.
  - Section 6.3.4, "DeFi and Tokenomics Interplays": buybacks and burns, and rewards paid from pool
    fees or newly minted tokens — untimed, **EF-042**'s and **EF-044**'s form.
- **Harvey, Ramachandran and Santoro** (chapter VI): MKR's holders gaining from a healthy platform
  and weighing a dividend against a backlash, recorded in AS-036-01 — fee capture's sign, untimed,
  **EF-042**'s form.
- **Voshmgir** (Part 3): thin decentralised exchanges prone to manipulation — untimed.
- **Off crypto**:
  - a broker trading ahead of a client's order, which harms the trader before whose order it trades
    (Harris, *Trading and Exchanges*, 2003, section 7.5.1);
  - limit orders exposed to traders who act on news before the quotes are revised (Foucault, Pagano
    and Röell, *Market Liquidity*, 2013, section 6.4.1), the analogue of liquidity providers' losses
    to arbitrageurs;
  - exchanges turned into listed firms, the NYSE in 2006, whose choices of market structure serve
    their shareholders, with trading fees a large part of their revenue (same book, section 1.4) —
    the nearest analogue to a venue's owners capturing its fees, held by the lab only inside XLF;
  - batch auctions proposed by Budish, Cramton and Shim (2015) against the race for speed, cited by
    Huang and others (section 5.4).
  - These are untimed claims on order flow and venues the lab does not see, **FP-003**'s,
    **FP-007**'s, **MR-006**'s and **LL-038**'s ground.

None gives a timed rule the lab could read.

## What the lab can read of it

The lab holds the daily bars and volumes of twenty-two funds and bitcoin — the funds from 2005 or
their later start, bitcoin from September 2014 — adjusted for dividends and splits, which encode the
funds' distributions, though no strategy reads them until a point-in-time reading with its own test
is built; the Treasury bill's yield from 2005 and two franc exchange rates; the funds' prices, never
their holdings' prices; and no DEX token, no pool, fee or extraction data; its snapshot is closed,
an asset or a series being added only before the first card. Nothing was computed from the bars for
this judgement. On those data:

- **DEX tokens' prices against their protocol's design**, the claim and every refutation: a
  cross-section of DEX tokens with their pools and fees, of which the lab holds none; bitcoin
  reaches Ethereum's exchanges as a wrapped token (Harvey and others, chapter VI; Huang and others,
  section 7.2.1), and its own price carries no protocol's fees.
- **Dated events on decentralised exchanges and their extraction**: inside bitcoin's in-sample years
  the library dates about thirty:
  - Bancor's token sale of June 2017, the front-running of its exchange, documented in an article of
    17 August 2017, and front-running first shown publicly in 2017 (Harvey and others, chapter VI);
  - a flash-loan launch of 16 July 2018 and an article on Uniswap of 28 March 2019 (Voshmgir's
    reading list);
  - an article on front-running an oracle of 16 September 2019 (Harvey and others, chapter VII, note
    14), and Balancer's bonding surface, dated 4 October 2019, recorded in AS-040-01;
  - bZx's attacks of 14 and 18 February 2020 (Voshmgir, Part 3; Harvey and others, chapter VII),
    with five articles on flash loans from 17 to 27 February and one of 8 March 2020 (Voshmgir's
    reading list);
  - an article of 5 April 2020 on Uniswap's second version (Voshmgir's reading list), articles on
    automated makers of July and 11 August 2020 (Harvey and others, chapters VI and VII), and UNI's
    release in September 2020 (chapter VI);
  - a flash-loan vote on MakerDAO of 26 October 2020 (Huang and others, section 9.3.5);
  - the attack on Yearn.finance through flash loans across Compound, dYdX, Aave and Uniswap on 4
    February 2021 (Harvey and others, chapter VII);
  - True Seigniorage Dollar's governance attack of 13 March 2021, its tokens sold on Pancakeswap,
    recorded in AS-036-01; Uniswap v3's announcement on 23 March 2021 (Harvey and others, chapter
    VI); the DODO exchange's hack in March 2021 (Huang and others, section 7.3.1) and the DNS
    spoofing of Cream Finance and PancakeSwap the same month (section 7.3.2);
  - Uniswap v3's launch on 5 May 2021; front-running revenues of hundreds of millions by mid-2021
    (Harvey and others, chapters VI and VII);
  - pools of Belt Finance, Rari Capital and BurgerSwap manipulated with flash loans, dated only by a
    reference of 2021, and AnubisDAO's pool emptied 20 hours after its launch on 28 October 2021
    (Huang and others, section 7.3.1);
  - Beanstalk's governance taken by a flash loan in April 2022 (section 9.3.5) and Convex Finance's
    DNS hijacking in June 2022 (section 7.3.2).
  
  Several are dated to the month or the year alone, and those of February 2020 fall within days of
  one another, which gate 1 groups. In the holdout the library dates only a court's ruling on bZx's
  DAO of 27 March 2023 (Huang and others, section 7.3.2), **AS-036**'s form. A rule entering and
  leaving bitcoin around the in-sample events makes at most about sixty-one decisions, fewer once
  grouped — above gate 1's thirty, so the count cannot settle it. What settles it:
  - a rule on bitcoin alone breaks the RUNBOOK's rule of at least four assets, and gate 6 fails it
    whatever the prices;
  - no source gives bitcoin a sign or a window around them: they concern tokens the lab does not
    hold, bitcoin reaches Ethereum's exchanges as a wrapped token, and extraction is less likely on
    its own network;
  - the hacks, spoofing and flash-loan votes are **AS-036**'s and **FP-031**'s ground more than a
    protocol's design.
- **The funds' own market structure**: their shares trade on exchanges with dealers and authorised
  participants, not on automated pools, and their tie to their basket is **LL-026**'s form; exchange
  operators, whose fees are the nearest analogue to a protocol's, reach the lab only inside XLF, the
  financials fund.
- **A fixed stance on bitcoin** makes one decision, and a strategy on bitcoin alone breaks the
  RUNBOOK's rule of at least four assets.

**The bank's siblings, and how AS-044 differs.** AS-044 claims that a DEX token inherits its
protocol's market design.
- **EF-042**, fee and revenue capture, the value a protocol passes to holders; **EF-044**, issuance
  and monetary policy, liquidity-mining emissions and burns.
- **AS-026**, token design, recorded not testable, whose fee integration and redistribution among
  users, validators and developers AS-044 applies to exchanges; **AS-028**, vesting and unlocks,
  recorded not testable, UNI's treasury vesting; **AS-020**, two-sided platforms, recorded not
  testable, liquidity providers and traders as a platform's two sides.
- **AS-040**, bonding curves, recorded not testable, a curve pricing a token's issuance rather than
  a pool's trades.
- **AS-036**, governance tokens, recorded not testable, UNI's votes; **AS-031**, exchange listing
  shock, recorded not testable, UNI's listing.
- **AS-043**, blockspace scarcity, recorded not testable, the competition for inclusion that
  extraction exploits; **AS-042**, on-chain transparency, recorded not testable, the public mempool
  extraction reads.
- **LL-037**, fragmented crypto venues' price discovery, **MR-038**, crypto's segmentation across
  exchanges, **LL-038**, order-flow externality and fragmentation, and **LL-035**, latency lead-lag,
  the competition between venues.
- **FP-002**, dealer inventory pressure, and **MR-006**, adverse selection, liquidity providers'
  inventory losses to informed arbitrage; **MR-037**, temporary deviations from arbitrage prices,
  and **MR-025**, limits to arbitrage, the external arbitrage that restores a pool's price.
- **FP-031**, DeFi liquidation cascades.
- **FP-003**, metaorders and latent liquidity, the flows front-runners read, and **FP-007**,
  predatory trading.
- **LL-026**, ETF arbitrage through creation and redemption, the funds' own market structure.

All are untouched but AS-020, AS-026, AS-028, AS-031, AS-036, AS-040, AS-042 and AS-043.

What would make it testable: at least four DEX tokens with their pools, volumes, fee revenue and
extraction data over the lab's years — outside the lab's data, and most such tokens trading only
from 2020, too late to fill three of gate 5's in-sample blocks — and a timed rule in the library.

## Status

AS-044 is recorded `not-testable`:
- its claim and every refutation read DEX tokens against their protocol's design, and the lab holds
  no DEX token and no pool, fee or extraction data;
- its references are not in the library, which describes the mechanism untimed;
- the library dates about thirty events on exchanges and tokens the lab does not hold, at most about
  sixty-one decisions, a count that settles nothing;
- bitcoin alone breaks the rule of at least four assets, and no source gives it a sign around those
  events.

No card is drawn, and no trial is spent.
