# Conformance test: ODTIS-0407 - federation product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0407
**Profile:** federation
**Trace:** P09, Book 1 D9

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: Suspended or expired federation agreements MUST disable federated routing on subsequent requests within documented cache...
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0407 (MUST) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
