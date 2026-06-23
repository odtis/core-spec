#!/usr/bin/env python3
"""Generate VenID phased implementation backlog from ODTIS registry."""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry/requirements.json"
OUT_YAML = ROOT / "implementation/phased-backlog.yaml"
OUT_MD = ROOT / "implementation/PHASED-BACKLOG.md"
GITHUB_ODTIS = "https://github.com/odtis/core-spec/blob/main"

sys.path.insert(0, str(ROOT / "scripts"))
from profile_registry import load_requirements, parse_profiles_yaml, profile_requirement_ids  # noqa: E402

PHASES = [
    {
        "id": "P0",
        "odtis_phase": 0,
        "name": "Spec and conformance foundation",
        "goal": "Publishable conformance claims, RI traceability, L1 lab ready.",
        "profiles": ["reference-architecture"],
        "book1_gate": "Mandato operador + baseline medible antes de produccion.",
    },
    {
        "id": "P1",
        "odtis_phase": 1,
        "name": "Pilot / sandbox - Core Identity",
        "goal": "Layer 1 IdP, consent, verification API; L1-L2 sandbox.",
        "profiles": ["reference-architecture", "core-identity"],
        "book1_gate": "5-10 RPs piloto; sin Extended en produccion (ODTIS-0533).",
    },
    {
        "id": "P2",
        "odtis_phase": 2,
        "name": "Production Layer 2 - Trust Network",
        "goal": "Exchange gateway, catalog, grants, multi-peer routing; TN L2.",
        "profiles": ["core-identity", "trust-network"],
        "book1_gate": "Nodos institucionales + grants + catalogo consumido (D3/D4).",
    },
    {
        "id": "P3",
        "odtis_phase": 3,
        "name": "National operator",
        "goal": "Operator PKI/governance, audit/regulator, E-Registry, federation prep.",
        "profiles": ["operator", "extended/E-Registry", "federation/prep"],
        "book1_gate": "Registro civil adapter Phase 3+; SOC/PKI maduro.",
    },
    {
        "id": "P4",
        "odtis_phase": 4,
        "name": "Full mandate",
        "goal": "Federation production, Extended modules, Operator L3.",
        "profiles": ["federation", "extended", "operator/L3"],
        "book1_gate": "Acuerdos bilaterales activos; modulos Extended declarados.",
    },
    {
        "id": "P5",
        "odtis_phase": 2,
        "name": "Reliance Extensions (Capa B)",
        "goal": "Claimable Reliance pilot with RI-MAP, Annex B crosswalk, and L2 smoke.",
        "profiles": ["reliance-extensions"],
        "book1_gate": "Core Identity + Trust Network L2; reliance_extensions declared with R-Base.",
    },
]

# Epic definitions: phase -> list of epics
EPICS: dict[str, list[dict]] = {
    "P0": [
        {
            "id": "P0-E01",
            "title": "Conformance statement pipeline",
            "component": "odtis/conformance + operator docs",
            "repo": "odtis/core-spec",
            "status": "done",
            "odtis_ids": ["ODTIS-0008", "ODTIS-0532", "ODTIS-0534", "ODTIS-0010"],
            "work": [
                "Template YAML/MD dual-format statement from registry",
                "CI job: validate statement fields vs ODTIS-0008",
                "Publish human + machine statements per environment",
            ],
            "completed": [
                "scripts/generate-conformance-statement.py",
                "scripts/validate-conformance-statement.py",
                "implementation/statements/venid-sandbox/",
            ],
        },
        {
            "id": "P0-E02",
            "title": "Profile claim guardrails",
            "component": "conformance lab",
            "repo": "odtis/core-spec",
            "status": "done",
            "odtis_ids": ["ODTIS-0001", "ODTIS-0002", "ODTIS-0003", "ODTIS-0004", "ODTIS-0005", "ODTIS-0006", "ODTIS-0007", "ODTIS-0009"],
            "work": [
                "Automated check: declared profiles match depends_on chain",
                "Reject prohibited marketing claims in statement linter",
            ],
        },
        {
            "id": "P0-E03",
            "title": "Reference implementation map",
            "component": "implementation/RI-MAP.yaml",
            "repo": "odtis/core-spec",
            "status": "done",
            "odtis_ids": ["ODTIS-0536"],
            "work": [
                "Map every ven-* surface to ODTIS IDs and OpenAPI",
                "Link gaps/KNOWN-GAPS.md to backlog item status",
            ],
        },
        {
            "id": "P0-E04",
            "title": "L1 lab validators",
            "component": "conformance/sandbox",
            "repo": "odtis/core-spec",
            "status": "done",
            "odtis_ids": ["ODTIS-0010"],
            "work": [
                "run-sandbox-check.sh against ven-identity-core sandbox",
                "Registry link check + manifest 100% coverage gate in CI",
            ],
        },
    ],
    "P1": [
        {
            "id": "P1-E01",
            "title": "LoA model and claims",
            "component": "ven-identity-core / Keycloak extension",
            "repo": "ven-identity-core",
            "status": "partial",
            "odtis_ids": ["ODTIS-0101", "ODTIS-0102", "ODTIS-0103", "ODTIS-0105", "ODTIS-0107", "ODTIS-0108", "ODTIS-0306"],
            "work": [
                "LoA Low/Medium/High assignment rules in identity-core",
                "Expose loa claim in id_token and verification API",
                "RP min LoA per client_id configuration",
            ],
        },
        {
            "id": "P1-E02",
            "title": "OIDC IdP hardening",
            "component": "Keycloak + api-gateway",
            "repo": "ven-identity-core",
            "status": "partial",
            "odtis_ids": ["ODTIS-0301", "ODTIS-0302", "ODTIS-0303", "ODTIS-0304", "ODTIS-0305", "ODTIS-0307", "ODTIS-0308"],
            "work": [
                "Discovery + JWKS documented for sandbox",
                "Authorization Code + PKCE; JWT expiry/refresh",
                "redirect_uri validation; logout / end_session_endpoint (gap 0308)",
            ],
        },
        {
            "id": "P1-E03",
            "title": "Registration and proofing",
            "component": "identity-core + verification-engine",
            "repo": "ven-identity-core",
            "status": "partial",
            "odtis_ids": ["ODTIS-0309", "ODTIS-0310", "ODTIS-0311", "ODTIS-0312", "ODTIS-0313", "ODTIS-0314"],
            "work": [
                "Stable subject_id on first registration",
                "Document + biometric proofing pipelines with liveness",
                "Manual review queue for inconclusive cases",
            ],
        },
        {
            "id": "P1-E04",
            "title": "Verification API",
            "component": "verification-api + verification-engine",
            "repo": "ven-identity-core",
            "status": "partial",
            "odtis_ids": ["ODTIS-0315", "ODTIS-0316", "ODTIS-0317", "ODTIS-0318"],
            "work": [
                "Client credentials auth for RPs",
                "Response: status + LoA + consented attributes only",
                "Run L2 tests from conformance/tests/core-identity/",
            ],
        },
        {
            "id": "P1-E05",
            "title": "RP client lifecycle",
            "component": "admin-api + identity-core",
            "repo": "ven-identity-core",
            "status": "partial",
            "odtis_ids": ["ODTIS-0319", "ODTIS-0320", "ODTIS-0321", "ODTIS-0337", "ODTIS-0338", "ODTIS-0339"],
            "work": [
                "RP registration, rotation, suspension",
                "Admission criteria documented; secrets hashed",
            ],
        },
        {
            "id": "P1-E06",
            "title": "Consent and privacy",
            "component": "consent-service + citizen-api",
            "repo": "ven-identity-core",
            "status": "partial",
            "odtis_ids": ["ODTIS-0328", "ODTIS-0329", "ODTIS-0330", "ODTIS-0331", "ODTIS-0332", "ODTIS-0333", "ODTIS-0334", "ODTIS-0335", "ODTIS-0336"],
            "work": [
                "Explicit consent before first release; revocation effective next request",
                "Consent UI fields; privacy policy + DSAR process",
                "TLS + encryption at rest; no sale/profiling",
            ],
        },
        {
            "id": "P1-E07",
            "title": "Citizen portal",
            "component": "portal-ciudadano + citizen-api",
            "repo": "ven-identity-core",
            "status": "partial",
            "odtis_ids": ["ODTIS-0322", "ODTIS-0323", "ODTIS-0324"],
            "work": [
                "Status, connected RPs, consent revoke UX",
                "Operator-configured locales; responsive web",
            ],
        },
        {
            "id": "P1-E08",
            "title": "Identity transport and rate limits",
            "component": "api-gateway + services",
            "repo": "ven-identity-core",
            "status": "partial",
            "odtis_ids": ["ODTIS-0325", "ODTIS-0326", "ODTIS-0327", "ODTIS-0521", "ODTIS-0522", "ODTIS-0523"],
            "work": [
                "TLS 1.2+ on all public endpoints",
                "Rate limiting auth/verify; OWASP baseline",
                "MFA for sensitive actions; liveness in High LoA path",
            ],
        },
        {
            "id": "P1-E09",
            "title": "Identity audit events",
            "component": "identity-core events + audit export",
            "repo": "ven-identity-core",
            "status": "partial",
            "odtis_ids": ["ODTIS-0526", "ODTIS-0527", "ODTIS-0529"],
            "work": [
                "Emit registration, verification, LoA, consent events",
                "Standard envelope with trace_id + timestamp",
            ],
        },
        {
            "id": "P1-E10",
            "title": "Phase 1 conformance package",
            "component": "operator publication",
            "repo": "odtis/core-spec",
            "status": "done",
            "odtis_ids": ["ODTIS-0533"],
            "work": [
                "Production statement: Core Identity only, phase=1, no Extended",
                "L2 test report for declared Core Identity IDs",
            ],
        },
    ],
    "P2": [
        {
            "id": "P2-E01",
            "title": "Exchange gateway receiver/sender",
            "component": "ven-trust-exchange-gateway",
            "repo": "ven-trust-network",
            "status": "partial",
            "odtis_ids": ["ODTIS-0201", "ODTIS-0202", "ODTIS-0203", "ODTIS-0204", "ODTIS-0205", "ODTIS-0206", "ODTIS-0207"],
            "work": [
                "All partner traffic via local gateway",
                "Receiver validates partner against trust registry",
                "mTLS gateway-to-gateway live interop test (KNOWN-GAP 0204)",
            ],
        },
        {
            "id": "P2-E02",
            "title": "Service catalog",
            "component": "ven-trust-registry",
            "repo": "ven-trust-network",
            "status": "done",
            "odtis_ids": ["ODTIS-0208", "ODTIS-0222", "ODTIS-0212", "ODTIS-0213", "ODTIS-0214"],
            "work": [
                "Stable service_id + gateway_base_url per remote peer (FASE-4)",
                "GET /registry/services?serviceId= and caller_partner_id filters",
                "Configurable cache refresh; optional @VenPartnerService autodiscovery",
            ],
        },
        {
            "id": "P2-E03",
            "title": "Service access grants",
            "component": "trust-registry + portal-api",
            "repo": "ven-trust-network",
            "status": "done",
            "odtis_ids": ["ODTIS-0209", "ODTIS-0210", "ODTIS-0211", "ODTIS-0224", "ODTIS-0226"],
            "work": [
                "Grants bind caller, provider, service_id",
                "Fail closed on grant denial (no implicit zone trust)",
                "Auditable grant request/approve/revoke workflows",
            ],
        },
        {
            "id": "P2-E04",
            "title": "Multi-peer sender routing",
            "component": "exchange-gateway sender + sdk",
            "repo": "ven-trust-network",
            "status": "done",
            "odtis_ids": ["ODTIS-0223"],
            "work": [
                "Resolve route by X-Exchange-Service / service_id",
                "ExchangeGatewayClient SDK documented in FASE-4",
                "Remove single hard-coded remote-gateway-url for prod",
            ],
        },
        {
            "id": "P2-E05",
            "title": "Metadata-only exchange (D4)",
            "component": "trust-registry + audit",
            "repo": "ven-trust-network",
            "status": "done",
            "odtis_ids": ["ODTIS-0225"],
            "work": [
                "Catalog/audit stores: routing metadata only, not authoritative payloads",
                "Review persistence layer for payload centralization",
            ],
        },
        {
            "id": "P2-E06",
            "title": "Trust Network PKI",
            "component": "trust-authority + central-server",
            "repo": "ven-trust-network",
            "status": "partial",
            "odtis_ids": ["ODTIS-0215", "ODTIS-0216", "ODTIS-0217", "ODTIS-0218", "ODTIS-0106"],
            "work": [
                "Partner/service cert hierarchy; CRL/OCSP validation",
                "Document FAL controls and ceremony docs",
            ],
        },
        {
            "id": "P2-E07",
            "title": "Exchange audit and SLA",
            "component": "audit-service + operator policy",
            "repo": "ven-trust-network",
            "status": "partial",
            "odtis_ids": ["ODTIS-0219", "ODTIS-0220", "ODTIS-0221", "ODTIS-0528", "ODTIS-0517"],
            "work": [
                "Exchange events with correlation IDs",
                "Published gateway SLA; verify partner every request",
            ],
            "notes": [
                "ven-trust-network/scripts/exchange-audit-check.sh",
                "ven-trust-network/docs/operator/EXCHANGE-AUDIT-SLA.md",
            ],
        },
        {
            "id": "P2-E08",
            "title": "Fail-closed cross-layer",
            "component": "identity + trust integration",
            "repo": "ven-identity-core + ven-trust-network",
            "status": "partial",
            "odtis_ids": ["ODTIS-0535"],
            "work": [
                "Unified denial behavior: OIDC, Verification API, exchange grants",
                "Integration tests: zero attribute leakage on deny",
            ],
        },
        {
            "id": "P2-E09",
            "title": "Phase 2 conformance package",
            "component": "operator publication",
            "repo": "odtis/core-spec",
            "status": "done",
            "odtis_ids": ["ODTIS-0532"],
            "work": [
                "Statement: phase=2, Core Identity + Trust Network L2",
                "Full trust-network test suite green in staging",
            ],
        },
    ],
    "P3": [
        {
            "id": "P3-E01",
            "title": "Operator governance",
            "component": "portal-operador + policy docs",
            "repo": "ven-identity-core + docs",
            "status": "partial",
            "odtis_ids": ["ODTIS-0501", "ODTIS-0502", "ODTIS-0503", "ODTIS-0504", "ODTIS-0505", "ODTIS-0506"],
            "work": [
                "Publish scope, governance units, subject admin procedures",
                "Phase-appropriate PKI/SOC in conformance statement",
            ],
        },
        {
            "id": "P3-E02",
            "title": "Operator PKI stewardship",
            "component": "trust-authority + HSM runbooks",
            "repo": "ven-trust-network",
            "status": "partial",
            "odtis_ids": ["ODTIS-0507", "ODTIS-0508", "ODTIS-0509", "ODTIS-0510"],
            "work": [
                "CP/CPS publication; dual-control ceremonies",
                "CRL/OCSP; tested PKI DR on schedule",
            ],
        },
        {
            "id": "P3-E03",
            "title": "SLA, partners, metrics",
            "component": "operator policy + reports-api",
            "repo": "ven-identity-core",
            "status": "partial",
            "odtis_ids": ["ODTIS-0511", "ODTIS-0512", "ODTIS-0513"],
            "work": [
                "IdP/Verification availability targets",
                "Partner onboarding rules; ecosystem metrics export",
            ],
        },
        {
            "id": "P3-E04",
            "title": "Regulator, incidents, liability",
            "component": "regulator-api + legal docs",
            "repo": "ven-identity-core",
            "status": "partial",
            "odtis_ids": ["ODTIS-0514", "ODTIS-0515", "ODTIS-0516"],
            "work": [
                "Aggregated audit export without bulk PII",
                "Incident runbook; liability in ToS and RP contracts",
            ],
        },
        {
            "id": "P3-E05",
            "title": "Security and secrets platform",
            "component": "infra + all services",
            "repo": "ven-infra-core",
            "status": "partial",
            "odtis_ids": ["ODTIS-0518", "ODTIS-0519", "ODTIS-0520", "ODTIS-0525"],
            "work": [
                "No sensitive microservices on public internet",
                "Secrets manager for RP secrets and PKI keys",
                "Fraud monitoring dashboard + manual review SLA",
            ],
        },
        {
            "id": "P3-E06",
            "title": "Audit platform and regulator export",
            "component": "audit-service + reports-api",
            "repo": "ven-trust-network + ven-identity-core",
            "status": "partial",
            "odtis_ids": ["ODTIS-0530"],
            "work": [
                "Tamper-evident storage; PII-minimized regulator export",
                "Cross-link identity + exchange audit by correlation_id",
            ],
        },
        {
            "id": "P3-E07",
            "title": "E-Registry adapter",
            "component": "new eregistry-adapter service",
            "repo": "ven-identity-core (TBD)",
            "status": "partial",
            "odtis_ids": ["ODTIS-0104", "ODTIS-0344", "ODTIS-0349", "ODTIS-0350", "ODTIS-0351", "ODTIS-0352", "ODTIS-0353"],
            "work": [
                "National LoA only with E-Registry declared + adapter active",
                "Phase 3+ activation; bilateral agreement with registry authority",
                "Hashing only; no raw biometric persistence; audit every verification",
            ],
        },
        {
            "id": "P3-E08",
            "title": "Federation agreements (prep)",
            "component": "trust-registry federation module",
            "repo": "ven-trust-network",
            "status": "partial",
            "odtis_ids": ["ODTIS-0401", "ODTIS-0402", "ODTIS-0403", "ODTIS-0404", "ODTIS-0405", "ODTIS-0406"],
            "work": [
                "Bilateral agreement store: instance IDs, validity, pinned roots",
                "Reject federated routes without direct agreement",
                "Regulator export of agreement metadata (SHOULD)",
            ],
        },
        {
            "id": "P3-E09",
            "title": "Phase 3 conformance package",
            "component": "operator publication",
            "repo": "odtis/core-spec",
            "status": "partial",
            "odtis_ids": ["ODTIS-0532"],
            "work": [
                "Statement: phase=3, Operator L2-L3, E-Registry if active",
                "Third-party or internal audit dry-run",
            ],
        },
    ],
    "P4": [
        {
            "id": "P4-E01",
            "title": "Federation runtime",
            "component": "exchange-gateway federation router",
            "repo": "ven-trust-network",
            "status": "partial",
            "odtis_ids": ["ODTIS-0407", "ODTIS-0408"],
            "work": [
                "Suspend/expired agreements disable routing within cache bounds",
                "Federated audit: local + remote trust instance IDs",
            ],
        },
        {
            "id": "P4-E02",
            "title": "E-Wallet (OID4VP)",
            "component": "wallet issuer + wallet app",
            "repo": "ven-identity-core (TBD)",
            "status": "partial",
            "odtis_ids": ["ODTIS-0340", "ODTIS-0341", "ODTIS-0342", "ODTIS-0343", "ODTIS-0524"],
            "work": [
                "OID4VP presentations; issuer trust via trust registry",
                "Selective disclosure; shared LoA with Path A OIDC",
            ],
        },
        {
            "id": "P4-E03",
            "title": "E-Inclusion",
            "component": "inclusion onboarding flows",
            "repo": "ven-identity-core",
            "status": "partial",
            "odtis_ids": ["ODTIS-0354", "ODTIS-0355", "ODTIS-0356", "ODTIS-0357"],
            "work": [
                "Assisted consent; representative verification",
                "No LoA bypass; accessibility/offline where policy allows",
            ],
        },
        {
            "id": "P4-E04",
            "title": "E-Webhook",
            "component": "verification-api webhooks",
            "repo": "ven-identity-core",
            "status": "partial",
            "odtis_ids": ["ODTIS-0358", "ODTIS-0359", "ODTIS-0360", "ODTIS-0531"],
            "work": [
                "RP webhook registration API (OpenAPI pending)",
                "Signed payloads, retry/backoff, PII minimization",
            ],
        },
        {
            "id": "P4-E05",
            "title": "E-Signature",
            "component": "signature service",
            "repo": "ven-identity-core (TBD)",
            "status": "partial",
            "odtis_ids": ["ODTIS-0361", "ODTIS-0362", "ODTIS-0363"],
            "work": [
                "Sign bound to LoA; keys under operator PKI/TSP",
                "Auditable sign/verify events",
            ],
        },
        {
            "id": "P4-E06",
            "title": "E-KYB (preview)",
            "component": "kyb module",
            "repo": "ven-identity-core (TBD)",
            "status": "partial",
            "odtis_ids": ["ODTIS-0364", "ODTIS-0365"],
            "work": [
                "Legal entity verification separate from natural person",
                "Link representatives to verified subjects before B2B release",
            ],
        },
        {
            "id": "P4-E07",
            "title": "Operator L3 and Phase 4 statement",
            "component": "governance + external audit",
            "repo": "odtis/core-spec",
            "status": "partial",
            "odtis_ids": ["ODTIS-0532", "ODTIS-0006"],
            "work": [
                "L3 attestation; all claimed profiles + Extended modules listed",
                "Extended must not weaken base profile controls",
            ],
        },
    ],
    "P5": [
        {
            "id": "P5-E01",
            "title": "Reliance pilot overlay and statement",
            "component": "reliance-overlay + conformance package",
            "repo": "odtis/core-spec + ven-identity-core",
            "status": "partial",
            "odtis_ids": ["ODTIS-0701", "ODTIS-0707", "ODTIS-0708", "ODTIS-0532", "ODTIS-0536"],
            "work": [
                "RI-MAP reliance-overlay surface and component binding",
                "venid-reliance-pilot statement + l2-report via run-reliance-package.sh",
            ],
        },
        {
            "id": "P5-E02",
            "title": "Agent authority runtime",
            "component": "agent-mandate gateway",
            "repo": "ven-identity-core (TBD)",
            "status": "todo",
            "odtis_ids": ["ODTIS-0710", "ODTIS-0711", "ODTIS-0712", "ODTIS-0713"],
            "work": [
                "Signed mandate verification and revocation freshness window",
                "Human-anchor step-up for high-risk agent actions",
            ],
        },
        {
            "id": "P5-E03",
            "title": "Document capture PAD overlay",
            "component": "verification-engine capture adapter",
            "repo": "ven-identity-core",
            "status": "todo",
            "odtis_ids": ["ODTIS-0723", "ODTIS-0724", "ODTIS-0725"],
            "work": [
                "PAD/IAD provider disclosure on capture reliance decisions",
                "Fail-closed on unknown injection class",
            ],
        },
        {
            "id": "P5-E04",
            "title": "Remaining Reliance sub-modules",
            "component": "Capa B module overlays",
            "repo": "ven-identity-core",
            "status": "todo",
            "odtis_ids": ["ODTIS-0719", "ODTIS-0727", "ODTIS-0731", "ODTIS-0747"],
            "work": [
                "Tier 1 modules beyond pilot (Lifecycle, Liveness, Disclosure, VC-Gate, Public-eID, Portability)",
                "Tier 2/3 modules per Annex E phase gates",
            ],
        },
    ],
}


def epic_test_paths(epic: dict, reqs: dict) -> list[str]:
    paths: set[str] = set()
    for rid in epic.get("odtis_ids", []):
        ct = reqs.get(rid, {}).get("conformance_test")
        if ct:
            paths.add(ct)
    return sorted(paths)


def build_yaml_payload(version: str, reqs: dict) -> dict:
    phases_out = []
    totals = {"epics": 0, "odtis_ids": 0, "done": 0, "partial": 0, "todo": 0}
    for phase in PHASES:
        epics = EPICS[phase["id"]]
        epic_rows = []
        for epic in epics:
            totals["epics"] += 1
            totals[epic.get("status", "todo")] += 1
            ids = epic["odtis_ids"]
            totals["odtis_ids"] += len(ids)
            epic_rows.append(
                {
                    "id": epic["id"],
                    "title": epic["title"],
                    "status": epic["status"],
                    "component": epic["component"],
                    "repo": epic["repo"],
                    "odtis_ids": ids,
                    "conformance_tests": epic_test_paths(epic, reqs),
                    "work_items": epic["work"],
                }
            )
        phases_out.append({**phase, "epics": epic_rows})
    return {
        "spec_version": version,
        "generated": str(date.today()),
        "generator": "scripts/generate-phased-backlog.py",
        "summary": totals,
        "phases": phases_out,
        "execution_order": [
            "Complete P0 before public ODTIS claim",
            "P1 Core Identity L2 before P2 Trust Network production",
            "P2 before declaring Trust Network in production (ODTIS-0532)",
            "P3 Operator + E-Registry before National LoA in production",
            "P4 Federation + Extended only when agreements/modules active",
            "P5 Reliance Extensions pilot before Capa B production claims beyond declared modules",
        ],
        "references": {
            "ri_map": "implementation/RI-MAP.yaml",
            "known_gaps": "implementation/gaps/KNOWN-GAPS.md",
            "odtis_phases": "spec/10-deployment-profiles/SPEC.md",
            "platform_fase4": "implementation/RI-MAP.yaml",
            "book1_gates": "spec/10-deployment-profiles/SPEC.md",
        },
    }


def md_status_badge(status: str) -> str:
    return {"done": "DONE", "partial": "PARTIAL", "todo": "TODO"}.get(status, status.upper())


def build_markdown(payload: dict) -> str:
    s = payload["summary"]
    lines = [
        "# VenID phased implementation backlog",
        "",
        f"**ODTIS version:** `{payload['spec_version']}`  ",
        f"**Generated:** {payload['generated']}  ",
        "**Purpose:** Product backlog to implement VenID against ODTIS normative IDs and conformance tests, ordered by deployment phase.",
        "",
        "Machine-readable: [`phased-backlog.yaml`](phased-backlog.yaml) (regenerate with `python3 scripts/generate-phased-backlog.py`).",
        "",
        "---",
        "",
        "## Summary",
        "",
        "| Metric | Count |",
        "|--------|-------|",
        f"| Epics | {s['epics']} |",
        f"| ODTIS IDs referenced | {s['odtis_ids']} (of 149 total) |",
        f"| Status DONE | {s['done']} |",
        f"| Status PARTIAL | {s['partial']} |",
        f"| Status TODO | {s['todo']} |",
        "",
        "## Execution order",
        "",
    ]
    for i, rule in enumerate(payload["execution_order"], 1):
        lines.append(f"{i}. {rule}")
    lines.extend(
        [
            "",
            "## Phase map (ODTIS vs Book 1)",
            "",
            "| Backlog | ODTIS deployment phase | Profiles (production) | Book 1 gate |",
            "|---------|------------------------|------------------------|-------------|",
            "| **P0** | Pre-pilot (lab) | Reference Architecture | Mandato operador + RI map |",
            "| **P1** | Phase 1 | Core Identity | 5-10 RPs; no Extended in prod |",
            "| **P2** | Phase 2 | Core Identity + Trust Network | Nodos + grants + catalogo (D3/D4) |",
            "| **P3** | Phase 3 | + Operator + E-Registry | Registro adapter; PKI/SOC maduro |",
            "| **P4** | Phase 4 | + Federation + Extended | Acuerdos bilaterales activos |",
            "",
            "---",
            "",
        ]
    )

    for phase in payload["phases"]:
        lines.extend(
            [
                f"## {phase['id']} - {phase['name']} (ODTIS phase {phase['odtis_phase']})",
                "",
                f"**Goal:** {phase['goal']}  ",
                f"**Book 1 gate:** {phase['book1_gate']}  ",
                f"**Profiles:** {', '.join(phase['profiles'])}",
                "",
            ]
        )
        for epic in phase["epics"]:
            ids = ", ".join(f"`{x}`" for x in epic["odtis_ids"])
            tests = epic.get("conformance_tests", [])
            test_cell = f"{len(tests)} test(s)" if tests else "see registry"
            lines.extend(
                [
                    f"### {epic['id']} - {epic['title']} [{md_status_badge(epic['status'])}]",
                    "",
                    f"| Field | Value |",
                    f"|-------|-------|",
                    f"| Component | `{epic['component']}` |",
                    f"| Repo | `{epic['repo']}` |",
                    f"| ODTIS IDs | {ids} |",
                    f"| Conformance | {test_cell} |",
                    "",
                    "**Work items:**",
                    "",
                ]
            )
            for w in epic["work_items"]:
                lines.append(f"- [ ] {w}")
            if tests:
                lines.extend(["", "**Tests (sample):**", ""])
                for t in tests[:5]:
                    lines.append(f"- [`{t}`]({GITHUB_ODTIS}/{t})")
                if len(tests) > 5:
                    lines.append(f"- ... +{len(tests) - 5} more")
            lines.extend(["", "---", ""])

    lines.extend(
        [
            "## Definition of done (per epic)",
            "",
            "1. All listed **ODTIS IDs** satisfied in target environment.",
            "2. Linked **conformance tests** executed at L2 (staging) with pass evidence.",
            "3. **RI-MAP.yaml** updated with component surface mapping.",
            "4. **KNOWN-GAPS.md** entry closed or deferred with RFC.",
            "5. Conformance statement updated (`ODTIS-0532`, `ODTIS-0534`).",
            "",
            "## Related",
            "",
            "- [`RI-MAP.yaml`](RI-MAP.yaml)",
            "- [`gaps/KNOWN-GAPS.md`](gaps/KNOWN-GAPS.md)",
            "- [`../conformance/manifest.yaml`](../conformance/manifest.yaml)",
            "- [`../spec/10-deployment-profiles/SPEC.md`](../spec/10-deployment-profiles/SPEC.md)",
            f"- [Adoption guide]({GITHUB_ODTIS}/ADOPTION.md)",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    version = registry.get("spec_version", "0.9.0-draft")
    reqs = {r["id"]: r for r in load_requirements()}

    payload = build_yaml_payload(version, reqs)
    yaml_text = "# VenID phased backlog - generated\n"
    try:
        import yaml  # type: ignore

        yaml_text += yaml.dump(payload, sort_keys=False, allow_unicode=True)
    except ImportError:
        yaml_text += json.dumps(payload, indent=2)

    OUT_YAML.write_text(yaml_text, encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"Wrote {OUT_YAML.relative_to(ROOT)}")
    print(f"Wrote {OUT_MD.relative_to(ROOT)}")
    print(f"  {payload['summary']['epics']} epics, {payload['summary']['odtis_ids']} ID references")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
