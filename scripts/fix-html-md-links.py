#!/usr/bin/env python3
"""Convert raw HTML <a href=\"*.md\"> to Markdown for MkDocs md_in_html."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TAGS = (
    "odtis-hub-meta",
    "odtis-home-links",
    "odtis-landing-hero__links",
    "odtis-path-card__desc",
)

MD_LINK = re.compile(r'<a href="([^"]+\.md)">([^<]+)</a>')
LICENSE_HREF = re.compile(r'<a href="(?:\.\./)?LICENSE">([^<]+)</a>')


def fix_text(text: str) -> str:
    for cls in TAGS:
        text = re.sub(
            rf'(<p class="{cls}")(?!\s+markdown="1")',
            r'\1 markdown="1"',
            text,
        )
    text = MD_LINK.sub(r"[\2](\1)", text)
    text = LICENSE_HREF.sub(r'<a href="/LICENSE">\1</a>', text)
    return text


def main() -> int:
    changed: list[str] = []
    for path in sorted(ROOT.rglob("*.md")):
        if ".venv-site" in path.parts or path.name.startswith("."):
            continue
        orig = path.read_text(encoding="utf-8")
        new = fix_text(orig)
        if new != orig:
            path.write_text(new, encoding="utf-8")
            changed.append(str(path.relative_to(ROOT)))
    if changed:
        print(f"Fixed HTML .md links in {len(changed)} files:")
        for name in changed:
            print(f"  - {name}")
    else:
        print("No HTML .md links to fix")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
