# Source-first OFAC frame retrieval

Procedure `1.0.0`; input hash `sha256:6a5c4de562d43d5bb0860a31dab59b316bd418988b99ec7b040d9b5d4547473a`.

Enumerated 715 official listing URLs across
2022–2025, with 4 yearly
pagination traversals reconciled to the official displayed totals. Retrieved
715 action pages and 4
annual SDN histories. 0 parsed annual-history
dates have no enumerated Recent Actions URL. See `year_reconciliation.csv` and
`month_reconciliation.csv` for the exact check scope and incomplete states.

There are 416 explicit-marker ETH entry proposals,
154 distinct ETH addresses and
28 associated action pages. These are source
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
