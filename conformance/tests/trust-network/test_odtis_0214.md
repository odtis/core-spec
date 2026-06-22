# Conformance test: ODTIS-0214 - autodiscovery (@VenPartnerService)

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0214 
**Profile:** trust-network

## Scope @ 0.9.0-draft (FB-004)

- **SHOULD-only** for review draft; not an Annex A OpenAPI operation.
- No L2 automated check until Book 2 ch.9 defines discovery well-known URI.
- Pass via manual evidence: catalog registration without per-endpoint duplication when autodiscovery is declared supported.

## Procedure

1. If operator declares `@VenPartnerService` (or equivalent) support, register a multi-node service via autodiscovery.
2. Verify catalog lists a resolvable entry without duplicate manual endpoints.
3. If autodiscovery is not supported, document deferral in operator policy (SHOULD deviation rationale).

## Pass criteria

When supported: catalog reflects autodiscovered service. When not supported: documented rationale per operator policy.
