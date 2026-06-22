# Conformance test: ODTIS-0514 - regulator export

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0514
**Profile:** operator

## Procedure

1. Invoke regulator API or execute documented export job.
2. Verify aggregated metrics and audit events export successfully.
3. Inspect sample records for unnecessary citizen PII in bodies.

## Pass criteria

Regulator path works with PII minimization.
