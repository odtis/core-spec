#!/usr/bin/env python3
"""Create conformance test stubs for requirements missing test links."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ_FILE = ROOT / "registry/requirements.json"

PROFILE_PREFIX = {
    "02-terminology-loa": "core-identity",
    "03-identity-services": "core-identity",
    "05-consent-privacy": "core-identity",
    "04-trust-network": "trust-network",
    "06-federation": "federation",
    "07-operator-governance": "operator",
    "08-security": "operator",
    "09-audit-events": "operator",
    "10-deployment-profiles": "operator",
}


def slug(rid: str) -> str:
    return rid.lower().replace(".", "_")


def stub_body(rid: str, profile: str, text: str) -> str:
    short = text[:80].rstrip()
    return f"""# Conformance test: {rid}

**Status:** pending implementation  
**Requirement:** {rid}  
**Profile:** {profile}

## Procedure

1. Configure target deployment per conformance statement.
2. Exercise behavior required by: {short}…
3. Record evidence (request/response, logs, or policy document as applicable).

## Pass criteria

Implementation satisfies {rid} MUST/SHOULD as declared in spec prose.
"""


def main() -> int:
    data = json.loads(REQ_FILE.read_text(encoding="utf-8"))
    created = 0
    linked = 0
    for req in data["requirements"]:
        if req.get("conformance_test"):
            continue
        section = req.get("section", "")
        profile = PROFILE_PREFIX.get(section)
        if not profile:
            continue
        rid = req["id"]
        rel = f"conformance/tests/{profile}/test_{slug(rid)}.md"
        path = ROOT / rel
        if not path.is_file():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(stub_body(rid, profile, req.get("text", "")), encoding="utf-8")
            created += 1
        req["conformance_test"] = rel
        linked += 1

    data["requirement_count"] = len(data["requirements"])
    REQ_FILE.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"Linked {linked} requirements; created {created} new stub files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
