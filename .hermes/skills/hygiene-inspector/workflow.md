# Hygiene Inspector — Complete Workflow

Detailed step-by-step process for validating folder structure compliance on daily 23:00 runs.

---

## Overview

This workflow validates entire knowledge base folder structure against `wiki/meta/folder-structure.md`:
- **Input:** All paths in knowledge base + ground truth `wiki/meta/folder-structure.md`
- **Output:** Hygiene report in `wiki/reviews/YYYY-MM-DD_hygiene-report.md`
- **Side effect:** Update `wiki/reviews/_action-required.md`, send Telegram notification

Total time: 5-15 seconds for daily runs (fast directory scan)

---

## Step 1: Load Ground Truth

### 1.1 Read folder-structure.md

```bash
folder_spec_file="wiki/meta/folder-structure.md"

if [ ! -f "$folder_spec_file" ]; then
    echo "[FATAL ERROR] folder-structure.md not found"
    send_telegram("[FATAL] Hygiene validation failed: folder-structure.md missing")
    exit 1
fi

folder_spec=$(cat "$folder_spec_file")
```

**Validation:**
- File must exist
- File must be readable
- File must be valid markdown

**If missing:**
→ Fatal error, cannot validate without ground truth

### 1.2 Parse folder rules

Extract validation rules from folder-structure.md:

```python
def parse_folder_spec(content):
    """Extract folder structure rules from folder-structure.md."""

    rules = {
        'root_whitelist': [],
        'depth1_whitelist': {},
        'naming_rules': {},
        'forbidden_patterns': [],
        'ignored_paths': []
    }

    # Parse root level whitelist
    root_section = extract_section(content, "Root level")
    rules['root_whitelist'] = parse_allowed_paths(root_section)

    # Parse depth 1 whitelist (subfolders)
    for folder in ['raw', 'wiki', '.openclaw', '.hermes', 'context']:
        section = extract_section(content, f"{folder}/")
        rules['depth1_whitelist'][folder] = parse_allowed_subfolders(section)

    # Parse naming conventions
    naming_section = extract_section(content, "Naming conventions")
    rules['naming_rules'] = parse_naming_rules(naming_section)

    # Parse forbidden patterns
    forbidden_section = extract_section(content, "Forbidden patterns")
    rules['forbidden_patterns'] = parse_forbidden_patterns(forbidden_section)

    # Parse ignored paths (gitignored)
    rules['ignored_paths'] = ['.git', 'node_modules', '.obsidian', '.DS_Store']

    return rules
```

**Cached in memory:**
- Folder rules loaded once per validation run
- Reused for all paths

---

## Step 2: Scan Knowledge Base

### 2.1 Walk directory tree

```python
import os

def scan_kb(root_path):
    """Walk entire KB directory tree."""
    
    all_paths = []
    
    for dirpath, dirnames, filenames in os.walk(root_path):
        # Filter out ignored paths
        dirnames[:] = [d for d in dirnames if not should_ignore(d)]
        
        # Add directory paths
        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            rel_path = os.path.relpath(full_path, root_path)
            all_paths.append({
                'path': rel_path,
                'type': 'directory',
                'depth': rel_path.count(os.sep)
            })
        
        # Add file paths
        for filename in filenames:
            if should_ignore(filename):
                continue
            
            full_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(full_path, root_path)
            all_paths.append({
                'path': rel_path,
                'type': 'file',
                'depth': rel_path.count(os.sep)
            })
    
    return all_paths
```

**Ignored paths:**
```python
def should_ignore(name):
    """Check if path should be ignored."""
    ignored = [
        '.git',
        'node_modules',
        '.obsidian',
        '.DS_Store',
        '*.tmp',
        '*.bak',
        '*.swp',
        '__pycache__'
    ]
    
    for pattern in ignored:
        if fnmatch.fnmatch(name, pattern):
            return True
    
    return False
```

### 2.2 Build path list

```python
paths = scan_kb('.')

# Sort by depth (root first, then deeper)
paths.sort(key=lambda x: x['depth'])

# Group by depth for validation
paths_by_depth = {
    0: [p for p in paths if p['depth'] == 0],  # Root level
    1: [p for p in paths if p['depth'] == 1],  # Depth 1
    2: [p for p in paths if p['depth'] >= 2]   # Depth 2+
}
```

---

## Step 3: Validate Each Path

For each path:

```python
issues = []

# Check 1: Path whitelist
issues += validate_path_whitelist(path, folder_rules)

# Check 2: Naming conventions
issues += validate_naming(path, folder_rules)

# Check 3: Orphan detection
issues += validate_orphans(path, folder_rules)
```

---

## Step 4: Validate Path Whitelist

### 4.1 Check root level paths

```python
def validate_path_whitelist(path, rules):
    issues = []
    
    if path['depth'] == 0:
        # Root level - check against whitelist
        if path['path'] not in rules['root_whitelist']:
            # Check if temporary folder
            if path['path'].startswith('.tmp-'):
                issues.append({
                    'path': path['path'],
                    'severity': 'WARNING',
                    'category': 'Path',
                    'issue': 'Temporary folder at root (should be deleted when done)',
                    'current': path['path'],
                    'expected': 'Temporary folders should use .tmp- prefix and be deleted',
                    'suggested_fix': 'Delete when testing complete or promote to permanent'
                })
            else:
                issues.append({
                    'path': path['path'],
                    'severity': 'ERROR',
                    'category': 'Path',
                    'issue': 'Path not in root whitelist',
                    'current': path['path'],
                    'expected': 'Only allowed: ' + ', '.join(rules['root_whitelist']),
                    'suggested_fix': 'Remove path or add to folder-structure.md whitelist'
                })
    
    return issues
```

### 4.2 Check depth 1 paths

```python
if path['depth'] == 1:
    # Depth 1 - check against parent folder whitelist
    parent = path['path'].split(os.sep)[0]
    subfolder = path['path'].split(os.sep)[1]
    
    if parent in rules['depth1_whitelist']:
        allowed_subfolders = rules['depth1_whitelist'][parent]
        
        if subfolder not in allowed_subfolders:
            issues.append({
                'path': path['path'],
                'severity': 'ERROR',
                'category': 'Path',
                'issue': f'Subfolder not allowed in {parent}/',
                'current': subfolder,
                'expected': 'Only allowed: ' + ', '.join(allowed_subfolders),
                'suggested_fix': f'Remove {path["path"]} or add to folder-structure.md'
            })
```

### 4.3 Check depth 2+ paths

```python
if path['depth'] >= 2:
    # Depth 2+ - check against parent rules
    parent_path = os.path.dirname(path['path'])
    
    # Check if parent path is allowed
    if not is_path_allowed(parent_path, rules):
        issues.append({
            'path': path['path'],
            'severity': 'ERROR',
            'category': 'Path',
            'issue': 'Path in forbidden location',
            'current': path['path'],
            'expected': 'Path should be in allowed folder',
            'suggested_fix': f'Move to correct location or remove'
        })
```

### 4.4 Check forbidden patterns

```python
for pattern in rules['forbidden_patterns']:
    if fnmatch.fnmatch(path['path'], pattern):
        issues.append({
            'path': path['path'],
            'severity': 'ERROR',
            'category': 'Path',
            'issue': f'Path matches forbidden pattern: {pattern}',
            'current': path['path'],
            'expected': 'Path should not match forbidden patterns',
            'suggested_fix': 'Remove or rename path'
        })
```

---

## Step 5: Validate Naming Conventions

### 5.1 Check folder naming

```python
def validate_naming(path, rules):
    issues = []
    
    if path['type'] == 'directory':
        folder_name = os.path.basename(path['path'])
        
        # Exception: agent homes can use dots
        if folder_name in ['.openclaw', '.hermes', '.git', '.obsidian']:
            return issues
        
        # Exception: temporary folders
        if folder_name.startswith('.tmp-'):
            return issues
        
        # Check lowercase-hyphen format
        if not re.match(r'^[a-z0-9-]+$', folder_name):
            issues.append({
                'path': path['path'],
                'severity': 'WARNING',
                'category': 'Naming',
                'issue': 'Folder name does not follow lowercase-hyphen format',
                'current': folder_name,
                'expected': 'lowercase-hyphen-format',
                'suggested_fix': 'Rename to lowercase with hyphens only'
            })
    
    return issues
```

### 5.2 Check file naming

```python
if path['type'] == 'file':
    filename = os.path.basename(path['path'])
    parent_folder = os.path.dirname(path['path'])
    
    # Check based on location
    if parent_folder.startswith('wiki/sources'):
        # Source files must have src_ prefix
        if not filename.startswith('src_'):
            issues.append({
                'path': path['path'],
                'severity': 'ERROR',
                'category': 'Naming',
                'issue': 'Source file missing src_ prefix',
                'current': filename,
                'expected': 'src_<slug>.md',
                'suggested_fix': f'Rename to src_{filename}'
            })
    
    elif parent_folder.startswith('wiki/concepts'):
        # Concept files must be lowercase-hyphen
        slug = filename.replace('.md', '')
        if not re.match(r'^[a-z0-9-]+$', slug):
            issues.append({
                'path': path['path'],
                'severity': 'ERROR',
                'category': 'Naming',
                'issue': 'Concept filename does not follow format',
                'current': filename,
                'expected': '<slug>.md (lowercase-hyphen)',
                'suggested_fix': 'Rename to lowercase-hyphen format'
            })
```

### 5.3 Check for spaces and special characters

```python
if ' ' in path['path']:
    issues.append({
        'path': path['path'],
        'severity': 'ERROR',
        'category': 'Naming',
        'issue': 'Path contains spaces',
        'current': path['path'],
        'expected': 'Use hyphens instead of spaces',
        'suggested_fix': 'Rename path to remove spaces'
    })

if '_' in os.path.basename(path['path']) and not path['path'].startswith('wiki/sources/src_'):
    issues.append({
        'path': path['path'],
        'severity': 'WARNING',
        'category': 'Naming',
        'issue': 'Path contains underscores',
        'current': path['path'],
        'expected': 'Use hyphens instead of underscores',
        'suggested_fix': 'Rename path to use hyphens'
    })
```

---

## Step 6: Validate Orphans

### 6.1 Check for empty folders

```python
def validate_orphans(path, rules):
    issues = []
    
    if path['type'] == 'directory':
        full_path = path['path']
        
        # Check if folder is empty
        if is_empty_folder(full_path):
            issues.append({
                'path': path['path'],
                'severity': 'INFO',
                'category': 'Orphan',
                'issue': 'Empty folder detected',
                'current': 'Folder contains no files',
                'expected': 'Folders should contain files or be removed',
                'suggested_fix': 'Remove empty folder or add files'
            })
    
    return issues
```

### 6.2 Check for misplaced files

```python
if path['type'] == 'file':
    filename = os.path.basename(path['path'])
    parent_folder = os.path.dirname(path['path'])
    
    # Source files should be in wiki/sources/
    if filename.startswith('src_') and not parent_folder.startswith('wiki/sources'):
        issues.append({
            'path': path['path'],
            'severity': 'ERROR',
            'category': 'Orphan',
            'issue': 'Source file in wrong location',
            'current': path['path'],
            'expected': 'wiki/sources/src_<slug>.md',
            'suggested_fix': f'Move to wiki/sources/{filename}'
        })
    
    # Concept files should be in wiki/concepts/
    if parent_folder.startswith('wiki/') and not parent_folder.startswith('wiki/sources') \
       and not parent_folder.startswith('wiki/concepts') \
       and not parent_folder.startswith('wiki/meta') \
       and not parent_folder.startswith('wiki/reviews') \
       and not parent_folder.startswith('wiki/tag') \
       and not parent_folder.startswith('wiki/topic') \
       and not parent_folder.startswith('wiki/drafts'):
        issues.append({
            'path': path['path'],
            'severity': 'ERROR',
            'category': 'Orphan',
            'issue': 'File in unexpected wiki/ subfolder',
            'current': path['path'],
            'expected': 'Files should be in designated wiki/ subfolders',
            'suggested_fix': 'Move to correct subfolder or remove'
        })
```

### 6.3 Check for temporary files

```python
temp_extensions = ['.tmp', '.bak', '.swp', '~']

for ext in temp_extensions:
    if path['path'].endswith(ext):
        issues.append({
            'path': path['path'],
            'severity': 'WARNING',
            'category': 'Orphan',
            'issue': 'Temporary file detected',
            'current': path['path'],
            'expected': 'Temporary files should be cleaned up',
            'suggested_fix': 'Delete temporary file'
        })
```

### 6.4 Check for old review reports

```python
if path['path'].startswith('wiki/reviews/') and path['path'].endswith('-report.md'):
    # Extract date from filename
    match = re.match(r'wiki/reviews/(\d{4}-\d{2}-\d{2})_.*-report\.md', path['path'])
    
    if match:
        report_date = datetime.strptime(match.group(1), '%Y-%m-%d')
        age_days = (datetime.now() - report_date).days
        
        if age_days > 30:
            issues.append({
                'path': path['path'],
                'severity': 'INFO',
                'category': 'Orphan',
                'issue': f'Old review report ({age_days} days old)',
                'current': path['path'],
                'expected': 'Reports older than 30 days should be archived',
                'suggested_fix': f'Move to wiki/reviews/archive/{report_date.strftime("%Y-%m")}/'
            })
```

---

## Step 7: Score and Filter Issues

### 7.1 Assign severity scores

```python
severity_scores = {'ERROR': 3, 'WARNING': 2, 'INFO': 1}

for issue in all_issues:
    issue['score'] = severity_scores[issue['severity']]
```

### 7.2 Sort issues

```python
all_issues.sort(key=lambda x: (-x['score'], x['category'], x['path']))
```

### 7.3 Apply report limit

```python
max_issues = 20  # Daily validation limit

if len(all_issues) > max_issues:
    reported_issues = all_issues[:max_issues]
    log(f"[TRUNCATED] {len(all_issues) - max_issues} issues not included in report")
else:
    reported_issues = all_issues
```

---

## Step 8: Generate Report

### 8.1 Build report content

```python
report_date = datetime.now().strftime('%Y-%m-%d')
report_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

report = f"""# Hygiene Inspection — {report_date}

**Status:** pending
**Issues found:** {len(reported_issues)}
**Created:** {report_time}
**Validator:** hygiene-inspector

**Paths checked:** {len(paths)}

---

"""

for i, issue in enumerate(reported_issues, 1):
    report += f"""## Issue {i}: {issue['issue']}

**Path:** {issue['path']}
**Severity:** {issue['severity']}
**Category:** {issue['category']}
**Issue:** {issue['issue']}
**Current:** {issue['current']}
**Expected:** {issue['expected']}
**Suggested fix:** {issue['suggested_fix']}

---

"""
```

### 8.2 Write report file

```bash
report_file="wiki/reviews/${report_date}_hygiene-report.md"
cat > "$report_file" << 'EOF'
$report
EOF
```

---

## Step 9: Update _action-required.md

Same logic as other validators (append entry + cleanup old entries):

```python
def update_action_required(report_entry):
    content = read_file("wiki/reviews/_action-required.md")

    # Append new entry
    content = append_to_pending_reports(content, report_entry)

    # Cleanup old "Recently Applied" entries (>7 days)
    content = cleanup_recently_applied(content)

    # Update metadata
    content = update_timestamp(content)
    content = update_pending_count(content)

    write_file("wiki/reviews/_action-required.md", content)
```

---

## Step 10: Send Telegram Notification

```python
message = f"""Hygiene inspection complete

- Issues found: {len(reported_issues)} ({error_count} ERROR, {warning_count} WARNING, {info_count} INFO)
- Paths checked: {len(paths)}
- Report: wiki/reviews/{report_date}_hygiene-report.md

Review: wiki/reviews/_action-required.md

Commands:
- 'approve hygiene' to approve report
- 'show hygiene' for details
- 'reject hygiene' to reject
"""

send_telegram(message)
```

---

## Step 11: Log to Memory

```markdown
## {report_time} — Hygiene inspection

- **Paths checked:** {len(paths)} ({folder_count} folders + {file_count} files)
- **Issues found:** {len(reported_issues)} ({error_count} ERROR, {warning_count} WARNING, {info_count} INFO)
- **Report:** wiki/reviews/{report_date}_hygiene-report.md
- **Top violations:** {top_3_violation_types}
```

---

## Error Handling

### folder-structure.md errors

```python
try:
    rules = parse_folder_spec(folder_spec_content)
except Exception as e:
    log(f"[FATAL] Cannot parse folder-structure.md: {e}")
    send_telegram(f"[FATAL] Hygiene validation failed: folder-structure.md invalid")
    exit(1)
```

### Permission errors

```python
try:
    paths = scan_kb('.')
except PermissionError as e:
    log(f"[ERROR] Permission denied: {e}")
    send_telegram(f"[ERROR] Cannot scan KB: permission denied")
    exit(1)
```

### Path validation errors

```python
try:
    issues = validate_path(path, rules)
except Exception as e:
    log(f"[WARNING] Error validating {path}: {e}")
    # Continue with next path
    continue
```

---

## Performance Optimization

### Cache folder rules

```python
# Load once, reuse for all paths
folder_rules = parse_folder_spec(folder_spec_content)

for path in paths:
    validate_path(path, folder_rules)  # Reuse cached rules
```

### Efficient directory walking

```python
# Use os.walk with topdown=True to filter early
for dirpath, dirnames, filenames in os.walk('.', topdown=True):
    # Remove ignored directories from walk
    dirnames[:] = [d for d in dirnames if not should_ignore(d)]
    
    # Process remaining directories and files
    process_paths(dirpath, dirnames, filenames)
```

### Batch path checks

```python
# Group paths by depth for efficient validation
paths_by_depth = defaultdict(list)
for path in all_paths:
    paths_by_depth[path['depth']].append(path)

# Validate each depth level
for depth in sorted(paths_by_depth.keys()):
    validate_depth_level(paths_by_depth[depth], rules)
```

---

## Validation Checklist

Before marking validation complete:

- [ ] folder-structure.md loaded successfully
- [ ] All paths scanned
- [ ] All 3 validation categories checked
- [ ] Issues sorted by severity
- [ ] Report written to `wiki/reviews/`
- [ ] `_action-required.md` updated
- [ ] Old "Recently Applied" entries cleaned up
- [ ] Telegram notification sent
- [ ] MEMORY.md entry added
- [ ] No files or folders modified (read-only validator)

---

## Related Documentation

- [SKILL.md](SKILL.md) — Hygiene Inspector overview
- [examples.md](examples.md) — Sample hygiene issues and fixes
- [wiki/meta/folder-structure.md](../../wiki/meta/folder-structure.md) — Ground truth folder rules

---

**End of workflow.md**
