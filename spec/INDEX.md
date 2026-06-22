---
title: ODTIS specification index
description: Normative index for ODTIS sections 1-10, adoptable profiles, annexes, and machine-readable registry artifacts.
---

# ODTIS - Normative index

<div class="odtis-hub-hero" markdown="1">

Vendor-neutral normative specification for digital trust infrastructure: profiles, MUST/SHOULD requirements, and machine-readable annexes.

<div class="odtis-badges" markdown="1">
<span class="odtis-badge odtis-badge--draft">Version 0.9.0-draft</span>
<span class="odtis-badge odtis-badge--license">review draft - Phase 3.2</span>
</div>

<p class="odtis-hub-meta" markdown="1">
<strong>Adoption:</strong> [Adoption guide](../ADOPTION.md) | 
<strong>Project hub:</strong> [Project hub](../project/README.md) | 
<strong>Conformance:</strong> [Conformance overview](../conformance/README.md)
</p>

</div>

!!! warning "Review draft"
    This is not ODTIS `1.0.0`. See [Spec lifecycle stages](../governance/SPEC-STAGES.md) and [Project status](../site/STATUS.md).

---

## At a glance

| Item | Value |
|------|-------|
| **Normative sections** | 10 (sections 1-10) |
| **Registry requirements** | 149 ODTIS IDs |
| **Conformance profiles** | 6 (Reference Architecture + 5 functional) |
| **Test procedures** | 159 stubs | 81 with smoke evidence |
| **Annex A OpenAPI** | Frozen @ `0.9.0-draft` |

---

## Choose your path

| You are... | Start here | Outcome |
|------------|------------|---------|
| **New implementer** | [Getting started](../site/GETTING-STARTED.md) | Profiles + L1 in 15 minutes |
| **Picking a profile** | [Adoptable profiles](#adoptable-profiles) below | Profile doc + dependencies |
| **Reading normative prose** | [Normative sections](#normative-sections) below | Sections 1-10 |
| **Binding APIs** | [Annexes](#annexes) below | Annex A OpenAPI (frozen) |
| **Verifying a claim** | [Conformance overview](../conformance/README.md) | L1/L2/L3 path |
| **Browsing all IDs** | [Requirements index](../site/REQUIREMENTS-INDEX.md) | 149 requirements |

---

## Adoptable profiles

<div class="odtis-profile-grid" markdown="1">

<div class="odtis-profile-card" markdown="1">

### Reference Architecture

Layer model, claim structure, scope boundaries.

[Profile doc](profiles/reference-architecture-profile.md){ .md-button }

</div>

<div class="odtis-profile-card" markdown="1">

### Core Identity

OIDC IdP, verification API, LoA claims.

[Profile doc](profiles/core-identity-profile.md){ .md-button }

</div>

<div class="odtis-profile-card" markdown="1">

### Trust Network

Partner gateway, exchange semantics.

[Profile doc](profiles/trust-network-profile.md){ .md-button }

</div>

<div class="odtis-profile-card" markdown="1">

### Federation

Cross-operator bilateral trust.

[Profile doc](profiles/federation-profile.md){ .md-button }

</div>

<div class="odtis-profile-card" markdown="1">

### Operator

Platform governance duties.

[Profile doc](profiles/operator-profile.md){ .md-button }

</div>

<div class="odtis-profile-card" markdown="1">

### Extended

Optional modules (E-Wallet, E-Webhook, ...).

[Profile doc](profiles/extended-profile.md){ .md-button }

</div>

</div>

[Profile comparison](../site/PROFILES.md) | normative profile documents listed in the comparison table

## Normative sections

<div class="odtis-section-grid" markdown="1">

<div class="odtis-section-card odtis-section-card--meta" markdown="1">

<span class="odtis-section-card__num">1</span>

### Scope and conformance

<div class="odtis-section-card__meta" markdown="1">
<span>meta</span>
<span>review draft</span>
</div>

Keywords, profiles, conformance levels.

[Read section](01-scope-conformance/SPEC.md){ .md-button }

</div>

<div class="odtis-section-card" markdown="1">

<span class="odtis-section-card__num">2</span>

### Terminology and LoA

<div class="odtis-section-card__meta" markdown="1">
<span>8 IDs</span>
<span>ODTIS-0101..0108</span>
</div>

[Read section](02-terminology-loa/SPEC.md){ .md-button }

</div>

<div class="odtis-section-card" markdown="1">

<span class="odtis-section-card__num">3</span>

### Identity services

<div class="odtis-section-card__meta" markdown="1">
<span>27 IDs</span>
<span>ODTIS-0301..0327</span>
</div>

[Read section](03-identity-services/SPEC.md){ .md-button }

</div>

<div class="odtis-section-card" markdown="1">

<span class="odtis-section-card__num">4</span>

### Trust network

<div class="odtis-section-card__meta" markdown="1">
<span>21 IDs</span>
<span>ODTIS-0201..0221</span>
</div>

[Read section](04-trust-network/SPEC.md){ .md-button }

</div>

<div class="odtis-section-card" markdown="1">

<span class="odtis-section-card__num">5</span>

### Consent and privacy

<div class="odtis-section-card__meta" markdown="1">
<span>16 IDs</span>
<span>ODTIS-0328..0343</span>
</div>

[Read section](05-consent-privacy/SPEC.md){ .md-button }

</div>

<div class="odtis-section-card" markdown="1">

<span class="odtis-section-card__num">6</span>

### Federation

<div class="odtis-section-card__meta" markdown="1">
<span>6 IDs</span>
<span>ODTIS-0401..0406</span>
</div>

[Read section](06-federation/SPEC.md){ .md-button }

</div>

<div class="odtis-section-card" markdown="1">

<span class="odtis-section-card__num">7</span>

### Operator governance

<div class="odtis-section-card__meta" markdown="1">
<span>16 IDs</span>
<span>ODTIS-0501..0516</span>
</div>

[Read section](07-operator-governance/SPEC.md){ .md-button }

</div>

<div class="odtis-section-card" markdown="1">

<span class="odtis-section-card__num">8</span>

### Security

<div class="odtis-section-card__meta" markdown="1">
<span>9 IDs</span>
<span>ODTIS-0517..0525</span>
</div>

[Read section](08-security/SPEC.md){ .md-button }

</div>

<div class="odtis-section-card" markdown="1">

<span class="odtis-section-card__num">9</span>

### Audit and events

<div class="odtis-section-card__meta" markdown="1">
<span>6 IDs</span>
<span>ODTIS-0526..0531</span>
</div>

[Read section](09-audit-events/SPEC.md){ .md-button }

</div>

<div class="odtis-section-card" markdown="1">

<span class="odtis-section-card__num">10</span>

### Deployment

<div class="odtis-section-card__meta" markdown="1">
<span>2 IDs</span>
<span>ODTIS-0532..0533</span>
</div>

[Read section](10-deployment-profiles/SPEC.md){ .md-button }

</div>

</div>

Section review matrix: [Section review matrix](../governance/SECTION-REVIEW.md) | Requirements: [Requirements index](../site/REQUIREMENTS-INDEX.md)

## Annexes

<div class="odtis-annex-grid" markdown="1">

<div class="odtis-annex-card" markdown="1">

### Annex A - OpenAPI

<span class="odtis-badge odtis-badge--frozen">frozen @ 0.9.0-draft</span>

[OpenAPI registry](../annexes/A-openapi-registry/README.md){ .md-button }

</div>

<div class="odtis-annex-card" markdown="1">

### Annex B - Threats

Threat mitigations and red-team scenarios.

[Annex B](../annexes/B-threat-mitigations/README.md){ .md-button }

</div>

<div class="odtis-annex-card" markdown="1">

### Annex C - Standards

Standards mapping and LoA matrix.

[Annex C](../annexes/C-standards-mapping/README.md){ .md-button }

</div>

<div class="odtis-annex-card" markdown="1">

### Annex D - Extended

Extended profile modules.

[Annex D](../annexes/D-extended-profiles/README.md){ .md-button }

</div>

</div>

## Conformance

| Artifact | Path |
|----------|------|
| L1 + L2 suite | [Run script](../conformance/run.sh) (repo) |
| Self-certification | [Self-certification guide](../conformance/certification/self-cert-guide.md) |
| Certification program | [Certification program](../governance/CERTIFICATION.md) |
| Machine-readable manifest | `conformance/manifest.yaml` (repo only) |

---

## Related tabs

| Tab | When to use |
|-----|-------------|
| [Annexes](../annexes/README.md) | OpenAPI, threats, standards, Extended |
| [Conformance](../conformance/README.md) | L1/L2/L3 verification |
| [Project](../project/README.md) | Status, governance, downloads |

---

<div class="odtis-hub-footer" markdown="1">

## Still stuck?

| Goal | Document |
|------|----------|
| Domain map (ODTIS-0000..0006) | [Domain map](../site/DOMAINS.md) |
| Glossary | [Glossary](../site/GLOSSARY.md) |
| Section review matrix | [Section review matrix](../governance/SECTION-REVIEW.md) |
| Build plan / phases | [Build plan](../PLAN-PHASES.md) |

</div>
