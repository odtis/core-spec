# Ven Partner SDK evidence (#31)

**Status:** L2 sandbox - Spring autodiscovery library documented and mapped alongside exchange-client.

## Consolidation

See `ven-trust-network/docs/operator/TRUST-NETWORK-SDKS.md`:

| SDK | Role |
|-----|------|
| `exchange-client` | Consume remote services (ODTIS-0223) |
| `ven-partner-sdk` | Publish local REST endpoints (ODTIS-0214) |

## Smoke

```bash
cd ven-trust-network && ./scripts/ven-partner-sdk-check.sh
cd core-spec && ./conformance/run-ven-partner-sdk-checks.sh
```

Sample: `samples/partner-backend-example/`
