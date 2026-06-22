#!/usr/bin/env python3
"""Replace path-like Markdown link labels with human-readable titles."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MKDOCS = ROOT / "site/mkdocs.yml"

LINK_RE = re.compile(r"\[(`?)([^\]`]+)\1\]\(([^)]+)\)")
HTML_LINK_RE = re.compile(
    r'(<a\s+href=")([^"]+)(">)([^<]+)(</a>)',
    re.IGNORECASE,
)
ODTIS_ID_RE = re.compile(r"^ODTIS-\d{4}$")

SECTION_TITLES = {
    "01-scope-conformance": "Section 1 - Scope and conformance",
    "02-terminology-loa": "Section 2 - Terminology and LoA",
    "03-identity-services": "Section 3 - Identity services",
    "04-trust-network": "Section 4 - Trust network",
    "05-consent-privacy": "Section 5 - Consent and privacy",
    "06-federation": "Section 6 - Federation",
    "07-operator-governance": "Section 7 - Operator governance",
    "08-security": "Section 8 - Security",
    "09-audit-events": "Section 9 - Audit and events",
    "10-deployment-profiles": "Section 10 - Deployment",
}

PROFILE_TITLES = {
    "reference-architecture-profile.md": "Reference Architecture profile",
    "core-identity-profile.md": "Core Identity profile",
    "trust-network-profile.md": "Trust Network profile",
    "federation-profile.md": "Federation profile",
    "operator-profile.md": "Operator profile",
    "extended-profile.md": "Extended profile",
}

ARTIFACT_TITLES = {
    "requirements.json": "Requirements registry",
    "profiles.yaml": "Profile definitions",
    "domains.yaml": "Structural domains",
    "id-map.yaml": "Legacy ID map",
    "events.yaml": "Audit event catalog",
    "terminology.yaml": "Terminology registry",
    "book1-domains.yaml": "Book 1 domain map (YAML)",
    "manifest.yaml": "Conformance manifest",
    "conformance-statement.yaml": "Conformance statement template",
    "program.yaml": "Certification program (YAML)",
    "RI-MAP.yaml": "RI surface map",
    "rf-index.yaml": "RF traceability index",
    "coverage-report.yaml": "Coverage report",
    "gaps.yaml": "Gap register (YAML)",
    "mapping.yaml": "Standards mapping",
    "standards.yaml": "Standards catalog",
    "loa-matrix.yaml": "LoA crosswalk matrix",
    "threats.yaml": "Threat mitigations catalog",
    "CITATION.cff": "Citation metadata (CFF)",
    "venid-common.openapi.yaml": "VenID common schemas (OpenAPI)",
    "verification-api.openapi.yaml": "Verification API (OpenAPI)",
    "citizen-api.openapi.yaml": "Citizen API (OpenAPI)",
    "admin-api.openapi.yaml": "Admin API (OpenAPI)",
    "regulator-api.openapi.yaml": "Regulator API (OpenAPI)",
    "reports-api.openapi.yaml": "RP Reports API (OpenAPI)",
    "gov-api.openapi.yaml": "Government API (OpenAPI)",
    "exchange-gateway.openapi.yaml": "Exchange gateway (OpenAPI)",
    "INDEX.yaml": "Surface index (YAML)",
}

EXTRA_TITLES = {
    "index.md": "Home",
    "project/README.md": "Project hub",
    "spec/INDEX.md": "Specification index",
    "annexes/README.md": "Annexes overview",
    "conformance/README.md": "Conformance overview",
    "governance/README.md": "Governance overview",
    "implementation/README.md": "Reference implementations overview",
    "ietf/README.md": "IETF working drafts overview",
    "registry/README.md": "Requirements registry guide",
    "spec/profiles/README.md": "Profile index",
    "conformance/certification/README.md": "Certification docs index",
    "conformance/sandbox/README.md": "Sandbox alignment",
    "governance/rfc/README.md": "RFC drafts index",
    "governance/review/README.md": "Review templates index",
    "governance/working-groups/README.md": "Working groups",
    "annexes/A-openapi-registry/README.md": "Annex A - OpenAPI registry",
    "annexes/A-openapi-registry/FREEZE.md": "Annex A freeze record",
    "annexes/A-openapi-registry/oidc-discovery.md": "OIDC discovery contract",
    "annexes/B-threat-mitigations/README.md": "Annex B - Threat mitigations",
    "annexes/B-threat-mitigations/red-team-scenarios.md": "Red team scenarios",
    "annexes/C-standards-mapping/README.md": "Annex C - Standards mapping",
    "annexes/D-extended-profiles/README.md": "Annex D - Extended profiles",
    "site/GETTING-STARTED.md": "Getting started",
    "site/STATUS.md": "Project status",
    "site/FAQ.md": "FAQ",
    "site/DOWNLOADS.md": "Downloads",
    "site/ARTIFACTS.md": "Machine-readable artifacts",
    "site/PROFILES.md": "Profile comparison",
    "site/DOMAINS.md": "Domain map",
    "site/GLOSSARY.md": "Glossary",
    "site/REQUIREMENTS-INDEX.md": "Requirements index",
    "site/COMPONENT-BINDINGS.md": "Component bindings",
    "site/REPOSITORY-README.md": "Repository README",
    "ADOPTION.md": "Adoption guide",
    "STRUCTURE.md": "Repository map",
    "PLAN-PHASES.md": "Build plan",
    "CHANGELOG.md": "Changelog",
    "registry/BOOK1-DOMAINS.md": "Book 1 domain map",
    "publication/HOW-TO-CITE.md": "How to cite",
    "publication/zenodo/RELEASE-CHECKLIST.md": "Zenodo release checklist",
    "implementation/DOCUMENTATION-ROADMAP.md": "Documentation roadmap",
    "implementation/L3-CERTIFICATION-PACKAGE.md": "L3 certification package",
    "implementation/gaps/KNOWN-GAPS.md": "Known gaps",
    "implementation/gaps/DEFERRED-TRACK.md": "Deferred production track",
    "implementation/reports/ODTIS-CONSISTENCY-AUDIT-2026.md": "Consistency audit report",
    "conformance/FAQ.md": "Conformance FAQ",
    "conformance/certification/self-cert-guide.md": "Self-certification guide",
    "conformance/certification/auditor-guide.md": "Auditor guide",
    "conformance/certification/L3-AUDIT-CHECKLIST.md": "L3 audit checklist",
    "conformance/sandbox/L2-REPORT-TEMPLATE.md": "L2 report template",
    "governance/CERTIFICATION.md": "Certification program",
    "governance/CONTRIBUTING.md": "Contributing guide",
    "governance/SPEC-STAGES.md": "Spec lifecycle stages",
    "governance/FEEDBACK.md": "Feedback channels",
    "governance/REVIEW-CYCLE-1.md": "External review cycle 1",
    "governance/REVIEW-CYCLE-1-CLOSE.md": "Review close checklist",
    "governance/SECTION-REVIEW.md": "Section review matrix",
    "governance/ANNEX-REVIEW.md": "Annex review matrix",
    "governance/BOOK2-CROSS-REVIEW.md": "Book 2 cross-review",
    "governance/GOVERNANCE.md": "Governance process",
    "governance/VERSIONING.md": "Versioning policy",
    "governance/LANGUAGE.md": "Language policy",
    "governance/IPR-POLICY.md": "IPR policy",
    "governance/TRADEMARK-POLICY.md": "Trademark policy",
    "governance/ERRATA.md": "Errata policy",
    "governance/MAINTAINERS.md": "Maintainers",
    "governance/FOUNDATION-CHARTER.md": "Foundation charter",
    "governance/IETF-ROADMAP.md": "IETF roadmap",
    "governance/RFC-TEMPLATE.md": "RFC template",
    "governance/liaison/OIDF-POSITIONING.md": "OIDF positioning",
    "governance/liaison/GOVSTACK-POSITIONING.md": "GovStack positioning",
    "governance/liaison/IETF-SCOPING.md": "IETF scoping",
    "governance/liaison/NIST-XROAD-INDEX.md": "NIST and X-Road index",
    "governance/rfc/2026-06-12-federation-interoperability.md": "Federation interoperability RFC",
    "ietf/drafts/draft-odtis-tep-00.md": "TEP draft",
    "ietf/drafts/draft-odtis-verify-api-00.md": "Verify API draft",
    "ietf/drafts/draft-odtis-events-00.md": "Events draft",
    "ietf/drafts/draft-odtis-federation-00.md": "Federation protocol draft",
    "ietf/implementation-report/TEMPLATE.md": "Implementation report template",
    "implementation/statements/venid-phase4-full/conformance-statement.md": "Phase 4 conformance statement",
    "scripts/build-site.sh": "Site build script",
    "scripts/deploy-site.sh": "Site deploy script",
    "scripts/package-release.sh": "Release packaging script",
    "governance/review/clarify-001-5.1.4-test-linkage.md": "FB-001 test linkage",
    "governance/review/clarify-002-ha-informative-boundary.md": "FB-003 HA boundary",
    "governance/review/clarify-003-autodiscovery-should.md": "FB-004 autodiscovery",
    "governance/review/sandbox-001-l2-report-template.md": "FB-005 sandbox template",
}

DIR_TITLES = {
    "spec/": "Specification sections",
    "spec/profiles/": "Conformance profiles",
    "registry/": "Registry",
    "annexes/": "Annexes",
    "annexes/A-openapi-registry/": "Annex A OpenAPI registry",
    "annexes/C-standards-mapping/": "Annex C standards mapping",
    "implementation/": "Reference implementations",
    "registry/events/schemas/": "Event JSON schemas",
    "conformance/tests/": "Conformance test procedures",
    "conformance/tests/{profile}/": "Profile test procedures",
    "conformance/profiles/": "Profile manifests",
    "implementation/component-bindings/": "Component bindings",
    "implementation/statements/": "Conformance statements",
    "traceability/": "Traceability artifacts",
}


def load_nav_titles() -> dict[str, str]:
    titles: dict[str, str] = dict(EXTRA_TITLES)

    def walk(node, _key: str | None = None) -> None:
        if isinstance(node, str):
            titles[node] = _key or titles.get(node, title_for_path(node))
            return
        if isinstance(node, dict):
            for k, v in node.items():
                walk(v, k)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    if MKDOCS.is_file():
        in_nav = False
        nav_items: list = []
        for line in MKDOCS.read_text(encoding="utf-8").splitlines():
            if line.strip() == "nav:":
                in_nav = True
                continue
            if in_nav:
                if line and not line.startswith(" ") and not line.startswith("-"):
                    break
                nav_items.append(line)
        # crude YAML parse via regex for "Title: path"
        for line in nav_items:
            m = re.match(r"\s+-\s+(.+?):\s+(\S+\.md)\s*$", line)
            if m:
                titles[m.group(2)] = m.group(1).strip('"')
            m = re.match(r"\s+(.+?):\s+(\S+\.md)\s*$", line)
            if m and not m.group(1).startswith("-"):
                titles[m.group(2)] = m.group(1).strip('"')
    return titles


def normalize_target(target: str) -> str:
    target = target.split("#", 1)[0].strip()
    target = target.replace("\\", "/")
    while target.startswith("../"):
        target = target[3:]
    while target.startswith("./"):
        target = target[2:]
    return target


def title_for_path(path: str) -> str:
    path = normalize_target(path)
    if path in DIR_TITLES:
        return DIR_TITLES[path]
    if path in PROFILE_TITLES:
        return PROFILE_TITLES[path]
    name = Path(path).name
    if name in PROFILE_TITLES:
        return PROFILE_TITLES[name]
    if name in ARTIFACT_TITLES:
        return ARTIFACT_TITLES[name]
    if name == "README.md":
        parent = Path(path).parent.name.replace("-", " ")
        if parent:
            return f"{parent.replace('_', ' ').title()} overview"
        return "Overview"
    if name == "SPEC.md":
        section = Path(path).parent.name
        if section in SECTION_TITLES:
            return SECTION_TITLES[section]
    if name == "FREEZE.md":
        return "Freeze record"
    if name.endswith(".openapi.yaml"):
        stem = name.replace(".openapi.yaml", "").replace("-", " ")
        return f"{stem.title()} (OpenAPI)"
    if name.endswith(".yaml"):
        stem = name.replace(".yaml", "").replace("-", " ")
        return f"{stem.title()} (YAML)"
    if name.endswith(".json"):
        stem = name.replace(".json", "").replace("-", " ")
        return f"{stem.title()} (JSON)"
    if name.endswith(".md"):
        stem = name.replace(".md", "")
        if stem.startswith("draft-odtis-"):
            return stem.replace("draft-odtis-", "").replace("-00", "").replace("-", " ").upper() + " draft"
        return stem.replace("-", " ").replace("_", " ").title()
    if name.endswith(".sh"):
        return name.replace(".sh", "").replace("-", " ").title() + " script"
    if name.endswith(".py"):
        return name.replace(".py", "").replace("-", " ").title() + " script"
    stem = Path(path).name
    return stem.replace("-", " ").replace("_", " ").title()


def is_path_like_label(label: str) -> bool:
    text = label.strip().strip("`")
    if not text or text.startswith("ODTIS-"):
        return False
    if text.startswith("http://") or text.startswith("https://"):
        return False
    if re.match(r"^spec/\d{2}-", text):
        return True
    if "/" in text:
        return True
    if re.search(r"\.(md|yaml|yml|json|sh|py|cff|openapi\.yaml)\b", text, re.I):
        return True
    if re.match(r"^[A-Z][A-Z0-9_-]+\.md$", text):
        return True
    return False


def resolve_title(label: str, target: str, titles: dict[str, str]) -> str:
    norm = normalize_target(target)
    if norm in titles:
        return titles[norm]
    # try without leading path variations
    for key, title in titles.items():
        if norm.endswith(key) or key.endswith(norm):
            return title
    if norm in DIR_TITLES:
        return DIR_TITLES[norm]
    return title_for_path(norm or label)


def fix_markdown_links(text: str, titles: dict[str, str]) -> tuple[str, int]:
    changes = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal changes
        tick, label, target = m.group(1), m.group(2), m.group(3)
        if not is_path_like_label(label):
            return m.group(0)
        new_label = resolve_title(label, target, titles)
        if new_label == label.strip("`"):
            return m.group(0)
        changes += 1
        if tick and ODTIS_ID_RE.match(new_label.strip()):
            return f"[`{new_label}`]({target})"
        return f"[{new_label}]({target})"

    text = LINK_RE.sub(repl, text)
    return text, changes


def fix_html_links(text: str, titles: dict[str, str]) -> tuple[str, int]:
    changes = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal changes
        prefix, href, mid, label, suffix = m.groups()
        if not is_path_like_label(label):
            return m.group(0)
        new_label = resolve_title(label, href, titles)
        if new_label == label:
            return m.group(0)
        changes += 1
        return f"{prefix}{href}{mid}{new_label}{suffix}"

    text = HTML_LINK_RE.sub(repl, text)
    return text, changes


def should_process(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if ".venv" in rel or rel.startswith("build/"):
        return False
    if rel.startswith("conformance/tests/"):
        return False
    if rel.startswith("conformance/profiles/") and path.name == "README.md":
        return False
    if "Generated by" in path.read_text(encoding="utf-8")[:300] and path.name in {
        "DOMAINS.md",
        "REQUIREMENTS-INDEX.md",
        "GLOSSARY.md",
        "COMPONENT-BINDINGS.md",
    }:
        return True  # still fix links in generated files
    return True


def main() -> int:
    apply = "--apply" in sys.argv
    titles = load_nav_titles()
    total_files = 0
    total_changes = 0

    for path in sorted(ROOT.rglob("*.md")):
        if not should_process(path):
            continue
        original = path.read_text(encoding="utf-8")
        updated, n1 = fix_markdown_links(original, titles)
        updated, n2 = fix_html_links(updated, titles)
        n = n1 + n2
        if n:
            total_files += 1
            total_changes += n
            rel = path.relative_to(ROOT)
            print(f"{'WRITE' if apply else 'WOULD'} {rel}: {n} link(s)")
            if apply:
                path.write_text(updated, encoding="utf-8")

    print(f"\n{'Updated' if apply else 'Would update'} {total_changes} link label(s) in {total_files} file(s)")
    if not apply:
        print("Re-run with --apply to write changes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
