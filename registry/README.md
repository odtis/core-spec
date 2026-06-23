# ODTIS registry

<div class="odtis-hub-hero" markdown="1">

Machine-readable source for requirements, profiles, events, and terminology. **Normative prose** lives in `spec/`; the registry holds IDs, keywords, trace hints, and conformance test links.

<p class="odtis-hub-meta" markdown="1">
<strong>Version:</strong> <a href="/VERSION">0.9.0-draft</a> | 
<strong>Browse:</strong> [Requirements index](../site/REQUIREMENTS-INDEX.md) | 
<strong>Project hub:</strong> [Project hub](../project/README.md)
</p>

</div>

---

## At a glance

| Item | Count |
|------|-------|
| Requirement IDs | **204** |
| Conformance profiles | 7 (+ Extended / Reliance sub-modules) |
| Audit event schemas | 16 + envelope |
| Structural domains | 8 (`ODTIS-0000`..`0007`) |

---

## Artifacts

| File | Format | Description |
|------|--------|-------------|
| [Requirements registry](requirements.json) | JSON | 204 normative IDs with keywords, sections, `conformance_test` links |
| [Profile definitions](profiles.yaml) | YAML | Profile definitions and dependency graph |
| [Structural domains](domains.yaml) | YAML | Eight structural domains |
| [Legacy ID map](id-map.yaml) | YAML | Legacy -> canonical ID map |
| [Audit event catalog](events.yaml) | YAML | Audit event catalog |
| [Schemas](events/schemas/) | JSON Schema | Event payloads + envelope |
| [Terminology registry](terminology.yaml) | YAML | Normative term definitions |
| [Book 1 domain map (YAML)](book1-domains.yaml) | YAML | Book 1 D1-D10 -> profiles (informative mapping) |
| Site guide | [Book 1 domain map](BOOK1-DOMAINS.md) | Human-readable domain matrix |

!!! note "Not in HTML site"
    YAML/JSON files are excluded from MkDocs. Clone the repo or use [Downloads](../site/DOWNLOADS.md). Index: [Machine-readable artifacts](../site/DOWNLOADS.md#machine-readable-artifacts).

---

## ID format (ODTIS-MNNN)

| Layer | Pattern | Example |
|-------|---------|---------|
| **Domain** | `ODTIS-0000` .. `ODTIS-0007` | ODTIS-0007 Reliance Extensions |
| **Requirement** | `ODTIS-MNNN` (4 digits) | ODTIS-0301 (Identity Assurance) |
| **Legacy (traceability)** | `ODTIS-N.N.N` in `legacy_id` | ODTIS-3.1.1 -> ODTIS-0301 |

Section 1 Reference Architecture uses `ODTIS-0001`..`0010` in domain `ODTIS-0000`. Extended IDs `0344`..`0365` are in registry @ `0.9.0-draft` (Annex D).

---

## Section distribution

| Section | IDs |
|---------|-----|
| 01-scope-conformance | 10 |
| 02-terminology-loa | 8 |
| 03-identity-services | 27 |
| 04-trust-network | 26 |
| 05-consent-privacy | 34 |
| 06-federation | 8 |
| 07-operator-governance | 17 |
| 08-security | 10 |
| 09-audit-events | 6 |
| 10-deployment-profiles | 3 |
| 11-reliance-profiles | 55 |
| **Total** | **204** |

---

## Regenerate and validate

```bash
# from repository root
python3 scripts/expand-product-requirements.py # Book 1 / product backlog (idempotent)
python3 scripts/extract-requirements.py # transitional P18 sync
python3 scripts/validate-registry.py
python3 scripts/generate-spec-section-indexes.py
python3 scripts/validate-section-completeness.py
```

**Authoritative source:** normative prose in `spec/*/SPEC.md`. P18 was the extraction baseline; `extract-requirements.py` is transitional only.

---

<div class="odtis-hub-footer" markdown="1">

## Still stuck?

| Document | Purpose |
|----------|---------|
| [Domain map](../site/DOMAINS.md) | Structural domain map |
| [Specification index](../spec/INDEX.md) | Normative sections 1-11 |
| [Profile comparison](../site/PROFILES.md) | Profile comparison |
| [Conformance overview](../conformance/README.md) | L1/L2/L3 verification |

</div>
