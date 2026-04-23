# SPDX-License-Identifier: MIT

"""Shared accessor for dataset-level metadata (version, cutoff, commit, counts).

`dataset.meta.json` is the single source of truth: `scripts/build_dataset.py`
writes it, and downstream scripts (evidence-chain, comparable-case, site) read
it so their output carries consistent version / cutoff / commit strings.

If `dataset.meta.json` doesn't exist yet (e.g. a fresh checkout that hasn't
run `make dataset`), `load_meta()` synthesizes a best-effort fallback so the
scripts keep working. Fallback values are clearly marked with
`"_source": "synthesized"` so callers can warn or refuse if they need
strict meta.
"""
from __future__ import annotations

import json
import pathlib
import subprocess
from datetime import date, datetime, timezone
from typing import Any

import yaml


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
META_PATH = REPO_ROOT / "dataset.meta.json"
CITATION_CFF = REPO_ROOT / "CITATION.cff"
EVENTS_DIR = REPO_ROOT / "events"


def _read_cff_version() -> str:
    if not CITATION_CFF.exists():
        return "0.0.0-unreleased"
    for line in CITATION_CFF.read_text().splitlines():
        s = line.strip()
        if s.startswith("version:"):
            return s.split(":", 1)[1].strip().strip("'\"") or "0.0.0-unreleased"
    return "0.0.0-unreleased"


def _git_short_sha() -> str:
    try:
        r = subprocess.run(
            ["git", "rev-parse", "--short=7", "HEAD"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=5, check=False,
        )
        if r.returncode == 0:
            return r.stdout.strip()
    except (FileNotFoundError, subprocess.SubprocessError):
        pass
    return ""


def _synth_cutoff() -> str | None:
    # cutoff_date = max(last_verified, last_human_audit) across events.
    # Must stay in lock-step with scripts/build_dataset.py::build_meta.
    # Canonical definition lives in docs/limitations-and-use.md §2.5.
    cutoff: date | None = None
    for p in EVENTS_DIR.glob("*.yaml"):
        try:
            ev = yaml.safe_load(p.read_text())
        except Exception:
            continue
        if not isinstance(ev, dict):
            continue
        for key in ("last_verified", "last_human_audit"):
            v = ev.get(key)
            if v is None:
                continue
            if isinstance(v, datetime):
                d = v.date()
            elif isinstance(v, date):
                d = v
            else:
                try:
                    d = datetime.strptime(str(v), "%Y-%m-%d").date()
                except ValueError:
                    continue
            if cutoff is None or d > cutoff:
                cutoff = d
    return cutoff.isoformat() if cutoff else None


def _synth() -> dict[str, Any]:
    return {
        "dataset_name": "censorship-event-database",
        "dataset_version": _read_cff_version(),
        "cutoff_date": _synth_cutoff(),
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "source_commit": _git_short_sha(),
        "_source": "synthesized",
    }


def load_meta() -> dict[str, Any]:
    """Return dataset metadata. Prefers the committed `dataset.meta.json`;
    falls back to a synthesized dict if the file is missing."""
    if META_PATH.exists():
        try:
            meta = json.loads(META_PATH.read_text())
            meta.setdefault("_source", "file")
            return meta
        except (OSError, json.JSONDecodeError):
            pass
    return _synth()


def stamp_line(meta: dict[str, Any] | None = None, tool_version: str | None = None) -> str:
    """A single-line dataset identity stamp for Markdown headers."""
    m = meta or load_meta()
    parts = [
        f"dataset `{m.get('dataset_version') or '?'}`",
        f"cutoff `{m.get('cutoff_date') or 'n/a'}`",
    ]
    sc = m.get("source_commit")
    if sc:
        parts.append(f"commit `{sc}`")
    if tool_version:
        parts.append(f"tool `{tool_version}`")
    parts.append(
        f"generated `{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}`"
    )
    if m.get("_source") == "synthesized":
        parts.append("_(meta synthesized — run `make dataset` for a committed snapshot)_")
    return " · ".join(parts)
