# Partner node kit evidence (#37)

**Status:** L2 sandbox - static kit verification; live docker optional.

## Smoke

```bash
cd ven-trust-network && ./scripts/partner-node-kit-check.sh
cd core-spec && ./conformance/run-partner-node-kit-checks.sh
cd core-impl && ./scripts/ci-operator-checks.sh
```

## ODTIS-0512 pass criteria

Operator documents onboarding, certification, pricing transparency ([Partner Onboarding](https://github.com/odtis/core-impl/blob/main/ven-trust-network/docs/operator/PARTNER-ONBOARDING.md)) and ships verifiable partner node kit with `verify-kit.sh`.
