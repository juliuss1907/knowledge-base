---
name: git-secret-cleanup
description: Remove accidentally committed secrets from git history, update .gitignore, and force-push clean history. Covers the full end-to-end workflow with filter-branch, stash management, and ref cleanup.
category: devops
---

# Git Secret Cleanup

End-to-end workflow for removing secrets from git history and preventing future leaks via `.gitignore`. Designed for the knowledge-base repo but applicable to any repo.

## When to use

- GitHub push protection blocks a push due to secrets in history
- Secrets (API keys, OAuth tokens) accidentally committed
- Need to rewrite history to purge sensitive files AND prevent re-occurrence

## Prerequisites

- Push access to the remote (SSH key or valid GitHub token)
- No pending work that can't be recreated (history rewrite is destructive)
- Other collaborators must be notified — they'll need `git reset --hard origin/master` after

## Workflow

### Step 1: Backup

```bash
cp -r .git /tmp/repo-name-git-backup
```

### Step 2: Identify secret files

```bash
# GitHub will tell you the exact paths in the push rejection message
# e.g., .hermes/auth/google_oauth.json, .hermes/auth.json
```

### Step 3: Delete files from disk

```bash
rm -rf .hermes/auth/
```

### Step 4: Clean working directory completely

`filter-branch` is extremely strict — it will fail with "You have unstaged changes"
even when `git stash --all` appears to clear everything. This is because submodule
dirty state and certain modified files survive stash. Do NOT skip any of these:

```bash
# Stash everything including untracked and ignored
git stash push --all -m "temp-stash-before-filter"

# Discard any remaining modifications
git checkout .

# Force-delete any remaining untracked files (critical!)
git clean -fd   # requires approval for force delete

# Verify: git status must show NOTHING
git status
```

**If filter-branch STILL fails:** `git status --short` and `git checkout --` each
modified file individually. Submodule entries (`m <path>`) can be ignored.

### Step 5: Run filter-branch

```bash
FILTER_BRANCH_SQUELCH_WARNING=1 git filter-branch --force \
  --index-filter 'git rm -rf --cached --ignore-unmatch .hermes/auth/' \
  --prune-empty --tag-name-filter cat -- --all
```

**Pitfall:** If filter-branch fails with "You have unstaged changes" even after stash, check `git status` — there may be modified files not covered by stash. Use `git checkout -- <file>` for each.

### Step 6: Clean refs/original/ (filter-branch backup refs)

```bash
for ref in $(git for-each-ref --format="%(refname)" refs/original/); do
  git update-ref -d "$ref"
done
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

### Step 7: Update .gitignore

Add entries for the secret files AND related runtime state:

```gitignore
# Hermes auth & session data (không lên git)
.hermes/auth/
.hermes/auth.json
.hermes/channel_directory.json
.hermes/state.db*
.hermes/logs/
.hermes/sessions/
.hermes/cron/
```

Commit: `git add .gitignore && git commit -m "gitignore: exclude secrets and runtime state"`

### Step 8: Restore working files (optional)

```bash
git stash list        # find the right stash
git stash pop stash@{N}
```

### Step 9: Verify history is clean

```bash
git log --oneline master -- .hermes/auth/    # should be empty
git show master:.hermes/auth/google_oauth.json  # should fail with "NOT IN"
```

### Step 10: Force push

```bash
git push --force-with-lease origin master
```

## Knowledge-base specific .gitignore

The full Hermes exclusion set for this project:

```gitignore
.hermes/auth/
.hermes/auth.json
.hermes/channel_directory.json
.hermes/state.db*
.hermes/logs/
.hermes/sessions/
.hermes/cron/
```

Combined with Obsidian exclusions:

```gitignore
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/cache
```

## Pitfalls

- **filter-branch needs pristine working tree** — stash ALL changes including untracked (`--all`), then `git checkout .` then `git clean -fd`. Submodule dirty state (`m <path>`) is harmless and can be ignored.
- **Stash conflicts on pop** — stash may conflict with filter-branch rewritten files. Drop conflicting stashes and let them regenerate naturally.
- **No credential** — HTTPS remotes with no credential helper will fail. Check with `ssh -T git@github.com` or `gh auth status`. If neither works, the push must be done from a machine with valid GitHub auth.
- **Other machines must reset** — after force push, other clones need `git fetch origin && git reset --hard origin/master`, NOT a normal pull.
- **.gitignore does NOT untrack already-committed files** — after filter-branch, files you added to `.gitignore` may still appear in `git status` as tracked. You must explicitly `git rm --cached` each one, then commit. Always run `git ls-files <pattern>` to find stragglers, then `git rm --cached` them all before the final commit.
- **Session/state files constantly regenerate** — `.hermes/sessions/*.json`, `state.db*`, `.jsonl` files are recreated every time the agent runs. Make sure ALL variants are in `.gitignore` AND `git rm --cached`'d.

## Recovery

If filter-branch goes wrong: restore from `/tmp/repo-name-git-backup`:

```bash
rm -rf .git
cp -r /tmp/repo-name-git-backup .git
git reset --hard HEAD
```
