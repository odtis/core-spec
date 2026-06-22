# Clarify ODTIS-4.6.1 autodiscovery SHOULD scope

**Issue type:** clarification (non-normative) 
**Review ID:** FB-004 (**accepted**) 
**ODTIS ID:** ODTIS-4.6.1 
**Cross-ref:** Book 2 ch.9 (skeleton)

**Review cycle:** [External review cycle 1](../REVIEW-CYCLE-1.md) | **Project:** [Project hub](/project/)

---

## Observed text

ODTIS-4.6.1 states partners SHOULD support autodiscovery of gateway endpoints. Book 2 ch.9 is still a skeleton. L2 has no live autodiscovery check.

## Proposed clarification

Document in Annex A README that autodiscovery is **out of Annex A OpenAPI scope** for `0.9.0-draft`; conformance remains manual stub until Book 2 ch.9 and a discovery well-known URI are defined.

## Question for reviewers

Should autodiscovery stay SHOULD-only for `0.9.x`, or promote to MUST for Trust Network L2 in Phase 4?

## Decision (stewards @ 0.9.0-draft)

**SHOULD-only** for review draft. Autodiscovery is documented as **out of Annex A OpenAPI scope**; manual conformance stub remains until Book 2 ch.9 and a discovery well-known URI exist. Phase 4 MAY revisit MUST promotion for Trust Network L2.
