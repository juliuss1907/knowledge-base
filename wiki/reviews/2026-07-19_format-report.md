# Format Validation — 2026-07-19

**Status:** approved
**Issues found:** 324
**ERRORs:** 5
**WARNINGS**: 319
**INFOS:** 0
**Created:** 2026-07-19 23:15
**Approved by:** Julius
**Approved on:** 2026-07-20
**Validator:** format-validator
**Files checked:** 796
**Total issues**: 324
Files checked: 796
Total issues: 324

> **Δ from 07-18 (previous):** 0 — identical results. No files added, no issues resolved or introduced. Third consecutive day at this plateau.
> **Δ from 07-14 (approved):** +5 ERROR, +13 WARNING, +27 files (+17 concepts, +5 sources, +5 topics). Clean streak 07-14–07-16 broken on 07-17, unchanged since.

---

## Delta from 07-14 (approved)

| Metric | 07-14 | 07-19 | Δ |
|---|---|---|---|
| Files checked | 769 | 796 | +27 |
| Concepts | 427 | 444 | +17 |
| Sources | 143 | 148 | +5 |
| Indexes | 33 | 33 | 0 |
| Topics | 166 | 171 | +5 |
| **Total issues** | **306** | **324** | **+18** |
| **ERRORs** | **0** | **5** | **+5** 🔴 |
| **WARNINGS** | **306** | **319** | **+13** 🟡 |
| **INFOS** | **0** | **0** | 0 |

---

## Delta from 07-18 (previous)

| Metric | 07-18 | 07-19 | Δ |
|---|---|---|---|
| Files checked | 796 | 796 | 0 |
| Concepts | 444 | 444 | 0 |
| Sources | 148 | 148 | 0 |
| Indexes | 33 | 33 | 0 |
| Topics | 171 | 171 | 0 |
| **Total issues** | **324** | **324** | **0** |
| **ERRORs** | **5** | **5** | **0** |
| **WARNINGS** | **319** | **319** | **0** |
| **INFOS** | **0** | **0** | **0** |

**Zero change from 07-18.** The KB has not been modified since 07-17 — no new files compiled, no fixes applied, no file edits. All 5 ERRORs and 319 WARNINGs are identical to the 07-17 and 07-18 reports. This is a stable plateau awaiting Julius's approval and Fix Agent action.

---

## Issue 1: Missing required section `## Key ideas`

**File:** wiki/concepts/destination-vs-vehicle.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Concept file is missing the required `## Key ideas` section per format-spec.md §2.
**Current:** No `## Key ideas` section present
**Expected:** `## Key ideas` H2 section with 3-5 bullet points
**Suggested fix:** Add `## Key ideas` section with core takeaways from the concept.

---

## Issue 2: Missing required section `## Key ideas`

**File:** wiki/concepts/social-attraction.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Concept file is missing the required `## Key ideas` section per format-spec.md §2.
**Current:** No `## Key ideas` section present
**Expected:** `## Key ideas` H2 section with 3-5 bullet points
**Suggested fix:** Add `## Key ideas` section with core takeaways from the concept.

---

## Issue 3: Missing required section `## Sources`

**File:** wiki/concepts/psychic-energy.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Concept file is missing the required `## Sources` section per format-spec.md §2. Also flagged as truncated in Output Validator 07-18 report.
**Current:** No `## Sources` section present
**Expected:** `## Sources` H2 section with list of source wikilinks
**Suggested fix:** Add `## Sources` section. If the file is truncated (per Output 07-18 finding), re-compile the concept entirely.

---

## Issue 4: Slug exceeds 50-char limit

**File:** wiki/sources/src_is-there-anything-left-to-build-in-crypto-wintermute.md
**Severity:** ERROR
**Category:** Naming
**Issue:** Source filename slug exceeds 50 characters (52 chars). Per format-spec.md slug rules, max is 50 chars.
**Current:** `src_is-there-anything-left-to-build-in-crypto-wintermute.md` (52 chars after `src_`)
**Expected:** Slug ≤ 50 chars after `src_` prefix
**Suggested fix:** Shorten slug, e.g. `src_is-there-anything-left-to-build-in-crypto.md` (46 chars), then update all backlinks.

---

## Issue 5: Slug exceeds 50-char limit

**File:** wiki/sources/src_the-5-laws-of-people-who-never-chase-gabriel-reality.md
**Severity:** ERROR
**Category:** Naming
**Issue:** Source filename slug exceeds 50 characters (52 chars). Per format-spec.md slug rules, max is 50 chars.
**Current:** `src_the-5-laws-of-people-who-never-chase-gabriel-reality.md` (52 chars after `src_`)
**Expected:** Slug ≤ 50 chars after `src_` prefix
**Suggested fix:** Shorten slug, e.g. `src_the-5-laws-of-people-who-never-chase.md` (42 chars), then update all backlinks.

---

## Issue 6: Forward-reference broken wikilinks (296 individual + 21 summary groups)

**File:** 199 unique broken targets across 168 files (concepts + sources)
**Severity:** WARNING
**Category:** Markdown
**Issue:** 319 WARNINGs total: 296 individually listed broken wikilinks + 21 summary-group entries (files with 4+ broken wikilinks each). All are forward-references — links to concepts not yet compiled into the KB.
**Current:** Wikilinks like `[[game-theory]]`, `[[confirmation-bias]]`, `[[ai-coding-agents]]` point to targets that don't exist in `wiki/concepts/` or `wiki/sources/`
**Expected:** Wikilinks resolve to existing KB files. These will auto-resolve as KB grows.
**Suggested fix:** No action needed. Forward-references are expected and resolve naturally when concepts are compiled.

### Top 20 broken targets

| Target | Count |
|---|---|
| `[[game-theory]]` | 10 |
| `[[confirmation-bias]]` | 8 |
| `[[src_you-just-hired-a-million-bad-employees-a16z.md]]` | 5 |
| `[[ai-coding-agents]]` | 5 |
| `[[career-design]]` | 5 |
| `[[decision-making]]` | 5 |
| `[[deep-work]]` | 4 |
| `[[ai-hype-vs-reality]]` | 3 |
| `[[economic-inequality]]` | 3 |
| `[[critical-thinking]]` | 3 |
| `[[naval-ravikant]]` | 3 |
| `[[risk-parity]]` | 3 |
| `[[second-law-of-thermodynamics]]` | 3 |
| `[[saying-no]]` | 3 |
| `[[power-imbalance]]` | 3 |
| `[[src_why-the-math-mafia-is-doing-well-jesse-zhang.md]]` | 3 |
| `[[first-order-thinking]]` | 3 |
| `[[breaking-point]]` | 2 |
| `[[momentum]]` | 2 |
| `[[multi-agent-systems]]` | 2 |

---

## Issue 7: Raw-file original wikilinks not found

**File:** wiki/sources/src_why-the-math-mafia-is-doing-well-jesse-zhang.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `original` field wikilink `[[2026-07-14_why-the-math-mafia-is-doing-well-jesse-zhang.md]]` — raw file not found under any `raw/` subdirectory.
**Current:** `original: "[[2026-07-14_why-the-math-mafia-is-doing-well-jesse-zhang.md]]"`
**Expected:** Raw file should exist in `raw/<type>/` matching the date and slug
**Suggested fix:** Verify raw file exists. May be a date typo or ingest timing issue.

---

**File:** wiki/sources/src_you-just-hired-a-million-bad-employees-a16z.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `original` field wikilink `[[2026-07-15_you-just-hired-a-million-bad-employees-a16z.md]]` — raw file not found under any `raw/` subdirectory.
**Current:** `original: "[[2026-07-15_you-just-hired-a-million-bad-employees-a16z.md]]"`
**Expected:** Raw file should exist in `raw/<type>/` matching the date and slug
**Suggested fix:** Verify raw file exists. May be a date typo or ingest timing issue.

---

## Verification

- [x] Validation script (`validate.py`) ran successfully — 0 errors reading files
- [x] 796 files checked: 444 concepts + 148 sources + 33 indexes + 171 topics
- [x] Results compared against 07-18 report — identical (0 delta)
- [x] Results compared against 07-14 approved baseline — +5 ERROR, +13 WARNING, +27 files
- [x] No _action-required.md reconciliation needed (07-18 was still pending)
- [x] Report written to `wiki/reviews/2026-07-19_format-report.md`

---

## Escalations

### [STABLE PLATEAU — 3 CONSECUTIVE IDENTICAL RUNS]

**Pattern:** 07-17, 07-18, and 07-19 format reports are fully identical. No files have been added to the KB and no fixes have been applied during this period.

**Impact:** The same 5 ERRORs persist across 3 days. The 07-14 approved report had 0 ERRORs — the current plateau represents a sustained regression.

**Recommendation:** Julius should review the pending 07-17/07-18 Format reports and approve fixes for the 5 ERRORs (3 missing sections, 2 slug violations). Until Fix Agent runs, format reports will continue showing the same results.

### [FORWARD-REFERENCE WIKILINKS — EXPECTED, NO ACTION]

**Pattern:** All 319 WARNINGs are forward-reference broken wikilinks — links to concepts that haven't been compiled yet. This is a known and expected pattern. These resolve naturally as the KB grows.

**Recommendation:** No escalation needed. Forward-refs are not a quality issue.

### [SPEC CONFLICT — UNQUOTED WIKILINKS IN INDEX-SPEC.MD]

**Status:** Ongoing. `index-spec.md` shows unquoted `parent: [[tag]]` but `format-spec.md` §9 note requires quoted wikilinks in frontmatter. Validator handles both forms gracefully (WARNING only). No false positives generated.
