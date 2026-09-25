# Runbook

How one theory is processed, from the bank to its verdict. Each step leaves a file in the
strategy's folder, and every file speaks about the theory, the market and the strategy.

## Once

From the repository's root: `uv venv --python 3.14 .venv` and `uv pip install -r
alpha-lab/requirements.txt`: the runner refuses libraries other than these pinned versions. Every
command below runs from `alpha-lab/` with `../.venv/bin/python`.

The data is not in the repository. A run needs the snapshot that `data/manifest.json` names, in
`data/<snapshot>/`, and the folder of each addition it lists, with the same hashes: on another
machine, copy those folders from the one that froze them. A new download would be a new snapshot,
with a new manifest, and the lab's results belong to the snapshot they ran on. An asset or a rate
the universe gains before the first card is frozen by `python -m lab.data extend` in a folder of
its own, beside the snapshot, whose files never change.

| Command | What it does |
|---|---|
| `python -m lab.data check` | Verifies the snapshot `data/manifest.json` names and its additions: their hashes, the first sessions, the findings. |
| `python -m pytest` | The lab's tests. |
| `python -m lab.calibration` | Calibrates the battery again (about twenty minutes on nine workers); needed whenever the battery changes. |
| `python -m lab.status` | Regenerates the board, `STATUS.md`; every run does it too, and the tests refuse a board out of date. |
| `python -m lab.bank` | Checks every theory file of `bank/` and regenerates the bank's index, `bank/README.md`; the tests refuse an index out of date. |
| `python -m lab.compare strategies/<card> strategies/<reference>` | The card's alpha less the reference rule's, over the card's in-sample sessions from the first its base holds an asset into, at the lab's stated costs, with the standard error of the monthly differences, and the two appraisal ratios' difference with its standard error from paired draws of whole months — the measures of a card judged against a rule it refines. Refused until both cards have run as they stand, so it cannot size a band before a run. |

## One theory, step by step

1. **Pick.** Choose a theory whose status is `untouched` in `bank/`, set it to `in-progress` in
   its file, and run `python -m lab.bank` and `python -m lab.status`: the bank's index and the
   board show the status too, and the tests refuse either out of date. Read the files that share
   its references or its mechanism as well: the bank keeps the source's distinctions, so some of
   its theories are variants of one another (one premium on another universe, anchor or
   condition), and the reasoning says how this one differs.
2. **The folder**: `strategies/<theory-id>-<nn>-<slug>/`, `<nn>` counting the strategies drawn
   from the theory, from `01`. The folder's name is the card's id, and an id is used once.
3. **Reasoning**, `reasoning.md`: why this theory now; how its mechanism becomes a signal; each
   choice with its reason; the options rejected, and why.
4. **Hypothesis card**, `card.yaml`, from `templates/card.yaml`: the mechanism, the prediction
   (sign and rough size), the universe, the horizon, the signal, the parameters, three variants at
   most with the base first, and what would refute it.
   - Every numeric parameter of the base variant has its neighbours for gate 6: two values at
     ±25% and two at ±50% of the base, one on each side. A whole number, written without a
     decimal point (`2`, not `2.0`), takes whole numbers, the values rounded; a base of 1 takes 2
     alone at both steps, since 0 counts nothing and a lag of 0 reads the bar it trades on; a small
     count may take the same neighbours at both steps (3 takes 2 and 4). A real number (`0.5`,
     `2.0`) takes values within 1% of the base from those asked for: a count written `2.0`, which
     the strategy rounds with Python's `round()`, half to even, holds the base itself at 1.5 and
     2.5. A neighbour whose targets are the base's on every session from the base's first holding
     tests nothing: gate 6 fails it, and `--try` warns of it, once the card is locked. So move a
     parameter whose ±25% neighbours change the targets: on a rule whose targets change only a few
     dozen times in-sample (a slow signal against the parameter moved, a monthly or slower pace, a
     pick at an extreme rank), a span of 8 or 12 around 10 may change none of them. A number is
     written as a number, never as text, which gate 6 would not move.
   - The universe holds four assets at least, each named once: with three or fewer, one of them
     always carries more than 30% of the profit, and gate 6 fails whatever the edge. A theory about
     one asset is tested across several, or is `not-testable`.
   - Parameters are numbers, text or lists of them.
   - `memory`: the sessions the signal reads back from the session before a target, over every
     variant — the longest window, lags included; 252, a year, when left out. Gate 3's placebos
     shift the strategy's weights in time circularly, so that past the wrap a placebo holds weights
     set later than the day it is paid on: the shifts keep the memory and two sessions between them,
     so that no placebo holds weights whose signal read that day. Gate 1 checks the memory: the
     targets must not change when the prices older than it are scrambled, and `--try` warns before
     the run. A rule that reads its whole history — an expanding average, or an exponential one,
     which pandas computes over the whole series — reads further back than any memory; it bounds its
     window instead. Two gaps the check does not see: a rule that goes more than a year without
     setting a target holds weights drifted by the returns since, and the bill rate is not
     scrambled; a card whose signal does either declares a memory that covers it.
   - What would refute it: a clause that asks for an alpha of zero or less *and* a rank among the
     placebos at half or below assumes that the placebos earn about the benchmark. Shifting the
     weights in time keeps their average: a slow rule whose holdings persist averages far from equal
     weight, and if that average loses at every timing, the placebos lose too, and the second
     condition spares a theory on which the first alone would count (CA-024-01). For such a rule
     the card says which condition carries the claim, and why.
   - The split dates are the lab's: in-sample from 2005, or a later start, to the end of 2022; the
     holdout 2023 to 2025 for every card. A start that leaves fewer than three of gate 5's blocks
     with 126 sessions cannot pass gate 5. The card counts the weekdays after the start, which
     outnumber sessions, so it refuses only the starts that cannot pass whatever the calendar, from
     2014-07-09 on; a start a few days earlier is accepted and may still leave fewer than 126
     sessions in 2010-2014, which `--try`, counting the sessions after the strategy's first target,
     warns about.

   `python -m lab.report --check strategies/<folder>` checks all of this, and that no run of the
   registry bears this id or this card; like the run, it refuses while the registry is not whole
   (step 7), and while the folder holds anything but the card and its reasoning: the build plan and
   the code are written after the card is locked, not before. Then **commit the card alone**
   (`card: <id>`), before any code: from that commit, the card never changes. The hook
   `tools/hooks/pre-commit`, installed as `.git/hooks/pre-commit`, runs the check on every card a
   commit stages and stops the commit it refuses (SC-010-01, whose lock went through with a card
   that did not parse, the check's refusal piped away). The lock proves the order of the commits;
   the order of the work is for whoever runs the lab to keep, and a departure from it is written in
   the verdict. A changed hypothesis is a new card, `<nn>` plus one, which names this one as its
   `parent`; its trials add to the registry's count.
5. **Build plan**, `build-plan.md`: what code, in what order, and why.
6. **Strategy code**, `strategy.py`: a function `positions(market, **parameters)` that returns a
   target weight for each session and asset, commented against the build plan.
   - long only, weights summing to 1 at most; a row of NaN holds, and a row with any target
     sells every asset it does not name;
   - the weights of session t read the market up to t-1 (`.shift(1)`), and bitcoin through
     `market.signal_prices`, one day late; gate 1 checks both;
   - a periodic rebalance sets its targets on the first session of each period, not the last:
     knowing that a session is the last of its month means knowing the next session's date, and
     gate 1 counts that as reading the future;
   - no weight on an asset that is not trading (`market.tradable`), and a rule that chooses among
     assets chooses among those that trade;
   - targets only on the sessions and assets of the market it is given: a date or an asset outside
     it is refused. Gate 6 leaves each cluster out in turn by making its assets untradable, their
     prices still there to be read, so that a rule reading one market to trade another keeps its
     signal; it leaves bitcoin out by removing it from the market;
   - it reads nothing but its `market` argument (no file, no network, nothing of the lab: the run
     refuses a folder whose code imports `lab`), never edits that market (each call gets a copy of
     its frames, so an edit through pandas changes nothing the battery prices, only the strategy's
     own reading), and gives the same targets every time; it is compiled from its source, and a
     compiled file in its folder is refused;
   - the decision to hold reads the past only, like the targets: gate 1 checks sessions where the
     strategy holds as well as those where it sets a target, for every variant;
   - it is never backtested outside the runner: `python -m lab.report --try strategies/<folder>`
     checks the targets of every variant and every neighbour, and their timing (gate 1's for the
     variants; ten dates where it sets a target and ten where it holds for each neighbour), on
     the in-sample years, and shows no returns.

   Commit `reasoning.md`, `build-plan.md` and `strategy.py`, with any file they need, after the
   card: the run refuses a file of the folder committed before the card or with it, under its
   name or any name it was moved from (a file copied in is a new file); anything uncommitted,
   hidden from git, ignored by git or linked from elsewhere in the folder; and anything
   uncommitted or ignored in `lab/` (but Python's compiled files, which must hold their source's
   code, and which the runner removes after every run), in `templates/`, in the data
   manifest and in `requirements.txt`, whatever git's settings and filters.
7. **Run**: `python -m lab.report strategies/<folder>`, one run at a time (a second run in the
   clone waits until the first has written its lines, then is refused until they are committed).
   Gates 1 to 7 run, the registry gets one line per variant, `report.ipynb` is executed into the
   folder, and `STATUS.md` is regenerated. A warning that the lab's compiled files could not be
   removed names their folder: remove it before the next run. The run refuses a card that changed,
   a card already run (its holdout is opened once), a card committed with its code or after it,
   anything uncommitted, and registry lines not yet committed; a refusal leaves the card unused: fix
   the cause, never the card, and run again.
   Once its checks pass, the clone records the card, before the battery opens the holdout: from
   then on the card has run, whatever happens next. As a tripwire, not a sandbox, the run refuses a
   strategy that changes the lab's code or constants as it is imported; changed as the strategy
   runs, the run is void, and its lines say so. It watches the lab's own modules, not the libraries
   they compute with. **Commit `registry/trials.jsonl` at once, alone** (`registry: <id>`),
   whatever the run printed, and push it at once when the lab runs in more than one clone. Never
   amend, rebase or squash a commit of the registry: a rewritten history keeps no trace of the
   lines it dropped, and only the clone that wrote them can put them back.
   - If the notebook or the board fails, or the notebook is interrupted (a Ctrl-C during the
     notebook may say its kernel died), the run is recorded and says so: fix the cause, then
     `python -m lab.report --notebook strategies/<folder>`, or `python -m lab.status`. Where the
     run's data could not be written (a full disk), it says that its report cannot be drawn. A run
     stopped by SIGTERM after its lines, outside its notebook, ends where it stands, silently: once
     its data is written, the same two commands draw what it did not; stopped in the instant
     between its lines and its data, its report cannot be drawn.
   - If the run stops after its record (the battery raised, the run was interrupted, the lab
     changed), the card has run: its lines are written void, with the returns the battery computed
     when the lab changed, the board is regenerated, and a new card is needed. If the registry could
     not be written, the clone kept the lines: `python -m lab.registry restore` puts them back once
     it can be; the notebook and the board are drawn all the same.
   - If the runs that every gate judges break (the benchmarks, a choosing card's walk-forward),
     every gate fails with the error: the card has run, the trials its variants computed count in
     gate 4, the report says the runs broke, and a new card is needed.
   - No card runs, and no card is checked, while the registry is not whole, since gate 4 would count
     too few trials. A line that a commit held, or that this clone's runs wrote, and the file lacks:
     `python -m lab.registry restore` puts it back, with its returns; a line not yet committed of a
     card this clone ran that its run did not write (edited, a changed copy beside it, a line added
     under the card) is replaced by the run's line, or removed. Where the clone's copy in its git
     folder holds no line of the card (the copy lost, emptied, or an older one put back, or lines
     written by hand for a run that wrote none), `restore` and `void` cannot tell those lines apart,
     and say so, naming the card: put the clone's own copy back; commit the lines as they are if
     they are the runs' own; remove them from the file if they were written by hand. A run this
     clone began that wrote no line at all (interrupted before its lines, a strategy that ended its
     process, or both the registry and the clone's copy unwritable): `python -m lab.registry void`
     writes void lines without returns, once no run is going and no line written for its card by
     hand is left in the file. A line committed counts in gate 4 in every clone alike, whoever wrote
     it, one with returns before one without, a void line among them; only in the clone that ran a
     card does its run's own line come before any other of its variant alike in returns (both with,
     or both without), an edit of it among them. Never write one by hand: committed, a line written
     by hand counts as a run's over a run's line without returns when it has returns, in every
     clone, and beside a run's line alike in returns, in every clone but the one that ran the card,
     when it was committed first. A copy damaged within a run's lines, one of them lost from it,
     lets `restore` remove that line as not the run's: keep the copy whole. Then commit the
     registry, alone, and regenerate the board (`python -m lab.status`).
   - A merge of the registry keeps both sides' lines, and nothing else: a line that is not a
     registry line (conflict markers) stops every run and the board, which name it; remove it and
     commit.
8. **Verdict**, `verdict.md`: gate by gate, what the notebook shows; the verdict, which is the
   first gate failed or "passes gates 1 to 7"; what was learned about the theory, the market and
   the lab. A bug found after the run is written down; fixing it takes a new card. A card judged
   against a rule it refines takes its difference from `python -m lab.compare`, not from a script
   of its own: the measure is then the same for every such card.
9. **The theory's status**, once no other strategy will be drawn from it: `tested-conclusive` if
   one of its strategies passed gates 1 to 7, `tested-inconclusive` if they all failed, or
   `not-testable`, with the reason in `reasoning.md`.
10. **Commit**: first `python -m lab.status` and `python -m lab.bank`, so that the board and the
    bank's index show the verdict and the status; then the folder, `STATUS.md`, the theory's file
    and `bank/README.md`.
11. **A survivor** of gates 1 to 7 is re-read in full by a second reader, who did not write it —
    reasoning, card, code and verdict, against this runbook and the battery — before its registry
    lines are published, since the publication starts its gate 8: paper trading, for two to four
    weeks. Nothing else is to start: from the first run after the publication, the scheduled job
    (`python -m lab.paper --log <folder>`, after every US close) trades every survivor's base
    variant on the paper account, and, while there is none, the first strategy of the registry as a
    test of the chain; a `card.yaml` that differs from the one its registry line ran stops the job,
    which names it. After each session it logs the next session's targets and compares every earlier
    live signal with the backtest's, on its own branch, `paper`, with one page, a section per
    strategy. Before each publication, `python -m lab.paper --take` copies the job's summary into
    `paper/live.json` and regenerates the board, which then shows each strategy's gate 8: since
    when, its signals identical to the backtest's, and its return, shown and not judged; commit
    both. Gate 8 passes on identical signals over two to four weeks. Its conclusion, and any gap,
    are written in `gate-8.md` in the strategy's folder and summed up in the verdict; once that file
    is published, the job no longer trades the strategy, and what only it held is sold at the next
    session where another strategy sets targets.
12. **A survivor of gate 8** leaves as a strategy dossier that meets the
    [handoff contract](../handoff/README.md).

## Rules that never bend

- The card is locked by a commit before any code, and the holdout is opened once.
- Three variants at most; every trial stays in the registry, which only grows.
- The thresholds are the battery's, set before any card (`lab/battery.py`), and their version is
  written with every verdict; changing one is a versioned decision that applies only to later cards.
- Nothing is deleted: a rejected strategy stays where it is, with its verdict.
- Every file speaks about the theory, the market and the strategy, for a reader who knows
  nothing else.
