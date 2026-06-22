# Conformance test: ODTIS-0315 - Verification API client authentication

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0315
**Profile:** core-identity

## Procedure

1. Call Verification API verify endpoint without credentials - expect 401.
2. Call with invalid client credentials - expect 401.
3. Call with valid client credentials or mTLS client cert - expect 200/403 per subject state, not 401.

## Pass criteria

Unauthenticated RP backend calls rejected.
