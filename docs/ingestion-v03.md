# v0.3 Ingestion Workforce

This document defines the Phase 0A operational contract for the v0.3
`Corpus + Monitor` ingestion system. It is an internal collection workflow,
not a release surface and not a paper denominator.

## Scope

The canonical external event surface remains `events/*.yaml` using schema
`0.2.0`. v0.3 ingestion state lives in local SQLite under
`.local/ingestion_v03/` and may contain internal scheduling fields such as
`requires_v0_3_reextraction`, `verification_state`, and
`last_pipeline_stage`. Those fields must not appear in YAML.

YAML exposes only two v0.3 verification signals:

- `codebook_version`, currently `"1.0.0"`.
- `primary_source_verified`, initially `false` for legacy rows until real
  primary-source re-extraction and human review have been completed.

## Worker Shape

Workers are conceptually split into registry, fetch, OCR, extraction, codebook
application, entity resolution, verification, review, and export stages. In
Phase 0A these stages are implemented as functions in
`scripts/ingestion_v03.py`, not as independent services.

All workers write internal candidate rows and review-queue entries. They do
not write verified YAML directly.

## Local Commands

```sh
make ingestion-db
make ingestion-register-sources
make ingestion-bootstrap ENQUEUE=1
make ofac-canary
make ofac-canary-status
make review-next
make review-export
make review-packets
make review-triage
make human-audit-worksheet
make evidence-repair-plan
make repair-evidence-anchors
make source-discovery-worklist
make non-human-todo-list
make ingestion-report
make er-training-template
make audit-archive
```

`make ingestion-bootstrap ENQUEUE=1` imports the existing YAML corpus into the
local SQLite state and queues all rows whose `primary_source_verified` flag is
still false.

`make review-export` writes JSON, CSV, and Markdown queue snapshots under
`analysis/review_queue/`. These exports are coordination artifacts; they are
not paper tables.

`make review-packets` writes one Markdown packet per pending queue item under
`analysis/review_queue/packets/`. Packets contain machine prescreen counts,
trigger-citation summaries, required human decisions, and JSON decision
templates. Packet generation does not mutate queue status and does not set
`primary_source_verified`.

`make review-triage` writes a pre-human LLM/machine triage summary under
`analysis/review_queue/`. It separates rows where no machine blocker was
detected from rows flagged for evidence repair. A row marked
`llm_prescreen_before_human_audit` is not a human audit failure; it is a
pre-human flag that still requires evidence repair and later human
confirmation before `primary_source_verified` may become true.

`make human-audit-worksheet` writes a blank worksheet and JSONL decision
templates for rows marked `llm_prescreen_no_machine_blocker`. The templates
must not be submitted until a real human reviewer completes the worksheet.

`make evidence-repair-plan` writes a prioritized repair plan for rows marked
`llm_prescreen_before_human_audit`. These rows need source/anchor repair
before they should be put back in front of a human reviewer for final
confirmation.

`make repair-evidence-anchors` captures current HTTP bodies for existing
URL-bearing evidence rows that lack replayable anchors, patches matching YAML
entries with `body_hash` and `body_path`, and writes
`analysis/review_queue/evidence_anchor_repair_report.*`. This is still
pre-human evidence repair: it does not create new observation sources, does
not change queue status, and does not set `primary_source_verified`.

`make source-discovery-worklist` writes
`analysis/review_queue/source_discovery_worklist.*` for rows that still lack
primary observation evidence after direct anchor repair. This is not a human
audit result; it is the remaining non-human source-ingestion worklist.

`make non-human-todo-list` writes
`analysis/review_queue/non_human_todo_list.*`, summarizing which machine and
infrastructure tasks have been completed, which rows still require source
discovery or methodology repair, and which work is explicitly outside scope
because it requires real human audit.

`make ingestion-report` writes the maintainer-facing operating report under
`analysis/ingestion_reports/`. It summarizes source freshness, parser
failure rate, candidate-to-verified ratio, duplicate/merge rate, legacy draft
count, language coverage, and jurisdiction coverage.

`make er-training-template` writes a blank entity-resolution training
worksheet. It is intentionally unlabeled until a human labels difficult
pairs; do not treat the template as an ER evaluation result.

## OFAC Canary

The OFAC SDN source is registered in `sources/ingestion_sources.yaml`.
Registration does not mark a successful fetch. A successful fetch is recorded
only when the worker snapshots a raw document into the hash-addressed local
store.

The first OFAC canary run is baseline-only by default. If no prior local SDN
snapshot exists, the worker snapshots the current XML and compares it to
itself, producing zero candidate events. Later runs diff against the latest
local snapshot for the same source.

To force a historical backfill-style diff against an empty prior list, pass
`--compare-empty` directly to `scripts/ingestion_v03.py ofac-canary`. Do not
use that mode for the daily monitor.

## Source Death Policy

Sources follow the Phase 0A source-death policy:

- 3 consecutive failures appear in the status report as alerts.
- 30 days without a successful fetch marks the source deprecated.
- Deprecated and failed source rows are retained; they are not hard-deleted.
- `make audit-archive` keeps the hot SQLite audit log bounded by archiving
  rows older than 90 days to JSONL under `analysis/audit_log_archive/`.

## Promotion Contract

Allowed internal transitions are:

- `candidate -> verified`
- `verified -> candidate`
- `verified -> superseded`
- `verified -> retracted`

Only a review decision may set an internal event to `verified`. When that
happens, the YAML export maps it to:

- `status: admitted`
- `origin: human_reviewed`
- `primary_source_verified: true`

Phase 0A does not make legacy rows newly release-ready. It creates the
machinery needed to re-extract and review them against primary sources.
