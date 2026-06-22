# ODTIS conformance statement

> **Target packaging - not a production deployment claim.** Operational scope: Phase 2 pilot - see `ven-identity-core/docs/operator/PUBLISHED-SERVICE-SCOPE.md` and [Claim Vs Runtime](https://github.com/odtis/core-impl/blob/main/ven-identity-core/docs/operator/CLAIM-VS-RUNTIME.md).

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
| `tests.status` | partial (target packaging) |
| `tests.summary` | L3-target conformance packaging (not production deployed); see l2-report.md |
| `date` | 2026-06-22 |
| `contact` | conformance@odtis.org |

## Profiles declared

- `reference-architecture`
- `core-identity`
- `trust-network`
- `federation`
- `operator`
- `extended`

## ODTIS-0532 - Phase 4 scope

This Phase 4 statement declares **Core Identity + Trust Network + Federation + Operator + Extended** as an **L3-target packaging** scope for roadmap and audit dry-runs.

**Declared Extended sub-modules:** E-Wallet, E-Registry, E-Inclusion, E-Webhook, E-Signature, E-KYB.

Extended modules are implemented as **sandbox partial** (`venid.*.active=false` by default). Federation and Extended staging overlays validate runtime in L2 sandbox but are **not production claims** until `PUBLISHED-SERVICE-SCOPE.md` is updated under change control.

**Published operational scope:** Phase 2 - `core-spec/implementation/statements/venid-phase2-trust/conformance-statement.yaml`

**Claim vs runtime matrix:** `core-spec/implementation/evidence/published-service-scope/claims-vs-runtime-2026.yaml`

**ODTIS-0006:** Extended capabilities MUST NOT weaken Core Identity, Trust Network, or Federation MUST requirements. See `conformance/run-extended-no-weakening-checks.sh`.

**Pending:** third-party Operator L3 attestation; production activation of declared Extended/Federation modules.


## Notes

- Regenerate: `python3 scripts/generate-conformance-statement.py`
- Validate: `python3 scripts/validate-conformance-statement.py`
