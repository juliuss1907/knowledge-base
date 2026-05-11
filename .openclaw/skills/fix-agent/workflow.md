# Fix Agent — Complete Workflow

Detailed step-by-step process for applying Hermes validation report fixes.

---

## Overview

This workflow reads approved reports from `_action-required.md`, applies fixes, and updates the action file:
- **Input:** Approved reports listed in `wiki/reviews/_action-required.md`
- **Output:** Fixed wiki files + archived reports + updated `_action-required.md`
- **Side effect:** Telegram notification to Julius

Total time: 10-90 seconds depending on issue count and fix complexity.

---

## Trigger Flow (Complete Picture)

### Friday 18:00 — Hermes Validation

```
1. Hermes runs 3 validators (Output, Format, Hygiene)
   ↓
2. Hermes writes 3 report files:
   - wiki/reviews/2026-05-09_format-report.md
   - wiki/reviews/2026-05-09_hygiene-report.md
   - wiki/reviews/2026-05-09_output-report.md
   ↓
3. Hermes updates wiki/reviews/_action-required.md:
   - Add 3 entries to "Pending Reports" section
   - Update "Last updated" timestamp
   ↓
4. Hermes sends Telegram notification:
   "📋 Validation complete: 3 new reports
    Total pending: 3 reports
    Review: wiki/reviews/_action-required.md
    
    Commands:
    - 'approve format' to approve format report
    - 'approve all' to approve all reports
    - 'show format' for details"
```

### Julius Review (anytime after Friday 18:00)

```
Option 1 — Review in Obsidian:
1. Julius opens wiki/reviews/_action-required.md
2. Reads report summaries
3. Clicks links to detailed reports if needed
4. Decides: approve or reject

Option 2 — Review via Telegram:
1. Julius receives notification
2. Replies "show format" to see details
3. Decides: approve or reject
```

### Julius Approve (via Telegram)

```
Julius: "approve format"
  ↓
Hermes:
1. Finds report: wiki/reviews/2026-05-09_format-report.md
2. Updates report file: status: pending → approved
3. Updates _action-required.md: change status in entry
4. Replies: "✓ Format report approved. Run 'openclaw apply fixes' to apply."
```

### Julius Trigger Fix Agent

```
Julius: "openclaw apply fixes"
  ↓
Fix Agent starts (this workflow)
```

---

## Step 1: Read _action-required.md

### 1.1 Load action file

```bash
cat wiki/reviews/_action-required.md
```

### 1.2 Parse pending reports

**Find "Pending Reports" section:**
```markdown
## Pending Reports (3)

### 1. Format Validation — 2026-05-09
**File:** [2026-05-09_format-report.md](2026-05-09_format-report.md)
**Status:** approved    ← Look for this
**Issues:** 8 (5 ERROR, 2 WARNING, 1 INFO)
...

### 2. Hygiene Validation — 2026-05-09
**Status:** pending     ← Skip this (not approved)
...

### 3. Output Validation — 2026-05-09
**Status:** approved    ← Include this
...
```

**Extract approved reports:**
```python
approved_reports = []
for entry in pending_reports:
    if entry['status'] == 'approved':
        approved_reports.append({
            'type': entry['type'],  # Format, Hygiene, Output
            'date': entry['date'],
            'file': entry['file'],
            'issues': entry['issues'],
            'files_affected': entry['files_affected']
        })
```

**Result:**
```python
approved_reports = [
    {
        'type': 'Format Validation',
        'date': '2026-05-09',
        'file': '2026-05-09_format-report.md',
        'issues': 8,
        'files_affected': 4
    },
    {
        'type': 'Output Validation',
        'date': '2026-05-09',
        'file': '2026-05-09_output-report.md',
        'issues': 3,
        'files_affected': 2
    }
]
```

### 1.3 Check if any approved reports found

```python
if len(approved_reports) == 0:
    send_telegram("No approved reports to apply. Use 'approve <type>' first.")
    exit(0)
```

---

## Step 2: Load Report Files

For each approved report:

### 2.1 Read report file

```bash
report_file="wiki/reviews/${report['file']}"
cat "$report_file"
```

### 2.2 Verify report status

```bash
# Double-check status in report file
status=$(grep "^**Status:**" "$report_file" | awk '{print $2}')

if [ "$status" != "approved" ]; then
    echo "[WARNING] Report status mismatch: _action-required.md says approved, but report file says $status"
    echo "Skipping this report"
    continue
fi
```

### 2.3 Parse issues from report

Same as old workflow — extract issues, group by file.

---

## Step 3: Confirm with Julius

### 3.1 Generate summary

```
[FIX SUMMARY]
Found 2 approved reports:

1. Format Validation (2026-05-09)
   - Issues: 8 (5 ERROR, 2 WARNING, 1 INFO)
   - Files: 4
   - Fixes: add missing fields, fix YAML, reorder sections

2. Output Validation (2026-05-09)
   - Issues: 3 (2 WARNING, 1 INFO)
   - Files: 2
   - Fixes: expand summaries, add key points

Total: 11 issues across 6 files

Proceed with fixes? (yes/no)
```

### 3.2 Wait for confirmation

**If Julius says "yes":**
- Proceed to Step 4

**If Julius says "no":**
- Stop, do not apply fixes
- Log: `[FIX CANCELLED] User declined at confirmation step`
- Exit

**If Julius says "show details":**
- Display full issue list for each report
- Ask again: "Proceed? (yes/no)"

---

## Step 4: Apply Fixes

Same as old workflow — apply format/hygiene/output fixes per issue type.

(No changes to this section, already detailed in old workflow.md)

---

## Step 5: Verify Fixes

Same as old workflow — re-validate frontmatter, check sections, verify locations.

(No changes to this section)

---

## Step 6: Update Report Files

For each applied report:

### 6.1 Mark report as applied

```bash
# Update status
sed -i 's/^**Status:** approved/**Status:** applied/' "$report_file"

# Add applied timestamp
sed -i '/^**Status:** applied/a **Applied at:** '$(date '+%Y-%m-%d %H:%M:%S') "$report_file"
sed -i '/^**Applied at:/a **Applied by:** fix-agent' "$report_file"
```

### 6.2 Add fix summary to report

Append to end of report:

```markdown
---

## Fix Summary

**Applied:** 2026-05-09 21:30:45
**Files modified:** 4
**Backups created:** 4

### Files fixed:
- wiki/concepts/example-1.md — 3 issues resolved
- wiki/sources/src_example-2.md — 2 issues resolved
- wiki/concepts/example-3.md — 2 issues resolved
- wiki/sources/src_example-4.md — 1 issue resolved

### Verification:
- All fixes applied successfully
- All files validated
- No errors
```

---

## Step 7: Archive Reports

For each applied report:

### 7.1 Create archive folder

```bash
# Get report date
report_date=$(basename "$report_file" | cut -d_ -f1)
year_month=$(echo "$report_date" | cut -d- -f1,2)

# Create archive folder if not exists
mkdir -p "wiki/reviews/archive/${year_month}"
```

### 7.2 Move report to archive

```bash
# Move report
mv "$report_file" "wiki/reviews/archive/${year_month}/"

# Verify moved
test -f "wiki/reviews/archive/${year_month}/$(basename $report_file)" && \
    echo "✓ Report archived"
```

---

## Step 8: Update _action-required.md

This is the **critical new step** that replaces simple "remove from list" logic.

### 8.1 Read current _action-required.md

```bash
action_file="wiki/reviews/_action-required.md"
content=$(cat "$action_file")
```

### 8.2 Remove applied reports from "Pending Reports"

For each applied report:

```python
# Find and remove the entry
# Entry format:
# ### N. [Type] — YYYY-MM-DD
# **File:** [filename](filename)
# **Status:** applied
# ...
# ---

# Remove from "## Pending Reports" section
content = remove_report_entry(content, report_date, report_type)
```

### 8.3 Add to "Recently Applied" section

```python
# Build new entry for "Recently Applied"
new_entry = f"""
### {report_date} {report_type}
**Applied:** {applied_timestamp}
**Issues fixed:** {issues_count}
**Files modified:** {files_count}
**Report:** [archive/{year_month}/{report_filename}](archive/{year_month}/{report_filename})
"""

# Insert at top of "Recently Applied" section
content = insert_into_recently_applied(content, new_entry)
```

### 8.4 Update counts and timestamp

```python
# Count remaining pending reports
pending_count = count_pending_reports(content)

# Update section header
content = content.replace(
    "## Pending Reports (N)",
    f"## Pending Reports ({pending_count})"
)

# Update "Last updated" timestamp
content = content.replace(
    "Last updated: YYYY-MM-DD HH:MM:SS",
    f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
)
```

### 8.5 Handle "no pending reports" case

```python
if pending_count == 0:
    # Replace "Pending Reports" section with message
    content = replace_section(
        content,
        "## Pending Reports",
        """## Pending Reports (0)

No pending validation reports.

All issues have been resolved or are in progress.
"""
    )
```

### 8.6 Write updated _action-required.md

```bash
cat > "$action_file" << 'EOF'
$content
EOF
```

### 8.7 Verify update

```bash
# Check file updated
grep -q "Last updated: $(date '+%Y-%m-%d')" "$action_file" && \
    echo "✓ _action-required.md updated"

# Check applied report in "Recently Applied"
grep -q "${report_date} ${report_type}" "$action_file" && \
    echo "✓ Report added to Recently Applied"
```

---

## Step 9: Send Telegram Notification

### 9.1 Build notification message

```python
message = f"""✓ Fixes applied successfully

Reports processed: {len(applied_reports)}
"""

for report in applied_reports:
    message += f"""
- {report['type']} ({report['date']})
  Issues fixed: {report['issues']}
  Files modified: {report['files_affected']}
"""

message += f"""
Total issues fixed: {total_issues}
Total files modified: {total_files}
Backups created: {total_backups}

Updated: wiki/reviews/_action-required.md
"""
```

### 9.2 Send to Telegram

```python
send_telegram(message)
```

**Example notification:**
```
✓ Fixes applied successfully

Reports processed: 2

- Format Validation (2026-05-09)
  Issues fixed: 8
  Files modified: 4

- Output Validation (2026-05-09)
  Issues fixed: 3
  Files modified: 2

Total issues fixed: 11
Total files modified: 6
Backups created: 6

Updated: wiki/reviews/_action-required.md
```

---

## Step 10: Log to Memory

### 10.1 Append to MEMORY.md

```markdown
## 2026-05-09 21:30:45 — Applied fixes

- **Reports:** 2 (format, output)
- **Issues fixed:** 11
- **Files modified:** [wiki/concepts/example-1.md, wiki/sources/src_example-2.md, ...]
- **Backups created:** 6
- **Archived to:** wiki/reviews/archive/2026-05/
- **Updated:** wiki/reviews/_action-required.md
```

---

## Batch Processing

When applying multiple approved reports:

### Sequential processing

```bash
for report in "${approved_reports[@]}"; do
    apply_fixes "$report"
    
    # Verify before continuing
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to apply $report, stopping batch"
        break
    fi
    
    sleep 1  # Brief pause between reports
done

# Update _action-required.md once at the end
update_action_required_file "$applied_reports"
```

**Important:** Update `_action-required.md` **once** after all reports applied, not per report. This avoids multiple file rewrites.

---

## Error Handling

### No approved reports found

```
[INFO] No approved reports to apply
Action: Send Telegram: "No approved reports found. Use 'approve <type>' to approve reports first."
```

### Report file not found

```
[ERROR] Report file not found: wiki/reviews/2026-05-09_format-report.md
Action: Skip this report, log error, continue with others
```

### Status mismatch

```
[WARNING] Status mismatch
_action-required.md says: approved
Report file says: pending
Action: Skip this report, alert Julius
```

### Fix verification failed

```
[ERROR] Verification failed for wiki/concepts/example.md
Issue: Frontmatter still invalid after fix
Action: Restore from backup, alert Julius, stop batch
```

### _action-required.md update failed

```
[FATAL ERROR] Cannot update wiki/reviews/_action-required.md
Issue: Permission denied or disk full
Action: Fixes were applied but action file not updated. Alert Julius immediately.
```

→ This is critical — fixes are applied but Julius won't know. Manual intervention required.

---

## Validation Checklist

Before marking fixes complete:

- [ ] All issues in reports addressed
- [ ] All modified files verified
- [ ] All backups created
- [ ] All report files updated to "applied"
- [ ] All reports archived to correct folders
- [ ] **_action-required.md updated correctly:**
  - [ ] Applied reports removed from "Pending Reports"
  - [ ] Applied reports added to "Recently Applied"
  - [ ] Pending count updated
  - [ ] Timestamp updated
- [ ] Telegram notification sent
- [ ] MEMORY.md entry added
- [ ] No files written outside allowed zones

---

## Performance Benchmarks

Typical fix times by report type:

| Report type | Issues | Files | Time |
|---|---|---|---|
| Format | 5-10 | 3-5 | 10-30s |
| Hygiene | 3-5 | 2-4 | 15-45s |
| Output | 2-3 | 2-3 | 30-90s |

**Additional overhead (new):**
- Reading `_action-required.md`: +1s
- Updating `_action-required.md`: +2-3s
- Telegram notification: +1s

**Total overhead:** ~4-5s per batch (not per report)

---

## _action-required.md Update Logic (Detailed)

### Structure of _action-required.md

```markdown
# Action Required

Last updated: YYYY-MM-DD HH:MM:SS

---

## Pending Reports (N)

### 1. [Type] — YYYY-MM-DD
[entry content]
---

### 2. [Type] — YYYY-MM-DD
[entry content]
---

## Recently Applied (last 7 days)

### YYYY-MM-DD [Type]
[entry content]

### YYYY-MM-DD [Type]
[entry content]

---

## Quick Actions
[commands]
```

### Removal logic

```python
def remove_report_entry(content, report_date, report_type):
    # Find entry by date and type
    pattern = f"### \\d+\\. {report_type} — {report_date}.*?---"
    
    # Remove entry (including separator)
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Renumber remaining entries
    content = renumber_pending_entries(content)
    
    return content
```

### Addition logic

```python
def insert_into_recently_applied(content, new_entry):
    # Find "## Recently Applied" section
    section_start = content.find("## Recently Applied")
    
    # Find insertion point (after section header and blank line)
    insert_pos = content.find("\n\n", section_start) + 2
    
    # Insert new entry
    content = content[:insert_pos] + new_entry + "\n" + content[insert_pos:]
    
    return content
```

### Cleanup old entries (7-day rule)

```python
def cleanup_old_recently_applied(content):
    # Find all entries in "Recently Applied"
    entries = parse_recently_applied_entries(content)
    
    # Remove entries older than 7 days
    cutoff_date = datetime.now() - timedelta(days=7)
    
    for entry in entries:
        if entry['date'] < cutoff_date:
            content = remove_recently_applied_entry(content, entry)
    
    return content
```

→ This cleanup runs **every time** Fix Agent updates `_action-required.md`.

---

## Related Documentation

- [SKILL.md](SKILL.md) — Fix Agent overview
- [examples.md](examples.md) — sample fixes for each report type
- [reference.md](reference.md) — report format specification
- `wiki/meta/format-spec.md` — format ground truth
- `wiki/meta/folder-structure.md` — hygiene ground truth
