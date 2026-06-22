# Conformance test: ODTIS-0528 - exchange audit events

**Status:** implemented (static + unit + live E2E smoke)
**Requirement:** ODTIS-0528
**Profile:** trust-network

## Automation

```bash
cd core-impl && ./scripts/fail-closed-audit-e2e-check.sh
cd core-spec && ./conformance/run-fail-closed-audit-e2e-checks.sh
```

Evidence: `implementation/evidence/fail-closed-e2e/lab-notes.md`

## Procedure

1. Execute successful exchange; assert `exchange.request.received` with correlation trace_id.
2. Deny exchange (no grant); assert `exchange.request.denied`.
3. Verify gateway log shares trace_id with event store.

## Pass criteria

Exchange success and denial auditable with correlation.
