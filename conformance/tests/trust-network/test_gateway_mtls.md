# Conformance test: ODTIS-0204 - gateway mTLS

**Status:** implemented (static + unit + live staging smoke)
**Requirement:** ODTIS-0204
**Profile:** trust-network

## Automation

```bash
# Static + unit (CI-safe)
cd core-impl/ven-trust-network && ./scripts/mtls-live-check.sh

# Live (requires staging overlay on port 9443)
cd core-impl && ./scripts/mtls-staging-up.sh
cd core-impl/ven-trust-network && ./scripts/mtls-live-check.sh

# Conformance wrapper
cd core-spec && ./conformance/run-mtls-live-checks.sh
```

Evidence: `implementation/evidence/mtls-lab/lab-notes.md`

## Procedure

1. Initiate gateway-to-gateway TLS without client certificate — MUST fail handshake.
2. Repeat with valid partner client certificate (lab PKCS#12 under `deploy/mtls-lab/certs/`) — MUST succeed; `GET /exchange/health` returns 200.
3. Verify TLS version ≥ 1.2 (openssl `s_client` probe).

## Pass criteria

Mutual TLS required for gateway exchange on staging overlay (`SERVER_SSL_CLIENT_AUTH=need`).
