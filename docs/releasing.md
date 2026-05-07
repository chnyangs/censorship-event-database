# Releasing a dataset version

This repo's releases exist so external work — papers, briefs, memos,
downstream pipelines — can cite a fixed snapshot with a persistent identifier.
Every tagged release produces:

1. A **GitHub Release** with auto-generated source archives.
2. A **Zenodo deposit** with a DOI (via the Zenodo ↔ GitHub integration).
3. A refreshed `dataset.meta.json` + `dataset.{json,csv}` pinned to the tag.
4. A refreshed `sources/source_manifest.{csv,json,md}` with SHA-256 hashes
   for local source artifacts included in the release surface.

Current version lives in [`CITATION.cff`](../CITATION.cff) under the `version:`
key. `scripts/build_dataset.py` reads that file and bakes the value into
`dataset.meta.json::dataset_version` on every build, so the four places that
mention the version can never drift: `CITATION.cff` → generator → artifacts
→ site footer / evidence-chain / comparable-case reports.

## One-time setup — Zenodo integration

Do this once, before the first tag:

1. Go to <https://zenodo.org/account/settings/github/>. Log in with your
   GitHub account (first time will authorize Zenodo as an OAuth app).
2. Find `chnyangs/censorship-event-database` in the repo list and flip the
   toggle to **On**. Zenodo will now watch for GitHub Release events on this
   repo.
3. (Optional but recommended) Visit <https://zenodo.org/me/> → profile → add
   your ORCID so the DOI metadata includes it.
4. Verify `.zenodo.json` at the repo root — Zenodo reads this on each release
   for deposit metadata (title, description, license, creators, related DOIs).
   The file is already committed; edit only when the authors / license / kw
   set changes.

## Cutting a release

Every release is a **git tag** (GitHub + Zenodo react to the tag event):

```sh
# 1. Decide the version using semver:
#      MAJOR — schema break or backwards-incompatible admission-rule change
#      MINOR — new events, new layers, new framework tool, reproducibility fix
#      PATCH — pure documentation / metadata / typo fix
NEW_VERSION=0.1.1

# 2. Update CITATION.cff
sed -i '' "s/^version:.*/version: \"${NEW_VERSION}\"/" CITATION.cff
sed -i '' "s/^date-released:.*/date-released: \"$(date -u +%Y-%m-%d)\"/" CITATION.cff

# 3. Regenerate dataset artifacts so dataset.meta.json and source_manifest
#    pick up the version.
make regenerate

# 4. Run release gates. The strict reliability gate requires an
#    independent-human IRR report; omit only for non-release working snapshots.
python3 scripts/check_paper_readiness.py --strict-audit --strict-null-audit --strict-repro --strict-reliability

# 5. CHANGELOG entry summarising what's in this version.
$EDITOR CHANGELOG.md

# 6. Commit, tag, push. GitHub Release + Zenodo DOI both fire off the tag.
git add CITATION.cff CHANGELOG.md dataset.json dataset.csv dataset.meta.json \
  derived/ analysis/paper_tables/ analysis/evidence-chains/ site/ \
  sources/source_manifest.* sources/http_captures/ sources/l0_datasets/ \
  docs/ scripts/ tests/ sampling/ candidate_triggers/ events/
git status --short   # review the exact release surface before committing
git commit -m "release: v${NEW_VERSION}"
git tag -a "v${NEW_VERSION}" -m "Release v${NEW_VERSION}"
git push origin main "v${NEW_VERSION}"
```

After the push:

- **GitHub Release** — the workflow or your manual release-notes step creates
  a Release pointing at `v${NEW_VERSION}` on the Releases page.
- **Zenodo** — within a minute or two Zenodo registers the deposit and mints
  a DOI. The DOI is listed on <https://zenodo.org/account/settings/github/>
  under this repo. Update `CITATION.cff` to add the DOI field once it lands:
  ```yaml
  identifiers:
    - type: doi
      value: "10.5281/zenodo.XXXXXXX"
      description: "Archived snapshot of version ${NEW_VERSION}"
  ```
  Commit that as a lightweight fix-up (does not need a new release).

## What NOT to do

- **Don't amend or force-push a released tag.** DOIs are cut against an
  immutable tag commit. A rewritten tag leaves the DOI pointing at a commit
  that no longer exists in the remote's history. If you need a correction,
  release a patch version instead.
- **Don't edit `dataset.meta.json` by hand.** It's regenerated from
  `events/*.yaml` + `CITATION.cff`. Regenerate via `make dataset`.
- **Don't release with a schema_version mismatch across events.** The
  generator raises `SystemExit` if events disagree on `schema_version`; fix
  the drift first.
- **Don't release when `CITATION.cff::date-released` predates
  `dataset.meta.json::cutoff_date`.** The release metadata must describe the
  snapshot it is publishing, not an earlier working draft.

## Releases vs daily working commits

Between releases, `main` keeps moving. `dataset.meta.json::dataset_version`
will keep reading whatever `CITATION.cff` says, which is fine — consumers
who want a frozen snapshot pin to a tagged DOI, not to `main`.
