# GitHub Actions secrets for odtis.org deploy

Configure in **GitHub → odtis/core-spec → Settings → Secrets and variables → Actions → Repository secrets**.

| Secret | Value | Notes |
|--------|-------|-------|
| `ODTIS_EC2_HOST` | `ec2-user@YOUR_EC2_PUBLIC_IP` | Same value as local `scripts/odtis-deploy.env` |
| `ODTIS_SSH_KEY` | *full PEM file contents* | **Not** the file path |

## Paste the PEM correctly

On your Mac:

```bash
pbcopy < ~/.ssh/your-deploy-key.pem
```

In GitHub → **New repository secret**:

- **Name:** `ODTIS_SSH_KEY`
- **Secret:** Cmd+V (must include `-----BEGIN ... PRIVATE KEY-----` through `-----END ... PRIVATE KEY-----`)

Common mistakes:

| Wrong | Right |
|-------|-------|
| `~/.ssh/your-deploy-key.pem` | Full file contents |
| Only the middle lines | Include BEGIN and END lines |
| Extra quotes around the key | Paste raw PEM only |

## Verify locally before CI

```bash
ssh -i ~/.ssh/your-deploy-key.pem -o BatchMode=yes ec2-user@YOUR_EC2_PUBLIC_IP echo ok
```

Should print `ok`.

## Workflow

`.github/workflows/release-deploy.yml` on every push to `main` (except `chore(release):*`):

1. Verify secrets exist (fail fast if empty)
2. Bump semver minor in `VERSION`
3. Build site → rsync EC2
4. Commit `chore(release): ODTIS <version> site deploy`

## Re-run after fixing secrets

Actions → **Release and deploy site** → **Re-run all jobs**
