# Reliance Extensions: R-Stablecoin-CIP - ODTIS-0753

**Status:** implemented (static + policy smoke)
**Sub-module:** R-Stablecoin-CIP
**Requirements:** ODTIS-0753 (normative)
**Profile:** reliance-extensions

## Procedure

1. Configure target deployment and declare `R-Stablecoin-CIP` in `reliance_extensions` per conformance statement.
2. Review operator policy and audit exports: A protocol-agnostic credential presentation envelope and an identity-error recourse path SHOULD be supported.
3. Record evidence (policy document, audit export, or API trace as applicable).

## Pass criteria

Implementation satisfies ODTIS-0753 as declared in section 11 and Annex E (`ODTIS-0707` no-weakening applies).

## VenID reference stack (informative)

Map to operator policy, verification API audit fields, and RP registry per `implementation/RI-MAP.yaml` (Capa B overlay documentation).
