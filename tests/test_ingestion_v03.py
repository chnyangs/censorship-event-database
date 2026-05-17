# SPDX-License-Identifier: MIT
"""Regression guards for the v0.3 ingestion substrate."""
from __future__ import annotations

import json
import sqlite3

import yaml

from ingestion_v03 import (
    apply_source_death_policy,
    bootstrap_legacy_events,
    connect,
    build_ingestion_report,
    export_event_yaml,
    ingestion_status_report,
    init_db,
    latest_raw_document_body,
    load_source_registry,
    machine_prescreen_review_item,
    next_review_item,
    ofac_canary_status,
    record_source_failure,
    register_source_registry,
    resolve_review_item,
    run_ofac_canary,
    run_ofac_canary_with_prior_snapshot,
    snapshot_raw_document,
    upsert_source,
    write_er_training_set_template,
    write_ingestion_report,
    write_review_packets,
    write_review_triage_summary,
    write_human_audit_worksheet,
    write_evidence_repair_plan,
    write_source_discovery_worklist,
    write_non_human_todo_list,
)


def test_ingestion_db_creates_required_tables_and_indexes(tmp_path):
    db_path = tmp_path / "ingestion.sqlite"
    init_db(db_path)

    with sqlite3.connect(db_path) as conn:
        tables = {
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table'"
            )
        }
        indexes = {
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type = 'index'"
            )
        }
        event_columns = {
            row[1]
            for row in conn.execute("PRAGMA table_info(events)")
        }
        source_columns = {
            row[1]
            for row in conn.execute("PRAGMA table_info(sources)")
        }

    assert {
        "sources",
        "raw_documents",
        "events",
        "event_evidence",
        "event_clusters",
        "entity_aliases",
        "review_queue",
        "audit_log",
        "ocr_artifacts",
    } <= tables
    assert {
        "idx_events_canonical_slug",
        "idx_event_evidence_event_id",
        "idx_audit_log_timestamp",
    } <= indexes
    assert {
        "requires_v0_3_reextraction",
        "verification_state",
        "last_pipeline_stage",
        "last_review_queue_item_id",
    } <= event_columns
    assert "first_success_at" in source_columns


def test_raw_document_snapshot_is_hash_addressed_and_deduplicated(tmp_path):
    db_path = tmp_path / "ingestion.sqlite"
    raw_dir = tmp_path / "raw"
    first = snapshot_raw_document(
        db_path=db_path,
        body=b"primary source body",
        source_url="https://example.test/source",
        source_name="Example Source",
        source_kind="test_source",
        storage_dir=raw_dir,
        content_type="text/plain",
    )
    second = snapshot_raw_document(
        db_path=db_path,
        body=b"primary source body",
        source_url="https://example.test/source",
        source_name="Example Source",
        source_kind="test_source",
        storage_dir=raw_dir,
        content_type="text/plain",
    )

    assert first.raw_document_id == second.raw_document_id
    assert first.body_path.exists()
    assert first.manifest_path.exists()
    assert json.loads(first.manifest_path.read_text())["sha256"] == first.sha256

    with sqlite3.connect(db_path) as conn:
        count = conn.execute("SELECT COUNT(*) FROM raw_documents").fetchone()[0]
    assert count == 1


def test_source_registry_registration_does_not_mark_success(tmp_path):
    db_path = tmp_path / "ingestion.sqlite"
    registry = tmp_path / "sources.yaml"
    _write(
        registry,
        """
schema_version: "0.3.0-rc1"
sources:
  - source_id: ofac_sdn_xml
    name: OFAC SDN XML
    kind: ofac_sdn_xml
    url: https://example.test/sdn.xml
    language: en
    schedule: daily
    owner: test
    pipeline: ofac_sdn_daily_canary
    phase: phase_0a_canary
        """,
    )

    rows = load_source_registry(registry)
    result = register_source_registry(db_path=db_path, registry_path=registry)

    assert rows[0]["source_id"] == "ofac_sdn_xml"
    assert result["source_count"] == 1
    with sqlite3.connect(db_path) as conn:
        row = conn.execute(
            "SELECT first_success_at, last_success_at, failure_count FROM sources"
        ).fetchone()
    assert row == (None, None, 0)


def test_ofac_canary_writes_candidates_review_queue_and_yaml_mapping(tmp_path):
    db_path = tmp_path / "ingestion.sqlite"
    raw_dir = tmp_path / "raw"
    previous_xml = b"""
    <sdnList>
      <sdnEntry><uid>100</uid><lastName>Legacy Non Crypto</lastName></sdnEntry>
    </sdnList>
    """
    current_xml = b"""
    <sdnList>
      <sdnEntry><uid>100</uid><lastName>Legacy Non Crypto</lastName></sdnEntry>
      <sdnEntry>
        <uid>200</uid>
        <lastName>Example Mixer</lastName>
        <remarks>Digital Currency Address - ETH 0x1111111111111111111111111111111111111111</remarks>
      </sdnEntry>
    </sdnList>
    """

    result = run_ofac_canary(
        db_path=db_path,
        current_xml=current_xml,
        previous_xml=previous_xml,
        storage_dir=raw_dir,
    )

    assert result.added_count == 1
    assert result.removed_count == 0
    assert result.relevant_count == 1
    assert len(result.candidate_event_ids) == 1
    assert len(result.review_queue_ids) == 1

    candidate_yaml = yaml.safe_load(export_event_yaml(db_path, result.candidate_event_ids[0]))
    assert candidate_yaml["status"] == "draft"
    assert candidate_yaml["codebook_version"] == "1.0.0"
    assert candidate_yaml["primary_source_verified"] is False
    assert "requires_v0_3_reextraction" not in candidate_yaml

    item = next_review_item(db_path)
    assert item["queue_id"] == result.review_queue_ids[0]
    assert item["status"] == "pending"

    decision = resolve_review_item(
        db_path=db_path,
        queue_id=item["queue_id"],
        decision="resolved",
        actor="human:test",
        reason="test promotion after primary-source review",
        new_event_status="verified",
    )
    assert decision["queue"]["status"] == "resolved"

    verified_yaml = yaml.safe_load(export_event_yaml(db_path, result.candidate_event_ids[0]))
    assert verified_yaml["status"] == "admitted"
    assert verified_yaml["origin"] == "human_reviewed"
    assert verified_yaml["primary_source_verified"] is True

    with sqlite3.connect(db_path) as conn:
        audit_count = conn.execute("SELECT COUNT(*) FROM audit_log").fetchone()[0]
        evidence_count = conn.execute("SELECT COUNT(*) FROM event_evidence").fetchone()[0]
    assert audit_count == 1
    assert evidence_count == 1


def test_ofac_canary_first_run_baselines_then_diffs_from_snapshot(tmp_path):
    db_path = tmp_path / "ingestion.sqlite"
    raw_dir = tmp_path / "raw"
    first_xml = b"""
    <sdnList>
      <sdnEntry>
        <uid>200</uid>
        <lastName>Example Mixer</lastName>
        <remarks>Digital Currency Address - ETH 0x1111111111111111111111111111111111111111</remarks>
      </sdnEntry>
    </sdnList>
    """
    second_xml = b"""
    <sdnList>
      <sdnEntry>
        <uid>200</uid>
        <lastName>Example Mixer</lastName>
        <remarks>Digital Currency Address - ETH 0x1111111111111111111111111111111111111111</remarks>
      </sdnEntry>
      <sdnEntry>
        <uid>201</uid>
        <lastName>Second Mixer</lastName>
        <remarks>Virtual currency exchange</remarks>
      </sdnEntry>
    </sdnList>
    """

    first = run_ofac_canary_with_prior_snapshot(
        db_path=db_path,
        current_xml=first_xml,
        storage_dir=raw_dir,
    )
    prior = latest_raw_document_body(
        db_path=db_path,
        source_name="OFAC SDN XML",
        source_url="https://www.treasury.gov/ofac/downloads/sdn.xml",
    )
    second = run_ofac_canary_with_prior_snapshot(
        db_path=db_path,
        current_xml=second_xml,
        storage_dir=raw_dir,
    )
    third = run_ofac_canary_with_prior_snapshot(
        db_path=db_path,
        current_xml=second_xml,
        storage_dir=raw_dir,
    )

    assert first.baseline_only is True
    assert first.added_count == 0
    assert first.relevant_count == 0
    assert first.candidate_event_ids == []
    assert prior is not None
    assert second.baseline_only is False
    assert second.previous_raw_document_id == prior.raw_document_id
    assert second.added_count == 1
    assert second.relevant_count == 1
    assert len(second.candidate_event_ids) == 1
    assert third.added_count == 0
    assert third.relevant_count == 0


def _write(path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body.strip() + "\n")


def test_bootstrap_legacy_events_keeps_internal_flags_out_of_yaml(tmp_path):
    db_path = tmp_path / "ingestion.sqlite"
    events_dir = tmp_path / "events"
    _write(
        events_dir / "legacy-admitted.yaml",
        """
id: legacy-admitted
schema_version: 0.2.0
codebook_version: "1.0.0"
status: admitted
primary_source_verified: false
origin: human_reviewed
analysis_use: comparable_analysis
jurisdiction: [US]
trigger:
  type: ofac_sdn_designation
  actor: US_OFAC
  timestamp: 2024-01-01T00:00:00Z
target:
  kind: entity
  actor_name: Legacy Target
        """,
    )
    _write(
        events_dir / "legacy-draft.yaml",
        """
id: legacy-draft
schema_version: 0.2.0
codebook_version: "1.0.0"
status: draft
primary_source_verified: false
origin: agent_draft
analysis_use: comparable_analysis
jurisdiction: [US]
trigger:
  type: sec_action
  actor: US_SEC
  timestamp: 2024-01-02T00:00:00Z
target:
  kind: entity
  actor_name: Draft Target
        """,
    )

    result = bootstrap_legacy_events(
        db_path=db_path,
        events_dir=events_dir,
        enqueue_reextraction=True,
    )

    assert result.event_count == 2
    assert result.queued_count == 2
    assert result.counts_by_internal_status == {"candidate": 1, "verified": 1}
    assert result.counts_by_verification_state == {
        "legacy_admitted_pending_v0_3_primary_source": 1,
        "legacy_draft_requires_reextraction": 1,
    }

    exported = yaml.safe_load(export_event_yaml(db_path, "legacy-admitted"))
    assert exported["status"] == "admitted"
    assert exported["primary_source_verified"] is False
    assert "requires_v0_3_reextraction" not in exported
    assert "verification_state" not in exported
    assert "_source_file" not in exported

    report = ingestion_status_report(db_path)
    assert report["events"]["total"] == 2
    assert report["events"]["requires_v0_3_reextraction"] == 2
    assert report["review_queue"]["by_status"] == {"pending": 2}


def test_source_death_policy_alerts_and_deprecates(tmp_path):
    db_path = tmp_path / "ingestion.sqlite"
    init_db(db_path)
    with connect(db_path) as conn:
        for idx in range(3):
            record_source_failure(
                conn,
                name="OFAC SDN XML",
                kind="ofac_sdn_xml",
                url="https://example.test/sdn.xml",
                language="en",
                schedule="daily",
                error=f"failure {idx}",
            )
        conn.commit()
    report = ingestion_status_report(db_path)
    assert report["sources"]["failure_alerts"][0]["failure_count"] == 3

    with connect(db_path) as conn:
        source_id = upsert_source(
            conn,
            name="Old Source",
            kind="test_source",
            url="https://example.test/old",
        )
        conn.execute(
            """
            UPDATE sources
            SET first_success_at = '2020-01-01T00:00:00Z',
                last_success_at = '2020-01-01T00:00:00Z'
            WHERE source_id = ?
            """,
            (source_id,),
        )
        apply_source_death_policy(conn, source_id=source_id)
        deprecated = conn.execute(
            "SELECT deprecated_at FROM sources WHERE source_id = ?",
            (source_id,),
        ).fetchone()[0]
        assert deprecated is not None


def test_ingestion_operating_report_is_internal_monitor_surface(tmp_path):
    db_path = tmp_path / "ingestion.sqlite"
    raw_dir = tmp_path / "raw"
    current_xml = b"""
    <sdnList>
      <sdnEntry>
        <uid>200</uid>
        <lastName>Example Mixer</lastName>
        <remarks>Digital Currency Address - ETH 0x1111111111111111111111111111111111111111</remarks>
      </sdnEntry>
    </sdnList>
    """
    run_ofac_canary_with_prior_snapshot(
        db_path=db_path,
        current_xml=current_xml,
        storage_dir=raw_dir,
    )

    report = build_ingestion_report(db_path)
    paths = write_ingestion_report(
        db_path=db_path,
        out_dir=tmp_path / "reports",
    )

    assert report["paper_denominator"] is False
    assert report["summary"]["event_count"] == 0
    assert report["source_freshness"]["source_count"] == 1
    assert report["source_freshness"]["sources"][0]["parser_failure_rate"] == 0.0
    assert report["ofac_canary"]["clean_run_ready"] is False
    assert paths["json"].exists()
    assert paths["md"].exists()
    assert "not a paper denominator" in paths["md"].read_text()


def test_er_training_set_template_is_unlabeled(tmp_path):
    out = write_er_training_set_template(out_path=tmp_path / "er_training_set.template.csv")
    rows = out.read_text().splitlines()

    assert rows == [
        "pair_id,event_id_a,event_id_b,candidate_relation,label,labeler,evidence_ids,reason,notes"
    ]


def test_review_packets_do_not_resolve_queue_or_flip_verification(tmp_path):
    db_path = tmp_path / "ingestion.sqlite"
    events_dir = tmp_path / "events"
    _write(
        events_dir / "legacy-admitted.yaml",
        """
id: legacy-admitted
schema_version: 0.2.0
codebook_version: "1.0.0"
status: admitted
primary_source_verified: false
origin: human_reviewed
analysis_use: comparable_analysis
jurisdiction: [US]
trigger:
  type: ofac_sdn_designation
  actor: US_OFAC
  timestamp: 2024-01-01T00:00:00Z
  citation:
    - url: https://example.test/ofac
      body_hash: sha256:abc
      body_path: sources/example/ofac.html
target:
  kind: entity
  actor_name: Legacy Target
coverage: []
observations:
  - layer: offramp_cex
    sources:
      - type: primary_legal
        url: https://example.test/ofac
        body_hash: sha256:abc
        body_path: sources/example/ofac.html
scoped_claim: Legacy claim.
        """,
    )
    bootstrap_legacy_events(
        db_path=db_path,
        events_dir=events_dir,
        enqueue_reextraction=True,
    )

    result = write_review_packets(
        db_path=db_path,
        out_dir=tmp_path / "packets",
    )

    assert result["packet_count"] == 1
    packet = tmp_path / "packets" / "0001-legacy-admitted.md"
    assert packet.exists()
    text = packet.read_text()
    assert "machine-prepared" in text
    assert '"human_review_required": true' in text
    assert "primary_source_verified=true" in text
    assert (tmp_path / "packets" / "index.json").exists()
    assert (tmp_path / "packets" / "index.csv").exists()
    assert (tmp_path / "packets" / "index.md").exists()

    report = ingestion_status_report(db_path)
    assert report["review_queue"]["by_status"] == {"pending": 1}
    assert report["events"]["primary_source_verified"] == 0


def test_review_prescreen_counts_schema_wayback_as_replayable_anchor(tmp_path):
    db_path = tmp_path / "ingestion.sqlite"
    events_dir = tmp_path / "events"
    _write(
        events_dir / "wayback-admitted.yaml",
        """
id: wayback-admitted
schema_version: 0.2.0
codebook_version: "1.0.0"
status: admitted
primary_source_verified: false
origin: human_reviewed
analysis_use: comparable_analysis
jurisdiction: [US]
trigger:
  type: ofac_sdn_designation
  actor: US_OFAC
  timestamp: 2024-01-01T00:00:00Z
  citation:
    - url: https://example.test/ofac
      wayback: https://web.archive.org/web/20240101000000/https://example.test/ofac
target:
  kind: entity
  actor_name: Wayback Target
coverage: []
observations:
  - layer: offramp_cex
    sources:
      - type: primary_legal
        url: https://example.test/ofac
        wayback: https://web.archive.org/web/20240101000000/https://example.test/ofac
        """,
    )
    bootstrap_legacy_events(
        db_path=db_path,
        events_dir=events_dir,
        enqueue_reextraction=True,
    )

    paths = write_review_triage_summary(db_path=db_path, out_dir=tmp_path / "review_queue")
    rows = (tmp_path / "review_queue" / "pending_human_confirmation.csv").read_text()

    assert "wayback-admitted" in rows
    assert "llm_prescreen_no_machine_blocker" in rows
    assert json.loads(paths["json"].read_text())["llm_prescreen_no_machine_blocker_awaiting_human"] == 1


def test_review_prescreen_counts_semi_primary_wayback_as_observation_source(tmp_path):
    db_path = tmp_path / "ingestion.sqlite"
    events_dir = tmp_path / "events"
    _write(
        events_dir / "wayback-null.yaml",
        """
id: wayback-null
schema_version: 0.2.0
codebook_version: "1.0.0"
status: admitted
primary_source_verified: false
origin: human_reviewed
analysis_use: comparable_analysis
empirical_shape: null_event
jurisdiction: [US]
trigger:
  type: ofac_sdn_designation
  actor: US_OFAC
  timestamp: 2024-01-01T00:00:00Z
  citation:
    - url: https://example.test/ofac
      body_hash: sha256:abc
      body_path: sources/example/ofac.html
target:
  kind: entity
  actor_name: Wayback Null Target
coverage: []
observations:
  - layer: l4_frontend
    observation_kind: observed_no_change
    attribution: none
    sources:
      - type: semi_primary_wayback
        url: https://web.archive.org/web/20240101000000/https://example.test/app
        body_hash: sha256:def
        body_path: sources/example/app.html
        """,
    )
    bootstrap_legacy_events(
        db_path=db_path,
        events_dir=events_dir,
        enqueue_reextraction=True,
    )

    paths = write_review_triage_summary(db_path=db_path, out_dir=tmp_path / "review_queue")
    rows = (tmp_path / "review_queue" / "pending_human_confirmation.csv").read_text()

    assert "wayback-null" in rows
    assert "no_observation_primary_source_detected" not in rows
    assert json.loads(paths["json"].read_text())["llm_prescreen_no_machine_blocker_awaiting_human"] == 1


def test_review_prescreen_exempts_tagged_null_event_no_repair_needed():
    event = yaml.safe_load(
        """
id: null-no-repair
schema_version: 0.2.0
codebook_version: "1.0.0"
status: draft
primary_source_verified: false
origin: agent_draft
analysis_use: comparable_analysis
empirical_shape: null_event
admission_tier: null_case
jurisdiction: [PH]
trigger:
  type: corporate_policy_change
  actor: EXAMPLE_ISSUER
  timestamp: "2024-01-01T00:00:00Z"
  citation:
    - url: https://news.example.test/null
      wayback: https://web.archive.org/web/20240101000000/https://news.example.test/null
target:
  kind: entity
  actor_name: Example unresolved wallet cluster
coverage: []
observations:
  - layer: asset_onchain
    observation_kind: coverage_gap
    attribution: none
    sources:
      - type: supporting_journalism
        url: https://news.example.test/null
        wayback: https://web.archive.org/web/20240101000000/https://news.example.test/null
tags:
  - null_event_no_repair_needed
        """
    )
    prescreen = machine_prescreen_review_item(
        {
            "queue_id": 1,
            "item_id": "null-no-repair",
            "queue_status": "needs_recheck",
            "priority": 1,
            "internal_status": "candidate",
            "verification_state": "legacy_draft_requires_reextraction",
            "primary_source_verified": False,
            "requires_v0_3_reextraction": True,
            "event_payload_json": json.dumps({"yaml_event": event}),
            "queue_payload_json": "{}",
        }
    )

    assert "no_observation_primary_source_detected" not in prescreen["machine_blockers"]
    assert prescreen["machine_notes"] == ["null_event_no_repair_needed"]


def test_review_triage_summary_distinguishes_llm_prescreen_from_human_audit(tmp_path):
    db_path = tmp_path / "ingestion.sqlite"
    events_dir = tmp_path / "events"
    _write(
        events_dir / "legacy-admitted.yaml",
        """
id: legacy-admitted
schema_version: 0.2.0
codebook_version: "1.0.0"
status: admitted
primary_source_verified: false
origin: human_reviewed
analysis_use: comparable_analysis
jurisdiction: [US]
trigger:
  type: ofac_sdn_designation
  actor: US_OFAC
  timestamp: 2024-01-01T00:00:00Z
target:
  kind: entity
  actor_name: Legacy Target
coverage: []
observations: []
        """,
    )
    bootstrap_legacy_events(
        db_path=db_path,
        events_dir=events_dir,
        enqueue_reextraction=True,
    )

    item = next_review_item(db_path)
    resolve_review_item(
        db_path=db_path,
        queue_id=item["queue_id"],
        decision="needs_recheck",
        actor="agent:codex",
        reason="Machine prescreen detected missing anchors before human audit.",
        metadata={"review_type": "v0.3_machine_triage"},
    )

    paths = write_review_triage_summary(db_path=db_path, out_dir=tmp_path / "review_queue")
    summary = json.loads(paths["json"].read_text())
    repair_rows = paths["repair_csv"].read_text()

    assert summary["llm_prescreen_flagged_before_human_audit"] == 1
    assert summary["human_audited_by_this_triage"] == 0
    assert summary["primary_source_verified_mutated"] is False
    assert "llm_prescreen_before_human_audit" in repair_rows
    assert "not_human_audited" in repair_rows


def test_human_audit_worksheet_and_repair_plan_are_pre_human_surfaces(tmp_path):
    db_path = tmp_path / "ingestion.sqlite"
    events_dir = tmp_path / "events"
    _write(
        events_dir / "ready-admitted.yaml",
        """
id: ready-admitted
schema_version: 0.2.0
codebook_version: "1.0.0"
status: admitted
primary_source_verified: false
origin: human_reviewed
analysis_use: comparable_analysis
jurisdiction: [US]
trigger:
  type: ofac_sdn_designation
  actor: US_OFAC
  timestamp: 2024-01-01T00:00:00Z
  citation:
    - url: https://example.test/ofac
      body_hash: sha256:abc
      body_path: sources/example/ofac.html
target:
  kind: entity
  actor_name: Ready Target
coverage: []
observations:
  - layer: offramp_cex
    sources:
      - type: primary_legal
        url: https://example.test/ofac
        body_hash: sha256:abc
        body_path: sources/example/ofac.html
        """,
    )
    _write(
        events_dir / "repair-admitted.yaml",
        """
id: repair-admitted
schema_version: 0.2.0
codebook_version: "1.0.0"
status: admitted
primary_source_verified: false
origin: human_reviewed
analysis_use: comparable_analysis
jurisdiction: [US]
trigger:
  type: sec_action
  actor: US_SEC
  timestamp: 2024-01-02T00:00:00Z
  citation:
    - url: https://example.test/sec
target:
  kind: entity
  actor_name: Repair Target
coverage: []
observations: []
        """,
    )
    bootstrap_legacy_events(
        db_path=db_path,
        events_dir=events_dir,
        enqueue_reextraction=True,
    )
    with connect(db_path) as conn:
        queue_id = conn.execute(
            "SELECT queue_id FROM review_queue WHERE item_id = 'repair-admitted'"
        ).fetchone()[0]
    resolve_review_item(
        db_path=db_path,
        queue_id=queue_id,
        decision="needs_recheck",
        actor="agent:codex",
        reason="Machine prescreen detected missing evidence before human audit.",
        metadata={"review_type": "v0.3_machine_triage"},
    )

    worksheet_paths = write_human_audit_worksheet(db_path=db_path, out_dir=tmp_path / "review_queue")
    repair_paths = write_evidence_repair_plan(db_path=db_path, out_dir=tmp_path / "review_queue")

    worksheet = worksheet_paths["csv"].read_text()
    templates = worksheet_paths["decision_templates"].read_text()
    repair_plan = repair_paths["csv"].read_text()

    assert "ready-admitted" in worksheet
    assert "repair-admitted" not in worksheet
    assert "human:<name>" in templates
    assert "repair-admitted" in repair_plan
    assert "llm_prescreen_before_human_audit" not in worksheet
    report = ingestion_status_report(db_path)
    assert report["events"]["primary_source_verified"] == 0
    assert report["review_queue"]["by_status"] == {"needs_recheck": 1, "pending": 1}


def test_source_discovery_worklist_and_non_human_todos_exclude_human_audit(tmp_path):
    db_path = tmp_path / "ingestion.sqlite"
    events_dir = tmp_path / "events"
    _write(
        events_dir / "repair-draft.yaml",
        """
id: repair-draft
schema_version: 0.2.0
codebook_version: "1.0.0"
status: draft
primary_source_verified: false
origin: agent_draft
analysis_use: comparable_analysis
jurisdiction: [US]
trigger:
  type: corporate_policy_change
  actor: EXAMPLE_PLATFORM
  timestamp: 2024-01-02T00:00:00Z
  citation:
    - url: https://example.test/policy
      body_hash: sha256:abc
      body_path: sources/example/policy.html
target:
  kind: entity
  actor_name: Repair Draft Target
coverage: []
observations:
  - layer: l4_frontend
    observation_kind: observed_change
    attribution: direct
    sources:
      - type: supporting_journalism
        url: https://news.example.test/story
        wayback: https://web.archive.org/web/20240101000000/https://news.example.test/story
        """,
    )
    bootstrap_legacy_events(
        db_path=db_path,
        events_dir=events_dir,
        enqueue_reextraction=True,
    )
    item = next_review_item(db_path)
    resolve_review_item(
        db_path=db_path,
        queue_id=item["queue_id"],
        decision="needs_recheck",
        actor="agent:codex",
        reason="Machine prescreen detected missing primary observation source before human audit.",
        metadata={"review_type": "v0.3_machine_triage"},
    )

    out_dir = tmp_path / "review_queue"
    worklist_paths = write_source_discovery_worklist(
        db_path=db_path,
        out_dir=out_dir,
        events_dir=events_dir,
    )
    todo_paths = write_non_human_todo_list(db_path=db_path, out_dir=out_dir)

    worklist = worklist_paths["csv"].read_text()
    todos = json.loads(todo_paths["json"].read_text())

    assert "repair-draft" in worklist
    assert "find_primary_observed_change_anchor" in worklist
    assert "not_human_audited" in worklist
    assert todos["human_audit_performed"] is False
    assert todos["primary_source_verified_mutated"] is False
    assert todos["remaining_source_discovery_rows"] == 1
    human_task = [task for task in todos["tasks"] if task["task_id"] == "human_primary_source_audit"][0]
    assert human_task["status"] == "excluded_from_this_request"


def test_ofac_canary_status_blocks_until_clean_run_window(tmp_path):
    db_path = tmp_path / "ingestion.sqlite"
    raw_dir = tmp_path / "raw"
    current_xml = b"""
    <sdnList>
      <sdnEntry>
        <uid>200</uid>
        <lastName>Example Mixer</lastName>
        <remarks>Digital Currency Address - ETH 0x1111111111111111111111111111111111111111</remarks>
      </sdnEntry>
    </sdnList>
    """

    run_ofac_canary(db_path=db_path, current_xml=current_xml, storage_dir=raw_dir)
    report = ofac_canary_status(db_path)

    assert report["pipeline"] == "ofac_sdn_daily_canary"
    assert report["clean_run_ready"] is False
    assert report["pending_review_count"] == 1
