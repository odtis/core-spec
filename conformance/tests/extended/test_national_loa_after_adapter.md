# Conformance test: ODTIS-0350 - extended product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0350
**Profile:** extended
**Sub-module:** E-Registry
**Trace:** P11 4.2, ODTIS-0344

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: National LoA MUST be assigned only after successful registry adapter verification per operator policy
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0350 (MUST) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
