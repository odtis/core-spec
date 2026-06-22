#!/usr/bin/env python3
"""Bump ODTIS VERSION (semver minor by default for site releases)."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = ROOT / "VERSION"

VERSION_RE = re.compile(
    r"^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)(?P<suffix>[-.].*)?$"
)


def parse_version(raw: str) -> tuple[int, int, int, str]:
    m = VERSION_RE.match(raw.strip())
    if not m:
        raise ValueError(f"unsupported VERSION format: {raw!r} (expected X.Y.Z or X.Y.Z-suffix)")
    return (
        int(m.group("major")),
        int(m.group("minor")),
        int(m.group("patch")),
        m.group("suffix") or "",
    )


def format_version(major: int, minor: int, patch: int, suffix: str) -> str:
    return f"{major}.{minor}.{patch}{suffix}"


def bump_minor(version: str) -> str:
    major, minor, patch, suffix = parse_version(version)
    return format_version(major, minor + 1, 0, suffix)


def main() -> int:
    parser = argparse.ArgumentParser(description="Bump VERSION for ODTIS site releases")
    parser.add_argument("--minor", action="store_true", help="Bump semver minor (Y), reset patch to 0")
    parser.add_argument("--write", action="store_true", help="Write VERSION file")
    parser.add_argument("--dry-run", action="store_true", help="Print only; do not write")
    args = parser.parse_args()

    if not VERSION_FILE.is_file():
        print(f"ERROR: missing {VERSION_FILE}", file=sys.stderr)
        return 1

    current = VERSION_FILE.read_text(encoding="utf-8").strip()
    if not args.minor:
        print(current)
        return 0

    new_version = bump_minor(current)
    print(f"{current} -> {new_version}")

    if args.write and not args.dry_run:
        VERSION_FILE.write_text(new_version + "\n", encoding="utf-8")
        print(f"Wrote {VERSION_FILE}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
