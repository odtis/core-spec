# Conformance test: ODTIS-0354 - extended product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0354
**Profile:** extended
**Sub-module:** E-Inclusion
**Trace:** P13 representative model, RF-15

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: Assisted registration flows MUST obtain explicit subject or legal-representative consent with full audit trail
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0354 (MUST) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
