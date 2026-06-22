# Book 2 ↔ ODTIS cross-review (Phase 3.2)

**Status:** Phase 3.2.1 complete - no unresolved MUST contradictions (Jun 2026) 
**ODTIS version:** `0.9.0-draft` 
**Scope:** MUST/SHOULD alignment between Book 2 (Vol. II) and ODTIS sections 1-10

**Project hub:** [Project hub](../project/README.md) | **Sections:** [Section review matrix](SECTION-REVIEW.md)

---

## Method

1. Map each Book 2 chapter to ODTIS sections via [RF traceability index](../traceability/rf-index.yaml).
2. Flag MUST conflicts (Book 2 normative language vs ODTIS MUST).
3. Resolve by updating Book 2 (informative) or ODTIS (normative source of truth).

**Rule:** ODTIS governs conformance claims. Book 2 MUST NOT state requirements that contradict ODTIS MUST without an explicit "informative / pre-ODTIS" label.

---

## Full review matrix

| Book 2 | Title | ODTIS | Review | Notes |
|--------|-------|-------|--------|-------|
| 1 | Introduction | 1, 10 | ✅ | Two-layer model aligns with profiles |
| 2 | Comparative models | 2 (informative) | ✅ | No normative conflict |
| 3 | Reference architecture | 1, 3, 4 | ✅ | Layer 1/2 split matches ODTIS profiles |
| 4 | Digital identity core | 2, 3, 5 | ✅ | Updated: logout 3.1.8, recovery 3.1.9, ErrorCode, Annex A 0.9 |
| 5 | Trust layer / VC | Annex D | 🟡 | Wallet optional; E-Wallet in Annex D draft |
| 6 | Threat model | 8, Annex B | ✅ | Book descriptive; controls in ODTIS-8.x |
| 7 | Civil registry | 2.3.4, Annex D | 🟡 | E-Registry draft; National LoA in 2.3.4 |
| 8 | Exchange gateway | 4, Annex A | ✅ | Chapter rewritten; `exchange-gateway.openapi.yaml` |
| 9 | Autodiscovery | 4.6 (SHOULD) | ✅ | Book 2 ch.9 skeleton; FB-004 scope closed @ 0.9.0-draft |
| 10 | Zero-trust | 8 | ✅ | Cross-ref ODTIS-0525 |
| 11 | Operational PKI | 4.7, 7.3 | 🟡 | Book skeleton; ODTIS CP/CPS reqs complete |
| 12 | Trust federation | 6 | 🟡 | Book skeleton; ODTIS-6.x expanded to 6 IDs (FB-002) |
| 13 | DTI operator | 7, 10 | 🟡 | Book skeleton; RF-27 -> ODTIS-0504 in ODTIS + ch.4 |
| 14 | Reference deployment | 10 | 🟡 | HA metrics informative in ODTIS |
| Ap. F | Events | 9 | ✅ | JSON Schemas in `registry/events/schemas/` |

Legend: ✅ reviewed aligned | 🟡 Book 2 incomplete (skeleton) - no MUST conflict found

---

## Resolved items (was open)

| ID | Issue | Resolution |
|----|-------|------------|
| CR-01 | Logout SHOULD/MUST mix | Book 2 ch.4 section 4.4 cites ODTIS-0308; ODTIS normative |
| CR-02 | Operator UI RF-27 | Book 2 ch.4 section 4.7 maps to `admin.subjects.*`; ODTIS-0504 |
| CR-03 | Gateway vs OpenAPI | Book 2 ch.8 aligned to `exchange-gateway.openapi.yaml` |

---

## Remaining informative gaps (not blockers)

| ID | Gap | Owner | Phase |
|----|-----|-------|-------|
| IG-01 | Book 2 ch.11-13 skeletons | Book 2 | 2.x redaction |
| IG-02 | Federation depth (Book 12 vs ODTIS-6.x) | ODTIS + Book 2 | 3.2 / 4 |
| IG-03 | HA numeric SLAs in Book 14 vs ODTIS-10 | Book 2 | 3.2 |

---

## Exit criteria (Phase 3.2.1)

- [x] Zero unresolved MUST contradictions
- [x] TRACEABILITY-MATRIX ODTIS column synced (30/30 RF)
- [ ] External reviewer sign-off (3.2.4) - **cycle 1 open** until 2026-06-26 ([External review cycle 1](REVIEW-CYCLE-1.md))

---

## Related

- Plan: [Build plan](../PLAN-PHASES.md) Phase 3.2
- Annex A freeze: [Annex A freeze record](../annexes/A-openapi-registry/FREEZE.md)
- Sandbox RI: [Sandbox alignment](../conformance/sandbox/README.md)
- Feedback: [Feedback channels](FEEDBACK.md)
- Review cycle 1: [External review cycle 1](REVIEW-CYCLE-1.md)
