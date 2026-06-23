# Reliance Extensions: R-Assurance-Portability - ODTIS-0743

**Status:** implemented (static + policy smoke)
**Sub-module:** R-Assurance-Portability
**Requirements:** ODTIS-0743 (normative)
**Profile:** reliance-extensions

## Procedure

1. Configure target deployment and declare `R-Assurance-Portability` in `reliance_extensions` per conformance statement.
2. Review operator policy and audit exports: carry portable assurance metadata: proofing level and method, PAD and IAD coverage, and capture-channel integrity.
3. Record evidence (policy document, audit export, or API trace as applicable).

## Pass criteria

Implementation satisfies ODTIS-0743 as declared in section 11 and Annex E (`ODTIS-0707` no-weakening applies).

## VenID reference stack (informative)

Map to operator policy, verification API audit fields, and RP registry per `implementation/RI-MAP.yaml` (Capa B overlay documentation).
