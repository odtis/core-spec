# Reliance Extensions: R-Fraud-Orchestration - ODTIS-0749

**Status:** implemented (static + policy smoke)
**Sub-module:** R-Fraud-Orchestration
**Requirements:** ODTIS-0749 (normative)
**Profile:** reliance-extensions

## Procedure

1. Configure target deployment and declare `R-Fraud-Orchestration` in `reliance_extensions` per conformance statement.
2. Review operator policy and audit exports: A recourse path SHOULD be defined for wrongful blocks as well as for fraud victims.
3. Record evidence (policy document, audit export, or API trace as applicable).

## Pass criteria

Implementation satisfies ODTIS-0749 as declared in section 11 and Annex E (`ODTIS-0707` no-weakening applies).

## VenID reference stack (informative)

Map to operator policy, verification API audit fields, and RP registry per `implementation/RI-MAP.yaml` (Capa B overlay documentation).
