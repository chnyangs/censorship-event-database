"""Generate manuscript vector-PDF figures from the current corpus artifacts.

Run `make paper-figures`, or `python scripts/build_paper_figures.py --out DIR`
after `make derived`. Install requirements-analysis.txt. The default output is
figs/ in the sibling manuscript, or analysis/manuscript/figs in a standalone
clone. These figures describe existing coding; they do not validate its truth.
"""

import argparse
import csv
import json
import textwrap
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.text import Text
import numpy as np
import yaml

from build_paper_macros import default_paper_dir

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO = Path(__file__).resolve().parent.parent
DEFAULT_OUT = default_paper_dir() / "figs"

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
    "cex_only":          "CEX-only",
    "null_event":        "No recorded change",
    "frontend_only":     "Frontend-only",
    "multi_layer":       "Multi-layer",
    "asset_only":        "Asset-only",
    "other_single_layer": "Other",
}

# ACM sigconf widths in inches. The TeX values are 506.295pt and 241.14749pt;
# divide by 72.27 TeX points per inch. Figures are included at exactly these
# widths in the manuscript.
TEXT_W = 506.295 / 72.27
COL_W = 3.4
COL_H = 2.6   # taller figures where needed
PAPER_COLUMN_W = 241.14749 / 72.27
MIN_EMBEDDED_FONT_PT = 9.0
TIGHT_PAD_IN = 0.1

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


def embedded_font_report(fig, inclusion_width_inches: float,
                         pad_inches: float = TIGHT_PAD_IN) -> dict:
    """Estimate text sizes after a tight PDF is scaled to its manuscript width.

    Matplotlib font sizes are physical points. get_tightbbox reports the
    exported content extent in inches; tight savefig adds pad_inches on both
    sides. Every text element receives the same scale when LaTeX fits the PDF
    to inclusion_width_inches.
    """
    fig.canvas.draw()
    bbox = fig.get_tightbbox(fig.canvas.get_renderer())
    export_width_inches = bbox.width + 2 * pad_inches
    text_sizes = [
        artist.get_fontsize()
        for artist in fig.findobj(match=lambda item: isinstance(item, Text))
        if artist.get_visible() and artist.get_text().strip()
    ]
    if not text_sizes:
        raise ValueError("Target paper figure has no visible text")
    scale = inclusion_width_inches / export_width_inches
    return {
        "source_min_font_pt": min(text_sizes),
        "export_width_inches": export_width_inches,
        "inclusion_width_inches": inclusion_width_inches,
        "latex_scale": scale,
        "embedded_min_font_pt": min(text_sizes) * scale,
        "visible_text_elements": len(text_sizes),
    }


def save_legible_figure(fig, path: Path, inclusion_width_inches: float) -> dict:
    """Save a target figure only when every visible label remains at least 9pt."""
    report = embedded_font_report(fig, inclusion_width_inches)
    if report["embedded_min_font_pt"] + 1e-9 < MIN_EMBEDDED_FONT_PT:
        raise ValueError(
            f"{path.name}: minimum embedded font "
            f"{report['embedded_min_font_pt']:.2f}pt is below "
            f"{MIN_EMBEDDED_FONT_PT:.1f}pt"
        )
    fig.savefig(path, bbox_inches="tight", pad_inches=TIGHT_PAD_IN, dpi=300)
    return report

LAYER_ORDER = ["l0_network", "l1_consensus", "l3_rpc", "l4_frontend",
               "asset_onchain", "offramp_cex"]
LAYER_LABELS = {
    "l0_network": "L0 network", "l1_consensus": "L1 consensus",
    "l3_rpc": "L3 RPC", "l4_frontend": "L4 frontend",
    "asset_onchain": "Asset on-chain", "offramp_cex": "Off-ramp CEX",
}


def load_inputs(repo: Path = REPO) -> dict:
    """Load one snapshot, refusing mismatched derived event membership."""
    admitted = []
    for path in sorted((repo / "events").glob("*.yaml")):
        event = yaml.safe_load(path.read_text())
        if isinstance(event, dict) and event.get("status") == "admitted":
            admitted.append(event)
    if not admitted:
        raise ValueError("No admitted events; cannot render corpus figures")
    archetypes = json.loads((repo / "derived/event_archetypes.json").read_text())
    admitted_ids = {event["id"] for event in admitted}
    if ({row["event_id"] for row in archetypes} != admitted_ids
            or len(archetypes) != len(admitted)):
        raise ValueError("Archetype membership differs from admitted YAML; run make derived")
    observ = {row["layer"]: row for row in json.loads(
        (repo / "derived/layer_observability.json").read_text())}
    if any(row["total_events"] != len(admitted) for row in observ.values()):
        raise ValueError("Observability totals differ from admitted YAML; run make derived")
    sensitivity = {}
    with (repo / "derived/admission_sensitivity.csv").open() as fh:
        for row in csv.DictReader(fh):
            sensitivity[row["layer"]] = {
                rubric: {
                    "rate": float(row[f"{rubric}_rate"]) if row[f"{rubric}_rate"] else None,
                    "num": int(row[f"{rubric}_num"]),
                    "den": int(row[f"{rubric}_den"]),
                } for rubric in ("strict", "current", "permissive")
            }
    for layer in LAYER_ORDER:
        obs = observ[layer]
        if sensitivity[layer]["permissive"]["den"] != (
                obs["measured_count"] + obs["partially_measured_count"]):
            raise ValueError(f"{layer}: sensitivity denominator is stale; run make derived")
    return {"admitted": admitted, "archetypes": archetypes,
            "observ": observ, "sensitivity": sensitivity}


def layer_display(layer: str, sensitivity: dict) -> dict:
    """The blue marker and annotation use the SAME permissive rubric.

    L0 and asset rates remain suppressed regardless of coded numerators.
    Empty CSV rates are suppression signals and must not be recomputed.
    """
    row = sensitivity[layer]
    suppressed = layer in {"l0_network", "asset_onchain"}
    rates = {name: None if suppressed else item["rate"]
             for name, item in row.items()}
    broad = row["permissive"]
    fraction = f"{broad['num']}/{broad['den']}" if rates["permissive"] is not None else "—"
    return {"rates": rates, "fraction": fraction}


def jurisdiction_summary(admitted: list[dict]) -> tuple[Counter, str]:
    counts = Counter()
    for event in admitted:
        jurisdictions = event.get("jurisdiction") or []
        if isinstance(jurisdictions, str):
            jurisdictions = [jurisdictions]
        counts.update(set(jurisdictions))
    total = len(admitted)
    us = counts["US"]
    return counts, f"US: {us}/{total} ({100 * us / total:.1f}%)"


def fanout_rows(event: dict) -> list[tuple]:
    coverage = {row["layer"]: row["status"] for row in event.get("coverage", [])}
    rows = []
    for layer in LAYER_ORDER:
        observations = [row for row in event.get("observations", [])
                        if row.get("layer") == layer]
        changes = [row for row in observations if row.get("observation_kind") == "observed_change"]
        row = (changes or observations or [None])[0]
        if row is None:
            annotation = "No observation recorded; absence of a record does not establish no action."
        else:
            annotation = str(row.get("event", "observation")).replace("_", " ")
            details = [str(row.get("attribution", "unspecified attribution")),
                       str(row.get("precision", "unspecified precision"))]
            if row.get("delta_hours") is not None:
                details.append(f"coded delta {row['delta_hours']:g} h")
            annotation += " (" + "; ".join(details) + ")"
        status = coverage.get(layer, "not_measured")
        rows.append((layer, LAYER_LABELS[layer], status,
                     "change" if changes else "none",
                     annotation))
    return rows


def render(data: dict, output: Path) -> None:
    admitted = data["admitted"]
    archetypes = data["archetypes"]
    observ = data["observ"]
    sensitivity = data["sensitivity"]
    n_admitted = len(admitted)
    FIGS_DIR = output
    FIGS_DIR.mkdir(parents=True, exist_ok=True)
    font_legibility = {}

    # ---------------------------------------------------------------------------
    # Fig 1: the current Tornado Cash coding, including attribution and
    # precision. This illustrates the record structure; it is not a validated
    # behavioral timeline. Asset-rate suppression concerns the aggregate.
    # ---------------------------------------------------------------------------
    from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

    hero = next(event for event in admitted if event["id"] == "tornado-cash-ofac-2022")
    FANOUT = fanout_rows(hero)
    COVERAGE_FILL = {
        "measured": WONG["green"], "partially_measured": WONG["yellow"],
        "not_measured": "white", "not_applicable": "#DDDDDD",
    }

    fig1, ax1 = plt.subplots(figsize=(7.0, 3.8))
    fig1.subplots_adjust(left=0.005, right=0.995, top=0.99, bottom=0.005)
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis("off")

    n = len(FANOUT)
    top, bot = 0.86, 0.16
    ys = [top - (i + 0.5) * (top - bot) / n for i in range(n)]

    # Title
    ax1.text(0.5, 0.965,
             f"One trigger, six coded layers — {hero['id']}",
             ha="center", va="top", fontsize=11, fontweight="bold")

    # Trigger node (far left)
    trig_cx, trig_y = 0.065, 0.5
    ax1.add_patch(FancyBboxPatch((0.01, trig_y - 0.17), 0.11, 0.34,
                 boxstyle="round,pad=0.004,rounding_size=0.02",
                 facecolor=WONG["black"], edgecolor="none", zorder=3))
    ax1.text(trig_cx, trig_y,
             "\n".join(textwrap.wrap(hero["trigger"]["type"].replace("_", " "), width=16))
             + "\n—\n" + str(hero["trigger"]["timestamp"])[:10],
             ha="center", va="center", color="white", fontsize=10.5,
             zorder=4, linespacing=1.25)

    name_x = 0.30
    cell_x0, cell_x1 = 0.32, 0.50
    ann_x = 0.525
    row = (top - bot) / n

    for (key, label, cov, outcome, ann), y in zip(FANOUT, ys):
        # Fan connector. The endpoint cell supplies direction without a glyph
        # that could collide with the adjacent layer label.
        ax1.add_patch(FancyArrowPatch((0.125, trig_y), (cell_x0, y),
                     arrowstyle="-", color="#AAAAAA",
                     lw=0.7, zorder=1))
        # layer name (right-aligned, left of the cell)
        ax1.text(name_x, y, label, ha="right", va="center",
                 fontsize=10.5, fontweight="bold", zorder=3,
                 bbox=dict(boxstyle="square,pad=0.08", facecolor="white",
                           edgecolor="none"))
        # coverage cell
        hatch = "////" if cov == "not_measured" else None
        ax1.add_patch(Rectangle((cell_x0, y - row * 0.34), cell_x1 - cell_x0, row * 0.68,
                     facecolor=COVERAGE_FILL[cov], edgecolor=WONG["black"],
                     linewidth=0.8, linestyle=("--" if cov == "not_measured" else "-"),
                     hatch=hatch, zorder=2))
        # outcome glyph inside cell
        cx = (cell_x0 + cell_x1) / 2
        if outcome == "change":
            ax1.text(cx, y, "coded change", ha="center", va="center",
                     fontsize=10.5, color=WONG["black"], zorder=3, fontweight="bold")
        else:
            ax1.text(cx, y, "— no obs.", ha="center", va="center",
                     fontsize=10.5, color="#444444", zorder=4, style="italic",
                     bbox=dict(boxstyle="square,pad=0.15", facecolor="white",
                               edgecolor="none"))
        # annotation (right)
        ax1.text(ann_x, y, textwrap.fill(ann, width=48), ha="left", va="center",
                 fontsize=10.5, linespacing=1.12, color="#222222")

    # Coverage-state legend (bottom)
    leg_y = 0.05
    lx = 0.32
    for ck, lab in [("measured", "measured"),
                    ("partially_measured", "partially measured"),
                    ("not_measured", "unmeasured / gap")]:
        ax1.add_patch(Rectangle((lx, leg_y), 0.016, 0.028,
                     facecolor=COVERAGE_FILL[ck], edgecolor=WONG["black"],
                     linewidth=0.6, hatch=("////" if ck == "not_measured" else None)))
        ax1.text(lx + 0.022, leg_y + 0.014, lab, ha="left", va="center", fontsize=10.5)
        lx += 0.18 if ck == "measured" else 0.24

    font_legibility["fig1_tornado_fanout.pdf"] = save_legible_figure(
        fig1, FIGS_DIR / "fig1_tornado_fanout.pdf", TEXT_W
    )
    plt.close(fig1)
    print("Wrote fig1_tornado_fanout.pdf")

    # ---------------------------------------------------------------------------
    # Fig 2 — Corpus composition: archetype × stratum. Panels are vertical so
    # full category labels remain legible at one-column inclusion width.
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
    for ev in admitted:
        s = ev.get("research_stratum")
        if s in strat_counts:
            strat_counts[s] += 1
    if sum(arch_counts.values()) != n_admitted or sum(strat_counts.values()) != n_admitted:
        raise ValueError("Unrecognized archetype or stratum; update figure categories before publishing")

    fig2, axes = plt.subplots(2, 1, figsize=(COL_W, 4.6))
    fig2.subplots_adjust(hspace=0.62, left=0.42, right=0.95, top=0.95, bottom=0.10)

    def _hbar(ax, counts, color_map, label_map, title):
        """Horizontal bar chart of categorical counts, sorted descending."""
        keys = sorted((k for k in counts if counts.get(k, 0) > 0),
                      key=lambda k: -counts[k])
        vals = [counts[k] for k in keys]
        y = list(range(len(keys)))
        ax.barh(y, vals, color=[color_map[k] for k in keys],
                height=0.72, edgecolor="white", linewidth=0.3)
        ax.set_yticks(y)
        ax.set_yticklabels([label_map[k] for k in keys], fontsize=10)
        ax.invert_yaxis()  # largest bar at the top
        ax.set_title(title, fontsize=10.5, pad=5)
        ax.tick_params(axis="x", labelsize=10, length=3)
        ax.set_xlabel("Events", fontsize=10, labelpad=2)
        for sp in ("top", "right", "left"):
            ax.spines[sp].set_visible(False)
        mx = max(vals)
        for yi, v in zip(y, vals):
            ax.text(v + mx * 0.02, yi, str(v), va="center", ha="left", fontsize=10)
        ax.set_xlim(0, mx * 1.16)

    _hbar(axes[0], arch_counts, ARCHETYPE_COLORS, ARCHETYPE_LABELS,
          f"(a) Archetype  (n={n_admitted})")
    _hbar(axes[1], strat_counts, STRATUM_COLORS, STRATUM_LABELS,
          f"(b) Stratum  (n={n_admitted})")

    font_legibility["fig2_corpus_composition.pdf"] = save_legible_figure(
        fig2, FIGS_DIR / "fig2_corpus_composition.pdf", PAPER_COLUMN_W
    )
    plt.close(fig2)
    print("Wrote fig2_corpus_composition.pdf")

    # ---------------------------------------------------------------------------
    # Fig 3 — Visibility gradient: per-layer coverage-matched rate
    # Horizontal dot+bar chart; L0 and asset shown as honest gap/retracted NOT zero.
    # ---------------------------------------------------------------------------

    display = {layer: layer_display(layer, sensitivity) for layer in LAYER_ORDER}

    fig3, ax3 = plt.subplots(figsize=(COL_W, 3.3))
    fig3.subplots_adjust(left=0.23, right=0.82, top=0.92, bottom=0.27)

    y_pos = list(range(len(LAYER_ORDER)))[::-1]  # top-to-bottom display order

    for i, layer in enumerate(LAYER_ORDER):
        y = y_pos[i]
        rates = display[layer]["rates"]
        strict, current, permissive = (rates[name] for name in ("strict", "current", "permissive"))
        rate = permissive
        frac_str = display[layer]["fraction"]
        meas = observ[layer]["measured_count"]

        if rate is None:
            if layer == "l0_network":
                # Draw hatched bar across full width to signal observability gap
                ax3.barh(y, 1.0, height=0.5, left=0.0,
                         color="none", edgecolor=WONG["black"],
                         linewidth=0.7, linestyle="--", hatch="///", zorder=2)
                ax3.text(1.02, y, f"suppressed\n({meas} measured)",
                         va="center", ha="left", fontsize=5.5, color=WONG["black"])
            else:  # retracted asset or another undefined denominator
                ax3.barh(y, 1.0, height=0.5, left=0.0,
                         color="none", edgecolor=WONG["red"],
                         linewidth=0.7, linestyle=":", hatch="xxx", zorder=2)
                ax3.text(1.02, y, "retracted\n(circular)" if layer == "asset_onchain" else "undefined",
                         va="center", ha="left", fontsize=5.5, color=WONG["red"])
            continue

        # The current rate need not lie between strict and permissive.
        vals = [v for v in [strict, current, permissive] if v is not None]
        if len(vals) > 1:
            ax3.plot([min(vals), max(vals)], [y, y], color=WONG["black"], linewidth=1.8,
                     alpha=0.3, solid_capstyle="round", zorder=1)

        # Strict dot (open circle)
        if strict is not None:
            ax3.plot(strict, y, "o", color=WONG["black"],
                     markersize=4, markerfacecolor="white",
                     markeredgewidth=0.8, zorder=3)
        # Current = measured-only, direct + plausible (open square).
        if current is not None:
            ax3.plot(current, y, "s", color=WONG["black"],
                     markersize=4, markerfacecolor="white",
                     markeredgewidth=0.8, zorder=3)
        # Permissive = measured + partial; matches the fraction annotation.
        ax3.plot(permissive, y, "o", color=WONG["blue"],
                 markersize=6, markeredgewidth=0.6,
                 markeredgecolor="white", zorder=4)

        # Fraction annotation to the right
        ax3.text(1.02, y, frac_str,
                 va="center", ha="left", fontsize=5.5, color=WONG["blue"])

    # Axes formatting
    ax3.set_xlim(-0.02, 1.01)
    ax3.set_ylim(-0.6, len(LAYER_ORDER) - 0.4)
    ax3.set_yticks(y_pos)
    ax3.set_yticklabels([LAYER_LABELS[l] for l in LAYER_ORDER])
    ax3.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax3.set_xticklabels(["0", ".25", ".50", ".75", "1.0"])
    ax3.set_xlabel("Coded changes / covered event-layer cells")
    ax3.set_title("Recorded layer-change fractions (provisional)", pad=4)
    ax3.spines["top"].set_visible(False)
    ax3.spines["right"].set_visible(False)

    # Legend for marker types
    h_perm = plt.Line2D([0], [0], marker="o", color="w",
                            markerfacecolor=WONG["blue"], markersize=6,
                            label="Permissive: measured + partial")
    h_strict  = plt.Line2D([0], [0], marker="o", color="w",
                            markerfacecolor="white",
                            markeredgecolor=WONG["black"], markeredgewidth=0.8,
                            markersize=4, label="Strict: measured, direct")
    h_current = plt.Line2D([0], [0], marker="s", color="w",
                            markerfacecolor="white",
                            markeredgecolor=WONG["black"], markeredgewidth=0.8,
                            markersize=4, label="Current: measured, direct + plausible")
    ax3.legend(handles=[h_perm, h_current, h_strict],
               loc="upper center", bbox_to_anchor=(0.5, -0.24),
               frameon=False, fontsize=5.5)

    fig3.savefig(FIGS_DIR / "fig3_visibility_gradient.pdf", bbox_inches="tight", dpi=300)
    plt.close(fig3)
    print("Wrote fig3_visibility_gradient.pdf")

    # ---------------------------------------------------------------------------
    # Fig 4 — Collection density: admitted events per year stacked by stratum
    # Clearly labelled as COLLECTION DENSITY not phenomenon density.
    # ---------------------------------------------------------------------------

    # Build year × stratum matrix from event YAML files (admitted only)
    years_all = sorted({int(str(event["trigger"]["timestamp"])[:4]) for event in admitted})
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
    jur_counter, us_label = jurisdiction_summary(admitted)

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

    fig5, ax5 = plt.subplots(figsize=(COL_W, 4.5))
    fig5.subplots_adjust(left=0.36, right=0.97, top=0.88, bottom=0.25)

    y_pos5 = np.arange(len(jur_labels))
    bars = ax5.barh(y_pos5[::-1], jur_vals, color=bar_colors,
                    height=0.65, edgecolor="none")

    ax5.set_yticks(y_pos5)
    ax5.set_yticklabels(list(jur_labels)[::-1], fontsize=10.3)
    ax5.tick_params(axis="x", labelsize=10.3, length=3)
    ax5.set_xlabel("Events (inclusive count)", fontsize=10.3)
    ax5.set_title(f"Jurisdiction distribution — top {len(top_jurs)}",
                  fontsize=10.8, pad=5)
    ax5.spines["top"].set_visible(False)
    ax5.spines["right"].set_visible(False)

    # Annotate US bar with share
    us_count = jur_counter["US"]
    if "US" in jur_labels:
        us_y = len(jur_labels) - 1 - jur_labels.index("US")
        ax5.annotate(
            us_label + "\nSampling frame;\nnot a phenomenon\nrate.",
            xy=(us_count, us_y), xycoords="data",
            xytext=(0.97, 0.83), textcoords="axes fraction",
            fontsize=10.3, color=WONG["red"], va="top", ha="right",
            arrowprops=dict(arrowstyle="-", color=WONG["red"], lw=0.8),
        )

    # Legend
    h_us   = mpatches.Patch(color=WONG["red"],   label=f"US ({us_count})")
    h_corp = mpatches.Patch(color=WONG["black"], label="corporate_global")
    h_rest = mpatches.Patch(color=WONG["sky"],   label="Other jurisdictions")
    ax5.legend(handles=[h_us, h_corp, h_rest],
               loc="lower right", frameon=True, framealpha=0.9,
               edgecolor="none", fontsize=10.3, ncol=1,
               borderpad=0.35, labelspacing=0.35, handlelength=1.1)

    # Caveat below plot
    fig5.text(0.5, 0.01,
              "Inclusive tags: multi-jurisdiction events\n"
              "appear under every coded jurisdiction.\n"
              "Concentration describes the evidence frame\n"
              "and its public sources.",
              ha="center", va="bottom", fontsize=10.3, color="#555555",
              style="italic", wrap=True)

    font_legibility["fig5_jurisdiction_concentration.pdf"] = save_legible_figure(
        fig5, FIGS_DIR / "fig5_jurisdiction_concentration.pdf", PAPER_COLUMN_W
    )
    plt.close(fig5)
    print("Wrote fig5_jurisdiction_concentration.pdf")

    # ---------------------------------------------------------------------------
    # Summary
    # ---------------------------------------------------------------------------
    print()
    print(f"All figures written to: {FIGS_DIR}")
    print("  fig2_corpus_composition.pdf   — archetype + stratum stacked bars")
    print("  fig3_visibility_gradient.pdf  — provisional coded-change fractions")
    print("  fig4_collection_density.pdf   — collection density by year (NOT phenomenon density)")
    print("  fig5_jurisdiction_concentration.pdf — jurisdiction top-15 (evidence-frame framing)")
    for name, report in font_legibility.items():
        print(f"  {name}: minimum embedded font "
              f"{report['embedded_min_font_pt']:.2f}pt")

    (FIGS_DIR / "figure_inputs.json").write_text(json.dumps({
        "admitted_events": n_admitted,
        "archetypes": arch_counts,
        "strata": strat_counts,
        "layers": display,
        "jurisdictions": dict(jur_counter),
        "us_annotation": us_label,
        "hero_event": hero["id"],
        "hero_rows": FANOUT,
        "font_legibility": font_legibility,
    }, indent=2, sort_keys=True) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT,
                        help="Output directory for PDFs and figure_inputs.json")
    args = parser.parse_args()
    render(load_inputs(), args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
