# Source-Frame Triage Manifests

This directory holds optional source-frame discovery manifests for the 2008+
monthly ledger. The ledger generator also reads existing `events/*.yaml` and
`candidate_triggers/**/*.yaml`; these manifests are where empty months,
screened-out rows, source outages, and completed searches are recorded.

Each CSV or JSON row should use these fields:

| field | meaning |
| --- | --- |
| `source_frame_id` | One of the declared frame ids in `sampling/frame.yaml`. |
| `discovery_month` | `YYYY-MM` month being triaged. |
| `source_url` | Official archive, query URL, docket URL, or index page. |
| `trigger_date` | Optional `YYYY-MM-DD` trigger date when a row is candidate-like. |
| `target_name` | Candidate or screened target name. |
| `target_kind` | Candidate target type, when known. |
| `screening_status` | `searched_no_candidate`, `candidate_found`, `not_applicable_pre_market`, `source_unavailable`, `pending`, or a screened/rejected trigger status that maps to `searched_no_candidate`. |
| `screening_reason` | Short reason for the status. |
| `candidate_id` | Candidate stub id, if promoted into `candidate_triggers/`. |
| `promoted_event_id` | Event id, if promoted into `events/`. |

`pending` means not yet searched. `searched_no_candidate` means searched inside
the declared source frame and no concrete crypto target was found for that
month. These are intentionally distinct.
