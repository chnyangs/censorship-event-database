# Validation progress

Generated offline from cross-checked local artifacts; no retrieval is triggered.

Input hash: `sha256:bb6176ccf39e696755a51d9f3b0021b352fea787686c3572547e5338a20748e8`. Per-file hashes and missing-input markers are in `summary.json`.

| Evidence stage | Current scope/status |
|---|---|
| Source frame | 715/715 enumerated action pages retrieved |
| Machine candidates | 35 measurement units; 70 issuer units; 18 action windows; eligibility adjudication pending |
| Endpoint contrasts | 140/140 valid snapshots; 70 paired issuer units; complete_endpoint_pairs |
| Historical interfaces | 3/3 indexed runtime hash matches; provider literals `{"match": 3}` |
| Public disclosures | 105 target/operator units; `{"gap": 70, "no_disclosure_found_under_enumerated_archive": 35}` |
| Human reference labels | pending; independently adjudicated count unavailable |

## Recomputed endpoint pairs

| Issuer | 0/0 | 0/1 | 1/0 | 1/1 |
|---|---:|---:|---:|---:|
| USDC | 0 | 35 | 0 | 0 |
| USDT | 19 | 14 | 0 | 2 |

Pairs use first/last states inside declared windows. Equal pairs do not establish no intervening event; different pairs do not establish exact timing or causation.

## Optional evidence stages

Missing artifacts are pending with null metrics, never zero observations. Existing summaries are reported at their stated scope.

- **index_stream_collection**: available; `{"accepted_unique_logs": 2829, "all_four_index_ranges_complete": true, "independent_chain_completeness_verified": false, "pages_captured": 59}`. Input: `analysis/blockscout_issuer_logs/full_streams_v2/summary.json`.
- **candidate_event_matching**: available; `{"causal_attribution_performed": false, "event_trigger_interval_counts": {"after_interval": 22, "before_interval": 0, "within_interval": 27}, "exact_trigger_latency_established": false, "indexed_stream_coverage_complete": true, "issuer_units": 70, "issuer_units_with_indexed_events": 49, "matching_event_associations": 49, "measurement_units": 35, "measurement_units_with_indexed_events": 35, "unique_matching_event_identities": 49, "within_trigger_interval_order_indeterminate": true, "zero_is_not_no_action": true}`. Input: `analysis/blockscout_issuer_logs/cohort_matches_v2/summary.json`.
- **main_metadata**: available; `{"complete_queries": 615, "failed_or_incomplete_queries": 9, "metadata_rows": 9, "query_count": 624}`. Input: `analysis/evidence_repairs/l0_ooni_daily_v1/summary.json`.
- **retry_metadata**: available; `{"completed_retries": 9, "metadata_rows": 0, "retry_query_count": 9, "still_incomplete": 0}`. Input: `analysis/evidence_repairs/l0_ooni_daily_retry_v1/summary.json`.
- **effective_query_coverage**: verified_retry_overlay; `{"effective_complete_queries": 624, "effective_incomplete_queries": 0, "frozen_main_queries": 624, "main_complete_queries": 615, "retry_is_subset_of_main_incomplete": true, "verified_retry_complete_queries": 9}`. Input: `analysis/evidence_repairs/l0_ooni_daily_v1/manifest.json, analysis/evidence_repairs/l0_ooni_daily_v1/query_summaries.json, analysis/evidence_repairs/l0_ooni_daily_retry_v1/manifest.json, analysis/evidence_repairs/l0_ooni_daily_retry_v1/query_summaries.json`.
- **raw_measurements**: verified_frozen_stage_accounting; `{"censorship_finding": null, "frozen_metadata_rows": 9, "frozen_raw_urls": 9, "full_compressed_objects_retained": null, "http_attempts": 18, "human_review_complete": false, "identity_valid_metadata_rows": 0, "invalid_locator_rows": 0, "offline_artifact_accounting_verified": true, "raw_urls_attempted": 9, "url_status_counts": {"retrieval_gap": 9}}`. Input: `sources/evidence_repairs/l0_ooni_raw_v1/summary.json`.
- **jsonl_fallback**: verified_frozen_stage_accounting; `{"censorship_finding": null, "frozen_total_compressed_content_length": 17465310, "full_compressed_objects_retained": false, "human_review_complete": false, "identity_valid_metadata_rows": 0, "objects_attempted": 6, "objects_stream_scanned": 6, "offline_artifact_accounting_verified": true, "selected_uids": 9, "uid_status_counts": {"retrieval_gap": 9}}`. Input: `sources/evidence_repairs/l0_ooni_s3_v1/summary.json`.
- **postcan_fallback**: verified_frozen_stage_accounting; `{"censorship_finding": null, "frozen_total_compressed_content_length": 17774579, "full_compressed_objects_retained": false, "human_review_complete": false, "identity_valid_metadata_rows": 9, "objects_attempted": 6, "objects_stream_scanned": 6, "offline_artifact_accounting_verified": true, "selected_uids": 9, "uid_status_counts": {"retrieved_identity_valid": 9}}`. Input: `sources/evidence_repairs/l0_ooni_postcan_v2/summary.json`.
- **cross_transport**: verified_frozen_subset_accounting; `{"attempted_queries": 159, "captured_http_attempts": 159, "causal_attribution_performed": false, "full_cohort_reconciliation": false, "human_reference_complete": false, "maximum_total_requests": 298, "providers": [{"attempted_queries": 149, "matched_queries": 149, "matched_target_state_queries": 64, "planned_queries": 149, "provider": "drpc_public", "rate_limit_stop": false, "unissued_queries": 0}, {"attempted_queries": 10, "matched_queries": 8, "matched_target_state_queries": 0, "planned_queries": 149, "provider": "one_rpc_public", "rate_limit_stop": true, "unissued_queries": 139}], "selected_action_windows": 6, "selected_endpoint_snapshots": 64, "selected_issuer_units": 32, "selected_measurement_units": 16, "upstream_operator_independence_verified": false}`. Input: `analysis/cross_transport_reconciliation/earliest_windows_v1/summary.json`.

Indexed-log collection is not independent chain completeness. Effective OONI query completion is calculated only after checking frozen retry IDs against the main incomplete set; it is not an independent measurement denominator.

OONI retrieval stages are not additive: raw-API gaps and UID-free JSONL format gaps remain historical results when postcan later recovers the same selected records. Postcan identity checks do not establish censorship. Cross-transport agreement covers only the frozen subset; shared upstreams and unissued queries remain explicit.

Sourcify match levels remain literal. Local compiler reproduction and exact source-metadata verification are not inferred. Human references and source adjudication remain separate from machine collection.

Public-disclosure negative scope: Only no exact frozen alias/address mention in currently enumerable Kraken public WordPress post HTML whose date_gmt is in declared window. Not absence of all historical disclosure or enforcement.

Reproduce with `make validation-progress` or `python scripts/build_validation_progress.py`; `--tex-out PATH` optionally writes TeX macros without editing the manuscript.
