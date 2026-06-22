# Conformance test: ODTIS-0001 - Layer 2 requires Layer 1

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0001
**Profile:** reference-architecture

## Procedure

1. Obtain conformance statement claiming Trust Network without Core Identity.
2. Verify claim is rejected or marked invalid in review.

## Pass criteria

Trust Network profile MUST NOT appear without Core Identity for the same operator scope.
