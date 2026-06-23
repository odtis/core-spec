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
ID_PATTERN = re.compile(r"^ODTIS-\d{4}$")
THREAT_ID_PATTERN = re.compile(r"^T-P07-\d{3}$")
REL_THREAT_ID_PATTERN = re.compile(r"^T-REL-\d{3}$")
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


def parse_threat_blocks(text: str, section_key: str = "threats:") -> list[dict]:
    """Parse threat list entries from a YAML threats section."""
    if section_key not in text:
        return []
    body = text.split(section_key, 1)[1]
    for stop in ("odtis_8_coverage:", "reliance_threats:"):
        if stop in body and section_key == "threats:":
            body = body.split(stop, 1)[0]
    if section_key == "reliance_threats:":
        body = body.split("threats:", 1)[-1] if "threats:" in body else body

    blocks = re.split(r"\n- id: ", body)
    threats: list[dict] = []
    for chunk in blocks[1:]:
        first_line, _, rest = chunk.partition("\n")
        tid = first_line.strip()
        block = f"id: {tid}\n{rest}"
        reqs = re.findall(r"^- (ODTIS-\d{4})\s*$", block, re.M)
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
    body = section[1].split("reliance_threats:", 1)[0]
    coverage: dict[str, list[str]] = {}
    current: str | None = None
    for line in body.splitlines():
        m_key = re.match(r"^(ODTIS-\d{4}):\s*\[(.*)\]\s*$", line)
        if m_key:
            current = m_key.group(1)
            items = [x.strip() for x in m_key.group(2).split(",") if x.strip()]
            coverage[current] = items
            continue
        m_item = re.match(r"^\s{4}-\s+(T-P07-\d{3})\s*$", line)
        if m_item and current:
            coverage.setdefault(current, []).append(m_item.group(1))
    return coverage


def validate_threat_list(
    threats: list[dict],
    *,
    id_pattern: re.Pattern[str],
    registry_ids: set[str],
    errors: list[str],
    require_p07_row: bool,
    rows: set[int] | None = None,
) -> set[str]:
    seen_ids: set[str] = set()
    referenced: set[str] = set()
    row_set = rows if rows is not None else set()

    for t in threats:
        tid = t["id"]
        if not id_pattern.match(tid):
            errors.append(f"invalid threat id format: {tid}")
        if tid in seen_ids:
            errors.append(f"duplicate threat id {tid}")
        seen_ids.add(tid)

        if require_p07_row:
            row = t["p07_row"]
            if row is None:
                errors.append(f"{tid}: missing p07_row")
            elif row in row_set:
                errors.append(f"duplicate p07_row {row}")
            else:
                row_set.add(row)

        for req_id in t["odtis_requirements"]:
            referenced.add(req_id)
            if registry_ids and req_id not in registry_ids:
                errors.append(f"{tid}: unknown requirement {req_id}")
            if not ID_PATTERN.match(req_id):
                errors.append(f"{tid}: invalid requirement id {req_id}")

        for field in ("risk", "scenario", "control"):
            if not t.get(field):
                errors.append(f"{tid}: missing {field}")

    return referenced


def main() -> int:
    errors: list[str] = []

    if not THREATS.is_file():
        errors.append(f"missing {THREATS}")
        _report(errors)
        return 1

    text = THREATS.read_text(encoding="utf-8")
    if "p07_table_rows: 18" not in text:
        errors.append("threats.yaml missing p07_table_rows: 18")

    threats = parse_threat_blocks(text, "threats:")
    if len(threats) != 18:
        errors.append(f"expected 18 P07 threats, found {len(threats)}")

    registry_ids: set[str] = set()
    if REQ_FILE.is_file():
        registry_ids = {r["id"] for r in json.loads(REQ_FILE.read_text())["requirements"]}

    p07_rows: set[int] = set()
    referenced = validate_threat_list(
        threats,
        id_pattern=THREAT_ID_PATTERN,
        registry_ids=registry_ids,
        errors=errors,
        require_p07_row=True,
        rows=p07_rows,
    )

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
            if not THREAT_ID_PATTERN.match(tid):
                errors.append(f"coverage {req_id} references invalid threat {tid}")

    for req_id in ODTIS_8_IDS:
        if req_id not in referenced:
            errors.append(f"{req_id} not referenced in any threat odtis_requirements")

    reliance_threats: list[dict] = []
    if "reliance_threats:" in text:
        reliance_threats = parse_threat_blocks(text, "reliance_threats:")
        if len(reliance_threats) < 1:
            errors.append("reliance_threats section is empty")
        validate_threat_list(
            reliance_threats,
            id_pattern=REL_THREAT_ID_PATTERN,
            registry_ids=registry_ids,
            errors=errors,
            require_p07_row=False,
        )
        if "TC-RELIANCE" not in text:
            errors.append("reliance_threats missing TC-RELIANCE threat class")

    if errors:
        _report(errors)
        return 1

    classes = len(re.findall(r"^- id: TC-", text, re.M))
    rel_note = f", {len(reliance_threats)} reliance threats" if reliance_threats else ""
    print(
        f"OK: Annex B - {len(threats)} P07 threats, {classes} threat classes, "
        f"all ODTIS-8.x covered{rel_note}"
    )
    return 0


def _report(errors: list[str]) -> None:
    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)


if __name__ == "__main__":
    raise SystemExit(main())
