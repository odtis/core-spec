# ODTIS - Phased build plan

Aligned with [PLAN-PHASES](PLAN-PHASES.md) (Phase 3-4) and the [traceability coverage report](traceability/coverage-report.yaml) section 8.4.

**Project hub:** [Project hub](project/README.md) | **Live status:** [Project status](site/STATUS.md)

!!! info "Current phase: 3.2"
    Review and stabilization @ `0.9.0-draft`. External review cycle 1 open until **2026-06-26**. Exit criteria: [Review close checklist](governance/REVIEW-CYCLE-1-CLOSE.md).

---

## Current status: Phase 3.2 - Review and stabilization

| ID | Task | Status |
|----|------|--------|
| 3.1.1-3.1.10 | Sections 1-10 normative prose | ✅ review draft @ 0.9.0-draft |
| 3.1.11 | Annex A OpenAPI | ✅ frozen 0.9.0-draft |
| 3.1.12 | Annex B Threats | ✅ |
| 3.1.13 | Annex C Standards | ✅ |
| 3.1.14 | Annex D Extended | ✅ draft |
| 3.1.15 | Conformance suite | ✅ L1+L2; 159 procedures (81 implemented) |
| 3.1.16 | odtis.org site | ✅ build + local deploy to EC2 |
| 3.1.17 | TRACEABILITY-MATRIX sync | ✅ 30/30 RF |
| 3.2.1 | Book 2 ↔ ODTIS cross-review | ✅ |
| 3.2.2 | Annex A freeze | ✅ 0.9.0-draft + checksums |
| 3.2.3 | Sandbox RI alignment | ✅ map in `conformance/sandbox/` |
| 3.2.4 | External feedback | ✅ cycle 1 open (2026-06-12 -> 2026-06-26) |
| 3.2.5 | Foundation track A (publication, governance, ietf, profiles) | ✅ |
| 3.2.6 | Adoption guide + L3 auditor draft + structure coherence | ✅ |

Phase 3.0 scaffold: ✅ (2026-06-12)

---

## Phase 3.0 - Scaffold (complete)

| ID | Task | Status | Output |
|----|------|--------|--------|
| 3.0.1 | Create `odtis/` repo | ✅ | Full structure |
| 3.0.2 | Registry 103 IDs from P18 | ✅ | `registry/requirements.json` (+105) |
| 3.0.3 | Stubs sections 1-10 + Annex A-D | ✅ | `spec/`, `annexes/` |
| 3.0.4 | Draft conformance profiles | ✅ | `registry/profiles.yaml`, `conformance/` |
| 3.0.5 | Governance and versioning | ✅ | `governance/` |
| 3.0.6 | RF traceability stub | ✅ | `traceability/` |

---

## Phase 3.1 - Normative draft (8-12 workspace months)

**Depends on:** Book 2 ≥90% chapters drafted (Phase 2)

| ID | Deliverable | Source | Exit criteria |
|----|-------------|--------|---------------|
| 3.1.1 | **1 Scope & conformance** | P18 2, report 8.4 | Profiles, keywords, conformance levels drafted |
| 3.1.2 | **2 Terminology & LoA** | P01, P07, P11, doc 11 | Definitions + LoA matrix; ODTIS-2.x IDs from P18 |
| 3.1.3 | **3 Identity services** | P13, P14, doc 03 RF | Layer 1 MUST/SHOULD; OpenAPI cross-refs |
| 3.1.4 | **4 Trust network** | P04, P05, P09 | Gateway, discovery, grants |
| 3.1.5 | **5 Consent & privacy** | P01, P07 | Minimization, revocation |
| 3.1.6 | **6 Federation** | P09 | Bilateral, non-transitive |
| 3.1.7 | **7 Operator governance** | P10, P08, Book 1 ch. 13 | PKI, audit, liability |
| 3.1.8 | **8 Security** | P06, P07 | Zero-trust profile referenced |
| 3.1.9 | **9 Audit & events** | P15, DS-07, Book 2 App. F | Event catalog + retention |
| 3.1.10 | **10 Deployment profiles** | P12, P16 | Phases 1-4, HA, observability |
| 3.1.11 | **Annex A** OpenAPI registry | DS-10, P14 | Versioned schemas in repo |
| 3.1.12 | **Annex B** Threat mitigations | P07 | Threat -> control table |
| 3.1.13 | **Annex C** Standards mapping | P18, P02, P03 | eIDAS, NIST, OIDC |
| 3.1.14 | **Annex D** Extended profiles | P17, doc 14 | Webhooks, inclusion, KYB (draft) |
| 3.1.15 | Draft conformance suite | Registry + test stubs | ≥1 test per Core profile |
| 3.1.16 | `odtis.org` site | `site/mkdocs.yml` | Public draft preview |
| 3.1.17 | Sync TRACEABILITY-MATRIX | RF matrix | ≥60% RF with ODTIS ID |

**Target version:** `0.9.0-draft`

---

## Phase 3.2 - Review and stabilization

| ID | Deliverable | Criterion |
|----|-------------|-----------|
| 3.2.1 | Cross-review Book 2 ↔ ODTIS | No MUST/SHOULD contradictions |
| 3.2.2 | Freeze Annex A OpenAPI for draft | Semver tags pre-1.0 |
| 3.2.3 | Reference implementation (sandbox) | Book 3 C1-C4 aligned |
| 3.2.4 | External feedback (operators, RPs) | Issue tracker / lightweight RFC |

**Target version:** `0.9.x-draft` until feedback closed

---

## Phase 4 - ODTIS v1.0 (12-18 workspace months)

**Depends on:** ODTIS draft + Phase 1 pilot metrics

| ID | Deliverable | Exit criteria |
|----|-------------|---------------|
| 4.1 | **ODTIS v1.0** frozen text | Semver `1.0.0`; CHANGELOG; git tag |
| 4.2 | Conformance suite v1.0 | Automated tests per profile |
| 4.3 | Operator certification (process) | Final `governance/GOVERNANCE.md` |
| 4.4 | DOI / standards registry | Zenodo or equivalent |
| 4.5 | Book 3 Vol. III published | Implementation aligned to v1.0 |
| 4.6 | 100% RF traceability | Complete TRACEABILITY-MATRIX |
| 4.7 | JOSS / empirical evidence | Documented pilot metrics |

---

## Recommended work order (within Phase 3.1)

```
1 Scope -> 2 Terminology -> 3 Identity -> 5 Consent
-> 4 Trust Network -> 6 Federation
-> 8 Security -> 7 Operator -> 9 Events -> 10 Deployment
-> Annex C -> Annex A -> Annex B -> Annex D
-> conformance tests -> site publish
```

Section 3 and Annex A depend on stable P14. Section 9 depends on Book 2 App. F or P15.

---

## Do not

- Publish `1.0.0` before Book 2 is stable and pilot metrics exist
- Edit requirements only in P18 without syncing `registry/` and `spec/`
- Mix operational text (Book 3) into `spec/`
- Use CC BY-NC-ND for ODTIS normative text (use CC BY 4.0)

---

## Immediate next steps (Phase 3.2 -> 4)

1. **Adoption readiness** - [Adoption guide](ADOPTION.md); Zenodo DOI; deploy `odtis.org`
2. **External review** - Cycle 1 comment period ([External review cycle 1](governance/REVIEW-CYCLE-1.md))
3. **Executable Core Identity L2** - replace stub status on priority tests in `conformance/tests/core-identity/`
4. **Federation depth** - triage FB-002 ([Federation interoperability RFC](governance/rfc/2026-06-12-federation-interoperability.md))
5. **Host deploy** - Sync `build/odtis-spec-site/` to `odtis.org` when DNS ready
6. **Second implementation** - update [RI surface map](implementation/RI-MAP.yaml) interop report
7. Promote to **`0.9.x-draft`** after cycle 1 triage
