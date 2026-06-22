# Conformance test: ODTIS-0362 - extended product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0362
**Profile:** extended
**Sub-module:** E-Signature
**Trace:** P08, ODTIS-0507

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: Signature keys MUST be issued under operator PKI or recognized TSP integration documented in CP/CPS
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0362 (MUST) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
