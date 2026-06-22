# Exchange client SDK evidence (#19)

**Status:** L2 sandbox - library + operator documentation (no standalone compose service).

## Artifacts

| Path | Purpose |
|------|---------|
| `sdk/exchange-client/` | `ExchangeGatewayClient` Java 21 library |
| `docs/operator/EXCHANGE-CLIENT-SDK.md` | Operator / integrator guide |
| `scripts/exchange-client-sdk-check.sh` | Docs + source contract + unit smoke |
| `scripts/sender-routing-check.sh` | Gateway catalog routing (live optional) |

## Smoke

```bash
cd ven-trust-network && ./scripts/exchange-client-sdk-check.sh
cd core-spec && ./conformance/run-exchange-client-sdk-checks.sh
```

## ODTIS-0223 pass criteria

Sender backends use `X-Exchange-Service` via SDK; gateway resolves peer URL from synchronized catalog without hard-coded remote URLs.
