# Output Validation — 2026-08-31

**Status:** approved
**Issues found:** 6 (0 ERROR, 3 WARNING, 3 INFO)
**Created:** 2026-08-31 23:04:00
**Validator:** output-validator

---

## Summary

- **Files checked:** 763 (195 sources + 568 concepts)
- **New files:** 22 (8 sources + 14 concepts)
- **Batch origin:** 3 clusters từ batch 2026-08-30 Ingest — `ai-engineering-skills` (2 Andrew Ng articles + 1 concept tổng hợp), `frontend-dev-tools` (Archify, Impeccable, ThreeUI + 6 concepts), `self-driving-products` (PostHog + 2 concepts), `ai-security` (Anthropic Cybersecurity Skills + 2 concepts), `context-database` (OpenViking + 2 concepts)

### New files validated (22)

| File | Type | Definition | Key ideas | Verdict |
|---|---|---|---|---|
| src_ai-engineering-skills-map-building-deploying-ai-applications | source | — | 7 | ✅ PASS |
| src_ai-engineering-skills-map-software-engineering-fundamentals | source | — | 10 | ✅ PASS |
| src_archify | source | — | 11 | ✅ PASS |
| src_impeccable | source | — | 10 | ⚠️ WARNING (section name) |
| src_anthropic-cybersecurity-skills | source | — | 10 | ✅ PASS |
| src_posthog | source | — | 10 | ✅ PASS |
| src_threeui | source | — | 9 | ✅ PASS |
| src_openviking | source | — | 10 | ✅ PASS |
| ai-engineering-skills | concept | 2 câu | 16 | ⚠️ WARNING (2 issues) |
| architecture-as-code | concept | 2 câu | 7 | ✅ PASS |
| context-database | concept | 3 câu | 8 | ✅ PASS |
| code-visualization | concept | 2 câu | 6 | ℹ️ INFO (typo) |
| ai-observability | concept | 2 câu | 5 | ✅ PASS |
| ai-security-tools | concept | 2 câu | 6 | ✅ PASS |
| ai-frontend-design-guidance | concept | 2 câu | 7 | ✅ PASS |
| cybersecurity-skills-library | concept | 2 câu | 8 | ✅ PASS |
| design-systems | concept | 2 câu | 6 | ✅ PASS |
| frontend-design-agent | concept | 2 câu | 6 | ✅ PASS |
| product-analytics | concept | 2 câu | 6 | ✅ PASS |
| progressive-disclosure | concept | 2 câu | 5 | ✅ PASS |
| self-driving-products | concept | 2 câu | 5 | ✅ PASS |
| ui-component-library | concept | 2 câu | 7 | ✅ PASS |

### Mechanical checks — all clean

- Cả 5 biến thể typo Compile Agent: 0 instances (ngưởi / double-i / spacing-merge / capital-I / dropped-i)
- **Dropped-i variant-5 grep (bắt buộc):** 0 matches — **lần thứ 9 liên tiếp sạch** (08-23 → 08-31). Đã vượt ngưỡng 1 tuần (đạt 08-30). Đề xuất hạ tần suất xuống hàng tuần.
- 0 truncated files; frontmatter `original:` → raw/ đều tồn tại (8/8)
- 0 empty Key ideas/sources; 0 draft concepts mới
- Mọi concept mới đều definition 2-3 câu + 5-16 key ideas

---

## Issue 1: Sources section thiếu 2 backlinks tới sources trong frontmatter

**File:** wiki/concepts/ai-engineering-skills.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Frontmatter `sources:` khai 4 nguồn, nhưng section `## Sources` chỉ liệt kê 2. Thiếu `[[src_ai-engineering-skills-map-software-engineering-fundamentals]]` và `[[src_ai-engineering-skills-map-building-deploying-ai-applications]]` — 2 source được compile cùng batch hôm nay.
**Evidence:** Frontmatter dòng 8-11: `- "[[src_ai-engineering-skills-map-software-engineering-fundamentals]]"` và `- "[[src_ai-engineering-skills-map-building-deploying-ai-applications]]"`. Sources body dòng 52-53 chỉ có `[[src_ai-engineering-skills-map]]` và `[[src_ai-skills-map-building-deploying-ai-apps]]`.
**Suggested fix:** Thêm 2 dòng vào `## Sources` body:
- `- [[src_ai-engineering-skills-map-software-engineering-fundamentals]] — Andrew Ng, The Batch 2026-08-30 (part 3: software engineering fundamentals)`
- `- [[src_ai-engineering-skills-map-building-deploying-ai-applications]] — Andrew Ng, The Batch 2026-08-30 (part 2: building and deploying AI applications)`

---

## Issue 2: Key idea bị trùng lặp

**File:** wiki/concepts/ai-engineering-skills.md
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** Cùng ý "vibe coding thiếu fundamentals → bad tradeoffs" xuất hiện 2 lần với wording khác nhau — một lần ở dòng 26 (trong cụm 4 kỹ năng) và một lần riêng ở dòng 39 (trong phần software engineering fundamentals). Do concept tổng hợp từ 4 nguồn, Compile Agent chưa dedup.
**Evidence:** Dòng 26: `- **Vibe coding thiếu fundamentals = poor tradeoffs:** developer không biết tradeoff nào tồn tại sẽ không biết cung cấp context gì cho coding agent → agent ra quyết định kém; fundamentals cho phép steer agent bằng "precise language of software engineering"`. Dòng 39: `- **Vibe coding thiếu fundamentals = bad tradeoffs:** developer không biết tradeoff nào tồn tại (latency, availability, consistency, reliability, maintainability, simplicity, cost) thì không steer được agent`.
**Suggested fix:** Xóa một trong 2 bản (giữ bản ở dòng 39 vì liệt kê cụ thể các tradeoffs).

---

## Issue 3: Section naming deviation — `## Key ideas` thay vì `## Key points`

**File:** wiki/sources/src_impeccable.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Format-spec §3.3 yêu cầu `## Key points` cho source files. File này dùng `## Key ideas` (dòng 26). Format Validator sẽ báo missing section.
**Evidence:** Dòng 26: `## Key ideas`. 9 source còn lại trong batch đều dùng `## Key points`.
**Suggested fix:** Đổi `## Key ideas` → `## Key points`.

---

## Issue 4: Section `## Notes` rỗng ở EOF — systemic

**File:** 14/14 concept files mới
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Toàn bộ 14 concept files trong batch có header `## Notes` cuối file không có nội dung. Cosmetic — section optional theo format-spec, không blocking. Nhưng tần suất 14/14 cho thấy Compile Agent đang thêm Notes header mặc định.
**Affected files:**
- ai-engineering-skills.md, ai-frontend-design-guidance.md, ai-observability.md, ai-security-tools.md, architecture-as-code.md, code-visualization.md, context-database.md, cybersecurity-skills-library.md, design-systems.md, frontend-design-agent.md, product-analytics.md, progressive-disclosure.md, self-driving-products.md, ui-component-library.md
**Evidence:** Mỗi file kết thúc với `## Notes` và dòng trống, không có nội dung.
**Suggested fix:** Xóa 14 header `## Notes` rỗng. Precedent: Fix Agent đã xóa Notes rỗng ở các batch 08-26/08-27/08-29.

---

## Issue 5: Forward-reference wikilinks

**File:** 4 concept files
**Severity:** INFO
**Dimension:** Completeness
**Issue:** 4 wikilinks trong Related concepts trỏ tới concepts chưa tồn tại. Forward-references — sẽ resolve tự nhiên khi Compile Agent xử lý thêm raw files.
**Affected targets (3 unique):**
- `[[architecture-diagram]]` — trong architecture-as-code.md, code-visualization.md
- `[[diagram-as-code]]` — trong architecture-as-code.md, code-visualization.md
- `[[ai-assisted-development]]` — trong ai-frontend-design-guidance.md, frontend-design-agent.md
**Evidence:** grep trên wiki/concepts + wiki/sources cho 3 target = 0 file.
**Suggested fix:** Không cần Fix Agent action. Forward-references resolve tự nhiên.

---

## Issue 6: Khoảng trắng trước dấu hai chấm

**File:** wiki/concepts/code-visualization.md
**Severity:** INFO
**Dimension:** Vietnamese
**Issue:** Dòng 23 có khoảng trắng thừa trước dấu hai chấm: `- **Interactive** :` thay vì `- **Interactive:**`.
**Evidence:** Dòng 23: `- **Interactive** : Focus với \`/\`, trace route...`
**Suggested fix:** Xóa khoảng trắng: `- **Interactive:** Focus với \`/\`, trace route...`

---

## Escalation

Không có `[SYSTEMATIC ISSUE]`. Batch này sạch về typo (lần thứ 9 liên tiếp), frontmatter, truncated files. 3 WARNING là lỗi riêng lẻ:

1. **ai-engineering-skills.md** thiếu 2 source backlinks — variant của pattern 08-29 (concept dùng nhiều sources bị compile-agent bỏ sót backlink khi sources mới được compile cùng batch). Lần thứ 2 liên tiếp, cần theo dõi nếu lặp lại.
2. **ai-engineering-skills.md** duplicated key idea — do concept tổng hợp từ 4 nguồn, not systemic.
3. **src_impeccable.md** section naming — likely copy-paste từ concept template (concepts dùng `Key ideas`, sources dùng `Key points`).

14/14 empty Notes là systemic pattern nhưng đã biết (precedent 08-26/08-27/08-29) — không cần escalation mới.

**Dropped-i variant-5 clean streak: 9 lần liên tiếp (08-23 → 08-31).** Ngưỡng 1 tuần đã đạt từ 08-30. Đề xuất hạ tần suất grep bắt buộc từ daily xuống weekly.