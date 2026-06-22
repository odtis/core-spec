#!/usr/bin/env python3
"""Fix relative directory links in root-level MkDocs pages (ADOPTION, STRUCTURE, etc.)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = ["ADOPTION.md", "STRUCTURE.md", "CHANGELOG.md", "index.md"]
TOP_DIRS = (
    "spec",
    "registry",
    "annexes",
    "conformance",
    "implementation",
    "governance",
    "site",
    "publication",
    "ietf",
    "project",
)

GITHUB = "https://github.com/odtis/core-spec"


def fix_content(text: str) -> str:
    for d in TOP_DIRS:
        text = re.sub(rf"\]\(({re.escape(d)}/)", rf"](/{d}/", text)
        text = re.sub(rf"\]\(({re.escape(d)})\)", rf"](/{d}/)", text)

    text = re.sub(r"\]\(VERSION\)", "](/VERSION)", text)
    text = re.sub(r"\]\(LICENSE\)", "](/site/LICENSE/)", text)
    text = re.sub(r"\]\(CHANGELOG\.md\)", "](/CHANGELOG/)", text)
    text = re.sub(r"\]\(ADOPTION\.md\)", "](/ADOPTION/)", text)
    text = re.sub(r"\]\(PLAN-PHASES\.md\)", "](/PLAN-PHASES/)", text)
    text = re.sub(
        r"\]\(traceability/\)",
        f"]({GITHUB}/tree/main/traceability)",
        text,
    )
    text = re.sub(r"\]\(scripts/\)", "](/scripts/)", text)
    text = re.sub(r"\]\(conformance/run\.sh\)", "](/conformance/run.sh)", text)
    return text


def main() -> int:
    changed = 0
    for name in TARGETS:
        path = ROOT / name
        if not path.is_file():
            continue
        original = path.read_text(encoding="utf-8")
        updated = fix_content(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(f"Updated {name}")
            changed += 1
    print(f"Done ({changed} files updated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
