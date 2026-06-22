---
title: "Section 9: Audit and events"
description: Audit event catalog, JSON schemas, envelope format, correlation IDs, and retention requirements.
---

# 9 Audit and events

<div class="odtis-spec-meta" markdown="1">

| Field | Value |
|-------|-------|
| **Status** | review draft - Phase 3.2 |
| **Spec version** | 0.9.0-draft |
| **Derived from** | P18 9.3, DS-07, Book 2 Appendix F |
| **Registry IDs** | ODTIS-0526 - ODTIS-0531 (6 requirements) |
| **Profiles** | Core Identity (9.1-9.2); Trust Network (9.3); Operator (9.4); Extended E-Webhook (9.5) |

</div>

---

## 9.1 Scope

This section normatively defines **audit events**, **event envelopes**, **storage and export** rules, and **webhook integrity** for ODTIS implementations.

Audit provides:

- accountability for identity, consent, and exchange actions;
- correlation across microservices and gateway hops; and
- regulator-supervised export with PII minimization (ODTIS-0514, ODTIS-0530).

Event nomenclature follows **`resource.action`** (DS-07). The machine-readable catalog is [Audit event catalog](/registry/events.yaml). JSON Schemas are under [Event JSON schemas](/registry/events/schemas/).

---

## 9.2 Event envelope

!!! note "Requirement ID numbering"
    Registry IDs use the **`ODTIS-05xx`** domain (Governance). **`ODTIS-0529`** (envelope) appears in this section; **`ODTIS-0526`..`ODTIS-0528`** in 9.3; **`ODTIS-0526`** in 9.4; **`ODTIS-0530`** in 9.5; **`ODTIS-0531`** in 9.6. Section **9.9** indexes all six IDs. Subsection numbers such as "9.2.1" below are **not** ODTIS requirement IDs.

All auditable events MUST use a **standard header envelope** regardless of transport (message bus, log append, webhook).

### ODTIS-0529 - Header envelope

Event payloads **MUST** include in the header envelope at minimum:

| Field | Semantics |
|-------|-----------|
| `trace_id` | Correlation identifier propagated across services (W3C Trace Context compatible RECOMMENDED) |
| `timestamp` | Event time in UTC (ISO 8601) |
| `event_id` | Unique event instance ID |
| `event_type` | Stable type string (catalog ID) |
| `source` | Emitting service or component |
| `operator_id` | Instance or tenant identifier (optional for multi-tenant) |

Body fields MUST NOT duplicate header correlation data inconsistently.

**Trace (informative):** DS-07
**Conformance test:** Sample events from each profile validate required header fields via JSON Schema or contract test.

---

### Messaging semantics (informative)

Event bus implementations SHOULD provide **at-least-once delivery**. Consumers MUST be **idempotent** on `event_id`. Producers SHOULD include idempotency keys for side-effecting downstream actions.

Exact broker technology is operator choice; conformance evaluates emitted event content and audit persistence, not vendor selection.

---

## 9.3 Core Identity audit events

### ODTIS-0526 - Registration, verification, and LoA events

Core Identity **MUST** emit **auditable events** for:

| Lifecycle | Minimum event types | When |
|-----------|---------------------|------|
| Registration | `identity.created` | Subject record created (ODTIS-0310) |
| Verification / proofing | `identity.verified`, `verification.completed`, `verification.escalated` | LoA assigned, upgraded, or manual review triggered |
| LoA change | `identity.updated` or dedicated LoA change type | Active LoA changes |

Events MUST include `subject_id` (or pseudonymous reference per operator policy), prior and new LoA where applicable, and `trace_id`.

**Trace (informative):** RF-26
**Conformance test:** Execute registration and proofing flows; audit store contains expected event types with matching trace_id chain.

---

### ODTIS-0527 - Consent events

**Consent grant** and **revoke** operations **MUST** emit auditable events with at minimum:

- `subject_id` (or pseudonymous reference);
- `client_id`;
- `scopes` affected;
- `purpose` (on grant); and
- `trace_id`.

Minimum event types: `consent.granted`, `consent.revoked`.

**Trace (informative):** RF-18
**Conformance test:** Grant and revoke consent; verify both events in audit export with required fields.

---

## 9.4 Trust Network audit events

### ODTIS-0528 - Exchange events with correlation

Trust Network **MUST** emit **auditable exchange events** with **correlation IDs** linking gateway, backend, and grant evaluation (extends ODTIS-0219).

Minimum event types:

| Event type | When |
|------------|------|
| `exchange.request.received` | Inbound exchange accepted for processing |
| `exchange.request.denied` | Grant, policy, or certificate denial |
| `grant.created` / `grant.revoked` | Service grant lifecycle (ODTIS-0211) |

Each exchange event MUST include: caller partner, provider partner, `service_id`, outcome, and `trace_id`.

Federated exchange MUST include local and remote instance IDs (6.8).

**Trace (informative):** RF-26, ODTIS-0219
**Conformance test:** Successful and denied exchange; audit records share trace_id across gateway log and event store.

---

## 9.5 Audit storage and regulator export

### ODTIS-0530 - PII-minimized audit storage

**Audit storage MUST** support **regulator export** (ODTIS-0514) **without exposing unnecessary PII** in log bodies.

Rules:

1. Event bodies SHOULD use identifiers (`subject_id`, `client_id`) rather than full demographic payloads unless required for supervised investigation.
2. Bulk export formats MUST document field sensitivity classification.
3. Regulator API responses MUST default to aggregated or pseudonymized views where full PII is not legally required.

Citizen DSAR processes (ODTIS-0334) MAY require fuller subject views under separate controlled procedures.

**Trace (informative):** RNF-17, ODTIS-0514
**Conformance test:** Regulator export sample reviewed for absence of full document numbers, biometrics, or unrelated attributes in standard audit queries.

---

### 9.5.1 Retention and integrity (informative)

Operator policy MUST define audit **retention periods** aligned with applicable law (ODTIS-0333). Storage SHOULD support:

- append-only or tamper-evident patterns for critical security events; and
- optional trusted timestamping for long-term non-repudiation (ODTIS-0217, P08).

Specific retention durations are jurisdiction-specific and documented in operator policy, not universal ODTIS MUST values.

---

## 9.6 Extended sub-module: E-Webhook

### ODTIS-0531 - Signed webhook payloads

When **Extended sub-module E-Webhook** is declared, outbound **RP webhook payloads MUST** be **signed** using **HMAC** (or equivalent authenticated mechanism documented in operator policy).

Verifiers (RP backends) MUST be able to validate:

- signature integrity;
- timestamp freshness (replay window); and
- event type and minimal payload schema.

Unsigned webhooks MUST NOT be emitted in production for security-sensitive notifications.

**Trace (informative):** DS-07 4
**Conformance test:** Deliver webhook; RP validates HMAC with shared secret; tampered body MUST fail validation.

---

## 9.7 Event catalog

**Table 9-1 - Minimum normative event catalog**

| Event ID | Profile | ODTIS requirement |
|----------|---------|-------------------|
| `identity.created` | Core Identity | ODTIS-0526 |
| `identity.verified` / `verification.completed` | Core Identity | ODTIS-0526 |
| `verification.escalated` | Core Identity | ODTIS-0526 |
| `consent.granted` | Core Identity | ODTIS-0527 |
| `consent.revoked` | Core Identity | ODTIS-0527 |
| `exchange.request.received` | Trust Network | ODTIS-0528 |
| `exchange.request.denied` | Trust Network | ODTIS-0528 |
| `grant.created` / `grant.revoked` | Trust Network | ODTIS-0528, 4.3.4 |
| `operator.pki.ceremony` | Operator | 7.3.2 (informative) |
| `security.incident.reported` | Operator | ODTIS-0515 (informative) |

JSON Schema files under [Event JSON schemas](/registry/events/schemas/) (16 schemas including envelope) are the machine-readable binding for this section at `0.9.0-draft`. Regenerate with `scripts/generate-event-schemas.py`.

---

## 9.8 Cross-references

| Topic | Reference |
|-------|-----------|
| Security event correlation | ODTIS-0327 |
| Exchange audit | ODTIS-0219 |
| Regulator API | ODTIS-0514 |
| Book 2 Appendix F | Informative event narrative |

---

## 9.9 Requirement index

<!-- GENERATED:section-index:START -->
<!-- Generated by scripts/generate-spec-section-indexes.py @ 0.9.0-draft -->

**Table 9-* - Requirement index (6 IDs)**

| ID | Keyword | Summary |
|----|---------|---------|
| ODTIS-0526 | MUST | Core Identity MUST emit auditable events for registration, verification… |
| ODTIS-0527 | MUST | Consent grant and revoke MUST emit auditable events with subject, clien… |
| ODTIS-0528 | MUST | Trust Network MUST emit auditable exchange events with correlation IDs |
| ODTIS-0529 | MUST | Event payloads MUST include trace_id and timestamp in a standard header… |
| ODTIS-0530 | MUST | Audit storage MUST support regulator export without exposing unnecessar… |
| ODTIS-0531 | MUST | Extended E-Webhook sub-module MUST sign outbound RP webhook payloads (H… |

<!-- GENERATED:section-index:END -->

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| stub | 2026-06-12 | Scaffold Phase 3.0 |
| draft v0.5 | 2026-06-12 | 9.1-9.9 normative prose; 6 IDs |
| 0.9.0-draft | 2026-06-12 | Phase 3.2 section review; ID numbering note; subsection rename |

**Phase 3.1 checklist (9).**

- [x] Event catalog aligned with P18 minimum types
- [x] Envelope and export rules (9.4.x)
- [x] Cross-ref 4, 5, 7
- [x] JSON Schema per event (`registry/events/schemas/`)


**Phase 3.2 review checklist (9).**

- [x] Registry IDs cited in normative prose
- [x] Requirement index matches registry
- [x] Conformance test stub per ID
- [ ] External review cycle 1 ([Section review matrix](/governance/SECTION-REVIEW/))
