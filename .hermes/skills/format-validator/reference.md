# Fix Agent — Report Format & Fix Pattern Reference

Complete specification for Hermes report formats and fix patterns.

---

## Overview

This document defines:
- Hermes report file format
- `_action-required.md` format
- Fix patterns for each issue type
- Verification criteria
- Backup and restore procedures

---

## Hermes Report File Format

### File naming

**Pattern:** `wiki/reviews/YYYY-MM-DD_<type>-report.md`

**Types:**
- `format-report.md` — Format Validator output
- `hygiene-report.md` — Hygiene Inspector output
- `output-report.md` — Output Validator output

**Examples:**
- `wiki/reviews/2026-05-09_format-report.md`
- `wiki/reviews/2026-05-09_hygiene-report.md`
- `wiki/reviews/2026-05-09_output-report.md`

### File structure

```markdown
# [Report Type] — YYYY-MM-DD

**Status:** pending | approved | rejected | applied

**Issues found:** N

**Created:** YYYY-MM-DD HH:MM:SS

**Validator:** [output-validator | format-validator | hygiene-inspector]

---

## Issue 1: [Issue type]

**File:** wiki/<path>/<file>.md
**Severity:** ERROR | WARNING | INFO
**Issue:** <description>
**Suggested fix:** <action to take>

---

## Issue 2: [Issue type]

[...]

---

## Fix Summary

(Added by Fix Agent after applying fixes)

**Applied:** YYYY-MM-DD HH:MM:SS
**Files modified:** N
**Backups created:** M

### Files fixed:
- file1.md — X issues resolved
- file2.md — Y issues resolved

### Verification:
- All fixes applied successfully
- All files validated
- No errors
```

### Status field values

| Status | Meaning | Set by |
|---|---|---|
| `pending` | Awaiting Julius review | Hermes (initial) |
| `approved` | Julius approved, ready to apply | Hermes (after Telegram approval) |
| `rejected` | Julius rejected, will not apply | Hermes (after Telegram rejection) |
| `applied` | Fixes applied and archived | Fix Agent (after applying) |

### Severity levels

| Severity | Meaning | Action required |
|---|---|---|
| `ERROR` | Must fix (breaks format/structure) | High priority |
| `WARNING` | Should fix (suboptimal but valid) | Medium priority |
| `INFO` | Nice to fix (suggestions) | Low priority |

---

## _action-required.md Format

### File location

**Path:** `wiki/reviews/_action-required.md`

**Uniqueness:** Single file, always updated (no multiple `_action-required-*` files)

### File structure

```markdown
# Action Required

Last updated: YYYY-MM-DD HH:MM:SS

---

## Pending Reports (N)

### 1. [Report Type] — YYYY-MM-DD

**File:** [YYYY-MM-DD_<type>-report.md](YYYY-MM-DD_<type>-report.md)
**Status:** pending | approved
**Created:** YYYY-MM-DD HH:MM:SS
**Issues:** N (X ERROR, Y WARNING, Z INFO)
**Files affected:** M

**Summary:**
- Brief description of issues
- Key files affected

**Actions:**
- `approve <type>` — approve this report
- `reject <type>` — reject this report
- `show <type>` — show full report details

---

### 2. [Report Type] — YYYY-MM-DD

[...]

---

## Recently Applied (last 7 days)

### YYYY-MM-DD [Report Type]
**Applied:** YYYY-MM-DD HH:MM:SS
**Issues fixed:** N
**Files modified:** M
**Report:** [archive/YYYY-MM/YYYY-MM-DD_<type>-report.md](archive/YYYY-MM/YYYY-MM-DD_<type>-report.md)

### YYYY-MM-DD [Report Type]
[...]

---

## Quick Actions

- `approve all` — approve all pending reports
- `reject all` — reject all pending reports
- `show all` — show details of all reports
- `openclaw apply fixes` — apply all approved fixes (via Fix Agent)

---

## Statistics

- **Total reports this month:** N
- **Applied:** X
- **Pending:** Y
- **Rejected:** Z
- **Average resolution time:** D.D days
```

### Section rules

**Pending Reports:**
- Numbered sequentially (1, 2, 3, ...)
- Sorted by date (oldest first)
- Only includes reports with `status: pending` or `status: approved`
- Renumbered after each removal

**Recently Applied:**
- Not numbered
- Sorted by applied date (newest first)
- Kept for 7 days, then removed
- Links to archived reports

**Statistics:**
- Updated by Hermes weekly
- Reflects current month only

---

## Fix Patterns by Issue Type

### Format Issues

#### Missing frontmatter field

**Pattern:**
```python
# Read frontmatter
frontmatter = parse_yaml(file)

# Add missing field with default value
defaults = {
    'last_updated': datetime.now().strftime('%Y-%m-%d'),
    'status': 'draft',
    'sources': []
}

frontmatter[missing_field] = defaults.get(missing_field, '[to be filled]')

# Write back
write_yaml(frontmatter)
```

**Default values:**
- `last_updated` → current date
- `status` → `draft`
- `sources` → empty array `[]`
- Other fields → `[to be filled]` (requires manual input)

#### Incorrect field order

**Pattern:**
```python
# Standard order for source files
source_order = [
    'type', 'original', 'main_tag', 'sub_tags', 'topic',
    'date_ingested', 'date_compiled', 'url', 'author'
]

# Standard order for concept files
concept_order = [
    'type', 'status', 'main_tag', 'sub_tags', 'topic',
    'sources', 'last_updated'
]

# Reorder
ordered = {key: frontmatter[key] for key in order if key in frontmatter}
write_yaml(ordered)
```

#### Invalid YAML syntax

**Common issues and fixes:**

| Issue | Fix |
|---|---|
| Unescaped colon | Quote value: `"text: with colon"` |
| Unescaped hash | Quote value: `"#hashtag"` |
| Unescaped brackets | Quote value: `"[brackets]"` |
| Missing quotes around string | Add quotes: `"value"` |
| Wrong array syntax | Use `[item1, item2]` not `item1, item2` |

**Pattern:**
```python
# Detect special chars
special_chars = [':', '#', '[', ']', '{', '}', '|', '>', '<']

for field, value in frontmatter.items():
    if isinstance(value, str):
        if any(char in value for char in special_chars):
            if not (value.startswith('"') and value.endswith('"')):
                frontmatter[field] = f'"{value}"'
```

#### Missing required section

**Pattern:**
```python
# Section templates
templates = {
    'Definition': '\n## Definition\n\n[To be filled]\n',
    'Key ideas': '\n## Key ideas\n\n- [To be filled]\n',
    'Related concepts': '\n## Related concepts\n\n(empty)\n',
    'Sources': '\n## Sources\n\n(auto-maintained)\n',
    'Notes': '\n## Notes\n\n(empty)\n'
}

# Find insertion point (after title)
title_line = find_line_number(file, r'^# ')

# Insert section
insert_at_line(file, title_line + 1, templates[missing_section])
```

#### Section order incorrect

**Pattern:**
```python
# Parse sections
sections = parse_markdown_sections(file)

# Standard order for concept files
order = ['title', 'definition', 'key_ideas', 'related_concepts', 'sources', 'notes']

# Reorder
ordered_sections = [sections[key] for key in order if key in sections]

# Reconstruct file
content = frontmatter + '\n\n' + '\n\n'.join(ordered_sections)
write_file(file, content)
```

---

### Hygiene Issues

#### File in wrong folder

**Pattern:**
```python
# Determine correct folder from type
folder_map = {
    'source': 'wiki/sources/',
    'concept': 'wiki/concepts/'
}

file_type = frontmatter['type']
correct_folder = folder_map[file_type]

# Check current location
if not file.startswith(correct_folder):
    # Backup
    backup(file)
    
    # Move
    new_path = correct_folder + basename(file)
    move(file, new_path)
    
    # Update references (wikilinks don't include path, so no update needed)
```

#### Incorrect filename format

**Pattern:**
```python
# Generate correct filename
def sanitize_filename(name):
    # Lowercase
    name = name.lower()
    
    # Replace spaces and underscores with hyphens
    name = name.replace(' ', '-').replace('_', '-')
    
    # Remove special chars
    name = re.sub(r'[^a-z0-9-]', '', name)
    
    # Collapse multiple hyphens
    name = re.sub(r'-+', '-', name)
    
    # Strip leading/trailing hyphens
    name = name.strip('-')
    
    return name

# For source files, add src_ prefix
if file_type == 'source' and not name.startswith('src_'):
    name = 'src_' + name

# Backup
backup(file)

# Rename
new_name = sanitize_filename(basename(file))
rename(file, new_name)

# Update wikilinks
update_wikilinks(old_name, new_name)
```

#### Orphaned file

**Pattern:**
```python
# Check references
slug = basename(file).replace('.md', '')
refs = grep_recursive(f'[[{slug}]]', 'wiki/')

if len(refs) == 0:
    # No references found
    # Move to drafts with reason suffix
    backup(file)
    move(file, f'wiki/drafts/{slug}-orphaned-{date}.md')
    
    log(f"[ORPHAN] {file} moved to drafts (no references)")
```

#### Duplicate file

**Pattern:**
```python
# Find duplicates by content similarity
def find_duplicates(file):
    content = read_file(file)
    slug = basename(file).replace('.md', '')
    
    # Search for similar files
    similar = []
    for other in glob('wiki/**/*.md'):
        if other == file:
            continue
        
        other_content = read_file(other)
        similarity = calculate_similarity(content, other_content)
        
        if similarity > 0.8:  # 80% similar
            similar.append((other, similarity))
    
    return similar

# If duplicates found
if duplicates:
    # Move all to drafts
    for dup in duplicates + [file]:
        backup(dup)
        move(dup, f'wiki/drafts/{basename(dup)}-needs-merge.md')
    
    # Create merge note
    create_merge_note(duplicates + [file])
```

---

### Output Issues

#### Summary too short

**Pattern:**
```python
# Read current summary
current = extract_section(file, '## Summary')

# Count sentences
sentence_count = len(re.split(r'[.!?]+', current))

if sentence_count < 3:
    # Expand using LLM
    full_content = read_file(file)
    
    prompt = f"""
Expand this summary to 3-5 sentences while keeping the same language:

Current summary (too short):
{current}

Full content for context:
{full_content}

Output only the expanded summary, no explanation.
"""
    
    expanded = llm_call(prompt, model='claude-3-5-sonnet')
    
    # Replace summary section
    replace_section(file, '## Summary', expanded)
```

#### Insufficient key points

**Pattern:**
```python
# Read current key points
current = extract_section(file, '## Key points')
current_count = len(re.findall(r'^- ', current, re.MULTILINE))

if current_count < 5:
    # Add more using LLM
    full_content = read_file(file)
    
    prompt = f"""
Add {5 - current_count} to {10 - current_count} more key points to this list:

Current key points:
{current}

Full content:
{full_content}

Output only the additional bullet points (starting with -), no explanation.
"""
    
    additional = llm_call(prompt, model='claude-3-5-sonnet')
    
    # Append to key points section
    append_to_section(file, '## Key points', additional)
```

#### Definition unclear

**Pattern:**
```python
# Read current definition
current = extract_section(file, '## Definition')

# Check clarity (heuristics)
issues = []
if len(current) < 100:
    issues.append('too short')
if count_jargon(current) > 5:
    issues.append('too technical')
if not has_clear_structure(current):
    issues.append('lacks structure')

if issues:
    # Rewrite using LLM
    full_content = read_file(file)
    
    prompt = f"""
Rewrite this definition to be clearer and more accessible:

Current definition (issues: {', '.join(issues)}):
{current}

Full concept content for context:
{full_content}

Output only the improved definition (2-3 sentences), no explanation.
"""
    
    improved = llm_call(prompt, model='claude-3-5-sonnet')
    
    # Replace definition section
    replace_section(file, '## Definition', improved)
```

#### Sources not cited

**Pattern:**
```python
# This requires manual review — cannot auto-determine which source supports which claim

# Move to drafts with note
backup(file)
move(file, f'wiki/drafts/{basename(file)}-needs-citations.md')

# Create note
note = f"""
# Citation Needed

File: {file}

Issue: Key ideas mention facts but don't cite sources.

Action required:
1. Review key ideas section
2. Add source citations in format: (Source: [[src_name]])
3. Move back to wiki/concepts/ when done
"""

write_file(f'wiki/drafts/_citation-needed-{basename(file)}.md', note)

log(f"[MANUAL REVIEW] {file} needs source citations")
```

---

## Verification Criteria

### Frontmatter validation

```python
def verify_frontmatter(file):
    # Extract frontmatter
    frontmatter = parse_yaml(file)
    
    # Check YAML valid
    try:
        yaml.safe_load(frontmatter)
    except yaml.YAMLError:
        return False, "Invalid YAML syntax"
    
    # Check required fields
    file_type = frontmatter.get('type')
    
    required_fields = {
        'source': ['type', 'original', 'main_tag', 'sub_tags', 'topic', 
                   'date_ingested', 'date_compiled'],
        'concept': ['type', 'status', 'main_tag', 'sub_tags', 'topic', 
                    'sources', 'last_updated']
    }
    
    for field in required_fields[file_type]:
        if field not in frontmatter:
            return False, f"Missing required field: {field}"
    
    # Check field types
    if not isinstance(frontmatter['sub_tags'], list):
        return False, "sub_tags must be an array"
    
    if len(frontmatter['sub_tags']) < 1 or len(frontmatter['sub_tags']) > 3:
        return False, "sub_tags must have 1-3 items"
    
    return True, "Valid"
```

### Section validation

```python
def verify_sections(file):
    sections = parse_markdown_sections(file)
    file_type = frontmatter['type']
    
    required_sections = {
        'source': ['Metadata', 'Summary', 'Key points', 'Concepts referenced'],
        'concept': ['Definition', 'Key ideas', 'Related concepts', 'Sources']
    }
    
    for section in required_sections[file_type]:
        if section not in sections:
            return False, f"Missing required section: {section}"
    
    # Check section order
    order = {
        'concept': ['Definition', 'Key ideas', 'Related concepts', 'Sources', 'Notes']
    }
    
    if file_type in order:
        actual_order = [s for s in order[file_type] if s in sections]
        expected_order = [s for s in order[file_type] if s in sections]
        
        if actual_order != expected_order:
            return False, f"Section order incorrect"
    
    return True, "Valid"
```

### Location validation

```python
def verify_location(file):
    file_type = frontmatter['type']
    
    expected_folder = {
        'source': 'wiki/sources/',
        'concept': 'wiki/concepts/'
    }
    
    if not file.startswith(expected_folder[file_type]):
        return False, f"File should be in {expected_folder[file_type]}"
    
    return True, "Valid"
```

---

## Backup and Restore Procedures

### Backup creation

```python
def create_backup(file):
    # Generate backup filename
    slug = basename(file).replace('.md', '')
    date = datetime.now().strftime('%Y-%m-%d')
    backup_file = f'wiki/drafts/{slug}-backup-{date}.md'
    
    # Copy file
    shutil.copy2(file, backup_file)
    
    # Verify backup
    if not os.path.exists(backup_file):
        raise Exception(f"Backup creation failed: {backup_file}")
    
    # Log
    log(f"[BACKUP] {file} → {backup_file}")
    
    return backup_file
```

### Restore from backup

```python
def restore_from_backup(file, backup_file):
    # Verify backup exists
    if not os.path.exists(backup_file):
        raise Exception(f"Backup not found: {backup_file}")
    
    # Restore
    shutil.copy2(backup_file, file)
    
    # Verify restore
    if not os.path.exists(file):
        raise Exception(f"Restore failed: {file}")
    
    # Log
    log(f"[RESTORE] {backup_file} → {file}")
    
    return True
```

### Backup retention

**Rules:**
- Backups kept in `wiki/drafts/` indefinitely
- Julius manually reviews and deletes old backups
- Naming convention: `<slug>-backup-YYYY-MM-DD.md`
- Multiple backups per file allowed (different dates)

---

## Error Codes

| Code | Meaning | Action |
|---|---|---|
| `FIX_001` | Report file not found | Skip report, alert Julius |
| `FIX_002` | Report status not approved | Skip report, log warning |
| `FIX_003` | File mentioned in report not found | Skip fix, log warning, continue |
| `FIX_004` | Backup creation failed | Stop, alert Julius |
| `FIX_005` | Fix verification failed | Restore backup, alert Julius |
| `FIX_006` | Restore from backup failed | Critical error, alert Julius |
| `FIX_007` | _action-required.md update failed | Fixes applied but action file not updated, alert Julius |
| `FIX_008` | Disk full | Stop immediately, alert Julius |
| `FIX_009` | Permission denied | Stop, alert Julius |
| `FIX_010` | LLM call failed (output fixes) | Skip output fix, flag for manual review |

---

## Related Documentation

- [SKILL.md](SKILL.md) — Fix Agent overview
- [workflow.md](workflow.md) — Step-by-step fix process
- [examples.md](examples.md) — Sample fixes for each report type
- `wiki/meta/format-spec.md` — Format ground truth
- `wiki/meta/folder-structure.md` — Hygiene ground truth
