# ODTIS conformance statement

**Status:** review draft - machine-readable source: `conformance-statement.yaml`

Normative fields per ODTIS section 1.9.1 (`ODTIS-0008`, `ODTIS-0534`).

| Field | Value |
|-------|-------|
| `odtis_version` | 0.9.0-draft |
| `profiles` | reference-architecture, core-identity, trust-network, reliance-extensions |
| `extended_modules` | (none) |
| `reliance_extensions` | R-Base, R-Agent-Authority, R-Crypto-Agility, R-Document-Capture |
| `level` | L2 |
| `operator` | FinnectOS VenID Reliance Pilot |
| `environment` | sandbox |
| `jurisdiction` | VE |
| `deployment_phase` | 2 |
| `requirements` | 100 ODTIS IDs (see YAML) |
| `tests.status` | partial |
| `tests.summary` | L2 conformance package (reference-architecture, core-identity, trust-network, reliance-extensions); 153 linked tests; min stub coverage 100.0%; see l2-report.md for automated results |
| `date` | 2026-06-23 |
| `contact` | conformance@odtis.org |

## Profiles declared

- `reference-architecture`
- `core-identity`
- `trust-network`
- `reliance-extensions`

## ODTIS-0708  -  Reliance Extensions scope

**Active Reliance Extension sub-modules:** R-Base, R-Agent-Authority, R-Crypto-Agility, R-Document-Capture.

Capa B reliance overlays MUST NOT weaken Core Identity, Trust Network, Federation, or Operator requirements (`ODTIS-0707`).


## ODTIS-0532  -  Phase 2 scope

This Phase 2 statement declares **Core Identity + Trust Network** (`core-identity`, `trust-network`). Federation and Extended sub-modules are not declared unless explicitly listed in `extended_modules`.


## Notes

- Regenerate: `python3 scripts/generate-conformance-statement.py`
- Validate: `python3 scripts/validate-conformance-statement.py`
