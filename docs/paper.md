# Paper: shared database, domain research, and measurement validity

Working title: **Measuring Cross-Layer Crypto Censorship: Enforcement Evidence
and Observation Limits**.

The paper is organized around a shared database, Arm 1 (restriction/execution/
recovery behavior), Arm 2 (observation methods and error), and their connection:
which domain conclusions survive independent validation and correction.

- RQ1: Which actors and layers carry documented restrictions, and how do
  restriction/recovery unfold within a defined event/operator scope?
- RQ2: Which actions and scoped negatives can each evidence channel establish,
  with what coverage and coding error?
- RQ3: How do applicability, source-support, and coverage corrections change RQ1?

Implemented: legacy event registry, deterministic semantic screening,
review queues, blank reviewer packets, revised artifact/metric tooling, automated
OFAC frame traversal, source-verified panel sidecars, excluded historical-data
feasibility pilots, a source-defined endpoint-snapshot collector, and
joint-analysis software with reference-readiness gates. The full machine
candidate endpoint campaign, indexed-event traversal and matching, public
disclosure collection, OONI metadata and raw-record recovery, and a frozen
cross-transport subset have also executed with explicit gaps. The offline
[validation progress report](../analysis/validation_progress/README.md), schema
`1.1.0`, validates the separate retrieval stages: nine selected OONI records
were recovered and identity-checked through the POST archive; dRPC matched
149/149 subset queries, and 1RPC matched 8 of 10 attempts before stopping.
These are collection and transport results, not independently adjudicated
enforcement findings.
Pending: human eligibility and source-support adjudication, independent
reference labels, validated correction effects, and strict archival release.

Current aggregate tables describe existing coding; they are not enforcement
prevalence, confirmed negatives, or a test of administrative control.

See [execution plan](two-arm-execution-plan.md),
[validation protocol](two-arm-validation-protocol.md),
[claim policy](paper_claims.md), and [artifact reproduction](paper-artifacts.md).
The source manuscript is maintained in the sibling paper repository; use
PAPER_DIR to connect it explicitly to the artifact.
