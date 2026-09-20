"""Evaluation regressions: fixed classes, gating, and snapshot identity."""
import pytest

import benchmark_coverage_prediction as benchmark
import compile_llm_comparison as comparison
import llm_baseline_coverage as llm


def test_fixed_class_f1_does_not_reward_absent_classes():
    assert benchmark.macro_f1(["not_applicable"] * 3, ["not_applicable"] * 3) == 0.25
    assert llm.macro_f1 is benchmark.macro_f1
    assert comparison.macro_f1 is benchmark.macro_f1
    assert benchmark.scope_f1(["not_applicable"], ["not_applicable"]) == 0.5
    assert benchmark.cond_quality(["measured"], ["measured"]) == pytest.approx(1 / 3)
    assert benchmark.cond_quality(["measured"], ["not_applicable"]) == 0
    assert benchmark.scope_f1(["measured"], [llm.INVALID]) == 0
    with pytest.raises(ValueError, match="length"):
        benchmark.macro_f1(["measured"], [])


def test_reaction_oracle_and_end_to_end_use_same_gold_denominator():
    rows = [{"event_id": str(year), "year": year, "feat": {},
             "labels": {layer: ("measured", "observed_change") for layer in benchmark.LAYERS}}
            for year in (2016, 2017)]
    _, reactions = benchmark.rolling_eval(
        rows, lambda _: lambda feat, layer: "not_applicable",
        lambda _: lambda feat, layer: "observed_change")
    for layer in benchmark.LAYERS:
        values = reactions[layer]
        assert values["gold"] == values["oracle"] == ["observed_change"]
        assert values["end_to_end"] == [benchmark.ABSTAIN]
        assert benchmark.macro_f1(values["gold"], values["end_to_end"], benchmark.REACTION) == 0


def test_prompt_only_grounded_mode_receives_training_counts():
    feat = {"stratum": "S1", "trigger_type": "designation", "us": True,
            "target_kind": "service", "year": 2026}
    zero = llm.make_prompt(feat)
    assert zero == llm.BASE + llm.CLOSE % feat
    assert "TRAINING-SPLIT" not in zero
    for old_claim in ("poorest", "by far the largest", "Most triggers touch", "before 2025"):
        assert old_claim not in zero
    grounded = llm.make_prompt(feat, "TRAIN-ONLY-COUNTS", cutoff=2023)
    assert "trigger year < 2023" in grounded
    assert "TRAIN-ONLY-COUNTS" in grounded


def test_frozen_snapshot_cannot_silently_join_current_rows():
    data = {"n": 2, "gold": {l: ["measured", "not_measured"] for l in benchmark.LAYERS},
            "pred": {l: ["measured", "not_applicable"] for l in benchmark.LAYERS}}
    rows = [{"event_id": "b", "labels": {l: "not_measured" for l in benchmark.LAYERS}},
            {"event_id": "a", "labels": {l: "measured" for l in benchmark.LAYERS}}]
    with pytest.raises(ValueError, match="event IDs"):
        comparison.align_current_predictions(data, rows)
    data.update(event_ids=["a", "b"], prompt_version=llm.PROMPT_VERSION)
    assert comparison.align_current_predictions(data, rows)[benchmark.LAYERS[0]] == [
        "not_applicable", "measured"]
    rows[0]["labels"][benchmark.LAYERS[0]] = "measured"
    with pytest.raises(ValueError, match="gold labels"):
        comparison.align_current_predictions(data, rows)


def test_prediction_failure_is_invalid_not_not_applicable(monkeypatch):
    def unavailable(*args, **kwargs):
        raise OSError("unavailable")

    monkeypatch.setattr(llm.subprocess, "run", unavailable)
    assert set(llm.llm_predict(("unused", "test")).values()) == {llm.INVALID}
