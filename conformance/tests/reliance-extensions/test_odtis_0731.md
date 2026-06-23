# Reliance Extensions: R-Disclosure-Assurance - ODTIS-0731

**Status:** implemented (static + policy smoke)
**Sub-module:** R-Disclosure-Assurance
**Requirements:** ODTIS-0731 (normative)
**Profile:** reliance-extensions

## Procedure

1. Configure target deployment and declare `R-Disclosure-Assurance` in `reliance_extensions` per conformance statement.
2. Review operator policy and audit exports: define per-relying-party-role disclosure sets bound to purpose, with prohibited fields enumerated per tier.
3. Record evidence (policy document, audit export, or API trace as applicable).

## Pass criteria

Implementation satisfies ODTIS-0731 as declared in section 11 and Annex E (`ODTIS-0707` no-weakening applies).

## VenID reference stack (informative)

Map to operator policy, verification API audit fields, and RP registry per `implementation/RI-MAP.yaml` (Capa B overlay documentation).
