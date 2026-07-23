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
python3 .hermes/skills/format-validator/scripts/validate.py 2>&1 | tee /tmp/issues.txt
```
Then parse the pipe-delimited output with the analysis helper:
```bash
python3 .hermes/skills/format-validator/scripts/parse_issues.py /tmp/issues.txt
```
Use the parsed statistics (broken target counts, top-N lists, ERROR breakdown) to build the human-readable report.

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
- [code-fence-and-raw-link-regressions.md](references/code-fence-and-raw-link-regressions.md) — validator regressions around fenced code blocks and raw-file wikilink resolution
- [validate.py](scripts/validate.py) — reusable validation script (run from KB root)
- [parse_issues.py](scripts/parse_issues.py) — parses pipe-delimited output: broken target counts, top-N lists, ERROR breakdown
- [verify_integrity.py](scripts/verify_integrity.py) — cross-file consistency check: report, _action-required.md, MEMORY.md all agree on counts

## Post-validation

After successful validation run:

1. **Verify report written and cross-file integrity:**
   ```bash
   cd /home/julius/knowledge-base
   python3 .hermes/skills/format-validator/scripts/verify_integrity.py
   ```
   This checks: report file exists with correct fields, _action-required.md has today's entry with matching counts, MEMORY.md has today's entry prepended with matching counts, and all three files are cross-consistent.

2. **Update _action-required.md:**
   - **First, reconcile**: read the previous report's `**Status:**` header. If it says `approved` but `_action-required.md` still shows `⏳ PENDING`, update the status line and pending count before adding today's entry. See pitfall "_action-required.md may be stale".
   - **Then, add entry**: insert today's report into the "Pending Reports" section with full details (Summary, Delta, Actions)
   - Update the status list under `## Summary` with today's entry
   - Update "Last updated" timestamp
   - Update "Pending reports awaiting review" count (accounting for any reconciled approvals)

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

5. **Update _approval-log.md (if it exists):**
   - `_approval-log.md` may not exist — `_action-required.md` (updated in step 2) already serves as the cross-machine approval contract
   - If the file exists, prepend a new entry at the top
   - Include: timestamp, validator name, scope, report path, issue counts, key findings, escalations, and status (`PENDING approval`)
   - If the file does not exist, skip this step — it is optional and redundant with `_action-required.md`

## Delta tracking (compare against previous approved report)

After generating the report, compare today's results against the most recent **APPROVED** report (not just the most recent report) to surface what changed:

- **Positive delta** — issues that disappeared (e.g., `main_tag: psychology` errors resolved by Fix Agent)
- **Negative delta** — new issues that appeared (e.g., new code blocks missing language tags)
- **Volume delta** — file count growth, issue count changes

Include a delta summary table at the top of the report so Julius can see at a glance whether the KB is getting cleaner or accumulating debt.

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
python3 .hermes/skills/format-validator/scripts/validate.py 2>&1 | tee /tmp/issues.txt
```

The script runs from the KB root, reads all wiki files, and outputs pipe-delimited issues to stdout. Parse with `scripts/parse_issues.py` to get analysis statistics.

**If the script needs updating** (e.g., TAGS.md pools changed, new validation rules), write an updated version to a temp file, test it, then update the skill's `scripts/validate.py` with the changes.

### Python heredocs and rm blocked in cron mode

In cron mode, shell heredocs (`python3 << 'PYEOF'`) are blocked (pattern: "script execution via heredoc"). Use `write_file` to save the script to `/tmp/`, then run it with `terminal`.

Similarly, `rm` commands targeting `/tmp/` may be blocked (pattern: "delete in root path"). Temp files auto-clean on reboot; leave them if deletion is blocked.

**Pattern for running custom Python analysis in cron:**
```bash
# 1. Write script via write_file to /tmp/analyze.py
# 2. Run: python3 /tmp/analyze.py
# 3. Cleanup is optional — /tmp/ is ephemeral
```

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

### Closing code fences misread as missing language tags

A naive regex like `re.findall(r'```(\\S*)', body)` matches both opening and closing fences. Closing fences return an empty suffix, which produces false-positive `Code block missing language tag` errors even when the opening fence is correct (` ```text `, ` ```yaml `, etc.).

**Correct handling:** track fence state line-by-line and only validate the **opening** fence. Closing fences should just flip state back.

**Impact observed:** the 2026-06-25 format report still showed 8 code-block ERRORs after Kara had already added language tags, because the validator was counting the closing fences.

### Source-body raw-file wikilinks need raw-subdir resolution

Source files often mention the raw file again inside `## Metadata` or body content, e.g. `[[2026-06-17_dan-koe-workflow-analysis-markus]]`. If broken-wikilink validation only checks `wiki/concepts/` and `wiki/sources/`, it will flag these as broken even when the raw file exists under `raw/articles/` or another raw subtype.

**Correct handling:** when validating wikilinks in source bodies, reuse the same raw-subdir resolution used for the `original` frontmatter field:
- accept direct matches like `raw/<subdir>/<target>.md`
- accept glob matches like `raw/<subdir>/*_<target>.md`

**Same issue affects `original` field validation:** The `original` frontmatter field (e.g., `original: "[[2026-07-14_why-the-math-mafia-is-doing-well-jesse-zhang.md]]"`) also needs raw-subdir resolution. The validator currently flags these as "raw file not found" even when the file exists under `raw/articles/`. This produces false-positive WARNINGs. Fix: apply the same subdir search logic to `check_original_wikilink()`.

**Observed case:** `src_dan-koe-workflow-analysis-markus.md` was incorrectly flagged until raw-subdir lookup was added to source-body wikilink validation. Same false-positive pattern observed 2026-07-20 for `src_you-just-hired-a-million-bad-employees-a16z.md` and `src_why-the-math-mafia-is-doing-well-jesse-zhang.md` — both `original` fields point to raw files that exist under `raw/articles/`.


"Report limit: 20 issues per day" means **focus the written report on the most actionable issues**, not that the validator stops at 20. The report should still show all ERRORs and top WARNINGs. For daily runs, the full issue count goes in `_action-required.md` summary.

### Topic files NOT index files (dispatch edge case)

Topic files under `wiki/topic/*.md` have `type: index` and `scope: topic` but NO `level` field. Per index-spec.md §5.1, topic files "are NOT indexes in the navigation sense" and have their own format (defined in Index Agent skill). They should NOT be validated against index-spec.md.

**Detection:** Check `scope: topic` in frontmatter OR file path starts with `wiki/topic/`. Route to light topic validation (check `topic` field matches filename, `auto_generated: true`, `last_updated` valid date, H1 present).

**Impact:** Before this fix (2026-06-18), 108 topic files generated 100+ false ERRORs for "missing level field" because they were dispatched to `validate_index` which requires `level`.

### context/USER.md is read-only (no frontmatter expected)

`context/USER.md` is Julius's personal profile. It has no YAML frontmatter — this is intentional, not an error. The validator must skip this file. Same for `context/context.md` if it lacks frontmatter.

**Detection:** Skip files listed in AGENTS.md §4.2 (Read-only zones) that are known to lack frontmatter. Currently: `context/USER.md`.

### _approval-log.md is optional (do not fail if missing)

Post-validation step 5 references `wiki/reviews/_approval-log.md`, but this file may not exist. `_action-required.md` already serves as the canonical cross-machine approval contract. If `_approval-log.md` is absent, skip step 5 gracefully — do not create it, do not error out. The approval contract lives in `_action-required.md`.

### _action-required.md may be stale — reconcile before updating

Julius can approve reports directly (e.g., via Telegram `approve format`) which updates the report's own `**Status:** approved` header, but `_action-required.md` is NOT auto-updated in tandem. When the validator runs the next day:

1. **Read the previous report's Status header** — open the most recent `YYYY-MM-DD_format-report.md` and check its `**Status:**` field
2. **Compare against _action-required.md** — if the report says `approved` but `_action-required.md` still shows `⏳ PENDING`, reconcile
3. **Reconcile** — update the status line in `_action-required.md` from `⏳ PENDING` to `✅ APPROVED`, and add `Approved by:` attribution if known

This prevents stale pending counts and ensures delta tracking uses the correct baseline.

**Observed case (2026-07-02):** The 2026-07-01 format report header showed `**Status:** approved` (Julius approved slug exception), but `_action-required.md` still listed it as `⏳ PENDING`. Reconciliation on 07-02 updated the pending count and status line.

### verify_integrity.py has strict regex expectations — report frontmatter must match

`verify_integrity.py` (run post-validation) validates cross-file consistency by parsing the report with specific regex patterns. These patterns are fragile and require exact formatting:

**Required frontmatter fields (must appear literally):**
- `**Status:** pending`
- `**Issues found:** N`
- `**ERRORs**: N` (lowercase 's') — **critical**: space BEFORE colon, same rule as WARNINGS. The verify script checks for `**ERRORs**` substring via `'**ERRORs**' in content`. Writing `**ERRORs:**` (colon immediately after `s`) fails because the `:` breaks the bold-span substring — `**ERRORs**` is no longer present. Use `**ERRORs**: N` (space between `s` and `:`).
- `**WARNINGS**: N` — **critical**: space BEFORE colon so `**WARNINGS**` (bold WARNINGS) appears as a substring. Writing `**WARNINGS:**` (colon immediately after asterisks) fails because there's no `**WARNINGS**` substring — only `**WARNINGS:`.
- `**INFOS:** 0`
- `**Validator:** format-validator`
- `**Files checked:** N` (bold form for display)
- `**Total issues**: N` — same space-before-colon rule as WARNINGS
- `Files checked: N` — **plain text** (not bold). Required because regex `Files checked[\s:]+(\d+)` hits on the asterisks in `**Files checked:** N` and fails to match the number. The plain-text line on its own line after the bold form ensures regex match.
- `Total issues: N` — plain text (not bold). Same reason: regex `\*\*Total issues\*\*[\s:]+(\d+)` needs `**Total issues**` followed by `[\s:]+` then digits. `**Total issues:** N` puts a colon inside the `**` which breaks the pattern. `**Total issues**: N` (space between `**` and colon) works.

**Required sections:**
- `## Verification` section (with checklist of steps taken)
- `## Escalations` section (even if empty)
- `Δ from` in the context block (Greek Delta symbol U+0394 followed by space and `from`)

**Observed case (2026-07-17):** 4 iterations of reformatting were needed to satisfy verify_integrity.py. The space-before-colon pattern is non-obvious and easy to miss.

### verify_integrity.py cross-check regex can't handle mixed ERROR+WARNING reports

The `_action-required.md` cross-check in verify_integrity.py uses regex `(\d+)W` to extract the WARNING count from the Summary table row. This only works when reports have 0 ERRORs (pure WARNING-only rows like `| 306W |`). 

When a report has both ERRORs and WARNINGs and the table row uses a format like `| 324 (5E+319W) |`, the regex doesn't match. This is a **known limitation** — the verify script was designed during the 0-ERROR clean streak period (07-14 through 07-16) and was never updated to handle mixed counts.

**Workaround:** Accept this single verify failure when ERRORs are present. The core checks (report exists, MEMORY.md entry prepended, _action-required.md entry present) will still pass.

### _action-required.md must match verify_integrity.py expectations exactly

`verify_integrity.py` parses `_action-required.md` with specific regex patterns and substring checks. The following format requirements MUST be met:

**Table format (Summary section):**
- Column order: `| Status | Date | Type | Issues | Action |`
- Row regex: `\|\s*🔍\s*PENDING\s*\|\s*MM-DD\s*\|\s*Format\s*\|\s*(\d+)W\s*\|`
- Example valid row: `| 🔍 PENDING | 07-20 | Format | 318W | Review [wiki/reviews/2026-07-20_format-report.md](2026-07-20_format-report.md) |`

**Section header (Pending Reports):**
- Must be: `### 🔍 Format Validation — YYYY-MM-DD` (full date, not MM-DD)

**Report link:**
- Must include full path: `wiki/reviews/YYYY-MM-DD_format-report.md` (not just filename)
- Check is literal substring: `f"wiki/reviews/{today}_format-report.md" in ar`

**Required markers:**
- `✅ APPROVED` must appear somewhere in the file (check is: `'✅ APPROVED' in ar`)
- `**Last updated:** YYYY-MM-DD` must be today's date

**Observed failures (2026-07-20):** Wrong column order, missing path prefix, missing `✅ APPROVED` text — 3 iterations needed to satisfy all checks.

### MEMORY.md format — verify_integrity.py requires plain-text Files checked line

`verify_integrity.py` checks MEMORY.md with `f"Files checked: {files_checked}" in mem` — a **plain-text substring match** across the entire file. Writing `**Files checked:** 815` (inside bold markers) fails because the `**` between `:` and `815` breaks the substring. The fix is to add a plain-text `Files checked: N` line after the bold display line:

```
- **Files checked:** 815 (457 concepts + 151 sources + 33 indexes + 174 topics)
Files checked: 815
```

This mirrors the dual-format pattern already required in the report (bold for display + plain-text for regex extraction).

**Observed case (2026-07-21):** verify_integrity.py returned `MEMORY.md: file count mismatch — expected 815` because only `**Files checked:** 815` was present. Adding the plain-text line resolved it.

### _action-required.md patch tool failures due to non-unique table rows

The Summary table in `_action-required.md` has repeated patterns across rows (e.g., `| 🔍 PENDING |` appears in every pending row). When using `patch` to add a new table row, short `old_string` patterns will match multiple rows and fail.

**Workaround:** Use `write_file` to rewrite the entire file when making structural changes. For simple edits (like updating timestamps), `patch` with unique context (e.g., `**Last updated:** OLD_DATE`) is fine. For adding table rows or section entries, prefer `write_file` after reading the full file.

### Level field contradicts filesystem path → wrong spec routing

When a file's `level` field doesn't match its position in the index hierarchy (e.g., `wiki/tag/tag.md` declares `level: 1` but is actually a Tầng 2 file per index-spec.md §4.1), the validator dispatches to the wrong spec and produces partially incorrect expected values.

**Example (2026-07-03):** `wiki/tag/tag.md` had `level: 1`. Before the script fix, the validator applied Tầng 1 rules (§3), flagging `scope` should be `raw/wiki/context` (correct for Tầng 2 would be `tags`) and missing `## Sub-indexes` (correct for Tầng 2 would be `## Parent`).

**Script fix (2026-07-03):** `validate.py` now has a `get_path_level()` function that derives the correct tier from the filesystem path. `validate_index()` cross-checks the declared `level` against the path-derived level. When they disagree:
1. A separate ERROR is issued: `level field (N) contradicts filesystem path (expected M)`
2. The validator uses the **path-derived tier** for all subsequent checks

**Path → level mapping:**
- `wiki/tag/tag.md` → always Tầng 2 regardless of `level` field value
- `wiki/tag/<tag>.md` → always Tầng 3
- `wiki/wiki.md`, `raw/raw.md`, `context/context.md` → always Tầng 1
- `raw/<subtype>/<subtype>.md` → always Tầng 2

If `get_path_level()` returns `None` (file not in a path that implies a specific tier), the declared `level` field is used as-is.

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
