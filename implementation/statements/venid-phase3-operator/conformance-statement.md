# ODTIS conformance statement

**Status:** review draft - machine-readable source: `conformance-statement.yaml`

Normative fields per ODTIS section 1.9.1 (`ODTIS-0008`, `ODTIS-0534`).

| Field | Value |
|-------|-------|
| `odtis_version` | 0.9.0-draft |
| `profiles` | reference-architecture, core-identity, trust-network, operator |
| `extended_modules` | (none) |
| `level` | L2 |
| `operator` | FinnectOS VenID Phase 3 |
| `environment` | staging |
| `jurisdiction` | VE |
| `deployment_phase` | 3 |
| `requirements` | 118 ODTIS IDs (see YAML) |
| `tests.status` | partial |
| `tests.summary` | L2 conformance package (reference-architecture, core-identity, trust-network, operator); 134 linked tests; min stub coverage 100.0%; see l2-report.md for automated results |
| `date` | 2026-06-15 |
| `contact` | conformance@odtis.org |

## Profiles declared

- `reference-architecture`
- `core-identity`
- `trust-network`
- `operator`

## ODTIS-0532 - Phase 3 scope

This Phase 3 statement declares **Core Identity + Trust Network + Operator** (`core-identity`, `trust-network`, `operator`) at **L2-L3** operator maturity.

**Active Extended sub-modules:** (none active in production).

**Staging overlays (not production claims):** Federation lab, E-Registry sandbox, Extended profile, E-Webhook lab - see `implementation/evidence/published-service-scope/staging-overlays-2026.yaml` and `PUBLISHED-SERVICE-SCOPE.md`.

**Prep (not activated in production):** E-Registry adapter (`eregistry-adapter`, `venid.eregistry.active=false` by default); federation runtime via optional compose overlay (`docker-compose.federation.yml`).

National LoA, federated routing, and Extended modules MUST NOT be claimed in production until `PUBLISHED-SERVICE-SCOPE.md` and this statement are updated under change control.


## Notes

- Regenerate: `python3 scripts/generate-conformance-statement.py`
- Validate: `python3 scripts/validate-conformance-statement.py`
