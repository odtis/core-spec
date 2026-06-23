# Reliance Extensions: R-Agent-Authority - ODTIS-0710

**Status:** implemented (static + policy smoke)
**Sub-module:** R-Agent-Authority
**Requirements:** ODTIS-0710 (normative)
**Profile:** reliance-extensions

## Procedure

1. Configure target deployment and declare `R-Agent-Authority` in `reliance_extensions` per conformance statement.
2. Resolve agent identifier to principal and accountable sponsor before honoring agent-initiated action.
3. Record evidence (policy document, audit export, or API trace as applicable).

## Pass criteria

Implementation satisfies ODTIS-0710 as declared in section 11 and Annex E (`ODTIS-0707` no-weakening applies).

## VenID reference stack (informative)

Map to operator policy, verification API audit fields, and RP registry per `implementation/RI-MAP.yaml` (Capa B overlay documentation).
