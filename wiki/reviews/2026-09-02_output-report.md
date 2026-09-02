# Output Validation — 2026-09-02

**Status:** pending
**Issues found:** 1 (0 ERROR, 1 WARNING, 0 INFO)
**Created:** 2026-09-02 23:09:11
**Validator:** output-validator

---

## Issue 1: Missing backlink target `[[prompt-injection]]`

**File:** wiki/concepts/agent-sandbox-runtimes.md (dòng 34) + wiki/concepts/network-egress-default-deny.md (dòng 31)
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Hai concept mới trong batch 09-02 link đến `[[prompt-injection]]` trong section Related concepts, nhưng target không tồn tại — không có `wiki/concepts/prompt-injection.md`, không có `wiki/sources/src_prompt-injection.md`, và không có raw material trong `raw/` (0 file chứa prompt-injection). Khác với các forward-refs thông thường (target concept chưa compile nhưng đã có source pending trong raw/ → resolve tự nhiên), target này không có nguồn nào để Compile Agent xử lý.
**Evidence:**
- `agent-sandbox-runtimes.md` dòng 34: `- [[prompt-injection]] — attack vector that bypasses hypervisor`
- `network-egress-default-deny.md` dòng 31: `- [[prompt-injection]] — attack vector that exploits unrestricted egress`
- `find wiki/ -iname '*prompt-injection*'` → 0 kết quả (chỉ 2 file reference ở trên)
**Suggested fix:** Đây là forward-reference hợp lệ về nội dung (prompt injection chính là attack vector được thảo luận trong source Google Cloud), nhưng vì không có raw source, link sẽ không tự resolve. Khi có source về prompt injection (vd. raw post/article) được ingest + compile thành concept `prompt-injection`, link sẽ tự lành — không cần Fix Agent action ngay. Nếu không có kế hoạch compile concept này, có thể bỏ 2 link khỏi Related concepts. Format Validator sẽ track target này trong broken-targets backlog.

---

## Summary

- **Files checked:** 767 (196 sources + 571 concepts)
- **New files:** 5 (1 source + 4 concepts) — cluster Google Cloud agent sandbox runtimes
- **New sources:** `src_google-cloud-agent-sandbox-runtimes.md` (x.com GoogleCloudTech, 2026-09-01)
- **New concepts:** `agent-sandbox-runtimes`, `isolation-spectrum`, `sandbox-state-forking`, `network-egress-default-deny`
- **PROMOTE:** 4/4 concepts + 1/1 source (5/5 files pass all 4 dimensions)
- **Batch quality:** cao — mọi concept definition 2 câu, key ideas 5-6 items, backlink frontmatter ↔ body Sources khớp 1:1 (single-source, không dính Defect A/B multi-source), source dùng đúng `## Key points`, không truncation, không empty sections, không `## Notes` rỗng ở EOF, `original:` → `raw/posts/2026-09-01_google-cloud-agent-sandbox-runtimes.md` tồn tại (verified)

## Typo sweep

- `ngưởi`: 0 | double-i `ngườii`: 0 | spacing merge: 0 | capital-I: 0 | **dropped-i variant 5: 0** (lần thứ **11 liên tiếp** sạch, 08-23 → 09-02, cả 3 sub-patterns)
- 1-sentence definitions: 112 (depth-debt baseline legacy, không có file mới trong danh sách — 0/4 concept mới bị)
- Too-few-key-points: 84 baseline legacy, không có file mới nào trong danh sách

## Verdicts

| File | Verdict |
|---|---|
| src_google-cloud-agent-sandbox-runtimes.md | PROMOTE |
| agent-sandbox-runtimes.md | PROMOTE (1 WARNING backlink shared) |
| isolation-spectrum.md | PROMOTE |
| sandbox-state-forking.md | PROMOTE |
| network-egress-default-deny.md | PROMOTE (1 WARNING backlink shared) |

## Carry-over inventory

- Depth-debt baseline: 112 defs ≤1 câu + 84 key ideas <5 (legacy, không tăng trong batch này)
- Dropped-i variant 5: **11 consecutive clean runs** (08-23 → 09-02). Demotion to weekly recommended lần thứ 4 (08-30/08-31/09-01/09-02). Chưa được Julius/Connor xác nhận — giữ daily grep.
