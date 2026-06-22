# Extended gateway routes evidence (#13)

**Status:** L2 sandbox — static route/auth verification; live docker optional.

## Artifacts

| Path | Role |
| --- | --- |
| `ven-identity-core/config/api-gateway.yml` | Routes to wallet/inclusion/signature/kyb + rate limits |
| `api/api-gateway/.../ExtendedMachineClientGlobalFilter.java` | Machine-client JWT gate when extended auth enabled |
| `compose/staging/docker-compose.extended.yml` | Patches api-gateway URIs + enables extended auth |

## Smoke

```bash
cd core-impl && ./scripts/gateway-extended-check.sh
cd core-spec && ./conformance/run-gateway-extended-checks.sh
```

## Pass criteria (#13)

1. Extended APIs reachable via gateway paths `/v1/wallet`, `/v1/inclusion`, `/v1/signature`, `/v1/kyb`.
2. Extended auth defaults **off** in Phase 2 pilot config.
3. Extended staging overlay enables machine-client JWT validation (same policy as verification-api).
4. Rate limits and correlation ID apply to extended routes.
