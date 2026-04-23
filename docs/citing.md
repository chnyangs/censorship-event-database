# Citing this dataset

The authoritative record is [`CITATION.cff`](../CITATION.cff) at the repo
root — GitHub renders a "Cite this repository" button from it, and Zenodo
reads it on each tagged release to populate the deposit metadata. If the
field you need isn't in any of the templates below, pull it from
`CITATION.cff` and you'll be right.

**What should always accompany a citation:**

- the dataset **version** (`CITATION.cff :: version`, also in
  `dataset.meta.json :: dataset_version`), and
- the **cutoff date** (`dataset.meta.json :: cutoff_date`) — the **max** of
  (`last_verified`, `last_human_audit`) across events at the time of the
  snapshot; i.e., the snapshot's upper bound of verification activity.
  See [limitations-and-use.md §2.5](limitations-and-use.md#25-snapshot-decay)
  for the canonical definition.

Both together identify the exact catalog state your claim rests on. For
observation-level quoting, pair them with the `body_hash` from the source
you depended on (see [datasheet.md §5.1](datasheet.md#51-how-to-use-a-specific-observation-in-a-paper--brief)).

Replace `{VERSION}` and `{DOI}` with the release values — until the first
Zenodo deposit is minted, use the version string without a DOI.

## BibTeX

### Whole-dataset citation

```bibtex
@dataset{yang_2026_censorship_event_db,
  author       = {Yang, Xiangwen},
  title        = {Cross-Layer Censorship Event Database},
  year         = 2026,
  version      = {{VERSION}},
  publisher    = {Zenodo},
  doi          = {{DOI}},
  url          = {https://github.com/chnyangs/censorship-event-database},
  note         = {Dataset cutoff: {CUTOFF_DATE}}
}
```

### Citing a specific event

Prefer the whole-dataset citation + an in-text reference to the event slug.
Example:

> As recorded in the Cross-Layer Censorship Event Database (Yang, 2026,
> v0.1.0, event `tornado-cash-ofac-2022`), the first asset-layer reaction
> was observed 5.9 hours after the OFAC designation …

If a venue requires per-event entries (rare), use:

```bibtex
@misc{ccdb_tornado_cash_ofac_2022,
  author       = {Yang, Xiangwen},
  title        = {Event {\texttt{tornado-cash-ofac-2022}}:
                  {Tornado Cash OFAC Designation (2022-08-08)}},
  howpublished = {Cross-Layer Censorship Event Database,
                  event record, version {VERSION}},
  year         = 2026,
  url          = {https://chnyangs.github.io/censorship-event-database/events/tornado-cash-ofac-2022.html}
}
```

## APA (7th)

Yang, X. (2026). *Cross-Layer Censorship Event Database* (Version {VERSION})
\[Data set]. Zenodo. {DOI}
<https://github.com/chnyangs/censorship-event-database> (cutoff date: {CUTOFF_DATE})

## Chicago (Author-Date)

Yang, Xiangwen. 2026. "Cross-Layer Censorship Event Database." Version {VERSION}.
Zenodo. {DOI}. Dataset cutoff: {CUTOFF_DATE}.
<https://github.com/chnyangs/censorship-event-database>.

## MLA (9th)

Yang, Xiangwen. *Cross-Layer Censorship Event Database.* Version {VERSION}, Zenodo,
2026, {DOI}. Dataset cutoff: {CUTOFF_DATE}.

## Plain-text (interview / on-air attribution)

> the Cross-Layer Censorship Event Database, version {VERSION}, maintained
> by Xiangwen Yang and archived on Zenodo

## Citing derived output

### Evidence-chain output

If you reproduce or quote a rendered evidence chain, cite the event record
*and* the tool version printed in the chain's header line, e.g.
`Tool version: 0.1.0`.

### Comparable-case retrieval output

Cite both the dataset and the comparable-case tool version. The output is
**retrieval, not prediction** — see
[limitations-and-use.md](limitations-and-use.md) — so phrasing should be
"structurally similar precedents surfaced by retrieval" rather than
"predicted outcomes" or "expected cascade shape."

## After each release

The release process in [releasing.md](releasing.md) auto-populates the DOI
into Zenodo. As the maintainer, once a DOI is minted, append it to
`CITATION.cff` under the `identifiers:` block so the canonical record
carries it. All templates above use the same placeholder so you only edit
one file.

## When citing pre-release (no DOI yet)

Until the first tagged release exists, cite by the git tag or commit
short-sha in place of the DOI:

> Yang, X. (2026). *Cross-Layer Censorship Event Database* (Version
> {VERSION}, commit `{COMMIT}`) [Data set].
> <https://github.com/chnyangs/censorship-event-database>

The commit hash is persistent on GitHub and gives a readable provenance
anchor until the DOI supersedes it.
