#!/usr/bin/env python3
"""Validate ODTIS Annex E reliance extensions (stdlib only)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANNEX = ROOT / "annexes/E-reliance-profiles"
REQ_FILE = ROOT / "registry/requirements.json"
CANONICAL_ID = re.compile(r"^ODTIS-\d{4}$")


def parse_catalog(text: str) -> dict[str, list[str]]:
    """Parse reliance-requirements.yaml requirements block -> {module: [ids]}."""
    if "requirements:" not in text:
        return {}
    section = text.split("requirements:", 1)[1]
    catalog: dict[str, list[str]] = {}
    current: str | None = None
    for line in section.splitlines():
        m_mod = re.match(r"^(R-[\w-]+):\s*$", line)
        if m_mod:
            current = m_mod.group(1)
            catalog[current] = []
            continue
        m_id = re.match(r"^- id: (ODTIS-\d{4})\s*$", line)
        if m_id and current:
            catalog[current].append(m_id.group(1))
    return catalog


def parse_submodules(text: str) -> list[str]:
    section = text.split("sub_modules:", 1)
    if len(section) < 2:
        return []
    body = section[1].split("composition_rules:")[0]
    return re.findall(r"^- id: (R-[A-Za-z0-9-]+)\s*$", body, re.M)


def main() -> int:
    errors: list[str] = []
    paths = {
        "sub-modules": ANNEX / "sub-modules.yaml",
        "activation": ANNEX / "activation.yaml",
        "reliance-requirements": ANNEX / "reliance-requirements.yaml",
        "INDEX": ANNEX / "INDEX.yaml",
        "README": ANNEX / "README.md",
    }
    for name, path in paths.items():
        if not path.is_file():
            errors.append(f"missing {name}: {path}")
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1

    registry_ids: set[str] = set()
    section_ids: set[str] = set()
    if REQ_FILE.is_file():
        for r in json.loads(REQ_FILE.read_text())["requirements"]:
            registry_ids.add(r["id"])
            if r.get("section") == "11-reliance-profiles":
                section_ids.add(r["id"])

    sub_text = paths["sub-modules"].read_text(encoding="utf-8")
    cat_text = paths["reliance-requirements"].read_text(encoding="utf-8")

    submodules = parse_submodules(sub_text)
    if not submodules:
        errors.append("no sub-modules parsed from sub-modules.yaml")

    catalog = parse_catalog(cat_text)
    all_catalog: set[str] = set()
    for mod, ids in catalog.items():
        for rid in ids:
            if not CANONICAL_ID.match(rid):
                errors.append(f"{mod}: invalid catalog id {rid}")
            if rid in all_catalog:
                errors.append(f"duplicate catalog id {rid}")
            all_catalog.add(rid)
            if rid not in registry_ids:
                errors.append(f"{mod}: catalog id not in registry: {rid}")

    # every section-11 registry id should be catalogued, and vice versa
    missing_in_catalog = section_ids - all_catalog
    if missing_in_catalog:
        errors.append(f"section-11 ids missing from Annex E catalog: {sorted(missing_in_catalog)}")
    extra_in_catalog = all_catalog - section_ids
    if extra_in_catalog:
        errors.append(f"Annex E catalog ids not in section 11: {sorted(extra_in_catalog)}")

    # base schema present
    for base in ("ODTIS-0701", "ODTIS-0707", "ODTIS-0708"):
        if base not in all_catalog:
            errors.append(f"base reliance requirement missing: {base}")

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1

    print(
        f"OK: Annex E - {len(submodules)} sub-modules, "
        f"{len(all_catalog)} reliance requirements in registry, section 11 aligned"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
