# ODTIS conformance statement

**Status:** review draft - machine-readable source: `conformance-statement.yaml`

Normative fields per ODTIS section 1.9.1 (`ODTIS-0008`, `ODTIS-0534`).

| Field | Value |
|-------|-------|
| `odtis_version` | 0.9.0-draft |
| `profiles` | reference-architecture |
| `extended_modules` | (none) |
| `level` | L1 |
| `operator` | FinnectOS VenID Lab |
| `environment` | laboratory |
| `jurisdiction` | VE |
| `deployment_phase` | 1 |
| `requirements` | 10 ODTIS IDs (see YAML) |
| `tests.status` | partial |
| `tests.summary` | L1 structural validators; 10 profile test stubs linked; min req stub coverage 100.0% |
| `date` | 2026-06-15 |
| `contact` | conformance@finnectos.com |

## Profiles declared

- `reference-architecture`

## Notes

- Regenerate: `python3 scripts/generate-conformance-statement.py`
- Validate: `python3 scripts/validate-conformance-statement.py`
