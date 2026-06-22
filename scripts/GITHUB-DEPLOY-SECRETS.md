# GitHub Actions secrets for odtis.org deploy

Configure in **GitHub → odtis/core-spec → Settings → Secrets and variables → Actions**.

| Secret | Example value | Notes |
|--------|---------------|-------|
| `ODTIS_EC2_HOST` | `ec2-user@YOUR_EC2_PUBLIC_IP` | SSH `user@host` from your cloud console |
| `ODTIS_SSH_KEY` | *(full PEM private key contents)* | Paste entire `.pem` file including `BEGIN/END` lines |

Optional: set repository variable `ODTIS_REMOTE_DIR` if docroot differs from `/var/www/odtis.org`.

## Workflow

`.github/workflows/release-deploy.yml` runs on every push to `main` except `chore(release):*` commits:

1. Bump **semver minor** in `VERSION` (`0.9.0-draft` → `0.10.0-draft`)
2. Sync version across spec artifacts + MkDocs UX metadata
3. Build site (`../build/odtis-spec-site/`)
4. Rsync to EC2
5. Commit `chore(release): ODTIS <version> site deploy` back to `main`

## Version visibility on site

- Header badge: `config.extra.odtis_version`
- Footer build line: version + git sha + timestamp
- Home hero: link to `/VERSION` and `/site/BUILD-META.json`
- Static files: `/VERSION`, `/site/BUILD-META.json`

## Local manual deploy (unchanged)

```bash
cp scripts/odtis-deploy.env.example scripts/odtis-deploy.env
./scripts/deploy-ec2.sh
```
