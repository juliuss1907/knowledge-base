# Output Validation — 2026-05-24

**Status:** pending
**Issues found:** 20
**Created:** 2026-05-24 08:05:00
**Validator:** output-validator

---

## Summary

Validated 17 new/changed files (since 2026-05-22) across 11 concepts + 6 sources, plus quick-scan of 86 older files for systematic issues. Total: 103 files (84 concepts + 19 sources).

**Breakdown:** 1 ERROR · 11 WARNING · 8 INFO

---

## Issue 1: Broken wikilinks — 11 missing concept pages referenced by 7 new files

**File:** Multiple files (see evidence)
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** Seven newly compiled files reference concept pages that do not exist. These wikilinks resolve to nowhere in Obsidian, breaking the knowledge graph.

**Evidence:**
| Missing concept | Referenced by |
|---|---|
| `agent-initiated-code-artifacts.md` | `agent-harness.md`, `src_code-as-agent-harness-arxiv-2605-18747.md` |
| `multi-agent-systems.md` | `agent-harness.md`, `multi-agent-taxonomy.md`, `src_code-as-agent-harness-arxiv-2605-18747.md` |
| `code-for-reasoning.md` | `code-as-substrate.md`, `src_code-as-agent-harness-arxiv-2605-18747.md` |
| `code-for-action.md` | `code-as-substrate.md`, `src_code-as-agent-harness-arxiv-2605-18747.md` |
| `code-for-environment-modeling.md` | `code-as-substrate.md`, `src_code-as-agent-harness-arxiv-2605-18747.md` |
| `orchestrator-worker-validator.md` | `factory-missions.md`, `multi-agent-taxonomy.md`, `validation-contract.md`, `src_luke-alvoeiro-multi-agent-architecture-factory.md` |
| `agent-handoff.md` | `factory-missions.md`, `src_luke-alvoeiro-multi-agent-architecture-factory.md` |
| `harness-control.md` | `plan-execute-verify-loop.md` |
| `program-of-thoughts.md` | `src_code-as-agent-harness-arxiv-2605-18747.md` |
| `supergrok-subscription.md` | `src_hermes-xurl-skill-guide.md` |
| `nous-research.md` | `src_hermes-xurl-skill-guide.md` |

**Suggested fix:** Compile Agent cần tạo concept pages cho 11 khái niệm này, hoặc xóa wikilink nếu concept không đủ quan trọng để có page riêng.

---

## Issue 2: Empty Notes — systematic across all 11 new concepts

**File:** `wiki/concepts/active-thinking.md`, `agent-harness.md`, `code-as-substrate.md`, `cookie-fun-mcp.md`, `evolutionary-mismatch.md`, `factory-missions.md`, `grok-hermes-integration.md`, `multi-agent-taxonomy.md`, `plan-execute-verify-loop.md`, `validation-contract.md`, `x-search-tool.md`
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Tất cả 11 concept file mới có section `## Notes` trống. Đây là systematic issue — 88/84 concept files tồn tại đều có empty Notes.

**Evidence:** Mỗi file kết thúc bằng:
```markdown
## Notes

```
(không có nội dung sau header)

**Suggested fix:** Cân nhắc: (a) Xóa section Notes khỏi template nếu không dùng, hoặc (b) Thêm guidance để Compile Agent điền nội dung (personal reflections, application ideas, caveats). Hiện tại gây noise trong UI.

---

## Issue 3: Summary too short — 6 source files with 2-sentence summaries

**File:** `wiki/sources/src_1-month-with-hermes-ive-been-using-wrong.md`, `src_code-as-agent-harness-arxiv-2605-18747.md`, `src_hermes-xurl-skill-guide.md`, `src_how-ai-productivity-fails.md`, `src_how-some-people-become-unrecognizable.md`, `src_luke-alvoeiro-multi-agent-architecture-factory.md`
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Tất cả 6 source file được compile gần đây có Summary chỉ 2 câu, trong khi spec yêu cầu 3-5 sentences. Các summaries tuy súc tích nhưng thiếu depth.

**Evidence:**
- `src_1-month-with-hermes`: "Sau 1 tháng sử dụng Hermes, tác giả nhận ra đã dùng sai cách... Bài viết chia sẻ cách phân chia vai trò giữa Claude (builder) và Hermes (operator)..." — 2 câu
- `src_how-ai-productivity-fails`: "Hầu hết người dùng AI chỉ tăng năng suất 10-20%... Tác giả cho rằng mức tăng 2x hoặc 10x+ là hoàn toàn có thể đạt được..." — 2 câu

**Suggested fix:** Mở rộng summary lên 3-5 câu: thêm context về methodology, key insight, hoặc practical implication.

---

## Issue 4: Definition quá ngắn — 4 concepts có 1 câu

**File:** `wiki/concepts/code-as-substrate.md`, `cookie-fun-mcp.md`, `grok-hermes-integration.md`, `multi-agent-taxonomy.md`
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Definition section chỉ 1 câu, trong khi spec yêu cầu 2-3 sentences. Thiếu depth để standalone understanding.

**Evidence:**
- `code-as-substrate.md`: "Code như một nền tảng (substrate) cho agent intelligence..." — 1 câu
- `cookie-fun-mcp.md`: "MCP (Model Context Protocol) tool tích hợp với Cookie.fun..." — 1 câu
- `grok-hermes-integration.md`: "Tích hợp giữa Nous Research (Hermes) và xAI..." — 1 câu
- `multi-agent-taxonomy.md`: "Phân loại 5 mô hình giao tiếp cơ bản..." — 1 câu

**Suggested fix:** Mở rộng mỗi definition thêm 1-2 câu giải thích **tại sao** concept này quan trọng và **nó được dùng khi nào**.

---

## Issue 5: Key ideas thấp — 5 concepts có <5 key ideas

**File:** `wiki/concepts/agent-harness.md` (4 ideas), `code-as-substrate.md` (4), `evolutionary-mismatch.md` (4), `plan-execute-verify-loop.md` (4), `validation-contract.md` (4)
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Spec yêu cầu 5-10 key ideas. 5 file có 4 ideas, borderline low — có thể bỏ sót dimensions quan trọng.

**Suggested fix:** Review xem có dimension nào của concept bị bỏ sót không. Ví dụ: `agent-harness.md` có thể thêm "Fault tolerance" hoặc "Observability".

---

## Issue 6: Non-standard frontmatter syntax — sub_tags uses inline array

**File:** `wiki/concepts/cookie-fun-mcp.md`, `grok-hermes-integration.md`, `x-search-tool.md`
**Severity:** INFO
**Dimension:** Completeness
**Issue:** `sub_tags` sử dụng inline array syntax `[tools, defi]` thay vì multi-line list syntax. Cả hai đều là valid YAML, nhưng format-spec khuyến khích consistency.

**Evidence:**
```yaml
sub_tags: [tools, defi]
```
vs standard:
```yaml
sub_tags:
  - tools
  - defi
```

**Suggested fix:** Thống nhất về một syntax. Nếu Format Validator không flag, có thể ignore. Chỉ là cosmetic inconsistency.

---

## Issue 7: Comparison table in concept — mixed format pattern

**File:** `wiki/concepts/cookie-fun-mcp.md`, `grok-hermes-integration.md`
**Severity:** INFO
**Dimension:** Coherence
**Issue:** Hai concept files có sections phụ (## Comparison với x_search, ## Cost Comparison) ngoài các sections chuẩn. Nội dung hữu ích nhưng làm mất consistency với các concept files khác.

**Evidence:**
- `cookie-fun-mcp.md`: Có section `## Comparison với x_search` với bảng so sánh
- `grok-hermes-integration.md`: Có section `## Cost Comparison` với bảng chi phí

**Suggested fix:** Chuyển nội dung vào Key ideas hoặc Notes, hoặc tạo section chuẩn hóa nếu pattern này lặp lại.

---

## Issue 8: Setup code block in concept — domain-specific content

**File:** `wiki/concepts/x-search-tool.md`
**Severity:** INFO
**Dimension:** Coherence
**Issue:** X-search-tool.md có section `## Setup` chứa YAML config block. Đây là content domain-specific, hữu ích nhưng không phù hợp format concept file.

**Evidence:**
```yaml
## Setup

x_search:
  timeout_seconds: 240
  retries: 2
  model: grok-4.3
```

**Suggested fix:** Chuyển config example vào Notes section, hoặc dùng ## Notes để giữ tính nhất quán.

---

## Issue 9: Empty Original excerpts — 3 older source files

**File:** `wiki/sources/src_hermes-200-30-skills-3-worth-it.md`, `src_hermes-analyst-workflow-essentials.md`, `src_hermes-as-a-real-time-analyst.md`
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Ba source file cũ có section `## Original excerpts` trống. Section này tồn tại nhưng không có nội dung — gây confusion.

**Evidence:** Mỗi file có `## Original excerpts` theo sau bởi empty content, không có quotes nào.

**Suggested fix:** Thêm quotes từ nguồn gốc hoặc xóa section nếu không có excerpts phù hợp.

---

## Issue 10: Missing Original excerpts section — 1 older source file

**File:** `wiki/sources/src_aaron-wright-ai-agents-legal-body.md`
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Source file hoàn toàn thiếu section `## Original excerpts`. Đây là required section cho source files.

**Evidence:** File kết thúc sau Concepts referenced section, không có Original excerpts.

**Suggested fix:** Thêm section `## Original excerpts` với ít nhất 1-2 quotes từ nguồn.

---

## Issue 11: Definition reads as description, not definition — 1 concept

**File:** `wiki/concepts/evolutionary-mismatch.md`
**Severity:** INFO
**Dimension:** Coherence
**Issue:** Definition dài 4 câu, trong đó câu cuối ("Không phải vì cuộc sống hiện đại 'khó hơn', mà vì nó cắt đứt...") là elaboration hơn là definition. Definition nên gọn trong 2-3 câu core meaning.

**Evidence:**
> "Evolutionary mismatch (lệch lạc tiến hóa) là hiện tượng môi trường sống hiện đại khác biệt đáng kể so với môi trường mà con người đã tiến hóa qua hàng triệu năm, dẫn đến các vấn đề sức khỏe thể chất và tinh thần. Không phải vì cuộc sống hiện đại 'khó hơn', mà vì nó cắt đứt chúng ta khỏi cách chúng ta từng cảm nhận bản thân, nhau và thế giới."

**Suggested fix:** Chuyển câu thứ hai vào Key ideas, giữ Definition gọn trong 2 câu.

---

## Issue 12: English title in Vietnamese concept file

**File:** `wiki/concepts/evolutionary-mismatch.md`
**Severity:** INFO
**Dimension:** Vietnamese
**Issue:** Title `# Evolutionary mismatch` bằng tiếng Anh, trong khi toàn bộ nội dung bằng tiếng Việt. Nên thống nhất: hoặc tiêu đề tiếng Việt, hoặc cả file tiếng Anh.

**Evidence:** Definition bắt đầu bằng "Evolutionary mismatch (lệch lạc tiến hóa) là..." — cho thấy đây là concept được dịch sang tiếng Việt.

**Suggested fix:** Đổi title thành `# Evolutionary Mismatch (Lệch lạc tiến hóa)` hoặc `# Lệch lạc tiến hóa`.

---

## Issue 13: Hard-coded numbers without source verification — 1 concept

**File:** `wiki/concepts/evolutionary-mismatch.md`
**Severity:** INFO
**Dimension:** Factual Accuracy
**Issue:** Key ideas chứa nhiều số liệu cụ thể (~300,000 năm hunter-gatherer, 12,000 năm nông nghiệp, 6-7 vs 8-9 tiếng ngủ, 25-50 người/băng nhóm, 7% vs 100% thời gian ngoài trời, 6-10 dặm/ngày) nhưng không có citation inline.

**Evidence:**
> "Con người tiến hóa trong môi trường hunter-gatherer qua ~300,000 năm; chỉ 12,000 năm nay mới có nông nghiệp..."

**Suggested fix:** Thêm footnote hoặc citation cho các số liệu này, hoặc thêm confidence qualifier.

---

## Issue 14: Cost claims without verification date — 2 concepts

**File:** `wiki/concepts/grok-hermes-integration.md`, `x-search-tool.md`
**Severity:** INFO
**Dimension:** Factual Accuracy
**Issue:** Claims về giá ($0.5/ngày X API, $0.1/ngày x_search, $30/3 tháng Grok subscription) là time-sensitive pricing information, có thể đã thay đổi.

**Evidence:**
- `grok-hermes-integration.md`: "Từ X API ($0.5/ngày) xuống x_search ($0.1/ngày)", "Grok subscription hack: $30/3 tháng"
- `x-search-tool.md`: "~$0.1/ngày vs $0.5/ngày"

**Suggested fix:** Thêm qualifier "tại thời điểm viết (2026-05)" hoặc chuyển vào Notes để dễ update.

---

## Issue 15: Vietnamese-English code switching — inconsistent

**File:** `wiki/concepts/cookie-fun-mcp.md`
**Severity:** INFO
**Dimension:** Vietnamese
**Issue:** File mixes English terminology with Vietnamese descriptions inconsistently. Section title "## Comparison với x_search" dùng cả hai ngôn ngữ.

**Evidence:** Title "Comparison với x_search", nội dung bảng so sánh dùng English headers (Mạnh, Yếu) nhưng row content là English.

**Suggested fix:** Thống nhất: hoặc toàn bộ tiếng Việt, hoặc section titles bằng tiếng Việt với English terms trong ngoặc đơn.

---

## Issue 16: Source with truncated content — 1 file

**File:** `wiki/sources/src_how-some-people-become-unrecognizable.md`
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Key points section appears truncated — kết thúc với "Lea..." (incomplete word). Possible data loss during compilation.

**Evidence:** Line cuối của key points: "90-day sanity check... Lea..." (bị cắt)

**Suggested fix:** Re-compile từ source để khôi phục nội dung đầy đủ.

---

## Issue 17: Sources field inconsistent wikilink format — 1 concept

**File:** `wiki/concepts/evolutionary-mismatch.md`
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Frontmatter `sources` field dùng string thay vì array: `sources: "[[src_were-not-supposed-to-live-like-this.md]]"` — các file khác dùng list format.

**Evidence:**
```yaml
sources: "[[src_were-not-supposed-to-live-like-this.md]]"
```

**Suggested fix:** Chuyển thành:
```yaml
sources:
  - [[wiki/sources/src_were-not-supposed-to-live-like-this.md]]
```

---

## Issue 18: topic field shared across unrelated concepts — 3 concepts

**File:** `wiki/concepts/agent-harness.md`, `code-as-substrate.md`, `plan-execute-verify-loop.md`
**Severity:** INFO
**Dimension:** Coherence
**Issue:** Ba concept files đều có `topic: code-as-agent-harness`. Trong khi đây là cùng một cluster (từ cùng paper), mỗi concept có thể cần topic riêng để Obsidian navigation tốt hơn.

**Evidence:** Cả 3 file share topic `code-as-agent-harness` và source `src_code-as-agent-harness-arxiv-2605-18747.md`.

**Suggested fix:** Cân nhắc giữ shared topic nếu chúng luôn được browse cùng nhau, hoặc tách riêng nếu mỗi concept develop independently.

---

## Issue 19: Source original field uses wikilink not file path

**File:** `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md`, `src_luke-alvoeiro-multi-agent-architecture-factory.md`
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Frontmatter `original` field sử dụng wikilink `[[2026-05-22_...]]` thay vì path `raw/papers/2026-05-22_...`. Các source files khác dùng `raw/<type>/...`.

**Evidence:**
```yaml
original: [[2026-05-22_code-as-agent-harness-arxiv-2605-18747.md]]
```
vs standard:
```yaml
original: raw/articles/2026-05-18_1-month-with-hermes-ive-been-using-wrong.md
```

**Suggested fix:** Đổi thành absolute raw path để nhất quán với các source files khác.

---

## Issue 20: Date discrepancy — last_updated older than file timestamp

**File:** `wiki/concepts/active-thinking.md`
**Severity:** INFO
**Dimension:** Factual Accuracy
**Issue:** `last_updated: 2026-05-13` nhưng file được tạo/modified ngày 2026-05-24 (hôm nay). Timestamp không khớp.

**Evidence:** Frontmatter: `last_updated: 2026-05-13` vs filesystem: `2026-05-24T07:53:17`

**Suggested fix:** Cập nhật `last_updated` thành `2026-05-24`.

---

## Summary

| Severity | Count | Category |
|---|---|---|
| **ERROR** | 1 | Broken wikilinks (11 missing concepts) |
| **WARNING** | 11 | Empty Notes ×11, short summaries ×6, short definitions ×4, empty excerpts ×3, missing excerpts ×1, truncated content ×1, string sources field ×1, wikilink original field ×2 |
| **INFO** | 8 | Low key ideas ×5, syntax inconsistency ×2, mixed format ×3, title language ×1, unverified data ×1, stale pricing ×1, code switching ×1, shared topic ×1, date discrepancy ×1 |

---

## Systematic issues detected

**[SYSTEMATIC ISSUE]**
**Pattern:** 88/84 concept files have empty `## Notes` sections — essentially every concept file.
**Likely cause:** Compile Agent template includes Notes section by default but never populates it.
**Recommendation:** Either (a) remove Notes from template, or (b) add Compile Agent guidance to fill Notes with personal reflections, application notes, or caveats.

**[SYSTEMATIC ISSUE]**
**Pattern:** All 6 new source files have 2-sentence summaries (below 3-5 sentence requirement).
**Likely cause:** Compile Agent produces concise summaries but doesn't hit the length target.
**Recommendation:** Adjust compile-agent/SKILL.md to require minimum 3 sentences in Summary.
