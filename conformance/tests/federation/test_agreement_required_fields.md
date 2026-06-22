# Conformance test: ODTIS-0404 - federation agreement required fields

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0404
**Profile:** federation

## Procedure

1. Create a federation agreement missing one of: remote instance ID, validity window, or pinned remote trust material.
2. Attempt to enable outbound federated routing for that remote instance.
3. Assert routing remains disabled or requests are rejected.
4. Add all required fields; assert outbound federated routing may be enabled per policy.

## Pass criteria

No federated outbound route without complete agreement fields documented in section 6.2.2.
