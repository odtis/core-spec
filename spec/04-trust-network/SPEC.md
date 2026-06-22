---
title: "Section 4: Trust network"
description: Exchange gateway, service catalog, access grants, mTLS, metadata-only routing, and trust network audit.
---

# 4 Trust network semantics

<div class="odtis-spec-meta" markdown="1">

| Field | Value |
|-------|-------|
| **Status** | review draft - Phase 3.2 |
| **Spec version** | 0.9.0-draft |
| **Derived from** | P18 6, P04, P05, P08, P06 |
| **Registry IDs** | ODTIS-0201 - ODTIS-0226 (26 requirements) |
| **Profile** | Trust Network (requires Core Identity) |

</div>

---

## 4.1 Scope

This section normatively defines **Layer 2 Trust Network** behavior: governed inter-institution exchange among **partners** under **operator** governance, aligned with X-Road-style security server semantics [X-Road-SA].

Trust Network conformance **requires** Core Identity conformance for the same operator scope (1.7). Cross-network **federation** between independent operators is specified in 6; this section covers single-network and node-to-node exchange within a trust network.

Citizen LoA (2) governs identity assertions on Layer 1. Partner authentication on the exchange gateway is independent and MUST use partner certificates and grants (2.2.3, 4.4).

---

## 4.2 Trust network model

### 4.2.1 Roles

| Role | Definition |
|------|------------|
| **Network node** | Operator deployment exposing an exchange gateway and catalog |
| **Partner** | Institution registered on the network with partner identity and certificate |
| **Provider partner** | Partner exposing catalogued services |
| **Caller partner** | Partner invoking another partner's services |
| **Trust registry** | Operator-maintained registry of partners, certificates, services, and grants |

### 4.2.2 Design principles

1. **Gateway mediation** - Partner traffic enters only through the exchange gateway (ODTIS-0201).
2. **Service-level authorization** - Access is granted per catalogued service, not merely per partner pair (ODTIS-0209).
3. **No backend exposure** - Remote peers reach local services via gateway URLs only (ODTIS-0203).
4. **PKI-backed trust** - Partner identity is cryptographic, documented in operator PKI (4.7).
5. **Audit by default** - Exchange events are logged with correlation IDs (ODTIS-0219).

### 4.2.3 Relationship to Core Identity

Layer 1 identity services MAY be catalogued on the trust network as invokable services. Subject records MUST remain authoritative in identity-core (3.2). Trust network routing MUST NOT duplicate subject system-of-record data stores.

---

## 4.3 Exchange gateway architecture

!!! note "Requirement ID numbering"
    Gateway routing IDs **`ODTIS-4.1.x`** appear in this section (4.3). **`ODTIS-4.2.x`** in 4.4, **`ODTIS-4.3.x`** in 4.5, **`ODTIS-4.4.x`** in 4.6, **`ODTIS-4.5.x`** in 4.7, and **`ODTIS-4.7.x`** in 4.9. Section **4.12** indexes all 21 IDs.

Each network node MUST deploy an **exchange gateway** as the **sole external entry** for partner exchange traffic. Application backends MUST NOT accept unmediated partner connections from the trust network.

### ODTIS-0201 - Gateway-only routing

Trust Network implementations **MUST** route **all partner exchange traffic** through the **local exchange gateway**.

Direct partner-to-backend connections bypassing the gateway MUST be disabled in production Trust Network deployments.

**Trace (informative):** P04
**Conformance test:** Attempt partner call to known backend URL; MUST fail or be unreachable. Same call via gateway MUST succeed when grant exists.

---

### ODTIS-0202 - Receiver and sender modes

The gateway **MUST** operate in **receiver mode** (inbound partner traffic) and **sender mode** (outbound to peer gateways) using a **unified protocol** documented in operator policy or Annex A.

Asymmetric implementations that support only inbound OR outbound MUST NOT claim Trust Network profile.

**Trace (informative):** P04 3
**Conformance test:** Execute inbound and outbound exchange test vectors; both modes pass.

---

### ODTIS-0203 - Peer gateway URLs

Remote nodes **MUST** be reached via **peer gateway base URLs**, not via exposed backend URLs of provider services.

Network configuration MUST map `(partner, service)` to gateway endpoints. Backend URLs MUST remain internal to the provider node.

**Trace (informative):** P04 8
**Conformance test:** Inspect synchronized config; remote routes reference gateway bases only.

---

## 4.4 Transport and partner authentication

### ODTIS-0204 - Mutual TLS

Gateway-to-gateway communication **MUST** use **mutually authenticated TLS (mTLS)** with **partner client certificates** issued under the operator PKI hierarchy (4.7).

TLS 1.2 or higher MUST be used (consistent with ODTIS-0325).

**Trace (informative):** P04, P08, X-Road-SA
**Conformance test:** Establish gateway connection without client cert MUST fail; with valid partner cert MUST succeed.

---

### ODTIS-0205 - Trust registry validation

In **receiver mode**, the gateway **MUST** validate **partner identity** against the **trust registry** (certificate thumbprint, partner ID, revocation status) **before routing** to internal services.

Unknown or revoked partners MUST be rejected.

**Trace (informative):** P04 4
**Conformance test:** Send request with unregistered cert; MUST reject before backend invocation.

---

### ODTIS-0206 - Timestamp and anti-replay

Implementations **SHOULD** validate **request timestamps** and **anti-replay identifiers** (nonce, message ID, or equivalent) on inbound exchange messages.

Operator policy MUST document accepted clock skew and replay window if validation is enabled.

**Trace (informative):** P04 7
**Conformance test:** Replay identical message ID within window; SHOULD reject when policy enabled.

---

### ODTIS-0207 - Message body signatures

Implementations **MAY** require **RSA-SHA256** (or operator-documented equivalent) **body signatures** on exchange messages per operator policy.

When required, receiver mode MUST verify signatures before routing.

**Trace (informative):** P04, P08
**Conformance test:** If policy requires signatures, unsigned body MUST fail verification.

---

## 4.5 Service catalog and grants

Authorization is **service-level**: a caller partner MAY invoke only catalogued services for which an explicit **service access grant** exists.

### ODTIS-0208 - Service catalog

Trust Network **MUST** maintain a **catalog of exposed services** with **stable service identifiers** (immutable IDs across catalog versions unless deprecated with migration notice).

Each entry MUST identify provider partner, service ID, version or compatibility class, and gateway routing metadata.

**Trace (informative):** P04, P05
**Conformance test:** Catalog export contains stable IDs; deprecated services marked without ID reuse.

---

### ODTIS-0209 - Service access grants

Access **MUST** be authorized via **service_access_grants** binding:

| Grant field | Semantics |
|-------------|-----------|
| Caller partner | Institution initiating request |
| Provider partner | Institution exposing service |
| Service ID | Catalogued service identifier |
| Validity | Optional time bounds and conditions |

Requests without matching active grant MUST be rejected at gateway.

**Trace (informative):** P04 6
**Conformance test:** Call service without grant MUST fail; with grant MUST pass mTLS and routing.

---

### ODTIS-0210 - Grants override static permissions

**Static partner permissions**, if used for administrative convenience, **MUST NOT override denied service grants**.

Deny-by-grant MUST take precedence: absence of grant means deny regardless of coarse partner ACL.

**Trace (informative):** P04
**Conformance test:** Configure static allow with explicit grant deny; request MUST fail.

---

### ODTIS-0211 - Auditable grant changes

Grant create, update, revoke, and expire operations **MUST** be **auditable** with actor, timestamp, and correlation ID (9).

**Trace (informative):** RF-26, P10
**Conformance test:** Modify grant; audit log contains before/after or event type with correlation ID.

---

## 4.6 Sender mode and network configuration

Member nodes synchronize catalog and routing metadata for resilient outbound exchange.

### ODTIS-0212 - Route resolution

**Sender mode MUST** resolve remote routes from **synchronized network configuration** (local cache fed by operator registry or peer sync protocol).

Hard-coded peer URLs in application code MUST NOT substitute for synchronized configuration in production.

**Trace (informative):** P04 5
**Conformance test:** Update remote route in registry; sender resolves new gateway URL after sync without code deploy.

---

### ODTIS-0213 - Cache refresh policy

Cache refresh interval **MUST** be **operator-configurable**. **Stale cache behavior** (fail closed, fail open with logging, or grace period) **MUST** be **documented in operator policy**.

Production deployments SHOULD fail closed or use short grace periods for security-sensitive routes.

**Trace (informative):** P04
**Conformance test:** Operator policy documents stale behavior; simulate stale cache per documented rule.

---

### ODTIS-0214 - Autodiscovery (@VenPartnerService)

Implementations **SHOULD** support the **`@VenPartnerService`** autodiscovery pattern for **multi-node service registration** within a partner organization (P05).

When supported, autodiscovery MUST register services into the catalog without manual per-endpoint duplication.

!!! note "FB-004 - Autodiscovery scope @ 0.9.0-draft"
    Autodiscovery is **SHOULD-only** for review draft; promotion to MUST is deferred to Phase 4 pending Book 2 ch.9 and a discovery well-known URI. It is **out of Annex A OpenAPI scope** (frozen bundles). Conformance uses the manual stub [Test Odtis 4 4 3](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_odtis-4_4_3.md). See [FB-004 autodiscovery](/governance/review/clarify-003-autodiscovery-should/).

**Trace (informative):** P05
**Conformance test:** Register service via autodiscovery annotation or equivalent; catalog lists resolvable entry.

---

## 4.7 PKI, revocation, and timestamping

Operational PKI underpins partner certificates, optional message signing, and audit non-repudiation. Detailed ceremony rules also appear in 7 for Operator profile.

### ODTIS-0215 - PKI hierarchy

Trust Network **MUST** operate a **documented PKI hierarchy** for **partner and service certificates**, including root/intermediate CA roles, issuance policy, and certificate profiles.

**Trace (informative):** P08
**Conformance test:** Review PKI documentation; partner certs chain to documented trust anchor.

---

### ODTIS-0216 - Revocation checking

Implementations **MUST** validate **certificate revocation** (**CRL** or **OCSP** per operator policy) **before exchange**.

Revoked partner certificates MUST be rejected even if grant exists.

**Trace (informative):** P08 4
**Conformance test:** Revoke partner cert; next mTLS handshake MUST fail.

---

### ODTIS-0217 - Trusted timestamping

Trust Network **SHOULD** support **trusted timestamping** for signed exchange messages where operator policy requires non-repudiation or long-term audit validity.

**Trace (informative):** P08 6
**Conformance test:** If policy requires TSA, verify timestamp token on signed message.

---

### ODTIS-0218 - PKI ceremony documentation

**PKI ceremony documentation MUST** be maintained by the **DTI operator**, covering CA key generation, issuance, rotation, and disaster recovery (cross-ref 7).

**Trace (informative):** P08 7, P10
**Conformance test:** Conformance statement references current CPS or ceremony document version.

---

## 4.8 VenID trust exchange product requirements

Normative product requirements derived from Book 1 decisions **D3** (hub gateway), **D4** (route messages without payload centralization), and VenID platform exchange analysis (Fase 4 multi-node routing).

### ODTIS-0222 - Catalog gateway base URL

Synchronized service catalog entries for remote peers **MUST** include stable **service_id** and peer **gateway_base_url** suitable for sender route resolution.

**Trace (informative):** Book 1 D3, platform FASE-4
**Conformance test:** Catalog export contains `gateway_base_url` for each remote peer service; sender resolves route without backend URL leak.

### ODTIS-0223 - Multi-peer sender routing

Sender gateway **MUST** resolve outbound routes by **service_id** from synchronized catalog **without** requiring a single hard-coded remote gateway URL for all peers.

**Trace (informative):** platform FASE-4, P05
**Conformance test:** Configure two remote peers; sender selects correct gateway per service_id.

### ODTIS-0224 - Grant fail closed

Exchange gateway **MUST** fail closed when service grant validation fails; **MUST NOT** route on implicit network-zone trust.

**Trace (informative):** Book 2 ch.3.7 rule 1, Book 1 D4
**Conformance test:** Denied grant - exchange rejected before backend invocation.

### ODTIS-0225 - No payload centralization

Trust network metadata stores **MUST NOT** persist full business payloads as authoritative copies; routing metadata and audit envelopes only.

**Trace (informative):** Book 1 D4, P01 metadata model
**Conformance test:** Architecture review confirms payloads remain in agency systems; trust layer stores grants and audit metadata only.

### ODTIS-0226 - Grant workflow audit

Grant request, approval, and revocation workflows **MUST** emit auditable events when operator policy uses explicit service access grants.

**Trace (informative):** platform ANALISIS catalog/grants, P04
**Conformance test:** Grant lifecycle produces auditable events with correlation IDs.

---

## 4.9 FAL controls cross-reference

Gateway mTLS, signing, timestamping, and PKI path validation implement **Federation Assurance Level (FAL)** controls documented in ODTIS-0106. Trust Network operators MUST publish FAL mapping in operator policy when claiming Trust Network profile.

---

## 4.10 Audit, SLA, and zero trust

### ODTIS-0219 - Exchange audit events

**Exchange events MUST** be logged with **correlation IDs** suitable for **regulator export** and cross-service tracing (9).

Minimum logged fields SHOULD include: timestamp, caller partner, provider partner, service ID, grant ID, message ID, outcome, correlation ID.

**Trace (informative):** RF-26, P10
**Conformance test:** Execute exchange; audit export contains correlation ID linking gateway and backend logs.

---

### ODTIS-0220 - Gateway SLA

The DTI operator **MUST** publish **SLA targets for gateway availability** compatible with Core Identity **RNF-07** when **both** Core Identity and Trust Network profiles are claimed.

SLA MUST include measurement window, availability percentage or error budget, and exclusion policy.

**Trace (informative):** RNF-07, P10
**Conformance test:** Conformance statement or operator policy includes gateway availability SLA.

---

### ODTIS-0221 - Zero trust alignment

Trust Network **SHOULD** align **zero trust controls** with **NIST SP 800-207** per deployment profile (P06): least privilege on internal routing, continuous verification of partner identity, and segmented backend access from gateway.

**Trace (informative):** P06, NIST-800-207
**Conformance test:** Architecture review maps gateway controls to zero trust principles (L2+ documentation).

---

## 4.11 Federation boundary

Bilateral federation between **independent** trust networks is normatively defined in **6** (ODTIS-6.x). This section applies to exchange **within** a network or via explicitly activated federation agreements.

Implementations MUST NOT infer transitive trust across three or more networks without pairwise federation (6.1).

---

## 4.12 Informative standards alignment

| Referent | ODTIS mapping |
|----------|---------------|
| X-Road security architecture | Gateway mediation, mTLS, message signing [X-Road-SA] |
| NIST SP 800-207 | Zero trust deployment profile (ODTIS-0221) |
| NIST SP 800-63-3 FAL | Documented in 2.5.2 |

Full standards crosswalk: Annex C.

---

## 4.13 Requirement index

<!-- GENERATED:section-index:START -->
<!-- Generated by scripts/generate-spec-section-indexes.py @ 0.9.0-draft -->

**Table 4-* - Requirement index (26 IDs)**

| ID | Keyword | Summary |
|----|---------|---------|
| ODTIS-0201 | MUST | Trust Network implementations MUST route all partner exchange traffic t… |
| ODTIS-0202 | MUST | The gateway MUST operate in receiver and sender modes with a unified pr… |
| ODTIS-0203 | MUST | Remote nodes MUST be reached via peer gateway base URLs, not exposed ba… |
| ODTIS-0204 | MUST | Gateway-to-gateway communication MUST use mutually authenticated TLS wi… |
| ODTIS-0205 | MUST | Receiver mode MUST validate partner identity against the trust registry… |
| ODTIS-0206 | SHOULD | Implementations SHOULD validate request timestamps and anti-replay iden… |
| ODTIS-0207 | MAY | Implementations MAY require RSA-SHA256 body signatures per operator pol… |
| ODTIS-0208 | MUST | Trust Network MUST maintain a catalog of exposed services with stable s… |
| ODTIS-0209 | MUST | Access MUST be authorized via service_access_grants binding caller, pro… |
| ODTIS-0210 | MUST NOT | Static partner permissions, if used, MUST NOT override denied service g… |
| ODTIS-0211 | MUST | Grant changes MUST be auditable |
| ODTIS-0212 | MUST | Sender mode MUST resolve remote routes from synchronized network config… |
| ODTIS-0213 | MUST | Cache refresh MUST be configurable; stale cache behavior MUST be docume… |
| ODTIS-0214 | SHOULD | Autodiscovery pattern (`@VenPartnerService`) SHOULD be supported for mu… |
| ODTIS-0215 | MUST | Trust Network MUST operate a documented PKI hierarchy for partner and s… |
| ODTIS-0216 | MUST | Implementations MUST validate certificate revocation (CRL or OCSP per o… |
| ODTIS-0217 | SHOULD | Trust Network SHOULD support trusted timestamping for signed exchange m… |
| ODTIS-0218 | MUST | PKI ceremony documentation MUST be maintained by the DTI operator |
| ODTIS-0219 | MUST | Exchange events MUST be logged with correlation IDs suitable for regula… |
| ODTIS-0220 | MUST | DTI operator MUST publish SLA targets for gateway availability compatib… |
| ODTIS-0221 | SHOULD | Trust Network SHOULD align zero trust controls with NIST SP 800-207 per… |
| ODTIS-0222 | MUST | Synchronized service catalog entries for remote peers MUST include stab… |
| ODTIS-0223 | MUST | Sender gateway MUST resolve outbound routes by service_id from synchron… |
| ODTIS-0224 | MUST | Exchange gateway MUST fail closed when service grant validation fails; … |
| ODTIS-0225 | MUST NOT | Trust network metadata stores MUST NOT persist full business payloads a… |
| ODTIS-0226 | MUST | Grant request, approval, and revocation workflows MUST emit auditable e… |

<!-- GENERATED:section-index:END -->

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| stub | 2026-06-12 | Scaffold Phase 3.0 |
| draft v0.5 | 2026-06-12 | 4.1-4.12 normative prose; 21 IDs |
| 0.9.0-draft | 2026-06-12 | Phase 3.2 section review; FB-004 autodiscovery scope; index table fix |

**Phase 3.1 checklist (4).**

- [x] Gateway architecture and mTLS (4.3-4.4)
- [x] Catalog, grants, sender cache (4.5-4.6)
- [x] PKI and audit/SLA (4.7, 4.9)
- [x] Cross-ref 6 federation boundary (4.10)


**Phase 3.2 review checklist (4).**

- [x] Registry IDs cited in normative prose
- [x] Requirement index matches registry
- [x] Conformance test stub per ID
- [ ] External review cycle 1 ([Section review matrix](/governance/SECTION-REVIEW/))
- [x] FB-004 autodiscovery SHOULD scope ([FB-004 autodiscovery](/governance/review/clarify-003-autodiscovery-should/))
