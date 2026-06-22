# Conformance test: ODTIS-0209 - service grant required

**Status:** pending implementation
**Requirement:** ODTIS-0209
**Profile:** trust-network

## Procedure

1. Valid mTLS caller and catalogued service without grant - MUST deny.
2. Create service_access_grant for caller/provider/service.
3. Retry request - MUST allow routing to provider.

## Pass criteria

No exchange without explicit grant.
