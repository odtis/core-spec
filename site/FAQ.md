---
title: ODTIS FAQ
description: "Complete FAQ: ODTIS vs OIDC, OpenID Federation, eIDAS, profiles, Annex A OpenAPI download, L1/L2/L3 self-certification, Extended modules, and adoption for governments and vendors."
---

# Frequently asked questions

<div class="odtis-hub-hero" markdown="1">

Answers for adopters, national operators, vendors, integrators, auditors, and contributors. Use this page for quick orientation; follow links for normative depth.

<p class="odtis-hub-meta" markdown="1">
<strong>15-minute path:</strong> [Getting started](/site/GETTING-STARTED/) |
<strong>Full adoption:</strong> [Adoption guide](/ADOPTION/) |
<strong>L1/L2/L3 detail:</strong> [Conformance FAQ](/conformance/FAQ/) |
<strong>Contact:</strong> [info@digitaltrustinfrastructure.org](mailto:info@digitaltrustinfrastructure.org)
</p>

</div>

| Topic | Section |
|-------|---------|
| Basics | [General](#general) |
| Comparisons | [ODTIS vs other standards](#odtis-vs-other-standards) |
| Profiles | [Profiles and adoption](#profiles-and-adoption) |
| Spec structure | [Normative specification](#normative-specification) |
| APIs and surfaces | [Technical surfaces](#technical-surfaces-and-apis) |
| Extended | [Extended modules (Annex D)](#extended-modules-annex-d) |
| Downloads | [Artifacts and downloads](#artifacts-and-downloads) |
| Conformance | [Conformance L1, L2, L3](#conformance-l1-l2-l3) |
| Governments | [For governments and operators](#for-governments-and-operators) |
| Vendors | [For vendors and integrators](#for-vendors-and-integrators) |
| IETF / OIDC | [Standards and IETF track](#standards-and-ietf-track) |
| Informative docs | [Book 2, Book 3, and P18](#book-2-book-3-and-p18) |
| Contribute | [Contributing and governance](#contributing-and-governance) |
| Site | [Site, license, and contact](#site-license-and-contact) |

---

## General

### What is ODTIS?

**Open Digital Trust Infrastructure Specification (ODTIS)** is a vendor-neutral, [CC BY 4.0](/site/LICENSE/) open specification for digital trust infrastructure: reusable **Core Identity** (OIDC-based IdP, verification API, consent), **Trust Network** (institutional exchange gateway, catalog, grants), **Operator** governance, **Federation** between operators, security and audit events, and optional **Extended** modules (E-Wallet, E-KYB, E-Signature, and others).

### What problem does ODTIS solve?

ODTIS addresses two systemic gaps that many countries face in parallel:

1. **Problem A - reusable identity:** citizens and businesses repeat KYC/proofing across services instead of reusing a governed digital identity with explicit consent and Levels of Assurance (LoA).
2. **Problem B - institutional exchange:** agencies and enterprises build ad hoc bilateral integrations without uniform trust, mTLS, grants, or auditable metadata routing.

ODTIS normatively specifies both layers so independent vendors can implement interoperable products.

### Is ODTIS the same as VenID?

**No.** **VenID** is a product family and **informative** reference implementation (`ven-identity-core`, `ven-trust-network`). **ODTIS** is the normative specification anyone can implement without VenID code. A second independent implementation is expected before ODTIS `1.0.0` production claims. See [Reference implementations overview](/implementation/).

### Is ODTIS open source?

The **specification text and machine-readable artifacts** are open under [CC BY 4.0](/site/LICENSE/). ODTIS defines **interfaces and behaviour**, not a single open-source product. Implementations may be open or proprietary; conformance is proven by tests and published statements, not by repo license.

### Is this ODTIS 1.0?

**No.** The current release is **`0.9.0-draft`** (external review draft). See [Project status](/site/STATUS/) and [Spec lifecycle stages](/governance/SPEC-STAGES/). Annex A OpenAPI is **frozen** at this version; prose may still change via the RFC process until `1.0.0`.

### What language is authoritative?

**English only** for normative MUST/SHOULD/MAY text. End-user consent screens must be citizen-readable in the **local locale**, but the spec prose stays English. [Language policy](/governance/LANGUAGE/).

### Who maintains ODTIS?

Interim stewards under VenID / FinnectOS governance ([Maintainers](/governance/MAINTAINERS/), [Foundation charter](/governance/FOUNDATION-CHARTER/)). Long-term intent is an ODTIS Foundation after incorporation.

### Is ODTIS only for Venezuela?

**No.** ODTIS is jurisdiction-neutral. VenID and FinnectOS originated the work; the spec is written for any country or operator that adopts the profiles and conformance model.

---

## ODTIS vs other standards

### How is ODTIS different from OpenID Connect?

**OpenID Connect (OIDC)** is an authentication protocol. ODTIS **Core Identity** **binds** OIDC Core, Discovery, and PKCE and adds normative deltas: LoA claims, verification API semantics, consent scope rules, RP admission, audit events, and conformance profiles. Implement OIDC first; use ODTIS for what OIDC does not standardize in a national/operator context. Details: [OIDF positioning](/governance/liaison/OIDF-POSITIONING/).

### Is ODTIS Federation the same as OpenID Federation?

**No.** ODTIS Federation (section 6) is **bilateral, non-transitive** trust between **DTI operators** with explicit federation agreements and regulator export. **OpenID Federation** is a multilateral OIDC/OAuth trust framework (entities, trust anchors, federation metadata). Do not assume interoperability between them without a written mapping.

### How does ODTIS relate to eIDAS 2.0 / EUDI Wallet?

**eIDAS** regulates European digital identity and trust services; **EUDI Wallet** builds on that framework. ODTIS is a **technical interoperability specification** that can align with eIDAS concepts (LoA, qualified signatures) via [Annex C standards mapping](/annexes/C-standards-mapping/) but is **not** an eIDAS compliance checklist. Operators map ODTIS LoA and modules to local law.

### How does ODTIS relate to NIST SP 800-63?

ODTIS section 2 maps **LoA** levels to NIST 800-63-style proofing and authenticator concepts. ODTIS adds operator, gateway, federation, and audit requirements beyond identity proofing alone. See [NIST and X-Road liaison index](/governance/liaison/NIST-XROAD-INDEX/).

### How does ODTIS compare to X-Road?

**X-Road** is a mature national data exchange layer (members, security servers, central components). ODTIS **Trust Network** profile covers similar **institutional exchange** goals (catalog, grants, mTLS gateway, signed audit) with a REST/OpenAPI-first model and explicit ODTIS requirement IDs. X-Road deployments are informative comparators, not drop-in equivalents.

### Is ODTIS a replacement for OAuth 2.0?

**No.** Core Identity **requires** OAuth 2.0 and OIDC where applicable. ODTIS specifies **additional** MUST/SHOULD for operators, verification, consent, trust network, and audit that RFC 6749/OIDC do not cover.

### Does ODTIS require verifiable credentials (VCs)?

**Not for Core Identity.** Extended **E-Wallet** sub-module (Annex D) addresses holder-bound presentations where operators choose OID4VP-style flows. VC-heavy architectures may implement Extended modules; base Core Identity remains OIDC-centric.

### How is ODTIS different from W3C DID / decentralized identity?

ODTIS allows centralized operator-led identity (typical government IdP) **and** optional wallet modules. It does not mandate DIDs. Problem framing is **institutional trust infrastructure**, not a specific ledger or DID method.

---

## Profiles and adoption

### Which ODTIS profile should I implement first?

**Core Identity** for citizen IdP, verification API, consent, and citizen portal. Add **Trust Network** when you operate an exchange gateway between institutions. Add **Operator** for platform duties (SLA, PKI stewardship, regulator API). Add **Federation** only for cross-operator bilateral trust. **Extended** sub-modules are Phase 4 scope. Compare: [Profile comparison](/site/PROFILES/) | path: [Getting started](/site/GETTING-STARTED/).

### What are the six ODTIS conformance profiles?

| Profile | Purpose |
|---------|---------|
| **Reference Architecture** | Layer rules, statement format, extended non-weakening |
| **Core Identity** | OIDC IdP, registry, verification API, consent (sections 2, 3, 5) |
| **Trust Network** | Gateway, catalog, grants, mTLS exchange (section 4) |
| **Federation** | Bilateral operator federation (section 6) |
| **Operator** | Governance, SLA, PKI, regulator surfaces (section 7) |
| **Extended** | Optional Annex D modules (E-Wallet, E-KYB, ...) |

Normative profile docs: [Profiles](/spec/profiles/).

### Do I need all ten specification sections?

Only sections **mandatory for your declared profile(s)** in [Profile definitions](/registry/profiles.yaml). **Section 1** (scope and conformance) applies to everyone. Section 8 (security) and section 9 (audit events) apply broadly when your profile includes those surfaces.

### Can I declare multiple profiles at once?

**Yes**, when your deployment actually implements them. Your [conformance statement](/conformance/templates/conformance-statement.yaml) must list every profile your public claim implies, plus **reference-architecture**. Do not declare Federation or Extended without meeting phase rules ([Section 10](/spec/10-deployment-profiles/SPEC/)).

### What is deployment phase 1-4?

Phases gate which profiles and Extended modules you may **claim** in a conformance statement ([`ODTIS-0532`](/spec/10-deployment-profiles/SPEC/)):

| Phase | Typical conformance scope |
|-------|---------------------------|
| 1 | Core Identity (L1/L2 pilot) |
| 2 | + Trust Network, Federation |
| 3 | + Operator |
| 4 | + Extended (Annex D sub-modules) |

### Can I claim "ODTIS compatible" without tests?

**No meaningful public claim.** Publish a [conformance statement](/conformance/templates/conformance-statement.yaml) backed by L1 at minimum and L2 for behaviour claims. The **"ODTIS Certified"** mark requires L3 third-party attestation per [Trademark policy](/governance/TRADEMARK-POLICY/). Spec section 1.9.

### How long does ODTIS adoption typically take?

Depends on starting point. A team with OIDC experience often reaches **L2 Core Identity staging** in weeks to months; **Trust Network + Operator** adds gateway, PKI, and governance work; **L3 production attestation** is operator-specific. Use [Phased backlog](/implementation/PHASED-BACKLOG/) as an informative RI planning reference, not a normative timeline.

---

## Normative specification

### Where is the normative ODTIS text?

Sections **1-10** under [Index](/spec/INDEX/) with RFC 2119 keywords (MUST/SHOULD/MAY). Start at [Section 1 - Scope and conformance](/spec/01-scope-conformance/SPEC/).

### What are ODTIS requirement IDs (ODTIS-MNNN)?

**149 registry IDs** (e.g. `ODTIS-0301`) in [Requirements registry](/registry/requirements.json), each linked to a spec section and conformance test stub. Browse: [Requirements index](/site/REQUIREMENTS-INDEX/).

### What are the ODTIS annexes?

| Annex | Content |
|-------|---------|
| **A** | Frozen OpenAPI registry (nine API surfaces) |
| **B** | Threat mitigations (informative) |
| **C** | Standards mapping (OIDC, OAuth, NIST, eIDAS, ...) |
| **D** | Extended sub-module catalog |

Index: [Annexes](/annexes/).

### Is Book 2 normative?

**No.** Book 2 (Reference Architecture monograph) is **informative**. It must not contradict ODTIS MUST requirements. Cross-review: [Book 2 cross-review](/governance/BOOK2-CROSS-REVIEW/).

---

## Technical surfaces and APIs

### What is the ODTIS Verification API?

A normative REST surface (Annex A **S3**) for relying parties to request identity verification with consent scope, LoA, and audit. Core Identity profile. Spec: [Section 3](/spec/03-identity-services/SPEC/) | OpenAPI: [Annex A registry](/annexes/A-openapi-registry/).

### What is the ODTIS exchange gateway?

The **Trust Network** ingress/egress for institutional exchange: mTLS, partner validation, grant checks, metadata routing **without** centralizing business payloads (Book 1 D4). Spec: [Section 4](/spec/04-trust-network/SPEC/) | surface **S4** in Annex A.

### What are Levels of Assurance (LoA) in ODTIS?

Canonical values `low`, `medium`, `high`, `national` bound to proofing and RP minimum requirements (section 2). National LoA may require **E-Registry** adapter activation (Extended). Matrix: [Annex C LoA mapping](/annexes/C-standards-mapping/).

### What ODTIS audit events must I emit?

Section 9 defines a catalog with JSON schemas under [Schemas](/registry/events/schemas/). Events include identity lifecycle, verification, consent, grants, exchange, federation, and operator PKI ceremonies. Envelope: `envelope.schema.json`.

### Does ODTIS mandate a specific IdP product?

**No.** Core Identity requires OIDC/OAuth behaviour per profile deltas. Keycloak, custom Java, or commercial IdPs may conform if they pass declared tests.

### Does ODTIS require mTLS everywhere?

**Trust Network** exchange between partners: **yes** for gateway mutual TLS where profile is claimed. Citizen-facing OIDC may use standard TLS; mTLS applies to institutional exchange paths per section 4.

### What is metadata-only exchange (D4)?

Trust network stores **routing metadata and audit envelopes**, not authoritative copies of business payloads. Requirement [`ODTIS-0225`](/spec/04-trust-network/SPEC/). Prevents central data lake anti-patterns.

---

## Extended modules (Annex D)

### What is the ODTIS Extended profile?

Optional sub-modules beyond Core Identity: **E-Wallet**, **E-KYB**, **E-Signature**, **E-Registry**, **E-Inclusion**, **E-Webhook**, and others catalogued in [Annex D](/annexes/D-extended-profiles/). Declared only at **deployment phase 4** unless spec errata says otherwise.

### What is E-Registry in ODTIS?

An adapter pattern for **national registry verification** (hash/query, no civil-authority bypass) with phased activation. Extended module; not a replacement for Core Identity proofing.

### What is E-Wallet vs Core Identity?

Core Identity uses OIDC-centric flows. **E-Wallet** (Extended) adds holder-bound presentation semantics where operators adopt wallet modules. IDs `ODTIS-0340`..`0343` are **Extended**, not Core Identity.

### Can I implement Extended modules before Phase 4?

You may **build** code early, but your **conformance claim** must match [Section 10](/spec/10-deployment-profiles/SPEC/) phase rules. False phase claims fail statement validation and L3 audit.

---

## Artifacts and downloads

### How do I download ODTIS OpenAPI (Annex A)?

Browse [Annex A OpenAPI registry](/annexes/A-openapi-registry/) on this site or download bundles from [Downloads](/site/DOWNLOADS/#machine-readable-artifacts). Verify checksums: [CHECKSUMS.sha256](/annexes/A-openapi-registry/CHECKSUMS.sha256) | [Freeze record](/annexes/A-openapi-registry/FREEZE/).

### Why are YAML and JSON files not in every HTML page?

MkDocs excludes large machine-readable files from HTML rendering. They are copied into the static site root on build and listed in [Downloads](/site/DOWNLOADS/). Clone the [GitHub repository](https://github.com/odtis/core-spec) for full tree development.

### Is Annex A frozen?

**Yes** at `0.9.0-draft`. Normative API bundle versions and checksums are fixed until the next major release process. Editorial OpenAPI fixes follow [Errata policy](/governance/ERRATA/).

### Where is the ODTIS requirements registry?

[Requirements registry](/registry/requirements.json) (149 IDs), [Profile definitions](/registry/profiles.yaml), [Audit event catalog](/registry/events.yaml). Human index: [Requirements index](/site/REQUIREMENTS-INDEX/) | [Glossary](/site/GLOSSARY/).

### How do I cite ODTIS in a paper or procurement document?

[How to cite](/publication/HOW-TO-CITE/) and [Citation metadata (CFF)](/publication/CITATION.cff). Always cite **exact ODTIS version and declared profile(s)**. Zenodo DOI for ODTIS snapshot: pending ([Release checklist](/publication/zenodo/RELEASE-CHECKLIST/)).

### How do I verify a vendor's ODTIS claim?

Request their published **conformance-statement.yaml**, ODTIS version, profiles, level (L2/L3), environment, and evidence (L2 JSON, audit reports). Validate structure with `python3 scripts/validate-conformance-statement.py`. L3 claims require third-party attestation per [Certification program](/governance/CERTIFICATION/).

---

## Conformance L1, L2, L3

### What is ODTIS L1 conformance?

**Repository / lab integrity:** registry links, annex checksums, manifest completeness, validators pass in CI. Run: `./conformance/run.sh`. **Does not** prove live deployment behaviour.

### What is ODTIS L2 conformance?

**Staging behaviour:** automated checks and smoke scripts against your deployment (`ODTIS_TARGET`), plus honest [conformance statement](/conformance/templates/conformance-statement.yaml). Self-certified; suitable for pilots and procurement pre-qualification when disclosed as staging.

### What is ODTIS L3 conformance?

**Third-party production attestation** by an independent auditor. Required for the **ODTIS Certified** trademark. Guides: [Auditor guide](/conformance/certification/auditor-guide/) | [L3 checklist](/conformance/certification/L3-AUDIT-CHECKLIST/).

### How do I self-certify Core Identity (L2)?

1. Read [Self-certification guide](/conformance/certification/self-cert-guide/).
2. Run L1: `./conformance/run.sh`
3. Set `ODTIS_TARGET` to your OIDC realm root URL.
4. Run sandbox checks: `./conformance/sandbox/run-sandbox-check.sh`
5. Publish conformance statement with `level: L2` and evidence.

Full L1/L2/L3 FAQ: [Conformance FAQ](/conformance/FAQ/).

### What is an ODTIS conformance statement?

YAML + human-readable markdown declaring `odtis_version`, `profiles`, `level`, `deployment_phase`, `environment`, `tests`, and `contact`. Template: [Conformance statement template](/conformance/templates/conformance-statement.yaml). Required for honest public claims ([`ODTIS-0008`](/spec/01-scope-conformance/SPEC/)).

### How many ODTIS test procedures exist?

**159** procedures linked to registry MUSTs; **81** have smoke/L2 evidence in the reference lab ([Status](/site/STATUS/)). Pending stubs still obligate implementers to execute against their system before claiming `tests.status: pass`.

### Where are conformance test procedures documented?

Index: [Tests](/conformance/tests/). Individual `test_*.md` files live in the Git repository (browse via GitHub). Not all are rendered as HTML pages.

---

## For governments and operators

### Is ODTIS suitable for a national digital identity program?

**Yes**, when you adopt **Core Identity** + **Operator** (and optionally **Trust Network** for cross-agency exchange). ODTIS is designed for DTI operators running IdP, verification, consent, and institutional trust layers. Map local law (eIDAS, national PKI, data protection) via operator policy.

### Do we need a single national operator?

**Not mandated.** ODTIS supports one operator per country or federated multiple operators (section 6). Architecture choice is deployment-specific; spec requires clear published scope and conformance statements per operator.

### How does ODTIS support regulator oversight?

**Operator** profile includes Regulator API export (Annex A **S8**), SLA metrics, federation agreement export, and audit event access. Federation profile adds bilateral agreement metadata export ([`ODTIS-0406`](/spec/06-federation/SPEC/)).

### Can we procure "ODTIS-compliant" software?

**Yes**, if RFP language references specific **ODTIS version, profiles, level (L2/L3), and required requirement IDs**. Ask vendors for published conformance statements and L2/L3 evidence. Avoid vague "compatible" without tests.

### Does ODTIS define citizen UX for consent?

Section 5 requires **citizen-readable** consent, scope description, and RP admission rules. Exact UI is operator-specific; conformance tests check behaviour and audit, not pixel-perfect design.

---

## For vendors and integrators

### Can I ship a product without VenID code?

**Yes.** ODTIS is intentionally vendor-neutral. Implement from [Index](/spec/INDEX/), [Annex A OpenAPI](/annexes/A-openapi-registry/), and conformance tests. VenID repos are **informative** binding examples: [Component bindings](/site/COMPONENT-BINDINGS/).

### Which APIs should my identity product expose first?

Annex A surfaces **S2** (OIDC/OAuth IdP), **S3** (Verification API), and citizen portal endpoints per Core Identity. Trust Network vendors add **S4** gateway and catalog APIs.

### How do I map ODTIS to my existing OIDC server?

Start with [OIDF positioning](/governance/liaison/OIDF-POSITIONING/) gap list: LoA claims, verification API, consent scope enforcement, RP admission, audit events. Run [OIDC static checks](https://github.com/odtis/core-spec/tree/main/conformance) against your realm.

### Can SaaS multi-tenant operators conform?

**Yes**, if each tenant's published service scope, grants, and audit isolation meet profile MUSTs. Statement should describe tenancy model and which profiles apply per tenant tier.

### Where are known gaps in the VenID reference stack?

[Known gaps](/implementation/gaps/KNOWN-GAPS/) and [Deferred production track](/implementation/gaps/DEFERRED-TRACK/) document RI limits (live mTLS, national TSA, third-party L3). They do **not** waive spec MUSTs for independent vendors.

---

## Standards and IETF track

### Is ODTIS an IETF RFC?

**Not yet.** Scoped pieces (TEP, Verify API, Events, Federation protocol) have Markdown Internet-Drafts under [Drafts](/ietf/drafts/). Roadmap: [IETF roadmap](/governance/IETF-ROADMAP/) | scoping: [IETF scoping](/governance/liaison/IETF-SCOPING/).

### Will ODTIS become an OpenID Foundation specification?

Core Identity **uses** OIDC; ODTIS maintains profile deltas and operator/trust-network layers OIDF does not cover. Liaison positioning: [OIDF positioning](/governance/liaison/OIDF-POSITIONING/).

### How does ODTIS relate to GovStack?

Informative alignment for digital government building blocks: [GovStack positioning](/governance/liaison/GOVSTACK-POSITIONING/).

---

## Book 2, Book 3, and P18

### What is Book 2?

The **Reference Architecture** monograph (informative architecture chapters). Feeds ODTIS but does not override MUST text. Cross-review: [Book 2 cross-review](/governance/BOOK2-CROSS-REVIEW/).

### What is Book 3?

**Implementation Guide** (informative deployment patterns). Useful for engineering; **not** conformance authority.

### What is P18?

Paper 18 (*Standards alignment with ODTIS*) is an **informative** academic bridge. Normative text remains **ODTIS + registry**. Alignment tables: [Annex C](/annexes/C-standards-mapping/).

### Can I implement from Book 3 alone?

**No** for conformance claims. Authority: ODTIS sections 1-10, annexes, declared profile, and tests.

---

## Contributing and governance

### How do I report a bug or clarification?

| Change type | Path |
|-------------|------|
| Clarification / editorial | [Feedback channels](/governance/FEEDBACK/) or [GitHub issues](https://github.com/odtis/core-spec/issues) |
| MUST/SHOULD change | [RFC template](/governance/RFC-TEMPLATE/) |
| Sandbox L2 experience | [L2 report template](/conformance/sandbox/L2-REPORT-TEMPLATE/) |

External review cycle 1: [Review cycle 1](/governance/REVIEW-CYCLE-1/) (check [close checklist](/governance/REVIEW-CYCLE-1-CLOSE/) for status).

### How do I propose a normative RFC?

Copy [RFC template](/governance/RFC-TEMPLATE/), open a discussion issue, and follow [Governance process](/governance/GOVERNANCE/). Normative changes require comment period and steward review.

### Can I join a working group?

See [Working groups](/governance/working-groups/) and [Maintainers](/governance/MAINTAINERS/). [Collaborate](/site/COLLABORATE/) for institutions, hackathons, and research partnerships.

### What license applies to contributions?

Specification text: [CC BY 4.0](/site/LICENSE/). [IPR policy](/governance/IPR-POLICY/) | [Contributor terms](/site/TERMS/).

---

## Site, license, and contact

### Where is the official ODTIS website?

**https://digitaltrustinfrastructure.org** - this site. Source: [Site](https://github.com/odtis/core-spec). Operators with repo access: `./scripts/deploy-ec2.sh` (see `scripts/DEPLOY-EC2-SITE.md` in the repository).

### How do I build the site locally?

```bash
./scripts/build-site.sh
# output: build/odtis-spec-site/
```

Preview: `mkdocs serve -f site/mkdocs.yml` (from `odtis/` after venv setup).

### How do I contact the ODTIS team?

**Email:** [info@digitaltrustinfrastructure.org](mailto:info@digitaltrustinfrastructure.org) | **Contact page:** [Contact](/site/CONTACT/) | **GitHub:** [Issues](https://github.com/odtis/core-spec/issues)

### Is analytics used on digitaltrustinfrastructure.org?

Not by default. If enabled later, [Privacy policy](/site/PRIVACY/) will be updated. Theme preference uses browser local storage only.

### Can I mirror or translate ODTIS?

Mirrors are welcome with attribution (CC BY 4.0). **Translations are not normative** until a steward-approved process exists. [Language policy](/governance/LANGUAGE/).

---

<div class="odtis-hub-footer" markdown="1">

## Still stuck?

| Goal | Document |
|------|----------|
| 15-minute implementer path | [Getting started](/site/GETTING-STARTED/) |
| Full adoption path | [Adoption guide](/ADOPTION/) |
| L1/L2/L3 deep FAQ | [Conformance FAQ](/conformance/FAQ/) |
| Self-certification steps | [Self-certification guide](/conformance/certification/self-cert-guide/) |
| Repository map | [Repository map](/STRUCTURE/) |
| Project status | [Project status](/site/STATUS/) |
| Visual architecture | [Visual guide](/site/VISUAL-GUIDE/) |

</div>
