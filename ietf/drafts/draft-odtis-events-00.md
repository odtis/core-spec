# draft-odtis-events-00 - ODTIS Event Envelope (working draft)

**Status:** markdown working draft 
**ODTIS source:** section 9, [Envelope.Schema (JSON)](/registry/events/schemas/envelope.schema.json)

**IETF track:** [Project hub](../README.md) | **Project:** [Project hub](/project/)

**Authors:** Manuel Mérida Oliveros

---

## Abstract

This document defines a JSON event envelope for audit and lifecycle events in ODTIS deployments, with typed event payloads referenced by JSON Schema.

---

## 1. Envelope fields

See `envelope.schema.json`: event id, type, timestamp, operator id, correlation id, payload reference.

---

## 2. Relationship to OpenID Shared Signals

ODTIS events are **operator audit catalog** semantics. Mapping to [OpenID Shared Signals Framework](https://openid.net/developers/specs/) MAY be documented in Annex C; protocols are not identical.

---

*(Expand before Independent submission.)*
