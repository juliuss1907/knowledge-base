# Output Validation — 2026-05-21

**Status:** pending
**Issues found:** 11 (0 ERROR, 6 WARNING, 5 INFO)
**Created:** 2026-05-21 23:05:00
**Validator:** output-validator

**Files checked:** 96 (19 new, 77 existing)
**New files validated in-depth:** 19 (5 sources + 14 concepts)
**Existing files quick-scanned:** 77 (13 sources + 64 concepts) — no issues detected

---

## Issue 1: Empty Original excerpts section

**File:** wiki/sources/src_hermes-xurl-skill-guide.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** `## Original excerpts` section header present but no content follows
**Evidence:**
```
## Original excerpts
```
**Suggested fix:** Either add an excerpt from the original post or remove the empty section

---

## Issue 2: Too few key ideas — only 4 (need 5-10)

**File:** wiki/concepts/default-mode-network.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Key ideas section has only 4 bullet points (minimum 5 required)
**Evidence:**
```
- DMN hoạt động khi não "nghỉ ngơi"...
- Các chức năng của DMN...
- Nhàm chán là điều kiện tự nhiên...
- Thiếu thời gian cho DMN hoạt động...
```
**Suggested fix:** Add at least 1 more key idea (e.g., about DMN's role in creativity, or how meditation interacts with DMN)

---

## Issue 3: Too few key ideas — only 4 (need 5-10)

**File:** wiki/concepts/dunbar-number.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Key ideas section has only 4 bullet points (minimum 5 required)
**Evidence:**
```
- Con người tiến hóa trong băng nhóm hunter-gatherer khoảng 25-50 người...
- Chúng ta từ "chìm trong mạng lưới khuôn mặt"...
- 17% người Mỹ báo cáo không có bạn thân...
- Mất kết nối cộng đồng là yếu tố quan trọng...
```
**Suggested fix:** Add at least 1 more key idea (e.g., about Dunbar layers: 5/15/50/150/500, or practical implications for team size)

---

## Issue 4: Too few key ideas — only 4 (need 5-10)

**File:** wiki/concepts/evolutionary-mismatch.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Key ideas section has only 4 bullet points (minimum 5 required)
**Evidence:**
```
- Con người tiến hóa trong môi trường hunter-gatherer qua ~300,000 năm...
- Các khía cạnh cuộc sống hiện đại bị lệch lạc...
- "Tập thể dục" là khái niệm hiện đại...
- Giải pháp không phải "chữa lành" nhiều hơn...
```
**Suggested fix:** Split the long second bullet point into 2 separate items (e.g., separate sleep/community from work/nature) for at least 5 bullet points

---

## Issue 5: Vietnamese typo — "tiếm" should be "tiếng"

**File:** wiki/concepts/hunter-gatherer-lifestyle.md
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** Spelling error — missing diacritic: "tiếm" instead of "tiếng"
**Evidence:**
```
- Ngủ theo nhịp mặt trời, 8-9 tiếm mỗi đêm
```
**Suggested fix:** Correct to: `8-9 tiếng mỗi đêm`

---

## Issue 6: Broken wikilinks — referenced concepts don't exist

**File:** wiki/concepts/ai-white-collar-automation.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** "Related concepts" section references two concept files that don't exist: `[[economic-inequality]]` and `[[ubi-universal-basic-income]]`
**Evidence:**
```
## Related concepts

- [[economic-inequality]]
- [[ubi-universal-basic-income]]
- [[productivity-wage-gap]]
```
**Suggested fix:** Either compile the missing concepts or remove the broken wikilinks. If these concepts are pending compilation, add `[pending]` annotation.

---

## Issue 7: Too many key points — 11 (prefer 5-10)

**File:** wiki/sources/src_11-minutes-hack-github.md
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Key points section has 11 bullet points (maximum 10 recommended)
**Evidence:**
```
11 bullet points from "3,800 internal repos" through "Các mục tiêu trước: Trivy, Kics..."
```
**Suggested fix:** Consolidate the last 2-3 related points (e.g., the TeamPCP items and previous targets into fewer points)

---

## Issue 8: Too many key points — 11 (prefer 5-10)

**File:** wiki/sources/src_ai-will-destroy-world-economy.md
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Key points section has 11 bullet points (maximum 10 recommended)
**Evidence:**
```
11 bullet points from "Mustafa Suleyman..." through "Lời khuyên: Người xây dựng AI..."
```
**Suggested fix:** Consolidate related economic points or merge the two UBI-related items

---

## Issue 9: Pending concept compilations — 13 missing concept files

**File:** Multiple source files (5 affected)
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Source files reference 13 concept files that don't exist yet in `wiki/concepts/`. These concepts are pending compilation by OpenClaw Compile Agent.
**Evidence:**

From `src_11-minutes-hack-github.md`:
- [[orphan-commit-attack]], [[dns-tunneling]], [[dead-drop-communication]], [[github-security]]

From `src_ai-will-destroy-world-economy.md`:
- [[economic-inequality]], [[ubi-universal-basic-income]], [[financial-crisis-2008-comparison]]

From `src_hermes-polymarket-btc-trading-agent.md`:
- [[prediction-markets]], [[crypto-trading-bots]], [[self-learning-agents]], [[bittensor]]

From `src_hermes-xurl-skill-guide.md`:
- [[supergrok-subscription]], [[nous-research]]

**Suggested fix:** Compile the missing concept files. Alternatively, remove unreferenced wikilinks if the concepts won't be compiled.

---

## Issue 10: Broken wikilinks in concept "Related concepts"

**File:** Multiple concept files (2 affected)
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Concept files reference other concepts that have not been compiled yet.

From `wiki/concepts/team-pcp-hacker-group.md`:
- [[orphan-commit-attack]]

From `wiki/concepts/hermes-agent.md`:
- [[self-learning-agents]], [[mcp-model-context-protocol]]

**Suggested fix:** Same as Issue 9 — compile missing concepts or annotate as pending.

---

## Issue 11: Empty Notes sections across all 14 new concept files

**File:** All new concept files (14 files in `wiki/concepts/`)
**Severity:** INFO
**Dimension:** Completeness
**Issue:** All 14 newly compiled concept files have an empty `## Notes` section with no content. Notes is optional (for Julius's annotations), but having it present and empty across all files suggests a template artifact.
**Evidence:**
```
## Notes
```
(followed by nothing — consistently across all new concept files)
**Suggested fix:** Either populate Notes with relevant annotations or remove the empty section. Consider whether the compile-agent template should conditionally include Notes only when there's content.

---

## Summary

| Severity | Count | Files affected |
|---|---|---|
| ERROR | 0 | — |
| WARNING | 6 | 6 files |
| INFO | 5 | 19 files |

**Top issues by type:**
1. Completeness — insufficient key ideas (3 files with 4 key points, need 5-10)
2. Broken wikilinks — 15+ missing concept references across source and concept files
3. Empty sections — Original excerpts (source) and Notes (concepts)

**Overall quality assessment: Good.** No ERROR-level issues found. All required sections are present and definitions are properly formed (2-3 sentences). Vietnamese quality is strong with only one minor typo. The main improvement areas are: consolidating key points to 5-10 range, populating empty sections, and compiling the 13 pending concept files.
