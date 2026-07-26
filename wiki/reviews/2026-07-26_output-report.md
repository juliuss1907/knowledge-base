# Output Validator Report — 2026-07-26 (23:14 Update)

**Status:** pending
**Issues found:** 5
**Created:** 2026-07-26 23:14:05
**Validator:** output-validator
**Previous run:** 2026-07-26 11:31 (APPROVED & APPLIED by Fix Agent — fixed dropped-i typos in 6 files)
**Files checked:** 627 (155 sources + 472 concepts)
**New files:** 8 (2 sources + 6 concepts)
**Quick-scan:** Clean — 0 new mechanical typos (ngưởi, double-i, spacing-merge, capital-I, variant-5 dropped-i)

---

## Previous approved run context

Morning run at 11:31 found 2 issues (1 ERROR + 1 INFO):
- **ERROR:** Dropped-i typos (variant 5) in 6/8 new files (~10 instances): `thờ điểm`, `ngườ dùng`, `thờ gian`, `thay v`
- **INFO:** "thay v" word fragment in 2 files

Fix Agent applied corrections 2026-07-26. All 6 affected files now clean. This rerun validates post-fix state — the 5 issues below are net-new findings not present in the morning report.

---

## Issue 1–2: [SYSTEMATIC ISSUE] 13 forward-reference wikilinks point to missing concepts

**File:** 6 concept files (all new files today)
**Severity:** ERROR
**Dimension:** Completeness / Factual
**Issue:** Tất cả 6 concept files được tạo hôm nay chứa wikilinks đến các concept chưa tồn tại. 13 target concepts hoàn toàn không có file trong `wiki/concepts/`. Đây không phải lỗi riêng lẻ — Compile Agent liên tục tạo forward references đến các concepts chưa được biên dịch.

**Evidence — danh sách đầy đủ các target bị thiếu kèm file nguồn:**

| File nguồn | Target missing |
|---|---|
| `wiki/concepts/agent-backtesting.md` | `[[quantitative-finance]]`, `[[reinforcement-learning-environments]]` |
| `wiki/concepts/ai-agent-tool-orchestration.md` | `[[mcp-protocol]]`, `[[agent-capability-discovery]]` |
| `wiki/concepts/frozen-corpus-search.md` | `[[web-archiving]]`, `[[temporal-databases]]` |
| `wiki/concepts/pay-per-call-pricing.md` | `[[usage-based-pricing]]`, `[[api-economics]]`, `[[serverless-pricing]]` |
| `wiki/concepts/point-in-time-data.md` | `[[temporal-versioning]]`, `[[bimodal-data]]` |
| `wiki/concepts/unified-api-gateway.md` | `[[api-aggregator]]`, `[[microservices-gateway]]` |

**Affected:** 6/6 concept files (100%). Source files không bị ảnh hưởng — các source chỉ link đến concepts đã tồn tại hôm nay.

**Suggested fix:**
1. Compile 13 missing concepts từ raw sources hoặc tạo stub drafts
2. Hoặc: remove các wikilinks chưa có target, thay bằng plain text references
3. Recommend review compile-agent prompt để ngăn forward references trong tương lai

**Pattern note:** Đây là recurring pattern — các batch trước cũng có forward references. Nếu không được giải quyết, các file này sẽ có dead links vĩnh viễn.

---

## Issue 3: Code-switching quá mức trong Challenges section

**File:** `wiki/concepts/agent-backtesting.md`
**Severity:** WARNING
**Dimension:** Vietnamese quality
**Issue:** Section `## Challenges` chứa tỷ lệ tiếng Anh ~60% — các bullet point gần như là câu tiếng Anh với một vài từ tiếng Việt rải rác. Điều này làm giảm readability cho người đọc tiếng Việt.

**Evidence:**
> "Data leakage prevention: Đảm bảo agent không access information from the 'future'"
> "Look-ahead bias: Tránh situations nơi strategy dùng information không available tại thời điểm quyết định"
> "Overfitting: Agent optimize quá mức cho historical data mà không generalize cho future"

**Suggested fix:** Viết lại các bullet point bằng tiếng Việt hoàn chỉnh, giữ technical terms trong ngoặc đơn nếu cần. Ví dụ: "Rò rỉ dữ liệu (data leakage): Đảm bảo agent không truy cập thông tin từ 'tương lai'."

---

## Issue 4: Từ tiếng Anh không cần thiết trong Definition

**File:** `wiki/concepts/point-in-time-data.md`
**Severity:** WARNING
**Dimension:** Vietnamese quality
**Issue:** Definition section chứa các từ tiếng Anh có thể thay thế dễ dàng bằng tiếng Việt. "contaminate" → "nhiễm", "critical" → "thiết yếu", "subsequent updates" → "cập nhật sau đó", "revisions" → "chỉnh sửa".

**Evidence:**
> "...không bị contaminate bởi subsequent updates hoặc revisions."
> "...điều này critical cho việc đánh giá models trên historical scenarios..."

**Suggested fix:** Thay thế các từ tiếng Anh không phải technical terms bằng tiếng Việt tương đương. Technical terms như "look-ahead bias", "AI/ML" được giữ nguyên.

---

## Issue 5: Summary section hơi ngắn

**File:** `wiki/sources/src_introducing-backsearch-gr-inc.md`
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Summary section chỉ có 2 câu. Mặc dù đủ để truyền đạt nội dung chính, nhưng có thể mở rộng thêm 1-2 câu để bao quát đầy đủ hơn (pricing model, integration capabilities).

**Evidence:** Toàn bộ Summary section là 2 câu dài — không có lỗi nội dung, chỉ là hơi ngắn so với các source files khác (thường 3-5 câu).

**Suggested fix:** Thêm 1-2 câu về pricing model ($10/1K searches) và tích hợp OpenReward.

---

## Summary

| Severity | Count | Details |
|---|---|---|
| ERROR | 1 (systemic, 13 instances) | Forward-reference wikilinks đến concepts không tồn tại |
| WARNING | 2 | Code-switching quá mức (agent-backtesting), từ Anh trong definition (point-in-time-data) |
| INFO | 1 | Summary hơi ngắn (src_introducing-backsearch-gr-inc) |

**Tổng thể đánh giá batch:** Chất lượng cơ bản tốt — không có lỗi chính tả cơ học (sạch cả 5 variants), không có file bị cắt cụt, định dạng đúng. Vấn đề chính là forward-reference wikilinks (systematic pattern) và English-heavy phrasing ở một số sections.
