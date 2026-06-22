---
title: "Section 2: Terminology and LoA"
description: Levels of assurance (LoA), NIST mapping, canonical claims, and terminology for ODTIS Core Identity.
---

# 2 Terminology and Levels of Assurance

<div class="odtis-spec-meta" markdown="1">

| Field | Value |
|-------|-------|
| **Status** | review draft - Phase 3.2 |
| **Spec version** | 0.9.0-draft |
| **Derived from** | P18 4, P01 3.4, P11, P13 |
| **Registry IDs** | ODTIS-0101 - ODTIS-0108 (8 requirements) |
| **Profiles** | Core Identity (2.3, 2.7); Trust Network (2.5); Operator (2.5 documentation) |

</div>

---

## 2.1 Normative definitions

Terms in this section apply across all ODTIS profiles unless a profile or requirement explicitly narrows scope. The machine-readable glossary is [Terminology registry](/registry/terminology.yaml). The site glossary index is [Glossary](/site/GLOSSARY/) (generated from the registry).

National legal terms (for example, *qualified electronic signature*, *qualified trust service provider*) are **out of scope** for universal ODTIS definitions. Adopters map them in jurisdiction annexes and policy binding statements (see 1.2.2).

### 2.1.1 Architecture and roles

**Digital Trust Infrastructure (DTI)**
Combined Layer 1 identity services and Layer 2 trust network operated under operator governance.

**Layer 1 (Identity Product)**
Citizen- and Relying-Party-facing identity lifecycle: registration, proofing, Level of Assurance assignment, IdP, consent, verification API, and identity-related audit events.

**Layer 2 (Trust Network)**
Institutional exchange among partners: registration, service catalog, exchange gateway, grants, PKI, message signing, timestamping, and exchange audit events.

**Subject**
Natural or legal person represented by a stable platform identifier (`subject_id`) whose identity is registered, proofed, and managed by a Core Identity implementation.

**Relying Party (RP)**
Application or organization registered with the operator that consumes identity assertions, verification results, or consented attributes from Core Identity services.

**DTI Operator (Operator)**
Entity responsible for operating Core Identity and, when declared, Trust Network services; publishing operator policy; maintaining PKI and audit obligations per declared profiles.

**Conformance profile**
Declared ODTIS capability set as defined in 1.6 and [Profile definitions](/registry/profiles.yaml).

### 2.1.2 Trust network terms

**Trust Network**
Set of operators and partners exchanging identity-related artifacts and institutional messages through normative gateway and catalog semantics (4).

**Exchange Gateway**
The sole mTLS entry point for partner exchange traffic on a trust network node. Partner traffic MUST NOT bypass the gateway (4).

**Partner**
Institution or service provider registered on the trust network with a partner identity distinct from subject identity.

**Service catalog**
Operator-maintained registry of catalogued services available for exchange under grant policy.

**Service grant**
Authorization binding a calling partner, a providing partner, and a catalogued service, with scope and validity conditions (4).

**Federation**
Bilateral, non-transitive trust arrangement between two operators or networks (6).

### 2.1.3 Assurance terms

**Level of Assurance (LoA)**
Platform-assigned ordinal measure of identity proof strength for a subject at a point in time. ODTIS defines **Low**, **Medium**, **High**, and **National**.

**Active LoA**
The single LoA currently assigned to a subject. A subject MUST have at most one active LoA at any time.

**Proofing**
Process of collecting and validating identity evidence before LoA assignment or upgrade.

**Operator policy**
Published document binding proofing criteria, LoA rules, retention, authentication requirements, and mappings required by this section. Operator policy MUST NOT contradict ODTIS MUST requirements.

**Identity Assurance Level (IAL)**
NIST SP 800-63-3 identity proofing assurance category [NIST-800-63-3]. Used for cross-border disclosure mapping (2.5).

**Authentication Assurance Level (AAL)**
NIST SP 800-63-3 authentication assurance category [NIST-800-63-3]. Used for cross-border disclosure mapping (2.5).

**Federation Assurance Level (FAL)**
NIST SP 800-63-3 federation assurance category [NIST-800-63-3]. Used for gateway-to-gateway exchange controls (2.5.2).

---

## 2.2 Levels of Assurance

### 2.2.1 LoA taxonomy

Every subject handled by a Core Identity implementation MUST be assignable to exactly one of the LoA levels in Table 2-1 at any time. **National** is available only under Extended sub-module **E-Registry** (1.6.5, ODTIS-0104; see also ODTIS-0344 in 5.7.1).

**Table 2-1 - VenID LoA levels**

| LoA | Name | Minimum proofing criteria | Typical use (informative) |
|-----|------|----------------------------|---------------------------|
| **Low** | Contact verified | Verified email and/or phone | Pre-registration, low-risk access |
| **Medium** | Document verified | Valid government-issued ID document plus contact verification | Marketplaces, employment, general KYC |
| **High** | Document and biometrics | Medium criteria plus liveness detection and facial match to document | Fintech, banking, enhanced KYC/AML |
| **National** | Registry verified | High LoA plus successful 1:1 match against authoritative civil registry via E-Registry adapter | Government services, high-value transactions |

Proofing criteria beyond Table 2-1 minima MAY be defined in operator policy provided they do not weaken ODTIS MUST requirements.

### 2.2.2 LoA assignment rules

1. LoA MUST reflect the **strongest level supported by validated evidence**, not requested level alone.
2. LoA upgrade MUST require successful proofing for the target level.
3. LoA downgrade MAY occur on evidence expiry, operator revocation, fraud detection, or subject request, per operator policy and RF-07/RF-08 traceability.
4. High LoA MUST NOT be assigned without biometric proofing (ODTIS-0103).
5. National LoA MUST NOT be assigned without E-Registry (ODTIS-0104).

### 2.2.3 LoA and Layer 2 separation

Citizen LoA governs Layer 1 identity assertions and verification responses. Trust Network partner authentication is governed independently by partner certificates, grants, and FAL controls (2.5.2, 4). **Citizen LoA MUST NOT be substituted for partner authentication on the exchange gateway.**

---

## 2.3 Core Identity LoA requirements

Requirements in this subsection apply to implementations claiming the **Core Identity** profile.

### ODTIS-0101 - Supported LoA levels

A Core Identity implementation **MUST** support LoA **Low**, **Medium**, and **High** with assignable criteria documented in operator policy.

Operator policy MUST specify, for each level:

- acceptable evidence types;
- validation steps;
- expiry and re-proofing rules; and
- authentication requirements for sessions at that LoA.

**Trace (informative):** RF-06
**Conformance test:** Submit proofing vectors for Low, Medium, and High; verify assigned LoA matches evidence per operator policy.

---

### ODTIS-0102 - Expose active LoA

A Core Identity implementation **MUST** expose the subject's **active LoA** to Relying Parties in:

1. **OIDC ID Token** and/or **UserInfo** via a claim named `assurance_level` (or equivalent registered claim documented in operator policy); and
2. **Verification API** responses (3.5).

The exposed value MUST use the canonical tokens `low`, `medium`, `high`, or `national` (lowercase ASCII). Implementations MAY expose additional informative metadata (for example, proofing timestamp) in separate claims.

**Trace (informative):** RF-06, RF-22
**Conformance test:** Complete OIDC login and verification API call; assert `assurance_level` present and matches subject record.

---

### ODTIS-0103 - High LoA biometric gate

A Core Identity implementation **MUST NOT** assign **High** LoA without **successful biometric proofing** per operator policy, including at minimum:

- liveness detection; and
- facial match between live capture and document portrait (or equivalent biometric binding defined in operator policy).

Document-only proofing MUST NOT produce High LoA.

**Trace (informative):** RF-03, RF-06
**Conformance test:** Attempt High assignment with document evidence only; MUST fail. Repeat with successful biometric proofing; MUST succeed.

---

### ODTIS-0104 - National LoA and E-Registry

**National** LoA **MUST** be claimed only when:

1. the implementation declares Extended sub-module **E-Registry**; and
2. registry adapter rules in operator policy are satisfied, including successful **1:1 match** against the configured authoritative civil registry (or equivalent national population register).

Implementations without E-Registry MUST NOT expose `national` as an assignable or reportable LoA.

**Trace (informative):** RF-EXT5, P11
**Conformance test:** Without E-Registry declared, registry lookup for `national` MUST be rejected. With E-Registry and valid registry match, National MAY be assigned.

---

## 2.4 LoA lifecycle

LoA lifecycle operations (upgrade, downgrade, suspension, manual review) MUST be auditable (9). The following behaviors are normative for Core Identity:

| Event | Normative behavior |
|-------|-------------------|
| Evidence expiry | Implementation SHOULD downgrade LoA or require re-proofing before attribute release |
| Fraud signal | Implementation MUST be able to suspend or downgrade LoA per operator policy |
| Subject dispute | Implementation MUST support operator review workflow without deleting audit history |
| Re-proofing success | Implementation MUST upgrade LoA when target proofing succeeds |

Detailed procedures are operator policy matters bound to RF-07 and RF-08 unless a MUST in 3 or 5 applies.

---

## 2.5 Cross-border and federation assurance mappings

!!! note "Requirement ID numbering"
    Cross-border mapping requirements use registry IDs **`ODTIS-2.4.x`** and **`ODTIS-2.5.x`**. Prose for **ODTIS-0105** and **ODTIS-0106** appears in this section (2.5); LoA enforcement IDs **ODTIS-0107** and **ODTIS-0108** appear in 2.7. Section **2.8** indexes all eight IDs.

### 2.5.1 NIST IAL/AAL mapping - ODTIS-0105

Operator documentation **MUST** map VenID LoA levels to **NIST SP 800-63-3** IAL and AAL equivalents used for cross-border disclosure.

**Table 2-2 - Default informative mapping (operator policy MUST document equivalents; MAY adopt this table)**

| VenID LoA | NIST IAL | NIST AAL | Notes |
|-----------|----------|----------|-------|
| Low | IAL1 | AAL1 | Contact verification only |
| Medium | IAL2 | AAL2 | Document verification; MFA-capable authentication |
| High | IAL2 or IAL3 | AAL2 or AAL3 | Document plus biometric proofing; strong authentication (MFA, passkeys) |
| National | IAL3 | AAL3 | High LoA plus registry 1:1 match (E-Registry) |

Operator policy MUST state which column values apply for each LoA in the operator's jurisdiction and disclosure contexts. Deviations from Table 2-2 MUST include documented rationale.

**Trace (informative):** P01 Section 3.4.1
**Conformance test:** Review published operator policy for IAL/AAL mapping table covering Low, Medium, High, and National (if E-Registry declared).

---

### 2.5.2 FAL controls - ODTIS-0106

Trust Network implementations **MUST** document **FAL controls** for gateway-to-gateway exchange, including at minimum:

| Control area | Documentation requirement |
|--------------|---------------------------|
| Transport | mTLS client and server authentication at Exchange Gateway |
| Message integrity | Signing and verification algorithms and key sources |
| Timestamping | Timestamp authority use and validation rules |
| PKI path validation | Partner certificate chain, CRL or OCSP policy |
| Grant enforcement | Binding of grant to caller identity and catalogued service |

FAL documentation MUST be published in operator policy or a trust network security annex referenced by the conformance statement.

Citizen LoA alone MUST NOT satisfy FAL requirements.

**Trace (informative):** P04, P08, NIST-800-63-3
**Conformance test:** Review Trust Network security documentation for FAL control table; verify gateway rejects unsigned or unauthenticated partner traffic in test harness.

---

## 2.6 eIDAS-inspired mapping (informative)

This subsection is **informative**. ODTIS does not assert EU qualified status. Table 2-3 aids EU-adjacent adopters and wallet program architects. Full mappings appear in Annex C.

**Table 2-3 - eIDAS / EUDI concept crosswalk (informative)**

| eIDAS / EUDI concept | VenID / ODTIS construct | Profile |
|----------------------|-------------------------|---------|
| LoA Substantial / High (national eID schemes) | Medium / High LoA | Core Identity |
| Person Identification Data (PID) | Verified subject attributes via OIDC or VC | Core / E-Wallet |
| Wallet Provider / PID Provider | Layer 1 IdP plus optional wallet issuer | Core / E-Wallet |
| Relying Party | Registered OAuth client and verification API consumer | Core Identity |
| Trust service provider duties | Operator plus PKI ceremonies | Trust Network, Operator |
| Qualified trust service (QTS) | Operator PKI and timestamping; national QTS is adopter legal layer | Operator |

---

## 2.7 LoA enforcement model

LoA is enforced at three points to prevent cross-layer confusion:

**Table 2-4 - Enforcement points**

| Point | What is checked | Layer |
|-------|-----------------|-------|
| **Proofing pipeline** | Evidence sufficiency before LoA assignment | Layer 1 |
| **OIDC / Verification API** | RP receives active LoA; RP policy allows or denies transaction | Layer 1 |
| **Exchange Gateway** | Partner certificate, grant, and FAL controls; citizen LoA not used as wire credential by default | Layer 2 |

### ODTIS-0107 - RP minimum LoA configuration

Relying Parties **MUST** be able to configure a **minimum LoA per OAuth client application** (or equivalent RP registration record).

When a subject's active LoA is below the configured minimum, Core Identity MUST:

- deny attribute release beyond what operator policy allows for the failed check; and
- return an explicit error or claim indicating insufficient assurance, without exposing restricted attributes.

**Trace (informative):** RF-06, RF-23
**Conformance test:** Configure client with `minimum_loa=high`; authenticate subject at Medium; verify denial or insufficient-assurance signal.

---

### ODTIS-0108 - Verification API LoA on denial

The Verification API **MUST** return the subject's **current active LoA** even when **attribute release is denied** (for example, consent withheld, scope insufficient, or minimum LoA not met).

Response MUST NOT omit LoA while returning a denial reason code.

**Trace (informative):** RF-22
**Conformance test:** Invoke verification with denied attribute release; assert `assurance_level` (or equivalent) present and correct.

---

## 2.8 LoA, proofing, and claims matrix

**Table 2-5 - Normative summary matrix**

| LoA | Min. proofing | Biometrics required | E-Registry required | Canonical claim value | Core Identity MUST support |
|-----|---------------|--------------------|--------------------|----------------------|---------------------------|
| Low | Contact | No | No | `low` | Yes |
| Medium | Document + contact | No | No | `medium` | Yes |
| High | Document + contact | Yes | No | `high` | Yes |
| National | Document + contact + registry 1:1 | Yes | Yes | `national` | Only with E-Registry |

---

## 2.9 Requirement index

<!-- GENERATED:section-index:START -->
<!-- Generated by scripts/generate-spec-section-indexes.py @ 0.9.0-draft -->

**Table 2-* - Requirement index (8 IDs)**

| ID | Keyword | Summary |
|----|---------|---------|
| ODTIS-0101 | MUST | A Core Identity implementation MUST support LoA Low, Medium, and High w… |
| ODTIS-0102 | MUST | A Core Identity implementation MUST expose the active LoA to RPs in OID… |
| ODTIS-0103 | MUST NOT | A Core Identity implementation MUST NOT assign High LoA without success… |
| ODTIS-0104 | MUST | National LoA MUST be claimed only when Extended sub-module E-Registry i… |
| ODTIS-0105 | MUST | Operator documentation MUST map VenID LoA levels to NIST IAL/AAL equiva… |
| ODTIS-0106 | MUST | Trust Network implementations MUST document FAL controls for gateway-to… |
| ODTIS-0107 | MUST | RPs MUST be able to configure minimum LoA per client application |
| ODTIS-0108 | MUST | Verification API MUST return current LoA even when attribute release is… |

<!-- GENERATED:section-index:END -->

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| stub | 2026-06-12 | Scaffold Phase 3.0 |
| draft v0.5 | 2026-06-12 | 2.1-2.8 normative prose; 8 IDs elevated |
| 0.9.0-draft | 2026-06-12 | Phase 3.2 section review; glossary cross-ref |

**Phase 3.1 checklist (2).**

- [x] Expand normative definitions (2.1)
- [x] LoA × proofing × claims matrix (2.8)
- [x] Full normative text for ODTIS-0101-2.5.2
- [x] eIDAS informative mapping (2.6 -> Annex C)
- [x] Registry terminology sync


**Phase 3.2 review checklist (2).**

- [x] Registry IDs cited in normative prose
- [x] Requirement index matches registry
- [x] Conformance test stub per ID
- [ ] External review cycle 1 ([Section review matrix](/governance/SECTION-REVIEW/))
