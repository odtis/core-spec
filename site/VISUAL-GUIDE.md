---
title: Visual architecture guide
description: Diagrams for implementers, auditors, and operators
---

<div class="odtis-hub-hero" markdown="1">

# Visual architecture guide

**One page, engineer-first:** where ODTIS lives in repos, how the two layers talk, which profile to declare, and how to reach L1/L2/L3  - without reading 11 spec sections first.

<p class="odtis-hub-meta" markdown="1">
<strong>15-minute path:</strong> [Getting started](GETTING-STARTED.md) |
<strong>Normative text:</strong> [Specification](../spec/INDEX.md) |
<strong>RI mapping:</strong> [Component bindings](COMPONENT-BINDINGS.md) |
<strong>Academic figures:</strong> Paper P01 (PlantUML) on [digitaltrustinfrastructure.org](https://digitaltrustinfrastructure.org)
</p>

</div>

!!! tip "How to read these diagrams"
    Boxes name **logical ODTIS surfaces** (Annex A OpenAPI bundles). Ports and repo names in grey callouts are **informative** VenID bindings  - you can implement ODTIS without VenID. For mission and ecosystem narrative see [About ODTIS](ABOUT.md).

---

## Developer compass  - start here

Pick your lane. Each path links to the doc that answers the next question.

```mermaid
flowchart TB
  START([I want to...])

  START --> P1[Build an IdP / verification API]
  START --> P2[Integrate as Relying Party]
  START --> P3[Connect as institutional partner]
  START --> P4[Run or audit an operator]
  START --> P5[Fork the reference stack]

  P1 --> D1[Profile: Core Identity]
  P2 --> D2[OIDC client + verification-api scopes]
  P3 --> D3[Profile: + Trust Network mTLS]
  P4 --> D4[Profiles: + Operator Federation]
  P5 --> D5[core-impl + odtis-devkit]

  D1 --> L1[GETTING-STARTED.md]
  D2 --> L2[Annex A verification-api + OIDF liaison]
  D3 --> L3[exchange-gateway + partner SDK]
  D4 --> L4[ADOPTION.md + conformance statement]
  D5 --> L5[Component bindings + RI-MAP.yaml]

  style START fill:#e8eaf6,stroke:#3949ab
  style L1 fill:#f5f5f5,stroke:#9e9e9e
  style L2 fill:#f5f5f5,stroke:#9e9e9e
  style L3 fill:#f5f5f5,stroke:#9e9e9e
  style L4 fill:#f5f5f5,stroke:#9e9e9e
  style L5 fill:#f5f5f5,stroke:#9e9e9e
```

| If you are... | Read first | Then run |
|---------------|------------|----------|
| **Vendor / greenfield** | [Getting started](GETTING-STARTED.md) → [Profile comparison](PROFILES.md) | `./conformance/run.sh` (L1) |
| **RP / app team** | [OIDF positioning](../governance/liaison/OIDF-POSITIONING.md) + [verification-api OpenAPI](../annexes/A-openapi-registry/verification-api.openapi.yaml) | Sandbox OIDC against your IdP |
| **Partner backend** | [Trust Network spec](../spec/04-trust-network/SPEC.md) section 4.4 | mTLS smoke via `exchange-client` (RI) |
| **Operator / regulator** | [Operator profile](../spec/profiles/operator-profile.md) + [Section 10](../spec/10-deployment-profiles/SPEC.md) | L2 statement + [self-cert guide](../conformance/certification/self-cert-guide.md) |
| **Contributor** | [Component bindings](COMPONENT-BINDINGS.md) | Pick a component YAML + linked test |

---

## Ecosystem map  - spec, RI, and product layer

ODTIS is **normative in `core-spec`**; everything else is optional acceleration. You never need VenID to claim conformance.

```mermaid
flowchart TB
  subgraph normative [Normative  - odtis/core-spec]
    SPEC[11 spec sections + 7 profiles]
    REG[registry/ 204 requirement IDs]
    ANN[Annexes A-E OpenAPI events threats]
    CONF[conformance/ L1-L3 tests]
    SITE[odtis.org site]
  end

  subgraph ri [Reference implementation  - informative]
  IMPL[core-impl VenID]
  IC[ven-identity-core Layer 1]
  TN[ven-trust-network Layer 2]
  CS[ven-cloud-stack operator base]
  end

  subgraph accel [Adoption accelerators  - product layer]
    DK[odtis-devkit sandbox compose]
    TOOLS[odtis-tools CLI validators]
    KC[odtis-keycloak overlay]
    GW[odtis-gateway-plugins]
    REL[odtis-reliance-sdk Capa B]
    POL[odtis-policy-bindings legal templates]
  end

  subgraph external [External informative]
    B2[Book 2 architecture DTI Research]
    B3[Book 3 implementation patterns]
    IETF[IETF drafts TEP verify-api events]
  end

  SPEC --> REG
  SPEC --> ANN
  SPEC --> CONF
  SPEC --> SITE
  CONF -. validates .-> IMPL
  IMPL --> IC
  IMPL --> TN
  IMPL --> CS
  DK --> IMPL
  TOOLS --> CONF
  KC --> IC
  GW --> TN
  REL --> SPEC
  POL -. jurisdiction packs .-> SPEC
  B2 -. must not contradict .-> SPEC
  B3 -. deployment hints .-> SPEC
  IETF -. wire formats .-> ANN

  style normative fill:#e8eaf6,stroke:#3949ab
  style ri fill:#e0f2f1,stroke:#00695c
  style accel fill:#fff3e0,stroke:#ef6c00
```

**Rule of thumb:** implement against **Annex A + registry**; use RI only as a worked example. Product repos shorten time-to-first-green-test; they do not replace the spec.

---

## Two-layer stack  - trust boundaries

Two public edges, two threat models. Layer 1 = HTTPS + OIDC/JWT. Layer 2 = mTLS + partner grants only.

```mermaid
flowchart TB
 subgraph actors [Actors]
 C[Citizen / subject]
 RP[Relying Party app]
 P[Partner institution]
 OP[Operator / regulator]
 end

 subgraph edge [Public edge]
 GW["API Gateway / TLS<br/><i>RI :8080 api-gateway</i>"]
 end

 subgraph L1 [Layer 1  - Core Identity profile]
 KC["OIDC IdP<br/><i>RI Keycloak :8180</i>"]
 CA[citizen-api]
 VA["verification-api<br/><i>RI :8092</i>"]
 AA[admin-api / regulator-api]
 IC[(identity-core)]
 CS[(consent-service)]
 VE[verification-engine]
 end

 subgraph L2 [Layer 2  - Trust Network profile]
 XGW["exchange-gateway / mTLS<br/><i>RI :9080</i>"]
 TR[(trust-registry / catalog)]
 TS[trust-service / grants]
 AUD[(audit-service)]
 end

 C -->|browser OAuth| GW
 RP -->|server OAuth + verify| GW
 P -->|client cert only| XGW
 OP --> GW

 GW --> KC
 GW --> CA
 GW --> VA
 GW --> AA

 CA --> IC
 CA --> CS
 VA --> IC
 VA --> CS
 VA --> KC
 VE --> IC

 XGW --> TS
 XGW --> TR
 XGW --> VA
 XGW --> AUD
 IC -.-> AUD
 CS -.-> AUD
```

| Boundary | Protocol | Who | Fail-closed gate |
|----------|----------|-----|------------------|
| **L1 edge** | HTTPS, OIDC, JWT | Citizens, RPs, operators | Consent + LoA before attribute release ([ODTIS-0331](../spec/05-consent-privacy/SPEC.md)) |
| **L2 edge** | mTLS + `service_id` + purpose | Partner backends only | Grant + cert validation ([ODTIS-0224](../spec/04-trust-network/SPEC.md), [ODTIS-0535](../spec/08-security/SPEC.md)) |

Partners **never** call `citizen-api` or microservices directly  - only `exchange-gateway`.

---

## Request paths  - three flows that matter

=== "Citizen login (OIDC)"

    Standard OAuth 2.0 + PKCE. ODTIS adds consent audit and LoA claims on top of OIDC.

    ```mermaid
    sequenceDiagram
    autonumber
    participant U as Citizen browser
    participant RP as Relying Party
    participant GW as API Gateway
    participant KC as OIDC IdP
    participant CS as consent-service

    U->>RP: Open app
    RP->>GW: Authorization request + PKCE
    GW->>KC: /authorize
    KC->>U: Login + consent prompt
    U->>KC: Approve scopes
    KC->>RP: Authorization code
    RP->>KC: Token exchange
    KC-->>RP: ID token + access token
    Note over CS: consent.granted audited
    ```

    **Implementer notes:** register RP as OIDC client; request only scopes you can justify under consent policy. See [OIDF positioning](../governance/liaison/OIDF-POSITIONING.md).

=== "RP verification (server)"

    Server-to-server attribute release. **No consent → no attributes** (403, not partial leak).

    ```mermaid
    sequenceDiagram
    autonumber
    participant RP as Relying Party
    participant VA as verification-api
    participant CS as consent-service
    participant IC as identity-core

    RP->>VA: GET /users/:id/verification + scopes
    VA->>CS: Active consent for client_id?
    alt consent denied
    VA-->>RP: 403 consent_denied (no attributes)
    else consent OK + LoA sufficient
    VA->>IC: Load subject + LoA
    VA-->>RP: attributes + assurance_level
    end
    ```

    **OpenAPI:** [verification-api](../annexes/A-openapi-registry/verification-api.openapi.yaml) · **Tests:** `test_verification_consent_scope`, `test_loa_claim`

=== "Partner exchange (Layer 2)"

    Metadata-only exchange where possible ([ODTIS-0225](../spec/04-trust-network/SPEC.md)). Gateway proxies to L1 APIs after grant check.

    ```mermaid
    sequenceDiagram
    autonumber
    participant PB as Partner backend
    participant XGW as exchange-gateway
    participant TS as trust-service
    participant VA as verification-api
    participant AUD as audit-service

    PB->>XGW: mTLS + service_id + purpose
    XGW->>TS: Validate cert + grant
    alt denied
    XGW-->>PB: 403 fail-closed
    else approved
    XGW->>VA: Forward scoped request
    VA-->>XGW: Response
    XGW-->>PB: Response
    XGW->>AUD: exchange event + trace_id
    end
    ```

    **RI shortcut:** `ven-partner-sdk` / `exchange-client` in [core-impl](https://github.com/odtis/core-impl)

---

## Logical surfaces → reference code

Informative mapping only. Your stack may use different names; bind via [component-bindings YAML](../implementation/component-bindings/).

```mermaid
flowchart LR
  subgraph annex [Annex A logical API]
    VA2[verification-api]
    CA2[citizen-api]
    XGW2[exchange-gateway]
    AA2[admin-api]
  end

  subgraph repos [VenID RI repos]
    VIC[ven-identity-core]
    VTN[ven-trust-network]
    VCS[ven-cloud-stack]
  end

  VA2 --> VIC
  CA2 --> VIC
  AA2 --> VIC
  XGW2 --> VTN
  KC2[OIDC realm] --> VCS
  TR2[trust-registry] --> VTN
  TS2[trust-service] --> VTN

  style annex fill:#e8eaf6,stroke:#3949ab
  style repos fill:#e0f2f1,stroke:#00695c
```

Full matrix with ODTIS IDs per component: [Component bindings](COMPONENT-BINDINGS.md) · Machine-readable: [RI-MAP.yaml](../implementation/RI-MAP.yaml)

---

## Profiles and deployment phases

Profiles are **what you claim**. Deployment phases ([Section 10](../spec/10-deployment-profiles/SPEC.md)) are **how mature** your production posture is.

```mermaid
flowchart TB
  RA[Reference Architecture<br/>always required ODTIS-0001-0010]

  subgraph phase1 [Phase 1  - citizen identity]
    CI[Core Identity<br/>OIDC verify consent]
  end

  subgraph phase2 [Phase 2  - institutional exchange]
    TN[Trust Network<br/>mTLS catalog grants]
    REL[Reliance Extensions<br/>Capa B optional]
    FED[Federation<br/>bilateral operators]
  end

  subgraph phase3 [Phase 3  - operator duties]
    OP[Operator<br/>PKI audit regulator export]
  end

  subgraph phase4 [Phase 4  - sector modules]
    EXT[Extended Annex D<br/>wallet webhooks KYB]
  end

  RA --> CI
  CI --> TN
  TN --> FED
  CI --> REL
  RA --> OP
  CI --> OP
  RA --> EXT
  CI --> EXT
```

| Phase | Add profile | You gain | Typical integrator |
|-------|-------------|----------|-------------------|
| **1** | Core Identity | OIDC, verification API, consent | National IdP, bank KYC hub |
| **2** | + Trust Network | mTLS gateway, catalog, grants | Telco, insurer, agency exchange |
| **2+** | + Reliance Extensions | Capa B reliance schema + sub-modules | High-assurance RP overlay |
| **2+** | + Federation | Bilateral cross-operator trust | Cross-border wallet / eID |
| **3** | + Operator | PKI ceremonies, regulator export | Platform operator |
| **4** | + Extended | Wallet, webhooks, KYB, inclusion | Sector pilots |

Details: [Profile comparison](PROFILES.md) · Declare in [conformance-statement.yaml](../conformance/templates/conformance-statement.yaml)

---

## Conformance ladder  - L1 → L2 → L3

Each level answers a different question. Do not skip L1 in CI even if you only care about production.

```mermaid
flowchart LR
  subgraph L1 [L1 Laboratory]
    direction TB
    Q1{Is the spec<br/>repo coherent?}
    V1[validate-registry.py]
    V2[run.sh structural]
    Q1 --> V1
    Q1 --> V2
  end

  subgraph L2 [L2 Staging]
    direction TB
    Q2{Does your deployment<br/>behave correctly?}
    S1[Live OIDC / verify smoke]
    S2[conformance-statement.yaml]
    S3[L2 report template]
    Q2 --> S1
    Q2 --> S2
    Q2 --> S3
  end

  subgraph L3 [L3 Production]
    direction TB
    Q3{Independently<br/>verified?}
    A1[Third-party audit]
    A2[Attestation letter]
    Q3 --> A1
    Q3 --> A2
  end

  L1 -->|PASS| L2
  L2 -->|published claim| L3
```

| Level | Question | Command / artifact | Guide |
|-------|----------|-------------------|-------|
| **L1** | Registry + tests internally consistent? | `./conformance/run.sh` | [Conformance README](../conformance/README.md) |
| **L2** | Live stack matches declared profiles? | `run-sandbox-check.sh` + statement YAML | [Self-cert guide](../conformance/certification/self-cert-guide.md) |
| **L3** | Production maturity audited? | Auditor attestation | [Auditor guide](../conformance/certification/auditor-guide.md) |

!!! warning "Trademark"
    L2 self-cert does **not** grant the **ODTIS Certified** mark. See [Trademark policy](../governance/TRADEMARK-POLICY.md).

---

## Adoption workflow  - independent vendor

End-to-end path from zero to publishable claim (typically days to weeks, not months of spec archaeology).

```mermaid
flowchart LR
  A[1 Pick profile] --> B[2 Read mandatory sections]
  B --> C[3 Bind Annex A + registry]
  C --> D[4 Implement fail-closed gates]
  D --> E[5 L1 in CI]
  E --> F[6 L2 on staging]
  F --> G[7 Publish statement]

  A -.-> PROFILES[PROFILES.md]
  B -.-> SPEC[spec/INDEX]
  C -.-> ANNEX[Annex A frozen]
  D -.-> TESTS[conformance/tests]
  E -.-> RUN[run.sh]
  F -.-> SANDBOX[sandbox runner]
  G -.-> SELF[self-cert guide]
```

Expanded narrative: [Adoption guide](../ADOPTION.md) · [Getting started](GETTING-STARTED.md)

---

## Normative domains (requirement counts)

Where complexity lives in the registry  - useful when scoping a team or a sprint.

```mermaid
%%{init: {'themeVariables': { 'pie1': '#3949ab', 'pie2': '#5c6bc0', 'pie3': '#7986cb', 'pie4': '#9fa8da', 'pie5': '#283593', 'pie6': '#c5cae9', 'pie7': '#1a237e'}}}%%
pie showData
 title 204 requirement IDs by domain
 "Identity Assurance (61)" : 61
 "Reliance Extensions (55)" : 55
 "Governance (36)" : 36
 "Trust Registry (26)" : 26
 "Reference Arch (10)" : 10
 "Federation (8)" : 8
 "Core Concepts (8)" : 8
```

Table view: [Domain map](DOMAINS.md) | [Requirements index](REQUIREMENTS-INDEX.md)

---

## Data and trust boundaries

Personal data flows **in** through registration; flows **out** only through gates. Temp biometrics/docs purge per [ODTIS-0314](../spec/05-consent-privacy/SPEC.md).

```mermaid
flowchart LR
 subgraph collect [Collection]
 REG[Registration + proofing]
 DOC[Document / biometry refs]
 end
 subgraph store [Storage]
 PG[(PostgreSQL identity)]
 MINIO[(Object store temp)]
 end
 subgraph release [Distribution]
 OIDC[OIDC claims]
 VER[Verification API]
 end
 subgraph block [Fail-closed gates]
 CONS[consent-service]
 LOA[LoA minimum]
 GRANT[partner grant]
 end

 REG --> PG
 DOC --> MINIO
 MINIO -->|purge ODTIS-0314| X[Purged]
 PG --> CONS
 CONS --> OIDC
 CONS --> VER
 LOA --> VER
 GRANT --> VER
```

Privacy normative section: [Section 5 Consent and privacy](../spec/05-consent-privacy/SPEC.md) · Threat controls: [Annex B](../annexes/B-threat-mitigations/README.md)

---

<div class="odtis-hub-footer" markdown="1">

## Quick links by goal

| Goal | Document |
|------|----------|
| 15-minute implementer path | [Getting started](GETTING-STARTED.md) |
| Full adoption narrative | [Adoption guide](../ADOPTION.md) |
| RI surface → ODTIS ID map | [Component bindings](COMPONENT-BINDINGS.md) |
| VenID stack diagrams (ports, compose) | [core-impl ARCHITECTURE](https://github.com/odtis/core-impl/blob/main/docs/ARCHITECTURE.md) |
| OpenAPI downloads | [Downloads & artifacts](DOWNLOADS.md) |
| Profile dependencies | [Profile comparison](PROFILES.md) |
| Threat controls | [Annex B threats](../annexes/B-threat-mitigations/README.md) |
| Live project metrics | [Status](STATUS.md) |

</div>
