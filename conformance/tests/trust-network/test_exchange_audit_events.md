# Conformance test: ODTIS-0528 - exchange audit events

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0528
**Profile:** trust-network

## Procedure

1. Execute successful exchange; assert `exchange.request.received` with correlation trace_id.
2. Deny exchange (no grant); assert `exchange.request.denied`.
3. Verify gateway log shares trace_id with event store.

## Pass criteria

Exchange success and denial auditable with correlation.
