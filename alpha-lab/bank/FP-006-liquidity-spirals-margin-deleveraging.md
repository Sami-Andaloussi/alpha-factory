---
id: FP-006
title: Liquidity spirals and margin-driven deleveraging
family: flows and positioning
mechanism: [limits to arbitrage, flows, microstructure]
asset_classes: [stocks, equity indices, bonds, commodities, currencies, crypto]
horizon: [days, weeks]
data: [daily prices, margin requirements and haircuts, bid-ask spreads, fund flows, funding spreads, market volatility index, futures basis]
status: untouched
---

## Mechanism

A fall in prices can impair the funding capacity of leveraged investors, which forces further
sales, which push prices down again. The core of the mechanism is the interaction between market
liquidity (the ease of trading without moving the price) and funding liquidity (the capacity to
raise cash and meet margins). The capacity of traders and intermediaries to absorb orders depends on
their capital and on the margins they must post, and these margins depend in turn on the liquidity
and volatility of the asset. When volatility rises, required margins increase, haircuts tighten,
credit becomes scarce, and investors must shrink their balance sheets; higher margins reduce
traders' capacity to supply liquidity. Liquidating positions then worsens illiquidity, widens
spreads and raises price impact, which in turn tightens funding constraints further (Brunnermeier
and Pedersen 2009).

A spiral often starts from a modest initial shock. It gains strength when the price fall produces
losses, which trigger margin calls, deleveraging, capital withdrawals and a tightening of risk
management. The forced sales deepen the fall, which calls for still more sales, so that the price
comes to reflect balance-sheet constraints and the need to sell rather than fundamental information.
Pedersen describes the chain as losses, then higher margins, then funding problems, then reduced
positions, then prices further away from fundamentals; Shleifer shows the same logic in financial
crises and in the collapse of LTCM. The persistence of the fall is structural: even rational traders
are bound by the mechanics of margins and collateral, so the move is a consequence of the plumbing
of funding. A related channel is run risk in open-end funds and ETFs, where redemptions force fire
sales; swing pricing, redemption gates and redemptions in kind are the tools used to dampen it.

Capital is slow because it is financed, delegated and governed under constraints: haircuts, margin
calls, volatility, investor redemptions, concentration limits, mandates, aversion to drawdowns, or a
simple refusal to add to a risk that is already losing. When these constraints tighten, arbitrageurs
and value investors cannot step in at the moment assets become most obviously underpriced, and
assets can move further away from their value instead of returning to it at once. The spiral thus
creates overshoots, temporary imbalances that give way to convergence when the cycle turns: the
return to equilibrium comes only after funding stabilises, volatility falls, margins relax, forced
sellers are exhausted, or the holders of risk capital are recapitalised.

The same squeeze reorders relative prices, a flight to liquidity and to quality: when funding
tightens, risky, cyclical or less liquid assets fall abruptly in price relative to liquid,
high-quality assets. As margins rise, intermediaries shrink their balance sheets and investors face
redemptions, the arbitrageurs who would normally correct price gaps become forced sellers
themselves. Relative prices then move away from fundamental value, not because the information has
changed in proportion, but because the capacity to carry positions has disappeared, and the
dislocation persists precisely because the traders able to arbitrage it are constrained at the
worst moment.

The canonical formulation comes from leveraged markets; the constrained holders also include spot
portfolios held by investors financed with credit, institutions managing under risk limits, and
entities that reallocate mechanically when volatility or drawdowns cross set thresholds. In equities
this can involve hedge funds, prime-brokered books, risk-parity strategies, multi-asset trend
followers (CTAs) or desks bound by internal limits. In futures markets, where margin is structural,
the mechanism concerns in particular the episodes in which prices depart from no-arbitrage relations
such as bases and spreads. In crypto the logic is even more visible, through collateralised loans,
on-chain collateral, margin calls on centralised exchanges and chains of liquidations.

The spiral persists because risk is endogenous: prices do not merely reflect an outside shock, they
change investors' ability to hold their positions. Arbitrageurs may themselves be leveraged and so
unable to stabilise the market; counter-cyclical capital is missing precisely at the worst moment;
and the assets sold can end up in the same crowded hands. The intensity depends on how funding is
structured, on margins, on the liquidity of the underlying assets and on the tools available to
manage redemptions. The framework accounts for excessive sell-offs, post-panic rebounds, anomalies
in spreads during stress, and episodes in which mean-reversion strategies temporarily stop working
because they are themselves crowded and forced to liquidate.

## Prediction

Price declines in assets held by leveraged or risk-constrained investors are followed by rising
margins and haircuts, wider spreads, larger price impact and further declines, so that some
sell-offs turn into cascades, which can produce violent and persistent trends in periods of stress.
Assets with high common ownership are fragile, and initially local moves can spread to securities
that have no fundamental news of their own, and across markets. Deviations from value can widen
while funding constraints tighten, and close only after funding stabilises, forced sellers are
exhausted, volatility falls and margins relax; the largest deviations from value therefore often
appear in the worst liquidity environments. An asset under forced selling can stay under pressure
for longer than in ordinary conditions. The natural horizon of the spiral is days to weeks. The same
logic has been shown in financial crises and in the LTCM episode, and in crypto through collateral
liquidations and exchange margin calls.

In relative terms, during a contraction of funding, liquid and high-quality assets outperform risky,
cyclical and illiquid ones by more than the change in fundamentals would warrant; once the funding
constraint eases, the assets that were sold far below their fundamental value recover relative to
the liquid and high-quality ones. This relative pattern has been observed during liquidity crises
and during unwinds of quantitative strategies; it depends on the regime, and a dislocation can
deepen for a long time before it closes.

## What would refute it

- Margins, haircuts and spreads that do not rise as prices fall and volatility climbs; market
  liquidity that does not deteriorate together with funding liquidity in stress episodes.
- Price declines among leveraged holders that are not followed by forced deleveraging or further
  declines; price falls in stress periods that do not persist or accelerate as liquidity
  deteriorates; forced sales by funding-constrained intermediaries that leave no trace in prices.
- Crises in which liquidity provision is unaffected by the capital losses of intermediaries, or in
  which arbitrageurs keep providing liquidity during funding squeezes instead of becoming forced
  sellers.
- In funding contractions, relative prices of illiquid and risky assets that fall only in
  proportion to the deterioration of their fundamentals and do not recover once funding conditions
  ease; a relative underperformance of illiquid and risky assets in crises that is unrelated to
  rising margins, shrinking intermediary balance sheets or investor redemptions.
- Assets held mainly by unleveraged, unconstrained investors falling as much in sell-offs as assets
  held by leveraged ones.
- No contagion to securities without news of their own, and no greater fragility for assets with
  high common ownership.
- Cascades as frequent and as deep where funding is stable and redemption tools are in place as
  where funding is short-term and margins are tight.
- Deviations from value that do not widen when margins, haircuts or redemptions increase, or that
  show no rebound when volatility falls, margins relax and capital returns; deviations no larger in
  bad liquidity environments than in calm ones.

## References

- Brunnermeier, M. and Pedersen, L. H. (2009). Market Liquidity and Funding Liquidity. Review of Financial Studies.
- Garleanu, N. and Pedersen, L. H. (2011). Margin-Based Asset Pricing and Deviations from the Law of One Price. Review of Financial Studies.
- Adrian, T. and Shin, H. S. (2010). Liquidity and Leverage. Journal of Financial Intermediation.
- Pedersen, Lasse Heje (2015). Efficiently Inefficient: How Smart Money Invests and Market Prices Are Determined. Princeton University Press. Chapter 3, pp. 42-46; chapter 5, pp. 82-84; pp. 61-63 and p. 262.
- Shleifer, A. (2000). Inefficient Markets: An Introduction to Behavioral Finance. Oxford University Press. Chapter 4, "Professional Arbitrage", p. 98 ff., and pp. 106-120.
- Madhavan, A. (2016). Exchange-Traded Funds and the New Dynamics of Investing. Oxford University Press. Chapter 17, pp. 212-216.
- Arjaliès, D.-L., Grant, P., Hardie, I., MacKenzie, D. and Svetlova, E. (2017). Chains of Finance: How Investment Management is Shaped. Oxford University Press. P. 19 and pp. 64-70.
- Vayanos, D. and Wang, J. (2012). Theories of Liquidity. Foundations and Trends in Finance. Sections "Funding Constraints" and "Search".
- Amihud, Yakov, Haim Mendelson and Lasse Heje Pedersen (2013). Market Liquidity: Asset Pricing, Risk, and Crises. Cambridge University Press. Chapter 6, "Market Liquidity and Funding Liquidity", p. 212 ff.; section "Fragility and Liquidity Spirals", p. 229 ff.; chapter 8, "Slow Moving Capital", p. 274 ff.; Part III, "Liquidity Crises", pp. 201-245, notably pp. 205, 210, 217, 236 and 245.
- Ilmanen, Antti (2011). Expected Returns: An Investor's Guide to Harvesting Market Rewards. Wiley. Chapter 20, "Endogenous Return and Risk: Feedback Effects", pp. 519 and 524; chapter 20, "Endogenous Return and Risk: Feedback Effects on Expected Returns", sections 20.1-20.2, pp. 584-586.
- Lo, A. W. (2017). Adaptive Markets: Financial Evolution at the Speed of Thought. Princeton University Press. Chapter 8, "Adaptive Markets in Action", p. 263 ff., notably p. 286; chapter 9, "Fear, Greed, and Financial Crisis", p. 296 ff.
