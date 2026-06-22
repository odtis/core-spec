# IETF scoping - what not to standardize via IETF

**Purpose:** keep ODTIS umbrella out of IETF; extract only protocol-sized slices.

**Project hub:** [Project hub](/project/) | **Roadmap:** [IETF roadmap](../IETF-ROADMAP.md) | **Drafts:** [IETF working drafts overview](../../ietf/README.md)

---

## Do NOT submit to IETF as standalone RFCs

| ODTIS content | Reason | ODTIS home |
|---------------|--------|------------|
| Operator governance (section 7) | Policy / organizational | ODTIS Operator profile |
| Deployment phases (section 10) | Program labels | ODTIS + Book 3 |
| Book 1 policy narrative | Non-technical | Book 1 |
| Full consent privacy prose (section 5) | Overlaps OAuth scopes + GDPR process | ODTIS + jurisdiction bindings |
| OIDC Core behaviour (section 3.3) | Already OIDC / OAuth RFCs | ODTIS profile binding |
| Annex B threat catalog | Informative mapping | ODTIS Annex B |
| Citizen portal UX | Out of scope | Book 2 / Book 3 |

---

## Suitable for IETF / IRTF extraction

| Slice | Format | Notes |
|-------|--------|-------|
| Trust Exchange Protocol message + mTLS | Protocol RFC | From section 4 + `exchange-gateway.openapi.yaml` |
| Verification API HTTP semantics | HTTP API RFC or ART | From section 3.5 + S2 OpenAPI |
| Event envelope JSON | Independent RFC | From section 9 schemas |
| Bilateral federation agreement | IRTF research first | From section 6; distinct from OpenID Federation |

---

## Overlap avoidance checklist (per I-D)

- [ ] Does an OAuth/OIDC RFC already cover this? -> reference, don't duplicate
- [ ] Is there running code in two implementations?
- [ ] Are Security Considerations (RFC 3552) complete?
- [ ] Are IANA registries needed (media types, error codes)?

---

## Related

- [IETF roadmap](../IETF-ROADMAP.md)
- [IETF working drafts overview](../../ietf/README.md)
