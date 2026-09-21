[Up: Factory](README.md)

# Glossary

## TL;DR

One English term per concept, used the same way on every page of the blueprint.
Each definition is written for a reader outside quantitative finance; pages link here at a term's first use.

## How to read it

Terms are sorted alphabetically. An acronym has a short entry that points to the full term.
Links inside a definition lead to other entries. Anchors are stable: a page links to
`glossary.md#<term>`, for example [point-in-time](#point-in-time).

## A

- <a id="adjusted-series"></a>**Adjusted series** — A price or volume series computed as of a date from the corporate actions known on that date, in a labelled view (split-adjusted or total-return) always served beside the raw series it comes from.
- <a id="adjustment-factor"></a>**Adjustment factor** — The multiplier applied to past prices and volumes so that a corporate action does not look like a price jump. It is applied only from the date it was known.
- <a id="admission"></a>**Admission** — The first step of the Strategy Lab: checking a strategy dossier against the handoff contract, restating its thesis in factory terms, then admitting it, returning it to the lab, or rejecting it.
- <a id="alert-to-action-table"></a>**Alert-to-action table** — The table that gives each alert of drift detection (S6.4), by symptom and severity, its default action (a smaller size or frequency, another venue, the cautious mode, a partial freeze, a call to a human), who carries it out (an automaton or the on-call), its conditions of exit, timeout and rollback, and its reason, written as a rule "if… then… because…". An alert with no entry and no runbook is refused. Lifecycle's decisions (retrain, recalibrate, freeze, roll back) sit in the [trigger-action catalogue](#trigger-action-catalogue).
- <a id="alignment-log"></a>**Alignment log** — The record of every join made by causal alignment: what was joined, when, with which lag and under which rule.
- <a id="allocation-layer"></a>**Allocation layer** — The layer that splits capital and the risk, liquidity and capacity budgets across strategies.
- <a id="alpha"></a>**Alpha** — The part of a strategy's return that comes from its edge, not from exposure to the market or to common factors.
- <a id="alpha-combination"></a>**Alpha combination** — Blending several signals or strategies into one, with weights that account for their correlation.
- <a id="anti-leakage-gate"></a>**Anti-leakage gate** — An automated check that blocks a dataset, a feature or a backtest when it could use information from after its decision time.
- <a id="as-of-api"></a>**As-of API** — The only way to read time-varying data in the factory: every request names the instant it reads as of, and receives the as-of view for that instant.
- <a id="as-of-join"></a>**As-of join** — A join that matches each record with the other table's values as they were known at that record's date. The factory refuses any join on time-varying data without one.
- <a id="as-of-view"></a>**As-of view** — The [point-in-time](#point-in-time) snapshot served for one date: data as it was known then, rebuilt from the bitemporal store.
- <a id="assembly-pattern"></a>**Assembly pattern** — A standard way of combining signals into a decision (committee, gating, hysteresis), with fuses that cut a component off when it misbehaves.
- <a id="audit-pack"></a>**Audit pack** — A ready-to-use dossier that proves a figure or a decision: its chronology, the source events, the transformations applied, the reconciliations, the decisions and signatures, and the versions needed to replay it within a stated tolerance. S6.3 assembles them; S6.2 contributes those of execution, S6.6 those of security.
- <a id="autocorrelation"></a>**Autocorrelation** — The correlation of a series with its own past values at a given lag; it shows how much of its past a series carries.

## B

- <a id="backtest"></a>**Backtest** — A simulation of how a strategy would have performed on past data.
- <a id="bag-manifest"></a>**Bag manifest** — The record of a resampling plan: the events of each bag, their order and seed, the out-of-bag set, and the projection of the bag on each validation split.
- <a id="bar"></a>**Bar** — A summary of trading over a window: open, high, low and close prices, and volume. The window can be fixed in time; in activity (a number of trades, of shares or of dollars traded); or in information, closing when the order flow departs from what was expected.
- <a id="base-rate"></a>**Base rate** — The share of events in a class before any model is applied, such as the share of targets hit; a model is judged against it.
- <a id="baseline"></a>**Baseline** — The reference a result is judged against: the versioned level of a metric, against which drift and SLOs are judged, or the simple method a new one must beat.
- <a id="batch-registry"></a>**Batch registry** — The catalogue of sealed batches with their fingerprints, versions and published references, which every downstream job pins.
- <a id="bid-ask-bounce"></a>**Bid-ask bounce** — The back-and-forth of trade prices between the bid and the ask, which adds noise, not information, to a price series.
- <a id="bitemporal-store"></a>**Bitemporal store** — The append-only tables that hold every fact with its valid time and transaction time, from which every as-of view is rebuilt.
- <a id="bitemporality"></a>**Bitemporality** — Storing every fact with both its [valid time](#valid-time) and its [transaction time](#transaction-time), and never overwriting. It answers both "what was true then" and "what did we know then".
- <a id="blameless-postmortem"></a>**Blameless postmortem** — A written review after an incident that looks for causes in the system, not for culprits, and ends with tracked actions.
- <a id="breadth"></a>**Breadth** — The number of independent bets a strategy makes per year.
- <a id="burn-rate"></a>**Burn rate** — How fast the error budget is being consumed. A high burn rate raises an alert before the SLO is breached.

## C

- <a id="calibration"></a>**Calibration** — Setting a model's parameters or thresholds so that its outputs match observed reality, for example predicted probabilities that match observed frequencies. In the Strategy Lab, "fine calibration" is the tuning of a strategy's parameters under a declared trial budget.
- <a id="canary-release"></a>**Canary release** — Releasing a change to a small share of traffic or capital first, and widening it only while its stop / go criteria stay green.
- <a id="candidate-package"></a>**Candidate package** — The standard record of one discovery at the end of inference: expected effect after shrinkage and debiasing, uncertainty, risk of being false, robustness flags and conditions of use, in the format section 4 reads.
- <a id="canonical-instrument"></a>**Canonical instrument** — The single, stable identity the factory gives a financial instrument, whatever its tickers, listings and venues over time.
- <a id="canonical-market-view"></a>**Canonical market view** — A standard, versioned view of market data (bars, quotes, trades, order book) built one way for every consumer.
- <a id="canonical-order"></a>**Canonical order** — The one agreed order of events, with a stable tie-break for identical timestamps, used everywhere so that every replay sees events in the same sequence.
- <a id="capacity"></a>**Capacity** — The amount of capital a strategy can trade before costs and market impact eat its edge.
- <a id="capital-allocation-plan"></a>**Capital allocation plan** — What capital steering (S7.8) decides at each weekly or fortnightly cadence: the target size and the caps of each unit of allocation (a strategy, a sleeve or a book), within its capital tier and the budgets of risk, costs and turnover; the plans of ramp; the calendar of rebalancing, with its cheap windows of the market and the days and hours to avoid; and the rules of freeze. The allocation layer (S5.4) turns it into budgets; the transition planner (S5.6) schedules it.
- <a id="capital-eligibility"></a>**Capital eligibility** — The conditions a strategy must meet before it can receive any capital.
- <a id="capital-ladder"></a>**Capital ladder** — The rules by which a strategy's capital rises and falls, kept by the lifecycle of models and strategies (S7.6): the bounds of each capital tier, the rules of promotion (stability net of costs, the gap from what was expected), of ramp-down and of the kill switch, and the windows of cooling before re-entry. Section 5 applies it: S5.4 the bounds of the tier each strategy holds, S5.9 the stages, freezes, ramp-downs and kills; capital steering (S7.8) allocates within it.
- <a id="capital-tier"></a>**Capital tier** — A stage of capital allocation (for example small, medium, full) that a strategy earns step by step, after paper trading.
- <a id="causal-alignment"></a>**Causal alignment** — Joining sources so that each value is used only from the moment it was actually visible, never before.
- <a id="causal-panel"></a>**Causal panel** — A table that aligns several sources on common reference times, each value carrying its publish time, so that no value appears before it was visible.
- <a id="certification-dossier"></a>**Certification dossier** — Everything that lets any peer replay a key result without help and reach the same verdict: the pre-registration, the manifests, the log of seeds, the descriptor of environment, the standard report, the opinions of two reviewers, and the results of a cold replay.
- <a id="certified-dataset"></a>**Certified dataset** — A dataset that has passed the data quality gate: its checks, repairs and quarantines are recorded in its scorecard, and it is safe to use point-in-time.
- <a id="champion-challenger"></a>**Champion / challenger** — Running a new model or strategy version (the challenger) next to the current one (the champion), and switching only when the challenger proves better under agreed criteria.
- <a id="change-management"></a>**Change management** — The process by which changes to code, data, models and limits are proposed, reviewed, released and, if needed, reversed.
- <a id="circuit-breaker"></a>**Circuit breaker** — An automatic switch that stops a flow (orders, data, a model) when failures pass a threshold, until conditions recover.
- <a id="clock-skew-budget"></a>**Clock skew budget** — The largest drift allowed between the clocks of different machines or sources, with an alert when it is exceeded.
- <a id="coefficient-of-variation"></a>**Coefficient of variation** — A standard deviation divided by its mean: a dispersion measure without units, which lets assets of different scales be compared.
- <a id="combination-rule"></a>**Combination rule** — The versioned rule by which a strategy's alphas become one score per asset, then target positions and orders: families and their budgets, base weights, regularisation, and the speed of change that holds costs; and, at each cadence, the positions and orders it produces.
- <a id="combinatorial-purged-cross-validation"></a>**Combinatorial purged cross-validation** — Testing on many combinations of train / test splits, with purging and embargo, to obtain a distribution of results instead of a single historical path.
- <a id="compression-recipe"></a>**Compression recipe** — The frozen transformation, learned inside the validation folds, that projects a group of features onto a more compact basis, with its parameters, normalisations and order of application, and its tests of parity and neutrality.
- <a id="condition-number"></a>**Condition number** — A measure (κ) of how much small errors in the inputs of a computation can be amplified in its outputs. A high value signals an unstable model.
- <a id="conditioning-package"></a>**Conditioning package** — The versioned, fitted transformations that prepare features for learning: monotone transforms and caps, robust scales, orthogonalisation matrices with the order of their axes, and the numerical contract (condition-number thresholds, tolerances, fallbacks).
- <a id="consolidated-market-feed"></a>**Consolidated market feed** — The trades and quotes of each instrument from every venue, normalised per venue and merged into one consolidated view by stable rules, with trades signed.
- <a id="contractual-cadence"></a>**Contractual cadence** — The agreed frequency, and the longest acceptable delay, for updating a key input such as a universe, a risk model or a threshold.
- <a id="control-directive"></a>**Control directive** — An instruction monitoring sends to section 5 to act at once: slow down, reroute, switch between passive and aggressive, enter a degraded mode or stop; with its scope, priority, window of application (a time to live), criteria of revert and explanation. Live execution fidelity (S6.2), data integrity (S6.3) and stabilisation (S6.5) issue them; section 5 obeys them.
- <a id="controlled-degradation"></a>**Controlled degradation** — Reducing activity step by step (smaller sizes, fewer instruments, no new positions) instead of failing abruptly when something goes wrong.
- <a id="convex-optimisation"></a>**Convex optimisation** — An optimisation problem with a single best solution that algorithms find reliably; most portfolio construction is set up this way.
- <a id="corporate-action"></a>**Corporate action** — An event decided by a company that changes its shares or their price history: split, dividend, merger, spin-off, change of symbol.
- <a id="corporate-action-ledger"></a>**Corporate action ledger** — The versioned, point-in-time record of every corporate action, with its source, its dates and the adjustment factors derived from it.
- <a id="cost-attribution-report"></a>**Cost attribution report** — What transaction cost analysis delivers: costs measured per order and broken into components (timing, impact, spread, fees, opportunity), their attribution to market conditions and choices of execution, the recalibrated parameters and cost budgets of the execution simulator, the scorecards of brokers, algorithms and venues, the routing policies, and the capacity curves with the rules of sizing.
- <a id="cost-of-change"></a>**Cost of change** — What moving from the current portfolio to a new one costs, measured before deciding to move: S5.4 sets its budget, and the transition planner (S5.6) spends within it. The risk taken while the trades are under way is the [value at risk of change](#value-at-risk-of-change).
- <a id="cost-surface"></a>**Cost surface** — The versioned map of expected trading costs and sustainable capacity as a function of volume, participation, liquidity and time of day, per context (instrument, size, venue, regime), with its interval of uncertainty, and the cost analysis it was recalibrated from: realised costs by segment, the errors of the models, the diagnostics of impact and adverse selection. Execution analytics (S5.8) recalibrates it from realised costs; portfolio construction, budgets and transition planning read it.
- <a id="cpcv"></a>**CPCV** — see [combinatorial purged cross-validation](#combinatorial-purged-cross-validation).
- <a id="cross-validation"></a>**Cross-validation** — Estimating how a model will perform on unseen data by training and testing it on several splits of the same dataset. On time series the splits must respect time, with [purging](#purging) and an [embargo](#embargo).

## D

- <a id="data-lifecycle"></a>**Data lifecycle** — The stages data goes through from acquisition to archive or purge, with its retention and provenance recorded at each stage.
- <a id="data-quality-scorecard"></a>**Data quality scorecard** — The certificate that goes with a dataset: its quality score, defects by type against P95 / P99 thresholds, repairs, quarantined zones, the version of the rules used, and a pass / fail verdict.
- <a id="dataset-manifest"></a>**Dataset manifest** — A file shipped with every dataset delivery, listing its sources, versions, rules, time window and content hash, so that anyone can check what it is and rebuild it.
- <a id="dead-letter-queue"></a>**Dead-letter queue** — Where messages that cannot be processed are parked for inspection instead of being lost.
- <a id="decision-frame"></a>**Decision frame** — The admitted strategy restated in factory terms on one page: scope and intent, falsifiable thesis, objective and budgets, the rules to act and to stop, and the evidence section 4 will demand. Every other sub-section of the Strategy Lab works from it.
- <a id="decision-graph"></a>**Decision graph** — The acyclic chain of computations that turns data into a decision, each with its latency budget.
- <a id="decision-log"></a>**Decision log** — The system of record for decisions: who decided what, when and why, with links to the evidence.
- <a id="deflated-sharpe-ratio"></a>**Deflated Sharpe ratio** — The probability that a strategy's Sharpe ratio is genuine once the number of trials, the length of the track record and non-normal returns are accounted for: the probabilistic Sharpe ratio measured against the best result that many random trials would produce.
- <a id="deployment-rulebook"></a>**Deployment rulebook** — Section 5's rules of deployment and safety, kept by S5.9: the perimeter (instruments, venues, trading windows), with the [restricted list](#restricted-list); the soft and hard limits per family, strategy and venue (risk, liquidity, costs, latency, concentration, leverage) with their windows of measurement and grace times; who may activate what; the stages from paper trading to canary, gradual and full release, with their criteria of promotion and rollback; and the real-time controls (throttles, circuit breakers, kill switch) with their thresholds.
- <a id="design-rationale"></a>**Design rationale** — The recorded reasons behind each design choice, so that a reviewer can check it and a successor can change it safely.
- <a id="design-task"></a>**Design task** — A step that needs judgment: choosing, specifying, reasoning about trade-offs. The build is sized by counting design tasks and execution tasks.
- <a id="deterministic"></a>**Deterministic** — Same inputs, same outputs, every time.
- <a id="dimensionality-reduction"></a>**Dimensionality reduction** — Compressing many features into fewer ones that keep most of their information.
- <a id="disciplined-optimisation"></a>**Disciplined optimisation** — Tuning a strategy under a declared trial budget, fixed stopping rules and a logged search, so that the search itself cannot manufacture a result.
- <a id="drawdown"></a>**Drawdown** — The fall from a peak in value to a later low.
- <a id="drift"></a>**Drift** — A lasting change in the data, the market, the system or a model's behaviour compared with its baseline.
- <a id="drill"></a>**Drill** — A rehearsed incident (a feed outage, a kill-switch test) that proves the response works before it is needed.
- <a id="dsr"></a>**DSR** — see [deflated Sharpe ratio](#deflated-sharpe-ratio).

## E

- <a id="effective-number-of-bets"></a>**Effective number of bets** — How many independent bets a set of signals or positions really amounts to once their correlations are counted: ten alphas that move together may be worth two bets.
- <a id="effective-sample-size"></a>**Effective sample size** — The number of truly independent observations a dataset is worth once overlaps and correlations are accounted for.
- <a id="embargo"></a>**Embargo** — A gap left after each test period (in some protocols, around it), from which no training data is taken, so that information cannot seep across the boundary.
- <a id="empirical-null"></a>**Empirical null** — The distribution of scores observed when there is no signal, learnt from the factory's own data instead of assumed from theory. Evidence is judged against it.
- <a id="ems"></a>**EMS** — see [order management system](#order-management-system).
- <a id="entry-ticket"></a>**Entry ticket** — The executable term sheet a strategy brings to the portfolio, signed at onboarding (S5.1): its verdict (green; orange, a dated pilot; red), its initial weight and bounds, target turnover, maximum losses, limits of participation and cadence, with its eligibility score, its compatibility with the strategies already running, its stop rules, and the hooks and triggers that monitoring and lifecycle watch. It references the normalised dossier it was signed on: the strategy's card, its point-in-time series of P&L and its aggregated exposures.
- <a id="error-budget"></a>**Error budget** — The amount of failure an SLO allows over a period, for example 0.1% of requests. Spending it too fast freezes risky changes.
- <a id="ess"></a>**ESS** — see [effective sample size](#effective-sample-size).
- <a id="event-bus"></a>**Event bus** — The shared channel through which components publish and receive events, with idempotent handlers, a dead-letter queue and replay.
- <a id="event-clock"></a>**Event clock** — Sampling data when something happens (a number of trades, a volume, a notional traded, or a price move) instead of at fixed clock times.
- <a id="event-index"></a>**Event index** — The table of the moments at which the factory takes an observation, triggered by events rather than by clock time; each entry has its asset, its interval [t0, t1] and the version of the rules that made it.
- <a id="event-log"></a>**Event log** — The immutable, append-only journal of every event in canonical order, from which all state can be rebuilt by replay.
- <a id="event-window"></a>**Event window** — The unit of work of the factory: an event time t0, or an interval [t0, t1], on which features, labels and decisions are computed.
- <a id="evidence-locker"></a>**Evidence locker** — The write-once store that keeps the proof behind each decision: manifests, test results, reports.
- <a id="ex-date"></a>**Ex-date** — The first day a share trades without the right to an announced corporate action (a dividend, another distribution, or the new shares of a split); its price adjusts on that day.
- <a id="execution-analytics"></a>**Execution analytics** — Measuring how orders were actually executed (costs, fills, timing, venues) and feeding what is learned back into decisions and into the execution simulator.
- <a id="execution-attribution"></a>**Execution attribution** — Explaining the cost of each trade by its causes: spread, impact, timing, venue choice, execution style.
- <a id="execution-chain"></a>**Execution chain** — Everything between a target portfolio and filled orders: pre-trade checks, order slicing, routing, the OMS and EMS, post-trade records.
- <a id="execution-fidelity"></a>**Execution fidelity** — How closely execution matches its simulation: fills, costs and markouts from the execution simulator against those observed live.
- <a id="execution-log"></a>**Execution log** — The immutable record of every order the execution chain (S5.7) sends: parent orders, child orders and fills linked by stable IDs, with monotonic timestamps, the state of the book, the decision and its parameters, rejections, latency and queue position. Execution analytics, monitoring and audit read it.
- <a id="execution-policy"></a>**Execution policy** — The versioned rules the execution chain (S5.7) applies per context (instrument, time of day, size, regime of liquidity): the style, the pacing, the mix of passive and aggressive orders, the venues and order types. Execution analytics (S5.8) proposes each new version from realised costs, and it is released by canary, with its criteria of promotion and rollback (S5.9).
- <a id="execution-profile"></a>**Execution profile** — What the execution simulator delivers for a strategy: capacity-to-cost curves, execution recipes (pace, order types, routing) and slippage budgets per regime, with their bands of uncertainty and conditions of use.
- <a id="execution-simulator"></a>**Execution simulator** — The factory's simulator of how orders would have been filled (queue position, partial fills, market impact), calibrated on real fills. Called XSIM on these pages.
- <a id="execution-task"></a>**Execution task** — A step that mostly needs work to a known specification: building, running, structuring, documenting.
- <a id="execution-transfer-coefficient"></a>**Execution transfer coefficient** — The share of a strategy's theoretical information ratio (IC × √breadth) that survives costs and turnover: net IR = τ × theoretical IR. The classical transfer coefficient measures what portfolio constraints let through; this one measures what execution lets through.
- <a id="expected-shortfall"></a>**Expected shortfall** — The average loss over the worst cases beyond a chosen confidence level, for example the worst 2.5% of days.
- <a id="experiment-design"></a>**Experiment design** — Planning which variants to test, in which order and how many, before running them, so that results can be interpreted and the trial budget is kept.
- <a id="experiment-passport"></a>**Experiment passport** — Everything needed to replay a validation experiment identically: its charter, final partitions, purge, embargo and warm-up settings, seeds, logs and checks. The execution simulator, cost analysis and paper trading reuse its partitions.
- <a id="experimental-protocol"></a>**Experimental protocol** — The written rules of a validation study (splits, metrics, trial count, stopping rules), fixed before the data is looked at.
- <a id="explainability"></a>**Explainability** — Being able to state why the system took a decision, from its recorded inputs, rules and models.
- <a id="explanation-sheet"></a>**Explanation sheet** — The standard reason the system of record (S7.2) gives for each trade or decision: a readable summary in 1–3 lines, then the values seen at the time, the active constraints, the contributions of the factors at the moment of the decision, the rules passed or failed, and the alternatives considered. It replays the real reasoning, never a story told afterwards, and is available within minutes of the fill.

## F

- <a id="fail-closed"></a>**Fail-closed** — Built to refuse when in doubt: a missing date, an ambiguous identifier or a failed check blocks the request instead of letting it through.
- <a id="fallback"></a>**Fallback** — The pre-planned safe action when something fails: reduce, freeze, roll back or stop.
- <a id="false-discovery-rate"></a>**False discovery rate** — The expected share of false positives among the results declared significant.
- <a id="falsifiable-thesis"></a>**Falsifiable thesis** — A strategy hypothesis stated as "if… then… because…", precise enough that data could prove it wrong.
- <a id="fdr"></a>**FDR** — see [false discovery rate](#false-discovery-rate).
- <a id="feature"></a>**Feature** — A measurable input a model uses to make a prediction, computed only from data available at decision time.
- <a id="feature-card"></a>**Feature card** — The self-describing record of one object in the feature registry: name, definition, recipe, units, clock, window, point-in-time guardrails, validity range, dependencies, owner and status.
- <a id="feature-mask"></a>**Feature mask** — The versioned list of the features kept per latency tier, horizon and regime, with the stability of each choice and the reason for each exclusion.
- <a id="feature-registry"></a>**Feature registry** — The catalogue of every feature with its definition, version, lineage and serving contract.
- <a id="feature-serving-contract"></a>**Feature-serving contract** — The guarantee of how a feature, label or weight is delivered to production: schema, freshness, latency, and identical computation to research.
- <a id="fingerprint"></a>**Fingerprint** — A deterministic hash of everything that defines an artefact (data, code, parameters, input schemas and versions, order of steps). Any change gives a new fingerprint, and must give a new version.
- <a id="fitness-function"></a>**Fitness function** — An automated check that measures whether the architecture still meets a quality goal (latency, coupling, cost) as it evolves.
- <a id="fitness-gate"></a>**Fitness gate** — The automatic gate that the fitness functions of S7.3 put on every change: go, slow (a canary, a quota) or stop, by the criticality of the property at stake. A hard fail blocks, a soft fail slows, a warning is only watched. Change management (S7.5) releases each change through it.
- <a id="fold"></a>**Fold** — One of the parts into which cross-validation cuts the data; each fold serves in turn as the test set while the others are used for training.
- <a id="fractional-differentiation"></a>**Fractional differentiation** — Transforming a price series just enough to make it stationary while keeping as much of its memory as possible.
- <a id="fundamental-law-of-active-management"></a>**Fundamental law of active management** — The rule that the information ratio is roughly skill times the square root of breadth: IR ≈ IC × √breadth.
- <a id="fuse"></a>**Fuse** — A reversible guardrail inside a strategy: when a market-state trigger fires, it tightens caps, slows turnover or switches to a fallback logic, and it releases with hysteresis once the market calms.

## G

- <a id="gate"></a>**Gate** — A checkpoint with written conditions. An entry gate says when work may start; an exit gate gives a verdict against thresholds set in advance: pass, retry, or fail.
- <a id="gate-report"></a>**Gate report** — The record of a gate's checks on one delivery: tests run, verdicts, measures and final status, kept in the evidence locker.
- <a id="gate-verdict"></a>**Gate verdict** — The outcome of an exit gate. Pass: every condition holds. Retry: a condition misses and the owning step can fix it. Fail: the conditions cannot be met without changing an upstream contract, so the work goes back to its owner.
- <a id="guardrail"></a>**Guardrail** — A control that automatically blocks a known kind of mistake or excess, instead of relying on someone noticing.

## H

- <a id="half-life"></a>**Half-life** — The time an effect, such as a shock or an autocorrelation, takes to fall to half its initial size.
- <a id="hard-soft-constraint"></a>**Hard / soft constraint** — A hard constraint can never be violated; a soft one can, at a stated penalty.
- <a id="human-in-the-loop"></a>**Human in the loop** — A process in which people review or decide at defined points, above all on the cases that rules and models cannot settle.
- <a id="hysteresis"></a>**Hysteresis** — Using a stricter threshold to raise an alarm than to clear it, so that a signal hovering near the limit does not flap on and off.

## I

- <a id="ic"></a>**IC** — see [information coefficient](#information-coefficient).
- <a id="idempotent"></a>**Idempotent** — Giving the same result whether it runs once or several times: a re-run never counts anything twice.
- <a id="identity-resolver"></a>**Identity resolver** — The service that takes an identifier and a date and returns the canonical instrument it designated on that date, or fails cleanly when the answer is ambiguous.
- <a id="immutability"></a>**Immutability** — Once written, a record is never modified; a correction is a new record.
- <a id="impact-analysis"></a>**Impact analysis** — Finding everything downstream that a change will affect, by following the lineage.
- <a id="implementation-shortfall"></a>**Implementation shortfall** — The gap between the return a decision would have earned at the decision price and the return actually achieved after execution.
- <a id="imputation"></a>**Imputation** — Filling a missing value with an estimate. In the factory it is bounded, logged, and never uses information from the future.
- <a id="in-sample-out-of-sample"></a>**In-sample / out-of-sample** — In-sample data is used to build or tune a model; out-of-sample data is kept apart to test it.
- <a id="incident-charter"></a>**Incident charter** — The frame every incident of the factory runs in, kept by incident response (S7.9): the roles (an incident commander, one voice who decides; a technical operator and a technical lead; a spokesperson; a scribe who keeps the journal; liaisons with the business and risk, and with brokers and providers), the on-call rota published 30 days ahead with its escalations and relays, one channel per incident, the templates (declaration, timeline, closure, postmortem), and the matrix of engagement: for each level of incident severity, its automatic actions, its target delays and who may cut what. Intervention (S6.7) applies it to every incident; stabilisation (S6.5) triggers its automatic actions.
- <a id="incident-response"></a>**Incident response** — The factory's organised handling of incidents, kept by lifecycle (S7.9): its [incident charter](#incident-charter) sets the roles and the severities, and the path every incident follows (detect, assess its severity, contain, recover, review), and it follows each corrective action to its close. [Intervention](#intervention) (S6.7) runs the live response under it.
- <a id="incident-severity"></a>**Incident severity** — The level given to an incident, on one scale from P1 to P4 that intervention (S6.7) keeps, which sets who responds and how fast; the incident charter of S7.9 ties each level to its actions.
- <a id="information-coefficient"></a>**Information coefficient** — The correlation between forecasts and realised outcomes: a measure of forecasting skill.
- <a id="information-matrix"></a>**Information matrix** — Scores of what each feature says about the target, and of what it adds to the others, per horizon and regime, with their uncertainty.
- <a id="information-ratio"></a>**Information ratio** — Active return divided by active risk: the excess return over a benchmark per unit of tracking error.
- <a id="input-output-charter"></a>**Input/output charter** — The rules every feature obeys at its input and output: units, scale invariance, and how missing values are flagged.
- <a id="interaction-map"></a>**Interaction map** — The living map of how strategies relate to one another (dependences that move over time, shared factors, crowding of liquidity, drawdowns that coincide under stress), with the interaction rules derived from it (caps per cluster, penalties for overlap, targeted neutralisations, interaction budgets) that portfolio construction (S5.3) and the allocation layer (S5.4) apply to keep the portfolio diversified.
- <a id="intervention"></a>**Intervention** — Monitoring's live response when something goes wrong in production, run by S6.7 under the [incident charter](#incident-charter): stabilise, work around, cut off, communicate; then the lessons that stop it from happening again.
- <a id="invariance"></a>**Invariance** — A property a strategy must keep under a transformation (rescaling, a time shift, a change of units), as a guard against spurious results.
- <a id="ir"></a>**IR** — see [information ratio](#information-ratio).

## K

- <a id="kill-switch"></a>**Kill switch** — The control that immediately stops a strategy or all trading, or cuts a component over to its fallback; it is tested regularly.
- <a id="kpi"></a>**KPI** — Key performance indicator: a number that tracks whether a step does its job, with an alert threshold.
- <a id="kpi-feed"></a>**KPI feed** — The stream of KPIs and alerts a sub-section publishes continuously, so that monitoring (section 6) can watch it.

## L

- <a id="label"></a>**Label** — The outcome a model learns to predict for each event: its direction (side), its size, or whether to act at all (meta-label).
- <a id="label-overlap"></a>**Label overlap** — Two events whose outcome windows share time have labels that are not independent; ignoring it overstates the evidence.
- <a id="label-set"></a>**Label set** — The published labels of an event index: primary labels (side, size, status, t0, t1, horizon) and meta labels (act or not, activation window, logged context), versioned with their rules.
- <a id="latency-budget"></a>**Latency budget** — The longest time each stage of a decision may take, so that the whole chain meets its deadline.
- <a id="leakage"></a>**Leakage** — Any path by which information from after the decision time reaches a feature, a label, a model or a backtest. It makes a strategy look better than it can ever be live.
- <a id="leakage-report"></a>**Leakage report** — The versioned proof that a delivery of features, labels, weights and time indexes can be used at t0: access tests, leakage smoke tests, substitution and stability maps, plausibility checks, and a reasoned go or no-go.
- <a id="lineage"></a>**Lineage** — The recorded chain of inputs and transformations behind a dataset, a feature, a model or a result. End-to-end lineage links any number to its sources through stable IDs: dataset, feature set, model, run, order.
- <a id="liquidity"></a>**Liquidity** — How easily an instrument can be traded in size without moving its price.
- <a id="listing-event"></a>**Listing event** — An event that changes whether or where an instrument trades: IPO, delisting, suspension, change of symbol or name, merger, move to another venue.

## M

- <a id="marginal-information-value"></a>**Marginal information value** — What a feature adds to those already selected, as opposed to what it merely repeats.
- <a id="marginal-sharpe-ratio"></a>**Marginal Sharpe ratio** — The change in the portfolio's Sharpe ratio caused by adding a strategy: its value to the whole, not on its own.
- <a id="market-impact"></a>**Market impact** — The price move caused by one's own trading.
- <a id="market-microstructure"></a>**Market microstructure** — How trading actually happens: order books, matching rules, tick sizes, spreads, halts. It shapes trading costs and short-term signals.
- <a id="markout"></a>**Markout** — The price move after a trade over a set horizon, from seconds to days, used to judge whether fills were well timed.
- <a id="memory"></a>**Memory** — How much of its past a series carries into its present values (slow trends, half-lives, regime effects); it often holds the predictive information that plain differencing erases.
- <a id="meta-labelling"></a>**Meta-labelling** — A second model that decides whether to act on a primary signal, and how much, rather than predicting its direction.
- <a id="microstructure-primitive"></a>**Microstructure primitive** — A basic measure of how trading unfolds (spread, depth, order-flow imbalance, signed volume), computed one standard way for every consumer.
- <a id="mission-card"></a>**Mission card** — The common card of a mission, lifecycle's unit of work: its ID, its source (a signal, a decision, a postmortem), the hypothesis and the bet, the acceptance criteria, the rollback, the owner and the due date. Lifecycle's pages open missions on it; the loop of missions (S7.10) keeps the queue, routes each card to the section that does the work, and follows it to its decision.
- <a id="monitoring-as-code"></a>**Monitoring as code** — Alerts, dashboards and rules written as versioned code, reviewed and tested like any other code.
- <a id="monitoring-signal"></a>**Monitoring signal** — A structured alert that monitoring publishes when it sees a deviation: the symptom, the metric and its period, the severity, the confidence, the scope, links to the evidence (traces, journals) and the default action. Stabilisation (S6.5), intervention (S6.7), the lifecycle of models and strategies (S7.6) and the loop of missions (S7.10) act on it; live execution fidelity (S6.2) reads those of drift detection (S6.4) as the context of the market, the budgets of reliability and risk (S7.4) the burn rates of S6.1, and capital steering (S7.8) the alerts on costs and the drifts of liquidity.
- <a id="monitoring-to-missions-feedback-loop"></a>**Monitoring-to-missions feedback loop** — The loop that turns every relevant monitoring signal (a breached SLO, a drift, slippage, latency, a data-quality issue) into a short, reversible, measurable mission with an owner, a priority, a test, acceptance criteria and a rollback.
- <a id="mttd-mttr"></a>**MTTD / MTTR** — Mean time to detect and mean time to repair: how long a defect or an incident lasts before it is seen, and before it is fixed.
- <a id="multi-venue-consolidation"></a>**Multi-venue consolidation** — Merging the quotes and trades of one instrument from several trading venues into one consistent view, by stable rules.
- <a id="multiple-testing"></a>**Multiple testing** — Running many tests raises the odds that some look significant by chance, so results must be corrected for the number of trials.

## N

- <a id="net-of-cost-objective"></a>**Net-of-cost objective** — The goal a strategy is optimised for, measured after transaction costs, never before.
- <a id="neutralisation"></a>**Neutralisation** — Removing a strategy's exposure to an unwanted factor (market, sector, size) so that its returns come only from its intended edge.
- <a id="no-trade-zone"></a>**No-trade zone** — A band around the current position within which small changes are not traded, so that no costs are paid for noise.

## O

- <a id="observability"></a>**Observability** — Being able to understand the state of the system from what it emits: metrics, logs and traces.
- <a id="oms"></a>**OMS** — see [order management system](#order-management-system).
- <a id="onboarding"></a>**Onboarding** — Bringing a promoted strategy into the live portfolio (S5.1): deciding whether it enters, at what size and within which bounds, and signing its entry ticket after checking its fit with the strategies already running and its limits.
- <a id="operating-contract"></a>**Operating contract** — What a strategy may do at size, fixed before capital: target size and ramp, maximum turnover, budget of costs, expected execution transfer coefficient, minimum return on execution costs, the safety envelope that triggers slowing down or reduction, and the rules of retreat.
- <a id="operating-mode"></a>**Operating mode** — The state the system runs in (normal, cautious, degraded, stopped), each with its own limits.
- <a id="optimisation-package"></a>**Optimisation package** — What the optimisation of a strategy delivers: the formalised problem (objective, constraints, penalties, tolerances), the target weights or positions, the active constraints and their multipliers, the diagnostics of stability and costs, and the frozen parameters with their validity window.
- <a id="order-book"></a>**Order book** — The list of buy and sell orders waiting at each price on a venue. Its depth is how much can trade near the best prices.
- <a id="order-management-system"></a>**Order management system** — The software that records, checks and tracks every order through its life (OMS). Its execution counterpart, the execution management system (EMS), works the orders in the market.
- <a id="order-slicing"></a>**Order slicing** — Splitting a large order into smaller ones over time or across venues to reduce market impact.
- <a id="orthogonalisation"></a>**Orthogonalisation** — Transforming features so that they carry no overlapping information, which stabilises models and their interpretation.
- <a id="out-of-bag"></a>**Out-of-bag** — The events left out when a bag is drawn; a model trained on the bag is evaluated on them.
- <a id="out-of-sample-pack"></a>**Out-of-sample pack** — The consolidated out-of-sample results of a validation experiment: the series per split with their metadata (seeds, splits, dates of freeze, versions), the distribution of each metric (median, dispersion, tail), its coverage of regimes, the map of the splits, and the notes of reading.
- <a id="overfitting"></a>**Overfitting** — Fitting a model to the noise in past data, so that it shines in backtest and fails live.
- <a id="overlap-map"></a>**Overlap map** — For each moment, the events whose label intervals are active at the same time; it shows how much labels share information.

## P

- <a id="paper-trading"></a>**Paper trading** — Running a strategy on live data with simulated orders and no capital. In the lab, a short run proving it behaves as in backtest; in the factory, an orchestrated multi-week campaign with guardrails.
- <a id="parameter-registry"></a>**Parameter registry** — The versioned tables of the parameters of the sampling rules (thresholds, windows, calibrations) per asset and regime, with the date and reason of every change.
- <a id="pbo"></a>**PBO** — see [probability of backtest overfitting](#probability-of-backtest-overfitting).
- <a id="pinning"></a>**Pinning** — Fixing the exact version of the data, code and environment a run uses, so that the run can be repeated.
- <a id="pit"></a>**PIT** — see [point-in-time](#point-in-time).
- <a id="point-in-time"></a>**Point-in-time** — Data exactly as it was known at a given moment, with no later correction or revision. A point-in-time query for 3 March returns only what the factory could have seen on 3 March; the [as-of view](#as-of-view) serves it.
- <a id="point-in-time-access-contract"></a>**Point-in-time access contract** — The rule that every data request states the moment it is made "as of". A request without one is refused, so no future information can leak in.
- <a id="point-in-time-universe"></a>**Point-in-time universe** — The list of instruments that could actually be traded on each day, with the reason each one entered or left. Nothing appears in it before it existed.
- <a id="policy-matrix"></a>**Policy matrix** — Lifecycle's rules that couple reliability and risk (S7.4): the ceilings of risk per horizon, the states of two counters, the error budget left and the risk budget consumed, shown as traffic lights, and the actions each state allows or forbids (deployments, the pace of ramp-up, freezes, caps on size and turnover, the delay of challengers), with hysteresis, dampers against pro-cyclicality and journalled overrides.
- <a id="portfolio-construction"></a>**Portfolio construction** — Turning forecasts, risk estimates and costs into target positions, under constraints.
- <a id="posterior-predictive-check"></a>**Posterior predictive check** — Simulating data from a fitted model or a generative hypothesis and comparing them with the observed data; systematic gaps show that the representation is implausible.
- <a id="pre-read"></a>**Pre-read** — The condensed brief, three screens at most, that monitoring (S6.1) compiles for each steering review (S7.1) and delivers 12 hours before it: reliability, alpha and research, and the strategic course, each finding coloured red, amber or green and stated in one line. A critical figure that is missing is labelled "uncertainty".
- <a id="pre-registration"></a>**Pre-registration** — Writing down, before a test runs, its falsifiable objective, universe, periods, metrics, thresholds of acceptance and rejection, count of trials and assumptions, so that the test cannot be bent to its results. In the factory, no test runs without one.
- <a id="pre-trade-check"></a>**Pre-trade check** — A control run before an order leaves: limits, restricted list, size, price sanity.
- <a id="precision-and-recall"></a>**Precision and recall** — Two measures of a detector. Precision: the share of its alerts that are real defects. Recall: the share of real defects it catches.
- <a id="probabilistic-sharpe-ratio"></a>**Probabilistic Sharpe ratio** — The probability that a strategy's true Sharpe ratio is above a benchmark, given the length and the shape of its track record.
- <a id="probability-of-backtest-overfitting"></a>**Probability of backtest overfitting** — The probability that the configuration picked as best in-sample does worse than the median configuration out-of-sample.
- <a id="progressive-rollout"></a>**Progressive rollout** — A release in stages (canary, then gradual, then full), each stage gated by stop / go criteria.
- <a id="promotion-gate"></a>**Promotion gate** — The gate a strategy passes to move up a stage: from validation to paper trading, from paper trading to capital, from one capital tier to the next.
- <a id="promotion-record"></a>**Promotion record** — The signed outcome of section 4's promotion gate, and its single exit: the decision (go, go under conditions, no-go) with its reasons and clauses, the operating charter (budgets, rules of orders, capacity limits), the ramp-up plan, the triggers of kill switch, rollback and quarantine with who decides, and the specification of the monitoring instrumentation. It references the frozen dossier of evidence it was decided on (selection report, robustness report, operating contract, execution profile, cost attribution report, stabilisation dossier, certification dossier), through which section 5 reads them.
- <a id="provenance"></a>**Provenance** — Where a piece of data came from, and everything that was done to it on the way.
- <a id="provenance-registry"></a>**Provenance registry** — The register of versions, hashes and dependencies that proves which inputs, rules and code produced each segment, snapshot or run.
- <a id="psr"></a>**PSR** — see [probabilistic Sharpe ratio](#probabilistic-sharpe-ratio).
- <a id="purging"></a>**Purging** — Removing from the training data every observation whose label window overlaps the test period.

## Q

- <a id="quality-flag"></a>**Quality flag** — A mark on a cell (one value) or a case (a whole event) that says whether it is clean, suspect or to be dropped, with its cause and severity.
- <a id="quarantine"></a>**Quarantine** — Holding something suspicious apart, still recorded, until it is fixed or explained: data, or a strategy, a component or a venue after an incident. What is quarantined never reaches a consumer, or the market, silently.

## R

- <a id="raci"></a>**RACI** — Who is Responsible, Accountable, Consulted and Informed for a task or a decision.
- <a id="rate-limiter"></a>**Rate limiter** — A control that caps how many actions, such as orders or requests, can happen per unit of time.
- <a id="rebalancing"></a>**Rebalancing** — Trading to bring a portfolio back to its target weights.
- <a id="reference-clock"></a>**Reference clock** — The single UTC time source, kept synchronised, against which every timestamp in the factory is taken.
- <a id="reference-data"></a>**Reference data** — Descriptive data about instruments and markets (identifiers, listings, venues, calendars), as opposed to prices and volumes.
- <a id="reference-implementation"></a>**Reference implementation** — The admitted strategy rebuilt in the factory's standard architecture, on the factory's own point-in-time data: decision graph and clock, interface charter, assembly pattern, invariance book with its tests, degraded modes, and what optimisation may touch. The lab's result must reproduce on it.
- <a id="reference-mid-price"></a>**Reference mid price** — The midpoint between the best bid and the best ask, computed by one fixed rule across venues and used as the reference for costs and signals.
- <a id="regime"></a>**Regime** — A persistent market state (calm, stressed, trending), identified by agreed rules and given an ID.
- <a id="regime-adjustment"></a>**Regime adjustment** — What regime adaptation (S5.5) publishes at each period: the current regime and its confidence, the scalers and dedicated limits its matrix of allocation sets for that regime, the adjusted targets with their no-trade bands and expected cost, and a short explanation; its journal keeps each switch (regime, scalers, trigger) with its costs expected and realised. It never exceeds the budgets of S5.4.
- <a id="regime-encoding"></a>**Regime encoding** — The causal state published for each event by S2.6 (trend or range, stress, liquidity, before or after an event), with its confidence and its rules of transition.
- <a id="regime-taxonomy"></a>**Regime taxonomy** — The agreed list of regimes, how transitions between them are detected, and how each one changes limits and gates.
- <a id="release-package"></a>**Release package** — The immutable unit in which any change travels to production (S7.5): what changes (code or rules, artefacts of data or features, parameters or models, configuration of execution), its manifests (versions, fingerprints, dependencies, compatibility), the links to its evidence of validation, its entry in the register of changes, and its rollout plan: the pattern, the steps of exposure or capital with their soak, the windows of the market, the criteria of promotion and the map of the kill switch.
- <a id="repair-log"></a>**Repair log** — The record of every repair made to data: before and after, rule, context, author (machine or person) and justification.
- <a id="replay"></a>**Replay** — Re-running a past period from recorded inputs to reproduce its outputs exactly, or within a stated numerical tolerance, and explaining any gap between live and replay.
- <a id="replay-api"></a>**Replay API** — The service that replays any past interval of the event log, or returns the state as of an instant, with the same bytes every time.
- <a id="reproducibility"></a>**Reproducibility** — Anyone can re-run a study from its recorded code, data, environment and seed, and obtain the same result.
- <a id="requalification"></a>**Requalification** — Re-running a sub-section's exit checks after something changes: a new data source, a drift, an incident, a rule change. A result stays valid only until one of its triggers fires.
- <a id="restricted-list"></a>**Restricted list** — The versioned list of instruments the factory must not trade, for compliance reasons. It belongs to the perimeter of S5.9's [deployment rulebook](#deployment-rulebook); the [pre-trade checks](#pre-trade-check) of the execution chain (S5.7) apply it before every order.
- <a id="retention-policy"></a>**Retention policy** — The rule that says how long each kind of data or record is kept, and how it is purged in a way that can be proven.
- <a id="return-on-execution-costs"></a>**Return on execution costs** — Net P&L divided by execution costs: how much a strategy earns for each unit it pays to trade. A deployment threshold, for example at least 1.5.
- <a id="risk-budget-book"></a>**Risk budget book** — Section 5's register of budgets (S5.4): every limit a strategy or the portfolio must respect (tracking error, expected shortfall, stress loss, liquidity and participation, turnover, capacity, leverage, concentration, and the interaction caps of S5.2 on crowding and common risk), per scope and on aligned horizons, ranked hard or soft, and translated into the constraints and penalties that portfolio construction, the transition planner and the execution chain apply, with the budget for the cost of change.
- <a id="risk-tolerance"></a>**Risk tolerance** — The loss, volatility or drawdown a stage accepts before the strategy is scaled back or stopped.
- <a id="risk-driven-deployment"></a>**Risk-driven deployment** — Putting decisions and changes into the market in small, controlled doses sized by the risk they carry, each one explainable, bounded and reversible within minutes.
- <a id="robust-feature-set"></a>**Robust feature set** — The features S2.6 builds over several horizons from cleaned and robustified data, each with its lag, latency, version, lineage and inherited quality flags.
- <a id="robustness"></a>**Robustness** — A result is robust when it survives reasonable changes to its parameters, data, period and assumptions.
- <a id="robustness-card"></a>**Robustness card** — The inspectable record of a strategy's robustness: the charter of risks and tolerances, the damper schema, the fuses and fallbacks, the influence tables, the resilience certificates, the invariance checklist, the requalification rules, and their machine-readable form.
- <a id="robustness-report"></a>**Robustness report** — Section 4's independent measure of how a candidate holds when it is shaken: the map of sensitivity to costs, liquidity, latency, noise and labels, alone and combined; a robustness index; tolerances per factor; the map of regimes; confidence intervals by block resampling; and the recommendations of capacity and exposure by regime. Section 3's robustness card is what the strategy builds in; this report is what section 4 measures.
- <a id="rollback"></a>**Rollback** — Returning to the previous known-good version. Every release must have a tested rollback.
- <a id="runbook"></a>**Runbook** — The written procedure for operating a component and for responding to its alerts and incidents.

## S

- <a id="sample-weight"></a>**Sample weight** — The importance given to each observation during training, for example lower when its label overlaps many others.
- <a id="schema-contract"></a>**Schema contract** — A versioned agreement between the producer of a dataset and its consumers, kept by the data lifecycle (S7.7): the structure (fields, types, units, mandatory and optional fields), the meanings, a service level of latency and a tolerance of late data, and the rules for adding and deprecating fields without breaking its consumers: an announcement, a period of coexistence, tests of compatibility and a plan of rollback.
- <a id="schema-registry"></a>**Schema registry** — The catalogue in which every schema contract and each of its versions is recorded.
- <a id="sealed-batch"></a>**Sealed batch** — A dataset delivery frozen together with its manifest and hash: it can be superseded by a new batch, never edited.
- <a id="secops"></a>**SecOps** — Security operations: access control, secrets, attestation of what runs, control of outgoing traffic.
- <a id="security-posture"></a>**Security posture** — The overall state of the factory's security controls, measured and reported.
- <a id="seed"></a>**Seed** — The starting value of a random number generator. Fixing it makes a random computation repeatable.
- <a id="segment-map"></a>**Segment map** — The dated boundaries of the coherent stretches of time found by break detection, each with the type of break and a confidence.
- <a id="selection-bias"></a>**Selection bias** — Picking the best of many results makes it look better than it is, and the more candidates, the stronger the bias.
- <a id="selection-report"></a>**Selection report** — What the hierarchical tournament of candidates leaves: for each candidate, its status (promote, retest or abandon), its probability of backtest overfitting, the decay to expect from in-sample to out-of-sample, its out-of-sample confidence curve (the plausible range of its future performance) and its decision sheet.
- <a id="sensitivity-analysis"></a>**Sensitivity analysis** — Measuring how much a result changes when one input or parameter changes.
- <a id="sentinel-backtest"></a>**Sentinel backtest** — A fixed reference backtest rerun on each new version of the data, to measure how much a data change moves the results.
- <a id="sequential-bootstrap"></a>**Sequential bootstrap** — Resampling that draws events one at a time, favouring those that overlap least with the events already drawn.
- <a id="sequential-control"></a>**Sequential control** — Adjusting decisions step by step as new information arrives, with rules for when to change and by how much.
- <a id="shadow-mode"></a>**Shadow mode** — Running a new version in parallel with the live one, on the same inputs, without its decisions being executed.
- <a id="shadow-price"></a>**Shadow price** — How much the objective would improve if a constraint were relaxed by one unit. It shows which constraints are expensive.
- <a id="sharpe-ratio"></a>**Sharpe ratio** — Average excess return divided by its volatility: the return earned per unit of risk.
- <a id="showback"></a>**Showback** — Reporting to each team or strategy the infrastructure costs it causes, without billing it.
- <a id="shrinkage"></a>**Shrinkage** — Pulling noisy estimates toward a simpler, more stable value: a little bias traded for much less error.
- <a id="simulation-plan"></a>**Simulation plan** — The list of tests section 4 will run on a strategy, with the pass criteria fixed before any test is run.
- <a id="single-source-of-truth"></a>**Single source of truth** — One agreed place for each metric or record, so that everyone reads the same number.
- <a id="sla"></a>**SLA** — Service level agreement: a promise made to a consumer, such as "the universe is updated before 08:00 the next day".
- <a id="sli"></a>**SLI** — Service level indicator: the measured quantity an SLO is judged on, such as latency or the share of data delivered on time.
- <a id="slippage"></a>**Slippage** — The difference between the price expected when an order is decided and the price actually obtained.
- <a id="slo"></a>**SLO** — Service level objective: the internal target behind a promise, stated as a share over a period, for example 99.9% of requests answered in under 100 ms.
- <a id="slo-catalogue"></a>**SLO catalogue** — The versioned definitions monitoring works from, kept by S6.1: for each critical path of the factory, its SLIs (formula, unit, window, source, filters), its SLOs and error budgets with their thresholds of burn rate, its baselines by segment (hour, day, regime), those of the markets and the models from drift detection (S6.4) among them, the rules of alert and escalation, and the dictionary of events with the schema of instrumentation (fields, correlation IDs, rules of timestamps, quotas and retentions), which the platform (S6.8) enforces.
- <a id="smart-order-routing"></a>**Smart order routing** — Choosing automatically where to send each order, among the available venues, for the best expected execution.
- <a id="snapshot"></a>**Snapshot** — A sealed, self-sufficient copy of the state at one point of the event log. Replaying from a snapshot plus the deltas after it gives exactly the state rebuilt from zero.
- <a id="sor"></a>**SOR** — see [smart order routing](#smart-order-routing).
- <a id="source-feed"></a>**Source feed** — Data as delivered by an external source (an exchange, a vendor, a publisher): prices, quotes, fundamentals, macro releases, news, event files, before any processing.
- <a id="source-specification"></a>**Source specification** — The written description of a data source: what each field means, where its valid time is read, when and how often it publishes, and how it corrects itself.
- <a id="source-trust-tier"></a>**Source trust tier** — The ranking of data sources by reliability for each type of data, used to decide which source wins when they disagree.
- <a id="spread"></a>**Spread** — The gap between the best ask and the best bid (the quoted spread). The effective spread compares a trade's price with the mid at that moment; the realised spread compares it with the mid a little later.
- <a id="stabilisation-dossier"></a>**Stabilisation dossier** — The record of the factory's paper-trading campaign: the daily KPIs (latency, rejections, drift against the execution simulator and cost analysis), the complete and replayable logs, the root-cause analyses, the matrix of guardrails (threshold, action, proof), the resilience tests, and the decision: promote, extend or rework.
- <a id="stabilised-series"></a>**Stabilised series** — A series transformed to be comparable over time (a steadier mean, variance and dependence) while keeping the memory that carries the edge; aligned on the event index and made by a versioned recipe.
- <a id="stale-quote"></a>**Stale quote** — A quote that has not been updated for longer than it should, and can no longer be trusted as a price.
- <a id="stationarity"></a>**Stationarity** — A series is stationary when its statistical behaviour does not change over time. Most models need stationary inputs.
- <a id="statistical-power"></a>**Statistical power** — The probability that a test detects an effect that is really there. With low power, a real edge looks like noise.
- <a id="steering-cadence"></a>**Steering cadence** — The fixed rhythm of reviews and decisions (daily, weekly, quarterly) at which the factory is steered.
- <a id="steering-note"></a>**Steering note** — What each steering review (S7.1) decides about the course: the budgets of reliability, risk and capital as arbitrated, the priorities for the next 7–14 days, the release cadence and the freezes, and the promotions and demotions proposed. Section 5 applies it within the day; lifecycle across the weeks.
- <a id="stochastic-optimisation"></a>**Stochastic optimisation** — Optimisation that takes the uncertainty of its inputs into account, by scenarios or by distributions, rather than trusting point estimates.
- <a id="strategy-dossier"></a>**Strategy dossier** — The complete folder in which a strategy travels from the research lab to the factory: theory, hypothesis stated before the data, code, logic, data used, results, validation report and [trial registry](#trial-registry). Its contract lives in [`handoff/`](../handoff/README.md).
- <a id="stress-test"></a>**Stress test** — Measuring losses under extreme but plausible scenarios.
- <a id="substitution-effect"></a>**Substitution effect** — When features carry the same information, importance spreads or shifts between them, so that one looks less, or more, important than it is.
- <a id="sunset"></a>**Sunset** — The planned retirement of a strategy or a model: its capital is wound down and its records archived.
- <a id="survivorship-bias"></a>**Survivorship bias** — The error of testing only on instruments that still exist today, which hides those that failed or disappeared and flatters the results.

## T

- <a id="t95"></a>**T95** — A delay met in 95% of cases (T90: in 90%). "T95 under one hour" means that 95% of events are processed within the hour.
- <a id="target-portfolio"></a>**Target portfolio** — What portfolio construction (S5.3) produces at each cycle: the target weights per strategy and asset, feasible within the budgets, with the planned turnover, the no-trade zones, the execution constraints derived from them (participation, windows), and the sensitivities and diagnostics that say which constraints bind and at what shadow price.
- <a id="tca"></a>**TCA** — see [transaction cost analysis](#transaction-cost-analysis).
- <a id="temporal-integrity"></a>**Temporal integrity** — The guarantee that every observation, label and validation split respects the order of time: nothing used to train, test or decide comes from after the moment it stands for.
- <a id="timebase"></a>**Timebase** — The single clock and ordering rule the whole factory uses to timestamp and sequence events, so that the same inputs always replay in the same order.
- <a id="total-return"></a>**Total return** — The return of an instrument with its dividends and other distributions reinvested.
- <a id="traceability"></a>**Traceability** — Every result can be followed back to the data, code, parameters and decisions that produced it.
- <a id="tracking-error"></a>**Tracking error** — The volatility of the difference between a portfolio's return and its benchmark's. Always written in full on these pages: the source plans use TE for their task tag.
- <a id="trade-signing"></a>**Trade signing** — Classifying each trade as buyer- or seller-initiated by aligning it with the quote in force; a trade that cannot be classified is marked unknown, not guessed.
- <a id="trading-calendar"></a>**Trading calendar** — The days and hours a market is open, with its holidays and early closes, for each market and time zone.
- <a id="trading-halt"></a>**Trading halt** — A suspension of trading in an instrument or a market, decided by the exchange.
- <a id="train-serve-parity"></a>**Train/serve parity** — The guarantee that a feature or a threshold is computed the same way in research and in production.
- <a id="transaction-cost-analysis"></a>**Transaction cost analysis** — Measuring what trading actually cost, broken down into spread, market impact, timing and fees, against a benchmark price.
- <a id="transaction-time"></a>**Transaction time** — When the factory recorded a fact. A correction published later gets a later transaction time, so that every past view stays reproducible.
- <a id="transformation-recipe"></a>**Transformation recipe** — The frozen settings that turn a series into a stabilised one: transformation family, bounded parameters, windows and calibration dates, applied identically in research and in serving.
- <a id="transition-plan"></a>**Transition plan** — The path from the current portfolio to the target one, trading off cost, risk and time along the way (S5.6): the dated quantities per window, the tempos of participation, the guardrails and the triggers to stop or slow down, with the rest of the path planned again whenever the targets or the market move.
- <a id="trial-budget"></a>**Trial budget** — The number of trials declared before a study starts. Every trial is logged in the trial registry and costs statistical significance.
- <a id="trial-registry"></a>**Trial registry** — The append-only record of every variant, parameter set and backtest tried for a strategy, in the research lab and in the factory. Statistics are corrected for the total number of trials it holds.
- <a id="trigger-action-catalogue"></a>**Trigger-action catalogue** — The table of "if this happens, do that" rules that the lifecycle of models and strategies (S7.6) keeps: which trigger (a drift of the signal or of behaviour, a change of regime, labels gone stale, costs or turnover exploding, capacity exceeded, an incident of data quality) calls for which action (retrain, recalibrate, freeze, ramp down, sunset), within which maximum latency from signal to action, with a double confirmation or a window of persistence against noise, and priority to the triggers of risk and costs. Monitoring (S6.1) registers its triggers and watches them.
- <a id="triple-barrier-method"></a>**Triple-barrier method** — Labelling an event by whichever comes first: a profit target, a stop loss, or a time limit.
- <a id="turnover"></a>**Turnover** — How much of a portfolio is traded over a period. It drives transaction costs.

## U

- <a id="uniqueness"></a>**Uniqueness** — The share of an event's label interval that no other active event shares; low uniqueness means the event repeats information already counted.

## V

- <a id="valid-time"></a>**Valid time** — When a fact is true in the world: the day a dividend goes ex, the period during which a ticker designates a company. One of the two time axes of [bitemporality](#bitemporality).
- <a id="validation-ready-index"></a>**Validation-ready index** — An index of events with their label windows, overlaps and embargoes already computed, from which leak-free validation splits can be generated on demand.
- <a id="validity-card"></a>**Validity card** — The identity card of a candidate's validity: the net effect with its confidence interval, the probability that it beats a minimum credible threshold, the same probability deflated for the number of trials, the statistical power, the effective number of trials, the stress results, and the verdict: pass, retry or fail.
- <a id="value-at-risk-of-change"></a>**Value at risk of change** — The risk created by moving the portfolio rather than holding it: the loss, at a chosen confidence level, that a change of weights could cause while its trades are under way. Portfolio construction caps it (S5.3); the transition planner keeps it within budget (S5.6).
- <a id="variant"></a>**Variant** — A version of a strategy that differs by a parameter, a rule or a data choice. Each variant tried is a trial.
- <a id="variant-map"></a>**Variant map** — What the exploration of controlled variants around an admitted strategy leaves: where the strategy holds and where it breaks, the comparison table, the sensitivity map, the short-list and the simulation brief for section 4.
- <a id="venue"></a>**Venue** — A place where an instrument trades: an exchange or another trading system.
- <a id="verification-and-validation"></a>**Verification and validation** — Verification checks that a model is built right: it does what its specification says. Validation checks that it is the right model: it matches reality.
- <a id="versioning"></a>**Versioning** — Giving each change of a dataset, schema, feature or model a new identifier, and never overwriting the previous one.

## W

- <a id="walk-forward"></a>**Walk-forward** — Testing by repeatedly training on the past and testing on the period just after it, moving forward in time.
- <a id="watermark"></a>**Watermark** — In a data stream, the point up to which all data is assumed to have arrived. Data arriving later is handled as late data, never silently inserted into the past.
- <a id="winsorisation"></a>**Winsorisation** — Capping extreme values at chosen quantiles instead of deleting them, so that outliers keep their sign but lose their excess weight.
- <a id="worm-storage"></a>**WORM storage** — Write once, read many: storage in which a record, once written, cannot be changed or deleted before its retention period ends.

## X

- <a id="xsim"></a>**XSIM** — see [execution simulator](#execution-simulator).
