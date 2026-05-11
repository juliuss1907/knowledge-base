# Format Validator — Complete Workflow

Detailed step-by-step process for validating wiki file format compliance on daily 22:30 runs.

---

## Overview

This workflow validates all wiki files for format compliance against `wiki/meta/format-spec.md`:
- **Input:** All files in `wiki/sources/` + `wiki/concepts/` + ground truth `wiki/meta/format-spec.md`
- **Output:** Format report in `wiki/reviews/YYYY-MM-DD_format-report.md`
- **Side effect:** Update `wiki/reviews/_action-required.md`, send Telegram notification

Total time: 15-45 seconds for daily runs (5-15 new files + quick scan of existing)

---

## Step 1: Load Ground Truth

### 1.1 Read format-spec.md

```bash
format_spec_file="wiki/meta/format-spec.md"

if [ ! -f "$format_spec_file" ]; then
    echo "[FATAL ERROR] format-spec.md not found"
    send_telegram("[FATAL] Format validation failed: format-spec.md missing")
    exit 1
fi

format_spec=$(cat "$format_spec_file")
```

**Validation:**
- File must exist
- File must be readable
- File must be valid markdown

**If missing:**
→ Fatal error, cannot validate without ground truth

### 1.2 Parse format rules

Extract validation rules from format-spec.md:

```python
def parse_format_spec(content):
    """Extract validation rules from format-spec.md."""

    rules = {
        'concept': {
            'required_frontmatter': [],
            'required_sections': [],
            'field_order': [],
            'section_order': []
        },
        'source': {
            'required_frontmatter': [],
            'required_sections': [],
            'field_order': [],
            'section_order': []
        },
        'markdown_rules': {}
    }

    # Parse concept file format
    concept_section = extract_section(content, "Concept file format")
    rules['concept']['required_frontmatter'] = parse_frontmatter_fields(concept_section)
    rules['concept']['required_sections'] = parse_required_sections(concept_section)
    rules['concept']['field_order'] = parse_field_order(concept_section)
    rules['concept']['section_order'] = parse_section_order(concept_section)

    # Parse source file format
    source_section = extract_section(content, "Source file format")
    rules['source']['required_frontmatter'] = parse_frontmatter_fields(source_section)
    rules['source']['required_sections'] = parse_required_sections(source_section)
    rules['source']['field_order'] = parse_field_order(source_section)
    rules['source']['section_order'] = parse_section_order(source_section)

    # Parse markdown rules
    markdown_section = extract_section(content, "Common validation rules")
    rules['markdown_rules'] = parse_markdown_rules(markdown_section)

    return rules
```

**Cached in memory:**
- Format rules loaded once per validation run
- Reused for all files

---

## Step 2: Scan Wiki Files

### 2.1 Find all wiki content files

```bash
find wiki/sources/ wiki/concepts/ -name "*.md" -type f
```

### 2.2 Build file list

```python
files = []

for file_path in all_files:
    content = read_file(file_path)
    frontmatter = parse_yaml_frontmatter(content)
    body = extract_body(content)

    files.append({
        'path': file_path,
        'type': frontmatter.get('type'),
        'frontmatter': frontmatter,
        'body': body,
        'sections': parse_markdown_sections(body)
    })
```

---

## Step 3: Validate Each File

For each file:

```python
issues = []

# Check 1: Frontmatter compliance
issues += validate_frontmatter(file, format_rules[file_type])

# Check 2: Section structure
issues += validate_sections(file, format_rules[file_type])

# Check 3: Naming conventions
issues += validate_naming(file, format_rules[file_type])

# Check 4: Markdown syntax
issues += validate_markdown(file, format_rules['markdown_rules'])
```

---

## Step 4: Validate Frontmatter Compliance

### 4.1 Check required fields

```python
def validate_frontmatter(file, rules):
    issues = []
    frontmatter = file['frontmatter']

    for field_rule in rules['required_frontmatter']:
        field_name = field_rule['field']

        if field_name not in frontmatter:
            issues.append({
                'file': file['path'],
                'severity': 'ERROR',
                'category': 'Frontmatter',
                'issue': f'Missing required field: {field_name}',
                'current': 'Field not present',
                'expected': f'{field_name}: <value>',
                'suggested_fix': f'Add {field_name} field to frontmatter'
            })

    return issues
```

### 4.2 Check field types

```python
for field_rule in rules['required_frontmatter']:
    field_name = field_rule['field']
    expected_type = field_rule['type']

    if field_name not in frontmatter:
        continue

    actual_value = frontmatter[field_name]

    if expected_type == 'string' and not isinstance(actual_value, str):
        issues.append({
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': f'Field {field_name} must be string',
            'current': f'{field_name}: {type(actual_value).__name__}',
            'expected': f'{field_name}: string',
            'suggested_fix': f'Quote the value: {field_name}: "{actual_value}"'
        })

    if expected_type == 'array' and not isinstance(actual_value, list):
        issues.append({
            'severity': 'ERROR',
            'category': 'Frontmatter',
            'issue': f'Field {field_name} must be array',
            'current': f'{field_name}: {actual_value}',
            'expected': f'{field_name}: [item1, item2]',
            'suggested_fix': 'Use bracket syntax'
        })

    if expected_type == 'date':
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', str(actual_value)):
            issues.append({
                'severity': 'ERROR',
                'category': 'Frontmatter',
                'issue': f'Field {field_name} must be YYYY-MM-DD format',
                'current': f'{field_name}: {actual_value}',
                'expected': f'{field_name}: YYYY-MM-DD',
                'suggested_fix': 'Use ISO date format: 2026-05-09'
            })
```

### 4.3 Check field order

```python
actual_order = list(frontmatter.keys())
expected_order = rules['field_order']

if actual_order != expected_order:
    issues.append({
        'severity': 'WARNING',
        'category': 'Frontmatter',
        'issue': 'Field order does not match format-spec.md',
        'current': ', '.join(actual_order),
        'expected': ', '.join(expected_order),
        'suggested_fix': 'Reorder fields to match format-spec.md'
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
        'current': str(e),
        'expected': 'Valid YAML',
        'suggested_fix': 'Fix YAML syntax error'
    })
```

---

## Step 5: Validate Section Structure

### 5.1 Check required sections

```python
def validate_sections(file, rules):
    issues = []
    sections = file['sections']
    section_headers = [s['header'] for s in sections]

    for required_section in rules['required_sections']:
        if required_section not in section_headers:
            issues.append({
                'file': file['path'],
                'severity': 'ERROR',
                'category': 'Sections',
                'issue': f'Missing required section: {required_section}',
                'current': ', '.join(section_headers),
                'expected': f'Must include ## {required_section}',
                'suggested_fix': f'Add ## {required_section} section'
            })

    return issues
```

### 5.2 Check section order

```python
expected_order = rules['section_order']
actual_order = section_headers

if actual_order != expected_order:
    issues.append({
        'severity': 'WARNING',
        'category': 'Sections',
        'issue': 'Section order does not match format-spec.md',
        'current': ', '.join(actual_order),
        'expected': ', '.join(expected_order),
        'suggested_fix': 'Reorder sections to match format-spec.md'
    })
```

### 5.3 Check heading levels

```python
for section in sections:
    if section['level'] != 2:
        issues.append({
            'severity': 'ERROR',
            'category': 'Sections',
            'issue': f'Section uses wrong heading level: {section["header"]}',
            'current': f'{"#" * section["level"]} {section["header"]}',
            'expected': f'## {section["header"]}',
            'suggested_fix': 'Use H2 (##) for all sections'
        })
```

### 5.4 Check for duplicate sections

```python
seen = set()
for header in section_headers:
    if header in seen:
        issues.append({
            'severity': 'ERROR',
            'category': 'Sections',
            'issue': f'Duplicate section: {header}',
            'current': f'Multiple ## {header} sections',
            'expected': f'Only one ## {header} section',
            'suggested_fix': 'Remove or merge duplicate sections'
        })
    seen.add(header)
```

---

## Step 6: Validate Naming Conventions

### 6.1 Check filename format

```python
def validate_naming(file, rules):
    issues = []
    filename = os.path.basename(file['path'])
    file_type = file['type']

    if file_type == 'source':
        if not re.match(r'^src_[a-z0-9-]+\.md$', filename):
            issues.append({
                'file': file['path'],
                'severity': 'ERROR',
                'category': 'Naming',
                'issue': 'Source filename does not match format',
                'current': filename,
                'expected': 'src_<slug>.md',
                'suggested_fix': 'Rename to src_<slug>.md format'
            })

    elif file_type == 'concept':
        if not re.match(r'^[a-z0-9-]+\.md$', filename):
            issues.append({
                'file': file['path'],
                'severity': 'ERROR',
                'category': 'Naming',
                'issue': 'Concept filename does not match format',
                'current': filename,
                'expected': '<concept-slug>.md',
                'suggested_fix': 'Rename to lowercase-hyphen format'
            })

    return issues
```

### 6.2 Check slug rules

```python
slug = filename.replace('.md', '')
if file_type == 'source':
    slug = slug.replace('src_', '')

if not re.match(r'^[a-z0-9-]+$', slug):
    issues.append({
        'severity': 'ERROR',
        'category': 'Naming',
        'issue': 'Slug contains invalid characters',
        'current': slug,
        'expected': 'lowercase-hyphen-format',
        'suggested_fix': 'Use only lowercase letters, numbers, and hyphens'
    })

if len(slug) > 50:
    issues.append({
        'severity': 'WARNING',
        'category': 'Naming',
        'issue': 'Slug too long',
        'current': f'{len(slug)} characters',
        'expected': 'Max 50 characters',
        'suggested_fix': 'Shorten slug to 50 characters or less'
    })
```

### 6.3 Check path correctness

```python
if file_type == 'source' and not file['path'].startswith('wiki/sources/'):
    issues.append({
        'severity': 'ERROR',
        'category': 'Naming',
        'issue': 'Source file in wrong folder',
        'current': file['path'],
        'expected': 'wiki/sources/<filename>',
        'suggested_fix': 'Move to wiki/sources/ folder'
    })

if file_type == 'concept' and not file['path'].startswith('wiki/concepts/'):
    issues.append({
        'severity': 'ERROR',
        'category': 'Naming',
        'issue': 'Concept file in wrong folder',
        'current': file['path'],
        'expected': 'wiki/concepts/<filename>',
        'suggested_fix': 'Move to wiki/concepts/ folder'
    })
```

---

## Step 7: Validate Markdown Syntax

### 7.1 Check wikilinks

```python
def validate_markdown(file, rules):
    issues = []
    body = file['body']

    single_bracket_links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', body)

    for text, url in single_bracket_links:
        if url.startswith('wiki/') or url.endswith('.md'):
            issues.append({
                'file': file['path'],
                'severity': 'WARNING',
                'category': 'Markdown',
                'issue': 'Internal link should use wikilink syntax',
                'current': f'[{text}]({url})',
                'expected': f'[[{url.replace(".md", "")}]]',
                'suggested_fix': 'Use [[slug]] for internal links'
            })

    return issues
```

### 7.2 Check code blocks

```python
code_blocks = re.findall(r'```(\w*)\n', body)

for i, lang in enumerate(code_blocks):
    if not lang:
        issues.append({
            'severity': 'INFO',
            'category': 'Markdown',
            'issue': f'Code block {i+1} missing language tag',
            'current': '```\n',
            'expected': '```python\n or ```bash\n',
            'suggested_fix': 'Add language tag after ```'
        })
```

### 7.3 Check list consistency

```python
bullet_markers = re.findall(r'^([-*+])\s', body, re.MULTILINE)

if len(set(bullet_markers)) > 1:
    issues.append({
        'severity': 'INFO',
        'category': 'Markdown',
        'issue': 'Inconsistent bullet list markers',
        'current': f'Uses: {", ".join(set(bullet_markers))}',
        'expected': 'Use - for all bullet lists',
        'suggested_fix': 'Standardize on - for bullets'
    })
```

### 7.4 Check broken links

```python
wikilinks = re.findall(r'\[\[([^\]]+)\]\]', body)

for link in wikilinks:
    target_file = find_wiki_file(link)

    if not target_file:
        issues.append({
            'severity': 'ERROR',
            'category': 'Markdown',
            'issue': f'Broken wikilink: [[{link}]]',
            'current': f'[[{link}]]',
            'expected': 'Link to existing file',
            'suggested_fix': f'Create {link}.md or fix link'
        })
```

---

## Step 8: Score and Filter Issues

### 8.1 Assign severity scores

```python
severity_scores = {'ERROR': 3, 'WARNING': 2, 'INFO': 1}

for issue in all_issues:
    issue['score'] = severity_scores[issue['severity']]
```

### 8.2 Sort issues

```python
all_issues.sort(key=lambda x: (-x['score'], x['category'], x['file']))
```

### 8.3 Apply report limit

```python
max_issues = 20  # Daily validation limit

if len(all_issues) > max_issues:
    reported_issues = all_issues[:max_issues]
    log(f"[TRUNCATED] {len(all_issues) - max_issues} issues not included in report")
else:
    reported_issues = all_issues
```

---

## Step 9: Generate Report

### 9.1 Build report content

```python
report_date = datetime.now().strftime('%Y-%m-%d')
report_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

report = f"""# Format Validation — {report_date}

**Status:** pending
**Issues found:** {len(reported_issues)}
**Created:** {report_time}
**Validator:** format-validator

**Files checked:** {len(files)}

---

"""

for i, issue in enumerate(reported_issues, 1):
    report += f"""## Issue {i}: {issue['issue']}

**File:** {issue['file']}
**Severity:** {issue['severity']}
**Category:** {issue['category']}
**Issue:** {issue['issue']}
**Current:** {issue['current']}
**Expected:** {issue['expected']}
**Suggested fix:** {issue['suggested_fix']}

---

"""
```

### 9.2 Write report file

```bash
report_file="wiki/reviews/${report_date}_format-report.md"
cat > "$report_file" << 'EOF'
$report
EOF
```

---

## Step 10: Update _action-required.md

Same logic as Output Validator (append entry + cleanup old entries):

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

## Step 11: Send Telegram Notification

```python
message = f"""Format validation complete

- Issues found: {len(reported_issues)} ({error_count} ERROR, {warning_count} WARNING, {info_count} INFO)
- Files checked: {len(files)}
- Report: wiki/reviews/{report_date}_format-report.md

Review: wiki/reviews/_action-required.md

Commands:
- 'approve format' to approve report
- 'show format' for details
- 'reject format' to reject
"""

send_telegram(message)
```

---

## Step 12: Log to Memory

```markdown
## {report_time} — Format validation

- **Files checked:** {len(files)} ({sources_count} sources + {concepts_count} concepts)
- **Issues found:** {len(reported_issues)} ({error_count} ERROR, {warning_count} WARNING, {info_count} INFO)
- **Report:** wiki/reviews/{report_date}_format-report.md
- **Top violations:** {top_3_violation_types}
```

---

## Error Handling

### format-spec.md errors

```python
try:
    rules = parse_format_spec(format_spec_content)
except Exception as e:
    log(f"[FATAL] Cannot parse format-spec.md: {e}")
    send_telegram(f"[FATAL] Format validation failed: format-spec.md invalid")
    exit(1)
```

### File read errors

```python
try:
    content = read_file(file)
except FileNotFoundError:
    log(f"[WARNING] File not found: {file}")
    continue
except PermissionError:
    log(f"[ERROR] Permission denied: {file}")
    send_telegram(f"[ERROR] Cannot read {file}")
    exit(1)
```

### YAML parse errors

```python
try:
    frontmatter = yaml.safe_load(frontmatter_text)
except yaml.YAMLError as e:
    # Report as format issue, don't crash
    issues.append({
        'severity': 'ERROR',
        'category': 'Frontmatter',
        'issue': 'Invalid YAML syntax',
        'current': str(e),
        'expected': 'Valid YAML',
        'suggested_fix': 'Fix YAML syntax'
    })
```

---

## Performance Optimization

### Cache format rules

```python
# Load once, reuse for all files
format_rules = parse_format_spec(format_spec_content)

for file in files:
    validate_file(file, format_rules)  # Reuse cached rules
```

### Batch file reads

```python
file_contents = {}
for file_path in all_files:
    file_contents[file_path] = read_file(file_path)

for file_path, content in file_contents.items():
    validate(file_path, content)
```

---

## Validation Checklist

Before marking validation complete:

- [ ] format-spec.md loaded successfully
- [ ] All files scanned
- [ ] All 4 validation categories checked
- [ ] Issues sorted by severity
- [ ] Report written to `wiki/reviews/`
- [ ] `_action-required.md` updated
- [ ] Old "Recently Applied" entries cleaned up
- [ ] Telegram notification sent
- [ ] MEMORY.md entry added
- [ ] No files modified (read-only validator)

---

## Related Documentation

- [SKILL.md](SKILL.md) — Format Validator overview
- [reference.md](reference.md) — format-spec.md rules with annotations
- [examples.md](examples.md) — Sample format issues and fixes
