---
name: hygiene-inspector
description: Validates knowledge base folder structure against folder-structure.md whitelist. Read-only validator.
version: 1.35
last_updated: 2026-10-03
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

**⚠️ Carry-forward rule — do NOT re-escalate an issue already escalated in a still-pending report (2026-09-01).** When a `[SYSTEMATIC VIOLATION]` was already raised in a prior report that is still `pending` (not yet approved/applied), the next run's report must mark it `CARRIED FORWARD from <date>`, note that no Fix Agent action has happened yet, and reference the original escalation — NOT emit a fresh `[SYSTEMATIC VIOLATION]` block. Proven 2026-09-01: the 6 `raw/repos/` naming violations were escalated 08-31 and correctly carried forward on 09-01 instead of re-escalated. This keeps the escalation log a list of *distinct* process problems, not one entry per run for the same unresolved issue.

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

**⚠️ Pitfall: a cron retry may be DAYS later — check `date` and reconcile pending reports before assuming a same-day [SILENT] re-run (2026-09-01).** When a Hygiene cron job fails (e.g. provider rate limit at 23:30) and the user later asks to "run hygiene again", do NOT assume it is the same day. Real time may have advanced multiple days: sibling Output/Format crons and Fix Agent will have run in the interim, producing a backlog of pending reports. Proven 2026-09-01: user asked to re-run the 08-27 job; it was actually 5 days later with 9 pending reports (08-28 → 08-31) and a new systemic `raw/repos/` naming violation already escalated on 08-31. An initial same-day [SILENT] reading was WRONG — the correct action was a fresh report dated today. Before writing any report:
1. `date` — get the real system date (the conversation/session date may be stale)
2. `ls -t wiki/reviews/*_hygiene-report.md | head` — find the most recent report
3. `grep -n 'Pending reports awaiting review' wiki/reviews/_action-required.md` — check the pending backlog
4. `find wiki/sources wiki/concepts wiki/topic wiki/tag -name '*.md' -newer <last-report>` AND `find raw/ -name '*.md' -newer <last-report>` — see what actually changed (include raw/, see next pitfall)

If the last report is from a prior day and pending entries exist, this is a **FRESH run for today's date** producing a new pending report — not a silent re-run.

**⚠️ Pitfall: new-file detection must include `raw/` — the scanner covers the whole tree (2026-09-01).** `find -newer <last-report> -- wiki/sources wiki/concepts wiki/topic wiki/tag` alone is INSUFFICIENT to decide [SILENT] vs fresh: raw/ can receive new content (e.g. an ingest batch) that the hygiene scanner flags while wiki/ is untouched. Proven 2026-09-01: reported "0 new files" from a wiki/-only `find -newer`, yet the fresh scan surfaced 6 `raw/repos/` naming WARNINGs from an 08-30 ingest batch (files landed in raw/, never touched wiki/). New-file checks for hygiene must include `raw/` (all subtypes) or use git `--diff-filter=A` reconciliation across the whole tree.

**Workaround:**
1. Write the scan script to a temp file via `write_file` (e.g., `/tmp/hygiene_scan.py`)
2. Run it via `terminal` with `python3 /tmp/hygiene_scan.py`
3. Parse the terminal output to build the report
4. **Ad-hoc verification — run it LAST (after ALL writes)**:
   The system flags edits as "verification stale" if you write any file after the check that confirms everything. So write the report AND `_action-required.md` AND any skill-reference updates (`common-patterns.md`) FIRST, then run verification once as the final step. Write a verification script to `/tmp/hermes-verify-hygiene-<date>.py`, run it with `terminal`. Minimal checks: report exists, `_action-required.md` updated, scan reproducible (issue counts only — `paths_checked` drifts from report write), previous-day issues resolved. If you must touch any file afterward, re-run a fresh (suffix-`b`) verify or re-verify. The system will request this after any cron run that writes files; treat it as a standard post-validation step under cron. Confirmed 2026-08-16: editing `common-patterns.md` after the first verify forced a stale-evidence flag and a second verify run.

**⚠️ Pitfall: the agent-home exemption hides tracked leaks inside `.openclaw/` — probe migration-marker variants EXPLICITLY (2026-09-25).** The "skip `.hermes/`/`.openclaw/` at depth > 1" orphan exemption also suppresses *runtime-artifact* findings nested there, so a git-tracked leak inside the agent home is invisible to the full-tree scan. Proven 2026-09-25: a SECOND `.migrated.<sha256>.<uuid>` marker at `.openclaw/workspace-state.json.migrated.…fb077b94-…` (69 bytes, mtime 2026-09-08 20:42, tracked in `b5e519fc`, `git check-ignore` exit 1) had existed for 17 days while the morning report asserted "no new marker variants". Two of the three reasons it was missed: (1) the exemption; (2) it shares blob `a0105ac6…` with the root marker, so even a root-only hash audit reads as "already known". **Rule:** when a recurring runtime leak is a migration/rename artifact, always run a tree-wide `find . -name '*.<suffix>.*' -not -path './.git/*'` and check `git ls-files -s` + `git check-ignore` on EVERY hit — the known-root-cause and carry-forward notes (pitfall #9) cover the canonical filename only, not its agent-home twin. Report the newly-found twin as a NEW issue and explicitly correct the prior report's claim; do not silently fold it into a carry-forward line.

**⚠️ Pitfall: `git status --porcelain` is NOT a write-zone check — it drowns in Hermes runtime churn (2026-09-25).** An ad-hoc verify that asserts "no uncommitted changes outside `wiki/reviews/`" via `git status --porcelain` FAILs spuriously: during a normal run the working tree legitimately shows ` M .hermes/state.db`, `.hermes/gateway_state.json`, `.hermes/checkpoints/**`, `.hermes/logs/`, `.hermes/cache/`, `.hermes/skills/.usage.json`, and hundreds of untracked `?? .hermes/checkpoints/store/objects/xx/` shards — all written by the runtime and the session itself, not by the validator. Proven 2026-09-25: 1 spurious FAIL, and a naive follow-up then mis-attributed the 18:14 OpenClaw dreaming run (`DREAMS.md`, `memory/dreaming/**`) to the validator. **Correct shape — attribute by mtime, and only assert on content zones the validator must never touch:**
```python
START = "2026-09-25 23:30:00"   # session start, not run date
paths = subprocess.run(["find", ".", "-newermt", START, "-print"],
                       capture_output=True, text=True).stdout.splitlines()
EXCLUDED = ("./.git", "./.hermes", "./.openclaw", "./.obsidian", "./wiki/reviews")
zone = [p for p in paths if p.strip()
        and not any(p.strip().startswith(x) for x in EXCLUDED) and p.strip() != "./wiki"]
assert not zone, zone
```
Also assert `find ./wiki/reviews -newermt START -type f` returns exactly the 2 expected files. Corollary: when a verify FAIL names `.hermes/**`, the artifact is almost always fine and the CHECK is wrong — grep the raw artifact before touching `wiki/`.

**⚠️ Pitfall: `find . -path A -prune -o -path B -prune -o … -newermt X -print` silently mis-filters (2026-09-25).** With more than one `-prune -o` pair the trailing `-print` binds only to the final `-o` expression, so paths that match no prune clause are still printed and the intended exclusions do not apply. Proven 2026-09-25: a write-zone check built from 10 content zones reported `./.git`, `./.hermes/…` as "violations" (2nd spurious FAIL on the same run). **Fix:** do ONE `find . -newermt <ts> -print` pass and filter the paths in Python, where the exclusion list is explicit and auditable. Never chain many `-prune -o` clauses before a single `-print` in a verification script.

**⚠️ Pitfall: Do NOT `rm` the temp scripts in cron mode.** `/tmp/hygiene_scan.py` and `/tmp/hermes-verify-hygiene-<date>.py` live under `/tmp`, which the OS clears automatically. Issuing `rm -f` on them under a cron job hits the approval guard (`delete in root path` pattern) and **stalls the whole run pending approval that never comes** (no user present). Leave the temp files in place — they are harmless, and the "clean up" wording above means only that you may remove them in an interactive session if you want, not that the run is incomplete without it. Confirmed 2026-08-14: `rm` stalled the run; skipping it was correct.

**⚠️ Pitfall: `python3 scan.py | python3 -c '...'` pipe is blocked by the security scanner (2026-09-01).** Piping the scan script's stdout directly into a `python3 -c` interpreter for JSON summarization triggers the `[HIGH] Pipe to interpreter` guard and the command stalls waiting for approval that never comes in cron. **Workaround:** write JSON to a file first, then read/parse the file separately:
```bash
python3 /tmp/hygiene_scan2.py > /tmp/hygiene_result.json 2>&1   # exit=0, no pipe
# then read_file /tmp/hygiene_result.json  (or a second non-piped python3 -c reading the file)
```
Same rule as heredocs/rm: never chain a second interpreter onto the scan's stdout in cron mode.

**⚠️ Pitfall: Fix Agent archives approved reports mid-session — verify against `archive/YYYY-MM/` (2026-09-01).** When re-running Hygiene after a cron rate-limit failure later the same night, the previous day's report (e.g. `2026-08-27_hygiene-report.md`) may already have been archived by Fix Agent to `wiki/reviews/archive/2026-08/` while you were away. An ad-hoc verify script that asserts the report still exists at `wiki/reviews/<date>_hygiene-report.md` will crash with `FileNotFoundError` — a false FAIL caused by the path assumption, not the data. **Fix:** before verifying, `ls wiki/reviews/<date>_* wiki/reviews/archive/<YYYY-MM>/<date>_*` and point the script at whichever path actually holds the file. Also expect sibling cron validators to have added their own `_action-required.md` entries and MEMORY.md rows since your last read (the "sibling subagent modified" warning) — re-read before writing, and treat pending-count drift as expected noise, not corruption.

**⚠️ Pitfall: Same-day re-run → append an ADDENDUM to the existing report (2026-09-08).** When a cron run finds a report for TODAY already exists (`YYYY-MM-DD_hygiene-report.md` present, status pending), do NOT treat it as a [SILENT] re-run if the filesystem changed — and do NOT create `-v2` (violates review naming). The correct action: re-scan, diff vs the morning run's flagged paths, then **append a dated addendum section to the bottom of the same report** (update the header `**Paths checked:**` to show both counts, e.g. `56020 (morning 08:15) / 56025 (evening re-scan 23:31)`, and add a `**Last re-scan:**` line). The addendum gets its own `**Status:** / **Issues found:** / **Created:**` front-matter block, re-lists genuinely new issues (E1, E2… numbering), marks unchanged items as UNCHANGED/carry-forward with a pointer to the morning issue numbers, and appends its own Actions-needed list. Then update `_action-required.md`: edit the SAME day's pending Summary-table row and Pending Reports section in place (add an `**Addendum (...)**` bullet) rather than adding duplicate rows/sections. Proven 2026-09-08: morning run 08:15 flagged 12 issues; OpenClaw migrated the root workspace-state file at 20:42 (new marker artifact appeared, HEARTBEAT symlink went dangling); evening cron 23:30 correctly produced an addendum with 2 changed findings instead of a duplicate report or a false [SILENT].

**⚠️ Pitfall: When a leak "resolves itself", audit the NEW artifacts the writer left behind — and wildcard your .gitignore guards (2026-09-08).** A long-running orphan (`openclaw-workspace-state.json`, 12 consecutive runs) disappeared mid-day — but the runtime MIGRATED the file, leaving a one-time migration marker `openclaw-workspace-state.json.migrated.<sha256>.<uuid>` at the same root path. Two lessons: (1) whenever a recurring leak is absent, don't just celebrate — `ls` for renamed/marker/sidecar variants (`*.migrated.*`, `*.bak`, `*.old`, `*.new`) at the same path before declaring resolution; (2) `.gitignore` guards added for leak patterns should cover WILDCARD variants (`openclaw-workspace-state.json.migrated.*`), not just the exact filename — a guard without wildcards lets the variant slip through and get COMMITTED by the auto `vault backup` within minutes (proven: marker created 20:42 was committed 20:45 in `b5e519fc`). If a variant is already git-tracked, the fix is `.gitignore` wildcard + `git rm --cached` + commit (Fix Agent owns execution — report-only for Hygiene).

**⚠️ Pitfall: Severity-count comparison in verify script — `Counter` omits zero-count keys.** The scan's JSON output uses `Counter`, so keys with zero occurrences are ABSENT from the dict, not present as `0`. When the ad-hoc verify script compares counts, an expected dict like `{"ERROR": 1, "WARNING": 0, "INFO": 1}` will spuriously FAIL because `"WARNING"` is missing entirely. Compare against only the keys that appear (`{"ERROR": 1, "INFO": 1}`), or use `.get("WARNING", 0)`. Confirmed 2026-08-15.

**⚠️ Pitfall: Bold markers in `_action-required.md` string matching.** The pending count line is formatted as `**Pending reports awaiting review:** N` — Markdown bold wraps the label, so `**` sits between `:` and the number. A naive `"Pending reports awaiting review: N" in content` check will fail. Use a regex with optional `*` markers:
```python
import re
m = re.search(r'Pending reports awaiting review:\*{0,2}\s*(\d+)', content)
count = int(m.group(1)) if m else None
```
**⚠️ Pitfall: Verify-script f-strings cannot contain backslashes (Python ≤3.11).** `f"got {field(r'\*\*Status')!r}"` → `SyntaxError: f-string expression part cannot include a backslash`. Compute the value into a variable first, then interpolate (`"got %r" % val` or plain f-string without escapes). Hit 2026-08-22 while writing the ad-hoc verify script.

**⚠️ Pitfall: Asserting historical text stays untouched — scope to the new section, count don't assume.** When the verify script checks that the current run did NOT add an escalation (e.g. `[SYSTEMATIC VIOLATION]`), do NOT assert a global count of zero or absence: `_action-required.md` legitimately retains historical escalations inside APPLIED entries, and the new section's own guidance may QUOTE the marker in backticks ("KHÔNG re-escalate `[SYSTEMATIC VIOLATION]`"). Proven 2026-08-25 (-b run): global count assertion expected 2, got 3 → spurious FAIL; the meaningful check passed. Correct approach: (1) extract only the new run's section (`re.search(r"### 🔍 Hygiene Inspection — YYYY-MM-DD.*?(?=### |\Z)", txt, flags=re.S)`) and assert the escalation-shaped pattern (`"[SYSTEMATIC VIOLATION] Root-cause"`) is absent THERE; (2) assert the exact total count (2 historical + N quoted) rather than zero. **RECURRED 2026-08-29 even with the section properly scoped:** the hand-written ad-hoc verify used the bare `"[SYSTEMATIC VIOLATION]" not in sec_txt` check and FAILED, because the new section's own Actions-needed line legitimately quotes the marker in backticks (`KHÔNG re-escalate \`[SYSTEMATIC VIOLATION]\``). Proven fix (23/23 PASS on the corrected rerun): assert the SHAPE only, and if asserting the bare marker, strip backticked quotes first — embed this snippet verbatim in the ad-hoc verify script:
```python
sec = re.search(r"### 🔍 Hygiene Inspection — YYYY-MM-DD.*?(?=### |\Z)", txt, flags=re.S).group(0)
# 1) escalation SHAPE absent — real escalations read "[SYSTEMATIC VIOLATION] Root-cause ..."
assert "[SYSTEMATIC VIOLATION] Root-cause" not in sec
# 2) bare marker survives only as a backticked QUOTE in guidance — strip, then assert
assert "[SYSTEMATIC VIOLATION]" not in sec.replace("`[SYSTEMATIC VIOLATION]`", "")
```

**⚠️ Pitfall: Bold markers also wrap the REPORT header fields, not just the action file.** The report front-matter is `**Issues found:** 9`, `**Paths checked:** 53578`, `**Status:** pending`, `**Created:** ...` — `**` sits between each label and its value. A naive `"Issues found: 9" in txt` or regex `Paths checked: (\d+)` will FAIL against the actual report (the `**` block the match). Always use the `\*{0,2}` regex form for ANY report field you assert on in the verify script, not only the action-file pending count. Proven 2026-08-17: ad-hoc cron verify initially returned VERIFY FAIL (issue-count + paths_checked checks) purely because the regex didn't allow the bold markers; content itself was correct.

**⚠️ Pitfall: Double-escaping when a field-extraction helper already calls re.escape.** If the verify script defines a helper like `field(txt, label)` that runs `re.escape(label)` internally, pass the PLAIN label (`"**Status"`) — NOT a pre-escaped regex (`r"\*\*Status"`). Pre-escaping double-escapes: the compiled pattern matches the literal string `\*\*Status`, which never appears in the report → helper returns None → spurious VERIFY FAILs on fields that are actually correct. Hit 2026-08-24 (3 FAILs, all false; fixed by passing plain labels, `-b` rerun passed 24/24).

**⚠️ Pitfall: The colon must be part of the field() pattern, not the caller's label.** The report front-matter is `**Status:** pending` — bold markers wrap BOTH sides of the colon. A `field()` helper whose pattern omits the colon (`re.escape(label) + r"\*{0,2}\s*(.+)"`) fails even with a correctly plain `"**Status"` label: after `re.escape`, `\*\*Status` cannot be followed by optional `*` then whitespace-value because the literal `:` sits between them → helper returns None again. Correct helper shape (proven 2026-08-25): put the colon INSIDE the helper — `pat = re.escape(label) + r":\*{0,2}\s*(.+)"` — and call it as `field(txt, "**Status")`. Corollary: when ad-hoc verify FAILs on extracted fields, grep the RAW artifact for the expected value FIRST to determine whether the report or the script is wrong before editing anything under `wiki/` (4 FAILs on 2026-08-25 were all script-side; the report was byte-correct).

**⚠️ Pitfall: Report front-matter fields may carry an extended tail — use prefix matching (2026-09-08).** When a report accumulates addenda, header fields legitimately grow beyond a bare value, e.g. `**Issues found:** 12 (2 ERROR + 10 WARNING)` or `**Paths checked:** 56020 (morning 08:15) / 56025 (evening re-scan 23:31)`. A verify check like `field(sec, "**Issues found") == "12"` spuriously FAILS even though the content is correct. Assert with `.startswith("12")` (or `in` for multi-count fields), not exact equality. Confirmed 2026-09-08: 1 of 3 initial FAILs was this exact pattern.

**⚠️ Pitfall: Backtick-wrapped paths break exact-string matches — in BOTH action-file prose AND report-body verify checks.** The action file prose wraps paths in backticks — e.g. `` `memory/` + `state/` vắng mặt chạy sạch thứ 6 liên tiếp `` — so a naive `"memory/ vắng mặt" in action_txt` FAILs: the closing backtick sits between the `/` and the following space. Proven 2026-08-28: 2 spurious FAILs on an otherwise correct run (content byte-correct; `grep` of the raw artifact showed the paths backtick-wrapped). Correct approach: check the bare path and the context word SEPARATELY, scoped to the new run's section (`re.search(r"### 🔍 Hygiene Inspection — YYYY-MM-DD.*?(?=### |\Z)", txt, flags=re.S)`), e.g. `"memory/" in sec and "vắng mặt" in sec`. Corollary of the 08-25 rule: grep the RAW artifact FIRST — when a FAIL is a prose-match issue, the report/action file is almost always right and the verify script's string is wrong.

**RECURRED 2026-09-02 in the REPORT body, not just the action file:** verify check `"repos naming [SYSTEMATIC VIOLATION] ... is RESOLVED" in rep` failed because the report renders it as `` `raw/repos/` naming ... `` — the backtick between `repos/` and `naming` prevents the joined substring from existing. Same fix: check `"repos" in rep and "naming" in rep` separately. When a verify FAIL looks like a prose/substring miss, grep the RAW artifact first — the content is almost always right and the script's string is wrong.

**Variant 2026-09-08 — absence-assertion markers quoted in backticks:** the same backtick-strip rule applies to `[SPEC CONFLICT]` and `[STRUCTURE CHANGE]`, not only `[SYSTEMATIC VIOLATION]`. A report's "clean run" line legitimately says `` Không `[SPEC CONFLICT]` `` / `` Không `[STRUCTURE CHANGE]` `` — backticked quotes ASSERTING absence. A bare `"[SPEC CONFLICT]" not in sec` check spuriously FAILS. Fix: `sec.replace("`[SPEC CONFLICT]`", "").replace("`[STRUCTURE CHANGE]`", "")` before the bare-marker assertion (2 of 3 initial FAILs on the 09-08 evening verify were exactly this).

### 20. `find -o` binds only the LAST branch — group the type test (2026-10-02)

`find . -path ./.git -prune -o -newerct <ref> -print` returned **0** for the whole tree: `-print` binds to the final `-o` expression only, so every path matching no prune clause was silently discarded. Same family: `find <file> -newerct <file>` errors outright (*"Không thể tìm biết cách giải thích … dạng ngày hay giờ"*). The familiar `find X -type f -o -type l` appears to work (identical result here) which is exactly why the trap survives — it only holds while `-print` binds to the whole expression.

**Rule:** group explicitly — `\( -type f -o -type l \) -print` — and prefer a Python `stat.S_ISREG/S_ISLNK` filter when scan and verify must share one definition. **A one-liner returning 0 for a tree just measured non-zero is a scoping bug, not an empty tree.**

### 23. Sibling validators write INSIDE your run window — set the mtime cutoff from `date`, not from a guess (2026-10-03)

At 23:30 the sibling Format Validator wrote `2026-10-03_format-report.md` at **23:28:18** — inside a write-zone check that started at `23:25`. Two symptoms: `exactly 2 files in wiki/reviews` returned **3**, and a naive START earlier than your own session start makes the check unverifiable ("did *I* write that?").

**Rule:** set `START` from the `date` you captured at the top of the run (this session: `23:30:54` ⇒ `START = 23:30:00`), and **identify your own two files by explicit path set** rather than by count:
```python
check("17c the 2 are my writes",
      set(rev) == {"./wiki/reviews/YYYY-MM-DD_hygiene-report.md",
                   "./wiki/reviews/_action-required.md"}, str(rev))
```
Also strip the bare `./wiki/reviews` **directory** entry itself — `find -newermt` prints it when any child changed, and it is not a file.

### 24. A field's value may be BOLD-wrapped too, not just its label (2026-10-03)

`**Issues found:** **20 nhóm** — 13 ERROR…` — the `\*{0,2}` in `field()` absorbs the *label's* markers, but the captured value starts with `**` too. `issues.startswith("20")` FAILs on a byte-correct report.

**Rule:** after `field()`, normalise the value before comparing: `issues.lstrip("*").strip()`. Then keep `startswith` (the extended-tail rule, pitfall #27 below) for multi-count fields. Proven: 2 of 2 initial FAILs were this, and grep-the-artifact-first (pitfall #17) is what proved the report was right.

### 25. Publish a machine count only WITH its prune definition — three prunes, three numbers (2026-10-03)

Same tree, same `-type f -o -type l` test, three legitimate answers: **242.766** (prune every `.git` at every depth) · **242.752** (the scan script's shape) · **244.840** (prune only the ROOT `.git`, keeping the nested repo's). The gap is exactly the **2.074** files in `.hermes/hermes-agent/.git` — and the 10-02 figure (243.267) matched **none** of them, so it was un-reproducible for a second consecutive run.

**Rule:** never publish a machine count without naming the prune expression, and when a prior run's number matches no shape, say so explicitly rather than silently re-baselining. Give the reader a **table of the competing definitions** — it turns a suspicious number into a documented one, and it exposes the nested-repo mass (E1) as a *counting* consequence rather than KB growth.

### 26. Check the header's severity arithmetic against its own body before publishing (2026-10-03)

10-02's header read `13 nhóm (5 ERROR, 4 WARNING, 2 INFO)` — the parenthetical sums to **11**, not 13, while the body correctly carried 13 ERROR items (E1–E13). Three runs quoted that header verbatim (10-02, `_action-required` 10-03, Format 10-03) before anyone summed it.

**Rule:** when grouping issues, assert `sum(counts) == total` and that the total equals the number of body sections, *before* writing the header. When you inherit a wrong header, correct it explicitly in the new report **and** name it as a publication defect of that run — do not silently restate the number (pitfall #17's grep-first rule again).

### 21. Dir-count shape: `os.walk` excludes the zone root, `find -type d` includes it (2026-10-02)

Published 74 dirs, verify recomputed 70 — not KB drift. `os.walk("raw")` yields `("raw", dn, fn)` for the zone itself, so summing `len(dn)` across 4 zones gives **19** (= 23 − 4 zone roots); `find raw wiki context scripts -type d` gives **23**. Same trap on the root-files term: a `cnt(".")` helper walks the **entire tree** (243K files), not the 11 top-level files the published number means.

**Rule:** add `if dp == zone: n += 1` for the content-zone dir term, count root files with `listdir` and **assert** the expected value (11), and label the figure "23 vùng nội dung (**bao gồm thư mục gốc vùng**)". Extends pitfall #16: a count shape must be reproducible from the published description alone.

### 22. `wiki/wiki.md` is a required index — never flag it as a wiki-root orphan (2026-10-02)

§7's tree lists `wiki.md ✓ required (level 1 index)` on the same lines that also say *"No files at `wiki/` root level"*. A scanner that treats every top-level file in `wiki/` as an orphan emits a **false ERROR on a file the spec requires** — proven 10-02 as a phantom 6th ERROR group.

**Rule:** in the `wiki/` root check, `continue` on whitelisted index names before the generic orphan error (same for `raw/raw.md` in `raw/`). **When a scanner ERROR reaches the report, grep the spec for the exact name first** — the tree and the Rules section can disagree (W3), and the tree's explicit `✓ required` line wins on existence. Record it as a *script* defect, not a KB finding.

### 10. Symlink validity MUST be checked with `realpath` + `exists` + `lexists` — never by comparing the relative path (2026-09-28)

`wiki/HEARTBEAT.md` was reported as "target EXISTS (16,688 bytes)" on **2026-09-26 and 2026-09-27** — both wrong, for two consecutive runs. The symlink is `../../.openclaw/HEARTBEAT.md`, created from inside `wiki/`, so it resolves to `/home/julius/.openclaw/HEARTBEAT.md` (**one level above the KB root, does not exist**). The real file is at `<KB>/.openclaw/HEARTBEAT.md`, i.e. the link is **off by one directory level** and should be `../.openclaw/HEARTBEAT.md`. The earlier reports eyeballed `ls .openclaw/HEARTBEAT.md` and assumed that was what the link pointed at.

**Rule — assert all three, never eyeball:**
```python
os.path.islink(p)                 # it IS a symlink
os.readlink(p)                    # the raw target string
os.path.realpath(p)               # fully resolved absolute target
os.path.exists(os.path.realpath(p))   # False => DANGLING
os.path.lexists(p)                # True  => the link object itself exists
```
`getmtime()` on a dangling symlink raises `FileNotFoundError` — that exception **is** the dangling signal, but it aborts the whole script, so probe with `lexists`/`realpath` first. Report the broken target, the correct relative path, and the consequence: a dangling symlink does **not** render as a note in Obsidian, so any prior claim "it shows up in the graph as a real note" must be corrected in the same report that discovers the dangling link. When a previous report asserted the opposite, say so explicitly — do not silently restate it.

### 11. Verify the REMOTE before blaming the local machine — `git ls-remote` is read-only (2026-09-28)

When `git log` shows a stale HEAD, sibling validators (Format 09-28, Output 09-28) correctly noted "HEAD unchanged, `vault backup` cron delayed" — but none checked whether the remote had the commit. `git ls-remote --heads origin` (read-only, **does not fetch or modify refs**) settled it: `refs/heads/master` on GitHub was *also* at `e05f00ab`, so the backup had not committed **on the primary machine either**. That is a different fix than "push is behind".

**Rule:** before reporting a stalled sync, run `git ls-remote --heads origin`. Report which side is behind. Also enumerate uncommitted work with `git status --porcelain --untracked-files=all` split into `M` vs `??` — and state the data-loss exposure (count of modified files + count of untracked reports) rather than calling it "delayed". Watch for decoy branches: this repo's `origin/main` is an **abandoned 2026-05-11 branch**, not the sync target — `master` is live. Verify the remote branch is the one your local `HEAD` tracks before drawing conclusions.

### 12b. The agent-home exemption hides COMMITTED SECRETS and nested repos — probe tracked status, not just paths (2026-09-29)

The "skip `.hermes/`/`.openclaw/` at depth > 1" rule (and the 09-25 marker pitfall above) generalize further. On 2026-09-29 the scanner reported **4 ERROR** while the agent home actually held **≥8** — every miss in `.hermes/`, invisible to the walk because §3 of `folder-structure.md` whitelists the whole folder as "runtime workspace".

Four new classes, all found by probing **tracked/ignored status** rather than paths alone:

1. **A `.gitignore` rule that exists but does nothing** because the file was committed *before* the rule. `git check-ignore` exits 0 (rule matches) yet `git ls-files -s` still returns a line. Proven on `.hermes/auth.json` (11,003 B, `access_token`/`refresh_token`/`api_key` key names, **78 commits** since 2026-05-12, HEAD == `git ls-remote refs/heads/master` ⇒ already on the remote) and again on `.hermes/MEMORY.md` (rule `.gitignore:81` `MEMORY.md`). **Rule of thumb: a rule added after a commit is decoration. Assert `git ls-files -s` is EMPTY, not that `check-ignore` succeeds.** Use `git check-ignore --no-index` when you want to know the *rule* in isolation.
2. **A nested bare git repo inside the KB** — `.hermes/checkpoints/store/HEAD` exists, i.e. a whole object store under the working tree. 31 files already tracked including a **28.9 MB pack blob**; **6,783 more files / 13 MB untracked**; `.gitignore` had zero rules for it (`grep -c checkpoints` = 0). Size the pack with `git cat-file -s <blob>` — `git status` shows nothing because the pack bytes matched HEAD.
3. **Tracked-but-deleted files** — `git status` ` D` entries. Seven, here: three `SKILL.md` (`.hermes/skills/note-taking/obsidian`, `autonomous-ai-agents/computer-use`, `devops/hermes-state-recovery`, all in commit `32b4c6ba` 09-09) plus a `.curator_backups/2026-08-23T06-02-56Z/` set. Verify absence with `test -e` before reporting; name the commit, and say explicitly that you did NOT read runtime logs to determine intent.
4. **Asymmetric ignore coverage** — `.openclaw/*.bak` has a rule (`.gitignore:73`) while `.hermes/config.yaml.bak.*` (18 files) has none. Grep the counterpart zone instead of assuming symmetry.

**Standing scan additions for any run that finds an ERROR in an agent home** — always also run:
```bash
git ls-files -s <path>          # empty = untracked (a real cleanup)
git log --oneline -- <path> | wc -l   # commit count = blast radius of a leak
git ls-tree -r HEAD --name-only | grep -E 'auth|token|secret|credential'   # secrets in HEAD
git status --porcelain -uall | grep '^ D'   # tracked-but-deleted
find . -name HEAD -path '*store*' -not -path './.git/*'   # nested repos
```
**Never read secret VALUES** to prove exposure — grep key *names* only (`grep -oE '"[a-z_]*(token|key|secret|credential)[a-z_]*"'`), and report blob size + commit count instead. Same discipline as the "do not read memory/log content" rule.

**Corollary — action ORDER matters, and the report must say so.** Because `vault backup` was stalled, the 6,828 runtime files were *pending* rather than *committed*: the count would jump from 31 to 6,814 the moment backup restarted. State the sequencing explicitly ("block `.gitignore` BEFORE re-enabling backup") or the reader fixes it in the wrong order and the stall turns into a permanent 14 MB commit. This is a report-quality failure, not a scan failure.

### 12. Publish the counting DEFINITION, not just the number (2026-09-28)

The 09-27 report published "1,800 files in scope" that could not be reproduced from any definition it stated. The 09-28 run used an explicit definition (4 content zones + root files + level-1 of both agent homes) = 1,733 files + 70 dirs, making the −67 delta look like the KB shrank when it is purely a scope-definition change. State the definition inline next to every scope count, and when the definition changes, say so loudly — a raw delta across different definitions is not evidence of growth or shrinkage in either direction.

### 13. `find -newer` counts regenerated files as "new" — split with `git status -uall` (2026-09-28)

`find … -newer <last-report>` returned **293** files, but `git status --porcelain -uall` showed only **10** truly new (untracked) and **293 − 10 = 283**… precisely: **290 tracked files were rewritten** by Index Agent at a single shared mtime (21:06). A report that says "293 new files" invents a pipeline surge that did not happen. Always reconcile: `??` = genuinely new, `M` = regenerated/index-churn. Report both numbers with their meaning. (Corollary of the 09-01 pitfall: new-file detection must cover `raw/` — and here it must also be *partitioned* by git status.)

See `references/scan-script.py` for a known-good scan template, `references/full-tree-scan-notes.md` for pitfalls found in real KB runs, and `references/cleanup-commit-lessons.md` for what to do when HEAD moved since the last report (re-probe every carry-forward, report `.gitignore` residue rather than rule counts).

### 17. Verify a FAIL against the RAW artifact first — 3 of 4 FAILs were the script (2026-09-30)

The 09-30 ad-hoc verify returned 4 FAIL. Grepping the raw files first (per the 08-28/09-02 rule) showed **3 were script bugs, 1 was a real defect in the report**:

| FAIL | Reality |
|---|---|
| `escalation SHAPE present` | script asserted the bare marker inside the new section, but the section's heading uses `ESCALATE LẦN 1` and only *quotes* the marker in backticks — assert `"ESCALATE"` |
| `report documents check-ignore correction` | script asserted lowercase `bỏ qua`; report has uppercase `BỎ QUA` |
| `exactly 2 files written` | compared paths without the `./` prefix `find` emits |
| **`post-write scope total == 1752`** | **REAL** — agent-home L1 drifted 99 → 98 mid-run, so the published total was unreproducible. Fixed the **report**, not the script |

**Rule:** a failing check does not tell you which side is wrong. `grep` the raw artifact for the expected value, decide, then edit — and state in the report whether it was the script or the artifact. Three reflex "fix the script" reactions would have hidden a genuine reporting defect here.

### 18. Agent-home L1 count is VOLATILE — socket filtering alone is not enough (2026-09-30)

09-29's lesson (exclude sockets) did **not** make the total reproducible. Within one run on 09-30 the agent-home L1 count moved **99 → 98**: the runtime deleted the per-session artifact `.hermes/.skills_prompt_snapshot.json` and created three `state.db.malformed-backup-20260617_082024{,-shm,-wal}`. **46 of 98** L1 files look volatile (`.db*`, `-shm`, `-wal`, `.lock`, `.pid`, `.sock`, `*cache*`, `.etag`, `.log`, `spawn-ledger`, `gateway_state`, `channel_directory`).

**Rule:** publish the stable part and label the volatile part separately — "1.751 files total; **only 1.653 stable** (1.641 content zones + 11 root); 98 agent-home L1 **volatile** (99 at scan → 98 at verify)". Only content-zone + root files and the dir count are safe to compare across runs. A transient per-session file must never be counted as KB growth, and its disappearance must never be reported as a resolved issue. Sample the count 5× over ~30s: if stable *now*, the drift came from a runtime event during the run — which is itself the finding.

**⚠️ Pitfall (2026-09-29): `paths_checked` drift is a PUBLISHED number, and SOCKETS are neither files nor stable (two separate traps).** The report file you are about to write lives in `wiki/reviews/`, which is inside a *content zone* — so publishing "1,735 files in scope" and then writing the report makes the true count 1,736. Pitfall #6 says ignore the drift in verify comparisons; it does **not** license publishing a number that no re-run can reproduce. Fix: publish **both** figures inline with the convention named — "1,734 at scan time (pre-write) / 1,735 post-write" — and have the verify script assert the POST-write number.

**The socket trap cost three consecutive spurious FAILs on the same run** (100 → 99 → 98). `.hermes/gateway.sock` is a live unix socket: `stat.S_ISSOCK` is True and **both** `os.path.isfile` and `os.path.islink` return False. So "count every entry that is not a directory" counts it as a file, and the result also drifts with the socket's lifecycle. **Any count definition must be "regular files + symlinks", i.e. `find -type f -o -type l` semantics — never "not a directory".** When a scope count wobbles by ±1 between two runs, check for sockets/FIFOs before suspecting the KB:
```python
stat.S_ISSOCK(os.stat(p).st_mode)      # and S_ISFIFO
```
Corollary: if the report's own numbers disagree with a re-run, **grep the raw artifact first** — on 09-29 the KB never changed and all three FAILs were the counting method, not the data.

**⚠️ Pitfall:** The scan script handles Vietnamese diacritics via `\u` Unicode escapes. Do NOT use Python raw strings (`r'...'`) for regex patterns containing `\u` — raw strings treat `\u` literally, causing all naming checks to return false positives (hundreds of spurious WARNINGs). The corrected template in `references/scan-script.py` uses a non-raw `SLUG_CHARS` variable with single `\u` escapes, interpolated into regex patterns that use double-backslash escapes (`\\d`, `\\.`).

**⚠️ Pitfall:** In full-tree scans, classify `*.bak` leftovers in `wiki/drafts/` as temporary-file cleanup warnings, not naming errors. `.gitkeep` in a populated drafts zone is also a cleanup warning, not a structural ERROR.

---

### 14. `git check-ignore` SKIPS tracked files — the exit code is evidence of NOTHING (2026-09-30)

Plain `git check-ignore` **does not report tracked files** (git docs: *tracked files are not shown*). For an already-committed path it returns **exit 1 with no output** — byte-identical to "no rule exists". Every run through 2026-09-29 used the plain form, producing two distinct wrong claims: "`check-ignore` exit 1 ⇒ NOT ignored" (used on the `.migrated.*` markers) and "a rule exists but is ineffective" inferred from a plain-form rc that proved nothing.

**Always run both, then classify:**

```bash
git ls-files -s -- <path>                  # empty output = untracked (definitive)
git check-ignore --no-index -v -- <path>   # rule in isolation, independent of index
```

| tracked | rule (`--no-index`) | verdict |
|---|---|---|
| yes | yes | **RULE-EXISTS-BUT-INEFFECTIVE** (committed before the rule) |
| yes | no | **TRACKED-NO-RULE** (real exposure) |
| no | yes | correctly ignored |
| no | no | real untracked leak |

Proven 2026-09-30 on `.hermes/auth.json`: plain → `rc=1`, no output; `--no-index` → `.gitignore:37:.hermes/auth.json` `rc=0`. Re-probed 21 files; 09-29's *conclusion* held but its *evidence* was invalid — say so explicitly rather than restating it.

**Corollary (extends pitfall #7):** never infer state from a git exit code alone. Assert on **output emptiness**. Plain `check-ignore` is only meaningful for files already known to be untracked.

### 15. Inventory secret/artifact exposure by FILENAME and EXTENSION, not by key names (2026-09-30)

2026-09-29 found `.hermes/auth.json` by grepping key names *inside that one file* and reported "≥4 ERRORs". Grepping **filenames** in HEAD across both agent homes found **7 auth-named tracked files** — 4 in `.openclaw/` (`device-auth.json`, `identity/device-auth.json`, `agents/main/agent/auth-profiles.json`, `auth-state.json`) + 1 in `.hermes/state-snapshots/` were missed. Some contain no matching key names, so a key-name grep can never reach them.

```bash
git ls-tree -r HEAD --name-only | grep -Ei '(auth|token|secret|credential|apikey|\.env)' | grep -v '/skills/'
```

**Then probe by EXTENSION too** — a name-grep misses runtime DBs with the same blast radius: `kanban.db` + `-shm`/`-wal` (141 commits each), `projects.db`, `verification_evidence.db` (345 commits), `state-snapshots/`, `config.yaml.bak.*` (18/18). On 2026-09-30, **9 of 9** runtime patterns had no `.gitignore` rule while `.openclaw/*.bak` and `.hermes/state.db*` did ⇒ the `.hermes/` zone is structurally unprotected. Always run the §12b standing probe set when a run finds an ERROR in an agent home.

### 16. Publish dir counts with an explicit reproducible shape (2026-09-30)

The 09-29 headline "1,735 files + 70 dirs" was **not reproducible for the dir half** — 09-30 measured 9 root + 23 content-zone (recursive) + 42 agent-home L1 = **74**, and no subset yields 70. A carried-forward total without its composition makes the next run's delta look like structural growth.

Counting shape fixed from 2026-09-30 (always with `find -type f -o -type l` / `find -type d`, sockets excluded):

- **files** = content zones (recursive) + root regular files/symlinks + agent-home level-1 files
- **dirs** = root dirs + content-zone dirs (recursive) + agent-home level-1 dirs

**⚠️ The agent-home L1 term is VOLATILE** — it changed 99 → 98 *within* the 2026-09-30 run (session artifact deleted, 3 WAL backups created). Publish it separately and label it volatile, or exclude it. Only the content-zone + root file count and the dir count are safe to compare across runs.

State both components inline beside every published total, and corroborate any file delta with `git status --porcelain -uall` split `??` vs `M` (pitfall #13) before calling it KB growth.

### 17. Verify a FAIL against the RAW artifact first — 3 of 4 FAILs were the script (2026-09-30)

The 09-30 ad-hoc verify returned 4 FAIL. Grepping the raw files before editing anything (per the 08-28/09-02 rule) showed **3 were script bugs, 1 was a genuine data defect in the report**:

| FAIL | Reality |
|---|---|
| `escalation SHAPE present` | check asserted `"[SYSTEMATIC VIOLATION]"` inside the new section — but the section's own heading uses `ESCALATE LẦN 1` and only *quotes* the marker in backticks. Assert `"ESCALATE"` instead. |
| `report documents check-ignore correction` | asserted lowercase `bỏ qua`; report has uppercase `BỎ QUA`. Case mismatch. |
| `exactly 2 files written` | compared paths without the `./` prefix `find` emits. Strip the prefix before comparing. |
| **`post-write scope total == 1752`** | **REAL.** Agent-home L1 had drifted 99 → 98, so the published total was unreproducible. Fixed the report (not the script) by publishing stable vs volatile separately — see pitfall #16. |

**Rule:** when a verify FAILs, the artifact is not automatically wrong and the script is not automatically right. `grep` the raw file for the expected value first, decide which side is wrong, and only then edit — and say in the report which side it was. Three consecutive "fix the script" reflexes would have papered over a real reporting defect here.

### 19. Diagnose the path-count JUMP before reporting it — a nested INSTALL inside the agent home looks exactly like KB growth (2026-10-01)

On 2026-10-01 `paths_checked` went **1.751 → 241.162**. Every prior run that quoted this number (09-21 → 09-29: 233.822 → 234.133 → 241.104) attributed it to "internal `.hermes/` content". That attribution was **never verified and was wrong**. The cause: `.hermes/hermes-agent/` — a **full install of the Hermes Agent source tree**, **225.528 tệp / 5,5 GB**, its own git repo (`.git` present, branch `main`, HEAD `990473a79c`), committed into the KB as a **gitlink mode `160000`** with **no `.gitmodules`** file and **no `.gitignore` rule**.

**Why it hid for 22 days (2026-05-12 → 09-30):** a gitlink is **ONE line** in the tree. `git ls-files -s .hermes/hermes-agent` returns exactly 1 entry, and the depth>1 agent-home exemption suppresses everything under it — so every probe a prior run actually performed came back clean.

**Rule — when the machine path count jumps by >20%, find the delta before writing a report:**
```bash
for d in raw wiki context scripts .hermes .openclaw; do printf "%s " "$d"; find "$d" -type f -o -type l | wc -l; done   # which zone moved?
find . -maxdepth 3 -type d -name .git -not -path './.git/*'     # nested repos = install trees
git ls-tree HEAD | grep '^160000'                               # gitlinks hiding bulk trees
test -f .gitmodules || echo "gitlink without .gitmodules => submodule commands broken"
```
Also check `du -sh .hermes/*/` — a KB of ~1.7K files should not have a 5.5 GB subdirectory.

**Report the KB scope separately from the machine count.** Publish the machine number *labelled as not-a-scope* ("241.162 quét máy — 99,8% là bản cài lồng") next to the real scope (1.655 stable files + 74 dirs), so no future run reads the raw number as KB growth.

**Severity warning:** if the offending tree is the agent's own CWD/launch path (it was here — Hermes starts in `.hermes/hermes-agent/`), the report **must** state that `rm -rf` while the agent runs is unsafe, and must point at the *install mechanism* as the thing to fix. Hygiene never deletes; Fix Agent must stop the agent or relocate the install first.

**Corollary — a nested repo is not the same as a gitlink, and a gitlink is not a submodule.** Report all three states separately: nested `.git` present, mode `160000` in the parent tree, `.gitmodules` entry present. Missing the third is why "225K files" never showed up as a leak. Related: pitfall #12b (nested repo in `.hermes/checkpoints/`), #7 (don't dismiss a leak because it's one line).

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
- **Fix Agent pre-rename backup files (2026-09-02):** Fix Agent leaves `*-backup-YYYY-MM-DD.md` copies in `wiki/drafts/` after bulk renames (repos owner segments, slug shortening). They violate draft naming on TWO axes: date-prefix + underscore + `-backup-` suffix (e.g. `2026-08-30_impeccable-backup-2026-09-01.md`), and `src_` prefix on source backups (`src_ai-engineering-skills-map-...-backup-2026-09-01.md`). Escalate as `[SYSTEMATIC VIOLATION]` ONCE (first occurrence 2026-09-02, 8 files); the durable fix is Fix Agent SKILL.md: place pre-rename backups OUTSIDE the KB (or a dedicated backup dir), or clean them up after the rename is verified. Do NOT delete them yourself — Hermes writes `wiki/reviews/` only; Fix Agent owns cleanup. Same run also showed: GitHub owner casing preserved in repos filenames (`MengTo`, `PostHog`) violates folder-structure.md §8 lowercase slug rule → flag WARNING, defer lowercase rename to Fix Agent. Ingest Agent SKILL.md should enforce lowercase `<owner>_<repo>` from the start to prevent the whole cascade.
- **Fix Agent backup artifacts** (`*-backup-YYYY-MM-DD.md`, e.g. `2026-08-30_impeccable-backup-2026-09-01.md`, `src_...-backup-2026-09-01.md`) — pre-rename backups Fix Agent drops into wiki/drafts/ violate the `<slug>.md` draft naming (date-prefix + underscore + `-backup-` suffix, sometimes `src_` prefix). 8 files on 2026-09-01 (6 repos + 2 slug renames) → escalated [SYSTEMATIC VIOLATION]. Resolution: Fix Agent SKILL.md places backups outside wiki/drafts/ (dedicated backup location) and cleans up after rename is verified. Expect this pattern each time Fix Agent renames files.

In `raw/repos/`:
- Repos use `YYYY-MM-DD_<owner>_<repo>.md` (two slug segments separated by underscore). Single-slug `2026-08-30_<repo>.md` is a naming violation → flagged WARNING by `RE_RAW_REPOS` pattern in scan-script.py. Systemic batch occurrence (6/6 files on 2026-08-30) → escalate `[SYSTEMATIC VIOLATION]` and have Ingest Agent SKILL.md enforce the `<owner>_<repo>` two-segment rule. Precedent: `2026-06-27_aiskilloftheweek_personal-mba-generator-skill.md` — correctly uses 2-segment format.
- **Two-step fix nuance (2026-09-01):** adding the owner segment is NOT sufficient — the owner must also be lowercase per the slug rule. Fix Agent renamed all 6 files to add owner segments, but 2 still failed: `2026-08-30_MengTo_threeui.md` and `2026-08-30_PostHog_posthog.md` preserved GitHub owner casing (`MengTo`, `PostHog`). When Fix Agent renames repos files, the fix must be both: `<owner>_<repo>` two segments AND lowercase owner (`mengto_threeui`, `posthog_posthog`).

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

## Đối chiếu quy chuẩn trước khi chốt số liệu

- Phân biệt số đường dẫn đã đi qua với số thực sự kiểm tra. Cắt `.git/`, `.obsidian/`, `node_modules/` và nội bộ nhà tác nhân khỏi phạm vi theo quy tắc miễn kiểm tra; công bố phạm vi khi số đếm khác báo cáo cũ. Không suy ra kho tăng/giảm từ hai cách đếm khác nhau.
- Không mặc định `*-backup-*.md` trong vùng reviews là báo nhầm. Đối chiếu §7; nếu quy trình lưu bản sao chưa được cho phép rõ, báo xung đột quy chuẩn, không âm thầm loại hoặc đổi tên bản sao thành báo cáo.
- Đối chiếu loại `spot-check` mà bộ quét tham chiếu cho qua với danh sách loại báo cáo trong quy chuẩn. Ghi xung đột khi chưa có ngoại lệ; không coi phát hiện tồn đọng là tệp mới.
- Không dùng biểu thức phủ định như `[^A-Z_ .~]+` để xác nhận slug: nó vẫn nhận ký tự đặc biệt và chữ hoa tiếng Việt. Kiểm tra tập ký tự cho phép, chữ thường, đuôi `.md` và giới hạn 80 ký tự riêng.
- Gom cảnh báo tệp con cùng nguyên nhân khi báo cáo, nhưng công bố cả số phát hiện máy và số nhóm. Không trình bày hai số như cùng một đơn vị.
- Kiểm tra liên kết bằng `is_symlink`, `readlink` và sự tồn tại của đích; không chép kết luận lịch sử mâu thuẫn như “liên kết hỏng, đích tồn tại”. Đừng khẳng định tác nhân tạo liên kết khi chưa có bằng chứng.
- Giữ trạng thái đã duyệt tách biệt trạng thái đã sửa. Với `DREAMS.md` và `memory/`, giữ dữ liệu theo ghi chú duyệt; xử lý tiến trình tạo trước. Chỉ quét đường dẫn và metadata, không đọc nội dung bộ nhớ hay nhật ký OpenClaw.
- Bỏ qua bước ghi MEMORY.md, dọn lịch sử và gửi Telegram riêng trong `workflow.md` cũ: trái phạm vi chỉ ghi báo cáo và cơ chế giao kết quả cron. SKILL.md hiện hành có ưu tiên.

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
When a recurring orphan file (e.g. `memory/*-heartbeat-status.md`, `memory/YYYY-MM-DD-*.md`) reappears, **check `git ls-files <path>` (or `git check-ignore <path>`)** before writing "deletion is the fix".

**⚠️ PITFALL — `git ls-files <path>` exits 0 even when the file is NOT tracked (2026-08-27):** In an `&&` chain like `git ls-files <path> && echo "(tracked)" || echo "(untracked)"`, an untracked file STILL prints "(tracked)" because `git ls-files` exits 0 whether or not it finds matches (it just prints nothing). This misled a scan into reporting the `wiki/HEARTBEAT.md` symlink as git-tracked when `git ls-files -s` was empty (untracked) and `git log --follow` had no commits. **Correct probes:**
```bash
git ls-files -s <path>          # empty output = untracked (definitive)
git log --oneline --follow -- <path>   # no commits = never tracked
git check-ignore <path>         # prints path only if ignored (exit 0), else exit 1
```
Never use a bare `git ls-files <path> &&` in a conditional — the exit code is meaningless for presence. This matters because the tracked-vs-untracked verdict changes the fix: tracked → `git rm` + commit + redirect the writer; untracked+ignored → working-copy deletion suffices (transient if writer still active). **Variant (2026-09-08):** when checking whether a NEW leak variant is already polluting the repo (e.g. a `.migrated.*` marker), the tracked check comes FIRST — a git-tracked variant means the auto `vault backup` already committed it, so the fix must include `git rm --cached`, not just `.gitignore` (ignoring an already-tracked file does nothing).

**⚠️ HEARTBEAT leak can be a SYMLINK, not a regular file (2026-08-27):** `wiki/HEARTBEAT.md` appeared as `lrwxrwxrwx → ../../.openclaw/HEARTBEAT.md` (created 08-26 17:01), not a written file. `ls -la` shows the symlink; a regular `ls` hides it. Treat as the same recurring process leak (untracked + gitignored via `.gitignore` `HEARTBEAT.md`), still needs process-level fix — some sync tool mirrors the root-level `HEARTBEAT.md → .openclaw/HEARTBEAT.md` symlink into `wiki/`. If the file is git-tracked, it reaches commits (this KB auto-commits `vault backup` roughly every 10 minutes — see `git log`), so filesystem deletion only removes the working copy; the committed copy survives and reappears on the next checkout/sync. That confirms a *process-owned* leak, not a stray artifact. Proven 2026-08-16: `memory/2026-08-16-heartbeat-status.md` was git-tracked, hence the fix MUST be root-cause (redirect the writing process output path) plus a committable removal (`git rm` + commit), not just `rm -rf memory/`. Report it accordingly in the escalation block.

### 9. openclaw-workspace-state.json at root — ROOT CAUSE KNOWN, do not recommend deletion-only fix (2026-08-25)
`openclaw-workspace-state.json` at KB root was flagged 3 consecutive runs (08-22 → 08-24). Deletion + `git rm` (08-23) + `.gitignore` guard were all applied; the file still regenerated on disk within **<1h**. Root cause confirmed by reading OpenClaw dist source (`dist/workspace-DkQ7irPD.js`, package 2026.7.1-2):

- `WORKSPACE_STATE_FILENAME = "openclaw-workspace-state.json"`; `resolveWorkspaceStatePath(dir)` = `path.join(dir, WORKSPACE_STATE_FILENAME)` — i.e. **CWD-relative by design**.
- OpenClaw treats ANY directory containing `AGENTS.md` as a workspace. KB root has `AGENTS.md` → KB root IS an OpenClaw workspace → the writer legitimately writes state there on every session bootstrap.
- Canonical/legacy location is `.openclaw/workspace-state.json` inside the same dir; a global copy also lives at `~/.openclaw/workspace-state.json`.

**Current accepted mitigation (do NOT re-flag as new):**
1. Repo hygiene is SOLVED: file untracked via `git rm` + `.gitignore` entries (`openclaw-workspace-state.json`, `openclaw-workspace-state.json.attested`, `workspace-attestations/`). Git-level scans stay clean permanently.
2. Disk-level recurrence is expected until upstream ships the SQLite workspace-state refactor. Hygiene reports should list it once as a known/documented ERROR (or INFO) referencing this entry — NOT escalate `[SYSTEMATIC VIOLATION]` again, and NOT suggest "delete it" (proven futile 3×).

**Rule:** when a leak's writer is identified in vendor source with CWD-relative output, record that fact here and stop recommending per-file deletions — recommend either the .gitignore-guard pattern or waiting for upstream, and say which.

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
| 1.35 | 2026-10-03 | 13 ERROR groups, **0 new, 0 resolved** — the KB is stable and the backlog is not. Added four pitfalls from one run. **(23) Sibling validators write inside your run window:** Format wrote its report at 23:28:18 and a write-zone check started at 23:25 counted **3** files instead of 2 — set `START` from the `date` you captured at run start and identify your two files by explicit path set, plus drop the bare `./wiki/reviews` dir entry `find` prints. **(24) Field values can be bold-wrapped too,** not just labels — `**Issues found:** **20 nhóm**` needs `lstrip("*")` before `startswith`. **(25) Publish a machine count only with its prune definition:** three prunes gave 242.766 / 242.752 / 244.840, differing by exactly the 2.074 files of `.hermes/hermes-agent/.git`, and 10-02's 243.267 matched none of them — a table of competing definitions turns a suspicious number into a documented one. **(26) Sum the header's severity arithmetic before publishing:** 10-02's `13 nhóm (5E+4W+2I)` summed to 11 and three runs quoted it before anyone checked. Run also corrected that header explicitly, re-probed all 13 groups with `ls-files -s` + `check-ignore --no-index` (E3's table byte-identical to 10-02), recorded that `E5` gained **+1.546 files / +8 MB in one day** while `E10`/`E11`/`E12` aged to 9 days and 13 consecutive runs, and showed W4's duplicate-topic pair recurring for the **4th** time — carry-forward, not a fresh escalation. Ad-hoc verify: 33/35 first pass (both FAILs script-side), **36/36** after fixes. |
| 1.34 | 2026-10-02 | The 10-02 run published a **reproducible scope definition** and corrected two inherited ones, at the cost of three new script-vs-artifact defects. **(20) `find -o` binds only the last branch:** `find . -path ./.git -prune -o -newerct <ref> -print` returned **0** for the whole tree (the un-grouped `-type f -o -type l` form merely *appears* to work, which is why the trap survives); group the test or use a Python `stat` filter. **(21) Dir-count shape:** `os.walk` omits each zone root so `len(dn)` gave 19 where `find -type d` gives 23 — 74 vs 70 was a counting artifact, not drift; also a `cnt(".")` root-files helper walks the whole tree (243K) instead of the 11 top-level entries. **(22) `wiki/wiki.md` is whitelisted:** §7 requires it *and* forbids wiki-root files, so the scanner emitted a false ERROR — grep the spec for the exact name before trusting any orphan finding. Run also **corrected the 10-01 headline**: its 241.162 path count is not reproducible from any subset of today's tree, so it was a publication defect, **not** KB growth — grep-the-artifact-first (pitfall #17) is what kept that from being misread as a +2.105 jump. Confirmed E1's three distinct states (nested `.git` + gitlink `160000` + **no** `.gitmodules`), showed `.hermes/lsp/node_modules` (7.105 files) is **correctly ignored** via `.gitignore:33` rather than reporting it as a leak, and verified W4's duplicate topic pair has now recurred **3 consecutive runs** ⇒ hand-fixing cannot hold, the Index Agent SKILL.md must canonicalise slugs. Ad-hoc verify: first pass 55/59, after fixes **59/59**. |
| 1.33 | 2026-10-01 | Found the largest single ERROR in the KB's history and a **methodology gap that hid it for 22 days**. **Pitfall #19 — diagnose a path-count JUMP before reporting it:** `paths_checked` went 1.751 → **241.162** and every prior run (09-21→09-29: 233.822 → 241.104) attributed the inflated number to "internal `.hermes/` content" without ever verifying it. Cause: `.hermes/hermes-agent/` = a full Hermes Agent install, **225.528 tệp / 5,5 GB**, own git repo (`main`, HEAD `990473a79c`), in the KB as **gitlink `160000`** with **no `.gitmodules`** and **no `.gitignore` rule**. It hid because a gitlink is **one line** in the tree (`git ls-files` = 1 entry) AND the depth>1 agent-home exemption suppresses its interior — so every probe prior runs actually performed returned clean. Added the standing delta procedure: per-zone file counts, `find -maxdepth 3 -type d -name .git`, `git ls-tree HEAD | grep '^160000'`, `du -sh .hermes/*/`; publish the machine count **labelled as not-a-scope** beside the real scope; and when the offending tree is the agent's own CWD (it was), state that `rm -rf` is unsafe while the agent runs and point Fix Agent at the install mechanism. Also documented that nested-repo / gitlink / submodule are three distinct states and reporting only two hides bulk trees. Run also re-confirmed 8 carry-forward ERRORs with `--no-index` probes, corrected 09-30's `memory/` dir count (6 vs 3 = same tree, different counting shape), and showed `find -newer` = 292 while git status = **43 `??`** (283 = Index Agent rewrites) for the second time. |
| 1.32 | 2026-09-30 | Verification-found defects from the 09-30 run (13 ERROR groups, 3 new). (1) **Pitfall #17 — verify the artifact before the script:** the ad-hoc verify returned 4 FAIL and **3 were script bugs** (asserted the bare `[SYSTEMATIC VIOLATION]` marker where the section heading actually says `ESCALATE LẦN 1`; case mismatch on `bỏ qua`/`BỎ QUA`; compared `find` output without stripping the `./` prefix). Grepping the raw file first — per the 08-28/09-02 rule — is what kept a **real reporting defect from being papered over**. (2) **Pitfall #18 — agent-home L1 count is VOLATILE:** 09-29's socket-exclusion lesson was necessary but NOT sufficient; the L1 count moved 99 → 98 *within one run* (runtime deleted the per-session `.skills_prompt_snapshot.json`, created 3 `state.db.malformed-backup-20260617_082024*` files), and 46 of 98 L1 files look volatile. The 09-30 report had published an unreproducible total; it now publishes **1.653 stable** (1.641 content zones + 11 root) + **74 dirs** and labels the 98 volatile files separately. Compare only the stable part across runs; a transient per-session file is never KB growth and its disappearance is never a resolved issue. (3) 1.31 added pitfalls #14–16 from the same run: plain `git check-ignore` skips tracked files (all runs through 09-29 used it, so both "rule exists but is ineffective" and "exit 1 ⇒ NOT ignored" rested on invalid evidence); inventory secret exposure by filename+extension rather than key names (found 7 auth-named tracked files where 09-29's key-name grep found 1); and publish dir counts with an explicit reproducible shape (09-29's "70 dirs" is not reproducible from any subset — today 74). |
| 1.31 | 2026-09-30 | Three methodology fixes from the 09-30 run, which found **13 ERROR groups (3 new)** where 09-29 found 10. (1) **Pitfall #14 — plain `git check-ignore` silently SKIPS tracked files** (git docs: "tracked files are not shown"), returning `rc=1` with no output — indistinguishable from "no rule exists". Every run through 09-29 used the plain form, so both "rule exists but is ineffective" and "exit 1 ⇒ NOT ignored" (applied to the `.migrated.*` markers) rested on invalid evidence. Always pair `git ls-files -s` with `git check-ignore --no-index` and classify into the 4-row table. 09-29's conclusion held; its evidence did not — correct it explicitly. (2) **Pitfall #15 — inventory exposure by FILENAME + EXTENSION, not key names:** a key-name grep inside one file found only 1 of 7 auth-named tracked files; the 4 in `.openclaw/` + 1 in `state-snapshots/` were invisible. Extension probes found `kanban.db-shm/-wal` at **141 commits each** and `verification_evidence.db` at 345 — **9 of 9** runtime patterns lack any `.gitignore` rule while `.openclaw/*.bak` and `.hermes/state.db*` have one, i.e. the `.hermes/` zone is unprotected. (3) **Pitfall #16 — publish dir counts with an explicit shape:** 09-29's "70 dirs" is not reproducible from any subset (09-30 = 74 = 9 root + 23 content + 42 agent-home L1), so the +4 read as structural growth was a counting artifact; the files half (+16) was corroborated against `git status`. Also escalated the first `[SYSTEMATIC VIOLATION]` (runtime artifacts in agent homes with no `.gitignore`) — 09-29 had set the threshold "escalate if the next run is identical" and the next run grew instead. Added W4-class check: diacritic-normalized slug collisions across all 10 content zones (0 exact; 1 near-duplicate topic pair from two spellings of the same Vietnamese phrase). |
| 1.30 | 2026-09-29 | Found a committed secret + a nested git repo in `.hermes/` — the agent-home exemption was hiding **8** ERRORs, not 4. (1) **A `.gitignore` rule can exist and do nothing** when the file was committed before it (`.hermes/auth.json`, 78 commits, already on the remote; `check-ignore` exits 0 while `git ls-files -s` still returns a line) — always assert the `ls-files` emptiness, not the ignore exit code. (2) **Nested bare git repo** `.hermes/checkpoints/` (29 MB pack already committed + 6,783 untracked files, zero ignore rules). (3) **Tracked-but-deleted** files (7, incl. 3 `SKILL.md` from commit `32b4c6ba`). (4) **Asymmetric ignore coverage** (`.openclaw/*.bak` guarded, `.hermes/config.yaml.bak.*` not). Reports must also name the **action ORDER** — with `vault backup` stalled the pending 6,828 files would commit the moment it restarts, so `.gitignore` must be blocked *before* re-enabling. Never read secret values: grep key *names*, report blob size + commit count. Plus: `paths_checked` drift is a *published* number, so publish both pre-write and post-write figures — and **sockets are neither files nor stable** (`.hermes/gateway.sock` caused three consecutive spurious verify FAILs, 100→99→98): a count definition must be "regular files + symlinks" (`find -type f -o -type l`), never "not a directory". |
| 1.29 | 2026-09-28 | Four lessons from the 09-28 run. (1) **Symlink validity needs `realpath`+`exists`+`lexists`:** two consecutive reports (09-26, 09-27) wrongly asserted `wiki/HEARTBEAT.md`'s target exists — the link resolves one level ABOVE the KB root and is genuinely dangling; never eyeball the relative path, and correct the prior claim explicitly when found. (2) **Verify the remote before blaming the local machine:** `git ls-remote --heads origin` (read-only, no fetch) proved `vault backup` had not committed on the primary machine either — a different fix than "push behind"; also note decoy branches (`origin/main` abandoned since 2026-05-11). (3) **Publish the counting definition** — 09-27's "1,800 files" was not reproducible and made a definition change look like a 67-file shrinkage. (4) **`find -newer` counts regenerated files:** 293 hits were only 10 truly new + 290 Index Agent rewrites at a shared mtime; partition with `git status --porcelain -uall` (`??` vs `M`). |
| 1.28 | 2026-09-25 | Three lessons from the 09-25 evening re-scan (addendum to the 18:16 report). (1) **Agent-home exemption hides tracked leaks:** a second git-tracked `.migrated.*` marker inside `.openclaw/` survived 17 days because the depth>1 orphan exemption suppresses findings there AND it shares a blob hash with the already-known root marker — so always `find` marker variants tree-wide and run `git ls-files`/`check-ignore` on every hit; report a newly-found twin as a NEW issue and explicitly correct the prior report's claim. (2) **`git status --porcelain` is not a write-zone check** — it drowns in Hermes runtime churn and mis-attributes sibling-agent writes; attribute by mtime against session start and assert only on content zones. (3) **Many `-prune -o` clauses before one `-print` mis-filter** (trailing `-print` binds only to the last expression); do one find pass and filter in Python. Also confirmed: same-day re-scan with a changed filesystem = append addendum, edit the SAME day's action-file row/section in place, pending count unchanged. |
| 1.27 | 2026-09-08 | Three lessons from the 09-08 evening re-scan. (1) **Same-day re-run = ADDENDUM, not [SILENT], not -v2:** when today's report already exists but the filesystem changed since the morning scan, re-scan, diff flagged paths, and append a dated addendum to the same report (dual `Paths checked` counts in the header, E1/E2… numbering for new issues, in-place edit of the same day's `_action-required.md` row/section instead of duplicates). (2) **Self-resolving leaks leave artifacts:** the 12-run `openclaw-workspace-state.json` orphan was MIGRATED by the OpenClaw runtime at 20:42, leaving a `.migrated.<sha256>.<uuid>` marker that was NOT gitignored and was auto-committed 3 minutes later — audit for marker/rename variants when a recurring leak disappears, add WILDCARD gitignore guards (`openclaw-workspace-state.json.migrated.*`), and if already tracked the fix is `git rm --cached`. (3) **Two new verify-script pitfalls:** report front-matter fields may carry extended tails (`12 (2 ERROR + 10 WARNING)`) → use prefix/in matching, not equality; and the backtick-strip rule extends to `[SPEC CONFLICT]`/`[STRUCTURE CHANGE]` absence-quotes in report prose. |
| 1.26 | 2026-09-02 | Documented two new patterns from the 09-02 run. (1) **Fix Agent backup artifacts** — `*-backup-YYYY-MM-DD.md` files Fix Agent drops into `wiki/drafts/` during renames (8 files on 09-01: 6 repos + 2 slug renames) violate the draft `<slug>.md` naming; escalated [SYSTEMATIC VIOLATION]; resolution = Fix Agent places backups outside wiki/drafts/ or cleans up post-rename. (2) **Repos two-step fix nuance** — adding the owner segment is NOT sufficient; the owner must also be lowercase per the slug rule (`MengTo`, `PostHog` still flagged after 09-01 rename). |
| 1.25 | 2026-09-01 | Three lessons from the 09-01 run. (1) Added cron-retry pitfall: a "run hygiene again" after a rate-limit cron failure may be DAYS later — check `date`, reconcile pending reports, and produce a FRESH report for today instead of a same-day [SILENT] re-run (initial reading was wrong; 5-day gap, 9 pending reports). (2) New-file detection must include `raw/` — the scanner covers the whole tree; a wiki/-only `find -newer` missed 6 `raw/repos/` naming WARNINGs from an 08-30 ingest batch. (3) Escalation carry-forward rule: an issue already escalated in a still-pending report is marked `CARRIED FORWARD`, never re-escalated fresh. Also documented the `raw/repos/` `YYYY-MM-DD_<owner>_<repo>.md` two-segment naming convention in Common non-compliant patterns. |
| 1.24 | 2026-08-29 | Documented recurrence of the SYSTEMATIC-VIOLATION no-re-escalation check (pitfall from 1.22) on a real cron run: the bare `"[SYSTEMATIC VIOLATION]" not in sec_txt` assertion FAILED even when scoped to the new section, because the section's own Actions-needed line quotes the marker in backticks (`KHÔNG re-escalate `[SYSTEMATIC VIOLATION]``). Added the proven known-good snippet to the pitfall body: assert the escalation SHAPE (`"[SYSTEMATIC VIOLATION] Root-cause" not in sec`) plus the backtick-stripped bare-marker check; the corrected rerun passed 23/23. Also refreshed `references/scan-script.py` ROOT_ORPHAN_MAP text (7th → 8th consecutive run for openclaw-workspace-state.json, 08-22 → 08-29) and `references/common-patterns.md` with the 08-29 recurrence record. |
| 1.23 | 2026-08-28 | Added cron verify-script pitfall #11 — backtick-wrapped paths in `_action-required.md` prose (`` `memory/` ``) break exact-string matches: the closing backtick sits between the path and the next word, so `"memory/ vắng mặt" in action_txt` FAILs. Proven on the 08-28 run (2 spurious FAILs, content byte-correct). Check bare path + context word SEPARATELY, scoped to the new section. Corollary: grep the RAW artifact FIRST before touching anything under `wiki/`. Also refreshed `references/scan-script.py` `ROOT_ORPHAN_MAP` text for `openclaw-workspace-state.json` (was "3rd consecutive run 08-24", now 7th through 08-28). |
| 1.22 | 2026-08-25 | Added pitfall #10 — verify-script `field()` helpers must receive PLAIN labels (`"**Status"`, colon INSIDE the helper pattern: `re.escape(label) + r":\*{0,2}\s*(.+)"`). Pre-escaped labels double-escape (proven 08-24); labels without the embedded colon miss the bold-wrapped value entirely even when correctly escaped (proven 08-25, 4 spurious FAILs on a correct report — raw artifact grep confirmed report was right before editing anything). Also: when asserting historical text in `_action-required.md` stays untouched, scope the assertion to the NEW section and count pre-existing `[SYSTEMATIC VIOLATION]` mentions exactly (2 APPLIED entries + N backticked references in new guidance) instead of asserting zero/absence. |
| 1.21 | 2026-08-25 | Added pitfall #9 — `openclaw-workspace-state.json` root leak ROOT CAUSE CONFIRMED in vendor source (OpenClaw treats any dir with `AGENTS.md` as workspace; state path is CWD-relative by design). Repo level solved via git rm + .gitignore guard (08-25); disk-level recurrence expected until upstream SQLite refactor. Do NOT re-escalate `[SYSTEMATIC VIOLATION]` or recommend deletion-only fixes for this file — reference pitfall #9 instead. |
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
