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

Read all wiki files (`wiki/sources/*.md` + `wiki/concepts/*.md`), validate format compliance, generate report listing format violations with severity levels. Report goes to `wiki/reviews/YYYY-MM-DD_format-report.md` and updates `wiki/reviews/_action-required.md`.

**Critical**: This validator only reads and reports. Never modifies wiki files. Fix Agent applies corrections after Julius approves.

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

1. **Load format-spec.md** — read ground truth format rules
2. **Scan wiki files** — read all `wiki/sources/*.md` + `wiki/concepts/*.md`
3. **Validate each file** — check frontmatter, sections, naming, markdown syntax
4. **Score violations** — assign severity (ERROR/WARNING/INFO)
5. **Generate report** — write to `wiki/reviews/YYYY-MM-DD_format-report.md`
6. **Update action file** — add entry to `wiki/reviews/_action-required.md`
7. **Send notification** — Telegram alert to Julius
8. **Log** to `.hermes/MEMORY.md`

## Critical rules

### Read-only validator
- **Only read** wiki files and format-spec.md
- **Only write** to `wiki/reviews/` (reports only)
- **Never modify** wiki content files
- **Never delete** any files

### Format dimensions (4 checks per file)

1. **Frontmatter compliance** — Required fields, field order, YAML syntax
2. **Section structure** — Required sections, section order, heading levels
3. **Naming conventions** — Filename format, slug rules, path correctness
4. **Markdown syntax** — Wikilinks, code blocks, lists, emphasis

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
- **Forbidden:** `wiki/sources/`, `wiki/concepts/`, `wiki/drafts/`, `wiki/tag/`, `wiki/topic/`, `wiki/meta/`

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

## Failure modes

| Issue | Action |
|---|---|
| format-spec.md not found | Fatal error, cannot validate without ground truth |
| format-spec.md invalid YAML | Fatal error, alert Julius |
| File has no frontmatter | ERROR severity, report issue |
| File has invalid YAML | ERROR severity, report issue |
| Cannot parse markdown | Skip file, log warning |
| Disk full / Permission denied | Stop, alert Julius |

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
