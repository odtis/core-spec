# Annex C - Standards mapping

| Field | Value |
|-------|-------|
| **Status** | review draft - Phase 3.2 |
| **Spec version** | 0.9.0-draft |
| **Source** | P18 4-9, normativa-estandares-referencia.md |
| **Format** | YAML |
| **Nature** | **Informative** - aids interoperability; does not assert EU/US certification |

**Annexes hub:** [Project hub](../README.md) | **Spec index:** [Specification index](../../spec/INDEX.md) | **Requirements:** [Requirements index](/site/REQUIREMENTS-INDEX/)

---

## Purpose

Annex C maps each ODTIS requirement to **external standards and frameworks** with a **coverage level**:

| Level | Meaning |
|-------|---------|
| `full` | ODTIS implements the cited construct without material gaps |
| `partial` | ODTIS subset; operator policy completes the standard |
| `informative` | Design alignment or disclosure aid only |
| `platform` | VenID operator/deployment rule without direct external clause |

ODTIS normative text remains in 1-10. This annex supports cross-border adopters, auditors, and EUDI program architects.

**Disclaimer:** ODTIS does **not** assert eIDAS qualified status, NIST certification, or ISO 27001 conformity through this mapping alone.

---

## Files

```
C-standards-mapping/
├── README.md
├── standards.yaml <- Catalog of ~20 external standards
├── loa-matrix.yaml <- NIST IAL/AAL/FAL + eIDAS-inspired crosswalk
└── mapping.yaml <- 149/149 ODTIS IDs -> standard clauses
```

---

## Standards catalog (summary)

| Domain | Standards |
|--------|-----------|
| Federation | OAuth 2.0, OIDC Core/Discovery, PKCE, JWT |
| Assurance | NIST SP 800-63-3, eIDAS (informative) |
| Exchange | X-Road security architecture |
| Wallet | OID4VP, OID4VCI, SD-JWT, EUDI ARF (informative) |
| Security | NIST SP 800-207, OWASP, TLS 1.2+ |
| PKI | RFC 5280 / CP-CPS patterns |
| Privacy | GDPR principles (informative; adopter legal layer) |
| Operator | ISO 27001 targets (informative), VenID platform model |

Full list: [Standards catalog](standards.yaml).

---

## LoA crosswalk

P18 4.3-4.4 tables live in [LoA crosswalk matrix](loa-matrix.yaml):

- **VenID LoA -> NIST IAL/AAL** (Low through National)
- **eIDAS / EUDI concepts -> ODTIS constructs** (informative)
- **Three enforcement points** (proofing, OIDC/API, gateway)

Operator documentation **MUST** publish NIST mapping per **ODTIS-0105**.

---

## Requirement coverage

[Standards mapping](mapping.yaml) lists all **149** registry requirements. Example:

```yaml
ODTIS-0302:
- standard_id: STD-OAUTH2
clause: "Authorization Code grant"
reference: "RFC 6749 4.1"
coverage: full
- standard_id: STD-PKCE
clause: "Public client code exchange"
reference: "RFC 7636"
coverage: full
```

Regenerate after registry changes:

```bash
python3 ../../scripts/generate-standards-mapping.py
```

---

## Validation

```bash
python3 ../../scripts/validate-standards-mapping.py
```

Checks: all registry IDs mapped, valid `standard_id`, valid coverage enum.

---

## Profile alignment (informative)

| Profile | Primary standards |
|---------|-------------------|
| Core Identity | OAuth/OIDC, NIST 800-63, TLS, OWASP |
| Trust Network | X-Road, mTLS, PKI RFC 5280, NIST 800-207 |
| Extended E-Wallet | OID4VP/VCI, SD-JWT, EUDI ARF |
| Operator | ISO 27001 roadmap, platform governance (P10) |

---

## Maintenance

| Trigger | Action |
|---------|--------|
| ODTIS registry adds/changes IDs | Update `generate-standards-mapping.py` + regenerate |
| eIDAS 2.0 / OID4VC spec updates | Review `loa-matrix.yaml` and EUDI rows (P18 10) |
| New external standard adopted | Add to `standards.yaml` + mapping entries |

---

## Checklist

- [x] Standards catalog (`standards.yaml`)
- [x] LoA / eIDAS crosswalk (`loa-matrix.yaml`)
- [x] 149/149 requirement mappings (`mapping.yaml`)
- [x] Generate + validate scripts
- [ ] Sync detailed rows with P02 comparative paper
- [ ] Periodic review when eIDAS 2.0 / OID4VC specs evolve

**Phase 3.2 review (C).**

- [x] 149/149 registry IDs mapped and validated
- [x] LoA / eIDAS crosswalk in `loa-matrix.yaml`
- [ ] External review cycle 1 ([Section review matrix](/governance/SECTION-REVIEW/))

---

## References

- P18 - *Standards Alignment and ODTIS*
- P02 - Comparative international models
- P03 - eIDAS 2.0 / SSI alignment
- [Normativa Estandares Referencia](https://github.com/finnectos/venezuela/blob/main/docs/sources/product/analisis/normativa-estandares-referencia.md)
