# LeetCode to GitHub Sync

This repository syncs accepted LeetCode submissions into GitHub using a GitHub Actions workflow.

## What it does

- Runs automatically every day at 12:00 AM IST
- Can also be triggered manually from the Actions tab
- Fetches accepted LeetCode submissions
- Writes each new solution to `solutions/<problem-slug>/submission-<submission-id>.<ext>`
- Tracks already-synced submission IDs in `synced_submissions.json`

## Repository structure

```text
.github/workflows/sync.yml     # GitHub Actions workflow
sync.py                        # Export script
synced_submissions.json        # Manifest of already-synced submission IDs
solutions/                     # Exported submissions
```

## Requirements

You need:

1. A GitHub repository
2. A signed-in LeetCode account
3. A GitHub repository secret named `LEETCODE_SESSION`

## Setup from scratch

### 1. Create a repository

Create a repository on GitHub and add these files:

- `.github/workflows/sync.yml`
- `sync.py`
- `README.md`

### 2. Add the LeetCode session secret

The workflow authenticates to LeetCode using your `LEETCODE_SESSION` cookie.

To get it:

1. Log in to LeetCode in your browser.
2. Open browser DevTools.
3. Go to the Application or Storage tab.
4. Open Cookies for `https://leetcode.com`.
5. Copy the value of the `LEETCODE_SESSION` cookie.

Then add it to GitHub:

1. Open your repository.
2. Go to `Settings`.
3. Open `Secrets and variables`.
4. Click `Actions`.
5. Click `New repository secret`.
6. Name it `LEETCODE_SESSION`.
7. Paste the cookie value and save.

If LeetCode expires or rotates the session, update this secret with a fresh cookie value.

## Do you need a GitHub token?

Usually, no.

For the normal same-repository setup, this project uses the built-in `GITHUB_TOKEN` provided by GitHub Actions. No personal access token is required.

You may need extra GitHub token setup only if:

- you want to push to a different repository
- branch protection blocks GitHub Actions from pushing directly to `main`
- your repo or organization restricts write access for `GITHUB_TOKEN`

If commits fail because Actions cannot push, check:

1. `Settings` → `Actions` → `General`
2. Under workflow permissions, allow read and write access for `GITHUB_TOKEN`

## Schedule

The workflow is configured to run:

- every day at 12:00 AM IST
- manually whenever you click `Run workflow`

Note: GitHub Actions cron uses UTC internally. `30 18 * * *` means 6:30 PM UTC, which is 12:00 AM IST.

## Manual trigger

To run it yourself:

1. Open the repository on GitHub.
2. Go to the `Actions` tab.
3. Open `Sync LeetCode submissions`.
4. Click `Run workflow`.
5. Select the branch and run it.

This is useful if you do not want to wait for the next scheduled run.

## How syncing works

On each run, the workflow:

1. Reads your recent LeetCode submissions
2. Filters accepted ones
3. Checks which submission IDs are already listed in `synced_submissions.json`
4. Fetches code for new accepted submissions
5. Writes solution files into the repository
6. Commits and pushes any new files

## Troubleshooting

### Workflow runs but nothing is added

Possible reasons:

- there are no new accepted submissions since the last sync
- `synced_submissions.json` already contains those submission IDs

### Workflow fails with LeetCode authentication errors

Your `LEETCODE_SESSION` secret is probably expired.

Fix:

1. Log in to LeetCode again
2. Copy a fresh `LEETCODE_SESSION` cookie
3. Update the repository secret
4. Run the workflow manually once

### Workflow fails while pushing to GitHub

Check:

- repository Actions permissions
- branch protection rules on `main`
- whether `GITHUB_TOKEN` has write access

## Notes

- This setup syncs accepted submissions only.
- The workflow is safe to re-run manually.
- If there are no new accepted submissions, it exits without creating a new commit.
