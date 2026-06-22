#!/usr/bin/env python3
"""Convert fragile ../../ cross-tree links to absolute site-root paths."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GITHUB_ODTIS = "https://github.com/odtis/core-spec/blob/main"
GITHUB_MONOREPO = "https://github.com/finnectos/venezuela/blob/main"

REPLACEMENTS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\]\(\.\./\.\./conformance/profiles/[^)]+/\)"), "](/conformance/tests/)"),
    (re.compile(r"\]\(\.\./\.\./conformance/tests/extended/\)"), "](/conformance/tests/)"),
    (re.compile(r"\]\(\.\./\.\./conformance/\)"), "](/conformance/)"),
    (re.compile(r"\]\(\.\./\.\./ietf/drafts/\)"), "](/ietf/drafts/)"),
    (re.compile(r"\]\(\.\./\.\./registry/events/schemas/\)"), "](/registry/events/schemas/)"),
    (re.compile(r"\]\(\.\./\.\./annexes/"), "](/annexes/"),
    (re.compile(r"\]\(\.\./\.\./governance/"), "](/governance/"),
    (re.compile(r"\]\(\.\./\.\./implementation/"), "](/implementation/"),
    (re.compile(r"\]\(\.\./\.\./registry/"), "](/registry/"),
    (re.compile(r"\]\(\.\./\.\./project/"), "](/project/"),
    (re.compile(r"\]\(\.\./\.\./site/"), "](/site/"),
    (re.compile(r"\]\(\.\./\.\./ADOPTION\.md\)"), "](/ADOPTION/)"),
    (re.compile(r"\]\(\.\./\.\./conformance/README\.md\)"), "](/conformance/)"),
    (re.compile(r'href="\.\./VERSION"'), 'href="/VERSION"'),
    (re.compile(r"\]\(\.\./VERSION\)"), "](/VERSION)"),
    (re.compile(r"\]\(\.\./CHANGELOG\.md\)"), "](/CHANGELOG/)"),
    (re.compile(r"\]\(\.\./spec/profiles/\)"), "](/spec/profiles/)"),
    (re.compile(r"\]\(\.\./spec/profiles/([^)]+)\)"), r"](/spec/profiles/\1)"),
    (re.compile(r"\]\(/spec/\)"), "](/spec/INDEX/)"),
    (re.compile(r"\]\(/publication/\)"), "](/publication/HOW-TO-CITE/)"),
    (re.compile(r"\]\(/site/\)"), "](/site/GETTING-STARTED/)"),
    (re.compile(r"\]\(/scripts/\)"), f"]({GITHUB_ODTIS}/tree/main/scripts)"),
]

TEST_MD = re.compile(r"\]\(\.\./\.\./(conformance/tests/[^)]+\.md)\)")
ABS_MD = re.compile(r"\]\((/[^)#]+)\.md\)(#[^)]+)?")
MONOREPO_DOC = re.compile(r"\]\((?:\.\./)+docs/sources/([^)]+)\)")


def abs_md_target(path: str) -> str:
    if path.endswith("/README"):
        return f"{path.rsplit('/', 1)[0]}/"
    return f"{path}/"


def fix_content(text: str) -> str:
    text = TEST_MD.sub(lambda m: f"]({GITHUB_ODTIS}/{m.group(1)})", text)
    text = MONOREPO_DOC.sub(lambda m: f"]({GITHUB_MONOREPO}/docs/sources/{m.group(1)})", text)
    text = ABS_MD.sub(lambda m: f"]({abs_md_target(m.group(1))}){m.group(2) or ''}", text)
    for pattern, repl in REPLACEMENTS:
        if callable(repl):
            continue
        text = pattern.sub(repl, text)
    return text


def main() -> int:
    changed = 0
    for path in sorted(ROOT.rglob("*.md")):
        if ".venv-site" in path.parts or "build" in path.parts:
            continue
        original = path.read_text(encoding="utf-8")
        updated = fix_content(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(f"Updated {path.relative_to(ROOT)}")
            changed += 1
    print(f"Done ({changed} files updated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
