#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""v0.3 ingestion substrate.

This module keeps the v0.3 ingestion workflow conceptually split into stages
without deploying nine separate workers.  The canonical release surface remains
`events/*.yaml`; this SQLite database is an internal working state for source
ingestion, review, entity resolution, and audit logging.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sqlite3
import sys
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from xml.etree import ElementTree as ET

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_STATE_DIR = REPO_ROOT / ".local" / "ingestion_v03"
DEFAULT_DB_PATH = DEFAULT_STATE_DIR / "ingestion.sqlite"
DEFAULT_RAW_DIR = DEFAULT_STATE_DIR / "raw_documents"
DEFAULT_SOURCE_REGISTRY = REPO_ROOT / "sources" / "ingestion_sources.yaml"
OFAC_SDN_URL = "https://www.treasury.gov/ofac/downloads/sdn.xml"
OFAC_SOURCE_NAME = "OFAC SDN XML"
OFAC_SOURCE_KIND = "ofac_sdn_xml"
USER_AGENT = "censorship-event-database-v03-ingestion/0.1"
CODEBOOK_VERSION = "1.0.0"

CRYPTO_KEYWORDS = (
    "virtual currency",
    "digital currency",
    "cryptocurrency",
    "digital asset",
    "blockchain",
    "bitcoin",
    "ethereum",
    "tether",
    "usdt",
    "usdc",
    "mixer",
    "wallet",
    "exchange",
)
ETH_ADDR_RE = re.compile(r"0x[0-9a-fA-F]{40}")
PRIMARY_OBSERVATION_SOURCE_TYPES = {
    "semi_primary_measurement",
    # Wayback captures of the observed surface are first-party observations of
    # page/domain state even though the archive service is the capture medium.
    "semi_primary_wayback",
}


@dataclass(frozen=True)
class RawDocumentSnapshot:
    raw_document_id: int
    sha256: str
    body_path: Path
    manifest_path: Path
    byte_length: int


@dataclass(frozen=True)
class OfacCanaryResult:
    raw_document_id: int | None
    added_count: int
    removed_count: int
    relevant_count: int
    candidate_event_ids: list[str]
    review_queue_ids: list[int]
    baseline_only: bool = False
    previous_raw_document_id: int | None = None


@dataclass(frozen=True)
class BootstrapResult:
    event_count: int
    queued_count: int
    counts_by_internal_status: dict[str, int]
    counts_by_verification_state: dict[str, int]


@dataclass(frozen=True)
class PriorRawDocument:
    raw_document_id: int
    body_path: Path
    body: bytes


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def connect(db_path: Path = DEFAULT_DB_PATH) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(db_path: Path = DEFAULT_DB_PATH) -> None:
    with connect(db_path) as conn:
        conn.executescript(
            """
            PRAGMA user_version = 3;

            CREATE TABLE IF NOT EXISTS sources (
                source_id INTEGER PRIMARY KEY,
                source_key TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL,
                kind TEXT NOT NULL,
                url TEXT,
                language TEXT,
                schedule TEXT,
                owner TEXT,
                failure_count INTEGER NOT NULL DEFAULT 0,
                first_success_at TEXT,
                last_success_at TEXT,
                last_failure_at TEXT,
                deprecated_at TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                metadata_json TEXT NOT NULL DEFAULT '{}'
            );

            CREATE TABLE IF NOT EXISTS raw_documents (
                raw_document_id INTEGER PRIMARY KEY,
                sha256 TEXT NOT NULL UNIQUE,
                source_id INTEGER REFERENCES sources(source_id),
                source_url TEXT,
                fetched_at TEXT NOT NULL,
                content_type TEXT,
                byte_length INTEGER NOT NULL,
                body_path TEXT NOT NULL,
                manifest_path TEXT NOT NULL,
                metadata_json TEXT NOT NULL DEFAULT '{}'
            );

            CREATE TABLE IF NOT EXISTS event_clusters (
                cluster_id TEXT PRIMARY KEY,
                canonical_event_id TEXT,
                merge_decision_reason TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS events (
                event_id TEXT PRIMARY KEY,
                canonical_slug TEXT NOT NULL,
                internal_status TEXT NOT NULL CHECK (
                    internal_status IN ('candidate', 'verified', 'superseded', 'retracted')
                ),
                pipeline TEXT NOT NULL,
                trigger_type TEXT,
                actor TEXT,
                subject TEXT,
                event_date TEXT,
                jurisdiction_scope TEXT,
                analysis_use TEXT,
                codebook_version TEXT,
                primary_source_verified INTEGER NOT NULL DEFAULT 0,
                same_event_cluster_id TEXT REFERENCES event_clusters(cluster_id),
                requires_v0_3_reextraction INTEGER NOT NULL DEFAULT 0,
                verification_state TEXT NOT NULL DEFAULT 'unverified',
                last_pipeline_stage TEXT,
                last_review_queue_item_id INTEGER,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                payload_json TEXT NOT NULL DEFAULT '{}'
            );

            CREATE TABLE IF NOT EXISTS event_evidence (
                evidence_id TEXT PRIMARY KEY,
                event_id TEXT NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
                raw_document_id INTEGER REFERENCES raw_documents(raw_document_id),
                evidence_role TEXT NOT NULL,
                source_language TEXT,
                original_excerpt TEXT,
                english_summary TEXT,
                translation_model TEXT,
                confidence REAL,
                created_at TEXT NOT NULL,
                metadata_json TEXT NOT NULL DEFAULT '{}'
            );

            CREATE TABLE IF NOT EXISTS entity_aliases (
                alias_id INTEGER PRIMARY KEY,
                canonical_entity TEXT NOT NULL,
                alias TEXT NOT NULL,
                language TEXT,
                source_id INTEGER REFERENCES sources(source_id),
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS review_queue (
                queue_id INTEGER PRIMARY KEY,
                item_type TEXT NOT NULL,
                item_id TEXT NOT NULL,
                status TEXT NOT NULL CHECK (
                    status IN ('pending', 'resolved', 'needs_recheck', 'deferred')
                ),
                priority INTEGER NOT NULL DEFAULT 50,
                reason TEXT,
                payload_json TEXT NOT NULL DEFAULT '{}',
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                resolved_at TEXT
            );

            CREATE TABLE IF NOT EXISTS audit_log (
                audit_id INTEGER PRIMARY KEY,
                timestamp TEXT NOT NULL,
                actor TEXT NOT NULL,
                action TEXT NOT NULL,
                object_type TEXT NOT NULL,
                object_id TEXT NOT NULL,
                previous_state_json TEXT,
                new_state_json TEXT,
                reason TEXT,
                metadata_json TEXT NOT NULL DEFAULT '{}'
            );

            CREATE TABLE IF NOT EXISTS ocr_artifacts (
                ocr_id INTEGER PRIMARY KEY,
                raw_document_id INTEGER NOT NULL REFERENCES raw_documents(raw_document_id),
                source_page_hash TEXT,
                recognized_text TEXT NOT NULL,
                engine TEXT NOT NULL,
                engine_version TEXT,
                confidence REAL,
                rerun_of_ocr_id INTEGER REFERENCES ocr_artifacts(ocr_id),
                created_at TEXT NOT NULL,
                metadata_json TEXT NOT NULL DEFAULT '{}'
            );

            CREATE UNIQUE INDEX IF NOT EXISTS idx_events_canonical_slug
                ON events(canonical_slug);
            CREATE INDEX IF NOT EXISTS idx_event_evidence_event_id
                ON event_evidence(event_id);
            CREATE INDEX IF NOT EXISTS idx_audit_log_timestamp
                ON audit_log(timestamp);
            """
        )
        ensure_column(conn, "sources", "first_success_at", "TEXT")
        ensure_column(conn, "events", "requires_v0_3_reextraction", "INTEGER NOT NULL DEFAULT 0")
        ensure_column(conn, "events", "verification_state", "TEXT NOT NULL DEFAULT 'unverified'")
        ensure_column(conn, "events", "last_pipeline_stage", "TEXT")
        ensure_column(conn, "events", "last_review_queue_item_id", "INTEGER")


def ensure_column(conn: sqlite3.Connection, table: str, column: str, ddl: str) -> None:
    columns = {row["name"] for row in conn.execute(f"PRAGMA table_info({table})")}
    if column not in columns:
        conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {ddl}")


def json_dumps(value: Any) -> str:
    return json.dumps(value or {}, sort_keys=True, separators=(",", ":"), default=str)


def _source_key(url: str | None, name: str) -> str:
    raw = url or name
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "source"
    return f"{slug}-{digest}"


def upsert_source(
    conn: sqlite3.Connection,
    *,
    name: str,
    kind: str,
    url: str | None = None,
    language: str | None = None,
    schedule: str | None = None,
    owner: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> int:
    now = utc_now()
    key = _source_key(url, name)
    conn.execute(
        """
        INSERT INTO sources (
            source_key, name, kind, url, language, schedule, owner,
            first_success_at, last_success_at, created_at, updated_at, metadata_json
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(source_key) DO UPDATE SET
            name=excluded.name,
            kind=excluded.kind,
            url=excluded.url,
            language=excluded.language,
            schedule=excluded.schedule,
            owner=excluded.owner,
            first_success_at=COALESCE(sources.first_success_at, excluded.first_success_at),
            last_success_at=excluded.last_success_at,
            failure_count=0,
            updated_at=excluded.updated_at,
            metadata_json=excluded.metadata_json
        """,
        (
            key,
            name,
            kind,
            url,
            language,
            schedule,
            owner,
            now,
            now,
            now,
            now,
            json_dumps(metadata),
        ),
    )
    row = conn.execute("SELECT source_id FROM sources WHERE source_key = ?", (key,)).fetchone()
    if row is None:  # pragma: no cover - defensive
        raise RuntimeError(f"failed to upsert source {key}")
    return int(row["source_id"])


def register_source(
    conn: sqlite3.Connection,
    *,
    name: str,
    kind: str,
    url: str | None = None,
    language: str | None = None,
    schedule: str | None = None,
    owner: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> int:
    """Register a source without marking a successful fetch."""
    now = utc_now()
    key = _source_key(url, name)
    conn.execute(
        """
        INSERT INTO sources (
            source_key, name, kind, url, language, schedule, owner,
            created_at, updated_at, metadata_json
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(source_key) DO UPDATE SET
            name=excluded.name,
            kind=excluded.kind,
            url=excluded.url,
            language=excluded.language,
            schedule=excluded.schedule,
            owner=excluded.owner,
            updated_at=excluded.updated_at,
            metadata_json=excluded.metadata_json
        """,
        (
            key,
            name,
            kind,
            url,
            language,
            schedule,
            owner,
            now,
            now,
            json_dumps(metadata),
        ),
    )
    row = conn.execute("SELECT source_id FROM sources WHERE source_key = ?", (key,)).fetchone()
    if row is None:  # pragma: no cover - defensive
        raise RuntimeError(f"failed to register source {key}")
    return int(row["source_id"])


def load_source_registry(registry_path: Path = DEFAULT_SOURCE_REGISTRY) -> list[dict[str, Any]]:
    if not registry_path.exists():
        return []
    data = yaml.safe_load(registry_path.read_text()) or {}
    rows = data.get("sources") or []
    if not isinstance(rows, list):
        raise ValueError(f"{registry_path} must contain a sources list")
    normalized: list[dict[str, Any]] = []
    for idx, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            raise ValueError(f"{registry_path}: sources[{idx}] must be a mapping")
        for required in ("source_id", "name", "kind", "url"):
            if not row.get(required):
                raise ValueError(f"{registry_path}: sources[{idx}] missing {required}")
        normalized.append(row)
    return normalized


def register_source_registry(
    *,
    db_path: Path = DEFAULT_DB_PATH,
    registry_path: Path = DEFAULT_SOURCE_REGISTRY,
) -> dict[str, Any]:
    init_db(db_path)
    rows = load_source_registry(registry_path)
    source_ids: list[int] = []
    with connect(db_path) as conn:
        for row in rows:
            metadata = dict(row.get("metadata") or {})
            metadata.update(
                {
                    "registry_source_id": row.get("source_id"),
                    "pipeline": row.get("pipeline"),
                    "phase": row.get("phase"),
                    "source_death_policy": row.get("source_death_policy"),
                }
            )
            source_ids.append(
                register_source(
                    conn,
                    name=str(row["name"]),
                    kind=str(row["kind"]),
                    url=str(row["url"]),
                    language=row.get("language"),
                    schedule=row.get("schedule"),
                    owner=row.get("owner"),
                    metadata=metadata,
                )
            )
    return {
        "registry_path": str(registry_path),
        "source_count": len(rows),
        "source_ids": source_ids,
    }


def snapshot_raw_document(
    *,
    db_path: Path = DEFAULT_DB_PATH,
    body: bytes,
    source_url: str | None,
    source_name: str,
    source_kind: str,
    storage_dir: Path = DEFAULT_RAW_DIR,
    content_type: str | None = None,
    language: str | None = None,
    schedule: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> RawDocumentSnapshot:
    init_db(db_path)
    digest = hashlib.sha256(body).hexdigest()
    shard_dir = storage_dir / "sha256" / digest[:2]
    shard_dir.mkdir(parents=True, exist_ok=True)
    body_path = shard_dir / f"{digest}.bin"
    manifest_path = shard_dir / f"{digest}.json"
    if not body_path.exists():
        body_path.write_bytes(body)

    with connect(db_path) as conn:
        source_id = upsert_source(
            conn,
            name=source_name,
            kind=source_kind,
            url=source_url,
            language=language,
            schedule=schedule,
            metadata=metadata,
        )
        fetched_at = utc_now()
        manifest = {
            "sha256": f"sha256:{digest}",
            "source_id": source_id,
            "source_url": source_url,
            "fetched_at": fetched_at,
            "content_type": content_type,
            "byte_length": len(body),
            "body_path": str(body_path),
            "metadata": metadata or {},
        }
        manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
        conn.execute(
            """
            INSERT INTO raw_documents (
                sha256, source_id, source_url, fetched_at, content_type,
                byte_length, body_path, manifest_path, metadata_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(sha256) DO UPDATE SET
                source_id=excluded.source_id,
                source_url=excluded.source_url,
                fetched_at=excluded.fetched_at,
                content_type=excluded.content_type,
                byte_length=excluded.byte_length,
                body_path=excluded.body_path,
                manifest_path=excluded.manifest_path,
                metadata_json=excluded.metadata_json
            """,
            (
                digest,
                source_id,
                source_url,
                fetched_at,
                content_type,
                len(body),
                str(body_path),
                str(manifest_path),
                json_dumps(metadata),
            ),
        )
        row = conn.execute(
            "SELECT raw_document_id FROM raw_documents WHERE sha256 = ?",
            (digest,),
        ).fetchone()
        raw_document_id = int(row["raw_document_id"])
    return RawDocumentSnapshot(
        raw_document_id=raw_document_id,
        sha256=f"sha256:{digest}",
        body_path=body_path,
        manifest_path=manifest_path,
        byte_length=len(body),
    )


def latest_raw_document_body(
    *,
    db_path: Path = DEFAULT_DB_PATH,
    source_name: str,
    source_url: str | None,
) -> PriorRawDocument | None:
    init_db(db_path)
    source_key = _source_key(source_url, source_name)
    with connect(db_path) as conn:
        row = conn.execute(
            """
            SELECT rd.raw_document_id, rd.body_path
            FROM raw_documents rd
            JOIN sources s ON s.source_id = rd.source_id
            WHERE s.source_key = ?
            ORDER BY rd.fetched_at DESC, rd.raw_document_id DESC
            LIMIT 1
            """,
            (source_key,),
        ).fetchone()
    if row is None:
        return None
    body_path = Path(row["body_path"])
    if not body_path.exists():
        return None
    return PriorRawDocument(
        raw_document_id=int(row["raw_document_id"]),
        body_path=body_path,
        body=body_path.read_bytes(),
    )


def fetch_url(url: str, timeout: float = 60.0) -> tuple[bytes, str | None]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read(), resp.headers.get("Content-Type")


def parse_ofac_entries(xml_bytes: bytes) -> dict[str, str]:
    entries: dict[str, str] = {}
    root = ET.fromstring(xml_bytes)
    for elem in root.iter():
        if not elem.tag.endswith("sdnEntry"):
            continue
        uid = ""
        texts: list[str] = []
        for child in elem.iter():
            if child.tag.endswith("uid") and child.text:
                uid = child.text.strip()
            if child.text and child.text.strip():
                texts.append(child.text.strip())
        if uid:
            entries[uid] = " | ".join(texts)
    return entries


def matches_crypto_signature(signature: str) -> bool:
    lower = signature.lower()
    return any(keyword in lower for keyword in CRYPTO_KEYWORDS) or bool(ETH_ADDR_RE.search(signature))


def slugify(value: str, fallback: str = "event") -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or fallback


def _event_payload_for_ofac_diff(
    *,
    uid: str,
    signature: str,
    direction: str,
    raw_document_id: int | None,
    observed_at: str,
) -> dict[str, Any]:
    trigger_type = "ofac_sdn_removal" if direction == "removed" else "ofac_sdn_designation"
    return {
        "source": "ofac_sdn_daily_canary",
        "sdn_uid": uid,
        "direction": direction,
        "signature": signature[:1000],
        "raw_document_id": raw_document_id,
        "observed_at": observed_at,
        "trigger": {
            "type": trigger_type,
            "actor": "US_OFAC",
            "source_url": OFAC_SDN_URL,
        },
    }


def upsert_candidate_event(
    conn: sqlite3.Connection,
    *,
    canonical_slug: str,
    pipeline: str,
    payload: dict[str, Any],
    trigger_type: str | None = None,
    actor: str | None = None,
    subject: str | None = None,
    event_date: str | None = None,
    jurisdiction_scope: str | None = "US",
    analysis_use: str | None = "comparable_analysis",
    raw_document_id: int | None = None,
) -> str:
    now = utc_now()
    event_id = canonical_slug
    conn.execute(
        """
        INSERT INTO events (
            event_id, canonical_slug, internal_status, pipeline, trigger_type,
            actor, subject, event_date, jurisdiction_scope, analysis_use,
            codebook_version, primary_source_verified, created_at, updated_at,
            payload_json
        )
        VALUES (?, ?, 'candidate', ?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?, ?)
        ON CONFLICT(event_id) DO UPDATE SET
            canonical_slug=excluded.canonical_slug,
            pipeline=excluded.pipeline,
            trigger_type=excluded.trigger_type,
            actor=excluded.actor,
            subject=excluded.subject,
            event_date=excluded.event_date,
            jurisdiction_scope=excluded.jurisdiction_scope,
            analysis_use=excluded.analysis_use,
            codebook_version=excluded.codebook_version,
            updated_at=excluded.updated_at,
            payload_json=excluded.payload_json
        """,
        (
            event_id,
            canonical_slug,
            pipeline,
            trigger_type,
            actor,
            subject,
            event_date,
            jurisdiction_scope,
            analysis_use,
            CODEBOOK_VERSION,
            now,
            now,
            json_dumps(payload),
        ),
    )
    if raw_document_id is not None:
        evidence_id = f"{event_id}:trigger:{raw_document_id}"
        conn.execute(
            """
            INSERT OR IGNORE INTO event_evidence (
                evidence_id, event_id, raw_document_id, evidence_role,
                source_language, created_at, metadata_json
            )
            VALUES (?, ?, ?, 'trigger_primary_source', 'en', ?, ?)
            """,
            (evidence_id, event_id, raw_document_id, now, json_dumps({"pipeline": pipeline})),
        )
    return event_id


def enqueue_review(
    conn: sqlite3.Connection,
    *,
    item_type: str,
    item_id: str,
    reason: str,
    payload: dict[str, Any] | None = None,
    priority: int = 50,
) -> int:
    existing = conn.execute(
        """
        SELECT queue_id FROM review_queue
        WHERE item_type = ? AND item_id = ? AND status = 'pending'
        ORDER BY queue_id LIMIT 1
        """,
        (item_type, item_id),
    ).fetchone()
    if existing is not None:
        return int(existing["queue_id"])
    now = utc_now()
    cur = conn.execute(
        """
        INSERT INTO review_queue (
            item_type, item_id, status, priority, reason, payload_json,
            created_at, updated_at
        )
        VALUES (?, ?, 'pending', ?, ?, ?, ?, ?)
        """,
        (item_type, item_id, priority, reason, json_dumps(payload), now, now),
    )
    return int(cur.lastrowid)


def run_ofac_canary(
    *,
    db_path: Path = DEFAULT_DB_PATH,
    current_xml: bytes,
    previous_xml: bytes | None = None,
    storage_dir: Path = DEFAULT_RAW_DIR,
    source_url: str = OFAC_SDN_URL,
    dry_run: bool = False,
    baseline_only: bool = False,
    previous_raw_document_id: int | None = None,
) -> OfacCanaryResult:
    observed_at = utc_now()
    raw_document_id: int | None = None
    if not dry_run:
        snapshot = snapshot_raw_document(
            db_path=db_path,
            body=current_xml,
            source_url=source_url,
            source_name=OFAC_SOURCE_NAME,
            source_kind=OFAC_SOURCE_KIND,
            storage_dir=storage_dir,
            content_type="application/xml",
            language="en",
            schedule="daily",
            metadata={"pipeline": "ofac_sdn_daily_canary"},
        )
        raw_document_id = snapshot.raw_document_id
        init_db(db_path)

    current_entries = parse_ofac_entries(current_xml)
    previous_entries = parse_ofac_entries(previous_xml) if previous_xml else {}
    added = [(uid, sig) for uid, sig in current_entries.items() if uid not in previous_entries]
    removed = [(uid, sig) for uid, sig in previous_entries.items() if uid not in current_entries]
    relevant = [
        ("added", uid, sig) for uid, sig in added if matches_crypto_signature(sig)
    ] + [
        ("removed", uid, sig) for uid, sig in removed if matches_crypto_signature(sig)
    ]

    candidate_event_ids: list[str] = []
    review_queue_ids: list[int] = []
    if dry_run:
        return OfacCanaryResult(
            None,
            len(added),
            len(removed),
            len(relevant),
            [],
            [],
            baseline_only=baseline_only,
            previous_raw_document_id=previous_raw_document_id,
        )

    with connect(db_path) as conn:
        for direction, uid, signature in relevant:
            trigger_type = "ofac_sdn_removal" if direction == "removed" else "ofac_sdn_designation"
            canonical_slug = slugify(f"ofac-sdn-{direction}-{uid}-{observed_at[:10]}")
            payload = _event_payload_for_ofac_diff(
                uid=uid,
                signature=signature,
                direction=direction,
                raw_document_id=raw_document_id,
                observed_at=observed_at,
            )
            event_id = upsert_candidate_event(
                conn,
                canonical_slug=canonical_slug,
                pipeline="ofac_sdn_daily_canary",
                payload=payload,
                trigger_type=trigger_type,
                actor="US_OFAC",
                subject=signature[:200],
                event_date=observed_at[:10],
                raw_document_id=raw_document_id,
            )
            candidate_event_ids.append(event_id)
            queue_id = enqueue_review(
                conn,
                item_type="event",
                item_id=event_id,
                reason="OFAC SDN canary detected a crypto-relevant list diff; human review required.",
                payload={"pipeline": "ofac_sdn_daily_canary", "direction": direction, "sdn_uid": uid},
                priority=20,
            )
            review_queue_ids.append(queue_id)

    return OfacCanaryResult(
        raw_document_id,
        len(added),
        len(removed),
        len(relevant),
        candidate_event_ids,
        review_queue_ids,
        baseline_only=baseline_only,
        previous_raw_document_id=previous_raw_document_id,
    )


def run_ofac_canary_with_prior_snapshot(
    *,
    db_path: Path = DEFAULT_DB_PATH,
    current_xml: bytes,
    previous_xml: bytes | None = None,
    storage_dir: Path = DEFAULT_RAW_DIR,
    source_url: str = OFAC_SDN_URL,
    dry_run: bool = False,
    compare_empty: bool = False,
) -> OfacCanaryResult:
    previous_raw_document_id: int | None = None
    baseline_only = False
    if previous_xml is None and not compare_empty:
        prior = latest_raw_document_body(
            db_path=db_path,
            source_name=OFAC_SOURCE_NAME,
            source_url=source_url,
        )
        if prior is None:
            previous_xml = current_xml
            baseline_only = True
        else:
            previous_xml = prior.body
            previous_raw_document_id = prior.raw_document_id
    return run_ofac_canary(
        db_path=db_path,
        current_xml=current_xml,
        previous_xml=previous_xml,
        storage_dir=storage_dir,
        source_url=source_url,
        dry_run=dry_run,
        baseline_only=baseline_only,
        previous_raw_document_id=previous_raw_document_id,
    )


def load_yaml_events(events_dir: Path = REPO_ROOT / "events") -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for path in sorted(events_dir.glob("*.yaml")):
        if path.name.startswith("_") or path.name == "TEMPLATE.yaml":
            continue
        event = yaml.safe_load(path.read_text())
        if isinstance(event, dict):
            event["_source_file"] = path.as_posix()
            events.append(event)
    return events


def internal_status_from_yaml(status: str | None) -> str:
    if status == "admitted":
        return "verified"
    if status == "rejected":
        return "retracted"
    return "candidate"


def verification_state_from_yaml(event: dict[str, Any]) -> str:
    if event.get("primary_source_verified") is True:
        return "primary_source_verified"
    if event.get("status") == "admitted":
        return "legacy_admitted_pending_v0_3_primary_source"
    if event.get("status") == "rejected":
        return "legacy_rejected_reference"
    if event.get("origin") == "agent_draft":
        return "legacy_draft_requires_reextraction"
    return "legacy_record_pending_v0_3_primary_source"


def _event_date(event: dict[str, Any]) -> str | None:
    timestamp = str((event.get("trigger") or {}).get("timestamp") or "")
    return timestamp[:10] if len(timestamp) >= 10 else None


def bootstrap_legacy_events(
    *,
    db_path: Path = DEFAULT_DB_PATH,
    events_dir: Path = REPO_ROOT / "events",
    enqueue_reextraction: bool = False,
) -> BootstrapResult:
    """Bootstrap existing YAML events into the internal v0.3 SQLite state.

    Internal-only scheduler flags stay in SQLite.  The payload preserves the
    YAML event so exports can round-trip through the current schema 0.2.0
    surface without adding `requires_v0_3_reextraction` to YAML.
    """
    init_db(db_path)
    events = load_yaml_events(events_dir)
    counts_status: dict[str, int] = {}
    counts_verification: dict[str, int] = {}
    queued_count = 0
    now = utc_now()
    with connect(db_path) as conn:
        for event in events:
            event_id = str(event.get("id"))
            internal_status = internal_status_from_yaml(event.get("status"))
            verification_state = verification_state_from_yaml(event)
            requires_reextraction = 0 if event.get("primary_source_verified") is True else 1
            trigger = event.get("trigger") or {}
            target = event.get("target") or {}
            subject = (
                target.get("actor_name")
                or target.get("protocol")
                or ",".join(target.get("canonical_domains") or [])
                or event_id
            )
            conn.execute(
                """
                INSERT INTO events (
                    event_id, canonical_slug, internal_status, pipeline, trigger_type,
                    actor, subject, event_date, jurisdiction_scope, analysis_use,
                    codebook_version, primary_source_verified, same_event_cluster_id,
                    requires_v0_3_reextraction, verification_state, last_pipeline_stage,
                    created_at, updated_at, payload_json
                )
                VALUES (?, ?, ?, 'legacy_yaml_bootstrap', ?, ?, ?, ?, ?, ?, ?, ?, NULL, ?, ?, 'bootstrap_legacy_yaml', ?, ?, ?)
                ON CONFLICT(event_id) DO UPDATE SET
                    canonical_slug=excluded.canonical_slug,
                    internal_status=excluded.internal_status,
                    pipeline=excluded.pipeline,
                    trigger_type=excluded.trigger_type,
                    actor=excluded.actor,
                    subject=excluded.subject,
                    event_date=excluded.event_date,
                    jurisdiction_scope=excluded.jurisdiction_scope,
                    analysis_use=excluded.analysis_use,
                    codebook_version=excluded.codebook_version,
                    primary_source_verified=excluded.primary_source_verified,
                    requires_v0_3_reextraction=excluded.requires_v0_3_reextraction,
                    verification_state=excluded.verification_state,
                    last_pipeline_stage=excluded.last_pipeline_stage,
                    updated_at=excluded.updated_at,
                    payload_json=excluded.payload_json
                """,
                (
                    event_id,
                    event_id,
                    internal_status,
                    trigger.get("type"),
                    trigger.get("actor"),
                    str(subject)[:500],
                    _event_date(event),
                    ",".join(event.get("jurisdiction") or []),
                    event.get("analysis_use"),
                    event.get("codebook_version") or CODEBOOK_VERSION,
                    1 if event.get("primary_source_verified") is True else 0,
                    requires_reextraction,
                    verification_state,
                    now,
                    now,
                    json_dumps({"yaml_event": event}),
                ),
            )
            if enqueue_reextraction and requires_reextraction:
                queue_id = enqueue_review(
                    conn,
                    item_type="event",
                    item_id=event_id,
                    reason="Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true.",
                    payload={
                        "pipeline": "legacy_yaml_bootstrap",
                        "verification_state": verification_state,
                        "source_file": event.get("_source_file"),
                    },
                    priority=70 if internal_status == "verified" else 90,
                )
                conn.execute(
                    "UPDATE events SET last_review_queue_item_id = ? WHERE event_id = ?",
                    (queue_id, event_id),
                )
                queued_count += 1
            counts_status[internal_status] = counts_status.get(internal_status, 0) + 1
            counts_verification[verification_state] = counts_verification.get(verification_state, 0) + 1
        conn.execute(
            """
            INSERT INTO audit_log (
                timestamp, actor, action, object_type, object_id,
                previous_state_json, new_state_json, reason, metadata_json
            )
            VALUES (?, 'system:bootstrap', 'legacy_yaml_bootstrap', 'corpus', 'events/*.yaml', NULL, ?, ?, ?)
            """,
            (
                now,
                json_dumps({"event_count": len(events), "queued_count": queued_count}),
                "Bootstrap existing YAML corpus into v0.3 internal SQLite state.",
                json_dumps({"enqueue_reextraction": enqueue_reextraction}),
            ),
        )
    return BootstrapResult(len(events), queued_count, counts_status, counts_verification)


def ingestion_status_report(db_path: Path = DEFAULT_DB_PATH) -> dict[str, Any]:
    init_db(db_path)
    with connect(db_path) as conn:
        def count_by(query: str) -> dict[str, int]:
            return {str(row[0]): int(row[1]) for row in conn.execute(query)}

        return {
            "generated_at": utc_now(),
            "events": {
                "total": conn.execute("SELECT COUNT(*) FROM events").fetchone()[0],
                "by_internal_status": count_by(
                    "SELECT internal_status, COUNT(*) FROM events GROUP BY internal_status"
                ),
                "by_verification_state": count_by(
                    "SELECT verification_state, COUNT(*) FROM events GROUP BY verification_state"
                ),
                "requires_v0_3_reextraction": conn.execute(
                    "SELECT COUNT(*) FROM events WHERE requires_v0_3_reextraction = 1"
                ).fetchone()[0],
                "primary_source_verified": conn.execute(
                    "SELECT COUNT(*) FROM events WHERE primary_source_verified = 1"
                ).fetchone()[0],
            },
            "review_queue": {
                "total": conn.execute("SELECT COUNT(*) FROM review_queue").fetchone()[0],
                "by_status": count_by("SELECT status, COUNT(*) FROM review_queue GROUP BY status"),
            },
            "sources": {
                "total": conn.execute("SELECT COUNT(*) FROM sources").fetchone()[0],
                "by_kind": count_by("SELECT kind, COUNT(*) FROM sources GROUP BY kind"),
                "failure_alerts": [
                    dict(row)
                    for row in conn.execute(
                        """
                        SELECT source_key, name, kind, failure_count, last_success_at,
                               last_failure_at, deprecated_at
                        FROM sources
                        WHERE failure_count >= 3 OR deprecated_at IS NOT NULL
                        ORDER BY failure_count DESC, name
                        """
                    )
                ],
            },
        }


def export_review_queue(
    *,
    db_path: Path = DEFAULT_DB_PATH,
    out_dir: Path = REPO_ROOT / "analysis" / "review_queue",
) -> dict[str, Path]:
    init_db(db_path)
    out_dir.mkdir(parents=True, exist_ok=True)
    with connect(db_path) as conn:
        rows = [dict(row) for row in conn.execute("SELECT * FROM review_queue ORDER BY status, priority, queue_id")]
    json_path = out_dir / "review_queue.json"
    csv_path = out_dir / "review_queue.csv"
    md_path = out_dir / "review_queue.md"
    json_path.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")
    fieldnames = [
        "queue_id",
        "item_type",
        "item_id",
        "status",
        "priority",
        "reason",
        "created_at",
        "updated_at",
        "resolved_at",
    ]
    with csv_path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key) for key in fieldnames})
    lines = [
        "# v0.3 Review Queue",
        "",
        "This is an export from the local ingestion SQLite state. It is not a paper denominator.",
        "",
        "| queue_id | status | priority | item_type | item_id | reason |",
        "| ---: | --- | ---: | --- | --- | --- |",
    ]
    for row in rows[:250]:
        reason = str(row.get("reason") or "").replace("|", "\\|")
        lines.append(
            f"| {row.get('queue_id')} | `{row.get('status')}` | {row.get('priority')} | "
            f"`{row.get('item_type')}` | `{row.get('item_id')}` | {reason} |"
        )
    if len(rows) > 250:
        lines.append(f"\n_Only first 250 of {len(rows)} rows shown; see CSV/JSON for full queue._")
    md_path.write_text("\n".join(lines) + "\n")
    return {"json": json_path, "csv": csv_path, "md": md_path}


def _json_loads(raw: str | None) -> dict[str, Any]:
    if not raw:
        return {}
    value = json.loads(raw)
    return value if isinstance(value, dict) else {}


def _citation_has_replayable_anchor(citation: Any) -> bool:
    if not isinstance(citation, dict):
        return False
    archive_url = str(citation.get("wayback") or citation.get("archive_url") or citation.get("wayback_url") or "")
    has_archive = "web.archive.org" in archive_url or archive_url.startswith("ipfs://")
    has_body = bool(citation.get("body_hash")) and bool(citation.get("body_path"))
    has_query = bool(citation.get("query_hash")) and bool(citation.get("body_path"))
    return has_archive or has_body or has_query


def _source_has_replayable_anchor(source: Any) -> bool:
    if not isinstance(source, dict):
        return False
    archive_url = str(source.get("wayback") or source.get("archive_url") or source.get("wayback_url") or "")
    has_archive = "web.archive.org" in archive_url or archive_url.startswith("ipfs://")
    has_body = bool(source.get("body_hash")) and bool(source.get("body_path"))
    has_query = bool(source.get("query_hash")) and bool(source.get("body_path"))
    return has_archive or has_body or has_query


def _source_is_primary(source: Any) -> bool:
    if not isinstance(source, dict):
        return False
    source_type = str(source.get("type") or "")
    return source_type.startswith("primary_") or source_type in PRIMARY_OBSERVATION_SOURCE_TYPES


def _is_null_event_no_repair_needed(event: dict[str, Any], observations: list[Any]) -> bool:
    tags = {str(tag) for tag in event.get("tags") or []}
    observation_kinds = {
        str(observation.get("observation_kind") or "")
        for observation in observations
        if isinstance(observation, dict)
    }
    return (
        "null_event_no_repair_needed" in tags
        and event.get("empirical_shape") == "null_event"
        and event.get("admission_tier") == "null_case"
        and "coverage_gap" in observation_kinds
        and "observed_change" not in observation_kinds
    )


def _yaml_event_from_joined_row(row: dict[str, Any]) -> dict[str, Any]:
    payload = _json_loads(row.get("event_payload_json"))
    event = payload.get("yaml_event")
    return dict(event) if isinstance(event, dict) else {}


def machine_prescreen_review_item(row: dict[str, Any]) -> dict[str, Any]:
    event = _yaml_event_from_joined_row(row)
    trigger = event.get("trigger") if isinstance(event.get("trigger"), dict) else {}
    trigger_citations = trigger.get("citation") if isinstance(trigger.get("citation"), list) else []
    observations = event.get("observations") if isinstance(event.get("observations"), list) else []
    coverage = event.get("coverage") if isinstance(event.get("coverage"), list) else []
    all_sources: list[dict[str, Any]] = []
    primary_sources: list[dict[str, Any]] = []
    replayable_sources: list[dict[str, Any]] = []
    for obs in observations:
        if not isinstance(obs, dict):
            continue
        sources = obs.get("sources") if isinstance(obs.get("sources"), list) else []
        for source in sources:
            if not isinstance(source, dict):
                continue
            all_sources.append(source)
            if _source_is_primary(source):
                primary_sources.append(source)
            if _source_has_replayable_anchor(source):
                replayable_sources.append(source)

    trigger_replayable = sum(1 for citation in trigger_citations if _citation_has_replayable_anchor(citation))
    primary_replayable = sum(
        1 for source in primary_sources if _source_has_replayable_anchor(source)
    )
    internal_status = str(row.get("internal_status") or "")
    verification_state = str(row.get("verification_state") or "")
    machine_notes: list[str] = []
    null_event_no_repair_needed = _is_null_event_no_repair_needed(event, observations)
    if null_event_no_repair_needed:
        machine_notes.append("null_event_no_repair_needed")
    if internal_status == "verified":
        bucket = "legacy_admitted_primary_source_recheck"
        next_action = "human_primary_source_recheck"
    elif verification_state == "legacy_draft_requires_reextraction":
        bucket = "legacy_draft_promotion_review"
        next_action = "human_promote_or_defer"
    elif internal_status == "retracted":
        bucket = "legacy_rejected_reference_review"
        next_action = "confirm_rejected_reference_or_defer"
    else:
        bucket = "candidate_primary_source_review"
        next_action = "human_candidate_review"
    blockers: list[str] = []
    if not event:
        blockers.append("missing_yaml_payload")
    if not trigger_citations:
        blockers.append("missing_trigger_citations")
    if trigger_citations and trigger_replayable == 0:
        blockers.append("no_replayable_trigger_anchor")
    if primary_sources and primary_replayable == 0:
        blockers.append("primary_sources_without_replayable_anchor")
    if not primary_sources and not null_event_no_repair_needed:
        blockers.append("no_observation_primary_source_detected")
    return {
        "queue_id": row.get("queue_id"),
        "event_id": row.get("event_id") or row.get("item_id"),
        "queue_status": row.get("queue_status"),
        "priority": row.get("priority"),
        "bucket": bucket,
        "next_action": next_action,
        "internal_status": internal_status,
        "verification_state": verification_state,
        "yaml_status": event.get("status"),
        "origin": event.get("origin"),
        "primary_source_verified": bool(row.get("primary_source_verified")),
        "requires_v0_3_reextraction": bool(row.get("requires_v0_3_reextraction")),
        "trigger_type": row.get("trigger_type") or trigger.get("type"),
        "actor": row.get("actor") or trigger.get("actor"),
        "event_date": row.get("event_date") or _event_date(event),
        "analysis_use": row.get("analysis_use") or event.get("analysis_use"),
        "source_file": (_json_loads(row.get("queue_payload_json")).get("source_file") or event.get("_source_file")),
        "trigger_citation_count": len(trigger_citations),
        "trigger_replayable_anchor_count": trigger_replayable,
        "coverage_row_count": len(coverage),
        "observation_count": len(observations),
        "observation_source_count": len(all_sources),
        "primary_observation_source_count": len(primary_sources),
        "replayable_observation_source_count": len(replayable_sources),
        "primary_replayable_observation_source_count": primary_replayable,
        "machine_blockers": blockers,
        "machine_notes": machine_notes,
    }


def _render_review_packet(row: dict[str, Any], prescreen: dict[str, Any]) -> str:
    event = _yaml_event_from_joined_row(row)
    queue_payload = _json_loads(row.get("queue_payload_json"))
    title = prescreen.get("event_id") or row.get("item_id")
    queue_reason = str(row.get("queue_reason") or "").replace("|", "\\|")
    promote_template = {
        "queue_id": prescreen["queue_id"],
        "decision": "resolved",
        "actor": "human:<name>",
        "reason": "Primary-source re-extraction completed; event evidence supports primary_source_verified=true.",
        "new_event_status": "verified",
        "metadata": {
            "review_type": "v0.3_primary_source_reextraction",
            "packet_generated_at": utc_now(),
            "human_review_required": True,
        },
    }
    needs_recheck_template = {
        "queue_id": prescreen["queue_id"],
        "decision": "needs_recheck",
        "actor": "human:<name>",
        "reason": "Primary-source re-extraction is incomplete or evidence is insufficient.",
        "metadata": {
            "review_type": "v0.3_primary_source_reextraction",
            "human_review_required": True,
        },
    }
    trigger = event.get("trigger") if isinstance(event.get("trigger"), dict) else {}
    target = event.get("target") if isinstance(event.get("target"), dict) else {}
    scoped_claim = str(event.get("scoped_claim") or "").replace("\n", " ")
    lines = [
        f"# v0.3 Review Packet: `{title}`",
        "",
        "This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.",
        "",
        "## Queue",
        "",
        "| Field | Value |",
        "| --- | --- |",
        f"| queue_id | `{prescreen['queue_id']}` |",
        f"| status | `{prescreen['queue_status']}` |",
        f"| priority | `{prescreen['priority']}` |",
        f"| bucket | `{prescreen['bucket']}` |",
        f"| next_action | `{prescreen['next_action']}` |",
        f"| reason | {queue_reason} |",
        "",
        "## Event",
        "",
        "| Field | Value |",
        "| --- | --- |",
        f"| event_id | `{prescreen['event_id']}` |",
        f"| yaml_status | `{prescreen['yaml_status']}` |",
        f"| internal_status | `{prescreen['internal_status']}` |",
        f"| verification_state | `{prescreen['verification_state']}` |",
        f"| origin | `{prescreen['origin']}` |",
        f"| primary_source_verified | `{prescreen['primary_source_verified']}` |",
        f"| requires_v0_3_reextraction | `{prescreen['requires_v0_3_reextraction']}` |",
        f"| trigger_type | `{prescreen['trigger_type']}` |",
        f"| actor | `{prescreen['actor']}` |",
        f"| event_date | `{prescreen['event_date']}` |",
        f"| source_file | `{prescreen.get('source_file') or ''}` |",
        f"| target_kind | `{target.get('kind') or ''}` |",
        f"| target_actor | `{target.get('actor_name') or target.get('protocol') or ''}` |",
        "",
        "## Machine Prescreen",
        "",
        "| Check | Count / Value |",
        "| --- | ---: |",
        f"| trigger citations | {prescreen['trigger_citation_count']} |",
        f"| replayable trigger anchors | {prescreen['trigger_replayable_anchor_count']} |",
        f"| coverage rows | {prescreen['coverage_row_count']} |",
        f"| observations | {prescreen['observation_count']} |",
        f"| observation sources | {prescreen['observation_source_count']} |",
        f"| primary observation sources | {prescreen['primary_observation_source_count']} |",
        f"| replayable observation sources | {prescreen['replayable_observation_source_count']} |",
        f"| primary replayable observation sources | {prescreen['primary_replayable_observation_source_count']} |",
        "",
        f"Machine blockers: `{', '.join(prescreen['machine_blockers']) or 'none_detected'}`",
        f"Machine notes: `{', '.join(prescreen.get('machine_notes') or []) or 'none'}`",
        "",
        "## Scoped Claim",
        "",
        scoped_claim or "_No scoped claim in YAML payload._",
        "",
        "## Trigger Citations",
        "",
    ]
    citations = trigger.get("citation") if isinstance(trigger.get("citation"), list) else []
    if citations:
        for idx, citation in enumerate(citations):
            if not isinstance(citation, dict):
                continue
            url = citation.get("url") or citation.get("archive_url") or citation.get("wayback_url") or ""
            lines.append(
                f"- citation[{idx}]: `{citation.get('source_type') or citation.get('type') or 'unknown'}` "
                f"replayable=`{_citation_has_replayable_anchor(citation)}` {url}"
            )
    else:
        lines.append("_No trigger citations detected._")
    lines.extend(
        [
            "",
            "## Required Human Decisions",
            "",
            "- Confirm this row is one concrete trigger/target unit under the codebook.",
            "- Confirm the trigger has at least one replayable primary or admission-grade source anchor.",
            "- Confirm layer observations still support the YAML status and scoped claim.",
            "- Resolve only after primary-source re-extraction is complete.",
            "",
            "## Decision JSON Templates",
            "",
            "Promotion after real human verification:",
            "",
            "```json",
            json.dumps(promote_template, indent=2, sort_keys=True),
            "```",
            "",
            "Needs recheck / cannot verify yet:",
            "",
            "```json",
            json.dumps(needs_recheck_template, indent=2, sort_keys=True),
            "```",
            "",
            "## Queue Payload",
            "",
            "```json",
            json.dumps(queue_payload, indent=2, sort_keys=True),
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def write_review_packets(
    *,
    db_path: Path = DEFAULT_DB_PATH,
    out_dir: Path = REPO_ROOT / "analysis" / "review_queue" / "packets",
    limit: int | None = None,
    include_resolved: bool = False,
) -> dict[str, Any]:
    init_db(db_path)
    out_dir.mkdir(parents=True, exist_ok=True)
    status_clause = "" if include_resolved else "WHERE q.status = 'pending'"
    query = f"""
        SELECT
            q.queue_id, q.item_type, q.item_id, q.status AS queue_status,
            q.priority, q.reason AS queue_reason, q.payload_json AS queue_payload_json,
            q.created_at AS queue_created_at, q.updated_at AS queue_updated_at,
            e.event_id, e.canonical_slug, e.internal_status, e.pipeline,
            e.trigger_type, e.actor, e.subject, e.event_date, e.jurisdiction_scope,
            e.analysis_use, e.codebook_version, e.primary_source_verified,
            e.requires_v0_3_reextraction, e.verification_state,
            e.payload_json AS event_payload_json
        FROM review_queue q
        LEFT JOIN events e ON e.event_id = q.item_id
        {status_clause}
        ORDER BY q.priority ASC, q.queue_id ASC
    """
    with connect(db_path) as conn:
        rows = [dict(row) for row in conn.execute(query)]
    if limit is not None:
        rows = rows[:limit]
    index_rows: list[dict[str, Any]] = []
    for row in rows:
        prescreen = machine_prescreen_review_item(row)
        filename = f"{int(row['queue_id']):04d}-{slugify(str(row['item_id']))}.md"
        packet_path = out_dir / filename
        packet_path.write_text(_render_review_packet(row, prescreen))
        index_row = dict(prescreen)
        try:
            index_row["packet_path"] = str(packet_path.relative_to(REPO_ROOT))
        except ValueError:
            index_row["packet_path"] = str(packet_path)
        index_rows.append(index_row)

    index_json = out_dir / "index.json"
    index_csv = out_dir / "index.csv"
    index_md = out_dir / "index.md"
    index_payload = {
        "generated_at": utc_now(),
        "packet_count": len(index_rows),
        "include_resolved": include_resolved,
        "queue_status_mutated": False,
        "primary_source_verified_mutated": False,
        "rows": index_rows,
    }
    index_json.write_text(json.dumps(index_payload, indent=2, sort_keys=True) + "\n")
    fieldnames = [
        "queue_id",
        "event_id",
        "queue_status",
        "priority",
        "bucket",
        "next_action",
        "internal_status",
        "verification_state",
        "primary_source_verified",
        "trigger_citation_count",
        "trigger_replayable_anchor_count",
        "primary_observation_source_count",
        "primary_replayable_observation_source_count",
        "machine_blockers",
        "machine_notes",
        "packet_path",
    ]
    with index_csv.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in index_rows:
            csv_row = {key: row.get(key) for key in fieldnames}
            csv_row["machine_blockers"] = ";".join(row.get("machine_blockers") or [])
            csv_row["machine_notes"] = ";".join(row.get("machine_notes") or [])
            writer.writerow(csv_row)

    lines = [
        "# v0.3 Review Packet Index",
        "",
        "Machine-prepared packets for human primary-source re-extraction. This index does not resolve queue items.",
        "",
        f"- Packet count: {len(index_rows)}",
        "- Queue status mutated: `false`",
        "- Primary-source verified mutated: `false`",
        "",
        "| queue_id | priority | bucket | event_id | blockers | packet |",
        "| ---: | ---: | --- | --- | --- | --- |",
    ]
    for row in index_rows:
        blockers = ", ".join(row.get("machine_blockers") or []) or "none_detected"
        lines.append(
            f"| {row['queue_id']} | {row['priority']} | `{row['bucket']}` | "
            f"`{row['event_id']}` | {blockers} | [{Path(row['packet_path']).name}]({Path(row['packet_path']).name}) |"
        )
    index_md.write_text("\n".join(lines) + "\n")
    return {
        "packet_count": len(index_rows),
        "out_dir": str(out_dir),
        "index_json": str(index_json),
        "index_csv": str(index_csv),
        "index_md": str(index_md),
    }


def _review_triage_audit_stage(row: dict[str, Any], machine_blockers: list[str]) -> tuple[str, str, str]:
    status = str(row.get("queue_status") or "")
    actor = str(row.get("last_decision_actor") or "")
    metadata = _json_loads(row.get("last_decision_metadata_json"))
    review_type = str(metadata.get("review_type") or "")
    if status == "pending":
        return (
            "llm_prescreen_no_machine_blocker",
            "awaiting_human_audit",
            "human_primary_source_confirmation",
        )
    if actor.startswith("agent:") or review_type == "v0.3_machine_triage":
        if not machine_blockers:
            return (
                "llm_prescreen_repaired_awaiting_human_audit",
                "awaiting_human_audit",
                "human_primary_source_confirmation_after_machine_repair",
            )
        return (
            "llm_prescreen_before_human_audit",
            "not_human_audited",
            "evidence_repair_then_human_confirmation",
        )
    return (
        "human_review_recorded",
        "human_audit_recorded",
        "follow_recorded_human_decision",
    )


def _trigger_url_hosts(event: dict[str, Any]) -> str:
    trigger = event.get("trigger") if isinstance(event.get("trigger"), dict) else {}
    citations = trigger.get("citation") or []
    if not isinstance(citations, list):
        return ""
    hosts: set[str] = set()
    for citation in citations:
        if not isinstance(citation, dict):
            continue
        url = citation.get("url")
        if isinstance(url, str) and url:
            host = urlparse(url).netloc
            if host:
                hosts.add(host)
    return ";".join(sorted(hosts))


def _review_triage_rows(db_path: Path = DEFAULT_DB_PATH) -> list[dict[str, Any]]:
    init_db(db_path)
    query = """
        WITH latest_audit AS (
            SELECT object_id, MAX(audit_id) AS audit_id
            FROM audit_log
            WHERE action = 'review_decision'
            GROUP BY object_id
        )
        SELECT
            q.queue_id, q.item_type, q.item_id, q.status AS queue_status,
            q.priority, q.reason AS queue_reason, q.payload_json AS queue_payload_json,
            q.created_at AS queue_created_at, q.updated_at AS queue_updated_at,
            e.event_id, e.canonical_slug, e.internal_status, e.pipeline,
            e.trigger_type, e.actor, e.subject, e.event_date, e.jurisdiction_scope,
            e.analysis_use, e.codebook_version, e.primary_source_verified,
            e.requires_v0_3_reextraction, e.verification_state,
            e.payload_json AS event_payload_json,
            a.actor AS last_decision_actor,
            a.reason AS last_decision_reason,
            a.metadata_json AS last_decision_metadata_json
        FROM review_queue q
        LEFT JOIN events e ON e.event_id = q.item_id
        LEFT JOIN latest_audit la ON la.object_id = q.item_id
        LEFT JOIN audit_log a ON a.audit_id = la.audit_id
        ORDER BY q.status, q.priority ASC, q.queue_id ASC
    """
    with connect(db_path) as conn:
        rows = [dict(row) for row in conn.execute(query)]
    output: list[dict[str, Any]] = []
    for row in rows:
        prescreen = machine_prescreen_review_item(row)
        event = _yaml_event_from_joined_row(row)
        machine_blockers = prescreen.get("machine_blockers") or []
        audit_stage, human_audit_status, next_human_action = _review_triage_audit_stage(row, machine_blockers)
        output.append(
            {
                "queue_id": prescreen["queue_id"],
                "event_id": prescreen["event_id"],
                "queue_status": row.get("queue_status"),
                "priority": prescreen["priority"],
                "bucket": prescreen["bucket"],
                "next_action": prescreen["next_action"],
                "audit_stage": audit_stage,
                "human_audit_status": human_audit_status,
                "next_human_action": next_human_action,
                "internal_status": prescreen["internal_status"],
                "verification_state": prescreen["verification_state"],
                "primary_source_verified": prescreen["primary_source_verified"],
                "trigger_citation_count": prescreen["trigger_citation_count"],
                "trigger_replayable_anchor_count": prescreen["trigger_replayable_anchor_count"],
                "primary_observation_source_count": prescreen["primary_observation_source_count"],
                "primary_replayable_observation_source_count": prescreen[
                    "primary_replayable_observation_source_count"
                ],
                "machine_blockers": ";".join(machine_blockers),
                "last_decision_actor": row.get("last_decision_actor") or "",
                "trigger_url_hosts": _trigger_url_hosts(event),
                "packet_path": f"analysis/review_queue/packets/{int(row['queue_id']):04d}-{slugify(str(row['item_id']))}.md",
            }
        )
    return output


def write_review_triage_summary(
    *,
    db_path: Path = DEFAULT_DB_PATH,
    out_dir: Path = REPO_ROOT / "analysis" / "review_queue",
) -> dict[str, Path]:
    rows = _review_triage_rows(db_path)
    out_dir.mkdir(parents=True, exist_ok=True)

    pending_human = [
        row
        for row in rows
        if row["queue_status"] == "pending" and row["audit_stage"] == "llm_prescreen_no_machine_blocker"
    ]
    llm_flagged = [
        row
        for row in rows
        if row["queue_status"] == "needs_recheck"
        and row["audit_stage"] == "llm_prescreen_before_human_audit"
    ]
    repaired_pending_human = [
        row
        for row in rows
        if row["audit_stage"] == "llm_prescreen_repaired_awaiting_human_audit"
    ]
    human_recorded = [row for row in rows if row["audit_stage"] == "human_review_recorded"]

    status_counts: dict[str, int] = {}
    blocker_counts: dict[str, int] = {}
    for row in rows:
        status = str(row["queue_status"])
        status_counts[status] = status_counts.get(status, 0) + 1
        blockers = str(row["machine_blockers"] or "none_detected")
        if status == "needs_recheck":
            blocker_counts[blockers] = blocker_counts.get(blockers, 0) + 1

    summary = {
        "generated_at": utc_now(),
        "report_kind": "v0.3_review_triage_summary",
        "total_queue_items": len(rows),
        "queue_status_counts": status_counts,
        "llm_prescreen_no_machine_blocker_awaiting_human": len(pending_human),
        "llm_prescreen_repaired_awaiting_human": len(repaired_pending_human),
        "llm_prescreen_flagged_before_human_audit": len(llm_flagged),
        "human_review_recorded": len(human_recorded),
        "human_audited_by_this_triage": 0,
        "primary_source_verified_mutated": False,
        "verified_events_mutated": False,
        "status_semantics": {
            "pending": "LLM/machine prescreen found no blocker; awaiting real human primary-source audit.",
            "needs_recheck": "Agent-authored needs_recheck rows are pre-human LLM flags. Rows with no current machine blockers have been machine-repaired and are awaiting human audit; remaining rows still require evidence/source repair.",
        },
        "needs_recheck_by_blocker": blocker_counts,
    }

    json_path = out_dir / "v0_3_review_triage_summary.json"
    md_path = out_dir / "v0_3_review_triage_summary.md"
    pending_csv = out_dir / "pending_human_confirmation.csv"
    repair_csv = out_dir / "needs_evidence_repair.csv"
    llm_flagged_csv = out_dir / "llm_prescreen_flagged_for_repair.csv"
    json_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")

    fieldnames = [
        "queue_id",
        "event_id",
        "queue_status",
        "priority",
        "bucket",
        "next_action",
        "audit_stage",
        "human_audit_status",
        "next_human_action",
        "internal_status",
        "verification_state",
        "primary_source_verified",
        "trigger_citation_count",
        "trigger_replayable_anchor_count",
        "primary_observation_source_count",
        "primary_replayable_observation_source_count",
        "machine_blockers",
        "last_decision_actor",
        "trigger_url_hosts",
        "packet_path",
    ]
    for path, data in [
        (pending_csv, pending_human),
        (repair_csv, llm_flagged),
        (llm_flagged_csv, llm_flagged),
    ]:
        with path.open("w", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
            writer.writeheader()
            for row in data:
                writer.writerow({key: row.get(key, "") for key in fieldnames})

    lines = [
        "# v0.3 Review Triage Summary",
        "",
        "This is a pre-human LLM/machine triage artifact. It does not constitute human audit, primary-source verification, or release approval.",
        "",
        "## Queue State",
        "",
        "| State | Count | Meaning |",
        "| --- | ---: | --- |",
        f"| `llm_prescreen_no_machine_blocker` | {len(pending_human)} | No machine blocker detected; awaiting human primary-source confirmation. |",
        f"| `llm_prescreen_repaired_awaiting_human_audit` | {len(repaired_pending_human)} | Earlier LLM flag now has no current machine blocker after evidence repair; awaiting human confirmation. |",
        f"| `llm_prescreen_before_human_audit` | {len(llm_flagged)} | LLM/machine flagged missing anchors or sources before human audit; repair evidence before confirmation. |",
        f"| `human_review_recorded` | {len(human_recorded)} | A non-agent review decision is already recorded in the local audit log. |",
        "",
        "No event was promoted, no human audit was recorded, and no `primary_source_verified` flag was changed by this triage.",
        "",
        "## Pending Human Confirmation",
        "",
        "| queue_id | bucket | event_id | packet |",
        "| ---: | --- | --- | --- |",
    ]
    for row in pending_human + repaired_pending_human:
        packet = Path(str(row["packet_path"])).name
        lines.append(
            f"| {row['queue_id']} | `{row['bucket']}` | `{row['event_id']}` | [packet](packets/{packet}) |"
        )
    lines.extend(
        [
            "",
            "## LLM-Prescreen Flagged For Repair",
            "",
            "| Blocker | Count |",
            "| --- | ---: |",
        ]
    )
    for blocker, count in sorted(blocker_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| `{blocker}` | {count} |")
    lines.extend(
        [
            "",
            "## Work Files",
            "",
            "- `pending_human_confirmation.csv`: rows ready for human confirmation after LLM/machine prescreen.",
            "- `llm_prescreen_flagged_for_repair.csv`: pre-human LLM/machine flags requiring evidence repair.",
            "- `needs_evidence_repair.csv`: compatibility alias for the same repair list.",
            "- `packets/index.md`: all machine-prepared packets with current queue status.",
        ]
    )
    md_path.write_text("\n".join(lines) + "\n")
    return {
        "json": json_path,
        "md": md_path,
        "pending_csv": pending_csv,
        "repair_csv": repair_csv,
        "llm_flagged_csv": llm_flagged_csv,
    }


def _human_verify_decision_template(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "queue_id": row["queue_id"],
        "decision": "resolved",
        "actor": "human:<name>",
        "reason": "Human primary-source re-extraction completed; event evidence supports primary_source_verified=true.",
        "new_event_status": "verified",
        "metadata": {
            "review_type": "v0.3_primary_source_reextraction",
            "human_review_required": True,
            "worksheet": "analysis/review_queue/human_audit_worksheet.csv",
            "evidence_confirmation": {
                "trigger_unit_confirmed": "<true/false>",
                "replayable_trigger_anchor_confirmed": "<true/false>",
                "observations_confirmed": "<true/false>",
                "scoped_claim_confirmed": "<true/false>",
            },
        },
    }


def _human_needs_recheck_decision_template(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "queue_id": row["queue_id"],
        "decision": "needs_recheck",
        "actor": "human:<name>",
        "reason": "Human primary-source re-extraction found evidence incomplete or insufficient.",
        "metadata": {
            "review_type": "v0.3_primary_source_reextraction",
            "human_review_required": True,
            "worksheet": "analysis/review_queue/human_audit_worksheet.csv",
        },
    }


def write_human_audit_worksheet(
    *,
    db_path: Path = DEFAULT_DB_PATH,
    out_dir: Path = REPO_ROOT / "analysis" / "review_queue",
) -> dict[str, Path]:
    rows = [
        row
        for row in _review_triage_rows(db_path)
        if row["audit_stage"]
        in {
            "llm_prescreen_no_machine_blocker",
            "llm_prescreen_repaired_awaiting_human_audit",
        }
    ]
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "human_audit_worksheet.csv"
    md_path = out_dir / "human_audit_worksheet.md"
    templates_path = out_dir / "human_audit_decision_templates.jsonl"

    fieldnames = [
        "queue_id",
        "event_id",
        "bucket",
        "audit_stage",
        "human_audit_status",
        "trigger_citation_count",
        "trigger_replayable_anchor_count",
        "primary_observation_source_count",
        "primary_replayable_observation_source_count",
        "trigger_url_hosts",
        "packet_path",
        "reviewer",
        "reviewed_at",
        "trigger_unit_confirmed",
        "replayable_trigger_anchor_confirmed",
        "observations_confirmed",
        "scoped_claim_confirmed",
        "decision",
        "decision_reason",
    ]
    with csv_path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            csv_row = {key: row.get(key, "") for key in fieldnames}
            for key in [
                "reviewer",
                "reviewed_at",
                "trigger_unit_confirmed",
                "replayable_trigger_anchor_confirmed",
                "observations_confirmed",
                "scoped_claim_confirmed",
                "decision",
                "decision_reason",
            ]:
                csv_row[key] = ""
            writer.writerow(csv_row)

    with templates_path.open("w") as fh:
        for row in rows:
            payload = {
                "event_id": row["event_id"],
                "verify_decision": _human_verify_decision_template(row),
                "needs_recheck_decision": _human_needs_recheck_decision_template(row),
            }
            fh.write(json.dumps(payload, sort_keys=True) + "\n")

    lines = [
        "# v0.3 Human Audit Worksheet",
        "",
        "This worksheet is blank by design. It is for real human primary-source confirmation after LLM/machine prescreening.",
        "",
        f"- Rows awaiting human audit: {len(rows)}",
        "- This worksheet does not mutate queue status.",
        "- This worksheet does not set `primary_source_verified=true`.",
        "- Use `human_audit_decision_templates.jsonl` only after completing the corresponding human review fields.",
        "",
        "| queue_id | event_id | trigger anchors | observation anchors | packet |",
        "| ---: | --- | ---: | ---: | --- |",
    ]
    for row in rows:
        packet = Path(str(row["packet_path"])).name
        lines.append(
            f"| {row['queue_id']} | `{row['event_id']}` | "
            f"{row['trigger_replayable_anchor_count']}/{row['trigger_citation_count']} | "
            f"{row['primary_replayable_observation_source_count']}/{row['primary_observation_source_count']} | "
            f"[packet](packets/{packet}) |"
        )
    md_path.write_text("\n".join(lines) + "\n")
    return {
        "csv": csv_path,
        "md": md_path,
        "decision_templates": templates_path,
    }


def _repair_class(blockers: str) -> tuple[int, str, str]:
    parts = set(filter(None, blockers.split(";")))
    if {"no_replayable_trigger_anchor", "no_observation_primary_source_detected"} <= parts:
        return (
            10,
            "repair_trigger_anchor_and_observation_source",
            "Add a replayable trigger anchor and at least one primary observation source before human confirmation.",
        )
    if {"no_replayable_trigger_anchor", "primary_sources_without_replayable_anchor"} <= parts:
        return (
            20,
            "repair_replayable_trigger_anchor",
            "Attach body_hash/body_path or another replayable anchor to the primary trigger/observation source.",
        )
    if "no_observation_primary_source_detected" in parts:
        return (
            30,
            "repair_observation_primary_source",
            "Attach at least one primary observation source that supports the layer observation.",
        )
    return (90, "manual_triage", "Inspect the packet and decide the evidence repair path.")


def write_evidence_repair_plan(
    *,
    db_path: Path = DEFAULT_DB_PATH,
    out_dir: Path = REPO_ROOT / "analysis" / "review_queue",
) -> dict[str, Path]:
    rows = [
        row
        for row in _review_triage_rows(db_path)
        if row["queue_status"] == "needs_recheck"
        and row["audit_stage"] == "llm_prescreen_before_human_audit"
        and row.get("machine_blockers")
    ]
    repair_rows: list[dict[str, Any]] = []
    for row in rows:
        base_priority, repair_class, repair_action = _repair_class(str(row.get("machine_blockers") or ""))
        bucket_boost = 0 if row["bucket"] == "legacy_admitted_primary_source_recheck" else 50
        repair_rows.append(
            {
                "repair_priority": base_priority + bucket_boost,
                "repair_class": repair_class,
                "repair_action": repair_action,
                **row,
            }
        )
    repair_rows.sort(key=lambda row: (int(row["repair_priority"]), int(row["queue_id"])))

    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "evidence_repair_plan.csv"
    json_path = out_dir / "evidence_repair_plan.json"
    md_path = out_dir / "evidence_repair_plan.md"

    fieldnames = [
        "repair_priority",
        "repair_class",
        "repair_action",
        "queue_id",
        "event_id",
        "bucket",
        "machine_blockers",
        "trigger_citation_count",
        "trigger_replayable_anchor_count",
        "primary_observation_source_count",
        "primary_replayable_observation_source_count",
        "trigger_url_hosts",
        "packet_path",
    ]
    with csv_path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in repair_rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})

    class_counts: dict[str, int] = {}
    for row in repair_rows:
        klass = str(row["repair_class"])
        class_counts[klass] = class_counts.get(klass, 0) + 1
    json_path.write_text(
        json.dumps(
            {
                "generated_at": utc_now(),
                "report_kind": "v0.3_evidence_repair_plan",
                "row_count": len(repair_rows),
                "human_audit_status": "not_human_audited",
                "class_counts": class_counts,
                "rows": repair_rows,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )

    lines = [
        "# v0.3 Evidence Repair Plan",
        "",
        "This plan covers LLM/machine flagged rows before human audit. It is not a human audit result.",
        "",
        "## Summary",
        "",
        "| Repair class | Count |",
        "| --- | ---: |",
    ]
    for klass, count in sorted(class_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| `{klass}` | {count} |")
    lines.extend(
        [
            "",
            "## Repair Queue",
            "",
            "| priority | event_id | class | blockers | packet |",
            "| ---: | --- | --- | --- | --- |",
        ]
    )
    for row in repair_rows:
        packet = Path(str(row["packet_path"])).name
        lines.append(
            f"| {row['repair_priority']} | `{row['event_id']}` | `{row['repair_class']}` | "
            f"`{row['machine_blockers']}` | [packet](packets/{packet}) |"
        )
    md_path.write_text("\n".join(lines) + "\n")
    return {"csv": csv_path, "json": json_path, "md": md_path}


def _observation_source_types(event: dict[str, Any]) -> list[str]:
    source_types: set[str] = set()
    for observation in event.get("observations") or []:
        if not isinstance(observation, dict):
            continue
        for source in observation.get("sources") or []:
            if isinstance(source, dict) and source.get("type"):
                source_types.add(str(source["type"]))
    return sorted(source_types)


def _observation_url_hosts(event: dict[str, Any]) -> str:
    hosts: set[str] = set()
    for observation in event.get("observations") or []:
        if not isinstance(observation, dict):
            continue
        for source in observation.get("sources") or []:
            if not isinstance(source, dict):
                continue
            url = source.get("url")
            if isinstance(url, str) and url:
                host = urlparse(url).netloc
                if host:
                    hosts.add(host)
    return ";".join(sorted(hosts))


def _load_event_yaml(events_dir: Path, event_id: str) -> dict[str, Any]:
    path = events_dir / f"{event_id}.yaml"
    if not path.exists():
        return {}
    event = yaml.safe_load(path.read_text()) or {}
    return event if isinstance(event, dict) else {}


def _source_discovery_class(event: dict[str, Any]) -> tuple[str, str]:
    observations = event.get("observations") if isinstance(event.get("observations"), list) else []
    if not observations:
        return (
            "define_observation_or_defer",
            "Add a concrete observation row with a replayable primary source, or defer/downgrade the row before human audit.",
        )
    if event.get("empirical_shape") == "null_event":
        return (
            "find_replayable_null_observation_anchor",
            "Attach a replayable primary null-observation substrate, such as a pinned Wayback bracket, query result, measurement slice, or on-chain/state receipt.",
        )
    return (
        "find_primary_observed_change_anchor",
        "Replace or supplement supporting sources with a primary actor notice, platform-state snapshot, on-chain receipt, official docket/order, or measurement artifact.",
    )


def _suggest_source_frames(event: dict[str, Any]) -> list[str]:
    event_id = str(event.get("id") or "")
    trigger = event.get("trigger") if isinstance(event.get("trigger"), dict) else {}
    actor = str(trigger.get("actor") or "")
    trigger_type = str(trigger.get("type") or "")
    stratum = str(event.get("research_stratum") or "")
    tags = " ".join(str(tag) for tag in event.get("tags") or [])
    jurisdictions = " ".join(str(item) for item in event.get("jurisdiction") or [])
    haystack = " ".join([event_id, actor, trigger_type, stratum, tags, jurisdictions]).lower()
    frames: list[str] = []

    if "ofac" in haystack or "sanction" in haystack:
        frames.append("ofac_recent_actions_or_sdn_diff_plus_target_surface_snapshot")
    if any(token in haystack for token in ["sec", "cftc", "doj", "fincen", "court", "bankruptcy"]):
        frames.append("official_agency_release_or_court_docket")
    if any(token in haystack for token in ["tether", "circle", "paxos", "stablecoin", "usdc", "usdt"]):
        frames.append("issuer_transparency_report_or_onchain_blacklist_receipt")
    if any(token in haystack for token in ["apple", "app_store"]):
        frames.append("app_store_regional_availability_snapshot")
    if any(token in haystack for token in ["google", "play"]):
        frames.append("google_play_regional_availability_snapshot")
    if any(token in haystack for token in ["github", "uniswap", "balancer", "aave", "ens", "tornado"]):
        frames.append("operator_git_platform_or_wayback_state_snapshot")
    if any(token in haystack for token in ["china", "pboc", "weibo", "sichuan", "inner-mongolia"]):
        frames.append("cn_primary_source_worker_official_notice_and_platform_archives")
    if any(token in haystack for token in ["japan", "korea", "russia", "bangladesh", "philippines", "thailand", "kazakhstan", "iceland"]):
        frames.append("local_language_regulator_or_platform_archive")
    if any(token in haystack for token in ["l0", "shutdown", "network", "mining", "hashrate"]):
        frames.append("measurement_artifact_ooni_ioda_netblocks_cbcei")

    if not frames:
        frames.append("primary_actor_notice_or_replayable_measurement_artifact")
    return sorted(dict.fromkeys(frames))


def write_source_discovery_worklist(
    *,
    db_path: Path = DEFAULT_DB_PATH,
    out_dir: Path = REPO_ROOT / "analysis" / "review_queue",
    events_dir: Path = REPO_ROOT / "events",
) -> dict[str, Path]:
    rows = [
        row
        for row in _review_triage_rows(db_path)
        if row["queue_status"] == "needs_recheck"
        and row["audit_stage"] == "llm_prescreen_before_human_audit"
        and "no_observation_primary_source_detected" in str(row.get("machine_blockers") or "")
    ]
    work_rows: list[dict[str, Any]] = []
    for row in rows:
        event = _load_event_yaml(events_dir, str(row["event_id"]))
        discovery_class, next_action = _source_discovery_class(event)
        source_types = _observation_source_types(event)
        base_priority, _repair_class_name, _repair_action = _repair_class(str(row.get("machine_blockers") or ""))
        bucket_boost = 0 if row["bucket"] == "legacy_admitted_primary_source_recheck" else 50
        work_rows.append(
            {
                "work_priority": base_priority + bucket_boost,
                "discovery_class": discovery_class,
                "next_non_human_action": next_action,
                "queue_id": row["queue_id"],
                "event_id": row["event_id"],
                "yaml_status": event.get("status", ""),
                "origin": event.get("origin", ""),
                "empirical_shape": event.get("empirical_shape", ""),
                "admission_tier": event.get("admission_tier", ""),
                "analysis_use": event.get("analysis_use", ""),
                "temporal_tier": event.get("temporal_tier", ""),
                "observation_count": len(event.get("observations") or []),
                "observation_source_types": ";".join(source_types),
                "trigger_url_hosts": row.get("trigger_url_hosts", ""),
                "observation_url_hosts": _observation_url_hosts(event),
                "suggested_source_frames": ";".join(_suggest_source_frames(event)),
                "packet_path": row.get("packet_path", ""),
                "event_path": str((events_dir / f"{row['event_id']}.yaml").relative_to(REPO_ROOT))
                if (events_dir / f"{row['event_id']}.yaml").is_relative_to(REPO_ROOT)
                else str(events_dir / f"{row['event_id']}.yaml"),
                "human_audit_status": "not_human_audited",
            }
        )
    work_rows.sort(key=lambda row: (int(row["work_priority"]), int(row["queue_id"])))

    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "source_discovery_worklist.csv"
    json_path = out_dir / "source_discovery_worklist.json"
    md_path = out_dir / "source_discovery_worklist.md"
    fieldnames = [
        "work_priority",
        "discovery_class",
        "next_non_human_action",
        "queue_id",
        "event_id",
        "yaml_status",
        "origin",
        "empirical_shape",
        "admission_tier",
        "analysis_use",
        "temporal_tier",
        "observation_count",
        "observation_source_types",
        "trigger_url_hosts",
        "observation_url_hosts",
        "suggested_source_frames",
        "packet_path",
        "event_path",
        "human_audit_status",
    ]
    with csv_path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in work_rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})

    class_counts: dict[str, int] = {}
    for row in work_rows:
        klass = str(row["discovery_class"])
        class_counts[klass] = class_counts.get(klass, 0) + 1
    json_path.write_text(
        json.dumps(
            {
                "generated_at": utc_now(),
                "report_kind": "v0.3_source_discovery_worklist",
                "human_audit_status": "not_human_audited",
                "row_count": len(work_rows),
                "class_counts": class_counts,
                "rows": work_rows,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )

    lines = [
        "# v0.3 Source Discovery Worklist",
        "",
        "This is a pre-human, non-audit worklist for rows that still lack primary observation evidence after machine anchor repair.",
        "",
        f"- Rows requiring source discovery or methodology repair: {len(work_rows)}",
        "- No queue status, YAML status, `last_human_audit`, or `primary_source_verified` field is changed by this artifact.",
        "",
        "## Summary",
        "",
        "| Discovery class | Count |",
        "| --- | ---: |",
    ]
    for klass, count in sorted(class_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| `{klass}` | {count} |")
    lines.extend(
        [
            "",
            "## Work Queue",
            "",
            "| priority | event_id | class | source frames | packet |",
            "| ---: | --- | --- | --- | --- |",
        ]
    )
    for row in work_rows:
        packet = Path(str(row["packet_path"])).name
        lines.append(
            f"| {row['work_priority']} | `{row['event_id']}` | `{row['discovery_class']}` | "
            f"`{row['suggested_source_frames']}` | [packet](packets/{packet}) |"
        )
    md_path.write_text("\n".join(lines) + "\n")
    return {"csv": csv_path, "json": json_path, "md": md_path}


def _csv_row_count(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open(newline="") as fh:
        return sum(1 for _row in csv.DictReader(fh))


def _capture_status_counts(path: Path) -> dict[str, int]:
    counts: dict[str, int] = {}
    if not path.exists():
        return counts
    with path.open(newline="") as fh:
        for row in csv.DictReader(fh):
            status = str(row.get("status") or "")
            counts[status] = counts.get(status, 0) + 1
    return counts


def write_non_human_todo_list(
    *,
    db_path: Path = DEFAULT_DB_PATH,
    out_dir: Path = REPO_ROOT / "analysis" / "review_queue",
) -> dict[str, Path]:
    rows = _review_triage_rows(db_path)
    ready_for_human = [
        row
        for row in rows
        if row["audit_stage"]
        in {"llm_prescreen_no_machine_blocker", "llm_prescreen_repaired_awaiting_human_audit"}
    ]
    source_discovery_rows = [
        row
        for row in rows
        if row["audit_stage"] == "llm_prescreen_before_human_audit"
        and "no_observation_primary_source_detected" in str(row.get("machine_blockers") or "")
    ]
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "non_human_todo_list.json"
    md_path = out_dir / "non_human_todo_list.md"

    capture_counts = _capture_status_counts(out_dir / "evidence_anchor_repair_report.csv")
    tasks = [
        {
            "task_id": "sqlite_bootstrap",
            "status": "complete",
            "artifact": ".local/ingestion_v03/ingestion.sqlite",
            "note": "Legacy YAML rows are represented in the internal v0.3 state without mutating YAML verification flags.",
        },
        {
            "task_id": "review_packets",
            "status": "complete" if (out_dir / "packets" / "index.csv").exists() else "needs_run",
            "artifact": "analysis/review_queue/packets/index.csv",
            "note": "Machine-prepared review packets only; not human audit.",
        },
        {
            "task_id": "machine_triage_summary",
            "status": "complete" if (out_dir / "v0_3_review_triage_summary.json").exists() else "needs_run",
            "artifact": "analysis/review_queue/v0_3_review_triage_summary.json",
            "note": "Separates machine-ready, machine-repaired, and still-blocked rows.",
        },
        {
            "task_id": "human_audit_worksheet_preparation",
            "status": "complete" if (out_dir / "human_audit_worksheet.csv").exists() else "needs_run",
            "artifact": "analysis/review_queue/human_audit_worksheet.csv",
            "note": f"Prepared {len(ready_for_human)} blank rows for future human audit; no audit result recorded.",
        },
        {
            "task_id": "evidence_repair_plan",
            "status": "complete" if (out_dir / "evidence_repair_plan.csv").exists() else "needs_run",
            "artifact": "analysis/review_queue/evidence_repair_plan.csv",
            "note": f"Current machine blocker rows: {len(source_discovery_rows)}.",
        },
        {
            "task_id": "existing_url_anchor_capture",
            "status": "complete" if capture_counts else "needs_run",
            "artifact": "analysis/review_queue/evidence_anchor_repair_report.csv",
            "note": "Direct body_hash/body_path capture attempted for existing URL-bearing missing anchors.",
            "status_counts": capture_counts,
        },
        {
            "task_id": "source_discovery_worklist",
            "status": "complete" if (out_dir / "source_discovery_worklist.csv").exists() else "needs_run",
            "artifact": "analysis/review_queue/source_discovery_worklist.csv",
            "note": f"{len(source_discovery_rows)} rows still need source discovery or methodology repair before they can enter the human worksheet.",
        },
        {
            "task_id": "human_primary_source_audit",
            "status": "excluded_from_this_request",
            "artifact": "analysis/review_queue/human_audit_worksheet.csv",
            "note": "Requires real human confirmation; not performed by this workflow.",
        },
    ]
    payload = {
        "generated_at": utc_now(),
        "report_kind": "v0.3_non_human_todo_list",
        "human_audit_performed": False,
        "primary_source_verified_mutated": False,
        "total_queue_items": len(rows),
        "ready_for_future_human_audit": len(ready_for_human),
        "remaining_source_discovery_rows": len(source_discovery_rows),
        "source_discovery_worklist_rows": _csv_row_count(out_dir / "source_discovery_worklist.csv"),
        "tasks": tasks,
    }
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    lines = [
        "# v0.3 Non-Human Todo List",
        "",
        "Scope: complete machine/infrastructure work and leave real human audit untouched.",
        "",
        f"- Queue rows: {len(rows)}",
        f"- Ready for future human audit: {len(ready_for_human)}",
        f"- Still requiring source discovery or methodology repair: {len(source_discovery_rows)}",
        "- Human audit performed here: `false`",
        "- `primary_source_verified` mutated here: `false`",
        "",
        "| Task | Status | Artifact | Note |",
        "| --- | --- | --- | --- |",
    ]
    for task in tasks:
        note = str(task["note"]).replace("|", "\\|")
        lines.append(
            f"| `{task['task_id']}` | `{task['status']}` | `{task['artifact']}` | {note} |"
        )
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "Rows in the human worksheet are ready only for future human confirmation. Rows in the source-discovery worklist still need primary observation evidence or a documented methodology decision before they should be offered to a human auditor as confirmable cases.",
        ]
    )
    md_path.write_text("\n".join(lines) + "\n")
    return {"json": json_path, "md": md_path}


def record_source_failure(
    conn: sqlite3.Connection,
    *,
    name: str,
    kind: str,
    url: str | None,
    error: str,
    language: str | None = None,
    schedule: str | None = None,
) -> int:
    now = utc_now()
    key = _source_key(url, name)
    conn.execute(
        """
        INSERT INTO sources (
            source_key, name, kind, url, language, schedule, failure_count,
            last_failure_at, created_at, updated_at, metadata_json
        )
        VALUES (?, ?, ?, ?, ?, ?, 1, ?, ?, ?, ?)
        ON CONFLICT(source_key) DO UPDATE SET
            failure_count=sources.failure_count + 1,
            last_failure_at=excluded.last_failure_at,
            updated_at=excluded.updated_at,
            metadata_json=excluded.metadata_json
        """,
        (key, name, kind, url, language, schedule, now, now, now, json_dumps({"last_error": error})),
    )
    row = conn.execute("SELECT source_id FROM sources WHERE source_key = ?", (key,)).fetchone()
    source_id = int(row["source_id"])
    apply_source_death_policy(conn, source_id=source_id)
    return source_id


def apply_source_death_policy(conn: sqlite3.Connection, *, source_id: int) -> None:
    row = conn.execute("SELECT * FROM sources WHERE source_id = ?", (source_id,)).fetchone()
    if row is None or row["deprecated_at"]:
        return
    last_success = row["last_success_at"] or row["first_success_at"] or row["created_at"]
    try:
        last_success_dt = datetime.fromisoformat(str(last_success).replace("Z", "+00:00"))
    except ValueError:
        return
    if datetime.now(timezone.utc) - last_success_dt >= timedelta(days=30):
        now = utc_now()
        conn.execute(
            "UPDATE sources SET deprecated_at = ?, updated_at = ? WHERE source_id = ?",
            (now, now, source_id),
        )


def ofac_canary_status(db_path: Path = DEFAULT_DB_PATH) -> dict[str, Any]:
    init_db(db_path)
    with connect(db_path) as conn:
        source = conn.execute(
            "SELECT * FROM sources WHERE kind = 'ofac_sdn_xml' ORDER BY source_id DESC LIMIT 1"
        ).fetchone()
        pending = conn.execute(
            """
            SELECT COUNT(*) FROM review_queue
            WHERE status = 'pending'
              AND payload_json LIKE '%ofac_sdn_daily_canary%'
            """
        ).fetchone()[0]
        candidates = conn.execute(
            "SELECT COUNT(*) FROM events WHERE pipeline = 'ofac_sdn_daily_canary'"
        ).fetchone()[0]
        report: dict[str, Any] = {
            "generated_at": utc_now(),
            "pipeline": "ofac_sdn_daily_canary",
            "candidate_count": candidates,
            "pending_review_count": pending,
            "clean_run_ready": False,
            "reason": "OFAC SDN canary has not run yet.",
        }
        if source is None:
            return report
        row = dict(source)
        report["source"] = {
            "source_key": row["source_key"],
            "first_success_at": row["first_success_at"],
            "last_success_at": row["last_success_at"],
            "failure_count": row["failure_count"],
            "last_failure_at": row["last_failure_at"],
            "deprecated_at": row["deprecated_at"],
        }
        first_success = row["first_success_at"]
        if not first_success:
            report["reason"] = "OFAC SDN source has no successful run timestamp."
            return report
        first_dt = datetime.fromisoformat(str(first_success).replace("Z", "+00:00"))
        clean_days = (datetime.now(timezone.utc) - first_dt).total_seconds() / 86400
        report["clean_days_since_first_success"] = round(clean_days, 3)
        if row["failure_count"]:
            report["reason"] = "OFAC SDN source has recorded failures; inspect source health before opening issuer worker."
        elif pending:
            report["reason"] = "OFAC SDN canary has pending review queue items."
        elif clean_days < 7:
            report["reason"] = "OFAC SDN canary has not accumulated 7 clean days yet."
        else:
            report["clean_run_ready"] = True
            report["reason"] = "OFAC SDN canary has at least 7 clean days, no recorded failures, and no pending queue items."
        return report


def _ratio(numerator: int, denominator: int) -> float | None:
    if denominator == 0:
        return None
    return round(numerator / denominator, 6)


def _days_since(timestamp: str | None) -> float | None:
    if not timestamp:
        return None
    try:
        dt = datetime.fromisoformat(str(timestamp).replace("Z", "+00:00"))
    except ValueError:
        return None
    return round((datetime.now(timezone.utc) - dt).total_seconds() / 86400, 3)


def build_ingestion_report(db_path: Path = DEFAULT_DB_PATH) -> dict[str, Any]:
    """Build the v0.3 operating report.

    This is a maintainer-facing monitor report. It summarizes internal
    candidates, source health, and review throughput; it is not a paper table
    and must not be used as a denominator for claims.
    """
    init_db(db_path)
    status = ingestion_status_report(db_path)
    ofac_status = ofac_canary_status(db_path)
    with connect(db_path) as conn:
        def count_by(query: str) -> dict[str, int]:
            return {str(row[0] or "unknown"): int(row[1]) for row in conn.execute(query)}

        total_events = int(conn.execute("SELECT COUNT(*) FROM events").fetchone()[0])
        candidate_count = int(
            conn.execute("SELECT COUNT(*) FROM events WHERE internal_status = 'candidate'").fetchone()[0]
        )
        verified_count = int(
            conn.execute("SELECT COUNT(*) FROM events WHERE internal_status = 'verified'").fetchone()[0]
        )
        legacy_draft_count = int(
            conn.execute(
                "SELECT COUNT(*) FROM events WHERE verification_state = 'legacy_draft_requires_reextraction'"
            ).fetchone()[0]
        )
        clustered_events = int(
            conn.execute("SELECT COUNT(*) FROM events WHERE same_event_cluster_id IS NOT NULL").fetchone()[0]
        )
        cluster_count = int(conn.execute("SELECT COUNT(*) FROM event_clusters").fetchone()[0])
        merge_decisions = int(
            conn.execute(
                "SELECT COUNT(*) FROM event_clusters WHERE merge_decision_reason IS NOT NULL"
            ).fetchone()[0]
        )
        source_rows = [
            dict(row)
            for row in conn.execute(
                """
                SELECT s.source_id, s.source_key, s.name, s.kind, s.language, s.schedule,
                       s.failure_count, s.first_success_at, s.last_success_at,
                       s.last_failure_at, s.deprecated_at,
                       COUNT(rd.raw_document_id) AS successful_snapshots
                FROM sources s
                LEFT JOIN raw_documents rd ON rd.source_id = s.source_id
                GROUP BY s.source_id
                ORDER BY s.kind, s.name
                """
            )
        ]
        sources = []
        for row in source_rows:
            success_count = int(row["successful_snapshots"] or 0)
            failure_count = int(row["failure_count"] or 0)
            sources.append(
                {
                    "source_key": row["source_key"],
                    "name": row["name"],
                    "kind": row["kind"],
                    "language": row["language"],
                    "schedule": row["schedule"],
                    "successful_snapshots": success_count,
                    "failure_count": failure_count,
                    "parser_failure_rate": _ratio(failure_count, success_count + failure_count),
                    "first_success_at": row["first_success_at"],
                    "last_success_at": row["last_success_at"],
                    "days_since_success": _days_since(row["last_success_at"]),
                    "last_failure_at": row["last_failure_at"],
                    "deprecated_at": row["deprecated_at"],
                    "needs_attention": bool(
                        row["deprecated_at"] or failure_count >= 3 or row["last_success_at"] is None
                    ),
                }
            )
        review_decisions = count_by(
            "SELECT action, COUNT(*) FROM audit_log GROUP BY action"
        )
        language_counts = count_by(
            """
            SELECT COALESCE(source_language, 'unknown'), COUNT(*)
            FROM event_evidence
            GROUP BY COALESCE(source_language, 'unknown')
            """
        )
        jurisdiction_counts = count_by(
            """
            SELECT COALESCE(NULLIF(jurisdiction_scope, ''), 'unknown'), COUNT(*)
            FROM events
            GROUP BY COALESCE(NULLIF(jurisdiction_scope, ''), 'unknown')
            """
        )

    return {
        "generated_at": utc_now(),
        "report_kind": "v0.3_ingestion_operating_report",
        "paper_denominator": False,
        "summary": {
            "event_count": total_events,
            "candidate_count": candidate_count,
            "verified_count": verified_count,
            "candidate_to_verified_ratio": _ratio(candidate_count, verified_count),
            "verified_share": _ratio(verified_count, total_events),
            "primary_source_verified_count": status["events"]["primary_source_verified"],
            "requires_v0_3_reextraction": status["events"]["requires_v0_3_reextraction"],
            "legacy_draft_count": legacy_draft_count,
            "pending_review_count": status["review_queue"]["by_status"].get("pending", 0),
        },
        "events": status["events"],
        "review_queue": status["review_queue"],
        "source_freshness": {
            "source_count": len(sources),
            "needs_attention_count": sum(1 for row in sources if row["needs_attention"]),
            "sources": sources,
        },
        "parser_health": {
            "failure_alerts": status["sources"]["failure_alerts"],
            "sources_with_failures": sum(1 for row in sources if row["failure_count"]),
        },
        "entity_resolution": {
            "cluster_count": cluster_count,
            "clustered_event_count": clustered_events,
            "merge_decision_count": merge_decisions,
            "duplicate_merge_rate": _ratio(clustered_events, total_events),
            "training_set_status": "template_only_until_human_labels_added",
        },
        "coverage": {
            "evidence_language_counts": language_counts,
            "jurisdiction_scope_counts": jurisdiction_counts,
        },
        "ofac_canary": ofac_status,
        "audit_log": {
            "actions": review_decisions,
        },
    }


def render_ingestion_report_md(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# v0.3 Ingestion Operating Report",
        "",
        f"Generated: `{report['generated_at']}`",
        "",
        "This report summarizes internal ingestion state. It is not a paper denominator.",
        "",
        "## Summary",
        "",
        "| Metric | Value |",
        "| --- | ---: |",
        f"| Events in local ingestion state | {summary['event_count']} |",
        f"| Candidates | {summary['candidate_count']} |",
        f"| Verified internal rows | {summary['verified_count']} |",
        f"| Candidate / verified ratio | {summary['candidate_to_verified_ratio']} |",
        f"| Primary-source verified rows | {summary['primary_source_verified_count']} |",
        f"| Rows requiring v0.3 re-extraction | {summary['requires_v0_3_reextraction']} |",
        f"| Legacy draft rows | {summary['legacy_draft_count']} |",
        f"| Pending review items | {summary['pending_review_count']} |",
        "",
        "## Sources",
        "",
        "| Source | Kind | Schedule | Snapshots | Failures | Failure rate | Days since success | Attention |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in report["source_freshness"]["sources"]:
        lines.append(
            f"| {row['name']} | `{row['kind']}` | `{row.get('schedule') or ''}` | "
            f"{row['successful_snapshots']} | {row['failure_count']} | "
            f"{row['parser_failure_rate']} | {row['days_since_success']} | "
            f"{'yes' if row['needs_attention'] else 'no'} |"
        )
    lines.extend(
        [
            "",
            "## Entity Resolution",
            "",
            "| Metric | Value |",
            "| --- | ---: |",
            f"| Clusters | {report['entity_resolution']['cluster_count']} |",
            f"| Clustered events | {report['entity_resolution']['clustered_event_count']} |",
            f"| Merge decisions | {report['entity_resolution']['merge_decision_count']} |",
            f"| Duplicate / merge rate | {report['entity_resolution']['duplicate_merge_rate']} |",
            "",
            "## OFAC Canary",
            "",
            f"- Clean-run ready: `{report['ofac_canary']['clean_run_ready']}`",
            f"- Reason: {report['ofac_canary']['reason']}",
            f"- Candidate count: {report['ofac_canary']['candidate_count']}",
            f"- Pending review count: {report['ofac_canary']['pending_review_count']}",
            "",
            "## Coverage",
            "",
            "### Evidence Languages",
            "",
            "| Language | Evidence rows |",
            "| --- | ---: |",
        ]
    )
    for language, count in sorted(report["coverage"]["evidence_language_counts"].items()):
        lines.append(f"| `{language}` | {count} |")
    lines.extend(["", "### Jurisdiction Scope", "", "| Scope | Events |", "| --- | ---: |"])
    for scope, count in sorted(report["coverage"]["jurisdiction_scope_counts"].items()):
        lines.append(f"| `{scope}` | {count} |")
    return "\n".join(lines) + "\n"


def write_ingestion_report(
    *,
    db_path: Path = DEFAULT_DB_PATH,
    out_dir: Path = REPO_ROOT / "analysis" / "ingestion_reports",
) -> dict[str, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    report = build_ingestion_report(db_path)
    json_path = out_dir / "v0_3_operating_report.json"
    md_path = out_dir / "v0_3_operating_report.md"
    json_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    md_path.write_text(render_ingestion_report_md(report))
    return {"json": json_path, "md": md_path}


def write_er_training_set_template(
    *,
    out_path: Path = REPO_ROOT / "analysis" / "inter_rater" / "er_training_set.template.csv",
) -> Path:
    """Write a blank ER training-set worksheet.

    Phase 0B needs human-labeled difficult pairs. This template deliberately
    contains no labels so it cannot be mistaken for a completed evaluation set.
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "pair_id",
        "event_id_a",
        "event_id_b",
        "candidate_relation",
        "label",
        "labeler",
        "evidence_ids",
        "reason",
        "notes",
    ]
    with out_path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
    return out_path


def next_review_item(db_path: Path = DEFAULT_DB_PATH) -> dict[str, Any] | None:
    init_db(db_path)
    with connect(db_path) as conn:
        row = conn.execute(
            """
            SELECT * FROM review_queue
            WHERE status = 'pending'
            ORDER BY priority ASC, created_at ASC, queue_id ASC
            LIMIT 1
            """
        ).fetchone()
        if row is None:
            return None
        return dict(row)


def resolve_review_item(
    *,
    db_path: Path = DEFAULT_DB_PATH,
    queue_id: int,
    decision: str,
    actor: str,
    reason: str,
    new_event_status: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    init_db(db_path)
    if decision not in {"resolved", "needs_recheck", "deferred"}:
        raise ValueError("decision must be one of: resolved, needs_recheck, deferred")
    if new_event_status is not None and new_event_status not in {"candidate", "verified", "superseded", "retracted"}:
        raise ValueError("new_event_status must be candidate, verified, superseded, or retracted")

    with connect(db_path) as conn:
        row = conn.execute("SELECT * FROM review_queue WHERE queue_id = ?", (queue_id,)).fetchone()
        if row is None:
            raise KeyError(f"review queue item {queue_id} not found")
        previous_queue = dict(row)
        now = utc_now()
        conn.execute(
            """
            UPDATE review_queue
            SET status = ?, updated_at = ?, resolved_at = CASE WHEN ? = 'deferred' THEN NULL ELSE ? END
            WHERE queue_id = ?
            """,
            (decision, now, decision, now, queue_id),
        )

        item_type = str(row["item_type"])
        item_id = str(row["item_id"])
        previous_event: dict[str, Any] | None = None
        new_event: dict[str, Any] | None = None
        if item_type == "event" and new_event_status is not None:
            event_row = conn.execute("SELECT * FROM events WHERE event_id = ?", (item_id,)).fetchone()
            previous_event = dict(event_row) if event_row is not None else None
            conn.execute(
                """
                UPDATE events
                SET internal_status = ?,
                    primary_source_verified = CASE WHEN ? = 'verified' THEN 1 ELSE primary_source_verified END,
                    requires_v0_3_reextraction = CASE WHEN ? = 'verified' THEN 0 ELSE requires_v0_3_reextraction END,
                    verification_state = CASE WHEN ? = 'verified' THEN 'primary_source_verified' ELSE verification_state END,
                    last_pipeline_stage = 'human_review_decision',
                    updated_at = ?
                WHERE event_id = ?
                """,
                (new_event_status, new_event_status, new_event_status, new_event_status, now, item_id),
            )
            event_row = conn.execute("SELECT * FROM events WHERE event_id = ?", (item_id,)).fetchone()
            new_event = dict(event_row) if event_row is not None else None

        new_queue = dict(conn.execute("SELECT * FROM review_queue WHERE queue_id = ?", (queue_id,)).fetchone())
        conn.execute(
            """
            INSERT INTO audit_log (
                timestamp, actor, action, object_type, object_id,
                previous_state_json, new_state_json, reason, metadata_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                now,
                actor,
                "review_decision",
                item_type,
                item_id,
                json_dumps({"queue": previous_queue, "event": previous_event}),
                json_dumps({"queue": new_queue, "event": new_event}),
                reason,
                json_dumps(metadata),
            ),
        )
        return {"queue": new_queue, "event": new_event}


def internal_event_to_yaml(event_row: sqlite3.Row | dict[str, Any]) -> dict[str, Any]:
    row = dict(event_row)
    payload = json.loads(row.get("payload_json") or "{}")
    yaml_event = dict(payload.get("yaml_event") or {})
    yaml_event.setdefault("id", row["canonical_slug"])
    yaml_event.setdefault("schema_version", "0.2.0")
    yaml_event["status"] = {
        "candidate": "draft",
        "verified": "admitted",
        "superseded": "rejected",
        "retracted": "rejected",
    }[row["internal_status"]]
    yaml_event["codebook_version"] = row.get("codebook_version") or CODEBOOK_VERSION
    yaml_event["primary_source_verified"] = bool(row.get("primary_source_verified"))
    yaml_event.setdefault("origin", "agent_draft" if row["internal_status"] == "candidate" else "human_reviewed")
    yaml_event.setdefault("analysis_use", row.get("analysis_use"))
    if row.get("trigger_type") and "trigger" not in yaml_event:
        yaml_event["trigger"] = {
            "type": row["trigger_type"],
            "actor": row.get("actor"),
            "timestamp": f"{row.get('event_date') or '1970-01-01'}T00:00:00Z",
            "timestamp_precision": "day",
            "citation": [],
        }
    yaml_event.pop("requires_v0_3_reextraction", None)
    yaml_event.pop("verification_state", None)
    yaml_event.pop("last_pipeline_stage", None)
    yaml_event.pop("last_review_queue_item_id", None)
    yaml_event.pop("_source_file", None)
    return {key: value for key, value in yaml_event.items() if value is not None}


def export_event_yaml(db_path: Path, event_id: str) -> str:
    init_db(db_path)
    with connect(db_path) as conn:
        row = conn.execute("SELECT * FROM events WHERE event_id = ?", (event_id,)).fetchone()
        if row is None:
            raise KeyError(f"event {event_id} not found")
        return yaml.safe_dump(internal_event_to_yaml(row), sort_keys=False, allow_unicode=False)


def archive_audit_log(
    *,
    db_path: Path = DEFAULT_DB_PATH,
    archive_dir: Path = REPO_ROOT / "analysis" / "audit_log_archive",
    older_than_days: int = 90,
    delete_after_archive: bool = True,
) -> Path | None:
    init_db(db_path)
    cutoff = datetime.now(timezone.utc) - timedelta(days=older_than_days)
    cutoff_text = cutoff.replace(microsecond=0).isoformat().replace("+00:00", "Z")
    with connect(db_path) as conn:
        rows = [
            dict(row)
            for row in conn.execute(
                "SELECT * FROM audit_log WHERE timestamp < ? ORDER BY timestamp, audit_id",
                (cutoff_text,),
            )
        ]
        if not rows:
            return None
        archive_dir.mkdir(parents=True, exist_ok=True)
        archive_path = archive_dir / f"audit_log_archive_{cutoff.date().isoformat()}.jsonl"
        archive_path.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows))
        if delete_after_archive:
            conn.execute("DELETE FROM audit_log WHERE timestamp < ?", (cutoff_text,))
        return archive_path


def _read_optional_bytes(path: str | None) -> bytes | None:
    if not path:
        return None
    return Path(path).read_bytes()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="v0.3 ingestion substrate CLI")
    parser.add_argument("--db", default=str(DEFAULT_DB_PATH))
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init-db", help="create or migrate the local ingestion SQLite DB")

    registry = sub.add_parser("register-sources", help="register ingestion sources without marking fetch success")
    registry.add_argument("--source-registry", default=str(DEFAULT_SOURCE_REGISTRY))

    bootstrap = sub.add_parser("bootstrap-legacy", help="bootstrap events/*.yaml into local SQLite state")
    bootstrap.add_argument("--events-dir", default=str(REPO_ROOT / "events"))
    bootstrap.add_argument(
        "--enqueue-reextraction",
        action="store_true",
        help="enqueue legacy rows that still need v0.3 primary-source re-extraction",
    )

    snap = sub.add_parser("snapshot", help="snapshot a local raw document into the hash store")
    snap.add_argument("--input", required=True, help="local file to snapshot")
    snap.add_argument("--source-url")
    snap.add_argument("--source-name", required=True)
    snap.add_argument("--source-kind", required=True)
    snap.add_argument("--content-type")

    ofac = sub.add_parser("ofac-canary", help="run the OFAC SDN canary on local or fetched XML")
    ofac.add_argument("--current-xml", help="local current SDN XML file; fetches live OFAC XML when omitted")
    ofac.add_argument("--previous-xml", help="optional previous SDN XML file for diff")
    ofac.add_argument("--dry-run", action="store_true")
    ofac.add_argument(
        "--compare-empty",
        action="store_true",
        help="treat missing prior snapshot as an empty list; default first run creates a no-candidate baseline",
    )
    ofac.add_argument("--source-registry", default=str(DEFAULT_SOURCE_REGISTRY))

    status = sub.add_parser("status-report", help="print local ingestion status as JSON")
    status.add_argument("--out", help="optional JSON output path")

    queue_export = sub.add_parser("export-review-queue", help="export review queue JSON/CSV/MD")
    queue_export.add_argument("--out-dir", default=str(REPO_ROOT / "analysis" / "review_queue"))

    review_packets = sub.add_parser("review-packets", help="write per-item v0.3 human review packets")
    review_packets.add_argument("--out-dir", default=str(REPO_ROOT / "analysis" / "review_queue" / "packets"))
    review_packets.add_argument("--limit", type=int)
    review_packets.add_argument("--include-resolved", action="store_true")

    review_triage = sub.add_parser(
        "review-triage-summary",
        help="write LLM/machine pre-human review triage summary and worklists",
    )
    review_triage.add_argument("--out-dir", default=str(REPO_ROOT / "analysis" / "review_queue"))

    human_audit = sub.add_parser(
        "human-audit-worksheet",
        help="write blank human-audit worksheet and decision templates for pending rows",
    )
    human_audit.add_argument("--out-dir", default=str(REPO_ROOT / "analysis" / "review_queue"))

    repair_plan = sub.add_parser(
        "evidence-repair-plan",
        help="write repair plan for LLM/machine flagged pre-human rows",
    )
    repair_plan.add_argument("--out-dir", default=str(REPO_ROOT / "analysis" / "review_queue"))

    source_worklist = sub.add_parser(
        "source-discovery-worklist",
        help="write non-human source-discovery worklist for rows still lacking primary observation evidence",
    )
    source_worklist.add_argument("--out-dir", default=str(REPO_ROOT / "analysis" / "review_queue"))
    source_worklist.add_argument("--events-dir", default=str(REPO_ROOT / "events"))

    non_human_todos = sub.add_parser(
        "non-human-todo-list",
        help="write status/todo list for all non-human v0.3 review-queue tasks",
    )
    non_human_todos.add_argument("--out-dir", default=str(REPO_ROOT / "analysis" / "review_queue"))

    ofac_status = sub.add_parser("ofac-canary-status", help="print OFAC canary clean-run status")
    ofac_status.add_argument("--out", help="optional JSON output path")

    ingestion_report = sub.add_parser("ingestion-report", help="write v0.3 ingestion operating report")
    ingestion_report.add_argument("--out-dir", default=str(REPO_ROOT / "analysis" / "ingestion_reports"))

    er_template = sub.add_parser("er-training-template", help="write blank entity-resolution training worksheet")
    er_template.add_argument(
        "--out",
        default=str(REPO_ROOT / "analysis" / "inter_rater" / "er_training_set.template.csv"),
    )

    export = sub.add_parser("export-yaml", help="render one internal event through the YAML mapping")
    export.add_argument("--event-id", required=True)

    archive = sub.add_parser("archive-audit-log", help="archive old audit rows to JSONL")
    archive.add_argument("--older-than-days", type=int, default=90)
    archive.add_argument("--keep-hot-copy", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    db_path = Path(args.db)
    if args.cmd == "init-db":
        init_db(db_path)
        print(f"[ingestion-v03] initialized {db_path}")
        return 0
    if args.cmd == "register-sources":
        result = register_source_registry(
            db_path=db_path,
            registry_path=Path(args.source_registry),
        )
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    if args.cmd == "bootstrap-legacy":
        result = bootstrap_legacy_events(
            db_path=db_path,
            events_dir=Path(args.events_dir),
            enqueue_reextraction=args.enqueue_reextraction,
        )
        print(json.dumps(result.__dict__, indent=2, sort_keys=True))
        return 0
    if args.cmd == "snapshot":
        result = snapshot_raw_document(
            db_path=db_path,
            body=Path(args.input).read_bytes(),
            source_url=args.source_url,
            source_name=args.source_name,
            source_kind=args.source_kind,
            content_type=args.content_type,
        )
        print(json.dumps(result.__dict__ | {"body_path": str(result.body_path), "manifest_path": str(result.manifest_path)}, indent=2))
        return 0
    if args.cmd == "ofac-canary":
        registry_rows = load_source_registry(Path(args.source_registry))
        ofac_source_url = OFAC_SDN_URL
        for row in registry_rows:
            if row.get("kind") == OFAC_SOURCE_KIND:
                ofac_source_url = str(row["url"])
                break
        register_source_registry(
            db_path=db_path,
            registry_path=Path(args.source_registry),
        )
        current = _read_optional_bytes(args.current_xml)
        content_type = None
        if current is None:
            try:
                current, content_type = fetch_url(ofac_source_url)
            except Exception as exc:
                init_db(db_path)
                with connect(db_path) as conn:
                    record_source_failure(
                        conn,
                        name=OFAC_SOURCE_NAME,
                        kind=OFAC_SOURCE_KIND,
                        url=ofac_source_url,
                        language="en",
                        schedule="daily",
                        error=f"{type(exc).__name__}: {exc}",
                    )
                print(f"[ingestion-v03] OFAC fetch failed: {exc}", file=sys.stderr)
                return 2
        previous = _read_optional_bytes(args.previous_xml)
        result = run_ofac_canary_with_prior_snapshot(
            db_path=db_path,
            current_xml=current,
            previous_xml=previous,
            dry_run=args.dry_run,
            compare_empty=args.compare_empty,
            source_url=ofac_source_url,
        )
        print(json.dumps(result.__dict__ | {"content_type": content_type}, indent=2, sort_keys=True))
        return 0
    if args.cmd == "status-report":
        report = ingestion_status_report(db_path)
        text = json.dumps(report, indent=2, sort_keys=True) + "\n"
        if args.out:
            Path(args.out).parent.mkdir(parents=True, exist_ok=True)
            Path(args.out).write_text(text)
        else:
            sys.stdout.write(text)
        return 0
    if args.cmd == "export-review-queue":
        paths = export_review_queue(db_path=db_path, out_dir=Path(args.out_dir))
        print(json.dumps({key: str(path) for key, path in paths.items()}, indent=2, sort_keys=True))
        return 0
    if args.cmd == "review-packets":
        result = write_review_packets(
            db_path=db_path,
            out_dir=Path(args.out_dir),
            limit=args.limit,
            include_resolved=args.include_resolved,
        )
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    if args.cmd == "review-triage-summary":
        paths = write_review_triage_summary(db_path=db_path, out_dir=Path(args.out_dir))
        print(json.dumps({key: str(path) for key, path in paths.items()}, indent=2, sort_keys=True))
        return 0
    if args.cmd == "human-audit-worksheet":
        paths = write_human_audit_worksheet(db_path=db_path, out_dir=Path(args.out_dir))
        print(json.dumps({key: str(path) for key, path in paths.items()}, indent=2, sort_keys=True))
        return 0
    if args.cmd == "evidence-repair-plan":
        paths = write_evidence_repair_plan(db_path=db_path, out_dir=Path(args.out_dir))
        print(json.dumps({key: str(path) for key, path in paths.items()}, indent=2, sort_keys=True))
        return 0
    if args.cmd == "source-discovery-worklist":
        paths = write_source_discovery_worklist(
            db_path=db_path,
            out_dir=Path(args.out_dir),
            events_dir=Path(args.events_dir),
        )
        print(json.dumps({key: str(path) for key, path in paths.items()}, indent=2, sort_keys=True))
        return 0
    if args.cmd == "non-human-todo-list":
        paths = write_non_human_todo_list(db_path=db_path, out_dir=Path(args.out_dir))
        print(json.dumps({key: str(path) for key, path in paths.items()}, indent=2, sort_keys=True))
        return 0
    if args.cmd == "ofac-canary-status":
        report = ofac_canary_status(db_path)
        text = json.dumps(report, indent=2, sort_keys=True) + "\n"
        if args.out:
            Path(args.out).parent.mkdir(parents=True, exist_ok=True)
            Path(args.out).write_text(text)
        else:
            sys.stdout.write(text)
        return 0
    if args.cmd == "ingestion-report":
        paths = write_ingestion_report(db_path=db_path, out_dir=Path(args.out_dir))
        print(json.dumps({key: str(path) for key, path in paths.items()}, indent=2, sort_keys=True))
        return 0
    if args.cmd == "er-training-template":
        path = write_er_training_set_template(out_path=Path(args.out))
        print(f"[ingestion-v03] wrote {path}")
        return 0
    if args.cmd == "export-yaml":
        sys.stdout.write(export_event_yaml(db_path, args.event_id))
        return 0
    if args.cmd == "archive-audit-log":
        path = archive_audit_log(
            db_path=db_path,
            older_than_days=args.older_than_days,
            delete_after_archive=not args.keep_hot_copy,
        )
        print(f"[ingestion-v03] archived to {path}" if path else "[ingestion-v03] no old audit rows")
        return 0
    raise AssertionError(args.cmd)


if __name__ == "__main__":
    raise SystemExit(main())
