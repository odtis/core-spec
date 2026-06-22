# draft-odtis-federation-00 - Bilateral Trust Federation (working draft)

**Status:** markdown working draft - IRTF research candidate 
**ODTIS source:** section 6

**IETF track:** [Project hub](../README.md) | **RFC FB-002:** [Federation interoperability RFC](/governance/rfc/2026-06-12-federation-interoperability/) | **Project:** [Project hub](/project/)

**Authors:** Manuel Mérida Oliveros

---

## Abstract

This document describes bilateral, non-transitive federation between independent trust network operator instances. It is **not** OpenID Federation (multilateral OIDC/OAuth entity statements).

---

## 1. Problem statement

Operators need controlled cross-network exchange without merged trust anchors or transitive trust through intermediaries.

---

## 2. Federation agreement fields

See ODTIS section 6.2.2: instance IDs, pinned trust material, service whitelist, validity, direction.

---

## 3. Non-transitivity

If A↔B and B↔C exist without A↔C, A MUST NOT reach C via B (ODTIS-6.1.x).

---

## 4. Distinction from OpenID Federation

| | This document | OpenID Federation 1.1 |
|--|---------------|----------------------|
| Scope | Institutional trust networks | OIDC/OAuth parties |
| Topology | Bilateral | Multilateral metadata |

---

*(See also governance RFC FB-002.)*
