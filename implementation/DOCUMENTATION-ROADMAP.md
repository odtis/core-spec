# ODTIS documentation roadmap (project site)

Phased plan to **complete, complement, and finalize** documentation on the ODTIS MkDocs site ([odtis.org](https://odtis.org)). Normative authority stays in `spec/`; this roadmap adds traceability depth without a third normative layer.

**Project hub:** [Project hub](../project/README.md) | **Status:** [Project status](../site/STATUS.md)

**Model:** ODTIS SPEC = normative | Book 2 / RI bindings = informative | Conformance tests = executable evidence.

**Audit baseline:** [Consistency audit report](reports/ODTIS-CONSISTENCY-AUDIT-2026.md)

---

## Phase R0 - Spec section completeness (site gate)

**Goal:** `validate-section-completeness.py` PASS; requirement indexes synced to registry.

| Task | Status | Artifact |
|------|--------|----------|
| Fix index validator for ODTIS-MNNN IDs | done | `scripts/validate-section-completeness.py` |
| Align spec ID drift (0104, 0340-0343) | done | `spec/02-*`, `spec/05-*` |
| Generator: section requirement indexes | done | `scripts/generate-spec-section-indexes.py` |
| Wire into site build | done | `scripts/build-site.sh` |
| CI / local gate | done | run validator before `mkdocs build --strict` |

**Exit:** Sections 2-10: every registry ID cited in prose + index + test stub.

---

## Phase R1 - Conformance test status sync

**Goal:** Reflect smoke/L2 PASS in test `.md` `**Status:**` fields; refresh coverage report.

| Task | Status | Artifact |
|------|--------|----------|
| Batch-update `implemented` from smoke scripts | done | `scripts/sync-test-status-from-smokes.py` |
| Smoke-to-test map | done | `conformance/smoke-test-map.yaml` |
| Regenerate `traceability/coverage-report.yaml` (204 reqs) | done | `scripts/generate-coverage-report.py` |
| Update `site/STATUS.md` implementation % | done | generated metrics block |

**Exit:** Coverage report matches registry count (204); STATUS page shows implemented/pending split from smoke evidence.

Regenerate after smoke runs:

```bash
python3 scripts/sync-test-status-from-smokes.py --run
python3 scripts/generate-coverage-report.py
```

---

## Phase R2 - Profile packs (Book 1 depth)

**Goal:** Each conformance profile documents D-domains, phase matrix, and section scope on the site.

| Task | Status | Artifact |
|------|--------|----------|
| Book 1 D1-D10 matrix per profile | done | `registry/book1-domains.yaml` + `generate-profile-docs.py` |
| Annex D phase activation table | done | injected from `activation.yaml` / `sub-modules.yaml` |
| Sync profile READMEs (test counts) | done | `scripts/generate-profile-readmes.py` |
| `PHASED-BACKLOG.md` header counts | done | `scripts/generate-phased-backlog.py` (10 done / 29 partial / 0 todo) |

**Exit:** Each `*-profile.md` shows Book 1 domains + phase matrix; profile READMEs list all tests with implemented status; `PHASED-BACKLOG.md` summary matches epic state (10/29/0).

---

## Phase R3 - Component normative bindings

**Goal:** High-traffic RI surfaces have per-component binding pages.

| Task | Status | Artifact |
|------|--------|----------|
| Binding template + directory | done | `implementation/component-bindings/` |
| Site page generator | done | `scripts/generate-component-bindings-docs.py` |
| Binding validator | done | `scripts/validate-component-bindings.py` |
| Pilot bindings | done | verification-api, exchange-gateway |
| Phase 4 Extended bindings | done | wallet, inclusion, webhook, signature, kyb, eregistry |
| Federation runtime binding | done | `federation-runtime.yaml` |
| Cross-link `binding_doc` in RI-MAP | done | 10 surfaces |

**Exit:** Adopter navigates component -> ODTIS ID -> test -> evidence; RI-MAP `binding_doc` matches binding files.

```bash
python3 scripts/validate-component-bindings.py
python3 scripts/generate-component-bindings-docs.py
```

---

## Phase R4 - Production gaps & L3 certification docs

**Goal:** Close deferred gaps doc trail; L3 auditor package complete on site.

| Task | Status | Artifact |
|------|--------|----------|
| Track 4 deferred gaps (mTLS, TSA, TEP, L3 third-party) | done | `implementation/gaps/gaps.yaml` |
| Deferred resolution playbook | done | `implementation/gaps/DEFERRED-TRACK.md` |
| L3 certification package (site entry point) | done | `implementation/L3-CERTIFICATION-PACKAGE.md` |
| L3 audit checklist | done | `conformance/certification/L3-AUDIT-CHECKLIST.md` |
| Auditor guide + CERTIFICATION cross-links | done | `conformance/certification/auditor-guide.md`, `governance/CERTIFICATION.md` |
| Phase 4 full statement on site nav | done | `implementation/statements/venid-phase4-full/` |
| External review cycle 1 close | open | `governance/REVIEW-CYCLE-1-CLOSE.md` |

**Exit:** L3 auditor can run `run-phase4-package.sh` with site-only instructions.

```bash
./conformance/run-phase4-package.sh
# Review: implementation/L3-CERTIFICATION-PACKAGE.md
# Checklist: conformance/certification/L3-AUDIT-CHECKLIST.md
```

---

## Build commands

```bash
# Full site (generators + validators + mkdocs)
./scripts/build-site.sh

# Documentation gates only
python3 scripts/validate-section-completeness.py
python3 scripts/generate-spec-section-indexes.py
python3 scripts/generate-component-bindings-docs.py
python3 scripts/generate-profile-docs.py
```

---

## Navigation (MkDocs)

| Page | Phase |
|------|-------|
| `site/REQUIREMENTS-INDEX.md` | R0 |
| `site/COMPONENT-BINDINGS.md` | R3 |
| `site/PROFILES.md` | R2 |
| `implementation/DOCUMENTATION-ROADMAP.md` | meta (this file) |
| `implementation/L3-CERTIFICATION-PACKAGE.md` | R4 |
| `registry/BOOK1-DOMAINS.md` | R2 |
| `project/README.md` | Project hub (site UX) |
| `implementation/gaps/DEFERRED-TRACK.md` | R4 |
| `conformance/certification/L3-AUDIT-CHECKLIST.md` | R4 |

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-06-12 | R0 started; validator fix; component bindings pilot |
| 0.2 | 2026-06-15 | R4 complete: L3 package, deferred track, audit checklist |
