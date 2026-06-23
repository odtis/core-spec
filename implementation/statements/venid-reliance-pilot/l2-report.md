# ODTIS L2 test report - Phase 2 Reliance Extensions pilot

**Status:** PASS
**Passed:** 6/6
**Target:** (spec-only; set ODTIS_TARGET for live checks)
**ODTIS version:** 0.9.0-draft

## Profiles covered

- `reference-architecture`
- `core-identity`
- `trust-network`
- `reliance-extensions`

## Automated results

- **PASS** `l2-target-skipped` (-): Pass --target for live OIDC/PKCE/JWKS checks
- **PASS** `l2-loa-schema` (ODTIS-0316): Annex A VerifyResponse includes verified, assurance_level (live API: verification-api-check.sh)
- **PASS** `l2-gateway-mtls-spec` (ODTIS-0204): Exchange gateway OpenAPI declares partnerMutualTLS (live mTLS handshake requires certs)
- **PASS** `l2-reliance-schema` (ODTIS-0701): registry/reliance-profiles.yaml defines R-Base field catalog and declaration field
- **PASS** `l2-reliance-pilot` (ODTIS-0708): Pilot statement lists reliance-extensions profile and declared sub-modules
- **PASS** `l2-reliance-ri-map` (ODTIS-0536): RI-MAP maps reliance-overlay surface with component binding

## Manual evidence (pending)

Remaining procedures are listed in `conformance-statement.yaml` under `tests.pending_test_ids`. Execute against staging sandbox and attach logs.

Regenerate: `./conformance/run-reliance-package.sh`
