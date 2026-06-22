# ODTIS conformance statement

**Status:** review draft - machine-readable source: `conformance-statement.yaml`

Normative fields per ODTIS section 1.9.1 (`ODTIS-0008`, `ODTIS-0534`).

| Field | Value |
|-------|-------|
| `odtis_version` | 0.9.0-draft |
| `profiles` | reference-architecture, core-identity |
| `extended_modules` | (none) |
| `level` | L2 |
| `operator` | FinnectOS VenID Phase 1 |
| `environment` | sandbox |
| `jurisdiction` | VE |
| `deployment_phase` | 1 |
| `requirements` | 55 ODTIS IDs (see YAML) |
| `tests.status` | partial |
| `tests.summary` | L2 conformance package (reference-architecture, core-identity); 68 linked tests; min stub coverage 100.0%; see l2-report.md for automated results |
| `date` | 2026-06-15 |
| `contact` | conformance@digitaltrustinfrastructure.org |

## Profiles declared

- `reference-architecture`
- `core-identity`

## ODTIS-0533 - Phase 1 scope

This Phase 1 statement declares **Core Identity only** (`core-identity` profile). No Annex D optional sub-modules are declared in this statement.


## Notes

- Regenerate: `python3 scripts/generate-conformance-statement.py`
- Validate: `python3 scripts/validate-conformance-statement.py`
