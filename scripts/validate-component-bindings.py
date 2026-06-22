#!/usr/bin/env python3
"""Validate component binding YAML files against registry and RI-MAP.yaml."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BINDINGS_DIR = ROOT / "implementation/component-bindings"
RI_MAP = ROOT / "implementation/RI-MAP.yaml"
REGISTRY = ROOT / "registry/requirements.json"
ID_PATTERN = re.compile(r"^ODTIS-\d{4}$")


def load_binding(path: Path) -> dict:
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "generate_component_bindings_docs", ROOT / "scripts/generate-component-bindings-docs.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.load_yaml_simple(path)


def parse_ri_map_binding_docs(text: str) -> dict[str, str]:
    """surface_id -> binding_doc path (last wins per surface block)."""
    docs: dict[str, str] = {}
    current_surface: str | None = None
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("- id:"):
            current_surface = line.split(":", 1)[1].strip()
        elif line.startswith("binding_doc:") and current_surface:
            docs[current_surface] = line.split(":", 1)[1].strip()
    return docs


def main() -> int:
    if not BINDINGS_DIR.is_dir():
        print(f"ERROR: missing {BINDINGS_DIR}", file=sys.stderr)
        return 1

    reg = {r["id"] for r in json.loads(REGISTRY.read_text(encoding="utf-8"))["requirements"]}
    ri_docs = parse_ri_map_binding_docs(RI_MAP.read_text(encoding="utf-8")) if RI_MAP.is_file() else {}
    errors: list[str] = []
    warnings: list[str] = []

    binding_by_file: dict[str, dict] = {}
    for path in sorted(BINDINGS_DIR.glob("*.yaml")):
        if path.name.upper().startswith("TEMPLATE"):
            continue
        b = load_binding(path)
        rel = f"implementation/component-bindings/{path.name}"
        binding_by_file[rel] = b
        cid = b.get("component_id", path.stem)

        for rid in b.get("odtis_ids", []):
            if not ID_PATTERN.match(rid):
                errors.append(f"{path.name}: invalid id {rid}")
            elif rid not in reg:
                errors.append(f"{path.name}: unknown registry id {rid}")

        surfaces = list(b.get("ri_map_surfaces") or [])
        if b.get("ri_map_surface"):
            surfaces.insert(0, b["ri_map_surface"])

        if not surfaces:
            warnings.append(f"{path.name}: no ri_map_surface defined")
            continue

        for sid in surfaces:
            doc = ri_docs.get(sid)
            if not doc:
                warnings.append(f"{path.name}: RI-MAP surface `{sid}` has no binding_doc")
            elif doc != rel:
                errors.append(f"{path.name}: RI-MAP `{sid}` binding_doc is `{doc}`, expected `{rel}`")

    for surface, doc in ri_docs.items():
        if doc not in binding_by_file:
            errors.append(f"RI-MAP `{surface}` binding_doc missing file: {doc}")
        elif binding_by_file[doc].get("ri_map_surface") != surface:
            surfaces = binding_by_file[doc].get("ri_map_surfaces") or []
            primary = binding_by_file[doc].get("ri_map_surface")
            if surface != primary and surface not in surfaces:
                warnings.append(f"RI-MAP `{surface}` -> {doc} but binding primary surface is `{primary}`")

    for w in warnings:
        print(f"WARN: {w}")
    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)

    if errors:
        return 1
    print(f"OK: {len(binding_by_file)} component bindings validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
