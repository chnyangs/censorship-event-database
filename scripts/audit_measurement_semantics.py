#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Screen legacy measurement semantics; never adjudicate or relabel an event.

Reads source YAML, not dataset.json. Outputs deterministic risk queues and a
blank, label-blinded two-reviewer packet. A source reused by a trigger and an
observation is an audit flag, not proof that the observation is invalid.
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import io
import json
import pathlib
import re
from typing import Any

from _yaml_strict import load_yaml_unique_keys

ROOT = pathlib.Path(__file__).resolve().parent.parent
VERSION = "1.0.0"
LAYERS = ("l0_network", "l1_consensus", "l3_rpc", "l4_frontend", "asset_onchain", "offramp_cex")
STATES = ("measured", "partially_measured", "not_measured", "not_applicable", "missing")
SOURCE_FIELDS = ("url", "wayback", "body_hash", "body_path", "query_hash", "measurement_ids", "tx_hash", "commit")
RESPONSE_FIELDS = (
    "reviewer_id", "reviewed_at_utc", "applicability", "applicability_rationale",
    "source_entailment", "supported_claim", "supporting_source_and_locator",
    "furthest_supported_stage", "measurement_coverage", "negative_scope",
    "negative_query_or_probe_artifact", "negative_detection_limits",
    "attribution_basis", "uncertainty_notes",
)
# These lexical screens intentionally favor recall. A legitimate structural
# reason can match; the coordinator must inspect context before any recoding.
NA_PATTERNS = {
    "missing_capture_or_anchor": re.compile(
        r"\b(?:no|without|absent|not)\b.{0,90}\b(?:captured|pinned|verified|tx_hash|freeze tx|evidence)\b", re.I),
    "absence_of_observed_action": re.compile(
        r"\b(?:no|not)\b.{0,55}\b(?:observed|documented|on-chain freeze|on.chain claim)\b", re.I),
}


def _json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, default=str)


def source_refs(sources: list[dict]) -> list[dict]:
    """Only retrieval identifiers; omit author notes, grades and interpretations."""
    return [{k: s[k] for k in SOURCE_FIELDS if s.get(k)} for s in sources if isinstance(s, dict)]


def overlapping_sources(trigger_sources: list[dict], observation_sources: list[dict]) -> list[dict]:
    matches = []
    for oi, obs in enumerate(observation_sources):
        for ti, trigger in enumerate(trigger_sources):
            fields = [key for key in ("url", "body_hash")
                      if obs.get(key) and obs.get(key) == trigger.get(key)]
            if fields:
                matches.append({"observation_source_index": oi, "trigger_source_index": ti,
                                "matching_fields": fields})
    return matches


def load_events(events_dir: pathlib.Path) -> tuple[list[tuple[pathlib.Path, dict]], str]:
    events = []
    digest = hashlib.sha256()
    ids = set()
    for path in sorted(events_dir.glob("*.yaml")):
        if path.name == "TEMPLATE.yaml" or path.name.startswith("_"):
            continue
        event = load_yaml_unique_keys(path)
        if not isinstance(event, dict) or not event.get("id"):
            raise ValueError(f"Event mapping with id required: {path}")
        if event["id"] in ids:
            raise ValueError(f"Duplicate event id: {event['id']}")
        ids.add(event["id"])
        raw = path.read_bytes()
        digest.update(path.name.encode() + b"\0" + str(len(raw)).encode() + b"\0" + raw)
        events.append((path, event))
    if not events:
        raise ValueError(f"No event YAML found: {events_dir}")
    return events, "sha256:" + digest.hexdigest()


def _summary(events: list[dict], overlaps: list[dict], na_flags: list[dict]) -> dict:
    ids = {e["id"] for e in events}
    null_ids = {e["id"] for e in events
                if any(o.get("observation_kind") == "observed_no_change" for o in e.get("observations", []))
                and not any(o.get("observation_kind") == "observed_change" for o in e.get("observations", []))}
    no_change = [r for r in overlaps if r["event_id"] in ids and r["observation_kind"] == "observed_no_change"]
    changes = [r for r in overlaps if r["event_id"] in ids and r["observation_kind"] == "observed_change"]
    states = collections.Counter(c.get("status", "missing") for e in events for c in e.get("coverage", []))
    kinds = collections.Counter(o.get("observation_kind", "missing") for e in events for o in e.get("observations", []))
    return {
        "events": len(events), "expected_layer_cells": len(events) * len(LAYERS),
        "recorded_layer_cells": sum(states.values()), "layer_status_counts": dict(sorted(states.items())),
        "observation_kind_counts": dict(sorted(kinds.items())),
        "null_events": len(null_ids),
        "null_events_with_trigger_source_overlap": len(null_ids & {r["event_id"] for r in no_change}),
        "no_change_rows_with_trigger_source_overlap": len(no_change),
        "no_change_overlap_by_layer": dict(sorted(collections.Counter(r["layer"] for r in no_change).items())),
        "changed_rows_with_trigger_source_overlap": len(changes),
        "changed_events_with_trigger_source_overlap": len({r["event_id"] for r in changes}),
        "na_missing_evidence_note_flags": sum(r["event_id"] in ids for r in na_flags),
        "na_flagged_events": len({r["event_id"] for r in na_flags if r["event_id"] in ids}),
    }


def build_audit(events: list[tuple[pathlib.Path, dict]], source_hash: str) -> dict:
    overlaps, na_flags, layer_counts, blind_rows, keys = [], [], [], [], []
    for path, e in events:
        trigger = e.get("trigger", {})
        citations = trigger.get("citation", [])
        observations = e.get("observations", [])
        cov = {}
        for index, row in enumerate(e.get("coverage", [])):
            layer = row.get("layer")
            if layer in cov:
                raise ValueError(f"Duplicate coverage layer {layer}: {path}")
            cov[layer] = row
            note = " ".join(str(row.get("note", "")).split())
            matches = [name for name, regex in NA_PATTERNS.items() if regex.search(note)]
            if row.get("status") == "not_applicable" and matches:
                na_flags.append({"event_id": e["id"], "event_status": e.get("status"),
                                 "source_yaml": f"events/{path.name}", "coverage_index": index,
                                 "layer": layer, "screen_rules": _json(matches), "legacy_note": note,
                                 "trigger_sources": _json(source_refs(citations)),
                                 "verdict": "unadjudicated_risk_flag"})
        for index, obs in enumerate(observations):
            matches = overlapping_sources(citations, obs.get("sources", []))
            if matches and obs.get("observation_kind") in ("observed_no_change", "observed_change"):
                overlaps.append({"event_id": e["id"], "event_status": e.get("status"),
                                 "source_yaml": f"events/{path.name}", "observation_index": index,
                                 "layer": obs.get("layer"), "observation_kind": obs.get("observation_kind"),
                                 "legacy_claim": obs.get("event", ""), "matches": _json(matches),
                                 "trigger_sources": _json(source_refs(citations)),
                                 "observation_sources": _json(source_refs(obs.get("sources", []))),
                                 "verdict": "unadjudicated_risk_flag"})
        if e.get("status") != "admitted":
            continue
        for layer in LAYERS:
            # Opaque stable identifier is for pairing, not cryptographic blinding.
            item_id = hashlib.sha256(("measurement-audit-v1\0" + e["id"] + "\0" + layer).encode()).hexdigest()[:20]
            obs_here = [o for o in observations if o.get("layer") == layer]
            refs = source_refs([s for o in obs_here for s in o.get("sources", [])])
            target = e.get("target", {})
            blind_rows.append({"item_id": item_id, "layer": layer,
                               "trigger_timestamp": str(trigger.get("timestamp", "")),
                               "trigger_actor": trigger.get("actor", ""),
                               "target_identifiers": _json({k: target[k] for k in
                                  ("entity", "protocol", "actor_name", "addresses", "chains", "canonical_domains") if target.get(k)}),
                               "trigger_source_refs": _json(source_refs(citations)),
                               "layer_source_refs": _json(refs),
                               **{field: "" for field in RESPONSE_FIELDS}})
            keys.append({"item_id": item_id, "event_id": e["id"], "source_yaml": f"events/{path.name}",
                         "layer": layer, "legacy_coverage": cov.get(layer, {}).get("status", "missing"),
                         "legacy_coverage_note": cov.get(layer, {}).get("note", ""),
                         "legacy_observations": _json(obs_here), "human_gold_status": "not_available"})
    for scope, subset in (("all_records", [e for _, e in events]),
                          ("admitted", [e for _, e in events if e.get("status") == "admitted"])):
        for layer in LAYERS:
            counts = collections.Counter(next((c.get("status", "missing") for c in e.get("coverage", [])
                                                if c.get("layer") == layer), "missing") for e in subset)
            layer_counts.append({"scope": scope, "layer": layer, "events": len(subset),
                                 **{state: counts.get(state, 0) for state in STATES}})
    all_events = [e for _, e in events]
    admitted = [e for e in all_events if e.get("status") == "admitted"]
    summary = {"procedure_version": VERSION, "source_input_hash": source_hash,
               "input": "events/*.yaml (raw source bytes; not dataset.json)",
               "execution_status": "automated_screen_completed_human_adjudication_not_started",
               "interpretation": "Source overlap and lexical N/A flags are review priorities, not invalidity verdicts or human gold.",
               "status_counts": dict(sorted(collections.Counter(e.get("status", "missing") for e in all_events).items())),
               "all_records": _summary(all_events, overlaps, na_flags),
               "admitted": _summary(admitted, overlaps, na_flags),
               "human_packet": {"items_per_reviewer": len(blind_rows), "reviewers": 2,
                                "response_cells_prefilled": 0, "selection": "all admitted events x six layers",
                                "blinding_limit": "Legacy labels and claims omitted; existing source availability and target identities remain visible."},
               "na_screen_patterns": {name: pattern.pattern for name, pattern in NA_PATTERNS.items()}}
    return {"summary": summary, "overlaps": overlaps, "na_flags": na_flags,
            "layer_counts": layer_counts, "blind_rows": sorted(blind_rows, key=lambda r: r["item_id"]),
            "keys": sorted(keys, key=lambda r: r["item_id"])}


def csv_text(rows: list[dict], fields: list[str] | None = None) -> str:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields or list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


def render_outputs(audit: dict) -> dict[str, str]:
    summary = audit["summary"]
    admitted = summary["admitted"]
    nacells = admitted["layer_status_counts"].get("not_applicable", 0)
    cells = admitted["expected_layer_cells"]
    macros = {"AuditEvents": admitted["events"], "AuditCells": cells, "AuditNACells": nacells,
              "AuditNAPct": f"{100 * nacells / cells:.1f}" if cells else "0.0",
              "AuditNullEvents": admitted["null_events"],
              "AuditNullTriggerOverlap": admitted["null_events_with_trigger_source_overlap"],
              "AuditNoChangeRows": admitted["observation_kind_counts"].get("observed_no_change", 0),
              "AuditNoChangeTriggerOverlap": admitted["no_change_rows_with_trigger_source_overlap"],
              "AuditChangedRows": admitted["observation_kind_counts"].get("observed_change", 0),
              "AuditChangedTriggerOverlap": admitted["changed_rows_with_trigger_source_overlap"],
              "AuditNAMissingEvidenceFlags": admitted["na_missing_evidence_note_flags"],
              "AuditReviewItems": summary["human_packet"]["items_per_reviewer"]}
    numbers = ("% AUTO-GENERATED; legacy coding audit flags, NOT human-validated error counts.\n"
               f"% procedure_version: {VERSION}\n% source_input_hash: {summary['source_input_hash']}\n"
               + "".join(f"\\newcommand{{\\{name}}}{{{value}}}\n" for name, value in macros.items()))
    overlap_fields = ["event_id", "event_status", "source_yaml", "observation_index", "layer", "observation_kind",
                      "legacy_claim", "matches", "trigger_sources", "observation_sources", "verdict"]
    na_fields = ["event_id", "event_status", "source_yaml", "coverage_index", "layer", "screen_rules", "legacy_note", "trigger_sources", "verdict"]
    readme = f"""# Measurement semantics audit

Automated screen completed; human adjudication has NOT started. Procedure `{VERSION}`.
Input hash: `{summary['source_input_hash']}`. Counts come from source YAML, not `dataset.json`.

The admitted corpus has {admitted['events']} events and {cells} possible layer cells;
{nacells} cells retain the legacy N/A label. Of {admitted['null_events']} legacy null events,
{admitted['null_events_with_trigger_source_overlap']} reuse at least one trigger source URL or body hash.
There are {admitted['no_change_rows_with_trigger_source_overlap']} overlapping no-change observations
out of {admitted['observation_kind_counts'].get('observed_no_change', 0)} no-change observations.
These are **audit flags, not counts of false observations**. Source reuse can be valid.
The N/A screen flags {admitted['na_missing_evidence_note_flags']} admitted coverage notes using
lexical evidence-absence patterns; both false positives and false negatives are possible.

`summary.json` separates all registry records from admitted records. The three
queues retain event status, zero-based row indices, source YAML paths and retrieval
identifiers. No event, legacy label, admission state or human-review stamp is changed.

## Independent review packet

Distribute `human_review/reviewer_a.csv` only to reviewer A and
`human_review/reviewer_b.csv` only to reviewer B, together with the raw source files
and `docs/two-arm-validation-protocol.md`. Each contains {summary['human_packet']['items_per_reviewer']}
event-layer items; every response cell is blank. Reviewers independently derive a
supported claim from the supplied sources rather than seeing the previous answer.
Do not give reviewers this audit report, risk queues, the other reviewer sheet, or
`human_review/sealed_key.csv` before both sheets are locked. The key is coordinator-only
**plain text**, not encrypted; directory separation alone does not enforce blinding.
Labels, legacy claims, author notes and links to event YAML are omitted from reviewer
sheets. Source paths/target identities and the old collection's source availability
remain visible: this is label blinding, not fully independent evidence collection.

`source_entailment` is the reviewer's finding about what the bundle establishes,
not an answer prefilled by an agent. Response definitions and adjudication steps are
in the protocol. No empty, automated or agent-authored sheet counts as human gold.
Use a separate output directory for each new corpus snapshot. Regeneration refuses
to overwrite reviewer sheets whose bytes differ from the generated blank templates.

## Reproduce

Run `python scripts/audit_measurement_semantics.py` from the repository root.
The bounded validation cohort in the protocol is **NOT EXECUTED**; this retrospective
screen does not establish sampling-frame completeness or measurement validity.
"""
    return {"summary.json": json.dumps(summary, indent=2, sort_keys=True) + "\n",
            "null_source_overlap_queue.csv": csv_text([r for r in audit["overlaps"] if r["observation_kind"] == "observed_no_change"], overlap_fields),
            "action_source_overlap_queue.csv": csv_text([r for r in audit["overlaps"] if r["observation_kind"] == "observed_change"], overlap_fields),
            "na_missing_evidence_queue.csv": csv_text(audit["na_flags"], na_fields),
            "layer_status_counts.csv": csv_text(audit["layer_counts"]),
            "human_review/reviewer_a.csv": csv_text(audit["blind_rows"]),
            "human_review/reviewer_b.csv": csv_text(audit["blind_rows"]),
            "human_review/sealed_key.csv": csv_text(audit["keys"]),
            "paper_numbers.tex": numbers, "README.md": readme}


def write_outputs(outputs: dict[str, str], out_dir: pathlib.Path) -> None:
    # Check all reviewer sheets before writing anything, preserving completed work.
    for name, content in outputs.items():
        path = out_dir / name
        if name.startswith("human_review/reviewer_") and path.exists() and path.read_text() != content:
            raise ValueError(f"Refusing to overwrite changed reviewer sheet {path}; use a new --out-dir")
    for name, content in outputs.items():
        path = out_dir / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--events-dir", type=pathlib.Path, default=ROOT / "events")
    parser.add_argument("--out-dir", type=pathlib.Path, default=ROOT / "analysis" / "measurement_audit")
    args = parser.parse_args()
    events, source_hash = load_events(args.events_dir)
    audit = build_audit(events, source_hash)
    write_outputs(render_outputs(audit), args.out_dir)
    print(json.dumps({"out_dir": str(args.out_dir), "admitted": audit["summary"]["admitted"]}, indent=2))


if __name__ == "__main__":
    main()
