# Conformance test: ODTIS-0360 - extended product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0360
**Profile:** extended
**Sub-module:** E-Webhook
**Trace:** P14 6.4, ODTIS-0530

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: Webhook payloads MUST minimize PII; use opaque subject references where operator policy requires
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0360 (MUST) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
