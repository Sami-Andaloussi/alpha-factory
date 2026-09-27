# AS-042-01 — Open data and on-chain transparency: reasoning, not testable as a theory of its own

## The theory, and the forms its sources give it

AS-042 holds that crypto stands apart through a public and granular information regime — addresses,
clusters, flows, the distribution of holdings, block explorers, sometimes governance and
participation, all observable almost in real time — which gives the market a source of repricing
that shares lack: it can quickly revise its view of adoption, concentration, the network's health or
custody flows, and the regime persists because the ledger is public by design. The theory does not
claim that every on-chain metric predicts. Its refutations: changes visible on public ledgers in
adoption, concentration, network health or custody flows not moving prices; on-chain information
carrying nothing about holders' economic behaviour once exchanges, custodians and smart contracts
are accounted for. The bank names crypto, intraday and over days, and on-chain data, address
clusters, custody flows and daily prices; its references are Burniske and Tatar's *Cryptoassets*
(2017), Voshmgir's *Token Economy*, whose second edition (2020) is the one the library holds, not
the third the bank names, and Antonopoulos's *Mastering Bitcoin*, whose third edition (2023, with
Harding) is the one the library holds, not the second the bank names.

**Its sources, as the lab read them in the library.**

- **Burniske and Tatar** (*Cryptoassets*, 2017, chapter 2): a study grouping bitcoin's addresses
  into "super clusters" of business entities and mapping their payments from 2009 to 2015, finding
  three regimes, from a prototype through a stage of gambling and black markets to one moving away
  from them — what the public ledger lets an analyst see, with no price sign.
- **Voshmgir** (*Token Economy*, second edition, 2020):
  - Part 1, "Block-explorer": anyone able to run analyses on the whole ledger, though few have the
    skills to — a limit on how fast the ledger's news is read.
  - Part 3, "Privacy Tokens", "Privacy of Blockchain Tokens": exchanges sharing data with
    law-enforcement agencies and chain-analysis firms, simple chain analysis correlated with a
    user's footprint off the chain able to single out identities, forensic services detecting
    transaction patterns, and tokens refused for a tainted history, which lowers their fungibility;
    mixers and privacy tokens built against it.
  - Part 4, "Criticism of Steemit": all of Steem's transaction data public and open to simple chain
    analysis, yet its distribution poorly documented, the rich lists abandoned and the only reliable
    figures years old.
  - These are the open ledger as a source of information, and its limits, with no price.
- **Antonopoulos and Harding** (*Mastering Bitcoin*, third edition, 2023): bitcoin's privacy when
  used correctly (chapter 1); a block explorer showing transactions, their relationships and flows
  (chapter 2); addresses and their reuse (chapters 4 and 5) — the mechanics of what is visible, with
  no price sign.
- **Chuen, ed.** (*Handbook of Digital Currency*, 2015):
  - Bhaskar and Chuen (chapter 28, "Bitcoin Exchanges", section 28.5, "Discussion"): bitcoin's
    ledger, each transaction announced publicly, more transparent than fiat transactions or
    over-the-counter products, and a regulated stock exchange's depository revealing far less of
    trading patterns — the theory's comparison with shares, stated directly; academics modelling
    behaviour from the ledger, with two phases of the network (Kondor and others, 2014), addresses
    per entity up to May 2012 (Ron and Shamir) and dormant coins settling near 60% (Ober and others)
    — untimed, before the lab's years, with no price sign.
  - Lam and Chuen (chapter 1, section 1.4.7, "Pseudoanonymity"): addresses linked to one another and
    to identities by clustering — the analyst's tools, untimed.
  - Bhaskar and Chuen (chapter 3): proofs of solvency, verifiable from anywhere and limited to
    bitcoin reserves, shown by Kraken, Bitfinex and Bitstamp, and proofs of reserves sought by
    clients since Mt Gox's demise, dated only by a reference of March 2014, before bitcoin's data —
    the custody-flow disclosure the theory names, with no price.
- **Huang and others** (*Web3*, 2024): on-chain data as a source (section 1.1.11); analytics
  platforms gathering, identifying, clustering, modelling and visualising on-chain data for
  agencies, exchanges and institutions (section 2.1.1); and, in the appendix to chapter 7 (7A.1),
  real-time wallet and swap alerts and indicators such as coin days destroyed, the Puell multiple
  and unrealised profit and loss — the tools, untimed, with no sign.

**Return signs near the theory.**

- **Burniske and Tatar** (chapter 13, "Operating Health of Cryptoasset Networks and Technical
  Analysis"):
  - Network value divided by daily transaction volume as a crypto "PE ratio", bitcoin appearing to
    rest near fifty times its daily volume, wide swings from it possibly signalling bearish or
    bullish trends, a price rising without volume possibly signalling overvaluation — a sign read
    from on-chain volume, untimed and read off a chart, **EF-040**'s and **EF-046**'s form.
  - Users, transactions and their dollar value as measures of adoption, and an exchange such as
    Coinbase holding only a handful of addresses for millions of users — untimed, and the custodial
    confound of the second refutation.
  - Hash rate often following price, and sometimes price following hash rate — an untimed lead and
    lag on an on-chain series, **EF-047**'s form.
- **Huang and others** (section 6.3.2): a concentrated distribution bringing volatility when its
  holders sell, and a deeper probe possibly revealing a more decentralised one — recorded in
  AS-035-01, **AS-035**'s form.
- **Hendrickson and Luther** (chapter 4 in Caton, ed., *The Economics of Blockchain and
  Cryptocurrency*, 2022): bitcoin's daily mean fee, from an on-chain data provider, peaking in
  December 2017 as a surge in price brought extreme congestion — the price leading the ledger,
  **AS-043**'s and **EF-046**'s form.
- **Off crypto**: insiders' large trades reported to the regulator within two business days since
  September 2002, so that outsiders can mimic them, and large shareholders' trades followed by 0.7%
  of abnormal return over twelve months against 5.0% for top executives (Singal, *Beyond the Random
  Walk*, 2003, chapter 7), recorded in AS-035-01; and managers' holdings disclosed in Form 13F
  filings, a portfolio mimicking Berkshire Hathaway's a month after each disclosure beating the
  market by about 14% a year from 1976 to 2006, the market slow to absorb what was disclosed (Martin
  and Puthenpurackal, in Gray and Carlisle, *Quantitative Value*, 2013, chapter 9) — a timed rule on
  single stocks the lab does not hold; both are disclosure regimes slower than a public ledger.

None gives a timed rule the lab could read.

## What the lab can read of it

The lab holds the daily bars and volumes of twenty-two funds and bitcoin — the funds from 2005 or
their later start, bitcoin from September 2014 — adjusted for dividends and splits, which encode the
funds' distributions, though no strategy reads them until a point-in-time reading with its own test
is built; the Treasury bill's yield from 2005 and two franc exchange rates; the funds' prices, never
their holdings' prices; and no on-chain series — no address, cluster, transaction count or volume,
custody flow or hash rate — and no intraday bar; its snapshot is closed, an asset or a series being
added only before the first card. Nothing was computed from the bars for this judgement. On those
data:

- **Prices against on-chain changes**, the claim and every refutation: every one reads a series from
  the public ledger, and the lab holds none; bitcoin's exchange volume in its bars is trading on
  venues, not transactions on the chain.
- **Crypto's information regime against shares'**: a comparison of how fast prices revise on each,
  which needs the on-chain news themselves and intraday prices; the lab holds daily bars only.
- **Dated events**: the one ledger disclosure the library dates, Mt Gox's move of 424,242 bitcoins
  to one of its addresses in 2011 to prove it was in control (Chuen, ed., chapter 28, section
  28.3.1), falls before bitcoin's data. Inside bitcoin's in-sample years it dates about twenty-eight
  events whose flows were visible on a ledger, none of them a disclosure:
  - the large holders' and platforms' events counted in AS-035-01 and AS-032-01, about fifteen once
    merged — the thefts from Bitfinex's custody in 2016 and Binance's in 2019, an exchange hack in
    2018, China's investigation of its exchanges from 6 January 2017, an exchange's client funds
    frozen by mid-2018 and its New York settlement in April 2019, Steem's takeover and Hive fork in
    February and March 2020, the exit of Chinese miners in 2021, and the failures of FTX in November
    2022 and of Celsius, Three Arrows Capital and BlockFi in 2022;
  - exploits drained through contracts: TheDAO on 17 June 2016 (Harvey, Ramachandran and Santoro,
    *DeFi and the Future of Finance*, 2021, chapter VII); bZx's two attacks of February 2020
    (Voshmgir, Part 3; Harvey and others, chapter VII); dForce's Lendf.Me in April 2020 and Yearn
    Finance in February 2021 (same chapter, "Smart Contract Risk"); True Seigniorage Dollar on 13
    March 2021, recorded in AS-036-01; the DODO exchange in March 2021 (Huang and others, section
    7.3.1); the Poly Network and Punk Protocol in August 2021, a bZx developer's key in November
    2021 and the Slope wallet in August 2022 (section 7.3.2); the Ronin bridge, the largest attack
    by April 2022 (section 5.3.2); and Beanstalk's governance in April 2022 (section 9.3.5), where
    Huang and others date a few more attacks of 2020 and 2021.
  
  Most are dated to the month or the year alone. In the holdout it dates only the SEC's actions
  against two large exchanges in 2023, dated to no month (Huang and others, section 6.1.4). A rule
  entering and leaving bitcoin around the in-sample events makes at most about fifty-seven
  decisions, fewer once grouped — above gate 1's thirty, so the count cannot settle it. What settles
  it:
  - a rule on bitcoin alone breaks the RUNBOOK's rule of at least four assets, and gate 6 fails it
    whatever the prices;
  - no source gives bitcoin a sign or a window around these events;
  - the events are **AS-035**'s, **AS-032**'s, **AS-036**'s, **AS-044**'s and **FP-031**'s forms —
    large holders, platforms, governance and contracts — not a repricing on what the ledger
    disclosed.
- **The funds**: the lab's index funds publish their holdings every day (Abner, *The ETF Handbook*,
  second edition, 2016), the nearest thing it has to a public ledger, but it holds their prices, not
  their holdings; their tie to the basket is **LL-026**'s form and their flows **FP-014**'s.
- **A fixed stance on bitcoin** makes one decision, and a strategy on bitcoin alone breaks the
  RUNBOOK's rule of at least four assets.

**The bank's siblings, and how AS-042 differs.** AS-042 claims that the public ledger itself is a
channel of repricing, where its siblings each claim what one on-chain measure or one kind of event
predicts.
- **FP-027**, exchange reserves and on-chain net flows, the custody flows.
- **EF-037**, network adoption and Metcalfe valuation; **EF-038**, crypto's value premium on active
  addresses; **EF-040**, token velocity, which names the ratio of network value to transactions;
  **EF-046**, network operating health and fees; **EF-047**, the proof-of-work security budget,
  which reads hash rate.
- **EF-036**, utility against speculative value; **EF-039**, **EF-041**, **EF-043** and **EF-045**,
  which read on-chain data for token value.
- **FP-028**, stablecoin supply; **FP-029**, miners' selling; **FP-031**, DeFi liquidation cascades,
  on-chain lending positions; **FP-010**, which reads on-chain holdings.
- **AS-035**, supply concentration, recorded not testable, what the ledger shows of holders;
  **AS-032**, exchange clientele comovement, recorded not testable; **AS-031**, exchange listing
  shock, recorded not testable; **AS-021**, the native network token, recorded not testable.
- **AS-043**, blockspace scarcity, fees and block fullness; **AS-044**, decentralised exchanges and
  extraction, which read pools on the chain.
- **TM-007**, underreaction to public information, and **TM-008**, gradual information diffusion,
  recorded not testable, the speed of repricing the theory claims.

All are untouched but AS-021, AS-031, AS-032, AS-035, TM-007 and TM-008.

What would make it testable: on-chain series — addresses, clusters, flows, holdings — for at least
four tokens, with prices timestamped finely enough for the intraday claim, over the lab's years —
outside the lab's data — and a timed rule in the library.

## Status

AS-042 is recorded `not-testable`:
- its claim and every refutation read changes on the public ledger against prices, and the lab holds
  no on-chain series and no intraday bar;
- the library shows what the ledger reveals, states the comparison with shares untimed, and gives
  untimed signs on on-chain volume and hash rate, which belong to its on-chain siblings;
- the one ledger disclosure it dates falls before bitcoin's data; the events it dates in the lab's
  years, about twenty-eight in-sample, belong to other theories and give bitcoin no sign;
- bitcoin alone breaks the rule of at least four assets.

No card is drawn, and no trial is spent.
