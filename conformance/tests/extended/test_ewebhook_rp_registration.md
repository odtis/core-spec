# Conformance test: ODTIS-0358 - extended product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0358
**Profile:** extended
**Sub-module:** E-Webhook
**Trace:** P14 6.4, RF-22

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: E-Webhook MUST allow RPs to register callback URLs, subscribed event types, and shared signing secret via authenticated ...
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0358 (MUST) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
