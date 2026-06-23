# Reliance Extensions: R-Assurance-Portability - ODTIS-0745

**Status:** implemented (static + policy smoke)
**Sub-module:** R-Assurance-Portability
**Requirements:** ODTIS-0745 (normative)
**Profile:** reliance-extensions

## Procedure

1. Configure target deployment and declare `R-Assurance-Portability` in `reliance_extensions` per conformance statement.
2. Review operator policy and audit exports: Only assurance that is actually portable SHOULD be reused; non-portable assurance SHOULD trigger re-verification.
3. Record evidence (policy document, audit export, or API trace as applicable).

## Pass criteria

Implementation satisfies ODTIS-0745 as declared in section 11 and Annex E (`ODTIS-0707` no-weakening applies).

## VenID reference stack (informative)

Map to operator policy, verification API audit fields, and RP registry per `implementation/RI-MAP.yaml` (Capa B overlay documentation).
