# Output Validation — 2026-08-25

**Status:** approved
**Issues found:** 3 (0 ERROR, 2 WARNING, 1 INFO)
**Created:** 2026-08-25 23:01
**Validator:** output-validator

---

## Scope

- **Files checked:** 712 (180 sources + 532 concepts)
- **New files today:** 6 (1 source + 5 concepts — daily-planning cluster từ Dickie Bush post 2026-08-21)
  - `wiki/sources/src_daily-planning-routine-creativity-productivity.md`
  - `wiki/concepts/busywork-vs-deep-work.md`
  - `wiki/concepts/five-types-of-business-work.md`
  - `wiki/concepts/gtd-four-lists.md`
  - `wiki/concepts/leverage.md`
  - `wiki/concepts/one-thing-daily-priority.md`
- Existing files: quick-scan + targeted sweeps (variant-5 manual grep per SKILL mandate)

## Headline

Batch mới sạch hoàn toàn: 6/6 file PASS hết 4 chiều (factual, completeness, coherence, Vietnamese). 0 typo trong file mới, wikilink resolve đầy đủ (23 links unique, kể cả `original:` trỏ về raw/posts/ tồn tại). Lần thứ BA liên tiếp dropped-i variant-5 grep = 0 matches trên toàn KB.

Tin đáng chú ý: lần đầu tiên sau khi patch quick-scan (08-25), hai counter "1-sentence definitions" và "<5 key points" cho số LIỆU THẬT thay vì false positive — lộ ra một kho nợ depth legacy chưa từng được đo chính xác.

---

## Issue 1: Carry-over capital-I typos — sub-pattern MỚI nằm ngoài mọi detector

**File:** 5 files cũ (không phải batch hôm nay)
**Severity:** WARNING
**Dimension:** Vietnamese

5 instances capital-I trong từ tiếng Việt ở 5 file khác nhau — nhưng lần này chữ trước `I` là chữ cái ASCII thường, KHÔNG phải nguyên âm có dấu. Toàn bộ detector hiện có (quick-scan variant-4 `[diacritic]I\b` + broad sweep `[a-zà-ỹ]I`) đều bỏ sót vì pattern class khác:

| File | Line | Sai | Đúng |
|---|---|---|---|
| `wiki/sources/src_the-5-laws-of-people-who-never-chase.md` | 28 | `tương laI` | `tương lai` |
| `wiki/sources/src_is-there-anything-left-build-crypto-wintermute.md` | 24 | `tương laI` | `tương lai` |
| `wiki/concepts/machine-economy.md` | 42 | `khả thI` | `khả thi` |
| `wiki/concepts/agentic-commerce.md` | 16 | `thực thI` | `thực thi` |
| `wiki/concepts/autonomous-agents.md` | 16 | `thực thI` | `thực thi` |

**Evidence:** grep context xác nhận cả 5 đều là typo thật (URL YouTube `_fDEpfGO_cI` trong steve-jobs là false positive duy nhất của broad sweep, đã loại).
**Suggested fix:** sed từng file:
```bash
sed -i 's/tương laI/tương lai/g' <2 source files>
sed -i 's/thực thI/thực thi/g' <agentic-commerce> <autonomous-agents>
sed -i 's/khả thI/khả thi/g' <machine-economy>
```

---

## Issue 2: [SYSTEMIC] Legacy depth-debt — baseline đầu tiên đo được chính xác

**File:** 195 concepts (aggregate — không liệt kê individually)
**Severity:** WARNING
**Dimension:** Completeness

Sau khi patch quick-scan 08-25 (counter sentence-count + numbered-list), 2 heuristic cho kết quả TRUSTWORTHY lần đầu. Spot-check thủ công xác nhận đây là dữ liệu thật, không phải false-positive era nữa:

- **111 concepts** có Definition ≤ 1 câu (tiêu chuẩn: 2-3 câu). Verified samples: `agentic-commerce`, `ai-coach-prompting`, `autonomous-agents` — definition thật sự chỉ 1 câu dài.
- **84 concepts** có Key ideas < 5 items (tiêu chuẩn: 5-10). Verified sample: `mental-models.md` chỉ 3 bullets thật.

Đặc điểm quan trọng: **0/195 file này thuộc batch gần đây** — toàn bộ `last_updated` < 2026-08. Đây là nợ tích lũy từ các batch trước chuẩn hiện tại, không phải regression. Batch 08-25 đạt chuẩn đầy đủ (definitions 2-3 câu, 7-8 key ideas mỗi concept).

**Suggested fix:** Quyết định chiến lược với Julius — (a) chấp nhận làm baseline và chỉ enforce chuẩn cho batch mới, hoặc (b) lập kế hoạch backfill từ từ (ví dụ 5-10 concepts/lần Fix Agent chạy). Không khuyến nghị sửa hàng loạt một lúc.

---

## Issue 3: Detection gap — quick-scan chưa phủ capital-I sau chữ ASCII

**File:** `.hermes/skills/output-validator/scripts/quick-scan.sh` (tooling, không phải wiki)
**Severity:** INFO
**Dimension:** Vietnamese (detection coverage)

Variant-4 hiện tại chỉ match `[diacritic-vowel]I`. Batch hôm nay chứng minh typo còn xuất hiện dạng `[ascii-letter]I` (`laI`, `thI`). Pattern đề xuất bổ sung (loại trừ acronym bằng word-boundary + blacklist `AI`, `UI`, `CI`... trong URL/code):

```bash
grep -rPn '\b[a-zà-ỹ]{2,}I\b' wiki/sources/ wiki/concepts/ | grep -vP '(http|\.com|youtu)'
```

Cần tinh chỉnh để không re-create vụ hủy diệt acronym "AI" tháng 08-25 (xem Production Lessons) — khuyến nghị chỉ match khi ký tự cuối trước `I` là `h` hoặc `c` hoặc thêm whitelist từ (`laI|thI|sI|nI`).

**Suggested fix:** Thêm check section 2c vào quick-scan.sh HOẶC ghi nhận vào Production Lessons như known gap và xử lý bằng manual grep định kỳ.

---

## Files validated — new batch detail (all PASS)

| File | Def sentences | Key ideas | Links | Typos | Verdict |
|---|---|---|---|---|---|
| src_daily-planning-routine | n/a (Summary 5 câu ✓) | 9 key points | 5/5 resolve | 0 | PASS |
| busywork-vs-deep-work | 3 | 8 | 10/10 | 0 | PASS |
| five-types-of-business-work | 3 | 8 | 8/8 | 0 | PASS |
| gtd-four-lists | 2 | 7 | 8/8 | 0 | PASS |
| leverage | 2 | 9 | 15/15 | 0 | PASS |
| one-thing-daily-priority | 2 | 7 | 7/7 | 0 | PASS |

Coherence: source ↔ 5 concepts nhất quán (framework 5 nhóm, 4 lists GTD, one-thing, leverage= output/input — không mâu thuẫn chéo). Attribution sạch: David Allen (GTD gốc), Naval Ravikant (3 levers), Dickie Bush (framework) đều được ghi đúng chủ thể.

Factual: không phát hiện claim sai. Con số trong source (444K followers, engagement stats) là metadata từ bài gốc. Flappy Bird $50K/ngày và 2000h/năm labor cap là claims được attribute rõ vào source `src_3-ways-to-get-rich`.

## Checks performed

- quick-scan.sh full run (post-patch counters)
- Variant-5 dropped-i manual grep ×3 patterns (SKILL mandate): **0 matches** — clean run thứ 3 liên tiếp
- Broad capital-I sweeps ×2 patterns (diacritic-preceded: 0; ascii-preceded: 5 real)
- Wikilink resolution: toàn bộ link trong 6 file mới (kể cả frontmatter `original:` → raw/)
- Section completeness + truncation check: 0 truncated
- Spot-check depth counters trên sample files (đối chiếu quick-scan vs sed/grep trực tiếp)

## Summary

| Severity | Count |
|---|---|
| ERROR | 0 |
| WARNING | 2 |
| INFO | 1 |

ERROR streak tiếp tục: ngày thứ 9 liên tiếp không có ERROR. File mới sạch 100%. Hai WARNING đều thuộc kho nợ cũ/tooling, không chặn referencing batch mới.
