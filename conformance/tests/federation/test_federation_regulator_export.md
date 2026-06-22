# Conformance test: ODTIS-0406 - federation agreement regulator export

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0406
**Profile:** federation, operator

## Procedure

1. Declare Federation profile in conformance statement.
2. Verify operator policy or Regulator API (Annex A S8) documents how active federation agreements are exported (instance pairs, validity, suspension state).
3. If export is not implemented, document deferral in operator policy with rationale.

## Pass criteria

Federation agreement metadata is exportable or explicitly deferred with documented operator rationale (SHOULD).
