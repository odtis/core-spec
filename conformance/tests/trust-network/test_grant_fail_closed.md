# Conformance test: ODTIS-0224 - trust-network product requirement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0224
**Profile:** trust-network
**Trace:** Book 2 ch.3.7 rule 1, Book 1 D4

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: Exchange gateway MUST fail closed when service grant validation fails; MUST NOT route on implicit network-zone trust
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0224 (MUST) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
