# ODTIS L2 sandbox conformance report

**Issue type:** sandbox / implementation experience 
**Review ID:** FB-005 (optional reference) 
**Spec version:** `0.9.0-draft` 
**Level:** L2 (live `--target` + repository checks)

Use this template when filing a GitHub issue labeled **ODTIS sandbox report**. Attach the JSON report from `./conformance/sandbox/run-sandbox-check.sh`.

**Before filing:** run L1 (`./conformance/run.sh`) and L2 against your live target. See [Sandbox alignment](README.md) and [Self-certification guide](../certification/self-cert-guide.md).

---

## Operator

| Field | Value |
|-------|-------|
| Organization | |
| Contact | |
| Sandbox URL (realm base) | `https://.../realms/...` |
| Environment | sandbox / staging |
| Deployment phase (1-4) | |
| Date (UTC) | |

---

## Profiles claimed

- [ ] reference-architecture
- [ ] core-identity
- [ ] trust-network
- [ ] federation
- [ ] operator
- [ ] extended (list sub-modules: )

**Extended sub-modules (if checked):** E-Wallet | E-Registry | E-Inclusion | E-Webhook | E-Signature | E-KYB

Conformance statement: link to `conformance-statement.yaml` or operator policy URL.

---

## Commands run

```bash
# from repository root
# L1
./conformance/run.sh

# L2
export ODTIS_TARGET=https://YOUR_REALM_URL
./conformance/sandbox/run-sandbox-check.sh
# Report: conformance/reports/l2-sandbox-<timestamp>.json
```

Optional profile smokes (record pass/fail below):

```bash
# Trust Network (if claimed)
../core-impl/ven-trust-network/scripts/exchange-gateway-check.sh
../core-impl/ven-trust-network/scripts/service-grants-check.sh

# Extended (if claimed)
./conformance/run-ewallet-checks.sh
```

Optional manual stubs - execute procedure in `conformance/tests/<profile>/` and note result:

```bash
# Example: consent scope (ODTIS-0331)
# conformance/tests/core-identity/test_verification_consent_scope.md
```

---

## L1 summary (repository)

Paste output from `./conformance/run.sh`:

```text
(paste L1 PASS/FAIL summary)
```

---

## L2 automated results

Paste human summary from `run_l2.py` or attach JSON.

| Check ID | Requirement | Result | Notes |
|----------|-------------|--------|-------|
| l2-oidc-discovery | ODTIS-0301 | OK / FAIL | |
| l2-discovery-fields | ODTIS-0301 | OK / FAIL | |
| l2-jwks | ODTIS-0301 | OK / FAIL | |
| l2-pkce-s256 | ODTIS-0302 | OK / FAIL | |
| l2-pkce-enforced | ODTIS-0302 | OK / FAIL | |
| l2-redirect-uri | ODTIS-0305 | OK / FAIL | |
| l2-logout-endpoint | ODTIS-0308 | INFO / OK / FAIL | informational if logout not enabled |
| l2-revocation | ODTIS-0303 | INFO / OK / FAIL | |
| l2-loa-schema | ODTIS-0316 | OK / FAIL | Annex A VerifyResponse |
| l2-gateway-mtls-spec | ODTIS-0204 | OK / FAIL | OpenAPI declares partnerMutualTLS |

**Overall L2 status:** PASS / FAIL / PARTIAL 
**Report file:** attach `conformance/reports/l2-sandbox-*.json`

---

## Manual procedure sample (optional)

| Test file | ODTIS ID | Result | Notes |
|-----------|----------|--------|-------|
| | | PASS / FAIL / N/A | |
| | | PASS / FAIL / N/A | |

Full procedure index: [Requirements registry](/registry/requirements.json) (`conformance_test` field).

---

## Gaps and observations

**Implementation gaps** (normative behaviour not met):

-

**Operator policy gaps** (documentation, not code):

-

**Suggested clarifications for stewards** (non-normative):

-

Known deferred items (VenID RI): [Deferred production track](/implementation/gaps/DEFERRED-TRACK/)

---

## Request to stewards

- [ ] Acknowledge report in [Review Log (YAML)](/governance/REVIEW-LOG.yaml)
- [ ] Open clarification issue if spec ambiguity found
- [ ] Open RFC if new MUST/SHOULD proposed

---

## Related

- [Sandbox alignment map](README.md)
- [Self-certification guide](../certification/self-cert-guide.md)
- Structural baseline: [FB-005 sandbox template](/governance/review/sandbox-001-l2-report-template/)
- Review cycle: [External review cycle 1](/governance/REVIEW-CYCLE-1/)
- Conformance hub: [Project hub](../README.md)
