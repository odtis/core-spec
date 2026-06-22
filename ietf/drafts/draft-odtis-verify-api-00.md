# draft-odtis-verify-api-00 - Verification API HTTP Profile (working draft)

**Status:** markdown working draft 
**ODTIS source:** section 3.5, Annex A S2 `verification-api.openapi.yaml`

**IETF track:** [Project hub](../README.md) | **Project:** [Project hub](/project/)

**Authors:** Manuel Mérida Oliveros

---

## Abstract

This document defines an HTTP profile for server-to-server identity verification between Relying Parties and an operator's Verification API, including assurance level reporting, consent scope enforcement, and client authentication.

---

## 1. Scope

Normative HTTP semantics for verify operations. Does not replace OpenID Connect for browser login.

---

## 2. Relationship to OIDC Identity Assurance

Implementations MAY map `assurance_level` to [OpenID Connect for Identity Assurance 1.0](https://openid.net/developers/specs/) verified claims where applicable.

---

## 3. OpenAPI

Authoritative machine-readable contract: [Verification API (OpenAPI)](/annexes/A-openapi-registry/verification-api.openapi.yaml) at ODTIS version in [Version](../../VERSION).

---

## 4. Security Considerations

Client authentication required (ODTIS-0315). Denial responses MUST NOT leak restricted attributes (ODTIS-0331).

---

*(Expand before IETF Independent submission.)*
