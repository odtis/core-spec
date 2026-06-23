#!/usr/bin/env python3
"""Validate ODTIS conformance statements (ODTIS-0008, ODTIS-0532, ODTIS-0534)."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = ROOT / "VERSION"

sys.path.insert(0, str(ROOT / "scripts"))
from profile_registry import (  # noqa: E402
    parse_profiles_yaml,
    parse_reliance_phase_minimum,
    parse_reliance_submodule_ids,
)

REQUIRED_TOP = (
    "odtis_version",
    "profiles",
    "extended_modules",
    "reliance_extensions",
    "level",
    "operator",
    "scope",
    "requirements",
    "tests",
    "date",
    "contact",
)

REQUIRED_SCOPE = ("environment", "jurisdiction", "deployment_phase")
REQUIRED_TESTS = ("suite_version", "status", "summary")
VALID_LEVELS = {"L1", "L2", "L3"}
VALID_ENVIRONMENTS = {"laboratory", "sandbox", "staging", "production"}
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MD_FIELD_PATTERN = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*(.+?)\s*\|\s*$")

PROHIBITED_CLAIM_PATTERNS = [
    (re.compile(r"\bODTIS\s+certified\b", re.I), "ODTIS-0007: prohibited claim without L3 program"),
    (re.compile(r"\beIDAS\s+compliant\b", re.I), "ODTIS-0007: eIDAS claim from ODTIS alone"),
    (re.compile(r"\bQTSP\s+equivalent\b", re.I), "ODTIS-0007: QTSP equivalence from ODTIS alone"),
    (re.compile(r"\bFull\s+ODTIS\b", re.I), "ODTIS-0007: Full ODTIS without listing all profiles"),
]

IMPLIED_PROFILE_HINTS = [
    ("trust network", "trust-network"),
    ("federation", "federation"),
    ("operator profile", "operator"),
    ("extended module", "extended"),
    ("e-wallet", "extended"),
    ("e-registry", "extended"),
    ("reliance extension", "reliance-extensions"),
    ("r-agent", "reliance-extensions"),
    ("capa b", "reliance-extensions"),
]


def load_statement(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if path.suffix in (".yaml", ".yml"):
        try:
            import yaml  # type: ignore

            data = yaml.safe_load(text)
        except ImportError:
            data = json.loads(text)
    elif path.suffix == ".json":
        data = json.loads(text)
    else:
        raise ValueError(f"unsupported format: {path.suffix}")
    if not isinstance(data, dict):
        raise ValueError("statement root must be a mapping")
    return data


def valid_profile_ids() -> set[str]:
    return {p["id"] for p in parse_profiles_yaml()}


def valid_reliance_module_ids() -> set[str]:
    return parse_reliance_submodule_ids()


def valid_extended_module_ids() -> set[str]:
    path = ROOT / "annexes/D-extended-profiles/sub-modules.yaml"
    ids: set[str] = set()
    if not path.is_file():
        return ids
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^- id:\s*(.+)$", line.strip())
        if m:
            ids.add(m.group(1).strip())
    return ids


def parse_markdown_fields(md_path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    in_table = False
    for line in md_path.read_text(encoding="utf-8").splitlines():
        if line.strip() == "| Field | Value |":
            in_table = True
            continue
        if in_table:
            if line.strip().startswith("|---"):
                continue
            if not line.strip().startswith("|"):
                in_table = False
                continue
            m = MD_FIELD_PATTERN.match(line.strip())
            if m:
                fields[m.group(1)] = m.group(2).strip()
    return fields


def validate_statement(data: dict, *, spec_version: str) -> list[str]:
    errors: list[str] = []
    profiles_known = valid_profile_ids()
    extended_known = valid_extended_module_ids()

    for field in REQUIRED_TOP:
        if field not in data or data[field] in (None, ""):
            errors.append(f"missing required field: {field} (ODTIS-0008)")

    version = data.get("odtis_version")
    if version and version != spec_version:
        errors.append(
            f"odtis_version '{version}' != repository VERSION '{spec_version}'"
        )

    profiles = data.get("profiles")
    if profiles is not None:
        if not isinstance(profiles, list) or not profiles:
            errors.append("profiles must be a non-empty list")
        else:
            for pid in profiles:
                if pid not in profiles_known:
                    errors.append(f"unknown profile: {pid}")
            if "reference-architecture" not in profiles:
                errors.append(
                    "profiles must include reference-architecture for any ODTIS claim"
                )

    extended = data.get("extended_modules")
    if extended is not None:
        if not isinstance(extended, list):
            errors.append("extended_modules must be a list")
        else:
            for mod in extended:
                if mod not in extended_known:
                    errors.append(f"unknown extended module: {mod}")

    reliance_known = valid_reliance_module_ids()
    reliance = data.get("reliance_extensions")
    if reliance is not None:
        if not isinstance(reliance, list):
            errors.append("reliance_extensions must be a list")
        else:
            for mod in reliance:
                if mod not in reliance_known:
                    errors.append(f"unknown reliance extension module: {mod}")
    else:
        errors.append("missing required field: reliance_extensions (ODTIS-0008)")

    level = data.get("level")
    if level and level not in VALID_LEVELS:
        errors.append(f"level must be one of {sorted(VALID_LEVELS)}")

    scope = data.get("scope")
    if isinstance(scope, dict):
        for key in REQUIRED_SCOPE:
            if key not in scope or scope[key] in (None, ""):
                errors.append(f"scope.{key} required (ODTIS-0532)")
        env = str(scope.get("environment", "")).lower()
        if env and env not in VALID_ENVIRONMENTS:
            errors.append(
                f"scope.environment must be one of {sorted(VALID_ENVIRONMENTS)}"
            )
        phase = scope.get("deployment_phase")
        if phase is not None and phase not in (1, 2, 3, 4):
            errors.append("scope.deployment_phase must be 1, 2, 3, or 4")
    elif scope is not None:
        errors.append("scope must be a mapping")

    tests = data.get("tests")
    if isinstance(tests, dict):
        for key in REQUIRED_TESTS:
            if key not in tests or tests[key] in (None, ""):
                errors.append(f"tests.{key} required")
        status = str(tests.get("status", "")).lower()
        if status == "partial" and not tests.get("pending_test_ids"):
            errors.append(
                "tests.status partial requires pending_test_ids list (ODTIS-0010)"
            )
    elif tests is not None:
        errors.append("tests must be a mapping")

    date = data.get("date")
    if date and not DATE_PATTERN.match(str(date)):
        errors.append("date must be YYYY-MM-DD")

    reqs = data.get("requirements")
    if reqs is not None:
        if isinstance(reqs, list):
            for rid in reqs:
                if not re.match(r"^ODTIS-\d{4}$", str(rid)):
                    errors.append(f"invalid requirement id: {rid}")
        elif isinstance(reqs, str):
            if not reqs.strip():
                errors.append("requirements reference must be non-empty")
        else:
            errors.append("requirements must be a list of IDs or a reference string")

    return errors


def validate_profile_chain(profiles: list[str]) -> list[str]:
    errors: list[str] = []
    by_id = {p["id"]: p for p in parse_profiles_yaml()}
    declared = set(profiles)

    for pid in profiles:
        profile = by_id.get(pid)
        if not profile:
            continue
        for dep in profile.get("depends_on", []):
            if dep not in declared:
                errors.append(
                    f"profile {pid} depends on {dep} but {dep} not declared (ODTIS-0004)"
                )

    if "trust-network" in declared and "core-identity" not in declared:
        errors.append("ODTIS-0001: trust-network requires core-identity")
    if "federation" in declared and "trust-network" not in declared:
        errors.append("ODTIS-0002: federation requires trust-network")
    if "extended" in declared and "core-identity" not in declared:
        errors.append("extended profile requires core-identity")
    if "reliance-extensions" in declared and "core-identity" not in declared:
        errors.append("reliance-extensions profile requires core-identity")

    return errors


def validate_phase_reliance_rules(data: dict) -> list[str]:
    errors: list[str] = []
    scope = data.get("scope") or {}
    phase = scope.get("deployment_phase")
    reliance = data.get("reliance_extensions") or []
    profiles = data.get("profiles") or []
    if not reliance:
        return errors
    if "reliance-extensions" not in profiles:
        errors.append(
            "ODTIS-0708: active reliance_extensions require reliance-extensions profile"
        )
    if "R-Base" not in reliance:
        errors.append("ODTIS-0708: reliance_extensions MUST include R-Base when any module is declared")
    min_phase = parse_reliance_phase_minimum()
    if phase is not None:
        for mod in reliance:
            required = min_phase.get(mod)
            if required is not None and phase < required:
                errors.append(
                    f"ODTIS-0532: {mod} requires deployment phase {required}+ (statement phase {phase})"
                )
    return errors


def validate_phase_extended_rules(data: dict) -> list[str]:
    errors: list[str] = []
    scope = data.get("scope") or {}
    phase = scope.get("deployment_phase")
    extended = data.get("extended_modules") or []
    profiles = data.get("profiles") or []
    if phase == 1 and extended:
        errors.append(
            "ODTIS-0533: Phase 1 must not declare Extended sub-modules in production statement"
        )
    if phase == 2:
        if "trust-network" not in profiles:
            errors.append(
                "ODTIS-0532: Phase 2 statement must declare trust-network profile"
            )
        if "core-identity" not in profiles:
            errors.append(
                "ODTIS-0532: Phase 2 statement must declare core-identity profile"
            )
        if "federation" in profiles:
            errors.append(
                "ODTIS-0532: Phase 2 must not claim federation without explicit bilateral pilot scope"
            )
    if phase == 3:
        if "operator" not in profiles:
            errors.append(
                "ODTIS-0532: Phase 3 statement must declare operator profile"
            )
        if "trust-network" not in profiles:
            errors.append(
                "ODTIS-0532: Phase 3 statement must declare trust-network profile"
            )
        if "core-identity" not in profiles:
            errors.append(
                "ODTIS-0532: Phase 3 statement must declare core-identity profile"
            )
        if "federation" in profiles:
            errors.append(
                "ODTIS-0532: Phase 3 must not claim federation production profile (use prep evidence)"
            )
        level = data.get("level")
        if level not in ("L2", "L3"):
            errors.append(
                "ODTIS-0532: Phase 3 requires conformance level L2 or L3"
            )
        for mod in extended:
            if mod == "E-Registry":
                prep = (scope.get("extended_module_status") or {}).get("E-Registry")
                if prep == "inactive_prep":
                    continue
    if phase == 4:
        if "operator" not in profiles:
            errors.append(
                "ODTIS-0532: Phase 4 statement must declare operator profile"
            )
        if "trust-network" not in profiles:
            errors.append(
                "ODTIS-0532: Phase 4 statement must declare trust-network profile"
            )
        if "core-identity" not in profiles:
            errors.append(
                "ODTIS-0532: Phase 4 statement must declare core-identity profile"
            )
        if "federation" not in profiles:
            errors.append(
                "ODTIS-0532: Phase 4 statement must declare federation profile"
            )
        level = data.get("level")
        if level not in ("L2", "L3"):
            errors.append(
                "ODTIS-0532: Phase 4 requires conformance level L2 or L3"
            )
        if extended and "extended" not in profiles:
            errors.append(
                "ODTIS-0532: active Extended sub-modules require extended profile"
            )
    return errors


def scan_prohibited_claims(*paths: Path) -> list[str]:
    errors: list[str] = []
    for path in paths:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for pattern, message in PROHIBITED_CLAIM_PATTERNS:
            if pattern.search(text):
                errors.append(f"{path.name}: {message}")
    return errors


def validate_no_implied_profiles(data: dict, md_path: Path | None) -> list[str]:
    errors: list[str] = []
    declared = set(data.get("profiles") or [])
    only_core = declared <= {"core-identity", "reference-architecture"}
    if not only_core or not md_path or not md_path.is_file():
        return errors
    text = md_path.read_text(encoding="utf-8").lower()
    for hint, implied in IMPLIED_PROFILE_HINTS:
        if implied in declared:
            continue
        for line in text.splitlines():
            line_lower = line.lower()
            if hint not in line_lower:
                continue
            # Skip explicit negations (e.g. "no extended modules declared")
            if re.search(rf"\bno\b[^.\n]*{re.escape(hint)}", line_lower):
                continue
            if re.search(rf"\bnot\b[^.\n]*{re.escape(hint)}", line_lower):
                continue
            errors.append(
                f"ODTIS-0009: text implies {implied} but profile not declared"
            )
            break
    return errors


def validate_dual_format(yaml_data: dict, md_path: Path) -> list[str]:
    errors: list[str] = []
    if not md_path.is_file():
        return [f"missing human-readable statement: {md_path} (ODTIS-0534)"]

    md_fields = parse_markdown_fields(md_path)
    parity = {
        "odtis_version": str(yaml_data.get("odtis_version", "")),
        "level": str(yaml_data.get("level", "")),
        "operator": str(yaml_data.get("operator", "")),
        "date": str(yaml_data.get("date", "")),
        "contact": str(yaml_data.get("contact", "")),
    }
    for key, expected in parity.items():
        actual = md_fields.get(key, "")
        if actual and actual != expected:
            errors.append(f"dual-format mismatch for {key}: yaml={expected!r} md={actual!r}")

    yaml_profiles = ", ".join(yaml_data.get("profiles") or [])
    if md_fields.get("profiles") and md_fields["profiles"] != yaml_profiles:
        errors.append(
            f"dual-format mismatch for profiles: yaml={yaml_profiles!r} md={md_fields['profiles']!r}"
        )

    yaml_reliance = ", ".join(yaml_data.get("reliance_extensions") or []) or "(none)"
    if md_fields.get("reliance_extensions") and md_fields["reliance_extensions"] != yaml_reliance:
        errors.append(
            f"dual-format mismatch for reliance_extensions: yaml={yaml_reliance!r} md={md_fields['reliance_extensions']!r}"
        )

    scope = yaml_data.get("scope") or {}
    if md_fields.get("deployment_phase"):
        expected = str(scope.get("deployment_phase", ""))
        if md_fields["deployment_phase"] != expected:
            errors.append("dual-format mismatch for deployment_phase")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate ODTIS conformance statement")
    parser.add_argument(
        "statement",
        type=Path,
        nargs="?",
        default=ROOT / "implementation/statements/venid-sandbox/conformance-statement.yaml",
        help="Path to YAML or JSON statement",
    )
    parser.add_argument(
        "--human",
        type=Path,
        help="Human-readable Markdown statement (default: sibling .md)",
    )
    parser.add_argument(
        "--no-dual-format",
        action="store_true",
        help="Skip ODTIS-0534 Markdown parity check",
    )
    args = parser.parse_args()

    statement_path = args.statement
    if not statement_path.is_file():
        print(f"ERROR: statement not found: {statement_path}", file=sys.stderr)
        return 1

    spec_version = (
        VERSION_FILE.read_text(encoding="utf-8").strip()
        if VERSION_FILE.is_file()
        else "unknown"
    )

    try:
        data = load_statement(statement_path)
    except (ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    errors = validate_statement(data, spec_version=spec_version)

    profiles = data.get("profiles") or []
    if isinstance(profiles, list):
        errors.extend(validate_profile_chain(profiles))
        errors.extend(validate_phase_extended_rules(data))
        errors.extend(validate_phase_reliance_rules(data))

    md_path = args.human
    if md_path is None:
        md_path = statement_path.with_suffix(".md")

    if not args.no_dual_format:
        errors.extend(validate_dual_format(data, md_path))

    errors.extend(scan_prohibited_claims(statement_path, md_path))
    errors.extend(validate_no_implied_profiles(data, md_path))

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    profiles = ", ".join(data.get("profiles") or [])
    print(
        f"OK: conformance statement valid ({statement_path.name}) "
        f"profiles=[{profiles}] level={data.get('level')} phase="
        f"{(data.get('scope') or {}).get('deployment_phase')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
