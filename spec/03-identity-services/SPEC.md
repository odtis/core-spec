---
title: "Section 3: Identity services"
description: OIDC IdP, subject registry, verification API, proofing, citizen portal, and RP client lifecycle requirements.
---

# 3 Identity services

<div class="odtis-spec-meta" markdown="1">

| Field | Value |
|-------|-------|
| **Status** | review draft - Phase 3.2 |
| **Spec version** | 0.9.0-draft |
| **Derived from** | P18 5, P13, P14, Book 2 ch. 4 |
| **Registry IDs** | ODTIS-0301 - ODTIS-0327 (27 requirements) |
| **Profile** | Core Identity |

</div>

---

## 3.1 Service inventory

Core Identity implementations MUST provide the Layer 1 services in Table 3-1. Internal decomposition MAY use separate microservices; external conformance is evaluated on **observable behavior** at each integration surface.

**Table 3-1 - Core Identity services**

| Service | ref | Integration surface | Annex A OpenAPI |
|---------|-------|---------------------|-----------------|
| Identity Provider (OIDC/OAuth 2.0) | 3.3 | Browser and mobile RP login | Discovery + JWKS (not VenID OpenAPI) |
| Subject registry (identity-core) | 3.2 | Internal; state source for LoA and attributes | `identity-core` (internal gRPC optional) |
| Proofing orchestration | 3.4 | Citizen API + operator review | `citizen-api`, operator API |
| Verification API | 3.5 | RP backend server-to-server | `verification-api` |
| Consent service | 5 | OIDC + Verification API (cross-ref) | `consent-api` |
| Citizen portal | 3.7 | Subject self-service | `citizen-api` |
| Notification / OTP | 3.9 | Supporting channel | `notification-api` |
| Wallet / VC issuer | 3.10 | Optional Extended E-Wallet | `wallet-api` |

Trust network components (exchange gateway, trust registry) live in Layer 2 (4). They MUST consume Layer 1 identity as catalogued services and MUST NOT duplicate subject system-of-record tables.

---

## 3.2 Data model

### 3.2.1 System of record

The **subject registry** (logical service: identity-core) is the system of record for:

- stable `subject_id`;
- subject `status`;
- active `assurance_level` (LoA);
- verified demographics and contact verification flags;
- optional national registry verification timestamp when E-Registry is declared.

The OIDC Identity Provider (IdP) MUST NOT be the sole store of verified attributes or LoA. Token claims MUST reflect registry state at issuance time (ODTIS-0306).

### 3.2.2 Normative entities

**Table 3-2 - Core entities**

| Entity | Owner service | Purpose |
|--------|---------------|---------|
| **Identity (Subject)** | identity-core | Stable `subject_id`, status, LoA, document hash, lifecycle timestamps |
| **IdentityDemographics** | identity-core | Given name, family name, birth date, nationality |
| **Contact** | identity-core | Email, phone, verification flags (LoA Low evidence) |
| **Consent** | consent-service | Per-RP scopes, purpose, grant/revoke lifecycle |
| **IdentityVerification** | verification-engine | Proofing attempts, provider scores, manual review outcome |
| **RegistrationSession** | verification-engine | Multi-step registration workflow state |

Extended entities (Representative, Incident, WebhookSubscription) are required only for declared Extended sub-modules (Annex D).

### 3.2.3 Identity (Subject) attributes

| Attribute | Semantics | Normative rules |
|-----------|-----------|-----------------|
| `subject_id` | Public immutable identifier; OIDC `sub` | Assigned once at first successful registration (ODTIS-0310) |
| `status` | `active`, `suspended`, `revoked`, `pending_verification` | Transitions MUST be auditable (9) |
| `assurance_level` | `low`, `medium`, `high`, `national` | MUST follow 2 |
| `document_number_hash` | One-way hash of ID document | MUST NOT store reversible document number for arbitrary search |
| `national_registry_verified_at` | Registry match timestamp | Set only via E-Registry (ODTIS-0344) |

### 3.2.4 Consent entity

Consent records MUST bind at minimum: `identity_id`, `client_id`, `scopes`, `purpose`, `granted_at`, and optional `revoked_at`. Active consent rules are normatively defined in 5.

### 3.2.5 IdentityVerification entity

Proofing outcomes MUST be stored without raw document images or raw biometric images in the long-term identity record. Provider result JSON MAY contain scores and decision metadata only (ODTIS-0314). Temporary object storage for capture MAY exist with lifecycle deletion per operator policy.

### 3.2.6 Logical relationships

```
Identity 1 - 1 IdentityDemographics
Identity 1 - 1 Contact
Identity 1 - * Consent
Identity 1 - * IdentityVerification
Consent * - 1 RP client (client_id)
```

Physical schema details are informative in P13 and Annex A; entity semantics above are normative for conformance.

---

## 3.3 Identity Provider (OIDC / OAuth 2.0)

The IdP exposes OpenID Connect for citizen login and RP federation. Implementations MUST align with [RFC 6749], [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html), and [RFC 7636](https://www.rfc-editor.org/rfc/rfc7636) (PKCE).

!!! note "Requirement ID numbering"
    OIDC IdP requirements in this subsection use registry IDs **`ODTIS-3.1.x`** (P18 extract). Section **3.12** indexes all Core Identity IDs including 3.2.x, 3.5.x, 3.6.x, 3.8.x, and 3.9.x.

### ODTIS-0301 - Discovery and JWKS

Core Identity **MUST** expose:

- `/.well-known/openid-configuration` with issuer, authorization, token, userinfo, and jwks_uri endpoints; and
- a JWKS document for signature verification of issued tokens.

**Trace (informative):** OIDC Discovery
**Conformance test:** Fetch discovery document and JWKS; validate RS256 (or documented alg) keys verify sample `id_token`.

---

### ODTIS-0302 - Authorization Code and PKCE

Core Identity **MUST** support the OAuth 2.0 Authorization Code flow. **Public clients MUST use PKCE** (`code_challenge` / `code_verifier`). Confidential clients SHOULD use PKCE unless alternative client authentication documented in operator policy prevents code interception risk.

**Trace (informative):** RFC 6749, RFC 7636
**Conformance test:** Public client login without PKCE MUST fail; with PKCE MUST succeed.

---

### ODTIS-0303 - JWT tokens and rotation

Core Identity **MUST** issue JWT `access_token` and `id_token`. Expiry durations MUST be operator-configurable. Refresh token rotation MUST be supported for flows that issue refresh tokens. Access token lifetime SHOULD be short enough to limit replay window per operator policy.

**Trace (informative):** RF-12, RNF-05
**Conformance test:** Inspect token claims for `exp`; exercise refresh flow; verify rotated refresh invalidates prior refresh token when rotation enabled.

---

### ODTIS-0304 - MFA and passkeys

Core Identity **MUST** support multi-factor authentication for sensitive operations (defined in operator policy, including step-up before High LoA attribute release where required).

Core Identity **SHOULD** support WebAuthn / passkeys when operator policy enables.

**Trace (informative):** RF-10, DS-11
**Conformance test:** Trigger sensitive operation; verify MFA challenge enforced. WebAuthn test optional at SHOULD level.

---

### ODTIS-0305 - Redirect URI validation

Core Identity **MUST** validate the `redirect_uri` parameter against the registered RP client allowlist. Wildcard redirect URIs MUST NOT be permitted in production unless explicitly documented with compensating controls in operator policy.

**Trace (informative):** RF-23
**Conformance test:** Authorization request with unregistered redirect MUST fail.

---

### ODTIS-0306 - Claims from identity-core state

Custom LoA and verification claims (including `assurance_level` and `identity_verified`) **MUST** be derived from **identity-core state**, not solely from IdP session or token mapper defaults.

If registry LoA changes between token issuance and validation, resource servers and Verification API MUST use current registry state for authorization decisions.

**Trace (informative):** P13 3.3, RF-06
**Conformance test:** Upgrade subject LoA in registry; new token MUST reflect updated LoA; old token MUST NOT authorize above current LoA if policy enforces real-time check.

---

### ODTIS-0307 - Consent-gated custom claims

Attributes beyond standard OIDC claims (`openid`, `profile`, `email`) **MUST NOT** be released in ID Token, UserInfo, or access token custom claims without an **active consent** record for the requesting `client_id` and requested scopes (5).

**Trace (informative):** RF-17, ODTIS-0331
**Conformance test:** Request custom scope without consent; UserInfo MUST omit or deny custom attributes.

---

### ODTIS-0308 - Session end and RP-initiated logout

Core Identity **SHOULD** support [OpenID Connect RP-Initiated Logout 1.0](https://openid.net/specs/openid-connect-rpinitiated-1_0.html) when operator policy enables federated sessions across RPs.

Core Identity **MUST** terminate the IdP browser session on explicit user logout and **MUST** invalidate refresh tokens bound to that session unless operator policy documents an alternative session-binding model.

When front-channel or back-channel logout is enabled, implementations **MUST** propagate logout to registered RPs that advertise `post_logout_redirect_uri` or back-channel logout endpoints in client metadata.

Discovery **SHOULD** publish `end_session_endpoint` when logout is supported (see Annex A Surface S1).

**Trace (informative):** RF-13
**Conformance test:** Complete login; invoke logout; assert IdP session cleared and refresh token rejected.

---

### ODTIS-0309 - Account recovery

Core Identity **MUST** offer **account recovery** flows (password reset and MFA recovery) that verify identity through contact verification, proofing replay, or step-up MFA per operator policy.

Recovery **MUST NOT** bypass LoA or consent requirements for subsequent attribute release.

Recovery endpoints **MUST** enforce rate limiting per ODTIS-0326 and **MUST** emit auditable security events (`identity.recovery.initiated`, `identity.recovery.completed` per 9).

**Trace (informative):** RF-14
**Conformance test:** Initiate recovery; assert identity verification step required; assert rate limit after threshold.

---

### 3.3.1 Standard and custom scopes

**Table 3-3 - Scopes and claims**

| Scope / claim | Purpose |
|---------------|---------|
| `openid`, `profile`, `email` | Standard OIDC claims |
| `assurance_level` | Active LoA (2.3.2) |
| `identity_verified` | Boolean or enum verification status |
| RP-specific scopes | Consented attribute bundles (operator-defined) |

---

## 3.4 Registration and proofing

The proofing pipeline orchestrates contact verification, document capture, biometric verification, manual review, and optional registry escalation (E-Registry).

### ODTIS-0310 - Stable subject_id

Core Identity **MUST** assign a stable, immutable `subject_id` at **first successful registration** (contact or document path). The same natural person re-registering MUST be resolved per operator deduplication policy; duplicate active identities for the same person MUST NOT be created without documented merge procedure.

**Trace (informative):** RF-05
**Conformance test:** Complete registration; verify `subject_id` present and unchanged on subsequent logins.

---

### ODTIS-0311 - Document proofing for Medium LoA

Core Identity **MUST** support document-based proofing sufficient to assign **Medium** LoA per 2.2.1 (valid government-issued ID document plus contact verification).

**Trace (informative):** RF-02, RF-06
**Conformance test:** Submit valid document bundle; assert Medium LoA assigned.

---

### ODTIS-0312 - Biometric proofing for High LoA

Core Identity **MUST** support biometric proofing with **liveness detection** sufficient to assign **High** LoA per ODTIS-0103.

**Trace (informative):** RF-03
**Conformance test:** Biometric path with liveness; assert High LoA. See also `test_high_biometric_gate.md`.

---

### ODTIS-0313 - Manual review queue

Core Identity **MUST** support a **manual review queue** for inconclusive automated proofing (RF-08). Reviewers MUST be able to approve or reject with audit trail; outcomes MUST update identity-core LoA and status.

**Trace (informative):** RF-08
**Conformance test:** Inject inconclusive proofing case; verify queue entry, reviewer action, and final LoA update.

---

### ODTIS-0314 - Biometric minimization

Core Identity **SHOULD** retain biometric **raw images** only per minimization policy. Long-term storage SHOULD use derived scores, templates, or pass/fail outcomes as defined in operator policy. Raw images in temporary storage MUST have documented retention and deletion schedules.

**Trace (informative):** RNF-01, P01 3.6
**Conformance test:** Review operator policy and storage lifecycle; verify raw biometrics not retained beyond declared period.

---

## 3.5 Verification API

The Verification API is a **server-to-server** surface for RP backends distinct from browser OIDC login. OpenAPI paths and schemas are registered in Annex A (`verification-api`).

### ODTIS-0315 - RP client authentication

Core Identity **MUST** expose a Verification API that authenticates RP clients using **OAuth 2.0 client credentials** and/or **mTLS** with RP-issued client certificates per operator policy.

Anonymous or subject-cookie authentication MUST NOT substitute for RP client authentication on this API.

**Trace (informative):** RF-19, RF-21, P14 6
**Conformance test:** Call verify endpoint without client auth MUST return 401; with valid credentials MUST succeed.

---

### ODTIS-0316 - Verification status and LoA

Verification API responses **MUST** include:

- **verification status** (e.g., verified, pending, not_verified); and
- **current active LoA** (`assurance_level`).

See also ODTIS-0108 (LoA on attribute denial).

**Trace (informative):** RF-19, RF-22
**Conformance test:** Verify subject; assert status and LoA fields present and match registry.

---

### ODTIS-0317 - Consented attributes only

Verification API **MUST** return only attributes within **active consented scopes** for the authenticated RP client. Requests outside consent MUST NOT return restricted attribute values (HTTP 403 or empty attribute set with explicit denial code per Annex A error model).

**Trace (informative):** RF-20, RF-17
**Conformance test:** Withhold consent; verify restricted attributes not returned.

---

### ODTIS-0318 - Latency target

Verification API **SHOULD** meet **P95 latency ≤ 2 seconds** under operator-defined reference load compatible with real-time RP flows (RNF-11). Implementations SHOULD publish measured latency in operator SLA or conformance statement when claiming L2+.

**Trace (informative):** RNF-11
**Conformance test:** Load test at reference profile; measure P95; document result.

---

### 3.5.1 Verification API operations (informative)

P14 defines normative-descriptive operations including verify, precheck, and status query. Annex A MUST register operationIds referenced by conformance tests. Minimum Core Identity operations:

| Operation | Purpose |
|-----------|---------|
| Verify subject | Return LoA, status, consented attributes |
| Precheck | RP policy check before redirect to login |
| Health | Liveness for deployment profile 10 |

---

## 3.6 Relying Party management

Operator-controlled registration of OAuth clients and Verification API credentials.

### ODTIS-0319 - RP client registration

Core Identity **MUST** allow operator registration of RP clients with at minimum:

- `client_id` and authentication method;
- allowed **redirect URIs**;
- requested **scopes**; and
- **policies** including minimum LoA (2.7).

**Trace (informative):** RF-23
**Conformance test:** Create RP record via operator API; use client in OIDC flow.

---

### ODTIS-0320 - RP lifecycle

Core Identity **MUST** support **activation**, **deactivation**, and **credential rotation** for RP clients. Deactivated clients MUST NOT obtain new tokens or Verification API access.

**Trace (informative):** RF-24, RF-25
**Conformance test:** Deactivate client; authorization MUST fail. Rotate secret; old secret MUST fail after grace period if configured.

---

### ODTIS-0321 - Client secret protection

RP client secrets **MUST NOT** be stored or transmitted in **clear text**. Storage MUST use one-way hashing or vault encryption; transmission MUST use TLS 1.2+ only.

**Trace (informative):** RNF-02
**Conformance test:** Inspect operator storage configuration documentation; verify no plaintext secret at rest.

---

## 3.7 Citizen portal and transparency

Subject-facing self-service for status, LoA, and consent transparency.

### ODTIS-0322 - Verification status portal

Core Identity **MUST** provide a citizen-facing portal (responsive web minimum) showing:

- current **verification status**; and
- active **LoA**.

**Trace (informative):** RF-28
**Conformance test:** Authenticated subject views portal; status and LoA displayed match registry.

---

### ODTIS-0323 - Consent transparency and revocation

Core Identity **SHOULD** allow citizens to view **connected RPs** and **revoke consents** from the portal. Revocation MUST take effect on subsequent OIDC and Verification API requests (5).

**Trace (informative):** RF-29, RF-16
**Conformance test:** Revoke consent in portal; next API call MUST deny attribute release.

---

### ODTIS-0324 - Locale and responsive web

Citizen-facing flows **MUST** be available in **operator-configured locale(s)**. **Responsive web** is the minimum supported client; native apps MAY be offered additionally.

**Trace (informative):** RF-30, RNF-22
**Conformance test:** Switch locale; UI strings change. Render portal at mobile viewport without horizontal scroll breakage.

---

## 3.8 Core Identity security baseline

Cross-reference detailed threat controls in Annex B and 8.

### ODTIS-0325 - TLS

All **public identity endpoints** (OIDC, Citizen API, Verification API) **MUST** use **TLS 1.2 or higher**. TLS 1.0 and 1.1 MUST NOT be enabled.

**Trace (informative):** RNF-01
**Conformance test:** SSL scan of public endpoints; TLS ≥ 1.2 only.

---

### ODTIS-0326 - Rate limiting

Core Identity **MUST** implement **rate limiting** on authentication and verification endpoints to mitigate credential stuffing and abuse (RF-14).

**Trace (informative):** RF-14, DS-06
**Conformance test:** Exceed configured threshold; receive HTTP 429 with retry guidance.

---

### ODTIS-0327 - Auditable security events

Security events including **login failure**, **consent change**, and **verification** outcomes **MUST** be auditable with **correlation IDs** suitable for cross-service trace (9).

**Trace (informative):** RF-26, RNF-06
**Conformance test:** Trigger login failure and consent change; verify audit events with shared correlation ID in log export.

---

## 3.9 Notification service

OTP and notification delivery for contact verification and step-up flows is a supporting Core Identity capability. Normative event types appear in [Audit event catalog](/registry/events.yaml).

Implementations MUST integrate notification delivery with proofing flows for LoA Low (contact verification). Detailed OTP rate limits and channel policies MAY be defined in operator policy and Book 3; minimum abuse controls MUST align with ODTIS-0326.

---

## 3.10 Wallet and verifiable credentials (optional)

Wallet issuance and OID4VC flows are **not** required for Core Identity conformance. When Extended sub-module **E-Wallet** is declared, normative requirements appear in Annex D and ODTIS-5.4.x (5 cross-ref).

E-Wallet MUST NOT replace identity-core as LoA system of record (ODTIS-2.3, ODTIS-0306).

---

## 3.11 OpenAPI and Annex A

Public REST surfaces in 3.5, 3.7, and operator APIs MUST be registered in **Annex A** with:

- one OpenAPI 3.x document per edge service (P14 10);
- shared error components (`403` consent denied, `429` rate limit);
- `VerifyResponse` required fields matching ODTIS-0316.

OIDC discovery JSON remains authoritative for Surface S1 (IdP); it is not duplicated in VenID OpenAPI bundles.

---

## 3.12 Requirement index

<!-- GENERATED:section-index:START -->
<!-- Generated by scripts/generate-spec-section-indexes.py @ 0.9.0-draft -->

**Table 3-* - Requirement index (27 IDs)**

| ID | Keyword | Summary |
|----|---------|---------|
| ODTIS-0301 | MUST | Core Identity MUST expose `/.well-known/openid-configuration` and JWKS … |
| ODTIS-0302 | MUST | Core Identity MUST support Authorization Code flow; public clients MUST… |
| ODTIS-0303 | MUST | Core Identity MUST issue JWT `access_token` and `id_token` with configu… |
| ODTIS-0304 | SHOULD | Core Identity MUST support MFA for sensitive operations and SHOULD supp… |
| ODTIS-0305 | MUST | Core Identity MUST validate `redirect_uri` against registered RP client… |
| ODTIS-0306 | MUST | Custom LoA and verification claims MUST be derived from identity-core s… |
| ODTIS-0307 | MUST NOT | Attribute claims beyond standard OIDC MUST NOT be released without reco… |
| ODTIS-0308 | MUST | Core Identity MUST terminate IdP session on logout and SHOULD support O… |
| ODTIS-0309 | MUST | Core Identity MUST offer account recovery flows with identity verificat… |
| ODTIS-0310 | MUST | Core Identity MUST assign a stable `subject_id` at first successful reg… |
| ODTIS-0311 | MUST | Core Identity MUST support document-based proofing for Medium LoA |
| ODTIS-0312 | MUST | Core Identity MUST support biometric proofing for High LoA with livenes… |
| ODTIS-0313 | MUST | Core Identity MUST support manual review queue for inconclusive automat… |
| ODTIS-0314 | SHOULD | Core Identity SHOULD retain biometric raw images only per minimization … |
| ODTIS-0315 | MUST | Core Identity MUST expose a verification API authenticating RP clients … |
| ODTIS-0316 | MUST | Verification API responses MUST include verification status and current… |
| ODTIS-0317 | MUST | Verification API MUST return only consented attributes within contracte… |
| ODTIS-0318 | SHOULD | Verification API SHOULD meet P95 latency targets compatible with real-t… |
| ODTIS-0319 | MUST | Core Identity MUST allow operator registration of RP clients with redir… |
| ODTIS-0320 | MUST | Core Identity MUST support activation, deactivation, and credential rot… |
| ODTIS-0321 | MUST NOT | RP client secrets MUST NOT be stored or transmitted in clear text |
| ODTIS-0322 | MUST | Core Identity MUST provide a citizen-facing portal showing verification… |
| ODTIS-0323 | SHOULD | Core Identity SHOULD allow citizens to view connected RPs and revoke co… |
| ODTIS-0324 | MUST | Citizen-facing flows MUST be available in operator-configured locale(s)… |
| ODTIS-0325 | MUST | All public identity endpoints MUST use TLS 1.2 or higher |
| ODTIS-0326 | MUST | Core Identity MUST implement rate limiting on authentication and verifi… |
| ODTIS-0327 | MUST | Security events (login failure, consent change, verification) MUST be a… |

<!-- GENERATED:section-index:END -->

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| stub | 2026-06-12 | Scaffold Phase 3.0 |
| draft v0.5 | 2026-06-12 | 3.1-3.12 normative prose; 25 IDs; +3.1.6, 3.1.7 added to registry |
| 0.9.0-draft | 2026-06-12 | Phase 3.2 section review; requirement index (27 IDs) |

**Phase 3.1 checklist (3).**

- [x] Normative entities from P13 (3.2)
- [x] OIDC, proofing, verification, RP, citizen, security requirements
- [x] Annex A cross-reference (3.11)
- [x] Registry updated to 25 IDs normative


**Phase 3.2 review checklist (3).**

- [x] Registry IDs cited in normative prose
- [x] Requirement index matches registry
- [x] Conformance test stub per ID
- [ ] External review cycle 1 ([Section review matrix](/governance/SECTION-REVIEW/))
