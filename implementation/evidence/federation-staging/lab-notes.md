# Federation staging evidence (#25 / P4-E01)

**Status:** L2 sandbox - staging overlay with bilateral agreements from `V16__federation_agreements.sql`.

## Stack

| Asset | Purpose |
|-------|---------|
| `compose/staging/docker-compose.federation.yml` | Enables `APP_EXCHANGE_FEDERATION_ENABLED`, sender mode, partner-b gateway :9081 |
| `scripts/federation-staging-up.sh` | Applies overlay on ven-trust-network compose |
| `trust-service` `/internal/federation/validate-route` | Proxies to trust-registry for exchange-gateway sender |

Lab instances: `VE:VENID:GOV:001` (local) ↔ `VE:VENID:LAB:002` (partner B).

## Smoke

```bash
cd core-impl && ./scripts/federation-overlay-check.sh
cd core-impl && ./scripts/federation-staging-up.sh
cd ven-trust-network && ./scripts/federation-runtime-check.sh
cd core-spec && ./conformance/run-federation-runtime-checks.sh
```

## Pass criteria

- **ODTIS-0407:** suspended agreement → `validate-route` returns `allowed:false` / `agreement_suspended`.
- **ODTIS-0408:** federated audit events include `local_trust_instance_id` and `remote_trust_instance_id` (unit: `ExchangeAuditEventsTest`).
