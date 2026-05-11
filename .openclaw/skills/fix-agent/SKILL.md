---
name: fix-agent
description: Applies approved fixes from Hermes validation reports. Use when user says "apply fixes", "fix report issues", "apply [report-name]", or after Julius approves a Hermes report. Reads wiki/reviews/ reports, applies corrections to wiki files (format fixes, hygiene cleanup, content improvements), then marks report as applied. Does NOT auto-fix without approval.
when_to_use: After Julius reviews Hermes reports and approves fixes. On-demand only, never runs automatically. Triggered by explicit user command with report filename or "apply all approved".
disable-model-invocation: false
user-invocable: true
allowed-tools: Read Write Edit Grep Bash(date *)
---

# Fix Agent

Applies approved corrections from Hermes validation reports to wiki files.

## Role

Read Hermes reports from `wiki/reviews/`, apply approved fixes to wiki files:
- **Format fixes** — correct frontmatter, section order, naming
- **Hygiene fixes** — move misplaced files, clean up structure
- **Content fixes** — improve quality based on Output Validator feedback

Then mark report as applied and archive it.

## When to use

- After Julius reviews `wiki/reviews/_action-required.md` and approves fixes
- On-demand: "apply fixes from [report-name]", "fix format issues", "apply all approved"
- Never runs automatically — always requires explicit user command

## Quick start

1. **Read report** — load specified report from `wiki/reviews/`
2. **Parse issues** — extract file paths, issue types, suggested fixes
3. **Confirm with Julius** — show summary, ask for approval
4. **Apply fixes** — edit files according to report
5. **Verify** — check all fixes applied correctly
6. **Mark report applied** — update report status
7. **Archive report** — move to `wiki/reviews/archive/YYYY-MM/`
8. **Log** to `.openclaw/MEMORY.md`

## Critical rules

### Approval required
- **Never** apply fixes without Julius's explicit approval
- **Always** show summary before applying
- **Stop** if Julius says no or if uncertain

### Report types
Fix Agent handles 3 types of Hermes reports:
1. **Format reports** — frontmatter, sections, naming issues
2. **Hygiene reports** — folder structure, misplaced files
3. **Output reports** — content quality issues

### Read-only zones
- **Never** modify `wiki/meta/format-spec.md` or `wiki/meta/folder-structure.md`
- **Never** modify `TAGS.md` or `AGENTS.md`
- **Never** modify raw files (except status updates by Compile Agent)

### Preserve user content
- **Always** preserve `## Notes` sections in concept files (Julius's annotations)
- **Never** delete content without explicit approval
- **Backup** before destructive operations (move to `wiki/drafts/`)

## Report format

Hermes reports follow this structure:

```markdown
# [Report Type] — YYYY-MM-DD

**Status:** pending | approved | rejected | applied

**Issues found:** N

---

## Issue 1: [Issue type]

**File:** wiki/<path>/<file>.md
**Severity:** ERROR | WARNING | INFO
**Issue:** <description>
**Suggested fix:** <action to take>

## Issue 2: [Issue type]

...
```

## Fix types

### Format fixes

**Common issues:**
- Missing required frontmatter fields
- Incorrect field order
- Invalid YAML syntax
- Missing required sections
- Section order incorrect

**Actions:**
- Add missing fields with default values
- Reorder frontmatter fields
- Fix YAML syntax (quote values, escape colons)
- Add missing sections
- Reorder sections per format-spec.md

### Hygiene fixes

**Common issues:**
- File in wrong folder
- Incorrect filename format
- Orphaned files (no references)
- Duplicate files

**Actions:**
- Move file to correct folder
- Rename file to match convention
- Move orphans to `wiki/drafts/` for review
- Flag duplicates for Julius to resolve

### Output fixes

**Common issues:**
- Summary too short or missing
- Key points insufficient
- Definition unclear
- Sources not cited

**Actions:**
- Expand summary (requires LLM call)
- Add more key points
- Clarify definition
- Add source citations

## Constraints

### Write zones
- **Allowed:** `wiki/sources/`, `wiki/concepts/`, `wiki/drafts/`
- **Allowed (move):** Files within allowed zones
- **Forbidden:** `wiki/tag/`, `wiki/topic/`, `wiki/reviews/`, `wiki/meta/`, `raw/`

### Forbidden actions
- ❌ Applying fixes without approval
- ❌ Deleting files (move to drafts instead)
- ❌ Modifying ground truth files (format-spec.md, folder-structure.md, TAGS.md)
- ❌ Auto-fixing Output Validator issues without LLM review
- ❌ Changing tags without checking TAGS.md

### Backup strategy
Before destructive operations:
1. Copy original file to `wiki/drafts/<filename>-backup-YYYY-MM-DD.md`
2. Apply fix
3. Verify
4. If verification fails → restore from backup

## Escalation

Ask Julius when:

### Ambiguous fix
```
[FIX CLARIFICATION]
Report: wiki/reviews/YYYY-MM-DD_format-report.md
Issue: File wiki/concepts/unclear.md has invalid main_tag
Suggested fix: Change to #ai or #tech
Question: Which tag is more appropriate for this content?
```

### Destructive operation
```
[DESTRUCTIVE FIX]
Report: wiki/reviews/YYYY-MM-DD_hygiene-report.md
Issue: File wiki/sources/orphan.md has no references
Suggested fix: Delete file
Confirm: Move to drafts or delete permanently? (move/delete)
```

### Conflicting fixes
```
[CONFLICT]
Report 1: Says move file to wiki/concepts/
Report 2: Says file format is invalid, move to drafts
Question: Which report takes precedence?
```

## Details

For complete fix application logic, backup procedures, and error handling, see:
- [workflow.md](workflow.md) — step-by-step fix process
- [examples.md](examples.md) — sample fixes for each report type
- [reference.md](reference.md) — report format specification

## Post-fix

After successful fix application:

1. **Verify all fixes applied:**
   ```bash
   # Check each file mentioned in report
   for file in $fixed_files; do
       verify_fix "$file"
   done
   ```

2. **Update report status:**
   ```yaml
   status: applied
   applied_at: YYYY-MM-DD HH:MM:SS
   applied_by: fix-agent
   ```

3. **Archive report:**
   ```bash
   # Move to archive folder
   mv wiki/reviews/YYYY-MM-DD_<type>-report.md \
      wiki/reviews/archive/YYYY-MM/YYYY-MM-DD_<type>-report.md
   ```

4. **Update _action-required.md:**
   - Remove applied report from list
   - If no pending reports remain, clear file

5. **Log to MEMORY.md:**
   ```markdown
   ## YYYY-MM-DD HH:MM:SS — Applied fixes
   - Report: wiki/reviews/YYYY-MM-DD_<type>-report.md
   - Issues fixed: N
   - Files modified: [<file1>, <file2>, ...]
   - Backups created: M
   ```

## Batch behavior

When applying multiple reports:
- Process **sequentially** (avoid conflicts)
- After each report, verify before proceeding
- On error: stop batch, log error, alert Julius
- Final summary: count applied, count failed

## Failure modes

| Issue | Action |
|---|---|
| Report file not found | Alert Julius, skip |
| Report status not "approved" | Alert Julius, do not apply |
| File mentioned in report not found | Log warning, skip that fix, continue |
| Fix verification fails | Restore from backup, alert Julius |
| Disk full | Stop, alert Julius |
| Permission denied | Stop, alert Julius |

## Performance benchmarks

Typical fix times:

| Report type | Issues | Time |
|---|---|---|
| Format | 5-10 issues | 10-30s |
| Hygiene | 3-5 issues | 15-45s |
| Output | 2-3 issues | 30-90s (LLM calls) |

**Bottlenecks:**
- Output fixes (require LLM calls)
- File moves (I/O)
- Verification (re-reading files)
