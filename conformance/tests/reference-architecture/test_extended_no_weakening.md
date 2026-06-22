# Conformance test: ODTIS-0006 - Extended must not weaken base profiles

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0006
**Profile:** reference-architecture

## Procedure

1. For each active Extended sub-module, review operator policy and implementation design.
2. Confirm no Extended configuration bypasses Core Identity, Trust Network, or Federation MUST requirements.

## Pass criteria

Extended capabilities add declared behavior only; base profile MUST requirements remain enforced.
