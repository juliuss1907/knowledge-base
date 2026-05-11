# Hygiene Inspector

Ensures knowledge base folder structure complies with specifications defined in `wiki/meta/folder-structure.md`.

---

## Role

Scan entire knowledge base directory tree, validate folder structure and file paths, generate report listing hygiene violations. Report goes to `wiki/reviews/YYYY-MM-DD_hygiene-report.md` and updates `wiki/reviews/_action-required.md`.

**Critical**: This validator only reads and reports. Never modifies files or folders. Fix Agent applies corrections after Julius approves.

---

## When to use

- **Daily**: 23:00 (after Format and Output Validators complete)
- **On-demand**: Julius says "validate hygiene" or "check folder structure"
- **After bulk operations**: File moves, folder restructuring, cleanup
- **After structure changes**: When folder-structure.md is updated

**Why daily validation:**
- Catch misplaced files immediately
- Detect orphaned files from failed operations
- Ensure folder structure stays clean
- Small daily checks easier than weekly cleanup

---

## Quick start

1. **Load folder-structure.md** — read ground truth folder rules
2. **Scan entire KB** — walk directory tree from root
3. **Validate each path** — check against whitelist
4. **Detect orphans** — files in wrong locations
5. **Generate report** — write to `wiki/reviews/YYYY-MM-DD_hygiene-report.md`
6. **Update action file** — add entry to `wiki/reviews/_action-required.md`
7. **Send notification** — Telegram alert to Julius
8. **Log** to `.hermes/MEMORY.md`

---

## Critical rules

### Read-only validator
- **Only read** file and folder paths
- **Only write** to `wiki/reviews/` (reports only)
- **Never modify** folder structure
- **Never move** or delete files

### Validation dimensions (3 checks)

1. **Path whitelist** — Only allowed paths exist
2. **Naming conventions** — Folders and files follow rules
3. **Orphan detection** — No files in wrong locations

### Severity levels

| Severity | Meaning | Example |
|---|---|---|
| **ERROR** | Forbidden path exists | File in root that shouldn't be there |
| **WARNING** | Naming convention violated | Folder uses uppercase |
| **INFO** | Suggestion for cleanup | Could archive old files |

---

## Report format

```markdown
# Hygiene Inspection — YYYY-MM-DD

**Status:** pending
**Issues found:** N
**Created:** YYYY-MM-DD HH:MM:SS
**Validator:** hygiene-inspector

**Paths checked:** M

---

## Issue 1: [Issue type]

**Path:** <path>
**Severity:** ERROR | WARNING | INFO
**Category:** Path | Naming | Orphan
**Issue:** <description>
**Current:** <what exists now>
**Expected:** <what folder-structure.md requires>
**Suggested fix:** <action to take>

---

## Issue 2: [Issue type]

[...]
```

---

## Validation categories summary

### Path whitelist
- Root level: only allowed files/folders
- Depth 1: only whitelisted subfolders
- Depth 2+: follow folder-structure.md rules
- No files outside designated zones

### Naming conventions
- Folders: lowercase-hyphen (except `.openclaw`, `.hermes`)
- Files: follow type-specific rules
- No spaces, underscores, special chars
- Agent homes: exact names required

### Orphan detection
- Files in wrong folders (e.g., source in concepts/)
- Empty folders (no files inside)
- Temporary files left behind (.tmp, .bak)
- Archive candidates (old review reports)

---

## Handling Structure Changes

When Julius needs to add/remove folders or files from the knowledge base:

### Adding new folder

**Workflow:**
1. Update `wiki/meta/folder-structure.md` first (add to whitelist)
2. Commit changes to git
3. Create folder
4. Next Hygiene Inspector run will validate new structure

**Example:**
```bash
# 1. Edit folder-structure.md
vim wiki/meta/folder-structure.md
# Add: wiki/experiments/ — Testing new concepts

# 2. Commit
git add wiki/meta/folder-structure.md
git commit -m "feat: add wiki/experiments/ to structure"

# 3. Create folder
mkdir wiki/experiments/

# 4. Next hygiene run (23:00) → OK
```

**If folder created before updating folder-structure.md:**
- Hygiene Inspector will report ERROR
- Julius can approve with note: "Intentional, updating folder-structure.md"
- Update folder-structure.md within 24h
- Next run will validate correctly

---

### Removing folder

**Workflow:**
1. Backup files if needed
2. Update `wiki/meta/folder-structure.md` (remove from whitelist)
3. Update agent SKILL.md files (remove references to folder)
4. Commit changes
5. Delete folder
6. Next Hygiene Inspector run will validate new structure

**Example:**
```bash
# 1. Backup if needed
cp -r wiki/drafts/ wiki-drafts-backup/

# 2. Edit folder-structure.md
vim wiki/meta/folder-structure.md
# Remove: wiki/drafts/

# 3. Update agent skills
vim .openclaw/skills/compile-agent/SKILL.md
# Remove references to wiki/drafts/

# 4. Commit
git add wiki/meta/folder-structure.md .openclaw/skills/
git commit -m "refactor: remove wiki/drafts/ folder"

# 5. Delete folder
rm -rf wiki/drafts/

# 6. Next hygiene run (23:00) → OK
```

---

### Adding file at root level

**Workflow:**
1. Update `wiki/meta/folder-structure.md` Section "Root level" (add to whitelist)
2. Commit changes
3. Create file
4. Next Hygiene Inspector run will validate

**Example:**
```bash
# 1. Edit folder-structure.md
vim wiki/meta/folder-structure.md
# Add to root whitelist: CHANGELOG.md

# 2. Commit
git add wiki/meta/folder-structure.md
git commit -m "feat: add CHANGELOG.md to root"

# 3. Create file
touch CHANGELOG.md

# 4. Next hygiene run (23:00) → OK
```

**Current root whitelist:**
- `AGENTS.md`
- `TAGS.md`
- `README.md`
- `knowledge-base.md`
- `.openclaw/`
- `.hermes/`
- `context/`
- `raw/`
- `wiki/`

Any other file at root → ERROR

---

### Temporary folders (experimental)

**For quick testing without updating folder-structure.md:**

Use `.tmp-` prefix:
```bash
mkdir .tmp-experiments/
```

**Hygiene Inspector behavior:**
- Paths with `.tmp-` prefix → **WARNING** (not ERROR)
- Allows Julius to test quickly
- Should be deleted when done (not permanent)

**Cleanup:**
```bash
# After testing
rm -rf .tmp-experiments/

# Or promote to permanent
mv .tmp-experiments/ wiki/experiments/
# Then update folder-structure.md
```

---

### Emergency bypass

**If Julius needs folder urgently and can't update folder-structure.md immediately:**

1. Create folder
2. Hygiene Inspector will report ERROR
3. Julius approves report via Telegram: `approve hygiene`
4. Add note: "Intentional, will update folder-structure.md"
5. Update folder-structure.md within 24 hours
6. Next run will validate correctly

**This should be rare** — prefer updating folder-structure.md first.

---

### Renaming folder

**Workflow:**
1. Update `wiki/meta/folder-structure.md` (change folder name)
2. Update agent SKILL.md files (update references)
3. Commit changes
4. Rename folder using git
5. Next Hygiene Inspector run will validate

**Example:**
```bash
# 1. Edit folder-structure.md
vim wiki/meta/folder-structure.md
# Change: wiki/tag/ → wiki/tags/

# 2. Update agent skills
vim .openclaw/skills/index-agent/SKILL.md
# Update references: wiki/tag/ → wiki/tags/

# 3. Commit
git add wiki/meta/folder-structure.md .openclaw/skills/
git commit -m "refactor: rename wiki/tag/ to wiki/tags/"

# 4. Rename folder
git mv wiki/tag/ wiki/tags/

# 5. Commit rename
git add wiki/
git commit -m "refactor: apply folder rename"

# 6. Next hygiene run (23:00) → OK
```

---

## Constraints

### Write zones
- **Allowed:** `wiki/reviews/` only
- **Forbidden:** Everything else

### Forbidden actions
- No modifying folder structure
- No moving files
- No deleting files or folders
- No creating folders
- No renaming files or folders

### Performance
- Scan entire KB in one pass
- **Report limit: 20 issues per day** (daily runs)
- Skip `.git/`, `node_modules/`, `.obsidian/` (gitignored)

---

## Escalation

Flag for Julius when:

### Ambiguous path rule
```
[HYGIENE UNCERTAINTY]
Path: wiki/new-folder/
Issue: folder-structure.md doesn't specify if this folder is allowed
Question: Should this folder exist?
```

### Systematic violation
```
[SYSTEMATIC VIOLATION]
Pattern: 15 files in wiki/drafts/ older than 30 days
Likely cause: Drafts not being reviewed
Recommendation: Archive or delete old drafts
```

### Folder-structure.md conflict
```
[SPEC CONFLICT]
Issue: folder-structure.md has contradictory rules
Section A says: "wiki/tag/ auto-generated"
Section B says: "wiki/tag/ manual only"
Recommendation: Clarify folder-structure.md
```

### Structure change detected
```
[STRUCTURE CHANGE]
New folder detected: wiki/experiments/
Not in folder-structure.md whitelist
Action: If intentional, update folder-structure.md
```

---

## Details

For complete validation algorithm, folder rules, and error handling, see:
- [workflow.md](workflow.md) — step-by-step validation process
- [examples.md](examples.md) — sample hygiene issues and fixes
- [wiki/meta/folder-structure.md](../../wiki/meta/folder-structure.md) — ground truth folder rules

---

## Post-validation

After successful validation run:

1. **Verify report written:**
   ```bash
   test -f "wiki/reviews/$(date +%Y-%m-%d)_hygiene-report.md"
   ```

2. **Update _action-required.md:**
   - Add entry to "Pending Reports" section
   - Update "Last updated" timestamp

3. **Send Telegram notification:**
   ```
   Hygiene inspection complete
   - Issues found: N (X ERROR, Y WARNING, Z INFO)
   - Paths checked: M
   - Report: wiki/reviews/YYYY-MM-DD_hygiene-report.md

   Review: wiki/reviews/_action-required.md
   Commands: 'approve hygiene' or 'show hygiene'
   ```

4. **Log to MEMORY.md:**
   ```markdown
   ## YYYY-MM-DD HH:MM:SS — Hygiene inspection
   - Paths checked: M
   - Issues found: N (A ERROR, B WARNING, C INFO)
   - Report: wiki/reviews/YYYY-MM-DD_hygiene-report.md
   - Top violations: [violation types]
   ```

---

## Batch behavior

Hygiene Inspector always processes entire KB in one run:
- Walk directory tree from root
- Check every path against folder-structure.md
- Generate single report
- No incremental validation

**Typical run time:** 5-15 seconds (fast directory scan)

---

## Failure modes

| Issue | Action |
|---|---|
| folder-structure.md not found | Fatal error, cannot validate without ground truth |
| folder-structure.md invalid | Fatal error, alert Julius |
| Permission denied on path | Skip path, log warning |
| Disk full / Permission denied | Stop, alert Julius |

---

## Performance benchmarks

Typical validation times (daily runs):

| Total paths | Time |
|---|---|
| 100-500 | 5-10s |
| 500-1000 | 10-15s |
| 1000-2000 | 15-30s |

**Bottlenecks:**
- Walking large directory trees
- Checking many paths against whitelist

---

## Relationship with other agents

**OpenClaw agents** should follow folder-structure.md when creating files.

**Hygiene Inspector** catches:
- Files created in wrong locations
- Folders created without permission
- Orphaned files from failed operations
- Naming convention violations

If systematic violations found, review agent SKILL.md files and update to match folder-structure.md.

---

**End of SKILL.md**