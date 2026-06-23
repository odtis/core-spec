# Reliance Extensions: R-Base - ODTIS-0706

**Status:** implemented (static + policy smoke)
**Sub-module:** R-Base
**Requirements:** ODTIS-0706 (normative)
**Profile:** reliance-extensions

## Procedure

1. Configure target deployment and declare `R-Base` in `reliance_extensions` per conformance statement.
2. Trigger revocation or assurance downgrade; verify step-up or deny path fires per policy.
3. Record evidence (policy document, audit export, or API trace as applicable).

## Pass criteria

Implementation satisfies ODTIS-0706 as declared in section 11 and Annex E (`ODTIS-0707` no-weakening applies).

## VenID reference stack (informative)

Map to operator policy, verification API audit fields, and RP registry per `implementation/RI-MAP.yaml` (Capa B overlay documentation).
