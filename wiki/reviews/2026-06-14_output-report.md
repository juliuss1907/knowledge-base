# Output Validation — 2026-06-14

**Status:** pending
**Issues found:** 20
**Created:** 2026-06-14 22:15:00
**Validator:** output-validator

---

## Issue 1: [Systematic] Broken concept backlinks

**File:** 154 concept files + 127 source files
**Severity:** ERROR
**Dimension:** Factual
**Issue:** 281 backlinks trỏ đến các concepts/sources không tồn tại. Các target phổ biến nhất: confirmation-bias (6), game-theory (5), ai-coding-agents (4), pareto-principle (4), second-law-of-thermodynamics (3), career-design (3), decision-making (3).
**Evidence:** `[[momentum]]` trong `activation-energy.md`; `[[economic-inequality]]` trong `ai-white-collar-automation.md`; `[[agent-initiated-code-artifacts]]` trong `agent-harness.md`
**Suggested fix:** Compile Agent cần kiểm tra backlink tồn tại trước khi ghi, hoặc Index Agent cần tạo các concepts này.

---

## Issue 2: [Systematic] Widespread draft status

**File:** ~160 concept files
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Hơn một nửa số concepts có `status: draft` mặc dù nội dung đã đầy đủ (có Definition, Key ideas, Sources). Nhiều file draft đã được compile từ nhiều ngày trước nhưng chưa được promote.
**Evidence:** `activation-energy.md`, `hypergamy.md`, `relationship-dynamics.md`, `entropy.md`, `inversion.md`, `systems-thinking.md`, `first-principles-thinking.md`, `probabilistic-thinking.md`, `mental-models.md`
**Suggested fix:** Review và promote các file draft có nội dung đầy đủ sang `status: reviewed`. Các file cần cải thiện nên giữ draft.

---

## Issue 3: [Systematic] English-only concepts

**File:** ~15 concept files
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** Một số concepts được viết hoàn toàn bằng tiếng Anh, không có tiếng Việt. Điều này mâu thuẫn với tiêu chuẩn wiki (tiếng Việt chính, giữ thuật ngữ kỹ thuật bằng tiếng Anh).
**Evidence:** `abstraction-layer-fallacy.md` (en=119, vi=0); `active-thinking.md` (en=118, vi=0); `ashbys-law.md` (en=171, vi=0); `complex-adaptive-systems.md` (en=165, vi=0); `complicated-vs-complex.md` (en=160, vi=0); `cynefin-framework.md` (en=162, vi=0); `information-compression.md` (en=78, vi=0); `lazy-thinking.md` (en=127, vi=0); `nice-syndrome.md` (en=100, vi=0); `organizational-incrementalism.md` (en=115, vi=0); `philosopher-syndrome.md` (en=111, vi=0); `systems-thinking-limitations.md` (en=150, vi=0)
**Suggested fix:** Dịch Definition và Key ideas sang tiếng Việt, giữ thuật ngữ kỹ thuật bằng tiếng Anh.

---

## Issue 4: Missing Key ideas section

**File:** `wiki/concepts/csa-hca-attention.md`
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** File có `## Definition` và `## Sources` nhưng thiếu `## Key ideas`
**Evidence:** Body sections: Definition, How it works, Comparison with GQA, Results, Related concepts, Sources, Notes
**Suggested fix:** Thêm `## Key ideas` với 3-5 bullet points tóm tắt các ý chính.

---

## Issue 5: Missing Key ideas section

**File:** `wiki/concepts/fp4-lightning-indexer.md`
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** File có `## Definition` và `## Sources` nhưng thiếu `## Key ideas`
**Evidence:** Body sections: Definition, Three-layer compression, Multi-agent advantage, Economic profile, Related concepts, Sources, Notes
**Suggested fix:** Thêm `## Key ideas` với 3-5 bullet points.

---

## Issue 6: Missing Key ideas section

**File:** `wiki/concepts/dollar-as-rent-payment.md`
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** File có `## Definition` và `## Sources` nhưng thiếu `## Key ideas`
**Evidence:** Body sections: Definition, The mechanism, Key insight, Implication for collapse, Related concepts, Sources, Notes
**Suggested fix:** Thêm `## Key ideas` với 3-5 bullet points.

---

## Issue 7: Missing Key ideas section

**File:** `wiki/concepts/deepseek-v4-flash-vs-pro.md`
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** File có `## Definition` và `## Sources` nhưng thiếu `## Key ideas`
**Evidence:** Body sections: Definition, Comparison, Key differences, Practitioner guidance, Related concepts, Sources, Notes
**Suggested fix:** Thêm `## Key ideas` với 3-5 bullet points.

---

## Issue 8: Missing Key ideas section

**File:** `wiki/concepts/existential-vacuum.md`
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** File có `## Definition` và `## Sources` nhưng thiếu `## Key ideas`
**Evidence:** Body sections: Definition, In modern society, The trap, Related concepts, Sources, Notes
**Suggested fix:** Thêm `## Key ideas` với 3-5 bullet points.

---

## Issue 9: Missing Key ideas section

**File:** `wiki/concepts/false-reinforcement-loop.md`
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** File có `## Definition` và `## Sources` nhưng thiếu `## Key ideas`
**Evidence:** Body sections: Definition, Example, Kết quả, Related concepts, Sources, Notes
**Suggested fix:** Thêm `## Key ideas` với 3-5 bullet points.

---

## Issue 10: Missing Key ideas section

**File:** `wiki/concepts/kissinger-deal-1974.md`
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** File có `## Definition` và `## Sources` nhưng thiếu `## Key ideas`
**Evidence:** Body sections: Definition, Context, The deal, Why Saudi accepted, Related concepts, Sources, Notes
**Suggested fix:** Thêm `## Key ideas` với 3-5 bullet points.

---

## Issue 11: Missing Key ideas section

**File:** `wiki/concepts/long-context-models.md`
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** File có `## Definition` và `## Sources` nhưng thiếu `## Key ideas`
**Evidence:** Body sections: Definition, Key challenges, Solutions in V4, Benchmark results, Related concepts, Sources, Notes
**Suggested fix:** Thêm `## Key ideas` với 3-5 bullet points.

---

## Issue 12: Missing Key ideas section

**File:** `wiki/concepts/mixture-of-experts-moe.md`
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** File có `## Definition` và `## Sources` nhưng thiếu `## Key ideas`
**Evidence:** Body sections: Definition, Key ideas, Comparison, Related concepts, Sources, Notes
**Suggested fix:** Thêm `## Key ideas` với 3-5 bullet points.

---

## Issue 13: Missing Key ideas section

**File:** `wiki/concepts/petrodollar-system.md`
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** File có `## Definition` và `## Sources` nhưng thiếu `## Key ideas`
**Evidence:** Body sections: Definition, The common myth, The real foundation, Current status, Related concepts, Sources, Notes
**Suggested fix:** Thêm `## Key ideas` với 3-5 bullet points.

---

## Issue 14: Missing Key ideas section

**File:** `wiki/concepts/policy-review-framework.md`
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** File có `## Definition` và `## Sources` nhưng thiếu `## Key ideas`
**Evidence:** Body sections: Definition, Four components, Sai lầm phổ biến, Related concepts, Sources, Notes
**Suggested fix:** Thêm `## Key ideas` với 3-5 bullet points.

---

## Issue 15: Missing Key ideas section

**File:** `wiki/concepts/saudi-pakistan-defense-agreement.md`
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** File có `## Definition` và `## Sources` nhưng thiếu `## Key ideas`
**Evidence:** Body sections: Definition, Significance, Context, Related concepts, Sources, Notes
**Suggested fix:** Thêm `## Key ideas` với 3-5 bullet points.

---

## Issue 16: Missing Key ideas section

**File:** `wiki/concepts/tragic-optimism.md`
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** File có `## Definition` và `## Sources` nhưng thiếu `## Key ideas`
**Evidence:** Body sections: Definition, Core idea, From concentration camps, The ultimate freedom, Related concepts, Sources, Notes
**Suggested fix:** Thêm `## Key ideas` với 3-5 bullet points.

---

## Issue 17: Missing Key ideas section

**File:** `wiki/concepts/us-security-umbrella.md`
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** File có `## Definition` và `## Sources` nhưng thiếu `## Key ideas`
**Evidence:** Body sections: Definition, Evidence of erosion, Saudi response, Related concepts, Sources, Notes
**Suggested fix:** Thêm `## Key ideas` với 3-5 bullet points.

---

## Issue 18: Sources section nearly empty

**File:** `wiki/concepts/ai-white-collar-automation.md`
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Sources section chỉ có link `[[src_ai-will-destroy-world-economy]]` mà không có mô tả
**Evidence:** `## Sources\n\n- [[src_ai-will-destroy-world-economy]]`
**Suggested fix:** Thêm mô tả nguồn (vd: "Bài viết từ ...")

---

## Issue 19: Sources section nearly empty

**File:** `wiki/concepts/inversion.md`
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Sources section có một dòng mô tả dài nhưng có vẻ là copy-paste từ nội dung bài viết
**Evidence:** `- [[src_inversion]] — Bài viết từ Farnam Street giải thích chi tiết về mental model Inversion...`
**Suggested fix:** Rút gọn mô tả nguồn xuống 1-2 dòng.

---

## Issue 20: Summary too short

**File:** `wiki/sources/src_viktor-frankl-meaning-video.md`
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Summary chỉ có 1 câu
**Evidence:** `Triết lý của Viktor Frankl, người sống sót qua trại tập trung Đức Quốc xã: ý nghĩa cuộc sống không đến từ tiền bạc, danh vọng hay khoái lạc...`
**Suggested fix:** Expand Summary thành 2-3 câu.

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 17 (3 systematic + 14 individual) |
| WARNING | 3 (2 systematic + 1 individual) |
| INFO | 0 |

**Files checked:** 364 (282 concepts + 82 sources)
**New files since last run:** ~20 (compiled 2026-06-14)

### Systemic issues flagged
1. **Broken backlinks:** 281 instances across 154 concepts + 127 sources — Compile Agent cần verify links trước khi ghi
2. **Draft status:** ~160 concepts vẫn ở draft — cần review batch promote
3. **English-only:** ~15 concepts không có tiếng Việt — cần dịch

---

**Verdict:** REVISE — 20 issues across 3 systemic patterns + 14 individual files. Fixable by Fix Agent.
