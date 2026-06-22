# Conformance test: ODTIS-0201 - gateway-only routing

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0201
**Profile:** trust-network

## Procedure

1. Identify internal backend URL for catalogued service.
2. Attempt partner-authenticated call directly to backend - MUST fail or be blocked.
3. Call same operation via local exchange gateway with valid grant - MUST succeed.

## Pass criteria

Partner exchange only through gateway.
