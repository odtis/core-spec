---
title: "Section 8: Security"
description: Security controls, OWASP baseline, fail-closed behavior, transport security, and incident reporting for ODTIS.
---

# 8 Security requirements

<div class="odtis-spec-meta" markdown="1">

| Field | Value |
|-------|-------|
| **Status** | review draft - Phase 3.2 |
| **Spec version** | 0.9.0-draft |
| **Derived from** | P18 9.1-9.2, P06, P07, DS-02, DS-06 |
| **Registry IDs** | ODTIS-0517 - ODTIS-0525, ODTIS-0535 (10 requirements) |
| **Profiles** | Trust Network (8.1); Core Identity + Operator (8.2) |

</div>

---

## 8.1 Scope

This section normatively defines **security controls** for ODTIS implementations. It complements:

- transport and endpoint controls in 3.9 and 4.4;
- PKI stewardship in 7.4;
- privacy rules in 5; and
- informative threat-to-control mapping in **Annex B** (P07).

ODTIS references NIST SP 800-207 zero trust practice [NIST-800-207] without duplicating every control identifier from P06. Annex B provides the full mitigation matrix for auditors.

---

## 8.2 Zero trust and infrastructure security

!!! note "Requirement ID numbering"
    Trust Network infrastructure controls use registry IDs **`ODTIS-0517`..`ODTIS-0520`** (prose in this section, 8.2). Identity-layer mitigations use **`ODTIS-0521`..`ODTIS-0525`** (prose in 8.3). Section **8.7** indexes all nine IDs.

Requirements in 8.2 apply when **Trust Network** and/or **Operator** profiles are claimed. Several apply to any deployment handling sensitive identity data.

### 8.2.1 Zero trust principles (informative)

| Principle | ODTIS expression |
|-----------|------------------|
| Never trust, always verify | ODTIS-0517 per-request partner verification |
| Least privilege | Service grants (4.5), internal network segmentation |
| Assume breach | Audit, fraud monitoring (ODTIS-0525), incident response (7.6) |
| Explicit verification | mTLS, registry validation (4.4) |

---

### ODTIS-0517 - Per-request partner verification

Trust Network implementations **MUST** verify **partner identity on every exchange request**. **Implicit network-zone trust MUST NOT** substitute for certificate, registry, and grant checks at the gateway.

Each inbound exchange request MUST re-validate partner certificate, registry entry, grant authorization, and revocation status (4.4, 4.5).

**Trace (informative):** P06, NIST-800-207
**Conformance test:** Remove grant mid-session; next request MUST fail despite prior success in same TCP session.

---

### ODTIS-0518 - Internal service exposure

Internal microservices handling **sensitive identity data** (identity-core, consent-service, verification-engine, PKI signing services) **MUST NOT** be exposed to the **public internet**.

Public integration MUST terminate at API gateway, OIDC edge, or exchange gateway only. Administrative access MUST use separate protected channels.

**Trace (informative):** P06, DS-02
**Conformance test:** External port scan / architecture review confirms internal services reachable only from private network or service mesh.

---

### ODTIS-0519 - Secrets management

**Secrets** including **RP client secrets** and **PKI private keys MUST** be stored in a **dedicated secrets manager** (Vault pattern or HSM-backed equivalent), not in source code, container images, or plaintext configuration files.

Runtime injection MUST use short-lived credentials where supported.

**Trace (informative):** DS-06, P08
**Conformance test:** Configuration audit finds no plaintext secrets in repos or env files; secrets manager references documented.

---

### ODTIS-0520 - Zero trust maturity roadmap

Implementations **SHOULD** progress toward the **full zero-trust profile** defined in operator phase plan (P06 6, 10).

Conformance statements SHOULD document current zero-trust maturity tier and planned controls by deployment phase.

**Trace (informative):** P06 6
**Conformance test:** Review phase plan mapping P06 controls to deployment timeline (L2+).

---

## 8.3 Identity-layer threat mitigations

Requirements in 8.3 apply to **Core Identity** and **Operator** profiles. Annex B maps threats T-xxx to these controls.

### ODTIS-0521 - OWASP-informed web security

Core Identity **MUST** resist common web attacks per **OWASP-informed design**, including at minimum:

| Category | Control expectation |
|----------|---------------------|
| Injection | Parameterized queries; input validation on APIs |
| XSS | Output encoding; CSP on citizen portal |
| CSRF | Token validation on state-changing citizen flows |
| Broken authentication | OIDC hardening (3.3), rate limits (ODTIS-0326) |

**Trace (informative):** RNF-03, P07
**Conformance test:** Security assessment or automated DAST on public surfaces; critical findings remediated or documented with compensating controls.

---

### ODTIS-0522 - MFA availability

**MFA MUST** be **available** for **sensitive citizen and operator actions** (also ODTIS-0304).

Sensitive actions MUST be defined in operator policy (for example: step-up before High LoA release, operator console login, consent changes for high-risk scopes).

**Trace (informative):** RF-10, P07
**Conformance test:** Trigger defined sensitive action; MFA challenge MUST be offered or enforced.

---

### ODTIS-0523 - Liveness in proofing

The proofing pipeline **MUST** include **liveness detection** for **High LoA biometric verification** (consistent with ODTIS-0103, ODTIS-0312).

Static photo or pre-recorded video attacks MUST be rejected by liveness controls.

**Trace (informative):** RF-03, P07
**Conformance test:** Submit non-live biometric capture; High LoA assignment MUST fail.

---

### ODTIS-0524 - Wallet holder signatures

When **Extended sub-module E-Wallet** is declared, wallet **Verifiable Presentations MUST** require **holder signature** (OID4VP or equivalent).

Presentations without valid holder proof MUST be rejected by verifiers.

**Trace (informative):** P07 7, ODTIS-0340
**Conformance test:** Present VP without holder signature; verifier MUST reject.

---

### ODTIS-0525 - Fraud monitoring

The **operator MUST** maintain **fraud monitoring metrics**, including at minimum:

- impersonation or synthetic identity attempt counts;
- manual review queue depth and **SLA** (time to resolution); and
- anomalous verification failure rates by RP or channel.

Metrics MUST feed operator incident response (ODTIS-0515) and MAY be exported in aggregated form (ODTIS-0513).

**Trace (informative):** P07 8.5
**Conformance test:** Review fraud dashboard or metric export; manual review SLA documented and measured.

---

### ODTIS-0535 - Fail-closed denial paths

**Authentication, consent evaluation, and grant denial paths MUST fail closed**:

- no partial attribute release when consent or grant checks fail;
- no implicit trust fallback to anonymous or default partner context; and
- error responses MUST NOT leak attributes beyond what the failed check would have permitted.

This rule applies across Core Identity OIDC flows, Verification API gates, and Trust Network exchange authorization (cross-ref ODTIS-0224, ODTIS-0331).

**Trace (informative):** Book 2 ch. 3.7 rule 1, Book 1 D5
**Conformance test:** Deny consent and grant in sequence; verify zero attribute leakage and no fallback session.

---

## 8.4 Annex B cross-reference

**Table 8-1 - Threat -> ODTIS control mapping (informative sample)**

| Threat area | Primary ODTIS controls | Annex B |
|-------------|------------------------|---------|
| Consent bypass | ODTIS-0331, ODTIS-0521 | T-consent-* |
| Token replay | ODTIS-0303, ODTIS-0521 | T-token-* |
| Partner impersonation | ODTIS-0205, ODTIS-0517 | T-gateway-* |
| Biometric spoof | ODTIS-0523 | T-bio-* |
| Secret leakage | ODTIS-0519, ODTIS-0321 | T-secret-* |
| Insider / lateral movement | ODTIS-0518, ODTIS-0520 | T-zt-* |

Full threat rows are in [Threat mitigations catalog](/annexes/B-threat-mitigations/threats.yaml) (Annex B draft v0.9.0-draft). Each **ODTIS-05xx** security ID is cross-referenced in at least one Annex B row.

---

## 8.5 Cryptography (informative baseline)

Operator policy MUST document approved algorithms and key lengths for:

- TLS (≥1.2; preferred 1.3);
- JWT signing (RS256 or documented equivalent);
- document and message hashing; and
- optional exchange body signatures (ODTIS-0207).

Deprecated algorithms (MD5, SHA-1 for signatures, TLS 1.0/1.1) MUST NOT be used for new deployments.

---

## 8.6 Cross-references

| Topic | Section / ID |
|-------|----------------|
| TLS on public endpoints | ODTIS-0325 |
| Rate limiting | ODTIS-0326 |
| Gateway mTLS | ODTIS-0204 |
| CP/CPS and ceremonies | 7.4 |
| Zero trust (Trust Network) | ODTIS-0221 |
| Incident response | ODTIS-0515 |

---

## 8.7 Requirement index

<!-- GENERATED:section-index:START -->
<!-- Generated by scripts/generate-spec-section-indexes.py @ 0.9.0-draft -->

**Table 8-* - Requirement index (10 IDs)**

| ID | Keyword | Summary |
|----|---------|---------|
| ODTIS-0517 | MUST | Trust Network implementations MUST verify partner identity on every exc… |
| ODTIS-0518 | MUST NOT | Internal microservices handling sensitive identity data MUST NOT be exp… |
| ODTIS-0519 | MUST | Secrets (RP client secrets, PKI keys) MUST be stored in a dedicated sec… |
| ODTIS-0520 | SHOULD | Implementations SHOULD progress toward full zero-trust profile per oper… |
| ODTIS-0521 | MUST | Core Identity MUST resist common web attacks (injection, XSS, CSRF, bro… |
| ODTIS-0522 | MUST | MFA MUST be available for sensitive citizen and operator actions |
| ODTIS-0523 | MUST | Proofing pipeline MUST include liveness detection for High LoA biometri… |
| ODTIS-0524 | MUST | Wallet presentations (E-Wallet) MUST require holder signature on Verifi… |
| ODTIS-0525 | MUST | Operator MUST maintain fraud monitoring metrics (impersonation attempts… |
| ODTIS-0535 | MUST | Auth, consent, and grant denial paths MUST fail closed without partial … |

<!-- GENERATED:section-index:END -->

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| stub | 2026-06-12 | Scaffold Phase 3.0 |
| draft v0.5 | 2026-06-12 | 8.1-8.7 normative prose; 9 IDs |
| 0.9.0-draft | 2026-06-12 | Phase 3.2 section review; Annex B cross-ref; index table fix |

**Phase 3.1 checklist (8).**

- [x] Zero trust and infrastructure controls (8.1.x)
- [x] Identity-layer mitigations (8.2.x)
- [x] Annex B cross-reference table (sample)
- [x] Full Annex B threat rows linked (Annex B draft v0.5)


**Phase 3.2 review checklist (8).**

- [x] Registry IDs cited in normative prose
- [x] Requirement index matches registry
- [x] Conformance test stub per ID
- [ ] External review cycle 1 ([Section review matrix](/governance/SECTION-REVIEW/))
