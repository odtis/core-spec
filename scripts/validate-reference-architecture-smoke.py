#!/usr/bin/env python3
"""Static smoke checks for Reference Architecture profile (ODTIS-0001..0010)."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

import importlib.util

_spec = importlib.util.spec_from_file_location(
    "validate_conformance_statement",
    ROOT / "scripts/validate-conformance-statement.py",
)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)

PROHIBITED_CLAIM_PATTERNS = _mod.PROHIBITED_CLAIM_PATTERNS
load_statement = _mod.load_statement
validate_profile_chain = _mod.validate_profile_chain
validate_statement = _mod.validate_statement

STATEMENTS = [
    ROOT / "implementation/statements/venid-phase1-core/conformance-statement.yaml",
    ROOT / "implementation/statements/venid-phase2-trust/conformance-statement.yaml",
    ROOT / "implementation/statements/venid-phase3-operator/conformance-statement.yaml",
    ROOT / "implementation/statements/venid-phase4-full/conformance-statement.yaml",
]

NEGATION_HINTS = (
    "must not",
    "do not",
    "does not",
    "not grant",
    "not a",
    "not an",
    "without ",
    "prohibited",
    "no ",
    "don't",
    "doesn't",
    "false ",
    "forbidden",
    "requires l3",
    "requires third-party",
)


def spec_version() -> str:
    version_file = ROOT / "VERSION"
    return version_file.read_text(encoding="utf-8").strip() if version_file.is_file() else "unknown"


def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    raise SystemExit(1)


def ok(msg: str) -> None:
    print(f"OK: {msg}")


def run_negative_profile_chain_checks() -> None:
    """ODTIS-0001, ODTIS-0002, ODTIS-0004: validator rejects invalid profile chains."""
    cases = [
        (["reference-architecture", "trust-network"], "ODTIS-0001"),
        (["reference-architecture", "core-identity", "federation"], "ODTIS-0002"),
        (["reference-architecture", "operator"], "ODTIS-0004"),
    ]
    for profiles, label in cases:
        errors = validate_profile_chain(profiles)
        if not errors:
            fail(f"{label}: expected profile-chain rejection for {profiles}")
    ok("profile dependency chain rejects invalid declarations (0001/0002/0004)")


def validate_all_statements() -> None:
    """ODTIS-0003, ODTIS-0005, ODTIS-0008: statements validate with version binding."""
    version = spec_version()
    for path in STATEMENTS:
        if not path.is_file():
            fail(f"missing statement: {path.relative_to(ROOT)}")
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts/validate-conformance-statement.py"), str(path)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            print(proc.stdout, file=sys.stderr)
            print(proc.stderr, file=sys.stderr)
            fail(f"statement validation failed: {path.name}")
        data = load_statement(path)
        if str(data.get("odtis_version", "")) != version:
            fail(f"{path.name}: odtis_version must match VERSION ({version})")
        profiles = data.get("profiles") or []
        if "reference-architecture" not in profiles:
            fail(f"{path.name}: must declare reference-architecture profile")
    ok(f"all VenID statements validate with odtis_version={version} (0003/0005/0008)")


def normalize_claim_line(line: str) -> str:
    return re.sub(r"[*_`]", "", line).lower()


def scan_claim_docs_for_prohibited() -> None:
    """ODTIS-0007: operator-facing docs must not use prohibited affirmative claims."""
    candidates = [
        ROOT / "implementation/statements/venid-phase2-trust/conformance-statement.md",
        ROOT / "implementation/statements/venid-phase2-trust/conformance-statement.yaml",
        ROOT / "README.md",
        ROOT / "index.md",
        ROOT / "site/STATUS.md",
    ]
    impl_scope = ROOT.parent / "core-impl/ven-identity-core/docs/operator/PUBLISHED-SERVICE-SCOPE.md"
    if impl_scope.is_file():
        candidates.append(impl_scope)

    for path in candidates:
        if not path.is_file():
            continue
        for num, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            lower = normalize_claim_line(line)
            if any(h in lower for h in NEGATION_HINTS):
                continue
            for pattern, message in PROHIBITED_CLAIM_PATTERNS:
                if pattern.search(line):
                    fail(f"{path.relative_to(ROOT)}:{num}: {message}")
    ok("operator-facing docs avoid prohibited affirmative claims (0007)")


def validate_applicable_tests_honesty() -> None:
    """ODTIS-0010: published statements report partial status with pending IDs when needed."""
    coverage = ROOT / "traceability/coverage-report.yaml"
    if not coverage.is_file():
        fail("missing traceability/coverage-report.yaml")
    text = coverage.read_text(encoding="utf-8")
    if "implemented_pct:" not in text:
        fail("coverage-report missing implemented_pct")
    if "total_procedures:" not in text:
        fail("coverage-report missing total_procedures")

    phase2 = ROOT / "implementation/statements/venid-phase2-trust/conformance-statement.yaml"
    data = load_statement(phase2)
    tests = data.get("tests") or {}
    status = str(tests.get("status", "")).lower()
    pending = tests.get("pending_test_ids") or []
    if status not in {"partial", "implemented"}:
        fail("phase2-trust tests.status must be partial or implemented")
    if status == "partial" and not pending:
        fail("phase2-trust partial status requires pending_test_ids (00010)")
    ok("coverage report and phase2 statement declare honest test status (0010)")


def validate_minimal_claim_alignment() -> None:
    """ODTIS-0009: published production scope does not imply undeclared profiles."""
    scope = ROOT.parent / "core-impl/ven-identity-core/docs/operator/PUBLISHED-SERVICE-SCOPE.md"
    if not scope.is_file():
        print("WARN: PUBLISHED-SERVICE-SCOPE.md not found; skipping 0009 live scope check")
        return
    text = scope.read_text(encoding="utf-8")
    for label in ("Federation", "E-Wallet", "E-Inclusion", "E-Signature", "E-KYB"):
        if not re.search(rf"{re.escape(label)}.*\*\*No\*\*", text):
            fail(f"PUBLISHED-SERVICE-SCOPE must mark {label} as No for production claim (0009)")
    if re.search(r"\bproduction ODTIS Certified\b", text, re.I):
        fail("PUBLISHED-SERVICE-SCOPE must not claim production ODTIS Certified (0009)")
    ok("published production scope does not imply Extended/Federation claims (0009)")


def main() -> int:
    run_negative_profile_chain_checks()
    validate_all_statements()
    scan_claim_docs_for_prohibited()
    validate_applicable_tests_honesty()
    validate_minimal_claim_alignment()
    print("\nReference architecture smoke validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
