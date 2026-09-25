---
id: LL-023
title: Frog-in-the-pan
family: lead-lag and information diffusion
mechanism: [behavioural, information]
asset_classes: [stocks, equity indices, bonds, commodities, currencies]
horizon: [months]
data: [daily prices, analyst coverage]
status: tested-inconclusive
---

## Mechanism

The frog-in-the-pan describes slow diffusion caused not by a lack of information but by its low
salience. Two securities with exactly the same past return do not carry the same information if
their price paths were different: one asset may reach a given 12-month return through a regular,
smooth trend with few negative days, another through irregular, volatile jumps. Gray and Vogel (2016),
drawing on Bhattacharya, Li and Sonaer (2017), propose that the quality of the path matters as much as
the size of the move: the signal depends not only on how much the price rose but on how it rose.

The mechanism is limited attention; the library presents the frog-in-the-pan as a particular case of
slow information diffusion. When good or bad news arrives in small, continuous increments rather than as
a spectacular shock, investors underweight it more. A large, discrete piece of news attracts attention,
forces the information to be processed quickly and brings the price rapidly close to a fuller valuation.
A succession of small pieces of news, each unspectacular, attracts little attention individually: the
information arrives continuously but investors aggregate it poorly, so the price stays behind the value
implied by the flow of news and the full adjustment takes longer, because it never triggered immediate
attention; the trend persists. This is the image of the frog in water that heats slowly. Attention is
scarce, large events capture the screens, and gradual signals seep more slowly into portfolios and into
market narratives. The delay is not necessarily between two securities but between the information that
is available and its full incorporation into prices, and it is more likely where analyst coverage and
investor attention are weak.

A gradual rise spread over many days is read as the sign of information entering the market little by
little, of patient institutional accumulation or of a lasting buying pressure. A rise concentrated in a
few abrupt jumps looks more like a speculative episode, a lottery effect, a transient attention shock or
a microstructure effect, a move the market has already "seen" and whose continuation is not assured. The
shape of momentum thus indicates the nature of the traders involved and the likelihood that the trend
will continue, and it separates "healthy" trends from more fragile ones. Gray and Vogel link the idea
explicitly to information diffusion and to low analyst coverage. By analogy, the logic can extend to
futures markets when their trends are fed by a sequence of macroeconomic data, flows or public reports
rather than by a single shock.

## Prediction

At equal cumulative past return, securities with smooth, gradual paths (a high share of positive days,
returns not driven by a few outliers) show stronger and more persistent subsequent continuation than
securities whose past return came from a few large jumps: momentum is stronger when the information
behind it arrived gradually. With a 12-month formation period, the signal of the smooth-path winners
holds best over the following 3 to 6 months. The effect is more likely in stocks with low analyst
coverage and little investor attention. Gray and Vogel, citing Da, Gurun and Warachka, show that winners
whose path was smooth and continuous often persist more strongly than jumpy winners. The effect has been
documented mostly on stocks, in particular on US stocks; the path-quality effect is reported by
Bhattacharya, Li and Sonaer (2017) and is part of the momentum framework of Gray and Vogel (2016).

## What would refute it

- Past winners with smooth, continuous paths continuing no more than past winners with the same
  return built from a few jumps; no difference in subsequent returns between high and low shares of
  positive days among stocks with the same 12-month return.
- Information arriving in small continuous increments incorporated into prices as fast as the same
  information arriving in one large shock.
- A difference between smooth and jumpy winners that is no more present in stocks with little analyst
  coverage and investor attention than in other stocks.

## References

- Da, Z., Gurun, U. G. & Warachka, M. (2014). Frog in the Pan: Continuous Information and Momentum. Review of Financial Studies.
- Gray, Wesley R. and Jack R. Vogel (2016). Quantitative Momentum: A Practitioner's Guide to Building a Momentum-Based Stock Selection System, ch. 6 "Maximizing Momentum: The Path Matters", pp. 100-105; p. 93, pp. 100-103 on the mechanism and p. 121 for a practitioner summary; PDF pp. 111-124, notably PDF pp. 118-124, with the work of Z. Da et al. on the gradualness of the formation-period return cited at the opening of the chapter; chapters 4-5 on frog-in-the-pan and path dependency. Wiley.
- Bhattacharya, D., Li, W.-H. & Sonaer, G. (2017). Has Momentum Lost Its Momentum? Review of Quantitative Finance and Accounting.
- Ilmanen, A. (2011). Expected Returns: An Investor's Guide to Harvesting Market Rewards, remarks on the complementarity of slow and fast signals and on signal decay, PDF pp. 637-645. Wiley.
- Bali, T. G., Engle, R. F. & Murray, S. (2016). Empirical Asset Pricing: The Cross Section of Stock Returns, ch. 18 "Investor Attention", p. 481. Wiley.
