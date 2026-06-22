# ODTIS specification stages

Aligned with OpenID Foundation draft -> Implementer's Draft -> Final, adapted for ODTIS pre-foundation releases.

**Current stage:** Review draft (`0.9.0-draft`) - see [Version](/VERSION) 
**Project status:** [Project status](../site/STATUS.md) | **Governance:** [Project hub](README.md)

---

## Stage definitions

| Stage | VERSION pattern | Meaning | Citation disclaimer |
|-------|-----------------|--------|---------------------|
| **Scaffold** | `0.1.0-draft` | Structure, registry extract | Not for implementation claims |
| **Working draft** | `0.5.x-draft` | Sections 1-10 prose in progress | Experimental |
| **Review draft** | `0.9.x-draft` | Feature-complete for external review | Working draft - cite version + DOI |
| **Stabilized draft** | `0.9.x` (no suffix) | Review closed; errata only | Pre-standard |
| **Standard** | `1.0.0` | Frozen after pilot validation (Phase 4) | Normative standard |

Suffix `-draft` indicates **mutable** text except where Annex A is explicitly frozen (see [Annex A freeze record](../annexes/A-openapi-registry/FREEZE.md)).

---

## Promotion criteria

### -> `0.9.x-draft` (stabilized)

- External review cycle closed ([Review Log (YAML)](REVIEW-LOG.yaml))
- No open MUST RFCs blocking release
- L1 validators PASS; L2 structural PASS
- Zenodo snapshot + DOI published

### -> `1.0.0`

See [Build plan](../PLAN-PHASES.md) Phase 4:

- Pilot metrics documented
- Conformance suite v1.0 operational
- Book 2 stable alignment
- Errata process live ([Errata policy](ERRATA.md))

---

## Immutability rules

| After release | Allowed changes |
|---------------|-----------------|
| Published `0.9.x-draft` snapshot | Errata clarifications; no silent MUST edits |
| `1.0.0` tag | Errata only in patch; new MUST in minor/major via RFC |

Published snapshots MUST NOT be overwritten. New versions supersede via CHANGELOG and optional *Obsoletes* notes.

---

## Related

- [Versioning policy](VERSIONING.md)
- [Errata policy](ERRATA.md)
- [Zenodo release checklist](../publication/zenodo/RELEASE-CHECKLIST.md)
