# Conformance test: ODTIS-0223 - trust-network product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0223
**Profile:** trust-network
**Trace:** platform FASE-4, P05

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: Sender gateway MUST resolve outbound routes by service_id from synchronized catalog without requiring a single hard-code...
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0223 (MUST) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
