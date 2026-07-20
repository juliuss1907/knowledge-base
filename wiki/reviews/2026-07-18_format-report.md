# Format Validation — 2026-07-18

**Status:** approved
**Issues found:** 324
**ERRORs:** 5
**WARNINGS**: 319
**INFOS:** 0
**Created:** 2026-07-18 23:16
**Approved by:** Julius
**Approved on:** 2026-07-20
**Validator:** format-validator
**Files checked:** 796
**Total issues**: 324
Files checked: 796
Total issues: 324

> **Δ from 07-17 (previous):** 0 — identical results. No files added, no issues resolved or introduced since yesterday.
> **Δ from 07-14 (approved):** +5 ERROR, +13 WARNING, +27 files (+17 concepts, +5 sources, +5 topics). Clean streak from 07-14–07-16 broken on 07-17.

---

## Delta from 07-14 (approved)

| Metric | 07-14 | 07-18 | Δ |
|---|---|---|---|
| Files checked | 769 | 796 | +27 |
| Concepts | 427 | 444 | +17 |
| Sources | 143 | 148 | +5 |
| Indexes | 33 | 33 | 0 |
| Topics | 166 | 171 | +5 |
| **Total issues** | **306** | **324** | **+18** |
| **ERRORs** | **0** | **5** | **+5** 🔴 |
| **WARNINGs** | **306** | **319** | **+13** |

## Delta from 07-17 (previous)

| Metric | 07-17 | 07-18 | Δ |
|---|---|---|---|
| Files checked | 796 | 796 | 0 |
| Concepts | 444 | 444 | 0 |
| Sources | 148 | 148 | 0 |
| Indexes | 33 | 33 | 0 |
| Topics | 171 | 171 | 0 |
| **Total issues** | **324** | **324** | **0** |
| **ERRORs** | **5** | **5** | **0** |
| **WARNINGs** | **319** | **319** | **0** |

---

## Positive Delta (vs 07-14)

None — all metrics degraded or unchanged since last approved baseline. The 0-ERROR streak from 07-14 through 07-16 has not recovered.

---

## Negative Delta (vs 07-14)

- **+5 ERRORs**: 3 missing required sections, 2 slug exceeds 50-char limit (new concepts compiled since 07-14)
- **+13 WARNINGs**: All are additional forward-reference broken wikilinks in new source/concept files
- **2 raw-file original link warnings**: `src_why-the-math-mafia-is-doing-well-jesse-zhang.md` and `src_you-just-hired-a-million-bad-employees-a16z.md` — raw files have different naming than expected

---

## Issue breakdown

| Severity | Count | Categories |
|---|---|---|
| ERROR | 5 | 3 Sections, 2 Naming |
| WARNING | 319 | 317 Markdown (broken wikilinks), 2 Frontmatter (original link) |
| INFO | 0 | — |

---

## ERROR details (5)

### Issue 1: Missing required section — ## Key ideas

**File:** wiki/concepts/destination-vs-vehicle.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Concept file missing required section `## Key ideas`
**Expected:** All concept files must have `## Key ideas` after Definition
**Suggested fix:** Add `## Key ideas` section with key takeaways

### Issue 2: Missing required section — ## Sources

**File:** wiki/concepts/psychic-energy.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Concept file missing required section `## Sources`
**Expected:** All concept files must have `## Sources` section linking to source files
**Suggested fix:** Add `## Sources` section with wikilinks to relevant source files. Note: this concept was flagged as truncated in Output Validation 07-18 — re-compile from scratch.

### Issue 3: Missing required section — ## Key ideas

**File:** wiki/concepts/social-attraction.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Concept file missing required section `## Key ideas`
**Expected:** All concept files must have `## Key ideas` after Definition
**Suggested fix:** Add `## Key ideas` section with key takeaways

### Issue 4: Slug exceeds 50-character limit

**File:** wiki/sources/src_is-there-anything-left-to-build-in-crypto-wintermute.md
**Severity:** ERROR
**Category:** Naming
**Issue:** Source slug body is 52 characters (limit: 50)
**Current:** `is-there-anything-left-to-build-in-crypto-wintermute` (52 chars)
**Suggested fix:** Shorten slug, e.g. `is-there-anything-left-build-crypto-wintermute` (49 chars)

### Issue 5: Slug exceeds 50-character limit

**File:** wiki/sources/src_the-5-laws-of-people-who-never-chase-gabriel-reality.md
**Severity:** ERROR
**Category:** Naming
**Issue:** Source slug body is 52 characters (limit: 50)
**Current:** `the-5-laws-of-people-who-never-chase-gabriel-reality` (52 chars)
**Suggested fix:** Shorten slug, e.g. `the-5-laws-of-people-who-never-chase-gabriel` (46 chars)

---

## WARNING summary (319)

### Broken wikilinks — forward references (317)

All 319 WARNINGs are expected forward-references: wikilinks pointing to concepts that have not yet been compiled into the KB. This is normal KB growth behavior — concepts reference each other before all targets exist.

**Breakdown:**
- 296 individual broken wikilinks across concept and source files
- 21 summary-group warnings (files with 4+ broken targets, grouped for readability)
- 199 unique broken targets

**Top 10 most-referenced missing targets:**

| Target | Count |
|---|---|
| [[game-theory]] | 10 |
| [[confirmation-bias]] | 8 |
| [[src_you-just-hired-a-million-bad-employees-a16z.md]] | 5 |
| [[ai-coding-agents]] | 5 |
| [[career-design]] | 5 |
| [[decision-making]] | 5 |
| [[deep-work]] | 4 |
| [[ai-hype-vs-reality]] | 3 |
| [[economic-inequality]] | 3 |
| [[critical-thinking]] | 3 |

**Top files by warning count:**

| File | Warnings |
|---|---|
| wiki/concepts/collaborative-thinking.md | 5 |
| wiki/concepts/probabilistic-thinking.md | 5 |
| wiki/concepts/feedback-loops.md | 4 |
| wiki/concepts/hanlons-razor.md | 4 |
| wiki/concepts/meaning-through-work.md | 4 |

### Original-file wikilink warnings (2)

**File:** wiki/sources/src_why-the-math-mafia-is-doing-well-jesse-zhang.md
**Issue:** `original: [[2026-07-14_why-the-math-mafia-is-doing-well-jesse-zhang.md]]` — raw file not found
**Suggested fix:** Verify correct raw filename and update original field

**File:** wiki/sources/src_you-just-hired-a-million-bad-employees-a16z.md
**Issue:** `original: [[2026-07-15_you-just-hired-a-million-bad-employees-a16z.md]]` — raw file not found
**Suggested fix:** Verify correct raw filename and update original field

---

## Files without format issues

Of 796 files checked, 472 had zero issues (59.3%). Of the 324 files with issues, 319 have only forward-reference wikilink WARNINGs (expected), 3 have section ERRORs, and 2 have naming ERRORs.

---

## Escalations

### [SYSTEMATIC VIOLATION]

**Pattern:** 2 concept files (`destination-vs-vehicle.md`, `social-attraction.md`) compiled without `## Key ideas` section. This is a Compile Agent regression — the agent should always include all required sections.

**Recommendation:** Review compile-agent/SKILL.md to ensure section checklist is enforced.

### [SYSTEMATIC VIOLATION]

**Pattern:** 2 source files exceed 50-char slug limit. Both compiled in latest batch. Compile Agent should validate slug length before finalizing filename.

**Recommendation:** Add slug-length guard to compile-agent naming logic.

---

## Verification

- [x] All 796 files read and parsed successfully (0 errors reading)
- [x] format-spec.md rules applied: frontmatter, sections, naming, markdown
- [x] index-spec.md rules applied: 33 indexes + 171 topics validated
- [x] Topic files (171) validated with light validation (no false level ERRORs)
- [x] Broken wikilink validation with raw-subdir resolution
- [x] Code fence language tag check (state-tracking, not regex)
- [x] YAML date parsing handles datetime.date objects correctly
- [x] Unquoted wikilink in YAML detected as list → WARNING correctly issued
- [x] context/USER.md skipped (read-only, no frontmatter)
- [x] wiki/drafts/ and wiki/reviews/ excluded from scan
- [x] Results identical to 07-17 (confirmed no regression, no resolution)
- [x] Delta tracking: vs 07-17 (0 change), vs 07-14 approved (+5E, +13W, +27 files)
- [x] Report written to wiki/reviews/2026-07-18_format-report.md
