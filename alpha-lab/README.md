# Alpha Lab

The research lab annexed to the factory. It takes a theory from its bank, turns it into a strategy,
tests it, and returns a verdict. A strategy that survives leaves as a dossier that meets the
[handoff contract](../handoff/README.md), and the factory re-validates it in depth.

**Every theory and every strategy is shown**, each strategy with its written trail, failures
included. The [status board](STATUS.md) lists them all.

## How a theory is processed

bank → pick → reasoning → hypothesis card, locked by a commit → build plan → strategy code, three
variants at most → the battery, gates 1 to 7 → notebook and verdict → paper trading, gate 8 →
dossier. The [runbook](RUNBOOK.md) gives each step and its command.

## The battery

Each gate removes one way of being fooled; every gate is computed every time, and the verdict is
the first gate failed.

| Gate | Protects against | Passes when |
|---|---|---|
| 1 · Hygiene | Look-ahead, bad data, too little evidence | For every variant, no look-ahead and no read of the bar it trades on, over 50 sessions where it sets a target and 50 where it holds; prices above zero, with no gap; 30 clustered decisions or more; 5 years in-sample or more |
| 2 · Economic edge | An edge explained by costs or by market exposure | Sharpe ratio of 0.4 or more, at least the benchmark's, with a positive alpha; at twice the costs, 0.3 or more and a positive alpha; costs a third of the gross Sharpe ratio at most |
| 3 · Significance | Luck; being paid only for being invested | Probabilistic Sharpe ratio of 0.95 or more, adjusted for autocorrelation; better than 90% of 1,000 placebos, the strategy's own weights and costs shifted a year or more over the whole period, where each asset trades on both days; an asset keeps its own weight where that day comes before its start, and the share of assets that do not trade yet takes the strategy's own weights of the day |
| 4 · Multiple testing | The best of many tries | Deflated Sharpe ratio of the edge, hedged of the benchmark, of 0.90 or more over every trial of the registry |
| 5 · Stability | An edge in one variant or one episode | The variants' blend passes gates 2 to 4, and its worst variant has a positive Sharpe ratio; alpha positive in 3 of 5 fixed periods, and without the year of its largest edge; a card that must choose, a walk-forward efficiency of 50% or more |
| 6 · Robustness | A peak, one asset, timing too tight, a clone | Median parameter neighbour at 0.7 of the base Sharpe ratio or more, none at ±25% below 0.5; each cluster left out keeps 0.5 or more; no asset above 30% of the profit; gate 2 still passes without bitcoin; one day late keeps 0.7 or more; correlation with earlier survivors of 0.7 at most |
| 7 · Sealed holdout | Bugs and large decay | 2023 to 2025, opened once: Sharpe ratio and alpha at the 10th percentile of in-sample 2.5-year windows or above, no hygiene break in any variant, and the holdout's prices above zero, with no gap |
| 8 · Paper trading | A strategy that behaves differently live | The same signals live as in the backtest, over two to four weeks |

Before judging any theory, the battery was run on cases whose truth is known, 200 draws of each
on the real data. Of 1,800 strategies with no edge, cheap or costly to trade, alone or the best of
ten, on assets that trade from the start or start late, or close to their benchmark, it passed 4
(5% of each kind is allowed). Of strategies given an edge whose returns, hedged of the benchmark,
have a Sharpe ratio of 0.8, it passed 86.5% (73% at 0.5) with no other trial in the registry, and
about half at best against 30 independent earlier trials. The
[calibration](calibration/calibration.ipynb) shows each case, gate by gate.

## Data, universe, costs

Daily bars from Yahoo Finance, adjusted for dividends and splits, 2005 to 2025, frozen in a dated
snapshot whose [manifest](data/manifest.json) holds a hash per file; the data itself stays out of
the repository. Twenty-two ETFs — the eleven sector funds, five broad indices, three Treasury funds,
gold, silver, a commodity basket — and bitcoin, whose signals are read a day late; the Treasury
funds, and the franc's rates against the dollar and the euro, were added before the first card, in a
folder of their own beside the snapshot. Long only, no leverage, multi-day holding. Costs of 5 bps
per side on ETFs and 20 bps on bitcoin. Returns are measured above the Treasury-bill rate, which
cash earns.

## Where things are

| Path | What it holds |
|---|---|
| [`bank/`](bank/) | The theories, one file each, described without judgment. |
| [`strategies/`](strategies/) | One folder per strategy: reasoning, card, build plan, code, notebook, verdict. |
| [`registry/`](registry/) | Every trial ever run, one line each; it only grows. |
| [`calibration/`](calibration/) | The battery tested against nulls and planted edges. |
| [`lab/`](lab/) | The code: data, engine, costs, statistics, battery, registry, report, status, paper trading. |
| [`templates/`](templates/) | The hypothesis card and the report notebook. |
