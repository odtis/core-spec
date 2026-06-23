#!/usr/bin/env python3
"""Generate ODTIS Annex C mapping.yaml from registry + P18 alignment tables."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry/requirements.json"
OUT = ROOT / "annexes/C-standards-mapping/mapping.yaml"

sys.path.insert(0, str(ROOT / "scripts"))
from standards_mapping_supplemental import supplemental_mappings  # noqa: E402

# standard_id, clause, reference, coverage - per requirement
MAPPING: dict[str, list[tuple[str, str, str, str]]] = {
"ODTIS-0101": [
("STD-NIST-800-63-3", "IAL proofing levels", "NIST SP 800-63-3 6", "partial"),
("STD-EIDAS", "Assurance levels (informative)", "eIDAS LoA concepts", "informative"),
],
"ODTIS-0102": [
("STD-OIDC-CORE", "Claims in ID Token / UserInfo", "OIDC Core 5", "partial"),
("STD-NIST-800-63-3", "IAL disclosure to RPs", "NIST SP 800-63-3", "partial"),
],
"ODTIS-0103": [
("STD-NIST-800-63-3", "IAL2/IAL3 biometric proofing", "NIST SP 800-63A", "partial"),
],
"ODTIS-0344": [
("STD-NIST-800-63-3", "IAL3 registry-verified identity", "NIST SP 800-63A", "partial"),
("STD-EIDAS", "National eID level (informative)", "eIDAS high assurance", "informative"),
("STD-ODTIS-PLATFORM", "E-Registry Extended sub-module", "P11, Annex D", "platform"),
],
"ODTIS-0105": [
("STD-NIST-800-63-3", "IAL/AAL mapping documentation", "NIST SP 800-63-3", "full"),
],
"ODTIS-0106": [
("STD-NIST-800-63-3", "FAL federation assurance", "NIST SP 800-63C", "partial"),
("STD-XROAD", "Gateway federation controls", "X-Road security server", "partial"),
],
"ODTIS-0107": [
("STD-NIST-800-63-3", "RP minimum assurance policy", "NIST SP 800-63-3", "partial"),
("STD-OIDC-CORE", "Client-specific authorization policy", "OIDC Core", "partial"),
],
"ODTIS-0108": [
("STD-OIDC-CORE", "Claims on denied release", "OIDC / verification API", "partial"),
],
"ODTIS-0301": [
("STD-OIDC-DISC", "Provider Metadata and JWKS", "OIDC Discovery 3", "full"),
],
"ODTIS-0302": [
("STD-OAUTH2", "Authorization Code grant", "RFC 6749 4.1", "full"),
("STD-PKCE", "Public client code exchange", "RFC 7636", "full"),
],
"ODTIS-0303": [
("STD-OAUTH2", "Access and refresh tokens", "RFC 6749 6", "partial"),
("STD-JWT", "JWT access_token and id_token", "RFC 7519", "full"),
],
"ODTIS-0304": [
("STD-NIST-800-63-3", "AAL2/AAL3 MFA", "NIST SP 800-63B", "partial"),
("STD-WEBAUTHN", "Phishing-resistant authenticators", "WebAuthn", "partial"),
],
"ODTIS-0305": [
("STD-OAUTH2", "Redirect URI validation", "RFC 6749 3.1.2", "full"),
("STD-OIDC-CORE", "Client registration constraints", "OIDC Core 15", "partial"),
],
"ODTIS-0306": [
("STD-OIDC-CORE", "Custom claims from authoritative source", "OIDC Core 5", "partial"),
("STD-ODTIS-PLATFORM", "identity-core as claims source", "P13, P01", "platform"),
],
"ODTIS-0307": [
("STD-OIDC-CORE", "Scope and consent-gated claims", "OIDC Core 5", "partial"),
("STD-GDPR", "Purpose limitation (informative)", "GDPR Art. 5", "informative"),
],
"ODTIS-0308": [
("STD-OIDC-CORE", "RP-Initiated Logout", "OIDC RP-Initiated Logout", "partial"),
("STD-OIDC-CORE", "Session termination", "OIDC Core", "partial"),
],
"ODTIS-0309": [
("STD-NIST-800-63-3", "Account recovery with verification", "NIST SP 800-63B", "partial"),
("STD-ODTIS-PLATFORM", "Auditable recovery events", "RF-14", "platform"),
],
"ODTIS-0310": [
("STD-NIST-800-63-3", "Persistent subject identifier", "NIST SP 800-63A", "partial"),
],
"ODTIS-0311": [
("STD-NIST-800-63-3", "IAL2 document proofing", "NIST SP 800-63A", "partial"),
],
"ODTIS-0312": [
("STD-NIST-800-63-3", "IAL2/IAL3 biometric proofing", "NIST SP 800-63A", "partial"),
],
"ODTIS-0313": [
("STD-NIST-800-63-3", "Manual adjudication of proofing", "NIST SP 800-63A", "partial"),
("STD-ODTIS-PLATFORM", "Operator review queue", "P01, P07", "platform"),
],
"ODTIS-0314": [
("STD-GDPR", "Data minimization (informative)", "GDPR Art. 5(1)(c)", "informative"),
("STD-NIST-800-63-3", "Biometric data handling", "NIST SP 800-63A", "partial"),
],
"ODTIS-0315": [
("STD-OAUTH2", "Client credentials protected resource", "RFC 6749 4.4", "partial"),
("STD-ODTIS-PLATFORM", "Verification API surface", "P14 Annex A", "platform"),
],
"ODTIS-0316": [
("STD-OIDC-CORE", "Verification status claims", "OIDC / custom claims", "partial"),
],
"ODTIS-0317": [
("STD-OIDC-CORE", "Scope-limited attribute release", "OIDC Core 5", "partial"),
("STD-GDPR", "Purpose limitation", "GDPR Art. 5", "informative"),
],
"ODTIS-0318": [
("STD-ODTIS-PLATFORM", "Performance design target", "RNF-11", "platform"),
],
"ODTIS-0319": [
("STD-OIDC-CORE", "Dynamic client registration pattern", "OIDC Core 15", "partial"),
("STD-OAUTH2", "Client metadata (redirect, scope)", "RFC 6749", "partial"),
],
"ODTIS-0320": [
("STD-OAUTH2", "Client credential lifecycle", "RFC 6749", "partial"),
],
"ODTIS-0321": [
("STD-OAUTH2", "Client secret confidentiality", "RFC 6749 2.3.1", "partial"),
("STD-OWASP", "Secret storage baseline", "OWASP ASVS", "informative"),
],
"ODTIS-0322": [
("STD-GDPR", "Transparency (informative)", "GDPR Art. 12-15", "informative"),
("STD-ODTIS-PLATFORM", "Citizen portal", "P01 3.6", "platform"),
],
"ODTIS-0323": [
("STD-GDPR", "Right to withdraw consent (informative)", "GDPR Art. 7", "informative"),
],
"ODTIS-0324": [
("STD-ODTIS-PLATFORM", "Accessibility and locale", "RNF-22", "platform"),
],
"ODTIS-0325": [
("STD-TLS", "TLS 1.2+ on public endpoints", "RFC 8446", "full"),
],
"ODTIS-0326": [
("STD-OWASP", "Rate limiting / abuse prevention", "OWASP API Security", "informative"),
],
"ODTIS-0327": [
("STD-ODTIS-PLATFORM", "Security audit events", "DS-07", "platform"),
],
"ODTIS-0201": [
("STD-XROAD", "Security server as sole entry", "X-Road architecture", "partial"),
],
"ODTIS-0202": [
("STD-XROAD", "Client and server proxy roles", "X-Road SS", "partial"),
],
"ODTIS-0203": [
("STD-XROAD", "Peer security server addressing", "X-Road federation", "partial"),
],
"ODTIS-0204": [
("STD-TLS", "Mutual TLS authentication", "RFC 8446", "full"),
("STD-XROAD", "Partner certificate authentication", "X-Road 4", "partial"),
],
"ODTIS-0205": [
("STD-XROAD", "Member identification at gateway", "X-Road SS receiver", "partial"),
("STD-NIST-800-207", "Never trust, always verify", "NIST SP 800-207", "informative"),
],
"ODTIS-0206": [
("STD-XROAD", "Message replay protection", "X-Road message headers", "partial"),
],
"ODTIS-0207": [
("STD-XROAD", "Message-level signatures", "X-Road / XML-DSig pattern", "partial"),
("STD-PKI-RFC5280", "Signature verification", "RFC 5280", "partial"),
],
"ODTIS-0208": [
("STD-XROAD", "Service description / WSDL catalog", "X-Road service registry", "partial"),
("STD-ODTIS-PLATFORM", "VenID service catalog", "P04, P05", "platform"),
],
"ODTIS-0209": [
("STD-XROAD", "Access rights / ACL grants", "X-Road access rights", "partial"),
],
"ODTIS-0210": [
("STD-XROAD", "Grant precedence over static permissions", "X-Road governance", "partial"),
],
"ODTIS-0211": [
("STD-ODTIS-PLATFORM", "Grant lifecycle audit", "P10, DS-07", "platform"),
],
"ODTIS-0212": [
("STD-XROAD", "Global configuration / routing", "X-Road conf", "partial"),
],
"ODTIS-0213": [
("STD-XROAD", "Configuration cache refresh", "X-Road SS cache", "partial"),
],
"ODTIS-0214": [
("STD-ODTIS-PLATFORM", "Service autodiscovery", "P05", "platform"),
],
"ODTIS-0215": [
("STD-PKI-RFC5280", "CA hierarchy for partner certs", "RFC 5280", "partial"),
("STD-EIDAS", "Trust service PKI (informative)", "eIDAS TSP", "informative"),
],
"ODTIS-0216": [
("STD-PKI-RFC5280", "CRL / OCSP validation", "RFC 5280", "partial"),
],
"ODTIS-0217": [
("STD-PKI-RFC5280", "Trusted timestamping", "RFC 3161 pattern", "partial"),
("STD-EIDAS", "Qualified timestamps (informative)", "eIDAS TSP", "informative"),
],
"ODTIS-0218": [
("STD-ODTIS-PLATFORM", "PKI ceremony documentation", "P08, P10", "platform"),
],
"ODTIS-0219": [
("STD-XROAD", "Exchange audit logs", "X-Road log architecture", "partial"),
("STD-ODTIS-PLATFORM", "Regulator export correlation", "P10", "platform"),
],
"ODTIS-0220": [
("STD-ODTIS-PLATFORM", "Gateway SLA targets", "RNF-07, P10", "platform"),
],
"ODTIS-0221": [
("STD-NIST-800-207", "Zero trust alignment", "NIST SP 800-207", "informative"),
],
"ODTIS-0328": [
("STD-OIDC-CORE", "Consent before attribute release", "OIDC Core 15", "partial"),
("STD-GDPR", "Consent (informative)", "GDPR Art. 6-7", "informative"),
],
"ODTIS-0329": [
("STD-GDPR", "Consent records (informative)", "GDPR Art. 7", "informative"),
("STD-ODTIS-PLATFORM", "consent-service records", "P01 3.6", "platform"),
],
"ODTIS-0330": [
("STD-GDPR", "Withdraw consent (informative)", "GDPR Art. 7(3)", "informative"),
],
"ODTIS-0331": [
("STD-OIDC-CORE", "Scope enforcement", "OIDC Core 5", "partial"),
],
"ODTIS-0332": [
("STD-GDPR", "Transparent information (informative)", "GDPR Art. 12-13", "informative"),
],
"ODTIS-0333": [
("STD-GDPR", "Privacy notice (informative)", "GDPR Art. 13-14", "informative"),
],
"ODTIS-0334": [
("STD-GDPR", "Data subject access (informative)", "GDPR Art. 15", "informative"),
],
"ODTIS-0335": [
("STD-TLS", "Encryption in transit", "RFC 8446", "full"),
("STD-OWASP", "Encryption at rest baseline", "OWASP ASVS", "informative"),
],
"ODTIS-0336": [
("STD-GDPR", "Purpose limitation (informative)", "GDPR Art. 5(1)(b)", "informative"),
],
"ODTIS-0337": [
("STD-ODTIS-PLATFORM", "RP onboarding governance", "P07 6.3, P10", "platform"),
],
"ODTIS-0338": [
("STD-GDPR", "Processor/controller duties (informative)", "GDPR Art. 28", "informative"),
("STD-ODTIS-PLATFORM", "RP contractual obligations", "Book 1", "platform"),
],
"ODTIS-0339": [
("STD-OAUTH2", "Client deactivation", "RFC 6749 client lifecycle", "partial"),
],
"ODTIS-0401": [
("STD-XROAD", "Federation without transitivity", "X-Road federation model", "partial"),
],
"ODTIS-0402": [
("STD-XROAD", "Federation member certificates", "X-Road federation", "partial"),
],
"ODTIS-0403": [
("STD-ODTIS-PLATFORM", "Phased federation activation", "P09, P10", "platform"),
],
"ODTIS-0404": [
("STD-XROAD", "Federation agreement fields", "X-Road federation", "partial"),
("STD-ODTIS-PLATFORM", "Pinned trust material", "P09", "platform"),
],
"ODTIS-0405": [
("STD-XROAD", "Non-transitive federation routing", "X-Road federation", "partial"),
],
"ODTIS-0406": [
("STD-ODTIS-PLATFORM", "Regulator federation export", "Annex A S8", "platform"),
],
"ODTIS-0501": [
("STD-ODTIS-PLATFORM", "Conformance scope declaration", "P10", "platform"),
],
"ODTIS-0502": [
("STD-ISO27001", "ISMS governance (target)", "ISO 27001", "informative"),
("STD-ODTIS-PLATFORM", "DTI operator model", "P10 4", "platform"),
],
"ODTIS-0503": [
("STD-ODTIS-PLATFORM", "Delegated operator / PPP", "P10 5", "platform"),
],
"ODTIS-0504": [
("STD-ODTIS-PLATFORM", "Subject administration API", "RF-27, Annex A S5", "platform"),
],
"ODTIS-0505": [
("STD-ISO27001", "Maturity roadmap (informative)", "ISO 27001", "informative"),
("STD-ODTIS-PLATFORM", "Phase-appropriate conformance", "P10 6", "platform"),
],
"ODTIS-0506": [
("STD-ODTIS-PLATFORM", "Honest conformance claims", "P10", "platform"),
],
"ODTIS-0507": [
("STD-PKI-RFC5280", "Certificate Policy / CPS", "RFC 3647 pattern", "partial"),
],
"ODTIS-0508": [
("STD-PKI-RFC5280", "Key ceremony dual control", "WebTrust / RFC 3647", "partial"),
],
"ODTIS-0509": [
("STD-PKI-RFC5280", "CRL / OCSP publication", "RFC 5280", "partial"),
],
"ODTIS-0510": [
("STD-ISO27001", "BC/DR testing (informative)", "ISO 22301 related", "informative"),
("STD-ODTIS-PLATFORM", "PKI DR schedule", "P08", "platform"),
],
"ODTIS-0511": [
("STD-ODTIS-PLATFORM", "IdP / verification SLA", "RNF-07, P10", "platform"),
],
"ODTIS-0512": [
("STD-ODTIS-PLATFORM", "Partner onboarding transparency", "P10 9", "platform"),
],
"ODTIS-0513": [
("STD-ODTIS-PLATFORM", "Ecosystem metrics", "RNF-25, P10", "platform"),
],
"ODTIS-0514": [
("STD-GDPR", "Accountability / oversight (informative)", "GDPR Art. 30", "informative"),
("STD-ODTIS-PLATFORM", "Regulator API export", "P10, Annex A S8", "platform"),
],
"ODTIS-0515": [
("STD-ISO27001", "Incident management (informative)", "ISO 27001 A.16", "informative"),
("STD-ODTIS-PLATFORM", "Operator IR procedures", "P07, RNF-06", "platform"),
],
"ODTIS-0516": [
("STD-ODTIS-PLATFORM", "Liability documentation", "Book 1 ch. 13", "platform"),
],
"ODTIS-0517": [
("STD-NIST-800-207", "Per-request verification", "NIST SP 800-207", "partial"),
("STD-XROAD", "Gateway partner validation", "X-Road SS", "partial"),
],
"ODTIS-0518": [
("STD-NIST-800-207", "Network segmentation", "NIST SP 800-207", "partial"),
],
"ODTIS-0519": [
("STD-OWASP", "Secrets management", "OWASP ASVS V14", "informative"),
("STD-ODTIS-PLATFORM", "Vault / HSM pattern", "DS-06, P08", "platform"),
],
"ODTIS-0520": [
("STD-NIST-800-207", "Zero trust maturity roadmap", "NIST SP 800-207 6", "informative"),
],
"ODTIS-0521": [
("STD-OWASP", "Web application baseline", "OWASP Top 10", "informative"),
],
"ODTIS-0522": [
("STD-NIST-800-63-3", "MFA for sensitive actions", "NIST SP 800-63B", "partial"),
],
"ODTIS-0523": [
("STD-NIST-800-63-3", "Liveness for biometric proofing", "NIST SP 800-63A", "partial"),
],
"ODTIS-0524": [
("STD-OID4VP", "Holder binding via VP signature", "OID4VP", "partial"),
],
"ODTIS-0525": [
("STD-ODTIS-PLATFORM", "Fraud monitoring metrics", "P07 8.5", "platform"),
],
"ODTIS-0526": [
("STD-ODTIS-PLATFORM", "Identity lifecycle audit events", "DS-07", "platform"),
],
"ODTIS-0527": [
("STD-GDPR", "Consent audit trail (informative)", "GDPR Art. 7", "informative"),
("STD-ODTIS-PLATFORM", "consent.granted / revoked events", "DS-07", "platform"),
],
"ODTIS-0528": [
("STD-XROAD", "Exchange audit events", "X-Road logs", "partial"),
],
"ODTIS-0529": [
("STD-ODTIS-PLATFORM", "Audit envelope (trace_id, timestamp)", "DS-07", "platform"),
],
"ODTIS-0530": [
("STD-GDPR", "Minimization in logs (informative)", "GDPR Art. 5", "informative"),
("STD-ODTIS-PLATFORM", "Regulator export without excess PII", "P10", "platform"),
],
"ODTIS-0531": [
("STD-OWASP", "Webhook payload integrity", "OWASP API Security", "informative"),
("STD-ODTIS-PLATFORM", "E-Webhook HMAC signing", "DS-07", "platform"),
],
"ODTIS-0532": [
("STD-ODTIS-PLATFORM", "Conformance statement profiles", "P18 3.3", "platform"),
],
"ODTIS-0533": [
("STD-ODTIS-PLATFORM", "Phase honesty for Extended claims", "P10, P17", "platform"),
],
}


def render_entry(req_id: str, rows: list[tuple[str, str, str, str]]) -> str:
    lines = [f"  {req_id}:"]
    for std_id, clause, reference, coverage in rows:
        lines.extend(
            [
                "    - standard_id: " + std_id,
                '      clause: "' + clause.replace('"', '\\"') + '"',
                '      reference: "' + reference.replace('"', '\\"') + '"',
                "      coverage: " + coverage,
            ]
        )
    return "\n".join(lines)


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    req_ids = [r["id"] for r in registry["requirements"]]
    full_mapping = dict(MAPPING)
    full_mapping.update(supplemental_mappings())
    missing = [rid for rid in req_ids if rid not in full_mapping]
    extra = [rid for rid in full_mapping if rid not in req_ids]
    if missing:
        raise SystemExit(f"missing mappings for: {', '.join(missing)}")
    if extra:
        raise SystemExit(f"unknown mapping keys: {', '.join(extra)}")

    version = registry.get("spec_version", "0.9.0-draft")
    header = f"""# ODTIS Annex C - Requirement to standard mapping
# Source: P18 4-9; generated by scripts/generate-standards-mapping.py
# Informative annex - does not assert external certification

spec_version: "{version}"
source: "P18, normativa-estandares-referencia.md"
standards_catalog: standards.yaml
loa_matrix: loa-matrix.yaml

requirement_coverage:
"""
    body = "\n".join(render_entry(rid, full_mapping[rid]) for rid in req_ids)
    OUT.write_text(header + body + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({len(req_ids)} requirements)")


if __name__ == "__main__":
    main()
