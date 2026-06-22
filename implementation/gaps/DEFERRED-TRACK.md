# Deferred production track (reference stack)

**Updated:** 2026-06-12 
**Spec:** ODTIS `0.9.0-draft`

**Project hub:** [Project hub](/project/) | **All gaps:** [Known gaps](KNOWN-GAPS.md) 
**Machine-readable:** [Gap register (YAML)](gaps.yaml)

These items are **intentionally deferred**. They do not weaken ODTIS MUST requirements in the spec; they document what the VenID reference stack has **not** yet proven in production or external review.

---

## Summary

| Gap ID | Track | Blocks ODTIS Certified? | Target phase |
|--------|-------|-------------------------|--------------|
| [GAP-IC-GOV-API](#gap-ic-gov-api-annex-a-s7) | Contract-only S7 | No (Phase 2 pilot) | Phase 3+ national operator |
| [GAP-TN-0204](#gap-tn-0204-live-mtls) | Production interop | Yes (Trust Network L3 live) | P2-E01 production |
| [GAP-TN-0217](#gap-tn-0217-national-tsa) | Production PKI | Conditional (policy-dependent) | P2-E06 production |
| [GAP-TN-TEP](#gap-tn-tep-ietf-extraction) | IETF informative | No | Governance IETF track |
| [GAP-CERT-L3-ATT](#gap-cert-l3-att-third-party-l3) | Certification | Yes (L3 mark claim) | P4-E07 external |

---

## GAP-IC-GOV-API: Annex A S7 (gov-api)

| Field | Value |
|-------|-------|
| ODTIS ID | `ODTIS-0315`, `ODTIS-0344` (registry assertions) |
| Surface | Annex A **S7** — `gov-api.openapi.yaml` |
| Issue | [#29](https://github.com/odtis/core-impl/issues/29) |

**Decision (Option B — defer):** Keep `gov-api.openapi.yaml` as **normative contract draft**. Do **not** ship `api/gov-api` in Phase 2 pilot.

**Current evidence:**

- Decision record: [gov-api Decision 2026 (YAML)](../evidence/gov-api/gov-api-decision-2026.yaml)
- Annex A index: [INDEX.yaml S7](../../annexes/A-openapi-registry/INDEX.yaml) (`status: deferred`)
- Component binding: [gov-api.yaml](../component-bindings/gov-api.yaml)

**Interim (reference stack):**

| Need | Use instead |
|------|-------------|
| Sector verification | verification-api (S2) |
| National LoA / registry assertions | eregistry-adapter (Extended sandbox overlay) |

**Resolution criteria:**

1. National operator gate and agency credential model approved.
2. Implement `api/gov-api` in `ven-identity-core` matching OpenAPI operationIds.
3. Add `gov-api.yml`, api-gateway route, CI image, conformance smokes.
4. Update `PUBLISHED-SERVICE-SCOPE.md` and close gap in `gaps.yaml`.

**Does not block:** Phase 2 pilot, L2 self-cert, Extended sandbox, or honest Phase 4 target packaging.

---

## GAP-TN-0204: Live mTLS

| Field | Value |
|-------|-------|
| ODTIS ID | `ODTIS-0204` |
| Surface | `exchange-gateway` |
| Test | [Test Gateway Mtls](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_gateway_mtls.md) |
| Epic | P2-E01 |

**Current evidence:** OpenAPI declares `partnerMutualTLS`; static checks PASS (`exchange-gateway-check.sh` spec-only path). Live bilateral handshake requires staging stack with partner client certificates.

**Resolution criteria:**

1. Staging deployment with two exchange-gateway nodes and operator-issued partner certs.
2. Successful mTLS handshake logged; revoked cert rejected (cross-ref GAP-TN-0216 closed).
3. Execute `test_gateway_mtls.md` with signed lab notes; mark test `implemented (live smoke)`.
4. Set gap `status: closed` in `gaps.yaml`; remove `gaps: [GAP-TN-0204]` from RI-MAP exchange-gateway surface.

**Operator doc:** `ven-trust-network/docs/operator/EXCHANGE-GATEWAY.md`

---

## GAP-TN-0217: National TSA

| Field | Value |
|-------|-------|
| ODTIS ID | `ODTIS-0217` |
| Surface | `exchange-gateway` |
| Test | [Test Odtis 0217](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_odtis_0217.md) |
| Epic | P2-E06 |

**Current evidence:** Message timestamp window and signing hooks exist; **national TSA** integration not wired.

**Resolution criteria:**

1. Operator policy names authoritative TSA for production jurisdiction.
2. Implement TSA token validation on signed exchange envelopes per policy.
3. L2/L3 test evidence for timestamp verification path.
4. Close gap when operator policy + live test PASS.

**Note:** Sandbox MAY defer TSA if operator policy does not require it for Phase 2; L3 production audit must document policy choice.

---

## GAP-TN-TEP: IETF extraction

| Field | Value |
|-------|-------|
| ODTIS ID | - (informative) |
| Surface | `exchange-gateway` |
| IETF draft | [TEP draft](../../ietf/drafts/draft-odtis-tep-00.md) |

**Current evidence:** TEP behavior documented in Book 2 and trust-network docs; standalone IETF draft is working-group track, not an ODTIS MUST waiver.

**Resolution criteria:**

1. Publish revised TEP draft with implementer feedback.
2. Cross-link from Annex C and `governance/IETF-ROADMAP.md`.
3. Close gap when draft reaches community review milestone (informative only).

---

## GAP-CERT-L3-ATT: Third-party L3

| Field | Value |
|-------|-------|
| ODTIS ID | `ODTIS-0532` |
| Surface | `conformance-publication` |
| Epic | P4-E07 |

**Current evidence:**

- Phase 4 statement: [Venid Phase4 Full](/implementation/statements/venid-phase4-full/) (target packaging — not production claim)
- Internal dry-run: [L3 Audit Dry Run 2026 Q2 (YAML)](../evidence/phase4-conformance/l3-audit-dry-run-2026-Q2.yaml)
- Auditor evidence pack: [L3 Auditor Evidence Pack 2026 (YAML)](../evidence/phase4-conformance/l3-auditor-evidence-pack-2026.yaml)
- Engagement tracking: [L3 Auditor Engagement 2026 (YAML)](../evidence/phase4-conformance/l3-auditor-engagement-2026.yaml)
- Package script: `conformance/run-phase4-package.sh`
- Evidence smoke: `conformance/run-l3-auditor-evidence-checks.sh`

**Resolution criteria:**

1. Engage accredited auditor or national conformity body.
2. Auditor executes [L3 audit checklist](../../conformance/certification/L3-AUDIT-CHECKLIST.md).
3. Publish attestation letter + findings register (template in [Auditor guide](../../conformance/certification/auditor-guide.md)).
4. Submit summary to `certified-products.yaml` when program is operational.
5. Close gap; update statement `environment: production` only after attestation.

**Does not block:** L2 self-cert, sandbox pilots, or honest Phase 4 **staging** scope declaration.

---

## Process

1. Move gap to `in_progress` in `gaps.yaml` when work starts.
2. Link evidence path before closing.
3. Never mark ODTIS MUST as waived in this file - fix implementation or file RFC per [Errata policy](/governance/ERRATA/).

Related: [Known gaps](KNOWN-GAPS.md) | [L3 certification package](../L3-CERTIFICATION-PACKAGE.md)
