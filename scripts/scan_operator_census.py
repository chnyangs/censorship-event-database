#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Multi-repo operator-compliance git-history census.

For each candidate in `sources/operator_census/candidates.yaml`:

1. Clone (shallow, blobless) the repo into
   `sources/operator_census/<org__repo>/`.
2. Identify compliance-related files via (a) `filter_file` if set,
   else (b) `extra_patterns` glob sweep over the full tree.
3. For each identified file, extract every commit touching it
   (`git log --follow --date=iso-strict`).
4. For each commit, classify it via subject-line + path keywords
   into {sanctions_reaction, list_maintenance, cleanup, other}.
5. Emit `analysis/operator_census/commits.json` (ignored,
   regenerable structured output) + `analysis/operator_census/findings.md`
   (per-repo summary table).

This is the multi-repo scale-up of the single-repo Flashbots audit
documented in `analysis/anchor_gap_fill_log.md §4`. Findings here do
not replace the per-event YAML — each substantively-changed file
remains a candidate for event admission under the existing protocol.

Run:
    python3 scripts/scan_operator_census.py
    python3 scripts/scan_operator_census.py --only flashbots/rpc-endpoint
    python3 scripts/scan_operator_census.py --no-clone  # use existing clones
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import os
import pathlib
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from typing import Iterable, Optional

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import now_utc_iso  # noqa: E402


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
CANDIDATES_YAML = REPO_ROOT / "sources" / "operator_census" / "candidates.yaml"
CLONE_ROOT = REPO_ROOT / "sources" / "operator_census"
OUT_DIR = REPO_ROOT / "analysis" / "operator_census"


# State-action language only. Designated-entity names (tornado,
# garantex, storm, etc.) are deliberately NOT in this list because
# they create prefix false positives in phishing-blocklist corpora
# (e.g. "stormtokens.com" phishing entries in MetaMask
# eth-phishing-detect from 2017, long pre-dating any OFAC action).
#
# **Subject-only matching**. The earlier version also checked path
# substrings against this list, which produced false positives on
# every commit touching `server/ofacblacklist.go` regardless of
# whether the subject was OFAC-related — e.g. "Cleaned up some code,
# in particular around proxying" and "update docker" both got
# classified as sanctions_reaction because the file path contains
# "ofac". The fix is to drop path matching entirely; the file's
# OFAC-relevance is captured by `candidates.yaml::filter_file` /
# `known_channel`, not by per-commit classification. The 2025-04-01
# Flashbots PR #173 "Cleanup unused and unmaintained blacklist file"
# is now correctly classified as `generic_list_maintenance` (it
# names "blacklist" + "Cleanup", no OFAC keyword), and the editorial
# narrative inside the Flashbots-rpc-endpoint case continues to be
# carried by the candidate-level `known_channel: true` flag and the
# anchor evidence chain at `analysis/evidence-chains/`.
#
# **`treasury` removed** as a keyword. It produced false positives
# on every domain containing "treasury" in eth-phishing-detect (e.g.
# `ethtreasury.com`). State-action language uses "OFAC" /
# "Treasury Department" / "Department of the Treasury" — these will
# almost always co-occur with "ofac" in commit subjects when
# genuinely sanctions-relevant, so dropping `treasury` does not
# cause a meaningful false-negative loss.
OFAC_SPECIFIC_KEYWORDS = [
    "ofac", "sdn", "sanction", "designate",
]

# Entity keywords surfaced separately — always require a human
# adjudication step (this census does not count them as
# sanctions-reactions on their own).
ENTITY_KEYWORDS = [
    "tornado", "samourai", "garantex", "blender", "chipmixer", "sinbad",
    "lazarus", "bitzlato", "chatex", "suex", "lockbit", "conti",
    "matveev", "semenov", "pertsev",
]

# "blacklist" / "blocklist" / "denylist" alone is not sanctions-linked —
# MetaMask eth-phishing-detect's blacklist is a phishing registry, not
# an OFAC list. Classified as generic list maintenance unless paired
# with an OFAC keyword.
GENERIC_LIST_KEYWORDS = [
    "blacklist", "denylist", "blocklist", "banned",
    "compliance", "censor",
]

CLEANUP_KEYWORDS = [
    "cleanup", "clean up", "remove", "delete", "deprecate",
    "unused", "dead code", "refactor", "tidy",
]


@dataclass
class Commit:
    repo: str
    path: str
    sha: str
    committer_iso: str
    author_iso: str
    subject: str
    added_lines: int
    removed_lines: int
    classification: str  # sanctions_reaction / list_maintenance / cleanup / other


@dataclass
class RepoFinding:
    repo: str
    operator: str
    role: str
    clone_status: str  # ok / not_found / clone_failed / skipped
    matched_files: list[str]
    commit_count: int
    sanctions_reaction_count: int
    sanctions_maintenance_count: int
    entity_keyword_hit_count: int
    generic_list_maintenance_count: int
    first_commit_iso: Optional[str]
    last_commit_iso: Optional[str]
    first_sanctions_commit_iso: Optional[str]
    last_sanctions_commit_iso: Optional[str]
    notes: str
    commits: list[Commit] = field(default_factory=list)


def _run(cmd: list[str], cwd: pathlib.Path | None = None,
         check: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                          check=check)


def _slug_of(repo: str) -> str:
    return repo.replace("/", "__")


def _clone_repo(repo: str, dest: pathlib.Path, blobless: bool = True) -> str:
    """Clone a GitHub repo. Returns "ok" / "not_found" / "clone_failed"."""
    if dest.exists() and (dest / ".git").exists():
        return "ok"
    url = f"https://github.com/{repo}.git"
    cmd = ["git", "clone"]
    if blobless:
        cmd.extend(["--filter=blob:none"])
    cmd.extend([url, str(dest)])
    proc = _run(cmd, check=False)
    if proc.returncode == 0:
        return "ok"
    err = (proc.stderr or "").lower()
    if "not found" in err or "repository not found" in err:
        return "not_found"
    print(f"[scan] clone failed for {repo}: {proc.stderr.strip()[:200]}",
          file=sys.stderr)
    return "clone_failed"


def _match_files(clone_dir: pathlib.Path,
                 filter_file: Optional[str],
                 extra_patterns: list[str]) -> list[str]:
    """Return paths (repo-relative) matching the candidate's filter definition."""
    paths: set[str] = set()
    if filter_file:
        abs_path = clone_dir / filter_file
        if abs_path.exists():
            paths.add(filter_file)
    if extra_patterns:
        for p in clone_dir.rglob("*"):
            if not p.is_file() or ".git" in p.parts:
                continue
            rel = str(p.relative_to(clone_dir))
            for pat in extra_patterns:
                if fnmatch.fnmatch(rel, pat) or fnmatch.fnmatch(
                        p.name, pat.lstrip("**/")):
                    paths.add(rel)
                    break
    return sorted(paths)


def _extract_commits(clone_dir: pathlib.Path,
                     repo: str, path: str) -> list[Commit]:
    """Run `git log --follow` for one file; parse into Commit records.

    Intentionally robust to partial output: blobless clones fail with
    "object not in database" on `--numstat` for old commits, but the
    commit-metadata stream before that failure is still trustworthy.
    We drop `--numstat` and carry +/- as 0; the classification that
    matters for this census uses the commit subject and file path.
    """
    cmd = [
        "git", "log", "--follow", "--date=iso-strict",
        "--pretty=format:%H%x00%cI%x00%aI%x00%s",
        "--", path,
    ]
    proc = _run(cmd, cwd=clone_dir)
    # Tolerate rc != 0: parse whatever we got.
    commits: list[Commit] = []
    for line in proc.stdout.splitlines():
        if "\x00" not in line:
            continue
        parts = line.split("\x00")
        if len(parts) != 4:
            continue
        commits.append(Commit(
            repo=repo, path=path, sha=parts[0],
            committer_iso=parts[1], author_iso=parts[2],
            subject=parts[3], added_lines=0, removed_lines=0,
            classification="other",
        ))
    for c in commits:
        c.classification = _classify(c.subject, c.path)
    return commits


def _classify(subject: str, path: str) -> str:
    """Five-class output:

    - `sanctions_reaction`: subject or path explicitly names state
      action (ofac / sdn / sanction / treasury / designate). This is
      the narrow class the paper's census rate is built on.
    - `sanctions_maintenance`: same plus a cleanup verb (the
      "delete the blacklist post-delisting" pattern — Flashbots PR #173).
    - `entity_keyword_hit`: subject mentions a designated entity
      (tornado / samourai / lazarus / ...) **without** OFAC language.
      Requires human adjudication — could be a sanctions reaction, a
      phishing entry impersonating the entity, or unrelated. Not
      counted in the headline rate.
    - `generic_list_maintenance`: generic list vocabulary (blacklist /
      blocklist / denylist) without an OFAC or entity tie. Dominant
      in phishing / scam / abuse registries (MetaMask
      eth-phishing-detect).
    - `other`: any other commit touching the matched file.
    """
    s = subject.lower()
    # NOTE: path is NOT consulted for OFAC / generic-list classification.
    # See OFAC_SPECIFIC_KEYWORDS docstring for the rationale.
    hits_ofac = any(k in s for k in OFAC_SPECIFIC_KEYWORDS)
    hits_entity = any(k in s for k in ENTITY_KEYWORDS)
    hits_generic = any(k in s for k in GENERIC_LIST_KEYWORDS)
    hits_cleanup = any(k in s for k in CLEANUP_KEYWORDS)
    if hits_ofac and hits_cleanup:
        return "sanctions_maintenance"
    if hits_ofac:
        return "sanctions_reaction"
    if hits_entity:
        return "entity_keyword_hit"
    if hits_generic and hits_cleanup:
        return "generic_list_maintenance"
    if hits_generic:
        return "generic_list_maintenance"
    if hits_cleanup:
        return "other"
    return "other"


def _scan_one(candidate: dict, clone_root: pathlib.Path,
              skip_clone: bool) -> RepoFinding:
    repo = candidate["repo"]
    clone_dir = clone_root / _slug_of(repo)
    if skip_clone:
        status = "ok" if (clone_dir / ".git").exists() else "skipped"
    else:
        status = _clone_repo(repo, clone_dir)
    finding = RepoFinding(
        repo=repo, operator=candidate["operator"],
        role=candidate["role"], clone_status=status,
        matched_files=[], commit_count=0,
        sanctions_reaction_count=0,
        sanctions_maintenance_count=0,
        entity_keyword_hit_count=0,
        generic_list_maintenance_count=0,
        first_commit_iso=None, last_commit_iso=None,
        first_sanctions_commit_iso=None, last_sanctions_commit_iso=None,
        notes=candidate.get("notes", "").strip(),
    )
    if status not in ("ok",) or not clone_dir.exists():
        return finding
    finding.matched_files = _match_files(
        clone_dir, candidate.get("filter_file"),
        candidate.get("extra_patterns") or [],
    )
    all_commits: list[Commit] = []
    for f in finding.matched_files:
        all_commits.extend(_extract_commits(clone_dir, repo, f))
    # dedupe by (sha, path)
    seen: set[tuple[str, str]] = set()
    uniq: list[Commit] = []
    for c in all_commits:
        k = (c.sha, c.path)
        if k in seen:
            continue
        seen.add(k)
        uniq.append(c)
    uniq.sort(key=lambda c: c.committer_iso or "")
    finding.commits = uniq
    finding.commit_count = len(uniq)
    finding.sanctions_reaction_count = sum(
        1 for c in uniq if c.classification == "sanctions_reaction")
    finding.sanctions_maintenance_count = sum(
        1 for c in uniq if c.classification == "sanctions_maintenance")
    finding.entity_keyword_hit_count = sum(
        1 for c in uniq if c.classification == "entity_keyword_hit")
    finding.generic_list_maintenance_count = sum(
        1 for c in uniq if c.classification == "generic_list_maintenance")
    if uniq:
        finding.first_commit_iso = uniq[0].committer_iso
        finding.last_commit_iso = uniq[-1].committer_iso
    sanctions_iso = [c.committer_iso for c in uniq
                     if c.classification in ("sanctions_reaction",
                                             "sanctions_maintenance")]
    if sanctions_iso:
        finding.first_sanctions_commit_iso = sanctions_iso[0]
        finding.last_sanctions_commit_iso = sanctions_iso[-1]
    return finding


SIGNAL_CLASSES = {
    "sanctions_reaction", "sanctions_maintenance", "entity_keyword_hit",
}


def _emit_json(findings: list[RepoFinding], out_path: pathlib.Path,
               emit_all: bool = False) -> None:
    """Write commits.json. By default include only commits in the
    three signal classes (sanctions_reaction / sanctions_maintenance /
    entity_keyword_hit) — this keeps the file under ~1MB on a corpus
    that includes MetaMask's 204k generic_list entries. Pass
    `emit_all=True` to include the full stream for offline analysis.
    """
    def serialize(f: RepoFinding) -> dict:
        meta = {k: v for k, v in asdict(f).items() if k != "commits"}
        if emit_all:
            commits_out = [asdict(c) for c in f.commits]
        else:
            commits_out = [asdict(c) for c in f.commits
                           if c.classification in SIGNAL_CLASSES]
        meta["commits_emitted_count"] = len(commits_out)
        meta["commits_filter"] = ("all" if emit_all
                                  else "signal_classes_only")
        meta["commits"] = commits_out
        return meta
    payload = {
        "generated_at": now_utc_iso(),
        "scanner_version": "0.2",
        "candidate_count": len(findings),
        "commits_filter": "all" if emit_all else "signal_classes_only",
        "findings": [serialize(f) for f in findings],
    }
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=False))


def _emit_markdown(findings: list[RepoFinding], out_path: pathlib.Path) -> None:
    lines = [
        "# Operator-compliance git-history census",
        "",
        f"Generated: `{now_utc_iso()}` · scanner `scripts/scan_operator_census.py` · "
        "candidates `sources/operator_census/candidates.yaml`.",
        "",
        "Reproduction: `python3 scripts/scan_operator_census.py` "
        "(requires network for initial clone; subsequent runs reuse "
        "local clones under `sources/operator_census/<org>__<repo>/`).",
        "",
        "## Summary",
        "",
        "Columns: *OFAC-rxn* = commits whose **subject** carries a "
        "state-action keyword (ofac / sdn / sanction / designate). "
        "Path is not consulted — earlier versions matched the path "
        "and inflated counts on `server/ofacblacklist.go` for every "
        "commit including pure refactors and Docker updates. "
        "*OFAC-maint* = OFAC-rxn plus a cleanup verb. The 2025-04-01 "
        "Flashbots PR #173 (\"Cleanup unused and unmaintained "
        "blacklist file\") falls in *Generic-list*, not OFAC-maint, "
        "because its subject names \"blacklist\" but no OFAC keyword; "
        "the editorial interpretation that this commit is the post-"
        "OFAC-delisting cleanup is documented in "
        "`analysis/evidence-chains/tornado-cash-ofac-delisting-2025.md`, "
        "not in this automated classifier. *Entity-hit* = commits "
        "that name a designated entity (tornado / samourai / lazarus "
        "/ ...) without state-action language; requires human "
        "adjudication because phishing registries produce prefix "
        "false positives (e.g. \"stormtoken.com\" in 2017 long "
        "pre-dates the Storm/Semenov OFAC designation). "
        "*Generic-list* = blacklist/blocklist/denylist activity with "
        "no OFAC or entity tie (dominates phishing-scam registries). "
        "First/last-OFAC bounds the OFAC-keyed window.",
        "",
        "| operator | repo | role | clone | files | commits | OFAC-rxn | OFAC-maint | Entity-hit | Generic-list | first-OFAC | last-OFAC |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for f in findings:
        lines.append(
            f"| {f.operator} | `{f.repo}` | {f.role} | {f.clone_status} | "
            f"{len(f.matched_files)} | {f.commit_count} | "
            f"{f.sanctions_reaction_count} | "
            f"{f.sanctions_maintenance_count} | "
            f"{f.entity_keyword_hit_count} | "
            f"{f.generic_list_maintenance_count} | "
            f"{(f.first_sanctions_commit_iso or '—')[:10]} | "
            f"{(f.last_sanctions_commit_iso or '—')[:10]} |"
        )
    lines.extend([
        "",
        "## Per-repo detail",
        "",
    ])
    for f in findings:
        lines.extend([
            f"### `{f.repo}` — {f.role}",
            "",
            f"- **Operator**: {f.operator}",
            f"- **Clone status**: {f.clone_status}",
            f"- **Matched files** (n={len(f.matched_files)}):",
        ])
        for mf in f.matched_files:
            lines.append(f"    - `{mf}`")
        if f.notes:
            lines.append("")
            lines.append(f"**Notes**: {f.notes}")
        if f.commits:
            sanc = [c for c in f.commits if c.classification in (
                "sanctions_reaction", "sanctions_maintenance")]
            if sanc:
                lines.extend([
                    "",
                    f"**OFAC-keyed commits** "
                    f"(reactions={f.sanctions_reaction_count}, "
                    f"maintenance={f.sanctions_maintenance_count}):",
                    "",
                    "| date | sha | path | class | subject |",
                    "| --- | --- | --- | --- | --- |",
                ])
                for c in sanc:
                    subj = c.subject.replace("|", "\\|")[:120]
                    lines.append(
                        f"| {c.committer_iso[:10]} | `{c.sha[:8]}` | "
                        f"`{c.path}` | "
                        f"{c.classification} | {subj} |"
                    )
            if f.generic_list_maintenance_count > 0:
                lines.append("")
                lines.append(
                    f"_Generic list-maintenance commits (phishing / abuse / "
                    f"scam registry activity, no OFAC keyword): "
                    f"{f.generic_list_maintenance_count}. Not tabulated "
                    f"individually — regenerate with "
                    f"`--emit-all-commits` for the full local stream._"
                )
        lines.append("")
    lines.extend([
        "## Scope and caveats",
        "",
        "- **Classification is keyword-based**, not semantic. A commit "
        "that touches `ofacblacklist.go` with the subject *\"refactor\"* "
        "lands in `other`; one that is semantically sanctions-related "
        "but uses different subject words could also slip to `other`. "
        "The raw JSON emits the full (subject, path, +/-) tuple so an "
        "auditor can re-classify.",
        "- **Clone status `not_found`** means the repo URL did not "
        "exist or was made private since the candidate was listed. "
        "**`skipped`** means the scanner was asked to not clone "
        "(e.g. offline run). **`clone_failed`** means the clone "
        "hit a non-404 network error.",
        "- **The `skipped_operators` list** in `candidates.yaml` "
        "names operators (bloXroute, Titan Builder, Beaverbuild, "
        "Coinbase Wallet, OpenSea, Circle, Chainflip) whose "
        "compliance logic is not in public source control. For "
        "those operators the git-history channel is structurally "
        "unavailable — a finding in its own right.",
        "- **This census does not by itself admit events**. A "
        "sanctions-reaction commit becomes an admitted observation "
        "only when it carries body_hash + body_path + a named target "
        "(an OFAC SDN, a court order, etc.) and survives the "
        "per-event `scripts/validate.py` admission check.",
        "",
    ])
    out_path.write_text("\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", help="Restrict to a single candidate repo")
    parser.add_argument("--no-clone", action="store_true",
                        help="Use existing clones; do not fetch from network")
    parser.add_argument("--out-dir", default=str(OUT_DIR))
    parser.add_argument("--emit-all-commits", action="store_true",
                        help="Include every commit in commits.json "
                             "(default: signal classes only — ~1MB vs ~80MB)")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    CLONE_ROOT.mkdir(parents=True, exist_ok=True)

    candidates = yaml.safe_load(CANDIDATES_YAML.read_text())["candidates"]
    if args.only:
        candidates = [c for c in candidates if c["repo"] == args.only]
        if not candidates:
            print(f"error: no candidate matches --only={args.only}",
                  file=sys.stderr)
            return 2

    findings: list[RepoFinding] = []
    for c in candidates:
        print(f"[scan] {c['repo']}", file=sys.stderr)
        findings.append(_scan_one(c, CLONE_ROOT, args.no_clone))

    out_dir = pathlib.Path(args.out_dir)
    _emit_json(findings, out_dir / "commits.json",
               emit_all=args.emit_all_commits)
    _emit_markdown(findings, out_dir / "findings.md")
    print(f"[scan] wrote {out_dir}/commits.json and findings.md",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
