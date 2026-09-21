[Up: Factory](../README.md)

# Sections — the 64 sub-sections

## TL;DR

The factory is split into seven sections and 64 sub-sections, and every sub-section page has the same layout.
This page lists them all, one line each, in pipeline order: from raw data to the lifecycle of live strategies.

## How pages are named

- Sub-section IDs run from `S1.1` to `S7.10`. They are stable across the repository: every page,
  table and diagram refers to a sub-section by its ID.
- Each section has a folder, `sN-<slug>/`, whose `README.md` presents the section on one page.
- Each sub-section has one file in its section's folder, named `sN.K-<short-slug>.md`.
- File names are frozen: a title may be reworded later, its file name does not change.

## Index

| ID | Sub-section | Purpose |
|---|---|---|
| **S1** | **[Data Foundation](s1-data-foundation/README.md)** | |
| S1.1 | [Identity, reference data & point-in-time universe](s1-data-foundation/s1.1-identity-reference-universe.md) | Who each instrument is, where it trades and whether it could be traded, on any past day. |
| S1.2 | [Temporal semantics & bitemporality](s1-data-foundation/s1.2-bitemporality.md) | Two clocks on every fact, and reads made only as of a stated date. |
| S1.3 | [Deterministic timebase, immutability & replay](s1-data-foundation/s1.3-timebase-replay.md) | One immutable, ordered event log that replays bit for bit. |
| S1.4 | [Causality & multi-source synchronisation](s1-data-foundation/s1.4-causality-synchronization.md) | Multi-source panels in which no value is used before it was published. |
| S1.5 | [Data quality: rules, ML and human in the loop](s1-data-foundation/s1.5-data-quality.md) | Rules, detectors and people certify every dataset before it is used. |
| S1.6 | [Corporate actions, adjustments & traceability](s1-data-foundation/s1.6-corporate-actions.md) | Splits, dividends and mergers adjusted without leaking the future. |
| S1.7 | [Canonical market views & microstructure primitives](s1-data-foundation/s1.7-canonical-market-views.md) | One standard set of bars and microstructure measures for the whole factory. |
| S1.8 | [Governance: provenance, versioning & anti-leakage gates](s1-data-foundation/s1.8-data-governance.md) | The single gate: sealed, versioned batches with proof of no leakage. |
| **S2** | **[Feature & Label Factory](s2-feature-label-factory/README.md)** | |
| S2.1 | [Event clocks & sampling design](s2-feature-label-factory/s2.1-event-clocks-sampling.md) | When to observe: a causal event index per asset and regime, in place of the wall clock. |
| S2.2 | [Labelling schemes (side, size, meta)](s2-feature-label-factory/s2.2-labeling.md) | What followed each event: its side, its size and a meta label, all point-in-time. |
| S2.3 | [Overlap-aware sample weights & resampling](s2-feature-label-factory/s2.3-sample-weights.md) | Weights that count overlapping events once, and resampling without leakage. |
| S2.4 | [Temporal integrity & validation-ready indexing](s2-feature-label-factory/s2.4-temporal-integrity.md) | Purged, embargoed, versioned splits: validation with zero leakage. |
| S2.5 | [Stationarity & memory preservation](s2-feature-label-factory/s2.5-stationarity-memory.md) | Stationary series that keep the memory carrying the edge. |
| S2.6 | [Robust feature construction, microstructure & regime encoding](s2-feature-label-factory/s2.6-robust-features.md) | Robust multi-horizon features, quality flags and dated market regimes. |
| S2.7 | [Numerical conditioning & orthogonalisation](s2-feature-label-factory/s2.7-numerical-conditioning.md) | Well-scaled, weakly redundant features, identical in research and serving. |
| S2.8 | [Information & dimension management](s2-feature-label-factory/s2.8-information-dimension.md) | A short, stable, cheap core of features, chosen out of sample. |
| S2.9 | [Representation sanity & leakage checks](s2-feature-label-factory/s2.9-leakage-checks.md) | The firewall: nothing leaves section 2 unless it is usable at t0. |
| S2.10 | [Registry, lineage & feature-serving contracts](s2-feature-label-factory/s2.10-feature-registry.md) | The registry: what each feature is, how it was made and how it is served. |
| **S3** | **[Strategy Lab](s3-strategy-lab/README.md)** | |
| S3.1 | [Admission: dossier intake & decision frame](s3-strategy-lab/s3.1-admission.md) | The front door: the lab's dossier checked, its thesis restated, then admitted, returned or rejected. |
| S3.2 | [Architecture & invariances: re-implementation on factory data](s3-strategy-lab/s3.2-architecture-invariances.md) | The strategy rebuilt on factory data, in a standard architecture; the lab's result must reproduce. |
| S3.3 | [Disciplined optimisation programme](s3-strategy-lab/s3.3-disciplined-optimization.md) | Fine calibration under a declared trial budget: a useful objective, few constraints, a stable solution. |
| S3.4 | [Alpha combination & internal allocation](s3-strategy-lab/s3.4-alpha-combination.md) | Many alphas into one position per asset, and the strategy measured against those already running. |
| S3.5 | [Large-scale inference (calibration, shrinkage, tests, multiplicity)](s3-strategy-lab/s3.5-large-scale-inference.md) | Hundreds of variants into a few credible candidates, the lab's trials counted. |
| S3.6 | [Controlled variant exploration & experiment design](s3-strategy-lab/s3.6-variant-exploration.md) | Controlled variants around the admitted strategy, never idea search: which hold, which break. |
| S3.7 | [Robustness by construction](s3-strategy-lab/s3.7-robustness-by-construction.md) | Shock absorbers built into the strategy: close to the plain version in calm markets, safer in dirty ones. |
| S3.8 | [Simulation plans & pass criteria (towards section 4)](s3-strategy-lab/s3.8-simulation-plans.md) | The test bench and the frozen green, orange or red contract that section 4 will run. |
| S3.9 | [Traceability & design rationale: the living strategy dossier](s3-strategy-lab/s3.9-traceability-rationale.md) | The living strategy dossier: idea, choices, trials, evidence and decision, replayable by anyone. |
| **S4** | **[Validation, execution simulation, cost analysis, paper trading](s4-validation/README.md)** | |
| S4.1 | [Experimental protocol & anti-leakage barriers](s4-validation/s4.1-experimental-protocol.md) | Honest tests against the future: purged and embargoed partitions, every trial run and counted. |
| S4.2 | [Validity inference & control of statistical illusions](s4-validation/s4.2-validity-inference.md) | A probabilistic verdict on each edge: real, repeatable and useful after costs, deflated for every trial. |
| S4.3 | [Hierarchical selection & selection-bias risk (PBO)](s4-validation/s4.3-selection-bias.md) | A tournament that measures how likely the in-sample winner is to fail out of sample. |
| S4.4 | [Multi-axis robustness & sensitivity (statistical and engineering)](s4-validation/s4.4-robustness-sensitivity.md) | What breaks the strategy when data, costs, liquidity, latency or regimes are shaken. |
| S4.5 | [Economic viability, capacity & the fundamental law](s4-validation/s4.5-economic-viability.md) | Net P&L at size: costs, turnover, capacity, and the share of the edge that survives execution. |
| S4.6 | [Execution simulator (XSIM): microstructure, calibration, verification & validation](s4-validation/s4.6-execution-simulator.md) | The execution twin: costs, fills and delays at size and by regime, calibrated and validated. |
| S4.7 | [Universal transaction cost analysis & execution attribution (closed loop)](s4-validation/s4.7-transaction-cost-analysis.md) | The meter of ground truth: every basis point from decision to fill, measured and explained. |
| S4.8 | [Orchestrated paper trading & operational guardrails](s4-validation/s4.8-paper-trading.md) | The factory's paper-trading campaign: the whole chain live on the market, with no capital at risk. |
| S4.9 | [Scientific governance, traceability & reproducibility](s4-validation/s4.9-scientific-governance.md) | Every result pre-registered, traced, and replayable by any peer within a known tolerance. |
| S4.10 | [Promotion gates, risk tolerances & fallback mechanisms](s4-validation/s4.10-promotion-gates.md) | The promotion gate: go, go under conditions or no-go, with its limits, ramp-up and retreat. |
| **S5** | **[Decision & Execution](s5-decision-execution/README.md)** | |
| S5.1 | [Onboarding & capital eligibility](s5-decision-execution/s5.1-onboarding-eligibility.md) | Whether a promoted strategy enters the portfolio, at what size and within which bounds: its entry ticket. |
| S5.2 | [Interaction mapping & alpha diversification](s5-decision-execution/s5.2-interaction-mapping.md) | Who resembles, completes, hinders or breaks with whom: the living interaction map and its rules. |
| S5.3 | [Portfolio construction engine (convex & stochastic)](s5-decision-execution/s5.3-portfolio-construction.md) | Target weights that maximise net value within the budgets: feasible, robust, explained by their sensitivities. |
| S5.4 | [Allocation layer & budgets (risk, liquidity, capacity)](s5-decision-execution/s5.4-allocation-budgets.md) | The workable envelope of risk, liquidity and capacity, as constraints the engine applies: the risk budget book. |
| S5.5 | [Regime adaptation (sequential control)](s5-decision-execution/s5.5-regime-adaptation.md) | Exposures scaled to the market regime, only when the benefit beats the cost, never beyond the budgets. |
| S5.6 | [Transition planner (path-aware rebalancing)](s5-decision-execution/s5.6-transition-planner.md) | What to move, when and how fast, from the current portfolio to the target: the dated transition plan. |
| S5.7 | [Unified execution chain (pre-trade, smart routing, OMS/EMS)](s5-decision-execution/s5.7-execution-chain.md) | Target weights and a transition path turned into real fills at the least cost, safely, with every order traced. |
| S5.8 | [Execution analytics & the TCA/XSIM feedback loop into decisions](s5-decision-execution/s5.8-execution-analytics.md) | What execution really cost, why it differed from the forecast, and the recalibrated costs and rules that follow. |
| S5.9 | [Governance, safety & risk-driven deployment](s5-decision-execution/s5.9-governance-safety.md) | The control tower: decisions released in small doses, bounded, reversible in minutes, explained in five. |
| **S6** | **[Monitoring](s6-monitoring/README.md)** | |
| S6.1 | [Single source of truth: shared observability (SLIs, SLOs & baselines)](s6-monitoring/s6.1-shared-observability.md) | One common, measurable and binding language about operations: what is measured, what is promised, what is normal. |
| S6.2 | [Live execution fidelity & operational TCA](s6-monitoring/s6.2-execution-fidelity.md) | The live quality of fills against section 4's expectations: each gap qualified, each action proven. |
| S6.3 | [Data integrity, traceability & compliance](s6-monitoring/s6.3-data-integrity-compliance.md) | A continuous, replayable journal of truth: every figure traced to its source events, reconciled, provable in audit. |
| S6.4 | [Drift & regime-change detection](s6-monitoring/s6.4-drift-detection.md) | Spots early that the factory has left the world it expects, and puts it in the right mode before anything degrades. |
| S6.5 | [Stabilisation & controlled degradation](s6-monitoring/s6.5-controlled-degradation.md) | Immediate, proportionate and reversible actions that keep the factory in its safe zone, down a ladder of modes. |
| S6.6 | [Operational security & posture (factory SecOps)](s6-monitoring/s6.6-operational-security.md) | Security under control: see early, decide fast, contain cleanly, with a trail that can be replayed. |
| S6.7 | [Intervention & learning](s6-monitoring/s6.7-intervention-learning.md) | The control tower when things go wrong, and the record that stops them from happening again. |
| S6.8 | [Observability platform & monitoring-as-code](s6-monitoring/s6.8-monitoring-as-code.md) | The single control room: one platform that captures, correlates, alerts and acts, all managed as code. |
| **S7** | **[Lifecycle](s7-lifecycle/README.md)** | |
| S7.1 | [Steering cadences & directional vision](s7-lifecycle/s7.1-steering-cadences.md) | A short, regular ritual that rules on reliability, reads the health of alpha, sets the course, and ends in written decisions that become missions. |
| S7.2 | [Traceability, audit & explainability: the system of record for decisions](s7-lifecycle/s7.2-decision-record.md) | The factory's system of record: who decided what, when, why and with what, down to the fill, with a readable reason per trade and a replay that matches reality. |
| S7.3 | [System-wide fitness & architectural evolution](s7-lifecycle/s7.3-architectural-fitness.md) | What good means for the factory, encoded as living tests that let each change through, slow it or stop it, and that steer the architecture's evolution. |
| S7.4 | [Reliability budgets (SLO/SLI) & risk budgets](s7-lifecycle/s7.4-reliability-risk-budgets.md) | An automatic, traceable frame that couples the error budget left and the risk budget consumed, and says when the factory may accelerate and when it must ease off. |
| S7.5 | [Change management & release strategies](s7-lifecycle/s7.5-change-management.md) | Any change reaches production as one immutable release package: checked before flight, rehearsed, rolled out step by step under guard, and reversible in seconds. |
| S7.6 | [Model & strategy lifecycle (champion / challenger)](s7-lifecycle/s7.6-champion-challenger.md) | A permit to operate for each strategy, and its clean withdrawal: statuses, a path through paper trading, a canary and capital tiers, the rules that move capital, and the triggers. |
| S7.7 | [Data lifecycle & provenance](s7-lifecycle/s7.7-data-lifecycle.md) | Keeps section 1's guarantees true over the life of the data: a reliable record for every value, living contracts, idempotent backfills, batch and stream that converge. |
| S7.8 | [Capital, capacity & cost steering](s7-lifecycle/s7.8-capital-cost-steering.md) | The right size at the right place and pace: capital, capacity and costs arbitrated at a cadence, moves smoothed, budgets respected, every choice journalled. |
| S7.9 | [Incident response & blameless postmortems](s7-lifecycle/s7.9-incident-response.md) | Stabilise fast, explain clearly, correct for good: the frame every incident runs in, and the follow-through that turns each postmortem into lasting fixes. |
| S7.10 | [Monitoring-to-missions feedback loop](s7-lifecycle/s7.10-monitoring-feedback-loop.md) | One queue of missions: every relevant signal becomes a short, reversible, measurable mission, run as a canary, decided on its criteria, and recorded. |
