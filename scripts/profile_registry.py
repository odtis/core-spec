"""Shared profile ↔ requirement resolution for ODTIS tooling."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILES_YAML = ROOT / "registry/profiles.yaml"
REQUIREMENTS_JSON = ROOT / "registry/requirements.json"
EXTENDED_REQS = ROOT / "annexes/D-extended-profiles/extended-requirements.yaml"
RELIANCE_SUBMODULES = ROOT / "annexes/E-reliance-profiles/sub-modules.yaml"
RELIANCE_ACTIVATION = ROOT / "annexes/E-reliance-profiles/activation.yaml"


def parse_profiles_yaml(path: Path | None = None) -> list[dict]:
    text = (path or PROFILES_YAML).read_text(encoding="utf-8")
    if "profiles:" not in text:
        return []
    body = text.split("profiles:", 1)[1]
    if "levels:" in body:
        body = body.split("levels:", 1)[0]

    profiles: list[dict] = []
    current: dict | None = None
    pending_key: str | None = None
    list_key: str | None = None

    def flush() -> None:
        nonlocal current
        if current:
            profiles.append(current)
            current = None

    for raw in body.splitlines():
        if not raw.strip():
            continue
        id_match = re.match(r"^\s+- id:\s*(.+)$", raw)
        if id_match:
            flush()
            current = {
                "id": id_match.group(1).strip(),
                "title": "",
                "status": "draft",
                "description": "",
                "depends_on": [],
                "mandatory_sections": [],
                "optional_sections": [],
                "requirement_prefixes": [],
                "exclude_requirement_ids": [],
                "include_requirement_ids": [],
                "domains": [],
                "sub_modules": [],
                "annex": "",
            }
            pending_key = None
            list_key = None
            continue
        if current is None:
            continue

        key_only = re.match(r"^\s+([\w-]+):\s*$", raw)
        if key_only:
            key = key_only.group(1)
            if key in (
                "mandatory_sections",
                "optional_sections",
                "requirement_prefixes",
                "exclude_requirement_ids",
                "include_requirement_ids",
                "domains",
                "sub_modules",
                "depends_on",
            ):
                list_key = key
            pending_key = None
            continue

        scalar = re.match(r"^\s+([\w-]+):\s+(.+)$", raw)
        if scalar and not raw.startswith("      "):
            key, val = scalar.group(1), scalar.group(2).strip().strip('"')
            if val == ">":
                pending_key = key
                current[key] = ""
            else:
                current[key] = val
                pending_key = None
                list_key = None
            continue

        if pending_key and re.match(r"^\s{4,}\S", raw):
            chunk = raw.strip()
            sep = " " if current[pending_key] else ""
            current[pending_key] = f"{current[pending_key]}{sep}{chunk}"
            continue

        if list_key:
            item = re.match(r'^\s+- "?([^"]+)"?\s*$', raw)
            if item:
                current[list_key].append(item.group(1).strip('"'))
            continue

        pending_key = None

    flush()
    return profiles


def req_matches_prefix(req_id: str, prefixes: list[str]) -> bool:
    return any(req_id.startswith(p.rstrip(".")) for p in prefixes)


def parse_extended_annex(path: Path | None = None) -> tuple[list[str], list[str]]:
    """Return (registry_ref IDs, draft IDs) from Annex D."""
    text = (path or EXTENDED_REQS).read_text(encoding="utf-8")
    registry_ids: list[str] = []
    draft_ids: list[str] = []
    in_registry_refs = False
    in_draft = False
    current_module: str | None = None

    for raw in text.splitlines():
        if raw.strip() == "registry_refs:":
            in_registry_refs = True
            in_draft = False
            current_module = None
            continue
        if raw.strip() == "draft_requirements:":
            in_registry_refs = False
            in_draft = True
            current_module = None
            continue
        if in_registry_refs:
            if re.match(r"^([A-Z][\w-]+):\s*$", raw):
                current_module = raw.split(":", 1)[0]
                continue
            rid = re.match(r"^- (ODTIS-\d{4})$", raw.strip())
            if rid and current_module:
                registry_ids.append(rid.group(1))
            continue
        if in_draft:
            if re.match(r"^([A-Z][\w-]+):\s*$", raw):
                current_module = raw.split(":", 1)[0]
                continue
            if raw.strip().startswith("- id:"):
                draft_ids.append(raw.split(":", 1)[1].strip())

    return sorted(set(registry_ids)), sorted(set(draft_ids))


def parse_reliance_submodule_ids(path: Path | None = None) -> set[str]:
    text = (path or RELIANCE_SUBMODULES).read_text(encoding="utf-8")
    if "sub_modules:" not in text:
        return set()
    body = text.split("sub_modules:", 1)[1].split("composition_rules:", 1)[0]
    return set(re.findall(r"^- id: (R-[A-Za-z0-9-]+)\s*$", body, re.M))


def parse_reliance_module_requirements(path: Path | None = None) -> dict[str, list[str]]:
    text = (path or RELIANCE_SUBMODULES).read_text(encoding="utf-8")
    if "sub_modules:" not in text:
        return {}
    body = text.split("sub_modules:", 1)[1].split("composition_rules:", 1)[0]
    modules: dict[str, list[str]] = {}
    current: str | None = None
    for line in body.splitlines():
        m_id = re.match(r"^- id: (R-[A-Za-z0-9-]+)\s*$", line)
        if m_id:
            current = m_id.group(1)
            modules[current] = []
            continue
        m_reqs = re.match(r"^\s+requirements: \[(.+)\]\s*$", line)
        if m_reqs and current:
            modules[current] = [r.strip() for r in m_reqs.group(1).split(",")]
    return modules


def parse_reliance_phase_minimum(path: Path | None = None) -> dict[str, int]:
    text = (path or RELIANCE_ACTIVATION).read_text(encoding="utf-8")
    phases: dict[str, int] = {}
    in_block = False
    for line in text.splitlines():
        if line.strip() == "module_phase_minimum:":
            in_block = True
            continue
        if in_block and line.strip().startswith("tier_status:"):
            break
        if in_block:
            m = re.match(r"^\s+(R-[\w-]+):\s*(\d+)\s*$", line)
            if m:
                phases[m.group(1)] = int(m.group(2))
    return phases


def reliance_requirement_ids(declared_modules: list[str]) -> list[str]:
    """Resolve ODTIS-07xx IDs for declared Reliance Extension sub-modules (always includes R-Base)."""
    mod_reqs = parse_reliance_module_requirements()
    ids: set[str] = set(mod_reqs.get("R-Base", []))
    for mod in declared_modules:
        if mod == "R-Base":
            continue
        ids.update(mod_reqs.get(mod, []))
    return sorted(ids)


def profile_requirement_ids(profile: dict, requirements: list[dict] | None = None) -> list[str]:
    pid = profile["id"]
    if pid == "extended":
        registry_ids, draft_ids = parse_extended_annex()
        ids = sorted(set(registry_ids + draft_ids + profile.get("include_requirement_ids", [])))
        return ids

    prefixes = profile.get("requirement_prefixes", [])
    exclude = set(profile.get("exclude_requirement_ids", []))
    include = profile.get("include_requirement_ids", [])

    matched: set[str] = set()
    if requirements:
        for req in requirements:
            rid = req["id"]
            if rid in exclude:
                continue
            if req_matches_prefix(rid, prefixes):
                matched.add(rid)
    else:
        # Prefix-only resolution without full registry scan (fallback).
        for prefix in prefixes:
            matched.add(prefix)

    for rid in include:
        if rid not in exclude:
            matched.add(rid)

    return sorted(matched)


def registry_requirements_for_profile(profile: dict, requirements: list[dict]) -> list[dict]:
    ids = set(profile_requirement_ids(profile, requirements))
    if profile["id"] == "extended":
        by_id = {r["id"]: r for r in requirements}
        rows: list[dict] = []
        for rid in sorted(ids):
            if rid in by_id:
                rows.append(by_id[rid])
        return rows

    matched = [r for r in requirements if r["id"] in ids]
    return sorted(matched, key=lambda r: r["id"])


def profiles_for_req(req: dict, profiles: list[dict], requirements: list[dict]) -> list[str]:
    req_id = req.get("id", "")
    matched: list[str] = []
    for profile in profiles:
        ids = profile_requirement_ids(profile, requirements)
        if req_id in ids:
            matched.append(profile.get("title") or profile["id"])
    return matched


def load_requirements(path: Path | None = None) -> list[dict]:
    registry = json.loads((path or REQUIREMENTS_JSON).read_text(encoding="utf-8"))
    return registry.get("requirements", [])
