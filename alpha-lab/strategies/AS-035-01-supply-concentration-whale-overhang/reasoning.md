# AS-035-01 — Supply concentration, whale overhang and validator concentration: reasoning, not testable as a theory of its own

## The theory, and the forms its sources give it

AS-035 holds that an asset whose supply or validation power is concentrated among a few holders,
pools or validators carries a structural fragility of its own: its price is more sensitive to a few
actors' liquidity needs, to their coordination and to the market's view of how decentralised it
really is, and it trades at a premium or a discount tied to its holding structure, with
accelerations around governance events, bankruptcies, vesting, transfers to exchanges or known
sales; by analogy, it resembles blockholder and reduced-float effects on shares. Its refutations:
concentrated assets showing the same price dynamics as widely held ones; governance events,
bankruptcies, vesting, transfers to exchanges and known sales by large holders moving concentrated
assets no more than widely held ones; the measured concentration, once custodial addresses are
separated from economic owners, unrelated to price behaviour. The bank names crypto and stocks, over
days, months and years, and on-chain holder distributions, validator and mining-pool shares,
exchange flows and daily prices; its references are Makarov and Schoar's *Blockchain Analysis of the
Bitcoin Market* (2022), which the library does not hold, nor any of their papers — Schianchi and
Mantovi cite their BIS working paper on cryptocurrencies and decentralised finance (2022) —
Voshmgir's *Token Economy*, whose second edition (2020) is the one the library holds, not the third
the bank names, Li, Niyato and Han's *Cryptoeconomics* (2023) and Caton's edited *The Economics of
Blockchain and Cryptocurrency* (2022).

**Its sources, as the lab read them in the library.**

- **Voshmgir** (*Token Economy*, second edition, 2020): in Part 1, "Network Nodes", bitcoin's mining
  described by some as an oligopoly of a handful of pools; in Part 2, "The Myth of Decentralization
  & Trustless Networks", power gathering around the experts who shape upgrades, and, in "Off-Chain
  vs. On-Chain Governance", on-chain governance as plutocratic while holdings are uneven, 3.06% of
  bitcoin's addresses holding 95.66% of its supply when the chapter was written and the top hundred
  of TheDAO's 11,000 investors over 46% of its tokens in May 2016; in Part 4, Steemit, the top ten
  holders once controlling 79.3% of Steem Power and 85% of STEEM, and the Tron Foundation's takeover
  of Steemit Inc. in February 2020 with about a fifth of STEEM's supply, the community's soft fork
  against those tokens, its reversal early in March by exchanges voting with their users' tokens,
  and the hard fork into Hive in mid-March 2020 — static figures on addresses and a past episode on
  a token the lab does not hold, told as governance, with no price given.
- **Li, Niyato and Han** (*Cryptoeconomics*, 2023): the 51% attack, open to miners pooling more than
  half of the mining power (section 2.1, "Security Basics"), and a chain open to such attacks losing
  its value (section 7.2.3) — a security sign, untimed, **EF-047**'s form.
- **Alston** (chapter 7 in Caton, ed., *The Economics of Blockchain and Cryptocurrency*, 2022):
  proof of work gathering processing power into mining pools able in principle to redirect funds and
  weighing heavily in protocol votes; its note 13, the pools' stated incentive to keep the network
  trusted; and Hendrickson and Luther (chapter 4 of the same book, note 4), the risk of devaluing
  their own coins deterring pools from holding more than half the power — untimed claims, the last
  tying pools' restraint to their coins' value.
- **Schianchi and Mantovi** (*The Economics of Cryptocurrencies and Digital Money*, 2023, section
  4.4, "The Implications of Mining Pools"): GHash.io reaching 51% of the hashrate in July 2014, and
  pool sizes showing a mean-reverting pattern, no large pool staying dominant for long — a past
  episode before bitcoin's data begin in the lab, with no price given; Bhaskar and Chuen (chapter 3
  in Chuen, ed., *Handbook of Digital Currency*, 2015) tell the same pool's hold of 55% for about a
  day, and the calls to cap pools at 25%.

**Return signs near the theory.**

- **Huang and others** (*Web3*, 2024, section 6.3.2, "Token Distribution and Allocation"): a supply
  held by a limited group bringing price volatility, its major holders' dumping causing selling
  pressure and price drops — the theory's claim with its sign, untimed, with no measure or window,
  on tokens the lab does not hold; farmers dumping at the opening, with lock-ups and vesting as the
  remedy — **AS-028**'s form; groups quietly holding a disproportionate share to inflate a token and
  then offload it (section 6.4.1) — **FP-034**'s form; the European Central Bank's concern that
  Uniswap's tokens are concentrated among a few (section 10.5.2) — untimed.
- **Burniske and Tatar** (*Cryptoassets*, 2017): in chapter 11, section "Pumping, Dumping, and
  Cornering Cryptoassets", dash's masternodes and its instamine leaving about 15% of its supply
  floating and giving its masternodes the means and the incentive to corner it, and bitcoin's rich
  list, two addresses holding about 1.4% of the supply and 116 more about 19%, holders less able
  than dash's to push the price, one person possibly holding many addresses — an untimed claim on a
  token the lab does not hold and a static figure on bitcoin; in chapter 13, mining concentration
  measured by the Herfindahl-Hirschman index, bitcoin at times moderately concentrated, a chart the
  book does not tabulate; in chapter 15, the Winklevoss twins holding about 1% of all bitcoin in
  2013.
- **Chuen, ed.** (*Handbook of Digital Currency*, 2015): at least 55% of bitcoins dormant between
  2010 and 2013, hoarded for their expected rise (Tarasiewicz and Newman, chapter 10); a small float
  or a large pre-mine making a coin's market value easy to manipulate (chapter 5); bitcoin's
  ownership presumed concentrated among early miners and open to manipulation while it stays so (Mas
  and Chuen, chapter 21) — static figures before bitcoin's lab years and untimed claims.
- **On shares and funds**: closed-end funds with blockholders trading at an average discount of 14%
  against 4% for those without (Barclay, Holderness and Pontiff, in Minio-Paluello, chapter 12 in
  Keim and Ziemba, eds., *Security Market Imperfections in Worldwide Equity Markets*, 2000, section
  2.1.3) — the theory's discount tied to holding structure, a cross-section of funds the lab does
  not hold, **MR-026**'s form; small price reactions to block sales by large holders (Scholes, in
  Shleifer, *Inefficient Markets*, 2000, chapter 1) — the second refutation on single stocks,
  **MR-015**'s and **MR-010**'s form; large shareholders' trades followed by 0.7% of abnormal return
  over twelve months, against 5.0% for top executives (Singal, *Beyond the Random Walk*, 2003,
  chapter 7); a blockholder choosing between intervening and selling, the price revised when its
  exit is known, and short-run reactions to announced activism (Foucault, Pagano and Röell, *Market
  Liquidity*, 2013, section 10.3) — single stocks, **AS-010**'s form.
- **Gold's official holders**: central banks' sales depressing gold for many years before 2000,
  their sales capped in 1999 and again in September 2004, the cap contributing to a shortage
  (Heidorn and Demidova-Menzel, chapter 32, and Cai, Clacher and others, chapter 31, in Fabozzi,
  Füss and Kaiser, eds., *The Handbook of Commodity Investing*, 2008) — past episodes on an asset
  the lab holds through its gold fund, all dated before the lab's years.

None gives a timed rule the lab could read.

## What the lab can read of it

The lab holds the daily bars and volumes of twenty-two funds and bitcoin — the funds from 2005 or
their later start, bitcoin from September 2014 — adjusted for dividends and splits, which encode the
funds' distributions, though no strategy reads them until a point-in-time reading with its own test
is built; the Treasury bill's yield from 2005 and two franc exchange rates; the funds' prices, never
their holdings' prices; and no other cryptoasset, no on-chain series, no holder distribution and no
mining-pool share; its snapshot is closed, an asset or a series being added only before the first
card. Nothing was computed from the bars for this judgement. On those data:

- **Concentrated against widely held assets**, the claim and every refutation: a cross-section of
  assets with their holder distributions, of which the lab holds one token, bitcoin, and no
  distribution for it.
- **Bitcoin's concentration over time**: the library gives static figures — a rich list in a book of
  2017, an address share around 2020, a dormant share before 2014 — a pool-concentration chart it
  does not tabulate, and one pool episode in July 2014, before the lab's bitcoin data begin; a
  series of holders' or pools' shares over the lab's years is on-chain data the lab does not hold.
- **Large holders' dated events**, the theory's accelerations around bankruptcies, thefts and known
  sales: inside bitcoin's in-sample years the library dates about ten — the thefts from Bitfinex's
  custody in 2016 and Binance's in 2019 (Harvey, Ramachandran and Santoro, *DeFi and the Future of
  Finance*, 2021, chapter VII, "Custodial Risk"), Steem's takeover, reversed soft fork and Hive fork
  in February and March 2020, the exit of Chinese miners in 2021 (Schianchi and Mantovi, section
  1.1), and the failures of FTX in November 2022 and of Celsius, Three Arrows Capital and BlockFi in
  2022 (same book, section 1.1.2; Huang and others, chapter 7 and section 10.3) — most dated to the
  year alone; the Mt Gox failure of February 2014 and the Silk Road shutdown of October 2013, its
  coins seized by November (Chuen, ed., chapters 2 and 17) fall before bitcoin's data begin, and no
  sale or repayment of those coins is dated in the lab's years; in the holdout only the SEC's
  actions against two large exchanges in 2023, dated to no month (Huang and others, section 6.1.4).
  A rule entering and leaving around each on bitcoin makes at most about twenty-one decisions
  in-sample and three in the holdout, fewer if events fall within five sessions of one another,
  certain to fail gate 1's thirty whatever the prices (RUNBOOK step 9); a strategy on bitcoin alone
  also breaks the RUNBOOK's rule of at least four assets.
- **Gold's official holders**: the library's episodes end in 2004 and it dates no central bank's
  sale or cap inside 2005-2025, so no rule on the gold fund can be drawn.
- **Shares**: the lab holds funds, not their holdings, and the funds' creation and redemption tie
  their price to their holdings' value whoever holds them; blockholder and float effects on single
  stocks are **AS-010**'s, **AS-003**'s and **FP-011**'s, and the closed-end funds where the
  blockholder discount lives are not in the lab's universe and are **MR-026**'s.
- **A fixed stance on bitcoin** makes one decision.

**The bank's siblings, and how AS-035 differs.** AS-035 claims the premium or discount and the
fragility tied to how concentrated the holders are. **AS-028**, vesting and unlocks, recorded not
testable, supply released by schedule rather than held by a few; **AS-030**, the staking ratio and
the float's scarcity, recorded not testable, the float locked by staking; **AS-029**, staking and
slashing, recorded not testable, of which concentrated stake is one channel; **AS-036**, governance
tokens and voting design, the weight of large holders in votes; **AS-042**, on-chain transparency,
what the visible ledger reveals of large holders; **FP-005**, asset fire sales, large holders forced
to liquidate; **FP-034**, corners and squeezes, a dominant holder of the float; **FP-007**,
predatory trading, against a large holder's forced sale; **FP-027**, exchange reserves and on-chain
flows, transfers to exchanges; **FP-029**, miners' selling pressure, reinforced by pool
concentration; **FP-010**, common ownership and crowding; **MR-015**, downward-sloping demand
curves, and **MR-010**, temporary price pressure, the price of a large block; **MR-026**, closed-end
fund discounts, which the blockholder evidence prices; **EF-047**, the proof-of-work security
budget, what pays against a 51% attack; **EF-039**, the edge of decentralisation, the market's view
of it; **EF-043**, purpose-driven tokens' value capture, whose tokens can be held by a few;
**AS-010**, the separation of ownership and control, recorded not testable, blockholders on shares;
**AS-003**, lock-up expirations, recorded not testable; **FP-011**, index inclusion and float; all
untouched but AS-003, AS-010, AS-028, AS-029 and AS-030.

What would make it testable: many tokens with their holder distributions and mining-pool or
validator shares over the lab's years, with custodial addresses separated from owners — outside the
lab's data — and a timed rule in the library.

## Status

AS-035 is recorded `not-testable`: its claim and every refutation compare assets by the
concentration of their holders or validators, and the lab holds one token, bitcoin, with no holder
distribution and no pool shares; the library signs the claim untimed, gives static figures and
episodes before the lab's years, past episodes on tokens it does not hold, and a blockholder
discount on funds it does not hold; large holders' dated events on bitcoin are about ten in-sample
and one in the holdout, at most about twenty-one decisions; gold's official sales end before the
lab's years. No card is drawn, and no trial is spent.
