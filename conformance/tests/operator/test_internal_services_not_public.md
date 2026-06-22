# Conformance test: ODTIS-0518 - internal services not public

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0518
**Profile:** operator

## Procedure

1. Identify identity-core, consent-service, verification-engine endpoints.
2. Attempt direct access from public internet without VPN/gateway.
3. Services MUST be unreachable or reject non-mesh traffic.

## Pass criteria

Sensitive microservices not publicly exposed.
