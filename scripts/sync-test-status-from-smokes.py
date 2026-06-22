#!/usr/bin/env python3
"""Sync conformance test Status fields from smoke script PASS results."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TESTS_DIR = ROOT / "conformance/tests"
MAP_FILE = ROOT / "conformance/smoke-test-map.yaml"
REGISTRY = ROOT / "registry/requirements.json"
EVIDENCE_OUT = ROOT / "implementation/evidence/smoke-sync/last-run.yaml"

STATUS_LINE = re.compile(r"^\*\*Status:\*\*\s*(.+)\s*$", re.M)
TEST_PATH_RE = re.compile(r"conformance/tests/[^\s\\]+\.md")
ODTIS_ID_RE = re.compile(r"ODTIS-\d{4}")
ODTIS_RANGE_RE = re.compile(r"ODTIS-(\d{4})\.\.(\d{4})")
IMPLEMENTED = "implemented (static + unit smoke)"


def parse_yaml_smokes(text: str) -> list[dict]:
    """Minimal parser for conformance/smoke-test-map.yaml smokes list."""
    entries: list[dict] = []
    current: dict | None = None
    list_key: str | None = None

    for raw in text.splitlines():
        line = raw.rstrip()
        if not line or line.strip().startswith("#"):
            continue
        if line.startswith("  - script:"):
            if current:
                entries.append(current)
            current = {"script": line.split(":", 1)[1].strip(), "tests": [], "odtis_ids": []}
            list_key = None
            continue
        if current is None:
            continue
        if line.strip() == "tests:":
            list_key = "tests"
            continue
        if line.strip() == "odtis_ids:":
            list_key = "odtis_ids"
            continue
        if list_key and line.strip().startswith("- "):
            current[list_key].append(line.strip()[2:].strip())
    if current:
        entries.append(current)
    return entries


def expand_odtis_tokens(text: str) -> set[str]:
    ids: set[str] = set()
    normalized = text.replace("-", "..").replace(" - ", "..")
    for m in ODTIS_RANGE_RE.finditer(normalized):
        start, end = int(m.group(1)), int(m.group(2))
        for n in range(start, end + 1):
            ids.add(f"ODTIS-{n:04d}")
    for m in ODTIS_ID_RE.finditer(normalized):
        ids.add(m.group(0))
    return ids


def load_registry() -> dict[str, str]:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    return {
        r["id"]: r["conformance_test"]
        for r in data.get("requirements", [])
        if r.get("conformance_test")
    }


def extract_explicit_tests(script_path: Path) -> list[str]:
    if not script_path.is_file():
        return []
    return sorted(set(TEST_PATH_RE.findall(script_path.read_text(encoding="utf-8"))))


def header_odtis(script_path: Path) -> set[str]:
    if not script_path.is_file():
        return set()
    head = "\n".join(script_path.read_text(encoding="utf-8").splitlines()[:6])
    return expand_odtis_tokens(head)


def resolve_tests(
    script: str,
    explicit: list[str],
    odtis_ids: list[str],
    by_id: dict[str, str],
) -> list[str]:
    tests = set(explicit)
    script_path = ROOT / script if not script.startswith("../") else (ROOT / script).resolve()
    tests.update(extract_explicit_tests(script_path))
    ids = set(odtis_ids) | header_odtis(script_path)
    for rid in ids:
        path = by_id.get(rid)
        if path:
            tests.add(path)
    return sorted(tests)


def discover_smokes(manual: list[dict]) -> list[dict]:
    manual_by_script = {e["script"]: e for e in manual}
    discovered: dict[str, dict] = {}

    for path in sorted((ROOT / "conformance").glob("run-*-checks.sh")):
        if path.name == "run-gap-closure-checks.sh":
            continue
        rel = str(path.relative_to(ROOT))
        entry = manual_by_script.get(rel, {"script": rel, "tests": [], "odtis_ids": []})
        discovered[rel] = {
            "script": rel,
            "tests": entry.get("tests", []),
            "odtis_ids": entry.get("odtis_ids", []),
        }

    for rel, entry in manual_by_script.items():
        if rel not in discovered:
            discovered[rel] = entry

    return sorted(discovered.values(), key=lambda e: e["script"])


def run_smoke(script: str) -> bool:
    path = (ROOT / script).resolve() if not script.startswith("../") else (ROOT / script).resolve()
    if not path.is_file():
        print(f"WARN: smoke script missing: {script}", file=sys.stderr)
        return False
    print(f"RUN: {script}")
    result = subprocess.run(["bash", str(path)], cwd=ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        return False
    return True


def update_test_status(test_rel: str, dry_run: bool) -> bool:
    path = ROOT / test_rel
    if not path.is_file():
        print(f"WARN: missing test file: {test_rel}", file=sys.stderr)
        return False
    text = path.read_text(encoding="utf-8")
    m = STATUS_LINE.search(text)
    if not m:
        print(f"WARN: no Status line in {test_rel}", file=sys.stderr)
        return False
    current = m.group(1).strip()
    if current.startswith("implemented"):
        return False
    new_text = STATUS_LINE.sub(f"**Status:** {IMPLEMENTED}", text, count=1)
    if dry_run:
        print(f"  would mark: {test_rel}")
        return True
    path.write_text(new_text, encoding="utf-8")
    print(f"  marked: {test_rel}")
    return True


def write_evidence(results: list[dict]) -> None:
    EVIDENCE_OUT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"as_of: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        "generator: scripts/sync-test-status-from-smokes.py",
        "smokes:",
    ]
    for row in results:
        lines.append(f"  - script: {row['script']}")
        lines.append(f"    ok: {str(row['ok']).lower()}")
        lines.append(f"    tests: [{', '.join(row['tests'])}]")
    EVIDENCE_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", action="store_true", help="Execute smoke scripts before syncing")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing")
    parser.add_argument("--assume-pass", action="store_true", help="Mark tests without running smokes")
    args = parser.parse_args()

    if not REGISTRY.is_file():
        print(f"ERROR: missing {REGISTRY}", file=sys.stderr)
        return 1

    manual = parse_yaml_smokes(MAP_FILE.read_text(encoding="utf-8")) if MAP_FILE.is_file() else []
    smokes = discover_smokes(manual)
    by_id = load_registry()

    passed_tests: set[str] = set()
    results: list[dict] = []

    for entry in smokes:
        script = entry["script"]
        tests = resolve_tests(script, entry.get("tests", []), entry.get("odtis_ids", []), by_id)
        ok = True
        if args.run:
            ok = run_smoke(script)
        elif not args.assume_pass:
            print(f"SKIP run: {script} ({len(tests)} tests)  -  use --run or --assume-pass")
            results.append({"script": script, "ok": False, "tests": tests})
            continue
        results.append({"script": script, "ok": ok, "tests": tests})
        if ok:
            passed_tests.update(tests)

    updated = 0
    for test_rel in sorted(passed_tests):
        if update_test_status(test_rel, args.dry_run):
            updated += 1

    if not args.dry_run:
        write_evidence(results)

    total_tests = len(list(TESTS_DIR.rglob("*.md"))) - len(list(TESTS_DIR.rglob("README.md")))
    print(
        f"\nSmoke sync: {len(passed_tests)} tests linked; "
        f"{updated} status lines updated"
    )
    if args.dry_run:
        return 0
    if args.run or args.assume_pass:
        return 0
    print("No action taken  -  pass --run or --assume-pass", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
