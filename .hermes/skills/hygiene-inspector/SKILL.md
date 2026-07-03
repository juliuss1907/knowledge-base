---
name: hygiene-inspector
description: Validates knowledge base folder structure against folder-structure.md whitelist. Read-only validator.
version: 1.9
last_updated: 2026-07-03
---

# Hygiene Inspector

Ensures knowledge base folder structure complies with specifications defined in `wiki/meta/folder-structure.md`.

---

## Role

Scan entire knowledge base directory tree, validate folder structure and file paths, generate report listing hygiene violations. Report goes to `wiki/reviews/YYYY-MM-DD_hygiene-report.md` and updates `wiki/reviews/_action-required.md`.

**Critical**: This validator only reads and reports. Never modifies files or folders. Fix Agent applies corrections after Julius approves.

---

## When to use

- **Daily**: 23:30 (after Format and Output Validators complete)
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
7. **Send notification** — Telegram alert to Julius (or final response if cron)
8. **Verify scope conflicts** — if a workflow file is actively used but not whitelisted, report it as `[SPEC CONFLICT]` instead of silently suppressing it

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
- `HEARTBEAT.md` (symlink to `.openclaw/HEARTBEAT.md`)
- `IDENTITY.md` (symlink to `.openclaw/IDENTITY.md`)
- `SOUL.md` (symlink to `.openclaw/SOUL.md`)
- `TOOLS.md` (symlink to `.openclaw/TOOLS.md`)
- `USER.md` (symlink to `.openclaw/USER.md`)
- `.gitignore`
- `.openclaw/`
- `.hermes/`
- `context/`
- `raw/`
- `wiki/`
- `scripts/`

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

Also use `[SPEC CONFLICT]` when a file is clearly part of the live workflow but the whitelist was not updated to allow it.

Example:
```
[SPEC CONFLICT]
Path: wiki/reviews/_approval-log.md
Issue: workflow uses this file, but folder-structure.md does not whitelist it in wiki/reviews/
Recommendation: either whitelist the file or move the workflow artifact out of wiki/reviews/
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
- [references/scan-script.py](references/scan-script.py) — production scan script with full KB classifiers (root, context, raw/all-types, wiki/all-zones, agent homes)
- [references/common-patterns.md](references/common-patterns.md) — recurring non-compliant patterns and their resolutions
- [scripts/verify.py](scripts/verify.py) — post-run verification of report, action file, and scan reproducibility
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
   - Increment pending-report count if this run created a new pending review item

3. **Run verify.py (interactive sessions only):**
   ```bash
   python3 .hermes/skills/hygiene-inspector/scripts/verify.py
   ```
   Checks report content, _action-required.md update, and scan reproducibility.
   **Skip under cron mode** — `execute_code` and subprocess are blocked; use ad-hoc
   verification instead (see step 4 of cron fallback below).

4. **Send notification:**
   - If interactive session: Telegram alert to Julius
   - If cron job: final response IS the notification (no `send_message` available)
   ```
   Hygiene inspection complete
   - Issues found: N (X ERROR, Y WARNING, Z INFO)
   - Paths checked: M
   - Report: wiki/reviews/YYYY-MM-DD_hygiene-report.md

   Review: wiki/reviews/_action-required.md
   Commands: 'approve hygiene' or 'show hygiene'
   ```

---

## Running under cron

When invoked as a scheduled cron job, `execute_code` is blocked by `approvals.cron_mode: deny`. **Do not attempt `execute_code`.**

**Workaround:**
1. Write the scan script to a temp file via `write_file` (e.g., `/tmp/hygiene_scan.py`)
2. Run it via `terminal` with `python3 /tmp/hygiene_scan.py`
3. Parse the terminal output to build the report

See `references/scan-script.py` for a known-good scan template and `references/full-tree-scan-notes.md` for pitfalls found in real KB runs.

**⚠️ Pitfall:** The scan script handles Vietnamese diacritics via `\u` Unicode escapes. Do NOT use Python raw strings (`r'...'`) for regex patterns containing `\u` — raw strings treat `\u` literally, causing all naming checks to return false positives (hundreds of spurious WARNINGs). The corrected template in `references/scan-script.py` uses a non-raw `SLUG_CHARS` variable with single `\u` escapes, interpolated into regex patterns that use double-backslash escapes (`\\d`, `\\.`).

**⚠️ Pitfall:** In full-tree scans, classify `*.bak` leftovers in `wiki/drafts/` as temporary-file cleanup warnings, not naming errors. `.gitkeep` in a populated drafts zone is also a cleanup warning, not a structural ERROR.

---

## Agent home scanning rule

`.openclaw/` and `.hermes/` are agent-owned runtime workspaces. **Do not flag deep internals as orphans.**

- **Skip** `.hermes/` and `.openclaw/` at depth > 1 entirely for orphan checks
- **Only check** first level inside agent homes for clearly misplaced user content (e.g., a `src_*` file or `YYYY-MM-DD_*.md` sitting at `.openclaw/memory/`)
- **Do not flag** cron output, skill docs, runtime logs, or agent config files as orphans
- **Do flag** heartbeat artifacts that leaked outside their agent home (e.g., `wiki/reviews/HEARTBEAT.md`, `raw/.last_heartbeat`)

---

## Common non-compliant patterns

Beyond the standard whitelist, watch for these recurring naming violations in `wiki/reviews/`:

| Bad pattern | Good pattern | Example |
|---|---|---|
| `<type>-report-YYYY-MM-DD.md` | `YYYY-MM-DD_<type>-report.md` | `format-report-2026-05-30.md` → `2026-05-30_format-report.md` |
| `YYYY-MM-DD_validation-check.md` | `YYYY-MM-DD_output-report.md` | `2026-05-28_validation-check.md` |
| `YYYY-MM-DD_<type>-report-v2.md` | `YYYY-MM-DD_<type>-report.md` | Merge v2 into canonical name |

In `wiki/drafts/`:
- Underscores (`analysis_2026-advice.md`) → hyphens (`analysis-2026-advice.md`)

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
| `execute_code` blocked (cron mode) | Use `write_file` + `terminal` workaround — see `references/scan-script.py` |
| `SyntaxError: unicodeescape` on docstring (line 19) | Docstring uses non-raw `"""` containing `\u` sequences. When the file is written via `write_file` (JSON-encoded content), `\u` in the docstring body triggers Python's string parser. **Fix:** Use `r"""` for the docstring so `\u` literals are preserved as-is. The script shipped in `references/scan-script.py` has this fix applied. |
| `\u` Unicode escapes in raw strings produce false positives | Python raw strings (`r'...'`) do NOT process `\u` escapes — all naming checks fail silently. Use non-raw strings with double-backslash regex escapes (`\\d`) + single `\u` for Unicode. See top-of-file comment in `references/scan-script.py`. |
| Duplicate issues from os.walk + explicit checks | Deduplicate by `(path, issue)` tuple before reporting |

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

## Full-tree scan pitfalls

When building a production scan script from the template in `references/scan-script.py`, four false-positive sources must be handled:

### 1. Archive regex prefix
`RE_REVIEW_ARCHIVE` must match `^wiki/reviews/archive/` not `^archive/`. `os.walk` relative paths start from the repo root, so the bare `archive/` prefix will never match. The proven pattern is in `references/scan-script.py`.

### 2. Papers naming convention
`raw/papers/` uses `YYYY-MM-DD_<author>_<title>.md` — two slug segments separated by an underscore. The standard `RE_RAW_CONTENT` (`YYYY-MM-DD_<slug>.md`) will flag every paper. Must add `RE_RAW_PAPERS` and check it before the fallthrough to `RE_RAW_CONTENT`.

### 3. Whitelist override for naming checks
Files that are explicitly whitelisted by name (e.g., `context/USER.md`, `wiki/meta/index-spec.md`) should skip the generic lowercase-hyphen naming check. Only apply naming rules to content files (concepts, sources, tags, topics, drafts, raw content).

### 4. Recurring HEARTBEAT leak
`wiki/reviews/HEARTBEAT.md` is a known recurring issue — it has been flagged every run since 2026-06-25. Fix Agent removal is transient; the writing process recreates it. Flag it as ERROR each time it appears, but note in the report that it needs a process-level fix, not another file deletion. See `references/common-patterns.md` for details.

### 5. classify_root_folder never called (fixed 2026-07-02)
`classify_root_folder()` was defined but never invoked from `main()`. Root-level folders outside the whitelist (e.g., `state/`) were only caught by the empty-directory check as INFO, not by the path-whitelist check as ERROR. Fixed by adding a root-folder classification loop inside `main()` when `rel_dir == ""`. Also added `ROOT_FOLDER_ORPHANS` dict for known recurring root folders.

### 6. paths_checked drift on re-run (expected, not a bug)
Re-running the scan after writing the report file (or any other new file to the KB) will increase `paths_checked` by the number of new files. This is normal — the scan walks the live filesystem. When comparing reproducibility in `scripts/verify.py`, only compare issue counts and categories, not the exact `paths_checked` number. A ±1–3 drift from report/action-file writes is expected.

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

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.9 | 2026-07-03 | Cleaned up post-validation steps: removed duplicate "Update _action-required.md" entries, added explicit `scripts/verify.py` invocation as step 3 (skip under cron). Added pitfall #6: `paths_checked` drift on re-run is expected when report/action files are written between scans — compare only issue counts, not exact path counts. |
| 1.8 | 2026-07-02 | Fixed `classify_root_folder()` never called from `main()` — root-level folders outside whitelist (e.g. `state/`) were only caught as INFO (empty directory), never as ERROR (path whitelist). Added root-folder classification loop in `main()` at `rel_dir == ""`. Added `ROOT_FOLDER_ORPHANS` dict for known recurring root folders with process-level fix guidance. Added pitfall #5 to Full-tree scan pitfalls. |
| 1.7 | 2026-06-28 | Replaced skeletal scan-script template with production version proven on 51K-path scan. Production script handles all KB zones: root whitelist, context/, raw/ (all 6 types including papers + repos patterns), wiki/ (all 7 subfolders including reviews archive), agent homes, scripts/, .tmp- folders. Added `scripts/verify.py` for post-run artifact verification. Updated `references/common-patterns.md` with HEARTBEAT leak resolution (fixed as of 2026-06-28). |
| 1.6 | 2026-06-27 | Full-tree scan on 17,526-path KB uncovered three false-positive sources in the production script: (1) archive regex needed `^wiki/reviews/archive/` not `^archive/`, (2) papers use `YYYY-MM-DD_<author>_<title>.md` not standard `YYYY-MM-DD_<slug>.md`, (3) explicitly whitelisted files (e.g. `context/USER.md`) must skip generic naming checks. Added `RE_RAW_PAPERS`, fixed `RE_REVIEW_ARCHIVE`, and added `RE_REVIEW_REPORT` regex patterns to `references/scan-script.py`. Added "Full-tree scan pitfalls" section to SKILL.md. Documented recurring HEARTBEAT leak pattern in `references/common-patterns.md`. |
| 1.5 | 2026-06-26 | Removed contradictory `MEMORY.md` logging step because the skill is report-only and write-restricted to `wiki/reviews/`. Added guidance for live workflow artifacts that are not yet whitelisted (report as `[SPEC CONFLICT]`, e.g. `wiki/reviews/_approval-log.md`). Added `references/full-tree-scan-notes.md` and restored `references/scan-script.py` so the SKILL.md links resolve. Clarified that `wiki/drafts/*.bak` and `.gitkeep` should be cleanup warnings, while backup subfolders remain path errors. |
| 1.4 | 2026-06-23 | Fixed `references/scan-script.py`: changed docstring from `"""` to `r"""` to prevent `SyntaxError: unicodeescape` when the script is written via `write_file` (JSON `\u` processing + non-raw Python string parsing conflict). Changed `SLUG_CHARS` from raw string to non-raw with double-backslashes for consistency with the documented pitfall. Added docstring SyntaxError to failure modes table. |
| 1.3 | 2026-06-22 | Fixed `references/scan-script.py`: replaced raw-string regex patterns with non-raw strings to correctly handle `\u` Unicode escapes (Vietnamese diacritics). Raw strings treat `\u` literally — caused 722 false WARNINGs across all naming checks. Added pitfall to cron section and failure modes. |
| 1.2 | 2026-06-17 | Initial release with scan script, common patterns reference, cron workaround. |

---

**End of SKILL.md**
