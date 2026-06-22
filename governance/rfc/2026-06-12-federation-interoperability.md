# RFC: Federation interoperability requirements (IG-02)

Steward draft for review cycle 1 (**FB-002**, accepted). Template: [RFC template](../RFC-TEMPLATE.md).

**Project hub:** [Project hub](/project/) | **I-D:** [Federation protocol draft](../../ietf/drafts/draft-odtis-federation-00.md)

---

## RFC metadata

| Field | Value |
|-------|-------|
| **Title** | Federation interoperability requirements |
| **Author** | ODTIS stewards |
| **Status** | accepted |
| **Created** | 2026-06-12 |
| **Review ID** | FB-002 |
| **ODTIS version** | 0.9.0-draft |
| **Profiles affected** | federation, trust-network |

---

## Summary

Expand ODTIS section 6 with interoperable federation agreement fields and gateway routing rules so bilateral federation is testable beyond the current three requirement IDs.

---

## Motivation

- **IG-02:** Book 2 ch.12 vs ODTIS-6.x depth gap
- Operators need normative fields for federation agreement exchange (instance ID, pinned CA, service whitelist)
- L2 cannot automate federation without concrete MUSTs on agreement validation and non-transitivity enforcement evidence

---

## Normative proposal

### New or changed requirements

| ID | Keyword | Proposed text |
|----|---------|---------------|
| ODTIS-0404 | MUST | Federation agreements MUST include remote instance identifier, validity window, and pinned remote trust material before outbound federated routing is enabled |
| ODTIS-0405 | MUST | Sender gateway MUST reject federated routes when direct bilateral agreement is absent, even if a transitive path exists through a third instance |
| ODTIS-0406 | SHOULD | Operators SHOULD publish federation agreement metadata to regulators via S8 export when Federation profile is claimed |

### Spec sections to edit

- `spec/06-federation/SPEC.md` - expand 6.2-6.4 with tables above
- `registry/requirements.json` - add IDs
- `conformance/tests/federation/` - extend `test_non_transitivity.md` + new agreement field stub

### Conformance

- Manual: agreement missing pinned CA -> routing denied
- L2: not feasible without second sandbox instance (Phase 4)

---

## Alternatives considered

| Option | Rejected because |
|--------|------------------|
| Defer all federation normative text to Phase 4 | Blocks Phase 3 sandbox federation prep (Book 3 C3 phase 2+) |
| Copy Book 2 ch.12 draft wholesale | Book 2 not stable; ODTIS must lead conformance |

---

## Backward compatibility

- `0.9.0-draft` implementers with Federation profile: add agreement fields; no Annex A breaking change
- Book 2 ch.12 updated informatively after RFC acceptance

---

## Review checklist

- [x] Traceability updated (TRACEABILITY-MATRIX / rf-index)
- [x] Annex C mapping row added
- [x] CHANGELOG [Unreleased]
- [x] No contradiction with Book 2 (or Book 2 updated informatively)

---

## Decision

| Date | Outcome | Notes |
|------|---------|-------|
| 2026-06-12 | **Accepted** | ODTIS-0404, ODTIS-0405, ODTIS-0406 merged into 0.9.0-draft |
| | | Comment period closes 2026-06-26 |
