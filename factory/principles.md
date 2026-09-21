[Up: Factory](README.md)

# Design principles

## TL;DR

Twelve rules the whole blueprint follows, distilled from the twenty foundation pages of the former corpus.
Each gives the rule in one sentence, why it matters, and where it shows in the sub-sections.
A rule changes only as principles 3 and 4 allow: by an open, written revision, never by a private exception.

## The twelve rules

| # | Principle | The rule in one sentence |
|---|---|---|
| 1 | [One language](#1-one-language) | One word has one meaning in every section, and every object has its place in one shared map. |
| 2 | [A bounded, lasting intent](#2-a-bounded-lasting-intent) | The factory says what it produces and what it refuses, and every local choice traces back to that intent. |
| 3 | [Why before how](#3-why-before-how) | Principles, policies, processes and procedures are kept apart, each change is checked against the level above, and none changes in private. |
| 4 | [The producer is never the judge](#4-the-producer-is-never-the-judge) | No one validates their own work, conflicts of interest are declared, and no decision with impact goes live without a second pair of eyes. |
| 5 | [Small, measurable, reversible](#5-small-measurable-reversible) | Every change is small, measured, and comes with a way back tested before it goes out. |
| 6 | [Simple by default, removable by design](#6-simple-by-default-removable-by-design) | Complexity enters only on proof that it pays, and what no longer serves is retired along a written path. |
| 7 | [Reasons written when decided](#7-reasons-written-when-decided) | Every decision is written when it is taken, with its reasons, the options rejected and a version, and is cited by that version. |
| 8 | [A ladder of proof, on comparable terms](#8-a-ladder-of-proof-on-comparable-terms) | A claim is acted on once observed, reproduced, evaluated and reviewed, and figures are compared on the same conventions only. |
| 9 | [Named states, governed transitions](#9-named-states-governed-transitions) | The factory is always in a named mode, and changes mode only through written [gates](glossary.md#gate), ramps and resumes. |
| 10 | [Loose coupling through contracts](#10-loose-coupling-through-contracts) | Parts meet only through written, versioned contracts, and change them without surprising their consumers. |
| 11 | [A steady cadence, little work in progress](#11-a-steady-cadence-little-work-in-progress) | Decisions are taken at fixed rituals with written outputs, and new work waits until open work has landed. |
| 12 | [Learn without blame](#12-learn-without-blame) | Every incident is rebuilt from facts, without blame, and closes only when its fixes have landed and held. |

## 1. One language

**Rule.** One word has one meaning in every section, and every object of the factory (a dataset, a
[feature](glossary.md#feature), a strategy, an order, an incident, a mission) has one name and its
place in one shared map of entities, flows, events and states.

**Why.** When two teams use one word for two things, the difference ends up frozen in schemas,
metrics and gates: the factory becomes inconsistent for reasons of language, not of technique. A
stable language is what lets two modules, two strategies or two decisions be compared line by line.
The same care applies to what a sentence is: an intention, a hypothesis, a decision or a proof,
never one taken for another.

**Where it shows.** The [glossary](glossary.md) holds one entry per concept, and every page links a
term at its first use. Every Interfaces table names what flows with glossary terms, so a flow means
the same at both ends. Each definition has one home: every [SLO](glossary.md#slo) sits in the
[SLO catalogue](glossary.md#slo-catalogue) of
[S6.1](sections/s6-monitoring/s6.1-shared-observability.md), every risk budget in the
[risk budget book](glossary.md#risk-budget-book) of
[S5.4](sections/s5-decision-execution/s5.4-allocation-budgets.md). Identity is settled once, per
date: an instrument, a listing, an issuer and an alias each have one meaning
([S1.1](sections/s1-data-foundation/s1.1-identity-reference-universe.md)). A strategy enters as a
[falsifiable thesis](glossary.md#falsifiable-thesis), a hypothesis and not a result
([S3.1](sections/s3-strategy-lab/s3.1-admission.md)).

**From.** Foundations 1 (the factory's grammar), 7 (a common ontology of objects) and 19 (the same
words, the same effects).

## 2. A bounded, lasting intent

**Rule.** The factory states what it produces and what it refuses to produce, and aims at returns
net of costs and risks, never gross; every local choice can be traced back to that intent, every
extension of scope is argued and requalified, and what is built is meant to stay true, readable and
useful in ten years.

**Why.** Without a bounded intent, scope grows in silence: a team widens its role, a tool made to
observe starts to decide, curiosity runs outside any frame. A shortcut that does not survive the
next cycle is a debt, not progress.

**Where it shows.** The factory is bounded: it never searches for [alpha](glossary.md#alpha), and
section 3 re-engineers what the lab found, admitting, returning or rejecting each dossier (S3.1);
every strategy is optimised for a [net-of-cost objective](glossary.md#net-of-cost-objective)
([S3.3](sections/s3-strategy-lab/s3.3-disciplined-optimization.md)). Every sub-section opens with
its purpose and what success looks like, and names the triggers that make it run again
([requalification](glossary.md#requalification)). A few invariants hold whatever the tools:
[point-in-time](glossary.md#point-in-time) data
([S1.2](sections/s1-data-foundation/s1.2-bitemporality.md)),
[train/serve parity](glossary.md#train-serve-parity)
([S2.10](sections/s2-feature-label-factory/s2.10-feature-registry.md)), and an immutable record that
can be replayed ([S1.3](sections/s1-data-foundation/s1.3-timebase-replay.md),
[S7.2](sections/s7-lifecycle/s7.2-decision-record.md)).

**From.** Foundations 2 (the contract of intent and scope) and 12 (a long-term posture).

## 3. Why before how

**Rule.** Principles (why), policies (what is required or forbidden), processes (the logical
sequence) and procedures (the concrete gestures) are kept apart. A new procedure stays local while
its process holds; a change of process, policy or principle calls for a review across sections, and
a changed process takes a major version. No level changes except by an open, written revision, never
by a private exception.

**Why.** Mixing the levels turns a debate on a log format into a challenge to
[traceability](glossary.md#traceability) itself. Kept apart, the upper levels change slowly and
protect continuity, while the lower ones can change fast without breaking an invariant.

**Where it shows.** This page holds the principles. Policies sit in documents such as the
[deployment rulebook](glossary.md#deployment-rulebook) of
[S5.9](sections/s5-decision-execution/s5.9-governance-safety.md) and the
[policy matrix](glossary.md#policy-matrix) of
[S7.4](sections/s7-lifecycle/s7.4-reliability-risk-budgets.md). The steps of each sub-section are
its processes, and the [runbooks](glossary.md#runbook) that
[S6.7](sections/s6-monitoring/s6.7-intervention-learning.md) gathers are the procedures; no alert is
left silent, since every alert points to its runbook
([S7.3](sections/s7-lifecycle/s7.3-architectural-fitness.md)). The blueprint reads in the same
order: section page, sub-section page, then the detail folded under each summary (the notes under
the Interfaces table, and the steps).

**From.** Foundations 3 (levels of abstraction) and 17 (the integrity grid: no private exception).

## 4. The producer is never the judge

**Rule.** No one validates their own work: no decision that is irreversible or carries impact goes
live without a second pair of eyes, no one can produce, validate and deploy an artefact alone, a
conflict of interest is declared before the verdict it could bend, and every exception or override
is recorded with its reason.

**Why.** The author of a model is attached to it; a second reviewer, working from written criteria,
removes that bias without a committee. A private exception makes the factory depend on the one
person who knows, and it can no longer [replay](glossary.md#replay) its own decisions.

**Where it shows.** Section 3 improves and section 4 judges: section 3 never validates its own
improvements, and section 4 deflates its statistics for every trial in the
[trial registry](glossary.md#trial-registry), the lab's and section 3's included
([S3.5](sections/s3-strategy-lab/s3.5-large-scale-inference.md),
[S4.2](sections/s4-validation/s4.2-validity-inference.md)); a strategy leaves section 4 only through
the signed decision of its [promotion gates](glossary.md#promotion-gate)
([S4.10](sections/s4-validation/s4.10-promotion-gates.md)). Two pairs of eyes are mandatory on the
[entry ticket](glossary.md#entry-ticket)
([S5.1](sections/s5-decision-execution/s5.1-onboarding-eligibility.md)), on the
[kill switch](glossary.md#kill-switch) and the [rollback](glossary.md#rollback) (S7.4), and in
section 5's weekly cross review (S5.9); there, no single person can disable a hard stop. Overrides
are capped, and each is reviewed afterwards (S5.4, S7.4). Each role gets the least access it needs
([S6.6](sections/s6-monitoring/s6.6-operational-security.md)). The three signers of the promotion
decision, research, execution and risk, each declare any conflict of interest before signing
(S4.10).

**From.** Foundations 4 (decision rights and the two pairs of eyes) and 17 (the integrity grid).

## 5. Small, measurable, reversible

**Rule.** Every change is small enough for its effect to be attributed, measured against a stated
hypothesis, ended by a due date or a stopping rule, and reversible by a way back planned and tested
before the change goes out.

**Why.** A large change mixes causes, so its effect cannot be attributed; a change without a measure
is an opinion; a change without a way back is a latent risk for the whole factory. Reversibility is
what makes it safe to try.

**Where it shows.** Novelties reach the market in small doses (paper, then
[canary](glossary.md#canary-release), then gradual tiers, then full), with the rollback ready before
the go (S5.9). Every change travels as one immutable [release package](glossary.md#release-package),
rehearsed, rolled out step by step and reversible in seconds
([S7.5](sections/s7-lifecycle/s7.5-change-management.md)); schemas change by "expand and contract"
(S7.3). Every mission of the loop is short, reversible and measurable, has an owner and a due date,
and runs as a canary release ([S7.10](sections/s7-lifecycle/s7.10-monitoring-feedback-loop.md)). In
doubt, the factory [fails closed](glossary.md#fail-closed)
([S6.5](sections/s6-monitoring/s6.5-controlled-degradation.md)), the conservative option wins
(S5.1), and [regime](glossary.md#regime) adaptation stays neutral when its context is missing
([S5.5](sections/s5-decision-execution/s5.5-regime-adaptation.md)).

**From.** Foundation 5 (reversibility and safe experimentation).

## 6. Simple by default, removable by design

**Rule.** Start simple and add complexity only on proof that it pays for itself; accepted complexity
is bounded, documented and reviewed; and anything that no longer serves is retired along a written
path: reported, qualified, marked deprecated, then withdrawn.

**Why.** Complexity grows faster than the number of parts, since each parameter multiplies the
interactions to understand. A factory that cannot shed what it no longer needs becomes opaque, slow
and inconsistent.

**Where it shows.** Optimisation prefers few degrees of freedom, with explicit penalties on
complexity ([S3.2](sections/s3-strategy-lab/s3.2-architecture-invariances.md), S3.3); section 2 maps
redundant features and keeps representatives
([S2.8](sections/s2-feature-label-factory/s2.8-information-dimension.md)). The
[feature registry](glossary.md#feature-registry) gives every feature a status (draft, active,
deprecated) and a policy of deprecation, with an overlap period and an end-of-life date (S2.10).
Strategies are withdrawn cleanly, down to their [sunset](glossary.md#sunset)
([S7.6](sections/s7-lifecycle/s7.6-champion-challenger.md)).

**From.** Foundations 10 (parsimony and clarity) and 20 (the simplification charter and the right to
retire).

## 7. Reasons written when decided

**Rule.** Every decision is written when it is taken, with its context, the options weighed and
rejected, its criteria and its expected effects; it carries a stable ID and a version, a later
change annotates it instead of rewriting it, and whatever depends on it cites the version in force,
never a name alone.

**Why.** An explanation written afterwards is a story, not a proof. What is not recorded does not
exist: without the reasons, a later review cannot tell why a rule exists, and the same debates come
back.

**Where it shows.** Every page of the factory writes its [decision log](glossary.md#decision-log)
into the system of record (S7.2), which also keeps a readable reason for every trade. Each strategy
carries its [design rationale](glossary.md#design-rationale) in its living
[strategy dossier](glossary.md#strategy-dossier)
([S3.9](sections/s3-strategy-lab/s3.9-traceability-rationale.md)). No test runs without its
[pre-registration](glossary.md#pre-registration), written before it sees the data
([S4.9](sections/s4-validation/s4.9-scientific-governance.md)). Records are never updated in place:
a correction is a new event that points to the original (S1.3). Every job and experiment pins the
batches it reads, and a job without [pinning](glossary.md#pinning) is rejected
([S1.8](sections/s1-data-foundation/s1.8-data-governance.md)).

**From.** Foundations 6 (intellectual traceability and the log of reasons) and 14 (document
governance and the versions of ideas).

## 8. A ladder of proof, on comparable terms

**Rule.** A claim is acted on only when it has climbed four rungs: observed (timestamped and
replayable), reproduced (the same result from an independent run), evaluated (against benchmarks,
regimes, stress and costs) and reviewed (signed and published); a proof holds only in its context,
so a cancelled or missing review sends it back to the second rung, and a revised rule demotes every
proof that depends on it; and two figures are compared only when they share the same horizon, base,
unit and window.

**Why.** Without an agreed ladder, conclusions turn on rhetoric; without shared conventions, an
improvement can be an artefact of the window, and a comparison of net with gross says nothing.

**Where it shows.** Section 1 makes every observation point-in-time and replayable bit for bit
(S1.3), and a backfill must pass "run twice, same result"
([S7.7](sections/s7-lifecycle/s7.7-data-lifecycle.md)); section 4 evaluates out of sample, under
regimes and under costs ([S4.1](sections/s4-validation/s4.1-experimental-protocol.md),
[S4.4](sections/s4-validation/s4.4-robustness-sensitivity.md)); its signed
[promotion record](glossary.md#promotion-record) is the review, taken again when the market's rules,
the universe or a key hypothesis change (S4.10). Section 4 expresses every metric in the same base
of time and asset (S4.1); cost analysis anchors every cost on the decision price and normalises by
context, against Simpson's paradox
([S4.7](sections/s4-validation/s4.7-transaction-cost-analysis.md)); monitoring keeps one definition
of every measure, as the factory's [single source of truth](glossary.md#single-source-of-truth)
(S6.1).

**From.** Foundations 8 (the scale of proof) and 9 (comparability hygiene).

## 9. Named states, governed transitions

**Rule.** The factory, and each of its parts, is always in a named mode with its own permissions
(normal, cautious, degraded, stopped), and changes mode only through written gates, stepped ramps
and tested resumes, never by improvisation.

**Why.** Each component then knows what it may do without a debate, an incident carries the name of
its mode instead of "everything broke", and the return to normal is defined in advance. A factory
shows its quality in its transitions, when everything changes.

**Where it shows.** Stabilisation owns the ladder of [operating modes](glossary.md#operating-mode),
from normal to a global stop, each step with [hysteresis](glossary.md#hysteresis), a cooldown and a
time to live (S6.5). The policy matrix turns the state of the budgets of reliability and risk into
traffic lights tied to actions: ramp up, freeze, kill (S7.4). Each strategy holds a status, from
paper through canary and [capital tiers](glossary.md#capital-tier) to
[champion](glossary.md#champion-challenger), [quarantine](glossary.md#quarantine) and sunset (S7.6).
And every sub-section passes its own gates: entry, exit (pass, retry or fail) and requalification.

**From.** Foundation 11 (states and transitions).

## 10. Loose coupling through contracts

**Rule.** Parts meet only through written, versioned contracts (what each expects, offers and
guarantees: formats, units, timing, modes of failure), and a contract changes by being announced,
run old and new side by side, migrated consumer by consumer, then retired, with its past versions
still replayable.

**Why.** A hidden dependency turns every change into a shock wave; a clear contract lets one part be
improved or replaced without touching its neighbours.

**Where it shows.** Every sub-section declares its flows in its Interfaces table, and a flow is
declared at both ends. Data is read through one [as-of API](glossary.md#as-of-api) (S1.8); features
are served under a [feature-serving contract](glossary.md#feature-serving-contract) (S2.10); the
[schema contracts](glossary.md#schema-contract) of data are kept by S7.7 and change by "expand and
contract" (S7.5). In monitoring, each flow stays declared from its producer to its reader, and the
platform only carries it ([S6.8](sections/s6-monitoring/s6.8-monitoring-as-code.md)).

**From.** Foundation 15 (couplings and interface contracts).

## 11. A steady cadence, little work in progress

**Rule.** The factory decides at fixed rituals, each as frequent as the
[half-life](glossary.md#half-life) of what it treats requires, with a standard input (a
[pre-read](glossary.md#pre-read)) and a standard output (written decisions, missions, the date of
the next review), and no decision is oral; it caps the work in progress, and opens new work only
once open work has landed.

**Why.** Without a rhythm, signals pile up and decisions follow the emergency of the moment; beyond
a few items at once, switching between them costs more than the work. Speed comes from finishing,
not from opening.

**Where it shows.** Each steering review starts from a pre-read and ends with 3–5 written decisions,
assigned and dated, which become missions; it sets a limit of work in progress, and nothing is added
while that limit is reached ([S7.1](sections/s7-lifecycle/s7.1-steering-cadences.md)). The loop of
missions limits the hot and warm missions run in parallel (S7.10). Capital is arbitrated every week
or fortnight, with no decision outside that cadence except on an incident
([S7.8](sections/s7-lifecycle/s7.8-capital-cost-steering.md)). Each strategy's cadence of adjustment
follows its half-life (S5.1).

**From.** Foundations 13 (cognitive flow and limits of work in progress) and 18 (rhythms and
rituals).

## 12. Learn without blame

**Rule.** Every incident or significant deviation is rebuilt from the facts as they were, into a
neutral timeline; its causes are sought in the system, never in a person; and it closes only when
each corrective action, with its owner and its date, has landed and held.

**Why.** Blame destroys information: people stop reporting weak signals, and the logs empty. A
lesson that never reaches a rule, a test or a guide is a failure of the loop.

**Where it shows.** [Intervention](glossary.md#intervention) writes a
[blameless postmortem](glossary.md#blameless-postmortem) for every incident (S6.7);
[incident response](glossary.md#incident-response) turns its actions into missions and tests of
non-regression, and follows them to their close
([S7.9](sections/s7-lifecycle/s7.9-incident-response.md)). Monitoring's signals become missions that
are decided, recorded, and fed back into its thresholds (S7.10).

**From.** Foundation 16 (a learning culture and blameless postmortems).
