# Reliance Extensions: R-Lifecycle-Revocation - ODTIS-0720

**Status:** implemented (static + policy smoke)
**Sub-module:** R-Lifecycle-Revocation
**Requirements:** ODTIS-0720 (normative)
**Profile:** reliance-extensions

## Procedure

1. Configure target deployment and declare `R-Lifecycle-Revocation` in `reliance_extensions` per conformance statement.
2. Review operator policy and audit exports: unify physical and digital credential status into a reconstructable audit reference per lifecycle event.
3. Record evidence (policy document, audit export, or API trace as applicable).

## Pass criteria

Implementation satisfies ODTIS-0720 as declared in section 11 and Annex E (`ODTIS-0707` no-weakening applies).

## VenID reference stack (informative)

Map to operator policy, verification API audit fields, and RP registry per `implementation/RI-MAP.yaml` (Capa B overlay documentation).
