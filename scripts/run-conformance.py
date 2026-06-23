#!/usr/bin/env python3
"""Run ODTIS conformance suite (L1 structural + profile reports)."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry/requirements.json"
MANIFEST = ROOT / "conformance/manifest.yaml"

VENV_PYTHON = ROOT / ".venv-site" / "bin" / "python"
PYTHON = str(VENV_PYTHON) if VENV_PYTHON.is_file() else sys.executable

VALIDATORS = [
    "scripts/validate-registry.py",
    "scripts/validate-section-completeness.py",
    "scripts/validate-openapi.py",
    "scripts/pin-annex-a-checksums.py",
    "scripts/validate-threats.py",
    "scripts/validate-standards-mapping.py",
    "scripts/validate-extended-annex.py",
    "scripts/validate-reliance-annex.py",
    "scripts/validate-conformance-statement.py",
    "scripts/validate-ri-map.py",
]


def run_script(rel_path: str, extra: list[str] | None = None) -> tuple[bool, str]:
    cmd = [PYTHON, str(ROOT / rel_path)] + (extra or [])
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    out = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode == 0, out.strip()


def check_registry_links() -> tuple[bool, list[str]]:
    errors: list[str] = []
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    for r in data.get("requirements", []):
        ct = r.get("conformance_test")
        if not ct:
            continue
        path = ROOT / ct
        if not path.is_file():
            errors.append(f"{r['id']}: missing test file {ct}")
    return len(errors) == 0, errors


def parse_profile_blocks(manifest_text: str) -> dict[str, dict]:
    if "profiles:" not in manifest_text:
        return {}
    section = manifest_text.split("profiles:", 1)[1]
    profiles: dict[str, dict] = {}
    current: str | None = None
    for line in section.splitlines():
        m_pid = __import__("re").match(r"^  ([a-z-]+):\s*$", line)
        if m_pid:
            current = m_pid.group(1)
            profiles[current] = {"tests": [], "coverage_pct": 0, "missing_total": 0}
            continue
        if current and line.strip().startswith("coverage_pct:"):
            profiles[current]["coverage_pct"] = float(line.split(":", 1)[1].strip())
        if current and line.strip().startswith("missing_total:"):
            profiles[current]["missing_total"] = int(line.split(":", 1)[1].strip())
        if current and line.strip().startswith("- path:"):
            path = line.split(":", 1)[1].strip()
            profiles[current]["tests"].append(path)
    return profiles


def main() -> int:
    parser = argparse.ArgumentParser(description="ODTIS conformance runner")
    parser.add_argument("--profile", help="Filter report to one profile id")
    parser.add_argument("--level", default="L1", choices=["L1", "L2", "L3"])
    parser.add_argument("--check-links", action="store_true", help="Only verify registry test paths")
    parser.add_argument("--json", action="store_true", help="Emit JSON report")
    parser.add_argument("--rebuild", action="store_true", help="Regenerate manifest before run")
    parser.add_argument("--target", help="Base URL for L2 live checks (IdP realm URL)")
    args = parser.parse_args()

    if args.rebuild:
        ok, out = run_script("scripts/build-conformance-manifest.py")
        if not ok:
            print(out, file=sys.stderr)
            return 1

    results: list[dict] = []
    failed = 0

    if args.check_links:
        ok, errors = check_registry_links()
        if not ok:
            for e in errors:
                print(f"ERROR: {e}", file=sys.stderr)
            return 1
        print("OK: all registry conformance_test paths exist")
        return 0

    for script in VALIDATORS:
        ok, out = run_script(script)
        results.append({"id": Path(script).stem, "passed": ok, "output": out})
        if not ok:
            failed += 1
            print(out, file=sys.stderr)

    ok_links, link_errors = check_registry_links()
    results.append({"id": "registry-test-links", "passed": ok_links, "output": "\n".join(link_errors)})
    if not ok_links:
        failed += 1
        for e in link_errors:
            print(f"ERROR: {e}", file=sys.stderr)

    profile_summary: dict = {}
    if MANIFEST.is_file():
        profile_summary = parse_profile_blocks(MANIFEST.read_text(encoding="utf-8"))

    if args.level == "L2":
        l2_args = [sys.executable, str(ROOT / "conformance/l2/run_l2.py")]
        if args.target:
            l2_args.extend(["--target", args.target])
        proc = subprocess.run(l2_args, capture_output=True, text=True, cwd=ROOT)
        l2_ok = proc.returncode == 0
        results.append({"id": "l2-automated", "passed": l2_ok, "output": (proc.stdout or proc.stderr or "").strip()})
        if not l2_ok:
            failed += 1
            print(proc.stdout or proc.stderr, file=sys.stderr)

    report = {
        "odtis_version": Path(ROOT / "VERSION").read_text().strip() if (ROOT / "VERSION").is_file() else "unknown",
        "level": args.level,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "structural_tests": results,
        "passed": failed == 0,
        "profiles": profile_summary,
    }

    if args.profile and args.profile in profile_summary:
        report["profile_filter"] = args.profile
        report["profile"] = profile_summary[args.profile]

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        status = "PASS" if failed == 0 else "FAIL"
        label = args.level
        print(f"ODTIS conformance {label}: {status} ({len(results) - failed}/{len(results)} checks)")
        if profile_summary:
            print("\nProfile test coverage (stub/manual):")
            for pid, info in sorted(profile_summary.items()):
                if args.profile and pid != args.profile:
                    continue
                print(
                    f"  {pid}: {len(info.get('tests', []))} tests, "
                    f"{info.get('coverage_pct', 0)}% req stubs, "
                    f"{info.get('missing_total', 0)} reqs without test"
                )
        if args.level == "L1":
            print("\nNote: L1 validates repository integrity only. Use --level L2 [--target URL] for automated API/OIDC checks.")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
