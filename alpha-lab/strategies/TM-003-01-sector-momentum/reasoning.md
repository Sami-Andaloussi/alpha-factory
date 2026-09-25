# TM-003-01 — Sector momentum: reasoning

## Why this theory now

TM-003 holds that momentum lives in industries as much as in single stocks: shocks to demand,
costs, regulation and technology hit whole industries, investors take them in slowly and by theme,
and the industries that led over the past months keep leading. Its source, Moskowitz and Grinblatt
(1999), ranks twenty US industries, each a value-weighted portfolio of its stocks, from July 1963
to July 1995, buys the top three and sells the bottom three, holds them for some months and
rebalances monthly. Ranked on the past six months and held for six (their Table III, the strategy
they call IM(6,6)), the winners beat the losers by 0.43% a month (t = 4.24), and most of it is on
the long side: the winners beat the middle three industries by 0.36% a month (t = 4.38), and the
middle beat the losers by 0.07% (t = 0.98), not significant. Skipping a month between the ranking
and the holding changes little (0.40%). Ranked on the past twelve months and held for six,
IM(12,6), the winners beat the losers by 0.53% a month and the middle by 0.38% (t = 4.59), the
long side with the highest t-statistic in the table.

The lab holds the industries' closest traded form: the eleven sector funds, each a capped
value-weighted basket of the S&P 500's stocks in its sector. CA-001-01 already ranked them, as one
of its three groups, on a different rule — the past year less its last month, the top third,
rebuilt each month — and its verdict records that the sectors earned nothing there, an appraisal
ratio of −0.07. This card tests the source's own form, which CA-001-01 did not: a ranking with no
month left out, three leaders, and six overlapping monthly tranches. Its parameters are the
source's, fixed before any run on them; CA-001-01's figure is a warning, not an input.

The bank's neighbours: **CA-001**, momentum within groups, sectors among them; **TM-001**, stock
momentum, which Moskowitz and Grinblatt find industry momentum largely explains; **LL-009**, the diffusion of
information within industries, the lead and lag this theory's persistence would come from.

**What this card does not test.** The theory also holds that industry momentum explains much of
stock momentum, and that a sector's less visible members follow its leaders with a delay. Neither
can be tested without stock data, which the lab does not hold. The verdict will speak only for the
continuation of sector returns.

## From the mechanism to a signal

- **The ranking.** On the first session of each month, each sector fund's return over the past
  `lookback` sessions, up to the session before, no month left out, as in the source's main table.
  A fund is ranked once it has traded that long.
- **The leaders.** The top three, as the source buys three industries; with eleven funds that is
  more than a quarter of them, where the source's three of twenty are 15%. The source reports that
  more industries on each side give "largely the same" results (its footnote 19). Before three funds
  are ranked, all of them are held.
- **The holding.** As in the source, a position is held for `hold` months and the portfolio is
  rebalanced monthly: each month's three leaders form a tranche, and the portfolio holds the last
  `hold` tranches in equal shares, so that about a sixth of it turns over each month, plus the resetting of drifted weights — the source
  estimates about 200% a year for IM(6,6).
- **Long only.** The source's long side carries most of the profit of both forms tested (0.36% of
  0.43% a month for IM(6,6), 0.38% of 0.53% for IM(12,6)): a long-only form keeps most of the
  evidence.
- **Two variants.** The base is IM(6,6), 126 sessions and six months, the source's main strategy;
  the variant IM(12,6), 252 sessions and six months, its strongest long side, outside the base's
  neighbours and unlike CA-001-01's monthly ranking with the last month left out. The source's
  strongest strategy overall, IM(1,1), is not taken: more than half its profit is on the short side,
  which the lab cannot hold; it vanishes when a month is skipped (0.01%, t = 0.03), so it lives
  wholly in the last month; and it lies outside the theory's horizon of three to twelve months, for
  which a one-month continuation would be the "short-lived artefact" the bank's refutation names.

## What the battery judges, and what to expect

The benchmark holds the sector funds that trade in equal parts, nine until September 2016: the
alpha is the leaders' edge over all the funds, winners included.

**The size predicted.** The source's long side earned 0.36% a month, about 4.3% a year, among
twenty industries in 1963–95. Here the winners are also in the benchmark, 3 of 11 of it where they
are 3 of 20 in the source, so that the winners' edge over the equal weight is about 8/11 of their
edge over the middle: about 3.1% a year. The lab's sectors are coarser than the source's industries
— eleven broad baskets — and its years come after the publication, when anomalies are often found
to weaken (McLean and Pontiff, 2016, measure returns about 26% lower out of sample and 58% lower
after publication); the card assumes half. It predicts an alpha of about 1.5 to 2% a year. The source's
long side moved by about 5.6% a year (0.36% a month over a t-statistic of 4.38 in 383 months);
at that tracking, the predicted alpha is an appraisal ratio of about 0.3.

**The test's power.** Over about 17 years in-sample, an appraisal ratio is measured to about ±0.24.
If the true ratio is the predicted 0.3, the clause refutes wrongly about 5% of the time; the
source's full size — its long side's t-statistic of 4.38 over 32 years is an annual ratio near 0.8
— would be refuted by the clause's weaker test (0.3 or less) about 2% of the time. Gate 4 counts
this card's two trials, which are unlikely to move with the earlier nineteen-fund cards: with about eight or
nine effective trials, about 0.37 is expected from the best by luck, and the edge would need an
appraisal ratio of about 0.68 to pass. A true 0.3 would pass gate 4 about 7% of the time; a true
0.8 about two times in three. The test can therefore show the source's size, and can refute an
edge near zero; the predicted, halved edge will most likely read as not proven.

**Risks named before the run.**

- **The 2009 momentum crash.** CA-001-01's and TM-024-01's verdicts record it on these funds:
  staples, utilities and health care, the crash's leaders, were held into the rebound of March to
  December 2009. With six-month tranches, those formed up to March 2009 are held until August: the
  2008–09 block is likely negative, and gate 5 needs three of the five blocks positive.
- **One fund, one year.** Energy in 2021–22 is the likeliest single source of profit, and the
  profit shares are counted in dollars on compounded value, so that the last years weigh most: one
  fund above 30% of the profit, and no alpha without the best year, 2022 likely, are real threats.
- **Gate 6's clusters.** The sectors are one cluster, the whole universe: the check of a cluster
  left out does not apply, and the verdict will say so.
- **The variant starts later.** It needs 252 sessions before it can rank, and holds nothing before
  February 2006, where the base starts in August 2005: the variant and the blend carry six months
  of cash in the base's period, a negligible effect.
- **Late funds.** XLRE trades from 2016-09-19 and XLC from 2018-06-19. For their first `lookback`
  sessions the benchmark holds them and the rule cannot rank them: a small mechanical difference.
- **Funds whose holdings changed.** Real estate left XLF in 2016, and XLC took its stocks from XLK
  and XLY in 2018: a fund's past return can reflect stocks it no longer holds, where the source's
  industries had no such breaks.

## Choices, and the options rejected

- **CA-001-01's ranking** (the past year less its last month, the top third): tested there.
- **A month left out** before the holding: the source's main table leaves none, and finds that for
  IM(6,6) leaving one out changes little.
- **Two leaders**, the source's 15% of eleven: three follows its count, and its footnote reports the
  count matters little.
- **A tranche rebalanced every six months** instead of overlapping tranches: the source rebalances
  monthly, holding each month's winners for six months.
- **Shorting the laggards**: the lab is long only; the source's own breakdown shows what that costs.

## Implementation

Long only, fully invested, eleven US sector funds, each with a European (UCITS) fund tracking the
same S&P sector index, rebalanced monthly on closes with the orders filled at the next close: the
ranking reads the session before, so a day of delay is built in, and gate 6 adds another. No fund
of the universe stops trading between 2005 and 2025; the rule for one that does is there for
gate 6's tests.
