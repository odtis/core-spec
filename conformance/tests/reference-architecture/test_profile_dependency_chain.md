# Conformance test: ODTIS-0004 - Profile dependency chain

**Status:** pending implementation
**Requirement:** ODTIS-0004
**Profile:** reference-architecture

## Procedure

1. Parse declared profiles against [`profiles.yaml`](../../../registry/profiles.yaml) `depends_on` chains.
2. Flag any profile claimed without its dependencies.

## Pass criteria

No profile appears unless all profiles in its `depends_on` chain are also declared.
