"""ODTIS four-digit identifier scheme (ODTIS-XXXX).

Domains ODTIS-0000 .. ODTIS-0006 are structural modules.
Normative requirements use ODTIS-MNNN where M is the domain hundreds digit
(00 = Reference Architecture, 01 = Core Concepts, ...).
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LEGACY_ID = re.compile(r"^ODTIS-\d+\.\d+\.\d+$")
CANONICAL_ID = re.compile(r"^ODTIS-\d{4}$")

DOMAINS: list[dict] = [
    {
        "id": "ODTIS-0000",
        "title": "Reference Architecture",
        "summary": "Two-layer model, profile composition, conformance claim structure, and scope boundaries.",
        "sections": ["01-scope-conformance"],
        "spec_paths": ["spec/01-scope-conformance/SPEC.md"],
        "status": "normative",
    },
    {
        "id": "ODTIS-0001",
        "title": "Core Concepts",
        "summary": "Terminology, LoA foundations, and assurance mapping.",
        "sections": ["02-terminology-loa"],
        "spec_paths": ["spec/02-terminology-loa/SPEC.md"],
        "status": "normative",
    },
    {
        "id": "ODTIS-0002",
        "title": "Trust Registry",
        "summary": "Partner registry, service catalog, exchange gateway, and institutional routing.",
        "sections": ["04-trust-network"],
        "spec_paths": ["spec/04-trust-network/SPEC.md"],
        "status": "normative",
    },
    {
        "id": "ODTIS-0003",
        "title": "Identity Assurance",
        "summary": "OIDC identity services, verification API, consent, and privacy controls.",
        "sections": ["03-identity-services", "05-consent-privacy"],
        "spec_paths": ["spec/03-identity-services/SPEC.md", "spec/05-consent-privacy/SPEC.md"],
        "status": "normative",
    },
    {
        "id": "ODTIS-0004",
        "title": "Federation",
        "summary": "Bilateral cross-operator trust and federated verification.",
        "sections": ["06-federation"],
        "spec_paths": ["spec/06-federation/SPEC.md"],
        "status": "normative",
    },
    {
        "id": "ODTIS-0005",
        "title": "Governance",
        "summary": "Operator duties, security controls, audit events, and deployment phases.",
        "sections": [
            "07-operator-governance",
            "08-security",
            "09-audit-events",
            "10-deployment-profiles",
        ],
        "spec_paths": [
            "spec/07-operator-governance/SPEC.md",
            "spec/08-security/SPEC.md",
            "spec/09-audit-events/SPEC.md",
            "spec/10-deployment-profiles/SPEC.md",
        ],
        "status": "normative",
    },
    {
        "id": "ODTIS-0006",
        "title": "Payment Trust Layer",
        "summary": "Reserved domain for payment-scoped trust extensions (out of ODTIS 0.9 scope).",
        "sections": [],
        "spec_paths": [],
        "status": "reserved",
    },
]

SECTION_TO_DOMAIN: dict[str, str] = {}
for domain in DOMAINS:
    for section in domain["sections"]:
        SECTION_TO_DOMAIN[section] = domain["id"]

DOMAIN_BY_ID = {d["id"]: d for d in DOMAINS}


def legacy_sort_key(legacy_id: str) -> tuple[int, ...]:
    parts = legacy_id.replace("ODTIS-", "").split(".")
    return tuple(int(p) for p in parts)


def requirement_id_for(domain_id: str, seq: int) -> str:
    domain_num = int(domain_id.split("-")[1])
    return f"ODTIS-{domain_num * 100 + seq:04d}"


def build_requirement_id_map(requirements: list[dict]) -> dict[str, str]:
    """Map legacy ODTIS-N.N.N IDs to canonical ODTIS-MNNN IDs."""
    by_domain: dict[str, list[dict]] = {d["id"]: [] for d in DOMAINS}
    for req in requirements:
        section = req.get("section", "")
        domain_id = SECTION_TO_DOMAIN.get(section)
        if not domain_id:
            raise ValueError(f"No domain for section {section!r} ({req.get('id')})")
        by_domain[domain_id].append(req)

    mapping: dict[str, str] = {}
    for domain_id, reqs in by_domain.items():
        if domain_id == "ODTIS-0006":
            continue
        ordered = sorted(reqs, key=lambda r: legacy_sort_key(r["id"]))
        for idx, req in enumerate(ordered, start=1):
            mapping[req["id"]] = requirement_id_for(domain_id, idx)
    return mapping
