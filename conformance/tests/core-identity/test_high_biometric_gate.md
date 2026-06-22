# Conformance test: ODTIS-0103 - High LoA biometric gate

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0103
**Profile:** core-identity

## Procedure

1. Submit proofing bundle with valid document only (no biometric capture).
2. Attempt assignment to High LoA - MUST fail.
3. Submit proofing with liveness and facial match per operator policy.
4. Attempt assignment to High LoA - MUST succeed.

## Pass criteria

High LoA impossible without biometric proofing path.
