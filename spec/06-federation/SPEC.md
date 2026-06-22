---
title: "Section 6: Federation"
description: Bilateral federation agreements, non-transitivity, routing, regulator export, and federated trust establishment.
---

# 6 Federation

<div class="odtis-spec-meta" markdown="1">

| Field | Value |
|-------|-------|
| **Status** | review draft - Phase 3.2 |
| **Spec version** | 0.9.0-draft |
| **Derived from** | P18 6.6, P09, P10 |
| **Registry IDs** | ODTIS-0401 - ODTIS-0408 (8 requirements) |
| **Profile** | Federation (requires Trust Network + Core Identity) |

</div>

---

## 6.1 Scope

This section normatively defines **bilateral federation** between **independent trust network instances** (operators). Federation enables controlled cross-network exchange without merging trust anchors, registries, or certificate authorities.

Federation conformance **requires** Trust Network and Core Identity profiles for the declaring operator (1.7). Intra-network exchange within a single instance is governed by 4 alone.

**Non-transitivity** is a core ODTIS rule: trust MUST NOT propagate across three or more networks without explicit pairwise agreements.

---

## 6.2 Federation model

### 6.2.1 Trust instance

A **trust instance** is an independently operated Trust Network deployment identified by a stable **instance identifier** (for example, `VENID-VE`, `VENID-NORDIC-01`).

Each instance maintains:

- its own trust registry and PKI hierarchy (4.7);
- its own service catalog and grants (4.5); and
- its own exchange gateway endpoints.

Instances MUST NOT share a single trust anchor or merged partner registry in production federation mode unless documented as a single-instance deployment (not federation).

### 6.2.2 Federation agreement

A **federation agreement** is a **bilateral** policy record between two trust instances **A** and **B** specifying:

| Field | Semantics |
|-------|-----------|
| Local instance | Declaring operator's instance ID |
| Remote instance | Peer instance ID |
| Direction | Outbound allowed services and inbound acceptance policy |
| Remote trust material | Pinned remote CA certificate and/or allowed gateway certificate thumbprints |
| Service whitelist | Federated services callable under the agreement |
| Validity | Effective and expiry dates; suspension state |
| Metadata | Operator notes, legal reference, contact |

Agreements are configured **independently on each side**: A configures A->B; B configures B->A. Symmetric operational configuration is required for bidirectional exchange but is not automatic discovery.

### ODTIS-0404 - Required federation agreement fields

Before **outbound federated routing** is enabled for a remote instance, the local federation agreement **MUST** include at minimum:

1. **remote instance identifier** (stable instance ID);
2. **validity window** (effective and expiry dates, or equivalent time-bound policy); and
3. **pinned remote trust material** (remote CA certificate and/or allowed gateway certificate thumbprints per 6.2.2).

Implementations MUST NOT route federated traffic to a remote instance when any required field is missing, expired, or suspended.

**Trace (informative):** P09, FB-002
**Conformance test:** Agreement missing pinned CA or instance ID - outbound federated routing MUST remain disabled.

### 6.2.3 Federated service

A **federated service** is a catalog entry exposed by a **remote instance** that local sender gateways MAY route to when:

1. a federation agreement authorizes the remote instance; and
2. a **service access grant** (4.5) or federated equivalent authorizes the specific service.

Federated catalog entries MUST be marked with remote instance identity and MUST NOT appear as local backend URLs in synchronized configuration (ODTIS-0203).

---

## 6.3 Non-transitivity

**Table 6-1 - Transitivity rules**

| Relationship | Permitted? |
|--------------|------------|
| A federated with B (explicit agreement) | Yes |
| B federated with C (separate agreement) | Yes |
| A reaches C **through B** without A↔C agreement | **No** |
| Implicit trust propagation via shared intermediary | **No** |

Implementations MUST enforce non-transitivity at:

- **routing** - sender gateway MUST NOT follow multi-hop federated paths through an intermediary instance; and
- **policy** - absence of direct A↔C federation agreement MUST deny A->C exchange even if A↔B and B↔C exist.

---

### ODTIS-0401 - Bilateral federation and non-transitivity

Federated exchange **MUST** be **bilateral**. **Non-transitivity MUST** be preserved.

Gateway routing tables and federation policy engines MUST reject requests that would reach a third instance without a direct federation agreement between source and target instances.

**Trace (informative):** P09
**Conformance test:** Configure A↔B and B↔C agreements without A↔C. Attempt A->C via B route - MUST fail. A->B direct - MUST succeed when grant exists.

---

### ODTIS-0405 - Direct bilateral route requirement

The **sender gateway MUST** reject **federated routes** when a **direct bilateral agreement** between source and target instances is absent, **even if** a transitive path exists through a third instance.

This requirement applies at route selection time before mTLS establishment to the remote federated gateway. Multi-hop federation paths MUST NOT be synthesized from pairwise agreements.

**Trace (informative):** P09, FB-002
**Conformance test:** A↔B and B↔C configured; attempt A->C via B - MUST fail at sender routing policy.

---

## 6.4 Authentication and federation policy

Cross-instance exchange uses gateway-to-gateway mTLS (4.4) with **network-specific** trust material distinct from intra-network partner certificates.

### ODTIS-0402 - Network-specific authentication

Federated partners **MUST** authenticate with **network-specific certificates** and **federation policy** defined in the federation agreement.

Receiver mode MUST:

1. identify inbound client certificate against federation agreements before standard local partner validation; and
2. reject certificates valid locally but not pinned or CA-authorized for the remote instance.

Outbound sender mode MUST present credentials registered with the remote instance per agreement.

**Trace (informative):** P09 6
**Conformance test:** Present valid local partner cert without federation pinning - federated path MUST fail. Present agreement-pinned remote cert - MUST succeed.

---

## 6.5 Activation and deployment phases

Federation is a **Phase 3-4** capability in the VenID deployment roadmap (10). Phases 1-2 operate single-hub topology within one trust instance without cross-instance routing.

### ODTIS-0403 - Explicit federation activation

**Federation activation MUST** be **explicit** per **deployment phase** documented by the operator.

Operators MUST NOT claim Federation profile conformance while running Phase 1-2 single-instance topology only. Conformance statements MUST list:

- active federation agreements (instance pairs); and
- deployment phase at which federation was activated.

Suspension or expiry of an agreement MUST disable federated routing immediately on subsequent requests.

**Trace (informative):** P09 9, P10
**Conformance test:** Review conformance statement phase and agreement list. Deactivate agreement - federated calls MUST fail.

---

## 6.6 Protocol behavior

### 6.6.1 Outbound (sender) flow

1. Resolve `service_id` in synchronized catalog; if `federated=true`, select remote instance and gateway base URL from federation metadata.
2. Load federation agreement for remote instance; verify agreement active and service whitelisted.
3. Establish mTLS to remote gateway using federation credentials.
4. Apply 4 grant checks on federated service invocation where applicable.
5. Log exchange with correlation ID including local and remote instance IDs (ODTIS-0219).

### 6.6.2 Inbound (receiver) flow

1. Terminate mTLS at local gateway.
2. Match client certificate to federation agreement (remote instance identity).
3. Validate service request against federated whitelist and grants.
4. Route to local backend or reject.
5. Emit federated audit event.

### 6.6.3 LoA and identity data across federation

Citizen LoA and subject attributes crossing federation boundaries MUST:

- preserve **assurance_level** semantics per 2 and operator cross-border mapping (ODTIS-0105); and
- respect **consent** and purpose limitation on Layer 1 when identity payloads traverse federated identity services (5).

Federation authenticates **institutions and services**, not citizens on the wire (2.2.3).

---

## 6.7 Catalog extension

Federated services in catalog sync MUST include at minimum:

| Field | Purpose |
|-------|---------|
| `federated` | Boolean indicator |
| `trust_instance_id` | Remote instance identifier |
| `remote_service_id` | Stable ID in remote catalog |
| `gateway_base_url` | Remote peer gateway URL |

Sender route resolution (ODTIS-0212) MUST support federated entries without code changes per remote instance.

---

## 6.8 Audit and operator duties

Federated exchange MUST emit audit events distinguishable from intra-network exchange, including:

- local instance ID;
- remote instance ID;
- federation agreement ID; and
- correlation ID (ODTIS-0219).

Operators MUST maintain bilateral agreement documentation accessible for regulator export (7, 9).

### ODTIS-0406 - Regulator export of federation agreements

When the **Federation profile** is claimed, operators **SHOULD** publish **federation agreement metadata** to regulators through the **Regulator API** export surface (Annex A S8) or an equivalent audited export documented in operator policy.

Minimum export metadata SHOULD include instance pair, agreement validity, suspension state, and last change timestamp. PII MUST NOT appear in federation agreement export payloads.

**Trace (informative):** P09, P10, ODTIS-0514, ODTIS-0530
**Conformance test:** Verify export path or documented deferral in operator policy when Federation profile is declared.

---

### ODTIS-0407 - Agreement suspension disables routing

**Suspended or expired federation agreements MUST** disable **federated routing** on subsequent requests within documented cache refresh bounds.

**Trace (informative):** P09, Book 1 D9
**Conformance test:** Suspend agreement; federated call on next request MUST fail.

---

### ODTIS-0408 - Federated audit instance identifiers

**Federated exchange audit events MUST** include **local trust instance identifier** and **remote trust instance identifier**.

**Trace (informative):** Book 2 ch.6.8, P09
**Conformance test:** Federated exchange audit export contains both instance IDs.

---

## 6.9 Relationship to identity federation (informative)

SAML/OIDC **identity federation** (browser SSO between IdPs) is distinct from **trust network federation** in this section. ODTIS Federation profile governs **institutional exchange gateways**. OIDC cross-border login MAY coexist but MUST NOT substitute for ODTIS-6.1.x gateway controls.

---

## 6.10 Requirement index

<!-- GENERATED:section-index:START -->
<!-- Generated by scripts/generate-spec-section-indexes.py @ 0.9.0-draft -->

**Table 6-* - Requirement index (8 IDs)**

| ID | Keyword | Summary |
|----|---------|---------|
| ODTIS-0401 | MUST | Federated exchange MUST be bilateral; non-transitivity MUST be preserved |
| ODTIS-0402 | MUST | Federated partners MUST authenticate with network-specific certificates… |
| ODTIS-0403 | MUST | Federation activation MUST be explicit per deployment phase documented … |
| ODTIS-0404 | MUST | Federation agreements MUST include remote instance identifier, validity… |
| ODTIS-0405 | MUST | Sender gateway MUST reject federated routes when direct bilateral agree… |
| ODTIS-0406 | SHOULD | Operators SHOULD publish federation agreement metadata to regulators vi… |
| ODTIS-0407 | MUST | Suspended or expired federation agreements MUST disable federated routi… |
| ODTIS-0408 | MUST | Federated exchange audit events MUST include local trust instance ident… |

<!-- GENERATED:section-index:END -->

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| stub | 2026-06-12 | Scaffold Phase 3.0 |
| draft v0.5 | 2026-06-12 | 6.1-6.10 normative prose; 3 IDs |
| 0.9.0-draft | 2026-06-12 | Phase 3.2 section review; FB-002 adds ODTIS-0404-6.2.1 (6 IDs) |

**Phase 3.1 checklist (6).**

- [x] Bilateral model and non-transitivity (6.2-6.3)
- [x] Federation handshake and auth policy (6.4, 6.6)
- [x] Phase-gated activation (6.5)
- [x] Federation profile conformance test stubs


**Phase 3.2 review checklist (6).**

- [x] Registry IDs cited in normative prose
- [x] Requirement index matches registry
- [x] Conformance test stub per ID
- [ ] External review cycle 1 ([Section review matrix](/governance/SECTION-REVIEW/))
- [x] FB-002 federation depth RFC ([Federation interoperability RFC](/governance/rfc/2026-06-12-federation-interoperability/))
