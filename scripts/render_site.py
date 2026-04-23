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
import html
import json
import pathlib
import re
import shutil
import sys
from datetime import datetime, timezone
from typing import Any

import yaml


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
DOCS_DIR = REPO_ROOT / "docs"
SITE_DIR = REPO_ROOT / "site"

# Shared dataset-identity accessor (see scripts/_dataset_meta.py).
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import load_meta  # noqa: E402

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

  --font-body: -apple-system, BlinkMacSystemFont, "Inter", "Segoe UI", Roboto, sans-serif;
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
  background: var(--bg);
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
  background: var(--bg);
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

/* ------------------------------------------------------------- index hero */
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
  position: sticky; top: calc(54px + 96px); z-index: 10;
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
@media (max-width: 700px) {
  .site-header-inner { padding: 8px 0.8rem; }
  .header-link { display: none; }
  .page { padding: 0 0.8rem 3rem; }
  h1 { font-size: 1.5rem; }
  h2 { font-size: 1.1rem; }
  .hero { padding: 1.1rem 1.1rem 0.9rem; }
  .stat-grid { grid-template-columns: repeat(2, 1fr); gap: 0.55rem; }
  .stat-card { padding: 10px 12px; }
  .stat-number { font-size: 1.4rem; }
  .filter-bar { top: 48px; }
  table.events thead th { top: calc(48px + 120px); font-size: 0.75rem; padding: 6px 8px; }
  table.events tbody td { padding: 8px 8px; }
  table.events .col-hide-mobile { display: none; }
  .kv-list { grid-template-columns: 1fr; }
  .prev-next { grid-template-columns: 1fr; }
}

@media print {
  .site-header, .filter-bar, .theme-toggle, .prev-next { display: none !important; }
  body { background: #fff; color: #000; }
  .section-card { break-inside: avoid; }
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


def render_event_page(event: dict, all_events: list[dict], meta: dict | None = None) -> str:
    meta = meta or load_meta()
    dv = meta.get("dataset_version") or "unknown"
    cutoff = meta.get("cutoff_date") or "n/a"
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
    <div>Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} from <code>events/{escape(slug)}.yaml</code> · dataset v{escape(dv)} · cutoff {escape(cutoff)}. See <a href="../docs/citing.md">how to cite</a>.</div>
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


def render_index(events: list[dict], meta: dict | None = None) -> str:
    meta = meta or load_meta()
    dv = meta.get("dataset_version") or "unknown"
    cutoff = meta.get("cutoff_date") or "n/a"
    commit = meta.get("source_commit") or ""
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
  <meta name="description" content="Cross-Layer Censorship Event Database — {len(events)} curated crypto censorship events across six layers (network, consensus, RPC, frontend, asset, off-ramp) with hour-precision timelines and primary-source evidence.">
  <title>Chain Censorship Events Database</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
<header class="site-header">
  <div class="site-header-inner">
    <div class="brand"><a href="./index.html">Chain Censorship Events</a><span class="brand-tag">database</span></div>
    <div class="header-spacer"></div>
    <a class="header-link" href="https://github.com/chnyangs/censorship-event-database" rel="noopener">GitHub</a>
    <button id="theme-toggle" class="theme-toggle" type="button" aria-label="Toggle theme">☀ light</button>
  </div>
</header>

<main class="page">
  <section class="hero">
    <h1>Cross-Layer Censorship Events</h1>
    <p class="hero-lede">
      Curated catalog of crypto censorship events (OFAC SDN, DOJ, SEC/CFTC,
      nation-state, corporate) tracked across six independent layers — network,
      consensus, RPC, frontend, asset on-chain, and off-ramp CEX — with
      hour-precision timelines and primary-source evidence. Every event is
      admitted under a documented multi-source protocol and published as YAML
      with sha256 <code>body_hash</code> archival anchors.
    </p>
    <div class="hero-chips">
      <a href="#shape=cascade">cascade events</a>
      <a href="#tier=anchor_case">anchor cases</a>
      <a href="#stratum=S1_ofac_sdn">OFAC SDN</a>
      <a href="#stratum=S4_nation_state">nation-state</a>
      <a href="#year=2022">2022</a>
      <a href="#year=2025">2025</a>
    </div>
  </section>

  <div class="stat-grid">
    <div class="stat-card">
      <div class="stat-number">{len(events)}</div>
      <div class="stat-label">admitted events</div>
    </div>
    <div class="stat-card shape-cascade">
      <div class="stat-number">{shape_counts.get('cascade', 0)}</div>
      <div class="stat-label">cascade (≥3 layers)</div>
    </div>
    <div class="stat-card shape-comparison">
      <div class="stat-number">{shape_counts.get('comparison', 0)}</div>
      <div class="stat-label">comparison (1–2 layers)</div>
    </div>
    <div class="stat-card shape-null_event">
      <div class="stat-number">{shape_counts.get('null_event', 0)}</div>
      <div class="stat-label">null_event (0 layers)</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">{tier_counts.get('anchor_case', 0)}</div>
      <div class="stat-label">anchor cases</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">{tier_counts.get('empirical_case', 0)}</div>
      <div class="stat-label">empirical cases</div>
    </div>
  </div>

  <h2>Distribution</h2>
  {render_distribution_cards(events)}

  <h2>Events</h2>
  <div class="filter-bar" role="region" aria-label="Filters">
    <div class="filter-row">
      <label class="filter-search">
        <span class="visually-hidden" style="display:none">Search</span>
        <input id="filter-search" type="search" placeholder="Search slug, trigger, actor, jurisdiction…" autocomplete="off">
      </label>
      <button id="filter-reset" class="chip-reset" type="button">Reset filters</button>
      <span id="result-count" class="result-count">{len(events)} / {len(events)} events</span>
    </div>
    <div class="filter-row">{shape_chips}{tier_chips}</div>
    <div class="filter-row">{stratum_chips}{year_chips}{chain_chips}</div>
  </div>

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
    <div>Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} · {len(events)} events · v{escape(dv)} · cutoff {escape(cutoff)}</div>
    <div><a href="raw/">raw YAMLs</a> · <a href="https://github.com/chnyangs/censorship-event-database">GitHub</a></div>
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


def copy_meta(site_dir: pathlib.Path) -> None:
    """Publish CITATION.cff + dataset.meta.json alongside the site so
    citation tooling / consumers can fetch them via Pages URL."""
    for name in ("CITATION.cff", "dataset.meta.json"):
        src = REPO_ROOT / name
        if src.exists():
            shutil.copy2(src, site_dir / name)


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

    events: list[dict] = []
    for f in sorted(events_dir.glob("*.yaml")):
        events.append(yaml.safe_load(f.read_text()))
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

    (site_dir / "index.html").write_text(render_index(events, meta))
    copy_yaml_raw(events_dir, site_dir)
    n_docs = copy_docs_tree(DOCS_DIR, site_dir)
    copy_meta(site_dir)

    print(
        f"[render_site] wrote {site_dir}/index.html + {len(events)} per-event pages + "
        f"raw/ + docs/ ({n_docs} files) + CITATION.cff + dataset.meta.json"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
