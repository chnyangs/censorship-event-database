#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Render events/*.yaml into a static HTML site under site/.

No external dependencies beyond PyYAML. Emits:
  - site/index.html      (browse + filter + sort all events)
  - site/events/<slug>.html  (per-event detail page with cascade visuals)
  - site/raw/<slug>.yaml (copies for direct linking)
  - site/styles.css      (CSS variables + dark mode + print)
  - site/site.js         (filters + URL state + theme toggle + column sort)

Design choices (2026-04 rewrite):
  - Coherent palette: separate pill families for status / shape / tier /
    attribution / layer. No single color is reused across semantic axes.
  - Cascade is the primary artifact — every event page shows a 6-layer dot
    summary + a horizontal timeline scaled to delta_hours.
  - Index filters are chip-based across five facets (class / stratum / tier /
    year / chain), sync to URL hash so views are shareable.
  - Prefers-color-scheme dark mode + manual toggle, persisted in localStorage.
  - Semantic HTML5 + visible focus rings + keyboard-friendly controls.
"""

from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import html
import json
import pathlib
import re
import shutil
import sys
from datetime import datetime
from typing import Any

import yaml


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
DOCS_DIR = REPO_ROOT / "docs"
SITE_DIR = REPO_ROOT / "site"
SITE_MARKER = ".render_site_output"

# Shared dataset-identity accessor (see scripts/_dataset_meta.py).
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import load_meta, now_utc_datetime  # noqa: E402

# Canonical layer ordering used everywhere a cascade is shown.
LAYER_ORDER = [
    "l0_network", "l1_consensus", "l3_rpc",
    "l4_frontend", "asset_onchain", "offramp_cex",
]
LAYER_LABEL = {
    "l0_network":    "L0 network",
    "l1_consensus":  "L1 consensus",
    "l3_rpc":        "L3 RPC",
    "l4_frontend":   "L4 frontend",
    "asset_onchain": "Asset on-chain",
    "offramp_cex":   "Off-ramp CEX",
}
LAYER_SHORT = {
    "l0_network":    "L0",
    "l1_consensus":  "L1",
    "l3_rpc":        "L3",
    "l4_frontend":   "L4",
    "asset_onchain": "Asset",
    "offramp_cex":   "CEX",
}

# Acronyms that should retain uppercase when a slug is title-cased.
ACRONYMS = {
    "ofac", "doj", "sec", "cftc", "eu", "us", "uk", "un",
    "rbi", "cbn", "cbrt", "pboc", "dprk", "irgc", "nl",
    "fiod", "mica", "ru", "cn", "in", "de", "pl", "sg", "jp",
    "kr", "ca", "tr", "ng", "ir", "ooki", "cex", "dao", "rpc",
    "sdn", "ai", "api", "cdn", "kyc", "sto",
}

# Timeline maximum window (hours). Observations beyond this are flagged off-axis.
TIMELINE_MAX_HOURS = 168.0   # 7 days — covers most cascades
TIMELINE_TICKS = [0, 6, 12, 24, 48, 72, 168]

# Human-audit work queue. Keep this list aligned with human-audit.md and the
# null-case LLM pre-audit. These are the cases auditors can review through the
# static Human Audit Console; the console only generates records/templates and
# does not stamp last_human_audit automatically.
NULL_DENOMINATOR_AUDIT_CASES = [
    "iran-ransomware-ofac-2018",
    "irgc-ransomware-ofac-2022",
    "lazarus-entity-ofac-2019",
    "lazarus-laundering-ofac-2020",
    "lockbit-leader-ofac-2024",
    "matveev-ofac-2023",
    "pertsev-nl-arrest-2022",
    "russian-cybercrime-infra-ofac-2025",
    "sec-v-uniswap-wells-notice-2024",
    "sichuan-silence-ofac-2024",
    "sinbad-ofac-2023",
    "storm-semenov-doj-2023",
    "zservers-ofac-2025",
]

NULL_AUDIT_PRESTATUS = {
    "iran-ransomware-ofac-2018": ("pass_pre_audit", "Compare pre/post Enexchanger Wayback redirect-shell snapshots before narrative use."),
    "sinbad-ofac-2023": ("pass_pre_audit", "Compare event-day and +10 day sinbad.io Wayback snapshots before narrative use."),
    "sec-v-uniswap-wells-notice-2024": ("fail_pre_audit", "Highest risk: current anchors do not replay app.uniswap.org operational uptime across the full Wells-notice window."),
}


# ---------------------------------------------------------------------------
# Static assets (CSS + JS)
# ---------------------------------------------------------------------------

STATIC_CSS = """\
:root {
  color-scheme: light dark;

  --bg: #ffffff;
  --bg-alt: #f6f8fb;
  --bg-sunken: #eef1f6;
  --bg-card: #ffffff;
  --border: #dee2e7;
  --border-strong: #b4bac2;
  --text: #1a1d21;
  --text-muted: #5e6670;
  --text-soft: #7b8188;

  --link: #0a58d6;
  --link-hover: #003a94;
  --focus-ring: #4c8dff;

  --accent: #5d5fef;
  --accent-soft: #eeefff;

  /* Status (semantic) */
  --ok-fg: #1d5827;    --ok-bg: #dff5d6;
  --warn-fg: #6d4300;  --warn-bg: #fdecc0;
  --bad-fg: #7a1d1d;   --bad-bg: #fbd5d5;
  --na-fg: #4a5058;    --na-bg: #e6e8ec;

  /* Empirical shape — purple scale */
  --shape-cascade-fg: #4c1d95;    --shape-cascade-bg: #ece0ff;
  --shape-comparison-fg: #1e40af; --shape-comparison-bg: #dde7ff;
  --shape-null-fg: #374151;       --shape-null-bg: #e5e8ef;

  /* Admission tier — gold / indigo / gray */
  --tier-anchor-fg: #78350f;     --tier-anchor-bg: #fdeecb;
  --tier-empirical-fg: #3730a3;  --tier-empirical-bg: #e0e7ff;
  --tier-null-fg: #4b5563;       --tier-null-bg: #e5e7eb;

  /* Attribution */
  --attr-direct-fg: #7a1d1d;    --attr-direct-bg: #fbd5d5;
  --attr-plausible-fg: #6d4300; --attr-plausible-bg: #fdecc0;
  --attr-unknown-fg: #4a5058;   --attr-unknown-bg: #e6e8ec;
  --attr-none-fg: #4b5563;      --attr-none-bg: #eef0f4;

  /* Cascade layer qualitative palette */
  --layer-l0_network: #3b82f6;
  --layer-l1_consensus: #8b5cf6;
  --layer-l3_rpc: #ec4899;
  --layer-l4_frontend: #f59e0b;
  --layer-asset_onchain: #10b981;
  --layer-offramp_cex: #06b6d4;

  --radius-sm: 4px;
  --radius: 8px;
  --radius-lg: 14px;

  --shadow-sm: 0 1px 2px rgba(15,20,35,.06);
  --shadow: 0 4px 14px rgba(15,20,35,.08);

  --font-body: "Aptos", "IBM Plex Sans", "Segoe UI", sans-serif;
  --font-display: "Fraunces", Georgia, serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}

/* Dark palette — auto by prefers-color-scheme, manual via [data-theme="dark"] */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #0d1017;
    --bg-alt: #141922;
    --bg-sunken: #1a1f29;
    --bg-card: #161b25;
    --border: #272d39;
    --border-strong: #3b4353;
    --text: #e8eaef;
    --text-muted: #9da4b0;
    --text-soft: #7e8593;
    --link: #79a9ff;
    --link-hover: #a7c5ff;
    --focus-ring: #79a9ff;
    --accent: #a5a9ff;
    --accent-soft: #242644;

    --ok-fg: #93e6a8;    --ok-bg: #14391f;
    --warn-fg: #ffd873;  --warn-bg: #3d2a0b;
    --bad-fg: #ffb1b1;   --bad-bg: #3c1616;
    --na-fg: #a5abb8;    --na-bg: #222833;

    --shape-cascade-fg: #d8bfff;    --shape-cascade-bg: #2c1b48;
    --shape-comparison-fg: #bcd0ff; --shape-comparison-bg: #1b2a54;
    --shape-null-fg: #cbd0db;       --shape-null-bg: #232831;

    --tier-anchor-fg: #ffd778;     --tier-anchor-bg: #3b2607;
    --tier-empirical-fg: #b6bffa;  --tier-empirical-bg: #1d2250;
    --tier-null-fg: #c5cad4;       --tier-null-bg: #252a33;

    --attr-direct-fg: #ffb1b1;    --attr-direct-bg: #3c1616;
    --attr-plausible-fg: #ffd873; --attr-plausible-bg: #3d2a0b;
    --attr-unknown-fg: #a5abb8;   --attr-unknown-bg: #222833;
    --attr-none-fg: #c5cad4;      --attr-none-bg: #1f242d;
  }
}
:root[data-theme="dark"] {
  --bg: #0d1017;
  --bg-alt: #141922;
  --bg-sunken: #1a1f29;
  --bg-card: #161b25;
  --border: #272d39;
  --border-strong: #3b4353;
  --text: #e8eaef;
  --text-muted: #9da4b0;
  --text-soft: #7e8593;
  --link: #79a9ff;
  --link-hover: #a7c5ff;
  --focus-ring: #79a9ff;
  --accent: #a5a9ff;
  --accent-soft: #242644;
  --ok-fg: #93e6a8;    --ok-bg: #14391f;
  --warn-fg: #ffd873;  --warn-bg: #3d2a0b;
  --bad-fg: #ffb1b1;   --bad-bg: #3c1616;
  --na-fg: #a5abb8;    --na-bg: #222833;
  --shape-cascade-fg: #d8bfff;    --shape-cascade-bg: #2c1b48;
  --shape-comparison-fg: #bcd0ff; --shape-comparison-bg: #1b2a54;
  --shape-null-fg: #cbd0db;       --shape-null-bg: #232831;
  --tier-anchor-fg: #ffd778;     --tier-anchor-bg: #3b2607;
  --tier-empirical-fg: #b6bffa;  --tier-empirical-bg: #1d2250;
  --tier-null-fg: #c5cad4;       --tier-null-bg: #252a33;
  --attr-direct-fg: #ffb1b1;    --attr-direct-bg: #3c1616;
  --attr-plausible-fg: #ffd873; --attr-plausible-bg: #3d2a0b;
  --attr-unknown-fg: #a5abb8;   --attr-unknown-bg: #222833;
  --attr-none-fg: #c5cad4;      --attr-none-bg: #1f242d;
}

* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body {
  margin: 0;
  font-family: var(--font-body);
  background:
    radial-gradient(circle at 12% -10%, color-mix(in srgb, var(--accent) 16%, transparent), transparent 34rem),
    radial-gradient(circle at 92% 5%, color-mix(in srgb, var(--layer-asset_onchain) 12%, transparent), transparent 30rem),
    var(--bg);
  color: var(--text);
  line-height: 1.55;
  font-size: 16px;
  -webkit-font-smoothing: antialiased;
}
:focus-visible {
  outline: 2px solid var(--focus-ring);
  outline-offset: 2px;
  border-radius: var(--radius-sm);
}
a { color: var(--link); text-decoration: none; }
a:hover { text-decoration: underline; color: var(--link-hover); }
code, pre, kbd { font-family: var(--font-mono); font-size: 0.92em; }
pre {
  background: var(--bg-sunken); color: var(--text);
  padding: 12px 14px; overflow-x: auto;
  border-radius: var(--radius); border: 1px solid var(--border);
  white-space: pre-wrap; word-break: break-word;
}
hr { border: 0; border-top: 1px solid var(--border); margin: 2rem 0; }

/* ------------------------------------------------------------------- layout */
.page {
  max-width: 1180px; margin: 0 auto; padding: 0 1.2rem 4rem;
}
.site-header {
  position: sticky; top: 0; z-index: 50;
  background: color-mix(in srgb, var(--bg) 88%, transparent);
  border-bottom: 1px solid var(--border);
  backdrop-filter: saturate(1.3) blur(10px);
}
.site-header-inner {
  max-width: 1180px; margin: 0 auto;
  padding: 10px 1.2rem; display: flex; align-items: center; gap: 1rem;
}
.brand {
  font-weight: 700; font-size: 0.95rem; letter-spacing: -0.01em;
  color: var(--text); white-space: nowrap;
}
.brand a { color: inherit; }
.brand-tag {
  color: var(--text-muted); font-weight: 500; margin-left: 0.4rem; font-size: 0.88rem;
}
.header-spacer { flex: 1; }
.header-link {
  color: var(--text-muted); font-size: 0.9rem;
}
.header-link + .header-link { margin-left: 1rem; }
.theme-toggle {
  background: transparent; border: 1px solid var(--border);
  color: var(--text); border-radius: var(--radius); padding: 4px 10px;
  font-size: 0.85rem; cursor: pointer;
}
.theme-toggle:hover { background: var(--bg-alt); }

h1 {
  font-family: var(--font-display);
  font-size: 1.9rem; letter-spacing: -0.02em; margin: 1.6rem 0 0.4rem;
  line-height: 1.2;
}
h2 {
  font-size: 1.25rem; margin: 2.2rem 0 0.8rem; letter-spacing: -0.01em;
  padding-bottom: 0.3rem; border-bottom: 1px solid var(--border);
}
h3 { font-size: 1.03rem; margin: 1.4rem 0 0.4rem; }
.meta { color: var(--text-muted); font-size: 0.88rem; }
.muted { color: var(--text-muted); }

/* ------------------------------------------------------------- dashboard */
.dashboard-hero {
  display: grid; grid-template-columns: minmax(0, 1.45fr) minmax(280px, .75fr);
  gap: 1rem; align-items: stretch;
  margin-top: 1.4rem;
}
.hero-copy, .snapshot-panel, .signal-card, .artifact-card, .layer-card, .filter-drawer {
  background: color-mix(in srgb, var(--bg-card) 92%, transparent);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
}
.hero-copy {
  padding: 1.7rem 1.8rem;
  min-height: 360px;
  position: relative; overflow: hidden;
}
.hero-copy::after {
  content: ""; position: absolute; inset: auto -8% -40% 42%;
  height: 220px; border-radius: 999px;
  background: linear-gradient(90deg,
    color-mix(in srgb, var(--layer-l4_frontend) 22%, transparent),
    color-mix(in srgb, var(--layer-asset_onchain) 24%, transparent),
    color-mix(in srgb, var(--layer-offramp_cex) 20%, transparent));
  filter: blur(10px); opacity: .8; pointer-events: none;
}
.hero-copy > * { position: relative; z-index: 1; }
.hero-kicker {
  display: inline-flex; gap: .45rem; align-items: center;
  color: var(--text-muted); text-transform: uppercase; letter-spacing: .08em;
  font-size: .76rem; font-weight: 700;
}
.hero-kicker::before {
  content: ""; width: 34px; height: 2px; background: var(--accent);
  border-radius: 2px;
}
.dashboard-hero h1 {
  font-size: clamp(2.1rem, 6vw, 4.8rem);
  max-width: 12ch;
  margin: .75rem 0 .9rem;
  line-height: .95;
}
.hero-lede {
  font-size: 1.04rem; color: var(--text-muted); max-width: 66ch;
}
.hero-actions { display: flex; gap: .7rem; flex-wrap: wrap; margin-top: 1.2rem; }
.button {
  display: inline-flex; align-items: center; justify-content: center;
  border-radius: 999px; padding: .62rem .95rem;
  border: 1px solid var(--border-strong);
  background: var(--text); color: var(--bg);
  font-weight: 700; font-size: .88rem;
}
.button:hover { text-decoration: none; opacity: .9; color: var(--bg); }
.button.secondary { background: var(--bg-card); color: var(--text); }
.button.secondary:hover { color: var(--text); border-color: var(--text-muted); }
.snapshot-panel {
  padding: 1rem;
  display: grid; gap: .75rem;
  align-content: start;
}
.snapshot-head {
  padding: .9rem; border-radius: var(--radius);
  background: linear-gradient(135deg, var(--bg-alt), var(--bg-card));
  border: 1px solid var(--border);
}
.snapshot-head .label, .status-line .label, .artifact-card .label {
  color: var(--text-muted); text-transform: uppercase; letter-spacing: .07em;
  font-size: .72rem; font-weight: 700;
}
.snapshot-head .version {
  font-family: var(--font-display);
  font-size: 2.1rem; line-height: 1; margin-top: .25rem;
}
.status-line {
  display: grid; grid-template-columns: 1fr auto; gap: .5rem;
  align-items: center; padding: .72rem .8rem;
  border-radius: var(--radius); border: 1px solid var(--border);
  background: var(--bg-alt);
}
.status-line strong { font-size: .93rem; }
.status-dot {
  width: 10px; height: 10px; border-radius: 50%;
  background: var(--ok-fg); box-shadow: 0 0 0 4px color-mix(in srgb, var(--ok-fg) 14%, transparent);
}
.status-dot.warn {
  background: var(--warn-fg); box-shadow: 0 0 0 4px color-mix(in srgb, var(--warn-fg) 16%, transparent);
}
.status-dot.info {
  background: var(--accent); box-shadow: 0 0 0 4px color-mix(in srgb, var(--accent) 16%, transparent);
}
.section-heading {
  display: flex; justify-content: space-between; align-items: end; gap: 1rem;
  margin: 2rem 0 .8rem;
}
.section-heading h2 { margin: 0; border: 0; padding: 0; }
.section-heading p { margin: 0; max-width: 62ch; }
.signal-grid {
  display: grid; grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: .85rem; margin: 1rem 0 1.4rem;
}
.signal-card {
  padding: 1rem;
  position: relative; overflow: hidden;
}
.signal-card::before {
  content: ""; position: absolute; inset: 0 auto 0 0; width: 4px;
  background: var(--accent);
}
.signal-card.warn::before { background: var(--warn-fg); }
.signal-card.risk::before { background: var(--bad-fg); }
.signal-number {
  font-family: var(--font-display);
  font-size: 2.25rem; line-height: 1;
  letter-spacing: -.04em;
}
.signal-label { color: var(--text-muted); font-size: .86rem; margin-top: .25rem; }
.layer-board {
  display: grid; grid-template-columns: repeat(6, minmax(0, 1fr));
  gap: .7rem;
}
.layer-card {
  padding: .9rem;
  border-top: 4px solid var(--layer-color);
}
.layer-card h3 {
  margin: 0 0 .55rem;
  font-size: .9rem; font-family: var(--font-mono); color: var(--text);
}
.layer-metrics {
  display: grid; gap: .35rem; font-size: .82rem; color: var(--text-muted);
}
.layer-metrics strong { color: var(--text); font-variant-numeric: tabular-nums; }
.layer-meter {
  height: 7px; border-radius: 999px; background: var(--bg-sunken);
  overflow: hidden; margin-top: .7rem;
}
.layer-meter span {
  display: block; height: 100%; width: var(--pct);
  background: var(--layer-color); border-radius: inherit;
}
.artifact-grid {
  display: grid; grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: .85rem;
}
.artifact-card {
  padding: 1rem; display: flex; flex-direction: column; gap: .55rem;
  min-height: 150px;
}
.artifact-card h3 { margin: 0; font-size: 1rem; }
.artifact-card p { margin: 0; color: var(--text-muted); font-size: .88rem; }
.artifact-card a.stretch {
  margin-top: auto; font-weight: 700; font-size: .85rem;
}
.boundary-note {
  margin: 1rem 0; padding: 1rem 1.1rem;
  border: 1px solid color-mix(in srgb, var(--warn-fg) 36%, var(--border));
  border-left: 5px solid var(--warn-fg);
  background: color-mix(in srgb, var(--warn-bg) 24%, var(--bg-card));
  border-radius: var(--radius);
}
.boundary-note strong { color: var(--text); }
.filter-drawer {
  margin: .8rem 0 1rem;
  overflow: clip;
}
.filter-drawer summary {
  list-style: none; cursor: pointer;
  padding: .9rem 1rem;
  display: flex; justify-content: space-between; align-items: center; gap: 1rem;
}
.filter-drawer summary::-webkit-details-marker { display: none; }
.filter-drawer summary .title { font-weight: 700; }
.filter-drawer summary .hint { color: var(--text-muted); font-size: .85rem; }
.filter-drawer[open] summary { border-bottom: 1px solid var(--border); }
.filter-drawer .filter-bar {
  position: static; top: auto; margin: 0; padding: .85rem 1rem;
  border: 0; background: transparent;
}

/* ------------------------------------------------------------- audit console */
.audit-console {
  display: grid; gap: 1rem;
  margin-top: 1rem;
}
.audit-panel {
  background: color-mix(in srgb, var(--bg-card) 94%, transparent);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
  padding: 1rem;
}
.audit-panel.priority-high {
  border-color: color-mix(in srgb, var(--bad-fg) 36%, var(--border));
  border-left: 5px solid var(--bad-fg);
}
.audit-panel.priority-warn {
  border-left: 5px solid var(--warn-fg);
}
.audit-panel h3 {
  margin-top: 0;
}
.audit-grid {
  display: grid; grid-template-columns: minmax(0, .9fr) minmax(320px, 1.1fr);
  gap: 1rem;
}
.audit-links, .audit-paths {
  display: grid; gap: .35rem;
  margin: .7rem 0;
}
.audit-links a, .audit-paths a, .audit-paths code {
  display: block;
  overflow-wrap: anywhere;
}
.audit-form {
  display: grid; gap: .7rem;
}
.audit-form label {
  display: grid; gap: .25rem;
  color: var(--text-muted);
  font-size: .84rem;
}
.audit-form input, .audit-form select, .audit-form textarea {
  width: 100%;
  border: 1px solid var(--border-strong);
  border-radius: var(--radius);
  padding: .55rem .65rem;
  background: var(--bg);
  color: var(--text);
  font: inherit;
}
.audit-form textarea {
  min-height: 90px;
  resize: vertical;
}
.audit-checks {
  display: grid; gap: .35rem;
  padding: .65rem;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--bg-alt);
}
.audit-checks label {
  display: flex; align-items: start; gap: .45rem;
  color: var(--text);
  font-size: .86rem;
}
.audit-checks input {
  width: auto; margin-top: .2rem;
}
.audit-error {
  margin: .65rem 0;
  padding: .6rem .75rem;
  border: 1px solid var(--bad);
  border-radius: var(--radius);
  color: var(--bad);
  background: color-mix(in oklab, var(--bad) 8%, var(--bg));
  font-size: .88rem;
}
.audit-error[hidden] {
  display: none;
}
.audit-output-wrap {
  display: none;
  margin-top: .8rem;
}
.audit-output-wrap.visible {
  display: block;
}
.audit-output {
  min-height: 180px;
  font-family: var(--font-mono);
  font-size: .82rem;
}
.audit-result-actions {
  display: flex; gap: .5rem; flex-wrap: wrap;
  margin-top: .5rem;
}
.audit-note {
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--bg-alt);
  padding: .7rem .8rem;
}
.audit-task-list {
  display: grid; grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: .7rem;
}
.audit-task-list .audit-panel {
  min-height: 150px;
}

/* ------------------------------------------------------------- legacy hero */
.hero {
  margin-top: 1.6rem; padding: 1.6rem 1.8rem 1.2rem;
  background: linear-gradient(180deg, var(--bg-alt), transparent);
  border: 1px solid var(--border); border-radius: var(--radius-lg);
}
.hero h1 { margin-top: 0; }
.hero-lede { font-size: 1.02rem; color: var(--text-muted); max-width: 68ch; }
.hero-chips { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 1rem; }
.hero-chips a {
  color: var(--text); background: var(--bg-card);
  border: 1px solid var(--border); padding: 4px 10px;
  border-radius: 999px; font-size: 0.85rem;
}
.hero-chips a:hover { border-color: var(--border-strong); text-decoration: none; }

/* ------------------------------------------------------- stat cards */
.stat-grid {
  display: grid; gap: 0.9rem; margin: 1.4rem 0;
  grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
}
.stat-card {
  padding: 14px 16px; background: var(--bg-card);
  border: 1px solid var(--border); border-radius: var(--radius);
  position: relative; overflow: hidden;
}
.stat-card::before {
  content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 3px;
  background: var(--accent);
}
.stat-card.shape-cascade::before { background: var(--shape-cascade-fg); }
.stat-card.shape-comparison::before { background: var(--shape-comparison-fg); }
.stat-card.shape-null_event::before { background: var(--shape-null-fg); }
.stat-number {
  font-size: 1.9rem; font-weight: 700; line-height: 1;
  letter-spacing: -0.02em; color: var(--text);
}
.stat-label {
  color: var(--text-muted); font-size: 0.86rem; margin-top: 2px;
}

/* --------------------------------------------------------- distribution */
.distribution {
  display: grid; gap: 0.9rem; margin: 1rem 0 1.6rem;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}
.dist-card {
  padding: 14px 16px; background: var(--bg-card);
  border: 1px solid var(--border); border-radius: var(--radius);
}
.dist-card h3 { margin: 0 0 0.6rem; font-size: 0.88rem;
  text-transform: uppercase; letter-spacing: 0.06em; color: var(--text-muted);
  border: 0;
}
.dist-row {
  display: flex; align-items: center; gap: 0.6rem;
  font-size: 0.9rem; padding: 3px 0;
}
.dist-row .k { flex: 0 0 7.5em; color: var(--text); font-family: var(--font-mono); font-size: 0.85em; }
.dist-row .v { flex: 0 0 3em; text-align: right; color: var(--text-muted); font-variant-numeric: tabular-nums; }
.dist-row .bar {
  flex: 1; height: 6px; background: var(--bg-sunken); border-radius: 3px; overflow: hidden;
}
.dist-row .bar-fill {
  display: block; height: 100%; background: var(--accent); border-radius: 3px;
}

/* ---------------------------------------------------------- filter bar */
.filter-bar {
  position: sticky; top: 54px; z-index: 40;
  background: var(--bg);
  padding: 0.7rem 0.1rem; margin: 0.5rem 0; border-bottom: 1px solid var(--border);
}
.filter-row { display: flex; align-items: center; gap: 0.8rem; flex-wrap: wrap; }
.filter-row + .filter-row { margin-top: 0.5rem; }
.filter-search {
  flex: 1 1 240px; min-width: 220px;
  display: flex; align-items: center; gap: 0.4rem;
  border: 1px solid var(--border); border-radius: var(--radius);
  background: var(--bg-card); padding: 4px 10px;
}
.filter-search input {
  border: 0; outline: 0; background: transparent; color: var(--text);
  width: 100%; font-size: 0.95rem; padding: 4px 0;
}
.filter-group {
  display: flex; gap: 4px; flex-wrap: wrap; align-items: center;
}
.filter-group .glabel {
  font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.06em;
  color: var(--text-muted); margin-right: 0.4em;
}
.chip {
  font-size: 0.82rem; padding: 3px 10px; border-radius: 999px;
  border: 1px solid var(--border); background: var(--bg-card);
  color: var(--text); cursor: pointer; font-family: inherit;
  transition: border-color .12s, background .12s;
  white-space: nowrap;
}
.chip:hover { border-color: var(--border-strong); }
.chip[aria-pressed="true"] {
  background: var(--accent-soft); border-color: var(--accent);
  color: var(--text);
}
.chip-reset {
  font-size: 0.78rem; color: var(--text-muted);
  background: transparent; border: 0; padding: 3px 6px; cursor: pointer;
}
.chip-reset:hover { color: var(--text); }

.result-count {
  margin-left: auto; font-size: 0.85rem; color: var(--text-muted);
  font-variant-numeric: tabular-nums;
}

/* --------------------------------------------------------- events table */
.table-wrap { overflow-x: auto; border: 1px solid var(--border); border-radius: var(--radius); }
table.events {
  width: 100%; border-collapse: collapse; font-size: 0.92rem;
}
table.events thead th {
  position: sticky; top: 54px; z-index: 10;
  background: var(--bg-alt); color: var(--text);
  text-align: left; font-weight: 600; font-size: 0.84rem;
  letter-spacing: 0.02em;
  padding: 9px 12px; border-bottom: 1px solid var(--border);
  cursor: pointer; user-select: none; white-space: nowrap;
}
table.events thead th .arrow {
  display: inline-block; margin-left: 4px; opacity: 0.35;
  font-size: 0.78rem;
}
table.events thead th[aria-sort="ascending"] .arrow,
table.events thead th[aria-sort="descending"] .arrow { opacity: 1; color: var(--accent); }
table.events tbody td {
  padding: 10px 12px; border-top: 1px solid var(--border); vertical-align: middle;
}
table.events tbody tr:hover td { background: var(--bg-alt); }
table.events td.date { font-family: var(--font-mono); color: var(--text-muted); white-space: nowrap; font-size: 0.9em; }
table.events td.slug a { font-weight: 500; }
table.events td.size { color: var(--text-muted); font-variant-numeric: tabular-nums; font-size: 0.87em; white-space: nowrap; }
table.events tr.hidden { display: none; }

/* --------------------------------------------------------- cascade viz */
.cascade-dots {
  display: inline-flex; gap: 4px; align-items: center;
}
.cascade-dots .dot {
  width: 12px; height: 12px; border-radius: 50%;
  background: var(--bg-sunken);
  border: 1.5px solid var(--border-strong);
  position: relative;
}
.cascade-dots .dot.on {
  background: var(--layer-color); border-color: var(--layer-color);
}
.cascade-dots .dot.no-change {
  background: transparent; border-color: var(--layer-color);
  border-style: dashed;
}

.cascade-dots--xl .dot { width: 18px; height: 18px; border-width: 2px; }

/* on-event-page cascade timeline */
.timeline {
  margin: 0.8rem 0 1.4rem; padding: 14px 18px 6px;
  background: var(--bg-card); border: 1px solid var(--border);
  border-radius: var(--radius);
}
.timeline-head {
  display: flex; align-items: baseline; justify-content: space-between;
  font-size: 0.85rem; color: var(--text-muted);
  margin-bottom: 0.8rem;
}
.timeline-row {
  display: grid; grid-template-columns: 6em 1fr; gap: 10px;
  align-items: center; margin-bottom: 5px;
}
.timeline-row .tl-label {
  font-size: 0.82rem; color: var(--text-muted);
  font-family: var(--font-mono);
}
.timeline-row .track {
  position: relative; height: 18px; background: var(--bg-sunken);
  border-radius: 9px;
}
.timeline-row .track::before {
  content: ""; position: absolute; left: 0; top: 50%;
  width: 2px; height: 10px; margin-top: -5px;
  background: var(--text-muted); border-radius: 1px;
}
.timeline-row.has-change .track {
  background: color-mix(in srgb, var(--layer-color) 18%, var(--bg-sunken));
}
.tl-marker {
  position: absolute; top: 50%; transform: translate(-50%, -50%);
  width: 12px; height: 12px; border-radius: 50%;
  background: var(--layer-color);
  box-shadow: 0 0 0 2px var(--bg-card);
}
.tl-marker.no-change {
  background: transparent; border: 2px dashed var(--layer-color); box-shadow: none;
}
.tl-marker.overflow {
  right: 4px; left: auto; transform: translate(0,-50%);
  background: var(--text-muted);
}
.tl-marker[data-delta] { cursor: help; }
.timeline-axis {
  position: relative; height: 24px; margin: 8px 0 0 calc(6em + 10px);
  border-top: 1px dashed var(--border);
}
.timeline-axis .tick {
  position: absolute; top: 0; font-size: 0.72rem; color: var(--text-muted);
  font-family: var(--font-mono); transform: translateX(-50%);
  padding-top: 4px; white-space: nowrap;
}
.timeline-note { font-size: 0.8rem; color: var(--text-muted); margin-top: 0.4rem; }

/* ------------------------------------------------------------- pills */
.pill {
  display: inline-block; padding: 2px 10px; border-radius: 999px;
  font-size: 0.76rem; font-weight: 600; letter-spacing: 0.01em;
  background: var(--na-bg); color: var(--na-fg);
  white-space: nowrap;
}
.pill-neutral, .pill-unknown { background: var(--na-bg); color: var(--na-fg); }
.pill-admitted, .pill-observation_closed { background: var(--ok-bg); color: var(--ok-fg); }
.pill-draft, .pill-observation_active { background: var(--warn-bg); color: var(--warn-fg); }
.pill-rejected { background: var(--bad-bg); color: var(--bad-fg); }

.pill-cascade { background: var(--shape-cascade-bg); color: var(--shape-cascade-fg); }
.pill-comparison { background: var(--shape-comparison-bg); color: var(--shape-comparison-fg); }
.pill-null_event { background: var(--shape-null-bg); color: var(--shape-null-fg); }

.pill-anchor_case { background: var(--tier-anchor-bg); color: var(--tier-anchor-fg); }
.pill-empirical_case { background: var(--tier-empirical-bg); color: var(--tier-empirical-fg); }
.pill-null_case { background: var(--tier-null-bg); color: var(--tier-null-fg); }

.pill-measured { background: var(--ok-bg); color: var(--ok-fg); }
.pill-partially_measured { background: var(--warn-bg); color: var(--warn-fg); }
.pill-not_measured { background: var(--bad-bg); color: var(--bad-fg); }
.pill-not_applicable { background: var(--na-bg); color: var(--na-fg); }

.pill-observed_change { background: #fde2cc; color: #7b2e0b; }
.pill-observed_no_change { background: #dce7fb; color: #1e3a7a; }
.pill-coverage_gap { background: #f5ead2; color: #6d4a0c; }

.pill-direct { background: var(--attr-direct-bg); color: var(--attr-direct-fg); }
.pill-plausible { background: var(--attr-plausible-bg); color: var(--attr-plausible-fg); }
.pill-none { background: var(--attr-none-bg); color: var(--attr-none-fg); }

.pill-layer {
  font-family: var(--font-mono); font-size: 0.74rem;
  background: color-mix(in srgb, var(--layer-color) 15%, transparent);
  color: var(--layer-color);
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) .pill-observed_change { background: #3c2311; color: #ffcfac; }
  :root:not([data-theme="light"]) .pill-observed_no_change { background: #1c2749; color: #bcd0ff; }
  :root:not([data-theme="light"]) .pill-coverage_gap { background: #3a2e16; color: #f0d6a0; }
}
:root[data-theme="dark"] .pill-observed_change { background: #3c2311; color: #ffcfac; }
:root[data-theme="dark"] .pill-observed_no_change { background: #1c2749; color: #bcd0ff; }
:root[data-theme="dark"] .pill-coverage_gap { background: #3a2e16; color: #f0d6a0; }

/* ---------------------------------------------------- event hero */
.event-hero {
  margin-top: 1.4rem; padding: 1.4rem 1.6rem;
  border: 1px solid var(--border); border-radius: var(--radius-lg);
  background: var(--bg-card);
}
.event-hero h1 { margin: 0 0 0.4rem; }
.event-hero .tag-row { display: flex; gap: 0.4rem; flex-wrap: wrap; margin-bottom: 0.8rem; }
.event-hero .scoped-claim {
  margin: 0.9rem 0 0; padding: 0.9rem 1rem;
  background: var(--bg-alt); border-left: 3px solid var(--accent);
  border-radius: var(--radius-sm);
  font-size: 1.02rem; font-style: italic;
}
.event-hero .scoped-claim .label {
  display: block; font-size: 0.72rem; letter-spacing: 0.08em;
  text-transform: uppercase; color: var(--text-muted);
  font-style: normal; margin-bottom: 0.3rem;
}
.event-hero .hero-grid {
  display: grid; gap: 1rem; margin-top: 0.9rem;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
}
.hero-grid .fact .label {
  font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.07em;
  color: var(--text-muted); margin-bottom: 2px;
}
.hero-grid .fact .value { font-size: 0.95rem; color: var(--text); word-break: break-word; }
.hero-grid .fact .value code { font-size: 0.86em; }

.event-hero .cascade-summary {
  display: flex; align-items: center; gap: 0.7rem; flex-wrap: wrap; margin-top: 0.9rem;
}
.cascade-summary .cs-label {
  font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--text-muted);
}

/* ------------------------------------------- per-event detail sections */
.section-card {
  padding: 1.1rem 1.3rem; border: 1px solid var(--border);
  border-radius: var(--radius); background: var(--bg-card);
  margin: 1rem 0;
}
.section-card h2 { margin-top: 0; border: 0; padding: 0; }

.kv-list {
  display: grid; gap: 0.55rem 1rem;
  grid-template-columns: max-content 1fr;
  margin: 0.3rem 0;
}
.kv-list dt {
  color: var(--text-muted); font-size: 0.82rem; letter-spacing: 0.03em;
  text-transform: uppercase;
  padding-top: 2px;
}
.kv-list dd { margin: 0; }

table.plain {
  width: 100%; border-collapse: collapse; font-size: 0.93rem;
}
table.plain th, table.plain td {
  padding: 9px 12px; border-top: 1px solid var(--border); vertical-align: top;
  text-align: left;
}
table.plain thead th {
  background: var(--bg-alt); border-top: 0; font-weight: 600; font-size: 0.83rem;
  color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.03em;
}

.obs-group {
  border: 1px solid var(--border); border-radius: var(--radius);
  margin: 0.7rem 0; background: var(--bg-card);
  overflow: hidden;
}
.obs-group-head {
  display: flex; align-items: center; gap: 0.6rem;
  padding: 10px 14px; background: var(--bg-alt);
  border-bottom: 1px solid var(--border);
  font-size: 0.93rem;
}
.obs-group-head .layer-chip {
  display: inline-flex; width: 10px; height: 10px; border-radius: 50%;
  background: var(--layer-color);
}
.obs-group-head .gname { font-weight: 600; }
.obs-group-head .gcount { color: var(--text-muted); font-size: 0.85rem; }
.obs-group ul.obs-items { list-style: none; padding: 0; margin: 0; }
.obs-group ul.obs-items li {
  padding: 10px 14px; border-top: 1px solid var(--border);
}
.obs-group ul.obs-items li:first-child { border-top: 0; }
.obs-group .obs-head {
  display: flex; gap: 0.55rem; flex-wrap: wrap; align-items: center;
  margin-bottom: 4px;
}
.obs-group .obs-head .actor {
  font-family: var(--font-mono); font-size: 0.88em;
}
.obs-group .obs-head time {
  color: var(--text-muted); font-family: var(--font-mono); font-size: 0.85em;
}
.obs-group .obs-sources { margin: 4px 0 0; padding: 0; list-style: none; font-size: 0.87em; }
.obs-group .obs-sources li { padding: 4px 0 4px 14px; position: relative; color: var(--text-muted); }
.obs-group .obs-sources li::before { content: ""; position: absolute; left: 0; top: 12px; width: 6px; height: 1px; background: var(--border-strong); }
.obs-group .obs-sources code { background: var(--bg-sunken); padding: 0 4px; border-radius: 3px; }

/* ------------------------------------------------- source / citation */
.source-list {
  list-style: none; padding: 0; margin: 0.4rem 0;
  display: grid; gap: 0.4rem;
}
.source-list li {
  padding: 10px 12px; border: 1px solid var(--border);
  border-radius: var(--radius); background: var(--bg-alt);
  font-size: 0.92rem;
}
.source-list li .note { color: var(--text-muted); display: block; margin-top: 3px; }
.source-list li code { background: var(--bg-sunken); padding: 0 4px; border-radius: 3px; font-size: 0.82em; }

.hash-snip {
  display: inline-flex; align-items: center; gap: 4px;
  background: var(--bg-sunken); padding: 1px 6px;
  border-radius: 3px; font-size: 0.82em;
}

.addr-list {
  font-family: var(--font-mono); font-size: 0.8rem; line-height: 1.65;
  max-height: 260px; overflow: auto; padding: 10px 12px;
  border: 1px solid var(--border); border-radius: var(--radius);
  background: var(--bg-sunken);
  display: grid; grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
}
.addr-list span { padding: 0 6px 0 0; white-space: nowrap; }

/* ----------------------------------------------- tags + prev-next nav */
.tag-cloud { display: flex; gap: 6px; flex-wrap: wrap; }
.tag-cloud a {
  background: var(--bg-alt); color: var(--text); font-size: 0.82rem;
  padding: 2px 10px; border-radius: 999px; border: 1px solid var(--border);
}
.tag-cloud a:hover { background: var(--accent-soft); text-decoration: none; }

.prev-next {
  display: grid; gap: 0.6rem; grid-template-columns: 1fr 1fr;
  margin: 2rem 0 1rem;
}
.prev-next a {
  display: block; padding: 12px 14px; border: 1px solid var(--border);
  border-radius: var(--radius); background: var(--bg-card);
  color: var(--text);
}
.prev-next a:hover { border-color: var(--border-strong); text-decoration: none; }
.prev-next a .dir { font-size: 0.76rem; color: var(--text-muted); display: block; text-transform: uppercase; letter-spacing: 0.06em; }
.prev-next a.next { text-align: right; }

footer.site-footer {
  margin-top: 3rem; padding: 1.4rem 0; border-top: 1px solid var(--border);
  color: var(--text-muted); font-size: 0.86rem;
  display: flex; gap: 1rem; flex-wrap: wrap; justify-content: space-between;
}

/* ----------------------------------------- responsive tweaks */
@media (max-width: 1050px) {
  .signal-grid, .artifact-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .layer-board { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .audit-grid { grid-template-columns: 1fr; }
  .audit-task-list { grid-template-columns: 1fr; }
}

@media (max-width: 700px) {
  .site-header-inner { padding: 8px 0.8rem; }
  .header-link.optional { display: none; }
  .page { padding: 0 0.8rem 3rem; }
  h1 { font-size: 1.5rem; }
  h2 { font-size: 1.1rem; }
  .dashboard-hero { grid-template-columns: 1fr; }
  .hero-copy { min-height: 0; padding: 1.25rem; }
  .dashboard-hero h1 { font-size: 2.45rem; max-width: 14ch; }
  .section-heading { display: block; }
  .signal-grid, .artifact-grid { grid-template-columns: 1fr; }
  .layer-board { grid-template-columns: repeat(2, 1fr); }
  .audit-panel { padding: .85rem; }
  .hero { padding: 1.1rem 1.1rem 0.9rem; }
  .stat-grid { grid-template-columns: repeat(2, 1fr); gap: 0.55rem; }
  .stat-card { padding: 10px 12px; }
  .stat-number { font-size: 1.4rem; }
  .filter-bar { top: 48px; }
  table.events thead th { top: 48px; font-size: 0.75rem; padding: 6px 8px; }
  table.events tbody td { padding: 8px 8px; }
  table.events .col-hide-mobile { display: none; }
  .kv-list { grid-template-columns: 1fr; }
  .prev-next { grid-template-columns: 1fr; }
}

@media print {
  .site-header, .filter-bar, .filter-drawer, .theme-toggle, .prev-next { display: none !important; }
  body { background: #fff; color: #000; }
  .section-card { break-inside: avoid; }
}

/* ---- Expressive analysis layer (findings + cross-layer viz) ---- */
.viz-meter { height: 6px; border-radius: 999px; background: var(--bg-sunken); overflow: hidden; margin: .5rem 0; }
.viz-meter > span { display: block; height: 100%; border-radius: 999px; }
.viz-stack { display: flex; height: 14px; border-radius: 5px; overflow: hidden; background: var(--bg-sunken); }
.viz-stack > span { display: block; height: 100%; }
.viz-stack > span:not(:last-child) { box-shadow: 1px 0 0 var(--bg-card); }

.findings-grid {
  display: grid; gap: .9rem; margin: .4rem 0 1.6rem;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}
.finding-card {
  background: var(--bg-card); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 1rem 1.05rem;
}
.finding-number { font-family: var(--font-display); font-size: 2.1rem; font-weight: 700; line-height: 1; font-variant-numeric: tabular-nums; }
.finding-label { margin-top: .35rem; font-weight: 600; font-size: .92rem; }
.finding-detail { margin: .35rem 0 0; color: var(--text-muted); font-size: .82rem; line-height: 1.45; }

.locus-board, .cov-board, .year-board { display: flex; flex-direction: column; gap: .5rem; margin: .3rem 0 1.6rem; }
.locus-row { display: grid; grid-template-columns: 150px 1fr 110px; align-items: center; gap: .8rem; }
.locus-name, .cov-name { display: flex; align-items: center; gap: .45rem; font-size: .9rem; font-weight: 600; }
.locus-name .dot, .cov-name .dot { width: 10px; height: 10px; border-radius: 3px; flex: none; }
.locus-track { height: 18px; border-radius: 5px; background: var(--bg-sunken); overflow: hidden; }
.locus-track > span { display: block; height: 100%; border-radius: 5px; }
.locus-val { font-size: .85rem; color: var(--text-muted); text-align: right; font-variant-numeric: tabular-nums; }
.locus-val strong { color: var(--text); font-size: 1.05rem; }
.locus-val .gap { color: var(--bad-fg); }

.year-row { display: grid; grid-template-columns: 52px 1fr 42px; align-items: center; gap: .7rem; }
.year-name { font-size: .82rem; color: var(--text-muted); font-variant-numeric: tabular-nums; }
.year-track { width: var(--scale, 100%); min-width: 18px; }
.year-val { font-size: .8rem; color: var(--text-muted); text-align: right; font-variant-numeric: tabular-nums; }

.cov-row { display: grid; grid-template-columns: 150px 1fr 80px; align-items: center; gap: .8rem; }
.cov-track { }
.cov-val { font-size: .8rem; color: var(--text-muted); text-align: right; }

.legend { display: flex; flex-wrap: wrap; gap: .4rem 1rem; margin: .2rem 0 .7rem; }
.legend-item { display: inline-flex; align-items: center; gap: .35rem; font-size: .78rem; color: var(--text-muted); }
.legend-item .sw, .ready-sub .sw { width: 11px; height: 11px; border-radius: 3px; flex: none; display: inline-block; }

.jur-grid, .ready-grid { display: grid; gap: 1.2rem; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); margin: .3rem 0 1.6rem; }
.jur-col, .ready-block { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 1rem 1.1rem; }
.jur-col h3, .ready-head { margin: 0 0 .6rem; font-size: .95rem; }
.jur-col h3 .meta { font-weight: 400; }
.jur-row { display: grid; grid-template-columns: 96px 1fr 76px; align-items: center; gap: .6rem; margin: .3rem 0; }
.jur-row.mini { grid-template-columns: 56px 1fr 40px; }
.jur-name { font-size: .85rem; font-weight: 600; }
.jur-track { height: 14px; border-radius: 4px; background: var(--bg-sunken); overflow: hidden; }
.jur-track > span { display: block; height: 100%; border-radius: 4px; background: var(--accent); }
.jur-val { font-size: .8rem; color: var(--text-muted); text-align: right; font-variant-numeric: tabular-nums; }
.jur-val strong { color: var(--text); }

.ready-head { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: .4rem; }
.ready-head .meta { font-weight: 400; }
.ready-block .viz-stack { height: 18px; }
.ready-sub { display: flex; flex-wrap: wrap; gap: .3rem 1.1rem; margin-top: .55rem; font-size: .8rem; color: var(--text-muted); }
.ready-sub span { display: inline-flex; align-items: center; gap: .35rem; }

@media (max-width: 640px) {
  .locus-row { grid-template-columns: 110px 1fr 76px; gap: .5rem; }
  .cov-row { grid-template-columns: 110px 1fr; }
  .cov-val { display: none; }
  .locus-name, .cov-name { font-size: .8rem; }
}
"""


STATIC_JS = """\
(function () {
  // ---------------- Theme toggle (localStorage-persisted) ----------------
  const THEME_KEY = 'ccdb.theme';
  const root = document.documentElement;
  const stored = localStorage.getItem(THEME_KEY);
  if (stored === 'dark' || stored === 'light') root.setAttribute('data-theme', stored);
  const toggle = document.getElementById('theme-toggle');
  if (toggle) {
    const setLabel = () => {
      const cur = root.getAttribute('data-theme');
      const mql = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)');
      const effective = cur || (mql && mql.matches ? 'dark' : 'light');
      toggle.textContent = effective === 'dark' ? '☾ dark' : '☀ light';
      toggle.setAttribute('aria-label',
        effective === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
    };
    setLabel();
    toggle.addEventListener('click', () => {
      const cur = root.getAttribute('data-theme');
      const next = cur === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      localStorage.setItem(THEME_KEY, next);
      setLabel();
    });
  }

  // ----------------------- human audit console -----------------------
  function setupAuditConsole() {
    const forms = document.querySelectorAll('.audit-form[data-audit-type]');
    if (!forms.length) return;
    const today = new Date().toISOString().slice(0, 10);
    const randomSuffix = () => {
      const bytes = new Uint8Array(4);
      if (globalThis.crypto && globalThis.crypto.getRandomValues) {
        globalThis.crypto.getRandomValues(bytes);
        return Array.from(bytes, b => b.toString(16).padStart(2, '0')).join('');
      }
      return Math.floor(Math.random() * 0xffffffff).toString(16).padStart(8, '0');
    };
    const approvalDecision = (auditType, decision) => (
      (auditType === 'null_denominator' && decision === 'pass') ||
      (auditType === 'release_signoff' && decision.startsWith('approve_')) ||
      (auditType === 'independent_human_irr' && decision === 'complete_ready_for_kappa')
    );
    forms.forEach(form => {
      const dateInput = form.querySelector('input[name="audit_date"]');
      if (dateInput && !dateInput.value) dateInput.value = today;
      form.addEventListener('submit', ev => {
        ev.preventDefault();
        const data = new FormData(form);
        const auditType = form.dataset.auditType || 'unknown';
        const eventId = form.dataset.eventId || null;
        const taskId = form.dataset.taskId || eventId || auditType;
        const decision = data.get('decision') || '';
        const reviewed = JSON.parse(form.dataset.reviewedArtifacts || '[]');
        const checks = {};
        form.querySelectorAll('input[type="checkbox"][data-check]').forEach(cb => {
          checks[cb.dataset.check] = cb.checked;
        });
        const missingChecks = Object.entries(checks)
          .filter(([, checked]) => !checked)
          .map(([name]) => name);
        const error = form.querySelector('.audit-error');
        if (error) {
          error.hidden = true;
          error.textContent = '';
        }
        if (approvalDecision(auditType, decision) && missingChecks.length) {
          if (error) {
            error.textContent = 'Pass/approve decisions require all checklist items. Missing: ' + missingChecks.join(', ');
            error.hidden = false;
          }
          return;
        }
        const generatedAt = new Date().toISOString();
        const auditDate = data.get('audit_date') || today;
        const compactStamp = generatedAt.replace(/[-:.TZ]/g, '').slice(0, 14);
        const record = {
          audit_id: ['audit', auditType, taskId, auditDate, compactStamp, randomSuffix()].filter(Boolean).join('__'),
          audit_type: auditType,
          event_id: eventId,
          task_id: taskId,
          snapshot: globalThis.AUDIT_SNAPSHOT || {},
          auditor: {
            name: data.get('auditor_name') || '',
            affiliation: data.get('auditor_affiliation') || '',
            email: data.get('auditor_email') || '',
            independence_statement: data.get('independence_statement') || ''
          },
          reviewed_artifacts: reviewed,
          decision,
          checks,
          rationale: data.get('rationale') || '',
          limitations: data.get('limitations') || '',
          supporting_materials: data.get('supporting_materials') || '',
          audit_date: auditDate,
          attestation: data.get('attestation') || '',
          generated_by: 'static Human Audit Console',
          generated_at: generatedAt
        };
        let patch = '';
        if (auditType === 'null_denominator' && eventId) {
          if (decision === 'pass') {
            patch = [
              '',
              '# Suggested YAML patch fragment. Apply only after maintainer review.',
              '# File: events/' + eventId + '.yaml',
              'last_human_audit: ' + record.audit_date
            ].join('\\n');
          } else {
            patch = [
              '',
              '# No last_human_audit stamp should be applied for this decision.',
              '# Maintainer action: re-scope, exclude, or request more evidence for events/' + eventId + '.yaml'
            ].join('\\n');
          }
        } else if (auditType === 'independent_human_irr') {
          patch = [
            '',
            '# Expected maintainer action after accepting this record:',
            '# - place the independent recode output under analysis/inter_rater/',
            '# - run make irr-kappa,',
            '# - set coder_provenance.mode to independent_human only if the recode was truly independent.'
          ].join('\\n');
        } else if (auditType === 'release_signoff') {
          patch = [
            '',
            '# Expected maintainer action after accepting this record:',
            '# - update CITATION.cff version/date,',
            '# - regenerate artifacts from a clean intended source tree,',
            '# - run the strict submission gate.'
          ].join('\\n');
        }
        record.maintainer_patch_template = patch.trim();
        const outputText = JSON.stringify(record, null, 2);
        const output = form.parentElement.querySelector('.audit-output');
        const wrap = form.parentElement.querySelector('.audit-output-wrap');
        if (output) {
          output.value = outputText;
          output.focus();
          output.select();
        }
        if (wrap) wrap.classList.add('visible');
      });
    });
    document.querySelectorAll('[data-copy-audit-output]').forEach(btn => {
      btn.addEventListener('click', async () => {
        const target = document.getElementById(btn.dataset.copyAuditOutput);
        if (!target) return;
        target.select();
        try {
          await navigator.clipboard.writeText(target.value);
          btn.textContent = 'Copied';
          setTimeout(() => { btn.textContent = 'Copy output'; }, 1200);
        } catch (_) {
          document.execCommand('copy');
        }
      });
    });
  }
  setupAuditConsole();

  // --------------------------- index filters ---------------------------
  const table = document.getElementById('events-table');
  if (!table) return;
  const tbody = table.querySelector('tbody');
  const rows = Array.from(tbody.rows);
  const searchInput = document.getElementById('filter-search');
  const chipBtns = document.querySelectorAll('.chip[data-facet]');
  const resetBtn = document.getElementById('filter-reset');
  const countEl = document.getElementById('result-count');
  const facets = {};      // {facet: Set(values)}

  function syncHashFromState() {
    const parts = [];
    if (searchInput && searchInput.value) parts.push('q=' + encodeURIComponent(searchInput.value));
    for (const f in facets) {
      if (!facets[f].size) continue;
      parts.push(f + '=' + Array.from(facets[f]).map(encodeURIComponent).join(','));
    }
    const hash = parts.join('&');
    history.replaceState(null, '', hash ? '#' + hash : location.pathname + location.search);
  }
  function loadStateFromHash() {
    const raw = location.hash.replace(/^#/, '');
    if (!raw) return;
    for (const kv of raw.split('&')) {
      const [k, v] = kv.split('=');
      if (!k || !v) continue;
      const val = decodeURIComponent(v);
      if (k === 'q' && searchInput) searchInput.value = val;
      else facets[k] = new Set(val.split(',').map(decodeURIComponent));
    }
    chipBtns.forEach(b => {
      const f = b.dataset.facet, v = b.dataset.value;
      const on = facets[f] && facets[f].has(v);
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
  }
  function applyFilters() {
    const q = (searchInput && searchInput.value.toLowerCase().trim()) || '';
    let shown = 0;
    for (const tr of rows) {
      let ok = true;
      if (q) {
        ok = (tr.dataset.search || tr.innerText.toLowerCase()).includes(q);
      }
      if (ok) {
        for (const f in facets) {
          if (!facets[f].size) continue;
          const rowVals = (tr.dataset[f] || '').split('|').filter(Boolean);
          const hit = Array.from(facets[f]).some(v => rowVals.includes(v));
          if (!hit) { ok = false; break; }
        }
      }
      tr.classList.toggle('hidden', !ok);
      if (ok) shown++;
    }
    if (countEl) countEl.textContent = shown + ' / ' + rows.length + ' events';
    syncHashFromState();
  }

  chipBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const f = btn.dataset.facet, v = btn.dataset.value;
      facets[f] = facets[f] || new Set();
      if (facets[f].has(v)) { facets[f].delete(v); btn.setAttribute('aria-pressed', 'false'); }
      else { facets[f].add(v); btn.setAttribute('aria-pressed', 'true'); }
      applyFilters();
    });
  });
  if (searchInput) searchInput.addEventListener('input', applyFilters);
  if (resetBtn) resetBtn.addEventListener('click', () => {
    for (const f in facets) facets[f].clear();
    chipBtns.forEach(b => b.setAttribute('aria-pressed', 'false'));
    if (searchInput) searchInput.value = '';
    applyFilters();
  });

  // --------------------------- column sort ---------------------------
  const headers = table.querySelectorAll('thead th[data-sort]');
  let sortState = { key: 'date', dir: 'asc' };
  function cmp(a, b, key) {
    const av = a.dataset[key] || '';
    const bv = b.dataset[key] || '';
    const an = parseFloat(av), bn = parseFloat(bv);
    if (!isNaN(an) && !isNaN(bn)) return an - bn;
    return av.localeCompare(bv);
  }
  function applySort() {
    rows.sort((a, b) => {
      const c = cmp(a, b, sortState.key);
      return sortState.dir === 'desc' ? -c : c;
    });
    rows.forEach(r => tbody.appendChild(r));
    headers.forEach(h => {
      h.setAttribute('aria-sort',
        h.dataset.sort === sortState.key
          ? (sortState.dir === 'asc' ? 'ascending' : 'descending')
          : 'none');
    });
  }
  headers.forEach(h => {
    h.addEventListener('click', () => {
      const key = h.dataset.sort;
      sortState = { key, dir: (sortState.key === key && sortState.dir === 'asc') ? 'desc' : 'asc' };
      applySort();
    });
    h.addEventListener('keydown', ev => {
      if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); h.click(); }
    });
    h.setAttribute('tabindex', '0');
    h.setAttribute('role', 'button');
  });

  loadStateFromHash();
  applySort();
  applyFilters();

  // Re-apply when hero "cascade events" / "OFAC SDN" chip links (or a user
  // pasting a deep-linked URL into the address bar) change the hash.
  window.addEventListener('hashchange', () => {
    for (const f in facets) facets[f].clear();
    chipBtns.forEach(b => b.setAttribute('aria-pressed', 'false'));
    if (searchInput) searchInput.value = '';
    loadStateFromHash();
    applyFilters();
    // Scroll the events table into view so the filter effect is obvious.
    const t = document.getElementById('events-table');
    if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
})();
"""


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def escape(s: Any) -> str:
    if s is None:
        return ""
    if isinstance(s, datetime):
        return html.escape(fmt_ts(s))
    return html.escape(str(s))


def fmt_ts(value: Any, compact: bool = False) -> str:
    """Render a timestamp uniformly. PyYAML hands us datetime objects;
    str() on those produces '2022-08-08 13:30:00+00:00'. We want ISO-8601
    with a 'Z' zulu suffix instead. Strings pass through unchanged (they
    already have the right shape)."""
    if value is None or value == "":
        return ""
    if isinstance(value, datetime):
        iso = value.isoformat().replace("+00:00", "Z")
        return iso[:16].replace("T", " ") if compact else iso
    s = str(value)
    return s[:16].replace("T", " ") if compact else s


def titleify(slug: str) -> str:
    """Turn a kebab-case slug into a display title with acronym-awareness.

    "tornado-cash-ofac-2022" → "Tornado Cash OFAC 2022"
    "coinbase-india-exit-2022" → "Coinbase India Exit 2022"
    """
    parts = slug.split("-")
    out = []
    for p in parts:
        low = p.lower()
        if low in ACRONYMS:
            out.append(p.upper())
        elif p.isdigit():
            out.append(p)
        elif re.match(r"^v\d", low):
            out.append(low)
        else:
            out.append(p[:1].upper() + p[1:].lower())
    return " ".join(out)


def pill(text: Any, kind: str | None = None) -> str:
    """Render a pill. kind is a css class suffix, e.g. 'direct', 'cascade'."""
    if text is None or text == "":
        return ""
    cls = "pill"
    if kind:
        cls += f" pill-{kind}"
    return f'<span class="{cls}">{escape(text)}</span>'


def layer_pill(layer: str) -> str:
    if not layer:
        return ""
    return (
        f'<span class="pill pill-layer" style="--layer-color: var(--layer-{layer})">'
        f'{escape(LAYER_SHORT.get(layer, layer))}</span>'
    )


def hash_snip(value: str, take: int = 12) -> str:
    if not value:
        return ""
    s = str(value)
    short = s if len(s) <= take + 10 else s[: take + 7] + "…"
    return f'<code class="hash-snip">{escape(short)}</code>'


def parse_ts(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def changed_layers(event: dict) -> set[str]:
    return {
        o["layer"] for o in (event.get("observations") or [])
        if isinstance(o, dict)
        and o.get("observation_kind") == "observed_change"
        and o.get("layer") in LAYER_ORDER
    }


def no_change_layers(event: dict) -> set[str]:
    return {
        o["layer"] for o in (event.get("observations") or [])
        if isinstance(o, dict)
        and o.get("observation_kind") == "observed_no_change"
        and o.get("layer") in LAYER_ORDER
    }


def observations_by_layer(event: dict) -> dict[str, list[dict]]:
    by: dict[str, list[dict]] = {}
    for obs in event.get("observations") or []:
        if not isinstance(obs, dict):
            continue
        by.setdefault(obs.get("layer"), []).append(obs)
    for k in by:
        by[k].sort(key=lambda o: str(o.get("timestamp", "")))
    return by


# ---------------------------------------------------------------------------
# Per-event renderers
# ---------------------------------------------------------------------------

def render_cascade_dots(event: dict, xl: bool = False) -> str:
    changed = changed_layers(event)
    no_change = no_change_layers(event)
    cls = "cascade-dots cascade-dots--xl" if xl else "cascade-dots"
    dots = []
    for layer in LAYER_ORDER:
        extra = ""
        if layer in changed:
            extra = " on"
        elif layer in no_change:
            extra = " no-change"
        tip = f"{LAYER_LABEL[layer]}: "
        if layer in changed:
            tip += "observed_change"
        elif layer in no_change:
            tip += "observed_no_change"
        else:
            tip += "no observation"
        dots.append(
            f'<span class="dot{extra}" '
            f'style="--layer-color: var(--layer-{layer})" '
            f'title="{escape(tip)}" aria-label="{escape(tip)}"></span>'
        )
    return f'<span class="{cls}" role="img" aria-label="Cascade shape">{"".join(dots)}</span>'


def render_timeline(event: dict) -> str:
    trigger_ts = parse_ts((event.get("trigger") or {}).get("timestamp"))
    if trigger_ts is None:
        return ""
    obs_by_layer = observations_by_layer(event)
    # Only render if there's at least one observation with a time reference.
    has_any_timed = any(
        parse_ts(o.get("timestamp")) for obs in obs_by_layer.values() for o in obs
    )
    if not has_any_timed:
        return ""

    overflow = 0
    rows_html: list[str] = []
    for layer in LAYER_ORDER:
        observations = obs_by_layer.get(layer) or []
        has_change = any(o.get("observation_kind") == "observed_change" for o in observations)
        markers: list[str] = []
        for obs in observations:
            ts = parse_ts(obs.get("timestamp"))
            if ts is None:
                continue
            delta_h = (ts - trigger_ts).total_seconds() / 3600.0
            if delta_h < -0.1:
                continue
            kind_cls = " no-change" if obs.get("observation_kind") != "observed_change" else ""
            actor = obs.get("actor") or "—"
            evname = obs.get("event") or ""
            tip = f"{LAYER_LABEL[layer]} · {actor} · {evname} · Δ{delta_h:.1f}h"
            if delta_h > TIMELINE_MAX_HOURS:
                overflow += 1
                markers.append(
                    f'<span class="tl-marker overflow" '
                    f'title="{escape(tip)} (beyond 7d)" data-delta="{delta_h:.1f}"></span>'
                )
                continue
            pct = max(0.0, min(100.0, 100.0 * delta_h / TIMELINE_MAX_HOURS))
            markers.append(
                f'<span class="tl-marker{kind_cls}" '
                f'style="left: {pct:.2f}%" '
                f'title="{escape(tip)}" data-delta="{delta_h:.1f}"></span>'
            )
        row_cls = "timeline-row has-change" if has_change else "timeline-row"
        rows_html.append(
            f'<div class="{row_cls}" style="--layer-color: var(--layer-{layer})">'
            f'<span class="tl-label">{escape(LAYER_SHORT[layer])}</span>'
            f'<div class="track">{"".join(markers)}</div>'
            f"</div>"
        )

    ticks_html = "".join(
        f'<span class="tick" style="left: {100.0 * h / TIMELINE_MAX_HOURS:.2f}%">'
        f'{h}h{" (7d)" if h == 168 else ""}</span>'
        for h in TIMELINE_TICKS
    )
    note = (
        f'<p class="timeline-note">+ {overflow} observation(s) beyond 7 days — '
        f"see per-observation details below.</p>"
        if overflow else ""
    )
    return (
        '<div class="timeline" aria-label="Cascade timeline">'
        '<div class="timeline-head">'
        f'<span>Cascade timeline (t=0: trigger @ {escape(trigger_ts.isoformat().replace("+00:00","Z"))})</span>'
        "<span>0h → 7d</span>"
        "</div>"
        f'{"".join(rows_html)}'
        f'<div class="timeline-axis">{ticks_html}</div>'
        f"{note}"
        "</div>"
    )


def render_trigger_section(trig: dict) -> str:
    if not isinstance(trig, dict):
        return ""
    citations = trig.get("citation") or []
    cite_items = []
    for c in citations:
        if not isinstance(c, dict):
            cite_items.append(f'<li>{escape(c)}</li>')
            continue
        url = c.get("url") or ""
        label = c.get("type") or "citation"
        bh = c.get("body_hash") or ""
        note = str(c.get("note") or "").strip()
        wb = c.get("wayback") or ""
        parts = [f'<span class="pill pill-neutral">{escape(label)}</span>']
        if url:
            parts.append(f' <a href="{escape(url)}" rel="noopener">{escape(url)}</a>')
        if wb:
            parts.append(f' · <a href="{escape(wb)}" rel="noopener" title="Wayback">archive</a>')
        if bh:
            parts.append(f' · {hash_snip(bh)}')
        body = "".join(parts)
        if note:
            body += f'<span class="note">{escape(note[:300])}{"…" if len(note) > 300 else ""}</span>'
        cite_items.append(f'<li>{body}</li>')
    return (
        '<section class="section-card"><h2>Trigger</h2>'
        '<dl class="kv-list">'
        f'<dt>Type</dt><dd><code>{escape(trig.get("type") or "—")}</code></dd>'
        f'<dt>Actor</dt><dd><code>{escape(trig.get("actor") or "—")}</code></dd>'
        f'<dt>Timestamp</dt><dd><code>{escape(fmt_ts(trig.get("timestamp")) or "—")}</code> '
        f'<span class="meta">(precision: <code>{escape(trig.get("timestamp_precision") or "—")}</code>)</span></dd>'
        "</dl>"
        "<h3>Citations</h3>"
        f'<ul class="source-list">{"".join(cite_items)}</ul>'
        "</section>"
    )


def render_target_section(event: dict) -> str:
    t = event.get("target") or {}
    addrs = t.get("addresses") or []
    addrs_html = ""
    if addrs:
        addr_spans = "".join(f"<span>{escape(a)}</span>" for a in addrs)
        addrs_html = (
            f"<details><summary>Target addresses ({len(addrs)})</summary>"
            f'<div class="addr-list">{addr_spans}</div></details>'
        )
    enum_note = str(t.get("enumeration_note") or "").strip()
    return (
        '<section class="section-card"><h2>Target</h2>'
        '<dl class="kv-list">'
        f'<dt>Kind</dt><dd><code>{escape(t.get("kind") or "—")}</code></dd>'
        f'<dt>Enumeration</dt><dd><code>{escape(t.get("enumeration") or "—")}</code></dd>'
        f'<dt>Protocol</dt><dd><code>{escape(t.get("protocol") or "—")}</code></dd>'
        f'<dt>Chains</dt><dd><code>{escape(", ".join(t.get("chains") or []) or "—")}</code></dd>'
        + (f'<dt>Actor name</dt><dd>{escape(t.get("actor_name"))}</dd>' if t.get("actor_name") else "")
        + (f'<dt>Actor type</dt><dd><code>{escape(t.get("actor_type"))}</code></dd>' if t.get("actor_type") else "")
        + "</dl>"
        + (f'<p class="meta">{escape(enum_note[:500])}{"…" if len(enum_note) > 500 else ""}</p>' if enum_note else "")
        + addrs_html
        + "</section>"
    )


def render_coverage_section(event: dict) -> str:
    cov = event.get("coverage") or []
    if not cov:
        return ""
    rows = []
    cov_by_layer = {c.get("layer"): c for c in cov if isinstance(c, dict)}
    for layer in LAYER_ORDER:
        c = cov_by_layer.get(layer) or {"layer": layer, "status": "not_measured"}
        status = c.get("status") or "—"
        chain = c.get("chain") or ""
        scope = c.get("scope") or []
        if isinstance(scope, list):
            scope_s = ", ".join(scope) or "—"
        else:
            scope_s = str(scope)
        note = str(c.get("note") or "").strip().splitlines()
        note_s = note[0][:280] if note else ""
        rows.append(
            "<tr>"
            f"<td>{layer_pill(layer)} <span class=\"muted\">{escape(LAYER_LABEL[layer])}</span></td>"
            f"<td>{pill(status, status)}</td>"
            f"<td>{escape(chain) or '—'}</td>"
            f"<td class=\"meta\">{escape(scope_s)}</td>"
            f"<td class=\"meta\">{escape(note_s)}{'…' if len(note_s) >= 280 else ''}</td>"
            "</tr>"
        )
    return (
        '<section class="section-card"><h2>Coverage</h2>'
        '<table class="plain">'
        "<thead><tr><th>Layer</th><th>Status</th><th>Chain</th><th>Scope</th><th>Note</th></tr></thead>"
        f"<tbody>{''.join(rows)}</tbody>"
        "</table></section>"
    )


def render_obs_source(src: dict) -> str:
    if not isinstance(src, dict):
        return f"<li>{escape(src)}</li>"
    stype = src.get("type") or ""
    url = src.get("url") or ""
    wb = src.get("wayback") or ""
    bh = src.get("body_hash") or ""
    tx = src.get("tx_hash") or ""
    note = str(src.get("note") or "").strip()
    parts = [f"<code>{escape(stype)}</code>"]
    if url:
        short = url if len(url) <= 80 else url[:77] + "…"
        parts.append(f' <a href="{escape(url)}" rel="noopener">{escape(short)}</a>')
    if wb:
        parts.append(f' · <a href="{escape(wb)}" rel="noopener">archive</a>')
    if tx:
        parts.append(f' · tx {hash_snip(tx, 10)}')
    if bh:
        parts.append(f' · {hash_snip(bh)}')
    body = "".join(parts)
    if note:
        body += f'<br><span class="muted">{escape(note[:240])}{"…" if len(note) > 240 else ""}</span>'
    return f"<li>{body}</li>"


def render_observations_grouped(event: dict) -> str:
    obs_by_layer = observations_by_layer(event)
    if not obs_by_layer:
        return "<p class=\"muted\"><em>No observations recorded.</em></p>"
    groups = []
    for layer in LAYER_ORDER:
        items = obs_by_layer.get(layer) or []
        if not items:
            continue
        li_html = []
        for obs in items:
            kind = obs.get("observation_kind") or "—"
            attr = obs.get("attribution") or "—"
            actor = obs.get("actor") or "—"
            evname = obs.get("event") or ""
            ts_iso = fmt_ts(obs.get("timestamp"))
            delta = obs.get("delta_hours")
            delta_s = f" · Δ{delta}h" if delta is not None else ""
            sources_html = "".join(render_obs_source(s) for s in (obs.get("sources") or []))
            li_html.append(
                "<li>"
                '<div class="obs-head">'
                f"{pill(kind, kind)}{pill(attr, attr)}"
                f'<span class="actor">{escape(actor)}</span>'
                f'<span class="muted">· {escape(evname)}</span>'
                + (f'<time datetime="{escape(ts_iso)}">{escape(ts_iso)}{delta_s}</time>' if ts_iso else "")
                + "</div>"
                f'<ul class="obs-sources">{sources_html}</ul>'
                "</li>"
            )
        groups.append(
            f'<article class="obs-group" style="--layer-color: var(--layer-{layer})">'
            '<header class="obs-group-head">'
            '<span class="layer-chip" aria-hidden="true"></span>'
            f'<span class="gname">{escape(LAYER_LABEL[layer])}</span>'
            f'<span class="gcount">{len(items)} observation{"s" if len(items) != 1 else ""}</span>'
            "</header>"
            f'<ul class="obs-items">{"".join(li_html)}</ul>'
            "</article>"
        )
    return "".join(groups)


def render_related_events(event: dict, all_slugs: set[str]) -> str:
    rel = event.get("related_events") or []
    if not rel:
        return ""
    items = []
    for r in rel:
        if isinstance(r, str):
            slug, label = r, titleify(r)
        elif isinstance(r, dict):
            slug = r.get("slug") or r.get("id") or ""
            label = r.get("label") or titleify(slug)
        else:
            continue
        if slug in all_slugs:
            items.append(f'<a href="./{escape(slug)}.html">{escape(label)}</a>')
        else:
            items.append(f'<span>{escape(label)}</span>')
    if not items:
        return ""
    return (
        '<section class="section-card"><h2>Related events</h2>'
        '<div class="tag-cloud">' + ", ".join(items) + "</div></section>"
    )


def render_prev_next(slug: str, ordered_slugs: list[str]) -> str:
    if slug not in ordered_slugs:
        return ""
    idx = ordered_slugs.index(slug)
    prev = ordered_slugs[idx - 1] if idx > 0 else None
    nxt = ordered_slugs[idx + 1] if idx < len(ordered_slugs) - 1 else None
    left = (
        f'<a href="./{escape(prev)}.html"><span class="dir">← earlier</span>'
        f'<strong>{escape(titleify(prev))}</strong></a>'
        if prev else "<span></span>"
    )
    right = (
        f'<a class="next" href="./{escape(nxt)}.html"><span class="dir">later →</span>'
        f'<strong>{escape(titleify(nxt))}</strong></a>'
        if nxt else "<span></span>"
    )
    return f'<nav class="prev-next" aria-label="Sibling events">{left}{right}</nav>'


def collect_replay_artifacts(value: Any) -> list[dict[str, str]]:
    artifacts: list[dict[str, str]] = []

    def walk(obj: Any) -> None:
        if isinstance(obj, dict):
            body_path = obj.get("body_path")
            if body_path:
                artifacts.append({
                    "path": str(body_path),
                    "sha256": str(obj.get("body_hash") or obj.get("query_hash") or ""),
                    "type": str(obj.get("type") or "body_path"),
                })
            measurement_ids = obj.get("measurement_ids")
            if measurement_ids:
                artifacts.append({
                    "path": "measurement_ids:" + ",".join(str(x) for x in measurement_ids),
                    "sha256": "",
                    "type": "measurement_ids",
                })
            for child in obj.values():
                walk(child)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)

    walk(value)
    seen: set[tuple[str, str]] = set()
    out: list[dict[str, str]] = []
    for item in artifacts:
        key = (item.get("path", ""), item.get("sha256", ""))
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def artifact_link(path: str, label: str | None = None) -> str:
    label = label or path
    if path.startswith("measurement_ids:"):
        return f"<code>{escape(path)}</code>"
    return f'<a href="{escape(path)}"><code>{escape(label)}</code></a>'


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def site_artifact_record(site_dir: pathlib.Path, path: str, artifact_type: str) -> dict[str, str]:
    sha = ""
    if not path.startswith("measurement_ids:"):
        target = site_dir / path
        if target.is_file():
            sha = sha256_file(target)
    return {"path": path, "sha256": sha, "type": artifact_type}


def audit_snapshot(meta: dict, package_kind: str) -> dict[str, Any]:
    return {
        "dataset_version": meta.get("dataset_version") or "unknown",
        "cutoff_date": meta.get("cutoff_date") or "n/a",
        "source_commit": meta.get("source_commit") or "",
        "source_commit_full": meta.get("source_commit_full") or "",
        "source_input_hash": meta.get("source_input_hash") or "",
        "source_tree_dirty": bool(meta.get("source_tree_dirty")),
        "package_kind": package_kind,
    }


def audit_snapshot_script(meta: dict, package_kind: str) -> str:
    payload = json.dumps(audit_snapshot(meta, package_kind), sort_keys=True)
    return f"<script>window.AUDIT_SNAPSHOT = {payload};</script>"


def render_audit_form(
    *,
    audit_type: str,
    task_id: str,
    event_id: str | None,
    reviewed_artifacts: list[dict[str, str]],
    output_id: str,
    decision_options: list[tuple[str, str]],
    checklist: list[tuple[str, str]],
) -> str:
    options = "".join(
        f'<option value="{escape(value)}">{escape(label)}</option>'
        for value, label in decision_options
    )
    checks = "".join(
        '<label>'
        f'<input type="checkbox" name="{escape(name)}" data-check="{escape(name)}">'
        f'<span>{escape(label)}</span>'
        '</label>'
        for name, label in checklist
    )
    reviewed_json = escape(json.dumps(reviewed_artifacts, separators=(",", ":")))
    event_attr = f' data-event-id="{escape(event_id)}"' if event_id else ""
    return f"""
      <form class="audit-form" data-audit-type="{escape(audit_type)}" data-task-id="{escape(task_id)}"{event_attr} data-reviewed-artifacts="{reviewed_json}">
        <div class="audit-grid">
          <div>
            <label>Auditor name
              <input name="auditor_name" autocomplete="name" required>
            </label>
            <label>Affiliation
              <input name="auditor_affiliation" autocomplete="organization">
            </label>
            <label>Email / contact
              <input name="auditor_email" type="email" autocomplete="email">
            </label>
            <label>Audit date
              <input name="audit_date" type="date" required>
            </label>
            <label>Independence statement
              <textarea name="independence_statement" required placeholder="State whether you are independent of the original coding / LLM pre-audit and what materials you did or did not use."></textarea>
            </label>
          </div>
          <div>
            <label>Decision
              <select name="decision" required>
                <option value="">Select decision</option>
                {options}
              </select>
            </label>
            <div class="audit-checks" role="group" aria-label="Audit checks">
              {checks}
            </div>
            <label>Rationale
              <textarea name="rationale" required placeholder="Explain the evidence basis for this decision."></textarea>
            </label>
            <label>Limitations / follow-up
              <textarea name="limitations" placeholder="State remaining uncertainty, re-scope needs, or evidence gaps."></textarea>
            </label>
            <label>Supporting materials / returned files
              <textarea name="supporting_materials" placeholder="List completed worksheet filenames, command logs, hashes, or external files returned with this audit record."></textarea>
            </label>
            <label>Attestation
              <textarea name="attestation" required placeholder="Example: I reviewed the linked artifacts and this record reflects my independent judgment."></textarea>
            </label>
          </div>
        </div>
        <div class="audit-error" hidden></div>
        <button class="button" type="submit">Generate audit record</button>
      </form>
      <div class="audit-output-wrap">
        <label>Generated JSON / patch template
          <textarea id="{escape(output_id)}" class="audit-output" readonly></textarea>
        </label>
        <div class="audit-result-actions">
          <button class="button secondary" type="button" data-copy-audit-output="{escape(output_id)}">Copy output</button>
        </div>
      </div>
    """


def render_audit_console(events: list[dict], site_dir: pathlib.Path, meta: dict | None = None) -> str:
    meta = meta or load_meta()
    dv = meta.get("dataset_version") or "unknown"
    cutoff = meta.get("cutoff_date") or "n/a"
    commit = meta.get("source_commit") or ""
    generated_stamp = now_utc_datetime().strftime("%Y-%m-%d %H:%M UTC")
    by_id = {e.get("id"): e for e in events if e.get("id")}

    artifact = lambda path, typ: site_artifact_record(site_dir, path, typ)
    standard_docs = [
        artifact("docs/methodology.md", "methodology"),
        artifact("docs/l0-l3-denominator-appendix.md", "denominator_appendix"),
        artifact("docs/paper_claims.md", "claim_lock"),
        artifact("human-audit.md", "human_audit_queue"),
        artifact("analysis/llm_expert_audit/null_case_pre_audit.md", "llm_triage_not_conclusion"),
    ]

    null_cards = []
    for slug in NULL_DENOMINATOR_AUDIT_CASES:
        event = by_id.get(slug) or {}
        title = titleify(slug)
        status, note = NULL_AUDIT_PRESTATUS.get(
            slug,
            ("needs_human_attention", "Human must confirm that the observed_no_change anchor supports the coded scope and time window."),
        )
        priority_cls = " priority-high" if status == "fail_pre_audit" else (" priority-warn" if status == "needs_human_attention" else "")
        no_change_obs = [
            o for o in (event.get("observations") or [])
            if isinstance(o, dict) and o.get("observation_kind") == "observed_no_change"
        ]
        obs_lines = []
        for obs in no_change_obs:
            window = obs.get("window") or []
            window_s = " -> ".join(str(x) for x in window) if isinstance(window, list) else str(window or "")
            obs_lines.append(
                f'<li><code>{escape(obs.get("layer") or "unknown")}</code> · '
                f'{escape(obs.get("actor") or "unknown actor")} · '
                f'{escape(obs.get("event") or "observed_no_change")} '
                f'<span class="muted">{escape(window_s)}</span></li>'
            )
        replay = collect_replay_artifacts(event)
        reviewed = [
            artifact(f"raw/{slug}.yaml", "event_yaml"),
            artifact(f"events/{slug}.html", "rendered_event_page"),
            artifact(f"analysis/evidence-chains/{slug}.md", "evidence_chain"),
            *standard_docs,
            *replay,
        ]
        source_links = "".join(
            f'<div>{artifact_link(a["path"])}</div>' for a in replay
        ) or '<div class="muted">No replay artifact path found in event YAML.</div>'
        out_id = f"audit-output-{slug}"
        null_cards.append(f"""
        <article class="audit-panel{priority_cls}" id="audit-{escape(slug)}">
          <h3>{escape(title)}</h3>
          <p class="meta"><code>{escape(slug)}</code> · LLM pre-audit: <code>{escape(status)}</code></p>
          <p>{escape(note)}</p>
          <div class="audit-links">
            <a href="events/{escape(slug)}.html">Rendered event page</a>
            <a href="raw/{escape(slug)}.yaml">Raw YAML</a>
            <a href="analysis/evidence-chains/{escape(slug)}.md">Evidence chain</a>
            <a href="analysis/llm_expert_audit/null_case_pre_audit.md">LLM pre-audit triage</a>
          </div>
          <div class="audit-note">
            <strong>Observed no-change rows to audit</strong>
            <ul>{''.join(obs_lines) if obs_lines else '<li class="muted">No observed_no_change row found.</li>'}</ul>
          </div>
          <details>
            <summary>Replay artifact paths from YAML</summary>
            <div class="audit-paths">{source_links}</div>
          </details>
          {render_audit_form(
              audit_type="null_denominator",
              task_id=slug,
              event_id=slug,
              reviewed_artifacts=reviewed,
              output_id=out_id,
              decision_options=[
                  ("pass", "pass - anchor supports coded null scope"),
                  ("rescope", "re-scope - claim/window/layer must narrow"),
                  ("exclude", "exclude - remove from stronger null use"),
                  ("needs_more_evidence", "needs more evidence"),
              ],
              checklist=[
                  ("evidence_anchor_confirmed", "Replayable evidence anchor inspected, not just scope_descriptor"),
                  ("scope_confirmed", "Coded scope matches the artifact"),
                  ("time_window_confirmed", "No-change window is supported"),
                  ("denominator_language_confirmed", "Null is phrased as public-evidence denominator only"),
              ],
          )}
        </article>
        """)

    release_reviewed = [
        artifact("docs/a-class-submission-readiness.md", "readiness_plan"),
        artifact("analysis/a_class_submission_gap_report.md", "gap_report"),
        artifact("human-audit.md", "human_audit_queue"),
        artifact("docs/releasing.md", "release_protocol"),
        artifact("CITATION.cff", "citation_metadata"),
        artifact("dataset.meta.json", "dataset_metadata"),
        artifact("analysis/paper_tables/README.md", "paper_tables"),
        artifact("sources/source_manifest.md", "source_manifest"),
    ]

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Human Audit Console for the Chain Censorship Events Database.">
  <title>Human Audit Console — Chain Censorship Events</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
<header class="site-header">
  <div class="site-header-inner">
    <div class="brand"><a href="./index.html">Chain Censorship Events</a><span class="brand-tag">audit console</span></div>
    <div class="header-spacer"></div>
    <a class="header-link optional" href="h1_irr_packet/index.html">IRR packet</a>
    <a class="header-link optional" href="#h2-null-cases">Null cases</a>
    <a class="header-link optional" href="#h3-release">Release</a>
    <a class="header-link" href="./index.html">Dashboard</a>
    <button id="theme-toggle" class="theme-toggle" type="button" aria-label="Toggle theme">☀ light</button>
  </div>
</header>

<main class="page">
  <section class="dashboard-hero">
    <div class="hero-copy">
      <div class="hero-kicker">Human audit workflow</div>
      <h1>Audit console.</h1>
      <p class="hero-lede">
        Use this page for H2 null-denominator decisions and H3 release sign-off.
        H1 independent IRR uses a separate blank-workbook packet to preserve
        blinding. The forms generate structured JSON and patch templates only;
        maintainers must review and merge any YAML changes.
      </p>
      <div class="hero-actions">
        <a class="button" href="#h2-null-cases">Start null-case audit</a>
        <a class="button secondary" href="human-audit.md">Read human queue</a>
        <a class="button secondary" href="analysis/a_class_submission_gap_report.md">Current gap report</a>
      </div>
    </div>
    <aside class="snapshot-panel" aria-label="Audit snapshot">
      <div class="snapshot-head">
        <div class="label">dataset snapshot</div>
        <div class="version">v{escape(dv)}</div>
        <div class="meta">cutoff <code>{escape(cutoff)}</code>{f' · commit <code>{escape(commit)}</code>' if commit else ''}</div>
      </div>
      <div class="status-line"><span><span class="label">H1</span><br><strong>independent-human IRR pending</strong></span><span class="status-dot warn"></span></div>
      <div class="status-line"><span><span class="label">H2</span><br><strong>{len(NULL_DENOMINATOR_AUDIT_CASES)} null cases pending</strong></span><span class="status-dot warn"></span></div>
      <div class="status-line"><span><span class="label">H3</span><br><strong>release sign-off pending</strong></span><span class="status-dot warn"></span></div>
    </aside>
  </section>

  <section class="boundary-note">
    <strong>Do not treat this as direct database editing.</strong>
    A generated record is audit input. It becomes dataset provenance only after
    maintainer review, source-tree update, and the strict gate pass.
  </section>

  <div class="audit-task-list">
    <article class="audit-panel"><h3>H1 · Independent IRR</h3><p>Use the separate H1-only packet. Do not send this full console to IRR coders.</p><a href="h1_irr_packet/index.html">Open H1-only packet</a></article>
    <article class="audit-panel"><h3>H2 · Null denominators</h3><p>Review 13 observed-no-change cases and decide pass/re-scope/exclude.</p><a href="#h2-null-cases">Open H2 cards</a></article>
    <article class="audit-panel"><h3>H3 · Release sign-off</h3><p>Confirm version/date, clean tree, strict gate, and release authority.</p><a href="#h3-release">Open H3 form</a></article>
  </div>

  <section class="audit-console" id="h1-irr">
    <article class="audit-panel priority-warn">
      <h2>H1 · Independent-Human IRR Pass</h2>
      <p><strong>Distribution boundary:</strong> do not send this full dashboard/site bundle to the independent IRR coder. It contains raw YAML, rendered event pages, and LLM pre-audit material that would contaminate blinding.</p>
      <p>Send only the separate H1 packet folder, which contains blank human recode worksheets plus rubric/methodology material.</p>
      <div class="audit-links">
        <a href="h1_irr_packet/index.html">H1-only packet index</a>
        <a href="h1_irr_packet/coverage_status_human_blank.csv">coverage_status blank worksheet</a>
        <a href="h1_irr_packet/observation_kind_human_blank.csv">observation_kind blank worksheet</a>
        <a href="h1_irr_packet/attribution_human_blank.csv">attribution blank worksheet</a>
      </div>
    </article>
  </section>

  <div class="section-heading" id="h2-null-cases">
    <div>
      <h2>H2 · Null-Case Denominator Audit</h2>
      <p class="meta">Each card generates a standalone audit record. Send different cards to different auditors if needed.</p>
    </div>
  </div>
  <section class="audit-console">
    {''.join(null_cards)}
  </section>

  <section class="audit-console" id="h3-release">
    <article class="audit-panel priority-warn">
      <h2>H3 · Formal Release / Submission Sign-Off</h2>
      <p>Use this after H1/H2 records have landed. This record documents release authority; it does not replace the strict gate.</p>
      <div class="audit-links">
        <a href="docs/a-class-submission-readiness.md">A-class readiness plan</a>
        <a href="analysis/a_class_submission_gap_report.md">A-class gap report</a>
        <a href="human-audit.md">human audit queue</a>
        <a href="docs/releasing.md">release protocol</a>
        <a href="CITATION.cff">CITATION.cff</a>
        <a href="dataset.meta.json">dataset.meta.json</a>
      </div>
      {render_audit_form(
          audit_type="release_signoff",
          task_id="h3_release_signoff",
          event_id=None,
          reviewed_artifacts=release_reviewed,
          output_id="audit-output-h3-release",
          decision_options=[
              ("approve_submission_snapshot", "approve submission snapshot"),
              ("approve_tagged_release", "approve tagged release"),
              ("block_release", "block release"),
              ("needs_more_work", "needs more work"),
          ],
          checklist=[
              ("citation_date_valid", "CITATION date is on or after dataset cutoff"),
              ("clean_source_tree_confirmed", "Clean intended source tree confirmed"),
              ("strict_gate_run", "Strict gate command run and reviewed"),
              ("known_limitations_listed", "Known limitations listed in release/submission notes"),
          ],
      )}
    </article>
  </section>

  <footer class="site-footer">
    <div>Generated {generated_stamp} · audit console · dataset v{escape(dv)} · cutoff {escape(cutoff)}</div>
    <div><a href="index.html">Dashboard</a> · <a href="human-audit.md">Human audit queue</a></div>
  </footer>
</main>

{audit_snapshot_script(meta, "h2_h3_audit_console")}
<script src="site.js"></script>
</body>
</html>"""


def write_blank_recode_csv(src: pathlib.Path, dest: pathlib.Path) -> None:
    with src.open(newline="") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
    for row in rows:
        if "recode_value" in row:
            row["recode_value"] = ""
        if "recoder_comment" in row:
            row["recoder_comment"] = ""
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def render_h1_irr_packet_index(packet_dir: pathlib.Path, meta: dict) -> str:
    artifact = lambda path, typ: site_artifact_record(packet_dir, path, typ)
    reviewed = [
        artifact("coverage_status_human_blank.csv", "blank_human_worksheet"),
        artifact("observation_kind_human_blank.csv", "blank_human_worksheet"),
        artifact("attribution_human_blank.csv", "blank_human_worksheet"),
        artifact("sample_manifest.csv", "sample_manifest"),
        artifact("meta.yaml", "sampling_metadata"),
        artifact("docs/methodology.md", "methodology"),
        artifact("docs/case-review-rubric.md", "rubric"),
    ]
    generated_stamp = now_utc_datetime().strftime("%Y-%m-%d %H:%M UTC")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="H1-only independent human IRR packet for the Chain Censorship Events Database.">
  <title>H1 IRR Packet — Chain Censorship Events</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
<main class="page">
  <section class="dashboard-hero">
    <div class="hero-copy">
      <div class="hero-kicker">H1-only distribution packet</div>
      <h1>Independent IRR packet.</h1>
      <p class="hero-lede">
        This folder is intentionally isolated from the dashboard, raw YAML,
        event pages, answer keys, kappa reports, and LLM pre-audit notes. Send
        this packet only to the independent human coder.
      </p>
      <div class="hero-actions">
        <a class="button" href="coverage_status_human_blank.csv">coverage_status worksheet</a>
        <a class="button secondary" href="observation_kind_human_blank.csv">observation_kind worksheet</a>
        <a class="button secondary" href="attribution_human_blank.csv">attribution worksheet</a>
      </div>
    </div>
    <aside class="snapshot-panel" aria-label="IRR packet snapshot">
      <div class="snapshot-head">
        <div class="label">dataset snapshot</div>
        <div class="version">v{escape(meta.get("dataset_version") or "unknown")}</div>
        <div class="meta">cutoff <code>{escape(meta.get("cutoff_date") or "n/a")}</code></div>
      </div>
      <div class="status-line"><span><span class="label">scope</span><br><strong>blank recode only</strong></span><span class="status-dot warn"></span></div>
      <div class="status-line"><span><span class="label">forbidden</span><br><strong>no dashboard / labels / LLM notes</strong></span><span class="status-dot bad"></span></div>
    </aside>
  </section>

  <section class="boundary-note">
    <strong>Blinding boundary.</strong>
    Do not supplement this packet with the full <code>site/</code> directory,
    raw event YAML, rendered event pages, existing recode answers, kappa reports,
    or LLM pre-audit rationale.
  </section>

  <section class="audit-console">
    <article class="audit-panel">
      <h2>Materials</h2>
      <div class="audit-links">
        <a href="coverage_status_human_blank.csv">coverage_status blank worksheet</a>
        <a href="observation_kind_human_blank.csv">observation_kind blank worksheet</a>
        <a href="attribution_human_blank.csv">attribution blank worksheet</a>
        <a href="sample_manifest.csv">sample manifest</a>
        <a href="meta.yaml">sampling metadata</a>
        <a href="docs/methodology.md">methodology</a>
        <a href="docs/case-review-rubric.md">case-review rubric</a>
      </div>
      <p class="meta">Return the completed worksheet files together with the generated JSON below. List returned filenames and hashes in “Supporting materials / returned files”.</p>
    </article>

    <article class="audit-panel priority-warn">
      <h2>Generate H1 Audit Record</h2>
      {render_audit_form(
          audit_type="independent_human_irr",
          task_id="h1_independent_human_irr",
          event_id=None,
          reviewed_artifacts=reviewed,
          output_id="audit-output-h1-irr",
          decision_options=[
              ("complete_ready_for_kappa", "complete - ready for kappa recomputation"),
              ("needs_recode_revision", "needs recode revision"),
              ("invalid_not_independent", "invalid - independence/blinding failed"),
          ],
          checklist=[
              ("blinded_materials_only", "Coder received only this H1 packet"),
              ("independent_coder", "Coder is independent of original labels and LLM pre-audit"),
              ("coverage_status_recoded", "coverage_status recoded"),
              ("observation_kind_recoded", "observation_kind recoded"),
              ("attribution_recoded", "attribution recoded"),
          ],
      )}
    </article>
  </section>

  <footer class="site-footer">
    <div>Generated {generated_stamp} · H1-only IRR packet</div>
  </footer>
</main>

{audit_snapshot_script(meta, "h1_irr_packet")}
<script src="site.js"></script>
</body>
</html>"""


def write_h1_irr_packet(site_dir: pathlib.Path, meta: dict) -> int:
    packet_dir = site_dir / "h1_irr_packet"
    packet_dir.mkdir(parents=True, exist_ok=True)
    (packet_dir / "styles.css").write_text(STATIC_CSS)
    (packet_dir / "site.js").write_text(STATIC_JS)

    worksheet_map = {
        "coverage_status_blind.csv": "coverage_status_human_blank.csv",
        "observation_kind_blind.csv": "observation_kind_human_blank.csv",
        "attribution_blind.csv": "attribution_human_blank.csv",
    }
    copied = 2
    for src_name, dest_name in worksheet_map.items():
        write_blank_recode_csv(
            REPO_ROOT / "analysis" / "inter_rater" / src_name,
            packet_dir / dest_name,
        )
        copied += 1
    for src_rel, dest_rel in (
        ("analysis/inter_rater/sample_manifest.csv", "sample_manifest.csv"),
        ("analysis/inter_rater/meta.yaml", "meta.yaml"),
        ("docs/methodology.md", "docs/methodology.md"),
        ("docs/case-review-rubric.md", "docs/case-review-rubric.md"),
    ):
        src = REPO_ROOT / src_rel
        dest = packet_dir / dest_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        copied += 1
    (packet_dir / "index.html").write_text(render_h1_irr_packet_index(packet_dir, meta))
    return copied + 1


def render_event_page(event: dict, all_events: list[dict], meta: dict | None = None) -> str:
    meta = meta or load_meta()
    dv = meta.get("dataset_version") or "unknown"
    cutoff = meta.get("cutoff_date") or "n/a"
    generated_stamp = now_utc_datetime().strftime("%Y-%m-%d %H:%M UTC")
    slug = event.get("id", "unknown")
    title = titleify(slug)
    shape = event.get("empirical_shape") or ""
    tier = event.get("admission_tier") or ""
    status = event.get("status") or ""
    stratum = event.get("research_stratum") or ""
    trigger = event.get("trigger") or {}
    target = event.get("target") or {}
    jurisdictions = event.get("jurisdiction") or []
    tags = event.get("tags") or []
    scoped = str(event.get("scoped_claim") or "").strip()
    analysis = str(event.get("analysis_notes") or "").strip()

    changed = sorted(changed_layers(event))
    cascade_label = f"{len(changed)} changed layer{'s' if len(changed) != 1 else ''}"
    changed_pills = " ".join(layer_pill(l) for l in changed) if changed else \
        '<span class="muted">no observed changes</span>'

    ordered = sorted(
        (e.get("id") for e in all_events if e.get("id")),
        key=lambda s: str(
            next((e.get("trigger", {}).get("timestamp", "") for e in all_events if e.get("id") == s), "")
        ),
    )
    all_slugs = set(ordered)

    hero_grid = []
    trig_ts_iso = fmt_ts(trigger.get("timestamp"))
    hero_grid.append(
        f'<div class="fact"><div class="label">Trigger date</div>'
        f'<div class="value"><code>{escape(trig_ts_iso or "—")}</code></div></div>'
    )
    hero_grid.append(
        f'<div class="fact"><div class="label">Trigger type</div>'
        f'<div class="value"><code>{escape(trigger.get("type") or "—")}</code></div></div>'
    )
    hero_grid.append(
        f'<div class="fact"><div class="label">Actor</div>'
        f'<div class="value"><code>{escape(trigger.get("actor") or "—")}</code></div></div>'
    )
    hero_grid.append(
        f'<div class="fact"><div class="label">Jurisdiction</div>'
        f'<div class="value">{escape(", ".join(jurisdictions) or "—")}</div></div>'
    )
    hero_grid.append(
        f'<div class="fact"><div class="label">Chains</div>'
        f'<div class="value">{escape(", ".join(target.get("chains") or []) or "—")}</div></div>'
    )
    hero_grid.append(
        f'<div class="fact"><div class="label">Research stratum</div>'
        f'<div class="value"><code>{escape(stratum)}</code></div></div>'
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(title)} — cross-layer censorship event in the Chain Censorship Events Database: {escape(scoped[:200] or 'cross-layer event observations with primary-source evidence.')}">
  <title>{escape(title)} — Chain Censorship Events</title>
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
<header class="site-header">
  <div class="site-header-inner">
    <div class="brand"><a href="../index.html">Chain Censorship Events</a><span class="brand-tag">database</span></div>
    <div class="header-spacer"></div>
    <a class="header-link" href="../index.html">Browse</a>
    <a class="header-link" href="../raw/{escape(slug)}.yaml">Raw YAML</a>
    <button id="theme-toggle" class="theme-toggle" type="button" aria-label="Toggle theme">☀ light</button>
  </div>
</header>

<main class="page">
  <nav aria-label="Breadcrumb" style="margin-top:.8rem;font-size:.88rem;">
    <a href="../index.html">← All events</a>
  </nav>

  <article class="event-hero">
    <div class="tag-row">
      {pill(shape or "—", shape)}
      {pill(tier or "—", tier)}
      {pill(status or "—", status)}
      {pill(stratum or "—", "neutral")}
    </div>
    <h1>{escape(title)}</h1>
    <p class="meta">
      dataset v{escape(dv)} · cutoff {escape(cutoff)} ·
      schema {escape(event.get("schema_version") or "—")} ·
      last verified {escape(event.get("last_verified") or "—")} ·
      {len(target.get("addresses") or [])} target address{"es" if len(target.get("addresses") or []) != 1 else ""} ·
      {len(event.get("observations") or [])} observation{"s" if len(event.get("observations") or []) != 1 else ""}
    </p>

    <div class="cascade-summary">
      <span class="cs-label">Cascade shape</span>
      {render_cascade_dots(event, xl=True)}
      <span class="muted">{escape(cascade_label)}</span>
      <span style="margin-left:auto">{changed_pills}</span>
    </div>

    {f'<blockquote class="scoped-claim"><span class="label">Scoped claim</span>{escape(scoped)}</blockquote>' if scoped else ''}

    <div class="hero-grid">{"".join(hero_grid)}</div>
  </article>

  {render_timeline(event)}

  {render_trigger_section(trigger)}
  {render_target_section(event)}
  {render_coverage_section(event)}

  <section class="section-card">
    <h2>Observations (by layer)</h2>
    {render_observations_grouped(event)}
  </section>

  {f'<section class="section-card"><h2>Analysis notes</h2><pre>{escape(analysis)}</pre></section>' if analysis else ''}

  {render_related_events(event, all_slugs)}

  {('<section class="section-card"><h2>Tags</h2><div class="tag-cloud">' +
    "".join(f'<a href="../index.html#q={escape(t)}">#{escape(t)}</a>' for t in tags) +
    "</div></section>") if tags else ''}

  {render_prev_next(slug, ordered)}

  <footer class="site-footer">
    <div>Generated {generated_stamp} from <code>events/{escape(slug)}.yaml</code> · dataset v{escape(dv)} · cutoff {escape(cutoff)}. See <a href="../docs/citing.md">how to cite</a>.</div>
    <div><a href="../raw/{escape(slug)}.yaml">Raw YAML</a> · <a href="../index.html">All events</a></div>
  </footer>
</main>

<script src="../site.js"></script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Index renderer
# ---------------------------------------------------------------------------

def render_distribution_cards(events: list[dict]) -> str:
    year_counts: collections.Counter = collections.Counter()
    trigger_counts: collections.Counter = collections.Counter()
    chain_counts: collections.Counter = collections.Counter()
    jur_counts: collections.Counter = collections.Counter()
    for e in events:
        ts = str((e.get("trigger") or {}).get("timestamp", ""))[:4]
        if ts.isdigit():
            year_counts[ts] += 1
        t = (e.get("trigger") or {}).get("type")
        if t:
            trigger_counts[t] += 1
        for c in (e.get("target") or {}).get("chains") or []:
            chain_counts[c] += 1
        for j in e.get("jurisdiction") or []:
            jur_counts[j] += 1

    def card(title: str, counter: collections.Counter, top: int = 6) -> str:
        total = sum(counter.values()) or 1
        rows = counter.most_common(top)
        max_v = max((v for _, v in rows), default=1)
        lines = []
        for k, v in rows:
            pct = 100.0 * v / max_v
            lines.append(
                f'<div class="dist-row"><span class="k">{escape(k)}</span>'
                f'<div class="bar"><span class="bar-fill" style="width:{pct:.1f}%"></span></div>'
                f'<span class="v">{v}</span></div>'
            )
        extra = len(counter) - len(rows)
        if extra > 0:
            lines.append(f'<div class="meta" style="margin-top:.4rem">+ {extra} more</div>')
        return f'<div class="dist-card"><h3>{escape(title)}</h3>{"".join(lines)}</div>'

    return (
        '<div class="distribution">'
        + card("By year", year_counts)
        + card("By trigger type", trigger_counts)
        + card("By chain", chain_counts)
        + card("By jurisdiction", jur_counts)
        + "</div>"
    )


def chip_group(label: str, facet: str, values: list[tuple[str, int]]) -> str:
    btns = []
    for v, n in values:
        display = v if v else "—"
        btns.append(
            f'<button class="chip" type="button" '
            f'data-facet="{escape(facet)}" data-value="{escape(v)}" '
            f'aria-pressed="false">{escape(display)} <span class="muted">({n})</span></button>'
        )
    return (
        f'<div class="filter-group" role="group" aria-label="Filter by {escape(label)}">'
        f'<span class="glabel">{escape(label)}</span>{"".join(btns)}</div>'
    )


def render_signal_cards(events: list[dict], shape_counts: collections.Counter, tier_counts: collections.Counter) -> str:
    """Top-level dashboard KPIs. These intentionally mix corpus counts with
    provenance/readiness status so users see the dataset boundary before the
    event table."""
    return f"""
  <div class="signal-grid" aria-label="Corpus signals">
    <article class="signal-card">
      <div class="signal-number">{len(events)}</div>
      <div class="signal-label">admitted YAML records in the current corpus</div>
    </article>
    <article class="signal-card">
      <div class="signal-number">{shape_counts.get('cascade', 0)}</div>
      <div class="signal-label">multi-layer cascade cases; most evidence remains single-layer or null</div>
    </article>
    <article class="signal-card warn">
      <div class="signal-number">{shape_counts.get('null_event', 0)}</div>
      <div class="signal-label">null cases require public-evidence denominator language</div>
    </article>
    <article class="signal-card risk">
      <div class="signal-number">{tier_counts.get('anchor_case', 0)}</div>
      <div class="signal-label">anchor cases are narrative-ready only with human audit provenance</div>
    </article>
  </div>"""


def load_review_queue_dashboard() -> dict[str, Any]:
    """Load the lightweight v0.3 review queue snapshot, if generated."""
    path = REPO_ROOT / "analysis/review_queue/non_human_todo_list.json"
    try:
        data = json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def render_review_queue_dashboard() -> str:
    snapshot = load_review_queue_dashboard()
    if not snapshot:
        return ""

    total = snapshot.get("total_queue_items", "n/a")
    ready = snapshot.get("ready_for_future_human_audit", "n/a")
    remaining = snapshot.get("remaining_source_discovery_rows", "n/a")
    human_done = snapshot.get("human_audit_performed")
    verified_mutated = snapshot.get("primary_source_verified_mutated")

    human_label = "no human audit recorded" if human_done is False else str(human_done)
    verified_label = "primary_source_verified unchanged" if verified_mutated is False else str(verified_mutated)

    return f"""
  <section class="boundary-note" id="v0-3-review-queue">
    <strong>v0.3 review queue.</strong>
    The ingestion review surface tracks <strong>{escape(str(total))}</strong> queue rows:
    <strong>{escape(str(ready))}</strong> are machine-prepared for future human audit and
    <strong>{escape(str(remaining))}</strong> still require source discovery or methodology repair.
    This is pre-human workflow state: {escape(human_label)}; {escape(verified_label)}.
    <div class="hero-actions" style="margin-top:.85rem">
      <a class="button secondary" href="analysis/review_queue/non_human_todo_list.md">Non-human todo list</a>
      <a class="button secondary" href="analysis/review_queue/v0_3_review_triage_summary.md">Triage summary</a>
      <a class="button secondary" href="analysis/review_queue/source_discovery_worklist.md">Source worklist</a>
      <a class="button secondary" href="analysis/review_queue/human_audit_worksheet.md">Human worksheet</a>
    </div>
  </section>
"""


def render_layer_board(events: list[dict]) -> str:
    coverage: dict[str, collections.Counter] = {
        layer: collections.Counter() for layer in LAYER_ORDER
    }
    changed: collections.Counter = collections.Counter()
    no_change: collections.Counter = collections.Counter()
    for event in events:
        for row in event.get("coverage") or []:
            if isinstance(row, dict) and row.get("layer") in coverage:
                coverage[row["layer"]][row.get("status") or "unknown"] += 1
        for layer in changed_layers(event):
            changed[layer] += 1
        for layer in no_change_layers(event):
            no_change[layer] += 1

    cards = []
    total = len(events) or 1
    for layer in LAYER_ORDER:
        cov = coverage[layer]
        measured = cov.get("measured", 0)
        partial = cov.get("partially_measured", 0)
        denominator = measured + partial
        pct = 100.0 * denominator / total
        cards.append(
            f'<article class="layer-card" style="--layer-color: var(--layer-{layer})">'
            f'<h3>{escape(LAYER_SHORT[layer])} · {escape(LAYER_LABEL[layer])}</h3>'
            '<div class="layer-metrics">'
            f'<span><strong>{changed.get(layer, 0)}</strong> observed changes</span>'
            f'<span><strong>{no_change.get(layer, 0)}</strong> observed no-change rows</span>'
            f'<span><strong>{denominator}</strong> measured or partial coverage rows</span>'
            '</div>'
            f'<div class="layer-meter" title="{denominator}/{total} measured or partial">'
            f'<span style="--pct:{pct:.1f}%"></span></div>'
            '</article>'
        )
    return '<div class="layer-board">' + "".join(cards) + "</div>"


def render_artifact_cards() -> str:
    cards = [
        (
            "Measurement protocol",
            "Admission rules, coverage semantics, and denominator discipline.",
            "docs/methodology.md",
        ),
        (
            "Claim map",
            "Which paper claims are live, parked, or forbidden.",
            "docs/paper_claims.md",
        ),
        (
            "Draft paper",
            "Manuscript wrapper generated from the claim lock and paper tables.",
            "docs/paper.md",
        ),
        (
            "A-class readiness",
            "Submission-focused gates, blockers, and go/no-go criteria.",
            "docs/a-class-submission-readiness.md",
        ),
        (
            "A-class gap report",
            "Current machine/human blockers for the submission package.",
            "analysis/a_class_submission_gap_report.md",
        ),
        (
            "External benchmark crosswalk",
            "How adjacent measurement work is used for denominator and validity checks.",
            "analysis/external_crosschecks/README.md",
        ),
        (
            "Human audit console",
            "H2/H3 forms for collecting human audit records and patch templates.",
            "audit.html",
        ),
        (
            "H1 IRR packet",
            "Separate blank-workbook packet for independent-human recoding.",
            "h1_irr_packet/index.html",
        ),
        (
            "Paper tables",
            "Reproducible tables generated from YAML and derived panels.",
            "analysis/paper_tables/README.md",
        ),
        (
            "Coverage matrix",
            "Event by layer denominator eligibility and rate-reportability.",
            "derived/coverage_matrix.md",
        ),
        (
            "Trigger registry",
            "Sampling-frame and pre-admission trigger accounting.",
            "analysis/trigger_registry/trigger_registry.md",
        ),
        (
            "Source manifest",
            "SHA-256 inventory for local source artifacts.",
            "sources/source_manifest.md",
        ),
        (
            "LLM expert audit",
            "Multi-expert pre-audit; not human provenance.",
            "analysis/llm_expert_audit/README.md",
        ),
        (
            "Human audit queue",
            "Open human-only blockers for strict submission mode.",
            "human-audit.md",
        ),
        (
            "v0.3 review queue",
            "Machine-prepared review queue over the expanded 262-row ingestion corpus.",
            "analysis/review_queue/review_queue.md",
        ),
        (
            "v0.3 triage summary",
            "Pre-human split between machine-ready rows and rows still needing source repair.",
            "analysis/review_queue/v0_3_review_triage_summary.md",
        ),
        (
            "Source discovery worklist",
            "Rows still blocked on primary observation evidence or methodology repair.",
            "analysis/review_queue/source_discovery_worklist.md",
        ),
        (
            "Non-human todo list",
            "Completed non-human tasks and the remaining handoff boundary before audit.",
            "analysis/review_queue/non_human_todo_list.md",
        ),
    ]
    html_cards = []
    for title, desc, href in cards:
        html_cards.append(
            '<article class="artifact-card">'
            '<div class="label">artifact</div>'
            f'<h3>{escape(title)}</h3>'
            f'<p>{escape(desc)}</p>'
            f'<a class="stretch" href="{escape(href)}">Open artifact</a>'
            '</article>'
        )
    return '<div class="artifact-grid">' + "".join(html_cards) + "</div>"


# ---------------------------------------------------------------------------
# Findings & cross-layer analysis (expressive dashboard layer)
# ---------------------------------------------------------------------------

ARCHETYPE_ORDER = [
    "cex_only", "frontend_only", "asset_only",
    "multi_layer", "other_single_layer", "null_event",
]
ARCHETYPE_LABEL = {
    "cex_only": "Off-ramp / CEX",
    "frontend_only": "Frontend",
    "asset_only": "Asset on-chain",
    "multi_layer": "Multi-layer cascade",
    "other_single_layer": "Other single layer",
    "null_event": "Null (no observed change)",
}
ARCHETYPE_COLOR = {
    "cex_only": "var(--layer-offramp_cex)",
    "frontend_only": "var(--layer-l4_frontend)",
    "asset_only": "var(--layer-asset_onchain)",
    "multi_layer": "var(--layer-l1_consensus)",
    "other_single_layer": "var(--layer-l3_rpc)",
    "null_event": "color-mix(in srgb, var(--text-soft) 55%, transparent)",
}
COVERAGE_ORDER = ["measured", "partially_measured", "not_measured", "not_applicable"]
COVERAGE_LABEL = {
    "measured": "measured",
    "partially_measured": "partial",
    "not_measured": "observability gap",
    "not_applicable": "not applicable",
}
COVERAGE_COLOR = {
    "measured": "var(--ok-fg)",
    "partially_measured": "var(--warn-fg)",
    "not_measured": "var(--bad-fg)",
    "not_applicable": "color-mix(in srgb, var(--text-soft) 40%, transparent)",
}
EUROPE_CODES = {
    "EU", "UK", "CH", "DE", "NL", "FR", "PL", "PT", "BE", "NO",
    "DK", "IE", "ES", "IT", "AT", "SE", "FI", "CY", "MT", "LU",
}


def event_archetype(event: dict) -> str:
    """Deterministic archetype (mirrors derived/event_archetypes rules)."""
    ch = changed_layers(event)
    n = len(ch)
    if n == 0:
        return "null_event"
    if n >= 2:
        return "multi_layer"
    if ch == {"asset_onchain"}:
        return "asset_only"
    if ch == {"l4_frontend"}:
        return "frontend_only"
    if ch == {"offramp_cex"}:
        return "cex_only"
    return "other_single_layer"


def compute_corpus_analytics(events: list[dict]) -> dict[str, Any]:
    arch: collections.Counter = collections.Counter()
    arch_by_year: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    locus: collections.Counter = collections.Counter()
    cov: dict[str, collections.Counter] = {L: collections.Counter() for L in LAYER_ORDER}
    jur: collections.Counter = collections.Counter()
    region: collections.Counter = collections.Counter()
    evidence: collections.Counter = collections.Counter()
    for e in events:
        a = event_archetype(e)
        arch[a] += 1
        y = str((e.get("trigger") or {}).get("timestamp", ""))[:4]
        if y.isdigit():
            arch_by_year[y][a] += 1
        for layer in changed_layers(e):
            locus[layer] += 1
        for row in e.get("coverage") or []:
            if isinstance(row, dict) and row.get("layer") in cov:
                cov[row["layer"]][row.get("status") or "unknown"] += 1
        jset = set(e.get("jurisdiction") or [])
        for j in jset:
            jur[j] += 1
        if "US" in jset:
            region["US"] += 1
        if jset & EUROPE_CODES:
            region["Europe"] += 1
        if "corporate_global" in jset:
            region["Corporate"] += 1
        if jset - EUROPE_CODES - {"US", "corporate_global", "UN"}:
            region["Rest of world"] += 1
        evidence[e.get("evidence_tier") or "admission_grade"] += 1
    return {
        "n": len(events),
        "arch": arch,
        "arch_by_year": arch_by_year,
        "locus": locus,
        "cov": cov,
        "jur": jur,
        "region": region,
        "evidence": evidence,
    }


def load_review_readiness() -> dict[str, Any] | None:
    """Canonical release-readiness rollup, parsed from analysis/review-report.md
    (the project's own reported headline) so the dashboard matches the report
    rather than re-deriving it. Falls back to None if the report is absent."""
    try:
        text = (REPO_ROOT / "analysis/review-report.md").read_text()
    except (FileNotFoundError, OSError):
        return None

    def grab(label: str) -> int | None:
        m = re.search(re.escape(label) + r":\s*`?(\d+)`?", text)
        return int(m.group(1)) if m else None

    ready = grab("Release-ready cases")
    blocked = grab("Admitted but release-blocked cases")
    if ready is None or blocked is None:
        return None
    return {
        "ready": ready,
        "blocked": blocked,
        "total": ready + blocked,
        "complete": grab("Fully complete release-ready cases") or 0,
        "scoped": grab("Scope-limited release-ready cases") or 0,
    }


def _pct(n: int, d: int) -> float:
    return (100.0 * n / d) if d else 0.0


def viz_meter(pct: float, color: str, label: str = "") -> str:
    """A single proportional fill bar."""
    return (
        f'<div class="viz-meter" title="{escape(label)}">'
        f'<span style="width:{max(0.0, min(100.0, pct)):.1f}%;background:{color}"></span></div>'
    )


def viz_stack(segments: list[tuple[int, str, str]], total: int) -> str:
    """A stacked proportional bar. segments = [(value, color, label)]."""
    total = total or 1
    parts = []
    for value, color, label in segments:
        if value <= 0:
            continue
        parts.append(
            f'<span style="width:{_pct(value, total):.2f}%;background:{color}" '
            f'title="{escape(label)}: {value} ({_pct(value, total):.0f}%)"></span>'
        )
    return f'<div class="viz-stack">{"".join(parts)}</div>'


def render_findings_band(an: dict, region: collections.Counter) -> str:
    n = an["n"] or 1
    arch = an["arch"]
    locus = an["locus"]
    cex = arch.get("cex_only", 0)
    casc = arch.get("multi_layer", 0)
    l0 = locus.get("l0_network", 0)
    us = region.get("US", 0)
    nul = arch.get("null_event", 0)
    findings = [
        (f"{_pct(cex, n):.0f}%", cex, "land at the off-ramp (CEX) layer",
         "The fiat off-ramp is where most observed crypto censorship lands — not the protocol.",
         _pct(cex, n), "var(--layer-offramp_cex)"),
        (f"{_pct(casc, n):.0f}%", casc, "are true multi-layer cascades",
         "Cross-layer cascades are rare; most events change a single layer or none.",
         _pct(casc, n), "var(--layer-l1_consensus)"),
        (f"{l0}", l0, "events have an observed L0 network block",
         "The network layer is almost never the observed locus (38 rows are observability gaps).",
         _pct(l0, n), "var(--layer-l0_network)"),
        (f"{_pct(us, n):.0f}%", us, "of events touch a US trigger",
         "US enforcement dominates the corpus, with a long nation-state tail.",
         _pct(us, n), "var(--accent)"),
        (f"{_pct(nul, n):.0f}%", nul, "are null events (no observed change)",
         "Designations with no measured downstream effect — denominator controls, not absences.",
         _pct(nul, n), "color-mix(in srgb, var(--text-soft) 55%, transparent)"),
    ]
    cards = []
    for big, _count, label, detail, pct, color in findings:
        cards.append(
            '<article class="finding-card">'
            f'<div class="finding-number" style="color:{color}">{escape(big)}</div>'
            f'<div class="finding-label">{escape(label)}</div>'
            f'{viz_meter(pct, color)}'
            f'<p class="finding-detail">{escape(detail)}</p>'
            '</article>'
        )
    return f'<div class="findings-grid" aria-label="Headline findings">{"".join(cards)}</div>'


def render_layer_locus(an: dict) -> str:
    """Signature view: where observed censorship lands across the six layers."""
    locus = an["locus"]
    cov = an["cov"]
    mx = max([locus.get(L, 0) for L in LAYER_ORDER] + [1])
    ranked = sorted(LAYER_ORDER, key=lambda L: locus.get(L, 0), reverse=True)
    rows = []
    for layer in ranked:
        v = locus.get(layer, 0)
        gap = cov[layer].get("not_measured", 0)
        gap_note = f' · <span class="gap">{gap} gap</span>' if gap else ""
        rows.append(
            '<div class="locus-row">'
            f'<div class="locus-name"><span class="dot" style="background:var(--layer-{layer})"></span>{escape(LAYER_LABEL[layer])}</div>'
            f'<div class="locus-track"><span style="width:{_pct(v, mx):.1f}%;background:var(--layer-{layer})"></span></div>'
            f'<div class="locus-val"><strong>{v}</strong>{gap_note}</div>'
            '</div>'
        )
    return f'<div class="locus-board">{"".join(rows)}</div>'


def render_temporal_evolution(an: dict) -> str:
    """Archetype mix by year — how the locus of censorship shifted over time."""
    aby = an["arch_by_year"]
    years = sorted(y for y in aby if y.isdigit())
    if not years:
        return ""
    mx = max((sum(aby[y].values()) for y in years), default=1)
    rows = []
    for y in years:
        c = aby[y]
        tot = sum(c.values())
        segs = [(c.get(a, 0), ARCHETYPE_COLOR[a], ARCHETYPE_LABEL[a]) for a in ARCHETYPE_ORDER]
        rows.append(
            '<div class="year-row">'
            f'<div class="year-name">{escape(y)}</div>'
            f'<div class="year-track" style="--scale:{_pct(tot, mx):.1f}%">{viz_stack(segs, tot)}</div>'
            f'<div class="year-val">{tot}</div>'
            '</div>'
        )
    legend = "".join(
        f'<span class="legend-item"><span class="sw" style="background:{ARCHETYPE_COLOR[a]}"></span>{escape(ARCHETYPE_LABEL[a])}</span>'
        for a in ARCHETYPE_ORDER
    )
    return f'<div class="legend">{legend}</div><div class="year-board">{"".join(rows)}</div>'


def render_coverage_honesty(an: dict) -> str:
    """Denominator honesty: measured vs partial vs observability-gap per layer."""
    cov = an["cov"]
    rows = []
    for layer in LAYER_ORDER:
        c = cov[layer]
        tot = sum(c.get(s, 0) for s in COVERAGE_ORDER) or 1
        segs = [(c.get(s, 0), COVERAGE_COLOR[s], COVERAGE_LABEL[s]) for s in COVERAGE_ORDER]
        measured = c.get("measured", 0) + c.get("partially_measured", 0)
        rows.append(
            '<div class="cov-row">'
            f'<div class="cov-name"><span class="dot" style="background:var(--layer-{layer})"></span>{escape(LAYER_LABEL[layer])}</div>'
            f'<div class="cov-track">{viz_stack(segs, tot)}</div>'
            f'<div class="cov-val">{measured} obs.</div>'
            '</div>'
        )
    legend = "".join(
        f'<span class="legend-item"><span class="sw" style="background:{COVERAGE_COLOR[s]}"></span>{escape(COVERAGE_LABEL[s])}</span>'
        for s in COVERAGE_ORDER
    )
    return f'<div class="legend">{legend}</div><div class="cov-board">{"".join(rows)}</div>'


def render_jurisdiction(an: dict) -> str:
    jur = an["jur"]
    region = an["region"]
    n = an["n"] or 1
    region_rows = []
    for name in ("US", "Europe", "Rest of world", "Corporate"):
        v = region.get(name, 0)
        region_rows.append(
            '<div class="jur-row">'
            f'<div class="jur-name">{escape(name)}</div>'
            f'<div class="jur-track"><span style="width:{_pct(v, n):.1f}%"></span></div>'
            f'<div class="jur-val"><strong>{v}</strong> · {_pct(v, n):.0f}%</div>'
            '</div>'
        )
    top = jur.most_common(12)
    mx = max([v for _, v in top] + [1])
    country_rows = []
    for code, v in top:
        country_rows.append(
            '<div class="jur-row mini">'
            f'<div class="jur-name"><code>{escape(code)}</code></div>'
            f'<div class="jur-track"><span style="width:{_pct(v, mx):.1f}%"></span></div>'
            f'<div class="jur-val">{v}</div>'
            '</div>'
        )
    return (
        '<div class="jur-grid">'
        '<div class="jur-col"><h3>By region <span class="meta">(inclusive — events may touch several)</span></h3>'
        f'{"".join(region_rows)}</div>'
        '<div class="jur-col"><h3>Top jurisdictions</h3>'
        f'{"".join(country_rows)}</div>'
        '</div>'
    )


def render_readiness(an: dict, readiness: dict | None) -> str:
    evidence = an["evidence"]
    attested = evidence.get("attested_secondary", 0)
    grade = evidence.get("admission_grade", 0)
    blocks = []
    if readiness:
        total = readiness["total"] or 1
        ready = readiness["ready"]
        blocked = readiness["blocked"]
        segs = [
            (ready, "var(--ok-fg)", "release-ready"),
            (blocked, "var(--warn-fg)", "admitted but blocked"),
        ]
        blocks.append(
            '<div class="ready-block">'
            '<div class="ready-head"><strong>Release readiness</strong>'
            f'<span class="meta">{ready} ready · {blocked} blocked of {readiness["total"]} admitted</span></div>'
            f'{viz_stack(segs, total)}'
            '<div class="ready-sub">'
            f'<span><span class="sw" style="background:var(--ok-fg)"></span>release-ready <strong>{ready}</strong> ({readiness["complete"]} complete · {readiness["scoped"]} scoped)</span>'
            f'<span><span class="sw" style="background:var(--warn-fg)"></span>admitted but blocked <strong>{blocked}</strong></span>'
            '</div></div>'
        )
    et_total = (grade + attested) or 1
    et_segs = [
        (grade, "var(--accent)", "admission_grade"),
        (attested, "var(--layer-l4_frontend)", "attested_secondary"),
    ]
    blocks.append(
        '<div class="ready-block">'
        '<div class="ready-head"><strong>Evidence tier</strong>'
        f'<span class="meta">codebook §10 · {attested} admitted below the strict floor, explicitly filterable</span></div>'
        f'{viz_stack(et_segs, et_total)}'
        '<div class="ready-sub">'
        f'<span><span class="sw" style="background:var(--accent)"></span>admission_grade <strong>{grade}</strong></span>'
        f'<span><span class="sw" style="background:var(--layer-l4_frontend)"></span>attested_secondary <strong>{attested}</strong></span>'
        '</div></div>'
    )
    return f'<div class="ready-grid">{"".join(blocks)}</div>'


def render_analysis_block(events: list[dict], meta: dict | None = None) -> str:
    an = compute_corpus_analytics(events)
    readiness = load_review_readiness()
    return f"""
  <div class="section-heading" id="findings">
    <div>
      <h2>What this corpus shows</h2>
      <p class="meta">Headline patterns across the {an['n']} admitted records. These describe this curated corpus, not the external population of all censorship events.</p>
    </div>
  </div>
  {render_findings_band(an, an['region'])}

  <div class="section-heading" id="where-it-lands">
    <div>
      <h2>Where censorship lands</h2>
      <p class="meta">Count of events with an <strong>observed change</strong> at each layer. The off-ramp (CEX) layer dominates; the network/consensus/RPC base is rarely the observed locus.</p>
    </div>
  </div>
  {render_layer_locus(an)}

  <div class="section-heading" id="evolution">
    <div>
      <h2>How the locus shifted over time</h2>
      <p class="meta">Archetype mix by trigger year (bar length scaled to that year's event count). Off-ramp/CEX restrictions grew to dominate as the corpus moves toward the present.</p>
    </div>
  </div>
  {render_temporal_evolution(an)}

  <div class="section-heading" id="measurability">
    <div>
      <h2>Measurability &amp; the denominator</h2>
      <p class="meta">Per-layer coverage status. An <span style="color:var(--bad-fg)">observability gap</span> means the layer is unmeasured under the frame — never read it as censorship absence.</p>
    </div>
  </div>
  {render_coverage_honesty(an)}

  <div class="section-heading" id="jurisdiction">
    <div>
      <h2>Jurisdictional concentration</h2>
      <p class="meta">Which actors drive the corpus. Region rows are inclusive, so an event touching several regions counts in each.</p>
    </div>
  </div>
  {render_jurisdiction(an)}

  <div class="section-heading" id="readiness">
    <div>
      <h2>Evidence quality &amp; release readiness</h2>
      <p class="meta">The corpus is transparent about what is release-ready vs still blocked, and which rows sit on the lower <code>attested_secondary</code> evidence tier.</p>
    </div>
  </div>
  {render_readiness(an, readiness)}
"""


def render_index(events: list[dict], meta: dict | None = None) -> str:
    meta = meta or load_meta()
    dv = meta.get("dataset_version") or "unknown"
    cutoff = meta.get("cutoff_date") or "n/a"
    commit = meta.get("source_commit") or ""
    generated_stamp = now_utc_datetime().strftime("%Y-%m-%d %H:%M UTC")
    shape_counts: collections.Counter = collections.Counter(
        e.get("empirical_shape") for e in events
    )
    tier_counts: collections.Counter = collections.Counter(
        e.get("admission_tier") for e in events
    )
    stratum_counts: collections.Counter = collections.Counter(
        e.get("research_stratum") for e in events
    )
    year_counts: collections.Counter = collections.Counter()
    chain_counts: collections.Counter = collections.Counter()
    for e in events:
        ts = str((e.get("trigger") or {}).get("timestamp", ""))[:4]
        if ts.isdigit():
            year_counts[ts] += 1
        for c in (e.get("target") or {}).get("chains") or []:
            chain_counts[c] += 1

    shape_chips = chip_group(
        "shape", "shape",
        [(k, shape_counts.get(k, 0)) for k in ("cascade", "comparison", "null_event")],
    )
    tier_chips = chip_group(
        "tier", "tier",
        [(k, tier_counts.get(k, 0)) for k in ("anchor_case", "empirical_case", "null_case")],
    )
    stratum_chips = chip_group(
        "stratum", "stratum",
        sorted(
            [(k, v) for k, v in stratum_counts.items() if k],
            key=lambda x: x[0],
        ),
    )
    year_chips = chip_group(
        "year", "year",
        sorted(year_counts.items(), key=lambda x: x[0], reverse=True),
    )
    chain_chips = chip_group(
        "chain", "chain",
        chain_counts.most_common(10),
    )

    # ---- events table ----
    events_sorted = sorted(
        events,
        key=lambda e: str((e.get("trigger") or {}).get("timestamp", "")),
    )
    rows = []
    for e in events_sorted:
        slug = e.get("id", "—")
        trig = e.get("trigger") or {}
        ts = str(trig.get("timestamp") or "")[:10]
        year = ts[:4]
        shape = e.get("empirical_shape") or ""
        tier = e.get("admission_tier") or ""
        stratum = e.get("research_stratum") or ""
        trig_type = trig.get("type") or ""
        chains = (e.get("target") or {}).get("chains") or []
        chains_s = ", ".join(chains) or "—"
        jurs = e.get("jurisdiction") or []
        jur_s = ", ".join(jurs) or "—"
        n_obs = len(e.get("observations") or [])
        n_addr = len((e.get("target") or {}).get("addresses") or [])
        n_changed = len(changed_layers(e))

        search_blob = " ".join(
            x for x in [
                slug, trig_type, stratum, chains_s.lower(), jur_s.lower(),
                titleify(slug).lower(),
                (trig.get("actor") or "").lower(),
                " ".join(str(t).lower() for t in (e.get("tags") or [])),
                (e.get("target") or {}).get("protocol", "") or "",
                (e.get("target") or {}).get("entity", "") or "",
            ] if x
        )

        rows.append(
            f'<tr class="event-row" '
            f'data-slug="{escape(slug)}" '
            f'data-shape="{escape(shape)}" '
            f'data-tier="{escape(tier)}" '
            f'data-stratum="{escape(stratum)}" '
            f'data-year="{escape(year)}" '
            f'data-chain="{escape("|".join(chains))}" '
            f'data-date="{escape(ts)}" '
            f'data-changed="{n_changed}" '
            f'data-search="{escape(search_blob.lower())}"'
            ">"
            f'<td class="date">{escape(ts) or "—"}</td>'
            f'<td class="slug"><a href="events/{escape(slug)}.html">{escape(titleify(slug))}</a>'
            f'<div class="meta"><code>{escape(slug)}</code></div></td>'
            f'<td>{pill(shape or "—", shape)}</td>'
            f'<td>{pill(tier or "—", tier)}</td>'
            f'<td>{render_cascade_dots(e)}</td>'
            f'<td><code style="font-size:.82em">{escape(trig_type) or "—"}</code></td>'
            f'<td class="col-hide-mobile">{escape(chains_s)}</td>'
            f'<td class="col-hide-mobile">{escape(jur_s)}</td>'
            f'<td class="size">{n_addr} addr · {n_obs} obs</td>'
            "</tr>"
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Cross-Layer Censorship Event Database — {len(events)} curated crypto censorship events across six layers (network, consensus, RPC, frontend, asset, off-ramp) with precision-aware timelines and primary-source evidence.">
  <title>Chain Censorship Events Database</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
<header class="site-header">
  <div class="site-header-inner">
    <div class="brand"><a href="./index.html">Chain Censorship Events</a><span class="brand-tag">database</span></div>
    <div class="header-spacer"></div>
    <a class="header-link optional" href="#findings">Findings</a>
    <a class="header-link optional" href="#layers">Layers</a>
    <a class="header-link optional" href="#artifacts">Artifacts</a>
    <a class="header-link optional" href="#events">Events</a>
    <a class="header-link optional" href="audit.html">Audit</a>
    <a class="header-link" href="https://github.com/chnyangs/censorship-event-database" rel="noopener">GitHub</a>
    <button id="theme-toggle" class="theme-toggle" type="button" aria-label="Toggle theme">☀ light</button>
  </div>
</header>

<main class="page">
  <section class="dashboard-hero" id="overview">
    <div class="hero-copy">
      <div class="hero-kicker">Measurement protocol plus reproducible corpus</div>
      <h1>Cross-layer censorship events.</h1>
      <p class="hero-lede">
        A curated event database that links legal, regulatory, state, and corporate
        triggers to observed reactions across L0 network, L1 consensus, L3 RPC,
        frontend, asset on-chain, and off-ramp CEX layers. The dashboard is a
        navigation surface for the measurement artifacts, not a prevalence claim
        about all censorship events.
      </p>
      <div class="hero-actions">
        <a class="button" href="#events">Browse the corpus</a>
        <a class="button secondary" href="docs/paper_claims.md">Read claim boundaries</a>
        <a class="button secondary" href="audit.html">Human audit console</a>
        <a class="button secondary" href="analysis/llm_expert_audit/README.md">LLM audit notes</a>
      </div>
    </div>
    <aside class="snapshot-panel" aria-label="Dataset snapshot">
      <div class="snapshot-head">
        <div class="label">dataset snapshot</div>
        <div class="version">v{escape(dv)}</div>
        <div class="meta">cutoff <code>{escape(cutoff)}</code>{f' · commit <code>{escape(commit)}</code>' if commit else ''}</div>
      </div>
      <div class="status-line"><span><span class="label">machine gate</span><br><strong><code>make paper-check</code> gate</strong></span><span class="status-dot info"></span></div>
      <div class="status-line"><span><span class="label">reliability</span><br><strong>LLM self-consistency only</strong></span><span class="status-dot warn"></span></div>
      <div class="status-line"><span><span class="label">human audit</span><br><strong>strict submission pending</strong></span><span class="status-dot warn"></span></div>
    </aside>
  </section>

  {render_signal_cards(events, shape_counts, tier_counts)}
  {render_review_queue_dashboard()}

  {render_analysis_block(events, meta)}

  <section class="boundary-note">
    <strong>Interpretation boundary.</strong>
    Off-ramp CEX null rows are public-evidence disclosure nulls, not proof that
    no private exchange action occurred. L0/L3 gaps are denominator gaps unless
    a measurement substrate is explicitly present. Current kappa is LLM-assisted
    self-consistency, not independent-human IRR.
  </section>

  <div class="section-heading" id="layers">
    <div>
      <h2>Layer Observability</h2>
      <p class="meta">Each layer card separates observed changes, observed no-change rows, and the measured/partial coverage denominator.</p>
    </div>
  </div>
  {render_layer_board(events)}

  <div class="section-heading">
    <div>
      <h2>Corpus Distribution</h2>
      <p class="meta">Frame shape and source availability at a glance. Counts describe this admitted corpus, not the external population.</p>
    </div>
  </div>
  {render_distribution_cards(events)}

  <div class="section-heading" id="artifacts">
    <div>
      <h2>Artifact Map</h2>
      <p class="meta">Start here when reviewing methodology, paper claims, denominators, source hashes, or audit status.</p>
    </div>
  </div>
  {render_artifact_cards()}

  <div class="section-heading" id="events">
    <div>
      <h2>Event Explorer</h2>
      <p class="meta">Search and filter the {len(events)} admitted records. Filter state is encoded in the URL hash for shareable views.</p>
    </div>
    <span id="result-count" class="result-count">{len(events)} / {len(events)} events</span>
  </div>

  <details class="filter-drawer" open>
    <summary><span class="title">Filters</span><span class="hint">shape, tier, stratum, year, chain, and text search</span></summary>
    <div class="filter-bar" role="region" aria-label="Filters">
      <div class="filter-row">
        <label class="filter-search">
          <span class="visually-hidden" style="display:none">Search</span>
          <input id="filter-search" type="search" placeholder="Search slug, trigger, actor, jurisdiction…" autocomplete="off">
        </label>
        <button id="filter-reset" class="chip-reset" type="button">Reset filters</button>
      </div>
      <div class="filter-row">{shape_chips}{tier_chips}</div>
      <div class="filter-row">{stratum_chips}{year_chips}{chain_chips}</div>
    </div>
  </details>

  <div class="table-wrap">
    <table class="events" id="events-table">
      <thead><tr>
        <th data-sort="date">Date <span class="arrow">▾</span></th>
        <th data-sort="slug">Event <span class="arrow">▾</span></th>
        <th data-sort="shape">Shape <span class="arrow">▾</span></th>
        <th data-sort="tier">Tier <span class="arrow">▾</span></th>
        <th>Cascade</th>
        <th data-sort="stratum">Trigger <span class="arrow">▾</span></th>
        <th class="col-hide-mobile">Chains</th>
        <th class="col-hide-mobile">Jurisdiction</th>
        <th data-sort="changed" class="size">Size <span class="arrow">▾</span></th>
      </tr></thead>
      <tbody>{"".join(rows)}</tbody>
    </table>
  </div>

  <h2>Framework tools</h2>
  <p class="meta">Three tools built on the dataset. Each is retrieval- and argument-structure-focused; none of them make decisions for you. See <a href="docs/limitations-and-use.md">limitations &amp; use</a> and <a href="docs/citing.md">how to cite</a> before using any output.</p>
  <div class="stat-grid">
    <div class="stat-card">
      <div class="stat-label"><strong>A · Evidence chain</strong></div>
      <p class="meta" style="margin:.3rem 0 0">Per-event claim → observations → primary sources (body_hash) → gaps. Run <code>scripts/render_evidence_chain.py &lt;slug&gt;</code>.</p>
    </div>
    <div class="stat-card">
      <div class="stat-label"><strong>B · Comparable-case finder</strong></div>
      <p class="meta" style="margin:.3rem 0 0">Retrieves historical precedents structurally similar to a reference event, with transparent similarity weights. Not predictive.</p>
    </div>
    <div class="stat-card">
      <div class="stat-label"><strong>C · Decision rubric</strong></div>
      <p class="meta" style="margin:.3rem 0 0">Hand-followed structural checklist; maps features to pattern classes. Comparative only — never a substitute for expert judgment.</p>
    </div>
  </div>

  <h2>About</h2>
  <p>Schema v{escape(meta.get('schema_version') or '0.2.0')}. Each event YAML carries a <strong>trigger</strong> (legal / corporate action with primary citations), a <strong>target</strong> (address set / entity / domain), six <strong>coverage</strong> entries (measured / partially_measured / not_measured / not_applicable), layer-level <strong>observations</strong> with attribution grading, and a <strong>scoped_claim</strong> — the defensible single sentence the event supports. See <a href="docs/methodology.md">methodology</a>, <a href="docs/datasheet.md">datasheet</a>, <a href="docs/limitations-and-use.md">limitations &amp; use</a>.</p>

  <h2>Cite this dataset</h2>
  <p>This release is <strong>version {escape(dv)}</strong>, cutoff <code>{escape(cutoff)}</code>{f' (source commit <code>{escape(commit)}</code>)' if commit else ''}. Machine-readable metadata: <a href="CITATION.cff">CITATION.cff</a> · <a href="dataset.meta.json">dataset.meta.json</a>. Citation templates in <a href="docs/citing.md">docs/citing.md</a>. Once the first tagged release is made, Zenodo mints a DOI you can pin against.</p>

  <footer class="site-footer">
    <div>Generated {generated_stamp} · {len(events)} events · v{escape(dv)} · cutoff {escape(cutoff)}</div>
    <div><a href="raw/">admitted raw YAMLs</a> · <a href="https://github.com/chnyangs/censorship-event-database">GitHub</a></div>
  </footer>
</main>

<script src="site.js"></script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

def copy_yaml_raw(events_dir: pathlib.Path, site_dir: pathlib.Path) -> None:
    raw_dir = site_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    for src in events_dir.glob("*.yaml"):
        event = yaml.safe_load(src.read_text())
        if isinstance(event, dict) and event.get("status") == "admitted":
            shutil.copy2(src, raw_dir / src.name)


def copy_docs_tree(docs_dir: pathlib.Path, site_dir: pathlib.Path) -> int:
    """Copy docs/*.md (and any static image/pdf siblings) into site/docs/ so
    that in-site links like `docs/limitations-and-use.md` resolve after
    deploy. Previously the site pointed at `raw/../docs/...` which broke on
    GitHub Pages because `docs/` wasn't part of the published bundle."""
    if not docs_dir.is_dir():
        return 0
    dest = site_dir / "docs"
    dest.mkdir(parents=True, exist_ok=True)
    n = 0
    for src in docs_dir.rglob("*"):
        if not src.is_file():
            continue
        rel = src.relative_to(docs_dir)
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, target)
        n += 1
    return n


def copy_dashboard_artifacts(site_dir: pathlib.Path) -> int:
    """Publish the dashboard's linked research artifacts.

    The site is static, so links in the artifact map must resolve after deploy.
    Keep this whitelist tight: copy the review-facing summaries and manifests,
    not every local source capture or bulky analysis output.
    """
    copied = 0
    file_globs = [
        "human-audit.md",
        "analysis/a_class_submission_gap_report.md",
        "analysis/external_crosschecks/*",
        "analysis/evidence-chains/*.md",
        "analysis/audit_worksheets/*.md",
        "analysis/llm_expert_audit/*.md",
        "analysis/paper_tables/*",
        "analysis/review_queue/*.csv",
        "analysis/review_queue/*.json",
        "analysis/review_queue/*.jsonl",
        "analysis/review_queue/*.md",
        "analysis/review_queue/packets/*.csv",
        "analysis/review_queue/packets/*.json",
        "analysis/review_queue/packets/*.md",
        "analysis/trigger_registry/*",
        "derived/*.md",
        "derived/*.csv",
        "derived/*.json",
        "derived/*.meta.json",
        "sources/source_manifest.*",
    ]
    seen: set[pathlib.Path] = set()
    for pattern in file_globs:
        for src in sorted(REPO_ROOT.glob(pattern)):
            if not src.is_file():
                continue
            if src in seen:
                continue
            seen.add(src)
            rel = src.relative_to(REPO_ROOT)
            dest = site_dir / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
            copied += 1

    # Include only the source captures needed by the null-case audit console,
    # not the full sources/ tree.
    for slug in NULL_DENOMINATOR_AUDIT_CASES:
        for base_rel in (
            pathlib.Path("sources/http_captures") / slug,
            pathlib.Path("sources/l0_datasets") / slug,
        ):
            base = REPO_ROOT / base_rel
            if not base.is_dir():
                continue
            for src in sorted(base.rglob("*")):
                if not src.is_file() or src in seen:
                    continue
                seen.add(src)
                rel = src.relative_to(REPO_ROOT)
                dest = site_dir / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dest)
                copied += 1
    return copied


def copy_meta(site_dir: pathlib.Path) -> None:
    """Publish CITATION.cff + dataset.meta.json alongside the site so
    citation tooling / consumers can fetch them via Pages URL."""
    for name in ("CITATION.cff", "dataset.meta.json"):
        src = REPO_ROOT / name
        if src.exists():
            shutil.copy2(src, site_dir / name)


def _has_symlink_component(path: pathlib.Path) -> bool:
    """Refuse destructive cleanup through any symlinked path component."""
    candidate = path.expanduser()
    for part in (candidate, *candidate.parents):
        if part.is_symlink():
            return True
    return False


def prepare_site_dir(site_dir: pathlib.Path) -> pathlib.Path:
    """Create an empty output directory without risking repo data loss."""
    raw_path = site_dir.expanduser()
    if _has_symlink_component(raw_path):
        raise SystemExit(f"[render_site] refusing symlinked --site-dir: {raw_path}")

    resolved = raw_path.resolve()
    repo_root = REPO_ROOT.resolve()
    protected_roots = [
        (repo_root / ".git").resolve(),
        EVENTS_DIR.resolve(),
        DOCS_DIR.resolve(),
        (repo_root / "schema").resolve(),
        (repo_root / "scripts").resolve(),
        (repo_root / "sources").resolve(),
        (repo_root / "analysis").resolve(),
        (repo_root / "derived").resolve(),
        (repo_root / "tests").resolve(),
        (repo_root / ".github").resolve(),
    ]

    if resolved == repo_root or resolved in repo_root.parents:
        raise SystemExit(f"[render_site] refusing unsafe --site-dir: {resolved}")
    for protected in protected_roots:
        if resolved == protected or protected in resolved.parents:
            raise SystemExit(f"[render_site] refusing unsafe --site-dir: {resolved}")
    if (resolved / ".git").exists():
        raise SystemExit(f"[render_site] refusing to delete git checkout: {resolved}")

    if resolved.exists():
        marker = resolved / SITE_MARKER
        default_site_dir = SITE_DIR.resolve()
        if resolved != default_site_dir and not marker.exists():
            raise SystemExit(
                f"[render_site] refusing to delete existing unmarked --site-dir: {resolved}"
            )
        shutil.rmtree(resolved)
    resolved.mkdir(parents=True)
    (resolved / SITE_MARKER).write_text(
        "Generated by scripts/render_site.py; safe to replace.\n"
    )
    return resolved


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--events-dir", default=str(EVENTS_DIR))
    p.add_argument("--site-dir", default=str(SITE_DIR))
    args = p.parse_args()

    events_dir = pathlib.Path(args.events_dir)
    site_dir = prepare_site_dir(pathlib.Path(args.site_dir))
    (site_dir / "events").mkdir(parents=True)

    events: list[dict] = []
    for f in sorted(events_dir.glob("*.yaml")):
        event = yaml.safe_load(f.read_text())
        if isinstance(event, dict) and event.get("status") == "admitted":
            events.append(event)
    meta = load_meta()
    print(
        f"[render_site] loaded {len(events)} events · "
        f"dataset v{meta.get('dataset_version')} · cutoff {meta.get('cutoff_date')}"
    )

    (site_dir / "styles.css").write_text(STATIC_CSS)
    (site_dir / "site.js").write_text(STATIC_JS)

    for e in events:
        slug = e.get("id", "unknown")
        (site_dir / "events" / f"{slug}.html").write_text(render_event_page(e, events, meta))

    copy_yaml_raw(events_dir, site_dir)
    n_docs = copy_docs_tree(DOCS_DIR, site_dir)
    n_artifacts = copy_dashboard_artifacts(site_dir)
    copy_meta(site_dir)
    n_irr = write_h1_irr_packet(site_dir, meta)

    (site_dir / "index.html").write_text(render_index(events, meta))
    (site_dir / "audit.html").write_text(render_audit_console(events, site_dir, meta))

    print(
        f"[render_site] wrote {site_dir}/index.html + {len(events)} per-event pages + "
        f"raw/ + docs/ ({n_docs} files) + dashboard artifacts ({n_artifacts} files) "
        f"+ H1 IRR packet ({n_irr} files) + CITATION.cff + dataset.meta.json"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
