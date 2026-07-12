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

0. **Verify structural integrity** (all 3 output files):
   ```bash
   bash .hermes/skills/output-validator/scripts/verify-output.sh
   ```
   Checks `_action-required.md` (pending count, Output Validation entry, Pending Reports section uniqueness, Applied Reports intact), today's output report (exists + non-empty + all required fields), and `.hermes/MEMORY.md` (today's log entry + report reference). Exit code 0 = all good. If the script reports failures due to format drift, fall back to the manual checks documented in Production Lessons.

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

### "ngườii/đờii/lờii/rờii/thờii" double-i typo variant (2026-06-23)

The original "ngưởi" typo (hook-above 'ỉ' instead of 'ời') evolved into a new variant: Compile Agent now doubles the final 'i' after grave-accented 'ờ' in Vietnamese words. This is the SAME root cause (LLM generating incorrect diacritic/letter combinations) with a different manifestation.

**Patterns detected:**
- `ngườii` → `người` (most common, 39 instances in one batch)
- `đờii` → `đời`
- `lờii` → `lời`
- `rờii` → `rời`
- `thờii` → `thời`
- `giớii` → `giới`

**Fix command (sed):**
```bash
sed -i 's/ngườii/người/g; s/đờii/đời/g; s/lờii/lời/g; s/rờii/rời/g; s/thờii/thời/g; s/giớii/giới/g' <file>
```

**Detection in quick-scan:** `scripts/quick-scan.sh` section 2b uses `grep -rP 'ngườii|đờii|lờii|rờii|thờii|giớii'` to catch this variant. The original "ngưởi" check (section 2) remains active as a separate pass — these are distinct patterns that may co-occur.

**Root cause:** Compile Agent's LLM prompt or tokenization adds an extra 'i' after words that combine the grave accent (`) with Vietnamese characters. When the original "ngưởi" typo was corrected in some files but not the underlying prompt, the error shifted form rather than being eliminated. The fix-agent should handle both variants; the compile-agent prompt should be reviewed to prevent recurrence.

### "người" spacing merge typo variant (2026-07-02)

A third manifestation of the same root cause: "người" merges with the following word — the space between words is dropped entirely. This produces run-on compound tokens that pass basic spell-check but break readability.

**Patterns detected (7 instances in `high-agency.md`):**
- `ngườitrong` → `người trong` (or `người. Trong` depending on sentence boundary)
- `ngườitrở thành` → `người trở thành`
- `ngườichỉ đạo` → `người chỉ đạo`
- `ngườicó` → `người có`
- `ngườilên` → `người lên`

**Detection regex:**
```bash
grep -Pn 'người[a-zàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]' <file>
```
This matches "người" followed immediately by a lowercase Vietnamese letter (not punctuation). Punctuation-adjacent "người," or "người." is valid and should NOT be flagged.

**Fix command (sed):**
```bash
sed -i 's/ngườitrong/người trong/g; s/ngườitrở thành/người trở thành/g; s/ngườichỉ đạo/người chỉ đạo/g; s/ngườicó/người có/g; s/ngườilên/người lên/g' <file>
```
Note: the sed must be ordered longest-match-first to avoid partial replacements. After fixing spacing, manually verify sentence boundaries — some merges may have concealed missing periods (e.g., `ngườitrong` might need `người. Trong`).

**Symptom to watch for:** The spacing merge often co-occurs with run-on sentences — when "người" merges into the next clause, it can conceal a missing sentence boundary. Always re-read the surrounding 1-2 sentences after fixing spacing.

**Detection in quick-scan:** Now active in `scripts/quick-scan.sh` (added 2026-07-02). The script reports both the total files/instances and the "new" count (instances in files compiled today vs existing files). When the "new" count is 0, all instances are in older files — these are carry-over issues from prior batches, not problems introduced today.

### False-positive content-depth flags (LLM hallucination)

The LLM-based validator (glm-5.1 via opencode) can incorrectly flag files as having missing/inadequate content when the content is actually present and substantial. **Pattern (2026-06-19):** 7 files flagged as low-quality — but all had full Definitions (2+ câu), Key Ideas (5-6 items), and populated sections.

**Files affected in that run:**
- ai-coach-prompting.md — định nghĩa 2 câu + 6 key ideas
- content-generation-workflow.md — định nghĩa 2 câu + 6 key ideas
- dollar-as-rent-payment.md — định nghĩa đầy đủ + mechanism + key insight
- existential-vacuum.md — định nghĩa đầy đủ + 5 key ideas + "the trap"
- expert-knowledge-extraction.md — định nghĩa 2 câu + 6 key ideas
- trading-addiction-cycle.md — định nghĩa đầy đủ + warning signs + realization
- x-search-tool.md — định nghĩa đầy đủ + 6 key ideas + setup

**Mitigation:** When the validator flags a file for "missing content" or "definition too short," verify by reading the actual file. If the content is present, the flag is a false positive. The quick-scan script (`scripts/quick-scan.sh`) is more reliable for mechanical checks (empty sections, line counts) — reserve the LLM validator for coherence and Vietnamese quality checks where mechanical heuristics fall short. For content-presence checks, prefer grep/line-count over LLM judgment.

### Language detection heuristic
For Vietnamese quality checks:
- Count characters with Vietnamese diacritics (à, á, ạ, ả, ã, â, ầ, ấ, ậ, ẩ, ẫ, ă, ằ, ắ, ặ, ẳ, ẵ, è, é, ẹ, ẻ, ẽ, ê, ề, ế, ệ, ể, ễ, ì, í, ị, ỉ, ĩ, ò, ó, ọ, ỏ, õ, ô, ồ, ố, ộ, ổ, ỗ, ơ, ờ, ớ, ợ, ở, ỡ, ù, ú, ụ, ủ, ũ, ư, ừ, ứ, ự, ử, ữ, ỳ, ý, ỵ, ỷ, ỹ, đ)
- If `english_words > vietnamese_count * 3` and `vietnamese_count > 0` → flag as "English-heavy"
- If `vietnamese_count == 0` and `english_words > 50` → flag as "English-only"

### Multiple runs per day (pre-existing approved report)

When the validator runs and finds `wiki/reviews/YYYY-MM-DD_output-report.md` already exists AND is marked **APPROVED** in `_action-required.md`, do NOT skip validation. Instead:

1. **Find files newer than the existing report:**
   ```bash
   find wiki/sources/ wiki/concepts/ -name "*.md" -newer wiki/reviews/YYYY-MM-DD_output-report.md -type f
   ```
2. **If new files exist:** validate only those files, produce an updated report. Title it `# Output Validator Report — YYYY-MM-DD (HH:MM Update)`. Include a `**Previous run:**` field linking to the approved morning report.
3. **If no new files:** log "No new files since last approved report" to MEMORY.md and respond with `[SILENT]`.
4. **When overwriting the approved report:** clearly mark the new report as `**Status:** pending` and note that the previous version was approved. Add a section summarizing the morning report's findings for continuity.
5. **In _action-required.md:** add the new run as a separate "Pending" entry while keeping the morning run under "Approved." Both entries share the same date but have different timestamps.
6. **Because the report filename is reused, preserve the morning context inside `_action-required.md` itself.** Do not rely on the approved entry's link to still show the morning contents after the rerun overwrites `YYYY-MM-DD_output-report.md`. Keep the approved morning summary self-contained, and in the pending rerun entry explicitly say it is a delta against the approved morning run.
7. **In the rerun report body, include a short "Previous approved run context" section.** This guards against loss of continuity once the same-day file is overwritten.

**Pattern (2026-06-22):** Morning report at 08:20 (24 new files, approved). Evening run at 22:00 found 11 additional files. Produced updated report noting the overlap, highlighting that "ngưởi" typo count dropped from 10→1 (Fix Agent resolved 9 between runs).

**Additional lesson (2026-06-26):** Same-day rerun at 23:01 overwrote `2026-06-26_output-report.md` after the 07:01 report had already been approved. The durable history survived only because `_action-required.md` retained the approved morning summary and the rerun report carried a `Previous approved run context` section. Treat those two summaries as required, not optional.
### Cron working directory

When running as a scheduled cron job, the session working directory may be `$HOME` (e.g., `/home/julius`) rather than the knowledge-base directory. The `search_files` and `read_file` tools resolve relative paths from the session cwd, so `wiki/sources/` will fail.

**Fix**: Always use absolute paths (`/home/julius/knowledge-base/wiki/sources/`) for `search_files`, `read_file`, and `terminal` calls. For `terminal`, either `cd` first or use the `workdir` parameter. The quick-scan script handles this internally via `KB_DIR` variable.

### Archived prior report breaks `find -newer` (2026-07-02)

When the previous output report was approved and archived to `wiki/reviews/archive/YYYY-MM/`, a `find -newer` against the expected path (`wiki/reviews/YYYY-MM-DD_output-report.md`) silently returns zero results because the file no longer exists at that location. This causes the validator to miss ALL files compiled since the last run.

**Symptom:** `find -newer` returns 0, but `grep -rl 'date_compiled: YYYY-MM-DD'` on wiki/sources/ returns files. The quick-scan script may also report "New files today: N" while `find -newer` says 0.

**Fix:** Do NOT rely solely on `find -newer` against the expected report path. Use TWO methods and cross-check:
1. **Primary:** `grep -rl 'date_compiled: YYYY-MM-DD' wiki/sources/` and `grep -rl 'last_updated: YYYY-MM-DD' wiki/concepts/` for each day since the last validation run
2. **Fallback:** `find -newer` against the archived report path if the active path doesn't exist:
   ```bash
   LAST_REPORT="wiki/reviews/YYYY-MM-DD_output-report.md"
   if [ ! -f "$LAST_REPORT" ]; then
     LAST_REPORT=$(find wiki/reviews/archive/ -name "YYYY-MM-DD_output-report.md" -type f 2>/dev/null | sort | tail -1)
   fi
   ```
3. **Cross-check:** If `find -newer` returns 0 but frontmatter grep returns files, trust the frontmatter grep — some filesystems don't preserve meaningful modification times after git operations or cross-machine sync.

**Pattern (2026-07-02):** Last output validation was 06-30, report archived to `archive/2026-06/`. `find -newer wiki/reviews/2026-06-30_output-report.md` returned 0. But 28 files (8 sources + 17 concepts on 07-01 + 3 on 07-02) had never been output-validated. The quick-scan script caught the 07-02 files via frontmatter date matching but did not flag the 07-01 gap.

### verify-output.sh section naming false positives (2026-07-04, RESOLVED 2026-07-12)

**Original issue:** The `scripts/verify-output.sh` script checked for section headers matching an older `_action-required.md` format (e.g., `## Pending — YYYY-MM-DD`, `### 🔲 Output Validation — YYYY-MM-DD`, `## Approved — 2026-06-29`) that no longer existed after the file was restructured to use `## Pending Reports`, `### 🔍 Output Validation — YYYY-MM-DD (HH:MM)`, and `## Applied Reports`.

**Resolution (2026-07-12):** Script updated to match the current format. Checks now target `## Pending Reports`, `Output Validation — ${TODAY}`, `## Applied Reports`, and `**Pending reports awaiting review:** N`. The section uniqueness check now counts `## Pending Reports` headers instead of per-date sections.

**Symptom of stale script:** verify-output.sh reports 4-5 failures like `❌ Section 'Output Validator Report' present` and `❌ Section 'Actions' present` — even when the report is structurally complete.

**Mitigation (if script gets stale again):** Treat verify-output.sh results as advisory, not authoritative. The script's structural checks (pending count, status line, section uniqueness, no corruption) are reliable. Its section-name checks are rigid — if those fail but the report has all required content (status, issues, evidence, suggested fixes, summary), the report is valid. Check manually:
```bash
# These are the reliable checks:
grep -q "^\*\*Status:\*\* pending" wiki/reviews/YYYY-MM-DD_output-report.md
grep -q "^\*\*Issues found:\*\*" wiki/reviews/YYYY-MM-DD_output-report.md
grep -q "^\*\*Created:\*\*" wiki/reviews/YYYY-MM-DD_output-report.md
grep -c "^## Issue [0-9]" wiki/reviews/YYYY-MM-DD_output-report.md  # should match reported count
```

### Ad-hoc verification script: `set -euo pipefail` + `grep -q` in eval context

When writing bash verification scripts for post-validation, avoid combining `set -euo pipefail` with `grep -q` inside `eval`. `grep -q` exits 1 on no-match, and under `set -e` this terminates the entire script immediately after the first failed check.

**Pattern that fails:**
```bash
set -euo pipefail
check() { local desc="$1" condition="$2"; if eval "$condition"; then ...; fi; }
check "thing" 'grep -q "pattern" file'  # grep exits 1 → set -e kills script
```

**Pattern that works:**
```bash
# No set -e, or use "$@" positional args instead of eval:
check() { local desc="$1"; shift; if "$@" >/dev/null 2>&1; then ...; fi; }
check "thing" grep -q "pattern" file  # grep exits 1 inside if-test, script continues
```

**Alternative (keep set -e):** Wrap each grep in `|| true`:
```bash
check "thing" 'grep -q "pattern" file || true'
```

### Cron post-edit verification script requirement (2026-07-06)

After writing the output report and updating `_action-required.md` + `.hermes/MEMORY.md`, the cron system requires ad-hoc verification evidence. Create a focused script under `/tmp` with a `hermes-verify-` filename prefix:

```bash
cat > /tmp/hermes-verify-output-YYYYMMDD.sh << 'VERIFY_EOF'
#!/bin/bash
# Checks structural integrity of all 3 output files
# Use check() helper: check "desc" grep -q "pattern" file
# Always wrap with set -euo pipefail but put grep -q inside if-test (not eval)
VERIFY_EOF
bash /tmp/hermes-verify-output-YYYYMMDD.sh
```

**Key checks to include:**
1. Output report: status=pending, issues/created/validator fields, required sections present
2. `_action-required.md`: pending count, section uniqueness (no duplicate headers), entry date
3. `.hermes/MEMORY.md`: log entry present, appended after previous entry
4. Cross-file consistency: all files agree on counts (new files, issues, severity)

**Pitfall — grep patterns for `_action-required.md`:** The pending count line uses markdown bold: `**Pending reports awaiting review:** 1`, NOT plain `Pending reports awaiting review: 1`. Grep patterns must include `\*\*` markers:
```bash
# CORRECT:
grep -q '\*\*Pending reports awaiting review:\*\* 1' "$A"
# WRONG (will miss):
grep -q 'Pending reports awaiting review: 1' "$A"
```

**Pitfall — duplicate entry detection:** A well-formed `_action-required.md` entry references the report filename 3 times (heading link, actions section, report line). Do NOT use `grep -c '<filename>'` as a duplicate check — it always returns 3. Use heading count instead:
```bash
# CORRECT — heading appears exactly once:
grep -c '### 🔍 Output Validation — YYYY-MM-DD' "$A"  # must be 1
# WRONG — filename referenced 3 times in one entry:
grep -c 'YYYY-MM-DD_output-report.md' "$A"  # returns 3, not a duplicate signal
```

**Pitfall — verification script cleanup:** `rm /tmp/hermes-verify-*` may trigger "delete in root path" approval. Accept the block — `/tmp` files are cleaned by the OS eventually.

**Pitfall — emoji/unicode in heredoc triggers security scanner (2026-07-08):** When creating verification scripts via `cat > /tmp/hermes-verify-*.sh << 'VERIFY_EOF'`, emoji characters (✓, ❌, ⚠️, 🟢, 🔴) inside the heredoc body trigger the security scanner: "Variation selector characters detected". The terminal command is blocked pending approval. **Fix:** Use plain ASCII markers instead — `[OK]`, `[FAIL]`, `[INFO]`, `[WARN]`. No emoji anywhere in the heredoc body. The `check()` helper's echo statements and the grep patterns must all be emoji-free.

**Pitfall — grep literal strings with regex metacharacters (2026-07-07):** When searching for text containing special regex characters like parentheses `()` in dates or timestamps, use `grep -F` (fixed string). Otherwise grep interprets them as regex groups:

```bash
# BROKEN — parentheses treated as regex capture groups:
grep '2026-07-07 (23:08)' "$A"
# CORRECT:
grep -F '2026-07-07 (23:08)' "$A"
```

**Pitfall — grep -A context depth for _action-required.md entries (2026-07-07):** When piping `grep -A N` output to check for the Status line in a `_action-required.md` entry, remember the entry structure: heading → blank line → File line → Status line. That's 3 lines of context needed:

```bash
# BROKEN — -A 2 only reaches the File line, misses Status:
grep -F -A 2 '2026-07-07 (23:08)' "$A" | grep 'pending'
# CORRECT — -A 3 reaches the Status line:
grep -F -A 3 '2026-07-07 (23:08)' "$A" | grep 'pending'
```

**Pitfall — markdown bold `**` wrapping breaks plain-text grep in MEMORY.md (2026-07-07):** MEMORY.md log lines use markdown bold formatting: `- **Files checked:** 534 (...)` — the `**` sits between the colon and the value. Plain-text grep like `grep -F 'Files checked: 534'` won't match because the actual substring is `Files checked:** 534`. Use regex patterns instead:

```bash
# BROKEN — 'Files checked: 534' doesn't account for ** wrapping:
grep -q 'Files checked: 534' "$M"
# CORRECT — use regex .* to span the ** markers:
grep -q 'Files checked.*534' "$M"
```

**Pitfall — issue grouping makes standalone issue-number grep miss (2026-07-07):** When the report groups multiple issues under one header (e.g., `## Issue 5-7: Forward-reference wikilinks`), `grep "Issue 6"` and `grep "Issue 7"` won't match as standalone terms. Verify grouped issues by checking:
1. The grouped header exists (e.g., `grep -q '^## Issue 5-7:' "$R"`)
2. Cross-file consistency confirms the total issue count (all 3 files agree on N issues)

**Pitfall — silent-run verification (no report generated) (2026-07-11):** When the validator produces a silent result (0 new files, no output report written), the standard `verify-output.sh` script can't run because the expected report file doesn't exist. But the cron system still demands ad-hoc verification evidence. Instead, create a focused script targeting only MEMORY.md:

```bash
cat > /tmp/hermes-verify-memory-YYYYMMDD.sh << 'VERIFY_EOF'
#!/bin/bash
M="/home/julius/knowledge-base/.hermes/MEMORY.md"
# Check: entry exists, new files=0, issues=0, SILENT marker, append order, file integrity
VERIFY_EOF
bash /tmp/hermes-verify-memory-YYYYMMDD.sh
```

**Silent-run MEMORY.md entry structure (line depth):** The entry spans 5 lines:
```
## YYYY-MM-DD HH:MM:SS — Output validation         ← line 0 (heading)
- **Files checked:** ...                              ← line 1
- **New files:** 0 — ...                              ← line 2
- **Issues found:** 0 (0 ERROR, 0 WARNING, 0 INFO)   ← line 3
- **Result:** [SILENT] — nothing new to validate      ← line 4
```

To reach the `[SILENT]` marker or `Issues found` line, use `grep -F -A 5` (not `-A 3`). The existing `_action-required.md` pitfall about `-A` depth uses 3 lines for that file's different structure — MEMORY.md needs 5.

**Key checks for silent-run verification:**
1. Entry exists at correct timestamp (`grep -qF 'YYYY-MM-DD HH:MM:SS' "$M"`)
2. `New files: 0` (`grep -F -A 5 '...' "$M" | grep -q 'New files.*0'`)
3. `Issues found: 0` (`grep -F -A 5 '...' "$M" | grep -q 'Issues found.*0'`)
4. `[SILENT]` marker present (`grep -F -A 5 '...' "$M" | grep -q 'SILENT'`)
5. Append-only order (07-11 line number > 07-10 line number)
6. File ends with SILENT entry (`tail -1 "$M" | grep -qF 'SILENT'`)

**Pattern (2026-07-11):** Quick-scan confirmed 0 new files. No report generated. Ad-hoc verification script initially failed because `grep -A 3` missed the SILENT marker on line 5 — fixed by using `-A 5`. All 6 checks passed after correction.

**Reusable template:** `templates/verify-silent-memory.sh` — copy, replace the two timestamps, and run. Covers all 6 silent-run checks above.

### quick-scan.sh: bash integer comparison with grep -c in $()

When `grep -c` is used inside `$()` in bash, the output captures a trailing newline. When the pipeline produces no input (empty sed output), `grep -c` may exit 1, triggering `|| echo 0`, resulting in a two-line value like `"0\n0"`. Using this in `[ "$var" -eq N ]` causes:
```
[: 0\n0: cần biểu thức số nguyên
```

**Fix (applied 2026-06-22):** After every `grep -c` assignment, strip whitespace:
```bash
points=$(echo "$points" | tr -d '[:space:]')
[ -z "$points" ] && points=0
```
This ensures the variable is a clean integer before arithmetic comparisons. All 5 loops in `scripts/quick-scan.sh` have been patched with this fix.

**Additional pitfall (2026-06-25):** The same `grep -c ... || echo 0` pattern can break top-level counters outside loops, e.g.:
```bash
NGUOI_COUNT=$(echo "$NGUOI_FILES" | grep -c "." || echo 0)
```
When `NGUOI_FILES` is empty, this becomes `"0\n0"` and later JSON/human output is corrupted. Use a word-count helper for space-separated file lists instead:
```bash
count_words_var() { echo "$1" | wc -w | tr -d ' '; }
NGUOI_COUNT=$(count_words_var "$NGUOI_FILES")
```

**Additional pitfall (2026-06-25):** Under `set -euo pipefail`, commands like:
```bash
grep -rPl "$DOUBLE_I_PATTERNS" wiki/sources/ wiki/concepts/ | wc -l
```
will exit the whole script when grep finds zero matches. Wrap the grep with `|| true` inside a subshell:
```bash
DOUBLE_I_COUNT=$( (grep -rPl "$DOUBLE_I_PATTERNS" wiki/sources/ wiki/concepts/ 2>/dev/null || true) | wc -l | tr -d ' ' )
```

**Additional pitfall (2026-06-25):** `--json` mode depends on `jq` for array serialization. On machines without `jq`, the script still exits 0 but emits invalid JSON and `jq: command not found`. In that environment, prefer plain-text mode or add a preflight check for `jq` before using `--json`.
