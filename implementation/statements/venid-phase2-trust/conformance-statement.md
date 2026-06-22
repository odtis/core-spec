# ODTIS conformance statement

**Status:** review draft - machine-readable source: `conformance-statement.yaml`

Normative fields per ODTIS section 1.9.1 (`ODTIS-0008`, `ODTIS-0534`).

| Field | Value |
|-------|-------|
| `odtis_version` | 0.9.0-draft |
| `profiles` | reference-architecture, core-identity, trust-network |
| `extended_modules` | (none) |
| `level` | L2 |
| `operator` | FinnectOS VenID Phase 2 |
| `environment` | staging |
| `jurisdiction` | VE |
| `deployment_phase` | 2 |
| `requirements` | 82 ODTIS IDs (see YAML) |
| `tests.status` | partial |
| `tests.summary` | L2 conformance package (reference-architecture, core-identity, trust-network); 98 linked tests; min stub coverage 100.0%; see l2-report.md for automated results |
| `date` | 2026-06-15 |
| `contact` | conformance@odtis.org |

## Profiles declared

- `reference-architecture`
- `core-identity`
- `trust-network`

## ODTIS-0532 - Phase 2 scope

This Phase 2 statement declares **Core Identity + Trust Network** (`core-identity`, `trust-network`). Federation and Extended sub-modules are not declared unless explicitly listed in `extended_modules`.

## Published scope vs staging overlays (#15)

Production operator scope is documented in `ven-identity-core/docs/operator/PUBLISHED-SERVICE-SCOPE.md`. Optional staging overlays (Federation lab, Extended profile, E-Webhook lab, E-Registry sandbox) validate runtime in L2 sandbox but **do not** extend this statement's `profiles` or `extended_modules` until change control publishes an updated statement.

Overlay map: `implementation/evidence/published-service-scope/staging-overlays-2026.yaml`


## Notes

- Regenerate: `python3 scripts/generate-conformance-statement.py`
- Validate: `python3 scripts/validate-conformance-statement.py`
