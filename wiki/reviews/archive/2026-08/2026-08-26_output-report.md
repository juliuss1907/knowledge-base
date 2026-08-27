# Output Validation — 2026-08-26

**Status:** approved
**Issues found:** 2 (0 ERROR, 1 WARNING, 1 INFO)
**Created:** 2026-08-26 23:02:00
**Validator:** output-validator

---

## Scope

- **Files checked:** 724 (184 sources + 540 concepts)
- **New files today:** 13 (4 sources + 9 concepts)
  - **Sources (4):**
    - `wiki/sources/src_5-most-important-skills-2026-stoic-wisdoms.md`
    - `wiki/sources/src_habits-of-ai-writing-a16z-crypto.md`
    - `wiki/sources/src_impossible-to-manipulate-dan-koe.md`
    - `wiki/sources/src_this-essay-is-10-percent-ai-generated.md`
  - **Concepts (9):**
    - `critical-thinking.md`
    - `attention-management.md`
    - `financial-literacy.md`
    - `three-levels-of-thinking.md`
    - `ai-writing-hallmarks.md`
    - `paraphrase-test.md`
    - `author-function.md`
    - `ai-text-watermarking.md`
    - `intellectual-obesity.md`
- **Existing files:** quick-scan + targeted sweeps (variant-5 manual grep per SKILL mandate)

## Headline

Batch mới **sạch gần như hoàn toàn**: 12/13 file PASS hết 4 chiều (factual, completeness, coherence, Vietnamese). Lần thứ TƯ liên tiếp dropped-i variant-5 grep = 0 trên toàn KB, và cả 5 biến thể typo Compile Agent (ngưởi / double-i / spacing merge / capital-I / dropped-i) đều = 0 instances. Không file mới nào dính depth-debt baseline (mọi concept mới có definition 2-3 câu + 6+ key ideas). 4 frontmatter `original:` link → `raw/articles/` đều tồn tại.

---

## Issue 1: Forward-reference wikilinks tới 3 concept chưa tồn tại

**File:** `wiki/concepts/attention-management.md`, `wiki/concepts/ai-text-watermarking.md`
**Severity:** WARNING
**Dimension:** Completeness

3 wikilink trong `/## Related concepts` trỏ tới target `wiki/concepts/` chưa tồn tại:

| Target | Referenced from | Ref count (KB-wide) |
|---|---|---|
| `[[deep-work]]` | `attention-management.md` | 4 |
| `[[llm-output-detection]]` | `ai-text-watermarking.md` | 2 |
| `[[synthid]]` | `ai-text-watermarking.md` | 2 |

**Evidence:** `attention-management.md` line 34 `- [[deep-work]]`; `ai-text-watermarking.md` line 35 `- [[llm-output-detection]]`, line 36 `- [[synthid]]`.

**Assessment:** Đây là **forward-reference hợp lệ, KHÔNG phải broken link mới**:
- `deep-work` đã nằm trong Top-20 broken-target pool của Format 08-25 report (4 refs) — backlog pre-existing.
- `synthid` + `llm-output-detection` từng được ghi nhận trong Output 08-16 report (archive) là forward-refs sẽ resolve khi Compile Agent xử lý thêm raw sources.
- 3 target này resolve tự nhiên khi concept tương ứng được compile — precedent khẳng định qua các report 08-16, 08-24, 08-25 (đều "no action required").

**Suggested fix:** None — không cần Fix Agent action. Theo dõi trong pool broken-wikilink của Format Validator. Note nhỏ cho Compile Agent: `deep-work` đã có 4 refs KB-wide, ưu tiên compile concept này để resolve.

---

## Issue 2: Section `## Notes` rỗng ở EOF `ai-text-watermarking.md`

**File:** `wiki/concepts/ai-text-watermarking.md`
**Severity:** INFO
**Dimension:** Completeness

File có section `## Notes` ở cuối (line 44) nhưng content rỗng (0 dòng sau header).

**Evidence:** `tail -6` cho thấy `## Sources` → 2 bullet → `## Notes` kết thúc file, không có nội dung sau header.

**Assessment:** Section `## Notes` là OPTIONAL theo format-spec §2.3 ("INFO: Could add optional `## Notes` section"). Đây không phải ERROR (spec chỉ yêu cầu Definition/Key ideas/Related concepts/Sources). Section rỗng chỉ là cosmetic — bỏ qua, không ảnh hưởng tham chiếu.

**Suggested fix:** Optional — Fix Agent có thể xóa header `## Notes` rỗng (hoặc Julius điền annotation). Không blocking.

---

## Verification

- **Typo detectors (all 5 variants):** 0 instances / 0 files — `ngưởi`, double-i, spacing merge, capital-I, dropped-i grep (3 sub-pattern sub1/sub2/sub3) all clean.
- **Depth-debt baseline:** 0 file mới bị ảnh hưởng — không concept mới nào nằm trong 111-definition ≤1 câu / 84-key-ideas<5 subsets.
- **Truncated detection:** 0 file truncated (không thiếu `## Related concepts` / `## Sources`).
- **Empty sections:** 0 (chỉ `## Notes` rỗng ở Issue 2 — optional section).
- **Wikilinks:** 4 frontmatter `original:` → `raw/articles/` tồn tại; 3 forward-refs (Issue 1).
