# Candidate Triggers

Watcher and historical-backfill jobs drop unreviewed trigger stubs here
before they become full events. These files feed
`make trigger-registry`; they do **not** feed paper-facing admitted
counts until promoted to `events/*.yaml` and validated.

## Workflow

1. Watcher creates `candidate_triggers/YYYY-MM-DD-<slug>.yaml`.
2. Reviewer triages:
   - accept: promote into `events/<slug>.yaml`
   - reject: move into `candidate_triggers/rejected/`
   - defer: keep here with updated notes
3. Historical backfills may mark already-promoted rows as
   `promoted_to_event` and retain `promoted_event_id` so systematic source
   sweeps are auditable without double-counting them as new admitted cases.

This directory is no longer optional for v0.2 expansion: new cases should
enter here first so selection decisions remain visible under the declared
sampling frame in `sampling/frame.yaml`. The current frame is open-ended from
2008 onward; 120 admitted-quality events is a progress milestone, not a stop
rule. See `docs/final-collection-protocol.md`.

## Minimal stub

```yaml
id: 2026-example-trigger
registry_status: candidate  # candidate | draft_needs_evidence | deferred | not_measurable | screened_no_extractor_target
research_stratum: S1_ofac_sdn
temporal_tier: comparable_main_2017_present
analysis_use: comparable_analysis
source_frame_id: ofac_recent_actions_crypto_2017_2026
trigger:
  type: ofac_sdn_designation
  actor: US_OFAC
  timestamp: 2026-01-01T00:00:00Z
  timestamp_precision: day
  citation:
    - type: primary_legal
      url: https://example.gov/example-action
target:
  kind: entity
  chains: [ethereum]
jurisdiction: [US]
expected_layers: [l4_frontend, asset_onchain, offramp_cex]
triage_notes: >
  Candidate needs archived trigger source plus per-layer evidence before
  promotion to events/.
```

Rejected stubs should retain `rejection_reason` so the registry explains
why a trigger was excluded. New v0.2 stubs should preserve source-frame
provenance (`source_frame_id`, extractor artifact, and target-level frame
unit) before promotion; legacy v0.1 event rows are marked by the registry as
`legacy_v0_1_event_yaml`.

## OFAC recent-actions backfill

Run this only after updating the cached triage input:

```sh
make ofac-recent-action-candidates
make trigger-registry
```

The backfill reads
`sources/ofac_sdn_diffs/opensanctions/ofac-recent-actions-triage.json`
and writes missing `ofac-recent-action-YYYYMMDD.yaml` stubs. It does not
overwrite existing stubs unless the script is run with `--overwrite`.

Equivalent v0.2 triage manifests are still required for S3 federal
enforcement, S4 non-US state archives, S5 corporate policy archives, and
S6 supranational actions before those strata can claim source-frame
denominator repair.
