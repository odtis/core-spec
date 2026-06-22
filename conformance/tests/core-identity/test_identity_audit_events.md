# Conformance test: ODTIS-0526 - identity audit events

**Status:** pending implementation
**Requirement:** ODTIS-0526
**Profile:** core-identity

## Procedure

1. Complete subject registration and proofing to Medium LoA.
2. Query audit store or subscribe to event bus.
3. Assert `identity.created` and verification/LoA events present with shared trace_id.

## Pass criteria

Registration and LoA lifecycle emits auditable events.
