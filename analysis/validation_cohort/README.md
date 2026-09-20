# Bounded validation cohort: local preflight

**Outcome study NOT EXECUTED.** This is an inventory of available local caches,
not the executed cohort, independent human gold, or a complete OFAC action frame.

Window: 2022-01-01 through 2025-12-31. The inventory contains 46 cached
pages, 261 candidate page/address pairs, and
124 distinct hexadecimal strings.
There are 1415 days without a local cached page;
their status is **unassessed**, never zero actions. Every month still requires
source-frame reconciliation, including months with cached pages.

`cached_page_inventory.csv` preserves raw hashes and paths. `candidate_addresses.csv`
extracts visible-text address-shaped strings only. Even a zero-address page remains
in the inventory; it is not adjudicated out of scope. Regex does not identify
chain, legal additions/removals, named targets or frame eligibility.
`action_target_adjudication_blank.csv` leaves those decisions and reviewer fields
blank. `panel_manifest.json` instantiates the proposed named panel; endpoint,
contract and existence-interval verification remain pending.
`query_log_template.csv` is a header-only blank log, with no outcomes or executions.

Run `python scripts/prepare_validation_cohort.py` from the repository root.
No network requests are made. Changed adjudication worksheets, query logs, frame
reconciliation ledgers, and panel identity manifests are never overwritten;
use a new `--out-dir` for a new snapshot. See
`docs/two-arm-validation-protocol.md` for frame reconciliation, measurement stages,
uniform effort and the distinction between domain and measurement research arms.

Next: reconcile every source period, independently adjudicate action/target/chain,
verify the panel identities, freeze the execution manifest, then execute queries
with complete logs and independent source-entailment review. Outcomes and any
completeness claims require that additional work.
