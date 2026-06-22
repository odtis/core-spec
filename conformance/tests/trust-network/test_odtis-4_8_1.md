# Conformance test: ODTIS-4.8.1 - network participant registry

**Status:** pending implementation
**Requirement:** ODTIS-4.8.1
**Profile:** trust-network

## Procedure

1. Inspect operator participant registry export: verify each active partner has `partner_id`, gateway endpoint, cert thumbprint or subject DN.
2. Send inbound exchange with unregistered partner certificate; assert gateway rejects (ODTIS-0205 + 4.8.1).
3. Register partner; retry with valid grant - MUST route.

## Pass criteria

Participant registry is authoritative for gateway authorization; unknown partners rejected.
