# Conformance test: ODTIS-0349 - extended product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0349
**Profile:** extended
**Sub-module:** E-Registry
**Trace:** P11 1.1, RF-EXT5

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: E-Registry MUST NOT replace civil registry legal authority or issue national ID documents
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0349 (MUST NOT) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
