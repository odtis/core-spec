# Conformance test: ODTIS-0205 - trust registry validation

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0205
**Profile:** trust-network

## Procedure

1. Send inbound exchange request with certificate not registered in trust registry.
2. Assert gateway rejects before backend routing.
3. Register partner; retry - MUST route when grant exists.

## Pass criteria

Unknown partners rejected at gateway.
