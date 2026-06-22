# Clarify ODTIS-0331 conformance test linkage

**Issue type:** clarification (non-normative) 
**Review ID:** FB-001 (**accepted**) 
**ODTIS ID:** ODTIS-0331 
**Section:** `spec/05-consent-privacy/SPEC.md` 5.2

**Review cycle:** [External review cycle 1](../REVIEW-CYCLE-1.md) | **Templates:** [Project hub](README.md) | **Project:** [Project hub](/project/)

---

## Observed text

Section 5.2 cites `test_verification_consent_scope.md` and `test_consent_gated_claims.md` for ODTIS-0331, but those stubs listed only ODTIS-0317 and ODTIS-0307 respectively. The conformance manifest reported 98% core-identity coverage (1 requirement without explicit test link).

## Proposed clarification

**Steward action (2026-06-12):** Add ODTIS-0331 to both test stub requirement headers so manifest coverage matches spec cross-refs. No normative text change.

**Decision (2026-06-12):** Dedicated stub **`test_odtis-5_1_4.md`** added as canonical registry link. Composite stubs remain for 3.1.7 and 3.5.3 integration tests. Spec 5.1.4 note clarifies requirement boundaries.

## Question for reviewers

Is scope-enforcement (5.1.4) adequately distinguished from consent-gating (3.1.7) and Verification API scope rules (3.5.3), or should a dedicated `test_odtis-5_1_4.md` stub exist?

**Steward answer:** Yes - dedicated stub added; distinction documented in spec 5.1.4 note (FB-001 closed).

## Pass criteria suggestion

- Error payloads on denial MUST NOT leak restricted attribute values (5.1.4 second sentence).
