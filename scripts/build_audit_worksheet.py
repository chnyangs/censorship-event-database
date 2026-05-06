#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Generate per-event audit worksheets for human audit sign-off.

For every event whose `admission_tier` is in the selected tiers (default:
`anchor_case`), emit a Markdown worksheet under
`analysis/audit_worksheets/<slug>.md` enumerating every row a human
auditor must sign off on:

  1. Trigger timestamp + precision + citation hashes.
  2. Each `observations[]` row: layer, actor, event, kind, attribution,
     timestamp + precision + delta_hours, source types + archival hashes.
  3. Each `recovery[]` row: layer, resolved, resolved_timestamp.
  4. `scoped_claim` text for re-reading.
  5. A sign-off checklist (passage match / hash verify / precision
     appropriate / attribution not over-claimed / scoped_claim not
     overreading / changed-vs-no-change defensible).

The worksheet is deliberately verbose: every observation gets its own
table row + a notes slot, so auditors cannot skim past under-examined
observations without leaving a visible gap.

After a human audits and checks each row, `last_human_audit` should be
stamped in the event YAML with that date (the validator + CHANGELOG
entry already reflect this convention).

Usage:
    make audit-worksheets                 # anchor cases
    python3 scripts/build_audit_worksheet.py --tiers anchor_case,null_case
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import sys
from datetime import datetime, timezone
from typing import Any

import yaml


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
DEFAULT_OUT_DIR = REPO_ROOT / "analysis" / "audit_worksheets"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import load_meta, now_utc_iso  # noqa: E402


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate per-event audit worksheets.")
    p.add_argument("--events-dir", default=str(EVENTS_DIR))
    p.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    p.add_argument(
        "--tiers", default="anchor_case",
        help="comma-separated admission_tier values to include (default: anchor_case)",
    )
    p.add_argument(
        "--slug", default=None,
        help="limit to a single event slug (overrides --tiers)",
    )
    return p.parse_args()


def _hash_snippet(value: Any) -> str:
    """Return a short human-readable rendering of a body_hash or query_hash."""
    if not value:
        return "—"
    s = str(value)
    if ":" in s:
        prefix, rest = s.split(":", 1)
        if len(rest) > 20:
            return f"`{prefix}:{rest[:8]}…{rest[-4:]}`"
    return f"`{s[:24]}…`" if len(s) > 28 else f"`{s}`"


def _fmt_source(src: dict) -> str:
    parts: list[str] = []
    t = src.get("type") or "?"
    parts.append(f"type=`{t}`")
    url = src.get("url")
    if url:
        parts.append(f"url=<{url}>")
    wb = src.get("wayback")
    if wb:
        parts.append(f"wayback=<{wb}>")
    bh = src.get("body_hash")
    if bh:
        parts.append(f"body_hash={_hash_snippet(bh)}")
    bp = src.get("body_path")
    if bp:
        parts.append(f"body_path=`{bp}`")
    qh = src.get("query_hash")
    if qh:
        parts.append(f"query_hash={_hash_snippet(qh)}")
    mids = src.get("measurement_ids")
    if isinstance(mids, list) and mids:
        parts.append(f"measurement_ids=`{mids[0]}…` ({len(mids)})")
    scope = src.get("scope_descriptor")
    if isinstance(scope, dict) and scope:
        parts.append(f"scope_descriptor=({len(scope)} keys)")
    tx = src.get("tx")
    if tx:
        parts.append(f"tx={_hash_snippet(tx)}")
    block = src.get("block")
    if block:
        parts.append(f"block=`{block}`")
    return " · ".join(parts)


def _verify_body_hash(body_hash: Any, body_path: Any) -> str:
    """Return 'ok', 'MISMATCH', 'MISSING', or '—'."""
    if not body_hash or not body_path:
        return "—"
    bh = str(body_hash).strip()
    if not bh.startswith("sha256:"):
        return "BAD_FORMAT"
    expected = bh.split(":", 1)[1].strip().lower()
    path = REPO_ROOT / str(body_path)
    if not path.exists():
        return "MISSING"
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    return "ok" if actual == expected else "MISMATCH"


def _fmt_ts(obs: dict, trigger_ts: str | None) -> str:
    ts = obs.get("timestamp")
    prec = obs.get("precision") or "—"
    dh = obs.get("delta_hours")
    bits = []
    if ts:
        bits.append(f"`{ts}`")
    else:
        bits.append("—")
    bits.append(f"precision=`{prec}`")
    if dh is not None:
        bits.append(f"delta_hours=`{dh}`")
    return " · ".join(bits)


def render_worksheet(event: dict, ds_meta: dict) -> str:
    slug = event.get("id") or "unknown"
    trigger = event.get("trigger") or {}
    trigger_ts = trigger.get("timestamp")
    observations = event.get("observations") or []
    recovery = event.get("recovery") or []

    lines: list[str] = []
    lines.append(f"# Audit worksheet — `{slug}`")
    lines.append("")
    lines.append(
        f"Dataset snapshot: **v{ds_meta.get('dataset_version') or '?'}** · "
        f"cutoff `{ds_meta.get('cutoff_date') or 'n/a'}` · "
        f"commit `{ds_meta.get('source_commit') or 'n/a'}` · "
        f"generated `{now_utc_iso()}`"
    )
    lines.append("")
    lines.append(
        f"- **admission_tier**: `{event.get('admission_tier')}`"
    )
    lines.append(
        f"- **research_stratum**: `{event.get('research_stratum')}`"
    )
    lines.append(
        f"- **empirical_shape**: `{event.get('empirical_shape')}`"
    )
    lines.append(
        f"- **status**: `{event.get('status')}`"
    )
    lha = event.get("last_human_audit")
    lv = event.get("last_verified")
    lines.append(f"- **last_verified**: `{lv or '—'}`")
    lines.append(f"- **last_human_audit**: `{lha or '—'}`  ← update after sign-off")
    lines.append("")

    lines.append("## 0. How to use this worksheet")
    lines.append("")
    lines.append(
        "Work top-to-bottom. For each row: (a) open the cited source in a "
        "browser (or `body_path` on disk) and confirm the passage supports "
        "the claim; (b) confirm the timestamp precision is appropriate for "
        "the claim; (c) confirm the attribution (`direct` / `plausible` / "
        "`none`) is not over-stated; (d) check that `observation_kind` is "
        "correct (no-change vs change vs gap). Mark the checkbox when "
        "satisfied. Leave a NOTE line if you changed anything. "
        "Reject the row (uncheck) if the claim needs revision — do NOT "
        "stamp `last_human_audit` until every row is checked."
    )
    lines.append("")

    # --- trigger ---
    lines.append("## 1. Trigger")
    lines.append("")
    lines.append(f"- **type**: `{trigger.get('type')}`")
    lines.append(f"- **actor**: `{trigger.get('actor')}`")
    actor_name = trigger.get("actor_name")
    if actor_name:
        lines.append(f"- **actor_name**: `{actor_name}`")
    lines.append(f"- **timestamp**: `{trigger_ts}` · precision=`{trigger.get('precision') or '—'}`")
    lines.append("")
    lines.append("### Trigger citations")
    lines.append("")
    cites = trigger.get("citations") or trigger.get("citation") or []
    if not cites:
        lines.append("_No trigger citations._")
    else:
        for i, c in enumerate(cites):
            if isinstance(c, str):
                lines.append(f"- [ ] citation[{i}]: url=<{c}>")
            elif isinstance(c, dict):
                lines.append(
                    f"- [ ] citation[{i}]: {_fmt_source(c)}  "
                    f"· hash_check=`{_verify_body_hash(c.get('body_hash'), c.get('body_path'))}`"
                )
    lines.append("")
    lines.append(
        "Sign-off rules for the trigger: timestamp precision must match "
        "the citation granularity. If the SDN publishes to day precision, "
        "**do not** assert hour precision in any downstream observation's "
        "`delta_hours`."
    )
    lines.append("")

    # --- scoped_claim ---
    sc = event.get("scoped_claim")
    if sc:
        lines.append("## 2. Scoped claim (read carefully)")
        lines.append("")
        lines.append("> " + sc.replace("\n", "\n> "))
        lines.append("")
        lines.append(
            "- [ ] Scoped claim does NOT overread the evidence "
            "(e.g. \"the SDN caused X\" when attribution is `plausible`)."
        )
        lines.append(
            "- [ ] Scoped claim uses the dataset's controlled vocabulary "
            "(`observed_change` / `observed_no_change` / `plausible` / `direct`)."
        )
        lines.append("")

    # --- observations ---
    lines.append("## 3. Observations")
    lines.append("")
    if not observations:
        lines.append("_No observations on this event._")
    else:
        for idx, obs in enumerate(observations):
            if not isinstance(obs, dict):
                continue
            layer = obs.get("layer")
            actor = obs.get("actor")
            evnt = obs.get("event")
            kind = obs.get("observation_kind")
            attr = obs.get("attribution")
            lines.append(
                f"### 3.{idx + 1} · `{layer}` · actor=`{actor}` · event=`{evnt}`"
            )
            lines.append("")
            lines.append(f"- **observation_kind**: `{kind}`")
            lines.append(f"- **attribution**: `{attr}`")
            lines.append(f"- **timestamp**: {_fmt_ts(obs, trigger_ts)}")
            win = obs.get("window")
            if isinstance(win, list) and len(win) == 2:
                lines.append(f"- **window**: `{win[0]}` → `{win[1]}`")
            sources = obs.get("sources") or []
            lines.append(f"- **sources** ({len(sources)}):")
            for si, src in enumerate(sources):
                if not isinstance(src, dict):
                    continue
                hashline = _verify_body_hash(src.get("body_hash"), src.get("body_path"))
                lines.append(
                    f"  - [ ] src[{si}]: {_fmt_source(src)}  "
                    f"· hash_check=`{hashline}`"
                )
            note = obs.get("note")
            if note:
                short = str(note).strip().splitlines()[0][:200]
                lines.append(f"- **note (first line)**: {short}")
            lines.append("")
            lines.append("Audit checks:")
            lines.append(f"- [ ] Passage in each cited source supports `{kind}` for this layer.")
            lines.append(
                f"- [ ] Attribution `{attr}` is not over-stated "
                f"(`direct` requires primary_* source corroborating the causal link)."
            )
            lines.append(
                "- [ ] Timestamp precision is sufficient for any "
                "`delta_hours` downstream claim (day-precision → NO hour claim)."
            )
            if kind == "observed_no_change":
                lines.append(
                    "- [ ] `observed_no_change` is bounded by a `window` and at "
                    "least one falsifiable evidence anchor (query_hash / "
                    "measurement_ids / body_hash+body_path / scope_descriptor)."
                )
                lines.append(
                    "- [ ] `attribution` is `none` (no causal claim under null observation)."
                )
            if kind == "observed_change":
                lines.append(
                    "- [ ] The cited evidence rules out the observed change "
                    "being caused by an unrelated ecosystem-level shift "
                    "(especially for `direct` attribution)."
                )
            lines.append("- [ ] NOTE: _free-form audit note (if the row was revised)_")
            lines.append("")

    # --- recovery ---
    lines.append("## 4. Recovery")
    lines.append("")
    if not recovery:
        lines.append("_No recovery rows on this event._")
    else:
        for idx, r in enumerate(recovery):
            if not isinstance(r, dict):
                continue
            lines.append(
                f"- [ ] recovery[{idx}]: layer=`{r.get('layer')}` · "
                f"resolved=`{r.get('resolved')}` · "
                f"resolved_timestamp=`{r.get('resolved_timestamp') or '—'}`"
            )
            if r.get("layer"):
                lines.append(
                    f"  - [ ] recovery layer is in `changed_layers` for this event "
                    f"(derived/event_metrics.json intersects recovery with "
                    f"changed_layers; a recovery row on a non-changed layer is "
                    f"silently ignored — revise or remove)."
                )
        lines.append("")

    # --- sign-off ---
    lines.append("## 5. Sign-off")
    lines.append("")
    lines.append("- [ ] Every checkbox above is checked.")
    lines.append(
        f"- [ ] Update `events/{slug}.yaml`: "
        f"set `last_human_audit: YYYY-MM-DD` to today's UTC date."
    )
    lines.append(
        "- [ ] Run `make validate` after editing; `make derived` regenerates "
        "the derived artifacts consuming `last_human_audit` semantically."
    )
    lines.append(
        "- [ ] Log the audit in `CHANGELOG.md` (one line: `audit: <slug> · "
        "<auditor-initials> · <date> · <n-row-changes>`)."
    )
    lines.append("")
    lines.append(
        "If any row could not be signed off, **do not stamp** "
        "`last_human_audit`; file the specific blocker as a GitHub issue "
        "tagged `audit-blocker` and link it from the event YAML's "
        "`analysis_notes` field."
    )
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    events_dir = pathlib.Path(args.events_dir)
    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    events: list[dict] = []
    for f in sorted(events_dir.glob("*.yaml")):
        if f.name == "TEMPLATE.yaml" or f.name.startswith("_"):
            continue
        event = yaml.safe_load(f.read_text())
        if isinstance(event, dict) and event.get("status") == "admitted":
            events.append(event)

    if args.slug:
        selected = [e for e in events if e.get("id") == args.slug]
    else:
        tiers = {t.strip() for t in args.tiers.split(",") if t.strip()}
        selected = [e for e in events if e.get("admission_tier") in tiers]

    if not selected:
        print(f"[build_audit_worksheet] no events matched selection", file=sys.stderr)
        return 1

    ds_meta = load_meta()
    selected_slugs = {str(e.get("id")) for e in selected if e.get("id")}
    if not args.slug and out_dir.resolve() == DEFAULT_OUT_DIR.resolve():
        for stale in out_dir.glob("*.md"):
            if stale.stem not in selected_slugs:
                stale.unlink()
    for e in selected:
        slug = e.get("id") or "unknown"
        out_path = out_dir / f"{slug}.md"
        out_path.write_text(render_worksheet(e, ds_meta))
        print(f"[build_audit_worksheet] wrote {out_path.relative_to(REPO_ROOT)}")

    print(
        f"[build_audit_worksheet] {len(selected)} worksheet(s) written to "
        f"{out_dir.relative_to(REPO_ROOT)}/"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
