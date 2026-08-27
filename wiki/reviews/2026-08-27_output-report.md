# Output Validation — 2026-08-27

**Status:** pending
**Issues found:** 2 (0 ERROR, 1 WARNING, 1 INFO)
**Created:** 2026-08-27 19:10:00
**Validator:** output-validator

---

## Scope

- **Files checked:** 733 (185 sources + 548 concepts)
- **New files today:** 9 (1 source + 8 concepts)
  - **Sources (1):**
    - `wiki/sources/src_10-questions-for-your-startup-developers.md`
  - **Concepts (8):**
    - `agent-defense-in-depth.md`
    - `batch-vs-live-inference.md`
    - `cloud-auth-hierarchy.md`
    - `cloud-cost-governance.md`
    - `dynamic-shared-quota.md`
    - `gcp-ai-platform-migration.md`
    - `llm-consumption-modes.md`
    - `secrets-management.md`
- **Existing files:** quick-scan + targeted sweeps (variant-5 manual grep per SKILL mandate)

## Headline

Batch mới **sạch hoàn toàn về typo và link**: cả 5 biến thể typo Compile Agent (ngưởi / double-i / spacing merge / capital-I / dropped-i) đều = 0 instances trên toàn KB, lần thứ NĂM liên tiếp dropped-i variant-5 grep = 0. Không file mới nào có forward-reference wikilink (mọi target trong `## Related concepts` đều đã tồn tại — kiểm tra trực tiếp 10 targets). Không file truncated. Frontmatter `original:` link → `raw/articles/2026-08-26_10-questions-...` tồn tại.

Điểm cần chú ý duy nhất: **3/8 concept mới có Key ideas < 5** (batch-vs-live-inference 4, cloud-cost-governance 3, secrets-management 4) — lần đầu kể từ 08-26 có concept mới nằm trong depth-debt subset. Không phải ERROR (nội dung đủ chất lượng, đúng spec), nhưng lệch chuẩn completeness 5-10 items.

---

## Issue 1: Key ideas < 5 items ở 3 concept mới

**File:** `wiki/concepts/batch-vs-live-inference.md`, `wiki/concepts/cloud-cost-governance.md`, `wiki/concepts/secrets-management.md`
**Severity:** WARNING
**Dimension:** Completeness

Quick-scan flag 3/8 concept mới dưới ngưỡng 5 key ideas:

| File | Key ideas count | Ghi chú |
|---|---|---|
| `batch-vs-live-inference.md` | 4 | 1 bullet mẹ (3 câu hỏi phân loại) + 3 bullet con |
| `cloud-cost-governance.md` | 3 | 1 bullet mẹ (3 lớp spend control, numbered) + 2 bullet |
| `secrets-management.md` | 4 | 1 bullet mẹ (2 kỷ luật, sub-bullets) + 3 bullet |

**Evidence:** đếm top-level `- ` bullets trong `## Key ideas` mỗi file (quick-scan section "Too few key points (<5)").

**Assessment:** Nội dung không sai — các bullet mẹ chứa sub-list chi tiết (3 câu hỏi, 3 lớp spend control, 2 kỷ luật) nên thông tin đầy đủ hơn con số 3-4 gợi ý. Nhưng theo format-spec §2.2 "Key points are 5-10 items", 3 file này lệch chuẩn. Đây là depth-debt baseline đã biết (87 concepts KB-wide), không phải lỗi mới.

**Suggested fix:** Optional — Fix Agent có thể tách sub-bullets thành top-level key ideas (đặc biệt `cloud-cost-governance` 3 lớp spend control xứng đáng là 3 items riêng). Không blocking, không ảnh hưởng tham chiếu.

---

## Issue 2: Section `## Notes` rỗng ở EOF — 8/8 concept mới

**File:** tất cả 8 concepts mới (agent-defense-in-depth, batch-vs-live-inference, cloud-auth-hierarchy, cloud-cost-governance, dynamic-shared-quota, gcp-ai-platform-migration, llm-consumption-modes, secrets-management)
**Severity:** INFO
**Dimension:** Completeness

Cả 8 concept mới đều có `## Notes` ở cuối file nhưng content rỗng (0 dòng sau header).

**Evidence:** mỗi file kết thúc với `## Sources` → 1 bullet → `## Notes` (trống) ở dòng cuối.

**Assessment:** Giống precedent 08-26 (Issue 2) — section `## Notes` là OPTIONAL theo format-spec §2.3, rỗng chỉ là cosmetic, không ảnh hưởng tham chiếu.

**Suggested fix:** Optional — Fix Agent có thể xóa header `## Notes` rỗng ở 8 file (hoặc Julius điền annotation). Không blocking.

---

## Verification

- **Typo detectors (all 5 variants):** 0 instances / 0 files — `ngưởi`, double-i, spacing merge, capital-I, dropped-i grep (3 sub-pattern sub1/sub2/sub3) all clean. Lần thứ 5 liên tiếp dropped-i = 0.
- **Depth-debt baseline:** 3/8 concept mới nằm trong subset key-ideas<5 (Issue 1); 0 file mới bị definition ≤1 câu.
- **Truncated detection:** 0 file truncated (không thiếu `## Related concepts` / `## Sources`).
- **Empty sections:** 8/8 `## Notes` rỗng (Issue 2 — optional section).
- **Wikilinks:** 1 frontmatter `original:` → `raw/articles/` tồn tại; 0 forward-refs (10 targets trong Related concepts đều đã compile).
