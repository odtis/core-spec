---
title: "Section 11: Reliance Extensions (Capa B)"
description: Normative Capa B governance overlays for relying-party decisions, assurance metadata, audit evidence, recourse, and revocation.
---

# 11 Reliance Extensions (Capa B)

<div class="odtis-spec-meta" markdown="1">

| Field | Value |
|-------|-------|
| **Status** | review draft - Phase 3.2 |
| **Spec version** | 0.9.0-draft |
| **Registry IDs** | ODTIS-0701 - ODTIS-0772 (55 requirements) |
| **Profile** | `reliance-extensions` |
| **Domain** | ODTIS-0007 |
| **Annex** | E-reliance-profiles |

</div>

---

## 11.1 Scope

Reliance Extensions are **optional Capa B governance overlays** on the two-layer ODTIS model. Where Core Identity, Trust Network, and Federation define *how* trust signals are produced and exchanged (Capa A), Reliance Extensions define *who may rely* on a signal, *for what purpose*, *with what assurance*, *with what audit evidence*, and *with what recourse*.

Each sub-module specializes the **R-Base reliance schema** (`ODTIS-0701`-`ODTIS-0708`) and **MUST NOT weaken** any Core Identity, Trust Network, Federation, or Operator requirement (`ODTIS-0707`).

Sub-modules are declared independently in conformance statements (`ODTIS-0708`). Phase gates: [Annex E activation matrix](/annexes/E-reliance-profiles/activation.yaml).

---

## 11.2 R-Base reliance schema

Every Reliance Extension sub-module inherits the base schema below. These requirements apply whenever any Reliance Extension sub-module is claimed.

### ODTIS-0701 - Relying party identification

A reliance decision under any Reliance Extension **MUST** identify the relying party and its registered role before a trust signal is acted upon.

**Trace (informative):** DTI feed (Capa A/B thesis)
**Sub-module:** R-Base | **Min deployment phase:** 1
**Conformance test:** Exercise `ODTIS-0701` against declared reliance profile; record evidence that: A reliance decision under any Reliance Extension MUST identify the relying party and its r…

---

### ODTIS-0702 - Purpose binding

Each reliance decision **MUST** bind a declared purpose to every attribute or verdict consumed; use outside the declared purpose MUST be refused.

**Trace (informative):** DTI feed (Capa A/B thesis)
**Sub-module:** R-Base | **Min deployment phase:** 1
**Conformance test:** Exercise `ODTIS-0702` against declared reliance profile; record evidence that: Each reliance decision MUST bind a declared purpose to every attribute or verdict consumed…

---

### ODTIS-0703 - Assurance metadata

Each reliance decision **MUST** carry assurance metadata (assurance level and method) sufficient for the relying party risk tier.

**Trace (informative):** DTI feed (Capa A/B thesis)
**Sub-module:** R-Base | **Min deployment phase:** 1
**Conformance test:** Exercise `ODTIS-0703` against declared reliance profile; record evidence that: Each reliance decision MUST carry assurance metadata (assurance level and method) sufficie…

---

### ODTIS-0704 - Audit evidence reference

Each reliance decision **MUST** emit a tamper-evident audit evidence reference that a supervisor can reconstruct after the fact.

**Trace (informative):** DTI feed (Capa A/B thesis)
**Sub-module:** R-Base | **Min deployment phase:** 1
**Conformance test:** Exercise `ODTIS-0704` against declared reliance profile; record evidence that: Each reliance decision MUST emit a tamper-evident audit evidence reference that a supervis…

---

### ODTIS-0705 - Recourse path

Each Reliance Extension **MUST** define a recourse path for contested, failed, or wrongful decisions.

**Trace (informative):** DTI feed (Capa A/B thesis)
**Sub-module:** R-Base | **Min deployment phase:** 1
**Conformance test:** Exercise `ODTIS-0705` against declared reliance profile; record evidence that: Each Reliance Extension MUST define a recourse path for contested, failed, or wrongful dec…

---

### ODTIS-0706 - Revocation and step-up triggers

Each Reliance Extension **MUST** define revocation and step-up triggers where the underlying trust signal can change state.

**Trace (informative):** DTI feed (Capa A/B thesis)
**Sub-module:** R-Base | **Min deployment phase:** 1
**Conformance test:** Exercise `ODTIS-0706` against declared reliance profile; record evidence that: Each Reliance Extension MUST define revocation and step-up triggers where the underlying t…

---

### ODTIS-0707 - No-weakening rule

A Reliance Extension **MUST NOT** weaken or relax any Core Identity, Trust Network, Federation, or Operator requirement.

**Trace (informative):** DTI feed (Capa A/B thesis)
**Sub-module:** R-Base | **Min deployment phase:** 1
**Conformance test:** Exercise `ODTIS-0707` against declared reliance profile; record evidence that: A Reliance Extension MUST NOT weaken or relax any Core Identity, Trust Network, Federation…

---

### ODTIS-0708 - Conformance sub-module declaration

A conformance statement claiming Reliance Extensions **MUST** list each active sub-module and its deployment phase.

**Trace (informative):** DTI feed (Capa A/B thesis)
**Sub-module:** R-Base | **Min deployment phase:** 1
**Conformance test:** Exercise `ODTIS-0708` against declared reliance profile; record evidence that: A conformance statement claiming Reliance Extensions MUST list each active sub-module and…

---

## 11.3 Reliance Extension sub-modules

The following sub-modules extend R-Base for specific reliance contexts. Claiming a sub-module requires satisfying its requirements in addition to R-Base.

### 11.3.R-Agent-Authority - Agent authority reliance (Capa B for AI agents)

*Tier 1 (draft normative); minimum deployment phase 2.* External anchors (informative): IETF AIP did:aip, IETF AAE, draft-klrc-aiagent-auth-02, OAuth 2.0 RFC 8693, ….

Catalog: [Annex E sub-modules](/annexes/E-reliance-profiles/sub-modules.yaml).

### ODTIS-0710 - Agent identifier resolution

An agent reliance decision **MUST** resolve a verifiable agent identifier bound to a named principal and an accountable human or organizational sponsor.

**Trace (informative):** agentic-ai-odtis-alignment; estonia-ai-id
**Sub-module:** R-Agent-Authority | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0710` against declared reliance profile; record evidence that: An agent reliance decision MUST resolve a verifiable agent identifier bound to a named pri…

---

### ODTIS-0711 - Signed agent mandate

Delegated agent authority **MUST** be expressed as a signed mandate with allowed actions, prohibited actions, and value/time/session limits; each delegation hop MUST narrow scope and MUST NOT escalate privilege.

**Trace (informative):** agentic-ai-odtis-alignment; estonia-ai-id
**Sub-module:** R-Agent-Authority | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0711` against declared reliance profile; record evidence that: Delegated agent authority MUST be expressed as a signed mandate with allowed actions, proh…

---

### ODTIS-0712 - Mandate revocation freshness

A relying party **MUST** verify agent mandate revocation status within a declared freshness window before honoring a high-risk action, and MUST fail closed when status cannot be confirmed.

**Trace (informative):** agentic-ai-odtis-alignment; estonia-ai-id
**Sub-module:** R-Agent-Authority | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0712` against declared reliance profile; record evidence that: A relying party MUST verify agent mandate revocation status within a declared freshness wi…

---

### ODTIS-0713 - Human anchor for high-risk agent actions

High-risk agent actions such as financial disbursement, identity changes, or regulatory filings **SHOULD** require an explicit human-anchor reference and step-up in the delegation chain.

**Trace (informative):** agentic-ai-odtis-alignment; estonia-ai-id
**Sub-module:** R-Agent-Authority | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0713` against declared reliance profile; record evidence that: High-risk agent actions such as financial disbursement, identity changes, or regulatory fi…

---

### 11.3.R-Crypto-Agility - Crypto-agility assurance (PQC / HNDL)

*Tier 1 (draft normative); minimum deployment phase 2.* External anchors (informative): NIST FIPS 203/204/205, NIST SP 800-73/800-78 PIV PQC, ETSI ESI, eIDAS 2.0, ….

Catalog: [Annex E sub-modules](/annexes/E-reliance-profiles/sub-modules.yaml).

### ODTIS-0715 - Long-lived credential algorithm profile

A long-lived credential profile **MUST** publish its algorithm set, hybrid status, and a documented rotation policy and deprecation trigger.

**Trace (informative):** digital-id-quantum-resilience
**Sub-module:** R-Crypto-Agility | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0715` against declared reliance profile; record evidence that: A long-lived credential profile MUST publish its algorithm set, hybrid status, and a docum…

---

### ODTIS-0716 - Post-quantum acceptance criteria

Relying-party acceptance criteria **MUST** be declared for classical, hybrid, and post-quantum assertion paths, with audit evidence retained per accepted path.

**Trace (informative):** digital-id-quantum-resilience
**Sub-module:** R-Crypto-Agility | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0716` against declared reliance profile; record evidence that: Relying-party acceptance criteria MUST be declared for classical, hybrid, and post-quantum…

---

### ODTIS-0717 - Cryptographic bill of materials

Issuers **SHOULD** maintain a cryptographic bill of materials (CBOM) and classify harvest-now-decrypt-later exposure by credential validity and data sensitivity.

**Trace (informative):** digital-id-quantum-resilience
**Sub-module:** R-Crypto-Agility | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0717` against declared reliance profile; record evidence that: Issuers SHOULD maintain a cryptographic bill of materials (CBOM) and classify harvest-now-…

---

### 11.3.R-Lifecycle-Revocation - Identity lifecycle revocation (workforce/passkeys)

*Tier 1 (draft normative); minimum deployment phase 2.* External anchors (informative): FIDO2/passkeys, NIST 800-63, SPIFFE, PAM/IGA.

Catalog: [Annex E sub-modules](/annexes/E-reliance-profiles/sub-modules.yaml).

### ODTIS-0719 - Lifecycle revocation SLA

An identity lifecycle program **MUST** record both claimed and observed revocation SLA across every credential system that must fire on offboarding.

**Trace (informative):** identity-week-fido-hid
**Sub-module:** R-Lifecycle-Revocation | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0719` against declared reliance profile; record evidence that: An identity lifecycle program MUST record both claimed and observed revocation SLA across…

---

### ODTIS-0720 - Unified revocation evidence

Revocation evidence **MUST** unify physical and digital credential status into a reconstructable audit reference per lifecycle event.

**Trace (informative):** identity-week-fido-hid
**Sub-module:** R-Lifecycle-Revocation | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0720` against declared reliance profile; record evidence that: Revocation evidence MUST unify physical and digital credential status into a reconstructab…

---

### ODTIS-0721 - Orphan credential scanning

Operators **SHOULD** scan for orphan credentials and active sessions at defined intervals after a subject exit.

**Trace (informative):** identity-week-fido-hid
**Sub-module:** R-Lifecycle-Revocation | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0721` against declared reliance profile; record evidence that: Operators SHOULD scan for orphan credentials and active sessions at defined intervals afte…

---

### 11.3.R-Document-Capture - Document capture reliance (deepfake/injection)

*Tier 1 (draft normative); minimum deployment phase 2.* External anchors (informative): FinCEN FIN-2024-Alert004, ISO 30107 PAD, IAD.

Catalog: [Annex E sub-modules](/annexes/E-reliance-profiles/sub-modules.yaml).

### ODTIS-0723 - Document capture mode declaration

A document verification reliance decision **MUST** declare capture mode (live SDK, upload, or hybrid) and the injection-detection and document-forensics tiers in scope.

**Trace (informative):** shufti-deepfake
**Sub-module:** R-Document-Capture | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0723` against declared reliance profile; record evidence that: A document verification reliance decision MUST declare capture mode (live SDK, upload, or…

---

### ODTIS-0724 - Capture-channel integrity evidence

Reusable document verification outcomes **MUST** carry capture-channel integrity and device/session risk evidence; upload-only paths MUST be policy-gated by risk tier.

**Trace (informative):** shufti-deepfake
**Sub-module:** R-Document-Capture | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0724` against declared reliance profile; record evidence that: Reusable document verification outcomes MUST carry capture-channel integrity and device/se…

---

### ODTIS-0725 - Provider validation disclosure

Verification providers **SHOULD** disclose lab-versus-production validation metrics and define a fraud recourse and SAR escalation path.

**Trace (informative):** shufti-deepfake
**Sub-module:** R-Document-Capture | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0725` against declared reliance profile; record evidence that: Verification providers SHOULD disclose lab-versus-production validation metrics and define…

---

### 11.3.R-Liveness - Liveness reliance (presence != trust)

*Tier 1 (draft normative); minimum deployment phase 2.* External anchors (informative): ISO 30107, GDPR Art.13/14, Web Bot Auth, SPIFFE, ….

Catalog: [Annex E sub-modules](/annexes/E-reliance-profiles/sub-modules.yaml).

### ODTIS-0727 - Liveness decision metadata

A liveness reliance decision **MUST** declare the liveness provider, challenge type, identity-linkage class, and retention policy.

**Trace (informative):** google-liveness-captcha
**Sub-module:** R-Liveness | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0727` against declared reliance profile; record evidence that: A liveness reliance decision MUST declare the liveness provider, challenge type, identity-…

---

### ODTIS-0728 - Liveness verdict reuse prohibition

A human-presence (liveness) verdict **MUST NOT** be reused outside its declared purpose, and MUST NOT be treated as identity proof or statutory age proof without explicit authorization.

**Trace (informative):** google-liveness-captcha
**Sub-module:** R-Liveness | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0728` against declared reliance profile; record evidence that: A human-presence (liveness) verdict MUST NOT be reused outside its declared purpose, and M…

---

### ODTIS-0729 - Accessible liveness fallback

Liveness reliance **MUST** provide an accessible non-camera fallback of equivalent outcome and a recourse path for false rejection.

**Trace (informative):** google-liveness-captcha
**Sub-module:** R-Liveness | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0729` against declared reliance profile; record evidence that: Liveness reliance MUST provide an accessible non-camera fallback of equivalent outcome and…

---

### 11.3.R-Disclosure-Assurance - Disclosure assurance (audience-bound audit)

*Tier 1 (draft normative); minimum deployment phase 2.* External anchors (informative): draft-mih-scitt-aac-sel-disc-00, RFC 9901 SD-JWT, RFC 8785 JCS.

Catalog: [Annex E sub-modules](/annexes/E-reliance-profiles/sub-modules.yaml).

### ODTIS-0731 - Audience-bound disclosure sets

Audience-bound audit disclosure **MUST** define per-relying-party-role disclosure sets bound to purpose, with prohibited fields enumerated per tier.

**Trace (informative):** selective-disclosure-scitt
**Sub-module:** R-Disclosure-Assurance | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0731` against declared reliance profile; record evidence that: Audience-bound audit disclosure MUST define per-relying-party-role disclosure sets bound t…

---

### ODTIS-0732 - Offline verdict reconstruction

A verifier **MUST** be able to reconstruct a disclosed verdict offline from the registered evidence and the authorized disclosure set alone.

**Trace (informative):** selective-disclosure-scitt
**Sub-module:** R-Disclosure-Assurance | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0732` against declared reliance profile; record evidence that: A verifier MUST be able to reconstruct a disclosed verdict offline from the registered evi…

---

### ODTIS-0733 - Unauthorized disclosure refusal

A demand for fields outside the authorized disclosure set **MUST** be refused and MUST trigger a documented recourse path.

**Trace (informative):** selective-disclosure-scitt
**Sub-module:** R-Disclosure-Assurance | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0733` against declared reliance profile; record evidence that: A demand for fields outside the authorized disclosure set MUST be refused and MUST trigger…

---

### 11.3.R-Assurance-Portability - Assurance portability (reusable KYC)

*Tier 1 (draft normative); minimum deployment phase 2.* External anchors (informative): FinCEN, iProov threat intel, ISO 30107 PAD/IAD.

Catalog: [Annex E sub-modules](/annexes/E-reliance-profiles/sub-modules.yaml).

### ODTIS-0743 - Portable assurance metadata

A reusable verification outcome **MUST** carry portable assurance metadata: proofing level and method, PAD and IAD coverage, and capture-channel integrity.

**Trace (informative):** ai-kyc-pipeline-integrity
**Sub-module:** R-Assurance-Portability | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0743` against declared reliance profile; record evidence that: A reusable verification outcome MUST carry portable assurance metadata: proofing level and…

---

### ODTIS-0744 - Step-up before assurance reuse

A relying party **MUST** evaluate step-up requirements against its own risk tier before reusing assurance, rather than inheriting a prior yes/no decision.

**Trace (informative):** ai-kyc-pipeline-integrity
**Sub-module:** R-Assurance-Portability | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0744` against declared reliance profile; record evidence that: A relying party MUST evaluate step-up requirements against its own risk tier before reusin…

---

### ODTIS-0745 - Non-portable assurance re-verification

Only assurance that is actually portable **SHOULD** be reused; non-portable assurance SHOULD trigger re-verification.

**Trace (informative):** ai-kyc-pipeline-integrity
**Sub-module:** R-Assurance-Portability | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0745` against declared reliance profile; record evidence that: Only assurance that is actually portable SHOULD be reused; non-portable assurance SHOULD t…

---

### 11.3.R-VC-Maturity-Gate - VC standards maturity gate

*Tier 1 (draft normative); minimum deployment phase 1.* External anchors (informative): W3C VC Data Integrity 1.1, EdDSA/ECDSA cryptosuites 1.1, VCALM 1.0, VC Barcodes 1.0.

Catalog: [Annex E sub-modules](/annexes/E-reliance-profiles/sub-modules.yaml).

### ODTIS-0735 - External standard maturity gate

Adoption of an external credential standard **MUST** be gated by a declared maturity level; First Public Working Draft components MUST NOT be claimed for production national mandates.

**Trace (informative):** w3c-vc-lifecycle-barcodes
**Sub-module:** R-VC-Maturity-Gate | **Min deployment phase:** 1
**Conformance test:** Exercise `ODTIS-0735` against declared reliance profile; record evidence that: Adoption of an external credential standard MUST be gated by a declared maturity level; Fi…

---

### ODTIS-0736 - Capa B controls before production reliance

Each gated standard component **MUST** declare the Capa B controls (relying-party authentication, audit logging, rate limits, version pinning) required before production reliance.

**Trace (informative):** w3c-vc-lifecycle-barcodes
**Sub-module:** R-VC-Maturity-Gate | **Min deployment phase:** 1
**Conformance test:** Exercise `ODTIS-0736` against declared reliance profile; record evidence that: Each gated standard component MUST declare the Capa B controls (relying-party authenticati…

---

### ODTIS-0737 - Conformance lab before promotion

Ecosystems **SHOULD** run conformance labs and publish internal profiles before promoting a draft standard beyond pilot.

**Trace (informative):** w3c-vc-lifecycle-barcodes
**Sub-module:** R-VC-Maturity-Gate | **Min deployment phase:** 1
**Conformance test:** Exercise `ODTIS-0737` against declared reliance profile; record evidence that: Ecosystems SHOULD run conformance labs and publish internal profiles before promoting a dr…

---

### 11.3.R-Public-eID - Public-sector eID reliance (multi-eID coexistence)

*Tier 1 (draft normative); minimum deployment phase 2.* External anchors (informative): eIDAS 2.0 LoA High, EUDI ARF, NIST SP 800-63-4.

Catalog: [Annex E sub-modules](/annexes/E-reliance-profiles/sub-modules.yaml).

### ODTIS-0739 - Multi-eID acceptance matrix

A relying party accepting multiple eIDs **MUST** publish an acceptance matrix mapping each issuer and assurance level to service tier and purpose.

**Trace (informative):** sweden-state-eid
**Sub-module:** R-Public-eID | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0739` against declared reliance profile; record evidence that: A relying party accepting multiple eIDs MUST publish an acceptance matrix mapping each iss…

---

### ODTIS-0740 - Authentication versus authorization

Authentication success **MUST** be distinguished from authorization or eligibility, and cross-border acceptance MUST declare an assurance mapping.

**Trace (informative):** sweden-state-eid
**Sub-module:** R-Public-eID | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0740` against declared reliance profile; record evidence that: Authentication success MUST be distinguished from authorization or eligibility, and cross-…

---

### ODTIS-0741 - Wrongful-rejection recourse

Wrongful-rejection recourse and trust-event logging **SHOULD** be defined before multi-eID operation at scale.

**Trace (informative):** sweden-state-eid
**Sub-module:** R-Public-eID | **Min deployment phase:** 2
**Conformance test:** Exercise `ODTIS-0741` against declared reliance profile; record evidence that: Wrongful-rejection recourse and trust-event logging SHOULD be defined before multi-eID ope…

---

### 11.3.R-Fraud-Orchestration - Fraud event orchestration (PSD3/PSR)

*Tier 2 (preview); minimum deployment phase 3.* External anchors (informative): PSD3/PSR, Verification of Payee, APP fraud reimbursement, GDPR.

Catalog: [Annex E sub-modules](/annexes/E-reliance-profiles/sub-modules.yaml).

### ODTIS-0747 - Fraud decision trust-event chain

A fraud decision (block, step-up, hold, or refund) **MUST** be reconstructable as a trust-event chain linking KYC evidence, fraud signal, and where applicable the Verification of Payee result.

**Trace (informative):** finextra-fraud-psd3
**Sub-module:** R-Fraud-Orchestration | **Min deployment phase:** 3
**Conformance test:** Exercise `ODTIS-0747` against declared reliance profile; record evidence that: A fraud decision (block, step-up, hold, or refund) MUST be reconstructable as a trust-even…

---

### ODTIS-0748 - Fraud liability and sharing basis

Each fraud decision **MUST** record a liability owner and the legal basis for any cross-institution fraud-signal sharing.

**Trace (informative):** finextra-fraud-psd3
**Sub-module:** R-Fraud-Orchestration | **Min deployment phase:** 3
**Conformance test:** Exercise `ODTIS-0748` against declared reliance profile; record evidence that: Each fraud decision MUST record a liability owner and the legal basis for any cross-instit…

---

### ODTIS-0749 - Wrongful block recourse

A recourse path **SHOULD** be defined for wrongful blocks as well as for fraud victims.

**Trace (informative):** finextra-fraud-psd3
**Sub-module:** R-Fraud-Orchestration | **Min deployment phase:** 3
**Conformance test:** Exercise `ODTIS-0749` against declared reliance profile; record evidence that: A recourse path SHOULD be defined for wrongful blocks as well as for fraud victims.…

---

### 11.3.R-Stablecoin-CIP - Stablecoin CIP reliance (GENIUS Act)

*Tier 2 (preview); minimum deployment phase 3.* External anchors (informative): GENIUS Act, FinCEN CIP/BSA, FR 2026-12460, NIST 800-63-4, ….

Catalog: [Annex E sub-modules](/annexes/E-reliance-profiles/sub-modules.yaml).

### ODTIS-0751 - CIP reliance decision record

A CIP reliance decision **MUST** record the verifying institution, proofing method, assurance level, and reliance type (direct verification versus institutional reliance).

**Trace (informative):** us-stablecoin-genius
**Sub-module:** R-Stablecoin-CIP | **Min deployment phase:** 3
**Conformance test:** Exercise `ODTIS-0751` against declared reliance profile; record evidence that: A CIP reliance decision MUST record the verifying institution, proofing method, assurance…

---

### ODTIS-0752 - Institutional CIP reliance certification

Institutional reliance **MUST** reference an annual AML/CFT and CIP certification and MUST bind the decision to account-opening purpose.

**Trace (informative):** us-stablecoin-genius
**Sub-module:** R-Stablecoin-CIP | **Min deployment phase:** 3
**Conformance test:** Exercise `ODTIS-0752` against declared reliance profile; record evidence that: Institutional reliance MUST reference an annual AML/CFT and CIP certification and MUST bin…

---

### ODTIS-0753 - Protocol-agnostic CIP presentation

A protocol-agnostic credential presentation envelope and an identity-error recourse path **SHOULD** be supported.

**Trace (informative):** us-stablecoin-genius
**Sub-module:** R-Stablecoin-CIP | **Min deployment phase:** 3
**Conformance test:** Exercise `ODTIS-0753` against declared reliance profile; record evidence that: A protocol-agnostic credential presentation envelope and an identity-error recourse path S…

---

### 11.3.R-Travel - Cross-border travel reliance (ICAO/IATA)

*Tier 2 (preview); minimum deployment phase 3.* External anchors (informative): ICAO DTC/PKD, IATA One ID, ISO 18013, OpenID4VP.

Catalog: [Annex E sub-modules](/annexes/E-reliance-profiles/sub-modules.yaml).

### ODTIS-0755 - Travel touchpoint reliance declaration

A cross-border travel reliance decision **MUST** declare, per touchpoint, the relying party, purpose code, and allowed attribute set with an assurance-level mapping.

**Trace (informative):** wttc-biometria-travel
**Sub-module:** R-Travel | **Min deployment phase:** 3
**Conformance test:** Exercise `ODTIS-0755` against declared reliance profile; record evidence that: A cross-border travel reliance decision MUST declare, per touchpoint, the relying party, p…

---

### ODTIS-0756 - Journey-bound attribute reuse

Attribute reuse across touchpoints **MUST** be bounded by a declared reuse policy (one-time, session-bound, or journey-bound).

**Trace (informative):** wttc-biometria-travel
**Sub-module:** R-Travel | **Min deployment phase:** 3
**Conformance test:** Exercise `ODTIS-0756` against declared reliance profile; record evidence that: Attribute reuse across touchpoints MUST be bounded by a declared reuse policy (one-time, s…

---

### ODTIS-0757 - Cross-border travel recourse

A recourse endpoint and cross-border recognition scope **SHOULD** be published per touchpoint.

**Trace (informative):** wttc-biometria-travel
**Sub-module:** R-Travel | **Min deployment phase:** 3
**Conformance test:** Exercise `ODTIS-0757` against declared reliance profile; record evidence that: A recourse endpoint and cross-border recognition scope SHOULD be published per touchpoint.…

---

### 11.3.R-CRA-Resilience - CRA trust-resilience (software supply chain)

*Tier 2 (preview); minimum deployment phase 3.* External anchors (informative): EU CRA 2024/2847 Art.13/14, ENISA SRP, OSPS Baseline, SPDX/CycloneDX.

Catalog: [Annex E sub-modules](/annexes/E-reliance-profiles/sub-modules.yaml).

### ODTIS-0759 - Supply-chain role attestation

A software-supply-chain trust profile **MUST** attest manufacturer versus steward role and maintain SBOM provenance per release.

**Trace (informative):** cra-readiness-reality
**Sub-module:** R-CRA-Resilience | **Min deployment phase:** 3
**Conformance test:** Exercise `ODTIS-0759` against declared reliance profile; record evidence that: A software-supply-chain trust profile MUST attest manufacturer versus steward role and mai…

---

### ODTIS-0760 - Active-exploit trust-event chain

Active-exploit and severe-incident events **MUST** be recorded as a trust-event chain with corrective-measure and regulator-filing references and timestamps.

**Trace (informative):** cra-readiness-reality
**Sub-module:** R-CRA-Resilience | **Min deployment phase:** 3
**Conformance test:** Exercise `ODTIS-0760` against declared reliance profile; record evidence that: Active-exploit and severe-incident events MUST be recorded as a trust-event chain with cor…

---

### ODTIS-0761 - Post-market monitoring documentation

Post-market monitoring, a vulnerability-disclosure policy, and a component revocation path **SHOULD** be documented.

**Trace (informative):** cra-readiness-reality
**Sub-module:** R-CRA-Resilience | **Min deployment phase:** 3
**Conformance test:** Exercise `ODTIS-0761` against declared reliance profile; record evidence that: Post-market monitoring, a vulnerability-disclosure policy, and a component revocation path…

---

### 11.3.R-DPI-Resilience - DPI trust resilience (blast-radius control)

*Tier 2 (preview); minimum deployment phase 3.* External anchors (informative): Universal DPI Safeguards, World Bank/Alan Turing, WAVE, ISO 27001.

Catalog: [Annex E sub-modules](/annexes/E-reliance-profiles/sub-modules.yaml).

### ODTIS-0763 - DPI blast-radius authorization

A shared-infrastructure (DPI) trust profile **MUST** publish participant and relying-party authorization scoped per component, with blast-radius mapping of co-dependent services.

**Trace (informative):** dpi-attack-surface-blast-radius
**Sub-module:** R-DPI-Resilience | **Min deployment phase:** 3
**Conformance test:** Exercise `ODTIS-0763` against declared reliance profile; record evidence that: A shared-infrastructure (DPI) trust profile MUST publish participant and relying-party aut…

---

### ODTIS-0764 - Trust Resilience Evidence Pack

A Trust Resilience Evidence Pack covering authorization, purpose, assurance, audit, revocation/step-up, recourse, and reporting **MUST** be maintained from pilot day one.

**Trace (informative):** dpi-attack-surface-blast-radius
**Sub-module:** R-DPI-Resilience | **Min deployment phase:** 3
**Conformance test:** Exercise `ODTIS-0764` against declared reliance profile; record evidence that: A Trust Resilience Evidence Pack covering authorization, purpose, assurance, audit, revoca…

---

### ODTIS-0765 - Transparent DPI incident reporting

Security and incident metrics **SHOULD** be reported transparently to partners, regulators, and the public.

**Trace (informative):** dpi-attack-surface-blast-radius
**Sub-module:** R-DPI-Resilience | **Min deployment phase:** 3
**Conformance test:** Exercise `ODTIS-0765` against declared reliance profile; record evidence that: Security and incident metrics SHOULD be reported transparently to partners, regulators, an…

---

### 11.3.R-Sovereign-Chain-Interop - Sovereign identity-chain interop (reference)

*Tier 3 (preview); minimum deployment phase 4.* External anchors (informative): W3C VC/VP, OpenID4VP, ToIP, mutual recognition.

Catalog: [Annex E sub-modules](/annexes/E-reliance-profiles/sub-modules.yaml).

### ODTIS-0767 - Sovereign chain accountability

Reliance on a sovereign or external identity-chain credential **MUST** document the chain operator accountability and issuer liability and revocation before mutual recognition.

**Trace (informative):** china-identity-chain
**Sub-module:** R-Sovereign-Chain-Interop | **Min deployment phase:** 4
**Conformance test:** Exercise `ODTIS-0767` against declared reliance profile; record evidence that: Reliance on a sovereign or external identity-chain credential MUST document the chain oper…

---

### ODTIS-0768 - No institutional trust transfer

Technical interoperability with an external identity chain **MUST NOT** be treated as institutional trust transfer; cross-jurisdiction acceptance MUST declare assurance mapping, purpose binding, and a recourse path.

**Trace (informative):** china-identity-chain
**Sub-module:** R-Sovereign-Chain-Interop | **Min deployment phase:** 4
**Conformance test:** Exercise `ODTIS-0768` against declared reliance profile; record evidence that: Technical interoperability with an external identity chain MUST NOT be treated as institut…

---

### 11.3.R-LE-Biometric - Law-enforcement biometric reliance (sensitive)

*Tier 3 (preview); minimum deployment phase 4.* External anchors (informative): ISO 30107, WA PRIS Act 2024, PIA frameworks.

Catalog: [Annex E sub-modules](/annexes/E-reliance-profiles/sub-modules.yaml).

### ODTIS-0771 - Law-enforcement biometric decision record

A law-enforcement biometric reliance decision **MUST** record purpose, the alert-list authorizer, retention policy, and deployment class (overt or covert).

**Trace (informative):** wa-police-lfr
**Sub-module:** R-LE-Biometric | **Min deployment phase:** 4
**Conformance test:** Exercise `ODTIS-0771` against declared reliance profile; record evidence that: A law-enforcement biometric reliance decision MUST record purpose, the alert-list authoriz…

---

### ODTIS-0772 - False-match mitigation and recourse

False-match mitigation and a citizen recourse path **MUST** be defined before operational use.

**Trace (informative):** wa-police-lfr
**Sub-module:** R-LE-Biometric | **Min deployment phase:** 4
**Conformance test:** Exercise `ODTIS-0772` against declared reliance profile; record evidence that: False-match mitigation and a citizen recourse path MUST be defined before operational use.…

---

## 11.4 Sub-module activation matrix

Reliance Extension sub-modules MUST NOT be claimed in production before their minimum deployment phase. Tier 2 and Tier 3 sub-modules are preview profiles intended for national-scale or sensitive deployments.

| Sub-module | Tier | Min phase | Requirement IDs |
|------------|------|-----------|-----------------|
| R-Agent-Authority | 1 | 2 | `ODTIS-0710`, `ODTIS-0711`, `ODTIS-0712`, `ODTIS-0713` |
| R-Crypto-Agility | 1 | 2 | `ODTIS-0715`, `ODTIS-0716`, `ODTIS-0717` |
| R-Lifecycle-Revocation | 1 | 2 | `ODTIS-0719`, `ODTIS-0720`, `ODTIS-0721` |
| R-Document-Capture | 1 | 2 | `ODTIS-0723`, `ODTIS-0724`, `ODTIS-0725` |
| R-Liveness | 1 | 2 | `ODTIS-0727`, `ODTIS-0728`, `ODTIS-0729` |
| R-Disclosure-Assurance | 1 | 2 | `ODTIS-0731`, `ODTIS-0732`, `ODTIS-0733` |
| R-Assurance-Portability | 1 | 2 | `ODTIS-0743`, `ODTIS-0744`, `ODTIS-0745` |
| R-VC-Maturity-Gate | 1 | 1 | `ODTIS-0735`, `ODTIS-0736`, `ODTIS-0737` |
| R-Public-eID | 1 | 2 | `ODTIS-0739`, `ODTIS-0740`, `ODTIS-0741` |
| R-Fraud-Orchestration | 2 | 3 | `ODTIS-0747`, `ODTIS-0748`, `ODTIS-0749` |
| R-Stablecoin-CIP | 2 | 3 | `ODTIS-0751`, `ODTIS-0752`, `ODTIS-0753` |
| R-Travel | 2 | 3 | `ODTIS-0755`, `ODTIS-0756`, `ODTIS-0757` |
| R-CRA-Resilience | 2 | 3 | `ODTIS-0759`, `ODTIS-0760`, `ODTIS-0761` |
| R-DPI-Resilience | 2 | 3 | `ODTIS-0763`, `ODTIS-0764`, `ODTIS-0765` |
| R-Sovereign-Chain-Interop | 3 | 4 | `ODTIS-0767`, `ODTIS-0768` |
| R-LE-Biometric | 3 | 4 | `ODTIS-0771`, `ODTIS-0772` |

Machine-readable rules: [Activation (YAML)](/annexes/E-reliance-profiles/activation.yaml).

---

## 11.5 Requirement index

<!-- GENERATED:section-index:START -->
<!-- Generated by scripts/generate-spec-section-indexes.py @ 0.9.0-draft -->

**Table 11-* - Requirement index (55 IDs)**

| ID | Keyword | Summary |
|----|---------|---------|
| ODTIS-0701 | MUST | A reliance decision under any Reliance Extension MUST identify the rely… |
| ODTIS-0702 | MUST | Each reliance decision MUST bind a declared purpose to every attribute … |
| ODTIS-0703 | MUST | Each reliance decision MUST carry assurance metadata (assurance level a… |
| ODTIS-0704 | MUST | Each reliance decision MUST emit a tamper-evident audit evidence refere… |
| ODTIS-0705 | MUST | Each Reliance Extension MUST define a recourse path for contested, fail… |
| ODTIS-0706 | MUST | Each Reliance Extension MUST define revocation and step-up triggers whe… |
| ODTIS-0707 | MUST NOT | A Reliance Extension MUST NOT weaken or relax any Core Identity, Trust … |
| ODTIS-0708 | MUST | A conformance statement claiming Reliance Extensions MUST list each act… |
| ODTIS-0710 | MUST | An agent reliance decision MUST resolve a verifiable agent identifier b… |
| ODTIS-0711 | MUST | Delegated agent authority MUST be expressed as a signed mandate with al… |
| ODTIS-0712 | MUST | A relying party MUST verify agent mandate revocation status within a de… |
| ODTIS-0713 | SHOULD | High-risk agent actions such as financial disbursement, identity change… |
| ODTIS-0715 | MUST | A long-lived credential profile MUST publish its algorithm set, hybrid … |
| ODTIS-0716 | MUST | Relying-party acceptance criteria MUST be declared for classical, hybri… |
| ODTIS-0717 | SHOULD | Issuers SHOULD maintain a cryptographic bill of materials (CBOM) and cl… |
| ODTIS-0719 | MUST | An identity lifecycle program MUST record both claimed and observed rev… |
| ODTIS-0720 | MUST | Revocation evidence MUST unify physical and digital credential status i… |
| ODTIS-0721 | SHOULD | Operators SHOULD scan for orphan credentials and active sessions at def… |
| ODTIS-0723 | MUST | A document verification reliance decision MUST declare capture mode (li… |
| ODTIS-0724 | MUST | Reusable document verification outcomes MUST carry capture-channel inte… |
| ODTIS-0725 | SHOULD | Verification providers SHOULD disclose lab-versus-production validation… |
| ODTIS-0727 | MUST | A liveness reliance decision MUST declare the liveness provider, challe… |
| ODTIS-0728 | MUST NOT | A human-presence (liveness) verdict MUST NOT be reused outside its decl… |
| ODTIS-0729 | MUST | Liveness reliance MUST provide an accessible non-camera fallback of equ… |
| ODTIS-0731 | MUST | Audience-bound audit disclosure MUST define per-relying-party-role disc… |
| ODTIS-0732 | MUST | A verifier MUST be able to reconstruct a disclosed verdict offline from… |
| ODTIS-0733 | MUST | A demand for fields outside the authorized disclosure set MUST be refus… |
| ODTIS-0735 | MUST | Adoption of an external credential standard MUST be gated by a declared… |
| ODTIS-0736 | MUST | Each gated standard component MUST declare the Capa B controls (relying… |
| ODTIS-0737 | SHOULD | Ecosystems SHOULD run conformance labs and publish internal profiles be… |
| ODTIS-0739 | MUST | A relying party accepting multiple eIDs MUST publish an acceptance matr… |
| ODTIS-0740 | MUST | Authentication success MUST be distinguished from authorization or elig… |
| ODTIS-0741 | SHOULD | Wrongful-rejection recourse and trust-event logging SHOULD be defined b… |
| ODTIS-0743 | MUST | A reusable verification outcome MUST carry portable assurance metadata:… |
| ODTIS-0744 | MUST | A relying party MUST evaluate step-up requirements against its own risk… |
| ODTIS-0745 | SHOULD | Only assurance that is actually portable SHOULD be reused; non-portable… |
| ODTIS-0747 | MUST | A fraud decision (block, step-up, hold, or refund) MUST be reconstructa… |
| ODTIS-0748 | MUST | Each fraud decision MUST record a liability owner and the legal basis f… |
| ODTIS-0749 | SHOULD | A recourse path SHOULD be defined for wrongful blocks as well as for fr… |
| ODTIS-0751 | MUST | A CIP reliance decision MUST record the verifying institution, proofing… |
| ODTIS-0752 | MUST | Institutional reliance MUST reference an annual AML/CFT and CIP certifi… |
| ODTIS-0753 | SHOULD | A protocol-agnostic credential presentation envelope and an identity-er… |
| ODTIS-0755 | MUST | A cross-border travel reliance decision MUST declare, per touchpoint, t… |
| ODTIS-0756 | MUST | Attribute reuse across touchpoints MUST be bounded by a declared reuse … |
| ODTIS-0757 | SHOULD | A recourse endpoint and cross-border recognition scope SHOULD be publis… |
| ODTIS-0759 | MUST | A software-supply-chain trust profile MUST attest manufacturer versus s… |
| ODTIS-0760 | MUST | Active-exploit and severe-incident events MUST be recorded as a trust-e… |
| ODTIS-0761 | SHOULD | Post-market monitoring, a vulnerability-disclosure policy, and a compon… |
| ODTIS-0763 | MUST | A shared-infrastructure (DPI) trust profile MUST publish participant an… |
| ODTIS-0764 | MUST | A Trust Resilience Evidence Pack covering authorization, purpose, assur… |
| ODTIS-0765 | SHOULD | Security and incident metrics SHOULD be reported transparently to partn… |
| ODTIS-0767 | MUST | Reliance on a sovereign or external identity-chain credential MUST docu… |
| ODTIS-0768 | MUST NOT | Technical interoperability with an external identity chain MUST NOT be … |
| ODTIS-0771 | MUST | A law-enforcement biometric reliance decision MUST record purpose, the … |
| ODTIS-0772 | MUST | False-match mitigation and a citizen recourse path MUST be defined befo… |

<!-- GENERATED:section-index:END -->

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| 0.9.0-draft | 2026-06-23 | Initial Reliance Extensions catalog (55 IDs) from DTI editorial analysis |
| 0.9.0-draft | 2026-06-23 | Normative prose for all 55 requirements; section 11 completeness gate |

**Phase 3.2 review checklist (11).**

- [x] R-Base reliance schema normative prose (ODTIS-0701-0708)
- [x] 16 sub-modules with normative requirement blocks
- [x] Requirement index matches registry
- [x] Conformance test stub per ID
- [ ] Annex C external-standard anchors merged
- [ ] External review cycle 1 ([Section review matrix](/governance/SECTION-REVIEW/))
