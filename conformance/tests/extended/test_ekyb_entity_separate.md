# Conformance test: ODTIS-0364 - extended product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0364
**Profile:** extended
**Sub-module:** E-KYB
**Trace:** doc-03 sector KYB

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: E-KYB MUST verify legal entity identity separately from natural-person Core Identity proofing
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0364 (MUST) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
