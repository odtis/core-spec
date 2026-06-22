# Conformance test: ODTIS-0104 - National LoA gate

**Status:** pending implementation
**Requirement:** ODTIS-0104
**Profile:** extended

## Procedure

1. Verify conformance statement declares `E-Registry` when National LoA is offered to RPs.
2. Attempt to assign National LoA without E-Registry sub-module active - MUST fail.
3. With E-Registry active, verify registry adapter rules per operator policy before National LoA assignment.

## Pass criteria

National LoA is never exposed unless E-Registry is declared and adapter verification succeeds.
