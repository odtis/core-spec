# Conformance test: ODTIS-0225 - trust-network product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0225
**Profile:** trust-network
**Trace:** Book 1 D4, P01 metadata model

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: Trust network metadata stores MUST NOT persist full business payloads as authoritative copies; routing metadata and audi...
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0225 (MUST NOT) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
