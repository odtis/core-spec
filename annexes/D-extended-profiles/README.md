# Annex D - Extended profiles

| Field | Value |
|-------|-------|
| **Status** | review draft - Phase 3.2 |
| **Spec version** | 0.9.0-draft |
| **Source** | P18 3.3.3, P03, P11, P14, P08, RF-EXT |
| **Profile** | `extended` (optional; depends on Core Identity) |
| **Normative hook** | ODTIS 1.6.5, 10; E-Wallet partial in 5.4 |

---

## Purpose

Annex D defines **optional Extended sub-modules** implementers MAY declare beyond Core Identity and Trust Network. Each sub-module adds capabilities and conformance tests without weakening base profile requirements.

P17 (forthcoming) and Book 3 will expand sector-specific profiles; this annex provides the **review-draft catalog** aligned with P18 at `0.9.0-draft`.

---

## Sub-modules

| ID | Description | Min phase | Normative status |
|----|-------------|-----------|----------------|
| **E-Wallet** | OID4VCI / OID4VP, SD-JWT | 2 | **Partial** - ODTIS-5.4.x in registry |
| **E-Registry** | Civil registry adapter; National LoA | 3 | Draft ODTIS-5.5.x |
| **E-Inclusion** | Assisted onboarding, representatives | 2 | Draft ODTIS-5.6.x |
| **E-Webhook** | RP callback notifications | 2 | ODTIS-0531 + draft 5.7.x |
| **E-Signature** | Advanced electronic signature | 3 | Draft ODTIS-5.8.x |
| **E-KYB** | Business entity verification | 3 | Preview ODTIS-5.9.x |

Full definitions: [Sub Modules (YAML)](sub-modules.yaml).

---

## Files

```
D-extended-profiles/
├── README.md
├── INDEX.yaml <- Module -> IDs -> tests
├── sub-modules.yaml <- Catalog + composition rules
├── activation.yaml <- Deployment phase matrix (10)
└── extended-requirements.yaml <- Draft 5.5.x-5.9.x + registry refs
```

---

## Requirement layers

| Layer | IDs | Location |
|-------|-----|----------|
| **In registry (normative @ 0.9.0-draft)** | ODTIS-0340-0348, 0524, 0344-0365, 0531 | `registry/requirements.json` |
| **Annex D catalog (informative mirror)** | Same IDs | `extended-requirements.yaml` |

Annex D draft IDs **0344**..**0365** merged into the main registry at **`0.9.0-draft`** for VenID product backlog and conformance tests.

---

## Declaration rules

1. Conformance statements **MUST** list active sub-modules (**ODTIS-0532**).
2. **Phase 1 production** MUST NOT claim inactive Extended modules (**ODTIS-0533**).
3. **National LoA** requires **E-Registry** (**ODTIS-0344**).
4. Extended modules MUST NOT weaken Core / Trust Network / Federation controls.

Phase matrix: [Activation (YAML)](activation.yaml) | 10 deployment spec.

---

## Cross-references

| Topic | Location |
|-------|----------|
| E-Wallet standards | Annex C (OID4VP, EUDI ARF) |
| E-Wallet threats | Annex B T-P07-010, 011 |
| Webhook OpenAPI | Annex A S3 `citizen-api` / verification-api `/v1/rp/webhooks` |
| LoA National | Annex C `loa-matrix.yaml` |
| Conformance tests | [Test procedures hub](/conformance/tests/) |

---

## Validation

```bash
python3 ../../scripts/validate-extended-annex.py
```

---

## Checklist

- [x] Six sub-modules catalogued (`sub-modules.yaml`)
- [x] Phase activation matrix (`activation.yaml`)
- [x] Draft requirements 5.5.x-5.9.x (`extended-requirements.yaml`)
- [x] INDEX + validation script
- [x] Conformance test stubs (5 modules)
- [ ] Merge draft IDs into registry at v1.0
- [ ] P17 / Book 3 sector profiles
- [x] Webhook paths in Annex A OpenAPI (`verification-api` `/v1/rp/webhooks`)

**Phase 3.2 review (D).**

- [x] `activation.yaml` aligned with section 10 deployment phases
- [x] Six sub-modules + 17 draft IDs validated
- [ ] Merge draft IDs into registry at v1.0 (Phase 4)
- [ ] External review cycle 1 ([Section review matrix](/governance/SECTION-REVIEW/))

---

## References

- P18 3.3.3 - Extended profile
- P03 - Wallet / OID4VC
- P11 - Registry adapter (E-Registry)
- P14 6.4 - RP webhooks
- ODTIS 1.6.5, 10
