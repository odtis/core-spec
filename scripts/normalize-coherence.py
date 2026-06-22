#!/usr/bin/env python3
"""Normalize ODTIS document status lines and version references for coherence."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

SPEC_STATUS = "review draft - Phase 3.2"
ANNEX_A_STATUS = "frozen - see FREEZE.md"
ANNEX_BCD_STATUS = "review draft - Phase 3.2"


def patch_file(path: Path, replacements: list[tuple[str, str]]) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text
    for old, new in replacements:
        text = text.replace(old, new)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            return True
            return False


def normalize_spec_headers() -> int:
    count = 0
    for path in sorted((ROOT / "spec").glob("*/SPEC.md")):
        text = path.read_text(encoding="utf-8")
        text = re.sub(
        r"^\|\s*\*\*Status\*\*\s*\|\s*draft v0\.5[^\|]*\|\s*$",
        f"| **Status** | {SPEC_STATUS} |",
        text,
        flags=re.M,
        )
        text = re.sub(
        r"^\|\s*\*\*Spec version\*\*\s*\|\s*[^\|]+\|\s*$",
        f"| **Spec version** | {VERSION} |",
        text,
        count=1,
        flags=re.M,
        )
        new = text
        if new != path.read_text(encoding="utf-8"):
            path.write_text(new, encoding="utf-8")
            count += 1
            print(f" spec header {path.relative_to(ROOT)}")
            return count


def normalize_annex_readmes() -> int:
    count = 0
    mapping = {
    "A-openapi-registry": ANNEX_A_STATUS,
    "B-threat-mitigations": ANNEX_BCD_STATUS,
    "C-standards-mapping": ANNEX_BCD_STATUS,
    "D-extended-profiles": ANNEX_BCD_STATUS,
    }
    for sub, status in mapping.items():
        path = ROOT / "annexes" / sub / "README.md"
        if not path.is_file():
            continue
            text = path.read_text(encoding="utf-8")
            text = re.sub(
            r"^\|\s*\*\*Status\*\*\s*\|\s*[^\|]+\|\s*$",
            f"| **Status** | {status} |",
            text,
            count=1,
            flags=re.M,
            )
            text = re.sub(
            r"^\|\s*\*\*Spec version\*\*\s*\|\s*[^\|]+\|\s*$",
            f"| **Spec version** | {VERSION} |",
            text,
            count=1,
            flags=re.M,
            )
            if text != path.read_text(encoding="utf-8"):
                path.write_text(text, encoding="utf-8")
                count += 1
                print(f" annex {path.relative_to(ROOT)}")
                return count


def main() -> None:
    n = normalize_spec_headers()
    n += normalize_annex_readmes()
    # Fix spacing typo in annex A if present
    a = ROOT / "annexes/A-openapi-registry/README.md"
    if a.is_file():
        t = a.read_text(encoding="utf-8").replace(f"{VERSION}|", f"{VERSION} |")
        a.write_text(t, encoding="utf-8")
        print(f"Normalized {n} files (version {VERSION})")


if __name__ == "__main__":
    main()
