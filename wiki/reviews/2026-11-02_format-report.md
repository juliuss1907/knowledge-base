# Format Validation — 2026-11-02

**Status:** pending
**Issues found:** 396
**Created:** 2026-11-02 23:16:00 +0700
**Validator:** format-validator
**Files checked:** 1167 (634 concepts + 224 sources + 34 indexes + 275 topics)
**ERRORs**: 2
**WARNINGS**: 394
**INFOS:** 0
**Total issues**: 396
Files checked: 1167
Total issues: 396

Δ from 2026-11-01 23:16:00 run (pending — prior run): **+2 net change, biến thể warning-category / clean-streak break (chu kỳ 24h, 11-01 → 11-02).** 1163→1167 files (**+4: +2 concepts, +1 source, +1 topic**), tổng issues tăng từ 394 lên 396 (**+2 net: 2E+394W+0I**). **Chuỗi sạch 0-ERROR kết thúc ở 18 ngày liên tiếp** (10-15 → 11-01) do phát sinh 2 ERROR phân loại tag Pool A trong `sub_tags` ở 2 file mới biên soạn. WARNING giữ nguyên ở mức 394 (**375 cá nhân + 19 forward-reference groups = 394**; 4 file mới đóng góp 0 broken wikilink). Unique targets **267 flat** (ngày thứ 25 liên tiếp tại 267: 10-04, 10-10 → 11-02). Top-20 targets giữ nguyên toàn bộ slug và count (hạng 19-20 đồng hạng 3 ref). **Tầng wiki:** 5 file mới/cập nhật do Kara biên soạn lúc 08:05 (1 source mới, 2 concept mới, 2 concept cập nhật; Output Validator 23:05 ghi nhận 4 PROMOTE + 1 REVISE). **Tầng raw:** 0 unprocessed backlog (`raw/articles/2026-04-11_claude-best-practices-power-user-guide.md` đã được biên soạn xong lúc 08:05). **Tầng index hoạt động:** Index rebuild lúc 21:02–21:06 hôm nay (commit `cf879aa6`, 300 file: 25 tag + 275 topic, thêm 1 topic mới `claude-power-user-system.md`). **Git & backup:** 🟢 `vault backup` cron hoạt động trơn tru (15 commit trong 24h, HEAD `3227c0c6`).

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

## Delta so với 11-01

| Trục | 11-01 | 11-02 | Δ |
|---|---:|---:|---:|
| Files checked | 1163 | 1167 | **+4** |
| — concepts | 632 | 634 | +2 |
| — sources | 223 | 224 | +1 |
| — topics | 274 | 275 | +1 |
| — indexes | 34 | 34 | 0 |
| Total issues | 394 | 396 | **+2** |
| ERRORs | 0 | 2 | **+2** |
| WARNINGS | 394 | 394 | 0 |
| Individual broken | 375 | 375 | 0 |
| Forward-ref groups | 19 | 19 | 0 |
| Unique broken targets | 267 | 267 | **0** |
| New wiki content files | 0 | **3** | +3 |
| Updated wiki content files | 0 | **2** | +2 |
| Raw ingested (unprocessed) | 1 | **0** | -1 |
| Index Agent regenerate | 299 | **300** | +1 |

---

| Lớp | Kiểm tra | Kết quả |
|---|---|---|
| Committed additions | `git log --since="2026-11-01 23:16" --diff-filter=A -- wiki/{concepts,sources,tag,topic}` | **4** file wiki mới (`claude-cowork.md`, `socratic-prompting.md`, `src_claude-best-practices-power-user-guide.md`, `wiki/topic/claude-power-user-system.md`) |
| Committed modifications | `git log --since="2026-11-01 23:16" --diff-filter=M -- wiki/concepts` | **2** file concept cập nhật (`context-engineering.md`, `context-window-management.md`) |
| Deleted | `--diff-filter=D -- wiki/` | **0** |
| Modified (git status) | `git status --porcelain` | Sạch 100% |
| Untracked | `git status --porcelain \| grep '^??'` | **0** file trong wiki/ và raw/ |
| Compile activity | Kara compile lúc 08:05 | 5 files biên soạn từ bài Claude power user (Output Validator 23:05 đánh giá 4 PROMOTE, 1 REVISE) |
| Index rebuild | `find wiki/topic wiki/tag -type f -newermt "2026-11-02 00:00"` | **300** (275 topic + 25 tag) — mtime đồng loạt **21:02–21:06** hôm nay (commit `cf879aa6`) |
| Raw layer | `grep -rn 'status: unprocessed' raw/` | **0** file — backlog raw sạch hoàn toàn |
| Backup state | `git log -1 --oneline` | `3227c0c6` (23:17:22) — backup cron chạy đều đặn liên tục (15 commit trong 24h) |

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

Danh sách **không đổi** so với 11-01, 10-31, 10-30, 10-29, 10-28, 10-27, 10-26, 10-25, 10-24, 10-23, 10-22, 10-21, 10-20, 10-19, 10-18, 10-17, 10-16, 10-15, 10-14, 10-13, 10-12, 10-11, 10-10, 10-04 — cùng 19 file, tổng **106 ref** (không đổi).

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

Danh sách **không đổi** so với 11-01, 10-31, 10-30, 10-29, 10-28, 10-27, 10-26, 10-25, 10-24, 10-23, 10-22, 10-21, 10-20, 10-19, 10-18, 10-17, 10-16, 10-15, 10-14, 10-13, 10-12, 10-11, 10-10, 10-04 (plateau 267 unique targets, ngày thứ 25 liên tiếp).

---

## Escalations

- **Clean streak 0-ERROR kết thúc ở 18 ngày liên tiếp (10-15 → 11-01):** Phát sinh 2 ERROR phân loại tag do Kara sử dụng tag Pool A (`productivity`) trong trường `sub_tags` tại:
  1. `wiki/concepts/socratic-prompting.md`
  2. `wiki/sources/src_claude-best-practices-power-user-guide.md`
  Cần Fix Agent / Kara cập nhật frontmatter loại bỏ `productivity` khỏi `sub_tags` hoặc thay thế bằng sub-tag hợp lệ thuộc Pool B (`TAGS.md`).
- **Standing note (plateau 267 targets):** Backlog forward-reference giữ nguyên ngày thứ 25 tại 267 unique targets (394 WARNING). Toàn bộ 4 file mới hôm nay đều giải quyết chính xác 100% wikilinks và không tạo thêm forward-reference mới nào.

---

## Verification

- [x] Chạy `validate.py` trên 1167 file toàn KB: 2 ERROR, 394 WARNING, 0 INFO.
- [x] Phân tích bằng `parse_issues.py`: 375 broken cá nhân, 19 groups, 267 unique targets.
- [x] Xác minh đối chiếu git log và mtime: 4 file wiki mới được thêm trong 24h qua (`claude-cowork.md`, `socratic-prompting.md`, `src_claude-best-practices-power-user-guide.md`, `wiki/topic/claude-power-user-system.md`) và 2 concept cập nhật (`context-engineering.md`, `context-window-management.md`).
- [x] Kiểm tra tầng raw: 0 unprocessed file (bài Claude power user đã được biên soạn xong).
- [x] Kiểm tra trailing newline: 6 file mới/cập nhật đều có trailing newline hợp lệ.
- [x] Kiểm tra cross-file integrity qua `verify_integrity.py` và `ad-hoc-verify.py`.
