# Format Validation — 2026-06-30

**Status:** pending
**Issues found:** 439 (128 ERROR, 311 WARNING, 0 INFO)
**Created:** 2026-06-30 23:17:02 +0700
**Validator:** format-validator
**Scope:** Full KB — 634 files (361 concepts + 112 sources + 33 indexes + 128 topics)

---

## Delta from last approved (2026-06-29 23:15)

| Metric | 2026-06-29 (APPROVED) | 2026-06-30 | Delta |
|---|---|---|---|
| Scope | 628 files | 634 files | **+6** |
| ERROR | 69 | 128 | **+59** |
| WARNING | 317 | 311 | **−6** |
| INFO | 0 | 0 | 0 |

**Positive delta (issues resolved):**
- ✅ **69 tag-file section ERROR → GONE** — Fix Agent đã thêm `## Parent`, `## Stats`, `## Files with this tag` vào tất cả 23 `wiki/tag/*.md`. Xác nhận: tất cả 23 file tag hiện có đủ 3 sections.

**Negative delta (new/regression):**
- 🔴 **+128 topic-file frontmatter ERROR** — regression: 128 `wiki/topic/*.md` files không có YAML frontmatter. Đây là regression từ 06-29 (khi topic frontmatter ERROR đã được resolve). Có thể do Index Agent regenerate topic files không include frontmatter block.
- +2 topic files mới (128 vs 126 ngày 06-28, 127 ngày 06-29)

**WARNING delta:**
- ⚠️ **−6 WARNING**: broken wikilinks giảm nhẹ (311 vs 317)
- 290 individual broken wikilinks (không đổi)
- 21 forward-reference summary groups (không đổi)
- 194 unique broken targets (không đổi)

**Files growth:** +6 files since 06-29 (361 concepts + 112 sources today vs 357 concepts + 111 sources on 06-29)

---

## [SYSTEMATIC VIOLATION] Topic files missing YAML frontmatter — regression

**Pattern:** 128/128 topic files under `wiki/topic/` không có YAML frontmatter (file bắt đầu trực tiếp với `# Topic: <slug>`). Đây là regression: issue tương tự đã được resolve giữa 06-28 và 06-29, nhưng hôm nay xuất hiện trở lại trên toàn bộ 128 topic files.

**Likely cause:** Index Agent regenerate topic files mà không include YAML frontmatter block trong template. Fix Agent từng add frontmatter vào topic files nhưng bị overwrite khi Index Agent chạy lại.

**Affected files:** 128 topic files, ví dụ:
- `wiki/topic/ai-architecture.md` — starts with `# Topic: ai-architecture`
- `wiki/topic/active-thinking.md` — starts with `# Topic: active-thinking`
- ...và 126 files khác

**Expected:** Mỗi topic file cần có YAML frontmatter với tối thiểu các field:
```yaml
---
type: index
scope: topic
topic: <slug>
auto_generated: true
last_updated: YYYY-MM-DD
---
```

**Escalation:** `[SYSTEMATIC VIOLATION]` — 128/128 files thiếu frontmatter. Đây là template issue của Index Agent, không phải individual file errors. Regression từ fix trước đó cho thấy Fix Agent fix từng file không đủ — cần update Index Agent template để include frontmatter trong mọi lần generate.

**Recommendation:**
1. Update `index-agent/SKILL.md` topic file template để include YAML frontmatter block
2. Sau khi template được fix, chạy Index Agent regenerate toàn bộ topic files
3. Không nên dùng Fix Agent patch từng file vì sẽ bị overwrite khi Index Agent chạy lại

---

## Issue Group 1: Missing frontmatter in topic files (128 ERROR)

**Category:** Frontmatter
**Severity:** ERROR
**Count:** 128 (128 topic files × 1 missing frontmatter)

**Current:** Files start directly with `# Topic: <slug>` heading, no YAML frontmatter block (`---` opening not found).

**Expected:** Topic files should have frontmatter with `type: index`, `scope: topic`, `topic`, `auto_generated`, and `last_updated` fields, then the H1 heading.

**Files affected (128):** Tất cả file trong `wiki/topic/`

---

## Issue Group 2: Broken wikilinks — forward references (311 WARNING)

**Category:** Markdown
**Severity:** WARNING
**Count:** 311 (290 individual broken targets + 21 forward-reference summary groups)

**Unique broken targets:** 194 (không đổi từ 06-29)

**Top 20 broken targets:**

| Target | Occurrences |
|---|---|
| `game-theory` | 10 |
| `confirmation-bias` | 8 |
| `pareto-principle` | 6 |
| `ai-coding-agents` | 5 |
| `career-design` | 5 |
| `decision-making` | 5 |
| `deep-work` | 4 |
| `ai-hype-vs-reality` | 3 |
| `economic-inequality` | 3 |
| `critical-thinking` | 3 |
| `naval-ravikant` | 3 |
| `risk-parity` | 3 |
| `second-law-of-thermodynamics` | 3 |
| `saying-no` | 3 |
| `power-imbalance` | 3 |
| `first-order-thinking` | 3 |
| `breaking-point` | 2 |
| `momentum` | 2 |
| `multi-agent-systems` | 2 |
| `dao-legal-structure` | 2 |

**Top 10 files by broken wikilink count:**

| File | WARNINGs |
|---|---|
| `collaborative-thinking.md` | 5 |
| `probabilistic-thinking.md` | 5 |
| `feedback-loops.md` | 4 |
| `hanlons-razor.md` | 4 |
| `meaning-through-work.md` | 4 |
| `occams-broom.md` | 4 |
| `occams-razor.md` | 4 |
| `systematic-trading.md` | 4 |
| `vibe-coding.md` | 4 |
| `activation-energy.md` | 3 |

**Analysis:** Broken wikilink backlog ổn định ở 194 unique targets (same as 06-28 and 06-29). Đây là forward references đến concepts chưa được compile — expected trong KB đang phát triển. Không cần ưu tiên xử lý.

**21 forward-reference summary groups** trong source files: các file source link đến nhiều concept chưa tồn tại, validator gộp thành summary entry (e.g., "9 broken wikilinks (forward-references)"). Tương tự 06-29, không thay đổi.

---

## Summary

| Category | Count | Severity | Action needed |
|---|---|---|---|
| Topic files missing frontmatter | 128 | ERROR | Update Index Agent template + regenerate |
| Broken wikilinks (individual) | 290 | WARNING | Known backlog — no action |
| Forward-reference groups | 21 | WARNING | Known backlog — no action |

**Tag files (23):** Đã xác nhận fix từ 06-29 — tất cả 23 `wiki/tag/*.md` hiện có đủ `## Parent`, `## Stats`, `## Files with this tag`. ✅

**Code block language tags:** Không có ERROR mới về code blocks — regression check từ 06-26 confirmed clean. ✅

---
