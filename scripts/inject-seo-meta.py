#!/usr/bin/env python3
"""Ensure SEO front matter (title, description) on high-traffic ODTIS pages."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# path relative to core-spec/ -> (title, description)
SEO: dict[str, tuple[str, str]] = {
    "index.md": (
        "Open Digital Trust Infrastructure Specification",
        "ODTIS: vendor-neutral open standard for digital identity, trust networks, and institutional exchange. "
        "204 normative requirements, 7 conformance profiles, frozen OpenAPI Annex A, L1/L2/L3 verification.",
    ),
    "ADOPTION.md": (
        "ODTIS adoption guide",
        "How to adopt ODTIS: profiles, Annex A OpenAPI, conformance tests, self-certification (L2), and certification paths for vendors and operators.",
    ),
    "project/README.md": (
        "ODTIS project overview",
        "Project hub for ODTIS status, downloads, governance, reference implementations, IETF track, and publication.",
    ),
    "spec/INDEX.md": (
        "ODTIS specification index",
        "Normative index for ODTIS sections 1-11, adoptable profiles, annexes, and machine-readable registry artifacts.",
    ),
    "conformance/README.md": (
        "ODTIS conformance overview",
        "Conformance levels L1, L2, and L3; seven profiles; test procedures; self-certification and L3 certification program.",
    ),
    "site/GETTING-STARTED.md": (
        "Getting started with ODTIS",
        "15-minute path to read the spec, pick a profile, run L1 validators, and plan an honest conformance claim.",
    ),
    "site/FAQ.md": (
        "ODTIS FAQ",
        "Complete FAQ: ODTIS vs OIDC, OpenID Federation, eIDAS, profiles, Annex A OpenAPI download, L1/L2/L3 self-certification, Extended modules, and adoption for governments and vendors.",
    ),
    "site/DOWNLOADS.md": (
        "ODTIS downloads and artifacts",
        "Download OpenAPI bundles, requirement registry, event schemas, conformance manifests, and machine-readable ODTIS artifacts.",
    ),
    "site/STATUS.md": (
        "ODTIS project status",
        "Current maturity, review draft stage, coverage metrics, and honest readiness assessment for ODTIS 0.9.0-draft.",
    ),
    "publication/HOW-TO-CITE.md": (
        "How to cite ODTIS",
        "Citation formats for the ODTIS working draft, Zenodo DOI, and profile-specific conformance references.",
    ),
    "spec/01-scope-conformance/SPEC.md": (
        "Section 1: Scope and conformance",
        "Normative scope, adoptable profiles, conformance levels L1/L2/L3, and RFC 2119 keywords for ODTIS implementations.",
    ),
    "spec/02-terminology-loa/SPEC.md": (
        "Section 2: Terminology and LoA",
        "Levels of assurance (LoA), NIST mapping, canonical claims, and terminology for ODTIS Core Identity.",
    ),
    "spec/03-identity-services/SPEC.md": (
        "Section 3: Identity services",
        "OIDC IdP, subject registry, verification API, proofing, citizen portal, and RP client lifecycle requirements.",
    ),
    "spec/04-trust-network/SPEC.md": (
        "Section 4: Trust network",
        "Exchange gateway, service catalog, access grants, mTLS, metadata-only routing, and trust network audit.",
    ),
    "spec/05-consent-privacy/SPEC.md": (
        "Section 5: Consent and privacy",
        "Consent capture, RP admission, privacy minimization, E-Registry, E-Wallet, and extended module requirements.",
    ),
    "spec/06-federation/SPEC.md": (
        "Section 6: Federation",
        "Bilateral federation agreements, non-transitivity, routing, regulator export, and federated trust establishment.",
    ),
    "spec/07-operator-governance/SPEC.md": (
        "Section 7: Operator governance",
        "DTI operator model, published service scope, SLA metrics, PKI stewardship, and regulator API requirements.",
    ),
    "spec/08-security/SPEC.md": (
        "Section 8: Security",
        "Security controls, OWASP baseline, fail-closed behavior, transport security, and incident reporting for ODTIS.",
    ),
    "spec/09-audit-events/SPEC.md": (
        "Section 9: Audit and events",
        "Audit event catalog, JSON schemas, envelope format, correlation IDs, and retention requirements.",
    ),
    "spec/10-deployment-profiles/SPEC.md": (
        "Section 10: Deployment profiles",
        "Cross-profile deployment phases, adoption matrix, and profile combination rules for ODTIS operators.",
    ),
}

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
TITLE_RE = re.compile(r"^title:\s*.+$", re.MULTILINE)
DESC_RE = re.compile(r"^description:\s*.+$", re.MULTILINE)


def yaml_quote(value: str) -> str:
    if any(ch in value for ch in ':"\'\n#'):
        escaped = value.replace('"', '\\"')
        return f'"{escaped}"'
    return value


def upsert_front_matter(text: str, title: str, description: str) -> str:
    title_line = f"title: {yaml_quote(title)}"
    desc_line = f"description: {yaml_quote(description)}"

    match = FM_RE.match(text)
    if not match:
        block = f"---\n{title_line}\n{desc_line}\n---\n\n"
        return block + text.lstrip("\n")

    fm = match.group(1)
    body = text[match.end() :]
    if TITLE_RE.search(fm):
        fm = TITLE_RE.sub(title_line, fm, count=1)
    else:
        fm = fm.rstrip() + f"\n{title_line}"
    if DESC_RE.search(fm):
        fm = DESC_RE.sub(desc_line, fm, count=1)
    else:
        fm = fm.rstrip() + f"\n{desc_line}"
    return f"---\n{fm}\n---\n{body}"


def main() -> int:
    changed = 0
    for rel, (title, description) in SEO.items():
        path = ROOT / rel
        if not path.is_file():
            print(f"WARN: missing {rel}", file=sys.stderr)
            continue
        original = path.read_text(encoding="utf-8")
        updated = upsert_front_matter(original, title, description)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(f"Updated SEO meta: {rel}")
            changed += 1
    print(f"Done ({changed} files updated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
