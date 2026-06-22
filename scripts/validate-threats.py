#!/usr/bin/env python3
"""Validate ODTIS Annex B threat matrix (stdlib only)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANNEX = ROOT / "annexes/B-threat-mitigations"
THREATS = ANNEX / "threats.yaml"
REQ_FILE = ROOT / "registry/requirements.json"
ID_PATTERN = re.compile(r"^ODTIS-\d+\.\d+\.\d+$")
THREAT_ID_PATTERN = re.compile(r"^T-P07-\d{3}$")
ODTIS_8_IDS = [
    "ODTIS-0517",
    "ODTIS-0518",
    "ODTIS-0519",
    "ODTIS-0520",
    "ODTIS-0521",
    "ODTIS-0522",
    "ODTIS-0523",
    "ODTIS-0524",
    "ODTIS-0525",
]


def parse_threat_blocks(text: str) -> list[dict]:
    """Parse threat list entries from the threats: section only."""
    if "threats:" not in text:
        return []
    body = text.split("threats:", 1)[1]
    if "odtis_8_coverage:" in body:
        body = body.split("odtis_8_coverage:", 1)[0]

    blocks = re.split(r"\n- id: ", body)
    threats: list[dict] = []
    for chunk in blocks[1:]:
        first_line, _, rest = chunk.partition("\n")
        tid = first_line.strip()
        block = f"id: {tid}\n{rest}"
        reqs = re.findall(r"^- (ODTIS-\d+\.\d+\.\d+)\s*$", block, re.M)
        row_match = re.search(r"^p07_row:\s*(\d+)\s*$", block, re.M)
        fields = {}
        for name in ("risk", "scenario", "control", "threat_class"):
            m = re.search(rf"^{name}:\s*(.+)\s*$", block, re.M)
            fields[name] = m.group(1).strip() if m else ""
        threats.append(
            {
                "id": tid,
                "p07_row": int(row_match.group(1)) if row_match else None,
                "odtis_requirements": reqs,
                **fields,
            }
        )
    return threats


def parse_8_coverage(text: str) -> dict[str, list[str]]:
    section = text.split("odtis_8_coverage:", 1)
    if len(section) < 2:
        return {}
    coverage: dict[str, list[str]] = {}
    current: str | None = None
    for line in section[1].splitlines():
        m_key = re.match(r"^(ODTIS-8\.\d\.\d):\s*\[(.*)\]\s*$", line)
        if m_key:
            current = m_key.group(1)
            items = [x.strip() for x in m_key.group(2).split(",") if x.strip()]
            coverage[current] = items
            continue
        m_item = re.match(r"^\s{4}-\s+(T-P07-\d{3})\s*$", line)
        if m_item and current:
            coverage.setdefault(current, []).append(m_item.group(1))
    return coverage


def main() -> int:
    errors: list[str] = []

    if not THREATS.is_file():
        errors.append(f"missing {THREATS}")
        _report(errors)
        return 1

    text = THREATS.read_text(encoding="utf-8")
    if "p07_table_rows: 18" not in text:
        errors.append("threats.yaml missing p07_table_rows: 18")

    threats = parse_threat_blocks(text)
    if len(threats) != 18:
        errors.append(f"expected 18 threats, found {len(threats)}")

    registry_ids: set[str] = set()
    if REQ_FILE.is_file():
        registry_ids = {r["id"] for r in json.loads(REQ_FILE.read_text())["requirements"]}

    seen_ids: set[str] = set()
    referenced: set[str] = set()
    rows: set[int] = set()

    for t in threats:
        tid = t["id"]
        if not THREAT_ID_PATTERN.match(tid):
            errors.append(f"invalid threat id format: {tid}")
        if tid in seen_ids:
            errors.append(f"duplicate threat id {tid}")
        seen_ids.add(tid)

        row = t["p07_row"]
        if row is None:
            errors.append(f"{tid}: missing p07_row")
        elif row in rows:
            errors.append(f"duplicate p07_row {row}")
        else:
            rows.add(row)

        for req_id in t["odtis_requirements"]:
            referenced.add(req_id)
            if registry_ids and req_id not in registry_ids:
                errors.append(f"{tid}: unknown requirement {req_id}")
            if not ID_PATTERN.match(req_id):
                errors.append(f"{tid}: invalid requirement id {req_id}")

        for field in ("risk", "scenario", "control", "threat_class"):
            if not t.get(field):
                errors.append(f"{tid}: missing {field}")

    coverage = parse_8_coverage(text)
    for req_id in ODTIS_8_IDS:
        if req_id not in coverage:
            errors.append(f"odtis_8_coverage missing {req_id}")
        elif not coverage[req_id]:
            errors.append(f"odtis_8_coverage empty for {req_id}")

    for req_id, threat_list in coverage.items():
        if req_id not in ODTIS_8_IDS:
            errors.append(f"odtis_8_coverage unexpected key {req_id}")
        for tid in threat_list:
            if tid not in seen_ids:
                errors.append(f"coverage {req_id} references unknown threat {tid}")

    for req_id in ODTIS_8_IDS:
        if req_id not in referenced:
            errors.append(f"{req_id} not referenced in any threat odtis_requirements")

    if errors:
        _report(errors)
        return 1

    classes = len(re.findall(r"^- id: TC-", text, re.M))
    print(f"OK: Annex B - {len(threats)} threats, {classes} threat classes, all ODTIS-8.x covered")
    return 0


def _report(errors: list[str]) -> None:
    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)


if __name__ == "__main__":
    raise SystemExit(main())
