#!/usr/bin/env python3
"""Gate: all ODTIS profiles must have 100% conformance test stub coverage."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "conformance/manifest.yaml"
MIN_COVERAGE = 100.0


def parse_manifest(text: str) -> dict[str, dict]:
    if "profiles:" not in text:
        return {}
    section = text.split("profiles:", 1)[1]
    profiles: dict[str, dict] = {}
    current: str | None = None
    for line in section.splitlines():
        m = re.match(r"^  ([a-z-]+):\s*$", line)
        if m:
            current = m.group(1)
            profiles[current] = {}
            continue
        if not current:
            continue
        for key in ("requirement_count", "test_count", "covered_requirements", "missing_total", "coverage_pct"):
            if line.strip().startswith(f"{key}:"):
                val = line.split(":", 1)[1].strip()
                if key in ("requirement_count", "test_count", "covered_requirements", "missing_total"):
                    profiles[current][key] = int(val)
                else:
                    profiles[current][key] = float(val)
    return profiles


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate conformance manifest coverage")
    parser.add_argument("--min-coverage", type=float, default=MIN_COVERAGE)
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    args = parser.parse_args()

    if not args.manifest.is_file():
        print(f"ERROR: missing {args.manifest}", file=sys.stderr)
        return 1

    profiles = parse_manifest(args.manifest.read_text(encoding="utf-8"))
    if not profiles:
        print("ERROR: no profiles in manifest", file=sys.stderr)
        return 1

    errors: list[str] = []
    for pid, info in sorted(profiles.items()):
        cov = info.get("coverage_pct", 0.0)
        missing = info.get("missing_total", 999)
        if cov < args.min_coverage:
            errors.append(f"{pid}: coverage {cov}% < {args.min_coverage}%")
        if missing > 0:
            errors.append(f"{pid}: {missing} requirements without test stub")

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    total_tests = sum(p.get("test_count", 0) for p in profiles.values())
    print(
        f"OK: manifest coverage gate passed ({len(profiles)} profiles @ "
        f"{args.min_coverage}%+, {total_tests} tests)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
