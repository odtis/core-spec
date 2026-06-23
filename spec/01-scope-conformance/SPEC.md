---
title: "Section 1: Scope and conformance"
description: Normative scope, adoptable profiles, conformance levels L1/L2/L3, and RFC 2119 keywords for ODTIS implementations.
---

# 1 Scope and conformance

<div class="odtis-spec-meta" markdown="1">

| Field | Value |
|-------|-------|
| **Status** | review draft - Phase 3.2 (Foundation track A) |
| **Spec version** | 0.9.0-draft |
| **Derived from** | P18 3, REPORTE 8.4 |
| **Registry IDs** | ODTIS-0001 - ODTIS-0010 (Reference Architecture); profiles in [Profile definitions](/registry/profiles.yaml) |

</div>

---

## Abstract

ODTIS (Open Digital Trust Infrastructure Specification) is a vendor-neutral open specification for interoperable digital trust infrastructure. It defines conformance profiles, normative requirements, machine-readable API contracts, and test procedures for Layer 1 identity services (OIDC-based Core Identity), Layer 2 institutional trust networks, bilateral operator federation, operator governance, and optional extended modules.

---

## Status of This Specification

This document is an **ODTIS review draft** (`0.9.0-draft`). It is **not** an IETF Internet-Draft or OpenID Foundation Final Specification.

| Item | Value |
|------|-------|
| **Maturity** | Review draft - see [Spec lifecycle stages](/governance/SPEC-STAGES/) |
| **Canonical language** | English ([Language policy](/governance/LANGUAGE/)) |
| **License** | [CC BY 4.0](../../LICENSE) |
| **Copyright** | FinnectOS, Inc. (interim; see [LICENSE](../../LICENSE)) |
| **Errata** | [Errata policy](/governance/ERRATA/) |
| **Feedback** | [Feedback channels](/governance/FEEDBACK/) - review cycle 1 open |
| **Citation** | [How to cite](../../publication/HOW-TO-CITE.md) |

Implementers MUST cite the exact ODTIS version in conformance statements (1.11).

---

## Authors and editors

| Role | Name | Affiliation |
|------|------|-------------|
| Lead editor | Manuel Mérida Oliveros | FinnectOS, Inc. |

Maintainers: [Maintainers](/governance/MAINTAINERS/).

---

## 1.1 Purpose

**ODTIS (Open Digital Trust Infrastructure Standard)** is the vendor-neutral specification for interoperable digital trust infrastructure. It normatively defines:

- identity lifecycle services for subjects and Relying Parties (Layer 1);
- trust network semantics for governed inter-institution exchange (Layer 2);
- consent and privacy rules;
- bilateral federation between operators;
- operator governance, security controls, auditability, and deployment profiles;
- optional extended capabilities declared by sub-module.

This document is the **authoritative normative source** for ODTIS conformance testing. Implementations MUST satisfy the requirements referenced by their declared profile(s) at a declared ODTIS version.

ODTIS enables reuse of verified identity across Relying Parties while governing institutional exchange under PKI, audit, and operator accountability. It is **jurisdiction-agnostic**: national law, civil-registry mandates, qualified trust service obligations, and data-residency rules are **adopter responsibilities** documented as external policy bindings, not as universal MUST clauses in this specification.

---

## 1.2 Scope

### 1.2.1 In scope

The following capabilities fall within ODTIS normative scope when a profile is declared:

| Domain | ODTIS section | Typical standards referent (informative) |
|--------|---------------|------------------------------------------|
| Terminology and Levels of Assurance | 2 | NIST SP 800-63-3 IAL/AAL |
| Core identity services | 3 | OAuth 2.0, OpenID Connect |
| Trust network semantics | 4 | X-Road-style exchange, mTLS |
| Consent and privacy | 5 | Purpose limitation, minimization |
| Federation | 6 | Bilateral, non-transitive federation |
| Operator governance | 7 | PKI ceremonies, accountability |
| Security requirements | 8 | Zero trust practice (NIST SP 800-207) |
| Audit and events | 9 | Tamper-evident audit trails |
| Deployment profiles | 10 | Phased rollout, HA, observability |
| Reliance Extensions (Capa B) | 11 | Relying-party governance overlays |
| Extended capabilities | Annex D | OID4VC wallet, webhooks, inclusion |

Informative mappings to eIDAS-inspired trust services, sector schemes, and national IdP programs appear in Annex C. Those mappings do not, by themselves, confer regulatory certification.

### 1.2.2 Out of scope

The following are **out of scope** for universal ODTIS MUST requirements:

| Topic | Treatment |
|-------|-----------|
| National legal transposition | Adopter annexes and Book 3 editions |
| EU qualified trust service provider (QTSP) conformity assessment | Adopter pursuit; not granted by ODTIS |
| Procurement, pricing, and commercial SLA terms | Book 3 and operator contracts |
| User interface design and branding | Informative (Book 2 Appendix G) |
| Hypothetical case studies (e.g., illustrative national agencies) | Informative examples only |

An implementation MAY document jurisdiction-specific bindings in a **policy binding statement** separate from its ODTIS conformance claim. Such bindings MUST NOT weaken ODTIS MUST requirements.

### 1.2.3 Architectural layers

ODTIS adopts the VenID two-layer model as normative partitioning:

| Layer | Name | ODTIS focus |
|-------|------|-------------|
| **Layer 1** | Identity Product | Subject lifecycle, IdP, consent, verification - Core Identity profile |
| **Layer 2** | Trust Network | Partner exchange, gateway, catalog, grants - Trust Network and Federation profiles |

Layer 1 MAY be implemented without Layer 2. Layer 2 MUST NOT be claimed without an underlying Core Identity deployment that satisfies the Core Identity profile for the same operator scope.

---

## 1.3 Normative and informative content

| Content type | Location | Role |
|--------------|----------|------|
| **Normative** | ODTIS 1-11 | MUST/SHOULD/MAY requirements |
| **Normative** | ODTIS requirement IDs (`ODTIS-x.x.x`) | Stable identifiers in [Requirements registry](/registry/requirements.json) |
| **Normative** | Conformance tests | [Conformance](/conformance/) procedures linked from registry |
| **Informative** | VenID papers P01-P18 | Design rationale and evidence |
| **Informative** | Book 2 (Volume II) | Integrated reference architecture |
| **Informative** | Annex B, Annex C | Threat mapping and standards crosswalk |
| **Informative** | Annex A (schema-only notes) | OpenAPI bundles are normative for API surface; prose in Annex A is informative unless cross-referenced by 3 MUST |
| **Non-normative** | Book 3 | Implementation, migration, and jurisdiction playbooks |

**Golden rule:** Every ODTIS MUST in sections 2-11 MUST have:

1. at least one informative trace reference (paper section, RF/RNF ID, or design-system artifact); and
2. a conformance test definition, which MAY be marked `pending` until the test suite matures.

After ODTIS v1.0 publication, informative papers MUST NOT override ODTIS normative text. Errata and amendments follow [Versioning policy](/governance/VERSIONING/).

---

## 1.4 Requirement keywords

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** in this specification are to be interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174) when, and only when, they appear in all capitals, as shown here.

| Keyword | Conformance meaning |
|---------|---------------------|
| **MUST** / **MUST NOT** | Mandatory for the declared profile(s). Violation means the implementation does not conform. |
| **SHOULD** / **SHOULD NOT** | Recommended. An implementation that deviates MUST document rationale in its operator policy or conformance statement. |
| **MAY** | Optional. Absence does not affect baseline profile conformance unless a SHOULD or MUST elsewhere requires the capability. |

Requirements apply **only** to the profile(s) and sub-modules an implementation declares. A requirement scoped to the Trust Network profile does not apply to a Core Identity-only deployment.

---

## 1.5 Document structure

| Section | Title | Requirement ID prefix |
|---------|-------|----------------------|
| 1 | Scope and conformance | `ODTIS-1.x` / `ODTIS-0001`..`0010` (Reference Architecture) |
| 2 | Terminology and LoA | `ODTIS-2.x` |
| 3 | Identity services | `ODTIS-3.x` |
| 4 | Trust network semantics | `ODTIS-4.x` |
| 5 | Consent and privacy | `ODTIS-5.x` |
| 6 | Federation | `ODTIS-6.x` |
| 7 | Operator governance | `ODTIS-7.x` |
| 8 | Security requirements | `ODTIS-8.x` |
| 9 | Audit and events | `ODTIS-9.x` |
| 10 | Deployment profiles | `ODTIS-10.x` |
| 11 | Reliance Extensions | `ODTIS-07xx` |

Annexes:

| Annex | Title |
|-------|-------|
| A | OpenAPI registry |
| B | Threat mitigations (informative mapping) |
| C | Standards mapping (informative) |
| D | Extended profiles and sub-modules |
| E | Reliance Extensions (Capa B catalog) |

The machine-readable index of all requirement IDs is [Requirements registry](/registry/requirements.json). Section coverage counts appear in [Section Coverage (YAML)](../../traceability/section-coverage.yaml).

---

## 1.6 Conformance profiles

ODTIS defines **seven** conformance profiles. An implementation **declares** which profiles it satisfies. Profile definitions in [Profile definitions](/registry/profiles.yaml) are authoritative for automation; this section states normative intent.

Every ODTIS claim MUST include the **Reference Architecture** profile (`reference-architecture`, domain `ODTIS-0000`).

### 1.6.0 Reference Architecture

**ID:** `reference-architecture`

**Domain:** `ODTIS-0000`

**Purpose.** Structural foundation: two-layer VenID partitioning (1.2.3), profile composition and dependency rules (1.7), version binding, and conformance statement structure (1.9). Book 2 reference architecture views are **informative**; this profile binds what implementers MUST declare and how layers compose.

**Depends on:** none (root profile).

**Mandatory sections:** 1.

**Requirement prefixes:** `ODTIS-0001`..`ODTIS-0010`.

**Typical implementers:** all ODTIS adopters; auditors reviewing conformance statements before functional profile tests.

### 1.6.1 Core Identity

**ID:** `core-identity`

**Purpose.** Reusable digital identity for subjects and Relying Parties: registration, proofing, Level of Assurance assignment, OAuth 2.0 / OpenID Connect federation, consent, verification API, and identity-related audit events.

**Depends on:** Reference Architecture (`reference-architecture`).

**Mandatory sections:** 2, 3, 5.

**Requirement prefixes:** `ODTIS-2.*`, `ODTIS-3.*`, `ODTIS-5.*`.

**Included (normative intent).**

| Included | Excluded from Core Identity-only |
|----------|--------------------------------|
| Subject identity lifecycle and LoA assignment | Bilateral trust-network federation |
| OIDC IdP, MFA, token issuance | Partner mTLS exchange gateway |
| Consent per RP and scope enforcement | Cross-network catalog federation |
| Verification API for Relying Parties | Wallet / OID4VC (Extended sub-module E-Wallet) |
| Citizen-facing self-service API | National LoA via civil registry (Extended sub-module E-Registry) |
| Audit events for identity and consent | Institutional message routing |

**Typical implementers:** national or sector IdP operators, enterprise identity platforms, verification service providers.

### 1.6.2 Trust Network

**ID:** `trust-network`

**Purpose.** Governed inter-institution exchange: partner registration, service catalog, exchange gateway, service grants, PKI-backed partner authentication, message signing, timestamping, and exchange audit events.

**Depends on:** Core Identity (`core-identity`).

**Mandatory sections:** 4.

**Requirement prefixes:** `ODTIS-4.*`.

**Included (normative intent).**

| Capability | Requires Core Identity |
|------------|------------------------|
| Exchange Gateway as sole mTLS entry for partner traffic | Yes |
| Partner certificates and revocation checking | Yes |
| Service-level grants | Yes |
| `@VenPartnerService` autodiscovery | Yes |
| Audit trail for exchange events | Yes |
| Operator console for network operations | Yes |

**Typical implementers:** trust network node operators, institutional exchange gateway vendors.

### 1.6.3 Federation

**ID:** `federation`

**Purpose.** Bilateral, **non-transitive** trust and verification across two operators or networks.

**Depends on:** Trust Network (`trust-network`).

**Mandatory sections:** 6.

**Requirement prefixes:** `ODTIS-6.*`.

Federation MUST NOT be claimed without Trust Network conformance for the same operational scope. Implicit trust propagation across three or more networks without explicit pairwise agreements is prohibited (see 6).

**Typical implementers:** cross-border or cross-sector network operators establishing pairwise federation agreements.

### 1.6.4 Operator

**ID:** `operator`

**Purpose.** Platform operator obligations: governance, PKI ceremony documentation, security baseline, audit retention, deployment and observability duties.

**Depends on:** Core Identity (`core-identity`). Does **not** require Trust Network.

**Mandatory sections:** 7, 8, 9, 10.

**Requirement prefixes:** `ODTIS-7.*`, `ODTIS-8.*`, `ODTIS-9.*`, `ODTIS-10.*`.

Production deployments that handle live subject data SHOULD declare the Operator profile in addition to Core Identity. Sandbox or laboratory deployments MAY omit Operator at conformance level L1 (see 1.8).

**Typical implementers:** Digital Trust Infrastructure operators, regulated trust service operators, platform SRE and security teams.

### 1.6.5 Extended

**ID:** `extended`

**Purpose.** Optional capabilities beyond Core Identity and Trust Network. Extended sub-modules are **declared independently** within this profile.

**Depends on:** Core Identity (`core-identity`). Trust Network is required only when a sub-module explicitly depends on exchange semantics.

**Normative annex:** Annex D.

**Sub-modules.**

| Sub-module ID | Description | Typical dependency |
|---------------|-------------|-------------------|
| `E-Wallet` | OID4VCI / OID4VP credentials | Core Identity |
| `E-Registry` | Civil-registry adapter; National LoA | Core Identity |
| `E-Inclusion` | Assisted registration; low-connectivity channels | Core Identity |
| `E-Webhook` | Relying Party callback notifications | Core Identity |
| `E-Signature` | Advanced electronic signature integration | Core Identity; may use Trust Network |
| `E-KYB` | Business verification extensions | Core Identity |

Extended sub-modules MUST NOT weaken Core Identity, Trust Network, or Federation requirements. They add declared capabilities and associated conformance tests only.

**Deployment phasing (informative).** E-Wallet commonly activates in deployment Phase 2+; E-Registry in Phase 3+. Exact phasing is operator policy documented under 10.

### 1.6.6 Reliance Extensions

**ID:** `reliance-extensions`

**Purpose.** Optional **Capa B** governance overlays: who may rely on a trust signal, for what purpose, with what assurance metadata, audit evidence, recourse, and revocation/step-up. Reliance Extensions operate on top of Core Identity and MUST NOT weaken Core, Trust Network, Federation, or Operator requirements (`ODTIS-0707`).

**Depends on:** Core Identity (`core-identity`).

**Normative annex:** Annex E.

**Mandatory section:** 11.

**Sub-modules** (declared in `reliance_extensions`; R-Base is always required when the profile is claimed):

| Sub-module ID | Description | Min phase |
|---------------|-------------|-----------|
| `R-Base` | Base reliance schema (relying party, purpose, assurance, audit, recourse) | 1 |
| `R-Agent-Authority` | AI agent mandate and delegation | 2 |
| `R-Crypto-Agility` | PQC / crypto-agility acceptance | 2 |
| `R-Document-Capture` | Document capture and injection reliance | 2 |
| `R-VC-Maturity-Gate` | External VC standard maturity gate | 1 |
| *(see Annex E)* | 12 additional sector overlays | 2-4 |

Phase matrix: [Annex E activation](/annexes/E-reliance-profiles/activation.yaml).

---

## 1.7 Profile composition rules

Implementations MUST obey the following composition rules:

1. **Declaration.** A conformance claim MUST list every profile, Extended sub-module, and Reliance Extension sub-module satisfied.
2. **Dependencies.** An implementation MUST NOT claim a profile unless all profiles listed in its `depends_on` chain are also claimed and satisfied.
3. **Cumulative capability.** Trust Network adds requirements to Core Identity; Federation adds requirements to Trust Network. Operator adds requirements to Core Identity independently of Layer 2.
4. **Minimal claim.** An implementation MAY claim only Core Identity. It MUST NOT imply Trust Network, Federation, Operator, or Extended conformance without explicit declaration.
5. **Version binding.** A conformance claim MUST name the ODTIS spec version (from [Version](../../VERSION)) against which requirements and tests were evaluated.

**Valid examples.**

| Claim | Valid? |
|-------|--------|
| Core Identity @ 0.9.0-draft | Yes |
| Core Identity + Operator @ 0.9.0-draft | Yes |
| Core Identity + Trust Network + Federation @ 0.9.0-draft | Yes |
| Trust Network without Core Identity | No |
| Federation without Trust Network | No |
| Extended E-Wallet on Core Identity only | Yes |
| Extended E-Registry declaring National LoA without E-Registry sub-module | No (see ODTIS-0344 in 2) |

Profile dependency graph:

```
reference-architecture
└── core-identity
 ├── trust-network
 │ └── federation
 ├── operator
 ├── extended (sub-modules declared separately)
 └── reliance-extensions (Capa B sub-modules in reliance_extensions)
```

---

## 1.8 Conformance levels

Within each declared profile, an implementation MUST declare a conformance **level**:

| Level | ID | Requirements |
|-------|-----|--------------|
| Laboratory | `L1` | Self-assessed; automated tests run in CI or sandbox; operator policy MAY be draft |
| Staging | `L2` | All mandatory tests for declared profiles pass; operator policy published; SHOULD requirements documented if waived |
| Production | `L3` | L2 plus third-party audit or regulator attestation (process defined in [Governance process](/governance/GOVERNANCE/) at ODTIS v1.0) |

Level L1 is sufficient for development and conformance lab work. Public production services handling live subjects SHOULD target L2 minimum. Regulated operators SHOULD target L3 when required by applicable law or contract.

---

## 1.9 Conformance claims

### 1.9.1 Conformance statement

An entity claiming ODTIS conformance MUST publish a **conformance statement** containing at minimum:

| Field | Description |
|-------|-------------|
| `odtis_version` | ODTIS spec version tested (e.g., `0.9.0-draft`) |
| `profiles` | List of profile IDs (1.6) |
| `extended_modules` | List of Extended sub-module IDs, if any |
| `reliance_extensions` | List of Reliance Extension sub-module IDs, if any (`ODTIS-0708`; include `R-Base` when profile claimed) |
| `level` | L1, L2, or L3 |
| `operator` | Legal entity responsible for the deployment |
| `scope` | Environment (sandbox, staging, production) and jurisdiction bindings |
| `requirements` | List of satisfied `ODTIS-x.x.x` IDs, or reference to generated report |
| `tests` | Test suite version and pass summary |
| `date` | Statement issue date |
| `contact` | Public contact for conformance inquiries |

Statements SHOULD be machine-readable (JSON or YAML) and human-readable (Markdown or PDF).

### 1.9.2 Conformance testing

An implementation MUST pass all automated tests in [Conformance](/conformance/) applicable to its declared profiles and level, when those tests exist for the declared ODTIS version.

Until the test suite reaches coverage for a profile, the implementation MUST:

1. document manual test procedures used; and
2. mark the conformance statement with `tests: partial` and list pending test IDs.

Missing tests do not waive MUST requirements; they indicate incomplete suite maturity for the current draft version.

### 1.9.3 Prohibited claims

The following claims are prohibited:

- "ODTIS certified" without a published conformance statement and passing tests for the declared version;
- "eIDAS compliant" or "QTSP equivalent" based solely on ODTIS conformance;
- "Full ODTIS" without listing every profile and sub-module satisfied;
- Implying Federation or Trust Network conformance when only Core Identity is declared.

---

## 1.9.4 Reference Architecture product requirements

Book 1 adoption gates and Libro 2 design rules bind conformance **claims**, not only runtime APIs. The following IDs extend ODTIS-0001..0006:

| ID | Keyword | Summary | Book 1 / project trace |
|----|---------|---------|------------------------|
| ODTIS-0007 | MUST NOT | Prohibited claims (no false ODTIS certified / Full ODTIS / eIDAS from ODTIS alone) | 1.9.3 |
| ODTIS-0008 | MUST | Conformance statement minimum fields | 1.9.1 |
| ODTIS-0009 | MUST NOT | No implied undeclared profiles | 1.7.4, D1 |
| ODTIS-0010 | MUST | Pass applicable tests or mark partial without waiving MUSTs | 1.9.2 |

Each ID has a conformance test under `conformance/tests/reference-architecture/`.

---

## 1.10 Traceability

ODTIS uses a four-layer traceability chain:

```
Informative source (paper , RF/RNF, design system)
↓
ODTIS normative ID (ODTIS-x.x.x)
↓
Spec section (2-10)
↓
Conformance test
```

**Identifier stability.** Requirement IDs MUST NOT be reused with conflicting meaning. Deprecated IDs MUST be marked in the registry and noted in [Changelog](../../CHANGELOG.md).

**Traceability artifacts.**

| Artifact | Location |
|----------|----------|
| Requirement registry | [Requirements registry](/registry/requirements.json) |
| RF index | [RF traceability index](../../traceability/rf-index.yaml) |
| Master matrix | [Traceability index](../../traceability/rf-index.yaml) |

Implementations are not required to publish internal traceability matrices. Conformance statements MUST reference ODTIS IDs, not paper sections alone.

---

## 1.11 Version identification

The normative ODTIS version is recorded in [Version](../../VERSION).

| Stage | Version pattern | Authority |
|-------|-----------------|-----------|
| Draft | `0.x.y-draft` | This repository; informative papers may lag |
| Standard | `1.0.0` | Frozen at Phase 4 after pilot validation |

Versioning rules: [Versioning policy](/governance/VERSIONING/).

Implementations MUST cite the exact ODTIS version in conformance statements. Mixed-version claims (satisfying 3 from one version and 4 from another) are not permitted unless explicitly allowed in a migration guide for a minor draft release.

---

## 1.12 Relationship to the VenID publication series

| Volume | Role | Normative? |
|--------|------|------------|
| **I - Vision** (Book 1) | Policy and market framing | Informative |
| **II - Architecture** (Book 2) | Reference Architecture monograph | Informative; MUST align with ODTIS |
| **III - Standard** (ODTIS) | This specification | **Normative** |
| **Implementation Guide** (Book 3) | Deployment and migration | Non-normative |

| Paper | Role after ODTIS v1.0 |
|-------|----------------------|
| **P18** | Academic bridge; citable alignment evidence; superseded for implementation by ODTIS |
| **P13, P14** | Informative detail for 3 and Annex A |
| **P01-P12** | Informative architecture and comparative evidence |

Book 3 and operator runbooks MUST NOT contradict ODTIS MUST requirements. Where operational practice appears to conflict, ODTIS text governs for conformance purposes; Book 3 MUST be updated or the deployment MUST not claim affected profiles.

Independent implementers SHOULD start at [Adoption guide](/ADOPTION/) for profile selection, verification, certification, and IETF track context.

---

## 1.13 Audiences

| Audience | Uses ODTIS for |
|----------|----------------|
| Standards bodies | Baseline for national or sector profile derivation |
| DTI operators | Operator duties, PKI, audit, deployment obligations |
| System integrators | Interoperable APIs and trust network behavior |
| Compliance officers | Mapping to NIST- and eIDAS-inspired controls |
| Open-source maintainers | Conformance tests for reference implementations |
| Researchers | Traceability from evidence papers to testable requirements |

---

## 1.14 Regulatory certification disclaimer

ODTIS conformance demonstrates satisfaction of **technical requirements** in this specification. It does **not**:

- grant EU qualified trust service provider status;
- substitute for national electronic identification scheme approval;
- certify legal adequacy under any specific statute; or
- replace contractual SLA or liability arrangements between operators and Relying Parties.

Adopters pursue regulatory certification through applicable authorities independently of ODTIS conformance claims.

---

## 1.15 Language

The **canonical language** of ODTIS is **English**.

All normative prose in sections 1-11, published annex README text, registry requirement strings, OpenAPI human-readable fields (`summary`, `description`), conformance test procedures, and governance documents in this repository MUST be authored in English.

Informative translations (for example, Book 1 Spanish edition or national implementation playbooks) MAY exist outside this repository. They MUST NOT be cited as alternate normative sources. Implementations MUST map jurisdiction-specific legal terms in **policy binding statements** separate from ODTIS conformance claims (see 1.2.2).

End-user consent screens and citizen portals MUST present purpose and attribute disclosure in **citizen-readable language** appropriate to the subject's locale (see 5); that obligation does not require the specification itself to be multilingual.

Repository policy: [Language policy](/governance/LANGUAGE/).

---

## 1.16 Security considerations

ODTIS security requirements are normatively distributed across section 8, identity and consent sections (3, 5), trust network transport (4), and operator PKI (7). Informative threat-to-control mapping appears in **Annex B**.

Implementers SHOULD review:

| Topic | Location |
|-------|----------|
| OIDC / PKCE / logout | 3.3, ODTIS-3.1.x |
| Verification API client auth | 3.5, ODTIS-0315 |
| Consent and scope leakage | 5, ODTIS-0331 |
| Gateway mTLS and grants | 4, ODTIS-4.x |
| Audit and retention | 9 |
| Red-team scenarios | Annex B appendix |

Extracted IETF security text for gateway and verify API: [Drafts](/ietf/drafts/).

---

## 1.17 Normative references

| Reference | Title |
|-----------|-------|
| RFC 2119 | Key words for use in RFCs |
| RFC 8174 | Ambiguity of RFC 2119 key words |
| RFC 6749 | OAuth 2.0 Authorization Framework |
| RFC 7636 | PKCE |
| OpenID Connect Core 1.0 | Authentication and claims |
| OpenID Connect Discovery 1.0 | Provider metadata |

Bindings and OpenID Foundation positioning: [OIDF positioning](/governance/liaison/OIDF-POSITIONING/).

Machine-readable ODTIS requirements: [Requirements registry](/registry/requirements.json).

---

## 1.18 Informative references

| Reference | Role |
|-----------|------|
| P18 | Academic alignment bridge |
| Book 2 | Reference architecture (informative) |
| Book 3 | Implementation guide (non-normative) |
| Annex C | Standards mapping (204/204 IDs) |
| NIST SP 800-63-3 | LoA mapping |
| X-Road documentation | Trust network informative model |

Index: [NIST and X-Road index](/governance/liaison/NIST-XROAD-INDEX/).

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| stub | 2026-06-12 | Scaffold Phase 3.0 |
| draft v0.5 | 2026-06-12 | 1.1-1.14 normative prose Phase 3.1 |
| draft v0.5 | 2026-06-13 | 1.15 Language (English canonical) |
| 0.9.0-draft | 2026-06-12 | Foundation track A: Abstract, Status, Security, References; publication/ + governance foundation |
| 0.9.0-draft | 2026-06-12 | Review cycle 1 open; steward FB-001..FB-005 accepted ([Review close checklist](/governance/REVIEW-CYCLE-1-CLOSE/)) |

**Phase 3.1 checklist (1).**

- [x] Redact 1.1-1.14 complete prose
- [x] Define L1/L2/L3 conformance levels (1.8)
- [x] Link profiles to registry and conformance paths (1.6-1.7)
- [x] Align with [Versioning policy](/governance/VERSIONING/) (1.11)


**Phase 3.2 review checklist (1).**

- [x] Profiles, conformance levels, and claims (1.6-1.9)
- [x] Document structure and publication hierarchy (1.5, 1.12)
- [x] Language, security, and references (1.15-1.18)
- [x] Steward-seeded review items triaged (FB-001..FB-005; [Review Log (YAML)](/governance/REVIEW-LOG.yaml))
- [ ] External review cycle 1 ([Section review matrix](/governance/SECTION-REVIEW/); close checklist [Review close checklist](/governance/REVIEW-CYCLE-1-CLOSE/))
