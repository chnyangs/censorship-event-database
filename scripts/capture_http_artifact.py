#!/usr/bin/env python3
"""Capture reproducible HTTP artifacts for current-state web evidence.

Three modes are available:

- Default: fetch each URL, store body + metadata under --output-dir, write a
  manifest.json collecting the run.
- --wayback-submit: additionally POST each URL to the Wayback Machine save API
  and record the timestamped archive URL in the capture metadata.
- --patch-event <event.yaml>: after capture, inject body_hash, body_path, and
  wayback fields into source entries in the event YAML whose `url:` matches
  a captured URL. Text-based injection preserves existing formatting.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_ROOT = REPO_ROOT / "sources" / "http_captures"
USER_AGENT = "p1-event-db-capture/0.1 (contact: xwy411@gmail.com)"
WAYBACK_SAVE_BASE = "https://web.archive.org/save/"


class TitleParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.title_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)

    @property
    def title(self) -> str | None:
        title = "".join(self.title_parts).strip()
        return title or None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Capture HTTP artifacts for one or more URLs.")
    parser.add_argument("urls", nargs="+", help="HTTP or HTTPS URLs to capture.")
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory where capture metadata and bodies should be written.",
    )
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing capture files for the same URL. Default: abort on collision.",
    )
    parser.add_argument(
        "--wayback-submit",
        action="store_true",
        help="Also submit each URL to the Wayback Machine save API and record the archive URL in the manifest.",
    )
    parser.add_argument(
        "--wayback-timeout",
        type=float,
        default=120.0,
        help="Timeout (seconds) for each Wayback save submission.",
    )
    parser.add_argument(
        "--patch-event",
        metavar="YAML",
        default=None,
        help="After capture, inject body_hash / body_path / wayback fields into source entries in this event YAML whose url matches a captured URL.",
    )
    return parser.parse_args()


def sanitize_filename(value: str) -> str:
    sanitized = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-")
    return sanitized or "capture"


def build_basename(url: str) -> str:
    """Return a filesystem-safe, collision-resistant basename for a URL.

    The host-path form is retained for human readability; a short hash of the
    full URL (including query and fragment) is appended so that distinct URLs
    sharing the same host and path do not overwrite each other.
    """
    parsed = urllib.parse.urlparse(url)
    host = sanitize_filename(parsed.netloc.lower())
    path = sanitize_filename(parsed.path.strip("/")) or "root"
    url_hash = hashlib.sha256(url.encode("utf-8")).hexdigest()[:10]
    return f"{host}__{path}__{url_hash}"


def detect_extension(content_type: str) -> str:
    lowered = content_type.lower()
    if "html" in lowered:
        return ".html"
    if "json" in lowered:
        return ".json"
    if "text/plain" in lowered:
        return ".txt"
    if "xml" in lowered:
        return ".xml"
    return ".bin"


def extract_title(body: bytes, content_type: str) -> str | None:
    if "html" not in content_type.lower():
        return None
    parser = TitleParser()
    try:
        parser.feed(body.decode("utf-8", errors="ignore"))
    except Exception:
        return None
    return parser.title


def capture_url(url: str, timeout: float) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    fetched_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read()
        content_type = response.headers.get("Content-Type", "application/octet-stream")
        return {
            "requested_url": url,
            "final_url": response.geturl(),
            "status": response.status,
            "redirected": response.geturl() != url,
            "fetched_at": fetched_at,
            "headers": dict(response.headers.items()),
            "content_type": content_type,
            "content_length": len(body),
            "sha256": hashlib.sha256(body).hexdigest(),
            "title": extract_title(body, content_type),
            "body": body,
        }


def submit_to_wayback(url: str, timeout: float) -> tuple[str | None, str | None]:
    """Submit URL to the Wayback save API; return (wayback_url, error)."""
    request = urllib.request.Request(
        WAYBACK_SAVE_BASE + url,
        headers={"User-Agent": USER_AGENT},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            final_url = response.geturl()
            if "/web/" not in final_url:
                return None, f"Wayback did not return an archived URL (final: {final_url})"
            if response.status < 200 or response.status >= 300:
                return None, f"Wayback returned HTTP {response.status}"
            return final_url, None
    except urllib.error.HTTPError as exc:
        return None, f"Wayback HTTPError {exc.code}"
    except urllib.error.URLError as exc:
        return None, f"Wayback URLError {exc.reason}"
    except Exception as exc:  # pragma: no cover — defensive
        return None, f"{type(exc).__name__}: {exc}"


_SOURCE_FIELDS_TO_INJECT = ("wayback", "body_hash", "body_path")


def patch_event_yaml(yaml_path: Path, url_to_fields: dict[str, dict[str, str]]) -> dict[str, int]:
    """Inject new fields after matching `url: <URL>` lines in the event YAML.

    Uses text-level injection to preserve comments and formatting. Fields that
    already exist in the same source block are left untouched.
    """
    original = yaml_path.read_text()
    lines = original.splitlines(keepends=True)
    out_lines: list[str] = []
    stats = {"sources_patched": 0, "fields_injected": 0, "urls_not_found": 0}
    matched_urls: set[str] = set()

    url_line_re = re.compile(r"^(?P<indent>[ \t]+)url:[ \t]*(?P<value>\S+)[ \t]*$")

    i = 0
    while i < len(lines):
        line = lines[i]
        match = url_line_re.match(line.rstrip("\n"))
        out_lines.append(line)
        if not match:
            i += 1
            continue

        target_url = match.group("value").strip()
        if target_url not in url_to_fields:
            i += 1
            continue

        indent = match.group("indent")
        fields_requested = url_to_fields[target_url]

        # Scan the rest of the source block to find fields already present.
        existing_fields: set[str] = set()
        j = i + 1
        while j < len(lines):
            scan = lines[j].rstrip("\n")
            if not scan.strip():
                j += 1
                continue
            # End of block when we hit a less-indented line or a new list item.
            leading = scan[: len(indent)]
            if leading != indent:
                break
            remainder = scan[len(indent) :]
            if remainder.startswith("- "):
                break
            m = re.match(r"(\w+):", remainder)
            if m:
                existing_fields.add(m.group(1))
            j += 1

        injected_here = 0
        for field_name in _SOURCE_FIELDS_TO_INJECT:
            if field_name not in fields_requested:
                continue
            if field_name in existing_fields:
                continue
            value = fields_requested[field_name]
            out_lines.append(f"{indent}{field_name}: {value}\n")
            injected_here += 1

        if injected_here > 0:
            stats["sources_patched"] += 1
            stats["fields_injected"] += injected_here
        matched_urls.add(target_url)
        i += 1

    for url in url_to_fields:
        if url not in matched_urls:
            stats["urls_not_found"] += 1

    if stats["fields_injected"] > 0:
        yaml_path.write_text("".join(out_lines))

    return stats


def main() -> int:
    args = parse_args()
    output_dir = Path(args.output_dir).resolve()
    try:
        output_dir.relative_to(REPO_ROOT)
    except ValueError:
        print(
            f"[FAIL] --output-dir {output_dir} must be inside the repo root {REPO_ROOT} "
            "so that body_path values are repo-relative.",
            file=sys.stderr,
        )
        return 2
    output_dir.mkdir(parents=True, exist_ok=True)

    manifest: dict[str, Any] = {
        "captured_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "captures": [],
    }
    failures = 0
    # Fields per URL for optional --patch-event pass.
    url_to_fields: dict[str, dict[str, str]] = {}

    for url in args.urls:
        basename = build_basename(url)
        entry: dict[str, Any] = {"requested_url": url}
        captured_ok = False

        try:
            capture = capture_url(url, args.timeout)
            captured_ok = True
        except urllib.error.HTTPError as exc:
            failures += 1
            entry["capture_error"] = f"HTTPError {exc.code}"
            print(f"[FAIL-capture] {url} HTTPError {exc.code}")
        except urllib.error.URLError as exc:
            failures += 1
            entry["capture_error"] = f"URLError {exc.reason}"
            print(f"[FAIL-capture] {url} URLError {exc.reason}")

        if captured_ok:
            ext = detect_extension(capture["content_type"])
            body_name = f"{basename}{ext}"
            json_name = f"{basename}.json"
            body_path = output_dir / body_name
            json_path = output_dir / json_name

            if not args.force and (body_path.exists() or json_path.exists()):
                failures += 1
                error_message = (
                    f"capture collision: {body_path.name} or {json_path.name} already exists. "
                    "Pass --force to overwrite."
                )
                entry["capture_error"] = error_message
                captured_ok = False
                print(f"[SKIP] {url} {error_message}")
            else:
                body_path.write_bytes(capture.pop("body"))
                capture["body_path"] = str(body_path.relative_to(REPO_ROOT))
                capture["metadata_path"] = str(json_path.relative_to(REPO_ROOT))
                json_path.write_text(json.dumps(capture, indent=2, sort_keys=True) + "\n")
                entry.update(capture)
                print(
                    f"[OK-capture] {url} -> {capture['final_url']} "
                    f"({capture['status']}, sha256={capture['sha256'][:12]}...)"
                )
                url_to_fields.setdefault(url, {})
                url_to_fields[url]["body_hash"] = f"sha256:{capture['sha256']}"
                url_to_fields[url]["body_path"] = capture["body_path"]

        if args.wayback_submit:
            wb_url, wb_err = submit_to_wayback(url, args.wayback_timeout)
            if wb_url:
                entry["wayback"] = wb_url
                url_to_fields.setdefault(url, {})
                url_to_fields[url]["wayback"] = wb_url
                print(f"[OK-wayback] {url} -> {wb_url}")
            else:
                entry["wayback_error"] = wb_err
                failures += 1
                print(f"[FAIL-wayback] {url} {wb_err}")

        manifest["captures"].append(entry)

    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(f"Wrote manifest to {manifest_path}")

    if args.patch_event:
        yaml_path = Path(args.patch_event).resolve()
        if not yaml_path.is_file():
            print(f"[FAIL-patch] event file not found: {yaml_path}", file=sys.stderr)
            return max(failures, 1)
        if not url_to_fields:
            print("[SKIP-patch] no capture or wayback succeeded; nothing to inject.")
        else:
            stats = patch_event_yaml(yaml_path, url_to_fields)
            print(
                f"[patch] {yaml_path.name}: "
                f"{stats['sources_patched']} sources patched, "
                f"{stats['fields_injected']} fields injected, "
                f"{stats['urls_not_found']} URLs not found in YAML"
            )

    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
