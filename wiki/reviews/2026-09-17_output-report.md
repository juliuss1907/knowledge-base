# Output Validation — 2026-09-17

**Status:** pending
**Issues found:** 2 (0 ERROR, 2 WARNING, 0 INFO)
**Files checked:** 784 (201 sources + 583 concepts)
**New files:** 3 (1 source + 2 concepts; `harness-engineering.md` là re-compile mở rộng — file đã tồn tại từ 09-16)
**Created:** 2026-09-17 23:05:00
**Validator:** output-validator

---

## Tóm tắt

Batch 09-17: 1 source + 2 concepts chủ đề behavioral evals / harness engineering (@GoogleCloudTech, 2026-09-16). Nội dung batch sạch — 0 typo variant 1-5 toàn KB, Defect A/B/C pass, 8/8 backlink targets resolve. 1 WARNING nội dung: `harness-engineering.md` thêm source thứ 2 vào frontmatter nhưng không key idea nào phản ánh source đó. 1 WARNING ghi nhận forward-ref đã resolve (không cần action).

## Issue 1: Multi-source concept — source thứ 2 không được phản ánh trong key ideas

**File:** wiki/concepts/harness-engineering.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Frontmatter khai báo 2 sources (thêm `[[src_googletech-behavioral-evals-harness-engineering]]` trong re-compile 09-17) nhưng cả 8 key ideas chỉ phản ánh source gốc `src_harness-engineering-ai-coding` (context engineering, architectural constraints, HARNESS.md, progressive hardening, bounded trust). Không key idea nào từ source mới (behavioral evals, dogfooding trước evals, strict/fuzzy assertions, batch evals) — dù source 2 là bài chuyên sâu về đúng chủ đề này. Lưu ý: body `## Sources` liệt kê đủ 2 nguồn, khớp frontmatter — đây KHÔNG phải Defect A (count gap), mà là gap nội dung aggregation.
**Evidence:** 8/8 key ideas về harness components/verification cấu trúc; 0/8 nhắc behavioral evals, dogfooding, assertions, batch evals
**Suggested fix:** Compile Agent bổ sung 2-3 key ideas từ src_googletech-behavioral-evals-harness-engineering (vd: behavioral evals như lớp verification cấp vi mô bên trong harness; dogfooding trước — evals sau; batch evals thay vì block PR trên single run). Hoặc: nếu ý định chỉ là liên kết chéo, Fix Agent gỡ source 2 khỏi frontmatter + body Sources.

---

## Issue 2: Forward-ref [[agent-harness]] — đã resolve, ghi nhận tránh false positive

**File:** wiki/concepts/harness-engineering.md
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** Related concepts trỏ `[[agent-harness]]`. Check đầy đủ theo quy trình forward-ref: concept tồn tại (`wiki/concepts/agent-harness.md`), raw material tồn tại. Link đã resolve — không phải no-source forward-ref, không cần action. Ghi nhận để format-validator không đưa target vào broken-targets backlog nhầm.
**Evidence:** `ls wiki/concepts/agent-harness.md` = 1 hit; `find raw/ -iname '*agent-harness*'` = 1 hit
**Suggested fix:** Không cần action.

---

## Kiểm tra sạch (điểm đáng chú ý)

- **Typo variants 1-5: 0** toàn KB — quick-scan (ngưởi / double-i / spacing merge / capital-I) + 3 grep thủ công variant 5 (ngườ / thờ-compounds / thay v): 0 matches. Streak 11 runs liên tiếp (08-23 → 09-17).
- **Defect A** (frontmatter vs body sources count): behavioral-evals 1-1 ✓, harness-engineering 2-2 ✓
- **Defect B** (duplicate key ideas): không phát hiện ở cả 2 concepts
- **Defect C** (section-name drift): src_googletech dùng đúng `## Key points` ✓
- **Backlinks:** 8/8 targets resolve — agentic-coding, ai-evals, context-engineering, progressive-hardening, three-enforcement-loops, vibe-coding, agent-harness (concepts); src_harness-engineering-ai-coding (source)
- **Count integrity:** 582 concepts (09-16) + 1 mới (behavioral-evals) = 583 ✓. `harness-engineering.md` có trong git tree hôm qua → re-compile, không phải file mới. 4 commits 24h giờ chỉ delete `.hermes/kanban.db-shm/-wal` (benign) — không có deletion wiki content.
- **Structure:** Definition 2 câu (cả 2 concepts) ✓; source Summary đủ 3-5 câu ✓; Key points source = 7 items ✓; Key ideas concepts = 6-8 items ✓; không file truncated ✓

## Kết luận

Không có ERROR. Batch chất lượng tốt — 1 issue nội dung cần Compile/Fix Agent xử lý (Issue 1), 1 ghi nhận process (Issue 2).
