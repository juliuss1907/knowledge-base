---
name: output-validator
model: opencode/glm-5.1
description: Validates content quality of wiki files (sources and concepts). Checks factual accuracy, completeness, coherence, and Vietnamese language quality. Use daily at 22:00 after Index Agent completes, or when user says "validate output", "check content quality". Reads wiki/sources/ and wiki/concepts/, generates quality report in wiki/reviews/, does NOT modify any wiki files.
when_to_use: Daily 23:00 validation run (after Index Agent, before Hygiene Inspector), or on-demand when Julius requests content quality check. Runs after Compile Agent has processed new content.
disable-model-invocation: false
user-invocable: false
allowed-tools: Read Bash(date *)
---

# Output Validator

Ensures wiki content meets quality standards across four dimensions: factual accuracy, completeness, coherence, and Vietnamese language quality.

## Role

Read all wiki files (`wiki/sources/*.md` + `wiki/concepts/*.md`), validate content quality, generate report listing issues with severity levels. Report goes to `wiki/reviews/YYYY-MM-DD_output-report.md` and updates `wiki/reviews/_action-required.md`.

**Critical**: This validator only reads and reports. Never modifies wiki files. Fix Agent applies corrections after Julius approves.

## When to use

- **Daily**: 22:00 (after Index Agent completes, before Hygiene Inspector)
- **On-demand**: Julius says "validate output" or "check content quality"
- **After bulk operations**: Re-compilation, mass edits, migration

**Why daily instead of weekly:**
- Smaller batches (5-15 files/day vs 50-100 files/week)
- Faster feedback loop (catch issues same day as compilation)
- Easier review (2-3 issues/day vs 20-30 issues/week)
- Better context retention (Julius remembers what was compiled)

## Quick start

1. **Scan wiki files** — read all `wiki/sources/*.md` + `wiki/concepts/*.md`
2. **Validate each file** — run 4 quality checks (factual, completeness, coherence, Vietnamese)
3. **Score issues** — assign severity (ERROR/WARNING/INFO)
4. **Generate report** — write to `wiki/reviews/YYYY-MM-DD_output-report.md`
5. **Update action file** — add entry to `wiki/reviews/_action-required.md`
6. **Send notification** — Telegram alert to Julius
7. **Log** to `.hermes/MEMORY.md`

## Critical rules

### Read-only validator
- **Only read** wiki files for validation
- **Only write** to `wiki/reviews/` (reports only)
- **Never modify** wiki content files
- **Never delete** any files

### Quality dimensions (4 checks per file)

1. **Factual accuracy** — Content claims are verifiable and correct
2. **Completeness** — All required sections present with sufficient detail
3. **Coherence** — Logical flow, clear arguments, no contradictions
4. **Vietnamese quality** — Grammar, spelling, natural phrasing (for Vietnamese content)

### Severity levels

| Severity | Meaning | Example |
|---|---|---|
| **ERROR** | Critical quality issue | Missing definition, factually wrong claim |
| **WARNING** | Should improve | Summary too vague, weak coherence |
| **INFO** | Nice to improve | Could add more examples, minor grammar |

### Scoring threshold

- **ERROR**: Block file from being referenced (move to drafts)
- **WARNING**: File usable but needs improvement
- **INFO**: File acceptable, suggestions only

## Report format

```markdown
# Output Validation — YYYY-MM-DD

**Status:** pending
**Issues found:** N
**Created:** YYYY-MM-DD HH:MM:SS
**Validator:** output-validator

---

## Issue 1: [Issue type]

**File:** wiki/<path>/<file>.md
**Severity:** ERROR | WARNING | INFO
**Dimension:** Factual | Completeness | Coherence | Vietnamese
**Issue:** <description>
**Evidence:** <quote from file showing issue>
**Suggested fix:** <action to take>

---

## Issue 2: [Issue type]

[...]
```

## Validation criteria summary

### Factual accuracy
- Claims have sources cited
- Technical terms used correctly
- No contradictions with cited sources
- Dates/numbers are accurate

### Completeness
- All required sections present
- Summary is 3-5 sentences
- Key points are 5-10 items
- Definition is 2-3 sentences (concepts only)

### Coherence
- Logical flow between sections
- Arguments are clear and supported
- No internal contradictions
- Transitions make sense

### Vietnamese quality
- Grammar correct (subject-verb agreement, tenses)
- Spelling correct (no typos)
- Natural phrasing (not machine-translated feel)
- Technical terms preserved in English where appropriate

## Constraints

### Write zones
- **Allowed:** `wiki/reviews/` only
- **Forbidden:** `wiki/sources/`, `wiki/concepts/`, `wiki/drafts/`, `wiki/tag/`, `wiki/topic/`, `wiki/meta/`

### Forbidden actions
- ❌ Modifying any wiki content files
- ❌ Deleting files
- ❌ Moving files
- ❌ Creating files outside `wiki/reviews/`
- ❌ Auto-fixing issues (Fix Agent does this after approval)

### Performance
- Validate all files in one pass (don't re-read)
- Cache file content in memory during scan
- **Limit report to top 20 issues per day** (daily runs = smaller batches)
- Skip files in `wiki/drafts/` (already flagged)
- Skip files unchanged since last validation (check `last_updated` field)

## Escalation

Flag for Julius when:

### Ambiguous quality issue
```
[VALIDATION UNCERTAINTY]
File: wiki/concepts/<slug>.md
Issue: Definition seems circular but might be intentional
Question: Is this acceptable or should it be flagged?
```

### Systematic issue detected
```
[SYSTEMATIC ISSUE]
Pattern: 15 files have summaries <2 sentences
Likely cause: Compile Agent prompt needs tuning
Recommendation: Review compile-agent/SKILL.md
```

### Language detection unclear
```
[LANGUAGE UNCLEAR]
File: wiki/sources/src_<slug>.md
Issue: Content mixes English and Vietnamese
Question: Which language should be primary?
```

## Details

For complete validation algorithm, scoring rubrics, and error handling, see:
- [workflow.md](workflow.md) — step-by-step validation process
- [validation-criteria.md](validation-criteria.md) — detailed quality rubrics
- [examples.md](examples.md) — sample reports and issues

## Post-validation

After successful validation run:

1. **Verify report written:**
   ```bash
   test -f "wiki/reviews/$(date +%Y-%m-%d)_output-report.md"
   ```

2. **Update _action-required.md:**
   - Add entry to "Pending Reports" section
   - Update "Last updated" timestamp
   - **⚠️ PITFALL**: The `patch` tool's fuzzy matching produces false positives on this file. Never use `replace_all=true`. Use at least 5-6 lines of unique context in `old_string`. See Production Lessons for full details.

3. **Send Telegram notification:**
   ```
   📋 Output validation complete
   - Issues found: N (X ERROR, Y WARNING, Z INFO)
   - Files checked: M (K new since last run)
   - Report: wiki/reviews/YYYY-MM-DD_output-report.md
   
   Review: wiki/reviews/_action-required.md
   Commands: 'approve output' or 'show output'
   ```

4. **Log to MEMORY.md:**
   ```markdown
   ## YYYY-MM-DD HH:MM:SS — Output validation
   - Files checked: M (X sources + Y concepts)
   - New files: K (compiled today)
   - Issues found: N (A ERROR, B WARNING, C INFO)
   - Report: wiki/reviews/YYYY-MM-DD_output-report.md
   ```

## Batch behavior

Output Validator processes files in one run but optimizes for daily schedule:
- **Scan all files** to maintain full context
- **Prioritize new files** (compiled today) for detailed validation
- **Quick check existing files** for systematic issues only — use `scripts/quick-scan.sh` for efficient terminal-based checks (typos, truncated files, empty sections, draft count)
- Generate single report with issues sorted by severity

**Typical daily run time:** 15-45 seconds for 5-15 new files + quick scan of existing

## Failure modes

| Issue | Action |
|---|---|
| File has no frontmatter | Skip file, log warning |
| File has invalid YAML | Skip file (Format Validator will catch) |
| Cannot determine language | Default to English validation rules |
| LLM call fails (for coherence check) | Skip coherence check, flag in report |
| Disk full | Stop, alert Julius |
| Permission denied on wiki/reviews/ | Stop, alert Julius |
| No new files today | Generate empty report, log "No new files to validate" |

## Performance benchmarks

Typical validation times (daily runs):

| New files | Existing files | Time |
|---|---|---|
| 0-5 | 50-100 | 10-20s |
| 5-15 | 100-200 | 20-45s |
| 15-30 | 200-300 | 45-90s |

**Bottlenecks:**
- Coherence checks (require LLM calls)
- Vietnamese grammar validation (language model)
- Reading many files (I/O)

**Optimization:**
- Batch LLM calls (5-10 files per call)
- Cache common validation patterns
- **Skip unchanged files** (check `last_updated` < today)
- Prioritize ERROR severity checks over INFO checks

## Production lessons

### Backlink resolution
When validating `[[...]]` wikilinks:
- `[[slug]]` → `wiki/concepts/slug.md` (primary), then `wiki/sources/src_slug.md` (fallback)
- `[[src_slug]]` → `wiki/sources/src_slug.md` only
- Treat missing targets as ERROR, but aggregate by target concept when reporting to stay within the 20-issue limit.

### Systemic issue aggregation
When the same issue type appears >10 times, report it as a single systemic issue:
- One entry describing the pattern, count, and top affected targets
- 2–3 representative file examples as evidence
- This preserves the 20-issue limit while conveying full scope.

### Empty baseline report
If `wiki/reviews/YYYY-MM-DD_output-report.md` exists but is empty/placeholder, treat it as if no prior report exists. Scan all files rather than relying on file timestamps.

### _action-required.md patch tool pitfall

The `patch` tool uses fuzzy matching. `_action-required.md` has repeated structural patterns (identical "Actions:" blocks, similar summary formats across date entries) that cause fuzzy matching to find false positives — a search string that appears once in the file may match 2-3 times in the fuzzy index.

**Rules when updating `_action-required.md`:**
1. **Never use `replace_all=true`** on this file. A false positive duplicate match will corrupt unrelated sections. In a 2026-06-18 run, `replace_all` corrupted the "Approved Reports" section because it matched an entry there as well as the intended Pending Reports entry.
2. **Always use a unique context string** — include at least 5-6 lines of text with specific details (e.g., the exact issue count, the specific date, the specific summary bullets) that cannot appear elsewhere.
3. **If the patch tool reports >1 match**, do NOT force it with `replace_all`. Instead, broaden the old_string with even more surrounding lines until it uniquely identifies the target location.
4. **Fallback**: If the patch tool insists on multiple matches after 3 attempts with highly specific strings, write the entire file fresh using `write_file` with the full reconstructed content.

**Symptom to watch for**: The patch diff shows insertions in unexpected sections (e.g., new entries appearing in "Approved Reports" instead of "Pending Reports"). Immediately read back the file to verify correctness.

### Truncated file detection

When a concept file is incomplete (truncated mid-generation by Compile Agent), two signals:
1. `read_file` returns fewer `total_lines` than typical (e.g., 25 vs expected 35-40 for a concept)
2. The last line ends mid-sentence or mid-bullet (e.g., `- **Commoditization risk` with no closing)

Treat as ERROR — missing `## Related concepts` and `## Sources` sections. The concept should be blocked from referencing until re-compiled.

### Language detection heuristic
For Vietnamese quality checks:
- Count characters with Vietnamese diacritics (à, á, ạ, ả, ã, â, ầ, ấ, ậ, ẩ, ẫ, ă, ằ, ắ, ặ, ẳ, ẵ, è, é, ẹ, ẻ, ẽ, ê, ề, ế, ệ, ể, ễ, ì, í, ị, ỉ, ĩ, ò, ó, ọ, ỏ, õ, ô, ồ, ố, ộ, ổ, ỗ, ơ, ờ, ớ, ợ, ở, ỡ, ù, ú, ụ, ủ, ũ, ư, ừ, ứ, ự, ử, ữ, ỳ, ý, ỵ, ỷ, ỹ, đ)
- If `english_words > vietnamese_count * 3` and `vietnamese_count > 0` → flag as "English-heavy"
- If `vietnamese_count == 0` and `english_words > 50` → flag as "English-only"

### Cron working directory

When running as a scheduled cron job, the session working directory may be `$HOME` (e.g., `/home/julius`) rather than the knowledge-base directory. The `search_files` and `read_file` tools resolve relative paths from the session cwd, so `wiki/sources/` will fail.

**Fix**: Always use absolute paths (`/home/julius/knowledge-base/wiki/sources/`) for `search_files`, `read_file`, and `terminal` calls. For `terminal`, either `cd` first or use the `workdir` parameter. The quick-scan script handles this internally via `KB_DIR` variable.
