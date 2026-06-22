#!/usr/bin/env python3
"""Validate ODTIS reference implementation map (ODTIS-0536)."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RI_MAP = ROOT / "implementation/RI-MAP.yaml"
GAPS = ROOT / "implementation/gaps/gaps.yaml"
BACKLOG = ROOT / "implementation/phased-backlog.yaml"
REGISTRY = ROOT / "registry/requirements.json"
ID_PATTERN = re.compile(r"^ODTIS-\d{4}$")


def load_yaml(path: Path) -> dict:
    try:
        import yaml  # type: ignore
    except ImportError as exc:
        raise RuntimeError("PyYAML required") from exc
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def registry_ids() -> set[str]:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    return {r["id"] for r in data.get("requirements", [])}


def backlog_epic_ids() -> set[str]:
    if not BACKLOG.is_file():
        return set()
    data = load_yaml(BACKLOG)
    ids: set[str] = set()
    for phase in data.get("phases", []):
        for epic in phase.get("epics", []):
            eid = epic.get("id")
            if eid:
                ids.add(eid)
    return ids


def validate_implementation(impl: dict, reg: set[str], errors: list[str], warnings: list[str]) -> None:
    iid = impl.get("id", "?")
    path = impl.get("path")
    if path:
        abs_path = (ROOT / path).resolve()
        if not abs_path.exists():
            warnings.append(f"{iid}: repo path not found: {path}")

    surfaces = impl.get("surfaces") or []
    if not surfaces:
        errors.append(f"{iid}: no surfaces defined")
        return

    mapped: set[str] = set()
    for surface in surfaces:
        sid = surface.get("id", "?")
        ids = surface.get("odtis_ids") or []
        if not ids:
            if surface.get("informative") or surface.get("note"):
                continue
            errors.append(f"{iid}/{sid}: surface has no odtis_ids")
            continue
        for rid in ids:
            if not ID_PATTERN.match(str(rid)):
                errors.append(f"{iid}/{sid}: invalid id {rid}")
            elif rid not in reg:
                errors.append(f"{iid}/{sid}: unknown registry id {rid}")
            else:
                mapped.add(rid)

    profiles = impl.get("profiles_claimed") or []
    if profiles and "reference-architecture" not in profiles:
        errors.append(f"{iid}: profiles_claimed must include reference-architecture")


def validate_gaps(gap_data: dict, epic_ids: set[str], impl_ids: set[str], errors: list[str]) -> None:
    for gap in gap_data.get("gaps") or []:
        gid = gap.get("id", "?")
        impl = gap.get("implementation")
        if impl and impl not in impl_ids and impl != "odtis":
            errors.append(f"gap {gid}: unknown implementation {impl}")
        odtis_id = gap.get("odtis_id")
        if odtis_id and not ID_PATTERN.match(str(odtis_id)):
            errors.append(f"gap {gid}: invalid odtis_id {odtis_id}")
        epic = gap.get("backlog_epic")
        if epic and epic not in epic_ids:
            errors.append(f"gap {gid}: unknown backlog_epic {epic}")
        ct = gap.get("conformance_test")
        if ct and not (ROOT / ct).is_file():
            errors.append(f"gap {gid}: missing conformance_test {ct}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate RI-MAP.yaml")
    parser.add_argument("--map", type=Path, default=RI_MAP)
    parser.add_argument("--warn-only-paths", action="store_true")
    args = parser.parse_args()

    if not args.map.is_file():
        print(f"ERROR: missing {args.map}", file=sys.stderr)
        return 1

    data = load_yaml(args.map)
    reg = registry_ids()
    epic_ids = backlog_epic_ids()
    errors: list[str] = []
    warnings: list[str] = []

    impls = data.get("implementations") or []
    if not impls:
        errors.append("implementations list is empty")

    impl_ids = {i.get("id") for i in impls if i.get("id")}
    for impl in impls:
        validate_implementation(impl, reg, errors, warnings)

    if GAPS.is_file():
        validate_gaps(load_yaml(GAPS), epic_ids, impl_ids, errors)

    stmt = data.get("conformance_statements") or {}
    if not stmt.get("lab"):
        warnings.append("conformance_statements.lab not set")

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    surface_count = sum(len(i.get("surfaces") or []) for i in impls)
    gap_count = len(load_yaml(GAPS).get("gaps") or []) if GAPS.is_file() else 0
    for warn in warnings:
        print(f"WARN: {warn}", file=sys.stderr)
    print(
        f"OK: RI map valid ({len(impls)} implementations, {surface_count} surfaces, "
        f"{gap_count} tracked gaps)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
