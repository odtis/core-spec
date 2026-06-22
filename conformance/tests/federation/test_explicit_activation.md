# Conformance test: ODTIS-0403 - explicit federation activation

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0403
**Profile:** federation

## Procedure

1. Verify conformance statement documents deployment phase and active agreements.
2. Disable or expire federation agreement.
3. Federated exchange MUST fail on subsequent requests.
4. Re-enable agreement - exchange MAY resume per grants.

## Pass criteria

Federation only active when explicitly configured and documented.
