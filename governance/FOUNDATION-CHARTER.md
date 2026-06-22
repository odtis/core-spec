# ODTIS Foundation charter (draft)

**Status:** pre-incorporation draft - legal entity TO-BE Phase C 
**Normative text remains in:** `spec/`, `registry/`, `annexes/`

**Project hub:** [Project hub](../project/README.md) | **Working groups:** [Working groups](working-groups/README.md)

---

## Mission

Maintain the **Open Digital Trust Infrastructure Specification (ODTIS)** as a vendor-neutral, implementable open standard for digital trust infrastructure: Core Identity, Trust Network, Federation, Operator governance, and Extended modules.

---

## Principles

1. **Normative clarity** - testable MUST/SHOULD with conformance suites
2. **Open license** - CC BY 4.0 for specification text
3. **Neutral stewardship** - multi-stakeholder editors beyond a single vendor
4. **Standards liaison** - complementary to IETF, OpenID Foundation, NIST practice
5. **No regulatory substitution** - ODTIS conformance ≠ national certification

---

## Structure (planned)

| Body | Role |
|------|------|
| **Board** | Strategy, budget, trademark |
| **Editors** | Normative releases ([Maintainers](MAINTAINERS.md)) |
| **Working Groups** | Domain drafts ([Working groups](working-groups/README.md)) |
| **Conformance program** | Certification policy ([Certification program](CERTIFICATION.md)) |

---

## Membership (TO-BE)

Membership applies when the **ODTIS Foundation** legal entity is incorporated (Phase C). Until then, participation flows through [Maintainers](MAINTAINERS.md), [Working groups](working-groups/README.md) (planned), [Feedback channels](FEEDBACK.md), and [Collaborate](/site/COLLABORATE/) - without fees or formal membership.

!!! info "Spec access is never gated"
    Normative ODTIS text, registry, Annex A OpenAPI, and conformance tests remain **CC BY 4.0** and publicly available. Membership funds stewardship, certification governance, and liaison - it does **not** license the specification.

### Purpose of membership

| Goal | How membership supports it |
|------|----------------------------|
| **Neutral stewardship** | Multi-stakeholder board beyond a single vendor |
| **Conformance program** | L3 auditor roster, trademark enforcement, dispute resolution |
| **Working groups** | Chairs, meeting infrastructure, liaison travel |
| **Ecosystem visibility** | Accurate implementer/operator listings on [odtis.org](https://odtis.org) |

### Membership categories (draft)

| Category | Who | Typical fee (TO-BE) | Primary benefit |
|----------|-----|---------------------|-----------------|
| **Individual / Academic** | Researchers, students, independent experts | Low or waived | WG participation, newsletter, review cycle voice |
| **Implementer** | Vendors, integrators, OSS maintainers shipping ODTIS-based products | Tiered annual | Listed implementer (with honest L2 evidence), WG nomination |
| **Operator** | DTI operators, national programs, regulated trust providers | Tiered annual | Operator council input, regulator sandbox coordination, certification program feedback |
| **Auditor / Lab** | Independent L3 auditors, test labs | Application + listing fee | Accredited auditor listing (after competency review) |
| **Founding member** | Charter signatories at incorporation | Founding contribution (one-time + annual) | Board seat or observer seat (charter cap TBD), founding recognition |

Exact fee schedules, caps, and currency are **TO-BE** board approval after incorporation. FinnectOS / VenID interim stewardship does not prejudge founding-member allocation.

### Rights (by category - draft)

All members in good standing MAY:

- participate in public review cycles and [Working groups](working-groups/README.md) subject to [Code of conduct](/site/CODE-OF-CONDUCT/);
- propose clarifications via [Feedback channels](FEEDBACK.md) and normative changes via [RFC template](RFC-TEMPLATE.md);
- use accurate **descriptive** references to ODTIS version and profiles in product and academic materials.

**Implementer** and **Operator** members MAY additionally (TO-BE policy):

- appear in the **implementer / operator directory** on [odtis.org](https://odtis.org) when a valid [conformance statement](/conformance/templates/conformance-statement.yaml) is published at declared level;
- nominate WG chairs and editors (subject to board confirmation);
- receive early notification of **release candidates** (public comment period remains open to all).

**Founding members** MAY additionally (TO-BE charter):

- elect or appoint initial **board** seats per bylaws;
- approve first-year budget, trademark policy, and certification program rules.

Membership alone does **not** grant **ODTIS Certified** mark use. That requires L3 attestation per [Certification program](CERTIFICATION.md) and [Trademark policy](TRADEMARK-POLICY.md).

### Obligations (all members)

1. **Accurate claims** - no "ODTIS certified" or equivalent without program evidence ([Trademark policy](TRADEMARK-POLICY.md)).
2. **IPR alignment** - sign Contribution / Membership Agreement consistent with [IPR policy](IPR-POLICY.md) (patent disclosure for normative contributions).
3. **Code of conduct** - [Code of conduct](/site/CODE-OF-CONDUCT/) at events, mailing lists, and WG meetings.
4. **Fees** - pay applicable dues; grace period and downgrade rules TO-BE bylaws.
5. **Conflicts** - disclose material conflicts when participating in editor or certification decisions.

### Non-members (public)

Non-members retain full access to:

- normative spec, registry, annexes, and downloads;
- L1/L2 self-certification tools and public conformance statement templates;
- GitHub issues, external review cycles, and public RFC comment periods.

Non-members do not vote on board matters or appear in member-only auditor/operator listings without meeting published listing criteria.

### Application process (TO-BE)

| Step | Action |
|------|--------|
| 1 | Submit application to **info@odtis.org** (category, organization, jurisdiction, intended profiles) |
| 2 | Accept Membership Agreement + IPR terms |
| 3 | For **Auditor / Lab**: competency review against [Auditor guide](/conformance/certification/auditor-guide/) |
| 4 | For **directory listing**: publish or link conformance statement at honest level |
| 5 | Board secretary records member in public register (name, category, jurisdiction - no commercial endorsement) |

### Founding member intake (pre-incorporation)

Until bylaws exist, interested organizations SHOULD contact [info@odtis.org](mailto:info@odtis.org?subject=ODTIS%20founding%20member%20interest) with:

- organization profile and ODTIS profile interest (Core Identity, Trust Network, Operator, ...);
- intended contribution (implementation, operator pilot, research, audit capability, liaison);
- conflict disclosures relevant to editor or certification roles.

A public **founding member prospectus** MAY be published before incorporation (TO-BE).

### Related documents (TO-BE at incorporation)

| Document | Purpose |
|----------|---------|
| Bylaws | Board powers, voting, quorum |
| Membership Agreement | Fees, termination, liability |
| Contributor License Agreement | Normative contributions (extends [IPR policy](IPR-POLICY.md)) |
| Certification program bylaws | L3 mark, auditor accreditation ([Certification program](CERTIFICATION.md)) |

---

## Succession

Until incorporation, **FinnectOS, Inc.** holds copyright, acts as interim specification steward, and publishes releases per [Maintainers](MAINTAINERS.md). VenID ([core-impl](https://github.com/odtis/core-impl)) is the reference implementation, not the specification copyright holder.

Upon ODTIS Foundation incorporation, FinnectOS, Inc. intends to **assign or license** specification copyright to the Foundation so stewardship and copyright align under a neutral multi-stakeholder body. Until then, contributions remain under [CC BY 4.0](../LICENSE) as described in [IPR policy](IPR-POLICY.md).

---

## Related

- [IPR policy](IPR-POLICY.md)
- [Spec lifecycle stages](SPEC-STAGES.md)
