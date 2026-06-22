#!/usr/bin/env python3
"""Validate ODTIS registry integrity."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ_FILE = ROOT / "registry/requirements.json"
VERSION_FILE = ROOT / "VERSION"
ID_PATTERN = re.compile(r"^ODTIS-\d{4}$")


def main() -> int:
    errors: list[str] = []

    if not REQ_FILE.is_file():
        errors.append(f"missing {REQ_FILE}")
    else:
        data = json.loads(REQ_FILE.read_text(encoding="utf-8"))
        reqs = data.get("requirements", [])
        ids = [r.get("id") for r in reqs]
        if len(ids) != len(set(ids)):
            errors.append("duplicate requirement IDs in registry")
        for r in reqs:
            rid = r.get("id", "")
            if not ID_PATTERN.match(rid):
                errors.append(f"invalid ID format: {rid}")
            domain = r.get("domain", "")
            if domain and not ID_PATTERN.match(domain):
                errors.append(f"{rid}: invalid domain: {domain}")
            legacy = r.get("legacy_id", "")
            if legacy and not re.match(r"^ODTIS-\d+\.\d+\.\d+$", legacy):
                errors.append(f"{rid}: invalid legacy_id: {legacy}")
            for field in ("section", "keyword", "text", "status"):
                if field not in r or r[field] in (None, ""):
                    errors.append(f"{rid}: missing {field}")
        declared = data.get("requirement_count")
        if declared != len(reqs):
            errors.append(f"requirement_count {declared} != actual {len(reqs)}")

    if not VERSION_FILE.is_file():
        errors.append(f"missing {VERSION_FILE}")

    for yaml_name in ("profiles.yaml", "events.yaml", "terminology.yaml"):
        path = ROOT / "registry" / yaml_name
        if not path.is_file():
            errors.append(f"missing {path}")

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1

    count = len(json.loads(REQ_FILE.read_text())["requirements"])
    version = VERSION_FILE.read_text().strip()
    print(f"OK: ODTIS {version} - {count} requirements, registry files present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
