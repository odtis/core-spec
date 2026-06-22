# ODTIS conformance statement

**Status:** review draft - machine-readable source: `conformance-statement.yaml`

Normative fields per ODTIS section 1.9.1 (`ODTIS-0008`, `ODTIS-0534`).

| Field | Value |
|-------|-------|
| `odtis_version` | 0.9.0-draft |
| `profiles` | reference-architecture, core-identity, trust-network, federation, operator, extended |
| `extended_modules` | E-Wallet, E-Registry, E-Inclusion, E-Webhook, E-Signature, E-KYB |
| `level` | L3 |
| `operator` | FinnectOS VenID Phase 4 |
| `environment` | staging |
| `jurisdiction` | VE |
| `deployment_phase` | 4 |
| `requirements` | 149 ODTIS IDs (see YAML) |
| `tests.status` | pass |
| `tests.summary` | L3 conformance package (reference-architecture, core-identity, trust-network, federation, operator, extended); 172 linked tests; min stub coverage 100.0%; see l2-report.md for automated results |
| `date` | 2026-06-12 |
| `contact` | conformance@finnectos.com |

## Profiles declared

- `reference-architecture`
- `core-identity`
- `trust-network`
- `federation`
- `operator`
- `extended`

## ODTIS-0532 - Phase 4 scope

This Phase 4 statement declares **Core Identity + Trust Network + Federation + Operator + Extended** at **L3** operator maturity target.

**Declared Extended sub-modules:** E-Wallet, E-Registry, E-Inclusion, E-Webhook, E-Signature, E-KYB.

Extended modules are implemented as **sandbox partial** (`venid.*.active=false` by default). Federation runtime, OID4VP wallet, inclusion, webhook, signature, and KYB preview services are listed for honest Phase 4 scope declaration (ODTIS-0532).

**ODTIS-0006:** Extended capabilities MUST NOT weaken Core Identity, Trust Network, or Federation MUST requirements. See `conformance/run-extended-no-weakening-checks.sh`.

**Pending:** third-party Operator L3 attestation; production activation of declared Extended modules.


## Notes

- Regenerate: `python3 scripts/generate-conformance-statement.py`
- Validate: `python3 scripts/validate-conformance-statement.py`
