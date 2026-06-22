# ODTIS L2 test report - Phase 4 Core Identity + Trust Network

**Status:** PASS
**Passed:** 3/3
**Target:** (spec-only; set ODTIS_TARGET for live checks)
**ODTIS version:** 0.9.0-draft

## Profiles covered

- `reference-architecture`
- `core-identity`
- `trust-network`
- `federation`
- `operator`
- `extended`

## Automated results

- **PASS** `l2-target-skipped` (-): Pass --target for live OIDC/PKCE/JWKS checks
- **PASS** `l2-loa-schema` (ODTIS-0316): Annex A VerifyResponse includes verified, assurance_level (live API: verification-api-check.sh)
- **PASS** `l2-gateway-mtls-spec` (ODTIS-0204): Exchange gateway OpenAPI declares partnerMutualTLS (live mTLS handshake requires certs)

## Manual evidence (pending)

Remaining procedures are listed in `conformance-statement.yaml` under `tests.pending_test_ids`. Execute against staging sandbox and attach logs.

Regenerate: `./conformance/l2/run_l2.py`
