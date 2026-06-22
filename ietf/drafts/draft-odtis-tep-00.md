# draft-odtis-tep-00 - Trust Exchange Protocol (working draft)

**Status:** markdown working draft - not an IETF Internet-Draft yet 
**ODTIS source:** section 4, [Exchange gateway (OpenAPI)](/annexes/A-openapi-registry/exchange-gateway.openapi.yaml)

**IETF track:** [Project hub](../README.md) | **Project:** [Project hub](/project/) | **Governance:** [IETF roadmap](/governance/IETF-ROADMAP/)

**Authors:** Manuel Mérida Oliveros

---

## Abstract

This document specifies the Trust Exchange Protocol (TEP): mTLS-authenticated message exchange between institutional trust network gateways, including service grants, routing, and audit correlation identifiers. TEP is extracted from the Open Digital Trust Infrastructure Specification (ODTIS) for potential IETF standardization.

---

## Status of This Memo

This is a **working markdown draft** for ODTIS editors. It is not published on datatracker.ietf.org.

---

## 1. Introduction

ODTIS Layer 2 requires all partner traffic to traverse an exchange gateway (ODTIS-0201). TEP normatively defines the interoperable gateway behaviour independent of the ODTIS umbrella document.

---

## 2. Requirements notation

The key words "MUST", "MUST NOT", "SHOULD", "SHOULD NOT", and "MAY" in this document are to be interpreted as described in BCP 14 (RFC 2119, RFC 8174).

---

## 3. Protocol overview

*(Extract from ODTIS section 4.3-4.5 - to be expanded before xml2rfc conversion.)*

- Partner mutual TLS authentication
- Sender and receiver gateway modes
- Service catalog and grants
- Message signing and correlation IDs

---

## 4. Security Considerations

*(To be expanded: mTLS pinning, grant revocation, non-transitive routing - cross-ref ODTIS Annex B.)*

---

## 5. IANA Considerations

*(Future: media types, error codes shared with ODTIS Annex A `ErrorCode` enum.)*

---

## 6. Normative References

- ODTIS section 4 (informative source)
- RFC 8446 (TLS 1.3)

---

## 7. Informative References

- X-Road architecture
- ODTIS Open Digital Trust Infrastructure Specification
