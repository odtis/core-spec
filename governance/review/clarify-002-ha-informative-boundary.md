# Clarify HA / SLA boundary between ODTIS-10 and Book 2 ch.14

**Issue type:** clarification (non-normative) 
**Review ID:** FB-003 (**accepted**) 
**ODTIS IDs:** ODTIS-0532, ODTIS-0533 
**Cross-ref:** Book 2 ch.14 (IG-03)

**Review cycle:** [External review cycle 1](../REVIEW-CYCLE-1.md) | **Project:** [Project hub](/project/)

---

## Observed text

ODTIS section 10 defines deployment phases and conformance statement fields but does not norm numeric HA targets (uptime %, RTO/RPO). Book 2 ch.14 (skeleton) may imply numeric SLAs in informative prose.

## Proposed clarification

Numeric HA/SLA targets SHOULD remain **informative in Book 2** until Phase 4 operator certification defines auditable metrics. ODTIS-10 MUST continue to bind **phase** and **profile claims** only.

Add an informative note to `spec/10-deployment-profiles/SPEC.md` 10.3 cross-referencing Book 2 ch.14 without importing numeric MUSTs.

## Question for reviewers

Should ODTIS-10 add a SHOULD for minimum observability signals (e.g. health endpoints, SLO export) without fixing numeric thresholds?
