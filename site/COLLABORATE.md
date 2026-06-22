---
title: Collaborate - hackathons & institutions
description: Research, implementation, and normative collaboration with ODTIS
---

<div class="odtis-hub-hero" markdown="1">

# Collaborate with ODTIS

Hackathons, pilot labs, and institutional partnerships across **research**, **reference implementation**, and **normative** work - without vendor lock-in.

<p class="odtis-hub-meta" markdown="1">
<strong>Contact:</strong> <a href="mailto:info@odtis.org?subject=ODTIS%20collaboration%20proposal">info@odtis.org</a> | 
<strong>Feedback:</strong> [External review](../governance/FEEDBACK.md) | 
<strong>News:</strong> [Newsletter](NEWSLETTER.md) | 
<strong>Conduct:</strong> [Code of conduct](CODE-OF-CONDUCT.md)
</p>

</div>

!!! info "Open specification, many implementers"
    ODTIS is **vendor-neutral** (CC BY 4.0). Universities, public agencies, integrators, and startups can collaborate on the **same normative baseline** while keeping their own codebases and jurisdiction-specific policy bindings.

---

## Collaboration tracks

```mermaid
flowchart LR
 subgraph research [Research]
 R1[Architecture papers]
 R2[Conformance studies]
 R3[Threat / privacy analysis]
 end
 subgraph impl [Implementation]
 I1[RI extensions]
 I2[L2 sandbox pilots]
 I3[Hackathon prototypes]
 end
 subgraph norm [Normative]
 N1[Clarifications]
 N2[RFC proposals]
 N3[Annex A / tests]
 end
 research --> ODTIS[ODTIS spec + registry]
 impl --> ODTIS
 norm --> ODTIS
```

| Track | You contribute | ODTIS provides | Typical output |
|-------|----------------|----------------|----------------|
| **Research** | Studies, datasets (anonymized), comparative models | Stable IDs, profiles, citation path | Paper, Zenodo deposit, traceability to ODTIS-MNNN |
| **Implementation** | Adapter, gateway, IdP, or operator tooling | Annex A OpenAPI, L1/L2 tests, RI map | L2 report + `conformance-statement.yaml` |
| **Normative** | Review comments, RFC drafts, test procedures | Review cycle, RFC template, registry | Merged spec text, new conformance test |

---

## Who we partner with

<div class="odtis-paths odtis-paths--home" markdown="1">

<div class="odtis-path-card" markdown="1">
<span class="odtis-path-card__role">:material-school-outline:</span>
### Universities & labs
<p class="odtis-path-card__desc" markdown="1">Graduate projects, reproducibility studies, security evaluations, and architecture courses using ODTIS as the normative baseline.</p>
</div>

<div class="odtis-path-card" markdown="1">
<span class="odtis-path-card__role">:material-domain:</span>
### Public institutions
<p class="odtis-path-card__desc" markdown="1">Pilot identity programs, trust-network nodes, regulator sandboxes, and policy binding statements per jurisdiction.</p>
</div>

<div class="odtis-path-card" markdown="1">
<span class="odtis-path-card__role">:material-code-braces:</span>
### Integrators & vendors
<p class="odtis-path-card__desc" markdown="1">Independent Core Identity or Trust Network stacks; L2 self-certification and optional certified-products listing.</p>
</div>

<div class="odtis-path-card" markdown="1">
<span class="odtis-path-card__role">:material-account-group-outline:</span>
### Standards & industry bodies
<p class="odtis-path-card__desc" markdown="1">Liaison on OIDC/OAuth deltas, IETF TEP track, GovStack DPI alignment - see [liaison docs](../governance/liaison/OIDF-POSITIONING.md).</p>
</div>

</div>

---

## Hackathons & build sprints

ODTIS hackathons focus on **interoperable outcomes**, not throwaway demos.

### Suggested themes

| Theme | Duration | Goal |
|-------|----------|------|
| **Core Identity sprint** | 48-72 h | OIDC + PKCE + consent-gated Verification API against a fresh realm |
| **Trust Network sprint** | 48-72 h | Partner node + mTLS + grant + exchange audit event |
| **Conformance lab** | 1 week | Close L2 gaps for one profile; publish statement |
| **Privacy & DSAR** | 48 h | Citizen portal flows + operator DSAR runbook dry-run |
| **Extended module** | 1 week | Annex D sub-module (wallet, webhooks, KYB) with tests |

### What organizers get

| Asset | Location |
|-------|----------|
| Reproducible stack guide | Paper **P12** (VenID reference deployment) |
| L1 structural gate | `./conformance/run.sh` |
| L2 smoke target | `./conformance/sandbox/run-sandbox-check.sh` |
| Visual architecture | [Visual guide](VISUAL-GUIDE.md) |
| Scoring rubric (suggested) | L1 PASS + N live tests + published statement draft |

### Organizer checklist

1. Declare which **ODTIS profile(s)** teams must target.
2. Provide a shared **sandbox URL** (`ODTIS_TARGET`) or local Compose instructions.
3. Require teams to submit **`conformance-statement.yaml`** (even if partial).
4. Log normative gaps as **clarifications** or **RFCs** via [Feedback channels](../governance/FEEDBACK.md).

!!! tip "Co-branded events"
    Email stewards with institution name, dates, expected teams, and profiles in scope. We can link the event from the [Newsletter](NEWSLETTER.md) and provide a short ODTIS intro slot (remote).

---

## Active collaboration windows

| Window | Closes | Focus | How to join |
|--------|--------|-------|-------------|
| **Review cycle 1** | 2026-06-26 | Normative clarity, Annex A, L2 sandbox | [External review cycle 1](../governance/REVIEW-CYCLE-1.md) |
| **Working groups (planned)** | TBD | Connect, Trust Network, Operator, Extended | [Working groups](../governance/working-groups/README.md) |
| **L3 pilot attestation** | Phase 4 | Production operator audit | [L3 certification package](../implementation/L3-CERTIFICATION-PACKAGE.md) |

---

## Proposal template

Send a short note to **info@odtis.org** with:

1. **Institution** and contact
2. **Track** - research | implementation | normative (or combined)
3. **ODTIS profile(s)** in scope
4. **Timeline** and deliverables
5. **IP / publication** intent (open license preferred for normative contributions)

For normative changes, use the formal [RFC template](../governance/RFC-TEMPLATE.md) after initial alignment.

---

<div class="odtis-hub-footer" markdown="1">

## Still stuck?

| Goal | Document |
|------|----------|
| Implementer path | [Getting started](GETTING-STARTED.md) |
| Contributor workflow | [Contributing](../governance/CONTRIBUTING.md) |
| Certification | [Certification program](../governance/CERTIFICATION.md) |
| Stay updated | [Newsletter](NEWSLETTER.md) |

</div>
