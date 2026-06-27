# Hygiene Inspection — 2026-06-26

**Status:** pending
**Issues found:** 39 (9 ERROR, 11 WARNING, 19 INFO)
**Created:** 2026-06-26 23:30:59 +07
**Validator:** hygiene-inspector

**Paths checked:** 920

> **Scope note:** Full-tree scan từ `/home/julius/knowledge-base`, bỏ qua deep internals của `.git/`, `.obsidian/`, `node_modules/`, và agent-home internals ở depth > 1 theo skill rules.
> **Report cap:** Daily run chỉ liệt kê 20 issues ưu tiên cao nhất. 19 INFO còn lại chủ yếu là review reports cũ >30 ngày cần archive.

---

## Delta vs most recent approved hygiene report

Reference baseline: approved Hygiene Inspector run dated `2026-06-26 07:01 +07`.

| Metric | Current run | Previous approved | Delta |
|---|---:|---:|---:|
| Paths checked | 920 | 30 | +890 |
| Total findings | 39 | 1 actionable + 1 excluded | broader scope |
| ERROR | 9 | 1 | +8 |
| WARNING | 11 | 0 | +11 |
| INFO | 19 | 0 | +19 |

**Positive delta:** `wiki/reviews/HEARTBEAT.md` không còn hiện diện. Issue đó đã được resolve.

**Newly surfaced in full-tree scan:**
1. Root drift: `memory/` và `state/` không nằm trong root whitelist.
2. Spec drift: `wiki/reviews/_approval-log.md` đang được workflow sử dụng nhưng không có trong `folder-structure.md`.
3. Naming drift: 4 files trong `raw/papers/` không theo pattern `YYYY-MM-DD_<author>_<title>.md`.
4. Draft-zone drift: 2 subfolders backup trong `wiki/drafts/` + 10 `.bak` temp files.
5. Backlog cleanup: 19 old review reports >30 ngày chưa archive.

---

## Issue 1: Root folder `memory/` not in whitelist

**Path:** `memory/`
**Severity:** ERROR
**Category:** Path
**Issue:** Root-level folder này không được whitelist trong `wiki/meta/folder-structure.md`.
**Current:** `memory/` chứa các file markdown như `2026-06-24.md`, `2026-06-25-1626.md`, `2026-06-26-format-fixes.md`
**Expected:** Root chỉ cho phép `.git`, `.obsidian`, `.openclaw`, `.hermes`, `context/`, `raw/`, `wiki/`, `scripts/` và các file root đã liệt kê trong spec
**Suggested fix:** Remove `memory/` khỏi root hoặc update `folder-structure.md` nếu đây là cấu trúc mới được Julius phê duyệt

---

## Issue 2: Paper filename missing author/title split

**Path:** `raw/papers/2026-05-22_code-as-agent-harness-arxiv-2605-18747.md`
**Severity:** ERROR
**Category:** Naming
**Issue:** File paper không theo pattern `YYYY-MM-DD_<author>_<title>.md`.
**Current:** `2026-05-22_code-as-agent-harness-arxiv-2605-18747.md`
**Expected:** `YYYY-MM-DD_<author>_<title>.md`
**Suggested fix:** Rename file để tách rõ author và title theo spec

---

## Issue 3: Paper filename missing author/title split

**Path:** `raw/papers/2026-05-27_llm-need-sleep-consolidation.md`
**Severity:** ERROR
**Category:** Naming
**Issue:** File paper không theo pattern `YYYY-MM-DD_<author>_<title>.md`.
**Current:** `2026-05-27_llm-need-sleep-consolidation.md`
**Expected:** `YYYY-MM-DD_<author>_<title>.md`
**Suggested fix:** Rename file để tách rõ author và title theo spec

---

## Issue 4: Paper filename missing author/title split

**Path:** `raw/papers/2026-05-28_petrodollar-system-analysis.md`
**Severity:** ERROR
**Category:** Naming
**Issue:** File paper không theo pattern `YYYY-MM-DD_<author>_<title>.md`.
**Current:** `2026-05-28_petrodollar-system-analysis.md`
**Expected:** `YYYY-MM-DD_<author>_<title>.md`
**Suggested fix:** Rename file để tách rõ author và title theo spec

---

## Issue 5: Paper filename missing author/title split

**Path:** `raw/papers/2026-06-04_thermodynamics.md`
**Severity:** ERROR
**Category:** Naming
**Issue:** File paper không theo pattern `YYYY-MM-DD_<author>_<title>.md`.
**Current:** `2026-06-04_thermodynamics.md`
**Expected:** `YYYY-MM-DD_<author>_<title>.md`
**Suggested fix:** Rename file để tách rõ author và title theo spec

---

## Issue 6: Root folder `state/` not in whitelist

**Path:** `state/`
**Severity:** ERROR
**Category:** Path
**Issue:** Root-level folder này không được whitelist trong `wiki/meta/folder-structure.md`.
**Current:** `state/` tồn tại ở repo root
**Expected:** Root chỉ cho phép các path đã được whitelist trong spec
**Suggested fix:** Remove `state/` khỏi root hoặc update `folder-structure.md` nếu đây là cấu trúc runtime mới được Julius phê duyệt

---

## Issue 7: Backup subfolder inside `wiki/drafts/`

**Path:** `wiki/drafts/memory-backup-2026-06-15/`
**Severity:** ERROR
**Category:** Path
**Issue:** `wiki/drafts/` phải flat. Subfolder không được phép tồn tại ở zone này.
**Current:** `wiki/drafts/memory-backup-2026-06-15/`
**Expected:** `wiki/drafts/` chỉ chứa draft markdown files trực tiếp, không có subfolders
**Suggested fix:** Remove/move backup folder này hoặc update spec nếu đây là structure được chấp thuận

---

## Issue 8: Backup subfolder inside `wiki/drafts/`

**Path:** `wiki/drafts/search-backup-2026-06-15/`
**Severity:** ERROR
**Category:** Path
**Issue:** `wiki/drafts/` phải flat. Subfolder không được phép tồn tại ở zone này.
**Current:** `wiki/drafts/search-backup-2026-06-15/`
**Expected:** `wiki/drafts/` chỉ chứa draft markdown files trực tiếp, không có subfolders
**Suggested fix:** Remove/move backup folder này hoặc update spec nếu đây là structure được chấp thuận

---

## Issue 9: Workflow file not whitelisted in review zone

**Path:** `wiki/reviews/_approval-log.md`
**Severity:** ERROR
**Category:** Path
**Issue:** File này đang tồn tại và được workflow sử dụng, nhưng `folder-structure.md` không whitelist nó trong `wiki/reviews/`.
**Current:** `_approval-log.md`
**Expected:** Theo spec hiện tại, `wiki/reviews/` chỉ cho phép `_action-required.md`, `YYYY-MM-DD_<type>-report.md`, và `archive/`
**Suggested fix:** Một trong hai phải đúng: whitelist `_approval-log.md` trong `folder-structure.md`, hoặc di chuyển workflow này ra khỏi `wiki/reviews/`

---

## Issue 10: Placeholder file in drafts zone

**Path:** `wiki/drafts/.gitkeep`
**Severity:** WARNING
**Category:** Orphan
**Issue:** Placeholder file đang nằm trong zone vốn đã có draft files thật. Nó không thuộc output structure chuẩn.
**Current:** `.gitkeep`
**Expected:** `wiki/drafts/` chỉ chứa actual draft markdown files
**Suggested fix:** Remove `.gitkeep`

---

## Issue 11: Temporary backup file detected

**Path:** `wiki/drafts/ai-coach-prompting.md.bak`
**Severity:** WARNING
**Category:** Orphan
**Issue:** Temporary/backup file bị bỏ lại trong drafts zone.
**Current:** `wiki/drafts/ai-coach-prompting.md.bak`
**Expected:** Temporary files không nên tồn tại trong KB
**Suggested fix:** Delete backup file

---

## Issue 12: Temporary backup file detected

**Path:** `wiki/drafts/content-generation-workflow.md.bak`
**Severity:** WARNING
**Category:** Orphan
**Issue:** Temporary/backup file bị bỏ lại trong drafts zone.
**Current:** `wiki/drafts/content-generation-workflow.md.bak`
**Expected:** Temporary files không nên tồn tại trong KB
**Suggested fix:** Delete backup file

---

## Issue 13: Temporary backup file detected

**Path:** `wiki/drafts/dollar-as-rent-payment.md.bak`
**Severity:** WARNING
**Category:** Orphan
**Issue:** Temporary/backup file bị bỏ lại trong drafts zone.
**Current:** `wiki/drafts/dollar-as-rent-payment.md.bak`
**Expected:** Temporary files không nên tồn tại trong KB
**Suggested fix:** Delete backup file

---

## Issue 14: Temporary backup file detected

**Path:** `wiki/drafts/existential-vacuum.md.bak`
**Severity:** WARNING
**Category:** Orphan
**Issue:** Temporary/backup file bị bỏ lại trong drafts zone.
**Current:** `wiki/drafts/existential-vacuum.md.bak`
**Expected:** Temporary files không nên tồn tại trong KB
**Suggested fix:** Delete backup file

---

## Issue 15: Temporary backup file detected

**Path:** `wiki/drafts/expert-knowledge-extraction.md.bak`
**Severity:** WARNING
**Category:** Orphan
**Issue:** Temporary/backup file bị bỏ lại trong drafts zone.
**Current:** `wiki/drafts/expert-knowledge-extraction.md.bak`
**Expected:** Temporary files không nên tồn tại trong KB
**Suggested fix:** Delete backup file

---

## Issue 16: Temporary backup file detected

**Path:** `wiki/drafts/src_dan-koe-workflow-analysis-markus.md.bak`
**Severity:** WARNING
**Category:** Orphan
**Issue:** Temporary/backup file bị bỏ lại trong drafts zone.
**Current:** `wiki/drafts/src_dan-koe-workflow-analysis-markus.md.bak`
**Expected:** Temporary files không nên tồn tại trong KB
**Suggested fix:** Delete backup file

---

## Issue 17: Temporary backup file detected

**Path:** `wiki/drafts/src_map-is-not-territory.md.bak`
**Severity:** WARNING
**Category:** Orphan
**Issue:** Temporary/backup file bị bỏ lại trong drafts zone.
**Current:** `wiki/drafts/src_map-is-not-territory.md.bak`
**Expected:** Temporary files không nên tồn tại trong KB
**Suggested fix:** Delete backup file

---

## Issue 18: Temporary backup file detected

**Path:** `wiki/drafts/src_petrodollar-system-analysis.md.bak`
**Severity:** WARNING
**Category:** Orphan
**Issue:** Temporary/backup file bị bỏ lại trong drafts zone.
**Current:** `wiki/drafts/src_petrodollar-system-analysis.md.bak`
**Expected:** Temporary files không nên tồn tại trong KB
**Suggested fix:** Delete backup file

---

## Issue 19: Temporary backup file detected

**Path:** `wiki/drafts/trading-addiction-cycle.md.bak`
**Severity:** WARNING
**Category:** Orphan
**Issue:** Temporary/backup file bị bỏ lại trong drafts zone.
**Current:** `wiki/drafts/trading-addiction-cycle.md.bak`
**Expected:** Temporary files không nên tồn tại trong KB
**Suggested fix:** Delete backup file

---

## Issue 20: Temporary backup file detected

**Path:** `wiki/drafts/x-search-tool.md.bak`
**Severity:** WARNING
**Category:** Orphan
**Issue:** Temporary/backup file bị bỏ lại trong drafts zone.
**Current:** `wiki/drafts/x-search-tool.md.bak`
**Expected:** Temporary files không nên tồn tại trong KB
**Suggested fix:** Delete backup file

---

## Additional findings not expanded due daily cap

19 INFO findings không được liệt kê chi tiết trong report này. Chúng chủ yếu là old review reports >30 ngày trong `wiki/reviews/` cần archive theo spec. Không có ERROR nào bị ẩn ngoài 20 issues đã liệt kê.

---

## Escalations

### [SPEC CONFLICT]
`wiki/reviews/_approval-log.md` đang là file workflow thật. `folder-structure.md` hiện không whitelist file này. Một trong hai đang sai. Cần chỉnh spec hoặc workflow.

### [SYSTEMATIC VIOLATION]
10 temporary backup files (`*.bak`) đang nằm trong `wiki/drafts/`. Đây không phải individual mistake. Đây là cleanup/process issue.

---

## Summary

| Category | Count |
|---|---:|
| ERROR | 9 |
| WARNING | 11 |
| INFO | 19 |
| Paths checked | 920 |

## Verdict

**REVISE** — Structure hiện không clean. Root whitelist drift, review-zone spec drift, raw paper naming drift, và draft-zone backup artifacts đều cần xử lý.

## Verification

```bash
test -f "wiki/reviews/2026-06-26_hygiene-report.md" && echo "✅ Report written"
```