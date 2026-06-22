# Conformance test: ODTIS-0339 - RP suspension

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0339
**Profile:** core-identity

## Procedure

1. Active RP client with valid consent and working OIDC flow.
2. Operator suspends RP via management API or console.
3. Attempt new authorization - MUST fail.
4. Attempt Verification API with RP credentials - MUST fail or return client disabled.

## Pass criteria

Suspended RP cannot initiate new sessions or API calls.
