#!/usr/bin/env python3
"""Validate event YAML files against the repo's methodology rules.

This validator intentionally avoids non-stdlib dependencies except PyYAML,
because the current workspace does not have jsonschema installed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
VOCAB_PATH = REPO_ROOT / "schema" / "controlled_vocab.yaml"
SCHEMA_PATH = REPO_ROOT / "schema" / "event.schema.json"
EVENTS_DIR = REPO_ROOT / "events"
PLACEHOLDER_MARKERS = (
    "placeholder",
    "replace",
    "fill in",
    "example.org",
    "example_actor",
    "example_target",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate event YAML files.")
    parser.add_argument(
        "paths",
        nargs="*",
        help="Event YAML paths. Defaults to all YAML files under events/.",
    )
    parser.add_argument(
        "--check-citations",
        action="store_true",
        help="Attempt lightweight URL reachability checks for citations.",
    )
    parser.add_argument(
        "--check-archives",
        action="store_true",
        help=(
            "For each source: re-verify body_hash against the local file at body_path, "
            "and HEAD-check every wayback URL. CI-time archival rot detector."
        ),
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="Timeout in seconds for network checks.",
    )
    return parser.parse_args()


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text())


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def parse_iso8601(value: str) -> bool:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False


def parse_datetime(value: str) -> datetime | None:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def is_url(value: str) -> bool:
    parsed = urllib.parse.urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def source_is_primary(source_type: str) -> bool:
    return source_type.startswith("primary_")


def source_is_semi_primary(source_type: str) -> bool:
    return source_type.startswith("semi_primary_")


def source_is_supporting(source_type: str) -> bool:
    return source_type.startswith("supporting_")


def iter_citation_like_urls(event: dict[str, Any]) -> list[tuple[str, str]]:
    urls: list[tuple[str, str]] = []

    def walk(node: Any, label: str) -> None:
        if isinstance(node, dict):
            for key in ("url", "wayback"):
                value = node.get(key)
                if isinstance(value, str):
                    urls.append((f"{label}.{key}", value))
            for key, value in node.items():
                walk(value, f"{label}.{key}")
        elif isinstance(node, list):
            for idx, value in enumerate(node):
                walk(value, f"{label}[{idx}]")

    walk(event, "event")
    deduped: dict[str, str] = {}
    for label, url in urls:
        deduped.setdefault(url, label)
    return [(label, url) for url, label in deduped.items()]


def fetch_url_status(url: str, timeout: float) -> tuple[bool, str]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "p1-event-db-validator/0.1"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return True, f"HTTP {resp.status}"
    except urllib.error.HTTPError as exc:
        return False, f"HTTPError {exc.code}"
    except urllib.error.URLError as exc:
        return False, f"URLError {exc.reason}"
    except Exception as exc:  # pragma: no cover - defensive
        return False, f"{type(exc).__name__}: {exc}"


@dataclass
class ValidationResult:
    path: Path
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    @property
    def ok(self) -> bool:
        return not self.errors


class EventValidator:
    def __init__(self, vocab: dict[str, Any]) -> None:
        self.vocab = vocab
        self.layers = set(vocab["layers"])
        self.source_types = set(vocab["source_types"])
        self.coverage_statuses = set(vocab["coverage_statuses"])
        self.observation_kinds = set(vocab["observation_kinds"])
        self.attribution_levels = set(vocab["attribution_levels"])
        self.trigger_types = set(vocab["trigger_types"])
        self.event_classes = set(vocab["event_classes"])
        self.event_statuses = set(vocab["event_statuses"])
        self.precision_levels = set(vocab["precision_levels"])
        self.target_kinds = set(vocab["target_kinds"])
        self.target_enumerations = set(vocab.get("target_enumerations", []))
        self.origins = set(vocab.get("origins", []))

    def validate_event(
        self,
        path: Path,
        event: dict[str, Any],
        check_citations: bool = False,
        check_archives: bool = False,
        timeout: float = 10.0,
    ) -> ValidationResult:
        result = ValidationResult(path)
        if not isinstance(event, dict):
            result.error("Top-level document must be a mapping.")
            return result

        self._validate_top_level(event, result)
        self._validate_trigger(event.get("trigger"), result)
        self._validate_target(event.get("target"), result)
        self._validate_coverage(event.get("coverage"), result)
        self._validate_observations(event, result)
        self._validate_recovery(event.get("recovery"), result)
        self._validate_release_readiness(event, result)

        if check_archives:
            self._check_archive_reachability(event, result, timeout)

        if check_citations:
            self._check_citations(event, result, timeout)

        return result

    def _validate_top_level(self, event: dict[str, Any], result: ValidationResult) -> None:
        required = [
            "id",
            "schema_version",
            "status",
            "research_stratum",
            "empirical_shape",
            "admission_tier",
            "trigger",
            "target",
            "jurisdiction",
            "coverage",
            "observations",
        ]
        for key in required:
            if key not in event:
                result.error(f"Missing required top-level field: {key}")

        if "id" in event and (
            not isinstance(event["id"], str) or not event["id"] or "_" in event["id"]
        ):
            result.error("id must be a non-empty kebab-case string.")
        if event.get("status") not in self.event_statuses:
            result.error(f"status must be one of {sorted(self.event_statuses)}")

        # schema_version pin (P2 fix): reject stale schema tags.
        # Current canonical version is 0.2.0 (split-field schema). Older events
        # still advertising 0.1.0 are stale metadata and MUST be bumped.
        CURRENT_SCHEMA_VERSION = "0.2.0"
        if event.get("schema_version") != CURRENT_SCHEMA_VERSION:
            result.error(
                f"schema_version={event.get('schema_version')!r} is stale; "
                f"expected {CURRENT_SCHEMA_VERSION!r} after the split-field migration. "
                f"Re-run the migration tooling or bump manually."
            )

        # research_stratum / empirical_shape / admission_tier enumeration checks
        valid_strata = {"S1_ofac_sdn", "S2_ofac_removal", "S3_doj_sec_cftc_fiod", "S4_nation_state", "S5_corporate", "S6_supranational"}
        valid_shapes = {"cascade", "comparison", "null_event"}
        valid_tiers = {"anchor_case", "empirical_case", "null_case"}
        if event.get("research_stratum") not in valid_strata:
            result.error(f"research_stratum must be one of {sorted(valid_strata)}")
        if event.get("empirical_shape") not in valid_shapes:
            result.error(f"empirical_shape must be one of {sorted(valid_shapes)}")
        if event.get("admission_tier") not in valid_tiers:
            result.error(f"admission_tier must be one of {sorted(valid_tiers)}")

        # Consistency lint (Action 2): derived fields must match the actual data
        self._check_field_consistency(event, result)
        if "created_at" in event and not parse_iso8601(str(event["created_at"])):
            result.error("created_at must be ISO-8601 date-time.")
        if "last_verified" in event:
            try:
                datetime.strptime(str(event["last_verified"]), "%Y-%m-%d")
            except ValueError:
                result.error("last_verified must be YYYY-MM-DD.")
        jurisdictions = event.get("jurisdiction")
        if not isinstance(jurisdictions, list) or not jurisdictions:
            result.error("jurisdiction must be a non-empty list.")

        origin = event.get("origin")
        if origin is not None and self.origins and origin not in self.origins:
            result.error(f"origin must be one of {sorted(self.origins)} (got {origin!r}).")
        if (
            event.get("status") == "admitted"
            and origin == "agent_draft"
        ):
            result.error("status=admitted is incompatible with origin=agent_draft; promote to human_reviewed first.")

        if "last_human_audit" in event:
            try:
                datetime.strptime(str(event["last_human_audit"]), "%Y-%m-%d")
            except ValueError:
                result.error("last_human_audit must be YYYY-MM-DD.")

    def _check_field_consistency(self, event: dict, result: ValidationResult) -> None:
        """
        Action 2 lint: enforce that empirical_shape / admission_tier / research_stratum
        agree with the underlying observations + trigger.type, and that analysis_notes /
        tags don't contradict the declared fields. Catches the kind of drift the
        reviewer flagged (event_class state_block_event but notes say cascade_event).
        """
        # A) empirical_shape vs observed_change layer count
        obs = event.get("observations") or []
        changed_layers = {o.get("layer") for o in obs if isinstance(o, dict) and o.get("observation_kind") == "observed_change"}
        n_changed = len(changed_layers)
        shape = event.get("empirical_shape")
        if shape == "cascade" and n_changed < 3:
            result.error(f"empirical_shape=cascade but only {n_changed} distinct observed_change layer(s); need ≥3.")
        if shape == "comparison" and not (1 <= n_changed <= 2):
            result.error(f"empirical_shape=comparison but {n_changed} observed_change layer(s); need 1–2.")
        if shape == "null_event" and n_changed != 0:
            result.error(f"empirical_shape=null_event but {n_changed} observed_change layer(s) present.")

        # B) admission_tier vs attribution strength of changed layers
        strong = {o.get("layer") for o in obs
                  if isinstance(o, dict) and o.get("observation_kind") == "observed_change"
                  and o.get("attribution") in ("direct", "plausible")}
        tier = event.get("admission_tier")
        if tier == "anchor_case" and len(strong) < 2:
            result.error(f"admission_tier=anchor_case requires ≥2 observed_change layers with attribution in {{direct, plausible}}; have {len(strong)}.")
        if tier == "empirical_case" and len(strong) < 1:
            result.error(f"admission_tier=empirical_case requires ≥1 strong-attribution observed_change layer; have {len(strong)}.")
        if tier == "null_case" and len(strong) >= 1:
            result.error(f"admission_tier=null_case but {len(strong)} strong-attribution observed_change layer(s) exist; should be anchor_case or empirical_case.")

        # C) research_stratum vs trigger.type (complete map per schema 0.2.0)
        t = (event.get("trigger") or {}).get("type", "")
        expected_stratum = {
            "ofac_sdn_designation": "S1_ofac_sdn",
            "ofac_sdn_removal": "S2_ofac_removal",
            "doj_indictment": "S3_doj_sec_cftc_fiod",
            "doj_seizure_order": "S3_doj_sec_cftc_fiod",
            "sec_action": "S3_doj_sec_cftc_fiod",
            "cftc_action": "S3_doj_sec_cftc_fiod",
            "court_civil_order": "S3_doj_sec_cftc_fiod",
            "nation_state_block": "S4_nation_state",
            "non_us_sanctions": "S6_supranational",
            "supranational_regulation": "S6_supranational",
            "corporate_policy_change": "S5_corporate",
        }.get(t)
        if expected_stratum and event.get("research_stratum") != expected_stratum:
            result.error(f"research_stratum={event.get('research_stratum')} inconsistent with trigger.type={t} (expected {expected_stratum}).")

        # C2) trigger.actor vs trigger.type coherence check.
        # This is the fix for reviewer P1-B: previously you could write type=doj_indictment
        # with actor=US_SEC and the validator would wave it through.
        actor = (event.get("trigger") or {}).get("actor", "") or ""
        actor_upper = actor.upper()
        actor_type_rules = [
            # (actor substring, required trigger.type value, human label)
            ("US_SEC", "sec_action", "US_SEC requires trigger.type=sec_action"),
            ("US_CFTC", "cftc_action", "US_CFTC requires trigger.type=cftc_action"),
            ("US_DOJ", ("doj_indictment", "doj_seizure_order"), "US_DOJ requires trigger.type ∈ {doj_indictment, doj_seizure_order}"),
            ("US_OFAC", ("ofac_sdn_designation", "ofac_sdn_removal"), "US_OFAC requires trigger.type ∈ {ofac_sdn_designation, ofac_sdn_removal}"),
            ("EU_COUNCIL", ("non_us_sanctions", "supranational_regulation"), "EU_Council requires trigger.type ∈ {non_us_sanctions, supranational_regulation}"),
        ]
        for needle, allowed, msg in actor_type_rules:
            if needle in actor_upper:
                allowed_set = allowed if isinstance(allowed, tuple) else (allowed,)
                if t not in allowed_set:
                    result.error(f"trigger.actor={actor} + trigger.type={t} violates actor/type coherence: {msg}.")
                break  # only match first rule
        # Multi-framework exceptions (binance-4framework-2023 carries DOJ+FinCEN+OFAC+CFTC).
        # Allowed: if actor contains both DOJ and another agency name, skip the strict check above.
        # (Implemented via the `break` above — the DOJ rule fires and accepts doj_indictment for
        #  multi-agency resolutions because those DO carry DOJ as the primary prosecutor.)

        # D) analysis_notes / tags must not mention legacy event_class words at all
        # (event_class was deprecated in schema 0.2.0; any surviving mention is stale).
        # Reviewer P3 2026-04-22: lint must be case-insensitive so capitalized
        # variants (e.g. "State_block_event" in a title-case sentence start) are
        # caught.
        notes = str(event.get("analysis_notes") or "")
        notes_lower = notes.lower()
        tags = [t.lower() for t in (event.get("tags") or [])]
        legacy_class_words = ["state_block_event", "cascade_event", "comparison_event"]
        for word in legacy_class_words:
            if word in notes_lower:
                result.warn(f"analysis_notes mentions deprecated event_class term '{word}' (case-insensitive); replace with the current empirical_shape wording.")
            if word in tags:
                result.warn(f"tags include deprecated event_class term '{word}'; remove.")

        # E) status=admitted must not have 'will upgrade from draft' / 'still a draft' language
        if event.get("status") == "admitted":
            stale_admit_markers = ["will upgrade from draft", "still a draft", "maintaining as draft", "pending admission"]
            lowered = notes.lower()
            for m in stale_admit_markers:
                if m in lowered:
                    result.warn(f"status=admitted but analysis_notes contains stale-draft language '{m}'.")

    def _validate_trigger(self, trigger: Any, result: ValidationResult) -> None:
        if not isinstance(trigger, dict):
            result.error("trigger must be a mapping.")
            return
        for key in ("type", "actor", "timestamp", "timestamp_precision", "citation"):
            if key not in trigger:
                result.error(f"trigger missing required field: {key}")
        if trigger.get("type") not in self.trigger_types:
            result.error(f"trigger.type must be one of {sorted(self.trigger_types)}")
        if "timestamp" in trigger and not parse_iso8601(str(trigger["timestamp"])):
            result.error("trigger.timestamp must be ISO-8601 date-time.")
        if trigger.get("timestamp_precision") not in self.precision_levels:
            result.error(
                f"trigger.timestamp_precision must be one of {sorted(self.precision_levels)}"
            )
        if not isinstance(trigger.get("citation"), list) or not trigger["citation"]:
            result.error("trigger.citation must be a non-empty list.")

    def _validate_target(self, target: Any, result: ValidationResult) -> None:
        if not isinstance(target, dict):
            result.error("target must be a mapping.")
            return
        if target.get("kind") not in self.target_kinds:
            result.error(f"target.kind must be one of {sorted(self.target_kinds)}")
        if target.get("kind") == "address_set" and not target.get("addresses"):
            result.error("target.kind=address_set requires target.addresses.")
        enumeration = target.get("enumeration")
        if enumeration is not None and enumeration not in self.target_enumerations:
            result.error(
                f"target.enumeration must be one of {sorted(self.target_enumerations)} (got {enumeration!r})."
            )

    def _validate_coverage(self, coverage: Any, result: ValidationResult) -> None:
        if not isinstance(coverage, list):
            result.error("coverage must be a list.")
            return
        seen_layers: set[str] = set()
        for idx, entry in enumerate(coverage):
            if not isinstance(entry, dict):
                result.error(f"coverage[{idx}] must be a mapping.")
                continue
            layer = entry.get("layer")
            status = entry.get("status")
            if layer not in self.layers:
                result.error(f"coverage[{idx}].layer must be one of {sorted(self.layers)}")
            if status not in self.coverage_statuses:
                result.error(
                    f"coverage[{idx}].status must be one of {sorted(self.coverage_statuses)}"
                )
            if layer in seen_layers:
                result.error(f"coverage contains duplicate layer entry: {layer}")
            if isinstance(layer, str):
                seen_layers.add(layer)

        missing = self.layers - seen_layers
        for layer in sorted(missing):
            result.error(f"coverage missing required layer entry: {layer}")

    def _validate_observations(self, event: dict[str, Any], result: ValidationResult) -> None:
        observations = event.get("observations")
        if not isinstance(observations, list):
            result.error("observations must be a list (may be empty only on draft events).")
            return
        if not observations and event.get("status") != "draft":
            result.error("observations must be a non-empty list on non-draft events.")
            return
        if not observations:
            return

        coverage_by_layer = {
            entry["layer"]: entry["status"]
            for entry in event.get("coverage", [])
            if isinstance(entry, dict) and "layer" in entry and "status" in entry
        }
        changed_layers: set[str] = set()
        trigger_timestamp = parse_datetime(str(event.get("trigger", {}).get("timestamp", "")))
        seen_observations: set[tuple[str, str, str, str]] = set()

        for idx, obs in enumerate(observations):
            if not isinstance(obs, dict):
                result.error(f"observations[{idx}] must be a mapping.")
                continue

            for key in ("layer", "actor", "event", "observation_kind", "attribution", "sources"):
                if key not in obs:
                    result.error(f"observations[{idx}] missing required field: {key}")

            layer = obs.get("layer")
            kind = obs.get("observation_kind")
            attribution = obs.get("attribution")
            sources = obs.get("sources")

            if layer not in self.layers:
                result.error(f"observations[{idx}].layer must be one of {sorted(self.layers)}")
            if kind not in self.observation_kinds:
                result.error(
                    f"observations[{idx}].observation_kind must be one of {sorted(self.observation_kinds)}"
                )
            if attribution not in self.attribution_levels:
                result.error(
                    f"observations[{idx}].attribution must be one of {sorted(self.attribution_levels)}"
                )
            if "timestamp" in obs and not parse_iso8601(str(obs["timestamp"])):
                result.error(f"observations[{idx}].timestamp must be ISO-8601 date-time.")
            if "precision" in obs and obs["precision"] not in self.precision_levels:
                result.error(
                    f"observations[{idx}].precision must be one of {sorted(self.precision_levels)}"
                )
            if "timestamp_range" in obs:
                self._validate_time_range(
                    obs["timestamp_range"],
                    f"observations[{idx}].timestamp_range",
                    result,
                )
            if "window" in obs:
                self._validate_time_range(obs["window"], f"observations[{idx}].window", result)

            status = coverage_by_layer.get(layer)
            if kind in {"observed_change", "observed_no_change"} and status not in {
                "measured",
                "partially_measured",
            }:
                result.error(
                    f"observations[{idx}] requires measured or partially_measured coverage for layer {layer}."
                )

            obs_key = (
                str(layer),
                str(obs.get("actor")),
                str(obs.get("event")),
                str(kind),
            )
            if obs_key in seen_observations:
                result.error(
                    f"observations[{idx}] duplicates an earlier observation with the same layer/actor/event/kind."
                )
            seen_observations.add(obs_key)

            if kind == "observed_change":
                changed_layers.add(str(layer))
                if "timestamp" not in obs and "timestamp_range" not in obs:
                    result.error(
                        f"observations[{idx}] observed_change requires timestamp or timestamp_range."
                    )
                self._validate_chronology(idx, obs, trigger_timestamp, result)
            if kind == "observed_no_change":
                if "window" not in obs:
                    result.error(f"observations[{idx}] observed_no_change requires a window.")
                if attribution != "none":
                    result.error(
                        f"observations[{idx}] observed_no_change should use attribution='none'."
                    )
                if isinstance(sources, list):
                    for src_idx, src in enumerate(sources):
                        if not isinstance(src, dict):
                            continue
                        has_query_hash = isinstance(src.get("query_hash"), str) and src.get("query_hash").strip()
                        mids = src.get("measurement_ids")
                        has_mids = isinstance(mids, list) and len(mids) > 0
                        has_body = bool(src.get("body_hash")) and bool(src.get("body_path"))
                        has_scope = isinstance(src.get("scope_descriptor"), dict) and len(src.get("scope_descriptor")) > 0
                        if not (has_query_hash or has_mids or has_body or has_scope):
                            result.error(
                                f"observations[{idx}].sources[{src_idx}] supports an observed_no_change "
                                "claim but has no falsifiable evidence anchor (need query_hash, "
                                "measurement_ids, body_hash+body_path, or a structured scope_descriptor). "
                                "Free-form notes alone are insufficient for null claims."
                            )
            if kind == "coverage_gap" and attribution not in {"unknown", "none"}:
                result.error(
                    f"observations[{idx}] coverage_gap should use attribution 'unknown' or 'none'."
                )

            self._validate_sources(idx, layer, sources, result, event.get("status"))

        empirical_shape = event.get("empirical_shape")
        status = event.get("status")
        # empirical_shape rules gate admission, not draft. Drafts are explicitly
        # work-in-progress and may have observed_no_change / coverage_gap only.
        if status != "draft":
            if empirical_shape == "cascade" and len(changed_layers) < 3:
                result.error(
                    "empirical_shape=cascade requires observed_change entries in at least 3 distinct layers."
                )
            if empirical_shape == "comparison" and not (1 <= len(changed_layers) <= 2):
                result.error(
                    "empirical_shape=comparison requires observed_change entries in 1 or 2 distinct layers."
                )

        observed_layers: set[str] = {
            str(obs.get("layer"))
            for obs in observations
            if isinstance(obs, dict) and obs.get("layer") in self.layers
        }
        for layer, status in coverage_by_layer.items():
            if status in {"measured", "partially_measured"} and layer not in observed_layers:
                result.error(
                    f"coverage[{layer}].status={status} requires at least one observation "
                    f"on that layer (observed_change, observed_no_change, or coverage_gap). "
                    "Either add an observation or set status to not_measured / not_applicable."
                )

    def _validate_time_range(self, value: Any, label: str, result: ValidationResult) -> None:
        if not isinstance(value, list) or len(value) != 2:
            result.error(f"{label} must be a two-element list of ISO-8601 date-times.")
            return

        start = parse_datetime(str(value[0]))
        end = parse_datetime(str(value[1]))
        if start is None or end is None:
            result.error(f"{label} must contain valid ISO-8601 date-times.")
            return
        if start > end:
            result.error(f"{label} start must be <= end.")

    def _validate_chronology(
        self,
        idx: int,
        obs: dict[str, Any],
        trigger_timestamp: datetime | None,
        result: ValidationResult,
    ) -> None:
        timestamp_raw = obs.get("timestamp")
        if timestamp_raw is None:
            return

        obs_timestamp = parse_datetime(str(timestamp_raw))
        if obs_timestamp is None or trigger_timestamp is None:
            return

        if obs.get("attribution") in {"direct", "plausible"} and obs_timestamp < trigger_timestamp:
            result.error(
                f"observations[{idx}] timestamp precedes trigger.timestamp for a change attributed to the trigger."
            )

        if "delta_hours" not in obs:
            return

        try:
            delta_hours = float(obs["delta_hours"])
        except (TypeError, ValueError):
            result.error(f"observations[{idx}].delta_hours must be numeric.")
            return

        actual_delta = (obs_timestamp - trigger_timestamp).total_seconds() / 3600.0
        precision = obs.get("precision")
        tolerance_by_precision = {
            "second": 0.02,
            "minute": 0.1,
            "hour": 1.0,
            "hour_range": 1.0,
            "day": 24.0,
            "week": 168.0,
        }
        tolerance = tolerance_by_precision.get(str(precision), 1.0)
        if abs(actual_delta - delta_hours) > tolerance:
            result.error(
                f"observations[{idx}].delta_hours={delta_hours} disagrees with timestamp-trigger difference {actual_delta:.2f}h beyond tolerance for precision={precision}."
            )

    def _validate_sources(
        self,
        idx: int,
        layer: Any,
        sources: Any,
        result: ValidationResult,
        status: Any = None,
    ) -> None:
        if not isinstance(sources, list) or not sources:
            result.error(f"observations[{idx}].sources must be a non-empty list.")
            return

        primary_count = 0
        primary_onchain_count = 0
        semi_primary_count = 0
        supporting_count = 0
        semi_primary_group_ids: set[str] = set()
        semi_primary_ungrouped = 0

        for source_idx, source in enumerate(sources):
            if not isinstance(source, dict):
                result.error(f"observations[{idx}].sources[{source_idx}] must be a mapping.")
                continue
            source_type = source.get("type")
            if source_type not in self.source_types:
                result.error(
                    f"observations[{idx}].sources[{source_idx}].type must be one of {sorted(self.source_types)}"
                )
                continue
            if source_is_primary(source_type):
                primary_count += 1
            if source_type == "primary_onchain":
                primary_onchain_count += 1
            if source_is_semi_primary(source_type):
                semi_primary_count += 1
                group_id = source.get("evidence_group_id")
                if isinstance(group_id, str) and group_id.strip():
                    semi_primary_group_ids.add(group_id.strip())
                else:
                    semi_primary_ungrouped += 1
            if source_is_supporting(source_type):
                supporting_count += 1
            for url_key in ("url", "wayback"):
                if url_key in source and not is_url(str(source[url_key])):
                    result.error(
                        f"observations[{idx}].sources[{source_idx}].{url_key} must be a valid URL."
                    )

            self._validate_body_hash(idx, source_idx, source, result)
            self._validate_archival_anchor(idx, source_idx, source, result)

        if layer == "asset_onchain":
            if primary_onchain_count < 1:
                # asset_onchain primary_onchain requirement still holds even in draft:
                # admitted-level requires at least 1 chain receipt to anchor the claim.
                # For drafts we allow deferring this check.
                if status != "draft":
                    result.error(
                        f"observations[{idx}] asset_onchain requires at least one primary_onchain source."
                    )
            return

        if primary_count >= 1:
            return

        semi_primary_distinct = len(semi_primary_group_ids) + semi_primary_ungrouped
        if semi_primary_distinct >= 2:
            return
        # Admission threshold gates admission-grade observations. Drafts may have a single
        # anchor during in-progress work; promotion requires upgrading to >= 2 distinct
        # semi-primary groups or >= 1 primary source.
        if status == "draft":
            return
        if semi_primary_count >= 2 and semi_primary_distinct < 2:
            result.error(
                f"observations[{idx}] has {semi_primary_count} semi-primary sources but only "
                f"{semi_primary_distinct} distinct evidence groups (sources sharing an "
                f"evidence_group_id count as one). Admission requires 2 independent semi-primary groups."
            )
            return
        result.error(
            f"observations[{idx}] does not meet admission threshold (need 1 primary or 2 independent "
            f"semi-primary sources; {supporting_count} supporting-only sources do not satisfy admission)."
        )

    def _validate_archival_anchor(
        self,
        idx: int,
        source_idx: int,
        source: dict[str, Any],
        result: ValidationResult,
    ) -> None:
        """Enforce methodology §6: every admission-grade web source must be reproducibly archived.

        Anchor requirements by source type:
        - primary_onchain: exempt (tx_hash + block are self-anchoring)
        - semi_primary_measurement: one of {wayback, body_hash+body_path, query_hash, measurement_ids}
        - all other types: one of {wayback, body_hash+body_path}
        Enforced only when the source has a url (i.e. the source is web-based).
        """
        source_type = source.get("type")
        if source_type == "primary_onchain":
            return
        if "url" not in source:
            return

        label = f"observations[{idx}].sources[{source_idx}]"
        has_wayback = isinstance(source.get("wayback"), str) and source.get("wayback").strip()
        has_body_artifact = bool(source.get("body_hash")) and bool(source.get("body_path"))

        if source_type == "semi_primary_measurement":
            has_query_hash = isinstance(source.get("query_hash"), str) and source.get("query_hash").strip()
            measurement_ids = source.get("measurement_ids")
            has_measurement_ids = isinstance(measurement_ids, list) and len(measurement_ids) > 0
            if not (has_wayback or has_body_artifact or has_query_hash or has_measurement_ids):
                result.error(
                    f"{label}.type=semi_primary_measurement requires at least one of "
                    f"wayback, body_hash+body_path, query_hash, or measurement_ids."
                )
            return

        if not (has_wayback or has_body_artifact):
            result.error(
                f"{label}.type={source_type} requires at least one of wayback or body_hash+body_path "
                f"so the archived artifact can be located."
            )

    def _validate_body_hash(
        self,
        idx: int,
        source_idx: int,
        source: dict[str, Any],
        result: ValidationResult,
    ) -> None:
        """Verify that a body_hash claim is backed by a real local file."""
        body_hash_raw = source.get("body_hash")
        body_path_raw = source.get("body_path")
        if body_hash_raw is None and body_path_raw is None:
            return
        label = f"observations[{idx}].sources[{source_idx}]"

        if body_hash_raw is not None and body_path_raw is None:
            result.error(
                f"{label} declares body_hash but no body_path; a body_hash claim requires a "
                "structured body_path field so the archived artifact can be located."
            )
            return
        if body_path_raw is not None and body_hash_raw is None:
            result.error(
                f"{label} declares body_path but no body_hash; a body_path claim requires a "
                "body_hash so the archived artifact can be verified."
            )
            return

        body_hash = str(body_hash_raw).strip()
        if not body_hash.startswith("sha256:"):
            result.error(
                f"{label}.body_hash must be in the form 'sha256:<64-hex>'; got {body_hash[:32]!r}"
            )
            return
        expected_hex = body_hash.split(":", 1)[1].strip().lower()
        if len(expected_hex) != 64 or any(c not in "0123456789abcdef" for c in expected_hex):
            result.error(f"{label}.body_hash digest must be 64 lowercase hex characters.")
            return

        body_path_str = str(body_path_raw).strip()
        if body_path_str.startswith("/"):
            result.error(f"{label}.body_path must be a relative path from the repo root.")
            return
        artifact_path = (REPO_ROOT / body_path_str).resolve()
        try:
            artifact_path.relative_to(REPO_ROOT)
        except ValueError:
            result.error(f"{label}.body_path must resolve inside the repo root.")
            return
        if not artifact_path.is_file():
            result.error(
                f"{label}.body_path points to {body_path_str!r} but no file exists there."
            )
            return

        actual_hex = hashlib.sha256(artifact_path.read_bytes()).hexdigest()
        if actual_hex != expected_hex:
            result.error(
                f"{label}.body_hash does not match the local file at {body_path_str}: "
                f"expected {expected_hex[:12]}…, actual {actual_hex[:12]}…"
            )

    def _validate_recovery(self, recovery: Any, result: ValidationResult) -> None:
        if recovery is None:
            return
        if not isinstance(recovery, list):
            result.error("recovery must be a list when present.")
            return
        for idx, entry in enumerate(recovery):
            if not isinstance(entry, dict):
                result.error(f"recovery[{idx}] must be a mapping.")
                continue
            layer = entry.get("layer")
            if layer not in self.layers:
                result.error(f"recovery[{idx}].layer must be one of {sorted(self.layers)}")
            if "resolved_timestamp" in entry and not parse_iso8601(str(entry["resolved_timestamp"])):
                result.error(f"recovery[{idx}].resolved_timestamp must be ISO-8601 date-time.")

    def _validate_release_readiness(self, event: dict[str, Any], result: ValidationResult) -> None:
        status = event.get("status")
        if status in {"draft", "rejected"}:
            return

        target = event.get("target")
        if isinstance(target, dict):
            enumeration = target.get("enumeration")
            if enumeration in (None, "pending"):
                result.error(
                    "non-draft event requires target.enumeration to be 'complete' or 'subset'; "
                    f"got {enumeration!r}. Pending enumeration is only valid on draft events."
                )

        placeholders = []
        observed_change_count = 0
        invalid_admitted_coverage_gap = False
        coverage_by_layer = {
            entry["layer"]: entry["status"]
            for entry in event.get("coverage", [])
            if isinstance(entry, dict) and "layer" in entry and "status" in entry
        }

        for obs in event.get("observations", []):
            if not isinstance(obs, dict):
                continue
            if obs.get("observation_kind") == "observed_change":
                observed_change_count += 1
            if obs.get("observation_kind") == "coverage_gap":
                invalid_admitted_coverage_gap = True
            layer = obs.get("layer")
            if layer in coverage_by_layer and coverage_by_layer[layer] in {"not_measured", "not_applicable"}:
                result.error(
                    f"non-draft event has observation on layer {layer} but coverage is {coverage_by_layer[layer]}"
                )

        def walk(node: Any, path: str) -> None:
            if isinstance(node, dict):
                for key, value in node.items():
                    walk(value, f"{path}.{key}")
            elif isinstance(node, list):
                for idx, value in enumerate(node):
                    walk(value, f"{path}[{idx}]")
            elif isinstance(node, str):
                lowered = node.lower()
                for marker in PLACEHOLDER_MARKERS:
                    if marker in lowered:
                        placeholders.append(f"{path}: contains placeholder marker '{marker}'")
                        break

        walk(event, "event")
        for message in placeholders:
            result.error(f"non-draft event is not release-ready: {message}")
        # Admission-grade observation rule: cascade_event / comparison_event require at least
        # one observed_change (by definition, they exist to document a change). state_block_event
        # may be admitted with only observed_no_change observations — a persistent-no-cascade
        # finding is a legitimate paper-worthy result (e.g. foreign-operator mixer domain
        # survives an OFAC action, individual-level BTC designation produces no measurable
        # downstream effect). The observation must still be admission-grade under the source
        # rule (checked earlier).
        empirical_shape_final = event.get("empirical_shape")
        if observed_change_count == 0 and empirical_shape_final != "null_event":
            result.error("non-draft event with non-null empirical_shape must contain at least one observed_change observation.")
        elif observed_change_count == 0 and empirical_shape_final == "null_event":
            # require at least one observed_no_change instead
            observations = event.get("observations") or []
            noc = sum(1 for o in observations if isinstance(o, dict) and o.get("observation_kind") == "observed_no_change")
            if noc == 0:
                result.error(
                    "non-draft null_event must contain at least one observation "
                    "(observed_change or observed_no_change with admission-grade sources)."
                )
        if invalid_admitted_coverage_gap:
            result.error("non-draft event may not retain coverage_gap observations; express uncertainty in coverage instead.")

    def _check_citations(
        self,
        event: dict[str, Any],
        result: ValidationResult,
        timeout: float,
    ) -> None:
        for label, url in iter_citation_like_urls(event):
            if not is_url(url):
                result.error(f"{label} is not a valid URL: {url}")
                continue
            ok, detail = fetch_url_status(url, timeout)
            if not ok:
                result.warn(f"{label} unreachable: {url} ({detail})")

    def _check_archive_reachability(
        self,
        event: dict[str, Any],
        result: ValidationResult,
        timeout: float,
    ) -> None:
        """Archival rot detector: HEAD-check every wayback URL on every source.

        body_hash re-verification is already run unconditionally by
        `_validate_body_hash` during regular validation, so --check-archives
        only needs to hit the network for wayback URLs.
        """
        for obs_idx, obs in enumerate(event.get("observations", [])):
            if not isinstance(obs, dict):
                continue
            for src_idx, source in enumerate(obs.get("sources", [])):
                if not isinstance(source, dict):
                    continue
                wayback = source.get("wayback")
                if not wayback:
                    continue
                label = f"observations[{obs_idx}].sources[{src_idx}].wayback"
                ok, detail = fetch_url_status(str(wayback), timeout)
                if not ok:
                    result.error(f"{label} unreachable: {wayback} ({detail})")


def discover_paths(raw_paths: list[str]) -> list[Path]:
    if raw_paths:
        return [Path(path).resolve() for path in raw_paths]
    return sorted(
        path
        for path in EVENTS_DIR.glob("*.yaml")
        if path.name != "TEMPLATE.yaml" and not path.name.startswith("_")
    )


def main() -> int:
    args = parse_args()
    vocab = load_yaml(VOCAB_PATH)
    _ = load_json(SCHEMA_PATH)
    validator = EventValidator(vocab)
    paths = discover_paths(args.paths)

    if not paths:
        print("No event YAML files found.", file=sys.stderr)
        return 1

    all_ok = True
    for path in paths:
        event = load_yaml(path)
        result = validator.validate_event(
            path=path,
            event=event,
            check_citations=args.check_citations,
            check_archives=args.check_archives,
            timeout=args.timeout,
        )
        status = "OK" if result.ok else "FAIL"
        print(f"[{status}] {path}")
        for warning in result.warnings:
            print(f"  WARN: {warning}")
        for error in result.errors:
            print(f"  ERROR: {error}")
        all_ok = all_ok and result.ok

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
