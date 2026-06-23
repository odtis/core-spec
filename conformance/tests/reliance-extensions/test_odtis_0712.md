# Reliance Extensions: R-Agent-Authority - ODTIS-0712

**Status:** implemented (static + policy smoke)
**Sub-module:** R-Agent-Authority
**Requirements:** ODTIS-0712 (normative)
**Profile:** reliance-extensions

## Procedure

1. Configure target deployment and declare `R-Agent-Authority` in `reliance_extensions` per conformance statement.
2. High-risk action with stale mandate revocation check MUST fail closed.
3. Record evidence (policy document, audit export, or API trace as applicable).

## Pass criteria

Implementation satisfies ODTIS-0712 as declared in section 11 and Annex E (`ODTIS-0707` no-weakening applies).

## VenID reference stack (informative)

Map to operator policy, verification API audit fields, and RP registry per `implementation/RI-MAP.yaml` (Capa B overlay documentation).
