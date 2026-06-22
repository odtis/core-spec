# Conformance test: ODTIS-0204 - gateway mTLS

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0204
**Profile:** trust-network

## Procedure

1. Initiate gateway-to-gateway TLS without client certificate - MUST fail handshake.
2. Repeat with valid partner client certificate - MUST succeed.
3. Verify TLS version ≥ 1.2.

## Pass criteria

Mutual TLS required for gateway exchange.
