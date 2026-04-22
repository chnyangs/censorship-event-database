"""Canonical gap-marker vocabularies shared across validate / status / draft-gap tooling.

Three tiers, strictly nested: BLOCKING ⊆ STATUS ⊆ AUTHOR_DRAFT.

Previously validate.py, status_report.py, and draft_gap_report.py each defined
their own list. They diverged: a draft containing "replace Wayback hash" would
fail validate.py but show zero gap markers on the status dashboard, because
status_report's list omitted "replace". This module makes the three tools
agree on the base set and distinguish only by strictness.
"""

# Tier 1 — BLOCKING: placeholder / admission-scaffolding text that must never
# survive into admitted data. Used by validate.py as a hard rule.
BLOCKING: tuple[str, ...] = (
    "placeholder",
    "fill in",
    "example.org",
    "example_actor",
    "example_target",
    "tbd",
    "todo",
    "to be collected",
    "before admission",
    "still to be pinned",
)

# Tier 2 — STATUS: same as BLOCKING. Used by status_report.py for dashboard
# counting. Kept identical to BLOCKING so the two tools can never disagree.
STATUS: tuple[str, ...] = BLOCKING

# Tier 3 — AUTHOR_DRAFT: broader set used only on `status: draft` events by
# draft_gap_report.py to help authors surface unresolved scaffolding prose.
# These extras ("replace", "need ", "requires ") have false-positive potential
# in analytical prose, so they MUST NOT be used for BLOCKING / admission gates.
AUTHOR_DRAFT: tuple[str, ...] = BLOCKING + (
    "replace ",
    "need ",
    "needs ",
    "still need",
    "still needs",
    "requires ",
)

# Fields that hold analytical prose rather than retained-observation evidence.
# Scanners should skip these so gap markers in prose don't count against the event.
SKIP_FIELDS_FOR_GAP_SCAN: frozenset[str] = frozenset({
    "analysis_notes",
    "scoped_claim",
    "scoped_knowledge",
    "follow_on_reaction",
    "enumeration_note",
    "tags",
})
