#!/usr/bin/env python3
"""Merge Book 1 / VenID product requirements into registry and generate test stubs."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry/requirements.json"
ID_MAP = ROOT / "registry/id-map.yaml"

NEW_REQUIREMENTS: list[dict] = [
    # --- Reference Architecture (Book 1 section 1.7, section 1.9) ---
    {
        "id": "ODTIS-0007",
        "section": "01-scope-conformance",
        "keyword": "MUST NOT",
        "text": "Implementations MUST NOT use prohibited ODTIS claims including ODTIS certified without statement, Full ODTIS without listing profiles, or eIDAS/QTSP equivalence from ODTIS alone",
        "trace_informative": "P18 1.9.3, Book 1 cap. 5",
        "status": "normative",
        "domain": "ODTIS-0000",
        "legacy_id": "ODTIS-1.9.3",
        "profile": "reference-architecture",
        "slug": "prohibited_claims",
    },
    {
        "id": "ODTIS-0008",
        "section": "01-scope-conformance",
        "keyword": "MUST",
        "text": "Conformance statements MUST include odtis_version, profiles, extended_modules, level, operator, scope, requirements reference, tests summary, date, and contact",
        "trace_informative": "P18 1.9.1",
        "status": "normative",
        "domain": "ODTIS-0000",
        "legacy_id": "ODTIS-1.9.1",
        "profile": "reference-architecture",
        "slug": "statement_minimum_fields",
    },
    {
        "id": "ODTIS-0009",
        "section": "01-scope-conformance",
        "keyword": "MUST NOT",
        "text": "Implementations MUST NOT imply Trust Network, Federation, Operator, or Extended conformance when only Core Identity is declared",
        "trace_informative": "P18 1.7.4, Book 1 D1",
        "status": "normative",
        "domain": "ODTIS-0000",
        "legacy_id": "ODTIS-1.7.4",
        "profile": "reference-architecture",
        "slug": "minimal_claim_no_implied_profiles",
    },
    {
        "id": "ODTIS-0010",
        "section": "01-scope-conformance",
        "keyword": "MUST",
        "text": "Implementations MUST pass all applicable conformance tests for declared profiles and level, or mark tests partial and list pending test IDs without waiving MUST requirements",
        "trace_informative": "P18 1.9.2",
        "status": "normative",
        "domain": "ODTIS-0000",
        "legacy_id": "ODTIS-1.9.2",
        "profile": "reference-architecture",
        "slug": "applicable_tests_required",
    },
    # --- Trust Network (Book 1 D3/D4; RI client/discovery surfaces) ---
    {
        "id": "ODTIS-0222",
        "section": "04-trust-network",
        "keyword": "MUST",
        "text": "Synchronized service catalog entries for remote peers MUST include stable service_id and peer gateway_base_url suitable for sender route resolution",
        "trace_informative": "Book 1 D3, platform FASE-4",
        "status": "normative",
        "domain": "ODTIS-0002",
        "legacy_id": "ODTIS-4.8.1",
        "profile": "trust-network",
        "slug": "catalog_gateway_base_url",
    },
    {
        "id": "ODTIS-0223",
        "section": "04-trust-network",
        "keyword": "MUST",
        "text": "Sender gateway MUST resolve outbound routes by service_id from synchronized catalog without requiring a single hard-coded remote gateway URL for all peers",
        "trace_informative": "platform FASE-4, P05",
        "status": "normative",
        "domain": "ODTIS-0002",
        "legacy_id": "ODTIS-4.8.2",
        "profile": "trust-network",
        "slug": "sender_multi_peer_routing",
    },
    {
        "id": "ODTIS-0224",
        "section": "04-trust-network",
        "keyword": "MUST",
        "text": "Exchange gateway MUST fail closed when service grant validation fails; MUST NOT route on implicit network-zone trust",
        "trace_informative": "Book 2 ch.3.7 rule 1, Book 1 D4",
        "status": "normative",
        "domain": "ODTIS-0002",
        "legacy_id": "ODTIS-4.8.3",
        "profile": "trust-network",
        "slug": "grant_fail_closed",
    },
    {
        "id": "ODTIS-0225",
        "section": "04-trust-network",
        "keyword": "MUST NOT",
        "text": "Trust network metadata stores MUST NOT persist full business payloads as authoritative copies; routing metadata and audit envelopes only (Book 1 D4)",
        "trace_informative": "Book 1 D4, P01 metadata model",
        "status": "normative",
        "domain": "ODTIS-0002",
        "legacy_id": "ODTIS-4.8.4",
        "profile": "trust-network",
        "slug": "no_payload_centralization",
    },
    {
        "id": "ODTIS-0226",
        "section": "04-trust-network",
        "keyword": "MUST",
        "text": "Grant request, approval, and revocation workflows MUST emit auditable events when operator policy uses explicit service access grants",
        "trace_informative": "platform ANALISIS catalog/grants, P04",
        "status": "normative",
        "domain": "ODTIS-0002",
        "legacy_id": "ODTIS-4.8.5",
        "profile": "trust-network",
        "slug": "grant_workflow_audit",
    },
    # --- Federation (Book 1 D9) ---
    {
        "id": "ODTIS-0407",
        "section": "06-federation",
        "keyword": "MUST",
        "text": "Suspended or expired federation agreements MUST disable federated routing on subsequent requests within documented cache refresh bounds",
        "trace_informative": "P09, Book 1 D9",
        "status": "normative",
        "domain": "ODTIS-0004",
        "legacy_id": "ODTIS-6.2.2",
        "profile": "federation",
        "slug": "agreement_suspension_routing",
    },
    {
        "id": "ODTIS-0408",
        "section": "06-federation",
        "keyword": "MUST",
        "text": "Federated exchange audit events MUST include local trust instance identifier and remote trust instance identifier",
        "trace_informative": "Book 2 ch.6.8, P09",
        "status": "normative",
        "domain": "ODTIS-0004",
        "legacy_id": "ODTIS-6.2.3",
        "profile": "federation",
        "slug": "federated_audit_instance_ids",
    },
    # --- Operator (Book 1 cap. 5, Book 2 design rules) ---
    {
        "id": "ODTIS-0534",
        "section": "10-deployment-profiles",
        "keyword": "MUST",
        "text": "Operator MUST publish conformance statements in both human-readable and machine-readable forms",
        "trace_informative": "P18 1.9.1, Book 1 cap. 5.4",
        "status": "normative",
        "domain": "ODTIS-0005",
        "legacy_id": "ODTIS-10.2.1",
        "profile": "operator",
        "slug": "conformance_statement_dual_format",
    },
    {
        "id": "ODTIS-0535",
        "section": "08-security",
        "keyword": "MUST",
        "text": "Auth, consent, and grant denial paths MUST fail closed without partial attribute release or implicit trust fallback",
        "trace_informative": "Book 2 ch.3.7 rule 1, Book 1 D5",
        "status": "normative",
        "domain": "ODTIS-0005",
        "legacy_id": "ODTIS-8.3.1",
        "profile": "operator",
        "slug": "fail_closed_denial_paths",
    },
    {
        "id": "ODTIS-0536",
        "section": "07-operator-governance",
        "keyword": "MUST",
        "text": "Operator MUST maintain a reference implementation map or equivalent component-to-profile trace for L2 auditors when claiming VenID-class deployments",
        "trace_informative": "implementation/RI-MAP.yaml, ADOPTION.md",
        "status": "normative",
        "domain": "ODTIS-0005",
        "legacy_id": "ODTIS-7.6.1",
        "profile": "operator",
        "slug": "implementation_traceability_map",
    },
    # --- Extended E-Registry anchor (Book 1 D7) ---
    {
        "id": "ODTIS-0344",
        "section": "05-consent-privacy",
        "keyword": "MUST",
        "text": "National LoA via civil registry adapter MUST be offered only when E-Registry Extended sub-module is declared and registry adapter is active",
        "trace_informative": "Book 1 D7, ODTIS-0104, P11",
        "status": "normative",
        "domain": "ODTIS-0003",
        "legacy_id": "ODTIS-5.5.0",
        "profile": "extended",
        "slug": "eregistry_declaration_required",
        "sub_module": "E-Registry",
    },
]

# Annex D drafts merged into registry (product backlog for VenID implementation)
EXTENDED_DRAFTS: list[dict] = [
    {
        "id": "ODTIS-0349",
        "keyword": "MUST NOT",
        "text": "E-Registry MUST NOT replace civil registry legal authority or issue national ID documents",
        "trace_informative": "P11 1.1, RF-EXT5",
        "legacy_id": "ODTIS-5.5.1",
        "slug": "eregistry_no_civil_authority",
        "sub_module": "E-Registry",
    },
    {
        "id": "ODTIS-0350",
        "keyword": "MUST",
        "text": "National LoA MUST be assigned only after successful registry adapter verification per operator policy",
        "trace_informative": "P11 4.2, ODTIS-0344",
        "legacy_id": "ODTIS-5.5.2",
        "slug": "national_loa_after_adapter",
        "sub_module": "E-Registry",
    },
    {
        "id": "ODTIS-0351",
        "keyword": "MUST",
        "text": "Registry adapter MUST use agreed identifier hashing; raw registry biometrics MUST NOT be persisted in Core Identity",
        "trace_informative": "P11 5.1",
        "legacy_id": "ODTIS-5.5.3",
        "slug": "registry_hash_no_biometric_store",
        "sub_module": "E-Registry",
    },
    {
        "id": "ODTIS-0352",
        "keyword": "MUST",
        "text": "Registry adapter activation MUST require deployment Phase 3+ and documented bilateral agreement with registry authority",
        "trace_informative": "P11 4.2, P10",
        "legacy_id": "ODTIS-5.5.4",
        "slug": "eregistry_phase3_activation",
        "sub_module": "E-Registry",
    },
    {
        "id": "ODTIS-0353",
        "keyword": "MUST",
        "text": "Every registry verification call MUST emit auditable events with correlation ID and match outcome metadata",
        "trace_informative": "P11 5.1, ODTIS-0526",
        "legacy_id": "ODTIS-5.5.5",
        "slug": "registry_verification_audit",
        "sub_module": "E-Registry",
    },
    {
        "id": "ODTIS-0354",
        "keyword": "MUST",
        "text": "Assisted registration flows MUST obtain explicit subject or legal-representative consent with full audit trail",
        "trace_informative": "P13 representative model, RF-15",
        "legacy_id": "ODTIS-5.6.1",
        "slug": "inclusion_assisted_consent",
        "sub_module": "E-Inclusion",
    },
    {
        "id": "ODTIS-0355",
        "keyword": "MUST",
        "text": "Representative or tutor flows MUST verify legal relationship before attribute release on behalf of another subject",
        "trace_informative": "P13 5.3, UC-C07",
        "legacy_id": "ODTIS-5.6.2",
        "slug": "inclusion_representative_verify",
        "sub_module": "E-Inclusion",
    },
    {
        "id": "ODTIS-0356",
        "keyword": "MUST NOT",
        "text": "Inclusion channels MUST NOT bypass LoA proofing rules defined for online registration",
        "trace_informative": "P18 4.2, RF-06",
        "legacy_id": "ODTIS-5.6.3",
        "slug": "inclusion_no_loa_bypass",
        "sub_module": "E-Inclusion",
    },
    {
        "id": "ODTIS-0357",
        "keyword": "SHOULD",
        "text": "Inclusion flows SHOULD support operator-configured locales, accessibility, and offline capture with deferred sync where policy allows",
        "trace_informative": "RNF-22, doc-14",
        "legacy_id": "ODTIS-5.6.4",
        "slug": "inclusion_accessibility_offline",
        "sub_module": "E-Inclusion",
    },
    {
        "id": "ODTIS-0358",
        "keyword": "MUST",
        "text": "E-Webhook MUST allow RPs to register callback URLs, subscribed event types, and shared signing secret via authenticated API",
        "trace_informative": "P14 6.4, RF-22",
        "legacy_id": "ODTIS-5.7.1",
        "slug": "ewebhook_rp_registration",
        "sub_module": "E-Webhook",
    },
    {
        "id": "ODTIS-0359",
        "keyword": "MUST",
        "text": "Webhook delivery MUST retry with backoff on failure and log delivery outcomes for operator review",
        "trace_informative": "P14 6.4, DS-07",
        "legacy_id": "ODTIS-5.7.2",
        "slug": "ewebhook_retry_backoff",
        "sub_module": "E-Webhook",
    },
    {
        "id": "ODTIS-0360",
        "keyword": "MUST",
        "text": "Webhook payloads MUST minimize PII; use opaque subject references where operator policy requires",
        "trace_informative": "P14 6.4, ODTIS-0530",
        "legacy_id": "ODTIS-5.7.3",
        "slug": "ewebhook_pii_minimize",
        "sub_module": "E-Webhook",
    },
    {
        "id": "ODTIS-0361",
        "keyword": "MUST",
        "text": "E-Signature MUST bind each signature operation to a verified subject identity and active LoA meeting RP policy",
        "trace_informative": "RF-EXT1, P08",
        "legacy_id": "ODTIS-5.8.1",
        "slug": "esignature_loa_binding",
        "sub_module": "E-Signature",
    },
    {
        "id": "ODTIS-0362",
        "keyword": "MUST",
        "text": "Signature keys MUST be issued under operator PKI or recognized TSP integration documented in CP/CPS",
        "trace_informative": "P08, ODTIS-0507",
        "legacy_id": "ODTIS-5.8.2",
        "slug": "esignature_pki_keys",
        "sub_module": "E-Signature",
    },
    {
        "id": "ODTIS-0363",
        "keyword": "MUST",
        "text": "Signature creation and verification events MUST be auditable with correlation to subject_id and RP client_id",
        "trace_informative": "RF-EXT1, ODTIS-0526",
        "legacy_id": "ODTIS-5.8.3",
        "slug": "esignature_audit_events",
        "sub_module": "E-Signature",
    },
    {
        "id": "ODTIS-0364",
        "keyword": "MUST",
        "text": "E-KYB MUST verify legal entity identity separately from natural-person Core Identity proofing",
        "trace_informative": "doc-03 sector KYB",
        "legacy_id": "ODTIS-5.9.1",
        "slug": "ekyb_entity_separate",
        "sub_module": "E-KYB",
        "status": "preview",
    },
    {
        "id": "ODTIS-0365",
        "keyword": "SHOULD",
        "text": "E-KYB SHOULD link authorized representatives to verified natural-person subjects before B2B attribute release",
        "trace_informative": "UC-E07, RF-EXT5",
        "legacy_id": "ODTIS-5.9.2",
        "slug": "ekyb_representative_link",
        "sub_module": "E-KYB",
        "status": "preview",
    },
]


def test_path(profile: str, slug: str, rid: str) -> str:
    return f"conformance/tests/{profile}/test_{slug}.md"


def write_test_stub(path: Path, req: dict, profile: str) -> None:
    if path.is_file():
        return
    rid = req["id"]
    keyword = req.get("keyword", "MUST")
    text = req["text"]
    sub = req.get("sub_module")
    lines = [
        f"# Conformance test: {rid} - {profile} product requirement",
        "",
        "**Status:** pending implementation",
        f"**Requirement:** {rid}",
        f"**Profile:** {profile}",
    ]
    if sub:
        lines.append(f"**Sub-module:** {sub}")
    lines.extend(
        [
            f"**Trace:** {req.get('trace_informative', '-')}",
            "",
            "## Procedure",
            "",
            f"1. Configure target per declared profile and operator policy.",
            f"2. Verify behavior required by: {text[:120]}{'...' if len(text) > 120 else ''}",
            "3. Record evidence (API traces, audit logs, policy documents, or configuration export).",
            "",
            "## Pass criteria",
            "",
            f"Implementation satisfies {rid} ({keyword}) as declared in ODTIS spec prose.",
            "",
            "## VenID reference stack (informative)",
            "",
            "Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def append_id_map(entries: list[tuple[str, str]]) -> None:
    text = ID_MAP.read_text(encoding="utf-8")
    additions = []
    for legacy, canonical in entries:
        key = f"  {legacy}: {canonical}"
        if key not in text:
            additions.append(key)
    if not additions:
        return
    marker = "# Deprecated draft IDs"
    if marker in text:
        block = "\n".join(additions) + "\n\n"
        text = text.replace(marker, block + marker, 1)
    else:
        text = text.rstrip() + "\n" + "\n".join(additions) + "\n"
    ID_MAP.write_text(text, encoding="utf-8")


def main() -> int:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    by_id = {r["id"]: r for r in data["requirements"]}
    id_map_additions: list[tuple[str, str]] = []
    added = 0

    for raw in NEW_REQUIREMENTS:
        rid = raw["id"]
        if rid in by_id:
            continue
        profile = raw.pop("profile")
        slug = raw.pop("slug")
        raw.pop("sub_module", None)
        rel_test = test_path(profile, slug, rid)
        raw["conformance_test"] = rel_test
        by_id[rid] = raw
        write_test_stub(ROOT / rel_test, raw, profile)
        id_map_additions.append((raw["legacy_id"], rid))
        added += 1

    for raw in EXTENDED_DRAFTS:
        rid = raw["id"]
        if rid in by_id:
            # ensure test link exists
            if not by_id[rid].get("conformance_test"):
                slug = raw["slug"]
                rel_test = test_path("extended", slug, rid)
                by_id[rid]["conformance_test"] = rel_test
                write_test_stub(ROOT / rel_test, {**by_id[rid], **raw}, "extended")
            continue
        entry = {
            "id": rid,
            "section": "05-consent-privacy",
            "keyword": raw["keyword"],
            "text": raw["text"],
            "trace_informative": raw["trace_informative"],
            "status": raw.get("status", "normative"),
            "domain": "ODTIS-0003",
            "legacy_id": raw["legacy_id"],
        }
        rel_test = test_path("extended", raw["slug"], rid)
        entry["conformance_test"] = rel_test
        by_id[rid] = entry
        write_test_stub(ROOT / rel_test, {**entry, "sub_module": raw["sub_module"]}, "extended")
        id_map_additions.append((raw["legacy_id"], rid))
        added += 1

    data["requirements"] = sorted(by_id.values(), key=lambda r: r["id"])
    data["requirement_count"] = len(data["requirements"])
    REGISTRY.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    append_id_map(id_map_additions)

    print(f"Added {added} requirements; total {data['requirement_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
