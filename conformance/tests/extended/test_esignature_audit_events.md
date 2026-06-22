# Conformance test: ODTIS-0363 - extended product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0363
**Profile:** extended
**Sub-module:** E-Signature
**Trace:** RF-EXT1, ODTIS-0526

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: Signature creation and verification events MUST be auditable with correlation to subject_id and RP client_id
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0363 (MUST) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
