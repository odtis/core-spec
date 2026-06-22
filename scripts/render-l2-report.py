#!/usr/bin/env python3
"""Render human-readable L2 report markdown from JSON + conformance statement."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_statement_profiles(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    if path.suffix in (".yaml", ".yml"):
        try:
            import yaml  # type: ignore

            data = yaml.safe_load(text)
        except ImportError:
            data = json.loads(text)
    else:
        data = json.loads(text)
    return list(data.get("profiles") or [])


def load_statement_meta(path: Path) -> tuple[int | None, list[str]]:
    text = path.read_text(encoding="utf-8")
    if path.suffix in (".yaml", ".yml"):
        try:
            import yaml  # type: ignore

            data = yaml.safe_load(text)
        except ImportError:
            data = json.loads(text)
    else:
        data = json.loads(text)
    scope = data.get("scope") or {}
    phase = scope.get("deployment_phase")
    return phase, list(data.get("profiles") or [])


def report_title(statement: Path) -> str:
    phase, profiles = load_statement_meta(statement)
    label = f"Phase {phase}" if phase else "L2"
    if "trust-network" in profiles:
        return f"ODTIS L2 test report  -  {label} Core Identity + Trust Network"
    if "core-identity" in profiles:
        return f"ODTIS L2 test report  -  {label} Core Identity"
    return f"ODTIS L2 test report  -  {label}"


def regenerate_hint(statement: Path) -> str:
    phase, _ = load_statement_meta(statement)
    if phase == 2:
        return "./conformance/run-phase2-package.sh"
    if phase == 1:
        return "./conformance/run-phase1-package.sh"
    return "./conformance/l2/run_l2.py"


def render(statement: Path, l2: dict) -> str:
    profiles = load_statement_meta(statement)[1]
    lines = [
        f"# {report_title(statement)}",
        "",
        f"**Status:** {l2.get('status', 'UNKNOWN')}",
        f"**Passed:** {l2.get('passed', 0)}/{l2.get('total', 0)}",
        f"**Target:** {l2.get('target') or '(spec-only; set ODTIS_TARGET for live checks)'}",
        f"**ODTIS version:** {l2.get('odtis_version', '')}",
        "",
        "## Profiles covered",
        "",
    ]
    for pid in profiles:
        lines.append(f"- `{pid}`")
    lines.extend(["", "## Automated results", ""])
    for result in l2.get("results") or []:
        mark = "PASS" if result.get("ok") else "FAIL"
        if result.get("informational"):
            mark = "INFO"
        req = result.get("requirement", "-")
        lines.append(f"- **{mark}** `{result.get('id')}` ({req}): {result.get('detail')}")
    lines.extend(
        [
            "",
            "## Manual evidence (pending)",
            "",
            "Remaining procedures are listed in `conformance-statement.yaml` "
            "under `tests.pending_test_ids`. Execute against staging sandbox and attach logs.",
            "",
            f"Regenerate: `{regenerate_hint(statement)}`",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render L2 report markdown")
    parser.add_argument("--statement", type=Path, required=True)
    parser.add_argument("--l2", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if not args.l2.is_file():
        print(f"ERROR: L2 report not found: {args.l2}", file=sys.stderr)
        return 1

    md = render(args.statement, load_json(args.l2))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(md, encoding="utf-8")
    print(f"Wrote {args.output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
