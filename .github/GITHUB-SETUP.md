# GitHub setup guide - ODTIS `core-spec`

Checklist to publish and operate [odtis/core-spec](https://github.com/odtis/core-spec) as a first-class open-source specification repository.

**Automate what you can:**

```bash
gh auth login
cd core-spec
./scripts/set-github-repo-metadata.sh
```

---

## 1. Make the repository public

**Where:** GitHub -> `odtis/core-spec` -> **Settings** -> **General** -> **Danger Zone** -> **Change repository visibility** -> **Public**

**Before going public, run locally:**

```bash
./scripts/audit-before-publish.sh
```

---

## 2. Repository profile (Settings -> General)

| Field | Value |
|-------|--------|
| **Description** | `Open Digital Trust Infrastructure Specification (ODTIS) - vendor-neutral digital identity, trust networks, and conformance (0.9.0-draft).` |
| **Website** | `https://odtis.org` |
| **Topics** | `odtis`, `open-specification`, `digital-identity`, `trust-network`, `digital-trust`, `conformance`, `oidc`, `openapi`, `identity-management`, `zero-trust` |

**Social preview image (optional):** Settings -> **General** -> **Social preview** -> Upload `1280x640` image (use `site/assets/og-card.svg` exported to PNG, or a branded banner).

**Include in the home directory:** README, LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY - already present.

---

## 3. Features (Settings -> General)

| Feature | Recommendation |
|---------|----------------|
| **Issues** | On |
| **Discussions** | On (enable before categories) |
| **Projects** | Optional |
| **Wiki** | Off (use odtis.org + repo docs) |
| **Sponsorships** | Off unless you add `.github/FUNDING.yml` |

**Discussions enable via CLI:**

```bash
gh api -X PATCH repos/odtis/core-spec -f has_discussions=true
```

---

## 4. Pull requests (Settings -> General -> Pull Requests)

Recommended:

- [x] Allow squash merging (default message: PR title)
- [x] Allow merge commits (optional, for release merges)
- [ ] Allow rebase merging (optional)
- [x] **Automatically delete head branches** after merge
- [x] **Allow auto-merge** (optional)

**PR template:** `.github/pull_request_template.md` (auto-loaded).

---

## 5. Discussions

### 5.1 Create categories

**Where:** **Discussions** tab -> **gear icon** (Categories) or Repository **Settings** -> **Discussions** -> **Set up discussions**

Create these categories:

| Category | Format | Who can post | Purpose |
|----------|--------|--------------|---------|
| **General** | Open discussion | Everyone | Welcome, intros |
| **Q&A** | Question / Answer | Everyone | Spec interpretation |
| **Ideas** | Open discussion | Everyone | Non-normative proposals |
| **Show and tell** | Open discussion | Everyone | Pilots, integrations |
| **Announcements** | Announcement | Maintainers only | Releases, review cycles |

Discussion **templates** are in `.github/DISCUSSION_TEMPLATE/` (auto-suggested when opening a new discussion).

### 5.2 Pin welcome post (General)

**Where:** Discussions -> **New discussion** -> Category **General** -> paste below -> **Pin discussion**

<details>
<summary>Copy-paste: Welcome discussion body</summary>

```markdown
## Welcome to ODTIS Discussions

Community space for the **Open Digital Trust Infrastructure Specification (ODTIS)**.

- **Site:** https://odtis.org
- **Version:** `0.9.0-draft` (review draft)
- **License:** [CC BY 4.0](https://github.com/odtis/core-spec/blob/main/LICENSE)
- **Copyright:** FinnectOS, Inc.

### What belongs here

- Questions about profiles, Annex A, conformance (L1/L2/L3), adoption
- Ideas for examples, tooling, documentation
- Show and tell: sandbox results, integration approaches
- Introductions and collaboration

### What belongs elsewhere

| Topic | Channel |
|-------|---------|
| Security vulnerabilities | **info@odtis.org** ([SECURITY.md](https://github.com/odtis/core-spec/blob/main/SECURITY.md)) |
| Editorial clarification | [Clarification issue](https://github.com/odtis/core-spec/issues/new?template=odtis-clarification.yml) |
| Normative MUST change | [RFC issue](https://github.com/odtis/core-spec/issues/new?template=odtis-rfc.yml) |
| L2 sandbox report | [Sandbox issue](https://github.com/odtis/core-spec/issues/new?template=odtis-sandbox-report.yml) |

### Introduce yourself

Reply with who you are, what you are building, which **profile(s)** you care about, and how we can help.
```

</details>

---

## 6. Issues

**Templates in repo:** `.github/ISSUE_TEMPLATE/`

| Template | Use |
|----------|-----|
| ODTIS clarification | Non-normative wording fixes |
| ODTIS RFC | Normative MUST/SHOULD changes |
| ODTIS sandbox report | L1/L2 implementation evidence |
| Site or docs bug | odtis.org / MkDocs issues |

**Template chooser:** `.github/ISSUE_TEMPLATE/config.yml` (links to Discussions, Adoption guide, Security).

**Recommended labels** (create under **Issues** -> **Labels**):

| Label | Color | Purpose |
|-------|-------|---------|
| `odtis` | default | All spec work |
| `clarification` | | Non-normative |
| `rfc` | | Normative proposal |
| `conformance` | | Tests / L2 |
| `sandbox` | | Live target reports |
| `documentation` | | Site / docs |
| `site` | | odtis.org |

**Link issues to Discussions:** Settings -> **General** -> at bottom, enable **Issues** integration with Discussions; convert `question`-labeled issues to Discussions when appropriate.

---

## 7. Community standards

**Where:** **Insights** -> **Community** (community profile checklist)

| Item | File |
|------|------|
| README | `README.md` |
| License | `LICENSE` |
| Contributing | `CONTRIBUTING.md`, `governance/CONTRIBUTING.md` |
| Code of conduct | `CODE_OF_CONDUCT.md` |
| Security policy | `SECURITY.md` |
| Support | `.github/SUPPORT.md` |
| Issue templates | `.github/ISSUE_TEMPLATE/` |

Target: **100%** community profile completion.

---

## 8. Branch protection (recommended)

**Where:** Settings -> **Branches** -> **Add branch ruleset** (or classic rule for `main`)

Suggested for `main`:

- [x] Require a pull request before merging
- [x] Require approvals: **1** (after CODEOWNERS configured)
- [x] Require status checks (add CI later if reintroduced; optional for now)
- [x] Require conversation resolution
- [ ] Restrict who can push: maintainers only

**CODEOWNERS:** edit `.github/CODEOWNERS` with real `@handles`, then enable in ruleset.

---

## 9. Releases and tags

**Where:** **Releases** -> **Draft a new release**

For Zenodo / citation snapshots:

```bash
./scripts/package-release.sh
```

Tag format: `0.9.0-draft`, `0.9.1-draft`, eventually `1.0.0`.

Attach release notes from `CHANGELOG.md`.

---

## 10. Organization settings (optional)

If using the `odtis` GitHub organization:

- **Org profile:** logo, `https://odtis.org`, description
- **Member teams:** `spec-editors` for CODEOWNERS
- **Default repository visibility:** public for `core-spec`
- **Base permissions:** Read for members, Write for editors

---

## 11. Post-launch checklist

- [ ] Repository is **public**
- [ ] Description, website, topics set (`set-github-repo-metadata.sh`)
- [ ] **Discussions** enabled + categories + pinned welcome
- [ ] Social preview image uploaded
- [ ] Community profile **100%**
- [ ] Announce on odtis.org / newsletter
- [ ] Link Discussions from [FEEDBACK.md](governance/FEEDBACK.md) (already references issue templates)
- [ ] Review cycle 1 close date communicated (2026-06-26)

---

## 12. Files in this repository

```
.github/
  GITHUB-SETUP.md              # this guide
  repository-settings.md       # short metadata reference
  SUPPORT.md                   # GitHub Support link target
  CODEOWNERS                   # optional review routing
  pull_request_template.md
  ISSUE_TEMPLATE/
    config.yml
    odtis-clarification.yml
    odtis-rfc.yml
    odtis-sandbox-report.yml
    odtis-site-bug.yml
  DISCUSSION_TEMPLATE/
    general.yml
    q-and-a.yml
    ideas.yml
    show-and-tell.yml
scripts/
  set-github-repo-metadata.sh
```

---

## Related

- [Contributing](../governance/CONTRIBUTING.md)
- [Feedback channels](../governance/FEEDBACK.md)
- [Audit before publish](../scripts/audit-before-publish.sh)
