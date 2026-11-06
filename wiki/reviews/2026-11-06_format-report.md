# Format Validation — 2026-11-06

**Status:** pending
**Issues found:** 396
**Created:** 2026-11-06 23:16:00
**Validator:** format-validator
**Files checked:** 1167 (634 concepts + 224 sources + 34 indexes + 275 topics)
**ERRORs**: 2
**WARNINGS**: 394
**INFOS:** 0
**Total issues**: 396
Files checked: 1167
Total issues: 396

Δ from 2026-11-05 23:16:00 run (pending — prior run): **0 net change, biến thể exact-zero-flat no-compilation-happened (chu kỳ 24h, 11-05 → 11-06).** 1167→1167 files (**+0**), tổng issues giữ nguyên 396 (**0 net change: 2E+394W+0I**). 2 ERROR phân loại tag Pool A trong `sub_tags` tại 2 file biên soạn ngày 11-02 (`socratic-prompting.md`, `src_claude-best-practices-power-user-guide.md`) tiếp tục tồn tại (chờ Fix Agent xử lý sau khi Julius đã duyệt batch 11-02 ngày 11-03). WARNING giữ nguyên ở mức 394 (**375 cá nhân + 19 forward-reference groups = 394**). Unique targets **267 flat** (ngày thứ 29 liên tiếp tại 267: 10-04, 10-10 → 11-06). Top-20 targets giữ nguyên toàn bộ slug và count (hạng 19-20 đồng hạng 3 ref). **Tầng wiki:** 0 file mới được biên soạn trong 24h qua (Kara nghỉ, Output Validator 23:00 chạy silent). **Tầng raw:** 1 unprocessed backlog (`raw/articles/2026-11-04_cognitive-offloading-learning-ai.md`, ingest 11-06 16:10). **Tầng index:** Index Agent rebuild lúc 21:01 hôm nay (commit `847d9b2e`, tag + topic regenerate). **Git & backup:** 🟢 `vault backup` cron hoạt động trơn tru (13 commit trong 24h, HEAD `bef7d22a`).

---

## Issue 1: sub_tags chứa tag Pool A (ERROR — carry-over từ 11-02)

**File:** wiki/concepts/socratic-prompting.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `sub_tags` chứa `productivity` — tag này thuộc Pool A (main_tag pool), không thuộc Pool B (sub_tags pool)
**Current:** `sub_tags: [productivity, ...]`
**Expected:** `sub_tags` chỉ chứa tag từ Pool B; `productivity` chỉ hợp lệ ở `main_tag`
**Suggested fix:** Fix Agent thay `productivity` bằng sub-tag Pool B tương đương (xem TAGS.md), hoặc đổi `main_tag` nếu `productivity` là main tag đúng. Đã được Julius duyệt trong batch 11-02 (approved 11-03), chờ Fix Agent xử lý.

---

## Issue 2: sub_tags chứa tag Pool A (ERROR — carry-over từ 11-02)

**File:** wiki/sources/src_claude-best-practices-power-user-guide.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `sub_tags` chứa `productivity` — tag này thuộc Pool A, không thuộc Pool B
**Current:** `sub_tags` chứa `productivity`
**Expected:** `sub_tags` chỉ chứa tag từ Pool B
**Suggested fix:** Tương tự Issue 1. Cùng batch 11-02, cùng chờ Fix Agent.

---

## Issues 3–396: Broken wikilinks — 394 WARNING (375 cá nhân + 19 nhóm forward-reference)

394 WARNING toàn bộ là broken wikilinks — không có WARNING loại khác. Phân tích bằng `parse_issues.py`:

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1167 | 634 | 224 | 34 | 275 |

| Category | Count |
|---|---:|
| Individual broken wikilinks | 375 |
| Forward-reference groups | 19 |
| Unique broken targets | 267 |

| Metric | 11-05 | 11-06 | Δ |
|---|---|---|---:|
| Total issues | 396 | 396 | **0** |
| ERROR | 2 | 2 | **0** |
| WARNING | 394 | 394 | **0** |
| Individual broken | 375 | 375 | **0** |
| Forward-ref groups | 19 | 19 | **0** |
| Unique broken targets | 267 | 267 | **0** |

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

Danh sách **không đổi** so với 11-05, 11-04, 11-03, 11-02, 11-01, 10-31, 10-30, 10-29, 10-28, 10-27, 10-26, 10-25, 10-24, 10-23, 10-22, 10-21, 10-20, 10-19, 10-18, 10-17, 10-16, 10-15, 10-14, 10-13, 10-12, 10-11, 10-10, 10-04 (plateau 267 unique targets, ngày thứ 29 liên tiếp).

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

Danh sách file và số ref **giống hệt** run 11-05 — không group nào resolve, không group nào mới.

---

## Escalations

- **Standing note (plateau 267 targets):** Backlog forward-reference giữ nguyên ngày thứ 29 tại 267 unique targets (394 WARNING). Non-escalation: đây là trạng thái steady đã xác lập, không phải tín hiệu mới.
- **2 ERROR chờ Fix Agent:** Đã được Julius duyệt trong batch 11-02 (approved 11-03). Đây là ngày thứ 4 2 ERROR này tồn tại sau duyệt. Không escalate thêm — Fix Agent sẽ xử lý theo hàng đợi.
- **Raw backlog mới:** 1 file `raw/articles/2026-11-04_cognitive-offloading-learning-ai.md` (`status: unprocessed`, ingest 11-06 16:10) — cơ hội drain đầu tiên sau 4 ngày raw tĩnh. Non-escalation: đây là hoạt động bình thường của Ingest Agent.

---

## Verification

- [x] Chạy `validate.py` từ KB root: 1167 files, 396 issues (2E+394W+0I).
- [x] Phân tích bằng `parse_issues.py`: 375 broken cá nhân, 19 groups, 267 unique targets.
- [x] Delta baseline: report 11-05 (pending — prior run), không có Fix Agent action kể từ đó (`git log --diff-filter=A` rỗng, `git status` chỉ có `.hermes/skills/.usage.json` M).
- [x] 0 file wiki mới trong 24h (`git log --diff-filter=A -- wiki/concepts wiki/sources wiki/tag wiki/topic` rỗng, `git status --porcelain` 0 untracked wiki file).
- [x] 1 raw file unprocessed mới: `raw/articles/2026-11-04_cognitive-offloading-learning-ai.md` (mtime 11-06 16:10).
- [x] Top-20 broken targets khớp toàn bộ slug + count với report 11-05.
- [x] 19 forward-reference groups khớp toàn bộ file + ref count với report 11-05.
- [x] Vault backup cron hoạt động: 13 commit trong 24h, HEAD `bef7d22a` (23:02 hôm nay).
- [x] Index Agent regenerate tag/topic lúc 21:01 (commit `847d9b2e`) — regenerate, không tạo file mới.
