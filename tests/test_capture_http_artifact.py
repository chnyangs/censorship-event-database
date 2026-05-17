# SPDX-License-Identifier: MIT
"""Regression tests for HTTP evidence capture."""
from __future__ import annotations

import json
import hashlib
import sys

import capture_http_artifact as capture


def test_json_capture_keeps_body_and_metadata_separate(tmp_path, monkeypatch):
    repo_root = tmp_path
    output_dir = repo_root / "sources" / "http_captures" / "json-case"
    url = "https://example.test/api/query.json?x=1"

    def fake_capture_url(url_arg, timeout, allow_insecure_tls=False, user_agent=capture.USER_AGENT):
        return {
            "requested_url": url_arg,
            "final_url": url_arg,
            "status": 200,
            "redirected": False,
            "fetched_at": "2026-05-17T00:00:00Z",
            "headers": {"Content-Type": "application/json"},
            "content_type": "application/json",
            "content_length": 12,
            "sha256": "0" * 64,
            "title": None,
            "body": b'{"ok": true}',
        }

    monkeypatch.setattr(capture, "REPO_ROOT", repo_root)
    monkeypatch.setattr(capture, "capture_url", fake_capture_url)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "capture_http_artifact.py",
            url,
            "--output-dir",
            str(output_dir),
        ],
    )

    assert capture.main() == 0

    basename = capture.build_basename(url)
    body_path = output_dir / f"{basename}.json"
    meta_path = output_dir / f"{basename}.meta.json"
    assert body_path.read_text() == '{"ok": true}'
    metadata = json.loads(meta_path.read_text())
    assert metadata["body_path"] == str(body_path.relative_to(repo_root))
    assert metadata["metadata_path"] == str(meta_path.relative_to(repo_root))


def test_capture_url_uses_user_agent_override(monkeypatch):
    seen = {}

    class FakeHeaders:
        def get(self, name, default=None):
            return "application/json" if name == "Content-Type" else default

        def items(self):
            return [("Content-Type", "application/json")]

    class FakeResponse:
        status = 200
        headers = FakeHeaders()

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def read(self):
            return b'{"ok": true}'

        def geturl(self):
            return "https://example.test/api"

    def fake_urlopen(request, timeout, context):
        seen["user_agent"] = request.get_header("User-agent")
        return FakeResponse()

    monkeypatch.setattr(capture.urllib.request, "urlopen", fake_urlopen)

    result = capture.capture_url(
        "https://example.test/api",
        timeout=1,
        user_agent="Mozilla/5.0 evidence-capture",
    )

    assert seen["user_agent"] == "Mozilla/5.0 evidence-capture"
    assert result["sha256"] == hashlib.sha256(b'{"ok": true}').hexdigest()


def test_build_basename_truncates_long_percent_encoded_urls():
    url = "https://example.test/news/" + ("%D8%A7" * 80)

    basename = capture.build_basename(url)

    assert len(basename) <= capture.MAX_BASENAME_CHARS
    assert basename.startswith("example.test__news-")
    assert basename.endswith(hashlib.sha256(url.encode("utf-8")).hexdigest()[:10])
