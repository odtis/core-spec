#!/usr/bin/env python3
"""Validate ODTIS Annex C standards mapping (stdlib only)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANNEX = ROOT / "annexes/C-standards-mapping"
MAPPING = ANNEX / "mapping.yaml"
STANDARDS = ANNEX / "standards.yaml"
LOA = ANNEX / "loa-matrix.yaml"
REQ_FILE = ROOT / "registry/requirements.json"
ID_PATTERN = re.compile(r"^ODTIS-\d{4}$")
COVERAGE = {"full", "partial", "informative", "platform"}


def parse_standard_ids(text: str) -> set[str]:
    return set(re.findall(r"^\s+- id: (STD-[\w-]+)\s*$", text, re.M))


def parse_requirement_coverage(text: str) -> dict[str, list[dict]]:
    if "requirement_coverage:" not in text:
        return {}
    section = text.split("requirement_coverage:", 1)[1]
    coverage: dict[str, list[dict]] = {}
    current: str | None = None
    entry: dict | None = None

    for line in section.splitlines():
        m_req = re.match(r"^  (ODTIS-\d{4}):\s*$", line)
        if m_req:
            current = m_req.group(1)
            coverage[current] = []
            entry = None
            continue
        m_std = re.match(r"^\s+- standard_id: (STD-[\w-]+)\s*$", line)
        if m_std and current:
            entry = {"standard_id": m_std.group(1)}
            coverage[current].append(entry)
            continue
        m_cov = re.match(r"^\s+coverage: (\w+)\s*$", line)
        if m_cov and entry is not None:
            entry["coverage"] = m_cov.group(1)
    return coverage


def main() -> int:
    errors: list[str] = []

    for path in (MAPPING, STANDARDS, LOA):
        if not path.is_file():
            errors.append(f"missing {path}")

    registry_ids: list[str] = []
    if REQ_FILE.is_file():
        registry_ids = [r["id"] for r in json.loads(REQ_FILE.read_text())["requirements"]]

    std_ids: set[str] = set()
    if STANDARDS.is_file():
        std_ids = parse_standard_ids(STANDARDS.read_text(encoding="utf-8"))

    cov: dict[str, list[dict]] = {}
    if MAPPING.is_file():
        cov = parse_requirement_coverage(MAPPING.read_text(encoding="utf-8"))

    if len(cov) != len(registry_ids):
        errors.append(f"mapping entries {len(cov)} != registry {len(registry_ids)}")

    for rid in registry_ids:
        if rid not in cov:
            errors.append(f"missing mapping for {rid}")
        elif not cov[rid]:
            errors.append(f"empty mapping for {rid}")

    for rid, entries in cov.items():
        if not ID_PATTERN.match(rid):
            errors.append(f"invalid requirement id {rid}")
        for e in entries:
            sid = e.get("standard_id", "")
            if sid not in std_ids:
                errors.append(f"{rid}: unknown standard_id {sid}")
            cov_level = e.get("coverage", "")
            if cov_level not in COVERAGE:
                errors.append(f"{rid}: invalid coverage {cov_level}")

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1

    std_count = len(std_ids)
    print(f"OK: Annex C - {len(cov)} requirements mapped, {std_count} standards in catalog")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
