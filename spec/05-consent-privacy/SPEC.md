---
title: "Section 5: Consent and privacy"
description: Consent capture, RP admission, privacy minimization, E-Registry, E-Wallet, and extended module requirements.
---

# 5 Consent and privacy

<div class="odtis-spec-meta" markdown="1">

| Field | Value |
|-------|-------|
| **Status** | review draft - Phase 3.2 |
| **Spec version** | 0.9.0-draft |
| **Derived from** | P18 7, P01 3.6, P07 6, P13 |
| **Registry IDs** | ODTIS-0328 - ODTIS-0365 (34 requirements) |
| **Profiles** | Core Identity (5.1-5.3); Extended sub-modules (5.6-5.7, Annex D) |

</div>

---

## 5.1 Scope

This section normatively defines **consent**, **privacy**, and **Relying Party governance** rules for Core Identity implementations. Requirements apply to:

- OIDC IdP attribute release (3.3);
- Verification API responses (3.5);
- consent-service state (3.2.4); and
- operator and citizen-facing processes.

**Extended sub-module E-Wallet** requirements (5.6) apply only when declared per 1.6.5. They do not replace Core Identity consent rules for OIDC Path A.

Jurisdiction-specific legal bases (for example, GDPR Article 6, national data protection statutes) are documented in adopter annexes and operator policy, not as universal ODTIS MUST clauses (1.2.2).

---

## 5.2 Consent model

VenID implements **per-RP, per-scope consent** before attribute release. Consent is a distinct authorization layer from authentication: successful login MUST NOT imply attribute release without consent (ODTIS-0328).

### 5.2.1 Consent service

Core Identity implementations MUST provide a consent service (logical component: consent-service) that:

- records grants and revocations;
- resolves whether requested scopes are authorized for a `(subject_id, client_id)` pair; and
- is invoked by the IdP and Verification API **before** releasing custom attributes.

The IdP and Verification API MUST NOT bypass consent-service for custom scopes (ODTIS-0307, ODTIS-0317).

### 5.2.2 Active consent rule

A consent record is **active** when:

- `revoked_at` is null; and
- `expires_at` is null or in the future.

Inactive consent MUST block attribute release for the associated scopes.

---

### ODTIS-0328 - Explicit consent before first release

Core Identity **MUST** obtain **explicit user consent** before the **first attribute release** to each RP (`client_id`).

Standard OIDC scopes required solely for authentication (`openid` minimum) MAY be released after authentication without a separate attribute bundle, but any **identity attributes beyond authentication** (demographics, document-derived fields, custom scopes) MUST wait for consent.

**Trace (informative):** RF-15
**Conformance test:** First login to RP requesting custom scope; assert consent prompt before UserInfo or Verification API returns attributes.

---

### ODTIS-0329 - Consent record binding

Consent records **MUST** bind at minimum:

| Field | Semantics |
|-------|-----------|
| Subject | `identity_id` or `subject_id` |
| RP | OAuth `client_id` |
| Scopes | Authorized scope list (JSON array or equivalent) |
| Purpose | Citizen-visible purpose string |
| Timestamp | `granted_at` (and optional `expires_at`) |

Optional `revoked_at` MUST be set on revocation (ODTIS-0330).

**Trace (informative):** RF-15, RF-18
**Conformance test:** Inspect consent store after grant; all required fields populated and queryable.

---

### ODTIS-0330 - Revocation

Users **MUST** be able to **revoke consent** (via citizen portal per ODTIS-0323 or equivalent channel). Revocation **MUST** take effect on **subsequent** OIDC and Verification API requests without requiring RP cooperation.

Already-issued tokens MAY remain valid until expiry unless operator policy configures token revocation on consent change; new attribute requests MUST honor revocation immediately.

**Trace (informative):** RF-16
**Conformance test:** Revoke consent; next Verification API call MUST deny restricted attributes. Emit `consent.revoked` audit event (9).

---

### ODTIS-0331 - Scope enforcement

Verification API and IdP **MUST NOT** return attributes **outside active consented scopes** for the requesting RP.

Denial MUST NOT leak restricted attribute values in error payloads.

!!! note "Scope enforcement vs consent gating (FB-001)"
    **ODTIS-0331** is the privacy rule: no attributes outside active consented scopes, and denial payloads MUST NOT leak restricted values. **ODTIS-0307** gates OIDC custom claims on active consent. **ODTIS-0317** gates Verification API attribute release on consent scopes. Composite tests exercise all three; **`test_odtis-5_1_4.md`** focuses on 5.1.4 pass criteria (scope boundary and error non-leakage).

**Trace (informative):** RF-17, RF-20
**Conformance test:** `test_odtis-5_1_4.md`; also `test_verification_consent_scope.md` (3.5.3) and `test_consent_gated_claims.md` (3.1.7).

---

### ODTIS-0332 - Consent UI transparency

The consent user interface **MUST** display in **citizen-readable language**:

- **RP name** (not only `client_id`);
- **requested attributes** or scope descriptions; and
- **purpose** for the request.

Technical scope strings alone MUST NOT be the only disclosure.

**Trace (informative):** RNF-22
**Conformance test:** UX review or automated UI test asserts all three elements visible before accept button.

---

### 5.2.3 Consent lifecycle

**Table 5-1 - Consent lifecycle (normative behavior)**

| Event | Required behavior |
|-------|-------------------|
| First RP login with new scopes | Consent prompt; on accept, create record; emit `consent.granted` |
| User revokes in portal | Set `revoked_at`; emit `consent.revoked`; block future release |
| RP scope expansion | Operator policy MUST define re-consent rules; expanded scopes MUST NOT release without new consent |
| Consent expiry | Treat as inactive; block release until renewed |

```
First RP login -> consent prompt -> consent.granted -> attribute release
User revokes -> consent.revoked -> subsequent requests denied
Scope expansion -> re-consent (operator-configurable) -> new consent.granted
```

---

### 5.2.4 Re-consent on scope change

When an RP registration adds scopes to an existing relationship, Core Identity MUST either:

1. require re-consent before releasing new scopes; or
2. deny new scopes until consent updated.

Silent expansion of authorized scopes without user action MUST NOT occur.

---

## 5.3 Privacy and data minimization

Privacy principles from P01 3.6 map to normative ODTIS rules below. Operator policy MUST document how applicable law is satisfied; ODTIS MUST clauses define minimum technical and organizational behavior.

**Table 5-2 - Privacy principles**

| Principle | ODTIS expression |
|-----------|------------------|
| Purpose limitation | Attributes released only for declared RP purpose (ODTIS-0329, 5.1.4) |
| Minimization | No sale of identity data; no unrelated profiling (ODTIS-0336) |
| Biometric minimization | Raw biometrics retention per ODTIS-0314 |
| Transparency | Portal shows LoA and consents (ODTIS-0322, 3.8.2) |
| Auditability | Attribute shares logged with correlation ID (ODTIS-0327, 9) |
| Registry boundary | Civil-registry adapter does not replace registry authority (P11; E-Registry) |

---

### ODTIS-0333 - Published privacy policy

Operators **MUST** publish a **privacy policy** and **retention rules** aligned with applicable law. Publication MUST be accessible to subjects and RPs before production use.

Retention rules MUST cover identity attributes, consent records, proofing artifacts, and audit logs at a high level; detailed schedules MAY appear in operator policy annexes.

**Trace (informative):** RNF-14, RNF-16
**Conformance test:** Conformance statement links to published privacy policy URL or document ID.

---

### ODTIS-0334 - Data-subject access requests

Implementations **MUST** support **data-subject access requests** through documented operator processes (DSAR). Processes MUST include:

- identity verification of the requester;
- export or disclosure of subject-held data categories; and
- documented response timelines per applicable law.

Technical automation MAY be partial at L1; process documentation is mandatory for all conformance levels.

**Trace (informative):** RNF-15
**Conformance test:** Review operator DSAR procedure document; execute sample request in test environment.

---

### ODTIS-0335 - Encryption

Personal data **MUST** be encrypted **in transit** (TLS 1.2+ per ODTIS-0325) and **sensitive fields at rest** using industry-standard algorithms and key management.

Sensitive fields include at minimum: document identifiers, biometric templates or scores if retained, and contact channels not intended for public display.

**Trace (informative):** RNF-01
**Conformance test:** Architecture review confirms TLS on public paths and encryption at rest for declared sensitive columns.

---

### ODTIS-0336 - No sale or unrelated profiling

Identity attributes **MUST NOT** be **sold** or **repurposed for unrelated profiling** by the operator.

This clause addresses operator behavior. RP misuse is addressed through RP governance (5.4) and contractual duties (ODTIS-0338).

**Trace (informative):** P01 3.6
**Conformance test:** Operator privacy policy explicitly prohibits sale and unrelated profiling; audit sampling finds no prohibited transfers.

---

## 5.4 Relying Party governance

Technical scope enforcement (5.2) complements organizational RP accountability (P07 6.3).

### ODTIS-0337 - RP admission criteria

The DTI operator **MUST** define **RP admission criteria** before production onboarding. Criteria MUST be documented and MUST cover at minimum:

- permitted use cases and sectors;
- minimum security expectations; and
- data handling obligations.

**Trace (informative):** RF-23
**Conformance test:** Review RP onboarding checklist or policy; no production RP without documented approval.

---

### ODTIS-0338 - RP contractual duties

RP contracts **SHOULD** specify:

- **post-receipt data minimization** (RP may use data only for declared purpose); and
- **breach notification duties** toward the operator and affected subjects.

Deviations MUST be documented in operator conformance statement rationale when contracts omit SHOULD items.

**Trace (informative):** RNF-06, Book 1
**Conformance test:** Sample RP agreement review (L2+).

---

### ODTIS-0339 - RP suspension

The operator **MUST** be able to **suspend RP clients** for abuse, policy violation, or contract breach. Suspended clients MUST NOT obtain new tokens or Verification API access (ODTIS-0320).

**Trace (informative):** RF-24
**Conformance test:** Suspend RP in operator console; authorization and verify calls fail.

---

## 5.5 Threat and control cross-reference

Consent bypass and scope escalation are priority threats in P07. Implementations MUST map controls to Annex B. Minimum technical controls include:

| Threat | ODTIS control |
|--------|---------------|
| Consent bypass via API | ODTIS-0331, ODTIS-0317, consent-service gate |
| Scope escalation | ODTIS-0336 re-consent, ODTIS-0319 scope registration |
| RP impersonation | ODTIS-0319, ODTIS-0337 admission criteria |
| Unauthorized retention | ODTIS-0333, ODTIS-0335 |

---

## 5.6 Extended sub-module: E-Wallet

Requirements in this subsection apply **only** when Extended sub-module **E-Wallet** is declared. E-Wallet enables holder-controlled credentials (OID4VC) alongside central OIDC Path A (P03).

**Table 5-3 - EUDI ARF role mapping (informative)**

| EUDI ARF role | VenID component |
|---------------|-----------------|
| Wallet Provider | Wallet app |
| PID Provider / Credential Issuer | Trust Layer issuer + identity-core |
| Verifier / Relying Party | RP + Verification Gateway |
| Trust lists | Operator trust registry (Trust Network) |

---

### ODTIS-0340 - Verifiable Presentations

E-Wallet implementations **MUST** support **holder-signed Verifiable Presentations** using **OpenID for Verifiable Presentations (OID4VP)** or equivalent normative profile documented in operator policy.

**Trace (informative):** P03, P07 7
**Conformance test:** Present credential to test verifier via OID4VP flow; signature validates.

---

### ODTIS-0341 - Issuer trust validation

E-Wallet **MUST** validate **issuer trust** via the **operator trust registry** before accepting credentials. Untrusted issuers MUST be rejected.

**Trace (informative):** P03
**Conformance test:** Offer credential from untrusted issuer; wallet MUST reject.

---

### ODTIS-0342 - Selective disclosure

E-Wallet **SHOULD** support **selective disclosure** (SD-JWT or equivalent) for privacy-preserving attribute release to verifiers.

**Trace (informative):** P03, P07
**Conformance test:** Present minimal disclosed claims only; verifier receives subset.

---

### ODTIS-0343 - Shared LoA and consent with Path A

E-Wallet **MUST NOT** replace Core Identity **consent rules** for **OIDC Path A**. Wallet and OIDC paths **MUST** share **LoA state** from identity-core (ODTIS-0306, 2).

Wallet-only attribute release still MUST respect consent and purpose rules equivalent to ODTIS-5.1 for the verifier context.

**Trace (informative):** P03 5
**Conformance test:** Revoke OIDC consent; wallet presentation for same RP context MUST NOT bypass revocation policy defined in operator policy.

---

## 5.7 Extended sub-module product requirements

Book 1 decision domains **D6-D10** and Annex D bind the following **product requirements** for VenID implementation. Each applies **only** when the corresponding Extended sub-module is declared in the conformance statement (`ODTIS-0532`).

Normative catalog: [D Extended Profiles](/annexes/D-extended-profiles/) | tests: [Extended](/conformance/tests/).

### 5.7.1 E-Registry (National LoA)

### ODTIS-0344 - E-Registry declaration gate

**National LoA** via civil registry adapter **MUST** be offered **only** when sub-module **E-Registry** is declared and the registry adapter is active in production.

**Trace (informative):** Book 1 D7, ODTIS-0104, P11
**Conformance test:** Enable National LoA without E-Registry declaration; assignment MUST fail.

---

### ODTIS-0349 - No civil registry authority substitution

**E-Registry MUST NOT** replace civil registry **legal authority** or **issue national ID documents**.

**Trace (informative):** P11 1.1, RF-EXT5
**Conformance test:** Review adapter scope; no document issuance endpoints outside registry authority.

---

### ODTIS-0350 - National LoA after adapter verification

**National LoA MUST** be assigned **only after** successful registry adapter verification per operator policy.

**Trace (informative):** P11 4.2, ODTIS-0344
**Conformance test:** Failed registry match MUST NOT assign National LoA.

---

### ODTIS-0351 - Registry hashing and biometric non-persistence

The registry adapter **MUST** use **agreed identifier hashing**. **Raw registry biometrics MUST NOT** be persisted in Core Identity stores.

**Trace (informative):** P11 5.1
**Conformance test:** Inspect storage; no raw biometric blobs from registry feed.

---

### ODTIS-0352 - Phase 3+ registry activation

Registry adapter activation **MUST** require deployment **Phase 3+** and documented **bilateral agreement** with the registry authority.

**Trace (informative):** P11 4.2, P10
**Conformance test:** Phase 2 production MUST NOT activate registry adapter without documented exception.

---

### ODTIS-0353 - Registry verification audit

Every registry verification call **MUST** emit **auditable events** with correlation ID and match outcome metadata.

**Trace (informative):** P11 5.1, ODTIS-0526
**Conformance test:** Execute verification; audit export contains correlation and outcome.

---

### 5.7.2 E-Inclusion

### ODTIS-0354 - Assisted registration consent

Assisted registration flows **MUST** obtain **explicit subject or legal-representative consent** with full audit trail.

**Trace (informative):** P13 representative model, RF-15
**Conformance test:** Complete assisted flow; consent event present before attribute storage.

---

### ODTIS-0355 - Representative relationship verification

Representative or tutor flows **MUST** verify **legal relationship** before attribute release on behalf of another subject.

**Trace (informative):** P13 5.3, UC-C07
**Conformance test:** Release without verified relationship MUST fail.

---

### ODTIS-0356 - No LoA bypass via inclusion channels

Inclusion channels **MUST NOT** bypass LoA proofing rules defined for online registration.

**Trace (informative):** P18 4.2, RF-06
**Conformance test:** Assisted channel cannot assign higher LoA without equivalent proofing evidence.

---

### ODTIS-0357 - Accessibility and offline capture

Inclusion flows **SHOULD** support operator-configured **locales**, **accessibility**, and **offline capture** with deferred sync where policy allows.

**Trace (informative):** RNF-22, doc-14
**Conformance test:** Review operator policy for locale/offline options; exercise if declared.

---

### 5.7.3 E-Webhook

### ODTIS-0358 - RP webhook registration

**E-Webhook MUST** allow RPs to register **callback URLs**, **subscribed event types**, and **shared signing secret** via authenticated API.

**Trace (informative):** P14 6.4, RF-22, ODTIS-0531
**Conformance test:** Register webhook; subsequent signed delivery accepted.

---

### ODTIS-0359 - Webhook retry and delivery log

Webhook delivery **MUST** **retry with backoff** on failure and **log delivery outcomes** for operator review.

**Trace (informative):** P14 6.4, DS-07
**Conformance test:** Simulate receiver failure; retries and delivery log entries observed.

---

### ODTIS-0360 - Webhook PII minimization

Webhook payloads **MUST** **minimize PII**; use **opaque subject references** where operator policy requires.

**Trace (informative):** P14 6.4, ODTIS-0530
**Conformance test:** Inspect payload; no unnecessary PII beyond subscribed event contract.

---

### 5.7.4 E-Signature

### ODTIS-0361 - Signature LoA binding

**E-Signature MUST** bind each signature operation to a **verified subject identity** and **active LoA** meeting RP policy.

**Trace (informative):** RF-EXT1, P08
**Conformance test:** Sign with insufficient LoA; operation MUST fail.

---

### ODTIS-0362 - Signature PKI keys

Signature keys **MUST** be issued under **operator PKI** or recognized **TSP integration** documented in CP/CPS.

**Trace (informative):** P08, ODTIS-0507
**Conformance test:** Review key provenance against CP/CPS.

---

### ODTIS-0363 - Signature audit events

Signature creation and verification events **MUST** be **auditable** with correlation to `subject_id` and RP `client_id`.

**Trace (informative):** RF-EXT1, ODTIS-0526
**Conformance test:** Sign and verify; audit export contains subject and client correlation.

---

### 5.7.5 E-KYB (preview)

### ODTIS-0364 - Separate entity verification

**E-KYB MUST** verify **legal entity identity** separately from natural-person Core Identity proofing.

**Trace (informative):** doc-03 sector KYB
**Conformance test:** Entity verification path independent of personal IdP registration.

---

### ODTIS-0365 - Representative linkage for B2B

**E-KYB SHOULD** link **authorized representatives** to verified natural-person subjects before B2B attribute release.

**Trace (informative):** UC-E07, RF-EXT5
**Conformance test:** B2B release without linked representative SHOULD be flagged in operator review.

---

## 5.8 Requirement index

<!-- GENERATED:section-index:START -->
<!-- Generated by scripts/generate-spec-section-indexes.py @ 0.9.0-draft -->

**Table 5-4 - Requirement index (34 IDs)**

| ID | Keyword | Section | Summary |
|----|---------|---------|---------|
| ODTIS-0328 | MUST | 5.2 | Core Identity MUST obtain explicit user consent before first attribute … |
| ODTIS-0329 | MUST | 5.2 | Consent records MUST bind subject, RP client_id, scopes, purpose, and t… |
| ODTIS-0330 | MUST | 5.2 | Users MUST be able to revoke consent; revocation MUST take effect on su… |
| ODTIS-0331 | MUST NOT | 5.2 | Verification API and IdP MUST NOT return attributes outside active cons… |
| ODTIS-0332 | MUST | 5.2 | Consent UI MUST display RP name, requested attributes, and purpose in c… |
| ODTIS-0333 | MUST | 5.3 | Operators MUST publish privacy policy and retention rules aligned with … |
| ODTIS-0334 | MUST | 5.3 | Implementations MUST support data-subject access requests through docum… |
| ODTIS-0335 | MUST | 5.3 | Personal data MUST be encrypted in transit (TLS 1.2+) and sensitive fie… |
| ODTIS-0336 | MUST NOT | 5.3 | Identity attributes MUST NOT be sold or repurposed for unrelated profil… |
| ODTIS-0337 | MUST | 5.4 | DTI operator MUST define RP admission criteria before production onboar… |
| ODTIS-0338 | SHOULD | 5.4 | RP contracts SHOULD specify post-receipt data minimization and breach n… |
| ODTIS-0339 | MUST | 5.4 | Operator MUST be able to suspend RP clients for abuse or contract breach |
| ODTIS-0340 | MUST | 5.6 | E-Wallet implementations MUST support holder-signed Verifiable Presenta… |
| ODTIS-0341 | MUST | 5.6 | E-Wallet MUST validate issuer trust via operator trust registry before … |
| ODTIS-0342 | SHOULD | 5.6 | E-Wallet SHOULD support selective disclosure (SD-JWT or equivalent) for… |
| ODTIS-0343 | MUST NOT | 5.6 | E-Wallet MUST NOT replace Core Identity consent rules for OIDC Path A; … |
| ODTIS-0344 | MUST | 5.7.1 | National LoA via civil registry adapter MUST be offered only when E-Reg… |
| ODTIS-0349 | MUST NOT | 5.7.1 | E-Registry MUST NOT replace civil registry legal authority or issue nat… |
| ODTIS-0350 | MUST | 5.7.1 | National LoA MUST be assigned only after successful registry adapter ve… |
| ODTIS-0351 | MUST | 5.7.1 | Registry adapter MUST use agreed identifier hashing; raw registry biome… |
| ODTIS-0352 | MUST | 5.7.1 | Registry adapter activation MUST require deployment Phase 3+ and docume… |
| ODTIS-0353 | MUST | 5.7.1 | Every registry verification call MUST emit auditable events with correl… |
| ODTIS-0354 | MUST | 5.7.2 | Assisted registration flows MUST obtain explicit subject or legal-repre… |
| ODTIS-0355 | MUST | 5.7.2 | Representative or tutor flows MUST verify legal relationship before att… |
| ODTIS-0356 | MUST NOT | 5.7.2 | Inclusion channels MUST NOT bypass LoA proofing rules defined for onlin… |
| ODTIS-0357 | SHOULD | 5.7.2 | Inclusion flows SHOULD support operator-configured locales, accessibili… |
| ODTIS-0358 | MUST | 5.7.3 | E-Webhook MUST allow RPs to register callback URLs, subscribed event ty… |
| ODTIS-0359 | MUST | 5.7.3 | Webhook delivery MUST retry with backoff on failure and log delivery ou… |
| ODTIS-0360 | MUST | 5.7.3 | Webhook payloads MUST minimize PII; use opaque subject references where… |
| ODTIS-0361 | MUST | 5.7.4 | E-Signature MUST bind each signature operation to a verified subject id… |
| ODTIS-0362 | MUST | 5.7.4 | Signature keys MUST be issued under operator PKI or recognized TSP inte… |
| ODTIS-0363 | MUST | 5.7.4 | Signature creation and verification events MUST be auditable with corre… |
| ODTIS-0364 | MUST | 5.7.5 | E-KYB MUST verify legal entity identity separately from natural-person … |
| ODTIS-0365 | SHOULD | 5.7.5 | E-KYB SHOULD link authorized representatives to verified natural-person… |

<!-- GENERATED:section-index:END -->

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| stub | 2026-06-12 | Scaffold Phase 3.0 |
| draft v0.5 | 2026-06-12 | 5.1-5.8 normative prose; 16 IDs |
| 0.9.0-draft | 2026-06-12 | Phase 3.2 section review; FB-001 scope-enforcement note |

**Phase 3.1 checklist (5).**

- [x] Consent model aligned with P07 threat model (5.5)
- [x] Cross-ref 3 consent-service and API gates
- [x] Privacy and RP governance requirements
- [x] E-Wallet Extended requirements scoped to declared sub-module


**Phase 3.2 review checklist (5).**

- [x] Registry IDs cited in normative prose
- [x] Requirement index matches registry
- [x] Conformance test stub per ID
- [x] FB-001 scope enforcement traceability (5.1.4 vs 3.1.7 / 3.5.3)
- [ ] External review cycle 1 ([Section review matrix](/governance/SECTION-REVIEW/))
