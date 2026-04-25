#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""
Layer A of the framework: render a single event as a structured evidence
chain — "claim → supporting observations → sources (with body_hash) → gaps".

Consumers: paper authors writing specific sections, amicus-brief drafters,
expert-report authors. The output is Markdown that can be dropped into a
longer document as an auditable argument block.

Output artifact is stamped with `dataset_version` / `schema_version` /
`tool_version` / `generated_at` per the reproducibility contract in
docs/limitations-and-use.md.

Usage:
    python3 scripts/render_evidence_chain.py <event_slug>
    python3 scripts/render_evidence_chain.py --all        # renders every admitted event
    python3 scripts/render_evidence_chain.py <slug> --output-dir analysis/evidence-chains/
"""

from __future__ import annotations

import argparse
import pathlib
import sys
from typing import Any

import yaml


TOOL_VERSION = "0.1.0"
REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
DEFAULT_OUT_DIR = REPO_ROOT / "analysis" / "evidence-chains"

# Shared dataset-identity accessor (reads dataset.meta.json; falls back to a
# synthesized dict so this script keeps working on a fresh checkout that
# hasn't yet run `make dataset`).
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import load_meta, now_utc_iso  # noqa: E402


def load_event(slug: str) -> dict:
    path = EVENTS_DIR / f"{slug}.yaml"
    if not path.exists():
        raise FileNotFoundError(f"No event named {slug} (looking at {path})")
    return yaml.safe_load(path.read_text())


def render_source(src: dict, indent: str = "    ") -> list[str]:
    lines = []
    stype = src.get("type", "unknown")
    url = src.get("url", "")
    bh = src.get("body_hash", "")
    bp = src.get("body_path", "")
    wb = src.get("wayback", "")
    tx = src.get("tx_hash", "")
    note = (src.get("note") or "").strip()
    lines.append(f"{indent}- **`{stype}`**")
    if url:
        lines.append(f"{indent}  - URL: <{url}>")
    if wb:
        lines.append(f"{indent}  - Wayback: <{wb}>")
    if bh:
        lines.append(f"{indent}  - body_hash: `{bh}`")
    if bp:
        lines.append(f"{indent}  - body_path: `{bp}`")
    if tx:
        lines.append(f"{indent}  - tx_hash: `{tx}`")
    if note:
        # Quote it as a blockquote so the reader sees exactly our paraphrase
        nq = note.replace("\n", "\n> " + indent)
        lines.append(f"{indent}  > {nq}")
    return lines


def render_event_evidence_chain(event: dict, meta: dict) -> str:
    dataset_version = meta.get("dataset_version") or "unknown"
    cutoff = meta.get("cutoff_date") or "n/a"
    commit = meta.get("source_commit") or ""
    slug = event.get("id", "unknown")
    stratum = event.get("research_stratum", "?")
    shape = event.get("empirical_shape", "?")
    tier = event.get("admission_tier", "?")
    status = event.get("status", "?")
    schema_v = event.get("schema_version", "?")
    last_verified = event.get("last_verified", "?")

    obs = event.get("observations") or []
    changed = [o for o in obs if o.get("observation_kind") == "observed_change"]
    unchanged = [o for o in obs if o.get("observation_kind") == "observed_no_change"]
    changed_layers = sorted({o.get("layer") for o in changed})

    out = []

    # ===== Header =====
    out.append(f"# Evidence chain — `{slug}`")
    out.append("")
    out.append(f"**Status**: `{status}` · "
               f"**Stratum**: `{stratum}` · "
               f"**Shape**: `{shape}` ({len(changed_layers)} changed layer(s): "
               f"{', '.join(f'`{l}`' for l in changed_layers) or 'none'}) · "
               f"**Tier**: `{tier}`")
    out.append("")
    out.append(f"**Dataset version**: `{dataset_version}` · "
               f"**Dataset cutoff**: `{cutoff}`"
               + (f" · **Source commit**: `{commit}`" if commit else "")
               + f" · **Schema**: `{schema_v}` · "
               f"**Event last_verified**: `{last_verified}` · "
               f"**Tool version**: `{TOOL_VERSION}` · "
               f"**Generated**: `{now_utc_iso()}`")
    out.append("")
    out.append("> ⚠️ **This output is auditable evidence, not advice.** "
               "Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) "
               "before using any claim below in a brief, memo, or risk model.")
    out.append("")

    # ===== Scoped claim =====
    out.append("## Scoped claim")
    out.append("")
    claim = (event.get("scoped_claim") or "").strip()
    if claim:
        for line in claim.split("\n"):
            out.append(f"> {line}")
    else:
        out.append("> *(no scoped_claim recorded — event not paper-ready)*")
    out.append("")

    # ===== Trigger =====
    out.append("## 1. Trigger")
    out.append("")
    trig = event.get("trigger") or {}
    out.append(f"- **Type**: `{trig.get('type','?')}`")
    out.append(f"- **Actor**: `{trig.get('actor','?')}`")
    out.append(f"- **Timestamp**: `{trig.get('timestamp','?')}` "
               f"(precision: `{trig.get('timestamp_precision','?')}`)")
    out.append("")
    out.append("### Trigger citations")
    out.append("")
    for c in trig.get("citation") or []:
        out.extend(render_source(c, indent=""))
    out.append("")

    # ===== Target =====
    out.append("## 2. Target")
    out.append("")
    tgt = event.get("target") or {}
    out.append(f"- **Kind**: `{tgt.get('kind','?')}`")
    out.append(f"- **Enumeration**: `{tgt.get('enumeration','?')}`")
    if tgt.get("protocol"):
        out.append(f"- **Protocol**: `{tgt.get('protocol')}`")
    if tgt.get("actor_name"):
        out.append(f"- **Actor name**: {tgt.get('actor_name')}")
    if tgt.get("chains"):
        out.append(f"- **Chains**: {', '.join(f'`{c}`' for c in tgt['chains'])}")
    addrs = tgt.get("addresses") or []
    if addrs:
        out.append(f"- **Addresses**: {len(addrs)} total (enumerated in event YAML)")
    domains = tgt.get("canonical_domains") or []
    if domains:
        out.append(f"- **Canonical domains**: {', '.join(f'`{d}`' for d in domains)}")
    en = (tgt.get("enumeration_note") or "").strip()
    if en:
        out.append("")
        for line in en.split("\n"):
            out.append(f"> {line}")
    out.append("")

    # ===== Observations (changed layers — the claim evidence) =====
    out.append("## 3. Changed-layer observations (supports the scoped claim)")
    out.append("")
    if not changed:
        out.append("*No observed_change entries. This is a `null_event`; see §4 for "
                   "observed_no_change evidence supporting the null claim.*")
        out.append("")
    else:
        for o in changed:
            layer = o.get("layer", "?")
            ev = o.get("event", "?")
            attr = o.get("attribution", "?")
            ts = o.get("timestamp", "?")
            dh = o.get("delta_hours")
            out.append(f"### {layer} · attribution: `{attr}` · Δt = {dh}h")
            out.append("")
            out.append(f"**Event label**: `{ev}`")
            out.append("")
            out.append(f"**Timestamp**: `{ts}` (precision: `{o.get('precision','?')}`)")
            out.append("")
            out.append("**Sources**:")
            out.append("")
            for s in o.get("sources") or []:
                out.extend(render_source(s, indent=""))
            out.append("")

    # ===== Observations (no change — null claims) =====
    if unchanged:
        out.append("## 4. No-change observations (where applicable)")
        out.append("")
        for o in unchanged:
            layer = o.get("layer", "?")
            ev = o.get("event", "?")
            out.append(f"### {layer} — `{ev}`")
            out.append("")
            wdw = o.get("window")
            if wdw:
                out.append(f"**Window**: `{wdw[0]}` → `{wdw[1]}`")
                out.append("")
            out.append("**Sources**:")
            out.append("")
            for s in o.get("sources") or []:
                out.extend(render_source(s, indent=""))
            out.append("")

    # ===== Coverage gaps =====
    out.append("## 5. Honest coverage gaps")
    out.append("")
    any_gap = False
    for cov in event.get("coverage") or []:
        if cov.get("status") in ("not_measured",):
            any_gap = True
            out.append(f"- **{cov['layer']}** (`not_measured`): "
                       f"{str(cov.get('note','')).strip().splitlines()[0] if cov.get('note') else '(no note)'}")
    if not any_gap:
        out.append("*No layers are `not_measured` for this event — every applicable "
                   "layer is `measured`, `partially_measured`, or `not_applicable`.*")
    out.append("")

    # ===== Follow-on reactions (non-causal) =====
    foi = event.get("follow_on_reaction") or []
    if foi:
        out.append("## 6. Follow-on reactions (informational, not causally attributed)")
        out.append("")
        out.append("> These are cross-event reactions observed after the trigger but "
                   "with `attribution: unknown` or temporal gap too large for direct "
                   "causation. **They do NOT support the scoped claim above.** Tracked "
                   "for cross-event anchor purposes only.")
        out.append("")
        for r in foi:
            out.append(f"### {r.get('layer','?')} — `{r.get('event','?')}`")
            out.append("")
            out.append(f"- Attribution: `{r.get('attribution','?')}`")
            out.append(f"- Relationship: `{r.get('relationship','?')}`")
            out.append(f"- Δt from trigger: `{r.get('delta_hours_from_trigger','?')}h`")
            note = (r.get("note") or "").strip()
            if note:
                out.append("")
                for line in note.split("\n"):
                    out.append(f"> {line}")
            out.append("")
            for s in r.get("sources") or []:
                out.extend(render_source(s, indent=""))
            out.append("")

    # ===== Related events =====
    related = event.get("related_events") or []
    if related:
        out.append("## 7. Related events")
        out.append("")
        for r in related:
            out.append(f"- [`{r}`](./{r}.md)")
        out.append("")

    # ===== How to audit =====
    out.append("## 8. How to audit this chain")
    out.append("")
    out.append(
        f"1. Clone the repository at tag `v{dataset_version}`"
        + (f" (commit `{commit}`)" if commit else "")
        + "."
    )
    out.append(f"2. For each source above, fetch the file at its `body_path` and "
               f"compute its sha256. It must match the recorded `body_hash`.")
    out.append(f"3. For each primary-onchain source, look up the `tx_hash` on the "
               f"respective block explorer. The tx should exist in the block "
               f"referenced or within the same day.")
    out.append(f"4. If any check fails, file an issue per "
               f"[`docs/audit-protocol.md`](../../docs/audit-protocol.md).")
    out.append("")

    return "\n".join(out) + "\n"


def main() -> int:
    p = argparse.ArgumentParser(
        description="Render an event's evidence chain as auditable Markdown."
    )
    p.add_argument("slug", nargs="?", help="event slug (omit with --all)")
    p.add_argument("--all", action="store_true", help="render every admitted event")
    p.add_argument("--output-dir", default=str(DEFAULT_OUT_DIR),
                   help="output directory for --all mode")
    p.add_argument("--stdout", action="store_true",
                   help="print single-event output to stdout instead of writing")
    args = p.parse_args()

    meta = load_meta()

    if args.all:
        out_dir = pathlib.Path(args.output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        n = 0
        for f in sorted(EVENTS_DIR.glob("*.yaml")):
            event = yaml.safe_load(f.read_text())
            content = render_event_evidence_chain(event, meta)
            (out_dir / f"{f.stem}.md").write_text(content)
            n += 1
        print(f"[render_evidence_chain] wrote {n} chains to {out_dir} "
              f"(dataset v{meta.get('dataset_version')}, cutoff {meta.get('cutoff_date')})")
        return 0

    if not args.slug:
        p.error("provide a slug or use --all")

    event = load_event(args.slug)
    content = render_event_evidence_chain(event, meta)

    if args.stdout:
        print(content)
    else:
        out_dir = pathlib.Path(args.output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{args.slug}.md"
        out_path.write_text(content)
        print(f"[render_evidence_chain] wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
