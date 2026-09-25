# The trial registry

`trials.jsonl` holds every trial the lab has run, one line per variant of each run, and only
grows: a line is never changed or removed. No card runs while the file lacks a line that a
commit in the branch's history held, and a test checks the lab's own. The runner writes it
(`python -m lab.report`), and each run's lines are committed alone right after it. Never amend,
rebase or squash a commit of it, and when the lab runs in more than one clone, push that commit at
once: a rewritten history holds no trace of the lines it dropped, and only the clone that wrote
them can put them back. A merge of the file keeps both sides' lines, and nothing else: a line that
is not a registry line stops every run until it is removed.

Each line is a JSON object:

| Field | What it holds |
|---|---|
| `time` | When the run ended, in UTC; on the void lines of `python -m lab.registry void`, when the run began. Lines put back by `restore` keep their own. |
| `card`, `card_hash` | The card's id, and the SHA-256 of its file: a card runs once. |
| `variant`, `parameters` | The variant's rank on the card, the base first, and its parameters. |
| `snapshot`, `snapshot_hash` | The data snapshot's name, and a hash of the files its manifest lists; null on a void run written by `python -m lab.registry void`. |
| `commit`, `versions` | The code's commit, and the versions of Python and of the pinned libraries; null on a void run written by `python -m lab.registry void`. |
| `thresholds` | The version of the battery's thresholds; null on a void run written by `python -m lab.registry void`. |
| `sharpe`, `monthly` | The variant's monthly excess returns hedged of the benchmark, and their Sharpe ratio (the appraisal ratio); empty when the strategy could not run or never held an asset, or when a void run stopped before the battery computed them. |
| `gates`, `failed`, `survivor` | Each gate's result, the first gate failed, and whether gates 1 to 7 all passed, read from the gates. |
| `void` | Only on a void run, with no gates: why it is void (its strategy changed the lab as it ran, and its returns are kept; the run stopped or was interrupted; or no line of its run is in the registry or in the clone's copy, since it ended before it wrote them or they were lost). Its card has run. |

Gate 4 counts every trial here with returns, void runs' included, near-clones as one, and a card's
variant once: where two lines hold it, one with returns before one without, then the one this
clone's run wrote, then the one first committed. So a line written by hand and committed counts as
a run's over a run's line without returns when it has returns, in every clone, and beside a run's
line alike in returns, in every clone but the one that ran the card, when it was committed first.
Gate 6 compares a new survivor with every earlier one.

The clone keeps, in its git folder, the hash of every card whose run began and a copy of every line
its runs wrote. `python -m lab.registry restore` puts back the lines a commit held, or this clone
wrote, that the file lacks, and replaces by the run's line, or removes, any line not yet committed
that holds a card this clone ran and that its run did not write (an edit, a changed copy, a line
added by hand); where the copy holds no line of that card (the copy lost, emptied or older, or
lines written by hand for a run that wrote none), it refuses, names the card, and says how on.
`python -m lab.registry void` writes void lines for the runs this clone began that wrote no line,
and refuses while a run is going or such lines are in the file.
