from build_paper_macros import default_paper_dir


def test_standalone_clone_uses_local_analysis_directory(tmp_path):
    repo = tmp_path / "dataset"
    repo.mkdir()
    assert default_paper_dir(repo) == repo / "analysis/manuscript"


def test_existing_sibling_manuscript_is_selected(tmp_path):
    repo = tmp_path / "dataset"
    sibling = tmp_path / "6a1d66df502cdc827ad0999d"
    repo.mkdir()
    sibling.mkdir()
    (sibling / "main.tex").write_text("manuscript")
    assert default_paper_dir(repo) == sibling
