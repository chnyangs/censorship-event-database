# SPDX-License-Identifier: MIT
"""pytest configuration: make scripts/ importable from tests.

The derivation scripts live under `scripts/` and are imported as flat
modules (not a package). Adding them to sys.path here lets tests do
`from assign_archetypes import classify` without the test runner
having to mess with PYTHONPATH.
"""
from __future__ import annotations

import pathlib
import sys

SCRIPTS_DIR = pathlib.Path(__file__).resolve().parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
