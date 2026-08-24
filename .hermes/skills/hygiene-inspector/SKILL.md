---
name: hygiene-inspector
description: Validates knowledge base folder structure against folder-structure.md whitelist. Read-only validator.
version: 1.20
last_updated: 2026-08-16
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
- [references/raw-subindex-conventions.md](references/raw-subindex-conventions.md) — how to add a new raw/ sub-index correctly (folder, index file, frontmatter, parent update, scan-script update)
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
   - Add a new row to the Summary table AND a new subsection under "Pending Reports"
   - **⚠️ Pitfall: Markdown table patching.** When adding a row to the Summary table via `patch`, the trailing `|` of the matched row must be accounted for. Two proven approaches:
     - **Approach A (include `|` in old_string):** Match the existing row WITH its trailing `|`. The `new_string` must then provide the `|` for all rows (including the replacement of the matched row). The file's `|` is consumed by `old_string`, so `new_string` supplies both.
       ```
       old_string:  "| 🔍 PENDING | 07-17 | Format | 324... |"
       new_string:  "| 🔍 PENDING | 07-17 | Format | 324... |\n| 🔍 PENDING | 07-17 | Hygiene | 4... |"
       ```
     - **Approach B (exclude `|` from both):** Match the existing row WITHOUT its trailing `|`. The file's unconsumed `|` closes the LAST row of `new_string`. So `new_string` must NOT include a trailing `|` on any row — the file provides it for the last row.
       ```
       old_string:  "| 🔍 PENDING | 07-17 | Format | 324..."
       new_string:  "| 🔍 PENDING | 07-17 | Format | 324...\n| 🔍 PENDING | 07-17 | Hygiene | 4..."
       ```
     - **❌ Broken (produces `||`):** `old_string` without trailing `|` + `new_string` where any row ends with `|` → the file's leftover `|` lands on the last row, creating `||` (proven 2026-07-18 on a real run).

**⚠️ Pitfall: V4A multi-hunk patches need ≥1 change line per hunk.** An `@@` hunk containing only context lines (no `-`/`+`) fails the whole patch with `hunk (no hint) not found — old_string and new_string are identical`. To INSERT a new row/section without modifying any existing line, include one anchor line as a change: `-<existing line>` / `+<existing line>` followed by `+<new line(s)>`. Proven 2026-08-23 while inserting the Hygiene row into the Summary table of `_action-required.md`.

3. **Run verify.py (interactive sessions only):**
   ```bash
   python3 .hermes/skills/hygiene-inspector/scripts/verify.py
   ```
   **Skill file location:** this skill lives INSIDE the KB at
   `/home/julius/knowledge-base/.hermes/skills/hygiene-inspector/`, NOT at
   `~/.hermes/skills/` (proven 2026-08-23: reading `~/.hermes/...` fails; references/
   edits must target the KB copy). All relative paths above resolve from KB root.
   Checks report content, _action-required.md update, and scan reproducibility.
   **Skip under cron mode** — `execute_code` and subprocess are blocked; use ad-hoc
   verification instead (see step 4 of the "Running under cron" section below).

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
4. **Ad-hoc verification — run it LAST (after ALL writes)**:
   The system flags edits as "verification stale" if you write any file after the check that confirms everything. So write the report AND `_action-required.md` AND any skill-reference updates (`common-patterns.md`) FIRST, then run verification once as the final step. Write a verification script to `/tmp/hermes-verify-hygiene-<date>.py`, run it with `terminal`. Minimal checks: report exists, `_action-required.md` updated, scan reproducible (issue counts only — `paths_checked` drifts from report write), previous-day issues resolved. If you must touch any file afterward, re-run a fresh (suffix-`b`) verify or re-verify. The system will request this after any cron run that writes files; treat it as a standard post-validation step under cron. Confirmed 2026-08-16: editing `common-patterns.md` after the first verify forced a stale-evidence flag and a second verify run.

**⚠️ Pitfall: Do NOT `rm` the temp scripts in cron mode.** `/tmp/hygiene_scan.py` and `/tmp/hermes-verify-hygiene-<date>.py` live under `/tmp`, which the OS clears automatically. Issuing `rm -f` on them under a cron job hits the approval guard (`delete in root path` pattern) and **stalls the whole run pending approval that never comes** (no user present). Leave the temp files in place — they are harmless, and the "clean up" wording above means only that you may remove them in an interactive session if you want, not that the run is incomplete without it. Confirmed 2026-08-14: `rm` stalled the run; skipping it was correct.

**⚠️ Pitfall: Severity-count comparison in verify script — `Counter` omits zero-count keys.** The scan's JSON output uses `Counter`, so keys with zero occurrences are ABSENT from the dict, not present as `0`. When the ad-hoc verify script compares counts, an expected dict like `{"ERROR": 1, "WARNING": 0, "INFO": 1}` will spuriously FAIL because `"WARNING"` is missing entirely. Compare against only the keys that appear (`{"ERROR": 1, "INFO": 1}`), or use `.get("WARNING", 0)`. Confirmed 2026-08-15.

**⚠️ Pitfall: Bold markers in `_action-required.md` string matching.** The pending count line is formatted as `**Pending reports awaiting review:** N` — Markdown bold wraps the label, so `**` sits between `:` and the number. A naive `"Pending reports awaiting review: N" in content` check will fail. Use a regex with optional `*` markers:
```python
import re
m = re.search(r'Pending reports awaiting review:\*{0,2}\s*(\d+)', content)
count = int(m.group(1)) if m else None
```
**⚠️ Pitfall: Verify-script f-strings cannot contain backslashes (Python ≤3.11).** `f"got {field(r'\*\*Status')!r}"` → `SyntaxError: f-string expression part cannot include a backslash`. Compute the value into a variable first, then interpolate (`"got %r" % val` or plain f-string without escapes). Hit 2026-08-22 while writing the ad-hoc verify script.

**⚠️ Pitfall: Bold markers also wrap the REPORT header fields, not just the action file.** The report front-matter is `**Issues found:** 9`, `**Paths checked:** 53578`, `**Status:** pending`, `**Created:** ...` — `**` sits between each label and its value. A naive `"Issues found: 9" in txt` or regex `Paths checked: (\d+)` will FAIL against the actual report (the `**` block the match). Always use the `\*{0,2}` regex form for ANY report field you assert on in the verify script, not only the action-file pending count. Proven 2026-08-17: ad-hoc cron verify initially returned VERIFY FAIL (issue-count + paths_checked checks) purely because the regex didn't allow the bold markers; content itself was correct.

**⚠️ Pitfall: Double-escaping when a field-extraction helper already calls re.escape.** If the verify script defines a helper like `field(txt, label)` that runs `re.escape(label)` internally, pass the PLAIN label (`"**Status"`) — NOT a pre-escaped regex (`r"\*\*Status"`). Pre-escaping double-escapes: the compiled pattern matches the literal string `\*\*Status`, which never appears in the report → helper returns None → spurious VERIFY FAILs on fields that are actually correct. Hit 2026-08-24 (3 FAILs, all false; fixed by passing plain labels, `-b` rerun passed 24/24). Corollary: when ad-hoc verify FAILs, grep the RAW artifact for the expected value FIRST to determine whether the report or the script is wrong before editing anything under `wiki/`.

See `references/scan-script.py` for a known-good scan template and `references/full-tree-scan-notes.md` for pitfalls found in real KB runs.

**⚠️ Pitfall:** The scan script handles Vietnamese diacritics via `\u` Unicode escapes. Do NOT use Python raw strings (`r'...'`) for regex patterns containing `\u` — raw strings treat `\u` literally, causing all naming checks to return false positives (hundreds of spurious WARNINGs). The corrected template in `references/scan-script.py` uses a non-raw `SLUG_CHARS` variable with single `\u` escapes, interpolated into regex patterns that use double-backslash escapes (`\\d`, `\\.`).

**⚠️ Pitfall:** In full-tree scans, classify `*.bak` leftovers in `wiki/drafts/` as temporary-file cleanup warnings, not naming errors. `.gitkeep` in a populated drafts zone is also a cleanup warning, not a structural ERROR.

---

## Agent home scanning rule

`.openclaw/` and `.hermes/` are agent-owned runtime workspaces. **Do not flag deep internals as orphans.**

- **Skip** `.hermes/` and `.openclaw/` at depth > 1 entirely for orphan checks
- **Only check** first level inside agent homes for clearly misplaced user content (e.g., a `src_*` file or `YYYY-MM-DD_*.md` sitting at `.openclaw/memory/`)
- **Do not flag** cron output, skill docs, runtime logs, or agent config files as orphans
- **Do flag** heartbeat artifacts that leaked outside their agent home (e.g., `wiki/HEARTBEAT.md`, `wiki/reviews/HEARTBEAT.md`, `raw/.last_heartbeat`)

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

### 7. Confirm recurring leaks are git-tracked before dismissing as transient
When a recurring orphan file (e.g. `memory/*-heartbeat-status.md`, `memory/YYYY-MM-DD-*.md`) reappears, **check `git ls-files <path>` (or `git check-ignore <path>`)** before writing "deletion is the fix". If the file is git-tracked, it reaches commits (this KB auto-commits `vault backup` roughly every 10 minutes — see `git log`), so filesystem deletion only removes the working copy; the committed copy survives and reappears on the next checkout/sync. That confirms a *process-owned* leak, not a stray artifact. Proven 2026-08-16: `memory/2026-08-16-heartbeat-status.md` was git-tracked, hence the fix MUST be root-cause (redirect the writing process output path) plus a committable removal (`git rm` + commit), not just `rm -rf memory/`. Report it accordingly in the escalation block.

### 8. Whitelist dictionaries must stay in sync with folder-structure.md
The scan script's `RAW_SUBFOLDERS`, `ROOT_FILES`, `ROOT_FOLDERS`, `WIKI_SUBFOLDERS`, and `WIKI_META_FILES` dictionaries duplicate rules from `folder-structure.md`. When `folder-structure.md` is updated (e.g., a new raw subfolder is added), the scan script's corresponding dictionary must be updated to match. **Out-of-sync whitelists silently suppress violations.** Proven 2026-07-30: `tools` was in `RAW_SUBFOLDERS` but not in folder-structure.md v1.2 — the `raw/tools/` folder passed every scan for weeks until the script was aligned with the spec. When folder-structure.md changes, patch BOTH the spec AND the scan script's dictionaries in the same commit.

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
| 1.20 | 2026-08-16 | Added pitfall #7 — confirm recurring root orphans are git-tracked (`git ls-files` / `git check-ignore`) before dismissing a leak as a stray file: `memory/2026-08-16-heartbeat-status.md` was git-tracked, so it persisted across the ~10-min `vault backup` commits and file deletion alone could not fix it — requires redirecting the writer output path + a committable removal. Clarified cron ad-hoc verification must run LAST (after ALL writes incl. `common-patterns.md`), else the system flags evidence stale and forces a re-verify (proof 08-16). `memory/`+`state/` both resurfaced 3rd consecutive run; updated `references/common-patterns.md` with 08-16 record and fixed a literal-`\n` formatting bug. |
| 1.19 | 2026-08-15 | Added cron verify-script pitfall: `Counter` omits zero-count keys, so comparing severity counts against an expected dict that includes `XXX: 0` spuriously FAILs. Confirmed on live run — `{"ERROR":1,"WARNING":0,"INFO":1}` vs actual `{"ERROR":1,"INFO":1}`. Compare only keys that appear or use `.get(k, 0)`. `state/` orphan resurfaced for 2nd consecutive run; `memory/` absent (single-orphan regression after 08-14 dual). Updated `references/common-patterns.md` with 08-15 recurrence record. |
| 1.18 | 2026-08-14 | `memory/` and `state/` root orphans RESURFACED after 4 clean runs (08-11→08-13) — broke the 3-consecutive-clean streak. Evidence: `memory/2026-08-14-0153.md` (OpenClaw session log, created 08:54) proves the memory-log writer emits to KB root `memory/` instead of `.openclaw/memory/` → process-level leak, escalated as [SYSTEMATIC VIOLATION]. Added cron pitfall: do NOT `rm` temp scan/verify scripts under cron — `/tmp` is OS-cleared and `rm` stalls on the approval guard. Updated `references/common-patterns.md` with the 08-14 recurrence record. |
| 1.17 | 2026-08-10 | Added `wiki/HEARTBEAT.md` to `HEARTBEAT_LEAK_PATHS` in scan script — new HEARTBEAT leak variant at wiki/ root level (distinct from `wiki/reviews/HEARTBEAT.md`). Added HEARTBEAT check in `classify_wiki_entry` `len(parts)==2` branch before the generic "File at wiki/ root level" error. Updated `common-patterns.md` and SKILL.md Agent home scanning rule to document the new variant. Flagged 4th consecutive run (08-07 through 08-10). |
| 1.15 | 2026-07-22 | Added pitfall to cron verification step: `_action-required.md` uses Markdown bold markers (`**`) around the pending count label, so `**Pending reports awaiting review:** N` — a naive `in` check for `Pending reports awaiting review: N` misses the `**` between `:` and `N`. Use regex with `\*{0,2}`. Updated `references/common-patterns.md`: `memory/` and `state/` root folders confirmed resolved — absent two consecutive runs (07-21, 07-22). |
| 1.13 | 2026-07-18 | "✅ Good" example (`old_string` without `\|` + `new_string` rows with `\|`) actually produces `\|\|` on the last row — the file's unconsumed `\|` is appended after the entire new_string. Replaced with two proven approaches (A: include `\|` in old_string, B: exclude `\|` from all new_string rows). Confirmed on a live run that produced `\| \|` on the new row before the fix. |
| 1.11 | 2026-07-11 | Added `memory/` to `ROOT_FOLDER_ORPHANS` in scan script (recurring root folder — flagged 5 times since 07-03). Updated `common-patterns.md`: expanded `memory/` recurrence history through 07-11, removed duplicate one-liner entry. |
| 1.10 | 2026-07-05 | Added step 4 to cron workflow: ad-hoc verification pattern (write → run → check script at `/tmp/hermes-verify-hygiene-*.py`). Fixed broken cross-reference in post-validation step 3 — now points to "Running under cron" section instead of "cron fallback" (which had no step 4). |
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
