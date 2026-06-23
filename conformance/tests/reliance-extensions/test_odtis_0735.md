# Reliance Extensions: R-VC-Maturity-Gate - ODTIS-0735

**Status:** implemented (static + policy smoke)
**Sub-module:** R-VC-Maturity-Gate
**Requirements:** ODTIS-0735 (normative)
**Profile:** reliance-extensions

## Procedure

1. Configure target deployment and declare `R-VC-Maturity-Gate` in `reliance_extensions` per conformance statement.
2. Review operator policy and audit exports: be gated by a declared maturity level; First Public Working Draft components MUST NOT be claimed for production national mandates.
3. Record evidence (policy document, audit export, or API trace as applicable).

## Pass criteria

Implementation satisfies ODTIS-0735 as declared in section 11 and Annex E (`ODTIS-0707` no-weakening applies).

## VenID reference stack (informative)

Map to operator policy, verification API audit fields, and RP registry per `implementation/RI-MAP.yaml` (Capa B overlay documentation).
