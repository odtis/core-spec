# Conformance test: ODTIS-0356 - extended product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0356
**Profile:** extended
**Sub-module:** E-Inclusion
**Trace:** P18 4.2, RF-06

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: Inclusion channels MUST NOT bypass LoA proofing rules defined for online registration
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0356 (MUST NOT) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
