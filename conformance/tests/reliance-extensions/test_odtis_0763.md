# Reliance Extensions: R-DPI-Resilience - ODTIS-0763

**Status:** implemented (static + policy smoke)
**Sub-module:** R-DPI-Resilience
**Requirements:** ODTIS-0763 (normative)
**Profile:** reliance-extensions

## Procedure

1. Configure target deployment and declare `R-DPI-Resilience` in `reliance_extensions` per conformance statement.
2. Review operator policy and audit exports: publish participant and relying-party authorization scoped per component, with blast-radius mapping of co-dependent services.
3. Record evidence (policy document, audit export, or API trace as applicable).

## Pass criteria

Implementation satisfies ODTIS-0763 as declared in section 11 and Annex E (`ODTIS-0707` no-weakening applies).

## VenID reference stack (informative)

Map to operator policy, verification API audit fields, and RP registry per `implementation/RI-MAP.yaml` (Capa B overlay documentation).
