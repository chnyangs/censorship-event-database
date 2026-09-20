# Two-arm revision: executed checks (2026-09-20)

Historical first-revision report. See [the subsequent non-human execution](nonhuman_progress/README.md) for the current work and checks.

The manuscript has been reframed around domain behavior, measurement validity,
and their joint evaluation. The compiled working draft is
[main.pdf](../../6a1d66df502cdc827ad0999d/build/phase1_reframe.pdf) (7 pages).

| Check | Actual result |
| --- | --- |
| Parallel artifact build and cached cohort preflight | Passed |
| Full test suite | 227 passed; one unrelated Matplotlib 3D environment warning |
| Event validation and JSON Schema | Passed |
| Descriptor synchronization | Passed |
| Dataset input hash versus current sources | Matches |
| Git diff whitespace checks, both repositories | Passed |
| LaTeX, repeated passes | Passed; no undefined citations/references or horizontal overflow; one 1.17pt vertical box warning |
| Ordinary paper-readiness check | FAILED: two L0 observations lack measurement denominators |
| Strict release check | FAILED: L0 evidence plus missing/DRYRUN human reviews, simulated IRR, attribution reliability and missing evidence-tier IRR |

The failed gates were not bypassed. Tests validate implementation behavior;
they do not establish that corpus claims are true. No event YAML was edited.

Implemented research preparation includes a raw-YAML semantic-risk census,
two blank 2,388-row reviewer sheets, source-overlap/applicability queues,
a bounded validation protocol and a cached-frame preflight. The latter finds
46 pages and 124 distinct address-shaped strings, with 1,415 uncached dates
unassessed; zero actions are independently adjudicated and zero outcome queries
have been run. Edited reviewer sheets, logs, reconciliation ledgers and panel
manifests are protected from overwrite.

The next work is independent review, evidence-based migration, complete frame
reconciliation, panel verification, a frozen measurement manifest, and actual
joint analysis. See the [execution plan](../docs/two-arm-execution-plan.md).
Full commands, hashes, error messages and dependency details are in
[two_arm_revision_checks.json](two_arm_revision_checks.json) and
[two_arm_revision_logs](two_arm_revision_logs/).

The PDF was built using official acmart v2.20 obtained from CTAN in a temporary
TeX search directory. PDF and auxiliary outputs are in the manuscript `build/`
directory, selected by `.latexmkrc` and ignored by git. No commit, release or external publication was made.
