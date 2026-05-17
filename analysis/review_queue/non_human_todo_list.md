# v0.3 Non-Human Todo List

Scope: complete machine/infrastructure work and leave real human audit untouched.

- Queue rows: 262
- Ready for future human audit: 260
- Still requiring source discovery or methodology repair: 2
- Human audit performed here: `false`
- `primary_source_verified` mutated here: `false`

| Task | Status | Artifact | Note |
| --- | --- | --- | --- |
| `sqlite_bootstrap` | `complete` | `.local/ingestion_v03/ingestion.sqlite` | Legacy YAML rows are represented in the internal v0.3 state without mutating YAML verification flags. |
| `review_packets` | `complete` | `analysis/review_queue/packets/index.csv` | Machine-prepared review packets only; not human audit. |
| `machine_triage_summary` | `complete` | `analysis/review_queue/v0_3_review_triage_summary.json` | Separates machine-ready, machine-repaired, and still-blocked rows. |
| `human_audit_worksheet_preparation` | `complete` | `analysis/review_queue/human_audit_worksheet.csv` | Prepared 260 blank rows for future human audit; no audit result recorded. |
| `evidence_repair_plan` | `complete` | `analysis/review_queue/evidence_repair_plan.csv` | Current machine blocker rows: 2. |
| `existing_url_anchor_capture` | `complete` | `analysis/review_queue/evidence_anchor_repair_report.csv` | Direct body_hash/body_path capture attempted for existing URL-bearing missing anchors. |
| `source_discovery_worklist` | `complete` | `analysis/review_queue/source_discovery_worklist.csv` | 2 rows still need source discovery or methodology repair before they can enter the human worksheet. |
| `human_primary_source_audit` | `excluded_from_this_request` | `analysis/review_queue/human_audit_worksheet.csv` | Requires real human confirmation; not performed by this workflow. |

## Boundary

Rows in the human worksheet are ready only for future human confirmation. Rows in the source-discovery worklist still need primary observation evidence or a documented methodology decision before they should be offered to a human auditor as confirmable cases.
