# Conformance test: ODTIS-0530 - audit export PII minimization

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0530
**Profile:** operator

## Procedure

1. Run standard regulator audit export (not DSAR full subject export).
2. Inspect sample records for document numbers, biometrics, full demographics.
3. Verify only necessary identifiers appear in default export view.

## Pass criteria

Regulator export minimizes PII in log bodies.
