# ODTIS section completeness review

**Version:** [Version](/VERSION) (`0.9.0-draft`) 
**Phase:** 3.2 - Review and stabilization 
**Automated check:** `python3 scripts/validate-section-completeness.py`

**Project hub:** [Project hub](../project/README.md) | **Annexes:** [Annex review matrix](ANNEX-REVIEW.md) | **Close checklist:** [Review close checklist](REVIEW-CYCLE-1-CLOSE.md)

---

## Completeness criteria (sections 2-10)

| # | Criterion | Meaning |
|---|-----------|---------|
| C1 | Header metadata | Status, version, derived-from, registry ID range |
| C2 | Scope subsection | Section X.1 defines boundaries |
| C3 | Normative prose | Every registry ID cited before requirement index |
| C4 | Requirement index | Table lists exactly the section's registry IDs |
| C5 | Conformance tests | Each ID has a stub path that exists on disk |
| C6 | Document history | Includes `0.9.0-draft` line |
| C7 | Phase 3.2 checklist | Review checklist in SPEC footer |

Section **1** is meta (profiles, levels, claims) and is reviewed separately below.

---

## Section status matrix

| Sec | Section | IDs | Prose | Index | Tests | Phase 3.2 | Depth notes |
|-----|---------|-----|-------|-------|-------|-----------|-------------|
| 1 | Scope & conformance | meta | ✅ | n/a | n/a | ✅ | Review cycle 1 close checklist linked |
| 2 | Terminology & LoA | 8 | ✅ | ✅ | ✅ | ✅ | LoA matrix + Annex C crosswalk |
| 3 | Identity services | 27 | ✅ | ✅ | ✅ | ✅ | Index caption 27 IDs; section 3.10 wallet informative |
| 4 | Trust network | 21 | ✅ | ✅ | ✅ | ✅ | FB-004 autodiscovery; ID numbering note |
| 5 | Consent & privacy | 16 | ✅ | ✅ | ✅ | ✅ | E-Wallet reqs in 5.4.x |
| 6 | Federation | 6 | ✅ | ✅ | ✅ | ✅ | FB-002 accepted (6.1.4-6.2.1) |
| 7 | Operator governance | 16 | ✅ | ✅ | ✅ | ✅ | ID numbering note; RF-27 / Book 2 cross-ref |
| 8 | Security | 9 | ✅ | ✅ | ✅ | ✅ | Annex B linked; 8.1.x / 8.2.x numbering note |
| 9 | Audit & events | 6 | ✅ | ✅ | ✅ | ✅ | Event catalog + schemas; ID order note |
| 10 | Deployment | 2 | ✅ | ✅ | ✅ | ✅ | FB-003 HA boundary; Annex D activation.yaml |

---

## Annexes A-D

See [Annex review matrix](ANNEX-REVIEW.md). All annex validators PASS at `0.9.0-draft` (run via `./conformance/run.sh`).

| Annex | Phase 3.2 | Validator |
|-------|-----------|-----------|
| A OpenAPI | ✅ frozen | `validate-openapi.py` |
| B Threats | ✅ | `validate-threats.py` |
| C Standards | ✅ 149/149 | `validate-standards-mapping.py` |
| D Extended | ✅ draft catalog | `validate-extended-annex.py` |

**Legend:** ✅ = criterion met for review draft | 🟡 = structurally complete but known depth gap

---

## Section 1 (meta) checklist

| Item | Status |
|------|--------|
| 1.1-1.18 prose | ✅ |
| Five profiles defined (1.6) | ✅ |
| L1/L2/L3 levels (1.8) | ✅ |
| Conformance claims rules (1.9) | ✅ |
| Book 2 hierarchy (1.12) | ✅ |
| Language policy (1.15) | ✅ |
| Security considerations (1.16) | ✅ |
| Normative + informative refs (1.17-1.18) | ✅ |
| External review cycle 1 open | 🟡 |

---

## Known depth gaps (not missing sections)

These are **content expansion** targets for review cycle 1 or post-1.0 RFCs, not absent files:

| Gap | Section | Tracker |
|-----|---------|---------|
| Federation interop depth | 6 | ✅ FB-002 accepted 2026-06-12 |
| HA metrics normative boundary | 10 | ✅ FB-003 clarification in 10.4 |
| Autodiscovery SHOULD scope | 4 | ✅ FB-004 clarification in section 4.4.3 + Annex A |
| Scope enforcement test traceability | 5 | ✅ FB-001 dedicated stub + spec note |
| L2 sandbox report workflow | sandbox | ✅ FB-005 template + README (live reports welcome) |
| Extended module IDs in main registry | Annex D | Annex D merge (Phase 4) |
| Notification service dedicated IDs | 3.9 | Optional - covered by 3.9.1-3.9.3 |
| Wallet/OID4VC | 3.10 + Annex D | Extended profile only |

---

## Review workflow

1. Run `python3 scripts/validate-section-completeness.py` (also runs in `./conformance/run.sh`).
2. For each section, read scope + requirement blocks + cross-references.
3. Log editorial fixes as GitHub **ODTIS clarification** issues.
4. Log new MUST/SHOULD as **ODTIS RFC** per [RFC template](RFC-TEMPLATE.md).
5. Update this matrix when a section closes Phase 3.2 review.

---

## Related

- [Annex review matrix](ANNEX-REVIEW.md)
- [Review close checklist](REVIEW-CYCLE-1-CLOSE.md)
- [External review cycle 1](REVIEW-CYCLE-1.md)
- [Specification index](../spec/INDEX.md)
- [Build plan](../PLAN-PHASES.md) Phase 3.2
