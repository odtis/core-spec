# ODTIS Internet-Draft track

<div class="odtis-hub-hero" markdown="1">

Scoped protocol pieces may become Internet-Drafts while ODTIS retains profile binding, deployment phases, and operator governance in-repo.

<p class="odtis-hub-meta" markdown="1">
<strong>Status:</strong> pre-submission working drafts | 
<strong>Umbrella spec:</strong> [ODTIS](../spec/INDEX.md) (not submitted as a whole) | 
<strong>Project hub:</strong> [Project hub](../project/README.md)
</p>

</div>

!!! note "Normative boundary"
    ODTIS sections 1-10 remain authoritative for profiles and conformance. IETF drafts extract wire formats only.

---

## At a glance

| Item | Status |
|------|--------|
| **Working drafts** | 4 markdown drafts (`-00`) |
| **Governance** | [IETF roadmap](../governance/IETF-ROADMAP.md) |
| **Scoping rules** | [IETF scoping](../governance/liaison/IETF-SCOPING.md) |
| **Implementation reports** | Template published |
| **Datatracker submission** | Not yet (xml2rfc conversion pending) |

---

## Choose your path

| You want to... | Start here |
|----------------|------------|
| Read TEP (trust exchange) | [TEP draft](drafts/draft-odtis-tep-00.md) |
| Read Verify API HTTP profile | [Verify API draft](drafts/draft-odtis-verify-api-00.md) |
| Read event envelope schema | [Events draft](drafts/draft-odtis-events-00.md) |
| Read bilateral federation protocol | [Federation protocol draft](drafts/draft-odtis-federation-00.md) |
| File an implementation report | [Implementation report template](implementation-report/TEMPLATE.md) |
| Understand what stays in ODTIS | [IETF scoping](../governance/liaison/IETF-SCOPING.md) |

---

## Why a separate IETF track?

| ODTIS keeps in-repo | May extract to IETF |
|---------------------|---------------------|
| Conformance profiles and levels | Wire protocols (TEP) |
| Deployment phases 1-4 | HTTP message formats |
| Operator PKI and audit rules | Event envelope schema |
| OIDC **profile binding** | Bilateral federation protocol |

Core Identity **OIDC behaviour** stays on OIDC/OAuth RFCs - ODTIS profiles and binds them ([OIDF positioning](../governance/liaison/OIDF-POSITIONING.md)).

---

## Working drafts

| Draft | File | Target stream | ODTIS source |
|-------|------|---------------|--------------|
| Trust Exchange Protocol (TEP) | [TEP draft](drafts/draft-odtis-tep-00.md) | IETF | Section 4, gateway OpenAPI |
| Verification API HTTP Profile | [Verify API draft](drafts/draft-odtis-verify-api-00.md) | Independent | Section 3.5, Annex A S2 |
| Event Envelope | [Events draft](drafts/draft-odtis-events-00.md) | Independent | Section 9, JSON Schemas |
| Bilateral Federation | [Federation protocol draft](drafts/draft-odtis-federation-00.md) | IRTF -> IETF | Section 6 |

Future: convert to xml2rfc v3 (`.xml`) before datatracker submission.

---

## Implementation reports

IETF progression requires implementation reports from independent deployers.

| Resource | Purpose |
|----------|---------|
| [Implementation report template](implementation-report/TEMPLATE.md) | Report template |
| [L2 report template](../conformance/sandbox/L2-REPORT-TEMPLATE.md) | Sandbox L2 evidence (ODTIS conformance) |

---

## Related tabs

| Tab | When to use |
|-----|-------------|
| [Specification](../spec/INDEX.md) | Normative source sections |
| [Governance](../governance/README.md) | IETF roadmap, liaison |
| [Project](../project/README.md) | Status, publication |

---

<div class="odtis-hub-footer" markdown="1">

## Still stuck?

| Goal | Document |
|------|----------|
| Adoption guide (IETF relationship) | [Adoption guide](../ADOPTION.md) |
| FB-002 federation depth RFC | [Federation interoperability RFC](../governance/rfc/2026-06-12-federation-interoperability.md) |
| Deferred TEP production track | [Deferred production track](../implementation/gaps/DEFERRED-TRACK.md) |

</div>
