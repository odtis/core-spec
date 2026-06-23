---
title: "Section 10: Deployment profiles"
description: Cross-profile deployment phases, adoption matrix, and profile combination rules for ODTIS operators.
---

# 10 Deployment profiles

<div class="odtis-spec-meta" markdown="1">

| Field | Value |
|-------|-------|
| **Status** | review draft - Phase 3.2 |
| **Spec version** | 0.9.0-draft |
| **Derived from** | P18 9.4, P01 Figure 7, P10, P12, P16, DS-09 |
| **Registry IDs** | ODTIS-0532 - ODTIS-0534 (3 requirements) |
| **Profile** | Operator (cross-cutting); all conformance statements |

</div>

---

## 10.1 Scope

This section defines **deployment phases** for ODTIS implementations: which profiles and Extended sub-modules MAY be activated in production at each phase, and what **conformance statements MUST declare**.

Deployment phases are **operator program labels** aligned with the VenID roadmap (P01 Figure 7, P10, P12). They do not replace jurisdiction-specific procurement or certification milestones.

---

## 10.2 Phased deployment model

**Table 10-1 - Deployment phases (normative guidance + conformance binding)**

| Phase | Name | Typical scope | Minimum ODTIS profiles (production) | Extended sub-modules |
|-------|------|---------------|-------------------------------------|----------------------|
| **1** | Pilot / sandbox | Single region, limited RPs/partners | Core Identity (L1 acceptable) | None in production |
| **2** | Production scale-up | Single region production | Core Identity + Trust Network (L2 recommended) | E-Wallet optional pilot |
| **3** | National / multi-region | HA, registry integration | Core + Trust Network + Operator (L2-L3) | E-Registry, federation prep |
| **4** | Full operator mandate | Federation production, SOC 24/7 | All claimed profiles + Operator L3 targets | E-Registry, E-Inclusion, E-Webhook as declared |

Phases are **ordinal**: an operator MUST NOT skip phase-appropriate controls when claiming higher phase capabilities (see ODTIS-0505, ODTIS-0506).

**Table 10-2 - Security emphasis by phase (informative)**

| Phase | Security emphasis |
|-------|-------------------|
| 1 | OIDC hardening, audit baseline, gateway perimeter pilot |
| 2 | Zero trust Phase 2 (P06), grants and cache hardening |
| 3 | HSM PKI cutover, registry adapter security, federation agreements |
| 4 | SOC 24/7, certifications roadmap achieved, national governance |

---

### ODTIS-0532 - Conformance statement phase declaration

**Conformance statements MUST** declare:

1. **deployment phase** (1, 2, 3, or 4) of the production environment being evaluated;
2. **active Extended sub-modules** (E-Wallet, E-Registry, E-Inclusion, E-Webhook, E-Signature, E-KYB) actually activated in that environment; and
3. **active Reliance Extension sub-modules** (Annex E; e.g. R-Base, R-Agent-Authority) actually activated when the `reliance-extensions` profile is claimed.

Declaration MUST match observable production configuration, not roadmap intent alone. When Reliance Extensions are claimed, `reliance_extensions` MUST include **R-Base** and every additional active sub-module (`ODTIS-0708`).

**Trace (informative):** P01 Figure 7, P10, Annex E
**Conformance test:** Compare conformance statement to production config and feature flags; mismatches fail review.

---

### ODTIS-0533 - Phase 1 Extended module prohibition

**Phase 1 implementations MUST NOT** claim **Extended sub-modules** that are **not activated in production**.

Laboratory or sandbox testing of Extended capabilities MUST be labeled as non-production in conformance materials. Phase 1 production conformance MAY include Core Identity only, or Core Identity with Trust Network pilot if explicitly scoped and documented.

**Trace (informative):** 1.6.5, P18 3.3.3
**Conformance test:** Phase 1 conformance statement lists no Extended sub-modules unless production endpoints exist and pass Extended tests.

---

### ODTIS-0534 - Conformance statement dual format

The operator **MUST** publish conformance statements in **both**:

1. **human-readable** form (Markdown or PDF); and
2. **machine-readable** form (JSON or YAML).

Both forms MUST contain the minimum fields in ODTIS-0008 and MUST reference the same `odtis_version`, profiles, level, and test summary.

**Trace (informative):** P18 1.9.1, Book 1 cap. 5.4
**Conformance test:** Fetch human and machine statements; field parity check passes.

---

## 10.3 Profile activation by phase

**Table 10-3 - Profile activation matrix (normative intent)**

| Profile | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
|---------|---------|---------|---------|---------|
| Core Identity | MUST (if any ODTIS claim) | MUST | MUST | MUST |
| Trust Network | MAY (pilot) | MUST if Layer 2 production | MUST if Layer 2 production | MUST if Layer 2 production |
| Federation | MUST NOT (production) | MUST NOT unless agreement | MAY | MAY when agreements active |
| Operator | MAY (minimal L1) | SHOULD (L2) | SHOULD (L2-L3) | SHOULD (L3) |
| Extended | MUST NOT in prod (10.1.2) | Optional declared modules | E-Registry typical | Full optional set |
| Reliance Extensions | R-Base, R-VC-Maturity-Gate MAY (phase 1) | Tier 1 modules MAY (phase 2+) | Tier 2 modules MAY (phase 3+) | Tier 3 modules MAY (phase 4+) |

Reliance Extension phase gates: [Annex E activation](/annexes/E-reliance-profiles/activation.yaml). Claiming `reliance-extensions` without listing active sub-modules in `reliance_extensions` fails `ODTIS-0708`.

Federation profile (6) MUST NOT be claimed in production until Phase 3+ unless operator documents early bilateral pilot under Phase 2 with explicit scope limitation in conformance statement.

Machine-readable phase × Extended module rules: [Activation (YAML)](/annexes/D-extended-profiles/activation.yaml) (Annex D). Annex review matrix: [Annex review matrix](/governance/ANNEX-REVIEW/).

---

## 10.4 High availability and observability

Normative HA metrics are not universal MUST values in ODTIS draft; operators document targets in policy and conformance statements.

!!! note "FB-003 - HA / SLA boundary (informative)"
    Numeric uptime percentages, RTO, and RPO targets belong in **operator policy** and Book 2 ch. 14 (informative). ODTIS section 10 binds **deployment phase** and **profile claims** only (ODTIS-0532, ODTIS-0533). See [FB-003 HA boundary](/governance/review/clarify-002-ha-informative-boundary/).

### 10.4.1 High availability (informative)

Operators in Phase 3-4 SHOULD document:

| Metric | Typical target (informative) |
|--------|------------------------------|
| IdP / Verification API availability | ≥99.5% (ODTIS-0511) |
| Gateway availability | Per ODTIS-0220 when Trust Network claimed |
| RTO / RPO | Operator-defined; tested DR per ODTIS-0510 |

P16 and DS-09 provide engineering depth for Book 2 ch. 14 and Book 3.

### 10.4.2 Observability (informative)

Implementations SHOULD expose:

- metrics for registration, verification, exchange volume, and error rates (ODTIS-0513);
- distributed tracing compatible with `trace_id` (ODTIS-0529); and
- health endpoints for deployment profile validation (3.5.1).

Regulator-facing aggregates MUST use PII-minimized export (ODTIS-0530).

---

## 10.5 Reproducible demo and conformance lab

Paper P12 defines a **reproducible demonstration** profile for Phases 1-2. ODTIS conformance labs MAY use:

| Artifact | Purpose |
|----------|---------|
| Containerized or scripted deploy | Repeatable Core Identity + optional Trust Network sandbox |
| Test data vectors | Proofing, OIDC, verification API, gateway exchange |
| Conformance test suite | [Conformance](/conformance/) stubs linked from registry |

Lab deployments at **L1** MAY run at Phase 1 profile without production SLA claims. Lab MUST NOT be cited as Phase 4 production conformance.

---

## 10.6 Cross-references

| Topic | Section |
|-------|---------|
| Conformance levels L1-L3 | 1.8 |
| Conformance statement fields | 1.9 |
| Operator phase maturity | 7.3 |
| Federation activation | 6.5, ODTIS-0403 |
| Extended sub-modules | 1.6.5, Annex D |
| OpenAPI / verify contracts | Annex A |
| Standards / LoA disclosure | Annex C |
| Threat audit (informative) | Annex B |
| HA engineering depth (informative) | Book 2 ch. 14 |

---

## 10.7 Requirement index

<!-- GENERATED:section-index:START -->
<!-- Generated by scripts/generate-spec-section-indexes.py @ 0.9.0-draft -->

**Table 10-* - Requirement index (3 IDs)**

| ID | Keyword | Summary |
|----|---------|---------|
| ODTIS-0532 | MUST | Conformance statements MUST declare deployment phase, active Extended s… |
| ODTIS-0533 | MUST NOT | Phase 1 implementations MUST NOT claim Extended sub-modules not activat… |
| ODTIS-0534 | MUST | Operator MUST publish conformance statements in both human-readable and… |

<!-- GENERATED:section-index:END -->

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| stub | 2026-06-12 | Scaffold Phase 3.0 |
| draft v0.5 | 2026-06-12 | 10.1-10.7 normative prose; 2 IDs |
| 0.9.0-draft | 2026-06-12 | Phase 3.2 section review; FB-003 HA boundary; Annex D activation cross-ref |

**Phase 3.1 checklist (10).**

- [x] Phased model aligned with P01/P10/P18 Table 9.4
- [x] Conformance declaration requirements (10.1.x)
- [x] HA/observability/demo informative guidance
- [x] **1-10 normative prose complete** (review draft @ 0.9.0-draft)


**Phase 3.2 review checklist (10).**

- [x] Registry IDs cited in normative prose
- [x] Requirement index matches registry
- [x] Conformance test stub per ID
- [x] FB-003 HA metrics informative boundary ([FB-003 HA boundary](/governance/review/clarify-002-ha-informative-boundary/))
- [x] Annex D activation matrix cross-ref ([Annex review matrix](/governance/ANNEX-REVIEW/))
- [ ] External review cycle 1 ([Section review matrix](/governance/SECTION-REVIEW/))
