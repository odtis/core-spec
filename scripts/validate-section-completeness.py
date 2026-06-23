#!/usr/bin/env python3
"""Validate ODTIS spec sections 2-10 for registry/prose/test completeness."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
REGISTRY = ROOT / "registry/requirements.json"

SECTION_SPECS: dict[str, str] = {
    "02-terminology-loa": "spec/02-terminology-loa/SPEC.md",
    "03-identity-services": "spec/03-identity-services/SPEC.md",
    "04-trust-network": "spec/04-trust-network/SPEC.md",
    "05-consent-privacy": "spec/05-consent-privacy/SPEC.md",
    "06-federation": "spec/06-federation/SPEC.md",
    "07-operator-governance": "spec/07-operator-governance/SPEC.md",
    "08-security": "spec/08-security/SPEC.md",
    "09-audit-events": "spec/09-audit-events/SPEC.md",
    "10-deployment-profiles": "spec/10-deployment-profiles/SPEC.md",
    "11-reliance-profiles": "spec/11-reliance-profiles/SPEC.md",
}

DEPTH_WARNINGS: dict[str, str] = {
    "10-deployment-profiles": "only 2 normative IDs; phase binding is intentional; HA numeric targets informative",
}


def body_before_index(text: str) -> str:
    m = re.search(r"\n## \d+\.\d+ Requirement index|\n## Document history", text)
    return text[: m.start()] if m else text


def canonical_index_ids(block: str, reg_ids: set[str]) -> set[str]:
    """Collect ODTIS-MNNN IDs listed in a requirement index block."""
    found: set[str] = set()
    for rid in re.findall(r"ODTIS-\d{4}", block):
        if rid in reg_ids:
            found.add(rid)
    for rid in re.findall(r"ODTIS-\d+\.\d+\.\d+", block):
        if rid in reg_ids:
            found.add(rid)
    return found


def index_ids(text: str, reg_ids: set[str]) -> set[str]:
    m = re.search(r"## \d+\.\d+ Requirement index", text)
    if m:
        tail = text[m.start() :]
        end = re.search(r"\n## Document history", tail)
        block = tail[: end.start()] if end else tail
        return canonical_index_ids(block, reg_ids)

    dh = text.find("## Document history")
    pre = text[:dh] if dh > 0 else text
    return canonical_index_ids(pre, reg_ids)


def validate_section(section: str, spec_path: Path, reqs: list[dict]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not spec_path.is_file():
        errors.append(f"missing {spec_path}")
        return errors, warnings

    text = spec_path.read_text(encoding="utf-8")
    sec_reqs = [r for r in reqs if r["section"] == section]
    reg_ids = {r["id"] for r in sec_reqs}
    body = body_before_index(text)
    idx_ids = index_ids(text, reg_ids)

    if f"**Spec version** | {VERSION} |" not in text:
        errors.append(f"{section}: spec version header != {VERSION}")

    if "review draft - Phase 3.2" not in text:
        warnings.append(f"{section}: status line not Phase 3.2 review draft")

    if not re.search(r"## \d+\.1 ", text):
        errors.append(f"{section}: missing section X.1 opening subsection")

    has_index_heading = bool(re.search(r"## \d+\.\d+ Requirement index", text))
    has_index_table = len(idx_ids) == len(reg_ids) and len(reg_ids) > 0
    if not has_index_heading and not has_index_table:
        errors.append(f"{section}: missing requirement index")

    for rid in reg_ids:
        if rid not in body:
            errors.append(f"{section}: {rid} not cited in normative prose")
        if rid not in idx_ids:
            errors.append(f"{section}: {rid} missing from requirement index")
        test = next(r["conformance_test"] for r in sec_reqs if r["id"] == rid)
        if not (ROOT / test).is_file():
            errors.append(f"{section}: missing test file {test}")

    extra_idx = idx_ids - reg_ids
    if extra_idx:
        errors.append(f"{section}: requirement index lists IDs not in registry: {sorted(extra_idx)}")

    if len(reg_ids) != len(idx_ids):
        errors.append(f"{section}: index count {len(idx_ids)} != registry {len(reg_ids)}")

    if "0.9.0-draft" not in text:
        warnings.append(f"{section}: document history missing 0.9.0-draft entry")

    if "Phase 3.2 review checklist" not in text:
        warnings.append(f"{section}: missing Phase 3.2 review checklist")

    if section in DEPTH_WARNINGS:
        warnings.append(f"{section}: {DEPTH_WARNINGS[section]}")

    return errors, warnings


def main() -> int:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    reqs = data["requirements"]
    all_errors: list[str] = []
    all_warnings: list[str] = []

    for section, rel in SECTION_SPECS.items():
        errs, warns = validate_section(section, ROOT / rel, reqs)
        all_errors.extend(errs)
        all_warnings.extend(warns)

    for w in all_warnings:
        print(f"WARN: {w}")
    for e in all_errors:
        print(f"ERROR: {e}", file=sys.stderr)

    if all_errors:
        return 1

    total = sum(1 for r in reqs if r["section"] in SECTION_SPECS)
    print(f"OK: sections 2-11 complete - {total} requirements, prose + index + tests aligned @ {VERSION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
