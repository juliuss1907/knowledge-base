# Output Validation — 2026-11-02

**Status:** pending
**Issues found:** 1 (0 ERROR, 1 WARNING, 0 INFO)
**Created:** 2026-11-02 23:05:00
**Validator:** output-validator
**Files checked:** 858 (224 sources + 634 concepts)
**New files:** 5 (1 source + 4 concepts)

---

## Issue 1: Too few key points in concept

**File:** wiki/concepts/socratic-prompting.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Section `## Key ideas` chỉ có 4 ý (ngưỡng tối thiểu theo rubric completeness là 5-10 ý).
**Evidence:**
```markdown
## Key ideas

- **Hỏi trước khi làm:** Cấu trúc cốt lõi dựa trên mẫu "Tôi muốn làm [TASK] để đạt [MỤC TIÊU]. Hãy đọc bối cảnh và đặt câu hỏi cho tôi trước khi thực hiện".
- **Làm rõ giả định ẩn:** Quá trình chất vấn giúp người dùng nhận ra các thiếu sót, giới hạn biên hoặc yêu cầu kỹ thuật mà ban đầu chưa lường trước.
- **Quy trình tương tác chuẩn:** AI đưa ra bộ câu hỏi làm rõ → Người dùng phản hồi → AI trình bày kế hoạch xử lý → Người dùng duyệt hoặc điều chỉnh → AI thực thi.
- **Nâng cao chất lượng tác vụ phức tạp:** Đặc biệt hiệu quả với các nhiệm vụ dài hạn, thiết kế hệ thống, viết tài liệu chiến lược hoặc xây dựng agent tự động.
```
**Suggested fix:** Bổ sung ý thứ 5 từ nguồn `src_claude-best-practices-power-user-guide`, ví dụ: vai trò phỏng vấn ngược để rà soát edge cases / tradeoffs cho các bài toán đa nghĩa, hoặc mẫu tương tác form phản hồi tương tác giữa người dùng và Claude.

---

## Summary

- **Files checked:** 858 (224 sources + 634 concepts)
- **New files validated:** 5 (1 source mới: `src_claude-best-practices-power-user-guide.md`, 2 concept mới: `claude-cowork.md`, `socratic-prompting.md`, 2 concept cập nhật: `context-engineering.md`, `context-window-management.md`)
- **Factual accuracy:** 100% luận điểm khớp chính xác với raw source `raw/articles/2026-04-11_claude-best-practices-power-user-guide.md`.
- **Completeness:** 4/5 files đạt chuẩn; 1 concept (`socratic-prompting.md`) có 4/5 key ideas (WARNING).
- **Coherence:** Mạch lập luận chặt chẽ, không có mâu thuẫn nội tại hay trùng lặp ý (Defect B = 0, Defect D = 0).
- **Vietnamese quality:** Ngôn ngữ tự nhiên, dịch ngữ kỹ thuật chính xác, không có lỗi tokenization:
  - `ngưởi`: 0
  - `ngườii/đờii/lờii...` (double-i): 0
  - `người[a-z]` spacing merge: 0
  - `ngườI` capital-I: 0
  - dropped-i variant 5 (`ngườ`, `thờ`, `thay v`, `chính lờ`): 0 (chuỗi 38 lượt sạch liên tiếp)
  - CJK contamination: 0 ký tự Hán ngoại lai
- **Wikilinks & Backlinks:** 100% wikilink mới giải quyết chính xác đến các file tồn tại. Không có forward-ref mới nào. Defect A = 0 (100% khớp giữa frontmatter `sources:` và body `## Sources`). Source dùng `## Key points` chuẩn (Defect C = 0).
- **Raw layer:** `raw/articles/2026-04-11_claude-best-practices-power-user-guide.md` có `status: processed`, `compiled_to: "[[src_claude-best-practices-power-user-guide]]"`. Raw backlog: 0 unprocessed.

---

## Quality Checks

| Dimension | Result | Notes |
|---|---|---|
| Factual accuracy | PASS (5/5) | Luận điểm bám sát nguồn gốc về hệ thống Claude power user 2026, context engineering và Cowork. |
| Completeness | PARTIAL (4/5) | 1 concept (`socratic-prompting.md`) có 4 key ideas (<5). 4 file còn lại đạt 100% tiêu chí. |
| Coherence | PASS (5/5) | Cấu trúc mạch lạc, phân rã khái niệm độc lập và liên kết chặt chẽ. |
| Vietnamese quality | PASS (5/5) | Không lỗi ngữ pháp, không lỗi chính tả, thuật ngữ tiếng Anh giữ nguyên vị trí phù hợp. |

---

## Mechanical Checks

- `quick-scan.sh`: 5 files mới hôm nay; 0 typo `ngưởi`; 0 double-i; 0 spacing merge; 0 capital-I.
- Dropped-i variant 5 (quét thủ công 4 sub-patterns): 0 match. Chuỗi sạch đạt **38 lượt liên tiếp** (08-23 → 11-02).
- CJK contamination: 0 ký tự Hán ngoại lai trong 5 files mới. (Chỉ 3 file hợp lệ toàn KB: `byte-level-bpe.md`, `hundred-years-humiliation.md`, `chinese-culture-confucianism.md`).
- Truncated files: 0 concept/source bị ngắt cụt.
- Empty sections: 0 empty `Key ideas`, 0 empty `Key points`, 0 empty `Sources`.
- Multi-source invariants: 2 concept tích hợp 2 nguồn (`context-engineering.md`, `context-window-management.md`) đều có 2 nguồn ở frontmatter và đúng 2 bullet ở `## Sources` (Defect A = 0).
- Section naming: Source dùng `## Key points`, concepts dùng `## Key ideas` chuẩn spec (Defect C = 0).
- Wikilink resolution: 100% wikilink mới trỏ đến các file hợp lệ.

---

## Verdicts

| File | Type | Score | Verdict | Notes |
|---|---|---|---|---|
| `wiki/sources/src_claude-best-practices-power-user-guide.md` | Source | 10/10 | **PROMOTE** | Đầy đủ metadata, summary 3 câu mạch lạc, 7 key points chuẩn xác. |
| `wiki/concepts/context-engineering.md` | Concept | 10/10 | **PROMOTE** | Tích hợp nguồn mới nhuần nhuyễn, định nghĩa 2 câu chuẩn, 7 key ideas sâu sắc. |
| `wiki/concepts/context-window-management.md` | Concept | 9/10 | **PROMOTE** | Bổ sung 2 ý thực tiễn (tách session theo chủ đề, handoff doc), 7 key ideas, liên kết hoàn chỉnh. |
| `wiki/concepts/claude-cowork.md` | Concept | 10/10 | **PROMOTE** | Định nghĩa chuẩn xác về môi trường Cowork, 5 key ideas cấu trúc tốt, 3 liên kết hợp lệ. |
| `wiki/concepts/socratic-prompting.md` | Concept | 7/10 | **REVISE** | Khái niệm tốt, định nghĩa chuẩn nhưng `## Key ideas` chỉ có 4 mục (cần ≥5). |
