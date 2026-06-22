# ODTIS language policy

**Status:** normative for repository contributions 
**Canonical language:** **English (en)**

**Project hub:** [Project hub](../project/README.md) | **Contributing:** [Contributing guide](CONTRIBUTING.md)

---

## Rule

All **authoritative ODTIS text** MUST be written in English:

| In scope (English only) | Examples |
|-------------------------|----------|
| Normative specification | `spec/*/SPEC.md` |
| Annexes published on digitaltrustinfrastructure.org | `annexes/**/README.md`, OpenAPI `description` / `summary` fields |
| Registry metadata | `registry/requirements.json`, `terminology.yaml`, `profiles.yaml`, `events.yaml` |
| Conformance procedures | `conformance/tests/**/*.md`, `conformance/README.md` |
| Governance and site | `governance/*.md`, `README.md`, `CHANGELOG.md`, `PLAN-PHASES.md` |
| Machine-readable schemas | JSON Schema `title` / `description`; YAML comments in tracked annexes |

Translations (Spanish or other languages) MAY exist **outside** `odtis/` for narrative books, policy briefs, or jurisdiction playbooks. They are **informative** and MUST NOT contradict ODTIS MUST requirements.

---

## Exceptions

| Case | Treatment |
|------|-----------|
| **Proper nouns** | Keep original spelling (e.g., *Aadhaar*, *eIDAS*, agency names) |
| **Citizen-facing UI** | ODTIS requires *citizen-readable* consent text in the **end-user locale**; the spec prose describing that obligation stays in English |
| **External informative docs** | Book 1/2/3 and P18 on [digitaltrustinfrastructure.org](https://digitaltrustinfrastructure.org) are not vendored in this repo; link only, do not copy normative text |
| **Legacy redirect** | `PLAN-FASES.md` stub points to `PLAN-PHASES.md` |

---

## Pull request checklist

- [ ] New or changed normative prose is English
- [ ] No Spanish (or mixed-language) requirement text in `registry/requirements.json`
- [ ] OpenAPI human-readable fields are English
- [ ] Conformance test steps are English
- [ ] Use ASCII punctuation in site Markdown: `-` not em dash; `section N` not section sign
- [ ] Site Markdown passes `python3 scripts/validate-site-language.py` (MkDocs publish set)

See also [Contributing guide](CONTRIBUTING.md) and section **1.15 Language** in [Section 1 - Scope and conformance](../spec/01-scope-conformance/SPEC.md).
