# E-Webhook staging evidence (#14)

**Status:** L2 sandbox — static + optional live delivery validation.

## Artifacts

| Path | Role |
| --- | --- |
| `deploy/ewebhook-lab/receiver.py` | Lab receiver with HMAC verify + retry simulation |
| `compose/staging/docker-compose.ewebhook.yml` | Activates webhooks + lab dispatch + receiver |
| `scripts/ewebhook-staging-up.sh` | Start overlay on base stack |
| `scripts/ewebhook-live-check.sh` | Live HMAC, PII minimize, retry probes |

## Smoke

```bash
cd core-impl && ./scripts/ewebhook-overlay-check.sh
cd ven-identity-core && ./scripts/ewebhook-check.sh
cd core-spec && ./conformance/run-ewebhook-staging-checks.sh
```

## Live staging (optional)

```bash
cd core-impl && ./scripts/ewebhook-staging-up.sh
cd core-impl && ./scripts/ewebhook-live-check.sh
```

## Pass criteria (#14)

1. Default pilot keeps `venid.webhook.active: false`.
2. Staging overlay registers receiver and enables delivery + lab dispatch.
3. Live run validates HMAC (`ODTIS-0531`), PII minimization (`ODTIS-0360`), retry (`ODTIS-0359`), registration (`ODTIS-0358`).
