# Conformance test: ODTIS-0365 - extended product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0365
**Profile:** extended
**Sub-module:** E-KYB
**Trace:** UC-E07, RF-EXT5

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: E-KYB SHOULD link authorized representatives to verified natural-person subjects before B2B attribute release
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0365 (SHOULD) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
