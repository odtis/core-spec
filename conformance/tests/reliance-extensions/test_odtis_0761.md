# Reliance Extensions: R-CRA-Resilience - ODTIS-0761

**Status:** implemented (static + policy smoke)
**Sub-module:** R-CRA-Resilience
**Requirements:** ODTIS-0761 (normative)
**Profile:** reliance-extensions

## Procedure

1. Configure target deployment and declare `R-CRA-Resilience` in `reliance_extensions` per conformance statement.
2. Review operator policy and audit exports: Post-market monitoring, a vulnerability-disclosure policy, and a component revocation path SHOULD be documented.
3. Record evidence (policy document, audit export, or API trace as applicable).

## Pass criteria

Implementation satisfies ODTIS-0761 as declared in section 11 and Annex E (`ODTIS-0707` no-weakening applies).

## VenID reference stack (informative)

Map to operator policy, verification API audit fields, and RP registry per `implementation/RI-MAP.yaml` (Capa B overlay documentation).
