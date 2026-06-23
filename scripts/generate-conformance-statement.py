#!/usr/bin/env python3
"""Generate machine + human ODTIS conformance statements from registry."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = ROOT / "VERSION"
MANIFEST = ROOT / "conformance/manifest.yaml"

sys.path.insert(0, str(ROOT / "scripts"))
from profile_registry import (  # noqa: E402
    load_requirements,
    parse_profiles_yaml,
    profile_requirement_ids,
    reliance_requirement_ids,
)


def spec_version() -> str:
    return VERSION_FILE.read_text(encoding="utf-8").strip() if VERSION_FILE.is_file() else "0.9.0-draft"


def requirement_ids_for_profiles(
    profile_ids: list[str],
    extended_modules: list[str] | None = None,
    reliance_modules: list[str] | None = None,
) -> list[str]:
    reqs = load_requirements()
    profiles = {p["id"]: p for p in parse_profiles_yaml()}
    ids: set[str] = set()
    for pid in profile_ids:
        if pid not in profiles:
            raise ValueError(f"unknown profile: {pid}")
        if pid == "reliance-extensions":
            declared = list(reliance_modules or [])
            if "R-Base" not in declared:
                declared = ["R-Base"] + declared
            ids.update(reliance_requirement_ids(declared))
            continue
        ids.update(profile_requirement_ids(profiles[pid], reqs))
    return sorted(ids)


def manifest_summary(profile_ids: list[str], req_ids: list[str], level: str) -> dict:
    text = MANIFEST.read_text(encoding="utf-8") if MANIFEST.is_file() else ""
    blocks: dict[str, dict] = {}
    current: str | None = None
    for line in text.splitlines():
        m = __import__("re").match(r"^  ([a-z-]+):\s*$", line)
        if m:
            current = m.group(1)
            blocks[current] = {"test_count": 0, "coverage_pct": 0.0}
            continue
        if current and line.strip().startswith("test_count:"):
            blocks[current]["test_count"] = int(line.split(":", 1)[1].strip())
        if current and line.strip().startswith("coverage_pct:"):
            blocks[current]["coverage_pct"] = float(line.split(":", 1)[1].strip())

    total_tests = sum(blocks.get(p, {}).get("test_count", 0) for p in profile_ids)
    coverages = [blocks.get(p, {}).get("coverage_pct", 0) for p in profile_ids if p in blocks]
    min_cov = min(coverages) if coverages else 0.0
    if level == "L3":
        status = "pass"
        pending = []
    elif level == "L2":
        status = "partial"
        pending = list(req_ids)
    else:
        status = "partial"
        pending = list(req_ids)
    profile_label = ", ".join(profile_ids)
    return {
        "suite_version": spec_version(),
        "status": status,
        "summary": (
            f"{level} conformance package ({profile_label}); "
            f"{total_tests} linked tests; min stub coverage {min_cov}%; "
            f"see l2-report.md for automated results"
        ),
        "pending_test_ids": pending,
    }


def build_statement(args: argparse.Namespace) -> dict:
    profiles = list(args.profile)
    if "reference-architecture" not in profiles:
        profiles.insert(0, "reference-architecture")

    req_ids = requirement_ids_for_profiles(
        profiles,
        extended_modules=list(args.extended_module or []),
        reliance_modules=list(args.reliance_module or []),
    )
    return {
        "odtis_version": spec_version(),
        "profiles": profiles,
        "extended_modules": list(args.extended_module or []),
        "reliance_extensions": list(args.reliance_module or []),
        "level": args.level,
        "operator": args.operator,
        "scope": {
            "environment": args.environment,
            "jurisdiction": args.jurisdiction,
            "deployment_phase": args.deployment_phase,
        },
        "requirements": req_ids,
        "tests": manifest_summary(profiles, req_ids, args.level),
        "date": args.date or str(date.today()),
        "contact": args.contact,
    }


def render_markdown(data: dict) -> str:
    scope = data.get("scope") or {}
    tests = data.get("tests") or {}
    profiles = ", ".join(data.get("profiles") or [])
    extended = ", ".join(data.get("extended_modules") or []) or "(none)"
    reliance = ", ".join(data.get("reliance_extensions") or []) or "(none)"
    req_count = len(data.get("requirements") or [])

    lines = [
        "# ODTIS conformance statement",
        "",
        f"**Status:** review draft - machine-readable source: `conformance-statement.yaml`",
        "",
        "Normative fields per ODTIS section 1.9.1 (`ODTIS-0008`, `ODTIS-0534`).",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| `odtis_version` | {data.get('odtis_version', '')} |",
        f"| `profiles` | {profiles} |",
        f"| `extended_modules` | {extended} |",
        f"| `reliance_extensions` | {reliance} |",
        f"| `level` | {data.get('level', '')} |",
        f"| `operator` | {data.get('operator', '')} |",
        f"| `environment` | {scope.get('environment', '')} |",
        f"| `jurisdiction` | {scope.get('jurisdiction', '')} |",
        f"| `deployment_phase` | {scope.get('deployment_phase', '')} |",
        f"| `requirements` | {req_count} ODTIS IDs (see YAML) |",
        f"| `tests.status` | {tests.get('status', '')} |",
        f"| `tests.summary` | {tests.get('summary', '')} |",
        f"| `date` | {data.get('date', '')} |",
        f"| `contact` | {data.get('contact', '')} |",
        "",
        "## Profiles declared",
        "",
    ]
    for pid in data.get("profiles") or []:
        lines.append(f"- `{pid}`")
    scope = data.get("scope") or {}
    if scope.get("deployment_phase") == 1 and not (data.get("extended_modules") or []):
        lines.extend(
            [
                "",
                "## ODTIS-0533  -  Phase 1 scope",
                "",
                "This Phase 1 statement declares **Core Identity only** (`core-identity` profile). "
                "No Annex D optional sub-modules are declared in this statement.",
                "",
            ]
        )
    reliance = data.get("reliance_extensions") or []
    if reliance:
        rel_label = ", ".join(reliance)
        lines.extend(
            [
                "",
                "## ODTIS-0708  -  Reliance Extensions scope",
                "",
                f"**Active Reliance Extension sub-modules:** {rel_label}.",
                "",
                "Capa B reliance overlays MUST NOT weaken Core Identity, Trust Network, Federation, "
                "or Operator requirements (`ODTIS-0707`).",
                "",
            ]
        )
    if scope.get("deployment_phase") == 2 and "trust-network" in (data.get("profiles") or []):
        lines.extend(
            [
                "",
                "## ODTIS-0532  -  Phase 2 scope",
                "",
                "This Phase 2 statement declares **Core Identity + Trust Network** "
                "(`core-identity`, `trust-network`). Federation and Extended sub-modules "
                "are not declared unless explicitly listed in `extended_modules`.",
                "",
            ]
        )
    if scope.get("deployment_phase") == 3:
        ext = data.get("extended_modules") or []
        ext_label = ", ".join(ext) if ext else "(none active in production)"
        lines.extend(
            [
                "",
                "## ODTIS-0532  -  Phase 3 scope",
                "",
                "This Phase 3 statement declares **Core Identity + Trust Network + Operator** "
                "(`core-identity`, `trust-network`, `operator`) at **L2-L3** operator maturity.",
                "",
                f"**Active Extended sub-modules:** {ext_label}.",
                "",
                "**Prep (not activated in production):** E-Registry adapter (`eregistry-adapter`, "
                "`venid.eregistry.active=false`); federation agreements store (P3-E08, "
                "`app.exchange.federation.enabled=false`).",
                "",
                "National LoA and federated routing MUST NOT be claimed while prep modules remain inactive.",
                "",
            ]
        )
    if scope.get("deployment_phase") == 4:
        ext = data.get("extended_modules") or []
        ext_label = ", ".join(ext) if ext else "(none)"
        level = data.get("level", "")
        lines.extend(
            [
                "",
                "## ODTIS-0532  -  Phase 4 scope",
                "",
                "This Phase 4 statement declares **Core Identity + Trust Network + Federation + Operator + Extended** "
                f"at **{level}** operator maturity target.",
                "",
                f"**Declared Extended sub-modules:** {ext_label}.",
                "",
                "Extended modules are implemented as **sandbox partial** (`venid.*.active=false` by default). "
                "Federation runtime, OID4VP wallet, inclusion, webhook, signature, and KYB preview services "
                "are listed for honest Phase 4 scope declaration (ODTIS-0532).",
                "",
                "**ODTIS-0006:** Extended capabilities MUST NOT weaken Core Identity, Trust Network, or Federation "
                "MUST requirements. See `conformance/run-extended-no-weakening-checks.sh`.",
                "",
                "**Pending:** third-party Operator L3 attestation; production activation of declared Extended modules.",
                "",
            ]
        )
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- Regenerate: `python3 scripts/generate-conformance-statement.py`",
            "- Validate: `python3 scripts/validate-conformance-statement.py`",
            "",
        ]
    )
    return "\n".join(lines)


def write_outputs(data: dict, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    yaml_path = out_dir / "conformance-statement.yaml"
    md_path = out_dir / "conformance-statement.md"

    try:
        import yaml  # type: ignore

        yaml_text = "# ODTIS conformance statement - generated\n"
        yaml_text += yaml.dump(data, sort_keys=False, allow_unicode=True)
    except ImportError:
        yaml_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    else:
        yaml_path.write_text(yaml_text, encoding="utf-8")

    md_path.write_text(render_markdown(data), encoding="utf-8")
    yaml_rel = yaml_path.resolve().relative_to(ROOT.resolve())
    md_rel = md_path.resolve().relative_to(ROOT.resolve())
    print(f"Wrote {yaml_rel}")
    print(f"Wrote {md_rel}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate ODTIS conformance statement")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "implementation/statements/venid-sandbox",
    )
    parser.add_argument(
        "--profile",
        action="append",
        dest="profile",
        default=None,
        help="Profile id (repeatable)",
    )
    parser.add_argument("--extended-module", action="append", dest="extended_module")
    parser.add_argument("--reliance-module", action="append", dest="reliance_module")
    parser.add_argument("--level", default="L1", choices=["L1", "L2", "L3"])
    parser.add_argument("--operator", default="FinnectOS VenID Lab")
    parser.add_argument(
        "--environment",
        default="laboratory",
        choices=["laboratory", "sandbox", "staging", "production"],
    )
    parser.add_argument("--jurisdiction", default="VE")
    parser.add_argument("--deployment-phase", type=int, default=1, choices=[1, 2, 3, 4])
    parser.add_argument("--contact", default="conformance@odtis.org")
    parser.add_argument("--date", help="YYYY-MM-DD (default: today)")
    args = parser.parse_args()
    if not args.profile:
        args.profile = ["reference-architecture"]

    if not MANIFEST.is_file():
        print("WARN: manifest missing; run build-conformance-manifest.py first", file=sys.stderr)

    try:
        data = build_statement(args)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    write_outputs(data, args.out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
