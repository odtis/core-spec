# Reliance Extensions: R-Liveness - ODTIS-0727

**Status:** implemented (static + policy smoke)
**Sub-module:** R-Liveness
**Requirements:** ODTIS-0727 (normative)
**Profile:** reliance-extensions

## Procedure

1. Configure target deployment and declare `R-Liveness` in `reliance_extensions` per conformance statement.
2. Review operator policy and audit exports: declare the liveness provider, challenge type, identity-linkage class, and retention policy.
3. Record evidence (policy document, audit export, or API trace as applicable).

## Pass criteria

Implementation satisfies ODTIS-0727 as declared in section 11 and Annex E (`ODTIS-0707` no-weakening applies).

## VenID reference stack (informative)

Map to operator policy, verification API audit fields, and RP registry per `implementation/RI-MAP.yaml` (Capa B overlay documentation).
