# Annex B - Threat mitigations

| Field | Value |
|-------|-------|
| **Status** | review draft - Phase 3.2 |
| **Spec version** | 0.9.0-draft |
| **Source** | P07 mitigation matrix (Table 1), threat categories (4) |
| **Format** | YAML (`threats.yaml`) |
| **Normative controls** | ODTIS 5, 8, and related sections - this annex is **informative** |

**Annexes hub:** [Project hub](../README.md) | **Spec index:** [Specification index](../../spec/INDEX.md) | **Security section:** [Section 8 - Security](../../spec/08-security/SPEC.md)

---

## Purpose

Annex B maps the **P07 threat landscape** to ODTIS normative requirements. Auditors and operators use it to:

1. Trace each high-impact risk to concrete ODTIS controls.
2. Verify every **ODTIS-8.x** requirement mitigates at least one documented threat.
3. Scope conformance claims by profile (Core Identity, Trust Network, Extended, Operator).

Normative language remains in 8 and cross-referenced sections. Annex B does not introduce new MUST/SHOULD requirements.

---

## Files

| File | Description |
|------|-------------|
| [Threat mitigations catalog](threats.yaml) | 18-row P07 matrix + STRIDE + ODTIS requirement cross-refs |
| [Project hub](README.md) | This document |

---

## Threat taxonomy

Seven **threat classes** (derived from P07 4-7 and Figure 5):

| Class ID | Name | P07 reference |
|----------|------|---------------|
| TC-REG | Registration and proofing | 4.1, 4.3 |
| TC-ATO | Account takeover and session abuse | 4.2, 4.4 |
| TC-RP | Malicious or compromised RPs | 4.5 |
| TC-TRUST | Unauthorized issuers and trust partners | 4.6 |
| TC-WALLET | Wallet and VC abuse | 7 |
| TC-PRIV | Privacy and data abuse | 4.7 |
| TC-INFRA | Platform intrusion and data breach | Table 1 rows 12-13, P06 |

Each threat row uses ID **`T-P07-{NNN}`** aligned with P07 Table 1 row number.

---

## ODTIS-8.x coverage

All nine 8 requirements appear in `odtis_8_coverage` inside `threats.yaml`:

| Requirement | Primary threats |
|-------------|-----------------|
| ODTIS-0517 | T-P07-008, 012, 016 |
| ODTIS-0518 | T-P07-012, 013 |
| ODTIS-0519 | T-P07-012 |
| ODTIS-0520 | T-P07-012 |
| ODTIS-0521 | T-P07-002, 007, 012 |
| ODTIS-0522 | T-P07-002, 007, 010, 012, 014 |
| ODTIS-0523 | T-P07-001, 005 |
| ODTIS-0524 | T-P07-011, 014 |
| ODTIS-0525 | T-P07-001, 004, 006, 014 |

---

## Validation

```bash
python3 ../../scripts/validate-threats.py
```

Requires Python 3 only (no external packages).

---

## Profile applicability

| Profile | Relevant threat rows |
|---------|---------------------|
| Core Identity | T-P07-001 - 007, 009, 013 - 015, 017 - 018 |
| Trust Network | T-P07-008, 011, 012, 016 |
| Extended (E-Wallet) | T-P07-010, 011, 014, 017 |
| Operator | All rows (governance, fraud metrics, infra) |

---

## Checklist

- [x] Export P07 Table 1 (18 rows) to `threats.yaml`
- [x] Link each ODTIS-8.x to ≥1 threat row
- [x] Validation script
- [ ] Review with security white paper (O-1, Phase 2.9)
- [x] Red-team scenario appendix - [Red team scenarios](red-team-scenarios.md)

**Phase 3.2 review (B).**

- [x] 18 threats + ODTIS-8.x coverage validated
- [x] Cross-ref section 8.4 informative sample
- [ ] External review cycle 1 ([Section review matrix](/governance/SECTION-REVIEW/))

---

## References

- P07 - *Threat Modeling for Reusable Identity*
- P18 9.2 - ODTIS-8.x normative requirements
- ODTIS 8 - Security requirements
