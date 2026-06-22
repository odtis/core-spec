# Conformance test: ODTIS-0355 - extended product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0355
**Profile:** extended
**Sub-module:** E-Inclusion
**Trace:** P13 5.3, UC-C07

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: Representative or tutor flows MUST verify legal relationship before attribute release on behalf of another subject
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0355 (MUST) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
