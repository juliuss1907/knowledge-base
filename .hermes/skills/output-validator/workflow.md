# Output Validator — Complete Workflow

Detailed step-by-step process for validating wiki content quality on daily 22:00 runs.

---

## Overview

This workflow validates all wiki files for content quality across 4 dimensions:
- **Input:** All files in `wiki/sources/` + `wiki/concepts/`
- **Output:** Quality report in `wiki/reviews/YYYY-MM-DD_output-report.md`
- **Side effect:** Update `wiki/reviews/_action-required.md`, send Telegram notification

Total time: 15-45 seconds for daily runs (5-15 new files + quick scan of existing)

---

## Daily vs Full Validation

### Daily validation (default at 22:00)
- **Prioritize new files** — compiled today (check `date_compiled` or `last_updated`)
- **Quick scan existing files** — only check for systematic issues
- **Report limit:** 20 issues max
- **Focus:** Catch issues in fresh content

### Full validation (on-demand)
- **Deep check all files** — regardless of date
- **Report limit:** 50 issues max
- **Focus:** Comprehensive quality audit

**This workflow describes daily validation.** For full validation, skip Step 1.2 (file filtering).

---

## Step 1: Scan Wiki Files

### 1.1 Find all wiki content files

```bash
# Find all markdown files in sources and concepts
find wiki/sources/ wiki/concepts/ -name "*.md" -type f
```

**Expected count:**
- `wiki/sources/`: ~80-200 files
- `wiki/concepts/`: ~50-150 files
- Total: ~130-350 files typical

**Sort order:**
- By `last_updated` or `date_compiled` (newest first)
- Then alphabetical by path

### 1.2 Filter for new files (daily validation only)

```bash
# Get today's date
today=$(date +%Y-%m-%d)

# Filter files compiled or updated today
for file in $all_files; do
    # Extract frontmatter dates
    date_compiled=$(grep "^date_compiled:" "$file" | awk '{print $2}')
    last_updated=$(grep "^last_updated:" "$file" | awk '{print $2}')
    
    # Check if file is new today
    if [ "$date_compiled" = "$today" ] || [ "$last_updated" = "$today" ]; then
        new_files+=("$file")
    else
        existing_files+=("$file")
    fi
done
```

**Result:**
- `new_files[]` — files to validate deeply (5-15 typical)
- `existing_files[]` — files to quick-scan (100-300 typical)

### 1.3 Read frontmatter from each file

For each file:

```bash
# Extract frontmatter
sed -n '/^---$/,/^---$/p' "$file" | sed '1d;$d'
```

**Parse YAML fields:**
- `type` — source or concept
- `main_tag`, `sub_tags`, `topic` — for context
- `date_compiled` or `last_updated` — for filtering
- `sources` (concepts only) — for citation check

**Build in-memory structure:**
```python
files = []
for file in new_files + existing_files:
    frontmatter = parse_yaml(file)
    body = read_body(file)
    
    files.append({
        'path': file,
        'type': frontmatter['type'],
        'is_new': file in new_files,
        'frontmatter': frontmatter,
        'body': body,
        'language': detect_language(body)
    })
```

---

## Step 2: Validate Each File

For each file in `files[]`:

### 2.1 Determine validation depth

```python
if file['is_new']:
    # New file — full validation (all 4 dimensions)
    dimensions = ['factual', 'completeness', 'coherence', 'vietnamese']
else:
    # Existing file — quick scan (completeness only)
    dimensions = ['completeness']
```

**Rationale:**
- New files need thorough check (just compiled, may have issues)
- Existing files already validated — only check if structure changed

### 2.2 Run validation checks

For each dimension in `dimensions[]`:

```python
issues = []

if 'factual' in dimensions:
    issues += validate_factual_accuracy(file)

if 'completeness' in dimensions:
    issues += validate_completeness(file)

if 'coherence' in dimensions:
    issues += validate_coherence(file)

if 'vietnamese' in dimensions and file['language'] == 'vi':
    issues += validate_vietnamese_quality(file)
```

---

## Step 3: Validate Factual Accuracy

### 3.1 Check source citations

For concept files:

```python
def validate_factual_accuracy(file):
    issues = []
    body = file['body']
    
    # Extract claims (sentences with factual assertions)
    claims = extract_claims(body)
    
    for claim in claims:
        # Check if claim has citation
        if not has_citation(claim):
            issues.append({
                'file': file['path'],
                'severity': 'WARNING',
                'dimension': 'Factual',
                'issue': 'Claim without source citation',
                'evidence': claim,
                'suggested_fix': 'Add source citation: (Source: [[src_name]])'
            })
    
    return issues
```

**Citation patterns recognized:**
```
(Source: [[src_name]])
According to [[src_name]], ...
As mentioned in [[src_name]], ...
```

### 3.2 Check technical term usage

```python
# Load technical terms dictionary
tech_terms = load_tech_terms()  # From validation-criteria.md

for term in tech_terms:
    if term in body:
        # Check if used correctly (context-aware)
        if not is_correct_usage(term, body):
            issues.append({
                'severity': 'ERROR',
                'dimension': 'Factual',
                'issue': f'Technical term "{term}" used incorrectly',
                'evidence': extract_context(term, body),
                'suggested_fix': f'Review definition of "{term}" and correct usage'
            })
```

### 3.3 Check for contradictions with sources

For concept files with multiple sources:

```python
sources = file['frontmatter']['sources']

if len(sources) > 1:
    # Read all source files
    source_contents = [read_file(src) for src in sources]
    
    # Check for contradictions using LLM
    prompt = f"""
Check if this concept file contradicts any of its source files:

Concept: {file['body']}

Sources:
{'\n\n'.join(source_contents)}

Output: "OK" if no contradictions, or list contradictions found.
"""
    
    result = llm_call(prompt, model='claude-3-5-sonnet')
    
    if result != "OK":
        issues.append({
            'severity': 'ERROR',
            'dimension': 'Factual',
            'issue': 'Concept contradicts source material',
            'evidence': result,
            'suggested_fix': 'Reconcile contradiction or remove conflicting source'
        })
```

### 3.4 Check dates and numbers

```python
# Extract dates (YYYY-MM-DD format)
dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', body)

for date in dates:
    # Validate date format
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        issues.append({
            'severity': 'ERROR',
            'dimension': 'Factual',
            'issue': f'Invalid date format: {date}',
            'evidence': extract_context(date, body),
            'suggested_fix': 'Use YYYY-MM-DD format'
        })

# Extract numbers with units
numbers = re.findall(r'\b\d+(?:\.\d+)?\s*(?:GB|MB|KB|%|USD|VND)\b', body)

for number in numbers:
    # Check if number is reasonable (heuristic)
    if not is_reasonable_number(number):
        issues.append({
            'severity': 'WARNING',
            'dimension': 'Factual',
            'issue': f'Unusual number: {number}',
            'evidence': extract_context(number, body),
            'suggested_fix': 'Verify this number is correct'
        })
```

---

## Step 4: Validate Completeness

### 4.1 Check required sections

```python
def validate_completeness(file):
    issues = []
    sections = parse_markdown_sections(file['body'])
    
    # Required sections by file type
    required = {
        'source': ['Metadata', 'Summary', 'Key points', 'Concepts referenced'],
        'concept': ['Definition', 'Key ideas', 'Related concepts', 'Sources']
    }
    
    file_type = file['type']
    
    for section in required[file_type]:
        if section not in sections:
            issues.append({
                'severity': 'ERROR',
                'dimension': 'Completeness',
                'issue': f'Missing required section: {section}',
                'evidence': 'N/A',
                'suggested_fix': f'Add ## {section} section'
            })
    
    return issues
```

### 4.2 Check summary length

```python
summary = sections.get('Summary', '')

# Count sentences
sentence_count = len(re.split(r'[.!?]+', summary.strip()))

if sentence_count < 3:
    issues.append({
        'severity': 'WARNING',
        'dimension': 'Completeness',
        'issue': f'Summary too short ({sentence_count} sentences, need 3-5)',
        'evidence': summary,
        'suggested_fix': 'Expand summary to 3-5 sentences'
    })
elif sentence_count > 5:
    issues.append({
        'severity': 'INFO',
        'dimension': 'Completeness',
        'issue': f'Summary too long ({sentence_count} sentences, prefer 3-5)',
        'evidence': summary[:100] + '...',
        'suggested_fix': 'Condense summary to 3-5 sentences'
    })
```

### 4.3 Check key points count

```python
key_points = sections.get('Key points', '')

# Count bullet points
point_count = len(re.findall(r'^- ', key_points, re.MULTILINE))

if point_count < 5:
    issues.append({
        'severity': 'WARNING',
        'dimension': 'Completeness',
        'issue': f'Too few key points ({point_count}, need 5-10)',
        'evidence': key_points,
        'suggested_fix': 'Add more key points (target 5-10)'
    })
elif point_count > 10:
    issues.append({
        'severity': 'INFO',
        'dimension': 'Completeness',
        'issue': f'Too many key points ({point_count}, prefer 5-10)',
        'evidence': key_points[:100] + '...',
        'suggested_fix': 'Consolidate to 5-10 most important points'
    })
```

### 4.4 Check definition length (concepts only)

```python
if file['type'] == 'concept':
    definition = sections.get('Definition', '')
    
    # Count sentences
    sentence_count = len(re.split(r'[.!?]+', definition.strip()))
    
    if sentence_count < 2:
        issues.append({
            'severity': 'ERROR',
            'dimension': 'Completeness',
            'issue': f'Definition too short ({sentence_count} sentence, need 2-3)',
            'evidence': definition,
            'suggested_fix': 'Expand definition to 2-3 sentences'
        })
    elif sentence_count > 3:
        issues.append({
            'severity': 'INFO',
            'dimension': 'Completeness',
            'issue': f'Definition too long ({sentence_count} sentences, prefer 2-3)',
            'evidence': definition[:100] + '...',
            'suggested_fix': 'Condense definition to 2-3 sentences'
        })
```

---

## Step 5: Validate Coherence

### 5.1 Check logical flow using LLM

```python
def validate_coherence(file):
    issues = []
    body = file['body']
    
    # Use LLM to check coherence
    prompt = f"""
Analyze the logical flow and coherence of this wiki content:

{body}

Check for:
1. Clear progression of ideas
2. Logical connections between sections
3. Internal contradictions
4. Unsupported claims

Output format:
- "OK" if coherent
- Or list issues found with specific examples
"""
    
    result = llm_call(prompt, model='claude-3-5-sonnet')
    
    if result != "OK":
        # Parse LLM output into issues
        for issue_text in parse_llm_issues(result):
            issues.append({
                'severity': 'WARNING',
                'dimension': 'Coherence',
                'issue': issue_text,
                'evidence': extract_relevant_section(body, issue_text),
                'suggested_fix': 'Improve logical flow or clarify argument'
            })
    
    return issues
```

### 5.2 Check for internal contradictions

```python
# Extract all claims
claims = extract_claims(body)

# Check each pair for contradiction
for i, claim1 in enumerate(claims):
    for claim2 in claims[i+1:]:
        if are_contradictory(claim1, claim2):
            issues.append({
                'severity': 'ERROR',
                'dimension': 'Coherence',
                'issue': 'Internal contradiction detected',
                'evidence': f'Claim 1: {claim1}\nClaim 2: {claim2}',
                'suggested_fix': 'Resolve contradiction or clarify context'
            })
```

### 5.3 Check transition quality

```python
sections = parse_markdown_sections(body)
section_list = list(sections.values())

for i in range(len(section_list) - 1):
    current = section_list[i]
    next_section = section_list[i+1]
    
    # Check if transition exists
    if not has_transition(current, next_section):
        issues.append({
            'severity': 'INFO',
            'dimension': 'Coherence',
            'issue': f'Weak transition between sections {i+1} and {i+2}',
            'evidence': f'End of section {i+1}: {current[-100:]}\nStart of section {i+2}: {next_section[:100]}',
            'suggested_fix': 'Add transitional sentence or phrase'
        })
```

---

## Step 6: Validate Vietnamese Quality

### 6.1 Check grammar using language model

```python
def validate_vietnamese_quality(file):
    issues = []
    body = file['body']
    
    # Use Vietnamese language model
    prompt = f"""
Kiểm tra ngữ pháp tiếng Việt của văn bản sau:

{body}

Tìm lỗi:
1. Chủ ngữ - động từ không khớp
2. Thì không đúng
3. Lỗi chính tả
4. Cụm từ không tự nhiên

Output: Danh sách lỗi tìm thấy (hoặc "OK" nếu không có lỗi)
"""
    
    result = llm_call(prompt, model='gemini-2.0-flash')  # Better for Vietnamese
    
    if result != "OK":
        for error in parse_grammar_errors(result):
            issues.append({
                'severity': 'WARNING',
                'dimension': 'Vietnamese',
                'issue': error['description'],
                'evidence': error['context'],
                'suggested_fix': error['correction']
            })
    
    return issues
```

### 6.2 Check for machine translation artifacts

```python
# Common machine translation patterns
mt_patterns = [
    r'\b(?:được|bị)\s+(?:được|bị)\b',  # Double passive
    r'\b(?:của|về)\s+(?:của|về)\b',    # Double preposition
    r'\b(?:rất|quá)\s+(?:rất|quá)\b',  # Double intensifier
]

for pattern in mt_patterns:
    matches = re.finditer(pattern, body)
    for match in matches:
        issues.append({
            'severity': 'INFO',
            'dimension': 'Vietnamese',
            'issue': 'Possible machine translation artifact',
            'evidence': extract_context(match.group(), body),
            'suggested_fix': 'Rephrase more naturally'
        })
```

### 6.3 Check technical term preservation

```python
# Technical terms should stay in English
tech_terms_en = ['embedding', 'fine-tuning', 'prompt injection', 'RAG', 'LLM']

for term in tech_terms_en:
    # Check if term was translated to Vietnamese
    vn_translations = get_vietnamese_translation(term)
    
    for vn_term in vn_translations:
        if vn_term in body and term not in body:
            issues.append({
                'severity': 'WARNING',
                'dimension': 'Vietnamese',
                'issue': f'Technical term translated: "{vn_term}" should be "{term}"',
                'evidence': extract_context(vn_term, body),
                'suggested_fix': f'Use English term "{term}" instead'
            })
```

---

## Step 7: Score and Filter Issues

### 7.1 Assign severity scores

```python
severity_scores = {
    'ERROR': 3,
    'WARNING': 2,
    'INFO': 1
}

for issue in all_issues:
    issue['score'] = severity_scores[issue['severity']]
```

### 7.2 Sort issues

```python
# Sort by: severity (high to low), then file path (alphabetical)
all_issues.sort(key=lambda x: (-x['score'], x['file']))
```

### 7.3 Apply report limit

```python
# Daily validation: limit to 20 issues
max_issues = 20

if len(all_issues) > max_issues:
    reported_issues = all_issues[:max_issues]
    
    # Log truncation
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

report = f"""# Output Validation — {report_date}

**Status:** pending
**Issues found:** {len(reported_issues)}
**Created:** {report_time}
**Validator:** output-validator

**Files checked:** {len(files)} ({len(new_files)} new, {len(existing_files)} existing)

---

"""

for i, issue in enumerate(reported_issues, 1):
    report += f"""## Issue {i}: {issue['issue']}

**File:** {issue['file']}
**Severity:** {issue['severity']}
**Dimension:** {issue['dimension']}
**Issue:** {issue['issue']}
**Evidence:**
```
{issue['evidence']}
```
**Suggested fix:** {issue['suggested_fix']}

---

"""
```

### 8.2 Write report file

```bash
report_file="wiki/reviews/${report_date}_output-report.md"

cat > "$report_file" << 'EOF'
$report
EOF
```

### 8.3 Verify report written

```bash
test -f "$report_file" && echo "✓ Report written"
```

---

## Step 9: Update _action-required.md

### 9.1 Read current action file

```bash
action_file="wiki/reviews/_action-required.md"
content=$(cat "$action_file")
```

### 9.2 Build new entry

```python
new_entry = f"""
### {entry_number}. Output Validation — {report_date}

**File:** [{report_date}_output-report.md]({report_date}_output-report.md)
**Status:** pending
**Created:** {report_time}
**Issues:** {len(reported_issues)} ({error_count} ERROR, {warning_count} WARNING, {info_count} INFO)
**Files affected:** {len(affected_files)}

**Summary:**
- {error_count} critical quality issues
- {warning_count} improvements needed
- {info_count} suggestions

**Actions:**
- `approve output` — approve this report
- `reject output` — reject this report
- `show output` — show full report details

---
"""
```

### 9.3 Insert into "Pending Reports" section

```python
# Find insertion point (after "## Pending Reports (N)")
insert_pos = content.find("## Pending Reports")
insert_pos = content.find("\n\n", insert_pos) + 2

# Insert new entry
content = content[:insert_pos] + new_entry + content[insert_pos:]

# Update count
pending_count = count_pending_reports(content) + 1
content = content.replace(
    "## Pending Reports (N)",
    f"## Pending Reports ({pending_count})"
)

# Update timestamp
content = update_timestamp(content)
```

### 9.4 Update counts and timestamp

```python
# Update pending count
pending_count = count_pending_reports(content) + 1
content = content.replace(
    "## Pending Reports (N)",
    f"## Pending Reports ({pending_count})"
)

# Update timestamp
content = update_timestamp(content)
```

### 9.5 Cleanup old "Recently Applied" entries

Remove entries older than 7 days from "Recently Applied" section.

```python
def cleanup_recently_applied(content):
    """
    Remove entries from "Recently Applied" section that are older than 7 days.

    Rules:
    - Only affects "Recently Applied" section
    - Never touches "Pending Reports" (no time limit)
    - Idempotent (safe to run multiple times)
    - Runs every time validator updates _action-required.md
    """

    # Parse "Recently Applied" section
    entries = parse_recently_applied_entries(content)

    # Calculate cutoff date (7 days ago)
    cutoff_date = datetime.now() - timedelta(days=7)

    removed_count = 0

    # Remove entries older than 7 days
    for entry in entries:
        # Parse applied date from entry
        # Format: "**Applied:** YYYY-MM-DD HH:MM:SS"
        applied_match = re.search(r'\*\*Applied:\*\* (\d{4}-\d{2}-\d{2})', entry)

        if not applied_match:
            continue

        entry_date = datetime.strptime(applied_match.group(1), '%Y-%m-%d')

        if entry_date < cutoff_date:
            # Remove this entry
            content = remove_recently_applied_entry(content, entry)
            removed_count += 1

            # Log cleanup
            entry_title = extract_entry_title(entry)
            log(f"[CLEANUP] Removed old entry: {entry_title} ({entry_date.strftime('%Y-%m-%d')})")

    if removed_count > 0:
        log(f"[CLEANUP] Total removed: {removed_count} entries older than 7 days")

    return content


def parse_recently_applied_entries(content):
    """Extract all entries from Recently Applied section."""
    # Find "## Recently Applied" section
    section_start = content.find("## Recently Applied")

    if section_start == -1:
        return []

    # Find next ## section or end of file
    section_end = content.find("\n##", section_start + 1)
    if section_end == -1:
        section_end = len(content)

    section_content = content[section_start:section_end]

    # Split by ### (entry headers)
    entries = re.split(r'\n### ', section_content)[1:]  # Skip section header

    return entries


def remove_recently_applied_entry(content, entry):
    """Remove a specific entry from Recently Applied section."""
    # Find entry in content
    entry_pattern = re.escape(entry[:50])  # Use first 50 chars as pattern

    # Find and remove entry (including ### header)
    content = re.sub(
        r'### ' + entry_pattern + r'.*?(?=\n###|\n##|\Z)',
        '',
        content,
        flags=re.DOTALL
    )

    return content
```

**Cleanup behavior:**

- **Runs every time** validator updates _action-required.md (daily 22:00)
- **Idempotent** — safe to run multiple times per day (other validators also cleanup at 22:30, 23:00)
- **Only affects "Recently Applied"** — never touches "Pending Reports"
- **7-day retention** — entries older than 7 days are removed
- **Preserves archives** — archived reports in `wiki/reviews/archive/` are never deleted

**Example cleanup log:**

```
[CLEANUP] Removed old entry: 2026-05-01 Output Validation (2026-05-01)
[CLEANUP] Removed old entry: 2026-04-30 Format Validation (2026-04-30)
[CLEANUP] Total removed: 2 entries older than 7 days
```

### 9.6 Write updated action file

```bash
cat > "$action_file" << 'EOF'
$content
EOF
```

---

## Step 10: Send Telegram Notification

### 10.1 Build notification message

```python
message = f"""📋 Output validation complete

- Issues found: {len(reported_issues)} ({error_count} ERROR, {warning_count} WARNING, {info_count} INFO)
- Files checked: {len(files)} ({len(new_files)} new since last run)
- Report: wiki/reviews/{report_date}_output-report.md

Review: wiki/reviews/_action-required.md

Commands:
- 'approve output' to approve report
- 'show output' for details
- 'reject output' to reject
"""
```

### 10.2 Send to Telegram

```python
send_telegram(message)
```

---

## Step 11: Log to Memory

### 11.1 Append to MEMORY.md

```markdown
## {report_time} — Output validation

- **Files checked:** {len(files)} ({len(new_files)} sources + {len(new_concepts)} concepts)
- **New files:** {len(new_files)} (compiled today)
- **Issues found:** {len(reported_issues)} ({error_count} ERROR, {warning_count} WARNING, {info_count} INFO)
- **Report:** wiki/reviews/{report_date}_output-report.md
- **Top issues:** {top_3_issue_types}
```

---

## Error Handling

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

### LLM call failures

```python
try:
    result = llm_call(prompt, model='claude-3-5-sonnet')
except Exception as e:
    log(f"[WARNING] LLM call failed for {file}: {e}")
    # Skip this check, continue with others
    continue
```

### Report write failures

```python
try:
    write_file(report_file, report)
except Exception as e:
    log(f"[FATAL] Cannot write report: {e}")
    send_telegram(f"[FATAL] Output validation failed: cannot write report")
    exit(1)
```

---

## Performance Optimization

### Batch LLM calls

```python
# Instead of calling LLM per file
for file in files:
    result = llm_call(validate_coherence_prompt(file))

# Batch 5-10 files per call
for batch in chunk(files, 5):
    results = llm_call(validate_coherence_batch_prompt(batch))
    for file, result in zip(batch, results):
        process_result(file, result)
```

### Cache validation patterns

```python
# Cache common patterns to avoid re-checking
pattern_cache = {}

def check_pattern(pattern, text):
    if pattern not in pattern_cache:
        pattern_cache[pattern] = re.compile(pattern)
    return pattern_cache[pattern].search(text)
```

### Skip unchanged files

```python
# For existing files, check if content changed
last_validation = load_last_validation_state()

for file in existing_files:
    file_hash = hash_file(file)
    
    if file_hash == last_validation.get(file):
        # File unchanged, skip validation
        continue
    
    # File changed, validate
    validate(file)
    last_validation[file] = file_hash

save_validation_state(last_validation)
```

---

## Validation Checklist

Before marking validation complete:

- [ ] All new files validated (4 dimensions)
- [ ] All existing files quick-scanned (completeness)
- [ ] Issues sorted by severity
- [ ] Report written to `wiki/reviews/`
- [ ] `_action-required.md` updated
- [ ] Telegram notification sent
- [ ] MEMORY.md entry added
- [ ] No files modified (read-only validator)

---

## Related Documentation

- [SKILL.md](SKILL.md) — Output Validator overview
- [validation-criteria.md](validation-criteria.md) — Detailed quality rubrics
- [examples.md](examples.md) — Sample reports and issues
