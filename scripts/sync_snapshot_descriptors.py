#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Synchronize public snapshot descriptors from event YAML and CITATION.cff.

Run before build_dataset.py: README.md and .zenodo.json are themselves source
inputs to the dataset hash. Never read dataset.meta.json, generated timestamps,
or that hash here. Unrelated descriptor fields and README prose are preserved.
"""
from __future__ import annotations

import argparse
import collections
import copy
import json
from pathlib import Path

from _yaml_strict import load_yaml_unique_keys

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- SNAPSHOT:START -->"
END = "<!-- SNAPSHOT:END -->"


def author_name(author: dict) -> str:
    if author.get("family-names"):
        return ", ".join(str(author[key]) for key in ("family-names", "given-names") if author.get(key))
    if author.get("name"):
        return str(author["name"])
    raise ValueError("CFF author requires family-names or name")


def citation_text(cff: dict) -> str:
    """Use actual CFF authors and an optional declared release date only."""
    authors = "; ".join(author_name(author) for author in cff.get("authors", []))
    year = f" ({str(cff['date-released'])[:4]})." if cff.get("date-released") else ""
    prefix = f"{authors}.{year} " if authors else ""
    url = cff.get("repository-code") or cff.get("url", "")
    return f"{prefix}{cff['title']} (version {cff['version']}). {url}.".rstrip()


def load_snapshot(repo: Path) -> tuple[dict, dict]:
    cff = load_yaml_unique_keys(repo / "CITATION.cff")
    for field in ("title", "abstract", "version", "authors"):
        if not cff.get(field):
            raise ValueError(f"CITATION.cff requires {field}")
    events = []
    ids = set()
    for path in sorted((repo / "events").glob("*.yaml")):
        if path.name == "TEMPLATE.yaml" or path.name.startswith("_"):
            continue
        event = load_yaml_unique_keys(path)
        if not isinstance(event, dict) or not event.get("id") or not event.get("status"):
            raise ValueError(f"Event id and status required: {path}")
        if event["id"] in ids:
            raise ValueError(f"Duplicate event id: {event['id']}")
        ids.add(event["id"])
        events.append(event)
    if not events:
        raise ValueError("No event records found")
    return cff, {
        "total": len(events),
        "statuses": dict(sorted(collections.Counter(event["status"] for event in events).items())),
        "strata": dict(sorted(collections.Counter(event.get("research_stratum", "unspecified") for event in events).items())),
    }


def snapshot_text(snapshot: dict) -> str:
    statuses = snapshot["statuses"]
    labels = [f"{statuses.get(name, 0)} {name}" for name in ("admitted", "draft", "rejected")]
    labels.extend(f"{count} {name}" for name, count in statuses.items()
                  if name not in {"admitted", "draft", "rejected"})
    return f"{snapshot['total']} event records: {', '.join(labels)}."


def synchronize_text(cff: dict, snapshot: dict, readme: str, zenodo: dict, croissant: dict) -> dict[str, str]:
    if readme.count(START) != 1 or readme.count(END) != 1 or readme.index(END) < readme.index(START):
        raise ValueError("README.md requires exactly one ordered SNAPSHOT marker pair")
    counts = snapshot_text(snapshot)
    description = str(cff["abstract"]).strip() + " Current working registry: " + counts
    block = (
        f"\n**Working snapshot `{cff['version']}`:** {counts}\n"
        "Admitted denotes legacy repository status, not independent validation.\n"
        "Endpoint and indexed-log collection are complete for the machine candidate\n"
        "cohort; independent reference validation, human adjudication, and strict\n"
        "release sign-off remain pending.\n"
        "Counts are synchronized from event YAML;\n"
        "citation metadata comes from [CITATION.cff](CITATION.cff).\n"
    )
    readme = readme[:readme.index(START) + len(START)] + block + readme[readme.index(END):]
    zenodo = copy.deepcopy(zenodo)
    zenodo.update(title=cff["title"], description=description, version=str(cff["version"]))
    zenodo["creators"] = []
    creators = []
    for author in cff["authors"]:
        creator = {"name": author_name(author)}
        person = {"@type": "sc:Person", "name": author_name(author)}
        if author.get("affiliation"):
            creator["affiliation"] = str(author["affiliation"])
            person["affiliation"] = str(author["affiliation"])
        if author.get("orcid"):
            creator["orcid"] = str(author["orcid"]).removeprefix("https://orcid.org/")
            person["sameAs"] = str(author["orcid"])
        zenodo["creators"].append(creator)
        creators.append(person)
    if cff.get("keywords"):
        zenodo["keywords"] = list(cff["keywords"])
    if cff.get("license"):
        zenodo["license"] = cff["license"]
    croissant = copy.deepcopy(croissant)
    croissant.update(alternateName=cff["title"], description=description,
                     creator=creators, version=str(cff["version"]), citeAs=citation_text(cff))
    if cff.get("date-released"):
        zenodo["publication_date"] = str(cff["date-released"])
        croissant["datePublished"] = str(cff["date-released"])
    else:
        zenodo.pop("publication_date", None)
        croissant.pop("datePublished", None)
    for distribution in croissant.get("distribution", []):
        if distribution.get("sha256") == "main":
            distribution.pop("sha256")
        if distribution.get("@id") == "event-records":
            distribution["description"] = (
                f"One YAML file per event ({snapshot['total']} records). "
                "The record schema is schema/event.schema.json; schema conformance "
                "does not establish evidence support."
            )
    admitted = snapshot["statuses"].get("admitted", 0)
    strata = ", ".join(f"{name} ({count})" for name, count in snapshot["strata"].items())
    for record_set in croissant.get("recordSet", []):
        if record_set.get("@id") != "events":
            continue
        record_set["description"] = (
            counts + f" Descriptive paper summaries use {admitted} admitted legacy records; "
            "admission is not independent validation. Registry strata: " + strata + "."
        )
        for field in record_set.get("field", []):
            if field.get("@id") == "events/status":
                field["description"] = (
                    f"admitted | draft | rejected. The {admitted} admitted legacy records "
                    "form the descriptive corpus; status does not certify independent validation."
                )
    return {
        "README.md": readme,
        ".zenodo.json": json.dumps(zenodo, indent=2, ensure_ascii=False) + "\n",
        "croissant.json": json.dumps(croissant, indent=2, ensure_ascii=False) + "\n",
    }


def build_outputs(repo: Path) -> dict[str, str]:
    cff, snapshot = load_snapshot(repo)
    return synchronize_text(cff, snapshot, (repo / "README.md").read_text(),
                            json.loads((repo / ".zenodo.json").read_text()),
                            json.loads((repo / "croissant.json").read_text()))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true", help="Check synchronization without writing")
    args = parser.parse_args()
    outputs = build_outputs(args.repo)
    changed = [name for name, content in outputs.items() if (args.repo / name).read_text() != content]
    if args.check:
        print("Stale descriptors: " + ", ".join(changed) if changed else "Snapshot descriptors are synchronized")
        return int(bool(changed))
    for name in changed:
        (args.repo / name).write_text(outputs[name])
    print("Synchronized: " + ", ".join(changed) if changed else "Snapshot descriptors already synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
