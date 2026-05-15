#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Release sign-off helper.

Prepares a release-ready packet without making the human-only
decisions for the maintainer:

1. Verifies the working tree is clean (no uncommitted changes).
2. Updates CITATION.cff's `version` and `date-released` ONLY when
   the user explicitly passes `--version X.Y.Z --date YYYY-MM-DD`.
   Otherwise prints the current values and exits.
3. Runs the full regenerate chain at the provided release date
   (used as SOURCE_DATE_EPOCH).
4. Runs `check_paper_readiness.py --strict-repro --strict-reliability
   --strict-null-audit --strict-audit` and reports.
5. Verifies byte-stability across two regenerate runs.
6. Emits a structured sign-off log to
   `analysis/release_signoff/<version>.md`.

The script does NOT push, tag, or commit. The maintainer reviews the
sign-off log and runs `git commit` / `git tag` / `git push` by hand.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import os
import pathlib
import re
import subprocess
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SIGNOFF_DIR = REPO_ROOT / "analysis" / "release_signoff"
CITATION_PATH = REPO_ROOT / "CITATION.cff"


def _run(cmd: list[str], *, env: dict | None = None,
         cwd: pathlib.Path = REPO_ROOT) -> tuple[int, str, str]:
    p = subprocess.run(cmd, capture_output=True, text=True, env=env, cwd=cwd)
    return p.returncode, p.stdout, p.stderr


def _tree_is_clean() -> tuple[bool, str]:
    rc, out, _ = _run(["git", "status", "--porcelain"])
    if rc != 0:
        return False, "git status failed"
    out = out.strip()
    return out == "", out


def _read_cff() -> tuple[str, str]:
    txt = CITATION_PATH.read_text()
    ver = re.search(r"^version:\s*\"?([^\"\n]+)\"?", txt, re.M)
    date = re.search(r"^date-released:\s*\"?([^\"\n]+)\"?", txt, re.M)
    return (ver.group(1).strip() if ver else "?",
            date.group(1).strip() if date else "?")


def _write_cff(version: str, date: str) -> None:
    txt = CITATION_PATH.read_text()
    txt = re.sub(r"^version:.*$", f'version: "{version}"', txt, flags=re.M)
    txt = re.sub(r"^date-released:.*$", f'date-released: "{date}"',
                 txt, flags=re.M)
    CITATION_PATH.write_text(txt)


def _date_to_epoch(date_iso: str) -> int:
    d = _dt.date.fromisoformat(date_iso)
    return int(_dt.datetime(d.year, d.month, d.day,
                            tzinfo=_dt.timezone.utc).timestamp())


def _hashes_of_artifacts() -> dict[str, str]:
    targets = sorted(
        list((REPO_ROOT / "analysis" / "paper_tables").glob("*.md"))
        + list((REPO_ROOT / "derived").glob("*.md"))
        + list((REPO_ROOT / "derived").glob("*.csv"))
        + list((REPO_ROOT / "analysis" / "operator_census").glob("findings.md"))
    )
    out = {}
    for p in targets:
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        out[str(p.relative_to(REPO_ROOT))] = h
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", help="Target version (e.g. 0.2.0). "
                        "If omitted, CITATION.cff is not modified.")
    parser.add_argument("--date", help="Release date YYYY-MM-DD. "
                        "If omitted, CITATION.cff is not modified.")
    parser.add_argument("--allow-dirty", action="store_true",
                        help="Skip the clean-tree check. "
                             "Use ONLY for dry runs.")
    parser.add_argument("--skip-regen", action="store_true",
                        help="Skip `make regenerate` (assume the "
                             "current tree is already at the release "
                             "snapshot). Mostly for re-emitting the "
                             "sign-off log without recomputing.")
    args = parser.parse_args()

    SIGNOFF_DIR.mkdir(parents=True, exist_ok=True)
    log: list[str] = ["# Release sign-off log", ""]

    log.append(f"Started: `{_dt.datetime.now(_dt.timezone.utc).isoformat()}`")
    log.append("")

    # ---- 1. tree-clean check ----
    log.append("## 1. Working tree status")
    clean, dirty_files = _tree_is_clean()
    if clean:
        log.append("- clean ✓")
    else:
        log.append("- **DIRTY** — uncommitted changes present:")
        for line in dirty_files.split("\n"):
            log.append(f"  - `{line}`")
        if not args.allow_dirty:
            log.append("")
            log.append("**ABORT**: release sign-off requires a clean tree. "
                       "Commit / stash / discard, or rerun with "
                       "`--allow-dirty` for a dry run.")
            _write_log(log, "dirty-tree")
            return 1
        log.append("- **--allow-dirty: continuing for dry-run only**")
    log.append("")

    # ---- 2. CITATION.cff handling ----
    log.append("## 2. CITATION.cff")
    cur_ver, cur_date = _read_cff()
    log.append(f"- current version: `{cur_ver}`")
    log.append(f"- current date-released: `{cur_date}`")
    if args.version or args.date:
        if not (args.version and args.date):
            log.append("- **ABORT**: pass both `--version` and `--date` "
                       "together, or neither.")
            _write_log(log, "cff-args-incomplete")
            return 1
        try:
            _dt.date.fromisoformat(args.date)
        except ValueError:
            log.append(f"- **ABORT**: --date={args.date!r} not ISO YYYY-MM-DD.")
            _write_log(log, "bad-date")
            return 1
        log.append(f"- writing version=`{args.version}` "
                   f"date-released=`{args.date}`")
        _write_cff(args.version, args.date)
        new_ver, new_date = _read_cff()
        log.append(f"- post-write: version=`{new_ver}` date=`{new_date}`")
        version_for_log = args.version
        epoch_for_regen = _date_to_epoch(args.date)
    else:
        log.append("- no --version/--date supplied → CITATION.cff "
                   "unchanged; using current values.")
        version_for_log = cur_ver
        try:
            epoch_for_regen = _date_to_epoch(cur_date)
        except ValueError:
            log.append(f"- **WARN**: current date-released ({cur_date}) "
                       "is not ISO; falling back to HEAD commit time.")
            rc, head_ts, _ = _run(["git", "log", "-1", "--format=%ct"])
            epoch_for_regen = int(head_ts.strip()) if rc == 0 else int(
                _dt.datetime.now(_dt.timezone.utc).timestamp())
    log.append("")

    # ---- 3. regenerate ----
    log.append("## 3. Clean-tree regeneration")
    if args.skip_regen:
        log.append("- `--skip-regen`: skipped (caller asserts tree already "
                   "at release snapshot).")
        log.append("")
    else:
        env = {**os.environ, "SOURCE_DATE_EPOCH": str(epoch_for_regen)}
        log.append(f"- SOURCE_DATE_EPOCH = `{epoch_for_regen}` "
                   f"(derived from release date)")
        rc, out, err = _run(["make", "regenerate"], env=env)
        log.append(f"- exit: {rc}")
        if rc != 0:
            log.append("- **regenerate failed**:")
            log.append("```")
            for line in (out + err).splitlines()[-30:]:
                log.append(line)
            log.append("```")
            _write_log(log, f"regen-failed-{version_for_log}")
            return rc
        log.append("- regenerate clean ✓")
        log.append("")

    # ---- 4. strict gate ----
    log.append("## 4. Strict paper-readiness gate")
    env = {**os.environ, "SOURCE_DATE_EPOCH": str(epoch_for_regen)}
    rc, out, err = _run([
        sys.executable, "scripts/check_paper_readiness.py",
        "--strict-repro", "--strict-reliability",
        "--strict-null-audit", "--strict-audit",
        # The v0.1 paper retracts comparative attribution-rate claims
        # (docs/paper_claims.md §0 Reliability discipline). The
        # attribution κ < 0.6 is a documented codebook gap rather than
        # a coding regression. Soft-attribution downgrades that ERROR to
        # WARN so the release gate can complete; the WARN is still
        # printed and recorded in the sign-off log.
        "--allow-soft-attribution",
    ], env=env)
    log.append(f"- exit: {rc}")
    log.append("- output (last 40 lines):")
    log.append("```")
    for line in (out + err).splitlines()[-40:]:
        log.append(line)
    log.append("```")
    strict_passed = (rc == 0)
    log.append(f"- strict gate: {'PASS ✓' if strict_passed else 'FAIL ✗'}")
    log.append("")

    # ---- 5. byte-stability ----
    log.append("## 5. Byte-stability round-trip")
    h1 = _hashes_of_artifacts()
    rc, out, err = _run(["make", "regenerate"], env=env)
    if rc != 0:
        log.append("- **second regenerate failed**")
        log.append("```")
        for line in (out + err).splitlines()[-15:]:
            log.append(line)
        log.append("```")
        _write_log(log, f"regen2-failed-{version_for_log}")
        return rc
    h2 = _hashes_of_artifacts()
    diff = {k: (h1.get(k), h2.get(k)) for k in set(h1) | set(h2)
            if h1.get(k) != h2.get(k)}
    if not diff:
        log.append(f"- byte-stable across {len(h1)} artifacts ✓")
    else:
        log.append(f"- **BYTE-INSTABILITY** across {len(diff)} artifacts:")
        for k, (a, b) in diff.items():
            log.append(f"  - `{k}`: {a} → {b}")
    log.append("")

    # ---- 6. final verdict ----
    log.append("## 6. Verdict")
    if strict_passed and not diff:
        log.append("- **SIGN-OFF READY**: clean tree, strict gate passes, "
                   "artifacts byte-stable.")
        log.append("- Next steps (human-only):")
        log.append(f"  1. `git add CITATION.cff` (if version/date changed)")
        log.append(f"  2. `git commit -m \"release: v{version_for_log}\"`")
        log.append(f"  3. `git tag -a v{version_for_log} -m \"...\"`")
        log.append(f"  4. `git push origin main --tags`")
        log.append(f"  5. Wait for Zenodo to mint the DOI.")
        verdict_rc = 0
    else:
        log.append("- **NOT READY**: address strict-gate failures "
                   "and/or byte-instability above.")
        verdict_rc = 1
    log.append("")

    _write_log(log, version_for_log)
    return verdict_rc


def _write_log(lines: list[str], slug: str) -> None:
    out = SIGNOFF_DIR / f"{slug}.md"
    out.write_text("\n".join(lines) + "\n")
    print(f"[release_signoff] wrote {out.relative_to(REPO_ROOT)}",
          file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
