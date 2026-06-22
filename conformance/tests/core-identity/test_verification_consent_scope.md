# Conformance test: ODTIS-0317 - Verification API consent scope

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0317, ODTIS-0331
**Profile:** core-identity

## Procedure

1. Subject with verified attributes; no active consent for RP client.
2. Verification API request for restricted attributes - expect denial (403 or empty attributes with denial code); error MUST NOT include restricted attribute values (ODTIS-0331).
3. Grant consent for required scopes.
4. Repeat request - expect consented attributes only.

## Pass criteria

No out-of-scope attributes returned.
