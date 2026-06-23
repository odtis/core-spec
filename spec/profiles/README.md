# ODTIS conformance profiles (adoptable)

Standalone profile documents for implementers and auditors. Each profile composes **normative sections** from [Specification index](../INDEX.md) plus bindings in [OIDF positioning](/governance/liaison/OIDF-POSITIONING/).

**Start here for adoption:** [Adoption guide](/ADOPTION/) | **Compare profiles:** [Profile comparison](/site/PROFILES/) | **Conformance:** [Conformance overview](/conformance/)

**Registry:** 149 requirement IDs | **Test procedures:** 159 (85 with smoke evidence)

**Registry authority:** [Profile definitions](/registry/profiles.yaml)

Each profile document includes a **generated** table of applicable `ODTIS-MNNN` IDs. Regenerate:

```bash
python3 scripts/generate-profile-docs.py
```

| Profile | Document | Depends on |
|---------|----------|------------|
| Reference Architecture | [Reference Architecture profile](reference-architecture-profile.md) | - |
| Core Identity | [Core Identity profile](core-identity-profile.md) | reference-architecture |
| Trust Network | [Trust Network profile](trust-network-profile.md) | core-identity |
| Federation | [Federation profile](federation-profile.md) | trust-network |
| Operator | [Operator profile](operator-profile.md) | reference-architecture, core-identity |
| Extended | [Extended profile](extended-profile.md) | reference-architecture, core-identity (+ sub-modules) |
| Reliance Extensions | [Reliance Extensions profile](reliance-extensions-profile.md) | reference-architecture, core-identity (+ Capa B sub-modules) |

**Conformance:** [Self-certification guide](../../conformance/certification/self-cert-guide.md)
