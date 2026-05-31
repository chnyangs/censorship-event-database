# SPDX-License-Identifier: MIT
"""Strict YAML helpers for release-facing corpus files."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


class UniqueKeySafeLoader(yaml.SafeLoader):
    """PyYAML SafeLoader variant that rejects duplicate mapping keys."""


def _construct_mapping_without_duplicate_keys(
    loader: UniqueKeySafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[Any, Any]:
    seen: set[Any] = set()
    for key_node, _value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key {key!r}",
                key_node.start_mark,
            )
        seen.add(key)
    return yaml.SafeLoader.construct_mapping(loader, node, deep=deep)


UniqueKeySafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_mapping_without_duplicate_keys,
)


def load_yaml_unique_keys(path: Path) -> Any:
    return yaml.load(path.read_text(), Loader=UniqueKeySafeLoader)
