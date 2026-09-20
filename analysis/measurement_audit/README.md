# Measurement semantics audit

Automated screen completed; human adjudication has NOT started. Procedure `1.0.0`.
Input hash: `sha256:b463a656dd1e3a0013599b064430c4c19576a0f69f368cf920b38855f129f911`. Counts come from source YAML, not `dataset.json`.

The admitted corpus has 398 events and 2388 possible layer cells;
1831 cells retain the legacy N/A label. Of 107 legacy null events,
103 reuse at least one trigger source URL or body hash.
There are 108 overlapping no-change observations
out of 118 no-change observations.
These are **audit flags, not counts of false observations**. Source reuse can be valid.
The N/A screen flags 102 admitted coverage notes using
lexical evidence-absence patterns; both false positives and false negatives are possible.

`summary.json` separates all registry records from admitted records. The three
queues retain event status, zero-based row indices, source YAML paths and retrieval
identifiers. No event, legacy label, admission state or human-review stamp is changed.

## Independent review packet

Distribute `human_review/reviewer_a.csv` only to reviewer A and
`human_review/reviewer_b.csv` only to reviewer B, together with the raw source files
and `docs/two-arm-validation-protocol.md`. Each contains 2388
event-layer items; every response cell is blank. Reviewers independently derive a
supported claim from the supplied sources rather than seeing the previous answer.
Do not give reviewers this audit report, risk queues, the other reviewer sheet, or
`human_review/sealed_key.csv` before both sheets are locked. The key is coordinator-only
**plain text**, not encrypted; directory separation alone does not enforce blinding.
Labels, legacy claims, author notes and links to event YAML are omitted from reviewer
sheets. Source paths/target identities and the old collection's source availability
remain visible: this is label blinding, not fully independent evidence collection.

`source_entailment` is the reviewer's finding about what the bundle establishes,
not an answer prefilled by an agent. Response definitions and adjudication steps are
in the protocol. No empty, automated or agent-authored sheet counts as human gold.
Use a separate output directory for each new corpus snapshot. Regeneration refuses
to overwrite reviewer sheets whose bytes differ from the generated blank templates.

## Reproduce

Run `python scripts/audit_measurement_semantics.py` from the repository root.
The bounded validation cohort in the protocol is **NOT EXECUTED**; this retrospective
screen does not establish sampling-frame completeness or measurement validity.
