#!/usr/bin/env python3
"""Validate ODTIS Annex D extended profiles (stdlib only)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANNEX = ROOT / "annexes/D-extended-profiles"
REQ_FILE = ROOT / "registry/requirements.json"
CANONICAL_ID = re.compile(r"^ODTIS-\d{4}$")
LEGACY_ID = re.compile(r"^ODTIS-\d+\.\d+\.\d+$")
MODULE_IDS = {"E-Wallet", "E-Registry", "E-Inclusion", "E-Webhook", "E-Signature", "E-KYB"}


def parse_sub_modules(text: str) -> list[str]:
    section = text.split("sub_modules:", 1)
    if len(section) < 2:
        return []
    return re.findall(r"^- id: (E-[A-Za-z0-9-]+)\s*$", section[1].split("composition_rules:")[0], re.M)


def parse_registry_refs(text: str) -> dict[str, list[str]]:
    if "registry_refs:" not in text:
        return {}
    section = text.split("registry_refs:", 1)[1].split("draft_requirements:", 1)[0]
    refs: dict[str, list[str]] = {}
    current: str | None = None
    for line in section.splitlines():
        m_mod = re.match(r"^(E-[\w-]+|cross_cutting):\s*$", line)
        if m_mod:
            current = m_mod.group(1)
            refs[current] = []
            continue
        m_id = re.match(r"^- (ODTIS-\d{4})\s*$", line)
        if m_id and current:
            refs[current].append(m_id.group(1))
    return refs


def parse_annex_catalog_ids(text: str) -> dict[str, list[str]]:
    """Parse draft_requirements block (catalog mirror; may be merged in registry)."""
    if "draft_requirements:" not in text:
        return {}
    section = text.split("draft_requirements:", 1)[1]
    catalog: dict[str, list[str]] = {}
    current: str | None = None
    for line in section.splitlines():
        m_mod = re.match(r"^(E-[\w-]+):\s*$", line)
        if m_mod:
            current = m_mod.group(1)
            catalog[current] = []
            continue
        m_id = re.match(r"^- id: (ODTIS-\d{4})\s*$", line)
        if m_id and current:
            catalog[current].append(m_id.group(1))
    return catalog


def parse_index_modules(text: str) -> list[str]:
    m = re.search(r"^modules:\n", text, re.M)
    if not m:
        return []
    start = m.end()
    end = text.find("declaration_fields:", start)
    section = text[start:end] if end >= 0 else text[start:]
    return re.findall(r"^- id: (E-[A-Za-z0-9-]+)\s*$", section, re.M)


def main() -> int:
    errors: list[str] = []

    paths = {
        "sub-modules": ANNEX / "sub-modules.yaml",
        "activation": ANNEX / "activation.yaml",
        "extended-requirements": ANNEX / "extended-requirements.yaml",
        "INDEX": ANNEX / "INDEX.yaml",
    }
    for name, path in paths.items():
        if not path.is_file():
            errors.append(f"missing {name}: {path}")

    registry_ids: set[str] = set()
    if REQ_FILE.is_file():
        registry_ids = {r["id"] for r in json.loads(REQ_FILE.read_text())["requirements"]}

    sub_mod_text = paths["sub-modules"].read_text(encoding="utf-8") if paths["sub-modules"].is_file() else ""
    ext_text = paths["extended-requirements"].read_text(encoding="utf-8") if paths["extended-requirements"].is_file() else ""
    index_text = paths["INDEX"].read_text(encoding="utf-8") if paths["INDEX"].is_file() else ""

    sub_modules = parse_sub_modules(sub_mod_text)
    if set(sub_modules) != MODULE_IDS:
        errors.append(f"sub-modules expected {MODULE_IDS}, got {set(sub_modules)}")

    index_modules = parse_index_modules(index_text)
    if set(index_modules) != MODULE_IDS:
        errors.append(f"INDEX modules mismatch: {set(index_modules)}")

    refs = parse_registry_refs(ext_text)
    for mod in MODULE_IDS:
        for rid in refs.get(mod, []):
            if rid not in registry_ids:
                errors.append(f"{mod} registry_ref unknown in registry: {rid}")

    catalog = parse_annex_catalog_ids(ext_text)
    all_catalog: set[str] = set()
    for mod, ids in catalog.items():
        if mod not in MODULE_IDS:
            errors.append(f"catalog block for unknown module {mod}")
        for rid in ids:
            if rid in all_catalog:
                errors.append(f"duplicate catalog id {rid}")
            all_catalog.add(rid)
            if not CANONICAL_ID.match(rid):
                errors.append(f"invalid catalog id {rid}")
            if rid not in registry_ids:
                errors.append(f"Annex D catalog id not in registry (merge pending): {rid}")

    if paths["activation"].is_file():
        act = paths["activation"].read_text(encoding="utf-8")
        if "module_phase_minimum:" in act:
            for mod in MODULE_IDS:
                if mod not in act:
                    errors.append(f"activation missing phase minimum for {mod}")

    expected_catalog = 17
    if len(all_catalog) != expected_catalog:
        errors.append(f"expected {expected_catalog} Annex D catalog ids, found {len(all_catalog)}")

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1

    print(
        f"OK: Annex D - {len(sub_modules)} sub-modules, "
        f"{len(all_catalog)} catalog requirements in registry, INDEX aligned"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
