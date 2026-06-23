# Reliance Extensions: R-LE-Biometric - ODTIS-0771

**Status:** implemented (static + policy smoke)
**Sub-module:** R-LE-Biometric
**Requirements:** ODTIS-0771 (normative)
**Profile:** reliance-extensions

## Procedure

1. Configure target deployment and declare `R-LE-Biometric` in `reliance_extensions` per conformance statement.
2. Review operator policy and audit exports: record purpose, the alert-list authorizer, retention policy, and deployment class (overt or covert).
3. Record evidence (policy document, audit export, or API trace as applicable).

## Pass criteria

Implementation satisfies ODTIS-0771 as declared in section 11 and Annex E (`ODTIS-0707` no-weakening applies).

## VenID reference stack (informative)

Map to operator policy, verification API audit fields, and RP registry per `implementation/RI-MAP.yaml` (Capa B overlay documentation).
