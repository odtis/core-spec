# Known implementation gaps (reference stack)

**Updated:** 2026-06-12 
**Spec:** ODTIS `0.9.0-draft`

**Project hub:** [Project hub](/project/) | **RI overview:** [Project hub](../README.md) 
**Machine-readable:** [Gap register (YAML)](gaps.yaml) | **RI map:** [RI surface map](../RI-MAP.yaml) | **Backlog:** [Phased Backlog](../PHASED-BACKLOG.md)

**Closure evidence:** [Closure Report 2026 Q2 (YAML)](../evidence/gap-closure/closure-report-2026-Q2.yaml) 
**Smoke:** `./conformance/run-gap-closure-checks.sh`

!!! info "Informative only"
    Gaps describe the **VenID reference stack**, not independent vendor obligations. Closing a gap here does not waive ODTIS MUST requirements in the spec.

---

## Deferred (4)

Resolution playbook: [Deferred production track](DEFERRED-TRACK.md)

| Gap ID | ODTIS ID | Surface | Reason | Backlog |
|--------|----------|---------|--------|---------|
| GAP-TN-0204 | ODTIS-0204 | exchange-gateway | Live mTLS interop requires staging bilateral stack | [P2-E01](../PHASED-BACKLOG.md#p2-e01-exchange-gateway-receiversender-partial) |
| GAP-TN-0217 | ODTIS-0217 | exchange-gateway | National TSA integration not in sandbox scope | P2-E06 |
| GAP-TN-TEP | - | exchange-gateway | IETF informative track | - |
| GAP-CERT-L3-ATT | ODTIS-0532 | conformance-publication | Third-party Operator L3 attestation pending | [P4-E07](../PHASED-BACKLOG.md#p4-e07-operator-l3-and-phase-4-statement-partial) |

---

## Closed (20)

All closed on **2026-06-12** with static/unit L2 sandbox evidence via `run-gap-closure-checks.sh`.

| Gap ID | ODTIS ID | Surface | Summary |
|--------|----------|---------|---------|
| GAP-IC-0308 | ODTIS-0308 | keycloak-oidc-idp | RP-initiated logout in realm export |
| GAP-IC-0315 | ODTIS-0315 | verification-api | Machine-client auth on `/verify` |
| GAP-IC-0316 | ODTIS-0316 | verification-api | LoA fields in verify response |
| GAP-IC-0317 | ODTIS-0317 | verification-api | Consent denial without attribute leak |
| GAP-IC-0535 | ODTIS-0535 | verification-api | Fail-closed consent/LoA denial |
| GAP-IC-STMT | ODTIS-0534 | conformance-publication | Statements through Phase 4 |
| GAP-OP-PH2-STMT | ODTIS-0532 | conformance-publication | Phase 2 package |
| GAP-OP-PH3-STMT | ODTIS-0532 | conformance-publication | Phase 3 package |
| GAP-OP-PH4-STMT | ODTIS-0532 | conformance-publication | Phase 4 L3-target package |
| GAP-TN-0223 | ODTIS-0223 | exchange-gateway-sender | Multi-peer routing |
| GAP-TN-0224 | ODTIS-0224 | exchange-gateway | Grant fail-closed |
| GAP-TN-0225 | ODTIS-0225 | trust-registry | Metadata-only exchange |
| GAP-TN-0215 | ODTIS-0215 | trust-authority | PKI hierarchy docs |
| GAP-TN-0216 | ODTIS-0216 | trust-service | CRL validation |
| GAP-TN-0218 | ODTIS-0218 | trust-authority | PKI ceremony docs |
| GAP-TN-0219 | ODTIS-0219 | exchange-gateway | Exchange audit correlation IDs |
| GAP-TN-0220 | ODTIS-0220 | exchange-gateway | Gateway SLA published |
| GAP-TN-0528 | ODTIS-0528 | exchange-gateway | Exchange audit events |
| GAP-TN-0535 | ODTIS-0535 | exchange-gateway | Grant denial fail-closed |
| GAP-OP-RI | ODTIS-0536 | ri-map | Phase 4 Extended surfaces mapped |

---

## Process

1. Open gap in [Gap register (YAML)](gaps.yaml) with `backlog_epic` link.
2. Update surface `status` in [RI surface map](../RI-MAP.yaml) when implementation progresses.
3. Close gap when L2 conformance test passes; do **not** weaken ODTIS MUSTs - fix code or file RFC.

Regenerate gap cross-check: `python3 scripts/validate-ri-map.py` 
Close remaining implementation gaps: `./conformance/run-gap-closure-checks.sh`
