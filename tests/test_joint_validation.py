import csv
import pytest
import yaml

from analyze_joint_validation import FIELDS, evaluate_units, legacy_diagnostics, load_units, missingness_summary, write_template


def unit(uid="u1", **overrides):
    row = {key: "" for key in FIELDS}
    row.update(unit_id=uid, episode_id="e1", episode_family_id="family1", target_id=uid, surface="asset_onchain", panel_member_id="usdc", action_type="addition", window_start_utc="2022-08-01T00:00:00Z", window_end_utc="2022-09-08T00:00:00Z", split="evaluation", eligibility="eligible", outcome_definition="blacklist_state_change", legacy_outcome_definition="blacklist_state_change", revised_outcome_definition="blacklist_state_change", reference_outcome_definition="blacklist_state_change", legacy_outcome="unknown", revised_outcome="positive", reference_outcome="unknown", reference_provenance="pending")
    row.update(overrides)
    return row


def write_units(path, rows):
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    return path


def test_missingness_is_not_silently_zero():
    result = missingness_summary(["positive", "negative", "unknown", "unknown"])
    assert result["positive_fraction_observed_only"] == .5
    assert result["missing_as_zero_fraction"] == .25
    assert result["missingness_bounds"] == [.25, .75]
    assert missingness_summary([])["missingness_bounds"] is None


def test_legacy_gap_and_na_separated_even_with_claimed_change(tmp_path):
    for i, status in enumerate(["not_applicable", "not_measured", "measured"]):
        event = {"id": str(i), "status": "admitted", "coverage": [{"layer": "l0_network", "status": status}], "observations": [{"layer": "l0_network", "observation_kind": "observed_change"}]}
        (tmp_path / f"{i}.yaml").write_text(yaml.safe_dump(event))
    row = legacy_diagnostics(tmp_path)["rows"][0]
    assert row["eligible_units"] == 2
    assert row["positive"] == 1 and row["unknown"] == 1
    assert row["legacy_not_applicable_excluded"] == 1


@pytest.mark.parametrize("mutation,match", [
    ({"legacy_outcome": "negative", "legacy_outcome_definition": "announcement"}, "unmatched"),
    ({"revised_outcome": ""}, "explicit unknown"),
    ({"eligibility": "N/A"}, "invalid eligibility"),
    ({"window_end_utc": "2021-01-01T00:00:00Z"}, "window is reversed"),
    ({"legacy_query_seconds": "nan"}, "finite query duration"),
    ({"reference_outcome": "positive", "reference_provenance": "independent_human_adjudication"}, "reviewer IDs"),
])
def test_invalid_evaluation_input_fails(tmp_path, mutation, match):
    with pytest.raises(ValueError, match=match):
        load_units(write_units(tmp_path / "input.csv", [unit(**mutation)]))


def test_duplicate_units_rejected(tmp_path):
    with pytest.raises(ValueError, match="duplicate"):
        load_units(write_units(tmp_path / "input.csv", [unit(), unit()]))


def test_duplicate_natural_units_rejected(tmp_path):
    with pytest.raises(ValueError, match="underlying unit"):
        load_units(write_units(tmp_path / "input.csv", [unit(), unit("different_id", target_id="u1")]))


def test_duplicate_address_with_different_target_alias_rejected(tmp_path):
    address = "0x" + "a" * 40
    with pytest.raises(ValueError, match="underlying unit"):
        load_units(write_units(tmp_path / "input.csv", [unit(target_address=address), unit("alias", target_address=address)]))


@pytest.mark.parametrize("episode", ["e1", "related-legal-action"])
def test_pilot_family_cannot_leak_to_evaluation(tmp_path, episode):
    with pytest.raises(ValueError, match="pilot family"):
        load_units(write_units(tmp_path / "input.csv", [unit(split="pilot"), unit("evaluation", episode_id=episode)]))


def test_model_reference_does_not_unlock_quality_and_pilot_excluded(tmp_path):
    rows = load_units(write_units(tmp_path / "input.csv", [unit(reference_outcome="negative", reference_provenance="llm"), unit("pilot", split="pilot", episode_id="pilot-episode", episode_family_id="pilot-family")]))
    result = evaluate_units(rows)
    assert result["pilot_units_excluded"] == 1
    assert result["eligible_evaluation_units"] == 1
    assert result["groups"][0]["quality"]["revised"] is None
    assert result["status"] == "pending_independent_reference"


def test_reference_subset_abstention_and_naive_baseline(tmp_path):
    ref = dict(reference_outcome="positive", reference_provenance="independent_human_adjudication", reference_reviewer_ids="reviewer-a;reviewer-b", reference_completed_at_utc="2026-09-20T00:00:00Z", reference_artifact="fixture-only:adjudication")
    rows = load_units(write_units(tmp_path / "input.csv", [unit(**ref), unit("unreviewed")]))
    group = evaluate_units(rows)["groups"][0]
    assert group["reference_ready_units"] == 1 and group["reference_pending_units"] == 1
    assert group["quality"]["legacy"]["abstained"] == 1
    assert group["quality"]["legacy"]["accuracy_on_classified"] is None
    assert group["quality"]["naive_missing_as_zero"]["fn"] == 1
    assert group["quality"]["revised"]["end_to_end_correct_fraction"] == 1


def test_episode_bootstrap_and_separate_action_types(tmp_path):
    rows = [unit(f"a{i}", episode_id="e1", legacy_outcome="negative") for i in range(3)]
    rows += [unit("b", episode_id="e2", legacy_outcome="positive", revised_outcome="negative"), unit("r", action_type="removal")]
    groups = evaluate_units(load_units(write_units(tmp_path / "input.csv", rows)), n_boot=100)["groups"]
    assert len(groups) == 2
    added = next(g for g in groups if g["action_type"] == "addition")
    assert added["paired_change"]["revised_minus_legacy"] == .5
    ci = added["paired_change"]["cluster_bootstrap_ci"]
    assert ci["n_units"] == 2 and ci["resampling_unit"] == "legal_episode"


def test_template_protects_added_answers(tmp_path):
    path = tmp_path / "units.csv"
    write_template(path)
    path.write_text(path.read_text() + "human data\n")
    with pytest.raises(ValueError, match="Refusing"):
        write_template(path)


def test_empty_reference_input_produces_no_evaluation():
    result = evaluate_units([])
    assert result["status"] == "no_evaluation_units"
    assert result["groups"] == []
