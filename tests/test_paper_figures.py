"""Figure regressions that can change the interpretation of paper results."""
import csv
import json

import pytest
import yaml

pytest.importorskip("matplotlib")

from build_paper_figures import (
    LAYER_ORDER,
    MIN_EMBEDDED_FONT_PT,
    fanout_rows,
    jurisdiction_summary,
    layer_display,
    load_inputs,
    render,
)


def test_fraction_and_blue_point_use_same_rubric():
    rubrics = {
        "strict": {"rate": 0.0, "num": 0, "den": 8},
        "current": {"rate": 0.25, "num": 2, "den": 8},
        "permissive": {"rate": 0.625, "num": 10, "den": 16},
    }
    display = layer_display("l1_consensus", {"l1_consensus": rubrics})
    assert display["fraction"] == "10/16"
    assert display["rates"]["permissive"] == 10 / 16
    assert display["rates"]["current"] == 2 / 8


@pytest.mark.parametrize("layer", ["l0_network", "asset_onchain"])
def test_suppressed_rates_cannot_leak_from_numerical_source(layer):
    rubrics = {name: {"rate": 1.0, "num": 5, "den": 5}
               for name in ("strict", "current", "permissive")}
    display = layer_display(layer, {layer: rubrics})
    assert display["fraction"] == "—"
    assert all(value is None for value in display["rates"].values())


def test_jurisdiction_share_tracks_corpus_size_and_counts_each_code_once():
    counts, label = jurisdiction_summary([
        {"jurisdiction": ["US", "US", "EU"]},
        {"jurisdiction": "US"},
        {"jurisdiction": ["EU"]},
    ])
    assert counts == {"US": 2, "EU": 2}
    assert label == "US: 2/3 (66.7%)"


def test_fanout_uses_changed_source_labels_and_does_not_invent_observations():
    rows = fanout_rows({
        "coverage": [{"layer": "l3_rpc", "status": "not_measured"}],
        "observations": [{"layer": "l3_rpc", "event": "source_code_edit",
                          "observation_kind": "observed_change",
                          "attribution": "plausible", "precision": "day",
                          "delta_hours": 48}],
    })
    by_layer = {row[0]: row for row in rows}
    assert by_layer["l3_rpc"][2] == "not_measured"
    assert "source code edit" in by_layer["l3_rpc"][4]
    assert "plausible" in by_layer["l3_rpc"][4]
    assert "48 h" in by_layer["l3_rpc"][4]
    assert by_layer["l0_network"][3] == "none"


def test_snapshot_membership_guard_accepts_new_size_but_rejects_stale_rows(tmp_path):
    (tmp_path / "events").mkdir()
    (tmp_path / "derived").mkdir()
    (tmp_path / "events/one.yaml").write_text(yaml.safe_dump({"id": "one", "status": "admitted"}))
    archetypes = tmp_path / "derived/event_archetypes.json"
    archetypes.write_text(json.dumps([{"event_id": "one", "derived_archetype": "null_event"}]))
    (tmp_path / "derived/layer_observability.json").write_text(json.dumps([
        {"layer": layer, "total_events": 1, "measured_count": 1,
         "partially_measured_count": 0} for layer in LAYER_ORDER
    ]))
    fields = ["layer"] + [f"{rubric}_{field}"
                          for rubric in ("strict", "current", "permissive")
                          for field in ("rate", "num", "den")]
    with (tmp_path / "derived/admission_sensitivity.csv").open("w") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for layer in LAYER_ORDER:
            writer.writerow({"layer": layer, **{field: 1 for field in fields[1:]}})
    assert len(load_inputs(tmp_path)["admitted"]) == 1
    archetypes.write_text(json.dumps([{"event_id": "other"}]))
    with pytest.raises(ValueError, match="membership"):
        load_inputs(tmp_path)


def test_included_paper_figures_keep_every_text_element_at_least_9pt(tmp_path):
    render(load_inputs(), tmp_path)
    report = json.loads((tmp_path / "figure_inputs.json").read_text())["font_legibility"]
    expected = {
        "fig1_tornado_fanout.pdf",
        "fig2_corpus_composition.pdf",
        "fig5_jurisdiction_concentration.pdf",
    }
    assert set(report) == expected
    for name in expected:
        assert report[name]["visible_text_elements"] > 0
        assert report[name]["embedded_min_font_pt"] >= MIN_EMBEDDED_FONT_PT
        assert (tmp_path / name).is_file()
