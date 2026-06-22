# Fail-closed + audit cross-link E2E evidence (#26)

**Status:** L2 sandbox - identity + trust-network audit correlation on shared `request_id`.

## Flow (ODTIS-0535 + ODTIS-0528)

1. Append `identity.consent.denied` to audit-service with correlation `request_id`.
2. POST `/exchange/v1/verify` without partner auth → **403**, empty body (fail-closed).
3. Gateway emits `exchange.request.denied` with same `X-Exchange-Request-ID`.
4. `GET /api/events/by-correlation/{traceId}` returns split `identity_events` + `exchange_events`.
5. Optional: `GET /v1/regulator/audit-logs/correlation/{traceId}` (PII-minimized export).

## Smoke

```bash
cd core-impl && ./scripts/fail-closed-audit-e2e-check.sh
cd core-spec && ./conformance/run-fail-closed-audit-e2e-checks.sh
```

Requires trust-network stack (`exchange-gateway` :9080, `audit-service` :8084). Regulator probe optional (:8086).
