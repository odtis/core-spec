# Conformance test: ODTIS-0401 - non-transitivity

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0401
**Profile:** federation

## Procedure

1. Configure federation A↔B and B↔C without A↔C.
2. Attempt service call from instance A targeting instance C routed via B.
3. Assert rejection (routing or policy deny).
4. Configure A↔C agreement; direct A->C call with grant - MUST succeed.

## Pass criteria

No transitive federation path without direct agreement.
