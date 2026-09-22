# Handoff — the strategy dossier contract

The contract between `alpha-lab/` and `factory/`: what a complete
[strategy dossier](../factory/glossary.md#strategy-dossier) contains. The lab conforms to it as
its output format; the factory uses it as its admission criteria, in
[S3.1](../factory/sections/s3-strategy-lab/s3.1-admission.md).

## What a dossier is

One complete folder per strategy, readable without its author: a reader who comes to it cold
understands the idea, reruns the code on the data it names, and finds every result, the failed
variants included. The factory never searches for alpha: it admits a dossier (S3.1), improves it
(section 3) and judges it (section 4). A dossier that does not meet this contract goes back to the
lab with the list of its gaps; the factory does not fill them in.

## Fields

| Field | What it must contain | Why admission (S3.1) needs it |
|---|---|---|
| Theory | The mechanism the strategy exploits (economic, behavioural or microstructure), and who is on the other side of the trade. | S3.1 restates the thesis in factory terms; without a mechanism there is nothing to restate, and nothing to watch live. |
| Hypothesis stated before the data | The testable claim, dated and frozen before any result was seen: universe, horizon, expected sign and size of the effect, and the conditions under which it fails. | It separates a prediction from a story fitted afterwards; S3.1 checks its date against the first run of the trial registry. |
| Code | The version-pinned code that produces every result, with its environment and its random seeds. | S3.1 checks that it runs from a clean start; S3.2 compares its own re-implementation with it. |
| Logic | The decision chain in plain words: inputs, signal, sizing, rules to enter and exit, costs assumed. | S3.1 checks that the code does what the words say; S3.2 re-implements from it without guessing. |
| Data used | Each dataset with its source, period, universe, point-in-time status and fingerprint, and every exclusion or repair. | S3.1 maps it onto the factory's own data; data the factory cannot obtain point-in-time sends the dossier back to the lab, with the data named, while section 1 is asked for a new source. |
| Results | The figures and tables the claim rests on, gross and net of costs, each with the recipe that regenerates it and the tolerance within which a rerun must match. | They are what S3.2 must reproduce on factory data, within that tolerance; a figure without a recipe does not count. |
| Validation report | What the lab already tested (out-of-sample periods, cross-validation scheme, costs, robustness), the weaknesses it knows, and its short paper run: period, fresh data, comparison with the backtest. | S3.1 decides what the factory must still test, so section 4 neither redoes what is sound nor misses what is not; the paper run is the dossier's only evidence on fresh data, the proof that it leaves the lab alive. |
| Trial registry | Every variant tried, kept or dropped, with its parameters, date and result. | The number of trials corrects the statistics of S3.5, S4.2 and S4.3; a registry of winners only hides overfitting. |

## What the factory adds

The dossier keeps growing after admission. Section 3 adds its decision frame, its reference
implementation on factory data, its optimisation, combination, inference, variant and robustness
work, and the plan section 4 will run; every trial it runs joins the trial registry.
[S3.9](../factory/sections/s3-strategy-lab/s3.9-traceability-rationale.md) keeps the living
dossier from there on.

A dossier goes back to the lab only when S3.1 refuses it or
[S3.2](../factory/sections/s3-strategy-lab/s3.2-architecture-invariances.md) cannot reproduce it.
What section 3's [variants](../factory/glossary.md#variant) teach does not flow back on its own:
the lab draws the lessons for its theories itself.
