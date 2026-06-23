"""Supplemental Annex C mappings (reference arch, extended gaps, reliance extensions)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from profile_registry import parse_reliance_module_requirements

# (standard_id, clause, reference, coverage)
Row = tuple[str, str, str, str]

PLATFORM: Row = ("STD-ODTIS-PLATFORM", "ODTIS platform rule", "P18 / Annex E", "platform")
GDPR_INF: Row = ("STD-GDPR", "Privacy governance (informative)", "GDPR Art. 5-22", "informative")


def _rows(*items: Row) -> list[Row]:
    return list(items)


REFERENCE_ARCH: dict[str, list[Row]] = {
    f"ODTIS-{i:04d}": _rows(PLATFORM) for i in range(1, 11)
}

OTHER_GAP: dict[str, list[Row]] = {
    "ODTIS-0104": _rows(
        ("STD-NIST-800-63-3", "IAL3 / registry proofing", "NIST SP 800-63A", "partial"),
        ("STD-EIDAS", "National eID level (informative)", "eIDAS high assurance", "informative"),
        PLATFORM,
    ),
    "ODTIS-0222": _rows(("STD-XROAD", "Grant creation audit", "X-Road access rights", "partial"), PLATFORM),
    "ODTIS-0223": _rows(("STD-XROAD", "Grant revocation", "X-Road access rights", "partial"), PLATFORM),
    "ODTIS-0224": _rows(("STD-XROAD", "Grant scope binding", "X-Road ACL", "partial"), PLATFORM),
    "ODTIS-0225": _rows(("STD-XROAD", "Grant expiry", "X-Road access rights", "partial"), PLATFORM),
    "ODTIS-0226": _rows(("STD-XROAD", "Grant audit correlation", "X-Road logs", "partial"), PLATFORM),
    "ODTIS-0340": _rows(("STD-OID4VCI", "Credential issuance", "OID4VCI", "partial"), PLATFORM),
    "ODTIS-0341": _rows(("STD-OID4VP", "Verifiable presentations", "OID4VP", "partial"), PLATFORM),
    "ODTIS-0342": _rows(("STD-SD-JWT", "Selective disclosure", "SD-JWT VC", "partial"), PLATFORM),
    "ODTIS-0343": _rows(("STD-EUDI-ARF", "Wallet roles (informative)", "EUDI ARF", "informative"), PLATFORM),
    "ODTIS-0349": _rows(PLATFORM, ("STD-EIDAS", "Registry authority boundary", "eIDAS TSP", "informative")),
    "ODTIS-0350": _rows(("STD-NIST-800-63-3", "National LoA after registry", "NIST SP 800-63A", "partial"), PLATFORM),
    "ODTIS-0351": _rows(PLATFORM, GDPR_INF),
    "ODTIS-0352": _rows(PLATFORM,),
    "ODTIS-0353": _rows(PLATFORM, ("STD-XROAD", "Verification audit", "Exchange audit", "partial")),
    "ODTIS-0354": _rows(GDPR_INF, PLATFORM),
    "ODTIS-0355": _rows(GDPR_INF, PLATFORM),
    "ODTIS-0356": _rows(("STD-NIST-800-63-3", "LoA proofing parity", "NIST SP 800-63A", "partial"), PLATFORM),
    "ODTIS-0357": _rows(PLATFORM,),
    "ODTIS-0358": _rows(("STD-OWASP", "Webhook registration", "OWASP API Security", "informative"), PLATFORM),
    "ODTIS-0359": _rows(PLATFORM,),
    "ODTIS-0360": _rows(GDPR_INF, PLATFORM),
    "ODTIS-0361": _rows(("STD-EIDAS", "Advanced signature (informative)", "eIDAS qualified signature", "informative"), PLATFORM),
    "ODTIS-0362": _rows(("STD-PKI-RFC5280", "Signature PKI keys", "RFC 5280", "partial"), PLATFORM),
    "ODTIS-0363": _rows(PLATFORM,),
    "ODTIS-0364": _rows(PLATFORM,),
    "ODTIS-0365": _rows(PLATFORM,),
    "ODTIS-0407": _rows(("STD-XROAD", "Federated verification routing", "X-Road federation", "partial"), PLATFORM),
    "ODTIS-0408": _rows(("STD-XROAD", "Federation audit export", "X-Road logs", "partial"), PLATFORM),
    "ODTIS-0534": _rows(PLATFORM,),
    "ODTIS-0535": _rows(PLATFORM, ("STD-NIST-800-207", "Fail-closed verification", "NIST SP 800-207", "partial")),
    "ODTIS-0536": _rows(PLATFORM,),
}

MODULE_STANDARDS: dict[str, list[Row]] = {
    "R-Base": _rows(
        PLATFORM,
        GDPR_INF,
        ("STD-OIDC-CORE", "Relying party identification", "OIDC client registration", "partial"),
        ("STD-NIST-800-63-3", "Assurance metadata", "NIST SP 800-63-3", "partial"),
    ),
    "R-Agent-Authority": _rows(
        ("STD-OAUTH2", "Delegated authority", "RFC 8693 token exchange pattern", "partial"),
        ("STD-IETF-AIP", "Agent identity (informative)", "IETF AIP did:aip", "informative"),
        PLATFORM,
    ),
    "R-Crypto-Agility": _rows(
        ("STD-NIST-PQC", "Post-quantum algorithms", "FIPS 203/204/205", "partial"),
        ("STD-PKI-RFC5280", "Certificate agility", "RFC 5280", "partial"),
        ("STD-EIDAS", "Crypto agility (informative)", "eIDAS 2.0", "informative"),
    ),
    "R-Lifecycle-Revocation": _rows(
        ("STD-WEBAUTHN", "Passkey revocation", "WebAuthn", "partial"),
        ("STD-NIST-800-63-3", "Credential lifecycle", "NIST SP 800-63B", "partial"),
        PLATFORM,
    ),
    "R-Document-Capture": _rows(
        ("STD-ISO-30107", "PAD / injection detection", "ISO/IEC 30107", "partial"),
        ("STD-FINCEN", "Document fraud alerts (informative)", "FinCEN FIN-2024", "informative"),
        PLATFORM,
    ),
    "R-Liveness": _rows(
        ("STD-ISO-30107", "Liveness detection", "ISO/IEC 30107", "partial"),
        GDPR_INF,
        PLATFORM,
    ),
    "R-Disclosure-Assurance": _rows(
        ("STD-SD-JWT", "Selective disclosure", "RFC 9901 SD-JWT", "partial"),
        ("STD-IETF-SCITT", "Audience-bound audit (informative)", "IETF SCITT AAC", "informative"),
        PLATFORM,
    ),
    "R-Assurance-Portability": _rows(
        ("STD-NIST-800-63-3", "Portable assurance", "NIST SP 800-63-3", "partial"),
        ("STD-ISO-30107", "PAD/IAD portability", "ISO/IEC 30107", "partial"),
        PLATFORM,
    ),
    "R-VC-Maturity-Gate": _rows(
        ("STD-W3C-VC", "VC maturity gate", "W3C VC Data Integrity", "partial"),
        PLATFORM,
    ),
    "R-Public-eID": _rows(
        ("STD-EIDAS", "Multi-eID acceptance", "eIDAS 2.0 LoA High", "informative"),
        ("STD-NIST-800-63-4", "Assurance mapping", "NIST SP 800-63-4", "partial"),
        ("STD-EUDI-ARF", "Public-sector wallet (informative)", "EUDI ARF", "informative"),
    ),
    "R-Fraud-Orchestration": _rows(
        ("STD-PSD3", "Fraud / APP reimbursement (informative)", "PSD3/PSR", "informative"),
        PLATFORM,
    ),
    "R-Stablecoin-CIP": _rows(
        ("STD-FINCEN", "CIP / BSA reliance", "FinCEN CIP", "informative"),
        ("STD-GENIUS", "Stablecoin CIP (informative)", "GENIUS Act", "informative"),
        ("STD-NIST-800-63-4", "Identity proofing", "NIST SP 800-63-4", "partial"),
    ),
    "R-Travel": _rows(
        ("STD-ICAO-DTC", "Digital travel credential", "ICAO DTC/PKD", "informative"),
        ("STD-IATA-ONEID", "One ID journey", "IATA One ID", "informative"),
        ("STD-OID4VP", "Cross-border presentation", "OID4VP", "partial"),
    ),
    "R-CRA-Resilience": _rows(
        ("STD-EU-CRA", "Software supply chain", "EU CRA 2024/2847", "informative"),
        PLATFORM,
    ),
    "R-DPI-Resilience": _rows(
        ("STD-ISO27001", "DPI blast-radius controls", "ISO 27001", "informative"),
        PLATFORM,
    ),
    "R-Sovereign-Chain-Interop": _rows(
        ("STD-W3C-VC", "Cross-chain credential interop", "W3C VC/VP", "partial"),
        ("STD-OID4VP", "Presentation interop", "OID4VP", "partial"),
        PLATFORM,
    ),
    "R-LE-Biometric": _rows(
        ("STD-ISO-30107", "Biometric reliance", "ISO/IEC 30107", "partial"),
        GDPR_INF,
        PLATFORM,
    ),
}


def reliance_mappings() -> dict[str, list[Row]]:
    mod_reqs = parse_reliance_module_requirements()
    out: dict[str, list[Row]] = {}
    for mod, req_ids in mod_reqs.items():
        rows = MODULE_STANDARDS.get(mod, _rows(PLATFORM))
        for rid in req_ids:
            out[rid] = list(rows)
    return out


def supplemental_mappings() -> dict[str, list[Row]]:
    merged: dict[str, list[Row]] = {}
    merged.update(REFERENCE_ARCH)
    merged.update(OTHER_GAP)
    merged.update(reliance_mappings())
    # Refresh 0532 to mention reliance
    merged["ODTIS-0532"] = _rows(
        PLATFORM,
        ("STD-ODTIS-PLATFORM", "Reliance Extensions declaration", "Annex E, section 10", "platform"),
    )
    return merged
