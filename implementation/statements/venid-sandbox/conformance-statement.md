# ODTIS conformance statement

**Status:** review draft - machine-readable source: `conformance-statement.yaml`

Normative fields per ODTIS section 1.9.1 (`ODTIS-0008`, `ODTIS-0534`).

| Field | Value |
|-------|-------|
| `odtis_version` | 0.9.0-draft |
| `profiles` | reference-architecture |
| `extended_modules` | (none) |
| `reliance_extensions` | (none) |
| `level` | L1 |
| `operator` | FinnectOS VenID Lab |
| `environment` | laboratory |
| `jurisdiction` | VE |
| `deployment_phase` | 1 |
| `requirements` | 10 ODTIS IDs (see YAML) |
| `tests.status` | partial |
| `tests.summary` | L1 conformance package (reference-architecture); 10 linked tests; min stub coverage 100.0%; see l2-report.md for automated results |
| `date` | 2026-06-23 |
| `contact` | conformance@odtis.org |

## Profiles declared

- `reference-architecture`

## ODTIS-0533  -  Phase 1 scope

This Phase 1 statement declares **Core Identity only** (`core-identity` profile). No Annex D optional sub-modules are declared in this statement.


## Notes

- Regenerate: `python3 scripts/generate-conformance-statement.py`
- Validate: `python3 scripts/validate-conformance-statement.py`
