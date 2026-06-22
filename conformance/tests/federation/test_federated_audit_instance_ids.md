# Conformance test: ODTIS-0408 - federation product requirement

**Status:** implemented (static + unit + live staging smoke)
**Requirement:** ODTIS-0408
**Profile:** federation
**Trace:** Book 2 ch.6.8, P09

## Automation

```bash
cd core-impl/ven-trust-network && ./scripts/federation-runtime-check.sh
# ExchangeAuditEventsTest covers federated metadata fields
```

Evidence: `implementation/evidence/federation-staging/lab-notes.md`

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: Federated exchange audit events MUST include local trust instance identifier and remote trust instance identifier
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0408 (MUST) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
