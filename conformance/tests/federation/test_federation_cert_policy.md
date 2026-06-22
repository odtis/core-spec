# Conformance test: ODTIS-0402 - federation certificate policy

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0402
**Profile:** federation

## Procedure

1. Configure federation agreement with pinned remote CA/gateway cert.
2. Attempt federated inbound with local partner cert not in agreement - MUST reject.
3. Attempt with agreement-pinned certificate - MUST accept when service whitelisted.

## Pass criteria

Federated auth uses network-specific federation policy.
