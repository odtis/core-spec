# Conformance test: ODTIS-4.8.3 - registry separation

**Status:** pending implementation
**Requirements:** ODTIS-4.8.3, ODTIS-5.4.5
**Profile:** core-identity + trust-network

## Procedure

1. Review operator architecture documentation for distinct issuer/verifier registry vs network participant registry.
2. Add trusted issuer to Layer 1 registry without adding partner to participant registry.
3. Attempt Layer 2 exchange from that issuer's org - MUST fail at gateway unless participant registered with grants.

## Pass criteria

Layer 1 issuer trust does not imply Layer 2 exchange authorization.
