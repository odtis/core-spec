#!/usr/bin/env python3
"""Inject generated ODTIS-MNNN requirement tables into spec/profiles/*-profile.md."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILES_YAML = ROOT / "registry/profiles.yaml"
REQUIREMENTS = ROOT / "registry/requirements.json"
EXTENDED_REQS = ROOT / "annexes/D-extended-profiles/extended-requirements.yaml"
PROFILES_DIR = ROOT / "spec/profiles"
MANIFEST_DIR = ROOT / "conformance/profiles"
ODTIS_GITHUB = "https://github.com/odtis/core-spec/blob/main"

GENERATED_START = "<!-- GENERATED:profile-requirements:START -->"
GENERATED_END = "<!-- GENERATED:profile-requirements:END -->"

BOOK1_FILE = ROOT / "registry/book1-domains.yaml"
ACTIVATION_FILE = ROOT / "annexes/D-extended-profiles/activation.yaml"
SUBMODULES_FILE = ROOT / "annexes/D-extended-profiles/sub-modules.yaml"
TESTS_DIR = ROOT / "conformance/tests"
STATUS_LINE = re.compile(r"^\*\*Status:\*\*\s*(.+)\s*$", re.M)

PROFILE_FILES: dict[str, str] = {
    "reference-architecture": "reference-architecture-profile.md",
    "core-identity": "core-identity-profile.md",
    "trust-network": "trust-network-profile.md",
    "federation": "federation-profile.md",
    "operator": "operator-profile.md",
    "extended": "extended-profile.md",
    "reliance-extensions": "reliance-extensions-profile.md",
}

SECTION_META: dict[str, tuple[str, str, str]] = {
    "01-scope-conformance": ("1", "Scope and conformance", "spec/01-scope-conformance/SPEC.md"),
    "02-terminology-loa": ("2", "Terminology and LoA", "spec/02-terminology-loa/SPEC.md"),
    "03-identity-services": ("3", "Identity services", "spec/03-identity-services/SPEC.md"),
    "04-trust-network": ("4", "Trust network", "spec/04-trust-network/SPEC.md"),
    "05-consent-privacy": ("5", "Consent and privacy", "spec/05-consent-privacy/SPEC.md"),
    "06-federation": ("6", "Federation", "spec/06-federation/SPEC.md"),
    "07-operator-governance": ("7", "Operator governance", "spec/07-operator-governance/SPEC.md"),
    "08-security": ("8", "Security", "spec/08-security/SPEC.md"),
    "09-audit-events": ("9", "Audit and events", "spec/09-audit-events/SPEC.md"),
    "10-deployment-profiles": ("10", "Deployment", "spec/10-deployment-profiles/SPEC.md"),
    "11-reliance-profiles": ("11", "Reliance Extensions", "spec/11-reliance-profiles/SPEC.md"),
}


sys.path.insert(0, str(ROOT / "scripts"))
from profile_registry import (  # noqa: E402
    load_requirements,
    parse_profiles_yaml,
    profiles_for_req,
    registry_requirements_for_profile,
)

def parse_extended_annex() -> tuple[list[dict], list[dict]]:
    """Return (registry_refs rows, draft rows) for Extended profile."""
    text = EXTENDED_REQS.read_text(encoding="utf-8")
    registry_refs: list[dict] = []
    draft_rows: list[dict] = []
    current_module: str | None = None
    in_registry_refs = False
    in_draft = False
    current_draft: dict | None = None
    pending_text = False

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
            mod = re.match(r"^([A-Z][\w-]+):\s*$", raw)
            if mod:
                current_module = mod.group(1)
                continue
            rid = re.match(r"^- (ODTIS-\d{4})$", raw.strip())
            if rid and current_module:
                registry_refs.append(
                    {
                        "id": rid.group(1),
                        "module": current_module,
                        "status": "registry_ref",
                        "keyword": "-",
                        "text": "Referenced from Annex D; see normative section or draft merge target.",
                    }
                )
            continue
        if in_draft:
            mod = re.match(r"^([A-Z][\w-]+):\s*$", raw)
            if mod:
                if current_draft:
                    draft_rows.append(current_draft)
                current_module = mod.group(1)
                current_draft = None
                pending_text = False
                continue
            if raw.strip().startswith("- id:"):
                if current_draft:
                    draft_rows.append(current_draft)
                current_draft = {
                    "id": raw.split(":", 1)[1].strip(),
                    "module": current_module or "?",
                    "status": "draft",
                    "keyword": "",
                    "text": "",
                }
                pending_text = False
                continue
            if current_draft is None:
                continue
            key_match = re.match(r"^\s+(keyword|text|status):\s*(.+)$", raw)
            if key_match:
                key, val = key_match.group(1), key_match.group(2).strip().strip('"')
                current_draft[key] = val
                pending_text = key == "text" and val == ""
                continue
            if pending_text and raw.startswith("  ") and not raw.strip().startswith("trace"):
                chunk = raw.strip()
                sep = " " if current_draft["text"] else ""
                current_draft["text"] = f"{current_draft['text']}{sep}{chunk}"
                continue

    if current_draft:
        draft_rows.append(current_draft)
    return registry_refs, draft_rows


def enrich_extended_registry_refs(
    registry_refs: list[dict], requirements: list[dict]
) -> list[dict]:
    by_id = {r["id"]: r for r in requirements}
    enriched: list[dict] = []
    for row in registry_refs:
        req = by_id.get(row["id"])
        if req:
            enriched.append({**req, "module": row["module"], "status": req.get("status", "normative")})
        else:
            enriched.append(row)
    return sorted(enriched, key=lambda r: r["id"])


def load_manifest(profile_id: str) -> dict:
    path = MANIFEST_DIR / profile_id / "manifest.yaml"
    if not path.is_file():
        return {}
    data: dict = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(\w+):\s*(.+)$", line.strip())
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val.isdigit():
                data[key] = int(val)
            else:
                try:
                    data[key] = float(val)
                except ValueError:
                    data[key] = val.strip('"')
    return data


def parse_book1_domains() -> tuple[list[dict], dict[str, list[int]]]:
    """Return (domain rows, profile -> applicable ODTIS deployment phases)."""
    if not BOOK1_FILE.is_file():
        return [], {}
    text = BOOK1_FILE.read_text(encoding="utf-8")
    domains: list[dict] = []
    phase_map: dict[str, list[int]] = {}
    current: dict | None = None
    list_key: str | None = None

    for raw in text.splitlines():
        line = raw.rstrip()
        if not line or line.strip().startswith("#"):
            continue
        if line.startswith("profile_phase_applicability:"):
            if current:
                domains.append(current)
                current = None
            list_key = None
            continue
        if line.startswith("  ") and ":" in line and not line.strip().startswith("-"):
            k, v = line.strip().split(":", 1)
            k, v = k.strip(), v.strip()
            if k in PROFILE_FILES and v.startswith("["):
                phase_map[k] = [int(x.strip()) for x in v.strip("[]").split(",") if x.strip()]
                continue
        if line.strip().startswith("- id:"):
            if current:
                domains.append(current)
            current = {"id": line.split(":", 1)[1].strip()}
            list_key = None
            continue
        if current is None:
            continue
        if line.strip() in ("profiles:", "odtis_sections:", "key_ids:"):
            list_key = line.strip()[:-1]
            current[list_key] = []
            continue
        for key in ("profiles", "odtis_sections", "key_ids"):
            if line.strip().startswith(f"{key}:") and "[" in line:
                current[key] = [
                    x.strip() for x in line.split("[", 1)[1].split("]")[0].split(",") if x.strip()
                ]
                break
        else:
            if list_key and line.strip().startswith("- "):
                val = line.strip()[2:].strip()
                current[list_key].append(val)
                continue
            if list_key and ":" in line.strip():
                k, v = line.strip().split(":", 1)
                if k == list_key and v.strip().startswith("["):
                    current[list_key] = [x.strip() for x in v.strip("[]").split(",") if x.strip()]
                    list_key = None
                    continue
        if line.strip().startswith("title:"):
            current["title"] = line.split(":", 1)[1].strip()
        elif line.strip().startswith("description:"):
            current["description"] = line.split(":", 1)[1].strip()
    if current:
        domains.append(current)
    return domains, phase_map


def parse_activation_phases() -> list[dict]:
    if not ACTIVATION_FILE.is_file():
        return []
    phases: list[dict] = []
    current: dict | None = None
    for raw in ACTIVATION_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("- phase:"):
            if current:
                phases.append(current)
            current = {"phase": int(line.split(":", 1)[1].strip())}
            continue
        if current is None:
            continue
        if line.startswith("name:"):
            current["name"] = line.split(":", 1)[1].strip()
        elif line.startswith("extended_in_production:"):
            current["extended_in_production"] = line.split(":", 1)[1].strip()
        elif line.startswith("reference:"):
            current["reference"] = line.split(":", 1)[1].strip()
        elif line.startswith("allowed_lab_modules:"):
            current["allowed_lab_modules"] = [
                x.strip() for x in line.split(":", 1)[1].strip("[]").split(",") if x.strip()
            ]
        elif line.startswith("typical_modules:"):
            current["typical_modules"] = [
                x.strip() for x in line.split(":", 1)[1].strip("[]").split(",") if x.strip()
            ]
        elif line.startswith("notes:"):
            current["notes"] = line.split(":", 1)[1].strip().strip('"')
    if current:
        phases.append(current)
    return phases


def parse_sub_modules() -> list[dict]:
    if not SUBMODULES_FILE.is_file():
        return []
    modules: list[dict] = []
    current: dict | None = None
    for raw in SUBMODULES_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("composition_"):
            continue
        if line.startswith("- id:"):
            if current:
                modules.append(current)
            current = {"id": line.split(":", 1)[1].strip()}
            continue
        if current is None:
            continue
        if line.startswith("title:"):
            current["title"] = line.split(":", 1)[1].strip()
        elif line.startswith("min_deployment_phase:"):
            current["min_deployment_phase"] = int(line.split(":", 1)[1].strip())
        elif line.startswith("status:"):
            current["status"] = line.split(":", 1)[1].strip()
    if current:
        modules.append(current)
    return modules


def implemented_test_count(profile_id: str) -> int:
    manifest = load_manifest(profile_id)
    count = 0
    manifest_path = MANIFEST_DIR / profile_id / "manifest.yaml"
    if not manifest_path.is_file():
        return 0
    for m in re.finditer(r"path:\s*(conformance/tests/[^\s]+)", manifest_path.read_text()):
        path = ROOT / m.group(1)
        if not path.is_file():
            continue
        sm = STATUS_LINE.search(path.read_text(encoding="utf-8"))
        if sm and sm.group(1).strip().lower().startswith("implemented"):
            count += 1
    return count


def book1_section(profile_id: str, domains: list[dict]) -> list[str]:
    rows = [d for d in domains if profile_id in d.get("profiles", [])]
    if not rows:
        return []
    lines = [
        "## Book 1 decision domains (informative)",
        "",
        "Mapping from Book 1 sponsor decisions to this profile. Normative text remains in ODTIS sections.",
        "",
        "| Domain | Title | Key ODTIS IDs |",
        "|--------|-------|---------------|",
    ]
    for d in rows:
        keys = ", ".join(f"`{x}`" for x in d.get("key_ids", [])[:5])
        extra = len(d.get("key_ids", [])) - 5
        if extra > 0:
            keys += f" (+{extra})"
        lines.append(f"| **{d['id']}** | {d.get('title', '-')} | {keys or '-'} |")
    lines.extend(
        [
            "",
            "Full matrix: [`registry/book1-domains.yaml`](../../registry/book1-domains.yaml).",
            "",
        ]
    )
    return lines


def phase_section(profile_id: str, phase_map: dict[str, list[int]], phases: list[dict], modules: list[dict]) -> list[str]:
    applicable = phase_map.get(profile_id, [])
    if not applicable and profile_id != "extended":
        return []
    lines = [
        "## Deployment phase matrix",
        "",
    ]
    if applicable:
        lines.extend(
            [
                f"**ODTIS deployment phases applicable:** {', '.join(str(p) for p in applicable)}",
                "",
                "| Phase | Name | Extended in production |",
                "|-------|------|------------------------|",
            ]
        )
        for ph in phases:
            if ph["phase"] not in applicable:
                continue
            ext = ph.get("extended_in_production", "-")
            if profile_id != "extended" and ext == "optional" and ph["phase"] < 2:
                ext = "forbidden (base profile only)"
            lines.append(f"| {ph['phase']} | {ph.get('name', '-')} | {ext} |")
        lines.append("")

    if profile_id == "extended" and modules:
        lines.extend(
            [
                "**Annex D sub-modules** (declare in conformance statement per `ODTIS-0532`):",
                "",
                "| Module | Min phase | Status |",
                "|--------|-----------|--------|",
            ]
        )
        for mod in modules:
            lines.append(
                f"| {mod['id']} | {mod.get('min_deployment_phase', '-')} | {mod.get('status', '-')} |"
            )
        lines.extend(
            [
                "",
                "Phase rules: [`annexes/D-extended-profiles/activation.yaml`](../../annexes/D-extended-profiles/activation.yaml).",
                "",
            ]
        )
    elif applicable:
        lines.extend(
            [
                "Cross-profile matrix: [section 10](../10-deployment-profiles/SPEC.md), "
                "[`annexes/D-extended-profiles/activation.yaml`](../../annexes/D-extended-profiles/activation.yaml).",
                "",
            ]
        )
    return lines


def md_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def keyword_badge(keyword: str) -> str:
    if not keyword or keyword == "-":
        return "-"
    css = {
        "MUST": "odtis-kw--must",
        "MUST NOT": "odtis-kw--must-not",
        "SHOULD": "odtis-kw--should",
        "MAY": "odtis-kw--may",
    }.get(keyword, "odtis-kw--may")
    return f'<span class="odtis-kw {css}">{keyword}</span>'


def section_link(section_slug: str) -> str:
    num, title, path = SECTION_META.get(section_slug, ("?", section_slug, f"spec/{section_slug}/SPEC.md"))
    return f"[section {num}](../../{path})"


def test_cell(req: dict) -> str:
    test_path = req.get("conformance_test", "")
    if test_path:
        return f"`{Path(test_path).name}` ([repo]({ODTIS_GITHUB}/{test_path}))"
    return "-"


def requirement_table_rows(rows: list[dict], include_module: bool = False) -> list[str]:
    if include_module:
        header = "| ID | Module | Legacy | Keyword | Requirement | Spec | Test |"
        sep = "|----|--------|--------|---------|-------------|------|------|"
    else:
        header = "| ID | Legacy | Keyword | Requirement | Spec | Test |"
        sep = "|----|--------|---------|-------------|------|------|"

    lines = [header, sep]
    for row in rows:
        rid = row["id"]
        legacy = row.get("legacy_id", "-")
        keyword = keyword_badge(row.get("keyword", ""))
        text = md_escape(row.get("text", ""))
        section = row.get("section", "")
        spec = section_link(section) if section else "-"
        test = test_cell(row)
        if include_module:
            lines.append(
                f"| `{rid}` | {row.get('module', '-')} | `{legacy}` | {keyword} | {text} | {spec} | {test} |"
            )
        else:
            lines.append(f"| `{rid}` | `{legacy}` | {keyword} | {text} | {spec} | {test} |")
    return lines


def generate_profile_block(
    profile: dict,
    requirements: list[dict],
    version: str,
) -> str:
    pid = profile["id"]
    manifest = load_manifest(pid)
    book1_domains, phase_map = parse_book1_domains()
    activation_phases = parse_activation_phases()
    sub_modules = parse_sub_modules()
    impl_count = implemented_test_count(pid)
    lines = [
        f"<!-- Generated by scripts/generate-profile-docs.py @ {version} -->",
        "",
        "## Profile registry",
        "",
        f"| Field | Value |",
        f"|-------|-------|",
        f"| Profile ID | `{pid}` |",
        f"| Title | {profile.get('title') or pid} |",
        f"| Status | {profile.get('status', 'draft')} |",
    ]

    if profile.get("depends_on"):
        lines.append(f"| Depends on | {', '.join(f'`{d}`' for d in profile['depends_on'])} |")
    if profile.get("domains"):
        lines.append(f"| Domains | {', '.join(profile['domains'])} |")
    if profile.get("mandatory_sections"):
        sections = ", ".join(f"`{s}`" for s in profile["mandatory_sections"])
        lines.append(f"| Mandatory sections | {sections} |")
    if profile.get("annex"):
        annex_slug = profile["annex"]
        lines.append(f"| Annex | [`{annex_slug}`](../../annexes/{annex_slug}/README.md) |")
    if profile.get("sub_modules"):
        lines.append(f"| Sub-modules | {', '.join(f'`{m}`' for m in profile['sub_modules'])} |")

    lines.extend(
        [
            f"| Registry | [`profiles.yaml`](../../registry/profiles.yaml) |",
            "",
        ]
    )
    lines.extend(book1_section(pid, book1_domains))
    lines.extend(phase_section(pid, phase_map, activation_phases, sub_modules))
    lines.extend(
        [
            "## Normative requirements (ODTIS-MNNN)",
            "",
        ]
    )

    if pid == "extended":
        registry_refs, draft_rows = parse_extended_annex()
        registry_refs = enrich_extended_registry_refs(registry_refs, requirements)
        lines.extend(
            [
                "Extended composes **Annex D** sub-modules. Draft IDs below merge into "
                f"[`requirements.json`](../../registry/requirements.json) at ODTIS 1.0.",
                "",
            ]
        )
        if registry_refs:
            lines.extend(
                [
                    f"### Registry-linked ({len(registry_refs)} IDs)",
                    "",
                    *requirement_table_rows(registry_refs, include_module=True),
                    "",
                ]
            )
        if draft_rows:
            lines.extend(
                [
                    f"### Annex D draft ({len(draft_rows)} IDs)",
                    "",
                    *requirement_table_rows(draft_rows, include_module=True),
                    "",
                ]
            )
        total = len(registry_refs) + len(draft_rows)
        lines.append(f"**Total Extended scope:** {total} IDs ({len(registry_refs)} registry-linked, {len(draft_rows)} draft).")
    else:
        profile_reqs = registry_requirements_for_profile(profile, requirements)
        by_section: dict[str, list[dict]] = defaultdict(list)
        for req in profile_reqs:
            by_section[req.get("section", "unknown")].append(req)

        if profile_reqs:
            summary = (
                f"**{len(profile_reqs)} normative IDs** in this profile "
                f"(`{profile_reqs[0]['id']}` - `{profile_reqs[-1]['id']}`)."
            )
        else:
            summary = "**0 normative IDs** in registry for this profile."

        lines.extend(
            [
                summary,
                "",
                "Full index: [Requirements index](../../site/REQUIREMENTS-INDEX.md).",
                "",
            ]
        )

        for section in sorted(by_section.keys()):
            rows = by_section[section]
            num, title, _ = SECTION_META.get(section, ("?", section, ""))
            lines.extend(
                [
                    f"### Section {num} - {title} ({len(rows)})",
                    "",
                    *requirement_table_rows(rows),
                    "",
                ]
            )

    lines.extend(["## Conformance coverage", ""])
    if manifest:
        lines.extend(
            [
                f"| Metric | Value |",
                f"|--------|-------|",
                f"| Requirements in profile | {manifest.get('requirement_count', '-')} |",
                f"| Linked tests | {manifest.get('test_count', '-')} |",
                f"| Implemented (smoke) | {impl_count} |",
                f"| Manifest | [`conformance/profiles/{pid}/manifest.yaml`](/conformance/profiles/{pid}/manifest.yaml) |",
                "",
                "Regenerate manifests: `python3 scripts/build-conformance-manifest.py`",
                "",
            ]
        )
    else:
        lines.append("_No generated manifest yet._")
        lines.append("")

    lines.extend(
        [
            "Related: [Section 1 - Scope and conformance](../01-scope-conformance/SPEC.md) section 1.6, "
            "[Profile comparison](../../site/PROFILES.md).",
            "",
        ]
    )
    return "\n".join(lines)


def inject_generated(content: str, generated: str) -> str:
    if GENERATED_START in content and GENERATED_END in content:
        before = content.split(GENERATED_START, 1)[0]
        after = content.split(GENERATED_END, 1)[1]
        return f"{before}{GENERATED_START}\n\n{generated}\n{GENERATED_END}{after}"
    return content.rstrip() + f"\n\n---\n\n{GENERATED_START}\n\n{generated}\n{GENERATED_END}\n"


def main() -> int:
    if not REQUIREMENTS.is_file():
        print(f"ERROR: missing {REQUIREMENTS}", file=sys.stderr)
        return 1
    if not PROFILES_YAML.is_file():
        print(f"ERROR: missing {PROFILES_YAML}", file=sys.stderr)
        return 1

    registry = json.loads(REQUIREMENTS.read_text(encoding="utf-8"))
    requirements = registry.get("requirements", [])
    version = registry.get("spec_version", "unknown")
    profiles = parse_profiles_yaml()
    by_id = {p["id"]: p for p in profiles}

    for pid, filename in PROFILE_FILES.items():
        profile = by_id.get(pid)
        if not profile:
            print(f"WARN: profile {pid} not in profiles.yaml", file=sys.stderr)
            continue
        path = PROFILES_DIR / filename
        if not path.is_file():
            print(f"WARN: missing {path}", file=sys.stderr)
            continue
        generated = generate_profile_block(profile, requirements, version)
        updated = inject_generated(path.read_text(encoding="utf-8"), generated)
        path.write_text(updated, encoding="utf-8")
        count = len(registry_requirements_for_profile(profile, requirements))
        if pid == "extended":
            refs, drafts = parse_extended_annex()
            count = len(refs) + len(drafts)
        print(f"Wrote {path.relative_to(ROOT)} ({count} requirement rows)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
