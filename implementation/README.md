# Reference implementations

<div class="odtis-hub-hero" markdown="1">

Maps VenID product codebases to ODTIS profiles and conformance tests. **Informative only** - independent vendors are not required to use VenID code.

<p class="odtis-hub-meta" markdown="1">
<strong>Normative authority:</strong> ODTIS spec + registry | 
<strong>Project hub:</strong> [Project hub](../project/README.md) | 
<strong>Conformance:</strong> [Conformance overview](../conformance/README.md)
</p>

</div>

!!! tip "Independent implementers"
    Full adoption path without VenID code: [Adoption guide](../ADOPTION.md).

---

## At a glance

| Item | Value |
|------|-------|
| **RI surfaces mapped** | 19 (see [RI surface map](RI-MAP.yaml)) |
| **Component bindings** | 9 YAML files + [site index](../site/COMPONENT-BINDINGS.md) |
| **Gaps closed (L2 sandbox)** | 20 |
| **Gaps deferred (production)** | 4 |
| **Phase statements** | Phase 1-4 under [Statements](statements/) |

---

## Choose your path

| You are... | Start here | Outcome |
|------------|------------|---------|
| **Mapping VenID code to ODTIS** | [RI surface map](RI-MAP.yaml) | Surface -> profile -> IDs |
| **Auditing component bindings** | [Component bindings](../site/COMPONENT-BINDINGS.md) | Generated binding index |
| **Checking open RI gaps** | [Known gaps](gaps/KNOWN-GAPS.md) | Gap register |
| **Production deferred items** | [Deferred production track](gaps/DEFERRED-TRACK.md) | mTLS, TSA, L3 playbook |
| **L3 Phase 4 package** | [L3 certification package](L3-CERTIFICATION-PACKAGE.md) | Reproducible auditor bundle |
| **Site doc phases (maintainers)** | [Documentation roadmap](DOCUMENTATION-ROADMAP.md) | R0-R4 internal roadmap |

---

## Repositories (VenID monorepo)

| Component | Path | ODTIS profile | Primary sections |
|-----------|------|---------------|------------------|
| Identity core / IdP | `../core-impl/ven-identity-core/` | core-identity | 2, 3, 5 |
| Trust network | `../core-impl/ven-trust-network/` | trust-network | 4 |
| Trust network UI | `../core-impl/ven-trust-network-web/` | *(informative)* | - |

Extended Phase 4 services (wallet, inclusion, webhook, signature, KYB, eregistry) map to Annex D sub-modules in [RI surface map](RI-MAP.yaml).

---

## Traceability stack

| Artifact | Purpose |
|----------|---------|
| [RI surface map](RI-MAP.yaml) | Surface -> profile -> ODTIS IDs -> tests |
| [Component Bindings](component-bindings/) | Per-component normative bindings |
| [Component bindings](../site/COMPONENT-BINDINGS.md) | Generated site index |
| [Gap register (YAML)](gaps/gaps.yaml) | Machine-readable gap register |
| [Known gaps](gaps/KNOWN-GAPS.md) | Human gap summary |
| [Deferred production track](gaps/DEFERRED-TRACK.md) | Production resolution playbook |
| [Phased Backlog](PHASED-BACKLOG.md) | Epic backlog (generated header) |
| [Documentation roadmap](DOCUMENTATION-ROADMAP.md) | Maintainer site doc phases (R0-R4) |

Validate bindings:

```bash
python3 scripts/validate-component-bindings.py
python3 scripts/validate-ri-map.py
```

---

## Conformance statements (VenID)

| Phase | Statement | Profiles |
|-------|-----------|----------|
| 1 | [Venid Phase1 Core](/implementation/statements/venid-phase1-core/) | Core Identity |
| 2 | [Venid Phase2 Trust](/implementation/statements/venid-phase2-trust/) | + Trust Network |
| 3 | [Venid Phase3 Operator](/implementation/statements/venid-phase3-operator/) | + Operator |
| 4 | [Venid Phase4 Full](/implementation/statements/venid-phase4-full/) | Full mandate + Extended |

**L3 package:** [L3 certification package](L3-CERTIFICATION-PACKAGE.md) | reproduce: `./conformance/run-phase4-package.sh`

---

## Verify against RI

```bash
cd odtis

# L1 lab (CI gate)
./conformance/run-l1-lab.sh

# L2 live (Keycloak realm example)
export ODTIS_TARGET=http://localhost:8180/realms/identidad-digital
./conformance/sandbox/run-sandbox-check.sh

# Gap closure regression
./conformance/run-gap-closure-checks.sh
```

Certification rules: [Certification program](../governance/CERTIFICATION.md)

---

## Related tabs

| Tab | When to use |
|-----|-------------|
| [Conformance](../conformance/README.md) | L1/L2/L3 verification |
| [Specification](../spec/INDEX.md) | Normative prose |
| [Project](../project/README.md) | Status, governance, downloads |

---

<div class="odtis-hub-footer" markdown="1">

## Still stuck?

| Goal | Document |
|------|----------|
| Sandbox alignment map | [Sandbox alignment](../conformance/sandbox/README.md) |
| Book 2 vs ODTIS | [Book 2 cross-review](../governance/BOOK2-CROSS-REVIEW.md) |
| Live coverage metrics | [Project status](../site/STATUS.md) |

</div>
