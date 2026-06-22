# Book 1 decision domains (informative)

Maps **Book 1** policy decision domains (D1-D10) to ODTIS profiles, sections, and key requirement IDs.

**Nature:** informative bridge from narrative policy (Book 1) to normative ODTIS. Does **not** add new MUST requirements.

**Machine-readable:** [Book 1 domain map (YAML)](book1-domains.yaml) | **Project hub:** [Project hub](../project/README.md) | **Profiles:** [Profile comparison](../site/PROFILES.md)

---

## At a glance

| Item | Value |
|------|-------|
| **Domains** | D1-D10 |
| **Profiles covered** | All 6 conformance profiles |
| **Source** | Book 1 narrative policy; cross-ref ODTIS spec |
| **Used by** | Profile docs, phased backlog, site generators |

Regenerate profile depth: `python3 scripts/generate-profile-docs.py`

---

## Domain matrix

| ID | Title | Profiles | ODTIS sections | Key IDs |
|----|-------|----------|----------------|---------|
| **D1** | Institutional mandate and sponsor accountability | reference-architecture, operator | 1, 7 | ODTIS-0001, 0008, 0532, 0534, 0536 |
| **D2** | Subject-centric assurance and LoA lifecycle | core-identity | 2, 3 | ODTIS-0101-0103, 0107, 0108, 0306 |
| **D3** | Trust hub and exchange gateway routing | trust-network | 4 | ODTIS-0201, 0202, 0212, 0223 |
| **D4** | Metadata-only exchange (no payload centralization) | trust-network | 4 | ODTIS-0224, 0225, 0226 |
| **D5** | Fail-closed security and denial paths | core-identity, trust-network, operator | 3, 4, 8 | ODTIS-0317, 0535, 0517 |
| **D6** | Extended module composition (no weakening) | extended, reference-architecture | 1, 5, 10 | ODTIS-0006, 0532, 0533 |
| **D7** | E-Registry and National LoA | extended, core-identity | 2, 5 | ODTIS-0104, 0344, 0350, 0352 |
| **D8** | E-Inclusion and assisted onboarding | extended | 5 | ODTIS-0354-0357 |
| **D9** | Federation bilateral agreements | federation | 6 | ODTIS-0401, 0403, 0405, 0407, 0408 |
| **D10** | Operator maturity and phase-appropriate claims | operator | 7-10 | ODTIS-0505, 0506, 0530, 0532 |

---

## Profile phase applicability

When a domain applies depends on deployment phase ([`ODTIS-0532`](../spec/10-deployment-profiles/SPEC.md)):

| Profile | Phases |
|---------|--------|
| reference-architecture | 0, 1, 2, 3, 4 |
| core-identity | 1, 2, 3, 4 |
| trust-network | 2, 3, 4 |
| federation | 3, 4 |
| operator | 1, 2, 3, 4 |
| extended | 2, 3, 4 |

Phase 0 = pre-claim / internal only. Phase 4 = full Extended sub-module declaration.

---

## How to use this map

| Audience | Use |
|----------|-----|
| **Policy authors (Book 1)** | Ensure narrative domains cite ODTIS IDs without contradicting MUSTs |
| **Implementers** | See which decision area a profile addresses before reading section prose |
| **Reviewers** | Trace FB items and RFCs back to D-domains |

Detailed profile packs: [Profile index](/spec/profiles/) (generated Book 1 tables per profile).

---

## Related

| Document | Purpose |
|----------|---------|
| [Project hub](README.md) | Requirements registry |
| [Book 2 cross-review](../governance/BOOK2-CROSS-REVIEW.md) | Book 2 alignment |
| [Documentation roadmap](../implementation/DOCUMENTATION-ROADMAP.md) | Site doc phases (R2) |
