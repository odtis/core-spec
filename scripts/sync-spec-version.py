#!/usr/bin/env python3
"""Synchronize ODTIS spec_version across repository artifacts from VERSION file."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = ROOT / "VERSION"

PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"^(\|\s*\*\*Spec version\*\*\s*\|\s*)([^\|]+)(\s*\|.*)$"), "md_spec_table"),
    (re.compile(r"^(\*\*Spec version\*\*\s*\|\s*)([^\|]+)(\s*\|.*)$"), "md_spec"),
    (re.compile(r"^(\*\*Version:\*\*\s*)(.+)$"), "md_index"),
    (re.compile(r'^(spec_version:\s*")([^"]+)(".*)$'), "yaml"),
    (re.compile(r'^(program_version:\s*")([^"]+)(".*)$'), "yaml"),
    (re.compile(r"^(version:\s*)([^\s]+)\s*$"), "cff"),
]


def read_version() -> str:
    return VERSION_FILE.read_text(encoding="utf-8").strip()


def file_needs_update(path: Path, version: str) -> bool:
    if path.suffix == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        return data.get("spec_version") != version
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        for pat, _ in PATTERNS:
            m = pat.match(line)
            if m and len(m.groups()) >= 2:
                current = m.group(2).strip()
                if current != version:
                    return True
    return False


def update_file(path: Path, version: str) -> bool:
    if path.suffix == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("spec_version") == version:
            return False
        data["spec_version"] = version
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return True

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    changed = False
    new_lines: list[str] = []
    for line in lines:
        updated = line
        for pat, _ in PATTERNS:
            m = pat.match(line)
            if m:
                if len(m.groups()) == 3:
                    updated = f"{m.group(1)}{version}{m.group(3)}"
                else:
                    updated = f"{m.group(1)}{version}"
                break
        if updated != line:
            changed = True
        new_lines.append(updated)
    if changed:
        path.write_text("\n".join(new_lines) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")
    return changed


def targets() -> list[Path]:
    paths: list[Path] = [
        ROOT / "registry/requirements.json",
        ROOT / "registry/profiles.yaml",
        ROOT / "registry/terminology.yaml",
        ROOT / "registry/events.yaml",
        ROOT / "conformance/manifest.yaml",
        ROOT / "traceability/rf-index.yaml",
        ROOT / "traceability/rf-overrides.yaml",
        ROOT / "traceability/coverage-report.yaml",
        ROOT / "traceability/section-coverage.yaml",
        ROOT / "governance/REVIEW-LOG.yaml",
        ROOT / "implementation/RI-MAP.yaml",
        ROOT / "conformance/certification/program.yaml",
        ROOT / "conformance/certification/certified-products.yaml",
        ROOT / "spec/INDEX.md",
        ROOT / "publication/CITATION.cff",
        ROOT / "annexes/A-openapi-registry/INDEX.yaml",
        ROOT / "registry/README.md",
    ]
    for sub in ("B-threat-mitigations", "C-standards-mapping", "D-extended-profiles"):
        paths.extend((ROOT / "annexes" / sub).glob("*.yaml"))
    paths.extend((ROOT / "spec").glob("*/SPEC.md"))
    paths.extend((ROOT / "annexes").glob("**/README.md"))
    return sorted({p for p in paths if p.is_file()})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    version = read_version()
    stale: list[str] = []

    for path in targets():
        rel = str(path.relative_to(ROOT))
        if file_needs_update(path, version):
            stale.append(rel)
            if not args.check:
                update_file(path, version)
                print(f" synced {rel}")

    if not args.check and stale:
        subprocess.run(
            [sys.executable, str(ROOT / "scripts/build-conformance-manifest.py")],
            cwd=ROOT,
            check=False,
        )

    if args.check:
        if stale:
            print(f"FAIL - expected {version!r} in:")
            for s in stale:
                print(f" - {s}")
            return 1
        print(f"OK ({version})")
        return 0

    print(f"Done - version {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
