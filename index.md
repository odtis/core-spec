---
title: Open Digital Trust Infrastructure Specification
hide:
 - navigation
 - toc
description: "ODTIS: vendor-neutral open standard for digital identity, trust networks, and institutional exchange. 149 normative requirements, 6 conformance profiles, frozen OpenAPI Annex A, L1/L2/L3 verification."
---

<div class="odtis-home odtis-landing" markdown="1">

<div class="odtis-landing-hero" markdown="1">

<div class="odtis-landing-hero__main" markdown="1">

# Open specification for digital trust infrastructure

<p class="odtis-landing-hero__lead">
Adopt, implement, and certify interoperable identity and institutional exchange:
<strong>vendor-neutral</strong>, <strong>machine-readable</strong>, and <strong>testable at L1 / L2 / L3</strong>.
</p>

<div class="odtis-landing-hero__cta" markdown="1">
[Read the specification](/spec/INDEX/){ .md-button .md-button--primary .odtis-landing-cta--primary }
[Getting started (15 min)](/site/GETTING-STARTED/){ .md-button .odtis-landing-cta--secondary }
</div>

<p class="odtis-landing-hero__links" markdown="1">
[Vision & mission](/site/ABOUT/) |
[Visual guide](/site/VISUAL-GUIDE/) |
[Collaborate](/site/COLLABORATE/) |
[Newsletter](/site/NEWSLETTER/) |
[Adoption guide](/ADOPTION/) |
[Conformance overview](/conformance/) |
[Downloads and artifacts](/site/DOWNLOADS/)
</p>

</div>

<div class="odtis-landing-pillars" markdown="1">

<div class="odtis-landing-pillar" markdown="1">
<span class="odtis-landing-pillar__icon">:material-account-key-outline:</span>
<div class="odtis-landing-pillar__body" markdown="1">
<strong>Layer 1</strong>
<span class="odtis-landing-pillar__desc">OIDC + PKCE, Verification API, consent</span>
</div>
</div>

<div class="odtis-landing-pillar" markdown="1">
<span class="odtis-landing-pillar__icon">:material-swap-horizontal:</span>
<div class="odtis-landing-pillar__body" markdown="1">
<strong>Layer 2</strong>
<span class="odtis-landing-pillar__desc">mTLS gateway, catalog, signed audit</span>
</div>
</div>

<div class="odtis-landing-pillar" markdown="1">
<span class="odtis-landing-pillar__icon">:material-clipboard-check-outline:</span>
<div class="odtis-landing-pillar__body" markdown="1">
<strong>Conformance</strong>
<span class="odtis-landing-pillar__desc">6 profiles, Annex A, L1/L2/L3</span>
</div>
</div>

</div>

</div>

<div class="odtis-landing-trust" markdown="1">

<div class="odtis-stat" markdown="1">
<strong>149</strong>
<span>Requirement IDs</span>
</div>
<div class="odtis-stat" markdown="1">
<strong>6</strong>
<span>Profiles</span>
</div>
<div class="odtis-stat" markdown="1">
<strong>159</strong>
<span>Test procedures</span>
</div>
<div class="odtis-stat odtis-stat--meter" markdown="1">
<!-- GENERATED:coverage-hero:START -->
<strong>100</strong>
<span>Smoke-evidenced</span>
<div class="odtis-meter" role="presentation"><div class="odtis-meter__fill" style="width:63%"></div></div>
<small class="odtis-stat__hint">62.9% of 159 procedures</small>
<!-- GENERATED:coverage-hero:END -->
</div>
<div class="odtis-stat" markdown="1">
<strong>10</strong>
<span>Normative sections</span>
</div>
<div class="odtis-stat" markdown="1">
<strong>7</strong>
<span>Domains</span>
</div>

</div>

<div class="odtis-landing-section odtis-landing-section--panel" markdown="1">

<div class="odtis-landing-section__head odtis-landing-section__head--center" markdown="1">
<span class="odtis-section-head__eyebrow">About the project</span>
## Vision & mission
<p class="odtis-section-head__lead">A vendor-neutral open standard for verified identity and governed institutional exchange - testable, not self-asserted.</p>
</div>

<div class="odtis-landing-vm" markdown="1">

<div class="odtis-landing-vm-card" markdown="1">
<span class="odtis-landing-vm-card__icon">:material-telescope:</span>
### Vision
<p class="odtis-landing-vm-card__lead">Verified digital identity and governed institutional exchange across borders, vendors, and sectors - without locking citizens, governments, or businesses into a single proprietary stack.</p>
<ul class="odtis-landing-vm-list">
<li><strong>Interoperable</strong> - shared conformance profiles and exchange semantics</li>
<li><strong>Accountable</strong> - PKI, consent, audit, and regulator-visible governance</li>
<li><strong>Adoptable</strong> - national law stays in adopter policy bindings</li>
<li><strong>Verifiable</strong> - L1 / L2 / L3 evidence, not marketing labels</li>
</ul>
</div>

<div class="odtis-landing-vm-card" markdown="1">
<span class="odtis-landing-vm-card__icon">:material-bullseye-arrow:</span>
### Mission
<p class="odtis-landing-vm-card__lead">Define normative MUST/SHOULD/MAY requirements so vendors, operators, integrators, and auditors share one testable contract for digital trust infrastructure.</p>
<ol class="odtis-landing-vm-list odtis-landing-vm-list--ordered">
<li><strong>Standardize</strong> Layer 1 identity and Layer 2 trust networks</li>
<li><strong>Publish</strong> machine-readable registry, OpenAPI, and test procedures</li>
<li><strong>Enable</strong> phased adoption through conformance profiles</li>
<li><strong>Separate</strong> normative spec from reference code and national editions</li>
</ol>
</div>

</div>

<p class="odtis-home-links" markdown="1">
[Full vision, mission, and ecosystem diagram](/site/ABOUT/) |
[Visual architecture guide](/site/VISUAL-GUIDE/)
</p>

</div>

<div class="odtis-landing-section" markdown="1">

<div class="odtis-landing-section__head odtis-landing-section__head--center" markdown="1">
<span class="odtis-section-head__eyebrow">Why ODTIS</span>
## Built for independent adoption
<p class="odtis-section-head__lead">Normative MUST/SHOULD/MAY per BCP 14, without binding to VenID product code.</p>
</div>

<div class="odtis-landing-features" markdown="1">

<div class="odtis-landing-feature" markdown="1">
<span class="odtis-landing-feature__icon">:material-earth:</span>
### Vendor-neutral
<p class="odtis-landing-feature__desc">Declare conformance profiles and interoperate across operators, vendors, and jurisdictions without product lock-in.</p>
</div>

<div class="odtis-landing-feature" markdown="1">
<span class="odtis-landing-feature__icon">:material-code-json:</span>
### Machine-readable
<p class="odtis-landing-feature__desc">Frozen Annex A OpenAPI, a requirements registry, and profile manifests for traceable implementation and audit.</p>
</div>

<div class="odtis-landing-feature" markdown="1">
<span class="odtis-landing-feature__icon">:material-shield-check-outline:</span>
### Testable claims
<p class="odtis-landing-feature__desc">L1 structural validation, L2 sandbox smoke, and L3 third-party audit. Not self-asserted labels.</p>
</div>

</div>

</div>

<div class="odtis-landing-section odtis-landing-section--panel" markdown="1">

<div class="odtis-landing-section__head" markdown="1">
<span class="odtis-section-head__eyebrow">Start here</span>
## Choose your path
</div>

<div class="odtis-paths odtis-paths--home" markdown="1">

<div class="odtis-path-card" markdown="1">
<span class="odtis-path-card__role">:material-briefcase-outline:</span>
### Policy / executive
<p class="odtis-path-card__desc" markdown="1">Vision, two-layer model, and what ODTIS enables for governments and ecosystems - without implementation depth.</p>
[About the project](/site/ABOUT/){ .md-button }
</div>

<div class="odtis-path-card" markdown="1">
<span class="odtis-path-card__role">:material-domain:</span>
### Independent vendor
<p class="odtis-path-card__desc" markdown="1">Compare six profiles, download registries and manifests, and plan adoption without reference implementation code.</p>
[Adoption guide](/ADOPTION/){ .md-button }
</div>

<div class="odtis-path-card" markdown="1">
<span class="odtis-path-card__role">:material-bank-outline:</span>
### National operator
<p class="odtis-path-card__desc" markdown="1">Run Layer 1 and Layer 2 as platform operator: PKI, deployment phases, regulator export, and Operator profile duties.</p>
[Operator profile](/spec/profiles/operator-profile/){ .md-button }
</div>

<div class="odtis-path-card" markdown="1">
<span class="odtis-path-card__role">:material-wrench-outline:</span>
### Implementer
<p class="odtis-path-card__desc" markdown="1">Select profiles for your stack, bind [Annex A](/annexes/A-openapi-registry/), and run L1 structural checks before L2 sandbox smoke.</p>
[Getting started](/site/GETTING-STARTED/){ .md-button }
</div>

<div class="odtis-path-card" markdown="1">
<span class="odtis-path-card__role">:material-certificate-outline:</span>
### Auditor / test lab
<p class="odtis-path-card__desc" markdown="1">Review the L3 program, audit checklist, and evidence expectations for production conformance claims.</p>
[Certification program](/governance/CERTIFICATION/){ .md-button }
</div>

<div class="odtis-path-card" markdown="1">
<span class="odtis-path-card__role">:material-comment-eye-outline:</span>
### External reviewer
<p class="odtis-path-card__desc" markdown="1">Review cycle 1 is open until 2026-06-26 - submit clarifications, RFCs, and L2 sandbox reports.</p>
[External review cycle 1](/governance/REVIEW-CYCLE-1/){ .md-button }
</div>

<div class="odtis-path-card" markdown="1">
<span class="odtis-path-card__role">:material-handshake-outline:</span>
### Institution / collaborator
<p class="odtis-path-card__desc" markdown="1">Hackathons, pilot labs, and partnerships across research, implementation, and normative tracks.</p>
[Collaborate](/site/COLLABORATE/){ .md-button }
</div>

<div class="odtis-path-card" markdown="1">
<span class="odtis-path-card__role">:material-account-group-outline:</span>
### Contributor
<p class="odtis-path-card__desc" markdown="1">Open PRs, fix spec text, extend conformance tests, and follow governance and lifecycle stages.</p>
[Contributing](/governance/CONTRIBUTING/){ .md-button }
</div>

<div class="odtis-path-card" markdown="1">
<span class="odtis-path-card__role">:material-file-code-outline:</span>
### Standards body
<p class="odtis-path-card__desc" markdown="1">Track IETF working drafts, liaison positioning, and normative deltas relative to OIDC and OAuth.</p>
[IETF working drafts](/ietf/){ .md-button }
</div>

<div class="odtis-path-card" markdown="1">
<span class="odtis-path-card__role">:material-school-outline:</span>
### Researcher
<p class="odtis-path-card__desc" markdown="1">Cite ODTIS formally and trace requirement IDs back to the P18 evidence base.</p>
[How to cite](/publication/HOW-TO-CITE/){ .md-button }
</div>

</div>

</div>

<div class="odtis-landing-section" markdown="1">

<div class="odtis-landing-section__head odtis-landing-section__head--center" markdown="1">
<span class="odtis-section-head__eyebrow">How it works</span>
## Adopt in four steps
</div>

<div class="odtis-steps odtis-steps--landing" markdown="1">

<div class="odtis-step" markdown="1">
<span class="odtis-step__num">1</span>
<h3>Declare profiles</h3>
<p>Core Identity, Trust Network, Federation, Operator, or Extended.</p>
</div>

<div class="odtis-step" markdown="1">
<span class="odtis-step__num">2</span>
<h3>Bind artifacts</h3>
<p markdown="1">[Annex A OpenAPI](/annexes/A-openapi-registry/) + [requirements registry](/registry/).</p>
</div>

<div class="odtis-step" markdown="1">
<span class="odtis-step__num">3</span>
<h3>Verify</h3>
<p>L1 structural, then L2 sandbox, then L3 audit for production.</p>
</div>

<div class="odtis-step" markdown="1">
<span class="odtis-step__num">4</span>
<h3>Publish claim</h3>
<p markdown="1">[Conformance statement template](/conformance/certification/self-cert-guide/) with profile + level.</p>
</div>

</div>

</div>

<div class="odtis-landing-section odtis-landing-section--panel" markdown="1">

<div class="odtis-landing-section__head" markdown="1">
<span class="odtis-section-head__eyebrow">Architecture</span>
## Two-layer model
<p class="odtis-section-head__lead">Stop re-verifying people in every app, and stop wiring institutions one-by-one. ODTIS separates <strong>who someone is</strong> from <strong>who may exchange what</strong> - with standards underneath both.</p>
</div>

<div class="odtis-home-split" markdown="1">

<div class="odtis-home-split__visual odtis-diagram-panel odtis-diagram-panel--business" markdown="1">

```mermaid
flowchart TB
 subgraph actors [Who benefits]
 CIT[Citizens]
 APP[Apps and portals]
 ORG[Institutions and partners]
 end

 subgraph L1 [Layer 1 - Core Identity]
 L1B[One verified identity, reusable across services]
 L1T[Standard login APIs, consent, assurance levels]
 end

 subgraph L2 [Layer 2 - Trust Network]
 L2B[Governed data exchange between institutions]
 L2T[Explicit permissions, catalog, signed audit]
 end

 CIT --> L1B
 APP --> L1B
 ORG --> L2B
 L1B --> L1T
 L2B --> L2T
 L1T --> L2T
```

<p class="odtis-diagram-caption">One identity plane for people and apps. One trust plane for institutional exchange. Both are testable under ODTIS conformance profiles.</p>

</div>

<div class="odtis-landing-phases" markdown="1">

<div class="odtis-landing-phase">
<span class="odtis-landing-phase__num">1</span>
<div class="odtis-landing-phase__body">
<strong>Core Identity</strong>
<span>Citizens verify once; apps receive only consented attributes</span>
<small class="odtis-landing-phase__tech">OIDC login, verification API, LoA</small>
</div>
</div>

<div class="odtis-landing-phase">
<span class="odtis-landing-phase__num">2</span>
<div class="odtis-landing-phase__body">
<strong>Trust Network</strong>
<span>Institutions exchange data with explicit permission and logs</span>
<small class="odtis-landing-phase__tech">mTLS gateway, catalog, grants, audit</small>
</div>
</div>

<div class="odtis-landing-phase">
<span class="odtis-landing-phase__num">2+</span>
<div class="odtis-landing-phase__body">
<strong>Federation</strong>
<span>Operators trust each other bilaterally across borders</span>
<small class="odtis-landing-phase__tech">Non-transitive operator agreements</small>
</div>
</div>

<div class="odtis-landing-phase">
<span class="odtis-landing-phase__num">3</span>
<div class="odtis-landing-phase__body">
<strong>Operator</strong>
<span>PKI, deployment phases, and regulator-visible governance</span>
<small class="odtis-landing-phase__tech">Ceremonies, security baseline, export APIs</small>
</div>
</div>

</div>

</div>

<p class="odtis-home-links" markdown="1">
[Engineer diagrams and request paths](/site/VISUAL-GUIDE/) |
[Vision and ecosystem view](/site/ABOUT/) |
[Profile comparison](/site/PROFILES/) |
[Full specification](/spec/INDEX/)
</p>

</div>

<div class="odtis-landing-section odtis-landing-section--panel" markdown="1">

<div class="odtis-landing-section__head" markdown="1">
<span class="odtis-section-head__eyebrow">Documentation</span>
## Explore the specification
<p class="odtis-section-head__lead">Start with project context, then normative text, machine-readable annexes, and conformance verification.</p>
</div>

<div class="odtis-grid odtis-home-tabs" markdown="1">

<div class="odtis-card odtis-card--project" markdown="1">
<span class="odtis-card__icon">:material-folder-information-outline:</span>
### Project
<p class="odtis-card__desc">Adoption guide, status, governance, reference implementation notes, and contribution workflows.</p>
[Project hub](/project/){ .md-button }
</div>

<div class="odtis-card odtis-card--spec" markdown="1">
<span class="odtis-card__icon">:material-book-open-page-variant-outline:</span>
### Specification
<p class="odtis-card__desc">Ten normative sections, six profile packs, and the requirements registry with stable ODTIS-MNNN IDs.</p>
[Specification index](/spec/INDEX/){ .md-button }
</div>

<div class="odtis-card odtis-card--annex" markdown="1">
<span class="odtis-card__icon">:material-file-document-multiple-outline:</span>
### Annexes
<p class="odtis-card__desc">Frozen OpenAPI (Annex A), threat models, standards crosswalk, and Extended sub-modules (Annex D).</p>
[Annexes overview](/annexes/){ .md-button }
</div>

<div class="odtis-card odtis-card--conf" markdown="1">
<span class="odtis-card__icon">:material-shield-check-outline:</span>
### Conformance
<p class="odtis-card__desc">L1/L2/L3 levels, 159 test procedures, and smoke evidence for independent verification.</p>
[Conformance overview](/conformance/){ .md-button }
</div>

</div>

</div>

<div class="odtis-landing-cta" markdown="1">

## Ready to adopt ODTIS?

<p class="odtis-landing-cta__lead">Pick a profile, bind Annex A, run L1, then publish your conformance claim.</p>

<div class="odtis-landing-cta__actions" markdown="1">
[Adoption guide](/ADOPTION/){ .md-button .md-button--primary }
[Conformance overview](/conformance/){ .md-button }
</div>

</div>

</div>
