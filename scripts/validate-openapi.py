#!/usr/bin/env python3
"""Validate ODTIS Annex A OpenAPI registry files."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANNEX = ROOT / "annexes/A-openapi-registry"
INDEX = ANNEX / "INDEX.yaml"
REQUIRED_FILES = [
    "venid-common.openapi.yaml",
    "verification-api.openapi.yaml",
    "citizen-api.openapi.yaml",
    "admin-api.openapi.yaml",
    "reports-api.openapi.yaml",
    "gov-api.openapi.yaml",
    "regulator-api.openapi.yaml",
    "exchange-gateway.openapi.yaml",
    "INDEX.yaml",
    "CHECKSUMS.sha256",
    "FREEZE.md",
]


def load_yaml(path: Path) -> dict:
    try:
        import yaml  # type: ignore
    except ImportError:
        text = path.read_text(encoding="utf-8")
        if path.suffix == ".yaml" and "openapi:" not in text and "surfaces:" not in text:
            raise ValueError(f"{path} missing expected YAML markers")
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def main() -> int:
    errors: list[str] = []

    if not ANNEX.is_dir():
        errors.append(f"missing annex directory {ANNEX}")

    for name in REQUIRED_FILES:
        path = ANNEX / name
        if not path.is_file():
            errors.append(f"missing {path}")

    for path in ANNEX.glob("*.openapi.yaml"):
        text = path.read_text(encoding="utf-8")
        if "openapi:" not in text:
            errors.append(f"{path.name} missing openapi version key")
        if "info:" not in text:
            errors.append(f"{path.name} missing info block")
        if "version: 0.9.0-draft" not in text:
            errors.append(f"{path.name} info.version must be 0.9.0-draft (Annex A freeze)")

    if INDEX.is_file():
        try:
            data = load_yaml(INDEX)
            if data and "surfaces" not in data:
                errors.append("INDEX.yaml missing surfaces key")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"INDEX.yaml parse error: {exc}")

    for path in list(ANNEX.glob("*-api.openapi.yaml")) + [ANNEX / "exchange-gateway.openapi.yaml"]:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if "operationId:" not in text:
            errors.append(f"{path.name} has no operationId definitions")

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    count = len(list(ANNEX.glob("*.openapi.yaml")))
    print(f"OK: Annex A - {count} OpenAPI bundles, INDEX and required files present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
