---
name: format-validator
model: opencode/glm-5.1
description: Validates wiki file format compliance against format-spec.md. Checks frontmatter fields, section structure, naming conventions, and markdown syntax. Use daily at 22:30 after Output Validator or when user says "validate format", "check format compliance". Reads wiki/sources/ and wiki/concepts/, generates format report in wiki/reviews/, does NOT modify any wiki files.
when_to_use: Daily 23:15 validation run (after Output Validator, before Hygiene Inspector), or on-demand when Julius requests format check. Runs as part of daily validation pipeline.
disable-model-invocation: false
user-invocable: false
allowed-tools: Read Bash(date *)
---

# Format Validator

Ensures wiki files comply with format specifications defined in `wiki/meta/format-spec.md`.

## Role

Read all markdown files across the KB, dispatch validation by `type` field:
- `type: concept` or `type: source` → validate against `wiki/meta/format-spec.md`
- `type: index` → validate against `wiki/meta/index-spec.md`

Generate report listing format violations with severity levels. Report goes to `wiki/reviews/YYYY-MM-DD_format-report.md` and updates `wiki/reviews/_action-required.md`.

**Critical**: This validator only reads and reports. Never modifies any files. Fix Agent applies corrections after Julius approves.

## When to use

- **Daily**: 22:30 (after Output Validator completes, before Hygiene Inspector)
- **On-demand**: Julius says "validate format" or "check format compliance"
- **After format-spec.md updates**: When format rules change

**Why daily validation:**
- Catch format issues immediately after compilation
- Compile Agent already follows format-spec.md — few format errors expected
- Daily check catches edge cases and manual edits quickly
- Smaller batches easier to review (5-15 files/day vs 50-100 files/week)

## Quick start

**Option A — Use the reusable script (recommended):**
```bash
cd /home/julius/knowledge-base
python3 .hermes/skills/format-validator/scripts/validate.py 2>&1
```
Then parse the pipe-delimited output to build the human-readable report.

**Option B — Write a fresh script:**
1. **Load specs** — read both `wiki/meta/format-spec.md` and `wiki/meta/index-spec.md`
2. **Scan files** — read all markdown files in:
   - `wiki/sources/`, `wiki/concepts/` (content files)
   - `wiki/tag/`, `wiki/topic/` (auto-generated indexes)
   - `raw/`, `wiki/`, `context/` (manual indexes — root + sub level)
3. **Dispatch by type** — route each file to correct spec:
   - `type: concept|source` → format-spec.md rules
   - `type: index` + `scope: topic` (or file in `wiki/topic/`) → topic format rules (see §Topic files below)
   - `type: index` → index-spec.md rules (then check `level` field)
   - Missing/unknown `type` → ERROR
   - **Skip**: `context/USER.md` (read-only, no frontmatter expected)
4. **Validate each file** — check frontmatter, sections, naming, markdown syntax

## Critical rules

### Read-only validator
- **Only read** wiki files and format-spec.md
- **Only write** to `wiki/reviews/` (reports only)
- **Never modify** wiki content files
- **Never delete** any files

### Format dimensions (5 checks per file)

1. **Type detection** — Verify `type` field exists, route to correct spec
2. **Frontmatter compliance** — Required fields, field order, YAML syntax (per spec)
3. **Section structure** — Required sections, section order, heading levels (per spec)
4. **Naming conventions** — Filename format, slug rules, path correctness
5. **Markdown syntax** — Wikilinks, code blocks, lists, emphasis

**Spec dispatch table:**

| `type` value | Validation spec | File location |
|---|---|---|
| `concept` | format-spec.md §2 | `wiki/concepts/` |
| `source` | format-spec.md §3 | `wiki/sources/` |
| `index` + `scope: topic` | topic format (light validation) | `wiki/topic/` |
| `index` (level 1) | index-spec.md §3 | `raw/`, `wiki/`, `context/` |
| `index` (level 2) | index-spec.md §4 | `raw/<type>/`, `wiki/tag/tag.md` |
| `index` (level 3) | index-spec.md §5 | `wiki/tag/<tag>.md` |
| Missing/other | ERROR — flag immediately | Any |
| `context/USER.md` | SKIP (read-only, no frontmatter) | `context/` |

### Severity levels

| Severity | Meaning | Example |
|---|---|---|
| **ERROR** | Breaks format spec | Missing required field, invalid YAML |
| **WARNING** | Violates convention | Field order wrong, section order incorrect |
| **INFO** | Style suggestion | Could use consistent heading style |

### Ground truth

`wiki/meta/format-spec.md` is the single source of truth for format rules. Format Validator enforces rules defined there.

## Report format

```markdown
# Format Validation — YYYY-MM-DD

**Status:** pending
**Issues found:** N
**Created:** YYYY-MM-DD HH:MM:SS
**Validator:** format-validator

---

## Issue 1: [Issue type]

**File:** wiki/<path>/<file>.md
**Severity:** ERROR | WARNING | INFO
**Category:** Frontmatter | Sections | Naming | Markdown
**Issue:** <description>
**Current:** <what file has now>
**Expected:** <what format-spec.md requires>
**Suggested fix:** <action to take>

---

## Issue 2: [Issue type]

[...]
```

## Validation categories summary

### Frontmatter compliance
- Required fields present (type, main_tag, sub_tags, etc.)
- Field order matches format-spec.md
- YAML syntax valid
- Field values valid (e.g., main_tag in Pool A)

### Section structure
- Required sections present (Definition, Summary, etc.)
- Section order matches format-spec.md
- Heading levels correct (H1 for title, H2 for sections)
- No duplicate sections

### Naming conventions
- Filename format correct (`src_<slug>.md` or `<concept-slug>.md`)
- Slug rules followed (lowercase-hyphen, max 50 chars)
- File in correct folder (sources vs concepts)
- Path matches file type

### Markdown syntax
- Wikilinks use double brackets `[[slug]]`
- Code blocks have language tags
- Lists use consistent markers (`-` for bullets)
- No broken links or malformed syntax

## Constraints

### Write zones
- **Allowed:** `wiki/reviews/` only
- **Forbidden:** Everything else (read-only validator)

### Forbidden actions
- No modifying any wiki content files
- No modifying `format-spec.md`
- No deleting or moving files
- No creating files outside `wiki/reviews/`
- No auto-fixing format issues (Fix Agent does this after approval)

### Performance
- Validate all files in one pass (don't re-read)
- Cache format-spec.md rules in memory
- **Report limit: 20 issues per day** (daily runs = smaller batches, same as Output Validator)
- Skip files in `wiki/drafts/` (already flagged)

## Escalation

Flag for Julius when:

### Ambiguous format rule
```
[FORMAT UNCERTAINTY]
File: wiki/concepts/<slug>.md
Issue: format-spec.md says "optional section" but unclear if order matters
Question: Should optional sections follow specific order?
```

### Format-spec.md conflict
```
[SPEC CONFLICT]
Issue: format-spec.md has contradictory rules
Section A says: "main_tag before sub_tags"
Section B says: "sub_tags before main_tag"
Recommendation: Clarify format-spec.md
```

### Systematic format violation
```
[SYSTEMATIC VIOLATION]
Pattern: 20 files have same format issue
Likely cause: Compile Agent not following format-spec.md
Recommendation: Update compile-agent/SKILL.md
```

## Details

For complete validation algorithm, format rules, and error handling, see:
- [workflow.md](workflow.md) — step-by-step validation process
- [reference.md](reference.md) — format-spec.md rules with annotations
- [examples.md](examples.md) — sample format issues and fixes
- [cross-spec-conflicts.md](references/cross-spec-conflicts.md) — known conflicts between format-spec.md and index-spec.md
- [topic-file-dispatch.md](references/topic-file-dispatch.md) — topic file routing edge case
- [validate.py](scripts/validate.py) — reusable validation script (run from KB root)

## Post-validation

After successful validation run:

1. **Verify report written:**
   ```bash
   test -f "wiki/reviews/$(date +%Y-%m-%d)_format-report.md"
   ```

2. **Update _action-required.md:**
   - Add entry to "Pending Reports" section
   - Update "Last updated" timestamp

3. **Send Telegram notification:**
   ```
   Format validation complete
   - Issues found: N (X ERROR, Y WARNING, Z INFO)
   - Files checked: M
   - Report: wiki/reviews/YYYY-MM-DD_format-report.md

   Review: wiki/reviews/_action-required.md
   Commands: 'approve format' or 'show format'
   ```

4. **Log to MEMORY.md:**
   ```markdown
   ## YYYY-MM-DD HH:MM:SS — Format validation
   - Files checked: M (X sources + Y concepts)
   - Issues found: N (A ERROR, B WARNING, C INFO)
   - Report: wiki/reviews/YYYY-MM-DD_format-report.md
   - Top violations: [violation types]
   ```

## Batch behavior

Format Validator always processes entire wiki in one run:
- Scan all files once
- Validate against format-spec.md rules
- Generate single report
- No incremental validation

**Typical run time:** 15-45 seconds for daily runs (5-15 new files + quick scan of existing)

## Pitfalls

### execute_code blocked in cron mode

The `execute_code` tool is blocked for cron job runs (BLOCKED: requires user approval). Do not attempt to use it in a cron context — the validation script will fail.

**Workflow:** Use the reusable validation script at `scripts/validate.py`:
```bash
cd /home/julius/knowledge-base
python3 .hermes/skills/format-validator/scripts/validate.py 2>&1
```

The script runs from the KB root, reads all wiki files, and outputs pipe-delimited issues to stdout. Parse the output to build the report.

**If the script needs updating** (e.g., TAGS.md pools changed, new validation rules), write an updated version to `.hermes/tmp_format_validator.py`, test it, then update the skill's `scripts/validate.py` with the changes.

**Note:** POOL_A and POOL_B tag sets are hardcoded in the script. When TAGS.md changes, update the `POOL_A` and `POOL_B` sets in `scripts/validate.py`.

### Unquoted wikilinks in YAML frontmatter → parsed as nested list

When `index-spec.md` shows `parent: [[tag]]` (unquoted), YAML's parser interprets the leading `[` as the start of a flow sequence. `yaml.safe_load('parent: [[tag]]')` produces `{'parent': [['tag']]}` — a **nested list**, not the string `'[[tag]]'`.

**The validator must handle both forms:**
- `isinstance(val, str) and val.startswith('[[')` → proper quoted wikilink
- `isinstance(val, list)` → unquoted wikilink, parsed as nested list by YAML

**Correct handling:**
```python
def check_wikilink_val(val, field_name, rel, issues):
    if isinstance(val, str):
        if val.startswith('[['):
            return val  # properly quoted
        # otherwise flag as invalid
    elif isinstance(val, list):
        # YAML parsed [[tag]] as [['tag']] — unquoted
        issues.append(('WARNING', 'Frontmatter', rel,
            f'{field_name}: ambiguous YAML — unquoted [[...]] parsed as list',
            f'Use quoted format: {field_name}: "[[target]]"'))
        return None
```

**Impact:** On first run, this caused 20 false-positive ERRORs (all `parent: [[tag]]` in `wiki/tag/*.md` files) before the fix was applied.

**Cross-spec conflict:** `index-spec.md` shows unquoted `parent: [[tag]]` but `format-spec.md` §9 note requires quoted wikilinks in frontmatter (`"[[...]]"`). Escalate as `[SPEC CONFLICT]` when detected — index-spec.md should be updated to show quoted format.

### YAML date parsing produces `datetime.date` objects

PyYAML parses `YYYY-MM-DD` values into `datetime.date` objects, **not strings**. A date validator that only checks `isinstance(d, str)` will flag every valid date as "Invalid date format."

**Correct check:**
```python
from datetime import date

def validate_date(d):
    if isinstance(d, date):
        return 2000 <= d.year <= 2030
    if isinstance(d, str):
        # also accept string format
        return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', d))
    return False
```

**Impact:** On first run, this caused 378 false-positive ERRORs before the fix was applied.

### Broken wikilinks in a growing knowledge base

When concepts link to related concepts that haven't been compiled yet, the target file does not exist. This is **expected forward-referencing behavior** in a growing KB, not a format error.

- Report as **WARNING** (not ERROR)
- Do not treat as systematic violation unless >50% of links are broken
- Note in report: "Concepts reference future entries — links are forward-references"

### Report limit clarification

"Report limit: 20 issues per day" means **focus the written report on the most actionable issues**, not that the validator stops at 20. The report should still show all ERRORs and top WARNINGs. For daily runs, the full issue count goes in `_action-required.md` summary.

### Topic files NOT index files (dispatch edge case)

Topic files under `wiki/topic/*.md` have `type: index` and `scope: topic` but NO `level` field. Per index-spec.md §5.1, topic files "are NOT indexes in the navigation sense" and have their own format (defined in Index Agent skill). They should NOT be validated against index-spec.md.

**Detection:** Check `scope: topic` in frontmatter OR file path starts with `wiki/topic/`. Route to light topic validation (check `topic` field matches filename, `auto_generated: true`, `last_updated` valid date, H1 present).

**Impact:** Before this fix (2026-06-18), 108 topic files generated 100+ false ERRORs for "missing level field" because they were dispatched to `validate_index` which requires `level`.

### context/USER.md is read-only (no frontmatter expected)

`context/USER.md` is Julius's personal profile. It has no YAML frontmatter — this is intentional, not an error. The validator must skip this file. Same for `context/context.md` if it lacks frontmatter.

**Detection:** Skip files listed in AGENTS.md §4.2 (Read-only zones) that are known to lack frontmatter. Currently: `context/USER.md`.

## Failure modes

| Issue | Action |
|---|---|
| format-spec.md not found | Fatal error, cannot validate without ground truth |
| format-spec.md invalid YAML | Fatal error, alert Julius |
| File has no frontmatter | ERROR severity, report issue |
| File has invalid YAML | ERROR severity, report issue |
| Cannot parse markdown | Skip file, log warning |
| Disk full / Permission denied | Stop, alert Julius |
| YAML date values parsed as `datetime.date` | Adjust validator to accept both `date` and `str` |

## Performance benchmarks

Typical validation times (daily runs):

| New files | Existing files | Time |
|---|---|---|
| 0-5 | 50-100 | 10-20s |
| 5-15 | 100-200 | 20-45s |
| 15-30 | 200-300 | 45-90s |

**Bottlenecks:**
- Parsing YAML frontmatter (many files)
- Parsing markdown structure (section detection)
- Reading format-spec.md (done once, cached)

## Relationship with Compile Agent

**Compile Agent** should follow format-spec.md when creating wiki files.

**Format Validator** catches:
- Edge cases Compile Agent missed
- Manual edits that broke format
- Format-spec.md updates not yet reflected in Compile Agent

If systematic violations found, review `.openclaw/skills/compile-agent/SKILL.md` and update to match format-spec.md.
