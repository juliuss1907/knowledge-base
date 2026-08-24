# Output Validation — 2026-08-24

**Status:** pending
**Issues found:** 3 (0 ERROR, 2 WARNING, 1 INFO)
**Created:** 2026-08-24 23:06:38
**Validator:** output-validator

---

## Scope

- **Files checked:** 708 (179 sources + 529 concepts)
- **New files today:** 4 (1 source + 3 concepts) — `src_the-golden-rule-for-becoming-a-better-writer.md`, `flow-state.md`, `reading-brain-vs-digital-brain.md`, `read-widely-write-well.md`
- **Dropped-i variant 5 grep (mandatory, run manually):** sub-patterns `ngườ[ ,.\t;:!?)]`, `thờ (đại|gian|hiện|điểm|kỳ|buổi|trẻ)|đồng thờ[^i]`, `thay v ` — **0 matches** toàn KB. Sạch.
- **Quick-scan typo sweep:** cả 5 biến thể (ngưởi / double-i / spacing merge / capital-I) = 0 files, 0 instances, new: 0. Lần đầu toàn bộ inventory typo carry-over = 0 sau khi batch 08-23 được apply.

---

## Issue 1: Quick-scan heuristic đếm nhầm numbered list là "Empty Key ideas"

**File:** wiki/concepts/{ai-coach-prompting, ai-first-business-model, content-generation-workflow, digital-product-flywheel, expert-knowledge-extraction, google-project-oxygen, multi-agent-taxonomy, personal-branding-ai, six-stage-research-pipeline}.md
**Severity:** WARNING
**Dimension:** Completeness (false positive — tooling issue, không phải content issue)
**Issue:** quick-scan.sh section 6 chỉ đếm bullet `- ` trong `## Key ideas`; 9 file này dùng numbered list (`1.` `2.` ...). Python cross-check xác nhận **không file nào thực sự empty** — nội dung đầy đủ. Cờ "Empty Key ideas: 9" của quick-scan là false positive do heuristic.
**Evidence:** `google-project-oxygen.md` Key ideas bắt đầu bằng "**8 Behaviors của great manager...** 1. **Good coach** 🥇 2. Empowers team..."; `six-stage-research-pipeline.md` dùng markdown table; các file còn lại dùng `1. **...**`.
**Suggested fix:** Patch quick-scan.sh section 6: `grep -c '^- '` → `grep -cE '^- |^[0-9]+\. '`. Không cần sửa content.

---

## Issue 2: Heuristic "1-sentence definitions" báo 527/527 concepts trên toàn KB

**File:** wiki/reviews/_action-required.md (quick-scan output — tooling)
**Severity:** WARNING
**Dimension:** Completeness (false positive — tooling)
**Issue:** Quick-scan báo "📝 1-sentence definitions: 527 concepts" = 100% KB, trong khi 3 concept mới hôm nay đều có definition 2–4 câu rõ ràng (verified by read). Sed range `/^## Definition$/,/^## /p` + `grep -c '\.'` đếm số DÒNG chứa dấu chấm, không phải số câu — một đoạn văn nhiều câu liền 1 dòng chỉ được đếm 1.
**Evidence:** `flow-state.md` Definition = 3 câu trên 1 dòng → count = 1. Mọi file có cùng cấu trúc đều bị đếm sai tương tự.
**Suggested fix:** Patch quick-scan.sh section 3: thay `grep -c '\.'` bằng đếm câu thật, ví dụ đếm dấu chấm theo text: `grep -o '[.!?]' | wc -l` trên phần definition (hoặc bỏ hẳn check này vì đã chứng minh vô dụng từ nhiều run).

---

## Issue 3: Attribution "Reader, Come Home" chưa đối chiếu trực tiếp với nguồn gốc

**File:** wiki/sources/src_the-golden-rule-for-becoming-a-better-writer.md
**Severity:** INFO
**Dimension:** Factual
**Issue:** Source và 2 concepts (`reading-brain-vs-digital-brain.md`, `read-widely-write-well.md`) quy các claims về não đọc/não số cho Maryanne Wolf, "Reader, Come Home". Tên sách + tác giả nhất quán nội bộ giữa 3 file và khớp sách có thật của Maryanne Wolf (2026 edition context: xuất bản gốc 2018, subtitle "The Reading Brain in a Digital World"). Tuy nhiên validator chỉ verify được qua blog trung gian (nappertime.com), không đối chiếu trực tiếp chương/nội dung sách.
**Evidence:** Line 23 source: "nghiên cứu của Maryanne Wolf trong \"Reader, Come Home\""; line 20 `reading-brain-vs-digital-brain.md`: "Maryanne Wolf phân tích trong \"Reader, Come Home: The Reading Brain in a Digital World\"".
**Suggested fix:** Không bắt buộc — attribution nhất quán và hợp lý. Nếu Julius muốn chắc: spot-check chương về "deep reading" trong bản in/ebook.

---

## Files validated today — verdicts

| File | Type | Verdict |
|---|---|---|
| src_the-golden-rule-for-becoming-a-better-writer.md | source | PASS — summary 5 câu, 10 key points, excerpts nguyên văn, 3 wikilinks resolve hết |
| flow-state.md | concept | PASS — definition 3 câu, 5 key ideas, structure đặc biệt đầy đủ (Goal Structure, 5-step process), sources nêu attribution Csikszentmihalyi đúng |
| reading-brain-vs-digital-brain.md | concept | PASS — definition 2 câu, 6 key ideas, links hợp lệ |
| read-widely-write-well.md | concept | PASS — definition 2 câu, 7 key ideas, links hợp lệ |

File mới sạch hoàn toàn: 0 typo mới (cả 5 biến thể), 0 broken link, 0 truncated section, Vietnamese tự nhiên không MT-artifact.

---

## Summary

Batch nhỏ, chất lượng cao. 4 file mới đạt PROMOTE-grade — đây là batch đầu tiên kể từ 2026-06 mà **toàn bộ 5 biến thể typo Compile Agent = 0**, xác nhận Fix Agent đã xử lý dứt điểm inventory cũ ngày 08-24. 2 WARNING còn lại là false positive của tooling quick-scan (numbered-list Key ideas + sentence-count heuristic), không phải vấn đề content — recommend patch script, ưu tiên thấp hơn content fixes thông thường. 1 INFO attribution không blocking.

**Systemic note:** Không escalate `[SYSTEMATIC ISSUE]` lần này — 0 instance typo trên file mới. Chuỗi lỗi tokenization 'ờ'+i của Compile Agent có vẻ đã ngừng phát sinh file mới mang lỗi từ ~08-23.
