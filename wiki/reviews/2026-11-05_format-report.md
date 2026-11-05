# Format Validation — 2026-11-05

**Status:** pending
**Issues found:** 396
**Created:** 2026-11-05 23:16:00 +0700
**Validator:** format-validator
**Files checked:** 1167 (634 concepts + 224 sources + 34 indexes + 275 topics)
**ERRORs**: 2
**WARNINGS**: 394
**INFOS:** 0
**Total issues**: 396
Files checked: 1167
Total issues: 396

Δ from 2026-11-04 23:16:00 run (pending — prior run): **0 net change, biến thể exact-zero-flat no-compilation-happened (chu kỳ 24h, 11-04 → 11-05).** 1167→1167 files (**+0**), tổng issues giữ nguyên 396 (**0 net change: 2E+394W+0I**). 2 ERROR phân loại tag Pool A trong `sub_tags` tại 2 file biên soạn ngày 11-02 (`socratic-prompting.md`, `src_claude-best-practices-power-user-guide.md`) tiếp tục tồn tại (chờ Fix Agent xử lý sau khi Julius đã duyệt batch 11-02 ngày 11-03). WARNING giữ nguyên ở mức 394 (**375 cá nhân + 19 forward-reference groups = 394**). Unique targets **267 flat** (ngày thứ 28 liên tiếp tại 267: 10-04, 10-10 → 11-05). Top-20 targets giữ nguyên toàn bộ slug và count (hạng 19-20 đồng hạng 3 ref). **Tầng wiki:** 0 file mới được biên soạn trong 24h qua (Kara nghỉ, Output Validator 23:05 chạy silent). **Tầng raw:** 0 unprocessed backlog (`grep -rn 'status: unprocessed' raw/` rỗng). **Tầng index:** Index Agent rebuild lúc 21:03 hôm nay (commit `53ac8bc4`, 300 file: 25 tag + 275 topic, 0 topic mới). **Git & backup:** 🟢 `vault backup` cron hoạt động trơn tru (14 commit trong 24h, HEAD `f2e38640`).

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1167 | 634 | 224 | 34 | 275 |

---

## Issue 1: sub_tags contains Pool A tag

**File:** wiki/concepts/socratic-prompting.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `sub_tags` chứa "productivity" — tag này thuộc Pool A (Main-tags), `sub_tags` chỉ chấp nhận tag từ Pool B.
**Current:** `sub_tags: [productivity, tutorial]`
**Expected:** `sub_tags` chỉ chứa tag từ `TAGS.md` Pool B.
**Suggested fix:** Loại bỏ `productivity` giữ lại `sub_tags: [tutorial]`, hoặc thay bằng sub-tag hợp lệ từ Pool B (như `automation` hoặc `tools`).

---

## Issue 2: sub_tags contains Pool A tag

**File:** wiki/sources/src_claude-best-practices-power-user-guide.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `sub_tags` chứa "productivity" — tag này thuộc Pool A (Main-tags), `sub_tags` chỉ chấp nhận tag từ Pool B.
**Current:** `sub_tags: [productivity, tools, tutorial]`
**Expected:** `sub_tags` chỉ chứa tag từ `TAGS.md` Pool B.
**Suggested fix:** Loại bỏ `productivity` thành `sub_tags: [tools, tutorial]`, hoặc thay bằng sub-tag hợp lệ khác từ Pool B.

---

## Delta so với 11-04

| Trục | 11-04 | 11-05 | Δ |
|---|---:|---:|---:|
| Files checked | 1167 | 1167 | **0** |
| — concepts | 634 | 634 | 0 |
| — sources | 224 | 224 | 0 |
| — topics | 275 | 275 | 0 |
| — indexes | 34 | 34 | 0 |
| Total issues | 396 | 396 | **0** |
| ERRORs | 2 | 2 | 0 |
| WARNINGS | 394 | 394 | 0 |
| Individual broken | 375 | 375 | 0 |
| Forward-ref groups | 19 | 19 | 0 |
| Unique broken targets | 267 | 267 | **0** |
| New wiki content files | 0 | **0** | 0 |
| Updated wiki content files | 0 | **0** | 0 |
| Raw ingested (unprocessed) | 0 | **0** | 0 |
| Index Agent regenerate | 300 | **300** | 0 |

---

| Lớp | Kiểm tra | Kết quả |
|---|---|---|
| Committed additions | `git log --since="2026-11-04 23:16" --diff-filter=A -- wiki/{concepts,sources,tag,topic}` | **0** file wiki mới |
| Committed modifications | `git log --since="2026-11-04 23:16" --diff-filter=M -- wiki/concepts` | **0** file concept cập nhật |
| Deleted | `--diff-filter=D -- wiki/` | **0** |
| Modified (git status) | `git status --porcelain` | Sạch (chỉ có `.hermes/skills/.usage.json`) |
| Untracked | `git status --porcelain \| grep '^??'` | **0** file trong wiki/ và raw/ |
| Compile activity | Kara compile lúc 08:00 | 0 file biên soạn hôm nay (Output Validator 23:05 chạy silent) |
| Index rebuild | `find wiki/topic wiki/tag -type f -newermt "2026-11-05 00:00"` | **300** (275 topic + 25 tag) — mtime đồng loạt **21:03** hôm nay (commit `53ac8bc4`) |
| Raw layer | `grep -rn 'status: unprocessed' raw/` | **0** file — backlog raw sạch hoàn toàn |
| Backup state | `git log -1 --oneline` | `f2e38640` (23:03:49) — backup cron chạy đều đặn liên tục (14 commit trong 24h) |

---

## Forward-Reference Groups (19)

| File | Broken refs |
|---|---:|
| `wiki/concepts/third-order-thinking.md` | 6 |
| `wiki/concepts/thought-experiment.md` | 6 |
| `wiki/sources/src_11-minutes-hack-github.md` | 4 |
| `wiki/sources/src_ai-future-skills.md` | 4 |
| `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` | 4 |
| `wiki/sources/src_farnam-street-mental-models-biology-series.md` | 6 |
| `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` | 6 |
| `wiki/sources/src_feedback-loops-mental-model.md` | 4 |
| `wiki/sources/src_fs-blog-mental-models.md` | 7 |
| `wiki/sources/src_global-macro-investing.md` | 4 |
| `wiki/sources/src_hermes-polymarket-btc-trading-agent.md` | 4 |
| `wiki/sources/src_incentives-hidden-forces.md` | 6 |
| `wiki/sources/src_mental-models-of-art.md` | 9 |
| `wiki/sources/src_mental-models-of-economics.md` | 9 |
| `wiki/sources/src_probabilistic-thinking.md` | 6 |
| `wiki/sources/src_the-cost-of-discretion.md` | 4 |
| `wiki/sources/src_the-seed-and-the-machine.md` | 4 |
| `wiki/sources/src_thought-experiment.md` | 9 |
| `wiki/sources/src_tribute-system-new-world-order.md` | 4 |

Danh sách **không đổi** so với 11-04, 11-03, 11-02, 11-01, 10-31, 10-30, 10-29, 10-28, 10-27, 10-26, 10-25, 10-24, 10-23, 10-22, 10-21, 10-20, 10-19, 10-18, 10-17, 10-16, 10-15, 10-14, 10-13, 10-12, 10-11, 10-10, 10-04 — cùng 19 file, tổng **106 ref** (không đổi).

---

## Top 20 Broken Targets

| Target | Count |
|---|---:|
| `[[game-theory]]` | 10 |
| `[[confirmation-bias]]` | 8 |
| `[[deep-work]]` | 5 |
| `[[ai-coding-agents]]` | 5 |
| `[[career-design]]` | 5 |
| `[[decision-making]]` | 5 |
| `[[attention-economy]]` | 3 |
| `[[ai-hype-vs-reality]]` | 3 |
| `[[economic-inequality]]` | 3 |
| `[[intellectual-humility]]` | 3 |
| `[[network-effects]]` | 3 |
| `[[goal-setting]]` | 3 |
| `[[naval-ravikant]]` | 3 |
| `[[risk-parity]]` | 3 |
| `[[second-law-of-thermodynamics]]` | 3 |
| `[[homeostasis]]` | 3 |
| `[[saying-no]]` | 3 |
| `[[cognitive-dissonance]]` | 3 |
| `[[power-imbalance]]` | 3 |
| `[[stoicism]]` | 3 |

Danh sách **không đổi** so với 11-04, 11-03, 11-02, 11-01, 10-31, 10-30, 10-29, 10-28, 10-27, 10-26, 10-25, 10-24, 10-23, 10-22, 10-21, 10-20, 10-19, 10-18, 10-17, 10-16, 10-15, 10-14, 10-13, 10-12, 10-11, 10-10, 10-04 (plateau 267 unique targets, ngày thứ 28 liên tiếp).

---

## Escalations

- **2 ERROR phân loại tag Pool A trong `sub_tags` (carry-over 11-02):** Julius đã duyệt báo cáo 11-02 ngày 11-03. Cần Fix Agent / Kara cập nhật frontmatter loại bỏ `productivity` khỏi `sub_tags` hoặc thay thế bằng sub-tag hợp lệ thuộc Pool B (`TAGS.md`) tại:
  1. `wiki/concepts/socratic-prompting.md`
  2. `wiki/sources/src_claude-best-practices-power-user-guide.md`
- **Standing note (plateau 267 targets):** Backlog forward-reference giữ nguyên ngày thứ 28 tại 267 unique targets (394 WARNING).

---

## Verification

- [x] Chạy `validate.py` trên 1167 file toàn KB: 2 ERROR, 394 WARNING, 0 INFO.
- [x] Phân tích bằng `parse_issues.py`: 375 broken cá nhân, 19 groups, 267 unique targets.
- [x] Xác minh đối chiếu git log và mtime: 0 file wiki mới/cập nhật trong 24h qua.
- [x] Kiểm tra tầng raw: 0 unprocessed file (backlog sạch 100%).
- [x] Kiểm tra trailing newline: toàn bộ file đều có trailing newline hợp lệ (49 baseline kế thừa).
- [x] Kiểm tra cross-file integrity qua `verify_integrity.py` và `ad-hoc-verify.py`.
