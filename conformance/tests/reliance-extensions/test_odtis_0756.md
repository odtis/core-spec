# Reliance Extensions: R-Travel - ODTIS-0756

**Status:** implemented (static + policy smoke)
**Sub-module:** R-Travel
**Requirements:** ODTIS-0756 (normative)
**Profile:** reliance-extensions

## Procedure

1. Configure target deployment and declare `R-Travel` in `reliance_extensions` per conformance statement.
2. Review operator policy and audit exports: be bounded by a declared reuse policy (one-time, session-bound, or journey-bound).
3. Record evidence (policy document, audit export, or API trace as applicable).

## Pass criteria

Implementation satisfies ODTIS-0756 as declared in section 11 and Annex E (`ODTIS-0707` no-weakening applies).

## VenID reference stack (informative)

Map to operator policy, verification API audit fields, and RP registry per `implementation/RI-MAP.yaml` (Capa B overlay documentation).
