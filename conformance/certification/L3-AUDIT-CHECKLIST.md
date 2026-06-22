# L3 audit checklist (VenID / ODTIS 0.9.0-draft)

**Status:** draft for independent auditors 
**Companion:** [Auditor guide](auditor-guide.md) | [L3 certification package](/implementation/L3-CERTIFICATION-PACKAGE/)

Use this checklist for **third-party** L3 attestation. Internal dry-runs MAY skip sign-off blocks marked *(external)*.

!!! info "How to use this checklist"
    1. Complete **Section A** before site access or fieldwork.
    2. Run **Section B** and **C** from a clean checkout of the operator's statement commit.
    3. Use **Section D** for manual spot checks; expand to full registry as engagement scope requires.
    4. Record **Section E** items as conditional or residual risk - never silent PASS.
    5. Deliver **Section F** artefacts to the operator and program registry.

**Estimated effort (VenID Phase 4 full scope):** 3-5 auditor-days plus operator support.

---

## A. Engagement setup

| # | Item | Evidence | Pass |
|---|------|----------|------|
| A1 | ODTIS version pinned in scope document | Statement `odtis_version` | [ ] |
| A2 | Deployment phase declared (`ODTIS-0532`) | Statement `deployment_phase` | [ ] |
| A3 | Profiles match live deployment | Statement `profiles` vs architecture review | [ ] |
| A4 | Extended sub-modules listed honestly | Statement `extended_modules` | [ ] |
| A5 | Environment labeled (staging vs production) | Statement `environment` | [ ] |
| A6 | Prior L2 report available | `l2-report.md` / JSON | [ ] |

---

## B. Repository integrity (L1)

| # | Command / artefact | Pass |
|---|-------------------|------|
| B1 | `./conformance/run.sh` | [ ] |
| B2 | `python3 scripts/validate-section-completeness.py` | [ ] |
| B3 | `python3 scripts/validate-ri-map.py` | [ ] |
| B4 | `python3 scripts/validate-component-bindings.py` | [ ] |

---

## C. Automated L2 against target

| # | Item | Pass |
|---|------|------|
| C1 | `ODTIS_TARGET=<url> python3 conformance/l2/run_l2.py --output l2-report.json` | [ ] |
| C2 | Review FAIL items in rendered `l2-report.md` | [ ] |
| C3 | Re-run `./conformance/run-phase4-package.sh` with target set (if Phase 4 scope) | [ ] |

---

## D. Profile spot checks (manual)

Sample MUST requirements per profile; expand to full registry as needed.

### Reference Architecture

| # | Requirement | Procedure stub | Pass |
|---|-------------|----------------|------|
| D0 | ODTIS-0006 no weakening | `test_extended_no_weakening.md` | [ ] |

### Core Identity

| # | Requirement | Procedure stub | Pass |
|---|-------------|----------------|------|
| D1 | ODTIS-0301 OIDC discovery | `test_odtis_0301.md` | [ ] |
| D2 | ODTIS-0315 verify client auth | `test_verification_client_auth.md` | [ ] |
| D3 | ODTIS-0328 explicit consent | `test_explicit_consent_first_release.md` | [ ] |
| D4 | ODTIS-0535 fail-closed denial | `test_fail_closed_denial_paths.md` | [ ] |

### Trust Network

| # | Requirement | Procedure stub | Pass |
|---|-------------|----------------|------|
| D5 | ODTIS-0201 gateway-only routing | `test_gateway_only_routing.md` | [ ] |
| D6 | ODTIS-0224 grant fail-closed | `test_grant_fail_closed.md` | [ ] |
| D7 | ODTIS-0204 mTLS | `test_gateway_mtls.md` - see deferred note | [ ] |

### Federation

| # | Requirement | Procedure stub | Pass |
|---|-------------|----------------|------|
| D8 | ODTIS-0401 non-transitivity | `test_non_transitivity.md` | [ ] |
| D9 | ODTIS-0407 suspension routing | `test_agreement_suspension_routing.md` | [ ] |

### Operator

| # | Requirement | Procedure stub | Pass |
|---|-------------|----------------|------|
| D10 | ODTIS-0501 published scope | `test_published_service_scope.md` | [ ] |
| D11 | ODTIS-0530 regulator export | `test_audit_export_pii_minimized.md` | [ ] |

### Extended (only if declared)

| # | Module | Smoke script | Pass |
|---|--------|--------------|------|
| D12 | E-Wallet | `run-ewallet-checks.sh` | [ ] |
| D13 | E-Registry | `run-extended-eregistry-checks.sh` | [ ] |
| D14 | E-Inclusion | `run-inclusion-checks.sh` | [ ] |
| D15 | E-Webhook | `run-ewebhook-checks.sh` | [ ] |
| D16 | E-Signature | `run-esignature-checks.sh` | [ ] |
| D17 | E-KYB | `run-ekyb-checks.sh` | [ ] |
| D18 | ODTIS-0006 no weakening | `run-extended-no-weakening-checks.sh` | [ ] |

---

## E. Deferred production items (document, do not silently PASS)

| Gap ID | Auditor action |
|--------|----------------|
| GAP-TN-0204 | Record conditional FAIL or N/A until live mTLS evidence |
| GAP-TN-0217 | Confirm operator TSA policy; test if required |
| GAP-TN-TEP | Informative only - no ODTIS MUST waiver |
| GAP-CERT-L3-ATT | *(external)* This engagement closes the gap |

Details: [Deferred production track](/implementation/gaps/DEFERRED-TRACK/)

---

## F. Attestation outputs *(external)*

| # | Deliverable | Published |
|---|-------------|-----------|
| F1 | Attestation letter (profiles, version, date, auditor identity) | [ ] |
| F2 | Findings register (ODTIS ID, pass/fail, evidence ref) | [ ] |
| F3 | Residual risks (SHOULD gaps, deferred track) | [ ] |
| F4 | Optional: PR to `certified-products.yaml` when program live | [ ] |

---

## Sign-off

| Role | Name | Date |
|------|------|------|
| Lead auditor | | |
| Operator representative | | |
| Conformance lead | | |

Outcome: [ ] PASS [ ] CONDITIONAL PASS [ ] FAIL

---

## Related

- [Auditor guide](auditor-guide.md)
- [Certification program](/governance/CERTIFICATION/)
- [L3 certification package](/implementation/L3-CERTIFICATION-PACKAGE/)
