[Up: Factory](README.md)

# Stack

## TL;DR

One concrete tool per component of the factory, each with the reason it fits: a reference, not a requirement.
Any tool that meets the same need can replace it; what does not change is the practice it serves.
Each was checked on 21 September 2026: maintained, and able to do what its line says, per its own documentation.

## Data foundation

| Component | Kept by | Reference tool | Why this one | Practice it serves |
|---|---|---|---|---|
| [Event log](glossary.md#event-log) | [S1.3](sections/s1-data-foundation/s1.3-timebase-replay.md) | Apache Kafka | An append-only, partitioned log whose readers can [replay](glossary.md#replay) from any offset still retained; since version 4 it runs without ZooKeeper. | Logs and replay (Kleppmann) |
| [Bitemporal store](glossary.md#bitemporal-store) | [S1.2](sections/s1-data-foundation/s1.2-bitemporality.md) | XTDB | [Valid time](glossary.md#valid-time) and system time are built in, and a query reads as of either one. | Temporal-database practice |
| [Sealed batches](glossary.md#sealed-batch) and [batch registry](glossary.md#batch-registry) | [S1.8](sections/s1-data-foundation/s1.8-data-governance.md) | Apache Iceberg | Each batch is an immutable version of a table, pinned by its ID and read back by ID or by time. A version that a job pins is never expired: once expired, it can no longer be read. | Reproducible-computing practice |
| [Evidence locker](glossary.md#evidence-locker) | S1.8 | Amazon S3 Object Lock | In compliance mode, a stored version can be neither overwritten nor deleted by anyone until its retention ends. | Security engineering |
| As-of reads | S1.8 | DuckDB | Its ASOF JOIN pairs each row with the latest reference value at or before its time. | Temporal-database practice |
| Tests at the [gates](glossary.md#gate) | [S1.5](sections/s1-data-foundation/s1.5-data-quality.md), S1.8, [S2.9](sections/s2-feature-label-factory/s2.9-leakage-checks.md) | GX Core (Great Expectations) | Declarative expectations about data, run as checkpoints that pass or fail a batch. | Data-quality engineering |
| Instrument identity | [S1.1](sections/s1-data-foundation/s1.1-identity-reference-universe.md) | OpenFIGI | A free API that maps vendors' identifiers to FIGIs, the open identifiers of instruments and their listings. | Reference-data practice |
| [Trading calendars](glossary.md#trading-calendar) | S1.2 | exchange_calendars | Holidays, early closes and late opens for more than fifty exchanges. | Market-data practice |
| Clock discipline | S1.3, [S6.1](sections/s6-monitoring/s6.1-shared-observability.md) | chrony | Keeps a server's clock typically within tens of microseconds over a local network, and below one with hardware timestamps. | Clocks (Kleppmann) |

## Features, strategies and validation

| Component | Kept by | Reference tool | Why this one | Practice it serves |
|---|---|---|---|---|
| Pipelines and schedules | Every section | Dagster | Assets whose dependencies form the [lineage](glossary.md#lineage), and partitions that rerun a range of dates. | Reproducible-computing practice |
| [Feature registry](glossary.md#feature-registry) and serving | [S2.10](sections/s2-feature-label-factory/s2.10-feature-registry.md) | Feast | [Point-in-time](glossary.md#point-in-time) correct training sets, and an online store that serves the same definitions. | [Train/serve parity](glossary.md#train-serve-parity) (principle 2) |
| [Trial registry](glossary.md#trial-registry) and the dossier's runs | [S3.9](sections/s3-strategy-lab/s3.9-traceability-rationale.md), [S4.2](sections/s4-validation/s4.2-validity-inference.md) | MLflow | Every run with its parameters, metrics and artefacts, and a registry of versions linked back to their runs. | Counting every trial (López de Prado) |
| Optimiser | [S3.3](sections/s3-strategy-lab/s3.3-disciplined-optimization.md), [S5.3](sections/s5-decision-execution/s5.3-portfolio-construction.md), [S5.6](sections/s5-decision-execution/s5.6-transition-planner.md) | CVXPY | Convex problems written in Python, with the dual value, the [shadow price](glossary.md#shadow-price), of each explicit constraint. | [Convex optimisation](glossary.md#convex-optimisation) (Grinold & Kahn) |
| [Execution simulator](glossary.md#execution-simulator) | [S4.6](sections/s4-validation/s4.6-execution-simulator.md) | NautilusTrader | The same strategy code runs in [backtest](glossary.md#backtest) and live; fills walk the book when it is fed order-book data, and the position in the queue can be modelled. | Execution and costs (Kissell) |
| Cost analysis | [S4.7](sections/s4-validation/s4.7-transaction-cost-analysis.md), [S5.8](sections/s5-decision-execution/s5.8-execution-analytics.md) | Polars | No open-source tool is a standard for cost analysis: [implementation shortfall](glossary.md#implementation-shortfall) and its split are computed on the [execution log](glossary.md#execution-log), with a fast dataframe engine that plans its queries. | Costs (Kissell) |

## Decision and execution

| Component | Kept by | Reference tool | Why this one | Practice it serves |
|---|---|---|---|---|
| [Execution chain](glossary.md#execution-chain) and [kill switch](glossary.md#kill-switch) | [S5.7](sections/s5-decision-execution/s5.7-execution-chain.md), [S5.9](sections/s5-decision-execution/s5.9-governance-safety.md) | NautilusTrader | Live trading on the simulator's own code, with a risk engine whose trading states (active, reducing, halted) the kill switch and the [control directives](glossary.md#control-directive) set. | Train/serve parity (principle 2); reliability engineering |
| Rules as code: [deployment rulebook](glossary.md#deployment-rulebook), [policy matrix](glossary.md#policy-matrix) | S5.9, [S7.4](sections/s7-lifecycle/s7.4-reliability-risk-budgets.md) | Open Policy Agent | Rules written as code in its Rego language, versioned and tested, then evaluated at each decision. | Continuous delivery |
| Signed decisions: [entry ticket](glossary.md#entry-ticket), [promotion record](glossary.md#promotion-record), [capital ladder](glossary.md#capital-ladder) | [S4.10](sections/s4-validation/s4.10-promotion-gates.md), [S5.1](sections/s5-decision-execution/s5.1-onboarding-eligibility.md), [S7.6](sections/s7-lifecycle/s7.6-champion-challenger.md) | GitHub pull requests | A protected branch can require a set number of approving reviews, and a code owner's, before a change merges: two pairs of eyes by construction. | The producer is never the judge (principle 4) |

## Monitoring

| Component | Kept by | Reference tool | Why this one | Practice it serves |
|---|---|---|---|---|
| Metrics and alerts | S6.1 | Prometheus | Metrics, with recording rules that precompute them and alerting rules that fire. | Reliability engineering |
| [SLO catalogue](glossary.md#slo-catalogue) | S6.1 | Sloth | Each [SLO](glossary.md#slo) written once as a specification (its own format or OpenSLO), from which it generates the recording rules and the alerts on [burn rates](glossary.md#burn-rate) over several windows. | Reliability engineering |
| Traces and correlation IDs | S6.1, [S6.2](sections/s6-monitoring/s6.2-execution-fidelity.md) | OpenTelemetry | Traces, metrics and logs with one trace ID carried across services, from the tick to the fill. | Reliability engineering |
| [Drift](glossary.md#drift) detection | [S6.4](sections/s6-monitoring/s6.4-drift-detection.md) | Evidently | Reports and pass-or-fail tests of drift on data, predictions and targets. | Robust statistics |
| Secrets | [S6.6](sections/s6-monitoring/s6.6-operational-security.md) | OpenBao | Credentials created on demand and revoked when their lease ends, and rotation; an open-source fork of Vault, under the Linux Foundation. | Security engineering |
| Signed artefacts | S6.6, [S7.5](sections/s7-lifecycle/s7.5-change-management.md) | Sigstore cosign | Signs images and other artefacts, with attestations verified before deployment. | Security engineering |
| On-call and escalation | [S6.7](sections/s6-monitoring/s6.7-intervention-learning.md), [S7.9](sections/s7-lifecycle/s7.9-incident-response.md) | GoAlert | Open-source on-call schedules with automated escalation, run on the factory's own servers. | Reliability engineering and [incident response](glossary.md#incident-response) |
| [Monitoring as code](glossary.md#monitoring-as-code) | [S6.8](sections/s6-monitoring/s6.8-monitoring-as-code.md) | Grafana | Dashboards and alert rules provisioned from files kept under version control. | Reliability engineering |

## Lifecycle

| Component | Kept by | Reference tool | Why this one | Practice it serves |
|---|---|---|---|---|
| System of record | [S7.2](sections/s7-lifecycle/s7.2-decision-record.md) | XTDB | Every record keeps its valid time and its system time, so a decision reads as it was known when it was taken. | Temporal-database practice |
| Lineage | S7.2, [S7.7](sections/s7-lifecycle/s7.7-data-lifecycle.md) | DataHub | Collects OpenLineage events, the open standard for the lineage of jobs, runs and datasets. | Reproducible-computing practice |
| [Progressive rollout](glossary.md#progressive-rollout) and [rollback](glossary.md#rollback) | S7.5 | Argo Rollouts | Canary and blue-green releases whose automated analysis promotes or rolls back. It steps traffic between versions, not capital: capital moves by the tiers that S5.9 gates. | Continuous delivery |
| Switches that turn a module off without redeploying | S7.5 | OpenFeature with flagd | Code reads each switch through one open API; flagd serves the switches from files kept under version control and applies a change without a restart. | Continuous delivery |
| [Fitness functions](glossary.md#fitness-function) | [S7.3](sections/s7-lifecycle/s7.3-architectural-fitness.md) | Import Linter | Architectural rules on Python imports, checked as contracts in every build. | Evolutionary architecture |
| Loop of missions | [S7.10](sections/s7-lifecycle/s7.10-monitoring-feedback-loop.md) | Jira | One card template and one queue; its boards show a maximum per column, the limit that S7.10 sets. | Limits on work in progress (principle 11) |

## Reading this page

- **A reference, not a requirement.** Each tool shows that its component can be built with something
  that exists today; the page it serves says what the component must do, and any tool that does it
  can replace this one. The pages themselves impose no tool where it matters (S3.9,
  [S5.4](sections/s5-decision-execution/s5.4-allocation-budgets.md), S7.9).
- **Checked on 21 September 2026**, against each project's own documentation and release history:
  every open-source tool here had a release or a commit in 2026, each hosted service is current, and
  each does what its line says.
- **Pin the versions.** Feast, Evidently, Sloth and flagd are still before version 1; NautilusTrader
  and Polars are moving to a new major version; GX Core changed steward in 2026.
- **Licences.** Most tools are under Apache 2.0 or MIT. XTDB and OpenBao are under MPL 2.0,
  NautilusTrader under LGPL 3.0, chrony under GPL 2.0 and Grafana under AGPL 3.0. OpenBao is
  preferred to Vault, whose licence is no longer open source (BSL 1.1).
- **Hosted services.** S3 Object Lock, Jira and GitHub are hosted; where data must stay on the
  factory's own servers, a self-hosted tool with the same guarantee replaces them.
- **Set aside after checking.** Grafana OnCall, archived in March 2026; EventStoreDB, now KurrentDB,
  whose licence restricts hosting and whose streams can be deleted, unfit for a record that is never
  rewritten; Marquez, with no release since 2024.
- **The research lab keeps its own tools.** The factory re-implements each strategy on this stack
  ([S3.2](sections/s3-strategy-lab/s3.2-architecture-invariances.md)), so the lab's choice of tools
  never reaches production.
