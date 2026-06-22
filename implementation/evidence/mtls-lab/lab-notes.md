# mTLS lab evidence (GAP-TN-0204 / #10)

**Status:** L2 sandbox - staging overlay only (not production PKI).

## Assets

| Path | Purpose |
|------|---------|
| `core-impl/ven-trust-network/deploy/mtls-lab/generate-certs.sh` | Regenerates lab CA, server, partner PKCS#12 |
| `core-impl/ven-trust-network/deploy/mtls-lab/certs/` | Committed lab certs (private `*.key` gitignored) |
| `core-impl/compose/staging/docker-compose.mtls.yml` | Enables `SERVER_SSL_CLIENT_AUTH=need` on port 9443 |
| `V17__mtls_lab_partner.sql` | Seeds partner `MTLSLAB` with fixed thumbprint |

Fixed partner thumbprint (SHA-256 DER): `ac5113b43f6e9c9dd2b3d2b1243a930a4e9abb0cf4c3291f41bb1796edd14965`

## Smoke

```bash
cd core-impl && ./scripts/mtls-staging-up.sh
cd core-impl/ven-trust-network && ./scripts/mtls-live-check.sh
cd core-spec && ./conformance/run-mtls-live-checks.sh
```

## Pass criteria (ODTIS-0204)

1. TLS handshake without client certificate fails when overlay is active.
2. Handshake with lab partner PKCS#12 succeeds; `/exchange/health` returns 200.
3. TLS protocol ≥ 1.2 (openssl probe).
