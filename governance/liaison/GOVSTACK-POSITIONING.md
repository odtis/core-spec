# ODTIS positioning vs GovStack building blocks

**ODTIS version:** see [Version](../../VERSION) 
**GovStack specs:** https://specs.govstack.global/

**Project hub:** [Project hub](/project/) | **OIDF:** [OIDF positioning](OIDF-POSITIONING.md)

---

## Summary

| GovStack concept | ODTIS mapping | Gap ODTIS closes |
|------------------|---------------|------------------|
| **Identity BB** | Core Identity profile (sections 2-3, 5) | LoA + OIDC + consent + verification API |
| **Information Mediator (IM) BB** | Trust Network profile (section 4) - **partial** | Grants, participant registry, operator SLA |
| **Payments / Registries BB** | Out of ODTIS scope | Adopter integrates separately |
| **Building block catalog** | Informative modular DPI | ODTIS **unifies L1+L2 contract** on one operator |

**Policy message (Book 1 section 2.13):** GovStack modularizes capabilities; ODTIS normativizes the **connector contract** between identity and institutional exchange.

---

## Information Mediator vs ODTIS Trust Network

| Dimension | GovStack IM | ODTIS Trust Network |
|-----------|-------------|---------------------|
| Scope | Public-sector data exchange | Public + private Phase 1 RPs |
| Identity reuse | Assumes separate Identity BB | Core Identity **integrated** with gateway |
| Trust registry | IM service registry (informative) | **Dual registry**: issuer (L1) + participant (L2) |
| Authorization | IM access rights (BB spec) | `service_access_grants` + auditable deny |
| Operator | Implicit per country deployment | Explicit DTI operator model (section 7) |

Implementers MAY map GovStack IM components to ODTIS gateway + participant registry when deploying public-sector nodes. ODTIS conformance **MUST NOT** be claimed from IM BB documentation alone.

---

## UXP (regional reference)

**UXP** (Malaysia and regional variants derived from X-Road) is a **regional exchange reference**, not the IM BB product name in GovStack specs 2025-26. ODTIS maps UXP-style patterns to Trust Network semantics (mTLS, service catalog, audit) informatively via X-Road alignment (section 4.12).

---

## Building block crosswalk (informative)

| GovStack BB (informative ID) | ODTIS profile / section | Notes |
|------------------------------|-------------------------|-------|
| `govstack-bb-identity` | Core Identity | OIDC-first; wallet via Extended E-Wallet |
| `govstack-bb-information-mediator` | Trust Network section 4.3-4.6, section 4.11 | Grants + participant registry |
| `govstack-bb-consent` | Section 5 | Purpose limitation, RP admission |
| `govstack-bb-payments` | - | Out of scope |
| `govstack-bb-registration` | E-Registry (Annex D) | Civil registry adapter Phase 3+ |

Full matrix: Paper P18 section 2.6 | Annex C (planned merge at v1.0).

---

## Related

- [OIDF positioning](OIDF-POSITIONING.md) - OpenID Federation ≠ ODTIS Federation
- [Section 4 - Trust network](../../spec/04-trust-network/SPEC.md) section 4.11
- Book 1 section 2.13 | Book 2 ch. 2 section 2.8
