# Alpha Factory

A systematic trading research lab that runs, and the blueprint of the factory it feeds.

| Wing | What it is |
|---|---|
| [`alpha-lab/`](alpha-lab/) | The research lab: a bank of more than 260 market theories, and a chain that turns one into a strategy, tests it through eight gates and writes its verdict, failures included. Built, and it runs. |
| [`factory/`](factory/) | The blueprint of an institutional systematic trading pipeline, from data foundation to strategy lifecycle: seven sections, 64 sub-sections, and the system view (architecture, interfaces, build sequence, stack). Designed, not built. |
| [`handoff/`](handoff/) | The contract between the two wings: what a complete strategy dossier contains. |

## In two minutes

**The lab** asks one question of every theory: does a strategy built from it earn more than its
benchmark, after costs, in a way luck cannot explain? A theory is picked from the
[bank](alpha-lab/bank/) and written as a hypothesis card, fixed before any return is computed so
that the test cannot be bent to fit the result, and kept in the registry by its hash, which anyone
can check against the card; the strategy is then coded and run through seven gates: hygiene,
economic edge, significance, multiple testing, stability, robustness, and a holdout sealed until
then and opened once. A survivor enters the eighth, paper trading, where its live signals must match
its backtest's. Every trial is kept in a registry that only grows, and the multiple-testing gate
judges each strategy against all of them: the more the lab tries, the higher the bar.

**The factory** is what a survivor meets next: the blueprint of the pipeline an institution would
run to take a strategy from its dossier to capital, re-validating it on its own data before any
money is at stake. The lab hands over a [strategy dossier](handoff/README.md); the factory would
admit it, improve it and judge it.

## What to check in five minutes

1. **The board**, [`alpha-lab/STATUS.md`](alpha-lab/STATUS.md): every theory of the bank, its
   status, and each strategy drawn from it with the gate it reached.
2. **One strategy, from theory to verdict**: time-series momentum in its plainest form,
   [TM-017-01](alpha-lab/strategies/TM-017-01-time-series-momentum/), stopped at gate 3. Its
   [theory](alpha-lab/bank/TM-017-time-series-momentum.md), its
   [reasoning](alpha-lab/strategies/TM-017-01-time-series-momentum/reasoning.md), its
   [card](alpha-lab/strategies/TM-017-01-time-series-momentum/card.yaml), its
   [code](alpha-lab/strategies/TM-017-01-time-series-momentum/strategy.py), its
   [notebook](alpha-lab/strategies/TM-017-01-time-series-momentum/report.ipynb) and its
   [verdict](alpha-lab/strategies/TM-017-01-time-series-momentum/verdict.md).
3. **The battery's calibration**, [`calibration.ipynb`](alpha-lab/calibration/calibration.ipynb):
   before judging any theory, the battery was run on strategies with no edge and with a planted
   one, on the real data, to measure how often it is fooled and how often it finds what is there.
4. **Paper trading**, the branch
   [`paper`](https://github.com/Sami-Andaloussi/alpha-factory/tree/paper/paper): the scheduled
   job's log and its page, one line per strategy and session.
5. **The factory**, [`factory/README.md`](factory/README.md): the pipeline in one drawing, then
   each section.

The [lab's README](alpha-lab/README.md) gives its gates, its data and its costs, and the
[runbook](alpha-lab/RUNBOOK.md) each step with its command.

## Author

[Sami-Andaloussi](https://github.com/Sami-Andaloussi)
