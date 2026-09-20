"""Public descriptions follow source YAML/CFF without hash or timestamp cycles."""
import json

import pytest
import yaml

from sync_snapshot_descriptors import build_outputs, citation_text


@pytest.fixture
def descriptor_repo(tmp_path):
    (tmp_path / "events").mkdir()
    cff = {
        "title": "Test corpus", "abstract": "Working labels; validation pending.",
        "version": "0.2-test", "repository-code": "https://example.test/repo",
        "authors": [{"family-names": "Yang", "given-names": "Xiangwen", "affiliation": "Sydney"},
                    {"family-names": "Yu", "given-names": "Jiangshan", "affiliation": "Sydney"}],
    }
    (tmp_path / "CITATION.cff").write_text(yaml.safe_dump(cff))
    (tmp_path / "events/one.yaml").write_text(yaml.safe_dump({
        "id": "one", "status": "admitted", "research_stratum": "S1_ofac_sdn"}))
    (tmp_path / "events/two.yaml").write_text(yaml.safe_dump({
        "id": "two", "status": "draft", "research_stratum": "S4_nation_state"}))
    (tmp_path / "README.md").write_text("Keep intro.\n<!-- SNAPSHOT:START -->\nold\n<!-- SNAPSHOT:END -->\nKeep end.\n")
    (tmp_path / ".zenodo.json").write_text(json.dumps({
        "description": "stale", "creators": [{"name": "old author"}],
        "publication_date": "2026-01-01", "related_identifiers": [{"identifier": "keep"}],
    }))
    (tmp_path / "croissant.json").write_text(json.dumps({
        "@context": {"keep": "context"}, "datePublished": "2026",
        "distribution": [{"@id": "repo", "sha256": "main", "contentUrl": "keep-url"},
                         {"@id": "event-records", "description": "405 records", "includes": "events/*.yaml"}],
        "recordSet": [{"@id": "events", "description": "365 admitted", "field": [
            {"@id": "events/status", "description": "365", "dataType": "sc:Text"}]}],
    }))
    return tmp_path


def test_sources_replace_counts_and_authors_without_inventing_release(descriptor_repo):
    outputs = build_outputs(descriptor_repo)
    zenodo = json.loads(outputs[".zenodo.json"])
    croissant = json.loads(outputs["croissant.json"])
    assert [creator["name"] for creator in zenodo["creators"]] == ["Yang, Xiangwen", "Yu, Jiangshan"]
    assert "Yang, Xiangwen; Yu, Jiangshan." in croissant["citeAs"]
    assert "2026" not in croissant["citeAs"]
    assert "publication_date" not in zenodo
    assert "datePublished" not in croissant
    assert "sha256" not in croissant["distribution"][0]
    for text in outputs.values():
        assert "2 event records: 1 admitted, 1 draft, 0 rejected." in text
        assert "405" not in text and "365" not in text
    assert croissant["@context"] == {"keep": "context"}
    assert croissant["distribution"][0]["contentUrl"] == "keep-url"
    assert croissant["recordSet"][0]["field"][0]["dataType"] == "sc:Text"
    assert zenodo["related_identifiers"] == [{"identifier": "keep"}]
    assert outputs["README.md"].startswith("Keep intro.\n")
    assert outputs["README.md"].endswith("Keep end.\n")


def test_second_sync_is_stable_and_ignores_generated_metadata(descriptor_repo):
    first = build_outputs(descriptor_repo)
    for name, text in first.items():
        (descriptor_repo / name).write_text(text)
    (descriptor_repo / "dataset.meta.json").write_text('{"source_input_hash":"changes-after-build", "event_count":999}')
    assert build_outputs(descriptor_repo) == first
    (descriptor_repo / "dataset.meta.json").write_text('{"generated_at":"2099-01-01", "event_count":888}')
    assert build_outputs(descriptor_repo) == first


def test_new_yaml_status_updates_descriptors(descriptor_repo):
    path = descriptor_repo / "events/two.yaml"
    event = yaml.safe_load(path.read_text())
    event["status"] = "admitted"
    path.write_text(yaml.safe_dump(event))
    outputs = build_outputs(descriptor_repo)
    for text in outputs.values():
        assert "2 event records: 2 admitted, 0 draft, 0 rejected." in text


def test_declared_release_date_is_used_without_wall_clock(descriptor_repo):
    path = descriptor_repo / "CITATION.cff"
    cff = yaml.safe_load(path.read_text())
    cff["date-released"] = "2024-04-05"
    path.write_text(yaml.safe_dump(cff))
    outputs = build_outputs(descriptor_repo)
    assert json.loads(outputs[".zenodo.json"])["publication_date"] == "2024-04-05"
    assert json.loads(outputs["croissant.json"])["datePublished"] == "2024-04-05"
    assert "(2024)" in citation_text(cff)


def test_missing_markers_fail_before_rewriting_other_descriptors(descriptor_repo):
    (descriptor_repo / "README.md").write_text("No managed block")
    before = (descriptor_repo / ".zenodo.json").read_bytes()
    with pytest.raises(ValueError, match="SNAPSHOT marker"):
        build_outputs(descriptor_repo)
    assert (descriptor_repo / ".zenodo.json").read_bytes() == before
