# VenID phased implementation backlog

**ODTIS version:** `0.9.0-draft`  
**Generated:** 2026-06-22  
**Purpose:** Product backlog to implement VenID against ODTIS normative IDs and conformance tests, ordered by deployment phase.

Machine-readable: [`phased-backlog.yaml`](phased-backlog.yaml) (regenerate with `python3 scripts/generate-phased-backlog.py`).

---

## Summary

| Metric | Count |
|--------|-------|
| Epics | 39 |
| ODTIS IDs referenced | 154 (of 149 total) |
| Status DONE | 10 |
| Status PARTIAL | 29 |
| Status TODO | 0 |

## Execution order

1. Complete P0 before public ODTIS claim
2. P1 Core Identity L2 before P2 Trust Network production
3. P2 before declaring Trust Network in production (ODTIS-0532)
4. P3 Operator + E-Registry before National LoA in production
5. P4 Federation + Extended only when agreements/modules active

## Phase map (ODTIS vs Book 1)

| Backlog | ODTIS deployment phase | Profiles (production) | Book 1 gate |
|---------|------------------------|------------------------|-------------|
| **P0** | Pre-pilot (lab) | Reference Architecture | Mandato operador + RI map |
| **P1** | Phase 1 | Core Identity | 5-10 RPs; no Extended in prod |
| **P2** | Phase 2 | Core Identity + Trust Network | Nodos + grants + catalogo (D3/D4) |
| **P3** | Phase 3 | + Operator + E-Registry | Registro adapter; PKI/SOC maduro |
| **P4** | Phase 4 | + Federation + Extended | Acuerdos bilaterales activos |

---

## P0 - Spec and conformance foundation (ODTIS phase 0)

**Goal:** Publishable conformance claims, RI traceability, L1 lab ready.  
**Book 1 gate:** Mandato operador + baseline medible antes de produccion.  
**Profiles:** reference-architecture

### P0-E01 - Conformance statement pipeline [DONE]

| Field | Value |
|-------|-------|
| Component | `odtis/conformance + operator docs` |
| Repo | `odtis/core-spec` |
| ODTIS IDs | `ODTIS-0008`, `ODTIS-0532`, `ODTIS-0534`, `ODTIS-0010` |
| Conformance | 4 test(s) |

**Work items:**

- [ ] Template YAML/MD dual-format statement from registry
- [ ] CI job: validate statement fields vs ODTIS-0008
- [ ] Publish human + machine statements per environment

**Tests (sample):**

- [`conformance/tests/operator/test_conformance_statement_dual_format.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_conformance_statement_dual_format.md)
- [`conformance/tests/operator/test_phase_declaration.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_phase_declaration.md)
- [`conformance/tests/reference-architecture/test_applicable_tests_required.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/reference-architecture/test_applicable_tests_required.md)
- [`conformance/tests/reference-architecture/test_statement_minimum_fields.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/reference-architecture/test_statement_minimum_fields.md)

---

### P0-E02 - Profile claim guardrails [DONE]

| Field | Value |
|-------|-------|
| Component | `conformance lab` |
| Repo | `odtis/core-spec` |
| ODTIS IDs | `ODTIS-0001`, `ODTIS-0002`, `ODTIS-0003`, `ODTIS-0004`, `ODTIS-0005`, `ODTIS-0006`, `ODTIS-0007`, `ODTIS-0009` |
| Conformance | 8 test(s) |

**Work items:**

- [ ] Automated check: declared profiles match depends_on chain
- [ ] Reject prohibited marketing claims in statement linter

**Tests (sample):**

- [`conformance/tests/reference-architecture/test_extended_no_weakening.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/reference-architecture/test_extended_no_weakening.md)
- [`conformance/tests/reference-architecture/test_federation_requires_trust_network.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/reference-architecture/test_federation_requires_trust_network.md)
- [`conformance/tests/reference-architecture/test_layer2_requires_layer1.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/reference-architecture/test_layer2_requires_layer1.md)
- [`conformance/tests/reference-architecture/test_minimal_claim_no_implied_profiles.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/reference-architecture/test_minimal_claim_no_implied_profiles.md)
- [`conformance/tests/reference-architecture/test_profile_declaration_complete.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/reference-architecture/test_profile_declaration_complete.md)
- ... +3 more

---

### P0-E03 - Reference implementation map [DONE]

| Field | Value |
|-------|-------|
| Component | `implementation/RI-MAP.yaml` |
| Repo | `odtis/core-spec` |
| ODTIS IDs | `ODTIS-0536` |
| Conformance | 1 test(s) |

**Work items:**

- [ ] Map every ven-* surface to ODTIS IDs and OpenAPI
- [ ] Link gaps/KNOWN-GAPS.md to backlog item status

**Tests (sample):**

- [`conformance/tests/operator/test_implementation_traceability_map.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_implementation_traceability_map.md)

---

### P0-E04 - L1 lab validators [DONE]

| Field | Value |
|-------|-------|
| Component | `conformance/sandbox` |
| Repo | `odtis/core-spec` |
| ODTIS IDs | `ODTIS-0010` |
| Conformance | 1 test(s) |

**Work items:**

- [ ] run-sandbox-check.sh against ven-identity-core sandbox
- [ ] Registry link check + manifest 100% coverage gate in CI

**Tests (sample):**

- [`conformance/tests/reference-architecture/test_applicable_tests_required.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/reference-architecture/test_applicable_tests_required.md)

---

## P1 - Pilot / sandbox - Core Identity (ODTIS phase 1)

**Goal:** Layer 1 IdP, consent, verification API; L1-L2 sandbox.  
**Book 1 gate:** 5-10 RPs piloto; sin Extended en produccion (ODTIS-0533).  
**Profiles:** reference-architecture, core-identity

### P1-E01 - LoA model and claims [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `ven-identity-core / Keycloak extension` |
| Repo | `ven-identity-core` |
| ODTIS IDs | `ODTIS-0101`, `ODTIS-0102`, `ODTIS-0103`, `ODTIS-0105`, `ODTIS-0107`, `ODTIS-0108`, `ODTIS-0306` |
| Conformance | 7 test(s) |

**Work items:**

- [ ] LoA Low/Medium/High assignment rules in identity-core
- [ ] Expose loa claim in id_token and verification API
- [ ] RP min LoA per client_id configuration

**Tests (sample):**

- [`conformance/tests/core-identity/test_high_biometric_gate.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_high_biometric_gate.md)
- [`conformance/tests/core-identity/test_loa_claim.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_loa_claim.md)
- [`conformance/tests/core-identity/test_odtis_0101.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0101.md)
- [`conformance/tests/core-identity/test_odtis_0105.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0105.md)
- [`conformance/tests/core-identity/test_odtis_0107.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0107.md)
- ... +2 more

---

### P1-E02 - OIDC IdP hardening [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `Keycloak + api-gateway` |
| Repo | `ven-identity-core` |
| ODTIS IDs | `ODTIS-0301`, `ODTIS-0302`, `ODTIS-0303`, `ODTIS-0304`, `ODTIS-0305`, `ODTIS-0307`, `ODTIS-0308` |
| Conformance | 7 test(s) |

**Work items:**

- [ ] Discovery + JWKS documented for sandbox
- [ ] Authorization Code + PKCE; JWT expiry/refresh
- [ ] redirect_uri validation; logout / end_session_endpoint (gap 0308)

**Tests (sample):**

- [`conformance/tests/core-identity/test_consent_gated_claims.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_consent_gated_claims.md)
- [`conformance/tests/core-identity/test_odtis_0301.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0301.md)
- [`conformance/tests/core-identity/test_odtis_0303.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0303.md)
- [`conformance/tests/core-identity/test_odtis_0304.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0304.md)
- [`conformance/tests/core-identity/test_pkce_required.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_pkce_required.md)
- ... +2 more

---

### P1-E03 - Registration and proofing [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `identity-core + verification-engine` |
| Repo | `ven-identity-core` |
| ODTIS IDs | `ODTIS-0309`, `ODTIS-0310`, `ODTIS-0311`, `ODTIS-0312`, `ODTIS-0313`, `ODTIS-0314` |
| Conformance | 6 test(s) |

**Work items:**

- [ ] Stable subject_id on first registration
- [ ] Document + biometric proofing pipelines with liveness
- [ ] Manual review queue for inconclusive cases

**Tests (sample):**

- [`conformance/tests/core-identity/test_account_recovery.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_account_recovery.md)
- [`conformance/tests/core-identity/test_odtis_0310.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0310.md)
- [`conformance/tests/core-identity/test_odtis_0311.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0311.md)
- [`conformance/tests/core-identity/test_odtis_0312.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0312.md)
- [`conformance/tests/core-identity/test_odtis_0313.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0313.md)
- ... +1 more

---

### P1-E04 - Verification API [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `verification-api + verification-engine` |
| Repo | `ven-identity-core` |
| ODTIS IDs | `ODTIS-0315`, `ODTIS-0316`, `ODTIS-0317`, `ODTIS-0318` |
| Conformance | 4 test(s) |

**Work items:**

- [ ] Client credentials auth for RPs
- [ ] Response: status + LoA + consented attributes only
- [ ] Run L2 tests from conformance/tests/core-identity/

**Tests (sample):**

- [`conformance/tests/core-identity/test_odtis_0316.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0316.md)
- [`conformance/tests/core-identity/test_odtis_0318.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0318.md)
- [`conformance/tests/core-identity/test_verification_client_auth.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_verification_client_auth.md)
- [`conformance/tests/core-identity/test_verification_consent_scope.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_verification_consent_scope.md)

---

### P1-E05 - RP client lifecycle [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `admin-api + identity-core` |
| Repo | `ven-identity-core` |
| ODTIS IDs | `ODTIS-0319`, `ODTIS-0320`, `ODTIS-0321`, `ODTIS-0337`, `ODTIS-0338`, `ODTIS-0339` |
| Conformance | 6 test(s) |

**Work items:**

- [ ] RP registration, rotation, suspension
- [ ] Admission criteria documented; secrets hashed

**Tests (sample):**

- [`conformance/tests/core-identity/test_odtis_0319.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0319.md)
- [`conformance/tests/core-identity/test_odtis_0320.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0320.md)
- [`conformance/tests/core-identity/test_odtis_0321.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0321.md)
- [`conformance/tests/core-identity/test_odtis_0337.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0337.md)
- [`conformance/tests/core-identity/test_odtis_0338.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0338.md)
- ... +1 more

---

### P1-E06 - Consent and privacy [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `consent-service + citizen-api` |
| Repo | `ven-identity-core` |
| ODTIS IDs | `ODTIS-0328`, `ODTIS-0329`, `ODTIS-0330`, `ODTIS-0331`, `ODTIS-0332`, `ODTIS-0333`, `ODTIS-0334`, `ODTIS-0335`, `ODTIS-0336` |
| Conformance | 9 test(s) |

**Work items:**

- [ ] Explicit consent before first release; revocation effective next request
- [ ] Consent UI fields; privacy policy + DSAR process
- [ ] TLS + encryption at rest; no sale/profiling

**Tests (sample):**

- [`conformance/tests/core-identity/test_consent_revocation.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_consent_revocation.md)
- [`conformance/tests/core-identity/test_explicit_consent_first_release.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_explicit_consent_first_release.md)
- [`conformance/tests/core-identity/test_odtis_0329.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0329.md)
- [`conformance/tests/core-identity/test_odtis_0331.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0331.md)
- [`conformance/tests/core-identity/test_odtis_0332.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0332.md)
- ... +4 more

---

### P1-E07 - Citizen portal [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `portal-ciudadano + citizen-api` |
| Repo | `ven-identity-core` |
| ODTIS IDs | `ODTIS-0322`, `ODTIS-0323`, `ODTIS-0324` |
| Conformance | 3 test(s) |

**Work items:**

- [ ] Status, connected RPs, consent revoke UX
- [ ] Operator-configured locales; responsive web

**Tests (sample):**

- [`conformance/tests/core-identity/test_odtis_0322.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0322.md)
- [`conformance/tests/core-identity/test_odtis_0323.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0323.md)
- [`conformance/tests/core-identity/test_odtis_0324.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0324.md)

---

### P1-E08 - Identity transport and rate limits [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `api-gateway + services` |
| Repo | `ven-identity-core` |
| ODTIS IDs | `ODTIS-0325`, `ODTIS-0326`, `ODTIS-0327`, `ODTIS-0521`, `ODTIS-0522`, `ODTIS-0523` |
| Conformance | 6 test(s) |

**Work items:**

- [ ] TLS 1.2+ on all public endpoints
- [ ] Rate limiting auth/verify; OWASP baseline
- [ ] MFA for sensitive actions; liveness in High LoA path

**Tests (sample):**

- [`conformance/tests/core-identity/test_liveness_high_loa.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_liveness_high_loa.md)
- [`conformance/tests/core-identity/test_odtis_0325.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0325.md)
- [`conformance/tests/core-identity/test_odtis_0326.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0326.md)
- [`conformance/tests/core-identity/test_odtis_0327.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0327.md)
- [`conformance/tests/core-identity/test_owasp_baseline.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_owasp_baseline.md)
- ... +1 more

---

### P1-E09 - Identity audit events [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `identity-core events + audit export` |
| Repo | `ven-identity-core` |
| ODTIS IDs | `ODTIS-0526`, `ODTIS-0527`, `ODTIS-0529` |
| Conformance | 3 test(s) |

**Work items:**

- [ ] Emit registration, verification, LoA, consent events
- [ ] Standard envelope with trace_id + timestamp

**Tests (sample):**

- [`conformance/tests/core-identity/test_consent_audit_events.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_consent_audit_events.md)
- [`conformance/tests/core-identity/test_identity_audit_events.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_identity_audit_events.md)
- [`conformance/tests/operator/test_event_envelope.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_event_envelope.md)

---

### P1-E10 - Phase 1 conformance package [DONE]

| Field | Value |
|-------|-------|
| Component | `operator publication` |
| Repo | `odtis/core-spec` |
| ODTIS IDs | `ODTIS-0533` |
| Conformance | 1 test(s) |

**Work items:**

- [ ] Production statement: Core Identity only, phase=1, no Extended
- [ ] L2 test report for declared Core Identity IDs

**Tests (sample):**

- [`conformance/tests/operator/test_phase1_no_extended_claims.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_phase1_no_extended_claims.md)

---

## P2 - Production Layer 2 - Trust Network (ODTIS phase 2)

**Goal:** Exchange gateway, catalog, grants, multi-peer routing; TN L2.  
**Book 1 gate:** Nodos institucionales + grants + catalogo consumido (D3/D4).  
**Profiles:** core-identity, trust-network

### P2-E01 - Exchange gateway receiver/sender [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `ven-trust-exchange-gateway` |
| Repo | `ven-trust-network` |
| ODTIS IDs | `ODTIS-0201`, `ODTIS-0202`, `ODTIS-0203`, `ODTIS-0204`, `ODTIS-0205`, `ODTIS-0206`, `ODTIS-0207` |
| Conformance | 7 test(s) |

**Work items:**

- [ ] All partner traffic via local gateway
- [ ] Receiver validates partner against trust registry
- [ ] mTLS gateway-to-gateway live interop test (KNOWN-GAP 0204)

**Tests (sample):**

- [`conformance/tests/trust-network/test_gateway_mtls.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_gateway_mtls.md)
- [`conformance/tests/trust-network/test_gateway_only_routing.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_gateway_only_routing.md)
- [`conformance/tests/trust-network/test_odtis_0202.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_odtis_0202.md)
- [`conformance/tests/trust-network/test_odtis_0203.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_odtis_0203.md)
- [`conformance/tests/trust-network/test_odtis_0206.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_odtis_0206.md)
- ... +2 more

---

### P2-E02 - Service catalog [DONE]

| Field | Value |
|-------|-------|
| Component | `ven-trust-registry` |
| Repo | `ven-trust-network` |
| ODTIS IDs | `ODTIS-0208`, `ODTIS-0222`, `ODTIS-0212`, `ODTIS-0213`, `ODTIS-0214` |
| Conformance | 5 test(s) |

**Work items:**

- [ ] Stable service_id + gateway_base_url per remote peer (FASE-4)
- [ ] GET /registry/services?serviceId= and caller_partner_id filters
- [ ] Configurable cache refresh; optional @VenPartnerService autodiscovery

**Tests (sample):**

- [`conformance/tests/trust-network/test_catalog_gateway_base_url.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_catalog_gateway_base_url.md)
- [`conformance/tests/trust-network/test_odtis_0208.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_odtis_0208.md)
- [`conformance/tests/trust-network/test_odtis_0212.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_odtis_0212.md)
- [`conformance/tests/trust-network/test_odtis_0213.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_odtis_0213.md)
- [`conformance/tests/trust-network/test_odtis_0214.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_odtis_0214.md)

---

### P2-E03 - Service access grants [DONE]

| Field | Value |
|-------|-------|
| Component | `trust-registry + portal-api` |
| Repo | `ven-trust-network` |
| ODTIS IDs | `ODTIS-0209`, `ODTIS-0210`, `ODTIS-0211`, `ODTIS-0224`, `ODTIS-0226` |
| Conformance | 5 test(s) |

**Work items:**

- [ ] Grants bind caller, provider, service_id
- [ ] Fail closed on grant denial (no implicit zone trust)
- [ ] Auditable grant request/approve/revoke workflows

**Tests (sample):**

- [`conformance/tests/trust-network/test_grant_fail_closed.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_grant_fail_closed.md)
- [`conformance/tests/trust-network/test_grant_workflow_audit.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_grant_workflow_audit.md)
- [`conformance/tests/trust-network/test_odtis_0210.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_odtis_0210.md)
- [`conformance/tests/trust-network/test_odtis_0211.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_odtis_0211.md)
- [`conformance/tests/trust-network/test_service_grant_required.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_service_grant_required.md)

---

### P2-E04 - Multi-peer sender routing [DONE]

| Field | Value |
|-------|-------|
| Component | `exchange-gateway sender + sdk` |
| Repo | `ven-trust-network` |
| ODTIS IDs | `ODTIS-0223` |
| Conformance | 1 test(s) |

**Work items:**

- [ ] Resolve route by X-Exchange-Service / service_id
- [ ] ExchangeGatewayClient SDK documented in FASE-4
- [ ] Remove single hard-coded remote-gateway-url for prod

**Tests (sample):**

- [`conformance/tests/trust-network/test_sender_multi_peer_routing.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_sender_multi_peer_routing.md)

---

### P2-E05 - Metadata-only exchange (D4) [DONE]

| Field | Value |
|-------|-------|
| Component | `trust-registry + audit` |
| Repo | `ven-trust-network` |
| ODTIS IDs | `ODTIS-0225` |
| Conformance | 1 test(s) |

**Work items:**

- [ ] Catalog/audit stores: routing metadata only, not authoritative payloads
- [ ] Review persistence layer for payload centralization

**Tests (sample):**

- [`conformance/tests/trust-network/test_no_payload_centralization.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_no_payload_centralization.md)

---

### P2-E06 - Trust Network PKI [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `trust-authority + central-server` |
| Repo | `ven-trust-network` |
| ODTIS IDs | `ODTIS-0215`, `ODTIS-0216`, `ODTIS-0217`, `ODTIS-0218`, `ODTIS-0106` |
| Conformance | 5 test(s) |

**Work items:**

- [ ] Partner/service cert hierarchy; CRL/OCSP validation
- [ ] Document FAL controls and ceremony docs

**Tests (sample):**

- [`conformance/tests/core-identity/test_odtis_0106.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0106.md)
- [`conformance/tests/trust-network/test_cert_revocation.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_cert_revocation.md)
- [`conformance/tests/trust-network/test_odtis_0215.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_odtis_0215.md)
- [`conformance/tests/trust-network/test_odtis_0217.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_odtis_0217.md)
- [`conformance/tests/trust-network/test_odtis_0218.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_odtis_0218.md)

---

### P2-E07 - Exchange audit and SLA [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `audit-service + operator policy` |
| Repo | `ven-trust-network` |
| ODTIS IDs | `ODTIS-0219`, `ODTIS-0220`, `ODTIS-0221`, `ODTIS-0528`, `ODTIS-0517` |
| Conformance | 5 test(s) |

**Work items:**

- [ ] Exchange events with correlation IDs
- [ ] Published gateway SLA; verify partner every request

**Tests (sample):**

- [`conformance/tests/trust-network/test_exchange_audit_events.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_exchange_audit_events.md)
- [`conformance/tests/trust-network/test_odtis_0219.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_odtis_0219.md)
- [`conformance/tests/trust-network/test_odtis_0220.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_odtis_0220.md)
- [`conformance/tests/trust-network/test_odtis_0221.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_odtis_0221.md)
- [`conformance/tests/trust-network/test_per_request_partner_verify.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/trust-network/test_per_request_partner_verify.md)

---

### P2-E08 - Fail-closed cross-layer [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `identity + trust integration` |
| Repo | `ven-identity-core + ven-trust-network` |
| ODTIS IDs | `ODTIS-0535` |
| Conformance | 1 test(s) |

**Work items:**

- [ ] Unified denial behavior: OIDC, Verification API, exchange grants
- [ ] Integration tests: zero attribute leakage on deny

**Tests (sample):**

- [`conformance/tests/operator/test_fail_closed_denial_paths.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_fail_closed_denial_paths.md)

---

### P2-E09 - Phase 2 conformance package [DONE]

| Field | Value |
|-------|-------|
| Component | `operator publication` |
| Repo | `odtis/core-spec` |
| ODTIS IDs | `ODTIS-0532` |
| Conformance | 1 test(s) |

**Work items:**

- [ ] Statement: phase=2, Core Identity + Trust Network L2
- [ ] Full trust-network test suite green in staging

**Tests (sample):**

- [`conformance/tests/operator/test_phase_declaration.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_phase_declaration.md)

---

## P3 - National operator (ODTIS phase 3)

**Goal:** Operator PKI/governance, audit/regulator, E-Registry, federation prep.  
**Book 1 gate:** Registro civil adapter Phase 3+; SOC/PKI maduro.  
**Profiles:** operator, extended/E-Registry, federation/prep

### P3-E01 - Operator governance [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `portal-operador + policy docs` |
| Repo | `ven-identity-core + docs` |
| ODTIS IDs | `ODTIS-0501`, `ODTIS-0502`, `ODTIS-0503`, `ODTIS-0504`, `ODTIS-0505`, `ODTIS-0506` |
| Conformance | 6 test(s) |

**Work items:**

- [ ] Publish scope, governance units, subject admin procedures
- [ ] Phase-appropriate PKI/SOC in conformance statement

**Tests (sample):**

- [`conformance/tests/operator/test_no_false_phase4_claims.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_no_false_phase4_claims.md)
- [`conformance/tests/operator/test_odtis_0502.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_odtis_0502.md)
- [`conformance/tests/operator/test_odtis_0503.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_odtis_0503.md)
- [`conformance/tests/operator/test_odtis_0505.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_odtis_0505.md)
- [`conformance/tests/operator/test_operator_subject_admin.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_operator_subject_admin.md)
- ... +1 more

---

### P3-E02 - Operator PKI stewardship [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `trust-authority + HSM runbooks` |
| Repo | `ven-trust-network` |
| ODTIS IDs | `ODTIS-0507`, `ODTIS-0508`, `ODTIS-0509`, `ODTIS-0510` |
| Conformance | 4 test(s) |

**Work items:**

- [ ] CP/CPS publication; dual-control ceremonies
- [ ] CRL/OCSP; tested PKI DR on schedule

**Tests (sample):**

- [`conformance/tests/operator/test_cp_cps_published.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_cp_cps_published.md)
- [`conformance/tests/operator/test_odtis_0508.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_odtis_0508.md)
- [`conformance/tests/operator/test_odtis_0509.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_odtis_0509.md)
- [`conformance/tests/operator/test_odtis_0510.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_odtis_0510.md)

---

### P3-E03 - SLA, partners, metrics [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `operator policy + reports-api` |
| Repo | `ven-identity-core` |
| ODTIS IDs | `ODTIS-0511`, `ODTIS-0512`, `ODTIS-0513` |
| Conformance | 3 test(s) |

**Work items:**

- [ ] IdP/Verification availability targets
- [ ] Partner onboarding rules; ecosystem metrics export

**Tests (sample):**

- [`conformance/tests/operator/test_odtis_0511.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_odtis_0511.md)
- [`conformance/tests/operator/test_odtis_0512.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_odtis_0512.md)
- [`conformance/tests/operator/test_odtis_0513.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_odtis_0513.md)

---

### P3-E04 - Regulator, incidents, liability [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `regulator-api + legal docs` |
| Repo | `ven-identity-core` |
| ODTIS IDs | `ODTIS-0514`, `ODTIS-0515`, `ODTIS-0516` |
| Conformance | 3 test(s) |

**Work items:**

- [ ] Aggregated audit export without bulk PII
- [ ] Incident runbook; liability in ToS and RP contracts

**Tests (sample):**

- [`conformance/tests/operator/test_liability_documentation.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_liability_documentation.md)
- [`conformance/tests/operator/test_odtis_0515.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_odtis_0515.md)
- [`conformance/tests/operator/test_regulator_export.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_regulator_export.md)

---

### P3-E05 - Security and secrets platform [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `infra + all services` |
| Repo | `ven-infra-core` |
| ODTIS IDs | `ODTIS-0518`, `ODTIS-0519`, `ODTIS-0520`, `ODTIS-0525` |
| Conformance | 4 test(s) |

**Work items:**

- [ ] No sensitive microservices on public internet
- [ ] Secrets manager for RP secrets and PKI keys
- [ ] Fraud monitoring dashboard + manual review SLA

**Tests (sample):**

- [`conformance/tests/operator/test_fraud_metrics.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_fraud_metrics.md)
- [`conformance/tests/operator/test_internal_services_not_public.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_internal_services_not_public.md)
- [`conformance/tests/operator/test_odtis_0520.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_odtis_0520.md)
- [`conformance/tests/operator/test_secrets_manager.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_secrets_manager.md)

---

### P3-E06 - Audit platform and regulator export [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `audit-service + reports-api` |
| Repo | `ven-trust-network + ven-identity-core` |
| ODTIS IDs | `ODTIS-0530` |
| Conformance | 1 test(s) |

**Work items:**

- [ ] Tamper-evident storage; PII-minimized regulator export
- [ ] Cross-link identity + exchange audit by correlation_id

**Tests (sample):**

- [`conformance/tests/operator/test_audit_export_pii_minimized.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_audit_export_pii_minimized.md)

---

### P3-E07 - E-Registry adapter [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `new eregistry-adapter service` |
| Repo | `ven-identity-core (TBD)` |
| ODTIS IDs | `ODTIS-0104`, `ODTIS-0344`, `ODTIS-0349`, `ODTIS-0350`, `ODTIS-0351`, `ODTIS-0352`, `ODTIS-0353` |
| Conformance | 7 test(s) |

**Work items:**

- [ ] National LoA only with E-Registry declared + adapter active
- [ ] Phase 3+ activation; bilateral agreement with registry authority
- [ ] Hashing only; no raw biometric persistence; audit every verification

**Tests (sample):**

- [`conformance/tests/core-identity/test_odtis_0104.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0104.md)
- [`conformance/tests/extended/test_eregistry_declaration_required.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/extended/test_eregistry_declaration_required.md)
- [`conformance/tests/extended/test_eregistry_no_civil_authority.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/extended/test_eregistry_no_civil_authority.md)
- [`conformance/tests/extended/test_eregistry_phase3_activation.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/extended/test_eregistry_phase3_activation.md)
- [`conformance/tests/extended/test_national_loa_after_adapter.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/extended/test_national_loa_after_adapter.md)
- ... +2 more

---

### P3-E08 - Federation agreements (prep) [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `trust-registry federation module` |
| Repo | `ven-trust-network` |
| ODTIS IDs | `ODTIS-0401`, `ODTIS-0402`, `ODTIS-0403`, `ODTIS-0404`, `ODTIS-0405`, `ODTIS-0406` |
| Conformance | 6 test(s) |

**Work items:**

- [ ] Bilateral agreement store: instance IDs, validity, pinned roots
- [ ] Reject federated routes without direct agreement
- [ ] Regulator export of agreement metadata (SHOULD)

**Tests (sample):**

- [`conformance/tests/federation/test_agreement_required_fields.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/federation/test_agreement_required_fields.md)
- [`conformance/tests/federation/test_explicit_activation.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/federation/test_explicit_activation.md)
- [`conformance/tests/federation/test_federation_cert_policy.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/federation/test_federation_cert_policy.md)
- [`conformance/tests/federation/test_federation_regulator_export.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/federation/test_federation_regulator_export.md)
- [`conformance/tests/federation/test_non_transitivity.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/federation/test_non_transitivity.md)
- ... +1 more

---

### P3-E09 - Phase 3 conformance package [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `operator publication` |
| Repo | `odtis/core-spec` |
| ODTIS IDs | `ODTIS-0532` |
| Conformance | 1 test(s) |

**Work items:**

- [ ] Statement: phase=3, Operator L2-L3, E-Registry if active
- [ ] Third-party or internal audit dry-run

**Tests (sample):**

- [`conformance/tests/operator/test_phase_declaration.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_phase_declaration.md)

---

## P4 - Full mandate (ODTIS phase 4)

**Goal:** Federation production, Extended modules, Operator L3.  
**Book 1 gate:** Acuerdos bilaterales activos; modulos Extended declarados.  
**Profiles:** federation, extended, operator/L3

### P4-E01 - Federation runtime [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `exchange-gateway federation router` |
| Repo | `ven-trust-network` |
| ODTIS IDs | `ODTIS-0407`, `ODTIS-0408` |
| Conformance | 2 test(s) |

**Work items:**

- [ ] Suspend/expired agreements disable routing within cache bounds
- [ ] Federated audit: local + remote trust instance IDs

**Tests (sample):**

- [`conformance/tests/federation/test_agreement_suspension_routing.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/federation/test_agreement_suspension_routing.md)
- [`conformance/tests/federation/test_federated_audit_instance_ids.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/federation/test_federated_audit_instance_ids.md)

---

### P4-E02 - E-Wallet (OID4VP) [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `wallet issuer + wallet app` |
| Repo | `ven-identity-core (TBD)` |
| ODTIS IDs | `ODTIS-0340`, `ODTIS-0341`, `ODTIS-0342`, `ODTIS-0343`, `ODTIS-0524` |
| Conformance | 5 test(s) |

**Work items:**

- [ ] OID4VP presentations; issuer trust via trust registry
- [ ] Selective disclosure; shared LoA with Path A OIDC

**Tests (sample):**

- [`conformance/tests/core-identity/test_odtis_0340.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0340.md)
- [`conformance/tests/core-identity/test_odtis_0341.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0341.md)
- [`conformance/tests/core-identity/test_odtis_0342.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0342.md)
- [`conformance/tests/core-identity/test_odtis_0343.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/core-identity/test_odtis_0343.md)
- [`conformance/tests/operator/test_odtis_0524.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_odtis_0524.md)

---

### P4-E03 - E-Inclusion [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `inclusion onboarding flows` |
| Repo | `ven-identity-core` |
| ODTIS IDs | `ODTIS-0354`, `ODTIS-0355`, `ODTIS-0356`, `ODTIS-0357` |
| Conformance | 4 test(s) |

**Work items:**

- [ ] Assisted consent; representative verification
- [ ] No LoA bypass; accessibility/offline where policy allows

**Tests (sample):**

- [`conformance/tests/extended/test_inclusion_accessibility_offline.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/extended/test_inclusion_accessibility_offline.md)
- [`conformance/tests/extended/test_inclusion_assisted_consent.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/extended/test_inclusion_assisted_consent.md)
- [`conformance/tests/extended/test_inclusion_no_loa_bypass.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/extended/test_inclusion_no_loa_bypass.md)
- [`conformance/tests/extended/test_inclusion_representative_verify.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/extended/test_inclusion_representative_verify.md)

---

### P4-E04 - E-Webhook [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `verification-api webhooks` |
| Repo | `ven-identity-core` |
| ODTIS IDs | `ODTIS-0358`, `ODTIS-0359`, `ODTIS-0360`, `ODTIS-0531` |
| Conformance | 4 test(s) |

**Work items:**

- [ ] RP webhook registration API (OpenAPI pending)
- [ ] Signed payloads, retry/backoff, PII minimization

**Tests (sample):**

- [`conformance/tests/extended/test_ewebhook_pii_minimize.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/extended/test_ewebhook_pii_minimize.md)
- [`conformance/tests/extended/test_ewebhook_retry_backoff.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/extended/test_ewebhook_retry_backoff.md)
- [`conformance/tests/extended/test_ewebhook_rp_registration.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/extended/test_ewebhook_rp_registration.md)
- [`conformance/tests/operator/test_odtis_0531.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_odtis_0531.md)

---

### P4-E05 - E-Signature [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `signature service` |
| Repo | `ven-identity-core (TBD)` |
| ODTIS IDs | `ODTIS-0361`, `ODTIS-0362`, `ODTIS-0363` |
| Conformance | 3 test(s) |

**Work items:**

- [ ] Sign bound to LoA; keys under operator PKI/TSP
- [ ] Auditable sign/verify events

**Tests (sample):**

- [`conformance/tests/extended/test_esignature_audit_events.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/extended/test_esignature_audit_events.md)
- [`conformance/tests/extended/test_esignature_loa_binding.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/extended/test_esignature_loa_binding.md)
- [`conformance/tests/extended/test_esignature_pki_keys.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/extended/test_esignature_pki_keys.md)

---

### P4-E06 - E-KYB (preview) [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `kyb module` |
| Repo | `ven-identity-core (TBD)` |
| ODTIS IDs | `ODTIS-0364`, `ODTIS-0365` |
| Conformance | 2 test(s) |

**Work items:**

- [ ] Legal entity verification separate from natural person
- [ ] Link representatives to verified subjects before B2B release

**Tests (sample):**

- [`conformance/tests/extended/test_ekyb_entity_separate.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/extended/test_ekyb_entity_separate.md)
- [`conformance/tests/extended/test_ekyb_representative_link.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/extended/test_ekyb_representative_link.md)

---

### P4-E07 - Operator L3 and Phase 4 statement [PARTIAL]

| Field | Value |
|-------|-------|
| Component | `governance + external audit` |
| Repo | `odtis/core-spec` |
| ODTIS IDs | `ODTIS-0532`, `ODTIS-0006` |
| Conformance | 2 test(s) |

**Work items:**

- [ ] L3 attestation; all claimed profiles + Extended modules listed
- [ ] Extended must not weaken base profile controls

**Tests (sample):**

- [`conformance/tests/operator/test_phase_declaration.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/operator/test_phase_declaration.md)
- [`conformance/tests/reference-architecture/test_extended_no_weakening.md`](https://github.com/odtis/core-spec/blob/main/conformance/tests/reference-architecture/test_extended_no_weakening.md)

---

## Definition of done (per epic)

1. All listed **ODTIS IDs** satisfied in target environment.
2. Linked **conformance tests** executed at L2 (staging) with pass evidence.
3. **RI-MAP.yaml** updated with component surface mapping.
4. **KNOWN-GAPS.md** entry closed or deferred with RFC.
5. Conformance statement updated (`ODTIS-0532`, `ODTIS-0534`).

## Related

- [`RI-MAP.yaml`](RI-MAP.yaml)
- [`gaps/KNOWN-GAPS.md`](gaps/KNOWN-GAPS.md)
- [`../conformance/manifest.yaml`](../conformance/manifest.yaml)
- [`../spec/10-deployment-profiles/SPEC.md`](../spec/10-deployment-profiles/SPEC.md)
- [Adoption guide](https://github.com/odtis/core-spec/blob/main/ADOPTION.md)
