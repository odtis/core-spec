# ODTIS positioning vs OpenID Foundation specifications

**ODTIS version:** see [Version](../../VERSION) 
**Governance:** [Project hub](../README.md) | **Project:** [Project hub](/project/) 
**Reference index:** [OpenID Foundation - All Specifications](https://openid.net/developers/specs/)

---

## Summary

| Layer | ODTIS role | External spec |
|-------|------------|---------------|
| **Layer 1 IdP** | Profile + deltas | [OIDC Core](https://openid.net/specs/openid-connect-core-1_0.html), [Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html), RFC 7636 PKCE |
| **Identity assurance** | LoA + Verification API | [OIDC Identity Assurance 1.0](https://openid.net/developers/specs/) |
| **Wallet / VC** | Extended E-Wallet module | [OID4VCI](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html), [OID4VP](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) |
| **High-security OAuth** | Optional binding | [FAPI 2.0 Security Profile](https://openid.net/developers/specs/) |
| **Government OAuth/OIDC** | Optional binding | [iGov profiles](https://openid.net/developers/specs/) (Implementer's Draft) |
| **Layer 2 exchange** | **ODTIS-native** (TEP) | X-Road (informative); not OIDF |
| **Federation** | **ODTIS bilateral operators** | **≠** [OpenID Federation 1.1](https://openid.net/developers/specs/) |

---

## Critical disambiguation: Federation

| | **OpenID Federation** | **ODTIS Federation (section 6)** |
|--|----------------------|----------------------------|
| **Parties** | OPs, RPs, OAuth clients | Trust network **operators** |
| **Trust model** | Multilateral federation metadata | **Bilateral** agreements, **non-transitive** |
| **Protocol** | JWT trust chains, entity statements | Gateway routing + pinned CA + service whitelist |
| **Use when** | OIDC/OAuth federation at scale | Cross-network institutional exchange |

Implementers MUST NOT assume OpenID Federation satisfies ODTIS Federation profile requirements.

---

## Core Identity binding (normative intent)

Core Identity conformance **requires**:

1. OAuth 2.0 ([RFC 6749](https://www.rfc-editor.org/rfc/rfc6749))
2. OpenID Connect Core 1.0
3. OpenID Connect Discovery 1.0
4. PKCE S256 ([RFC 7636](https://www.rfc-editor.org/rfc/rfc7636))
5. ODTIS deltas in [Section 3 - Identity services](../../spec/03-identity-services/SPEC.md) and [Core Identity profile](../../spec/profiles/core-identity-profile.md)

See Annex C [Standards catalog](/annexes/C-standards-mapping/standards.yaml).

---

## Extended E-Wallet binding

E-Wallet sub-module SHOULD implement OID4VCI + OID4VP Final specifications and declare ODTIS-5.4.x + audit obligations. ODTIS MUST NOT duplicate OID4VP protocol details.

---

## Related

- [IETF scoping](IETF-SCOPING.md)
- [Annex C - Standards mapping](/annexes/C-standards-mapping/)
