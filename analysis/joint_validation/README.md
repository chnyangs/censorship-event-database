# Joint analysis execution

Legacy missing-label sensitivity executed; independent-reference evaluation remains pending unless explicitly supplied.

These are diagnostics of stored labels, not validated enforcement rates. N/A is excluded according to the old coding, not independently established applicability. Bounds assume the supplied positive/negative labels are correct and address missing labels only.

| Layer | Legacy applicable | Coded change | Coded negative | Unknown | Legacy N/A excluded |
| --- | ---: | ---: | ---: | ---: | ---: |
| l0_network | 24 | 5 | 0 | 19 | 374 |
| l1_consensus | 18 | 10 | 6 | 2 | 380 |
| l3_rpc | 13 | 6 | 1 | 6 | 385 |
| l4_frontend | 124 | 70 | 8 | 46 | 274 |
| asset_onchain | 49 | 26 | 1 | 22 | 349 |
| offramp_cex | 329 | 208 | 100 | 21 | 69 |

`legacy_missingness_sensitivity.json` includes missing-as-zero, observed-only and worst-case missing-label scenarios. None repairs unsupported existing labels or outcome-dependent applicability.

Independent evaluation input units: 0; status: `no_evaluation_units`. An empty CSV template does not produce model-quality scores.

`evaluation_units_template.csv` requires explicit unit/episode IDs, pilot exclusion, eligibility, additions versus removals, matching outcome definitions, and reference provenance. Keep observed effect, public disclosure and source-code changes separate. Duplicate IDs or unmatched outcome definitions are rejected. Episode bootstrap retains correlated units. Quality estimates require a supplied independent-human reference, two reviewer identifiers, completion time and an artifact locator; software cannot certify these assertions.

Run `python scripts/analyze_joint_validation.py` for current legacy diagnostics, or pass `--units PATH --out-dir NEW_DIRECTORY` for a separately prepared validation table. Never prefill reference fields with agent judgments.
