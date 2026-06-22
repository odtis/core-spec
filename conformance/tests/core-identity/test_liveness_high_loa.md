# Conformance test: ODTIS-0523 - liveness for High LoA

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0523
**Profile:** core-identity

## Procedure

1. Attempt High LoA proofing with static image injection (no liveness).
2. Pipeline MUST reject assignment to High LoA.
3. Valid live capture MUST pass when other evidence sufficient.

## Pass criteria

Liveness enforced for High LoA biometrics.
