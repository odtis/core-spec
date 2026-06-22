# Conformance test: ODTIS-0529 - event envelope

**Status:** pending implementation
**Requirement:** ODTIS-0529
**Profile:** operator

## Procedure

1. Collect sample events from Core Identity and Trust Network flows.
2. Validate each has trace_id, timestamp, event_id, event_type, source in header envelope.

## Pass criteria

All sampled events conform to envelope schema.
