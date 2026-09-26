# AS-039-01 — Algorithmic stablecoins and mint-burn reflexivity: reasoning, not testable as a theory of its own

## The theory, and the forms its sources give it

AS-039 holds that an algorithmic stablecoin, stabilised by rules that mint and burn it against a
companion token or an auxiliary debt rather than by an external reserve, is reflexive: its peg rests
on the companion's expected value, which rests on the peg, so that it holds while confidence is
coordinated and breaks non-linearly when confidence fails, the arbitrage meant to stabilise it
turning into a self-reinforcing selling spiral once the companion's residual capitalisation is too
small; a long phase of apparent stability, then an abrupt break, of the Terra-Luna type. Its
refutations: algorithmic stablecoins keeping their peg through losses of confidence with no spiral
between the stablecoin and its companion; breaks caused by external shocks unrelated to the
mint-burn design and hitting reserve-backed stablecoins alike; arbitrage still stabilising the
system when the companion's capitalisation no longer suffices. The bank names crypto, over days and
months, and stablecoin prices, the companion's price and capitalisation, and mint and burn volumes;
its references are Voshmgir's *Token Economy*, whose second edition (2020) is the one the library
holds, not the third the bank names, Harvey, Ramachandran and Santoro's *DeFi and the Future of
Finance* (2021), Schianchi and Mantovi's *The Economics of Cryptocurrencies and Digital Money*
(2023; the bank says 2024), Caton's edited *The Economics of Blockchain and Cryptocurrency* (2022),
and two papers the library does not hold, Liu, Makarov and Schoar (2023) and Aldasoro, Mehrling and
Neilson (2023).

**Its sources, as the lab read them in the library.**

- **Voshmgir** (*Token Economy*, second edition, 2020, Part 3, "Algorithmic Stable Tokens"):
  Seigniorage Shares, proposed by Robert Sams in a paper of 24 October 2014, minting tokens when the
  price is above the peg and buying them back below it; TerraMoney among such tokens; mechanisms
  resting on unproven assumptions about contraction, and many economists holding that such tokens
  cannot work, since the method assumes unlimited growth, each contraction raising future supply and
  risking a death spiral in the price of its bonds; few such projects live, most of them volatile —
  the theory's mechanism, untimed.
- **Harvey, Ramachandran and Santoro** (*DeFi and the Future of Finance*, 2021):
  - Chapter III, "DeFi Infrastructure", section "Stablecoins": non-collateralised stablecoins
    expanding supply to holders when demand rises and issuing bonds when the price slips below the
    peg, Ampleforth and Empty Set Dollar live, and the lack of backing able to cause runs in
    contractions.
  - Chapter IV, "DeFi Primitives": minting and burning as a contract's actions, seigniorage models
    such as Basis and Empty Set Dollar minting above the peg and burning below it.
  - Chapter VII, "Risks": Basis forced to shut down for regulatory reasons in December 2018, its
    notes dated 13 December 2018, and an anonymous fork, Basis Cash, launched since ("Regulatory
    Risk"); the governance attack on True Seigniorage Dollar, a seigniorage token, on 13 March
    2021, recorded in AS-036-01.
  - These are the mechanism, untimed, and past episodes on tokens the lab does not hold.
- **Glasner** (chapter 3 in Caton, ed., *The Economics of Blockchain and Cryptocurrency*, 2022,
  section 7, "A Stable Cryptocurrency?"): Basecoin, renamed Basis, whose prospectus of 2017 raised
  $133 million and which never launched, its funds returned; its $1 peg to be defended by issuing
  new coins to its investors when demand rose and by selling discounted claims, redeemed in order,
  when the price fell below it, its viability resting on demand yielding enough seigniorage — the
  theory's mechanism, with its auxiliary debt, and a dated past episode on a coin that never traded.
- **Schianchi and Mantovi** (*The Economics of Cryptocurrencies and Digital Money*, 2023, section
  5.3.3, "Terra and Luna"):
  - Terra launched in January 2018 and its firm incorporated in April 2018, its white paper in April
    2019, and the algorithmic stablecoin UST announced in September 2020 with Luna as its companion;
  - a securities investigation in 2021, and Luna rising that year from under a dollar to almost
    ninety, UST reaching $18.7 billion;
  - in March 2022 a trader's bet against Luna and, within days, Jump Trading, one of Luna's
    investors, proposing to deploy bitcoin reserves should Luna fall; Luna's peak near $120 on 6
    April 2022 and its supply at a low at the end of April;
  - UST losing its peg on 7 and 9 May, news on 11 May of its founder's part in Basis Cash, Luna down
    96% and the chain halted on 12 May, exchanges stopping trading on 13 May, and South Korean
    authorities' concern at the end of May;
  - a deposit rate of 20% on UST sustaining the system only while confidence held (BIS, 2022);
  - these are the theory's past episode, dated to the day, on tokens the lab does not hold; and, in
    section 5.3.2, algorithmic stablecoins admitting no solid monetary analysis.

**Return signs near the theory.**

- **Huang and others** (*Web3*, 2024): LUNA soaring on a yield near 20% for stakers and collapsing
  in May 2022, its reliance on its own token to back UST making it vulnerable to its price, and a
  stampede of users withdrawing and selling as confidence eroded (section 7.2.3); UST's crisis
  beginning around 5 May 2022, a senator warning in the Financial Times on 6 May, and the Federal
  Reserve's report of 9 May (section 10.8); the European Central Bank's view that stablecoins lost
  their perceived stability (section 10.5.1) — a past episode and untimed claims, on tokens the lab
  does not hold.
- **Schianchi and Mantovi** (section 6.3): the Terra-Luna crack as an empirical rejection of
  stability, stablecoins lacking a complete plan for runs; and, off crypto, Diamond and Dybvig's
  model, in which depositors run on a sound bank for fear that others will (section 2.2.4) — the
  theory's multiple equilibria, untimed, on banks the lab does not hold.
- **Off crypto**: Soros's boom-and-bust cycles, a self-reinforcing trend between perception and
  fundamentals followed by a reversal, and his short of the pound in the crisis of 1992 (Pedersen,
  *Efficiently Inefficient*, 2015, sections 11.6 and 11.7); exchange-rate crises under fixed rates,
  the crisis of the European Monetary System in 1992, and Argentina's currency board from 1991 to
  2001, its peso rates rising as investors feared its end (Blanchard, *Macroeconomics*, 2017,
  chapter 20); and the counter-view that crypto firms, doing no maturity transformation, are not
  exposed to runs as banks are (chapter 18 in Chuen, ed., *Handbook of Digital Currency*, 2015) —
  untimed claims and past episodes on currencies the lab does not hold, no bank theory's form but
  **TM-036**'s and **FP-024**'s for Soros's feedback.

None gives a timed rule the lab could read.

## What the lab can read of it

The lab holds the daily bars and volumes of twenty-two funds and bitcoin — the funds from 2005 or
their later start, bitcoin from September 2014 — adjusted for dividends and splits, which encode the
funds' distributions, though no strategy reads them until a point-in-time reading with its own test
is built; the Treasury bill's yield from 2005 and two franc exchange rates; the funds' prices, never
their holdings' prices; and no stablecoin, no companion token and no mint or burn series; its
snapshot is closed, an asset or a series being added only before the first card. Nothing was
computed from the bars for this judgement. On those data:

- **The peg and the companion's spiral**, the claim and every refutation: the lab holds neither an
  algorithmic stablecoin nor its companion, and no reserve-backed stablecoin to set against it.
- **Bitcoin around dated events**: inside bitcoin's in-sample years the library dates about fifteen
  events on algorithmic stablecoins:
  - Sams's paper of October 2014 and Basecoin's prospectus of 2017;
  - Terra's launch in January 2018 and its firm's incorporation in April 2018;
  - Basis's shutdown on 13 December 2018;
  - Terra's white paper in April 2019 and UST in September 2020;
  - the investigation of 2021 and Basis Cash's launch;
  - True Seigniorage Dollar's attack on 13 March 2021;
  - the bet and the reserve proposal of March 2022;
  - Luna's peak on 6 April and its supply low at the end of April;
  - the collapse from about 5 to 13 May 2022, which gate 1 groups in one or two episodes;
  - the South Korean concerns at the end of May.
  
  Several are dated to the year alone. In the holdout it dates only regulatory sequels, from April
  2023 to 2024, among them the European Central Bank's call for stablecoin rules, dated July 2023 by
  its reference (Huang and others, section 10.5.1), and the regulatory events of section 10.8 that
  AS-037-01 counted. A rule entering and leaving bitcoin around the in-sample events makes at most
  about thirty-one to thirty-three decisions, fewer once grouped — around gate 1's thirty, so the
  count alone cannot settle it. What settles it:
  - a rule on bitcoin alone breaks the RUNBOOK's rule of at least four assets, and gate 6 fails it
    whatever the prices;
  - no source gives bitcoin a sign or a window around these events: Jump Trading's proposal to
    deploy bitcoin reserves should Luna fall is an untimed conditional, the library never saying
    they were sold, **FP-005**'s form; bitcoin's fall from a peak near $46,000 in April 2022 to
    under $17,000 at the year's end (Schianchi and Mantovi, section 1.1) is one move over months,
    and the same authors judge that the year's collapses did not seem to have undermined bitcoin's
    foundations by spring 2023 (section 1.1.2);
  - bitcoin's move would be contagion, **FP-006**'s, **FP-031**'s or **FP-005**'s form, not the peg.
- **The funds**: no fund holds a stablecoin or its companion, and the library gives no fund's move
  around Terra's events; a form on them would be **FP-006**'s contagion.
- **The franc's floor**: the one peg in the lab's data, EURCHF's at 1.20, held from 2011 by a
  central bank rather than by minting against a companion, is a conversion rate, not a traded asset,
  and broke once, in January 2015 (Carver, *Systematic Trading*, 2015) — one decision.
- **A fixed stance on bitcoin** makes one decision.

**The bank's siblings, and how AS-039 differs.** AS-039 claims the reflexive break of a peg held by
minting and burning against a companion.
- **AS-040**, bonding curves, a price set by minting and burning against supply, with which AS-039
  shares Harvey and others' primitives, and which lacks the companion token and the peg.
- **AS-037**, asset-collateralised stablecoins, and **AS-038**, crypto-collateralised stablecoins,
  recorded not testable, whose pegs rest on reserves; Schianchi and Mantovi call every token-backed
  stablecoin algorithmic, blurring the line with AS-038.
- **AS-029**, staking and slashing, and **AS-030**, the staking ratio, recorded not testable, which
  read Terra's yield.
- **AS-036**, governance tokens, recorded not testable.
- **MR-025**, limits to arbitrage, the theory's own mechanism.
- **FP-028**, stablecoin supply as buying power.
- **FP-005**, fire sales, the reserves that might be sold.
- **FP-006**, liquidity spirals and margin deleveraging, and **FP-031**, DeFi liquidation cascades,
  the spiral's spill-over.
- **FP-024**, positive feedback trading.
- **EF-041**, dynamic tokenomics, whose token value is called fundamental but reflexive.
- **TM-031**, behavioural herding, and **TM-011**, informational cascades, recorded not testable,
  the run's coordination and fragility.

All are untouched but AS-029, AS-030, AS-036, AS-037, AS-038, TM-011 and TM-031.

What would make it testable: algorithmic stablecoins with their companions' prices and
capitalisations and their mint and burn volumes over the lab's years — outside the lab's data — and
a timed rule in the library.

## Status

AS-039 is recorded `not-testable`:
- its claim and every refutation read an algorithmic stablecoin against its companion, and the lab
  holds neither;
- two of its references are not in the library, whose sources give the mechanism and Terra's and
  Basis's past episodes on tokens the lab does not hold;
- its dated events, about fifteen in-sample, give at most about thirty-three decisions, around gate
  1's thirty;
- bitcoin alone breaks the rule of at least four assets, and no source gives it a sign.

No card is drawn, and no trial is spent.
