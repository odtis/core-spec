# Sandbox L2 report - structural baseline (no live target)

**Issue type:** sandbox / implementation experience 
**Review ID:** FB-005 (**accepted**) 
**Level:** L2 (repository-only)

**Live target template:** [L2 report template](../../conformance/sandbox/L2-REPORT-TEMPLATE.md) | **Project:** [Project hub](/project/)

---

## Operator

VenID spec stewards (internal baseline)

## Target

*(none - structural L2 only)*

## Profiles claimed

- [x] core-identity (Annex A + discovery checks when `--target` set)

## Results

```text
ODTIS conformance L2: PASS (8/8 checks)
[OK] l2-target-skipped: Pass --target for live OIDC/PKCE/JWKS checks
[OK] l2-loa-schema: Annex A VerifyResponse includes assurance_level
[OK] l2-gateway-mtls-spec: Exchange gateway OpenAPI declares partnerMutualTLS
```

Report JSON schema: `conformance/l2/run_l2.py --output conformance/reports/l2-report.json`

## Gaps found

- Live sandbox `--target` not yet exercised in CI (requires operator URL + DNS).
- `end_session_endpoint` check is informational until logout enabled on sandbox IdP.
- Manual profile stubs (159 procedures; 81 with smoke evidence in this repo) pending full operator execution.

## Request

Sandbox operators: run `./conformance/sandbox/run-sandbox-check.sh https://YOUR_REALM_URL` and file a GitHub issue using [L2 report template](../../conformance/sandbox/L2-REPORT-TEMPLATE.md) with attached JSON.
