#!/usr/bin/env python3
"""
Render events/*.yaml into a static HTML site under site/.

No external dependencies beyond PyYAML (already a project dep). Writes plain
HTML + single CSS file; designed for GitHub Pages hosting.
"""

from __future__ import annotations

import argparse
import collections
import html
import json
import pathlib
import shutil
import sys
from datetime import datetime, timezone

import yaml


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
SITE_DIR = REPO_ROOT / "site"


CSS = """
* { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  max-width: 1100px; margin: 2rem auto; padding: 0 1rem;
  color: #222; line-height: 1.5;
}
h1, h2, h3 { color: #111; margin-top: 1.8em; }
h1 { border-bottom: 2px solid #333; padding-bottom: 0.3em; }
h2 { border-bottom: 1px solid #aaa; padding-bottom: 0.2em; }
a { color: #06c; text-decoration: none; }
a:hover { text-decoration: underline; }
code, pre { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 0.92em; }
pre { background: #f6f8fa; padding: 0.8em; overflow-x: auto; border-radius: 4px; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; }
th, td { border: 1px solid #ddd; padding: 6px 10px; text-align: left; vertical-align: top; }
th { background: #f2f4f7; font-weight: 600; }
tr:nth-child(even) td { background: #fafbfc; }
.meta { color: #666; font-size: 0.9em; }
.pill {
  display: inline-block; padding: 1px 8px; border-radius: 10px;
  font-size: 0.78em; font-weight: 600; margin-right: 4px;
}
.pill-admitted { background: #e3f8dc; color: #1d5827; }
.pill-cascade { background: #fde4e4; color: #7b1a1a; }
.pill-comparison { background: #e4ecfd; color: #1e3a7a; }
.pill-state_block { background: #f2e9f9; color: #4f2870; }
.pill-measured { background: #d4ead4; color: #1d5827; }
.pill-partially_measured { background: #fff3c9; color: #755400; }
.pill-not_measured { background: #ffd8d8; color: #7a1d1d; }
.pill-not_applicable { background: #e5e7eb; color: #4a5058; }
.pill-observed_change { background: #ffddcc; color: #7a2e0b; }
.pill-observed_no_change { background: #ddeaff; color: #1a3f7a; }
.pill-coverage_gap { background: #f4e5cb; color: #6d4a0c; }
.pill-direct { background: #fde4e4; color: #7b1a1a; }
.pill-plausible { background: #fff3c9; color: #755400; }
.pill-none { background: #e5e7eb; color: #4a5058; }
.filter-bar {
  background: #f6f8fa; padding: 0.8em; border-radius: 6px;
  margin: 1em 0; display: flex; gap: 1em; flex-wrap: wrap;
}
.filter-bar label { font-weight: 600; }
.stat-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1em; margin: 1em 0;
}
.stat-card {
  background: #f6f8fa; border-left: 4px solid #06c;
  padding: 0.8em 1em; border-radius: 4px;
}
.stat-number { font-size: 1.8em; font-weight: 700; color: #06c; }
.stat-label { color: #666; font-size: 0.88em; }
nav.breadcrumb { margin-bottom: 1em; font-size: 0.9em; color: #666; }
.source-ref { font-size: 0.88em; color: #444; margin: 0.4em 0; padding-left: 1em; border-left: 2px solid #ddd; }
.source-ref code { background: #f6f8fa; padding: 0 4px; }
.addresses { font-family: ui-monospace, Menlo, monospace; font-size: 0.85em; line-height: 1.6; }
details { margin: 0.6em 0; }
summary { cursor: pointer; font-weight: 600; color: #06c; }
footer { margin-top: 4em; padding-top: 1em; border-top: 1px solid #ddd; color: #888; font-size: 0.85em; }
"""


def escape(s):
    return html.escape(str(s)) if s is not None else ""


def pill(text, cls_suffix=None):
    cls = "pill"
    if cls_suffix:
        cls += f" pill-{cls_suffix.replace(' ', '_')}"
    return f'<span class="{cls}">{escape(text)}</span>'


def render_observations(obs_list):
    if not obs_list:
        return "<p><em>No observations.</em></p>"
    rows = []
    for i, obs in enumerate(obs_list):
        layer = obs.get("layer", "—")
        kind = obs.get("observation_kind", "—")
        attribution = obs.get("attribution", "—")
        actor = obs.get("actor", "—")
        event_name = obs.get("event", "—")
        ts = obs.get("timestamp", "—")
        delta = obs.get("delta_hours", "—")
        sources = obs.get("sources", []) or []
        sources_html = "<ul>"
        for s in sources:
            stype = s.get("type", "—")
            url = s.get("url", "")
            bh = s.get("body_hash", "")
            note = s.get("note", "")
            sources_html += f'<li><code>{escape(stype)}</code>'
            if url:
                sources_html += f' <a href="{escape(url)}">{escape(url[:70])}{"…" if len(url) > 70 else ""}</a>'
            if bh:
                sources_html += f' <span class="meta"><code>{escape(bh[:23])}…</code></span>'
            if note:
                note_short = str(note).strip().split("\n")[0][:160]
                sources_html += f'<br><span class="meta">{escape(note_short)}{"…" if len(str(note)) > 160 else ""}</span>'
            sources_html += "</li>"
        sources_html += "</ul>"
        rows.append(f"""
        <tr>
          <td>{pill(layer)}</td>
          <td>{pill(kind, kind)}</td>
          <td>{pill(attribution, attribution)}</td>
          <td><code>{escape(actor)}</code><br><span class="meta">{escape(event_name)}</span></td>
          <td><code>{escape(ts)}</code><br><span class="meta">Δ{escape(delta)}h</span></td>
          <td>{sources_html}</td>
        </tr>""")
    return f"""
    <table>
      <thead><tr><th>Layer</th><th>Kind</th><th>Attribution</th><th>Actor / event</th><th>Time</th><th>Sources</th></tr></thead>
      <tbody>{"".join(rows)}</tbody>
    </table>"""


def render_coverage(cov_list):
    if not cov_list:
        return ""
    rows = []
    for c in cov_list:
        layer = c.get("layer", "—")
        status = c.get("status", "—")
        chain = c.get("chain", "")
        scope = c.get("scope") or []
        scope_s = ", ".join(scope) if isinstance(scope, list) else str(scope)
        note = c.get("note") or ""
        note_short = str(note).strip().split("\n")[0][:220]
        rows.append(f"""
        <tr>
          <td>{pill(layer)}</td>
          <td>{pill(status, status)}</td>
          <td><code>{escape(chain) or "—"}</code></td>
          <td>{escape(scope_s) or "—"}</td>
          <td class="meta">{escape(note_short)}{"…" if len(str(note)) > 220 else ""}</td>
        </tr>""")
    return f"""
    <table>
      <thead><tr><th>Layer</th><th>Status</th><th>Chain</th><th>Scope</th><th>Note</th></tr></thead>
      <tbody>{"".join(rows)}</tbody>
    </table>"""


def render_trigger(trig):
    citations = trig.get("citation") or []
    cite_rows = []
    for c in citations:
        cite_rows.append(f"""
        <div class="source-ref">
          <code>{escape(c.get('type','—'))}</code>
          <a href="{escape(c.get('url',''))}">{escape(c.get('url','')[:80])}</a><br>
          {f"<code>{escape(c.get('body_hash',''))}</code><br>" if c.get('body_hash') else ""}
          <span class="meta">{escape(str(c.get('note',''))[:260])}{"…" if len(str(c.get('note',''))) > 260 else ""}</span>
        </div>""")
    return f"""
    <p><strong>Type:</strong> <code>{escape(trig.get('type','—'))}</code> &nbsp;
       <strong>Actor:</strong> <code>{escape(trig.get('actor','—'))}</code> &nbsp;
       <strong>Timestamp:</strong> <code>{escape(trig.get('timestamp','—'))}</code>
       (precision <code>{escape(trig.get('timestamp_precision','—'))}</code>)</p>
    <h3>Citations</h3>
    {"".join(cite_rows)}"""


def render_event(event, relroot=".."):
    slug = event.get("id", "unknown")
    title = slug.replace("-", " ")
    ec = event.get("empirical_shape", "—")
    status = event.get("status", "—")
    target = event.get("target") or {}
    addrs = target.get("addresses") or []
    addrs_html = ""
    if addrs:
        addrs_html = f"""<details><summary>Target addresses ({len(addrs)})</summary>
        <div class="addresses">{"<br>".join(escape(a) for a in addrs)}</div></details>"""

    related = event.get("related_events") or []
    related_html = ""
    if related:
        related_html = "<p><strong>Related events:</strong> " + ", ".join(
            f'<a href="./{escape(r)}.html">{escape(r)}</a>' for r in related
        ) + "</p>"

    body = f"""<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<title>{escape(slug)} — Chain Censorship Events</title>
<link rel="stylesheet" href="{relroot}/styles.css">
</head><body>
<nav class="breadcrumb"><a href="{relroot}/index.html">← All events</a></nav>
<h1>{escape(title)}</h1>
<p>
  {pill(ec, ec)}
  {pill(status, status)}
  <span class="meta">schema {escape(event.get('schema_version','—'))} ·
   last verified {escape(event.get('last_verified','—'))} ·
   {len(addrs)} target addresses ·
   {len(event.get('observations') or [])} observations</span>
</p>
{related_html}

<h2>Trigger</h2>
{render_trigger(event.get('trigger') or {})}

<h2>Target</h2>
<p>
  <strong>Kind:</strong> <code>{escape(target.get('kind','—'))}</code> &nbsp;
  <strong>Enumeration:</strong> <code>{escape(target.get('enumeration','—'))}</code> &nbsp;
  <strong>Protocol:</strong> <code>{escape(target.get('protocol') or '—')}</code> &nbsp;
  <strong>Chains:</strong> <code>{escape(", ".join(target.get('chains') or []) or '—')}</code>
</p>
<p class="meta">{escape(str(target.get('enumeration_note',''))[:400])}</p>
{addrs_html}

<h2>Coverage</h2>
{render_coverage(event.get('coverage') or [])}

<h2>Observations</h2>
{render_observations(event.get('observations') or [])}

<h2>Analysis notes</h2>
<pre>{escape(str(event.get('analysis_notes','(none)')))}</pre>

<h2>Scoped claim</h2>
<blockquote><em>{escape(str(event.get('scoped_claim','(none)')))}</em></blockquote>

<h2>Tags</h2>
<p>{" ".join(pill(t) for t in (event.get('tags') or []))}</p>

<h2>Raw YAML</h2>
<p><a href="{relroot}/raw/{escape(slug)}.yaml">View raw YAML</a></p>

<footer>
  Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} from <code>events/{escape(slug)}.yaml</code>.
  Every primary source has a sha256 body_hash; values above truncated to 23 chars for readability.
  See repo for full hashes + archival anchors.
</footer>
</body></html>"""
    return body


def render_index(events):
    ec_counts = collections.Counter(e.get("empirical_shape") for e in events)
    tier_counts = collections.Counter(e.get("admission_tier") for e in events)
    stratum_counts = collections.Counter(e.get("research_stratum") for e in events)
    status_counts = collections.Counter(e.get("status") for e in events)
    trigger_counts = collections.Counter((e.get("trigger") or {}).get("type") for e in events)
    jur_counts = collections.Counter()
    chain_counts = collections.Counter()
    for e in events:
        for j in e.get("jurisdiction") or []:
            jur_counts[j] += 1
        for c in (e.get("target") or {}).get("chains") or []:
            chain_counts[c] += 1
    year_counts = collections.Counter()
    for e in events:
        ts = str((e.get("trigger") or {}).get("timestamp", ""))[:4]
        if ts:
            year_counts[ts] += 1

    def sorted_kv(c):
        return "<br>".join(f"<code>{escape(k)}</code>: <strong>{v}</strong>" for k, v in c.most_common())

    events_sorted = sorted(events, key=lambda e: str((e.get("trigger") or {}).get("timestamp", "")))
    rows = []
    for e in events_sorted:
        slug = e.get("id", "—")
        ts = str((e.get("trigger") or {}).get("timestamp", ""))[:10]
        ec = e.get("empirical_shape", "—")
        tier = e.get("admission_tier", "—")
        stratum = e.get("research_stratum", "—")
        tg_type = (e.get("trigger") or {}).get("type", "—")
        actor_type = (e.get("target") or {}).get("actor_type") or (e.get("target") or {}).get("protocol") or "—"
        n_obs = len(e.get("observations") or [])
        n_addr = len((e.get("target") or {}).get("addresses") or [])
        chains = ", ".join((e.get("target") or {}).get("chains") or []) or "—"
        jur = ", ".join(e.get("jurisdiction") or [])
        rows.append(f"""
        <tr data-slug="{escape(slug)}" data-eventclass="{escape(ec)}" data-year="{escape(ts[:4])}" data-trigger="{escape(tg_type)}">
          <td><code>{escape(ts)}</code></td>
          <td><a href="events/{escape(slug)}.html">{escape(slug)}</a></td>
          <td>{pill(ec, ec)}</td>
          <td><code>{escape(tg_type)}</code></td>
          <td><code>{escape(actor_type)}</code></td>
          <td class="meta">{escape(chains)}</td>
          <td class="meta">{escape(jur)}</td>
          <td class="meta">{n_addr} addrs · {n_obs} obs</td>
        </tr>""")

    return f"""<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<title>Chain Censorship Events Database</title>
<link rel="stylesheet" href="styles.css">
</head><body>
<h1>Chain Censorship Events Database</h1>

<p>Stratified-complete catalog of crypto censorship events: OFAC SDN
designations, DOJ seizures, nation-state bans, SEC enforcement, and
issuer-policy actions. Every event YAML carries one or more primary
sources with sha256 <code>body_hash</code> for independent reproduction.</p>

<p class="meta">Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}.
{len(events)} events; all validate via <code>scripts/validate.py</code>.</p>

<div class="stat-grid">
  <div class="stat-card"><div class="stat-number">{len(events)}</div><div class="stat-label">admitted events</div></div>
  <div class="stat-card"><div class="stat-number">{ec_counts.get('cascade', 0)}</div><div class="stat-label">cascade (3+ layers)</div></div>
  <div class="stat-card"><div class="stat-number">{ec_counts.get('comparison', 0)}</div><div class="stat-label">comparison (1–2 layers)</div></div>
  <div class="stat-card"><div class="stat-number">{ec_counts.get('null_event', 0)}</div><div class="stat-label">null_event (0 layers)</div></div>
</div>

<h2>Distribution</h2>
<table>
<tr><th>By year</th><th>By trigger type</th><th>By chain</th><th>By jurisdiction</th></tr>
<tr>
  <td>{sorted_kv(collections.Counter({k:v for k,v in year_counts.items() if k.isdigit()}))}</td>
  <td>{sorted_kv(trigger_counts)}</td>
  <td>{sorted_kv(chain_counts)}</td>
  <td>{sorted_kv(jur_counts)}</td>
</tr>
</table>

<h2>Events (sorted by trigger date)</h2>
<div class="filter-bar">
  <label>Filter:
    <input type="text" id="filter-input" placeholder="slug / trigger / year / chain…" onkeyup="filterRows()" style="padding: 4px 8px; width: 240px;">
  </label>
  <label>Event class:
    <select id="filter-class" onchange="filterRows()">
      <option value="">all</option>
      <option value="cascade">cascade</option>
      <option value="comparison">comparison</option>
      <option value="null_event">null_event</option>
    </select>
  </label>
</div>

<table id="events-table">
<thead><tr>
  <th>Date</th><th>Slug</th><th>Class</th><th>Trigger</th>
  <th>Actor type</th><th>Chains</th><th>Jurisdiction</th><th>Size</th>
</tr></thead>
<tbody>{"".join(rows)}</tbody>
</table>

<script>
function filterRows() {{
  const q = document.getElementById('filter-input').value.toLowerCase();
  const cls = document.getElementById('filter-class').value;
  const tbody = document.querySelector('#events-table tbody');
  for (const tr of tbody.rows) {{
    const textMatch = !q || tr.innerText.toLowerCase().includes(q);
    const clsMatch = !cls || tr.getAttribute('data-eventclass') === cls;
    tr.style.display = (textMatch && clsMatch) ? '' : 'none';
  }}
}}
</script>

<h2>Framework (3 layers)</h2>
<p>Three tools are built on top of the event database. Each has a distinct audience and intentionally stays away from making decisions on the user's behalf. Read <a href="raw/../docs/limitations-and-use.md"><code>docs/limitations-and-use.md</code></a> before using any output.</p>
<div class="stat-grid">
  <div class="stat-card">
    <div class="stat-label"><strong>A. Evidence Chain</strong></div>
    <p class="meta">Per-event structured argument: claim → observations → primary sources (with body_hash) → honest gaps. Use for papers, amicus briefs, expert reports. Generate via <code>scripts/render_evidence_chain.py &lt;slug&gt;</code>. Output in <a href="raw/../analysis/evidence-chains/"><code>analysis/evidence-chains/</code></a>.</p>
  </div>
  <div class="stat-card">
    <div class="stat-label"><strong>B. Comparable-Case Finder</strong></div>
    <p class="meta">Case-based retrieval of top-N historical precedents matching a proposed action, with transparent similarity weights and explicit divergence factors. <strong>Not a predictive model.</strong> Generate via <code>scripts/find_comparable_cases.py</code>.</p>
  </div>
  <div class="stat-card">
    <div class="stat-label"><strong>C. Decision Rubric</strong></div>
    <p class="meta">Hand-followed structural checklist distilling the dataset's findings into pattern classes. See <a href="raw/../docs/decision-rubric.md"><code>docs/decision-rubric.md</code></a>. Comparative only — never substitute for expert judgment.</p>
  </div>
</div>

<h2>About</h2>
<p>Schema version 0.2.0. Each event carries:</p>
<ul>
  <li><strong>trigger</strong>: legal / corporate action (OFAC SDN, DOJ indictment, etc.) with primary-source citations;</li>
  <li><strong>target</strong>: address set / entity / domain with chain enumeration;</li>
  <li><strong>coverage</strong>: per-layer status (l0_network / l1_consensus / l3_rpc / l4_frontend / asset_onchain / offramp_cex);</li>
  <li><strong>observations</strong>: observed_change / observed_no_change per layer with attribution grading;</li>
  <li><strong>scoped_claim</strong>: the defensible single sentence the event supports.</li>
</ul>

<p>See <code>docs/methodology.md</code> in the repository for admission rules.</p>

<footer>Repo: <code>p1-event-db</code> · Primary sources under <code>sources/</code> all carry sha256 body_hash for reproduction.</footer>
</body></html>"""


def copy_yaml_raw(events_dir: pathlib.Path, site_dir: pathlib.Path) -> None:
    raw_dir = site_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    for src in events_dir.glob("*.yaml"):
        shutil.copy2(src, raw_dir / src.name)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--events-dir", default=str(EVENTS_DIR))
    p.add_argument("--site-dir", default=str(SITE_DIR))
    args = p.parse_args()

    events_dir = pathlib.Path(args.events_dir)
    site_dir = pathlib.Path(args.site_dir)
    if site_dir.exists():
        shutil.rmtree(site_dir)
    site_dir.mkdir(parents=True)
    (site_dir / "events").mkdir(parents=True)

    events = []
    for f in sorted(events_dir.glob("*.yaml")):
        events.append(yaml.safe_load(f.read_text()))
    print(f"[render_site] loaded {len(events)} events")

    (site_dir / "styles.css").write_text(CSS)

    # Render each event page
    for e in events:
        slug = e.get("id", "unknown")
        (site_dir / "events" / f"{slug}.html").write_text(render_event(e))

    # Render index
    (site_dir / "index.html").write_text(render_index(events))

    # Copy raw YAMLs
    copy_yaml_raw(events_dir, site_dir)

    print(f"[render_site] wrote {site_dir}/index.html + {len(events)} per-event pages + raw/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
