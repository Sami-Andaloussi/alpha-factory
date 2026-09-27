# AS-043-01 — Blockspace scarcity and blockchain congestion: reasoning, not testable as a theory of its own

## The theory, and the forms its sources give it

AS-043 holds that a blockchain sells access to scarce block space as well as its token, so that a
layer-1 token's value depends on whether its block space is abundant, saturated, expensive or in
competition with layer-2 solutions: congestion raises fees, changes delays and the competition for
inclusion, and reshapes the token's utility, the fee revenue and security budget of its miners or
validators, and the arbitrage between uses of the same space — at once a sign of strong demand and
of a falling marginal utility. The scarcity is built by the protocol and cannot be arbitraged away
without changing the rules, adding capacity or moving activity to other layers. Its refutations:
token prices unrelated to congestion, fees or block fullness, in short peaks as in durable regimes;
among networks whose token pays for fees, prices unrelated to the state of their block space; rule
changes, capacity increases or migrations to other layers leaving the relation unchanged. The bank
names crypto, over days and months, and transaction fees, block fullness and daily prices; its
references are Zimmerman's *Blockchain Structure and Cryptocurrency Prices* (Bank of England, 2020)
and Cumming, Glatzer, Hendrickson and Luther's working paper *Block Fullness, Security, and the
Price of Bitcoin* (2025), neither of which the library holds.

**Its sources, as the lab read them in the library.** The two references are not in the library, and
the lab does not read papers outside it. The library describes the mechanism:

- **Hendrickson and Luther** (chapter 4 in Caton, ed., *The Economics of Blockchain and
  Cryptocurrency*, 2022):
  - Section 2: blocks capped at 1 megabyte, senders bidding with fees for inclusion when the network
    is congested, and bitcoin's daily mean fee, from an on-chain data provider, averaging 6 cents
    from July 2010 to July 2016, 18 cents in July 2016, $1.77 in July 2017, a peak of $55.83 in
    December 2017 "as a surge in price led to extreme congestion", $1.09 from July 2018 to July
    2020, $1.41 over the week ending 16 July 2020, $4.86 from August 2020 to January 2021, $20 from
    January to May 2021 and $18.03 over the week ending 12 May 2021 — dated regimes of congestion,
    told with the price leading the fees rather than following them.
  - Sections 1, 4 and 5: a model in which the fee decides whether bitcoin is held at all once fees
    alone pay the miners — a fee high enough leaving only currency held, one low enough only bitcoin
    — second layers such as Lightning cutting the cost per transaction, and fees too low to pay for
    security possibly leading sellers to refuse bitcoin; recorded in AS-021-01.
- **Cachanosky** (chapter 2 of the same book): the block's cap set for security, segwit working as
  if blocks grew from one to four megabytes, Lightning as a second layer, and transactions without a
  fee waiting days — the protocol's capacity, untimed.
- **Schianchi and Mantovi** (*The Economics of Cryptocurrencies and Digital Money*, 2023):
  - Section 1.1: segwit raising the limit to four megabytes in 2017, taproot adding capacity in
    2021, and fees as bids for block space.
  - Section 4.5, after Malik and others (2022): large miners leaving blocks partly empty to push
    users to compete on fees, bitcoin's throughput limited by the strategic play between miners and
    users, and miners preferring congestion to grow — untimed, with no price, **EF-047**'s,
    **FP-029**'s and **AS-035**'s ground.
- **Li, Niyato and Han** (*Cryptoeconomics*, 2023):
  - Section 1.2.3: Ethereum's growth held back by congestion and costly fees, and layer-2 networks
    such as Arbitrum moving work off the main chain — the migration the third refutation names,
    untimed.
  - Section 3.1.1.2: Ethereum's fee mechanism upgraded from 5 August 2021, burning part of each fee.
  - Section 5.2.2: miners putting higher fees first, small transactions waiting from 20 minutes to
    30 days, and a working fee market tied to a limit on block size — untimed.
- **Voshmgir** (*Token Economy*, second edition, 2020):
  - Part 1: fees rising with traffic, and, in "Protocol Forks & Network Splits", rising fees from
    congestion motivating the proposal to enlarge blocks that led to Bitcoin Cash's hard fork of
    July 2017, trading from 1 August 2017 at about $240 against bitcoin's $2,700, recorded in
    AS-036-01 — a past episode, the congestion's governance consequence.
  - Annex, "Blockchain Scalability Solutions": the trade-off between scale, security and
    decentralisation, blocks kept small so that weaker nodes can take part, and state channels,
    sidechains and sharding as ways out — untimed.
- **Antonopoulos and Harding** (*Mastering Bitcoin*, third edition, 2023): segwit, described in late
  2015 and activated in 2017 (chapters 6 and 12), with taproot in November 2021 (chapter 7); fee
  rates as bids for block space, a lower rate buying a longer wait (chapter 9); and Lightning's
  payment channels (chapter 14) — the mechanics, with no price sign.
- **Antonopoulos and Wood** (*Mastering Ethereum*, 2018): gas pricing each computation as a defence
  against denial of service, and the attacks of 2016, from block 2,283,397 on 18 September to block
  2,700,031 on 26 November, which made the network almost stall until hard forks repriced gas
  (Tangerine Whistle and Spurious Dragon in 2016), and Byzantium in October 2017 — past episodes on
  ether, which the lab does not hold.

**Return signs near the theory.**

- **Hendrickson and Luther**'s model: bitcoin held only while its fee stays low enough — an untimed
  sign on fees and bitcoin's use, set in the years after 2140 when fees alone pay the miners,
  **AS-021**'s and **EF-047**'s form.
- **Huang and others** (*Web3*, 2024):
  - Chapter 4: layer-1 scaling by larger blocks, segwit, sharding or new consensus, and layer-2
    solutions such as rollups and state channels (sections 4.2.2 and 4.2.3), larger blocks risking
    centralisation — the capacity side of the refutations, untimed, with no price.
  - Section 6.3.1: a pricing formula (Cong, Li and Wang, 2020) in which the token's price rises with
    users' need to transact, and a chain whose token and gas are too dear losing users to other
    chains — the second refutation's form, untimed, **EF-041**'s and **EF-037**'s.
  - Section 8.1: CryptoKitties congesting Ethereum around 2017 — a past episode on ether, with no
    price; and (section 6.3.2) an article of 4 August 2021 on Ethereum's London hard fork — ether's
    supply, **EF-042**'s and **EF-044**'s form.
- **Harvey, Ramachandran and Santoro** (*DeFi and the Future of Finance*, 2021): the gas price as an
  auction for inclusion in the next block, higher fees signalling higher demand, and keepers
  competing on gas (chapter IV); Ethereum's fixed block size limiting throughput, layer-2 use
  stagnant even as fees rose very high, and competing chains such as Polkadot, Zilliqa, Algorand and
  Solana (chapter VII, "Scaling Risk") — untimed, on ether, and against the migration the third
  refutation names.
- **Huang and others** (section 4.5.3) and **Antonopoulos and Harding**: bitcoin's Lightning Network
  moving payments off the chain for speed and low cost — undated, with no price.
- **Hendrickson and Luther** (note 4): pools restrained from a majority of the hash power by the
  risk to their own coins' value; and a majority pool able to hold back transactions and extort high
  fees (Bhaskar and Chuen, chapter 3, section 3.6, in Chuen, ed., *Handbook of Digital Currency*,
  2015) — the security side, **EF-047**'s and **AS-035**'s ground.
- **Burns** (chapter 5 in Caton, ed.): low-fee coins drawing users for remittances in Africa — the
  second refutation's form, untimed.
- **Off crypto**: storage near its upper limit bringing a deep contango, higher volatility and a
  negative skew, with oil's storage at Cushing, Oklahoma, effectively full in 2009 (Pirrong,
  *Commodity Price Dynamics*, 2011, section 3.5) — an untimed claim and a past episode on oil, which
  the lab holds only inside a commodity basket, nearest to **FP-034**, whose reference is Pirrong
  (2011).

None gives a timed rule the lab could read.

## What the lab can read of it

The lab holds the daily bars and volumes of twenty-two funds and bitcoin — the funds from 2005 or
their later start, bitcoin from September 2014 — adjusted for dividends and splits, which encode the
funds' distributions, though no strategy reads them until a point-in-time reading with its own test
is built; the Treasury bill's yield from 2005 and two franc exchange rates; the funds' prices, never
their holdings' prices; and no other cryptoasset and no on-chain series — no fee, block fullness,
mempool or hash rate; its snapshot is closed, an asset or a series being added only before the first
card. Nothing was computed from the bars for this judgement. On those data:

- **Prices against fees and block fullness**, the claim and the first refutation: both are on-chain
  series the lab does not hold; the library's fee figures are averages over windows and two single
  weeks, not a daily series, and a rule on bitcoin's own price or volume as a proxy for congestion
  would read the price the claim explains, which Hendrickson and Luther say led the fees in December
  2017.
- **Networks whose token pays for fees, compared**, the second refutation: a cross-section of
  layer-1 tokens, of which the lab holds one.
- **Capacity changes, migrations and dated congestion**, the third refutation: inside bitcoin's
  in-sample years the library dates about nineteen events:
  - on bitcoin, segwit's description in late 2015 and activation in 2017, the Bitcoin Cash split
    from 1 August 2017, and taproot in November 2021;
  - Hendrickson and Luther's fee figures — the rise of July 2016, July 2017, the peak of December
    2017, the calm from July 2018, the week ending 16 July 2020, the rises of August 2020 and
    January 2021, and the week ending 12 May 2021;
  - on ether, which the lab does not hold, the attacks from 18 September to 26 November 2016, the
    hard forks that repriced gas in 2016 and Byzantium in October 2017, CryptoKitties around 2017,
    and the London upgrade of 5 August 2021.
  
  Voshmgir's reading list on scalability adds five dated articles from January 2017 to June 2018.
  The halvings of July 2016 and May 2020 cut issuance, not capacity, and are **EF-044**'s form, not
  counted, as in AS-026-01. In the holdout the library dates only the halving expected in April or
  May 2024 (Antonopoulos and Harding, chapter 12; Voshmgir, Part 1, and Huang and others, section
  6.3.2, also date it to 2024), **EF-044**'s and **EF-047**'s form. A rule entering and leaving
  bitcoin around the in-sample events makes at most about forty-nine decisions, fewer once grouped —
  around or above gate 1's thirty, so the count cannot settle it. What settles it:
  - a rule on bitcoin alone breaks the RUNBOOK's rule of at least four assets, and gate 6 fails it
    whatever the prices;
  - no source gives bitcoin a sign or a window around these events — Hendrickson and Luther's sign
    on fees is untimed and set in the years after 2140, and their account of the peak has the price
    leading the fees;
  - the upgrades and the split are **AS-026**'s and **AS-036**'s forms, and ether's events belong to
    a token the lab does not hold.
- **The funds**: no fund's price carries a blockchain's fees or block space; the one capacity limit
  near their data, oil's storage, reaches the lab only through a commodity basket, and is
  **FP-034**'s ground.
- **A fixed stance on bitcoin** makes one decision, and a strategy on bitcoin alone breaks the
  RUNBOOK's rule of at least four assets.

**The bank's siblings, and how AS-043 differs.** AS-043 claims the value of the token as a function
of its block space's scarcity.
- **EF-046**, network operating health and fee support, fees as a floor under value; **EF-042**, fee
  and revenue capture, who receives the fees.
- **EF-047**, the proof-of-work security budget, which fees fund as issuance falls; **EF-044**,
  issuance and monetary policy, the halvings and ether's burn; **EF-045**, proof-of-stake valuation,
  fees and burns on staked networks.
- **EF-040**, token velocity; **EF-037**, network adoption; **EF-041**, dynamic tokenomics and
  adoption, users leaving a chain whose gas is too dear.
- **FP-029**, miners' selling pressure; **FP-034**, corners and squeezes, which exploit a limit on
  deliverable supply, the nearest capacity limit off crypto.
- **AS-021**, the native network token, recorded not testable, which pays for the network's security
  and holds Hendrickson and Luther's model; **AS-026**, token design, recorded not testable, which
  counted bitcoin's upgrades; **AS-036**, governance tokens, recorded not testable, which dated the
  block-size fork.
- **AS-042**, on-chain transparency, recorded not testable, whose series include the fees;
  **AS-044**, decentralised exchanges and maximal extractable value, the competition for inclusion.

All are untouched but AS-021, AS-026, AS-036 and AS-042.

What would make it testable: daily fee, block-fullness and mempool series for at least four layer-1
tokens, with their prices, over the lab's years — outside the lab's data — and a timed rule in the
library.

## Status

AS-043 is recorded `not-testable`:
- its claim and every refutation read fees and block fullness, which are on-chain series the lab
  does not hold, or a cross-section of layer-1 tokens, of which it holds one;
- its references are not in the library, which describes the fee auction and the limits on capacity,
  dates congestion regimes on bitcoin with the price leading the fees, and gives one untimed sign on
  fees, set in the years after 2140;
- its dated capacity changes and congestion, about nineteen in-sample and five more articles, make
  at most about forty-nine decisions, a count that settles nothing;
- bitcoin alone breaks the rule of at least four assets, and no source gives it a sign around those
  events.

No card is drawn, and no trial is spent.
