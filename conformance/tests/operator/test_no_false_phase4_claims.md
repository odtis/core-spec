# Conformance test: ODTIS-0506 - no false Phase 4 claims

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0506
**Profile:** operator

## Procedure

1. Identify deployment phase in conformance statement (Phase 1-2 vs 3-4).
2. Review public claims for ISO/WebTrust/QTSP certification presented as achieved.
3. If Phase 1-2 only, such claims MUST NOT appear as current state.

## Pass criteria

No Phase 4 certification claims while on Phase 1-2 profile.
