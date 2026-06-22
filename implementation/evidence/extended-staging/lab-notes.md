# Extended profile staging evidence (#12)

**Status:** L2 sandbox - static overlay verification; live docker optional.

## Artifacts

| Path | Role |
| --- | --- |
| `core-impl/compose/staging/docker-compose.extended.yml` | Compose overlay with profile `extended` |
| `core-impl/scripts/extended-staging-up.sh` | Start five extended services on base stack |
| `core-impl/scripts/extended-overlay-check.sh` | Static + optional live health probes |

## Smoke

```bash
cd core-impl && ./scripts/extended-overlay-check.sh
cd core-spec && ./conformance/run-extended-staging-checks.sh
```

## Live staging (optional)

```bash
# Base Phase 2 stack running first
cd core-impl && ./scripts/extended-staging-up.sh
docker compose -f ven-identity-core/docker-compose.yml \
-f compose/staging/docker-compose.extended.yml --profile extended ps
```

## Pass criteria (#12)

1. Default `docker-compose.yml` excludes all five extended services.
2. Config Server YAML keeps `active: false` for pilot.
3. `docker compose --profile extended up` starts wallet, inclusion, signature, kyb, eregistry-adapter with phase 4 activation env vars.
4. Each service exposes `/actuator/health` when running.
