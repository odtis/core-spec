# Reliance Extensions: R-Document-Capture - ODTIS-0724

**Status:** implemented (static + policy smoke)
**Sub-module:** R-Document-Capture
**Requirements:** ODTIS-0724 (normative)
**Profile:** reliance-extensions

## Procedure

1. Configure target deployment and declare `R-Document-Capture` in `reliance_extensions` per conformance statement.
2. Reusable document outcome carries capture-channel integrity; upload-only gated by risk tier.
3. Record evidence (policy document, audit export, or API trace as applicable).

## Pass criteria

Implementation satisfies ODTIS-0724 as declared in section 11 and Annex E (`ODTIS-0707` no-weakening applies).

## VenID reference stack (informative)

Map to operator policy, verification API audit fields, and RP registry per `implementation/RI-MAP.yaml` (Capa B overlay documentation).
