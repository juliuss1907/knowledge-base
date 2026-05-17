# Format Validator — Complete Workflow

Detailed step-by-step process for validating file format compliance on daily 23:15 runs.

---

## Overview

This workflow validates all markdown files across the KB for format compliance:
- **Input:** All `.md` files in `wiki/`, `raw/`, `context/` + ground truth specs
- **Output:** Format report in `wiki/reviews/YYYY-MM-DD_format-report.md`
- **Side effect:** Update `wiki/reviews/_action-required.md`, send Telegram notification

Total time: 15-45 seconds for daily runs.

**Spec dispatch table:**

| `type` value | Validation spec | File location |
|---|---|---|
| `concept` | format-spec.md §2 | `wiki/concepts/` |
| `source` | format-spec.md §3 | `wiki/sources/` |
| `index` (level 1) | index-spec.md §3 | `raw/raw.md`, `wiki/wiki.md`, `context/context.md` |
| `index` (level 2) | index-spec.md §4 | `raw/<type>/<type>.md`, `wiki/tag/tag.md` |
| `index` (level 3) | index-spec.md §5 | `wiki/tag/<tag>.md` |
| Missing/other | ERROR — flag immediately | Any |

---

## Step 1: Load Ground Truth Specs

### 1.1 Read both spec files

```bash
format_spec_file="wiki/meta/format-spec.md"
index_spec_file="wiki/meta/index-spec.md"

# Verify both specs exist
if [ ! -f "$format_spec_file" ]; then
    echo "[FATAL] format-spec.md not found"
    send_telegram("[FATAL] Format validation failed: format-spec.md missing")
    exit 1
fi

if [ ! -f "$index_spec_file" ]; then
    echo "[FATAL] index-spec.md not found"
    send_telegram("[FATAL] Format validation failed: index-spec.md missing")
    exit 1
fi

format_spec=$(cat "$format_spec_file")
index_spec=$(cat "$index_spec_file")
```

**If either missing:** Fatal error, cannot validate without ground truth.

### 1.2 Parse rules from both specs

```python
def load_all_rules():
    """Load validation rules from both spec files."""
    return {
        # From format-spec.md
        'concept': parse_concept_rules(format_spec),
        'source': parse_source_rules(format_spec),

        # From index-spec.md
        'index_level_1': parse_index_level_1_rules(index_spec),
        'index_level_2': parse_index_level_2_rules(index_spec),
        'index_level_3': parse_index_level_3_rules(index_spec),

        # Common rules (apply to all files)
        'markdown_rules': parse_markdown_rules(format_spec),
        'wikilink_rules': parse_wikilink_rules(format_spec)
    }
```

**Cached in memory:** Rules loaded once per validation run, reused for all files.

---

## Step 2: Scan All Files

### 2.1 Find all markdown files in scope

```bash
# Scan content folders
find \
    wiki/sources/ \
    wiki/concepts/ \
    wiki/tag/ \
    wiki/topic/ \
    raw/ \
    context/ \
    -maxdepth 3 \
    -name "*.md" \
    -type f \
    -not -path "*/archive/*"

# Include root-level index files
ls raw/raw.md wiki/wiki.md context/context.md 2>/dev/null
```

**Excluded:**
- `wiki/meta/` (ground truth specs, not validated)
- `wiki/reviews/` (Hermes outputs)
- `wiki/drafts/` (already flagged)
- `archive/` subfolders (historical)

### 2.2 Build file list with type detection

```python
files = []

for file_path in all_files:
    content = read_file(file_path)
    frontmatter = parse_yaml_frontmatter(content)
    body = extract_body(content)

    file_type = frontmatter.get('type')

    # Determine validation target
    if file_type in ['concept', 'source']:
        validation_target = file_type
        spec_source = 'format-spec.md'
    elif file_type == 'index':
        level = frontmatter.get('level')
        if level in [1, 2, 3]:
            validation_target = f'index_level_{level}'
            spec_source = 'index-spec.md'
        else:
            validation_target = 'unknown_index'
            spec_source = None
    else:
        validation_target = 'unknown'
        spec_source = None

    files.append({
        'path': file_path,
        'type': file_type,
        'level': frontmatter.get('level'),
        'validation_target': validation_target,
        'spec_source': spec_source,
        'frontmatter': frontmatter,
        'body': body,
        'sections': parse_markdown_sections(body)
    })
```

### 2.3 Flag files with missing or invalid type

```python
for file in files:
    if file['validation_target'] == 'unknown':
        if file['type'] is None:
            issues.append({
                'file': file['path'],
                'severity': 'ERROR',
                'category': 'Frontmatter',
                'issue': 'Missing type field',
                'current': '(no type field)',
                'expected': 'type: concept | source | index',
                'suggested_fix': 'Add type field to frontmatter'
            })
        else:
            issues.append({
                'file': file['path'],
                'severity': 'ERROR',
                'category': 'Frontmatter',
                'issue': f'Unknown type: {file["type"]}',
                'expected': 'type: concept | source | index'
            })

    elif file['validation_target'] == 'unknown_index':
        issues.append({
            'file': file['path'],
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': f'Invalid level for index file: {file["level"]}',
            'expected': 'level: 1 | 2 | 3'
        })
```

---

## Step 3: Dispatch Validation by Type

### 3.1 Route each file to correct validator

```python
for file in files:
    target = file['validation_target']

    if target == 'concept':
        issues += validate_concept(file, rules['concept'])
    elif target == 'source':
        issues += validate_source(file, rules['source'])
    elif target == 'index_level_1':
        issues += validate_index_level_1(file, rules['index_level_1'])
    elif target == 'index_level_2':
        issues += validate_index_level_2(file, rules['index_level_2'])
    elif target == 'index_level_3':
        issues += validate_index_level_3(file, rules['index_level_3'])

    # Common checks (skip for unknown files)
    if target not in ['unknown', 'unknown_index']:
        issues += validate_path(file)
        issues += validate_markdown(file, rules['markdown_rules'])
        issues += validate_wikilinks(file, rules['wikilink_rules'])
```

### 3.2 Path validation per type

```python
def validate_path(file):
    expected_paths = {
        'concept': lambda p: p.startswith('wiki/concepts/'),
        'source': lambda p: p.startswith('wiki/sources/'),
        'index_level_1': lambda p: p in [
            'raw/raw.md', 'wiki/wiki.md', 'context/context.md'
        ],
        'index_level_2': lambda p: (
            (p.startswith('raw/') and any(
                p.endswith(f'/{t}.md')
                for t in ['articles', 'posts', 'websites', 'videos', 'papers', 'repos']
            )) or p == 'wiki/tag/tag.md'
        ),
        'index_level_3': lambda p: (
            p.startswith('wiki/tag/') and p != 'wiki/tag/tag.md'
        )
    }

    target = file['validation_target']
    if target in expected_paths and not expected_paths[target](file['path']):
        return [{
            'file': file['path'],
            'severity': 'ERROR',
            'category': 'Naming',
            'issue': f'{target} file in wrong location',
            'current': file['path'],
            'suggested_fix': 'Move file to correct folder per dispatch table'
        }]
    return []
```

---

## Step 4: Validate Frontmatter (concept + source)

### 4.1 Check required fields

```python
def validate_frontmatter(file, rules):
    issues = []
    fm = file['frontmatter']

    for field_rule in rules['required_frontmatter']:
        field_name = field_rule['field']
        if field_name not in fm:
            issues.append({
                'file': file['path'],
                'severity': 'ERROR',
                'category': 'Frontmatter',
                'issue': f'Missing required field: {field_name}',
                'expected': f'{field_name}: <value>',
                'suggested_fix': f'Add {field_name} field'
            })

    return issues
```

### 4.2 Check field types

```python
for field_rule in rules['required_frontmatter']:
    field_name = field_rule['field']
    expected_type = field_rule['type']

    if field_name not in fm:
        continue

    value = fm[field_name]

    if expected_type == 'string' and not isinstance(value, str):
        issues.append({
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': f'{field_name} must be string'
        })

    if expected_type == 'array' and not isinstance(value, list):
        issues.append({
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': f'{field_name} must be array'
        })

    if expected_type == 'date':
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', str(value)):
            issues.append({
                'severity': 'ERROR',
                'category': 'Frontmatter',
                'issue': f'{field_name} must be YYYY-MM-DD'
            })
```

### 4.3 Check field order

```python
actual = list(fm.keys())
expected = rules['field_order']

if actual != expected:
    issues.append({
        'severity': 'WARNING',
        'category': 'Frontmatter',
        'issue': 'Field order does not match spec',
        'current': ', '.join(actual),
        'expected': ', '.join(expected)
    })
```

### 4.4 Check YAML syntax

```python
try:
    yaml.safe_load(frontmatter_text)
except yaml.YAMLError as e:
    issues.append({
        'severity': 'ERROR',
        'category': 'Frontmatter',
        'issue': 'Invalid YAML syntax',
        'current': str(e)
    })
```

---

## Step 4.5: Validate Index Files

### 4.5.1 Validate level 1 index

```python
def validate_index_level_1(file, rules):
    issues = []
    fm = file['frontmatter']

    required = ['type', 'level', 'scope', 'auto_generated', 'last_updated']
    for field in required:
        if field not in fm:
            issues.append({
                'severity': 'ERROR',
                'category': 'Frontmatter',
                'issue': f'Missing required field: {field}',
                'suggested_fix': 'Add per index-spec.md §3.2'
            })

    if fm.get('type') != 'index':
        issues.append({
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': f'type must be "index", got: {fm.get("type")}'
        })

    if fm.get('level') != 1:
        issues.append({
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': f'level must be 1, got: {fm.get("level")}'
        })

    if fm.get('scope') not in ['raw', 'wiki', 'context']:
        issues.append({
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': f'scope must be raw|wiki|context, got: {fm.get("scope")}'
        })

    if fm.get('auto_generated') is not False:
        issues.append({
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': 'auto_generated must be false for level 1'
        })

    required_sections = ['Overview', 'Sub-indexes', 'Notes']
    for section in required_sections:
        if section not in [s['header'] for s in file['sections']]:
            issues.append({
                'severity': 'ERROR',
                'category': 'Sections',
                'issue': f'Missing section: ## {section}'
            })

    return issues
```

### 4.5.2 Validate level 2 index

```python
def validate_index_level_2(file, rules):
    issues = []
    fm = file['frontmatter']

    required = [
        'type', 'level', 'scope', 'parent',
        'auto_generated', 'items_managed_by', 'last_updated'
    ]
    for field in required:
        if field not in fm:
            issues.append({
                'severity': 'ERROR',
                'category': 'Frontmatter',
                'issue': f'Missing required field: {field}',
                'suggested_fix': 'Add per index-spec.md §4.2'
            })

    if fm.get('level') != 2:
        issues.append({
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': f'level must be 2, got: {fm.get("level")}'
        })

    valid_scopes = [
        'articles', 'posts', 'websites',
        'videos', 'papers', 'repos', 'tags'
    ]
    if fm.get('scope') not in valid_scopes:
        issues.append({
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': f'Invalid scope: {fm.get("scope")}'
        })

    parent = str(fm.get('parent', ''))
    if not (parent.startswith('[[') and parent.endswith(']]')):
        issues.append({
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': 'parent field must be a wikilink',
            'expected': '[[raw]] or [[wiki]]'
        })

    valid_agents = ['ingest-agent', 'index-agent']
    if fm.get('items_managed_by') not in valid_agents:
        issues.append({
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': f'items_managed_by must be one of: {valid_agents}'
        })

    required_sections = ['Overview', 'Parent', 'Stats', 'Items', 'Notes']
    for section in required_sections:
        if section not in [s['header'] for s in file['sections']]:
            issues.append({
                'severity': 'ERROR',
                'category': 'Sections',
                'issue': f'Missing section: ## {section}'
            })

    issues += validate_stats_section(file, scope=fm.get('scope'))

    return issues
```

### 4.5.3 Validate level 3 index

```python
def validate_index_level_3(file, rules):
    issues = []
    fm = file['frontmatter']

    required = [
        'type', 'level', 'scope', 'parent', 'tag',
        'auto_generated', 'last_updated'
    ]
    for field in required:
        if field not in fm:
            issues.append({
                'severity': 'ERROR',
                'category': 'Frontmatter',
                'issue': f'Missing required field: {field}'
            })

    if fm.get('level') != 3:
        issues.append({
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': f'level must be 3, got: {fm.get("level")}'
        })

    if fm.get('scope') != 'tag':
        issues.append({
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': 'scope must be "tag" for level 3'
        })

    if fm.get('parent') != '[[tag]]':
        issues.append({
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': f'parent must be [[tag]], got: {fm.get("parent")}'
        })

    expected_tag = os.path.basename(file['path']).replace('.md', '')
    if fm.get('tag') != expected_tag:
        issues.append({
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': f'tag field must match filename: {expected_tag}'
        })

    if fm.get('auto_generated') is not True:
        issues.append({
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': 'auto_generated must be true for level 3'
        })

    required_sections = [
        'Parent', 'Stats', 'Files with this tag', 'Co-occurring tags'
    ]
    for section in required_sections:
        if section not in [s['header'] for s in file['sections']]:
            issues.append({
                'severity': 'ERROR',
                'category': 'Sections',
                'issue': f'Missing section: ## {section}'
            })

    return issues
```

### 4.5.4 Validate Stats section

```python
def validate_stats_section(file, scope):
    """Validate Stats section per index-spec.md §6."""
    issues = []
    stats = next(
        (s for s in file['sections'] if s['header'] == 'Stats'),
        None
    )

    if not stats:
        return []  # Already flagged in section check

    content = stats['content']

    raw_scopes = ['articles', 'posts', 'websites', 'videos', 'papers', 'repos']

    if scope in raw_scopes:
        required = ['Total:', 'By status:', 'By date:', 'Last updated:']
    elif scope == 'tags':
        required = [
            'Total tags:', 'Main tags:', 'Sub tags:',
            'Most used:', 'Last updated:'
        ]
    else:
        required = ['Last updated:']

    for line in required:
        if line not in content:
            issues.append({
                'severity': 'ERROR',
                'category': 'Stats',
                'issue': f'Stats missing field: {line}',
                'suggested_fix': 'Add per index-spec.md §6'
            })

    # Check freshness (>2 days = WARNING)
    match = re.search(r'Last updated:\s*(\d{4}-\d{2}-\d{2})', content)
    if match:
        last_updated = match.group(1)
        days_old = (
            datetime.now() - datetime.strptime(last_updated, '%Y-%m-%d')
        ).days
        if days_old > 2:
            issues.append({
                'severity': 'WARNING',
                'category': 'Stats',
                'issue': f'Stats outdated ({days_old} days old)',
                'suggested_fix': 'Trigger Index/Ingest Agent to refresh'
            })

    return issues
```

---

## Step 5: Validate Section Structure

### 5.1 Check required sections

```python
def validate_sections(file, rules):
    issues = []
    section_headers = [s['header'] for s in file['sections']]

    for required in rules['required_sections']:
        if required not in section_headers:
            issues.append({
                'severity': 'ERROR',
                'category': 'Sections',
                'issue': f'Missing section: {required}',
                'expected': f'## {required}'
            })

    return issues
```

### 5.2 Check section order

```python
if section_headers != rules['section_order']:
    issues.append({
        'severity': 'WARNING',
        'category': 'Sections',
        'issue': 'Section order does not match spec',
        'current': ', '.join(section_headers),
        'expected': ', '.join(rules['section_order'])
    })
```

### 5.3 Check heading levels

```python
for section in file['sections']:
    if section['level'] != 2:
        issues.append({
            'severity': 'ERROR',
            'category': 'Sections',
            'issue': f'Wrong heading level: {section["header"]}',
            'expected': f'## {section["header"]}'
        })
```

### 5.4 Check duplicate sections

```python
seen = set()
for header in section_headers:
    if header in seen:
        issues.append({
            'severity': 'ERROR',
            'category': 'Sections',
            'issue': f'Duplicate section: {header}'
        })
    seen.add(header)
```

---

## Step 6: Validate Naming Conventions

### 6.1 Filename format

```python
def validate_naming(file, rules):
    issues = []
    filename = os.path.basename(file['path'])
    file_type = file['type']

    if file_type == 'source':
        if not re.match(r'^src_[a-z0-9-]+\.md$', filename):
            issues.append({
                'severity': 'ERROR',
                'category': 'Naming',
                'issue': 'Source filename invalid',
                'current': filename,
                'expected': 'src_<slug>.md'
            })

    elif file_type == 'concept':
        if not re.match(r'^[a-z0-9-]+\.md$', filename):
            issues.append({
                'severity': 'ERROR',
                'category': 'Naming',
                'issue': 'Concept filename invalid',
                'current': filename,
                'expected': '<concept-slug>.md'
            })

    return issues
```

### 6.2 Slug rules

```python
slug = filename.replace('.md', '').replace('src_', '')

if not re.match(r'^[a-z0-9-]+$', slug):
    issues.append({
        'severity': 'ERROR',
        'category': 'Naming',
        'issue': 'Slug contains invalid characters',
        'expected': 'lowercase-hyphen-format'
    })

if len(slug) > 50:
    issues.append({
        'severity': 'WARNING',
        'category': 'Naming',
        'issue': f'Slug too long ({len(slug)} chars, max 50)'
    })
```

---

## Step 7: Validate Markdown Syntax

### 7.1 Wikilinks

```python
def validate_wikilinks(file, rules):
    issues = []
    body = file['body']

    # Find markdown links that should be wikilinks
    md_links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', body)
    for text, url in md_links:
        if url.startswith('wiki/') or url.endswith('.md'):
            issues.append({
                'severity': 'WARNING',
                'category': 'Markdown',
                'issue': 'Internal link should use wikilink',
                'current': f'[{text}]({url})',
                'expected': f'[[{url.replace(".md", "").split("/")[-1]}]]'
            })

    # Check broken wikilinks
    wikilinks = re.findall(r'\[\[([^\]]+)\]\]', body)
    for link in wikilinks:
        target = link.split('|')[0]  # Strip display text
        if not find_wiki_file(target):
            issues.append({
                'severity': 'ERROR',
                'category': 'Markdown',
                'issue': f'Broken wikilink: [[{link}]]',
                'suggested_fix': f'Create {target}.md or fix link'
            })

    return issues
```

### 7.2 Code blocks

```python
def validate_markdown(file, rules):
    issues = []
    body = file['body']

    code_blocks = re.findall(r'```(\w*)\n', body)
    for i, lang in enumerate(code_blocks):
        if not lang:
            issues.append({
                'severity': 'INFO',
                'category': 'Markdown',
                'issue': f'Code block {i+1} missing language tag'
            })

    return issues
```

### 7.3 List consistency

```python
markers = re.findall(r'^([-*+])\s', body, re.MULTILINE)
if len(set(markers)) > 1:
    issues.append({
        'severity': 'INFO',
        'category': 'Markdown',
        'issue': 'Inconsistent bullet markers',
        'expected': 'Use - for all bullets'
    })
```

---

## Step 8: Score and Filter Issues

### 8.1 Group by file

```python
issues_by_file = {}
for issue in all_issues:
    path = issue['file']
    if path not in issues_by_file:
        issues_by_file[path] = []
    issues_by_file[path].append(issue)
```

### 8.2 Sort by severity

```python
severity_rank = {'ERROR': 0, 'WARNING': 1, 'INFO': 2}

for path in issues_by_file:
    issues_by_file[path].sort(key=lambda x: severity_rank[x['severity']])
```

### 8.3 Limit total issues per report

```python
MAX_ISSUES = 20

if len(all_issues) > MAX_ISSUES:
    # Priority: ERRORs first, then WARNINGs, then INFOs
    errors = [i for i in all_issues if i['severity'] == 'ERROR']
    warnings = [i for i in all_issues if i['severity'] == 'WARNING']
    infos = [i for i in all_issues if i['severity'] == 'INFO']

    filtered = errors[:MAX_ISSUES]
    remaining = MAX_ISSUES - len(filtered)
    if remaining > 0:
        filtered += warnings[:remaining]
        remaining -= min(len(warnings), remaining)
    if remaining > 0:
        filtered += infos[:remaining]

    truncated = len(all_issues) - len(filtered)
    all_issues = filtered
```

---

## Step 9: Generate Report

### 9.1 Report structure

```markdown
---
type: validation-report
validator: format-validator
date: YYYY-MM-DD
status: pending-approval
---

# Format Validation Report — YYYY-MM-DD

## Summary

- **Files scanned:** N
- **Issues found:** N total (X ERROR, Y WARNING, Z INFO)
- **Files with issues:** N
- **Truncated:** N issues hidden (total: N)

## Issues by Severity

### ERRORs (X)

#### file/path.md

**[Frontmatter] Missing required field: tags**
- Current: (no tags field)
- Expected: tags: [tag1, tag2]
- Suggested fix: Add tags array to frontmatter

### WARNINGs (Y)

#### file/path.md

**[Frontmatter] Field order does not match spec**
- Current: type, title, date, tags
- Expected: type, title, tags, date

### INFOs (Z)

#### file/path.md

**[Markdown] Code block missing language tag**

## Statistics

- Concept files: N (X with issues)
- Source files: N (X with issues)
- Index files (level 1): N (X with issues)
- Index files (level 2): N (X with issues)
- Index files (level 3): N (X with issues)

## Next Actions

To approve: reply `approve format` in Telegram.
```

### 9.2 Write report file

```bash
report_file="wiki/reviews/$(date +%Y-%m-%d)_format-report.md"
cat > "$report_file" << EOF
... (generated content)
EOF
```

---

## Step 10: Update _action-required.md

```python
def update_action_required(report_path, summary):
    action_file = "wiki/reviews/_action-required.md"

    new_entry = f"""
### {date} — Format Validator

- **Report:** [[{report_path}]]
- **Issues:** {summary['total']} ({summary['errors']} ERROR, {summary['warnings']} WARNING, {summary['infos']} INFO)
- **Status:** Pending approval
- **Action:** Reply `approve format` to apply fixes
"""

    # Append to file (newest first)
    insert_at_top(action_file, new_entry)
```

---

## Step 11: Send Telegram Notification

```python
def send_telegram_notification(summary):
    message = f"""
Format Validation Complete

Files scanned: {summary['files_scanned']}
Issues found: {summary['total']}
  ERROR: {summary['errors']}
  WARNING: {summary['warnings']}
  INFO: {summary['infos']}

Report: {report_path}

To apply fixes: reply 'approve format'
"""
    send_telegram(message)
```

---

## Step 12: Log to Memory

```python
def log_to_memory(summary, duration):
    memory_entry = {
        'timestamp': datetime.now().isoformat(),
        'validator': 'format-validator',
        'duration_seconds': duration,
        'files_scanned': summary['files_scanned'],
        'issues_found': summary['total'],
        'severity_breakdown': {
            'error': summary['errors'],
            'warning': summary['warnings'],
            'info': summary['infos']
        },
        'report_path': report_path
    }

    append_to_memory('.hermes/MEMORY.md', memory_entry)
    update_heartbeat('.hermes/HEARTBEAT.md', 'format-validator', summary)
```

---

## Error Handling

**Fatal errors (abort):**
- format-spec.md missing
- index-spec.md missing
- Cannot write to wiki/reviews/

**Non-fatal errors (log + continue):**
- Single file unreadable → skip + flag
- YAML parse error → flag as ERROR + skip rest of file checks
- Network error sending Telegram → log + continue

**Recovery:**
- Always write report file even if Telegram fails
- Always update _action-required.md even if MEMORY.md write fails
