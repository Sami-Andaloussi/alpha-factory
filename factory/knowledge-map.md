[Up: Factory](README.md)

# Knowledge map

## TL;DR

What a builder must master before building each of the seven sections, one line each, with where to learn it.
Each part gives the section's intent, the knowledge it rests on, and at most five checks that say when a builder is ready.
Drawn from the prerequisite pages of the former corpus; the study notes behind them are not carried over.

## How to read it

| Section | Its intent, in short |
|---|---|
| [S1 — Data Foundation](#s1--data-foundation) | One [point-in-time](glossary.md#point-in-time) base of data, replayable bit for bit and traceable end to end. |
| [S2 — Feature & Label Factory](#s2--feature--label-factory) | Clocks, [labels](glossary.md#label), weights and [features](glossary.md#feature) that are causal, replayable and servable under contracts. |
| [S3 — Strategy Lab](#s3--strategy-lab) | The lab's strategies made readable, solvable, robust and governable. |
| [S4 — Validation, execution simulation, cost analysis, paper trading](#s4--validation-execution-simulation-cost-analysis-paper-trading) | Honest tests against the future: out of sample, across [regimes](glossary.md#regime), under costs. |
| [S5 — Decision & Execution](#s5--decision--execution) | Validated [alphas](glossary.md#alpha) turned into live capital, every decision explainable, bounded and reversible. |
| [S6 — Monitoring](#s6--monitoring) | Seeing right, early, and in a way that can be acted on. |
| [S7 — Lifecycle](#s7--lifecycle) | Written, traceable and replayable decisions that steer the factory over time. |

Each part opens with the section's **intent**. Its table lists what to master before building the
section, one line each, with where to learn it: a book from the [references](references.md), or,
when no book summary covers it, the practice it comes from. **Ready when** gives the checks a
builder runs on themselves before starting. The lines are common to the whole section; the steps of
each sub-section page name the finer methods they use, and cite them.

## S1 — Data Foundation

**Intent** of [S1](sections/s1-data-foundation/README.md): one canonical, time-aware base of data,
point-in-time safe, [deterministic](glossary.md#deterministic), replayable bit for bit, free of
[leakage](glossary.md#leakage) and of [survivorship bias](glossary.md#survivorship-bias), and
traceable end to end, so that any read rebuilds exactly what was visible as of T, with the same
bytes today and tomorrow.

| What to master first | Where to learn it |
|---|---|
| **Point in time and as-of.** Read only what was visible at T, never the state corrected later; no survivorship bias; a read without its instant is refused, [fail-closed](glossary.md#fail-closed); as-of is not as-corrected. | [Jansen (2020)](references.md#jansen-2020) |
| **[Bitemporality](glossary.md#bitemporality).** [Valid time](glossary.md#valid-time) against [transaction time](glossary.md#transaction-time), intervals [start, end), a transaction time that only grows, a key sequenced by ID and both start times. | Temporal-database practice (bitemporal tables); no book summary covers it. |
| **Interval algebra and the integrity of time intervals.** No overlapping valid intervals per ID, illegal overlaps caught, intervals closed, coalescing, inclusive against exclusive bounds. | Temporal-database practice. |
| **Financial identity and alias graphs.** Instrument, listing, issuer, [venue](glossary.md#venue) and alias told apart; one meaning per identifier as of each date; recycled tickers and multiple listings. | Reference-data practice; no book summary covers it. |
| **Canonical order and a deterministic [timebase](glossary.md#timebase).** A chosen reference time, a stable tie-break, append-only records with no update in place, canonical serialisation, hashes and manifests. | [Kleppmann (2017)](references.md#kleppmann-2017) |
| **Causality across sources and normalised clocks.** Time zones and daylight saving (UTC only in storage), no publication before the event, the causal join "as visible at t", [watermarks](glossary.md#watermark) and buffers. | [Kleppmann (2017)](references.md#kleppmann-2017) |
| **Corporate actions: meaning and factors.** [Ex-date](glossary.md#ex-date), record and payment dates, splits against cash or stock dividends, factors that compose, adjustments that are [idempotent](glossary.md#idempotent). | Market-data practice; idempotent processing from [Kleppmann (2017)](references.md#kleppmann-2017). |
| **Microstructure: quotes, trades, venues, sessions.** Top of book, condition codes, auctions and halts, [trade signing](glossary.md#trade-signing), the [reference mid price](glossary.md#reference-mid-price) per venue or consolidated. | [Kissell (2013)](references.md#kissell-2013); trade signing from market-microstructure practice. |
| **Data quality: rules, statistics and learning, triage.** A taxonomy of defects, deterministic rules, anomaly detection, [quarantine](glossary.md#quarantine), a [human in the loop](glossary.md#human-in-the-loop), and [SLOs](glossary.md#slo) on the time to detect and to repair ([MTTD](glossary.md#mttd-mttr), MTTR). | Data-quality engineering and robust statistics; no book summary covers them. |
| **Governance, manifests and pinning.** The [dataset manifest](glossary.md#dataset-manifest) of each [sealed batch](glossary.md#sealed-batch), [fingerprints](glossary.md#fingerprint) and hashes, the [evidence locker](glossary.md#evidence-locker), the [anti-leakage gate](glossary.md#anti-leakage-gate), and [pinning](glossary.md#pinning) made mandatory downstream. | [Kleppmann (2017)](references.md#kleppmann-2017) for immutable, replayable data; manifests and pinning from reproducible-computing practice. |
| **Non-regression tests and bit-for-bit replay.** Golden sets, consistent [snapshots](glossary.md#snapshot), [replays](glossary.md#replay) across environments, frozen numerical tolerances. | [Kleppmann (2017)](references.md#kleppmann-2017); reproducible-computing practice. |
| **Service levels and KPIs of data operations.** T90 and [T95](glossary.md#t95) delays (IPOs, suspensions, [corporate actions](glossary.md#corporate-action)), as-of latency at p95, divergence between sources, point-in-time coverage, explained churn. | Reliability engineering; no book summary covers it. |

**Ready when** the builder can:
1. explain point in time, valid and transaction time, replay,
   [canonical order](glossary.md#canonical-order) and the causal join in two minutes, knowing that
   as-of is not the latest state;
2. tell an instrument, a listing, an issuer and an alias apart without ambiguity, and name at least
   three traps: a recycled ticker, several venues, a migration;
3. describe the path from a raw tick to a canonical [bar](glossary.md#bar) to a
   [microstructure primitive](glossary.md#microstructure-primitive), and where the anti-leakage
   gates and the manifests sit on it.

## S2 — Feature & Label Factory

**Intent** of [S2](sections/s2-feature-label-factory/README.md): a factory in which every
representation (clock, labels, weights, features) is causal, traceable, replayable and servable
under contracts (formats, latencies, versions), and in which nothing moves on until causality,
[train/serve parity](glossary.md#train-serve-parity) and
[temporal integrity](glossary.md#temporal-integrity) ([purging](glossary.md#purging) and
[embargo](glossary.md#embargo)) are proven.

| What to master first | Where to learn it |
|---|---|
| **Point in time and strict causality.** Prove that every variable exists at t₀: snapshots, [as-of joins](glossary.md#as-of-join), monotone timestamps, gaps and duplicates, time zones, calendars, halts. | [López de Prado (2018)](references.md#lopez-de-prado-2018) |
| **A common clock and alignment across assets.** An [event index](glossary.md#event-index) of increasing t₀, intervals [t₀, t₁], and a map that aligns assets on shared references of time. | [López de Prado (2018)](references.md#lopez-de-prado-2018) |
| **Train/serve parity and [reproducibility](glossary.md#reproducibility).** One logic, the same normalisations and parameters, hashes and fingerprints, [seeds](glossary.md#seed), and tests that offline equals online. | [Kleppmann (2017)](references.md#kleppmann-2017) |
| **Service levels and classes of latency.** T90 and T95 per class (real time, near real time, batch), windows of recomputation, [fallbacks](glossary.md#fallback) and [kill switches](glossary.md#kill-switch). | Reliability engineering; no book summary covers it. |
| **Temporal integrity: purged splits, embargo, [CPCV](glossary.md#cpcv).** The definition of [label overlap](glossary.md#label-overlap), purging by adjacency, a calibrated embargo, schemes for data that are not independent, registers of splits. | [López de Prado (2018)](references.md#lopez-de-prado-2018) |
| **[Market microstructure](glossary.md#market-microstructure) in practice.** Hours, auctions and suspensions; ticks and [spreads](glossary.md#spread); stale or out-of-order quotes and prints; [bid-ask bounce](glossary.md#bid-ask-bounce); the effects of rule changes. | [López de Prado (2018)](references.md#lopez-de-prado-2018) |
| **Robust statistics and outliers.** Controlled [winsorisation](glossary.md#winsorisation) and clipping, robust centres and scales, outliers by cell against by case, diagnostics of influence. | Robust statistics; no book summary covers it. |
| **Numerical conditioning and stability.** The [condition number](glossary.md#condition-number) κ, spectra, SVD and pivoted QR, tolerances, and the same numeric types in training and in serving. | Numerical linear algebra; multicollinearity from [López de Prado (2018)](references.md#lopez-de-prado-2018). |
| **Overlap and effective sample size.** The [uniqueness](glossary.md#uniqueness) of events, [overlap maps](glossary.md#overlap-map), and the [effective sample size](glossary.md#effective-sample-size) that weighting and resampling rely on. | [López de Prado (2018)](references.md#lopez-de-prado-2018) |
| **Registry, [versioning](glossary.md#versioning), lineage and contracts.** [Feature cards](glossary.md#feature-card), stable IDs, an immutable fingerprint, a graph of dependencies, contracts of service (time to freshness, p95 and p99, cache, quotas), packs of signatures and [drift](glossary.md#drift). | [Kleppmann (2017)](references.md#kleppmann-2017) |

**Ready when** the builder can:
1. define and find t₀ and t₁, and prove point in time for every column;
2. explain pure time against event time, and why a clock is driven by activity, by price, or by
   both;
3. describe label overlap, the embargo, the effective sample size, uniqueness, train/serve parity,
   service levels, and IDs, versions and hashes;
4. draw the interfaces in advance (schemas, IDs, latencies), and the [KPIs](glossary.md#kpi) of go
   and no-go.

## S3 — Strategy Lab

**Intent** of [S3](sections/s3-strategy-lab/README.md): take the strategies the lab hands over and
make them readable, solvable, robust and governable end to end, ready for the
[execution simulator](glossary.md#execution-simulator), cost analysis and live trading, with no
leakage, no ambiguity at any interface, and a clear economic reading of every trade-off between
costs, risks and complexity.

| What to master first | Where to learn it |
|---|---|
| **Point in time and no leakage.** Every datum, feature, label, cost and decision evaluated at its instant; one clock; frozen calendars and time zones; tests of leakage; replay bit for bit (versions, seeds, manifests). | [López de Prado (2018)](references.md#lopez-de-prado-2018) |
| **Objective, constraints and penalties.** A [net-of-cost objective](glossary.md#net-of-cost-objective), constraints (risk, exposures, [turnover](glossary.md#turnover), [liquidity](glossary.md#liquidity)), penalties on complexity (L1, L2, minimum description length), the [shadow price](glossary.md#shadow-price) of each constraint and the duality gap, convexity by default. | [Grinold & Kahn (1999)](references.md#grinold-kahn-1999); few degrees of freedom from [Carver (2015)](references.md#carver-2015). |
| **Microstructure and costs.** Spread, fees, timing [slippage](glossary.md#slippage), impact (relative size, participation), latencies end to end, queue priority, partial fills and rejects; costs bucketed, forecast against realised. | [Kissell (2013)](references.md#kissell-2013) |
| **Invariances, symmetries and neutralisations.** What must not change under rescaling, a shift in time, the [neutralisation](glossary.md#neutralisation) of the market mode or a permutation of sub-universes; the maximal invariant statistic; no normalisation may add information. | Statistics and information theory (the data-processing inequality); no book summary covers it. |
| **A [decision graph](glossary.md#decision-graph), one clock and a latency budget.** A chain of decisions with no cycle, a cadence and a latency per block, up- and down-sampling and adapters, a [latency budget](glossary.md#latency-budget) up to the order. | The chain of models from [Narang (2013)](references.md#narang-2013); latency budgets from systems engineering. |
| **Falsifiability and the mechanisms of alpha.** Theses of the form "if…, then…, because…" with conditions of activation and invalidation, a mechanism tied to observable variables, and what the thesis does not claim. | [Ilmanen (2011)](references.md#ilmanen-2011) |
| **Interface contracts and stable normalisations.** Formats in and out (units, scales, signs, cadence, maximum latency, missing values), schema charters, point-in-time validation. | [Carver (2015)](references.md#carver-2015) |
| **Robust statistics and bounded influence.** Robust estimators (targeted winsorisation, weighted medians, bounded slopes), a limit on the influence of outliers, [fuses](glossary.md#fuse) and degraded modes set off by the state of the market. | Robust statistics; no book summary covers it. |
| **Disciplined experimentation and multiplicity.** Factorial and orthogonal designs, randomisation, controls, early stopping, a common measure, an [empirical null](glossary.md#empirical-null), [shrinkage](glossary.md#shrinkage) after selection, the [false discovery rate](glossary.md#false-discovery-rate) under dependence. | [López de Prado (2018)](references.md#lopez-de-prado-2018); large-scale inference in statistics. |
| **Traceability, versioning and governance.** Logs of what changed, IDs, versions and hashes, delays to integrate critical events, alert thresholds, and triggers of [requalification](glossary.md#requalification) with monitoring and lifecycle. | [Kleppmann (2017)](references.md#kleppmann-2017) |

**Ready when** the builder can:
1. explain in two minutes the net-of-cost objective, the 4–7 constraints that shape it, and what
   will be read (multipliers, diagnostics);
2. show that the chain is a graph with no cycle, with one clock, budgeted latencies, and inputs and
   outputs validated point in time;
3. make the [invariances](glossary.md#invariance) and neutralisations explicit and testable;
4. hold a plan of comparable experiments, a common measure, an empirical null and a protocol for
   multiplicity;
5. make the rules of [robustness](glossary.md#robustness) (fuses, degraded modes), the service
   levels and the triggers of requalification clear enough to publish.

## S4 — Validation, execution simulation, cost analysis, paper trading

**Intent** of [S4](sections/s4-validation/README.md): honest tests against the future, against
statistical illusions, at a size that can be executed and in a form that can be audited; every
conclusion must hold out of sample, across regimes and under realistic costs, or it is only a story.

| What to master first | Where to learn it |
|---|---|
| **Point in time and market clocks.** Market calendars (holidays, half days), time zones (UTC or local), monotone timestamps, and temporal leakage caught in features and labels. | [López de Prado (2018)](references.md#lopez-de-prado-2018) |
| **Temporal validation: [walk-forward](glossary.md#walk-forward), purged [cross-validation](glossary.md#cross-validation), CPCV.** When to use each, sizing [in-sample](glossary.md#in-sample-out-of-sample) and out-of-sample, the stride, reading a distribution of results rather than one path, the coverage of regimes. | [López de Prado (2018)](references.md#lopez-de-prado-2018); [Jansen (2020)](references.md#jansen-2020) |
| **Purging and embargo.** A purge p ≥ max(L, H) and an embargo e ≥ L (and no shorter than the operational latency when it matters); cleaned in-sample indices; purged overlap close to 100%. | [López de Prado (2018)](references.md#lopez-de-prado-2018) |
| **Robust measures and non-normality.** Metrics and confidence intervals that hold under heavy tails; median, dispersion and tails; the probabilistic and [deflated Sharpe ratios](glossary.md#deflated-sharpe-ratio). | [López de Prado (2018)](references.md#lopez-de-prado-2018) |
| **Multiple trials and the trial registry.** Counting trials, the effective number of trials once correlations are counted, control of the false discovery rate, deflated probabilities: no winner by contest. | [López de Prado (2018)](references.md#lopez-de-prado-2018); [multiple testing](glossary.md#multiple-testing) in statistics. |
| **[Statistical power](glossary.md#statistical-power) and sample size.** Curves of power for a net target effect, telling "not enough evidence" from "no effect", and the duration needed for a power of 80% or more. | Statistics; no book summary covers it. |
| **Microstructure and the grammar of execution.** [Order books](glossary.md#order-book), matching rules, latencies, order types, queues, intraday regimes; [implementation shortfall](glossary.md#implementation-shortfall), effective and realised costs, rates and delays of fill, temporary and permanent impact. | [Kissell (2013)](references.md#kissell-2013) |
| **Canonical cost analysis.** The decision price anchored, implementation shortfall, costs split into timing, impact, spread, fees, opportunity and latency, normalised by context against Simpson's paradox, and scorecards. | [Kissell (2013)](references.md#kissell-2013); Simpson's paradox from statistics. |
| **Capacity and the fundamental law.** [Information coefficient](glossary.md#information-coefficient), effective [breadth](glossary.md#breadth), [IR](glossary.md#ir) ≈ [IC](glossary.md#ic) × √breadth, then costs and turnover to the net IR through the [execution transfer coefficient](glossary.md#execution-transfer-coefficient) τ; the [capacity](glossary.md#capacity) curve and the operating point. | [Grinold & Kahn (1999)](references.md#grinold-kahn-1999) |
| **Verification, validation, traceability and reproducibility.** [Pre-registration](glossary.md#pre-registration), seeds, versions, manifests and fingerprints, cold replay, [certification dossiers](glossary.md#certification-dossier), service levels on updates. | [Kleppmann (2017)](references.md#kleppmann-2017); pre-registration from experimental science, [verification and validation](glossary.md#verification-and-validation) from simulation engineering. |
| **Operational guardrails and runbooks.** Quantified alerts, kill switches, [rollback](glossary.md#rollback) and quarantine, [RACI](glossary.md#raci), [drills](glossary.md#drill), and service levels on latency, rejects, and drifts of costs and performance. | Reliability engineering and [incident response](glossary.md#incident-response); no book summary covers them. |

**Ready when** the builder can:
1. express every metric in the same base of time and unit (annualisation, time zone, universe);
2. lock the experimental charter before cutting the data;
3. keep a [trial registry](glossary.md#trial-registry) and a target false discovery rate;
4. define costs from the decision price to the last fill, comparable everywhere;
5. run a cold replay (bit for bit for execution) in 30 minutes or less.

## S5 — Decision & Execution

**Intent** of [S5](sections/s5-decision-execution/README.md): turn validated alphas into live
capital (admitted, sized, aligned with the budgets, turned into target weights, reached through a
planned transition, executed, then measured and recalibrated), point in time, under service levels,
with [gates](glossary.md#gate), hooks and rollback, so that every decision is explainable, bounded
and reversible.

| What to master first | Where to learn it |
|---|---|
| **Point in time and versioning.** Data that can be replayed, versioned identifiers, monotone timestamps, consistent calendars and units; without them, compatibility, cost analysis and audit are wrong by construction. | [Kleppmann (2017)](references.md#kleppmann-2017) |
| **Microstructure, costs and capacity, before and after trading.** Spread, impact and latency, curves of participation against %ADV, ex-ante against ex-post, these models under stress, and the capacity that can be sustained. | [Kissell (2013)](references.md#kissell-2013) |
| **Budgets and constraints, hard or soft, turned into penalties.** A hierarchy of limits (risk, liquidity, concentration, turnover), [hard constraints](glossary.md#hard-soft-constraint) (never breached) against soft ones (penalised), shadow prices and sensitivities, tests of monotonicity and feasibility. | [Grinold & Kahn (1999)](references.md#grinold-kahn-1999) |
| **Horizon, half-life and cadence.** The natural speed of a signal tied to the window of analysis, the [no-trade zones](glossary.md#no-trade-zone) and the frequency of decision, against costly over-reaction. | [Carver (2015)](references.md#carver-2015); signal decay from [Grinold & Kahn (1999)](references.md#grinold-kahn-1999). |
| **Portfolio compatibility and interactions.** The [marginal Sharpe ratio](glossary.md#marginal-sharpe-ratio), co-movements and co-drawdowns, overlap of factors and of operations, and rules of interaction: caps, neutralisations, penalties. | [Grinold & Kahn (1999)](references.md#grinold-kahn-1999) |
| **Service levels and operational latency.** Latencies of computation, of publication and of ingesting critical events (IPOs, halts, delistings), with alerts and degraded modes. | Reliability engineering; no book summary covers it. |
| **Stress testing across regimes.** A library of scenarios (volatility, liquidity, dispersion, microstructure), criteria of overshoot and of return to normal, and the waterbed effect between budgets. | Crises from [Ilmanen (2011)](references.md#ilmanen-2011); [stress tests](glossary.md#stress-test) from [Kissell (2013)](references.md#kissell-2013); the waterbed effect from risk-management practice. |
| **Journalling and strong traceability.** Canonical schemas (parent order, child orders, fills), a point-in-time commit of record, links to the references of market and constraints and to versions, and an audit in 5 minutes. | [Kleppmann (2017)](references.md#kleppmann-2017) |
| **[Value at risk of change](glossary.md#value-at-risk-of-change) and the [cost of change](glossary.md#cost-of-change).** The risk that comes from adjusting, not only from the final exposure, and a budget for the cost of [rebalancing](glossary.md#rebalancing). | [Kissell (2013)](references.md#kissell-2013) |
| **Deployment governance and safety.** The [deployment rulebook](glossary.md#deployment-rulebook), RACI, the path paper → [canary](glossary.md#canary-release) → gradual → full, throttles, [circuit breakers](glossary.md#circuit-breaker) and kill switches, and [runbooks](glossary.md#runbook) of rollback. | [Paper trading](glossary.md#paper-trading) up to graduation from [López de Prado (2018)](references.md#lopez-de-prado-2018); the rest from reliability engineering. |

**Ready when** the builder can:
1. reason net of costs and impact, and decide at a rhythm aligned with each signal's
   [half-life](glossary.md#half-life);
2. keep point-in-time hygiene (timestamped versions, stable identifiers, harmonised time zones), to
   avoid any leakage and replay every verdict;
3. translate hard and soft budgets into constraints and penalties an optimiser can consume, and
   stress them before any release to production;
4. reach first for canary, then gradual, then full, under [guardrails](glossary.md#guardrail)
   (throttles, breakers, kill switch), with a tested rollback.

## S6 — Monitoring

**Intent** of [S6](sections/s6-monitoring/README.md): see right, early and in a way that can be
acted on, with a [single source of truth](glossary.md#single-source-of-truth)
([SLIs](glossary.md#sli), SLOs, [baselines](glossary.md#baseline)), detectors that make little
noise, reversible controllers, a [traceability](glossary.md#traceability) that holds up
(point-in-time replay) and a platform of [monitoring as code](glossary.md#monitoring-as-code);
evidence timestamped, versions frozen, p95 and p99 everywhere, and decisions centred on symptoms.

| What to master first | Where to learn it |
|---|---|
| **The grammar of SLIs, SLOs and errors.** An enforceable SLI (formula, unit, window, filters), SLOs per journey and segment, an [error budget](glossary.md#error-budget) per day, week or month, the attainment of each SLO, [burn rates](glossary.md#burn-rate) over several windows, severities and routing. | Reliability engineering; no book summary covers it. |
| **Baselines and segmented normality.** Normal per hour, day, regime and venue; robust profiles of quantiles; frozen windows, against temporal leakage; a policy of refresh; the detection of drift. | Robust statistics and reliability engineering; no book summary covers them. |
| **Timestamps and disciplined time.** Sources of time, a [clock skew budget](glossary.md#clock-skew-budget), monotone timestamps, what to do when clocks disagree, constraints at p95 and p99 per domain. | [Kleppmann (2017)](references.md#kleppmann-2017) |
| **Identities and correlation end to end.** Stable IDs (parent, child, fill), idempotence, keys that correlate a tick with its fill, distributed traces. | [Kleppmann (2017)](references.md#kleppmann-2017) |
| **An immutable journal and replay.** Append-only records kept in [WORM storage](glossary.md#worm-storage), hashing and chaining, a register of amendments, versioned snapshots of data, code and parameters, reproducible within ±ε. | [Kleppmann (2017)](references.md#kleppmann-2017) |
| **Robust statistics and quantiles.** p95, p99 and p99.9, the interquartile range, robust deviations, never a mean alone for latency or the quality of execution, confidence intervals, aggregation by desk, venue, symbol and regime. | Robust statistics; no book summary covers it. |
| **Microstructure and execution.** Benchmarks (arrival price, implementation shortfall), [markouts](glossary.md#markout) over several horizons, spread, volatility, liquidity and impact, passive against aggressive, rejects, acknowledgements, fills, fees. | [Kissell (2013)](references.md#kissell-2013) |
| **Sequential detection against noise.** Change points, scores of distance between distributions, [hysteresis](glossary.md#hysteresis), dwell time, refractory periods, fusion of signals, budgets of false positives, of precision and of time to detect. | Structural breaks from [López de Prado (2018)](references.md#lopez-de-prado-2018); sequential statistics. |
| **Control in production.** [Rate limiters](glossary.md#rate-limiter), backoff, circuit breakers, [operating modes](glossary.md#operating-mode) (normal, cautious, degraded, stopped), cooldowns and locality (venue, strategy, instrument): a fast time to safety without oscillation. | Reliability engineering and control; no book summary covers them. |
| **Incident management and postmortems.** Roles (incident commander, operator, spokesperson), an [incident severity](glossary.md#incident-severity) from P1 to P4, one timeline, a 2-page postmortem with dated actions and owners. | Reliability engineering; no book summary covers it. |
| **Security operations for [observability](glossary.md#observability).** Access by least privilege, multi-factor authentication and rotated secrets, attested binaries, controlled egress, latencies of detection and containment, separated roles, logs in WORM storage. | Security engineering; no book summary covers it. |
| **Monitoring as code, and its costs.** Versioned rules, a pipeline of lint, tests, dry runs, canary and rollback, quotas on cardinality and retention, tenancy and [showback](glossary.md#showback), topics of events and idempotent hooks of actuation. | [Kleppmann (2017)](references.md#kleppmann-2017); reliability engineering. |

**Ready when** the builder can:
1. define SLIs and SLOs, with their error budgets and burn rates;
2. build baselines per segment and regime, and read robust quantiles, never a mean alone;
3. work with reliable timestamps, correlation IDs end to end, and point-in-time replay;
4. explain sequential detection, hysteresis, dwell time and closed-loop control (rate limiters,
   backoff, circuit breakers);
5. produce the timeline of an incident and a
   [blameless postmortem](glossary.md#blameless-postmortem) with traced actions.

## S7 — Lifecycle

**Intent** of [S7](sections/s7-lifecycle/README.md): the living governance of the factory, which
turns signals, measures and constraints into written, traceable and replayable decisions without
breaking the chain from data to features, alpha and order, with rigour about time (point in time),
append-only records, releases that can be undone, and a net reading of the budgets of reliability,
risk and capital.

| What to master first | Where to learn it |
|---|---|
| **The grammar of time and point in time.** Event, decision, knowledge and processing time; as of T with no look-ahead; time zones; valid windows (markets, holidays); rules for late revisions. | [Kleppmann (2017)](references.md#kleppmann-2017) |
| **Canonical identities and lineage end to end.** Stable IDs (of datasets, feature sets, strategies, models, orders, executions, runs), [immutability](glossary.md#immutability), append-only records and idempotence, artefacts linked by fingerprint down to the fill. | [Kleppmann (2017)](references.md#kleppmann-2017) |
| **SLOs, SLIs and error budgets.** 2–4 SLIs per critical flow, SLOs on P95 or P99 quantiles, error budgets and burn rates, green, amber and red read with hysteresis against flapping. | Reliability engineering; no book summary covers it. |
| **Risk budgets.** [Tracking error](glossary.md#tracking-error), [expected shortfall](glossary.md#expected-shortfall), stress, liquidity, turnover and capacity: definitions, consistent horizons, aggregation per idea or book, and the share consumed in real time to guide ramp-ups and freezes. | [Grinold & Kahn (1999)](references.md#grinold-kahn-1999) |
| **Live against simulated.** A taxonomy of gaps in performance and costs (latency, costs, microstructure, data, non-determinism), what they mean for cost analysis, and the limits of capacity. | [Kissell (2013)](references.md#kissell-2013) |
| **Reversible release strategies.** Blue-green, canary, [progressive rollout](glossary.md#progressive-rollout), feature flags, kill switch, a timed rollback, and "expand and contract" for schemas and APIs. | Continuous delivery; schemas that evolve without breaking their readers from [Kleppmann (2017)](references.md#kleppmann-2017). |
| **An operational journal of decisions.** No hotfix outside the journal, an envelope for each event (identities, timestamps, fingerprints, the minimal context), one system of record across sections. | [Kleppmann (2017)](references.md#kleppmann-2017) |
| **[Fitness functions](glossary.md#fitness-function) and gates.** A target property (latency, drift, cost per unit of alpha, coupling) turned into living tests (before merge, at a cadence, on an event) that open or close the gates. | Evolutionary architecture; no book summary covers it. |
| **Capacity and cost curves.** Safe participation, market depth, cheap windows, curves of spread, impact and commissions, and the biases of their estimates. | [Kissell (2013)](references.md#kissell-2013) |
| **Incident command, severities and blameless postmortems.** Roles (incident commander, scribe, technical lead), one channel, a safe state before any diagnosis, factual timelines, corrective actions with tests of non-regression. | Reliability engineering; no book summary covers it. |

**Ready when** the builder can:
1. explain as-of, and event, decision, knowledge and processing time, without hesitating;
2. read an error budget and conclude go, slow down or stop;
3. tell live from simulated (alpha and costs), and draw a written action from the gap;
4. describe a clean rollout: canary, then tiers, then rollback;
5. prove the chain from data to trade: identities, fingerprints, [lineage](glossary.md#lineage).
