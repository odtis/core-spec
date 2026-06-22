# Conformance test: ODTIS-0351 - extended product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0351
**Profile:** extended
**Sub-module:** E-Registry
**Trace:** P11 5.1

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: Registry adapter MUST use agreed identifier hashing; raw registry biometrics MUST NOT be persisted in Core Identity
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0351 (MUST) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
