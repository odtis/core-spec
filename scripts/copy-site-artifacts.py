#!/usr/bin/env python3
"""Copy machine-readable YAML/JSON into the built static site (same paths as repo)."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT.parent / "build" / "odtis-spec-site"

SKIP_DIRS = {".venv-site", ".git", "__pycache__", "build", "conformance/reports"}
SKIP_FILES = {"site/mkdocs.yml", "site/requirements.txt"}
SUFFIXES = {".yaml", ".yml", ".json", ".openapi.yaml"}
EXTRA_ROOT_FILES = ("VERSION", "LICENSE")
SITE_META_FILES = ("site/BUILD-META.json",)
SCRIPT_SUFFIXES = {".py", ".sh"}
CONFORMANCE_SHELLS = True


def main() -> int:
    if not OUT.is_dir():
        print(f"ERROR: build output not found: {OUT}", file=sys.stderr)
        return 1

    copied = 0
    for name in EXTRA_ROOT_FILES:
        src = ROOT / name
        if src.is_file():
            dest = OUT / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
            copied += 1

    for rel in SITE_META_FILES:
        src = ROOT / rel
        if src.is_file():
            dest = OUT / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
            copied += 1

    scripts_dir = ROOT / "scripts"
    if scripts_dir.is_dir():
        for path in sorted(scripts_dir.rglob("*")):
            if path.is_file() and path.suffix in SCRIPT_SUFFIXES:
                dest = OUT / path.relative_to(ROOT)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, dest)
                copied += 1

    if CONFORMANCE_SHELLS:
        conf = ROOT / "conformance"
        if conf.is_dir():
            for path in sorted(conf.glob("*.sh")):
                dest = OUT / path.relative_to(ROOT)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, dest)
                copied += 1

    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel in SKIP_FILES:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix not in SUFFIXES and not path.name.endswith(".openapi.yaml"):
            continue
        dest = OUT / path.relative_to(ROOT)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)
        copied += 1

    print(f"Copied {copied} artifact files into {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
