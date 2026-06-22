# ODTIS -> IETF / IRTF roadmap

**Status:** planning - no Internet-Draft submitted yet 
**Umbrella spec:** ODTIS (this repository) 
**IETF path:** scoped Internet-Drafts, not the full ODTIS document

**Project hub:** [Project hub](../project/README.md) | **Drafts:** [IETF working drafts overview](../ietf/README.md) | **Scoping:** [IETF scoping](liaison/IETF-SCOPING.md)

---

## Principle

Per [RFC Editor - How to Write an RFC](https://www.rfc-editor.org/authors/rfc-how-to/):

> One Internet-Draft = one acutely scoped problem + running code + no duplication of existing RFCs.

ODTIS sections **3 OIDC** and **5 consent** SHOULD reference OAuth 2.0 / OpenID Connect rather than become standalone IETF RFCs.

---

## Candidate documents

| Priority | Working title | ODTIS source | Stream | Status |
|----------|---------------|--------------|--------|--------|
| 1 | Bilateral Trust Federation for Institutional Networks | section 6 | **IRTF** research -> IETF | Markdown draft in [Drafts](/ietf/drafts/) |
| 2 | ODTIS Verification API HTTP Profile | section 3.5, Annex A S2 | Independent / ART | Markdown draft |
| 3 | Trust Exchange Protocol (TEP) | section 4, gateway OpenAPI | IETF (WG TBD) | Markdown draft |
| 4 | ODTIS Event Envelope | section 9, JSON Schemas | Independent | Markdown draft |

---

## Sequence

```
IRTF/research: federation model (section 6)
↓
Independent I-D: Verification API profile
↓
Interop report (implementation/)
↓
IETF adoption: TEP (section 4) if operator interest
↓
ODTIS 1.0 references RFC numbers for extracted protocols
```

---

## Core Identity

**No standalone IETF RFC** for Core Identity. Publish:

- ODTIS Core Identity profile ([Core Identity profile](/spec/profiles/core-identity-profile/))
- Bindings to OIDC Core, Discovery, PKCE (RFC 7636)
- Delta document for ODTIS-only MUSTs

---

## Related

- [IETF scoping](liaison/IETF-SCOPING.md)
- [IETF working drafts overview](../ietf/README.md)
- [Implementation report template](../ietf/implementation-report/TEMPLATE.md)
