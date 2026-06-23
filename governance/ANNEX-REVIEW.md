# ODTIS annex completeness review

**Version:** [Version](/VERSION) (`0.9.0-draft`) 
**Phase:** 3.2 - Review and stabilization 
**Automated checks:** `./conformance/run.sh` (includes annex validators)

**Project hub:** [Project hub](../project/README.md) | **Sections:** [Section review matrix](SECTION-REVIEW.md)

Normative requirements remain in sections 1-11 and [Requirements registry](../registry/requirements.json). Annexes provide machine-readable bindings and informative crosswalks.

---

## Annex status matrix

| Annex | Title | Nature | Validator | Phase 3.2 | Notes |
|-------|-------|--------|-----------|-------------|-------|
| **A** | OpenAPI registry | Normative API binding | `validate-openapi.py` | ✅ frozen | 8 bundles; CHECKSUMS + FREEZE @ 0.9.0-draft |
| **B** | Threat mitigations | Informative | `validate-threats.py` | ✅ | 18 P07 rows + 6 reliance rows; all ODTIS-8.x covered |
| **C** | Standards mapping | Informative | `validate-standards-mapping.py` | ✅ | 204/204 registry IDs mapped |
| **D** | Extended profiles | Draft catalog | `validate-extended-annex.py` | ✅ | 6 sub-modules; 17 draft IDs (merge at v1.0) |
| **E** | Reliance Extensions | Normative Capa B | `validate-reliance-annex.py` | ✅ | 17 sub-modules; 55 normative IDs (ODTIS-0701-0772) |

**Legend:** ✅ = review draft complete for 0.9.0-draft

---

## Annex A (OpenAPI)

| Criterion | Status |
|-----------|--------|
| Core surfaces S2-S4, S8 in bundles | ✅ |
| Exchange gateway OpenAPI | ✅ |
| `INDEX.yaml` ODTIS cross-refs | ✅ |
| Shared `venid-common.openapi.yaml` | ✅ |
| Frozen @ 0.9.0-draft | ✅ [Annex A freeze record](../annexes/A-openapi-registry/FREEZE.md) |
| FB-004 autodiscovery out of scope | ✅ documented in README |
| Public spec site (`odtis.org`) | ✅ live |

---

## Annex B (Threats)

| Criterion | Status |
|-----------|--------|
| 18-row P07 matrix | ✅ |
| STRIDE + threat classes | ✅ |
| ODTIS-8.x coverage block | ✅ |
| Red-team scenarios appendix | ✅ |
| Cross-ref section 8.4 sample table | ✅ |
| External security paper sync (O-1) | 🟡 Phase 2.9 optional |

---

## Annex C (Standards)

| Criterion | Status |
|-----------|--------|
| `standards.yaml` catalog | ✅ 20 standards |
| `loa-matrix.yaml` NIST / eIDAS | ✅ |
| `mapping.yaml` full registry | ✅ 204/204 |
| Generate script | ✅ `generate-standards-mapping.py` |
| P02 detailed sync | 🟡 optional |
| eIDAS 2.0 / OID4VC periodic review | 🟡 ongoing |

---

## Annex D (Extended)

| Criterion | Status |
|-----------|--------|
| Six sub-modules in `sub-modules.yaml` | ✅ |
| Phase matrix `activation.yaml` | ✅ aligned with section 10 |
| Draft 5.5.x-5.9.x requirements | ✅ 17 IDs |
| Registry refs (5.4.x, 9.5.1, 10.1.x) | ✅ |
| Conformance stubs (`tests/extended/`) | ✅ 5 modules |
| Merge draft IDs to main registry | 🟡 Phase 4 / v1.0 |
| P17 / Book 3 sector profiles | 🟡 forthcoming |

---

## Annex E (Reliance Extensions)

| Criterion | Status |
|-----------|--------|
| Profile `reliance-extensions` in registry | ✅ |
| Seventeen sub-modules in `sub-modules.yaml` | ✅ |
| Tier / phase matrix `activation.yaml` | ✅ aligned with section 10 + 11 |
| Normative ODTIS-0701-0772 in registry | ✅ 55 IDs |
| R-Base field catalog `reliance-profiles.yaml` | ✅ |
| Conformance stubs (`tests/reliance-extensions/`) | ✅ 55 tests; static + policy smoke |
| `reliance_extensions` in conformance statement | ✅ P0 claimability |
| Annex C crosswalk for 07xx IDs | ✅ |

---

## Section 10-11 cross-links

| Section 10 topic | Annex |
|-----------|-------|
| Deployment phases 1-4 | D [Activation (YAML)](../annexes/D-extended-profiles/activation.yaml); E [Activation (YAML)](../annexes/E-reliance-profiles/activation.yaml) |
| Extended module declaration | D `sub-modules.yaml`; ODTIS-0532 |
| Reliance module declaration | E `sub-modules.yaml`; `reliance_extensions` field; section 11 |
| Phase 1 Extended prohibition | ODTIS-0533; D activation `extended_in_production: forbidden` |
| REST / verify API contracts | A OpenAPI bundles |
| Standards disclosure | C `loa-matrix.yaml`, `mapping.yaml` |
| Threat audit trail | B `threats.yaml` |

---

## Validation commands

```bash
# from repository root
python3 scripts/validate-openapi.py
python3 scripts/validate-threats.py
python3 scripts/validate-standards-mapping.py
python3 scripts/validate-extended-annex.py
python3 scripts/validate-reliance-annex.py
./conformance/run.sh
```

---

## Related

- [Section review matrix](SECTION-REVIEW.md) - Sections 1-11
- [Review close checklist](REVIEW-CYCLE-1-CLOSE.md) - External review close
- [Section 10 - Deployment](../spec/10-deployment-profiles/SPEC.md)
- [Annexes overview](../annexes/README.md)
