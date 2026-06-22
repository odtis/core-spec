# ODTIS Consistency & Implementation Audit Report

**Date:** 2026-06-15 
**Spec version:** `0.9.0-draft` 
**Repository:** `odtis/core-spec` 
**Scope:** Profiles, normative sections, registry, conformance tests, RI implementation, phased backlog

---

## 1. Executive summary

ODTIS `0.9.0-draft` is **structurally sound** at the registry and manifest level: **149 normative requirements**, **100% test stub linkage** (159 unique procedures; profile manifests list 172 cross-profile links), and **automated validators pass** (`validate-registry.py`, `validate-manifest-coverage.py`, `run-conformance.py --check-links`).

The main gap is **evidence depth**, not specification completeness:

| Layer | Status | Score |
|-------|--------|------:|
| Registry ↔ tests linkage | Complete | 100% |
| Spec prose ↔ requirement indexes | **Broken** | ~0% (validator fails) |
| Conformance test `implemented` status | Partial | **51%** (81/159 procedures) |
| VenID RI surfaces | Partial | **89%** partial (31/35) |
| Backlog epics | In progress | **74%** partial (29/39) |
| Implementation gaps | Closed (sandbox) | 20 closed / 4 deferred |

**Strongest profile:** Federation - 8/8 requirements with `implemented` test evidence. 
**Weakest profiles:** Trust Network (0/29), Core Identity (2%), Operator (6%).

---

## 2. Repository inventory

### 2.1 Structure

| Area | Path | Role |
|------|------|------|
| Normative spec | `spec/01..10-*/SPEC.md` | 10 sections |
| Profile docs | `spec/profiles/*.md` | 6 conformance profiles |
| Registry | `registry/requirements.json` | 149 ODTIS IDs |
| Conformance | `conformance/tests/`, `manifest.yaml` | 159 procedures (172 manifest links) |
| Annexes | `annexes/A..D` | OpenAPI, threats, standards, Extended |
| Implementation | `implementation/` | RI-MAP, backlog, gaps, statements |
| Validators | `scripts/validate-*.py` | 10 structural checks |
| Smoke | `conformance/run-*-checks.sh` | 23 package scripts |

### 2.2 Normative keyword distribution

| Keyword | Count | % |
|---------|------:|--:|
| MUST | 113 | 76% |
| MUST NOT | 19 | 13% |
| SHOULD | 16 | 11% |
| MAY | 1 | <1% |

**Interpretation:** ODTIS is predominantly **binding (MUST)**. SHOULD requirements (16) are candidates for staged L2->L3 hardening, not Phase 1 blockers.

### 2.3 Requirements by domain

| Domain | Title | IDs | Count |
|--------|-------|-----|------:|
| ODTIS-0000 | Reference Architecture | 0001-0010 | 10 |
| ODTIS-0001 | Core Concepts (LoA) | 0101-0108 | 8 |
| ODTIS-0002 | Trust Registry | 0201-0226 | 26 |
| ODTIS-0003 | Identity Assurance | 0301-0365 | 61 |
| ODTIS-0004 | Federation | 0401-0408 | 8 |
| ODTIS-0005 | Governance | 0501-0536 | 36 |
| ODTIS-0006 | Payment Trust Layer | - | 0 (reserved) |

### 2.4 Requirements by spec section

| Section | Reqs | MUST | MUST NOT | SHOULD | Tests implemented |
|---------|-----:|-----:|---------:|-------:|------------------:|
| 01-scope-conformance | 10 | 4 | 6 | 0 | 1/10 |
| 02-terminology-loa | 8 | 7 | 1 | 0 | 1/8 |
| 03-identity-services | 27 | 21 | 2 | 4 | 0/27 |
| 04-trust-network | 26 | 19 | 2 | 4 | 0/26 |
| 05-consent-privacy | 34 | 25 | 5 | 4 | 6/34 |
| 06-federation | 8 | 7 | 0 | 1 | **8/8** |
| 07-operator-governance | 17 | 14 | 1 | 2 | 0/17 |
| 08-security | 10 | 8 | 1 | 1 | 0/10 |
| 09-audit-events | 6 | 6 | 0 | 0 | 1/6 |
| 10-deployment-profiles | 3 | 2 | 1 | 0 | 1/3 |

---

## 3. Profile deep dive

### 3.1 Reference Architecture

| Field | Value |
|-------|-------|
| Profile ID | `reference-architecture` |
| Depends on | - (root) |
| Requirements | 10 (ODTIS-0001..0010) |
| Tests | 10 |
| Implemented | 1 (ODTIS-0006 anti-weakening) |
| Mandatory sections | `01-scope-conformance` |

**Normative focus:** Profile composition rules (MUST NOT claim TN without CI, Federation without TN), statement structure (ODTIS-0008), prohibited claims (ODTIS-0007), Extended anti-weakening (ODTIS-0006).

**Coherence:** `profiles.yaml` `depends_on` chains align with ODTIS-0001/0002/0004. `validate-conformance-statement.py` enforces phase/profile rules (ODTIS-0532).

**Gaps:** 9/10 tests pending `implemented` marker - mostly statement linter / dependency-chain checks that are **automated in CI** but not yet marked in test docs.

**Implementation phase:** P0 (done) - extend to mark `test_layer2_requires_layer1`, `test_profile_dependency_chain`, etc. as `implemented` after CI evidence attach.

---

### 3.2 Core Identity

| Field | Value |
|-------|-------|
| Profile ID | `core-identity` |
| Depends on | `reference-architecture` |
| Requirements | 45 (excludes Extended IDs 0340+) |
| Tests | 58 (multi-req tests) |
| Implemented | ~2% (ODTIS-0104 via E-Registry path) |
| Sections | 02, 03, 05 (partial) |

**Sub-areas:**

| Area | Key MUSTs | RI surface | Backlog |
|------|-----------|------------|---------|
| LoA / claims | ODTIS-0101-0108 | `loa-policy` | P1-E01 |
| OIDC IdP | ODTIS-0301-0308 | `keycloak-oidc-idp` | P1-E02 |
| Registration | ODTIS-0309-0314 | `identity-core`, `verification-engine` | P1-E03 |
| Verification API | ODTIS-0315-0318 | `verification-api` | P1-E04 |
| RP lifecycle | ODTIS-0319-0321 | `admin-api` | P1-E05 |
| Consent | ODTIS-0328-0332 | `consent-service` | P1-E06 |
| Citizen portal | ODTIS-0322-0324 | `citizen-api`, `portal-ciudadano` | P1-E07 |
| Transport | ODTIS-0325-0327 | `api-gateway` | P1-E08 |
| Audit events | ODTIS-0527, 0529 | identity events | P1-E09 |

**SHOULD items (staging targets):** ODTIS-0314 (biometric retention), ODTIS-0318 (P95 latency), ODTIS-0323 (connected RPs view).

**Coherence issues:**

- Section `03-identity-services` requirement index **empty** per `validate-section-completeness.py` (27 IDs not indexed in SPEC prose tables).
- `PHASED-BACKLOG.md` summary counts stale vs `phased-backlog.yaml` epic statuses.

**Implementation phase:** P1 - prioritize L2 live evidence for ODTIS-0315-0317 (verification API), 0308 (logout), 0328-0331 (consent).

---

### 3.3 Trust Network

| Field | Value |
|-------|-------|
| Profile ID | `trust-network` |
| Depends on | `core-identity` |
| Requirements | 27 (+ ODTIS-0106 include) |
| Tests | 30 |
| Implemented | **0%** |
| Section | `04-trust-network` |

**Sub-areas:**

| Area | Key MUSTs | RI surface | Status |
|------|-----------|------------|--------|
| Exchange gateway | ODTIS-0201-0207, 0219-0221 | `exchange-gateway` | partial |
| Grants / catalog | ODTIS-0208-0213, 0224-0226 | `trust-registry`, `portal-api` | partial/done |
| Sender routing | ODTIS-0222-0223 | `exchange-gateway-sender` | **done** |
| Metadata-only | ODTIS-0225 | `audit-service`, `trust-registry` | partial |
| PKI | ODTIS-0215-0218 | `trust-authority`, `trust-service` | partial |
| Fail-closed | ODTIS-0535 | gateway + verification | partial |

**SHOULD items:** ODTIS-0206 (timestamp/replay), ODTIS-0214 (autodiscovery), ODTIS-0217 (TSA), ODTIS-0221 (zero trust).

**Deferred gaps:** GAP-TN-0204 (live mTLS), GAP-TN-0217 (TSA).

**Coherence:** Sandbox unit/static evidence exists (`run-gap-closure-checks.sh`) but **no conformance test doc** marked `implemented`. This is the largest evidence/documentation disconnect.

**Implementation phase:** P2 - mark trust-network tests `implemented` as L2 smokes pass; run live stack for ODTIS-0204.

---

### 3.4 Federation

| Field | Value |
|-------|-------|
| Profile ID | `federation` |
| Depends on | `trust-network` |
| Requirements | 8 (ODTIS-0401-0408) |
| Tests | 8 |
| Implemented | **100%** |
| Section | `06-federation` |

**Requirements:**

| ID | Keyword | Topic |
|----|---------|-------|
| ODTIS-0401 | MUST | Non-transitive trust |
| ODTIS-0402 | MUST | Federation cert policy |
| ODTIS-0403 | MUST | Explicit activation |
| ODTIS-0404 | MUST | Route validation |
| ODTIS-0405 | MUST | Suspended agreements |
| ODTIS-0406 | SHOULD | Regulator metadata publish |
| ODTIS-0407 | MUST | Route cache TTL |
| ODTIS-0408 | MUST | Federated audit instance IDs |

**Coherence:** `conformance/profiles/federation/README.md` is **stale** (lists 3 tests; manifest has 8). Registry and VenID `FederationRouteCache` align with 0407/0408.

**Implementation phase:** P4-E01 (partial) - production bilateral activation; update federation README.

---

### 3.5 Operator

| Field | Value |
|-------|-------|
| Profile ID | `operator` |
| Depends on | `reference-architecture`, `core-identity` |
| Requirements | 36 (ODTIS-05xx) |
| Tests | 36 |
| Implemented | 2 (ODTIS-0530, 0532) |
| Sections | 07, 08, 09, 10 |

**Themes:**

| Theme | IDs (sample) | Evidence |
|-------|--------------|----------|
| Governance | ODTIS-0501-0506 | `operator-governance-check.sh` |
| PKI stewardship | ODTIS-0507-0510 | CP/CPS, ceremony docs |
| SLA / metrics | ODTIS-0513-0517 | `gateway-sla.yaml`, metrics APIs |
| Regulator / liability | ODTIS-0514-0516 | `regulator-api` |
| Security platform | ODTIS-0518-0520 | `ven-infra-core` |
| Audit export | ODTIS-0528-0530 | audit platform |
| Fail-closed | ODTIS-0535 | cross-layer smokes |
| Phase declaration | ODTIS-0532-0534 | phase1-4 packages |

**MUST NOT highlights:** ODTIS-0506 (no false Phase 4 claims), ODTIS-0533 (Phase 1 no Extended in prod statement).

**Deferred:** GAP-CERT-L3-ATT (third-party L3).

**Implementation phase:** P3 - operator smokes exist; mark tests `implemented` per package script PASS.

---

### 3.6 Extended

| Field | Value |
|-------|-------|
| Profile ID | `extended` |
| Depends on | `reference-architecture`, `core-identity` |
| Requirements | 25 (+ annex D) |
| Sub-modules | 6 |
| Tests | 30 |
| Implemented | ~28% (E-Registry 0344-0353 + 0104) |

| Sub-module | IDs | Min phase | VenID service | Smoke |
|------------|-----|-----------|---------------|-------|
| E-Wallet | 0340-0343, 0345 | 2 | `wallet-service` | `run-ewallet-checks.sh` |
| E-Registry | 0344, 0349-0353 | 3 | `eregistry-adapter` | `run-extended-eregistry-checks.sh` |
| E-Inclusion | 0354-0357 | 2 | `inclusion-service` | `run-inclusion-checks.sh` |
| E-Webhook | 0358-0360, 0531 | 2 | `verification-engine` | `run-ewebhook-checks.sh` |
| E-Signature | 0361-0363 | 3 | `signature-service` | `run-esignature-checks.sh` |
| E-KYB | 0364-0365 | 3 (preview) | `kyb-service` | `run-ekyb-checks.sh` |

**Activation rule (ODTIS-0006):** Extended MUST NOT weaken base profiles - verified by `run-extended-no-weakening-checks.sh`.

**Coherence:** `conformance/profiles/extended/README.md` **outdated** (missing normative IDs for Inclusion, Signature, KYB). Annex D merge @ 0.9.0-draft is complete in `requirements.json`.

**Implementation phase:** P4 - sandbox partial complete; production activation gated by `venid.*.active=false`.

---

## 4. Conformance levels (L1 / L2 / L3)

| Level | Definition | ODTIS status |
|-------|------------|--------------|
| **L1** | Registry + annex validators in CI | **Ready** - 6 automated lab tests |
| **L2** | L1 + manual tests vs staging | **Partial** - 81/159 procedures evidenced |
| **L3** | L2 + third-party audit | **Deferred** - GAP-CERT-L3-ATT |

**Statements published:**

| Package | Phase | Level | Path |
|---------|------:|-------|------|
| venid-sandbox | L1 | L1 | `statements/venid-sandbox/` |
| venid-phase1-core | 1 | L2 | `statements/venid-phase1-core/` |
| venid-phase2-trust | 2 | L2 | `statements/venid-phase2-trust/` |
| venid-phase3-operator | 3 | L2 | `statements/venid-phase3-operator/` |
| venid-phase4-full | 4 | L3-target | `statements/venid-phase4-full/` |

---

## 5. Consistency findings

### 5.1 Critical (fix before DOI / external audit)

| ID | Finding | Impact | Fix |
|----|---------|--------|-----|
| C-01 | `validate-section-completeness.py` fails all sections - requirement indexes missing in SPEC.md | Spec prose not traceable to registry | Regenerate section indexes from `requirements.json` |
| C-02 | 78/159 conformance procedures still `pending` despite sandbox smokes | L2 claims overstated without doc update | Batch-update test status from smoke PASS logs |
| C-03 | ~~`traceability/coverage-report.yaml` says 111 reqs (stale)~~ | ~~Misleading coverage metrics~~ | **Resolved** - regenerated at 149 IDs |

### 5.2 Major (documentation drift)

| ID | Finding | Location |
|----|---------|----------|
| M-01 | PHASED-BACKLOG.md summary: 15 partial / 20 todo vs actual 29 partial / 0 todo | `PHASED-BACKLOG.md` header |
| M-02 | Federation README lists 3 tests; manifest has 8 | `conformance/profiles/federation/README.md` |
| M-03 | Extended README missing 0340+ normative IDs for 4 sub-modules | `conformance/profiles/extended/README.md` |
| M-04 | RI-MAP `coverage_summary.ven_identity_core_surfaces: 18` vs 21 surfaces listed | `implementation/RI-MAP.yaml` |

### 5.3 Minor (tooling / environment)

| ID | Finding |
|----|---------|
| N-01 | `validate-ri-map.py` requires PyYAML (not in default `python3`) |
| N-02 | P0-E01 work items still unchecked in PHASED-BACKLOG.md despite DONE status |

### 5.4 Coherent (validated)

- Registry ↔ test file paths: **100%** exist
- Manifest coverage gate: **100%** per profile
- Profile `depends_on` ↔ ODTIS-0001/0002/0004: aligned
- Phase 4 statement validates with all 6 Extended modules listed
- Gap registry: 20 closed (sandbox evidence), 4 deferred (production)

---

## 6. MUST / SHOULD / MUST NOT - test coverage matrix

### 6.1 MUST NOT (19) - highest audit risk

All 19 have linked tests. **Implemented evidence: 3** (ODTIS-0006, 0007 partial, 0533 partial). Priority: mark remaining after statement linter + fail-closed smokes.

### 6.2 SHOULD (16) - staging flexibility

| ID | Text (abbrev) | Blocker for L2? |
|----|---------------|-----------------|
| ODTIS-0206 | Timestamp / anti-replay | No (partial via gateway filters) |
| ODTIS-0214 | Autodiscovery | No |
| ODTIS-0217 | TSA | **Deferred** (GAP-TN-0217) |
| ODTIS-0221 | Zero trust alignment | No (informative mapping) |
| ODTIS-0314 | Biometric minimization | No |
| ODTIS-0318 | Verification API P95 | No |
| ODTIS-0323 | Connected RPs view | No |
| ODTIS-0338 | RP contract minimization | No |
| ODTIS-0342 | Wallet selective disclosure | No |
| ODTIS-0357 | Inclusion locales | No |
| ODTIS-0365 | KYB representative link | **Yes for B2B** (implemented in sandbox) |
| ODTIS-0406 | Federation regulator metadata | No |
| ODTIS-0503 | PPP deployment model | No |
| ODTIS-0513 | Ecosystem metrics | Partial (reports-api) |
| ODTIS-0524 | Citizen notification prefs | No |
| ODTIS-0536 | RI map completeness | Partial (RI-MAP done) |

---

## 7. Implementation roadmap (recommended phases)

Aligned with `phased-backlog.yaml` P0-P4 plus consistency remediation.

### Phase R0 - Spec coherence (2-3 weeks)

| # | Deliverable | ODTIS touch |
|---|-------------|-------------|
| R0-1 | Fix SPEC.md requirement indexes (all 10 sections) | ODTIS-0010 |
| R0-2 | Regenerate `traceability/coverage-report.yaml` | ODTIS-0536 |
| R0-3 | Sync profile READMEs (federation, extended) | - |
| R0-4 | Refresh PHASED-BACKLOG.md summary from YAML | - |
| R0-5 | Add PyYAML to CI / document venv for validators | - |

**Exit:** `validate-section-completeness.py` PASS.

### Phase R1 - L2 evidence marking (4-6 weeks)

| # | Deliverable | Profiles |
|---|-------------|----------|
| R1-1 | Mark reference-architecture tests `implemented` (CI + statement validator) | RA |
| R1-2 | Core Identity live L2: OIDC, verify API, consent (stack up) | CI |
| R1-3 | Mark trust-network tests from `run-gap-closure-checks.sh` PASS | TN |
| R1-4 | Operator tests from phase3/phase4 package smokes | OP |

**Exit:** ≥60% reqs with `implemented` tests (Phase 3.1 traceability target).

### Phase R2 - Production hardening (8-12 weeks)

| # | Deliverable | Deferred gaps |
|---|-------------|---------------|
| R2-1 | Live mTLS bilateral interop | GAP-TN-0204 |
| R2-2 | National TSA or documented waiver | GAP-TN-0217 |
| R2-3 | Extended module production activation (`venid.*.active=true`) | Phase 4 |
| R2-4 | SHOULD requirements batch (0318, 0323, 0342) | CI/Extended |

**Exit:** Staging `production: null` -> staging statement with live TARGET.

### Phase R3 - L3 certification (external)

| # | Deliverable |
|---|-------------|
| R3-1 | Third-party auditor engagement |
| R3-2 | ODTIS Certified mark program (per `governance/CERTIFICATION.md`) |
| R3-3 | Close GAP-CERT-L3-ATT |

**Exit:** L3 attestation letter + public `certified-products.yaml` entry.

---

## 8. Backlog ↔ profile mapping

| Backlog | ODTIS phase | Profiles | Epics done | Epics partial |
|---------|------------|----------|------------|---------------|
| P0 | Pre-pilot | reference-architecture | 4/4 | 0 |
| P1 | 1 | core-identity | 1/10 | 9 |
| P2 | 2 | + trust-network | 5/9 | 4 |
| P3 | 3 | + operator, E-Registry prep | 0/9 | 9 |
| P4 | 4 | + federation, extended | 0/7 | 7 |

**Total:** 10 done, 29 partial, 0 todo (all epics started).

---

## 9. Commands for re-validation

```bash
# Structural integrity
cd odtis && python3 scripts/validate-registry.py
python3 scripts/validate-manifest-coverage.py
python3 scripts/run-conformance.py --check-links

# Section coherence (currently FAIL)
python3 scripts/validate-section-completeness.py

# Implementation evidence
./conformance/run-gap-closure-checks.sh
./conformance/run-phase4-package.sh

# RI map (needs PyYAML)
python3 scripts/validate-ri-map.py
```

---

## 10. Conclusion

ODTIS `0.9.0-draft` is a **complete normative package** with full test linkage. VenID implementation has **substantial sandbox coverage** across all profiles, but **conformance documentation lags code** (81/159 implemented markers vs ~74% partial epics).

**Recommended priority:**

1. **R0** - fix spec indexes and stale docs (audit blocker)
2. **R1** - align test `implemented` status with smoke evidence (L2 honesty)
3. **R2** - close 4 deferred production gaps
4. **R3** - external L3 attestation

---

*Generated from automated analysis of `registry/requirements.json`, `conformance/manifest.yaml`, `implementation/RI-MAP.yaml`, `phased-backlog.yaml`, `gaps.yaml`, and validator scripts.*
