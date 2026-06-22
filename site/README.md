# ODTIS specification site

Static site for [odtis.org](https://odtis.org) built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Local preview

```bash
cd odtis
python3 -m venv .venv-site
source .venv-site/bin/activate
pip install -r site/requirements.txt
mkdocs serve -f site/mkdocs.yml
```

Open http://127.0.0.1:8000

## Production build and deploy prep

```bash
./scripts/deploy-site.sh
# output: ../build/odtis-spec-site/ (workspace level, gitignored) + CNAME (odtis.org)
```

Sync to a static host:

```bash
ODTIS_DEPLOY_DEST=/var/www/odtis.org ./scripts/deploy-site.sh
```

## Deploy (GitHub Pages example)

```bash
mkdocs gh-deploy -f site/mkdocs.yml --remote-branch gh-pages
```

Or upload `build/odtis-spec-site/` (workspace root) to any static host bound to `odtis.org`.

## Site navigation

The sidebar uses **five top tabs** (Material theme). Order follows the adoption journey: read spec -> bind annexes -> verify -> project meta.

| Tab | Audience | Sidebar order (summary) |
|-----|----------|-------------------------|
| **Home** | Everyone | Landing only |
| **Specification** | Implementers, auditors | Index -> **Profiles** -> **Normative sections 1-10** -> **Reference indexes** |
| **Annexes** | Implementers | Overview -> Annex A-D (OpenAPI, threats, standards, Extended) |
| **Conformance** | Test labs, operators | Overview -> Getting started -> FAQ -> **L1/L2** -> **L3** |
| **Project** | Adopters, contributors | Overview -> **About** -> **Adoption** -> **Legal** -> **Citation** -> RI -> IETF -> Governance |

**Look and feel:** custom CSS in [Extra.Css](stylesheets/extra.css), logo in [Logo.Svg](assets/logo.svg).

Normative reading path: **Home -> Specification -> Profiles -> section 1**. Governance detail (IPR, errata, liaison, RFC template, etc.) is grouped under **Project -> Governance**; active review cycle items appear near the top of that section.

**Footer:** Changelog, Cite, Downloads (not in the sidebar). **Annex A** groups OpenAPI registry, freeze record, and OIDC discovery under the Annexes tab.

**Language:** all published pages are English (`theme.language: en`). `./scripts/build-site.sh` runs `scripts/validate-site-language.py` before each build.

**Generated pages:** `scripts/generate-site-indexes.py` rebuilds [Glossary](GLOSSARY.md) and [Requirements index](REQUIREMENTS-INDEX.md) from `registry/` before each `./scripts/build-site.sh` run.

## Configuration

- Config: [Mkdocs.Yml](mkdocs.yml)
- Content root: `odtis/` (`docs_dir: ..`)
- Build output: `build/odtis-spec-site/` at workspace root (outside `odtis/`, gitignored locally)
