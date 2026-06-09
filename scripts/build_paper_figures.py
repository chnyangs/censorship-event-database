"""
build_paper_figures.py — generate IEEE-column-width vector-PDF figures for:
  "A Denominator-Aware Event Corpus for Cross-Layer Crypto Censorship"

Output: 6a1d66df502cdc827ad0999d/figs/{fig2,fig3,fig4,fig5}.pdf

Run:
    python scripts/build_paper_figures.py

Requires: matplotlib, numpy, pyyaml (all standard in a data-science env).
Fails loudly if derived data files are missing.
"""

import json
import sys
import os
import glob
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import yaml

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO = Path(__file__).resolve().parent.parent
EVENTS_DIR       = REPO / "events"
ARCHETYPES_FILE  = REPO / "derived" / "event_archetypes.json"
OBSERV_FILE      = REPO / "derived" / "layer_observability.json"
SENSITIVITY_FILE = REPO / "derived" / "admission_sensitivity.csv"
FIGS_DIR         = REPO / "6a1d66df502cdc827ad0999d" / "figs"

def _require(path: Path) -> None:
    if not path.exists():
        sys.exit(f"ERROR: required file not found: {path}")

for _p in [EVENTS_DIR, ARCHETYPES_FILE, OBSERV_FILE, SENSITIVITY_FILE]:
    _require(_p)

FIGS_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Colorblind-safe palette (Wong 2011)
# We pick a consistent 6-colour subset used across all figures.
# ---------------------------------------------------------------------------
WONG = {
    "black":   "#000000",
    "orange":  "#E69F00",
    "sky":     "#56B4E9",
    "green":   "#009E73",
    "yellow":  "#F0E442",
    "blue":    "#0072B2",
    "red":     "#D55E00",
    "pink":    "#CC79A7",
}

# Stratum colours — consistent with Fig 3 and Fig 4
STRATUM_COLORS = {
    "S1_ofac_sdn":         WONG["red"],
    "S2_ofac_removal":     WONG["pink"],
    "S3_doj_sec_cftc_fiod": WONG["orange"],
    "S4_nation_state":     WONG["blue"],
    "S5_corporate":        WONG["sky"],
    "S6_supranational":    WONG["green"],
}
STRATUM_LABELS = {
    "S1_ofac_sdn":         "S1 OFAC SDN",
    "S2_ofac_removal":     "S2 OFAC removal",
    "S3_doj_sec_cftc_fiod": "S3 DOJ/SEC/CFTC",
    "S4_nation_state":     "S4 Nation-state",
    "S5_corporate":        "S5 Corporate",
    "S6_supranational":    "S6 Supranational",
}

ARCHETYPE_COLORS = {
    "cex_only":          WONG["blue"],
    "null_event":        WONG["black"],
    "frontend_only":     WONG["sky"],
    "multi_layer":       WONG["orange"],
    "asset_only":        WONG["green"],
    "other_single_layer": WONG["pink"],
}
ARCHETYPE_LABELS = {
    "cex_only":          "CEX-only (184)",
    "null_event":        "Null event (107)",
    "frontend_only":     "Frontend-only (46)",
    "multi_layer":       "Multi-layer (29)",
    "asset_only":        "Asset-only (21)",
    "other_single_layer": "Other (11)",
}

# IEEE single-column width in inches
COL_W = 3.4
COL_H = 2.6   # taller figures where needed

plt.rcParams.update({
    "font.size": 7,
    "axes.titlesize": 8,
    "axes.labelsize": 7,
    "xtick.labelsize": 6.5,
    "ytick.labelsize": 6.5,
    "legend.fontsize": 6,
    "lines.linewidth": 1.0,
    "patch.linewidth": 0.5,
    "pdf.fonttype": 42,   # embed fonts as Type 42 (TrueType) — required by IEEE
    "ps.fonttype": 42,
})

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
with open(ARCHETYPES_FILE) as fh:
    archetypes_raw = json.load(fh)

# Only admitted events (all rows in event_archetypes.json are admitted; confirm)
archetypes = archetypes_raw   # list of dicts

with open(OBSERV_FILE) as fh:
    observ_raw = json.load(fh)

# Build observability dict keyed by layer
observ = {row["layer"]: row for row in observ_raw}

# Sensitivity CSV (small; parse manually to avoid pandas dependency)
sensitivity = {}
with open(SENSITIVITY_FILE) as fh:
    header = fh.readline().strip().split(",")
    for line in fh:
        parts = line.strip().split(",")
        row = dict(zip(header, parts))
        layer = row["layer"]
        def _float(v):
            try:
                return float(v)
            except (ValueError, TypeError):
                return None
        sensitivity[layer] = {
            "strict":     _float(row.get("strict_rate")),
            "current":    _float(row.get("current_rate")),
            "permissive": _float(row.get("permissive_rate")),
            "note":       row.get("sensitivity", ""),
        }

# Load admitted event YAML for temporal + jurisdiction data
def load_admitted_events():
    events = []
    for f in sorted(glob.glob(str(EVENTS_DIR / "*.yaml"))):
        with open(f) as fh:
            d = yaml.safe_load(fh)
        if d.get("status") == "admitted":
            events.append(d)
    return events

admitted = load_admitted_events()
n_admitted = len(admitted)
assert n_admitted == 398, (
    f"Expected 398 admitted events, got {n_admitted}. "
    "Run `make derived` to refresh derived files."
)

# ---------------------------------------------------------------------------
# Fig 1 — HERO (page-1 concept figure): trigger fan-out grid for the
# 2022-08-08 OFAC Tornado Cash designation. One trigger, six layers, three-state
# coverage coloring. Shows the unit of analysis (a single event) and makes the
# "observability gap != zero" rule visceral before any aggregate number appears.
# Data: events/tornado-cash-ofac-2022.yaml (coverage[] + observations[]).
# Honesty note: in THIS event asset_onchain is measured + observed_change
# (direct, Circle on-chain tx); the corpus-wide asset rate retraction is an
# AGGREGATE property and is stated in the caption, not drawn on this cell.
# ---------------------------------------------------------------------------
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

# (layer_key, label, coverage_state, outcome, annotation)  — verbatim from event
FANOUT = [
    ("l0_network",   "L0 network",     "gap",      "none",
     "OONI: 0 volunteer probes in window → coverage gap.\n“---” is undefined, not 0% censored."),
    ("l1_consensus", "L1 consensus",   "partial",  "change",
     "Censoring-relay share 10.8% → 41.1% (post-Merge\nsubset, +39 d).  partial · plausible"),
    ("l3_rpc",       "L3 RPC",         "partial",  "change",
     "Flashbots rpc-endpoint OFAC filter committed +2 h 50 m\n(primary-source bookend).  partial · direct"),
    ("l4_frontend",  "L4 frontend",    "measured", "change",
     "tornado.cash UI / GitHub offline ≈ +22 h.\nmeasured · plausible"),
    ("asset_onchain","Asset on-chain", "measured", "change",
     "Circle USDC blacklists pool address +5 h 53 m\n(on-chain tx).  measured · direct †"),
    ("offramp_cex",  "Off-ramp CEX",   "partial",  "change",
     "dYdX flags accounts, close-only mode +34 h.\npartial · direct"),
]

COVERAGE_FILL = {
    "measured": WONG["green"],
    "partial":  WONG["yellow"],
    "gap":      "white",
}

fig1, ax1 = plt.subplots(figsize=(7.0, 2.75))
fig1.subplots_adjust(left=0.005, right=0.995, top=0.99, bottom=0.005)
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax1.axis("off")

n = len(FANOUT)
top, bot = 0.86, 0.16
ys = [top - (i + 0.5) * (top - bot) / n for i in range(n)]

# Title
ax1.text(0.5, 0.965,
         "One OFAC trigger, six observability fates — Tornado Cash, 2022-08-08",
         ha="center", va="top", fontsize=8.5, fontweight="bold")

# Trigger node (far left)
trig_cx, trig_y = 0.075, 0.5
ax1.add_patch(FancyBboxPatch((0.01, trig_y - 0.17), 0.13, 0.34,
             boxstyle="round,pad=0.004,rounding_size=0.02",
             facecolor=WONG["black"], edgecolor="none", zorder=3))
ax1.text(trig_cx, trig_y,
         "OFAC SDN\ndesignation\n—\nTornado Cash\n2022-08-08\n13:30 UTC",
         ha="center", va="center", color="white", fontsize=6.0,
         zorder=4, linespacing=1.25)

name_x = 0.295
cell_x0, cell_x1 = 0.305, 0.45
ann_x = 0.475
row = (top - bot) / n

for (key, label, cov, outcome, ann), y in zip(FANOUT, ys):
    # fan arrow trigger -> cell
    ax1.add_patch(FancyArrowPatch((0.145, trig_y), (cell_x0 - 0.004, y),
                 arrowstyle="-|>", mutation_scale=7, color="#AAAAAA",
                 lw=0.7, zorder=1))
    # layer name (right-aligned, left of the cell)
    ax1.text(name_x, y, label, ha="right", va="center",
             fontsize=6.8, fontweight="bold")
    # coverage cell
    hatch = "////" if cov == "gap" else None
    ax1.add_patch(Rectangle((cell_x0, y - row * 0.34), cell_x1 - cell_x0, row * 0.68,
                 facecolor=COVERAGE_FILL[cov], edgecolor=WONG["black"],
                 linewidth=0.8, linestyle=("--" if cov == "gap" else "-"),
                 hatch=hatch, zorder=2))
    # outcome glyph inside cell
    cx = (cell_x0 + cell_x1) / 2
    if outcome == "change":
        ax1.text(cx, y, "▲ reaction", ha="center", va="center",
                 fontsize=6.0, color=WONG["black"], zorder=3, fontweight="bold")
    else:
        ax1.text(cx, y, "— no obs.", ha="center", va="center",
                 fontsize=6.0, color="#444444", zorder=4, style="italic",
                 bbox=dict(boxstyle="square,pad=0.15", facecolor="white",
                           edgecolor="none"))
    # annotation (right)
    ax1.text(ann_x, y, ann, ha="left", va="center",
             fontsize=5.6, linespacing=1.12, color="#222222")

# Coverage-state legend (bottom)
leg_y = 0.05
lx = 0.305
for ck, lab in [("measured", "measured"),
                ("partial", "partially measured"),
                ("gap", "observability gap  (“---”, never 0%)")]:
    ax1.add_patch(Rectangle((lx, leg_y), 0.016, 0.028,
                 facecolor=COVERAGE_FILL[ck], edgecolor=WONG["black"],
                 linewidth=0.6, hatch=("////" if ck == "gap" else None)))
    ax1.text(lx + 0.022, leg_y + 0.014, lab, ha="left", va="center", fontsize=5.8)
    lx += 0.165 if ck == "measured" else 0.20

fig1.savefig(FIGS_DIR / "fig1_tornado_fanout.pdf", bbox_inches="tight", dpi=300)
plt.close(fig1)
print("Wrote fig1_tornado_fanout.pdf")

# ---------------------------------------------------------------------------
# Fig 2 — Corpus composition: archetype × stratum
# Two stacked horizontal bars side-by-side (archetypes left, strata right)
# ---------------------------------------------------------------------------

ARCHETYPE_ORDER = [
    "cex_only", "null_event", "frontend_only",
    "multi_layer", "asset_only", "other_single_layer",
]
STRATUM_ORDER = [
    "S1_ofac_sdn", "S2_ofac_removal", "S3_doj_sec_cftc_fiod",
    "S4_nation_state", "S5_corporate", "S6_supranational",
]

arch_counts = {a: 0 for a in ARCHETYPE_ORDER}
strat_counts = {s: 0 for s in STRATUM_ORDER}

for ev in archetypes:
    arch = ev.get("derived_archetype")
    if arch in arch_counts:
        arch_counts[arch] += 1
strat_meta = {}  # stratum -> count from event YAML (research_stratum field)
for ev in admitted:
    s = ev.get("research_stratum")
    if s in strat_counts:
        strat_counts[s] += 1

# Canonical check against paper macros (archetype counts, admitted corpus only).
# Stratum canonical values are admitted-only from table3 cross-tab, NOT the
# all-registry counts in paper_numbers.tex / dataset.meta.json (those = 420).
CANONICAL_ARCH = {
    "cex_only": 184, "null_event": 107, "frontend_only": 46,
    "multi_layer": 29, "asset_only": 21, "other_single_layer": 11,
}
# Admitted-only stratum counts (from table3_archetype_stratum.md totals):
CANONICAL_STRAT_ADMITTED = {
    "S1_ofac_sdn": 60, "S2_ofac_removal": 1, "S3_doj_sec_cftc_fiod": 84,
    "S4_nation_state": 119, "S5_corporate": 103, "S6_supranational": 31,
}
for k, v in CANONICAL_ARCH.items():
    if arch_counts.get(k) != v:
        print(f"WARNING: archetype {k}: got {arch_counts.get(k)}, expected {v}")
for k, v in CANONICAL_STRAT_ADMITTED.items():
    if strat_counts.get(k) != v:
        print(f"WARNING: stratum {k}: got {strat_counts.get(k)}, expected {v}")

fig2, axes = plt.subplots(1, 2, figsize=(COL_W, 2.7))
fig2.subplots_adjust(wspace=1.15, left=0.26, right=0.97, top=0.86, bottom=0.13)

def _hbar(ax, counts, color_map, label_map, title):
    """Horizontal bar chart of categorical counts, sorted descending."""
    keys = sorted((k for k in counts if counts.get(k, 0) > 0),
                  key=lambda k: -counts[k])
    vals = [counts[k] for k in keys]
    y = list(range(len(keys)))
    ax.barh(y, vals, color=[color_map[k] for k in keys],
            height=0.72, edgecolor="white", linewidth=0.3)
    ax.set_yticks(y)
    ax.set_yticklabels([label_map[k] for k in keys], fontsize=6)
    ax.invert_yaxis()  # largest bar at the top
    ax.set_title(title, fontsize=7, pad=4)
    ax.tick_params(axis="x", labelsize=5.5, length=2)
    ax.set_xlabel("events", fontsize=6, labelpad=1)
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    mx = max(vals)
    for yi, v in zip(y, vals):
        ax.text(v + mx * 0.02, yi, str(v), va="center", ha="left", fontsize=5.6)
    ax.set_xlim(0, mx * 1.16)

_hbar(axes[0], arch_counts, ARCHETYPE_COLORS, ARCHETYPE_LABELS,
      f"(a) Archetype  (n={n_admitted})")
_hbar(axes[1], strat_counts, STRATUM_COLORS, STRATUM_LABELS,
      f"(b) Stratum  (n={n_admitted})")

fig2.savefig(FIGS_DIR / "fig2_corpus_composition.pdf", bbox_inches="tight", dpi=300)
plt.close(fig2)
print("Wrote fig2_corpus_composition.pdf")

# ---------------------------------------------------------------------------
# Fig 3 — Visibility gradient: per-layer coverage-matched rate
# Horizontal dot+bar chart; L0 and asset shown as honest gap/retracted NOT zero.
# ---------------------------------------------------------------------------

# Layer display order: protocol base → application chokepoints
LAYER_ORDER = ["l0_network", "l1_consensus", "l3_rpc", "l4_frontend",
               "asset_onchain", "offramp_cex"]
LAYER_LABELS = {
    "l0_network":   "L0 network",
    "l1_consensus": "L1 consensus",
    "l3_rpc":       "L3 RPC",
    "l4_frontend":  "L4 frontend",
    "asset_onchain": "Asset on-chain",
    "offramp_cex":  "Off-ramp CEX",
}

# Current (measured+partial) rates from observability JSON
# L0: no measured denominator → gap; asset: retracted
layer_rate = {
    "l0_network":   None,           # zero measured denominator → observability gap
    "l1_consensus": 10/16,          # 10/16
    "l3_rpc":       6/7,            # 6/7
    "l4_frontend":  70/78,          # 70/78
    "asset_onchain": None,          # retracted (circular)
    "offramp_cex":  208/308,        # 208/308
}
layer_denom = {
    "l0_network":   (0, 5, 19),     # (measured, partial, not_measured)
    "l1_consensus": (8, 8, 2),
    "l3_rpc":       (1, 6, 6),
    "l4_frontend":  (57, 21, 46),
    "asset_onchain": (23, 4, 22),
    "offramp_cex":  (257, 51, 21),
}
layer_frac_label = {
    "l0_network":   "—",
    "l1_consensus": "10/16",
    "l3_rpc":       "6/7",
    "l4_frontend":  "70/78",
    "asset_onchain": "retracted",
    "offramp_cex":  "208/308",
}

# Admission-sensitivity ablation (strict / current / permissive)
# From derived/admission_sensitivity.csv and paper_numbers.tex
ablation = {
    "l0_network":   (None, None, 1.00),     # only partial; permissive only
    "l1_consensus": (0.00, 0.25, 0.625),
    "l3_rpc":       (1.00, 1.00, 0.8571),
    "l4_frontend":  (0.5965, 0.9123, 0.8974),
    "asset_onchain": (None, None, None),    # retracted
    "offramp_cex":  (0.4669, 0.6498, 0.6753),
}

fig3, ax3 = plt.subplots(figsize=(COL_W, 2.8))
fig3.subplots_adjust(left=0.23, right=0.82, top=0.92, bottom=0.12)

y_pos = list(range(len(LAYER_ORDER)))[::-1]  # top-to-bottom display order

for i, layer in enumerate(LAYER_ORDER):
    y = y_pos[i]
    rate = layer_rate[layer]
    strict, current, permissive = ablation[layer]
    label = LAYER_LABELS[layer]
    frac_str = layer_frac_label[layer]
    meas, part, not_meas = layer_denom[layer]

    if rate is None:
        if layer == "l0_network":
            # Draw hatched bar across full width to signal observability gap
            ax3.barh(y, 1.0, height=0.5, left=0.0,
                     color="none", edgecolor=WONG["black"],
                     linewidth=0.7, linestyle="--", hatch="///", zorder=2)
            ax3.text(1.02, y, "— (observability\ngap, 0 measured)",
                     va="center", ha="left", fontsize=5.5, color=WONG["black"])
        else:  # asset_onchain
            ax3.barh(y, 1.0, height=0.5, left=0.0,
                     color="none", edgecolor=WONG["red"],
                     linewidth=0.7, linestyle=":", hatch="xxx", zorder=2)
            ax3.text(1.02, y, "retracted\n(circular)",
                     va="center", ha="left", fontsize=5.5, color=WONG["red"])
        continue

    # Draw ablation range as a thin horizontal line (strict → permissive)
    vals = [v for v in [strict, permissive] if v is not None]
    if len(vals) == 2:
        ax3.plot(vals, [y, y], color=WONG["black"], linewidth=1.8,
                 alpha=0.3, solid_capstyle="round", zorder=1)

    # Strict dot (open circle)
    if strict is not None:
        ax3.plot(strict, y, "o", color=WONG["black"],
                 markersize=4, markerfacecolor="white",
                 markeredgewidth=0.8, zorder=3)
    # Permissive dot (open square)
    if permissive is not None:
        ax3.plot(permissive, y, "s", color=WONG["black"],
                 markersize=4, markerfacecolor="white",
                 markeredgewidth=0.8, zorder=3)
    # Current (filled circle) — the main reported rate
    ax3.plot(current, y, "o", color=WONG["blue"],
             markersize=6, markeredgewidth=0.6,
             markeredgecolor="white", zorder=4)

    # Fraction annotation to the right
    ax3.text(1.02, y, frac_str,
             va="center", ha="left", fontsize=5.5, color=WONG["blue"])

# Axes formatting
ax3.set_xlim(-0.02, 1.0)
ax3.set_ylim(-0.6, len(LAYER_ORDER) - 0.4)
ax3.set_yticks(y_pos)
ax3.set_yticklabels([LAYER_LABELS[l] for l in LAYER_ORDER])
ax3.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
ax3.set_xticklabels(["0", ".25", ".50", ".75", "1.0"])
ax3.set_xlabel("Coverage-matched changed/denominator rate")
ax3.set_title("Visibility gradient: per-layer reaction rate", pad=4)
ax3.spines["top"].set_visible(False)
ax3.spines["right"].set_visible(False)

# Legend for marker types
h_current = plt.Line2D([0], [0], marker="o", color="w",
                        markerfacecolor=WONG["blue"], markersize=6,
                        label="Current (measured+partial)")
h_strict  = plt.Line2D([0], [0], marker="o", color="w",
                        markerfacecolor="white",
                        markeredgecolor=WONG["black"], markeredgewidth=0.8,
                        markersize=4, label="Strict (measured only)")
h_perm    = plt.Line2D([0], [0], marker="s", color="w",
                        markerfacecolor="white",
                        markeredgecolor=WONG["black"], markeredgewidth=0.8,
                        markersize=4, label="Permissive")
ax3.legend(handles=[h_current, h_strict, h_perm],
           loc="lower right", frameon=True, framealpha=0.9,
           edgecolor="none", fontsize=5.5)

fig3.savefig(FIGS_DIR / "fig3_visibility_gradient.pdf", bbox_inches="tight", dpi=300)
plt.close(fig3)
print("Wrote fig3_visibility_gradient.pdf")

# ---------------------------------------------------------------------------
# Fig 4 — Collection density: admitted events per year stacked by stratum
# Clearly labelled as COLLECTION DENSITY not phenomenon density.
# ---------------------------------------------------------------------------

# Build year × stratum matrix from event YAML files (admitted only)
years_all = list(range(2007, 2027))
year_strat = {y: {s: 0 for s in STRATUM_ORDER} for y in years_all}
for ev in admitted:
    ts = ev.get("trigger", {}).get("timestamp", "")
    if not ts:
        continue
    year = int(str(ts)[:4])
    s = ev.get("research_stratum", "")
    if year in year_strat and s in STRATUM_ORDER:
        year_strat[year][s] += 1

years = [y for y in years_all if sum(year_strat[y].values()) > 0]
bottoms = np.zeros(len(years))
x = np.arange(len(years))

fig4, ax4 = plt.subplots(figsize=(COL_W, 2.7))
fig4.subplots_adjust(left=0.12, right=0.99, top=0.90, bottom=0.30)

for stratum in STRATUM_ORDER:
    vals = np.array([year_strat[y][stratum] for y in years], dtype=float)
    ax4.bar(x, vals, bottom=bottoms, color=STRATUM_COLORS[stratum],
            width=0.78, label=STRATUM_LABELS[stratum], edgecolor="none")
    bottoms += vals

ax4.set_xticks(x)
ax4.set_xticklabels([str(y)[2:] for y in years], rotation=45, ha="right")
ax4.set_xlabel("Year (trigger date)")
ax4.set_ylabel("Events admitted")
ax4.set_title("Collection density by year and stratum", pad=6)
ax4.spines["top"].set_visible(False)
ax4.spines["right"].set_visible(False)

# Caveat annotation — placed INSIDE the plot's empty upper-left (early years are
# sparse) so it never overlaps the title.
ax4.annotate(
    "Collection density (frame coverage),\nnot phenomenon frequency.",
    xy=(0.02, 0.97), xycoords="axes fraction",
    fontsize=5, ha="left", va="top",
    color="#555555", style="italic",
)

legend_patches = [mpatches.Patch(color=STRATUM_COLORS[s], label=STRATUM_LABELS[s])
                  for s in STRATUM_ORDER]
ax4.legend(handles=legend_patches, loc="upper left",
           bbox_to_anchor=(0.0, -0.44), ncol=2,
           frameon=False, fontsize=5, handlelength=1.0, handletextpad=0.4,
           columnspacing=0.8)

fig4.savefig(FIGS_DIR / "fig4_collection_density.pdf", bbox_inches="tight", dpi=300)
plt.close(fig4)
print("Wrote fig4_collection_density.pdf")

# ---------------------------------------------------------------------------
# Fig 5 — Jurisdiction concentration (top-N bar chart)
# US-dominant, framed as evidence-frame property not phenomenon claim.
# ---------------------------------------------------------------------------

# Count jurisdictions from admitted event YAML (multi-jurisdiction events
# count once per jurisdiction code — inclusive)
from collections import Counter

jur_counter = Counter()
for ev in admitted:
    jurs = ev.get("jurisdiction", [])
    if isinstance(jurs, str):
        jurs = [jurs]
    for j in jurs:
        if j:
            jur_counter[j] += 1

# Top-15 jurisdictions by count
TOP_N = 15
top_jurs = jur_counter.most_common(TOP_N)
jur_labels, jur_vals = zip(*top_jurs)

# Colour: US in red, corporate_global in grey, rest in blue
bar_colors = []
for jl in jur_labels:
    if jl == "US":
        bar_colors.append(WONG["red"])
    elif jl == "corporate_global":
        bar_colors.append(WONG["black"])
    else:
        bar_colors.append(WONG["sky"])

fig5, ax5 = plt.subplots(figsize=(COL_W, 2.6))
fig5.subplots_adjust(left=0.16, right=0.98, top=0.88, bottom=0.28)

y_pos5 = np.arange(len(jur_labels))
bars = ax5.barh(y_pos5[::-1], jur_vals, color=bar_colors,
                height=0.65, edgecolor="none")

ax5.set_yticks(y_pos5)
ax5.set_yticklabels(list(jur_labels)[::-1])
ax5.set_xlabel("Events (inclusive count)")
ax5.set_title("Jurisdiction distribution — top 15", pad=3)
ax5.spines["top"].set_visible(False)
ax5.spines["right"].set_visible(False)

# Annotate US bar with share
us_count = jur_counter["US"]
ax5.annotate(
    f"US: {us_count}/365 ({us_count/365*100:.0f}%)\nsampling-frame property,\nnot phenomenon rate",
    xy=(us_count, len(jur_labels) - 1),
    xytext=(us_count + 8, len(jur_labels) - 1),
    fontsize=5, color=WONG["red"], va="center",
    arrowprops=dict(arrowstyle="-", color=WONG["red"], lw=0.5),
)

# Legend
h_us   = mpatches.Patch(color=WONG["red"],   label=f"US ({us_count})")
h_corp = mpatches.Patch(color=WONG["black"], label="corporate_global")
h_rest = mpatches.Patch(color=WONG["sky"],   label="Other jurisdictions")
ax5.legend(handles=[h_us, h_corp, h_rest],
           loc="lower right", frameon=True, framealpha=0.9,
           edgecolor="none", fontsize=5.5, ncol=1)

# Caveat below plot
fig5.text(0.5, 0.01,
          "Inclusive counts: multi-jurisdiction events appear in each code. "
          "Concentration is an evidence-frame\nproperty (English-language "
          "public archives, high OFAC/DOJ volume 2022-2025).",
          ha="center", va="bottom", fontsize=4.8, color="#555555",
          style="italic", wrap=True)

fig5.savefig(FIGS_DIR / "fig5_jurisdiction_concentration.pdf",
             bbox_inches="tight", dpi=300)
plt.close(fig5)
print("Wrote fig5_jurisdiction_concentration.pdf")

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
print()
print(f"All figures written to: {FIGS_DIR}")
print("  fig2_corpus_composition.pdf   — archetype + stratum stacked bars")
print("  fig3_visibility_gradient.pdf  — per-layer coverage-matched rate (central finding)")
print("  fig4_collection_density.pdf   — collection density by year (NOT phenomenon density)")
print("  fig5_jurisdiction_concentration.pdf — jurisdiction top-15 (evidence-frame framing)")
