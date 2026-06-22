#!/usr/bin/env python3
"""Extract ODTIS requirement IDs from P18 tables into registry/requirements.json.

P18 is not vendored in core-spec. Set ODTIS_P18_PATH to a local PAPER-PUBLIC.md
copy (e.g. from digitaltrustinfrastructure.org materials) before running.
registry/requirements.json in the repo is the canonical draft registry for contributors.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "registry/requirements.json"
P18_SOURCE = (
    "P18 standards-alignment paper (informative; "
    "https://digitaltrustinfrastructure.org - see publication/HOW-TO-CITE.md)"
)

SECTION_MAP = {
    "2": "02-terminology-loa",
    "3": "03-identity-services",
    "4": "04-trust-network",
    "5": "05-consent-privacy",
    "6": "06-federation",
    "7": "07-operator-governance",
    "8": "08-security",
    "9": "09-audit-events",
    "10": "10-deployment-profiles",
}


def resolve_p18() -> Path | None:
    env = os.environ.get("ODTIS_P18_PATH")
    if env:
        path = Path(env).expanduser()
        return path if path.is_file() else None
    legacy = ROOT.parent / "docs/sources/papers/18-standards-alignment-odtis/PAPER-PUBLIC.md"
    return legacy if legacy.is_file() else None


def infer_keyword(text: str) -> str:
    if " MUST NOT " in text:
        return "MUST NOT"
    if " SHOULD " in f" {text} " or text.startswith("SHOULD"):
        return "SHOULD"
    if " MAY " in f" {text} " or text.startswith("MAY"):
        return "MAY"
    return "MUST"


def extract(text: str) -> list[dict]:
    requirements: list[dict] = []
    seen: set[str] = set()
    pattern = re.compile(
        r"\|\s*`(ODTIS-[0-9]+\.[0-9]+\.[0-9]+)`\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|"
    )
    for line in text.splitlines():
        match = pattern.search(line)
        if not match:
            continue
        rid, req_text, trace = match.group(1), match.group(2).strip(), match.group(3).strip()
        if rid in seen:
            continue
        seen.add(rid)
        section_num = rid.split("-")[1].split(".")[0]
        requirements.append(
            {
                "id": rid,
                "section": SECTION_MAP.get(section_num, "unknown"),
                "keyword": infer_keyword(req_text),
                "text": req_text,
                "trace_informative": trace,
                "status": "draft",
                "conformance_test": None,
            }
        )
    requirements.sort(key=lambda r: [int(x) for x in r["id"].replace("ODTIS-", "").split(".")])
    return requirements


def main() -> int:
    p18 = resolve_p18()
    if p18 is None:
        print(
            "error: P18 source not found. Set ODTIS_P18_PATH to PAPER-PUBLIC.md "
            "or use the committed registry/requirements.json as canonical.",
            file=sys.stderr,
        )
        return 1
    requirements = extract(p18.read_text(encoding="utf-8"))
    payload = {
        "spec_version": "0.1.0-draft",
        "source": P18_SOURCE,
        "requirement_count": len(requirements),
        "requirements": requirements,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(requirements)} requirements to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
