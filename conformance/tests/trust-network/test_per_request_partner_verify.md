# Conformance test: ODTIS-0517 - per-request partner verification

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0517
**Profile:** trust-network

## Procedure

1. Successful exchange with valid grant and certificate.
2. Revoke grant or certificate without closing connection.
3. Send next exchange request on same session.
4. Gateway MUST reject despite prior success.

## Pass criteria

No implicit trust from network zone or prior session alone.
