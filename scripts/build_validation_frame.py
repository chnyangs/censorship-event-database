#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Enumerate an OFAC source frame without crypto/outcome keyword selection.

All yearly Recent Actions listing pages are traversed and reconciled with the
official displayed totals. Annual SDN histories provide an independent date-level
cross-check. Parsing produces machine proposals, never human adjudication/gold.
"""
from __future__ import annotations

import argparse
import collections
from concurrent.futures import ThreadPoolExecutor
import csv
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import io
import json
import math
import pathlib
import re
import subprocess
import threading
import time
from urllib.parse import urljoin, urlparse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://ofac.treasury.gov"
ARCHIVE = BASE + "/specially-designated-nationals-list-sdn-list/archive-of-changes-to-the-sdn-list"
VERSION = "1.0.0"
ACTION_PATH = re.compile(r"^/recent-actions/(\d{8}(?:[_-][A-Za-z0-9_-]+)?)$")
ETH = re.compile(r"Digital\s+Currency\s+Address\s*[-–]\s*ETH\s+(0x[0-9a-fA-F]{40})(?![0-9a-fA-F])", re.I)
HEX = re.compile(r"(?<![A-Za-z0-9])0x[0-9a-fA-F]{40}(?![A-Za-z0-9])")


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(raw):
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def csv_text(rows, fields):
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader(); writer.writerows(rows)
    return output.getvalue()


class Page(HTMLParser):
    """Small stdlib parser retaining legal body line breaks and listing links."""
    def __init__(self, raw):
        super().__init__(convert_charrefs=True)
        self.all_text, self.body, self.links, self.listing_rows = [], [], [], []
        self.hidden, self.body_depth, self.depth = 0, None, 0
        self.row_depth, self.row = None, None
        self.anchor = None
        self.feed(raw.decode("utf-8", errors="replace"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        void = tag in ("area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr")
        if not void:
            self.depth += 1
        if "field--name-field-body" in attrs.get("class", "").split():
            self.body_depth = self.depth
        if "views-row" in attrs.get("class", "").split():
            self.row_depth = self.depth
            self.row = {"links": [], "text": []}
        if tag in ("script", "style"):
            self.hidden += 1
        if tag == "a":
            self.anchor = [attrs.get("href", ""), []]
        if tag in ("br", "p", "h1", "h2", "h3", "li"):
            self.all_text.append("\n")
            if self.body_depth is not None:
                self.body.append("\n")

    def handle_endtag(self, tag):
        if tag in ("area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"):
            return
        if tag == "a" and self.anchor:
            self.links.append((self.anchor[0], " ".join(self.anchor[1]).strip()))
            if self.row is not None:
                self.row["links"].append((self.anchor[0], " ".join(self.anchor[1]).strip()))
            self.anchor = None
        if tag in ("script", "style"):
            self.hidden = max(0, self.hidden - 1)
        if tag in ("p", "div", "h1", "h2", "h3", "li"):
            self.all_text.append("\n")
            if self.body_depth is not None:
                self.body.append("\n")
        if self.body_depth == self.depth:
            self.body_depth = None
        if self.row_depth == self.depth:
            self.listing_rows.append(self.row)
            self.row_depth, self.row = None, None
        self.depth = max(0, self.depth - 1)

    def handle_data(self, data):
        if self.hidden:
            return
        self.all_text.append(data)
        if self.body_depth is not None:
            self.body.append(data)
        if self.anchor:
            self.anchor[1].append(data)
        if self.row is not None:
            self.row["text"].append(data)

    @property
    def text(self):
        return " ".join(" ".join(self.all_text).split())


def parse_listing(raw, year):
    page = Page(raw)
    match = re.search(r"Displaying\s+([\d,]+)\s*[-–]\s*([\d,]+)\s+of\s+([\d,]+)\s+results", page.text)
    if not match:
        raise ValueError("Official result-count marker missing; listing not accepted")
    first, last, total = (int(part.replace(",", "")) for part in match.groups())
    actions = {}
    if page.listing_rows:
        for row in page.listing_rows:
            if not row["links"]:
                raise ValueError("Listing result has no action link")
            href, title = row["links"][0]
            url = urljoin(BASE, href)
            parsed = urlparse(url)
            if parsed.netloc != "ofac.treasury.gov":
                raise ValueError("Listing action link is outside official OFAC host")
            dates = re.findall(r"([A-Z][a-z]+ \d{1,2}, \d{4})", " ".join(row["text"]))
            if not dates:
                raise ValueError("Listing result publication date missing")
            # Titles may cite an earlier action date. The result's publication
            # metadata follows its title, so use the final date in this row.
            date_value = datetime.strptime(dates[-1], "%B %d, %Y").date()
            if date_value.year != year:
                raise ValueError("Listing result falls outside requested year")
            path_match = ACTION_PATH.match(parsed.path)
            slug = path_match[1] if path_match else (parsed.path.strip("/").replace("/", "-")[-120:])
            actions[url] = {"action_url": url, "action_slug": slug, "listing_title": title,
                            "date_candidate": date_value.isoformat()}
        return {"first": first, "last": last, "total": total, "actions": list(actions.values())}
    for href, title in page.links:
        url = urljoin(BASE, href)
        parsed = urlparse(url)
        action = ACTION_PATH.match(parsed.path)
        if action and parsed.netloc == "ofac.treasury.gov" and action[1].startswith(str(year)):
            actions[url] = {"action_url": url, "action_slug": action[1], "listing_title": title,
                            "date_candidate": f"{action[1][:4]}-{action[1][4:6]}-{action[1][6:8]}"}
    return {"first": first, "last": last, "total": total, "actions": list(actions.values())}


def classify_header(line):
    if not re.match(r"^(?:The following|In addition, the following)", line, re.I):
        return None
    if len(line) > 650:
        return None
    matched = []
    for word, label in ((r"\b(?:added|additions)\b", "addition"), (r"\b(?:removed|deleted|deletions|removals)\b", "removal"),
                        (r"\b(?:changed|updated|amended|changes|updates)\b", "update")):
        if re.search(word, line, re.I):
            matched.append(label)
    if not matched:
        return None
    return matched[0] if len(matched) == 1 else "unclassified_mixed_marker"


def parse_action(raw):
    page = Page(raw)
    lines = [" ".join(line.split()) for line in "".join(page.body).splitlines() if line.strip()]
    release = re.search(r"Release Date\s+(\d{2})/(\d{2})/(\d{4})", page.text)
    release_date = f"{release[3]}-{release[1]}-{release[2]}" if release else ""
    kind, header, list_scope = "unclassified", "", "unclassified"
    sections, entries = [], []
    for number, line in enumerate(lines, 1):
        if "LIST UPDATE" in line.upper() and len(line) < 180:
            if re.search(r"\bNON[- ]SDN\b", line, re.I):
                list_scope = "non_sdn"
            elif "SPECIALLY DESIGNATED NATIONALS" in line.upper():
                list_scope = "sdn"
        proposed = classify_header(line)
        if proposed:
            kind, header = proposed, line
            if re.search(r"\bNON[- ]SDN\b", line, re.I):
                list_scope = "non_sdn"
            elif re.search(r"\bSDN\b|Specially Designated Nationals", line, re.I):
                list_scope = "sdn"
            sections.append({"body_line": number, "proposed_action_type": kind,
                             "proposed_list_scope": list_scope, "explicit_header": header})
        matches = ETH.findall(line)
        for address in sorted(set(matches), key=str.lower):
            # Prefix is a transparent extraction locator, not a resolved identity.
            prefix = line.split(";", 1)[0][:400]
            entries.append({"body_line": number, "address": address, "normalized_address": address.lower(),
                            "chain_marker": "ETH", "proposed_action_type": kind, "proposed_list_scope": list_scope,
                            "explicit_section_header": header,
                            "target_entry_prefix_candidate": prefix, "entry_text": line,
                            "status": "machine_extracted_pending_independent_adjudication"})
    all_hex = {match.lower() for match in HEX.findall(" ".join(lines))}
    parsed_hex = {row["normalized_address"] for row in entries}
    return {"release_date": release_date, "body_present": bool(lines), "sections": sections, "entries": entries,
            "unclassified_hex_strings": sorted(all_hex - parsed_hex), "body_lines": len(lines)}


class Fetcher:
    def __init__(self, source_dir, *, offline=False, interval=0.4, attempts=2):
        self.root, self.offline, self.interval, self.attempts = source_dir, offline, interval, attempts
        self.lock, self.next_start = threading.Lock(), 0.0
        self.root.mkdir(parents=True, exist_ok=True)

    def fetch(self, url, relative):
        path = self.root / relative
        meta_path = path.with_suffix(path.suffix + ".meta.json")
        if path.exists() and meta_path.exists():
            meta = json.loads(meta_path.read_text())
            if meta.get("status") == "retrieved" and sha(path.read_bytes()) == meta.get("body_hash"):
                return meta
        if self.offline:
            return {"url": url, "status": "not_cached", "source_path": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)}
        for attempt in range(1, self.attempts + 1):
            with self.lock:
                wait = max(0, self.next_start - time.monotonic())
                if wait:
                    time.sleep(wait)
                self.next_start = time.monotonic() + self.interval
            started = utc()
            meta = {"url": url, "source_path": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
                    "retrieval_started_utc": started, "attempt": attempt}
            try:
                request = urllib.request.Request(url, headers={"User-Agent": "CensorshipEventResearch/1.0 (public-source archive reconciliation)"})
                with urllib.request.urlopen(request, timeout=45) as response:
                    raw = response.read()
                    meta.update({"status": "retrieved", "http_status": response.status,
                                 "final_url": response.url, "content_type": response.headers.get("Content-Type"),
                                 "body_hash": sha(raw), "bytes": len(raw)})
                if relative.endswith(".pdf") and not raw.startswith(b"%PDF"):
                    raise ValueError("PDF response does not begin with %PDF")
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(raw)
            except Exception as error:
                meta.update({"status": "retrieval_failed", "error": str(error)})
            meta["retrieval_finished_utc"] = utc()
            with self.lock:
                with (self.root / "retrieval_attempts.jsonl").open("a") as handle:
                    handle.write(json.dumps(meta, sort_keys=True) + "\n")
            meta_path.parent.mkdir(parents=True, exist_ok=True)
            meta_path.write_text(json.dumps(meta, sort_keys=True, indent=2) + "\n")
            if meta["status"] == "retrieved":
                return meta
            if attempt < self.attempts:
                time.sleep(2 * attempt)
        return meta


def get_raw(meta):
    path = pathlib.Path(meta["source_path"])
    return (path if path.is_absolute() else ROOT / path).read_bytes()


def history_dates(text, year):
    # A dated heading is independent of crypto content. Text layout can still
    # lose headings; dates are a cross-check, not an automatic completeness proof.
    result = set()
    for month, day, shortyear in re.findall(r"(?m)^\s*[•\uf0b7]?\s*(\d{2})/(\d{2})/(\d{2})\s*:?\s*$", text):
        if int(shortyear) != year % 100:
            continue
        try:
            value = datetime(year, int(month), int(day)).date().isoformat()
        except ValueError:
            continue
        result.add(value)
    return sorted(result)


def run(args):
    years = list(range(args.start_year, args.end_year + 1))
    fetcher = Fetcher(args.source_dir, offline=args.offline, interval=args.interval)
    listing_manifest, action_map, year_rows, archive_rows = [], {}, [], []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        landing = fetcher.fetch(ARCHIVE, "archive_index.html")
        archive_links = dict(Page(get_raw(landing)).links) if landing["status"] == "retrieved" else {}
        for year in years:
            first_url = f"{BASE}/recent-actions?ra_year={year}&page=0"
            first_meta = fetcher.fetch(first_url, f"listings/{year}/000.html")
            if first_meta["status"] != "retrieved":
                year_rows.append({"year": year, "official_total": "", "unique_action_urls": 0,
                                  "listing_status": "listing_fetch_failed", "expected_pages": "", "accepted_pages": 0})
                continue
            try:
                first = parse_listing(get_raw(first_meta), year)
            except ValueError as error:
                year_rows.append({"year": year, "official_total": "", "unique_action_urls": 0,
                                  "listing_status": str(error), "expected_pages": "", "accepted_pages": 0})
                continue
            page_size = first["last"] - first["first"] + 1
            count = math.ceil(first["total"] / page_size)
            jobs = [(f"{BASE}/recent-actions?ra_year={year}&page={p}", f"listings/{year}/{p:03d}.html") for p in range(1, count)]
            metas = [first_meta] + list(pool.map(lambda job: fetcher.fetch(*job), jobs))
            year_actions, accepted, positions = set(), 0, set()
            for page_number, meta in enumerate(metas):
                row = {"year": year, "page_number": page_number, **meta}
                if meta["status"] == "retrieved":
                    try:
                        parsed = parse_listing(get_raw(meta), year)
                        expected_first = page_number * page_size + 1
                        if parsed["total"] != first["total"] or parsed["first"] != expected_first:
                            raise ValueError("Pagination total/start drift")
                        if len(parsed["actions"]) != parsed["last"] - parsed["first"] + 1:
                            raise ValueError("Parsed action-link count differs from displayed range")
                        accepted += 1
                        positions.update(range(parsed["first"], parsed["last"] + 1))
                        for action in parsed["actions"]:
                            year_actions.add(action["action_url"])
                            action_map[action["action_url"]] = {**action, "year": year,
                                                               "listing_source_path": meta["source_path"],
                                                               "listing_body_hash": meta["body_hash"]}
                        row["parse_status"] = "accepted"
                    except ValueError as error:
                        row["parse_status"] = str(error)
                listing_manifest.append(row)
            exhausted = (accepted == count and len(year_actions) == first["total"]
                         and positions == set(range(1, first["total"] + 1)))
            year_rows.append({"year": year, "official_total": first["total"], "unique_action_urls": len(year_actions),
                              "listing_status": "official_listing_pagination_exhausted" if exhausted else "incomplete_or_inconsistent_listing",
                              "expected_pages": count, "accepted_pages": accepted})
            print(f"Year {year}: {len(year_actions)}/{first['total']} action URLs, {accepted}/{count} listing pages", flush=True)
        # Fetch only URLs explicitly linked from the official history index.
        for year in years:
            suffix = f"sdnnew{year % 100:02d}.pdf"
            link = next((href for href in archive_links if urlparse(href).path.endswith("/" + suffix)), None)
            if not link:
                archive_rows.append({"year": year, "status": "annual_history_link_unavailable", "dates": []})
                continue
            meta = fetcher.fetch(urljoin(ARCHIVE, link), f"histories/{suffix}")
            record = {"year": year, **meta, "dates": []}
            if meta["status"] == "retrieved":
                source = pathlib.Path(meta["source_path"])
                source = source if source.is_absolute() else ROOT / source
                text_path = source.with_suffix(".txt")
                try:
                    if not text_path.exists():
                        subprocess.run(["pdftotext", "-raw", str(source), str(text_path)], check=True, capture_output=True)
                    record["text_extraction_command"] = "pdftotext -raw"
                    record["dates"] = history_dates(text_path.read_text(errors="replace"), year)
                    record["text_body_hash"] = sha(text_path.read_bytes())
                    record["text_source_path"] = str(text_path.relative_to(ROOT)) if text_path.is_relative_to(ROOT) else str(text_path)
                    record["extraction_status"] = "dated_headings_extracted" if record["dates"] else "no_date_headings_parsed"
                except (OSError, subprocess.CalledProcessError) as error:
                    record["extraction_status"] = str(error)
            archive_rows.append(record)
            print(f"History {year}: {record.get('status')}, {len(record['dates'])} dated headings", flush=True)
        actions = sorted(action_map.values(), key=lambda row: row["action_slug"])
        selected = actions if args.max_action_pages is None else actions[:args.max_action_pages]
        jobs = [(row["action_url"], f"actions/{row['action_slug']}.html") for row in selected]
        print(f"Retrieving {len(selected)} of {len(actions)} enumerated action pages", flush=True)
        responses = {}
        for index, (row, meta) in enumerate(zip(selected, pool.map(lambda job: fetcher.fetch(*job), jobs)), 1):
            responses[row["action_url"]] = meta
            if index % 25 == 0 or index == len(selected):
                print(f"Actions {index}/{len(selected)}; retrieved {sum(m['status']=='retrieved' for m in responses.values())}", flush=True)
    sections, entries, unexplained, page_rows = [], [], [], []
    for action in actions:
        meta = responses.get(action["action_url"], {"status": "not_attempted_run_limit"})
        page_row = {**action, "fetch_status": meta["status"], "source_path": meta.get("source_path", ""),
                    "body_hash": meta.get("body_hash", ""), "release_date": "", "body_present": False,
                    "extraction_status": "not_extracted", "explicit_eth_rows": 0, "unclassified_hex_count": 0}
        if meta["status"] == "retrieved":
            parsed = parse_action(get_raw(meta))
            page_row.update({"release_date": parsed["release_date"], "body_present": parsed["body_present"],
                             "extraction_status": "machine_parsed_pending_adjudication" if parsed["body_present"] else "body_missing_manual_review",
                             "explicit_eth_rows": len(parsed["entries"]), "unclassified_hex_count": len(parsed["unclassified_hex_strings"])})
            common = {"action_slug": action["action_slug"], "action_url": action["action_url"],
                      "date_candidate": action["date_candidate"], "release_date": parsed["release_date"],
                      "source_path": meta["source_path"], "body_hash": meta["body_hash"]}
            sections.extend({**common, **row} for row in parsed["sections"])
            entries.extend({**common, **row} for row in parsed["entries"])
            unexplained.extend({**common, "hex_string": address, "status": "chain_and_context_unclassified"}
                               for address in parsed["unclassified_hex_strings"])
        page_rows.append(page_row)
    months = []
    for year in years:
        yr = next(row for row in year_rows if row["year"] == year)
        hist = next((row for row in archive_rows if row["year"] == year), {})
        for month in range(1, 13):
            label = f"{year}-{month:02d}"
            pages = [row for row in page_rows if row["date_candidate"].startswith(label)]
            listing_dates = {row["date_candidate"] for row in pages}
            hist_dates = {d for d in hist.get("dates", []) if d.startswith(label)}
            missing = sorted(hist_dates - listing_dates)
            months.append({"month": label, "year_listing_status": yr["listing_status"],
                           "enumerated_action_urls": len(pages), "retrieved_action_pages": sum(r["fetch_status"] == "retrieved" for r in pages),
                           "body_parsed_pages": sum(r["body_present"] for r in pages),
                           "annual_history_status": hist.get("extraction_status", hist.get("status", "unavailable")),
                           "annual_history_dates": len(hist_dates), "history_dates_without_listing_url": json.dumps(missing),
                           "eligibility_adjudication": "pending", "completeness_claim": "listing_enumeration_only_not_target_frame_gold"})
    input_hash = sha(json.dumps(sorted((m.get("url", ""), m.get("body_hash", ""))
                                     for m in [landing] + listing_manifest + archive_rows + list(responses.values())), separators=(",", ":")).encode())
    summary = {"procedure_version": VERSION, "source_input_hash": input_hash, "year_range": years,
               "selection": "All official Recent Actions URLs returned by yearly filters; no keyword, address, outcome or category preselection",
               "listing_years_exhausted": sum(r["listing_status"] == "official_listing_pagination_exhausted" for r in year_rows),
               "enumerated_action_urls": len(actions), "retrieved_action_pages": sum(r["fetch_status"] == "retrieved" for r in page_rows),
               "body_parsed_pages": sum(r["body_present"] for r in page_rows), "unretrieved_action_pages": sum(r["fetch_status"] != "retrieved" for r in page_rows),
               "annual_histories_retrieved": sum(r.get("status") == "retrieved" for r in archive_rows),
               "history_dates_missing_listing_url": sum(len(json.loads(r["history_dates_without_listing_url"])) for r in months),
               "machine_eth_entry_rows": len(entries), "distinct_explicit_eth_addresses": len({r["normalized_address"] for r in entries}),
               "action_pages_with_explicit_eth": len({r["action_slug"] for r in entries}),
               "proposed_action_types": dict(sorted(collections.Counter(r["proposed_action_type"] for r in entries).items())),
               "proposed_list_scopes": dict(sorted(collections.Counter(r["proposed_list_scope"] for r in entries).items())),
               "unclassified_hex_rows": len(unexplained), "independent_human_adjudication": "pending", "human_gold": False,
               "outcome_measurement_executed": False,
               "limits": ["Exhausted pagination establishes the retrieved official listing surface, not absence of unlisted or historically removed actions.",
                          "Annual histories reconcile dated headings only; PDF text extraction and page-date correspondence can be incomplete.",
                          "ETH address/target/action associations are explicit-marker machine proposals requiring independent adjudication; updates may contain old and new records.",
                          "Unclassified pages/strings and failed fetches are retained; no marker is not evidence of no in-scope action."]}
    args.out_dir.mkdir(parents=True, exist_ok=True)
    outputs = {"summary.json": json.dumps(summary, indent=2, sort_keys=True) + "\n",
               "archive_index_manifest.json": json.dumps(landing, indent=2, sort_keys=True) + "\n",
               "listing_manifest.json": json.dumps(listing_manifest, indent=2, sort_keys=True) + "\n",
               "annual_history_manifest.json": json.dumps(archive_rows, indent=2, sort_keys=True) + "\n",
               "year_reconciliation.csv": csv_text(year_rows, ["year", "official_total", "unique_action_urls", "listing_status", "expected_pages", "accepted_pages"]),
               "month_reconciliation.csv": csv_text(months, list(months[0])),
               "action_pages.csv": csv_text(page_rows, list(page_rows[0]) if page_rows else ["action_url", "fetch_status"]),
               "action_sections.csv": csv_text(sections, list(sections[0]) if sections else ["action_slug", "proposed_action_type"]),
               "ethereum_entry_proposals.csv": csv_text(entries, list(entries[0]) if entries else ["action_slug", "address", "status"]),
               "unclassified_hex_strings.csv": csv_text(unexplained, list(unexplained[0]) if unexplained else ["action_slug", "hex_string", "status"])}
    outputs["README.md"] = f"""# Source-first OFAC frame retrieval

Procedure `{VERSION}`; input hash `{input_hash}`.

Enumerated {summary['enumerated_action_urls']} official listing URLs across
{args.start_year}–{args.end_year}, with {summary['listing_years_exhausted']} yearly
pagination traversals reconciled to the official displayed totals. Retrieved
{summary['retrieved_action_pages']} action pages and {summary['annual_histories_retrieved']}
annual SDN histories. {summary['history_dates_missing_listing_url']} parsed annual-history
dates have no enumerated Recent Actions URL. See `year_reconciliation.csv` and
`month_reconciliation.csv` for the exact check scope and incomplete states.

There are {summary['machine_eth_entry_rows']} explicit-marker ETH entry proposals,
{summary['distinct_explicit_eth_addresses']} distinct ETH addresses and
{summary['action_pages_with_explicit_eth']} associated action pages. These are source
entry counts: aliases, old/new update entries, and same-day additions/removals can
repeat an address. They are **not counts of adjudicated targets or censorship events**.

Source enumeration does not preselect crypto keywords or observed reactions.
All pages and unresolved strings remain in the outputs. Target/action/list-scope
associations are machine proposals, with independent adjudication pending. No
human gold or operator outcome measurements have been created. Pagination
exhaustion establishes the captured official listing, not absence of unlisted or
historically removed actions, and annual-history reconciliation is date-level only.

Raw sources, hashes and retrieval-attempt logs are under `sources/validation_frame/`.
Rebuild using `python scripts/build_validation_frame.py --offline`; resume retrieval
without `--offline`. See `docs/validation-frame-retrieval.md` for protocol and limits.
"""
    for name, text in outputs.items():
        (args.out_dir / name).write_text(text)
    print(json.dumps(summary, indent=2), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=pathlib.Path, default=ROOT / "sources/validation_frame")
    parser.add_argument("--out-dir", type=pathlib.Path, default=ROOT / "analysis/validation_frame")
    parser.add_argument("--start-year", type=int, default=2022)
    parser.add_argument("--end-year", type=int, default=2025)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--interval", type=float, default=0.4, help="Minimum global interval between request starts (seconds)")
    parser.add_argument("--max-action-pages", type=int, help="Optional deterministic run bound; unattempted URLs remain in output")
    parser.add_argument("--offline", action="store_true", help="Rebuild only from hash-verified cached responses")
    args = parser.parse_args()
    if not 1 <= args.workers <= 4 or args.interval < 0.25:
        parser.error("Use 1..4 workers and interval >= 0.25 seconds")
    if args.start_year > args.end_year:
        parser.error("Start year must not follow end year")
    run(args)


if __name__ == "__main__":
    main()
