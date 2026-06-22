# Conformance test: ODTIS-0527 - consent audit events

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0527
**Profile:** core-identity

## Procedure

1. Grant consent for RP with known scopes.
2. Assert `consent.granted` with subject_id, client_id, scopes, trace_id.
3. Revoke consent; assert `consent.revoked` with same identifiers.

## Pass criteria

Consent lifecycle fully auditable.
