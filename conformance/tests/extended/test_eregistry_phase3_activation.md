# Conformance test: ODTIS-0352 - extended product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0352
**Profile:** extended
**Sub-module:** E-Registry
**Trace:** P11 4.2, P10

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: Registry adapter activation MUST require deployment Phase 3+ and documented bilateral agreement with registry authority
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0352 (MUST) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
