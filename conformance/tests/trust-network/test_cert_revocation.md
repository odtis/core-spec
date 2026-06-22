# Conformance test: ODTIS-0216 - certificate revocation

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0216
**Profile:** trust-network

## Procedure

1. Successful exchange with valid partner certificate.
2. Revoke certificate via CRL or OCSP update per operator policy.
3. Attempt new exchange - MUST fail revocation check.

## Pass criteria

Revoked certs blocked before exchange.
