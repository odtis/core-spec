#!/usr/bin/env python3
"""Replace typographic punctuation (em dash, section sign, en dash) with ASCII in ODTIS."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TEXT_SUFFIXES = {
    ".md",
    ".yaml",
    ".yml",
    ".json",
    ".py",
    ".sh",
    ".cff",
    ".openapi.yaml",
    ".txt",
}

SKIP_DIRS = {".venv-site", ".git", "__pycache__", "build"}

EN_DASH_RANGE = re.compile(r"(\d)\u2013(\d)")
SECTION_SIGN = re.compile(r"\u00a7(\d+(?:\.\d+)*)")

EM_DASH = "\u2014"
EN_DASH = "\u2013"


def normalize_text(text: str, *, tidy_whitespace: bool = True) -> str:
    text = EN_DASH_RANGE.sub(r"\1-\2", text)
    text = text.replace(EM_DASH, " - ")
    text = SECTION_SIGN.sub(r"section \1", text)
    text = text.replace(EN_DASH, "-")
    if not tidy_whitespace:
        return text
    text = re.sub(r"  +", " ", text)
    text = re.sub(r" +(\|)", r" \1", text)
    text = re.sub(r"(\|) +", r"\1 ", text)
    text = re.sub(r" +\n", "\n", text)
    text = re.sub(r"\n +", "\n", text)
    return text


def iter_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        name = path.name
        if name.endswith(".openapi.yaml") or path.suffix in TEXT_SUFFIXES:
            if path.suffix in {".yaml", ".yml", ".json"}:
                continue
            files.append(path)
    return sorted(files)


def file_has_targets(text: str) -> bool:
    return EM_DASH in text or EN_DASH in text or "\u00a7" in text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    stale: list[str] = []
    for path in iter_files():
        text = path.read_text(encoding="utf-8")
        if not file_has_targets(text):
            continue
        tidy = path.suffix in {".md", ".cff", ".txt"}
        new = normalize_text(text, tidy_whitespace=tidy)
        if new != text:
            stale.append(str(path.relative_to(ROOT)))
            if not args.check:
                path.write_text(new, encoding="utf-8")

    if args.check:
        if stale:
            print(f"FAIL - typographic punctuation in {len(stale)} files:")
            for s in stale[:30]:
                print(f"  - {s}")
            if len(stale) > 30:
                print(f"  ... and {len(stale) - 30} more")
            return 1
        print("OK - no em dash, en dash, or section sign")
        return 0

    print(f"Normalized {len(stale)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
