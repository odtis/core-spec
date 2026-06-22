# Conformance test: ODTIS-0007 - reference-architecture product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0007
**Profile:** reference-architecture
**Trace:** P18 1.9.3, Book 1 cap. 5

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: Implementations MUST NOT use prohibited ODTIS claims including ODTIS certified without statement, Full ODTIS without lis...
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0007 (MUST NOT) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
